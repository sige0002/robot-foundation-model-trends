#!/usr/bin/env python3
"""Deterministically generate README and all taxonomy pages from papers.csv."""
from __future__ import annotations

import argparse
import csv
import html
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import quote

try:
    from .db import CATEGORIES, ROOT, read_csv, split_values
    from .validate_csv import validate
except ImportError:
    from db import CATEGORIES, ROOT, read_csv, split_values
    from validate_csv import validate

LABELS = {"vla": "VLA · Vision–Language–Action", "wam": "WAM · World / Action Models",
          "agent": "Agent", "hybrid": "Hybrid"}
BANNER = "<!-- GENERATED from papers.csv by scripts/build_markdown.py; do not edit directly. -->\n"


def text(value: str) -> str:
    # Source titles/summaries are content, not Markdown/HTML instructions.
    value = html.escape(value or "", quote=False)
    for char in ("\\", "`", "*", "_", "[", "]", "|", "#"):
        value = value.replace(char, "\\" + char)
    return value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def link(label: str, url: str) -> str:
    # Escape Markdown link delimiters and encode Unicode/whitespace safely.
    return f"[{text(label)}]({quote(url, safe=':/?#=&%+@;,-._~')})"


def paper_block(row: dict) -> str:
    links = [link(label, row[field]) for field, label in (
        ("paper_url", "Paper"), ("pdf_url", "PDF"), ("code_url", "Code"), ("project_url", "Project")) if row.get(field)]
    output = [f"### {text(row['title'])}", "", f"- ID: `{row['id']}`",
              f"- Published: {row.get('published') or 'unknown / 未確認'}" + (f" · Updated: {row['updated']}" if row.get("updated") else ""),
              "- Authors: " + text("; ".join(split_values(row.get("authors", "")))),
              "- Venue: " + text(row.get("venue") or "unknown / 未確認"),
              "- Links: " + " · ".join(links),
              "- Tags: " + (", ".join(text(item) for item in split_values(row.get("tags", ""))) or "—"),
              "- Model size: " + text(row.get("model_size") or "unknown / 未確認"),
              "- Open-source: " + text(row.get("open_source", "unknown")),
              "- Code / weights / license: " + " / ".join(text(row.get(field) or "unknown") for field in ("code_status", "weights_status", "license_status")),
              "", "**概要（日本語）**", "", text(row.get("summary_ja", "")),
              "", "**主な貢献**", "", text(row.get("key_contribution", ""))]
    if row.get("source_checked") or row.get("review_status") or row.get("evidence_note"):
        output += ["", "**確認記録**", "", "- Checked: " + (row.get("source_checked") or "unknown") +
                   " · Review: " + text(row.get("review_status") or "unknown")]
        if row.get("evidence_note"):
            output += ["- " + text(row["evidence_note"])]
    return "\n".join(output) + "\n"


def ordered(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: (row.get("published", ""), row.get("id", "")), reverse=True)


def generated_files(rows: list[dict], template: str) -> dict[str, str]:
    counts = Counter((row["main_category"], row["subcategory"]) for row in rows)
    total = len(rows)
    # A reproducible data-review timestamp, never the build machine's clock.
    last_updated = max((row.get("source_checked") or "" for row in rows), default="") or "unknown / 未確認"
    files = {}
    count_lines = ["| 分類 | 論文数 |", "| --- | ---: |"]
    map_lines = []
    for category, subcategories in CATEGORIES.items():
        category_count = sum(counts[category, sub] for sub in subcategories)
        count_lines += [f"| [{LABELS[category]}]({category}/README.md) | {category_count} |"]
        map_lines += [f"### [{LABELS[category]}]({category}/README.md)", ""]
        index = [BANNER.rstrip(), f"# {LABELS[category]}", "", "[← データベース](../README.md)", "",
                 f"{category_count} records · 正本: [papers.csv](../papers.csv)", "",
                 "| Subcategory | Papers |", "| --- | ---: |"]
        for subcategory in subcategories:
            count = counts[category, subcategory]
            path = f"{category}/{subcategory}.md"
            selected = [row for row in rows if row["main_category"] == category and row["subcategory"] == subcategory]
            page = [BANNER.rstrip(), f"# {LABELS[category]} / {subcategory}", "",
                    f"[← {category}](README.md) · [CSV master](../papers.csv)", "",
                    f"{count} records · Published date 降順（同日 ID 降順）", ""]
            if not selected:
                page += ["この分類には、まだ登録がありません。", ""]
            else:
                for row in ordered(selected):
                    page += [paper_block(row).rstrip(), ""]
            files[path] = "\n".join(page).rstrip() + "\n"
            index += [f"| [{subcategory}]({subcategory}.md) | {count} |"]
            map_lines += [f"- [{subcategory}]({path}) ({count})"]
        map_lines += [""]
        index += ["", "## 論文", ""]
        if not category_count:
            index += ["まだ登録がありません。", ""]
        for row in ordered([row for row in rows if row["main_category"] == category]):
            index += [f"- {row.get('published') or 'unknown'} · {link(row['title'], row['subcategory'] + '.md')} · `{row['id']}`"]
        files[f"{category}/README.md"] = "\n".join(index).rstrip() + "\n"
    count_lines += [f"| **合計** | **{total}** |"]
    rendered = template.replace("{{COUNTS}}", "\n".join(count_lines)).replace("{{TECHMAP}}", "\n".join(map_lines).rstrip()).replace("{{TOTAL}}", str(total)).replace("{{LAST_UPDATED}}", last_updated)
    files["README.md"] = BANNER + rendered.rstrip() + "\n"
    return files


def build(csv_path: Path, output: Path, template: Path, check: bool = False) -> list[str]:
    headings, rows = read_csv(csv_path)
    errors = [issue for issue in validate(headings, rows) if issue.level == "error"]
    if errors:
        raise ValueError("Invalid CSV:\n" + "\n".join(str(error) for error in errors))
    files = generated_files(rows, template.read_text(encoding="utf-8"))
    changed = []
    for relative, content in sorted(files.items()):
        destination = output / relative
        existing = destination.read_text(encoding="utf-8") if destination.exists() else None
        if existing != content:
            changed.append(relative)
            if not check:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(content, encoding="utf-8", newline="\n")
    return changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=ROOT / "papers.csv")
    parser.add_argument("--output", type=Path, default=ROOT)
    parser.add_argument("--template", type=Path, default=ROOT / "docs/README.template.md")
    parser.add_argument("--check", action="store_true", help="fail if any generated file differs; do not write")
    args = parser.parse_args(argv)
    try:
        changed = build(args.csv, args.output, args.template, args.check)
    except (OSError, csv.Error, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if args.check and changed:
        print("Stale or missing generated files:\n" + "\n".join(changed))
        return 1
    print(f"{'Checked' if args.check else 'Generated'} 25 Markdown files; {len(changed)} changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
