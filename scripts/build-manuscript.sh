#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python scripts/validate-manuscript.py
python scripts/build_docx_v2.py

if ! command -v libreoffice >/dev/null 2>&1; then
  echo "LibreOffice is required to update the table of contents and export PDF." >&2
  exit 1
fi

PROFILE="/tmp/esg-thesis-lo-$$"
mkdir -p "$PROFILE"
libreoffice \
  -env:UserInstallation=file://$PROFILE \
  --headless \
  --accept='socket,host=127.0.0.1,port=2002;urp;StarOffice.ComponentContext' \
  --norestore \
  --nofirststartwizard \
  >/tmp/esg-thesis-libreoffice.log 2>&1 &
LO_PID=$!
trap 'kill ${LO_PID} 2>/dev/null || true; rm -rf "$PROFILE"' EXIT
sleep 4

PYTHONPATH="/usr/lib/python3/dist-packages${PYTHONPATH:+:$PYTHONPATH}" \
python scripts/update_toc_export.py \
  --port 2002 \
  --toc-document build/ESG-DP-2026-BLIND-01.docx \
  build/ESG-DP-2026-BLIND-01.docx \
  build/ESG-DP-2026-reviewer-instructions.docx \
  build/ESG-DP-2026-evaluation-form.docx \
  build/ESG-DP-2026-post-review-reveal.docx

kill "$LO_PID" 2>/dev/null || true
wait "$LO_PID" 2>/dev/null || true

printf 'Created review documents in %s/build\n' "$ROOT"
find build -maxdepth 1 -type f \( -name '*.docx' -o -name '*.pdf' \) -printf '  %f\n' | sort
