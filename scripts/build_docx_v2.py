#!/usr/bin/env python3
"""Final build wrapper with layout and terminology corrections discovered during visual QA."""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.shared import Cm, Pt

import build_docx as base

NUMBER_MARKER = "§NUM§"


def normalize_text(text: str) -> str:
    text = base_original_clean(text)
    replacements = {
        "ověřitelný výsledek či dopad": "externě podpořený konkrétní výsledek",
        "ověřitelný výsledek a dopad": "externě podpořený konkrétní výsledek",
        "ověřitelný dopad": "externě podpořený výsledek",
        "verifiable impact": "externally supported specific result",
        NUMBER_MARKER: "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def preprocess_numbered_lists(markdown: str) -> str:
    """Turn Markdown ordered-list items into isolated literal-number paragraphs.

    Word's built-in List Number style otherwise continues numbering across unrelated
    lists and chapters. Literal source numbers preserve the author's intended order.
    """
    output: list[str] = []
    for line in markdown.replace("\r\n", "\n").split("\n"):
        match = re.match(r"^(\s*)(\d+)\.\s+(.+)$", line)
        if match:
            if output and output[-1] != "":
                output.append("")
            output.append(f"{match.group(1)}{NUMBER_MARKER}{match.group(2)}. {match.group(3)}")
            output.append("")
        else:
            output.append(line)
    return "\n".join(output)


def parse_markdown_final(doc, markdown: str, *, references: bool = False) -> None:
    base_original_parse(doc, preprocess_numbered_lists(markdown), references=references)


def set_a4(section) -> None:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)


def setup_document_final(doc) -> None:
    base_original_setup(doc)
    for section in doc.sections:
        set_a4(section)


def start_numbered_section_final(doc) -> None:
    base_original_start_numbered_section(doc)
    set_a4(doc.sections[-1])


def polish_docx(path: Path) -> None:
    doc = Document(path)
    for section in doc.sections:
        set_a4(section)

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if re.match(r"^\d+\.\s+", text):
            paragraph.paragraph_format.left_indent = Cm(0.75)
            paragraph.paragraph_format.first_line_indent = Cm(-0.45)
            paragraph.paragraph_format.space_after = Pt(0)
        if text == base.TITLE:
            for run in paragraph.runs:
                run.font.size = Pt(16)
        if text == "UNIVERZITA JANA EVANGELISTY PURKYNĚ V ÚSTÍ NAD LABEM":
            for run in paragraph.runs:
                run.font.size = Pt(13)
        if text == "Diplomová práce - experimentální rukopis pro zaslepené odborné hodnocení":
            for run in paragraph.runs:
                run.text = run.text.replace(" - ", " – ")

    doc.save(path)


base_original_clean = base.clean_markdown_text
base_original_parse = base.parse_markdown
base_original_setup = base.setup_document
base_original_start_numbered_section = base.start_numbered_section

base.clean_markdown_text = normalize_text
base.parse_markdown = parse_markdown_final
base.setup_document = setup_document_final
base.start_numbered_section = start_numbered_section_final


def main() -> int:
    result = base.main()
    for path in sorted(base.BUILD.glob("*.docx")):
        polish_docx(path)
        print(f"Polished: {path}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
