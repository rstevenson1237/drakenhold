<!-- Tier 3 · region A · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  A_FARM["Ketter's Farmstead"]
  A_OUT["Outskirts"]
  A_UPPER["Upper town"]
  A_WHARF["Wharf quarter"]

  A_UPPER --- A_FARM
  A_OUT --- A_FARM
  A_UPPER --- A_OUT
  A_UPPER --- A_WHARF
```
