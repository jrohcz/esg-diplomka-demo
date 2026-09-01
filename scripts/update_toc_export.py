#!/usr/bin/env python3
"""Update document indexes through LibreOffice UNO, resave DOCX and export PDF."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


def prop(name: str, value):
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def connect(port: int, attempts: int = 30):
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    url = f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"
    last_error = None
    for _ in range(attempts):
        try:
            return resolver.resolve(url)
        except Exception as exc:  # UNO raises generated exception types.
            last_error = exc
            time.sleep(1)
    raise RuntimeError(f"Unable to connect to LibreOffice UNO at port {port}: {last_error}")


def export_document(path: Path, port: int, update_indexes: bool) -> tuple[Path, Path]:
    ctx = connect(port)
    service_manager = ctx.ServiceManager
    desktop = service_manager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    input_url = uno.systemPathToFileUrl(str(path.resolve()))
    document = desktop.loadComponentFromURL(
        input_url,
        "_blank",
        0,
        (prop("Hidden", True), prop("ReadOnly", False)),
    )
    if document is None:
        raise RuntimeError(f"LibreOffice could not open {path}")

    try:
        if update_indexes:
            indexes = document.getDocumentIndexes()
            for index in range(indexes.getCount()):
                indexes.getByIndex(index).update()

        # Resave the DOCX after index updates so the delivered editable file
        # contains the same visible TOC as the PDF.
        document.storeAsURL(
            input_url,
            (
                prop("FilterName", "Office Open XML Text"),
                prop("Overwrite", True),
            ),
        )

        pdf_path = path.with_suffix(".pdf")
        pdf_url = uno.systemPathToFileUrl(str(pdf_path.resolve()))
        filter_data = (
            prop("SelectPdfVersion", 1),
            prop("UseTaggedPDF", True),
            prop("ExportBookmarks", True),
            prop("ExportNotes", False),
        )
        document.storeToURL(
            pdf_url,
            (
                prop("FilterName", "writer_pdf_Export"),
                prop("Overwrite", True),
                prop("FilterData", filter_data),
            ),
        )
        return path, pdf_path
    finally:
        document.close(True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("documents", nargs="+", type=Path)
    parser.add_argument("--port", type=int, default=2002)
    parser.add_argument(
        "--toc-document",
        type=Path,
        help="Only this document receives an index update; all documents are exported.",
    )
    args = parser.parse_args()

    toc_resolved = args.toc_document.resolve() if args.toc_document else None
    for document in args.documents:
        if not document.is_file():
            raise FileNotFoundError(document)
        update = toc_resolved is not None and document.resolve() == toc_resolved
        docx, pdf = export_document(document, args.port, update)
        print(f"DOCX: {docx}")
        print(f"PDF:  {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
