#!/usr/bin/env python3
"""Deterministic integrity checks for the blinded ESG thesis manuscript."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "chapters/front-matter.md",
    "chapters/00-introduction.md",
    "chapters/01-theoretical-framework.md",
    "chapters/02-regulatory-context.md",
    "chapters/03-methodology.md",
    "chapters/04-results.md",
    "chapters/05-discussion.md",
    "chapters/06-conclusion.md",
    "chapters/references.md",
    "sources/corporate-documents.csv",
    "analysis/document-codebook-v2.csv",
    "data/document-corpus.csv",
    "analysis/coding-revisions.csv",
    "analysis/control-coding.csv",
    "analysis/high-evidence-review.csv",
    "analysis/evidence-matrix.csv",
    "audit/claim-evidence-ledger.csv",
]

FINAL_CHAPTERS = [ROOT / p for p in REQUIRED_FILES if p.startswith("chapters/")]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_csv(relative: str) -> list[dict[str, str]]:
    path = ROOT / relative
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        if not reader.fieldnames:
            fail(f"CSV has no header: {relative}")
        rows = list(reader)
        width = len(reader.fieldnames)
        for line_no, row in enumerate(rows, start=2):
            if None in row or len(row) != width:
                fail(f"Unstable CSV width in {relative} at line {line_no}")
        return rows


def main() -> int:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"Missing or empty required file: {relative}")

    csv_files = sorted(ROOT.glob("**/*.csv"))
    for path in csv_files:
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle, strict=True))
        if not rows:
            fail(f"Empty CSV: {path.relative_to(ROOT)}")
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            fail(f"Unstable CSV width: {path.relative_to(ROOT)}")

    corpus = read_csv("data/document-corpus.csv")
    if len(corpus) != 45:
        fail(f"Expected 45 first-round evidence segments, got {len(corpus)}")

    ids = [row["segment_id"] for row in corpus]
    if len(ids) != len(set(ids)):
        fail("Duplicate segment_id in document corpus")

    cases = Counter(row["case_id"] for row in corpus)
    expected_cases = {"CEZ": 11, "MONETA": 12, "O2": 11, "SKODA": 11}
    if dict(cases) != expected_cases:
        fail(f"Unexpected case distribution: {dict(cases)}")

    # Apply final coding override recorded after the blinded control round.
    final_classes = {row["segment_id"]: row["evidence_class"] for row in corpus}
    final_classes["CEZ-011"] = "E2"
    class_counts = Counter(final_classes.values())
    expected_classes = {"E0": 1, "E1": 8, "E2": 27, "E3": 8, "E4": 1}
    if dict(class_counts) != expected_classes:
        fail(f"Unexpected final evidence distribution: {dict(class_counts)}")

    high_review = read_csv("analysis/high-evidence-review.csv")
    expected_high = {sid for sid, cls in final_classes.items() if cls in {"E3", "E4"}}
    reviewed_high = {row["segment_id"] for row in high_review}
    if reviewed_high != expected_high:
        fail(
            "E3/E4 review coverage mismatch: "
            f"missing={sorted(expected_high - reviewed_high)}, "
            f"extra={sorted(reviewed_high - expected_high)}"
        )

    claims = read_csv("audit/claim-evidence-ledger.csv")
    if len(claims) < 25:
        fail("Claim-evidence ledger is unexpectedly small")
    if any(row["status"] != "verified" for row in claims):
        fail("Every manuscript claim must have status=verified before freeze")

    final_text = "\n".join(path.read_text(encoding="utf-8") for path in FINAL_CHAPTERS)
    forbidden_empirical = [
        r"syntetick(?:ý|á|é) rozhovor",
        r"respondent(?:i|ů|a)? S0[1-9]",
        r"synthetic-pilot-interviews",
        r"syntetick(?:á|ou) analýz",
    ]
    for pattern in forbidden_empirical:
        if re.search(pattern, final_text, flags=re.IGNORECASE):
            fail(f"Final manuscript appears to cite synthetic empirical material: {pattern}")

    required_strings = [
        "45 klíčových",
        "E0",
        "E4",
        "rozhodovací vazba",
        "omezené ujištění",
        "ČEZ Group",
        "MONETA Money Bank",
        "O2 Czech Republic",
        "Škoda Auto",
    ]
    for value in required_strings:
        if value not in final_text:
            fail(f"Required manuscript concept missing: {value}")

    print("Validation passed.")
    print(f"Required files: {len(REQUIRED_FILES)}")
    print(f"CSV files parsed strictly: {len(csv_files)}")
    print(f"Evidence segments: {len(corpus)}")
    print(f"Final evidence classes: {dict(sorted(class_counts.items()))}")
    print(f"Verified manuscript claims: {len(claims)}")
    print(f"High-evidence items rechecked: {len(high_review)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
