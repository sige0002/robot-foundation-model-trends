"""Adversarial offline tests: identity, schema, deterministic output, and downloads."""
import csv
import io
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from scripts import build_markdown, download_papers, validate_csv
from scripts.db import (CATEGORIES, OPTIONAL_COLUMNS, REQUIRED_COLUMNS, ROOT,
                        candidate_matches, canonical_arxiv, canonical_doi,
                        normalize_title, read_csv, title_match, valid_url)

HEADINGS = REQUIRED_COLUMNS + OPTIONAL_COLUMNS


def record(**overrides):
    row = {field: "" for field in HEADINGS}
    row.update(id="WAM-0001", title="Learning World Dynamics for Robot Planning",
               published="2024-01-02", authors="Alice Example|Bob Example",
               main_category="wam", subcategory="dynamics", tags="world-model|robotics",
               paper_url="https://arxiv.org/abs/2401.00001",
               pdf_url="https://arxiv.org/pdf/2401.00001", summary_ja="世界モデルの研究です。",
               key_contribution="Planning conditioned on actions.", open_source="unknown",
               code_status="unknown", weights_status="unknown", license_status="unknown",
               source_checked="2026-10-01", review_status="verified")
    row.update(overrides)
    return row


def write_csv(path, rows, headings=HEADINGS):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headings)
        writer.writeheader()
        writer.writerows(rows)


def errors(rows, headings=HEADINGS, previous=None):
    return [issue for issue in validate_csv.validate(headings, rows, previous) if issue.level == "error"]


class IdentityTests(unittest.TestCase):
    def test_arxiv_versions_and_legacy(self):
        for value in ("https://arxiv.org/abs/2401.00001v2", "https://arxiv.org/pdf/2401.00001v12.pdf",
                      "https://export.arxiv.org/pdf/2401.00001.pdf", "arXiv:2401.00001v1"):
            self.assertEqual(canonical_arxiv(value), "2401.00001")
        self.assertEqual(canonical_arxiv("https://arxiv.org/abs/cs/9901001v2"), "cs/9901001")
        self.assertIsNone(canonical_arxiv("https://evil.example/abs/2401.00001"))

    def test_doi_normalization(self):
        self.assertEqual(canonical_doi("https://doi.org/10.1234%2FABCD"), "10.1234/abcd")
        self.assertEqual(canonical_doi("DOI: 10.1234/AbCd."), "10.1234/abcd")
        self.assertEqual(canonical_doi("https://dx.doi.org/10.1234/AbCd?source=a"), "10.1234/abcd")
        self.assertIsNone(canonical_doi("https://evil.example/10.1234/abcd"))

    def test_arxiv_issued_doi_is_same_identity(self):
        first = record()
        second = record(id="WAM-0002", title="A Completely Retitled Revision",
                        paper_url="https://doi.org/10.48550/arXiv.2401.00001", pdf_url="")
        self.assertTrue(any("duplicate canonical arxiv" in str(issue) for issue in errors([first, second])))
        self.assertTrue(any("stable ID changed" in str(issue) for issue in errors([second], previous=[first])))
        self.assertIn("canonical identifier", candidate_matches({"paper_url": second["paper_url"]}, [first])[0]["reason"])

    def test_unicode_greek_pi_and_punctuation(self):
        self.assertEqual(normalize_title("π₀: A Vision–Language–Action Model"),
                         normalize_title("PI_0 — A Vision-Language-Action Model"))
        self.assertEqual(normalize_title("ＡＢＣ, Robot\u00a0Learning!"), "abc robot learning")
        self.assertEqual(title_match("π0: A Flow Model", "pi_0 A Flow Model")[0], "normalized title")

    def test_duplicate_arxiv_is_error_even_when_title_changes(self):
        first = record(pdf_url="https://arxiv.org/pdf/2401.00001v1.pdf")
        second = record(id="WAM-0002", title="Completely Retitled New Revision",
                        paper_url="https://arxiv.org/abs/2401.00001v3")
        self.assertTrue(any("duplicate canonical arxiv" in str(issue) for issue in errors([first, second])))

    def test_duplicate_doi_is_error(self):
        first = record(paper_url="https://doi.org/10.1234/ABC", pdf_url="")
        second = record(id="WAM-0002", title="A Different Title", paper_url="https://dx.doi.org/10.1234/abc", pdf_url="")
        self.assertTrue(any("duplicate canonical doi" in str(issue) for issue in errors([first, second])))

    def test_title_candidates_never_automatically_error(self):
        first = record(title="π0: A Vision-Language-Action Flow Model")
        second = record(id="VLA-0101", title="pi_0 A Vision Language Action Flow Model",
                        paper_url="https://arxiv.org/abs/2401.00002", pdf_url="")
        issues = validate_csv.validate(HEADINGS, [first, second])
        self.assertFalse([issue for issue in issues if issue.level == "error"])
        self.assertTrue(any("normalized title" in str(issue) for issue in issues))

    def test_subtitle_and_fuzzy_candidates(self):
        self.assertEqual(title_match("Learning World Dynamics for Robot Planning",
                                    "Learning World Dynamics for Robot Planning: An Open Framework")[0], "subtitle/prefix variant")
        self.assertEqual(title_match("Learning World Dynamics for Robot Planning",
                                    "Learning World Dynamics for Robotic Planning")[0], "fuzzy title")

    def test_related_generic_titles_are_not_duplicates(self):
        for a, b in (("RT-1", "RT-2"), ("Robot Learning", "Robot Planning"),
                     ("Planning with World Models for Robots", "Learning with Language Models for Robots"),
                     ("π0: Robot Control", "π0.5: Robot Control")):
            self.assertIsNone(title_match(a, b)[0], (a, b))

    def test_candidate_local_identifier_and_case_insensitive_id(self):
        rows = [record()]
        self.assertEqual(candidate_matches({"id": "wam-0001"}, rows)[0]["reason"], "stable ID")
        self.assertIn("canonical identifier", candidate_matches({"paper_url": "https://arxiv.org/abs/2401.00001v9"}, rows)[0]["reason"])
        self.assertEqual(candidate_matches({"title": "Unrelated document title"}, rows), [])

    def test_previous_stable_id_and_category_move(self):
        previous = [record()]
        moved = record(main_category="hybrid", subcategory="vla-wam")
        self.assertEqual(errors([moved], previous=previous), [])
        self.assertTrue(any("stable ID changed" in str(issue) for issue in errors([record(id="HYBRID-0101")], previous=previous)))


class SchemaTests(unittest.TestCase):
    def test_valid_record_and_required_only(self):
        self.assertEqual(errors([record()]), [])
        minimal = {key: value for key, value in record().items() if key in REQUIRED_COLUMNS}
        self.assertEqual(errors([minimal], REQUIRED_COLUMNS), [])

    def test_invalid_dates_and_order(self):
        for value in ("2024-02-30", "2024-1-2", "not-a-date"):
            self.assertTrue(errors([record(published=value)]))
        self.assertTrue(errors([record(updated="2024-01-01")]))
        self.assertTrue(errors([record(source_checked="2026-13-01")]))
        self.assertEqual(errors([record(published="2024-02-29")]), [])

    def test_unknown_date_requires_review_evidence(self):
        self.assertTrue(errors([record(published="")]))
        self.assertTrue(errors([record(published="", review_status="needs-review")]))
        self.assertEqual(errors([record(published="", review_status="needs-review", evidence_note="Exact first-preprint date is not public.")]), [])

    def test_enums_category_url_and_duplicate_id(self):
        self.assertTrue(errors([record(open_source="yes")]))
        self.assertTrue(errors([record(main_category="vla", subcategory="dynamics")]))
        self.assertTrue(errors([record(paper_url="javascript:alert(1)")]))
        self.assertTrue(errors([record(), record(title="Something Else", paper_url="https://example.org/paper", pdf_url="")]))
        self.assertTrue(errors([record(id="../unsafe")]))

    def test_open_source_license_separate_from_weights(self):
        self.assertEqual(errors([record(open_source="true", code_status="available", weights_status="unavailable",
                                        license_status="open-source", code_url="https://github.com/example/model")]), [])
        self.assertTrue(errors([record(open_source="true", license_status="unknown")]))
        self.assertEqual(errors([record(open_source="unknown", code_status="available", code_url="https://github.com/example/model")]), [])

    def test_csv_multiline_quoted_and_unicode(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.csv"
            original = record(summary_ja='改行を含む概要\n"引用", CSV のカンマ。')
            write_csv(path, [original])
            headings, rows = read_csv(path)
            self.assertEqual(rows, [original])
            self.assertEqual(errors(rows, headings), [])

    def test_bad_header_and_cell_count(self):
        self.assertTrue(errors([record()], list(reversed(HEADINGS))))
        extra = record(); extra[None] = ["too many"]
        self.assertTrue(errors([extra]))
        missing = record(); missing["title"] = None
        self.assertTrue(errors([missing]))

    def test_malformed_url_is_error_not_crash(self):
        for value in ("https://[", "https://[invalid/path", "https://example.org\\bad"):
            self.assertTrue(errors([record(paper_url=value)]))
        self.assertIsNone(canonical_arxiv("https://["))
        self.assertIsNone(canonical_doi("https://["))

    def test_multivalue_separator(self):
        self.assertTrue(errors([record(tags="robotics||vla")]))
        self.assertTrue(errors([record(authors="Alice| Bob")]))
        self.assertEqual(errors([record(tags="supporting-foundation|world-model")]), [])

    def test_url_credentials_and_bad_schemes(self):
        for url in ("https://name:password@example.org/paper", "ftp://example.org/paper",
                    "https://example.org/bad path", "https://[", "http://localhost/paper", "https://example.org\\bad"):
            self.assertFalse(valid_url(url))
        self.assertTrue(valid_url("https://example.org/paper?format=pdf"))


class MarkdownTests(unittest.TestCase):
    def test_all_pages_exist_even_empty_and_deterministic(self):
        template = (ROOT / "docs/README.template.md").read_text(encoding="utf-8")
        rows = [record(), record(id="WAM-0002", title="A Distinct Research Contribution",
                                 paper_url="https://arxiv.org/abs/2401.00002", pdf_url="")]
        first = build_markdown.generated_files(rows, template)
        second = build_markdown.generated_files(list(reversed(rows)), template)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 25)
        for category, subcategories in CATEGORIES.items():
            self.assertIn(f"{category}/README.md", first)
            for subcategory in subcategories:
                self.assertIn(f"{category}/{subcategory}.md", first)
        self.assertIn("まだ登録がありません", first["agent/planning.md"])
        self.assertIn("**2**", first["README.md"])

    def test_last_updated_uses_max_checked_not_wall_clock(self):
        template = "Last updated: {{LAST_UPDATED}}; total {{TOTAL}}"
        rows = [record(source_checked="2025-03-01"),
                record(id="WAM-0002", source_checked="2026-04-05", paper_url="https://example.org/paper", pdf_url="")]
        first = build_markdown.generated_files(rows, template)["README.md"]
        self.assertIn("Last updated: 2026-04-05", first)
        self.assertEqual(first, build_markdown.generated_files(list(reversed(rows)), template)["README.md"])
        self.assertIn("Last updated: unknown / 未確認", build_markdown.generated_files([], template)["README.md"])
        self.assertIn("Last updated: unknown / 未確認", build_markdown.generated_files([record(source_checked="")], template)["README.md"])

    def test_check_detects_stale_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            master = root / "source.csv"; write_csv(master, [record()])
            template = ROOT / "docs/README.template.md"
            self.assertEqual(len(build_markdown.build(master, root, template)), 25)
            self.assertEqual(build_markdown.build(master, root, template, check=True), [])
            (root / "README.md").write_text("stale", encoding="utf-8")
            self.assertEqual(build_markdown.build(master, root, template, check=True), ["README.md"])
            self.assertEqual((root / "README.md").read_text(), "stale")

    def test_unknown_date_sorts_last_and_displays_unknown(self):
        rows = [record(published="", review_status="needs-review", evidence_note="Date unknown"),
                record(id="WAM-0002", title="Known Date", paper_url="https://example.org/known", pdf_url="")]
        page = build_markdown.generated_files(rows, "{{COUNTS}}")["wam/dynamics.md"]
        self.assertLess(page.index("### Known Date"), page.index("### Learning World Dynamics"))
        self.assertIn("Published: unknown", page)

    def test_untrusted_markdown_and_newlines_are_escaped(self):
        block = build_markdown.paper_block(record(title="[bad](https://evil.example) <script>", summary_ja="Line one\nLine two"))
        self.assertIn("\\[bad\\]", block)
        self.assertIn("&lt;script&gt;", block)
        self.assertIn("Line one<br>Line two", block)


class DownloadTests(unittest.TestCase):
    def setUp(self):
        # DNS and HTTP are both mocked: these tests never contact the network.
        dns = patch("scripts.download_papers.socket.getaddrinfo", return_value=[
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443))])
        dns.start()
        self.addCleanup(dns.stop)

    def test_filters_and_safe_paths(self):
        rows = [record(), record(id="VLA-0101", main_category="vla", subcategory="adaptation")]
        self.assertEqual(download_papers.selected_rows(rows, category="vla")[0]["id"], "VLA-0101")
        self.assertEqual(download_papers.selected_rows(rows, ids=["WAM-0001"]), [rows[0]])
        for source in ("../outside", "/tmp/secret", "..", "", "WAM-0001"):
            name = download_papers.safe_filename(source)
            self.assertEqual(Path(name).name, name)
            self.assertNotIn("..", name)
            self.assertTrue(name.endswith(".pdf"))

    def test_schema_valid_filename_collisions_are_separated(self):
        ids = ("Paper", "Paper-", "Paper_", "Paper.", "paper", "PAPER")
        filenames = [download_papers.safe_filename(value) for value in ids]
        self.assertEqual(len(set(name.casefold() for name in filenames)), len(ids))
        self.assertEqual(download_papers.safe_filename("WAM-0001"), "WAM-0001.pdf")
        with tempfile.TemporaryDirectory() as directory:
            paths = []
            for index, stable_id in enumerate(ids):
                payload = f"%PDF-1.4\nPaper {index}\n%%EOF".encode()
                path, fresh = download_papers.download_one(record(id=stable_id), Path(directory),
                                                            opener=lambda *a, data=payload, **k: io.BytesIO(data))
                self.assertTrue(fresh)
                self.assertEqual(path.read_bytes(), payload)
                paths.append(path)
            self.assertEqual(len(set(paths)), len(ids))

    def test_private_literal_credentials_and_scheme_are_rejected(self):
        for url in ("http://127.0.0.1/paper", "http://169.254.169.254/latest/meta-data", "http://10.0.0.1/paper",
                    "http://[::1]/paper", "http://[ff02::1]/paper", "file:///tmp/paper.pdf",
                    "https://name:password@example.org/paper", "https://example.org:0/paper"):
            with self.assertRaises(download_papers.UnsafeEndpointError, msg=url):
                download_papers.validate_public_endpoint(url)
        with tempfile.TemporaryDirectory() as directory:
            with patch("scripts.download_papers.open_public_url") as opener:
                with self.assertRaises(RuntimeError):
                    download_papers.download_one(record(pdf_url="http://127.0.0.1/paper"), Path(directory), opener=opener)
                opener.assert_not_called()

    def test_private_mixed_and_missing_dns_are_rejected(self):
        for addresses in (["127.0.0.1"], ["93.184.216.34", "169.254.169.254"], ["224.0.0.1"], []):
            results = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in addresses]
            with patch("scripts.download_papers.socket.getaddrinfo", return_value=results):
                with self.assertRaises(download_papers.UnsafeEndpointError):
                    download_papers.validate_public_endpoint("https://example.org/paper")
        with patch("scripts.download_papers.socket.getaddrinfo", side_effect=socket.gaierror("unresolved")):
            with self.assertRaises(download_papers.UnsafeEndpointError):
                download_papers.validate_public_endpoint("https://example.org/paper")

    def test_redirect_guard_validates_before_request(self):
        handler = download_papers.PublicRedirectHandler()
        request = download_papers.Request("https://example.org/start")
        for target in ("http://169.254.169.254/latest/meta-data", "http://127.0.0.1/secret",
                       "https://name:password@example.org/paper", "file:///tmp/private"):
            with self.assertRaises(download_papers.UnsafeEndpointError):
                handler.redirect_request(request, None, 302, "Found", {}, target)
        result = handler.redirect_request(request, None, 302, "Found", {}, "https://example.org/public.pdf")
        self.assertEqual(result.full_url, "https://example.org/public.pdf")

    def test_connection_pins_public_ip_and_checks_peer(self):
        connection = download_papers.PublicHTTPConnection("example.org", timeout=7)
        fake = unittest.mock.Mock()
        fake.getpeername.return_value = ("93.184.216.34", 80)
        with patch("scripts.download_papers.socket.create_connection", return_value=fake) as create:
            connection.connect()
            self.assertEqual(create.call_args.args[0], ("93.184.216.34", 80))
            self.assertIs(connection.sock, fake)
        fake.getpeername.return_value = ("127.0.0.1", 80)
        with patch("scripts.download_papers.socket.create_connection", return_value=fake):
            with self.assertRaises(download_papers.UnsafeEndpointError):
                connection.connect()
            fake.close.assert_called()

    def test_https_pinning_preserves_hostname_verification(self):
        connection = download_papers.PublicHTTPSConnection("example.org", timeout=7)
        raw = unittest.mock.Mock(); raw.getpeername.return_value = ("93.184.216.34", 443)
        secure = unittest.mock.Mock()
        context = unittest.mock.Mock(); context.wrap_socket.return_value = secure
        connection._context = context
        with patch("scripts.download_papers.socket.create_connection", return_value=raw) as create:
            connection.connect()
            self.assertEqual(create.call_args.args[0], ("93.184.216.34", 443))
            context.wrap_socket.assert_called_once_with(raw, server_hostname="example.org")
            self.assertIs(connection.sock, secure)

    def test_opener_disables_proxy_and_installs_guarded_handlers(self):
        request = download_papers.Request("https://example.org/public.pdf")
        fake_opener = unittest.mock.Mock()
        with patch("scripts.download_papers.build_opener", return_value=fake_opener) as factory:
            download_papers.open_public_url(request, timeout=8)
            handlers = factory.call_args.args
            self.assertEqual(handlers[0].proxies, {})
            self.assertTrue(any(isinstance(handler, download_papers.PublicRedirectHandler) for handler in handlers))
            self.assertTrue(any(isinstance(handler, download_papers.PublicHTTPSHandler) for handler in handlers))
            fake_opener.open.assert_called_once_with(request, timeout=8)

    def test_valid_pdf_atomic_and_existing_skip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.7\nexample test bytes\n%%EOF"
            path, downloaded = download_papers.download_one(record(), root, opener=lambda *a, **k: io.BytesIO(payload))
            self.assertTrue(downloaded)
            self.assertEqual(path.read_bytes(), payload)
            self.assertEqual(list(root.glob("*.part")), [])
            def unexpected(*args, **kwargs):
                self.fail("existing PDF should not be re-downloaded")
            self.assertFalse(download_papers.download_one(record(), root, opener=unexpected)[1])

    def test_bad_pdf_retries_and_cleans_without_clobber(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "WAM-0001.pdf"; target.write_bytes(b"original non-PDF")
            delays = []
            with self.assertRaises(RuntimeError):
                download_papers.download_one(record(), root, attempts=2, sleeper=delays.append,
                                              opener=lambda *a, **k: io.BytesIO(b"<html>Access denied</html>"))
            self.assertEqual(target.read_bytes(), b"original non-PDF")
            self.assertEqual(list(root.glob("*.part")), [])
            self.assertEqual(delays, [1])

    def test_network_retry_backoff(self):
        with tempfile.TemporaryDirectory() as directory:
            calls, sleeps = [], []
            def opener(request, timeout):
                calls.append(timeout)
                if len(calls) < 3:
                    raise URLError("temporary")
                return io.BytesIO(b"%PDF-1.4\n%%EOF")
            result = download_papers.download_one(record(), Path(directory), opener=opener, sleeper=sleeps.append)
            self.assertTrue(result[1])
            self.assertEqual(sleeps, [1, 2])
            self.assertEqual(calls, [30.0, 30.0, 30.0])

    def test_permanent_http_failure_not_retried(self):
        with tempfile.TemporaryDirectory() as directory:
            def denied(*args, **kwargs):
                raise HTTPError("https://example.org/paper", 403, "Forbidden", {}, None)
            delays = []
            with self.assertRaises(RuntimeError):
                download_papers.download_one(record(), Path(directory), opener=denied, sleeper=delays.append)
            self.assertEqual(delays, [])

    def test_size_limit_truncated_and_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(RuntimeError):
                download_papers.download_one(record(), root, attempts=1, max_bytes=8,
                                              opener=lambda *a, **k: io.BytesIO(b"%PDF-1.4\nToo big"))
            with self.assertRaises(RuntimeError):
                download_papers.download_one(record(), root, attempts=1,
                                              opener=lambda *a, **k: io.BytesIO(b"%PDF-"))
            outside = root / "outside"; outside.write_bytes(b"unchanged")
            (root / "WAM-0001.pdf").symlink_to(outside)
            with self.assertRaises(ValueError):
                download_papers.download_one(record(), root, opener=lambda *a, **k: io.BytesIO(b"%PDF-1.4\n%%EOF"))
            self.assertEqual(outside.read_bytes(), b"unchanged")
            self.assertEqual(list(root.glob("*.part")), [])

    def test_default_list_is_offline(self):
        with tempfile.TemporaryDirectory() as directory:
            master = Path(directory) / "papers.csv"; write_csv(master, [record()])
            with patch("scripts.download_papers.download_one", side_effect=AssertionError("network forbidden")):
                with patch("sys.stdout", new=io.StringIO()):
                    self.assertEqual(download_papers.main(["--csv", str(master)]), 0)

    def test_case_insensitive_category_and_display_subcategory_cli(self):
        self.assertEqual(download_papers.category_key("Agent"), "agent")
        for value, expected in (("Dynamics", "dynamics"), ("World Representation", "world-representation"),
                                ("Reasoning / System 2", "reasoning-system2"), ("VLA + WAM", "vla-wam"),
                                ("ACTION-SYSTEM1", "action-system1")):
            self.assertEqual(download_papers.subcategory_key(value), expected)
        with tempfile.TemporaryDirectory() as directory:
            master = Path(directory) / "papers.csv"; write_csv(master, [record()])
            with patch("sys.stdout", new=io.StringIO()) as output:
                self.assertEqual(download_papers.main(["--csv", str(master), "--category", "WAM", "--subcategory", "Dynamics"]), 0)
                self.assertIn("WAM-0001", output.getvalue())
            with patch("sys.stdout", new=io.StringIO()) as output:
                self.assertEqual(download_papers.main(["--csv", str(master), "--category", "Agent", "--subcategory", "Planning"]), 0)
                self.assertIn("Selected 0 records", output.getvalue())

    def test_bulk_download_requires_explicit_opt_in(self):
        with patch("sys.stderr", new=io.StringIO()):
            with self.assertRaises(SystemExit):
                download_papers.main(["--download"])


if __name__ == "__main__":
    unittest.main()
