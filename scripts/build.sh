#!/bin/sh
# Assemble the Drakenhold Setting Playbook from source files.
# Usage: build.sh [OUT_PATH]   (default: build/Drakenhold_Playbook.md)
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/build.py" "$@"
