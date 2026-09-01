#!/usr/bin/env python3
"""Surface-style diagnostics for the authorial revision pass.

The script does NOT estimate whether a text was written by AI. It reports
observable properties that are useful during editing: sentence and paragraph
length, repeated sentence openings, stock phrases and repeated n-grams.

Examples:
    python scripts/style-audit.py chapters/01-theoretical-framework.md
    python scripts/style-audit.py chapters/*.md --format json
    python scripts/style-audit.py baseline.md --compare revised.md
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

WORD_RE = re.compile(r"\b[0-9A-Za-zÁ-žÀ-ž][0-9A-Za-zÁ-žÀ-ž’'\-]*\b", re.UNICODE)
HEADING_RE = re.compile(r"^#{1,6}\s+")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?(?:\s*\|\s*:?-{3,}:?)+\s*\|?\s*$")
LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+] |\d+[.)]\s+)")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ0-9„\"])")

PROTECTED_ABBREVIATIONS = (
    "např.",
    "tj.",
    "tzv.",
    "resp.",
    "apod.",
    "atd.",
    "kol.",
    "et al.",
    "Ing.",
    "Ph.D.",
    "Bc.",
    "Mgr.",
)

STOCK_PHRASES = (
    "pro tuto práci",
    "práce proto",
    "empirická analýza",
    "výsledky ukazují",
    "současně však",
    "zároveň však",
    "může, ale nemusí",
    "nejde pouze o",
    "lze tedy",
    "z tohoto důvodu",
    "na základě uvedeného",
    "pro empirickou část",
)

# Short function words are omitted when repeated n-grams are ranked. This does
# not remove them from sentence-length or lexical counts.
NGRAM_STOPWORDS = {
    "a",
    "i",
    "v",
    "ve",
    "z",
    "ze",
    "na",
    "do",
    "pro",
    "s",
    "se",
    "je",
    "jsou",
    "byl",
    "byla",
    "bylo",
    "být",
    "že",
    "který",
    "která",
    "které",
    "tento",
    "tato",
    "toto",
}


@dataclass(frozen=True)
class Distribution:
    count: int
    mean: float
    median: float
    stdev: float
    coefficient_of_variation: float
    minimum: int
    maximum: int
    p10: float
    p90: float


@dataclass(frozen=True)
class StyleReport:
    label: str
    files: list[str]
    words: int
    unique_words: int
    lexical_diversity: float
    sentences: Distribution
    paragraphs: Distribution
    stock_phrases: dict[str, int]
    stock_phrases_per_1000_words: dict[str, float]
    top_sentence_openings: list[tuple[str, int]]
    repeated_opening_sentences: int
    top_repeated_ngrams: list[tuple[str, int]]


def percentile(values: Sequence[int], percentile_value: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    index = (len(ordered) - 1) * percentile_value
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return float(ordered[lower])
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def distribution(values: Sequence[int]) -> Distribution:
    if not values:
        return Distribution(0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0)
    mean = statistics.mean(values)
    stdev = statistics.pstdev(values)
    return Distribution(
        count=len(values),
        mean=round(mean, 2),
        median=round(float(statistics.median(values)), 2),
        stdev=round(stdev, 2),
        coefficient_of_variation=round(stdev / mean, 3) if mean else 0.0,
        minimum=min(values),
        maximum=max(values),
        p10=round(percentile(values, 0.10), 2),
        p90=round(percentile(values, 0.90), 2),
    )


def protect_abbreviations(text: str) -> str:
    protected = text
    for abbreviation in PROTECTED_ABBREVIATIONS:
        protected = protected.replace(abbreviation, abbreviation.replace(".", "<DOT>"))
    return protected


def split_sentences(paragraph: str) -> list[str]:
    protected = protect_abbreviations(paragraph)
    sentences = SENTENCE_SPLIT_RE.split(protected)
    return [sentence.replace("<DOT>", ".").strip() for sentence in sentences if sentence.strip()]


def remove_markdown_noise(text: str) -> list[str]:
    """Return prose paragraphs while omitting code, tables and bare headings."""

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"```.*?```", "\n", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("*", "").replace("_", "")

    paragraphs: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        if not buffer:
            return
        paragraph = " ".join(part.strip() for part in buffer if part.strip())
        paragraph = re.sub(r"\s+", " ", paragraph).strip()
        buffer = []
        if len(WORD_RE.findall(paragraph)) >= 5:
            paragraphs.append(paragraph)

    for raw_line in text.split("\n"):
        line = raw_line.strip()
        if not line:
            flush()
            continue
        if HEADING_RE.match(line):
            flush()
            continue
        if TABLE_SEPARATOR_RE.match(line):
            flush()
            continue
        if line.startswith("|") and line.endswith("|"):
            flush()
            continue
        line = re.sub(r"^>\s?", "", line)
        line = LIST_MARKER_RE.sub("", line)
        buffer.append(line)

    flush()
    return paragraphs


def words(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]


def sentence_opening(sentence: str, length: int = 2) -> str:
    tokens = words(sentence)
    return " ".join(tokens[:length])


def repeated_ngrams(tokens: Sequence[str], n: int = 4, minimum_count: int = 2) -> list[tuple[str, int]]:
    counts: Counter[str] = Counter()
    for index in range(0, len(tokens) - n + 1):
        gram_tokens = tokens[index : index + n]
        if sum(token in NGRAM_STOPWORDS for token in gram_tokens) >= n - 1:
            continue
        counts[" ".join(gram_tokens)] += 1
    return [(gram, count) for gram, count in counts.most_common(20) if count >= minimum_count]


def build_report(paths: Sequence[Path], label: str) -> StyleReport:
    paragraphs: list[str] = []
    for path in paths:
        try:
            paragraphs.extend(remove_markdown_noise(path.read_text(encoding="utf-8")))
        except OSError as exc:
            raise RuntimeError(f"Cannot read {path}: {exc}") from exc

    sentence_list = [sentence for paragraph in paragraphs for sentence in split_sentences(paragraph)]
    all_text = " ".join(paragraphs)
    all_words = words(all_text)
    sentence_lengths = [len(words(sentence)) for sentence in sentence_list if words(sentence)]
    paragraph_lengths = [len(words(paragraph)) for paragraph in paragraphs if words(paragraph)]

    openings = [sentence_opening(sentence) for sentence in sentence_list]
    opening_counts = Counter(opening for opening in openings if opening)
    repeated_opening_sentences = sum(count for count in opening_counts.values() if count >= 3)

    lowered = all_text.lower()
    phrase_counts = {phrase: lowered.count(phrase) for phrase in STOCK_PHRASES}
    denominator = len(all_words) / 1000 if all_words else 1.0
    phrase_rates = {phrase: round(count / denominator, 2) for phrase, count in phrase_counts.items()}

    return StyleReport(
        label=label,
        files=[str(path) for path in paths],
        words=len(all_words),
        unique_words=len(set(all_words)),
        lexical_diversity=round(len(set(all_words)) / len(all_words), 3) if all_words else 0.0,
        sentences=distribution(sentence_lengths),
        paragraphs=distribution(paragraph_lengths),
        stock_phrases=phrase_counts,
        stock_phrases_per_1000_words=phrase_rates,
        top_sentence_openings=opening_counts.most_common(15),
        repeated_opening_sentences=repeated_opening_sentences,
        top_repeated_ngrams=repeated_ngrams(all_words),
    )


def markdown_report(report: StyleReport) -> str:
    lines = [
        f"# Style audit: {report.label}",
        "",
        "> This report describes surface properties. It does not estimate authorship or AI probability.",
        "",
        "## Corpus",
        "",
        f"- Files: {', '.join(report.files)}",
        f"- Words: {report.words}",
        f"- Unique words: {report.unique_words}",
        f"- Lexical diversity: {report.lexical_diversity}",
        "",
        "## Length distributions",
        "",
        "| Unit | Count | Mean | Median | SD | CV | Min | P10 | P90 | Max |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        (
            f"| Sentence (words) | {report.sentences.count} | {report.sentences.mean} | "
            f"{report.sentences.median} | {report.sentences.stdev} | "
            f"{report.sentences.coefficient_of_variation} | {report.sentences.minimum} | "
            f"{report.sentences.p10} | {report.sentences.p90} | {report.sentences.maximum} |"
        ),
        (
            f"| Paragraph (words) | {report.paragraphs.count} | {report.paragraphs.mean} | "
            f"{report.paragraphs.median} | {report.paragraphs.stdev} | "
            f"{report.paragraphs.coefficient_of_variation} | {report.paragraphs.minimum} | "
            f"{report.paragraphs.p10} | {report.paragraphs.p90} | {report.paragraphs.maximum} |"
        ),
        "",
        "## Stock phrases",
        "",
        "| Phrase | Count | Per 1,000 words |",
        "|---|---:|---:|",
    ]
    for phrase in STOCK_PHRASES:
        lines.append(
            f"| {phrase} | {report.stock_phrases[phrase]} | "
            f"{report.stock_phrases_per_1000_words[phrase]} |"
        )

    lines.extend(["", "## Repeated sentence openings", ""])
    lines.append(f"Sentences belonging to an opening repeated at least three times: {report.repeated_opening_sentences}")
    lines.append("")
    for opening, count in report.top_sentence_openings:
        lines.append(f"- `{opening}`: {count}")

    lines.extend(["", "## Repeated four-word sequences", ""])
    if report.top_repeated_ngrams:
        for gram, count in report.top_repeated_ngrams:
            lines.append(f"- `{gram}`: {count}")
    else:
        lines.append("No four-word sequence met the repetition threshold.")

    return "\n".join(lines) + "\n"


def comparison_markdown(first: StyleReport, second: StyleReport) -> str:
    def delta(new: float, old: float) -> str:
        value = new - old
        return f"{value:+.2f}"

    return "\n".join(
        [
            f"# Style comparison: {first.label} vs. {second.label}",
            "",
            "> Differences are editorial diagnostics, not evidence of human or AI authorship.",
            "",
            "| Metric | First | Second | Delta (second - first) |",
            "|---|---:|---:|---:|",
            f"| Words | {first.words} | {second.words} | {second.words - first.words:+d} |",
            f"| Sentence mean | {first.sentences.mean} | {second.sentences.mean} | {delta(second.sentences.mean, first.sentences.mean)} |",
            f"| Sentence SD | {first.sentences.stdev} | {second.sentences.stdev} | {delta(second.sentences.stdev, first.sentences.stdev)} |",
            f"| Sentence CV | {first.sentences.coefficient_of_variation} | {second.sentences.coefficient_of_variation} | {delta(second.sentences.coefficient_of_variation, first.sentences.coefficient_of_variation)} |",
            f"| Paragraph mean | {first.paragraphs.mean} | {second.paragraphs.mean} | {delta(second.paragraphs.mean, first.paragraphs.mean)} |",
            f"| Paragraph SD | {first.paragraphs.stdev} | {second.paragraphs.stdev} | {delta(second.paragraphs.stdev, first.paragraphs.stdev)} |",
            f"| Lexical diversity | {first.lexical_diversity} | {second.lexical_diversity} | {delta(second.lexical_diversity, first.lexical_diversity)} |",
            f"| Repeated-opening sentences | {first.repeated_opening_sentences} | {second.repeated_opening_sentences} | {second.repeated_opening_sentences - first.repeated_opening_sentences:+d} |",
            "",
        ]
    )


def expand_paths(patterns: Iterable[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        candidate = Path(pattern)
        if candidate.exists():
            paths.append(candidate)
            continue
        matches = sorted(Path().glob(pattern))
        paths.extend(path for path in matches if path.is_file())
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            unique.append(path)
            seen.add(resolved)
    return unique


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Markdown or plain-text files, optionally glob patterns")
    parser.add_argument("--label", default="primary", help="Label used in the report")
    parser.add_argument("--compare", nargs="+", help="Second set of files for a compact comparison")
    parser.add_argument("--compare-label", default="comparison", help="Label for the comparison corpus")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path, help="Write the report to a file instead of stdout")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    primary_paths = expand_paths(args.files)
    if not primary_paths:
        print("No readable primary files matched.", file=sys.stderr)
        return 2

    primary = build_report(primary_paths, args.label)
    reports = [primary]
    comparison_text = ""

    if args.compare:
        comparison_paths = expand_paths(args.compare)
        if not comparison_paths:
            print("No readable comparison files matched.", file=sys.stderr)
            return 2
        comparison = build_report(comparison_paths, args.compare_label)
        reports.append(comparison)
        comparison_text = comparison_markdown(primary, comparison)

    if args.format == "json":
        output = json.dumps([asdict(report) for report in reports], ensure_ascii=False, indent=2) + "\n"
    else:
        output = "\n".join(markdown_report(report) for report in reports)
        if comparison_text:
            output += "\n" + comparison_text

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
