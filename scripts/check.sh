#!/bin/sh
# Drakenhold mechanical reconciliation checks.
# Usage: check.sh [M1 [M2 ...]]   (no args = run all)
# Each check can be invoked alone: check.sh M1
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/check.py" "$@"
