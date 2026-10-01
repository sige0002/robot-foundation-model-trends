#!/usr/bin/env python3
"""List/select paper PDFs; download only with explicit --download opt-in."""
from __future__ import annotations

import argparse
import csv
import hashlib
import http.client
import ipaddress
import os
import re
import socket
import sys
import tempfile
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import (HTTPHandler, HTTPRedirectHandler, HTTPSHandler, ProxyHandler,
                            Request, build_opener)

try:
    from .db import CATEGORIES, ROOT, SCHEMA, normalize_title, read_csv
    from .validate_csv import validate
except ImportError:
    from db import CATEGORIES, ROOT, SCHEMA, normalize_title, read_csv
    from validate_csv import validate

USER_AGENT = "robot-foundation-model-trends/1.0 (research PDF downloader; opt-in)"


def category_key(value: str) -> str:
    return value.casefold()


def subcategory_key(value: str) -> str:
    """Accept exact machine keys or schema display names, case-insensitively."""
    normalized = normalize_title(value)
    for category, subcategories in CATEGORIES.items():
        for subcategory in subcategories:
            display = SCHEMA.get("subcategory_display_names", {}).get(subcategory, subcategory)
            if normalized in (normalize_title(subcategory), normalize_title(display)):
                return subcategory
    return value.casefold()


def safe_filename(stable_id: str) -> str:
    # Preserve conventional database IDs; digest every other full ID to avoid
    # punctuation-normalization and case-insensitive-filesystem collisions.
    if len(stable_id) <= 100 and re.fullmatch(r"(?:WAM|VLA|AGENT|HYBRID)-[0-9]{4,}", stable_id):
        return stable_id + ".pdf"
    prefix = re.sub(r"[^a-zA-Z0-9._-]", "_", stable_id).strip("._-")
    prefix = re.sub(r"\.{2,}", "_", prefix)[:64] or "paper"
    digest = hashlib.sha256(stable_id.encode("utf-8")).hexdigest()
    return f"{prefix}-{digest}.pdf"


class UnsafeEndpointError(ValueError):
    """A URL or resolved address is not an allowed public research endpoint."""


def is_public_address(value: str) -> bool:
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        return False
    if not address.is_global or any((address.is_private, address.is_loopback,
                                    address.is_link_local, address.is_reserved,
                                    address.is_multicast, address.is_unspecified)):
        return False
    # Reject transition addresses that can encode a non-public IPv4 target.
    if isinstance(address, ipaddress.IPv6Address):
        embedded = address.ipv4_mapped or address.sixtofour
        if embedded and not is_public_address(str(embedded)):
            return False
        if address.teredo and not all(is_public_address(str(ip)) for ip in address.teredo):
            return False
        if address in ipaddress.ip_network("64:ff9b::/96"):
            return is_public_address(str(ipaddress.IPv4Address(int(address) & 0xffffffff)))
    return True


def resolve_public_addresses(host: str, port: int) -> tuple[str, ...]:
    if "%" in host:
        raise UnsafeEndpointError("scoped or percent-encoded host is not allowed")
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        try:
            answers = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        except OSError as error:
            raise UnsafeEndpointError(f"cannot resolve public endpoint {host!r}: {error}") from error
        addresses = [answer[4][0] for answer in answers if answer[0] in (socket.AF_INET, socket.AF_INET6)]
    else:
        addresses = [str(literal)]
    if not addresses or any(not is_public_address(address) for address in addresses):
        raise UnsafeEndpointError(f"endpoint {host!r} has a non-public or missing IP address")
    return tuple(dict.fromkeys(addresses))


def validate_public_endpoint(url: str) -> tuple[str, int, tuple[str, ...]]:
    if not url or "\\" in url or any(char.isspace() or ord(char) < 32 for char in url):
        raise UnsafeEndpointError("invalid endpoint URL")
    try:
        parsed = urlsplit(url)
        host = parsed.hostname
        port = parsed.port if parsed.port is not None else (443 if parsed.scheme == "https" else 80)
    except ValueError as error:
        raise UnsafeEndpointError("malformed endpoint URL") from error
    if parsed.scheme not in ("http", "https") or not host or parsed.username is not None or parsed.password is not None:
        raise UnsafeEndpointError("only public HTTP(S) URLs without credentials are allowed")
    if not 1 <= port <= 65535:
        raise UnsafeEndpointError("invalid endpoint port")
    return host, port, resolve_public_addresses(host, port)


def _public_socket(connection):
    if connection._tunnel_host:
        raise UnsafeEndpointError("proxy tunnels are disabled")
    addresses = resolve_public_addresses(connection.host, connection.port)
    last_error = None
    for address in addresses:
        try:
            # Pin the connection to the checked literal address. urllib must not
            # resolve the original hostname again after our DNS check.
            sock = socket.create_connection((address, connection.port), connection.timeout,
                                            connection.source_address)
            if not is_public_address(sock.getpeername()[0]):
                sock.close()
                raise UnsafeEndpointError("connected peer is not a public address")
            return sock
        except OSError as error:
            last_error = error
    raise OSError(f"could not connect to public endpoint: {last_error}")


class PublicHTTPConnection(http.client.HTTPConnection):
    def connect(self):
        self.sock = _public_socket(self)


class PublicHTTPSConnection(http.client.HTTPSConnection):
    def connect(self):
        self.sock = _public_socket(self)
        # Keep certificate verification and SNI tied to the original hostname.
        self.sock = self._context.wrap_socket(self.sock, server_hostname=self.host)


class PublicHTTPHandler(HTTPHandler):
    def http_open(self, request):
        validate_public_endpoint(request.full_url)
        return self.do_open(PublicHTTPConnection, request)


class PublicHTTPSHandler(HTTPSHandler):
    def https_open(self, request):
        validate_public_endpoint(request.full_url)
        return self.do_open(PublicHTTPSConnection, request, context=self._context)


class PublicRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        # Validate BEFORE constructing/transmitting every redirected request.
        validate_public_endpoint(new_url)
        return super().redirect_request(request, response, code, message, headers, new_url)


def open_public_url(request, timeout=30):
    validate_public_endpoint(request.full_url)
    # Disable ambient proxy settings; all connections use checked pinned IPs.
    opener = build_opener(ProxyHandler({}), PublicHTTPHandler(), PublicHTTPSHandler(), PublicRedirectHandler())
    return opener.open(request, timeout=timeout)


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(5) == b"%PDF-"
    except OSError:
        return False


def selected_rows(rows: list[dict], category=None, subcategory=None, ids=None) -> list[dict]:
    ids = set(ids or [])
    return [row for row in rows
            if (not category or row["main_category"] == category)
            and (not subcategory or row["subcategory"] == subcategory)
            and (not ids or row["id"] in ids)]


def download_one(row: dict, destination: Path, attempts=3, timeout=30.0,
                 max_bytes=100 * 1024 * 1024, opener=open_public_url, sleeper=time.sleep) -> tuple[Path, bool]:
    if not row.get("pdf_url"):
        raise ValueError(f"{row['id']}: no pdf_url")
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    target = root / safe_filename(row["id"])
    if target.parent != root:
        raise ValueError("unsafe target path")
    # Do not follow pre-existing symlinks to files outside the selected directory.
    if target.is_symlink():
        raise ValueError(f"refusing symlink target: {target.name}")
    if target.exists() and is_pdf(target):
        return target, False
    last_error = None
    for attempt in range(attempts):
        temporary = None
        try:
            validate_public_endpoint(row["pdf_url"])
            request = Request(row["pdf_url"], headers={"User-Agent": USER_AGENT, "Accept": "application/pdf"})
            with opener(request, timeout=timeout) as response:
                with tempfile.NamedTemporaryFile(mode="wb", prefix=".download-", suffix=".part", dir=root, delete=False) as handle:
                    temporary = Path(handle.name)
                    first = response.read(5)
                    if first != b"%PDF-":
                        raise ValueError("response is not a PDF (missing %PDF- magic)")
                    written = len(first)
                    handle.write(first)
                    while True:
                        chunk = response.read(64 * 1024)
                        if not chunk:
                            break
                        written += len(chunk)
                        if written > max_bytes:
                            raise ValueError(f"PDF exceeds {max_bytes} byte limit")
                        handle.write(chunk)
                    if written <= 5:
                        raise ValueError("truncated PDF response")
                    handle.flush()
                    os.fsync(handle.fileno())
            # Atomic replace: failed attempts never clobber an existing file.
            if target.is_symlink():
                raise ValueError("target became a symlink")
            temporary.replace(target)
            temporary = None
            return target, True
        except (OSError, ValueError, URLError, HTTPError) as error:
            last_error = error
            if temporary is not None:
                temporary.unlink(missing_ok=True)
            # No retries for permanent client errors, except transient rate limits.
            permanent = isinstance(error, UnsafeEndpointError) or (isinstance(error, HTTPError) and error.code in (400, 401, 403, 404, 410))
            if permanent or attempt + 1 >= attempts:
                break
            sleeper(min(2 ** attempt, 30))
    raise RuntimeError(f"{row['id']}: download failed after {attempt + 1} attempt(s): {last_error}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=ROOT / "papers.csv")
    parser.add_argument("--category", type=category_key, choices=list(CATEGORIES), help="VLA/WAM/Agent/Hybrid, case-insensitive")
    parser.add_argument("--subcategory", type=subcategory_key, help="canonical slug or schema display label, case-insensitive")
    parser.add_argument("--id", action="append", dest="ids", help="stable ID; repeat to select multiple")
    parser.add_argument("--download", action="store_true", help="perform network requests; default only lists")
    parser.add_argument("--all", action="store_true", help="explicitly authorize all PDFs if no filters were supplied")
    parser.add_argument("--destination", type=Path, default=ROOT / "papers")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--max-mb", type=float, default=100)
    args = parser.parse_args(argv)
    if args.download and not (args.category or args.subcategory or args.ids or args.all):
        parser.error("choose --category/--subcategory/--id, or explicitly pass --all with --download")
    if args.attempts < 1 or args.attempts > 10 or args.timeout <= 0 or args.max_mb <= 0:
        parser.error("attempts must be 1–10; timeout and max-mb must be positive")
    if args.subcategory and args.subcategory not in {sub for values in CATEGORIES.values() for sub in values}:
        parser.error("unknown --subcategory")
    if args.category and args.subcategory and args.subcategory not in CATEGORIES[args.category]:
        parser.error("--subcategory does not belong to --category")
    try:
        headings, rows = read_csv(args.csv)
        errors = [issue for issue in validate(headings, rows) if issue.level == "error"]
        if errors:
            raise ValueError("invalid CSV: " + "; ".join(str(issue) for issue in errors))
        missing = set(args.ids or []) - {row["id"] for row in rows}
        if missing:
            raise ValueError("unknown IDs: " + ", ".join(sorted(missing)))
        selected = selected_rows(rows, args.category, args.subcategory, args.ids)
    except (OSError, csv.Error, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    failures = 0
    for row in selected:
        if not args.download:
            print(f"{row['id']}\t{row.get('pdf_url') or '(no pdf_url)'}")
            continue
        if not row.get("pdf_url"):
            print(f"SKIP {row['id']}: no pdf_url")
            continue
        try:
            path, downloaded = download_one(row, args.destination, args.attempts, args.timeout, int(args.max_mb * 1024 * 1024))
            print(f"{'DOWNLOADED' if downloaded else 'EXISTS'} {row['id']}: {path}")
        except (RuntimeError, ValueError, OSError) as error:
            failures += 1
            print(f"ERROR: {error}", file=sys.stderr)
    print(f"Selected {len(selected)} records; {failures} failures" + ("; list only (no downloads)" if not args.download else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
