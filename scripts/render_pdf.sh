#!/bin/sh
# Renders build/Drakenhold_Playbook.md to build/Drakenhold_Playbook.pdf.
# Requires scripts/build.sh to have run first, and node/npm to be available.
# Usage: render_pdf.sh [INPUT.md] [OUTPUT.pdf]
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/pdf"
if [ ! -d node_modules ]; then
  npm ci
fi
exec node render.mjs "$@"
