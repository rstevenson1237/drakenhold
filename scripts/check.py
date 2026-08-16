#!/usr/bin/env python3
"""
Drakenhold mechanical reconciliation checks M1–M10.

Usage:
    check.py [M1 [M2 ...]]   run the named checks (no args = all)
    check.py M1              run M1 alone
    check.py --final         run all checks in final-pass mode, where
                             surviving editorial notes are a failure (M10)

Output per check:
    M1 · Reference integrity … PASS
or
    M1 · Reference integrity … FAIL (3)
      regions/FA_Takdun.md:42 — dangling reference: ZZ.99

Exit code: 0 = all checks pass; else count of failed checks (1–127).

This script never writes to or modifies any content file.
"""

import re
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).resolve().parent.parent

# Authoritative corpus: what every check reads.
# Excluded by design:
#   mnt/user-data/outputs/   — stale pre-migration duplicate
#   archive/                  — frozen gazetteer, never edited or cited
#   Setting_Playbook_Template.md — illustrative content, contains fake codes
#   PROCEDURES_AND_RULES.md, RECONCILIATION.md, README.md, CLAUDE.md — process docs
_CORPUS_DIRS = ["regions", "blocks", "diagrams", "outlines"]
_CORPUS_FILES = [
    "Drakenhold_Setting_Outline.md",
    "HANDOFF.md",
    "DECISIONS.md",
    "OPEN_QUESTIONS.md",
]

STALE_TREE = REPO / "mnt"


def corpus_files() -> list[Path]:
    """All authoritative markdown files in scope for every check."""
    paths: list[Path] = []
    for d in _CORPUS_DIRS:
        p = REPO / d
        if p.exists():
            paths.extend(sorted(p.glob("*.md")))
    for f in _CORPUS_FILES:
        p = REPO / f
        if p.exists():
            paths.append(p)
    return paths


def region_files() -> list[Path]:
    """The 22 region files — excludes 00_INDEX.md (different structure)."""
    d = REPO / "regions"
    return [f for f in sorted(d.glob("*.md")) if f.name != "00_INDEX.md"]


def read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []


def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# Finding
# ---------------------------------------------------------------------------
class Finding(NamedTuple):
    path: Path
    lineno: int
    message: str

    def render(self) -> str:
        return f"  {relpath(self.path)}:{self.lineno} — {self.message}"


# ---------------------------------------------------------------------------
# Shared patterns
# ---------------------------------------------------------------------------
# Location code: 1–2 uppercase letters · dot · digits · optional lowercase letter
# Matches: A.1  FA.17  B.4a   but not bare region codes like FA or GB.
# Uses word boundaries so it matches codes inside backtick spans (``FA.17``) as well
# as bare prose references.  The dot is non-word so \b sits after the letters and
# after the final digit/letter, not around the dot itself.
LOC_CODE_RE = re.compile(r'\b([A-Z]{1,2}\.[0-9]+[a-z]?)\b')

# Stub heading: ### `CODE Name` — Three, Thematic, Tags
# The em-dash is U+2014.
STUB_HEADING_RE = re.compile(r'^### `([A-Z]{1,2}\.[0-9]+[a-z]?) [^`]+` — .+')


# ---------------------------------------------------------------------------
# M1 — Reference integrity
# ---------------------------------------------------------------------------
def m1(ctx: dict) -> list[Finding]:
    """Every location code in the corpus resolves to a stub in regions/."""

    # 1. Build the defined set from stub headings in region files.
    defined: dict[str, tuple[Path, int]] = {}   # code → (first-def path, lineno)
    for f in region_files():
        for lineno, line in enumerate(read_lines(f), 1):
            m = STUB_HEADING_RE.match(line)
            if m:
                code = m.group(1)
                if code not in defined:
                    defined[code] = (f, lineno)

    ctx["defined_stubs"] = defined

    # 2. Scan every corpus file for referenced location codes.
    #    Record only the first occurrence of each code for reporting.
    first_ref: dict[str, tuple[Path, int]] = {}   # code → (path, lineno)
    for f in corpus_files():
        for lineno, line in enumerate(read_lines(f), 1):
            for m in LOC_CODE_RE.finditer(line):
                code = m.group(1)
                if code not in first_ref:
                    first_ref[code] = (f, lineno)

    ctx["first_ref"] = first_ref

    # 3. Dangling: referenced but not defined as a stub anywhere.
    findings: list[Finding] = []
    for code in sorted(first_ref):
        if code not in defined:
            path, lineno = first_ref[code]
            findings.append(Finding(
                path, lineno,
                f"dangling reference: {code!r} — no matching stub heading in regions/"
            ))

    return findings


# ---------------------------------------------------------------------------
# Shared: parse ## CONNECTIONS bullets into directed edges
# ---------------------------------------------------------------------------

# Bullet line in CONNECTIONS: - **TARGET NAME** — description
# The em-dash is U+2014; some files may use U+2013.
_CONN_BULLET_RE = re.compile(r'^-\s+\*\*([^*]+)\*\*\s*[—–]\s*(.*)')

# First 1–2 uppercase letters followed by a space → region code prefix
_TARGET_CODE_RE = re.compile(r'^([A-Z]{1,2}) ')


def _known_region_codes() -> set[str]:
    """Region codes that have authoritative files in regions/."""
    return {f.name.split('_')[0] for f in region_files()}


def parse_connections(region_codes: set[str]) -> dict[str, list[tuple[str, bool, Path, int]]]:
    """
    Parse the ## CONNECTIONS section of every region file.

    Returns:
        src_code → [(target_code, is_one_way, path, lineno), ...]

    Only cross-region edges where target_code is a known region code are
    included.  Within-region targets (Wyla Fenn's grove, etc.) and named
    systems without a file (Servants' passages) are silently skipped.
    """
    result: dict[str, list] = {}
    for f in region_files():
        src = f.name.split('_')[0]
        edges: list = []
        lines = read_lines(f)
        in_conn = False
        for lineno, line in enumerate(lines, 1):
            s = line.rstrip()
            if s == '## CONNECTIONS':
                in_conn = True
                continue
            if in_conn and s.startswith('## '):
                break
            if not in_conn:
                continue
            bm = _CONN_BULLET_RE.match(s)
            if not bm:
                continue
            target_text = bm.group(1).strip()
            description = bm.group(2)
            cm = _TARGET_CODE_RE.match(target_text)
            if not cm:
                continue
            tcode = cm.group(1)
            if tcode not in region_codes or tcode == src:
                continue
            one_way = 'one-way' in description
            edges.append((tcode, one_way, f, lineno))
        result[src] = edges
    return result


# ---------------------------------------------------------------------------
# M2 — Connection symmetry
# ---------------------------------------------------------------------------
def m2(ctx: dict) -> list[Finding]:
    """For each non-one-way edge X→Y in ## CONNECTIONS, Y must name an edge back to X."""
    region_codes = _known_region_codes()
    edges = parse_connections(region_codes)
    ctx['connection_edges'] = edges

    # Collect the first line reference for each distinct (src, target) pair
    # that has at least one non-one-way edge.  Multiple bullets for the same
    # pair (e.g. FA→FB appears twice) collapse to one finding.
    non_one_way: dict[tuple[str, str], tuple[Path, int]] = {}
    for src, edge_list in edges.items():
        for target, one_way, path, lineno in edge_list:
            if not one_way:
                pair = (src, target)
                if pair not in non_one_way:
                    non_one_way[pair] = (path, lineno)

    findings: list[Finding] = []
    for (src, target), (path, lineno) in sorted(non_one_way.items()):
        return_edges = edges.get(target, [])
        has_return = any(t == src for t, _, _, _ in return_edges)
        if not has_return:
            findings.append(Finding(
                path, lineno,
                f"connection {src}→{target} not reciprocated: "
                f"{target} names no edge back to {src}"
            ))

    return findings


# ---------------------------------------------------------------------------
# Shared: mermaid edge parser (used by M3)
# ---------------------------------------------------------------------------

# Mermaid edge line patterns.  Directionality (one-way vs bidirectional) is
# encoded in the operator:
#   directed:      -->  -.->  ==>  (ends with >)
#   undirected:    ---  -.-   ===  (no arrowhead)
# Labels appear as |label| or |"label"|.
#
# We capture: node_a, operator_core, node_b from a single edge line.
# Node IDs may carry a display label: ID["display text"]; we resolve code
# from the label if present, else treat the ID itself as the code.

# Matches node id (with optional ["..."]), operator, node id
_MERMAID_EDGE_RE = re.compile(
    r'^\s*'
    r'(\w+)'                         # node A id
    r'(?:\[[^\]]*\])?'               # optional ["label"] on A (ignored here)
    r'\s*'
    r'(-[-=.]*>?|-\.[-=.]*>?|={2,}>?)'  # edge operator
    r'(?:\|[^|]*\|)?'               # optional |label|
    r'\s*'
    r'(\w+)'                         # node B id
    r'(?:\[[^\]]*\])?'               # optional ["label"] on B
    r'\s*$'
)

# Node definition: ID["display text"] or ID[display text]
_MERMAID_NODE_RE = re.compile(r'(\w+)\["?([^"\]]+)"?\]')


def _parse_mermaid_edges(lines: list[str], start: int, end: int
                         ) -> list[tuple[str, str, bool]]:
    """
    Parse mermaid edges from lines[start:end].
    Returns [(node_a, node_b, is_directed), ...] where node ids are raw.
    Also builds a node-id → display-label map for the caller to resolve codes.
    """
    # First pass: build node label map
    label_map: dict[str, str] = {}
    for line in lines[start:end]:
        for m in _MERMAID_NODE_RE.finditer(line):
            label_map[m.group(1)] = m.group(2).strip()

    edges = []
    for line in lines[start:end]:
        m = _MERMAID_EDGE_RE.match(line)
        if not m:
            continue
        a_id, op, b_id = m.group(1), m.group(2), m.group(3)
        directed = op.endswith('>')
        # Resolve display label to code if available
        a = label_map.get(a_id, a_id)
        b = label_map.get(b_id, b_id)
        # If display label is "CODE · Name" style, extract just the code token
        a_code = a.split('·')[0].strip() if '·' in a else a
        b_code = b.split('·')[0].strip() if '·' in b else b
        edges.append((a_code, b_code, directed))
    return edges


def _section_range(lines: list[str], heading: str) -> tuple[int, int]:
    """Return (start, end) line indices of content under a ## heading (exclusive)."""
    start = end = -1
    for i, line in enumerate(lines):
        if line.rstrip() == heading:
            start = i + 1
        elif start >= 0 and line.startswith('## ') and i > start:
            end = i
            break
    if start < 0:
        return (-1, -1)
    return (start, end if end >= 0 else len(lines))


def _find_mermaid_block(lines: list[str], sec_start: int, sec_end: int
                        ) -> tuple[int, int]:
    """Return (start, end) indices of the first ```mermaid…``` block in a slice."""
    in_block = False
    bstart = -1
    for i in range(sec_start, sec_end):
        s = lines[i].rstrip()
        if not in_block and s.startswith('```mermaid'):
            in_block = True
            bstart = i + 1
        elif in_block and s == '```':
            return (bstart, i)
    return (-1, -1)


# ---------------------------------------------------------------------------
# Shared: location Connections field parser (used by M3)
# ---------------------------------------------------------------------------

# A location Connections field is **Connections:** followed by inline or
# bulleted content until the next bold field (**Name:**) or heading.
# At step 7 these fields do not exist; the parser returns [] gracefully.
_CONN_FIELD_RE = re.compile(r'^\*\*Connections:\*\*\s*(.*)')


def _parse_location_connections_in_region(
        lines: list[str], region_code: str
) -> list[tuple[str, str, bool, Path, int]]:
    """
    Extract (loc_a, loc_b, one_way, path, lineno) edges from **Connections:**
    fields inside a region file.  loc_a is always the current location's code.
    """
    results = []
    current_loc: str | None = None
    in_conn = False

    for lineno, line in enumerate(lines, 1):
        s = line.rstrip()

        # Detect location stub heading to track current location code
        hm = STUB_HEADING_RE.match(s)
        if hm:
            current_loc = hm.group(1)
            in_conn = False
            continue

        # Enter Connections field
        fm = _CONN_FIELD_RE.match(s)
        if fm and current_loc:
            in_conn = True
            # Inline content on the same line
            inline = fm.group(1)
            for cm in LOC_CODE_RE.finditer(inline):
                tgt = cm.group(1)
                one_way = 'one-way' in inline
                results.append((current_loc, tgt, one_way, None, lineno))
            continue

        if in_conn:
            # Stop at next bold field or heading
            if s.startswith('**') or s.startswith('#'):
                in_conn = False
                continue
            # Bullet or inline continuation
            for cm in LOC_CODE_RE.finditer(s):
                tgt = cm.group(1)
                one_way = 'one-way' in s
                results.append((current_loc, tgt, one_way, None, lineno))

    return results


# ---------------------------------------------------------------------------
# M3 — Diagram agreement
# ---------------------------------------------------------------------------
def m3(ctx: dict) -> list[Finding]:
    """
    Every location connection bullet appears in the region's diagram, and
    every diagram edge appears in some location's Connections field.
    Diagram is authoritative.

    At step 7 all per-region diagrams are deferred and no Connections fields
    exist.  M3 passes trivially and earns its keep at steps 8–9.
    """
    findings: list[Finding] = []

    for f in region_files():
        src = f.name.split('_')[0]
        lines = read_lines(f)

        # Locate the ## REGION RELATIONAL DIAGRAM section
        sec_s, sec_e = _section_range(lines, '## REGION RELATIONAL DIAGRAM')
        diag_lineno = sec_s  # line of the heading content

        # Extract mermaid block within that section
        blk_s, blk_e = (-1, -1)
        if sec_s >= 0:
            blk_s, blk_e = _find_mermaid_block(lines, sec_s, sec_e)

        has_diagram = blk_s >= 0
        diagram_edges = _parse_mermaid_edges(lines, blk_s, blk_e) if has_diagram else []

        # Extract location Connections fields
        loc_conns = _parse_location_connections_in_region(lines, src)
        has_conns = bool(loc_conns)

        # Both absent → deferred, not a failure
        if not has_diagram and not has_conns:
            continue

        # One side absent when the other is present → failure
        if has_conns and not has_diagram:
            findings.append(Finding(
                f, sec_s + 1 if sec_s >= 0 else 1,
                f"region {src}: location Connections fields exist but diagram is missing"
            ))
            continue

        if has_diagram and not has_conns:
            findings.append(Finding(
                f, blk_s,
                f"region {src}: diagram present but no location Connections fields found"
            ))
            continue

        # Both present — check agreement.
        # Build sets: (code_a, code_b) pairs, undirected diagram edges expand both ways.
        diag_pairs: set[tuple[str, str]] = set()
        for a, b, directed in diagram_edges:
            diag_pairs.add((a, b))
            if not directed:
                diag_pairs.add((b, a))

        conn_pairs: set[tuple[str, str]] = set()
        for loc_a, loc_b, one_way, _, _ in loc_conns:
            conn_pairs.add((loc_a, loc_b))
            if not one_way:
                conn_pairs.add((loc_b, loc_a))

        # Diagram authoritative: bullets not in diagram fail
        for loc_a, loc_b, one_way, _, cln in loc_conns:
            if (loc_a, loc_b) not in diag_pairs:
                findings.append(Finding(
                    f, cln or 1,
                    f"connection {loc_a}→{loc_b} in Connections field not found in diagram"
                ))

        # Diagram edges with no corresponding bullet also fail
        conn_any = {(a, b) for a, b, *_ in loc_conns} | {(b, a) for a, b, *_ in loc_conns}
        for a, b, directed in diagram_edges:
            if (a, b) not in conn_any and (b, a) not in conn_any:
                findings.append(Finding(
                    f, blk_s,
                    f"diagram edge {a}↔{b} has no corresponding location Connections entry"
                ))

    return findings


# ---------------------------------------------------------------------------
# Shared: budget/stub-count parsers (used by M4)
# ---------------------------------------------------------------------------

# Region preamble line, e.g.:
#   "65 rooms budgeted; **34 are stubbed as locations** ..."
#   "52 rooms budgeted — 12 hall and support, 40 warren. **27 are stubbed**; ..."
#   "30 \"rooms\" budgeted, which here means posts... **16 are stubbed**; ..."
_BUDGET_LINE_RE = re.compile(r'(\d+)\s+"?rooms?"?\s+budgeted')
_STUBBED_RE = re.compile(r'\*\*(\d+)\s+are stubbed')


def _parse_region_budget_line(lines: list[str]) -> tuple[int, int, int] | None:
    """Return (budget, stated_stubbed, lineno) from a region's preamble, or None
    if the region states no room budget (approach regions A–E have none)."""
    for lineno, line in enumerate(lines, 1):
        bm = _BUDGET_LINE_RE.search(line)
        sm = _STUBBED_RE.search(line)
        if bm and sm:
            return int(bm.group(1)), int(sm.group(1)), lineno
    return None


def _parse_index_stub_table(lines: list[str]) -> dict[str, tuple[int, int]]:
    """Parse the Stubs column of regions/00_INDEX.md's region table.

    The table moved here from HANDOFF.md when the handoff was cut back to a
    pointer document. Columns are located by header name rather than by
    position, so adding a column does not silently break the check.

    Returns region_code → (stub_count, lineno). Handles "13 + 1 sub" as 14.
    """
    result: dict[str, tuple[int, int]] = {}
    code_col: int | None = None
    stub_col: int | None = None
    for lineno, line in enumerate(lines, 1):
        s = line.rstrip()
        if not s.startswith('|'):
            if code_col is not None:
                break          # table ended
            continue
        cols = [c.strip() for c in s.strip('|').split('|')]
        if code_col is None:
            lowered = [c.lower() for c in cols]
            if 'code' in lowered and 'stubs' in lowered:
                code_col = lowered.index('code')
                stub_col = lowered.index('stubs')
            continue
        if s.startswith('|---') or s.startswith('|-'):
            continue
        if max(code_col, stub_col) >= len(cols):
            continue
        code_m = re.match(r'^([A-Z]{1,2})\b', cols[code_col])
        if not code_m:
            continue
        nums = re.findall(r'\d+', cols[stub_col])
        if not nums:
            continue
        result[code_m.group(1)] = (sum(int(n) for n in nums), lineno)
    return result


# Block documents and the region codes each one aggregates.
_BLOCK_MEMBERS: dict[str, list[str]] = {
    "FIRST_LEVEL_BLOCK.md": ["FA", "GA", "HA"],
    "PEAK_1_BLOCK.md": ["FB", "FC", "FD", "FE"],
    "PEAK_2_BLOCK.md": ["GB", "GC", "GD", "GE"],
    "PEAK_3_BLOCK.md": ["HB", "HC", "HD", "HE"],
    "I_AND_J_BLOCK.md": ["I", "J"],
}

_BLOCK_BUDGET_COLON_RE = re.compile(r'Room budget for the block:\s*(\d+)')
_BLOCK_TOTAL_RE = re.compile(r'(\d+)\s+total')
_BLOCK_STUBBED_AGG_RE = re.compile(r'\*\*(\d+)\s+are stubbed')


# ---------------------------------------------------------------------------
# M4 — Budget and ratio
# ---------------------------------------------------------------------------
def m4(ctx: dict) -> list[Finding]:
    """
    Stub count against stated room budget, at roughly half (drift is flagged,
    not enforced to an exact number). Region totals against block totals.
    """
    findings: list[Finding] = []

    # Actual on-disk stub-heading counts, keyed by region code.
    actual: dict[str, int] = {}
    for f in region_files():
        code = f.name.split('_')[0]
        actual[code] = sum(1 for line in read_lines(f) if STUB_HEADING_RE.match(line))
    ctx['actual_stub_counts'] = actual

    # 1. Region preamble self-consistency: stated "M are stubbed" vs actual
    #    on-disk count, and the stubbed:budget ratio vs the ratified ~half.
    for f in region_files():
        code = f.name.split('_')[0]
        lines = read_lines(f)
        parsed = _parse_region_budget_line(lines)
        if parsed is None:
            continue   # no stated budget for this region (A–E) — nothing to check
        budget, stated_stubbed, lineno = parsed

        if stated_stubbed != actual.get(code, -1):
            findings.append(Finding(
                f, lineno,
                f"{code}: preamble states {stated_stubbed} stubbed, but "
                f"{actual.get(code, 0)} stub headings found on disk"
            ))

        if budget > 0:
            ratio = stated_stubbed / budget
            if not (0.35 <= ratio <= 0.65):
                findings.append(Finding(
                    f, lineno,
                    f"{code}: stubbed:budget ratio {stated_stubbed}/{budget} = "
                    f"{ratio:.2f} drifts far from the ratified ~half"
                ))

    # 2. regions/00_INDEX.md's Stubs column vs actual on-disk counts.
    index = REPO / "regions" / "00_INDEX.md"
    for code, (stubs, lineno) in sorted(_parse_index_stub_table(read_lines(index)).items()):
        if code in actual and actual[code] != stubs:
            findings.append(Finding(
                index, lineno,
                f"00_INDEX.md states {stubs} stubs for {code}, but "
                f"{actual[code]} stub headings found on disk"
            ))

    # 3. Block aggregate lines vs the sum of member regions' own preamble figures.
    for block_name, members in _BLOCK_MEMBERS.items():
        f = REPO / "blocks" / block_name
        lines = read_lines(f)
        if not lines:
            continue
        text = "\n".join(lines)
        budget_lineno = next(
            (i for i, l in enumerate(lines, 1) if 'Room budget for the block' in l), 1
        )

        total_m = _BLOCK_TOTAL_RE.search(text)
        colon_m = _BLOCK_BUDGET_COLON_RE.search(text)
        stated_total_budget = (
            int(total_m.group(1)) if total_m else
            int(colon_m.group(1)) if colon_m else None
        )

        sum_budget = 0
        sum_stubbed = 0
        have_all = True
        for code in members:
            rf = next((r for r in region_files() if r.name.split('_')[0] == code), None)
            if rf is None:
                have_all = False
                continue
            parsed = _parse_region_budget_line(read_lines(rf))
            if parsed is None:
                have_all = False
                continue
            b, s, _ = parsed
            sum_budget += b
            sum_stubbed += s

        if have_all and stated_total_budget is not None and stated_total_budget != sum_budget:
            findings.append(Finding(
                f, budget_lineno,
                f"{block_name}: states {stated_total_budget} total rooms, but "
                f"{'+'.join(members)} sum to {sum_budget}"
            ))

        stubbed_agg_m = _BLOCK_STUBBED_AGG_RE.search(text)
        if have_all and stubbed_agg_m:
            stated_stubbed_agg = int(stubbed_agg_m.group(1))
            if stated_stubbed_agg != sum_stubbed:
                findings.append(Finding(
                    f, budget_lineno,
                    f"{block_name}: states {stated_stubbed_agg} stubbed for the block, "
                    f"but {'+'.join(members)} sum to {sum_stubbed}"
                ))

    return findings


# ---------------------------------------------------------------------------
# Shared: region table parser (used by M5)
# ---------------------------------------------------------------------------

_CLASS_RE = re.compile(r'^\*\*Classification:\*\*\s*(\w+)')

# Classification → (expected bold table name, expected 2nd-column header)
_CLASS_TABLE = {
    "SAFE": ("Events", "Event"),
    "WILD": ("Encounter", "Encounter"),
    "DANGEROUS": ("Danger", "Danger"),
}

# The bold table-name line, e.g. "**Danger** — d6, presented at 6 on entry..."
_TABLE_NAME_LINE_RE = re.compile(r'^\*\*(\w+)\*\*\s*—\s*(d\d+),')


def _parse_region_table(lines: list[str], name_line_idx: int
                        ) -> tuple[list[str], list[tuple[list[str], int]]] | None:
    """Given the 0-based index of the bold table-name line, parse the markdown
    pipe table that follows it. Returns (header_cells, [(row_cells, lineno), ...])
    or None if no table is found immediately after."""
    i = name_line_idx + 1
    n = len(lines)
    while i < n and lines[i].strip() == '':
        i += 1
    if i >= n or not lines[i].strip().startswith('|'):
        return None
    header_cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    i += 1
    if i >= n or not lines[i].strip().startswith('|'):
        return None
    i += 1   # skip separator row
    rows: list[tuple[list[str], int]] = []
    while i < n and lines[i].strip().startswith('|'):
        cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        rows.append((cells, i + 1))
        i += 1
    return header_cells, rows


# ---------------------------------------------------------------------------
# M5 — Table conformance
# ---------------------------------------------------------------------------
def m5(ctx: dict) -> list[Finding]:
    """
    Classification determines table type (SAFE→Events, WILD→Encounter,
    DANGEROUS→Danger). Tables are always d6 / 6 rows regardless of the
    region's own Difficulty Die. Danger tables count down 6→1; all others
    ascend 1→6.
    """
    findings: list[Finding] = []

    for f in region_files():
        lines = read_lines(f)

        classification = None
        for line in lines[:6]:
            cm = _CLASS_RE.match(line)
            if cm:
                classification = cm.group(1)
                break
        if classification is None or classification not in _CLASS_TABLE:
            findings.append(Finding(f, 1, f"no recognised Classification field found"))
            continue

        expected_name, expected_col = _CLASS_TABLE[classification]

        # Find the bold table-name line.
        name_idx = None
        for i, line in enumerate(lines):
            if _TABLE_NAME_LINE_RE.match(line.strip()):
                name_idx = i
                break
        if name_idx is None:
            findings.append(Finding(
                f, 1, f"{classification} region has no table (expected a "
                f"**{expected_name}** table)"
            ))
            continue

        nm = _TABLE_NAME_LINE_RE.match(lines[name_idx].strip())
        actual_name, actual_die = nm.group(1), nm.group(2)
        name_lineno = name_idx + 1

        if actual_name != expected_name:
            findings.append(Finding(
                f, name_lineno,
                f"{classification} region has a **{actual_name}** table; "
                f"expected **{expected_name}**"
            ))

        if actual_die != "d6":
            findings.append(Finding(
                f, name_lineno,
                f"table die is {actual_die}; tables are always d6 regardless "
                f"of the region's Difficulty Die"
            ))

        parsed = _parse_region_table(lines, name_idx)
        if parsed is None:
            findings.append(Finding(
                f, name_lineno, f"no markdown table found under **{actual_name}**"
            ))
            continue

        header_cells, rows = parsed

        if len(header_cells) < 2 or header_cells[0] != "d6":
            findings.append(Finding(
                f, name_lineno + 1,
                f"table header first column is {header_cells[0]!r}; expected 'd6'"
            ))
        elif header_cells[1] != expected_col:
            findings.append(Finding(
                f, name_lineno + 1,
                f"table header second column is {header_cells[1]!r}; expected {expected_col!r}"
            ))

        if len(rows) != 6:
            findings.append(Finding(
                f, name_lineno,
                f"table has {len(rows)} rows; every region table is exactly 6 rows"
            ))

        expected_seq = [6, 5, 4, 3, 2, 1] if expected_name == "Danger" else [1, 2, 3, 4, 5, 6]
        for (cells, lineno), expected_val in zip(rows, expected_seq):
            actual_val_str = cells[0] if cells else ""
            if actual_val_str != str(expected_val):
                findings.append(Finding(
                    f, lineno,
                    f"table row out of sequence: found {actual_val_str!r}, "
                    f"expected {expected_val} "
                    f"({'descending' if expected_name == 'Danger' else 'ascending'} order)"
                ))

    return findings


# ---------------------------------------------------------------------------
# Shared: root-vocabulary parsers (used by M6)
# ---------------------------------------------------------------------------

# The outline's catalogued roots live in two TRUTHS bullets:
#   "- Roots: *az* high or royal, *kel* stone, ..."
#   "- Further roots, recovered from place-names within the hold: *tak* trade, ..."
# Each entry is *root* gloss, comma-separated.
_ROOT_ENTRY_RE = re.compile(r'\*(\w+)\*\s+([^,.*]+)')


def _catalogued_roots() -> dict[str, str]:
    """root → gloss, as recorded in the outline's TRUTHS root bullets.

    Found by scanning the corpus for the bullet prefixes rather than by reading
    a fixed path, so moving the TRUTHS field between files cannot silently
    empty the catalogue and turn M6 into a check that always passes."""
    roots: dict[str, str] = {}
    for f in corpus_files():
        for line in read_lines(f):
            s = line.strip()
            if s.startswith('- Roots:') or s.startswith('- Further roots'):
                for m in _ROOT_ENTRY_RE.finditer(s):
                    roots[m.group(1)] = m.group(2).strip()
    return roots


# A region proposing new roots marks them in bold-italic and says so explicitly:
#   "Proposed and added to the record this pass: ***rok*** road or way, ..."
_PROPOSED_ROOT_ENTRY_RE = re.compile(r'\*\*\*(\w+)\*\*\*\s+([^,.*]+)')


def _find_proposed_roots(files: list[Path]) -> list[tuple[str, str, Path, int]]:
    """[(root, gloss, path, lineno), ...] for every root a region marks as
    proposed-and-added, regardless of whether the outline was ever updated."""
    results: list[tuple[str, str, Path, int]] = []
    for f in files:
        for lineno, line in enumerate(read_lines(f), 1):
            if 'Proposed and added to the record' not in line:
                continue
            tail = line[line.index('Proposed and added to the record'):]
            for m in _PROPOSED_ROOT_ENTRY_RE.finditer(tail):
                results.append((m.group(1), m.group(2).strip(), f, lineno))
    return results


# A name's explicit self-decomposition in prose:
#   "**Khorven** — *khor* and *ven*, toward the forge — ..."
_NAME_DECOMP_RE = re.compile(
    r'\*\*([A-Z]\w*)\*\*\s*—\s*((?:\*\w+\*(?:\s+and\s+\*\w+\*)*)),'
)
_DECOMP_ROOT_RE = re.compile(r'\*(\w+)\*')


def _find_name_decompositions(files: list[Path]
                              ) -> list[tuple[str, list[str], Path, int]]:
    """[(name, [roots...], path, lineno), ...] for every explicit self-
    decomposition of a dwarven name found in prose."""
    results = []
    for f in files:
        for lineno, line in enumerate(read_lines(f), 1):
            for m in _NAME_DECOMP_RE.finditer(line):
                name = m.group(1)
                roots = _DECOMP_ROOT_RE.findall(m.group(2))
                results.append((name, roots, f, lineno))
    return results


# ---------------------------------------------------------------------------
# M6 — Vocabulary
# ---------------------------------------------------------------------------
def m6(ctx: dict) -> list[Finding]:
    """
    Names compound from the recorded root vocabulary. New roots are proposed,
    never coined in passing (CLAUDE.md rule 5). This check does not enforce
    that every dwarven proper name is decomposed — the corpus does that only
    occasionally, in prose. It enforces two things precisely, against the two
    conventions the authors themselves use to mark roots:

      1. A root a region explicitly marks "Proposed and added to the record"
         must actually be present in the outline's TRUTHS root catalogue.
         Proposing is not the same as recording; if the outline was never
         amended, that is a genuine gap and this fails.
      2. A root cited in an explicit name self-decomposition ("**Name** —
         *root* and *root*, gloss") must be either catalogued or proposed
         somewhere in the corpus — an entirely undocumented root is worse
         than an unreconciled one.
    """
    findings: list[Finding] = []
    files = corpus_files()

    catalogued = _catalogued_roots()
    proposed = _find_proposed_roots(files)
    proposed_roots = {root for root, _, _, _ in proposed}

    # 1. Every proposed root must actually be in the outline's catalogue.
    for root, gloss, path, lineno in proposed:
        if root not in catalogued:
            findings.append(Finding(
                path, lineno,
                f"root {root!r} ({gloss}) is marked 'proposed and added to the "
                f"record' but is not present in the outline's root catalogue "
                f"(Drakenhold_Setting_Outline.md TRUTHS)"
            ))

    # 2. Every root cited in a name's self-decomposition must be documented
    #    somewhere — catalogued outright, or at least proposed.
    known_roots = set(catalogued) | proposed_roots
    for name, roots, path, lineno in _find_name_decompositions(files):
        for root in roots:
            if root not in known_roots:
                findings.append(Finding(
                    path, lineno,
                    f"{name}: root {root!r} is not catalogued in the outline "
                    f"and not proposed anywhere in the corpus"
                ))

    return findings


# ---------------------------------------------------------------------------
# Shared: region format parsers (used by M7)
# ---------------------------------------------------------------------------

# Title line: # `CODE Name...`
_TITLE_RE = re.compile(r'^# `([A-Z]{1,2}) [^`]+`$')

# Classification/Difficulty/Tags line.
_CLASS_LINE_RE = re.compile(
    r'^\*\*Classification:\*\*\s*(\w+)\s*·\s*'
    r'\*\*Difficulty Die:\*\*\s*(d\d+)\s*·\s*'
    r'\*\*Tags:\*\*\s*(.+)$'
)

# The eight bold region fields, in the order the template lists them.
_REGION_FIELDS = ["Overview", "Ambiance", "Layout", "Features",
                  "Dangers", "Creatures", "Secrets", "Treasure"]
_REGION_FIELD_RE = re.compile(r'^\*\*(\w+):\*\*\s*(.*)$')

# Section headings and the two valid orderings (approach regions vs. the rest).
_SECTION_RE = re.compile(r'^## (.+)$')
_APPROACH_CODES = {"A", "B", "C", "D", "E"}
_ORDER_APPROACH = ["CONNECTIONS", "LOCATION STUBS", "TABLES", "REGION RELATIONAL DIAGRAM"]
_ORDER_DUNGEON = ["CONNECTIONS", "TABLES", "LOCATION STUBS", "REGION RELATIONAL DIAGRAM"]

# Location stub heading: ### `CODE Name` — Tag, Tag, Tag  (three tags expected,
# per every region's own "Code, name and three thematic tags per location" note)
_STUB_TAGS_RE = re.compile(r'^### `[A-Z]{1,2}\.[0-9]+[a-z]? [^`]+` — (.+)$')


# ---------------------------------------------------------------------------
# M7 — Format
# ---------------------------------------------------------------------------
def m7(ctx: dict) -> list[Finding]:
    """
    Headings, field names and entry formats match Setting_Playbook_Template.md.
    Required fields present, including those stating "None." A field whose
    value begins with "None" counts as present, never as missing.
    """
    findings: list[Finding] = []

    for f in region_files():
        lines = read_lines(f)
        code = f.name.split('_')[0]

        # 1. Title line.
        if not lines or not _TITLE_RE.match(lines[0]):
            findings.append(Finding(f, 1, "title line does not match '# `CODE Name`'"))

        # 2. Classification/Difficulty Die/Tags line (line 3 by convention).
        class_lineno = 3
        class_line = lines[2] if len(lines) >= 3 else ""
        cm = _CLASS_LINE_RE.match(class_line)
        if not cm:
            findings.append(Finding(
                f, class_lineno,
                "Classification/Difficulty Die/Tags line missing or malformed"
            ))
        else:
            classification, die, tags = cm.group(1), cm.group(2), cm.group(3)
            if classification not in ("SAFE", "WILD", "DANGEROUS"):
                findings.append(Finding(
                    f, class_lineno, f"unrecognised Classification {classification!r}"
                ))
            if not tags.strip():
                findings.append(Finding(f, class_lineno, "Tags field is empty"))

        # 3. The eight bold region fields, present, in order, non-empty.
        found_fields: list[tuple[str, str, int]] = []
        for lineno, line in enumerate(lines, 1):
            fm = _REGION_FIELD_RE.match(line)
            if fm and fm.group(1) in _REGION_FIELDS:
                found_fields.append((fm.group(1), fm.group(2).strip(), lineno))
            if line.strip() == '## CONNECTIONS':
                break   # region fields never appear past this point

        present_names = [name for name, _, _ in found_fields]
        missing = [name for name in _REGION_FIELDS if name not in present_names]
        for name in missing:
            findings.append(Finding(f, 1, f"required field **{name}:** not found"))

        # Order: the subsequence of recognised fields must match template order.
        expected_order = [n for n in _REGION_FIELDS if n in present_names]
        if present_names != expected_order:
            findings.append(Finding(
                f, found_fields[0][2] if found_fields else 1,
                f"region fields out of order: found {present_names}, "
                f"expected {expected_order}"
            ))

        # Empty values: a value is present if non-empty, even if it starts "None".
        for name, value, lineno in found_fields:
            if not value:
                findings.append(Finding(f, lineno, f"**{name}:** has no value"))

        # 4. Section headings: correct set, correct order for the region's class.
        expected_sections = (
            _ORDER_APPROACH if code in _APPROACH_CODES else _ORDER_DUNGEON
        )
        found_sections: list[tuple[str, int]] = []
        for lineno, line in enumerate(lines, 1):
            sm = _SECTION_RE.match(line.rstrip())
            if sm:
                found_sections.append((sm.group(1).strip(), lineno))

        found_names = [n for n, _ in found_sections]
        missing_sections = [s for s in expected_sections if s not in found_names]
        for s in missing_sections:
            findings.append(Finding(f, 1, f"required section '## {s}' not found"))

        extra_sections = [n for n in found_names if n not in expected_sections]
        for n in extra_sections:
            lineno = next(ln for name, ln in found_sections if name == n)
            findings.append(Finding(f, lineno, f"unexpected section '## {n}'"))

        present_expected = [n for n in expected_sections if n in found_names]
        actual_order = [n for n in found_names if n in expected_sections]
        if actual_order != present_expected:
            findings.append(Finding(
                f, found_sections[0][1] if found_sections else 1,
                f"sections out of order: found {actual_order}, expected {present_expected}"
            ))

        # 5. Location stub headings: exactly three comma-separated tags.
        for lineno, line in enumerate(lines, 1):
            sm = _STUB_TAGS_RE.match(line)
            if not sm:
                continue
            tag_count = len(sm.group(1).split(', '))
            if tag_count != 3:
                findings.append(Finding(
                    f, lineno,
                    f"location stub has {tag_count} tags, expected 3: {sm.group(1)!r}"
                ))

    return findings


# ---------------------------------------------------------------------------
# Shared: working-note / location-development markers (used by M8)
# ---------------------------------------------------------------------------
_WORKING_NOTE_RE = re.compile(r'^\*Working note:')
_PLAYERS_OVERVIEW_RE = re.compile(r"^\*Player'?s Overview:")
_REFEREE_OVERVIEW_RE = re.compile(r'^\*\*Referee Overview:\*\*')
_FEATURES_FIELD_RE = re.compile(r'^\*\*Features:\*\*')


# ---------------------------------------------------------------------------
# M8 — Struck notes
# ---------------------------------------------------------------------------
def m8(ctx: dict) -> list[Finding]:
    """
    A `*Working note:` is scaffolding for step 8/9 and is struck once a
    location's Overviews and Features are written (CLAUDE.md: the Architect
    register "must not survive" once its content is absorbed). Fails any
    location that has both a Referee Overview and a Features field — i.e. has
    been developed past the stub — while a Working note still remains.

    At step 7 every location is still a bare stub with no Overviews or
    Features, so this is expected to pass quietly; it earns its keep once
    steps 8–9 begin writing location outlines.
    """
    findings: list[Finding] = []

    for f in region_files():
        lines = read_lines(f)

        current_loc: str | None = None
        loc_start: int = 0
        has_ref_overview = False
        has_features = False
        working_note_lines: list[int] = []

        def _flush(end_idx: int) -> None:
            if current_loc is None:
                return
            if has_ref_overview and has_features and working_note_lines:
                for wn_lineno in working_note_lines:
                    findings.append(Finding(
                        f, wn_lineno,
                        f"{current_loc}: Working note remains but Referee Overview "
                        f"and Features are both written — strike the note"
                    ))

        for i, line in enumerate(lines):
            s = line.rstrip()
            hm = STUB_HEADING_RE.match(s)
            if hm:
                _flush(i)
                current_loc = hm.group(1)
                has_ref_overview = False
                has_features = False
                working_note_lines = []
                continue
            if s.startswith('## '):
                _flush(i)
                current_loc = None
                continue
            if current_loc is None:
                continue
            if _WORKING_NOTE_RE.match(s):
                working_note_lines.append(i + 1)
            elif _REFEREE_OVERVIEW_RE.match(s):
                has_ref_overview = True
            elif _FEATURES_FIELD_RE.match(s):
                has_features = True

        _flush(len(lines))

    return findings


# ---------------------------------------------------------------------------
# Shared: the editorial markup layer (used by M9 and M10)
# ---------------------------------------------------------------------------
#
# Two forms, ratified in DECISIONS.md ## NOTATION AND EDGE TYPES.
#
#   (SECTION, key)      a reference token. Survives to the finished playbook
#                       and becomes a link in the web and PDF targets.
#   [[ ... ]]           an editorial note. Designer-register, struck at the
#                       final pass alongside working notes and field labels.
#
# Single brackets are deliberately not used: `[local]`/`[setting]` already
# scope Standing Mysteries and `[tile]`/`[rod]`/`[hidden]`/... already type
# diagram edges. Double brackets collide with neither.

EDITORIAL_NOTE_RE = re.compile(r'\[\[(.+?)\]\]')

_CODE_SPAN_RE = re.compile(r'`[^`]*`')
_FENCE_RE = re.compile(r'^\s*```')


def markup_lines(path: Path):
    """Yield (lineno, text) for every line, with fenced blocks skipped and
    backtick code spans blanked out.

    A mark shown inside backticks is being *named* — in this file's own docs,
    in DECISIONS.md, in a worked example — not used. Same exemption the
    renderers apply when they substitute pointers and strip notes, so what
    the checks read and what a reader sees agree on where the markup is."""
    in_fence = False
    for lineno, line in enumerate(read_lines(path), 1):
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield lineno, _CODE_SPAN_RE.sub(lambda m: ' ' * len(m.group(0)), line)

# (SECTION, key) — SECTION is ALL CAPS, matching an outline `## ` heading
# (or the literal LORE, for LORE_INDEX.md). The key is optional; a token may
# also carry a second key, as in (TREASURE, II, 14).
REFERENCE_TOKEN_RE = re.compile(
    r'\(([A-Z][A-Z ]{2,}?)((?:,\s*[^(),]+){0,2})\)'
)

# Entry shapes the resolver keys on, one per section format actually in use.
_BESTIARY_ENTRY_RE = re.compile(r'^\*\*([^*]+)\*\*\s*\(')          # **Wolf** (Beast)
_BULLET_ENTRY_RE = re.compile(r'^-\s+\*\*([^*]+?)\.?\*\*')          # - **The covered pit.**
_TABLE_NAMED_RE = re.compile(r'^\*\*([^*]+)\*\*\s*—\s*d\d+')        # **What Is On The Board** — d6
_SUBSECTION_RE = re.compile(r'^###\s+(?:Type\s+)?([IVX]+)\b')       # ### Type II — ...
_DIE_HEADER_RE = re.compile(r'^\|\s*(d\d+)\s*\|')                   # | d20 | Graffiti |
_TABLE_ROW_RE = re.compile(r'^\|\s*(\d+)\s*\|')                     # | 14 | ... |
_LORE_ROW_RE = re.compile(r'^\|\s*([^|]+?)\s*\|')                   # | The watch log | ...

_ROMAN_RE = re.compile(r'^[IVX]+$')


def _outline_section_lines() -> dict[str, list[str]]:
    """SECTION name → its lines, gathered from wherever the field now lives.

    Sections are found by `## ` heading across the corpus plus LORE_INDEX.md,
    so splitting the outline into outlines/ — or moving a field again later —
    needs no change here."""
    sections: dict[str, list[str]] = {}
    for f in corpus_files() + [REPO / "LORE_INDEX.md"]:
        if f.parent.name == "regions" or f.parent.name == "blocks":
            continue
        current: str | None = None
        for line in read_lines(f):
            s = line.rstrip()
            if s.startswith('## '):
                name = s[3:].strip()
                current = name if name.isupper() else None
                if current:
                    sections.setdefault(current, [])
                continue
            if current:
                sections[current].append(s)
    # LORE_INDEX's register table is addressed as LORE.
    if 'THE REGISTER' in sections:
        sections['LORE'] = sections['THE REGISTER']
    return sections


def _section_entry_names(name: str, lines: list[str]) -> set[str]:
    """Every key a named reference into this section may use, lowercased."""
    names: set[str] = set()
    for s in lines:
        if name == 'LORE':
            if s.startswith('|') and not s.startswith('|---') and '|' in s[1:]:
                m = _LORE_ROW_RE.match(s)
                if m and m.group(1).lower() not in ('item', ''):
                    names.add(m.group(1).strip('` ').lower())
            continue
        for rx in (_BESTIARY_ENTRY_RE, _BULLET_ENTRY_RE, _TABLE_NAMED_RE):
            m = rx.match(s)
            if m:
                names.add(m.group(1).strip().lower())
    return names


def _section_subsections(lines: list[str]) -> set[str]:
    return {m.group(1) for s in lines if (m := _SUBSECTION_RE.match(s))}


def _section_dice(lines: list[str]) -> set[str]:
    return {m.group(1) for s in lines if (m := _DIE_HEADER_RE.match(s))}


def _section_row_numbers(lines: list[str], subsection: str | None) -> set[int]:
    """Row numbers of the section's tables. When a subsection key is given,
    only the rows of that subsection's table count."""
    rows: set[int] = set()
    active = subsection is None
    for s in lines:
        sm = _SUBSECTION_RE.match(s)
        if sm:
            active = (subsection is not None and sm.group(1) == subsection)
            continue
        if active and (m := _TABLE_ROW_RE.match(s)):
            rows.add(int(m.group(1)))
    return rows


# ---------------------------------------------------------------------------
# M9 — Editorial reference integrity
# ---------------------------------------------------------------------------
def m9(ctx: dict) -> list[Finding]:
    """
    Every `(SECTION, key)` reference token resolves.

    The section must be a real `## ` heading in the outline (or LORE), and the
    key — where one is given — must name something that section actually
    holds: a Bestiary creature, a Treasure type or row, a Traps entry, a
    procedural table, a die to roll, or a Lore register row.

    Location codes are not referenced this way. They keep their backticked
    form and stay M1's business, which is why a token carrying one fails here.
    """
    sections = _outline_section_lines()
    findings: list[Finding] = []

    for f in corpus_files():
        for lineno, line in markup_lines(f):
            for m in REFERENCE_TOKEN_RE.finditer(line):
                section = m.group(1).strip()
                keys = [k.strip() for k in m.group(2).split(',') if k.strip()]
                token = m.group(0)

                if section not in sections:
                    # Not every ALL-CAPS parenthetical is a reference token;
                    # only flag ones that look like one, i.e. that carry keys.
                    if keys:
                        findings.append(Finding(
                            f, lineno,
                            f"{token}: {section!r} is not an outline section"
                        ))
                    continue

                lines = sections[section]
                if not keys:
                    continue

                if LOC_CODE_RE.search(' '.join(keys)):
                    findings.append(Finding(
                        f, lineno,
                        f"{token}: carries a location code — write codes as "
                        f"backticked references, not reference tokens"
                    ))
                    continue

                subsection: str | None = None
                unresolved: list[str] = []
                for key in keys:
                    if _ROMAN_RE.match(key):
                        if key in _section_subsections(lines):
                            subsection = key
                        else:
                            unresolved.append(key)
                    elif key.startswith('d') and key[1:].isdigit():
                        if key not in _section_dice(lines):
                            unresolved.append(key)
                    elif key.isdigit():
                        if int(key) not in _section_row_numbers(lines, subsection):
                            unresolved.append(key)
                    else:
                        if key.lower() not in _section_entry_names(section, lines):
                            unresolved.append(key)

                for key in unresolved:
                    findings.append(Finding(
                        f, lineno,
                        f"{token}: {key!r} resolves to no entry in {section}"
                    ))

    return findings


# ---------------------------------------------------------------------------
# M10 — Editorial notes
# ---------------------------------------------------------------------------
def m10(ctx: dict) -> list[Finding]:
    """
    `[[ ... ]]` editorial notes are the designer register. CLAUDE.md: it
    "must not survive". They are struck at the final pass, alongside the
    working notes M8 governs and the field labels DECISIONS.md retires.

    During authoring this reports what is outstanding and passes. Run with
    --final it fails, which is the gate on the final pass.
    """
    findings: list[Finding] = []
    for f in corpus_files():
        for lineno, line in markup_lines(f):
            for m in EDITORIAL_NOTE_RE.finditer(line):
                note = m.group(1).strip()
                findings.append(Finding(
                    f, lineno,
                    f"editorial note outstanding: [[{note}]]"
                ))

    if not ctx.get("final"):
        for finding in findings:
            print(finding.render(), flush=True)
        return []
    return findings


# ---------------------------------------------------------------------------
# Check registry
# ---------------------------------------------------------------------------
CHECKS: dict[str, tuple[str, object]] = {
    "M1": ("Reference integrity",   m1),
    "M2": ("Connection symmetry",   m2),
    "M3": ("Diagram agreement",     m3),
    "M4": ("Budget and ratio",      m4),
    "M5": ("Table conformance",     m5),
    "M6": ("Vocabulary",            m6),
    "M7": ("Format",                m7),
    "M8": ("Struck notes",          m8),
    "M9": ("Editorial references",  m9),
    "M10": ("Editorial notes",      m10),
}


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
def main() -> None:
    # Hygiene warning about the stale duplicate tree (never affects exit code).
    if STALE_TREE.exists():
        print(
            "WARNING: mnt/user-data/outputs/regions/ exists as a stale pre-migration\n"
            "  duplicate. It is excluded from all checks. Consider removing it.\n",
            flush=True,
        )

    # Determine which checks to run.
    args = [a for a in sys.argv[1:] if a != "--final"]
    final = "--final" in sys.argv[1:]
    requested: list[str] = args if args else list(CHECKS)
    unknown = [r for r in requested if r.upper() not in CHECKS]
    if unknown:
        print(f"Unknown check(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"Available: {', '.join(CHECKS)}", file=sys.stderr)
        sys.exit(1)
    # Normalise case so "m1" works too.
    requested = [r.upper() for r in requested]

    ctx: dict = {"final": final}
    failed = 0

    for key in requested:
        label, fn = CHECKS[key]
        findings: list[Finding] = fn(ctx)
        if findings:
            print(f"{key} · {label} … FAIL ({len(findings)})")
            for f in findings:
                print(f.render())
            failed += 1
        else:
            print(f"{key} · {label} … PASS")

    sys.exit(min(failed, 127))


if __name__ == "__main__":
    main()
