#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"
mkdir -p "$BUILD"

FILES=(
  "$ROOT/chapters/front-matter.md"
  "$ROOT/chapters/00-introduction.md"
  "$ROOT/chapters/01-theoretical-framework.md"
  "$ROOT/chapters/02-regulatory-context.md"
  "$ROOT/chapters/03-methodology.md"
  "$ROOT/chapters/04-results.md"
  "$ROOT/chapters/05-discussion.md"
  "$ROOT/chapters/06-conclusion.md"
  "$ROOT/chapters/references.md"
)

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc is required to build the manuscript." >&2
  exit 1
fi

pandoc "${FILES[@]}" \
  --from=gfm \
  --to=docx \
  --toc \
  --number-sections \
  --metadata title="Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice" \
  --metadata lang=cs-CZ \
  -o "$BUILD/ESG-DP-2026-BLIND-01.docx"

pandoc "$ROOT/reviewer-packet/evaluation-form.md" \
  --from=gfm \
  --to=docx \
  --metadata title="Formulář nezávislého posudku" \
  --metadata lang=cs-CZ \
  -o "$BUILD/ESG-DP-2026-evaluation-form.docx"

echo "Created:"
echo "  $BUILD/ESG-DP-2026-BLIND-01.docx"
echo "  $BUILD/ESG-DP-2026-evaluation-form.docx"
echo "Convert the reviewed DOCX to PDF with a layout-preserving office suite."
