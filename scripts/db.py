"""Shared schema, CSV loading, and conservative paper identity matching."""
from __future__ import annotations

import csv
import difflib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema.json").read_text(encoding="utf-8"))
REQUIRED_COLUMNS = SCHEMA["required_columns"]
OPTIONAL_COLUMNS = SCHEMA["optional_columns"]
CATEGORIES = SCHEMA["categories"]
ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}\Z")
ARXIV_PATTERN = re.compile(
    r"(?<![\w.])(?:(\d{4}\.\d{4,5})|([a-z-]+(?:\.[a-z-]+)?/\d{7}))(?:v\d+)?(?:\.pdf)?(?=$|[/?#\s])",
    re.IGNORECASE,
)
GREEK = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "ζ": "zeta", "η": "eta", "θ": "theta", "ι": "iota", "κ": "kappa",
    "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "ο": "omicron",
    "π": "pi", "ρ": "rho", "σ": "sigma", "ς": "sigma", "τ": "tau",
    "υ": "upsilon", "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
}


@dataclass(frozen=True)
class Issue:
    level: str
    row: int
    message: str

    def __str__(self):
        return f"{self.level.upper()} row {self.row}: {self.message}"


def read_csv(path: str | Path):
    """Return headings and rows without dropping multiline/quoted CSV content."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        headings = reader.fieldnames or []
        rows = list(reader)
    return headings, rows


def valid_url(value: str) -> bool:
    if not value or "\\" in value or any(ch.isspace() or ord(ch) < 32 for ch in value):
        return False
    try:
        parsed = urlsplit(value)
        _ = parsed.port
        return bool(parsed.scheme in ("https", "http") and parsed.hostname
                    and "." in parsed.hostname and not parsed.username and not parsed.password)
    except ValueError:
        return False


def canonical_arxiv(value: str) -> str | None:
    """Canonical arXiv ID, independent of /abs vs /pdf and revision suffix."""
    if not value:
        return None
    candidate = value.strip()
    if "://" in candidate:
        try:
            parsed = urlsplit(candidate)
        except ValueError:
            return None
        if (parsed.hostname or "").casefold() not in {
                "arxiv.org", "www.arxiv.org", "export.arxiv.org"}:
            return None
        candidate = unquote(parsed.path).removeprefix("/abs/").removeprefix("/pdf/")
    candidate = candidate.removeprefix("arXiv:").removeprefix("arxiv:")
    match = ARXIV_PATTERN.fullmatch(candidate)
    if not match:
        return None
    return (match.group(1) or match.group(2)).casefold()


def canonical_doi(value: str) -> str | None:
    if not value:
        return None
    candidate = unicodedata.normalize("NFKC", value.strip())
    if "://" in candidate:
        try:
            parsed = urlsplit(candidate)
        except ValueError:
            return None
        if (parsed.hostname or "").casefold() not in {"doi.org", "dx.doi.org", "www.doi.org"}:
            return None
        candidate = unquote(parsed.path).lstrip("/")
    candidate = re.sub(r"^doi:\s*", "", candidate, flags=re.IGNORECASE)
    candidate = candidate.rstrip(".,;")
    if re.fullmatch(r"10\.\d{4,9}/\S+", candidate, re.IGNORECASE):
        return candidate.casefold()
    return None


def identifiers(row: dict) -> set[str]:
    result = set()
    for field in ("paper_url", "pdf_url"):
        value = row.get(field) or ""
        arxiv = canonical_arxiv(value)
        doi = canonical_doi(value)
        if arxiv:
            result.add("arxiv:" + arxiv)
        if doi:
            result.add("doi:" + doi)
            if doi.startswith("10.48550/arxiv."):
                issued_arxiv = canonical_arxiv(doi.removeprefix("10.48550/arxiv."))
                if issued_arxiv:
                    result.add("arxiv:" + issued_arxiv)
    return result


def normalize_title(title: str) -> str:
    """NFKC/casefold/punctuation/Greek normalization; not semantic equivalence."""
    value = unicodedata.normalize("NFKC", title).casefold()
    # Keep π0 and pi_0 comparable, also joining alphabetic model names with digits.
    value = "".join(GREEK.get(char, char) for char in value)
    value = "".join(char if char.isalnum() else " " for char in value)
    value = re.sub(r"(?<=[a-z])\s+(?=\d)|(?<=\d)\s+(?=[a-z])", "", value)
    return " ".join(value.split())


def title_match(a: str, b: str) -> tuple[str | None, float]:
    """Suggest possible duplicates conservatively; never delete or merge."""
    na, nb = normalize_title(a), normalize_title(b)
    if na and na == nb:
        return "normalized title", 1.0
    if not na or not nb:
        return None, 0.0
    ta, tb = set(na.split()), set(nb.split())
    ratio = difflib.SequenceMatcher(None, na, nb, autojunk=False).ratio()
    overlap = len(ta & tb) / len(ta | tb)
    # A complete title may be a prefix of its longer subtitle variant.
    shorter, longer = sorted((na, nb), key=len)
    subtitle = longer.startswith(shorter + " ") and len(shorter.split()) >= 4
    # Generic short names are poor duplicate evidence. Avoid broad 2-token matches.
    if subtitle or (min(len(ta), len(tb)) >= 4 and ratio >= .86 and overlap >= .6):
        return ("subtitle/prefix variant" if subtitle else "fuzzy title"), ratio
    return None, ratio


def candidate_matches(candidate: dict, rows: list[dict]) -> list[dict]:
    matches = []
    candidate_ids = identifiers(candidate)
    for row in rows:
        common = candidate_ids & identifiers(row)
        reason, score = title_match(candidate.get("title", ""), row.get("title", ""))
        if candidate.get("id") and str(candidate.get("id")).casefold() == str(row.get("id")).casefold():
            reason, score = "stable ID", 1.0
        elif common:
            reason, score = "canonical identifier: " + ", ".join(sorted(common)), 1.0
        if reason:
            matches.append({"id": row.get("id", ""), "title": row.get("title", ""),
                            "reason": reason, "score": round(score, 3)})
    return sorted(matches, key=lambda item: (-item["score"], item["id"]))


def split_values(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]
