#!/bin/sh
# Renders the Drakenhold sources to a browsable static site in build/web/.
# Requires node/npm. Run scripts/render_pdf.sh first if you want the PDF
# bundled alongside the site (the site links to it either way).
# Usage: build_web.sh [OUT_DIR]   (default: build/web)
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/pdf"
if [ ! -d node_modules ]; then
  npm ci
fi
exec node render_web.mjs "$@"
