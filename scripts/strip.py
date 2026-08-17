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
# The weight declaration is an authoring constraint and never a reader's
# business: the form carries weight to a reader.
_WEIGHT_LINE = re.compile(r'^\*\*Weight:\*\*')

# An editorial note, anywhere in a line.
_NOTE = re.compile(r'\[\[.+?\]\]')

# A block document's pass-shaped heading: `## PASS 3 — LOCATIONS (STEP 8)`
_PASS_HEADING = re.compile(
    r'^(?P<hashes>#{2,3})\s*PASS\s+\d+\s*—\s*(?P<title>.+?)(?:\s*\(STEP\s*\d+\))?\s*$'
)

# A Connections field runs until the next bold field or heading or blank-then-heading.
_FIELD_OR_HEADING = re.compile(r'^(\*\*[A-Za-z][^*]*:\*\*|#{1,6} |\*Working note:)')

# --- architect register in region files -------------------------------------
#
# Every region file carries italic process prose under its headings. CLAUDE.md
# says the architect register "must not survive", and one of these sentences
# describes the Connections: field that this same script removes.
#
# It cannot be struck by the line, because in several files the procedural
# sentences share a line with genuinely referee-facing content — the fill
# description in "40 rooms budgeted; 20 are stubbed and the balance is
# unnamed fill — bunk rows, kit rooms, empty cells by the dozen" tells a
# Referee what the unnamed rooms are, and that is play content. So this is
# sentence-level, with each pattern written out rather than inferred.
#
# Still subtractive: every pattern deletes and none rewrites. The room-budget
# note is handled separately below, as a whole line.
_ARCHITECT_SENTENCES = [
    re.compile(r'Procedure step \d+ for the code, name and three thematic tags; '
               r'\*\*procedure step \d+ for the outlines below them\.\*\*\s*'),
    re.compile(r'Procedure step \d+\.\s*(?=Block-level material)'),
    re.compile(r'Procedure step \d+ for [^.]*\.\s*'),
    re.compile(r'Procedure step \d+\.\s*Drawn from the stubs, before the location outlines\.\s*'),
    re.compile(r'Procedure step \d+\.\s*'),
    re.compile(r"Each location carries a Player's Overview in the player register, "
               r"a Referee Overview in the referee register, and the features the "
               r"location contains\.\s*"),
    re.compile(r'Feature detail is written at step \d+\.\s*'),
    re.compile(r'The step-\d+ working notes have been absorbed into the two '
               r'Overviews and struck\.\s*'),
    re.compile(r'Working notes are scaffolding for step \d+\.\s*'),
    re.compile(r'Code, name and three thematic tags per location\.\s*'),
    re.compile(r'The working note under each is scaffolding for step \d+\.\s*'),
    re.compile(r'Reconciled against the finished outlines before the region closes\.\s*'),
    # "Block-level material — ... lives in `X_BLOCK.md`" and "Worked as one
    # block with ..." are deliberately NOT here. They are cross-references,
    # and the blocks are published parts, so they point a reader at something
    # they can actually turn to.
    re.compile(r'\*\*Reconciled against the finished outlines at step \d+; this is the '
               r'reconciled diagram and it is the deliverable\.\*\*\s*'),
    re.compile(r'The diagram is authoritative: the \*\*Connections:\*\* field under each '
               r'stub is checked against it, never the reverse\.\s*'),
]

# The room-budget note: "40 rooms budgeted; **20 are stubbed as locations**
# and the balance is unnamed fill inside the stated groupings — emptied bins,
# collapsed rank ends, sleeping holes..."
#
# Struck whole, and this is the one removal that costs something. The budget
# and stub count are architect vocabulary and go. The fill description after
# the dash is referee-facing — it tells a Referee what the unnamed rooms are —
# and it goes with them, because "the balance is unnamed fill" is a fragment
# once the count it refers to is gone, and repairing it would be a rewrite
# rather than a removal.
#
# So the content is relocated rather than lost: the fill description belongs
# in the region's Layout field, in referee register, and moving it there is a
# step-10 task per region. Step 12's gate names it. This is J2 demotion —
# write the destination first, then cut — and the strike is the cut.
_BUDGET_LINE = re.compile(r'^\*[0-9]+ ["“]?rooms?["”]?[ ,]')

# An italic-only line, which is the shape all of this prose takes.
_ITALIC_LINE = re.compile(r'^\*(?!\*)(?P<body>.*)\*\s*$')


def _strip_architect(line: str):
    """Remove procedural sentences from an italic note. Returns None if
    nothing survives, meaning the whole line goes."""
    m = _ITALIC_LINE.match(line)
    if not m:
        return line
    body = m.group('body')
    original = body
    for pat in _ARCHITECT_SENTENCES:
        body = pat.sub('', body)
    if body == original:
        return line
    body = re.sub(r'\s{2,}', ' ', body).strip()
    return None if not body else f"*{body}*"


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

        # The weight declaration.
        if _WEIGHT_LINE.match(line):
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

        # The room-budget note, struck whole.
        if _BUDGET_LINE.match(line):
            i += 1
            if i < len(lines) and not lines[i].strip() and out and not out[-1].strip():
                i += 1
            continue

        # Architect register in an italic note: sentence-level.
        stripped = _strip_architect(line)
        if stripped is None:
            i += 1
            if i < len(lines) and not lines[i].strip() and out and not out[-1].strip():
                i += 1
            continue
        line = stripped

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
