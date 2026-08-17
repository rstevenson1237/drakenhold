#!/usr/bin/env python3
"""
Step 12 — the strike. Removes everything written for an author and never
for a reader.

Usage:
    strip.py                 report what would be removed; changes nothing
    strip.py --write         perform the strike, in place
    strip.py --repo PATH     operate on a different tree (fixtures)
    strip.py --diff          print the resulting diff to stdout, change nothing

PROCEDURES_AND_RULES.md step 12 states what comes off and this script is the
whole of the removal. What it takes out:

    *Working note: ...*             scaffolding, absorbed at step 9
    *Player's Overview: TEXT*  ->   *TEXT*        italic IS the marker
    **Referee Overview:** TEXT ->   TEXT          plain text IS the marker
    **Features:**                   the bullet list IS the marker
    **Connections:** ...            the `->` pointers ARE the record
    [[ ... ]]                       editorial notes, playtest ones included
    ## PASS 1 — MAJOR ROUTES   ->   ## MAJOR ROUTES

This script is subtractive only. It never writes a word that was not already
in the file, and the one thing that looks like an exception — turning
`## PASS 1 — MAJOR ROUTES` into `## MAJOR ROUTES` — is the removal of a
prefix, which is why step 12 owns it.

IT IS A ONE-WAY DOOR. It removes exactly the data the checks read: M3 parses
the Connections field, M8 parses the working notes, M12 parses both. Run it
only on a release branch cut from main, and never merge that branch back.
The script refuses to run on a tree whose git branch looks like main.

The gate in front of this script is judgement and is not the script's to
decide. See step 12: every region closed through step 11, J13 clear, M3
repointed, every predicate built, check.sh green on the pre-strike source,
and no route B/C/D item outstanding against shipped ground.
"""

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402  — the corpus definition and location grammar

# --- the removals -----------------------------------------------------------

# A whole line that is only a working note.
_WORKING_NOTE_LINE = re.compile(r'^\*Working note:.*\*\s*$')

# Label strips. Each keeps the text and drops the name of the field.
_PLAYERS_LABEL = re.compile(r"^\*Player'?s Overview:\s*")
_REFEREE_LABEL = re.compile(r'^\*\*Referee Overview:\*\*\s*')
_FEATURES_LINE = re.compile(r'^\*\*Features:\*\*\s*$')
_CONNECTIONS_LINE = re.compile(r'^\*\*Connections:\*\*')

# An editorial note, anywhere in a line.
_NOTE = re.compile(r'\[\[.+?\]\]')

# A block document's pass-shaped heading: `## PASS 3 — LOCATIONS (STEP 8)`
_PASS_HEADING = re.compile(
    r'^(?P<hashes>#{2,3})\s*PASS\s+\d+\s*—\s*(?P<title>.+?)(?:\s*\(STEP\s*\d+\))?\s*$'
)

# A Connections field runs until the next bold field or heading or blank-then-heading.
_FIELD_OR_HEADING = re.compile(r'^(\*\*[A-Za-z][^*]*:\*\*|#{1,6} |\*Working note:)')


def strip_text(text: str) -> str:
    """Apply the strike to one file's contents."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Connections field: drop the line and any continuation under it.
        if _CONNECTIONS_LINE.match(line):
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    break
                if _FIELD_OR_HEADING.match(nxt):
                    break
                i += 1
            # Collapse the blank line the field left behind.
            while out and not out[-1].strip() and i < len(lines) and not lines[i].strip():
                i += 1
            continue

        # Working note: drop the line, and the blank after it if it leaves a gap.
        if _WORKING_NOTE_LINE.match(line):
            i += 1
            if i < len(lines) and not lines[i].strip() and out and not out[-1].strip():
                i += 1
            continue

        # Features label: the bullet list below is the marker.
        if _FEATURES_LINE.match(line):
            i += 1
            if i < len(lines) and not lines[i].strip():
                i += 1
            continue

        # Field labels: keep the prose, drop the name.
        line = _PLAYERS_LABEL.sub('*', line)
        line = _REFEREE_LABEL.sub('', line)

        # Pass-shaped block headings lose the prefix.
        pm = _PASS_HEADING.match(line)
        if pm:
            line = f"{pm.group('hashes')} {pm.group('title').strip()}"

        # Editorial notes, wherever they sit.
        if _NOTE.search(line):
            line = _NOTE.sub('', line)
            if not line.strip():
                i += 1
                continue
            line = re.sub(r'\s{2,}', ' ', line).rstrip()

        out.append(line)
        i += 1

    return '\n'.join(out).rstrip('\n') + '\n'


def target_files() -> list:
    """Everything the strike touches: the corpus, plus the block documents."""
    return check.corpus_files()


def current_branch(repo: Path) -> str:
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def main() -> None:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--write", action="store_true", help="perform the strike in place")
    ap.add_argument("--diff", action="store_true", help="print the diff, change nothing")
    ap.add_argument("--repo", help="operate on a different tree")
    ap.add_argument("--force", action="store_true",
                    help="strike even on a branch that looks like main")
    args = ap.parse_args()

    if args.repo:
        check.set_repo(args.repo)
    repo = check.REPO

    if args.write:
        branch = current_branch(repo)
        if branch in {"main", "master"} and not args.force:
            print(
                f"refusing to strike on branch '{branch}'.\n"
                "  Step 12 runs on a release branch cut from main and never merged\n"
                "  back, because it removes the data every check reads and cannot\n"
                "  be re-run. Cut a branch, or pass --force if you meant it.",
                file=sys.stderr,
            )
            sys.exit(2)

    changed = 0
    removed_lines = 0
    for f in target_files():
        before = f.read_text(encoding="utf-8")
        after = strip_text(before)
        if before == after:
            continue
        changed += 1
        removed_lines += len(before.splitlines()) - len(after.splitlines())
        if args.diff:
            sys.stdout.writelines(difflib.unified_diff(
                before.splitlines(keepends=True),
                after.splitlines(keepends=True),
                fromfile=f"a/{check.relpath(f)}",
                tofile=f"b/{check.relpath(f)}",
            ))
        if args.write:
            f.write_text(after, encoding="utf-8")

    verb = "struck" if args.write else "would strike"
    print(f"{verb}: {changed} files, {removed_lines} lines removed", flush=True)
    if not args.write:
        print("  nothing was written. --write performs the strike.", flush=True)


if __name__ == "__main__":
    main()
