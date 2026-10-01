#!/usr/bin/env python3
"""Validate the CSV master and identify reviewable duplicate candidates, offline."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    from .db import (CATEGORIES, ID_PATTERN, OPTIONAL_COLUMNS, REQUIRED_COLUMNS, ROOT,
                     SCHEMA, Issue, candidate_matches, identifiers, normalize_title,
                     read_csv, title_match, valid_url)
except ImportError:
    from db import (CATEGORIES, ID_PATTERN, OPTIONAL_COLUMNS, REQUIRED_COLUMNS, ROOT,
                    SCHEMA, Issue, candidate_matches, identifiers, normalize_title,
                    read_csv, title_match, valid_url)


def iso_date(value: str) -> dt.date | None:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value or ""):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def validate(headings: list[str], rows: list[dict], previous: list[dict] | None = None) -> list[Issue]:
    issues = []
    if headings[:len(REQUIRED_COLUMNS)] != REQUIRED_COLUMNS:
        issues.append(Issue("error", 1, "required columns must appear in schema order: " + ",".join(REQUIRED_COLUMNS)))
    if len(headings) != len(set(headings)):
        issues.append(Issue("error", 1, "duplicate column headings"))
    for heading in headings:
        if heading not in REQUIRED_COLUMNS + OPTIONAL_COLUMNS:
            issues.append(Issue("error", 1, f"unknown column {heading!r}"))
    seen_ids, seen_identifiers, seen_titles = {}, {}, {}
    for number, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            issues.append(Issue("error", number, "row has too many or too few cells"))
        for field in ("id", "title", "authors", "main_category", "subcategory", "paper_url", "summary_ja", "key_contribution", "open_source"):
            if not (row.get(field) or "").strip():
                issues.append(Issue("error", number, f"{field} must not be empty"))
        for field, value in row.items():
            if field is not None and value is not None and value != value.strip():
                issues.append(Issue("error", number, f"{field} has leading/trailing whitespace"))
        stable_id = row.get("id") or ""
        if not ID_PATTERN.fullmatch(stable_id) or ".." in stable_id:
            issues.append(Issue("error", number, "id must be a stable ASCII identifier (1–100 chars; no '..')"))
        if stable_id in seen_ids:
            issues.append(Issue("error", number, f"duplicate id {stable_id!r}, first row {seen_ids[stable_id]}"))
        seen_ids[stable_id] = number
        published = iso_date(row.get("published") or "")
        if not published:
            unknown_reviewed = (not row.get("published") and row.get("review_status") == "needs-review" and bool(row.get("evidence_note")))
            if not unknown_reviewed:
                issues.append(Issue("error", number, "published must be a valid ISO first-preprint date; unknown date needs blank published, needs-review, and evidence_note"))
        for field in ("updated", "source_checked"):
            value = row.get(field) or ""
            parsed = iso_date(value)
            if value and not parsed:
                issues.append(Issue("error", number, f"{field} must be empty or a valid ISO date"))
            if field == "updated" and published and parsed and parsed < published:
                issues.append(Issue("error", number, "updated cannot precede published"))
        category = row.get("main_category") or ""
        if category not in CATEGORIES:
            issues.append(Issue("error", number, f"invalid main_category {category!r}"))
        elif row.get("subcategory") not in CATEGORIES[category]:
            issues.append(Issue("error", number, f"invalid subcategory for {category}: {row.get('subcategory')!r}"))
        for field in ("paper_url", "pdf_url", "code_url", "project_url"):
            value = row.get(field) or ""
            if value and not valid_url(value):
                issues.append(Issue("error", number, f"{field} must be an absolute http(s) URL without credentials or spaces"))
        for field, allowed in SCHEMA["enums"].items():
            value = row.get(field) or ""
            if field in headings and (value or field == "open_source") and value not in allowed:
                issues.append(Issue("error", number, f"invalid {field} {value!r}; expected one of {', '.join(allowed)}"))
        for field in ("authors", "tags"):
            value = row.get(field) or ""
            if value and any(not part.strip() or part != part.strip() for part in value.split("|")):
                issues.append(Issue("error", number, f"{field} uses '|' separators without empty values or extra padding"))
        if row.get("open_source") == "true":
            if row.get("license_status") and row["license_status"] != "open-source":
                issues.append(Issue("error", number, "open_source=true requires license_status=open-source when provided"))
            if row.get("code_status") == "unavailable":
                issues.append(Issue("error", number, "open_source=true conflicts with code_status=unavailable"))
            if not row.get("code_url"):
                issues.append(Issue("warning", number, "open_source=true has no code_url; retain public license/code evidence"))
        if row.get("code_status") == "available" and not row.get("code_url"):
            issues.append(Issue("error", number, "code_status=available requires code_url"))
        if row.get("review_status") == "verified" and not row.get("source_checked"):
            issues.append(Issue("error", number, "review_status=verified requires source_checked"))
        own_identifiers = identifiers(row)
        arxiv_ids = {item for item in own_identifiers if item.startswith("arxiv:")}
        if len(arxiv_ids) > 1:
            issues.append(Issue("error", number, "paper_url and pdf_url identify different arXiv papers"))
        for identifier in sorted(own_identifiers):
            if identifier in seen_identifiers:
                issues.append(Issue("error", number, f"duplicate canonical {identifier}, first row {seen_identifiers[identifier]}; arXiv revisions are one record"))
            seen_identifiers[identifier] = number
        title = normalize_title(row.get("title") or "")
        if title and title in seen_titles:
            issues.append(Issue("warning", number, f"same normalized title as row {seen_titles[title]}; inspect identity, do not auto-merge"))
        seen_titles[title] = number
    # Pairwise titles are local metadata only, never paper/PDF fetching.
    for i, row in enumerate(rows):
        for j in range(i):
            prior = rows[j]
            reason, score = title_match(row.get("title") or "", prior.get("title") or "")
            if reason and reason != "normalized title" and not identifiers(row) & identifiers(prior):
                issues.append(Issue("warning", i + 2, f"{reason} candidate vs row {j + 2} ({score:.3f}); human review required"))
    if previous:
        for number, row in enumerate(rows, 2):
            for old in previous:
                same_identity = bool(identifiers(row) & identifiers(old))
                if same_identity and row.get("id") != old.get("id"):
                    issues.append(Issue("error", number, f"stable ID changed from {old.get('id')!r}; preserve it across version/category changes"))
    return issues


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default=str(ROOT / "papers.csv"))
    parser.add_argument("--previous", help="previous CSV to enforce stable IDs for canonical identities")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--title", help="check one title against the local CSV without fetching papers")
    group.add_argument("--candidate", type=Path, help="small JSON object/list or CSV of candidate metadata to match offline")
    parser.add_argument("--strict-warnings", action="store_true", help="also fail on human-review candidate warnings")
    args = parser.parse_args(argv)
    try:
        headings, rows = read_csv(args.csv)
        if args.title or args.candidate:
            if args.title:
                candidates = [{"title": args.title}]
            elif args.candidate.suffix.casefold() == ".csv":
                _, candidates = read_csv(args.candidate)
            else:
                data = json.loads(args.candidate.read_text(encoding="utf-8"))
                candidates = data if isinstance(data, list) else [data]
            if not all(isinstance(candidate, dict) for candidate in candidates):
                raise ValueError("candidate must be a JSON object/list of objects or CSV")
            for candidate in candidates:
                if not any(candidate.get(field) for field in ("title", "id", "paper_url", "pdf_url")):
                    raise ValueError("each candidate needs title, id, paper_url, or pdf_url")
            print(json.dumps([{"candidate": candidate, "matches": candidate_matches(candidate, rows)}
                              for candidate in candidates], ensure_ascii=False, indent=2))
            return 0
        previous = read_csv(args.previous)[1] if args.previous else None
        issues = validate(headings, rows, previous)
    except (OSError, csv.Error, ValueError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    for issue in issues:
        print(issue)
    errors = sum(item.level == "error" for item in issues)
    warnings = sum(item.level == "warning" for item in issues)
    print(f"Validated {len(rows)} records: {errors} errors, {warnings} review warnings")
    return 1 if errors or (args.strict_warnings and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
