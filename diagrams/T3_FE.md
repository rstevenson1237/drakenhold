<!-- Tier 3 · region FE · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FE_ANTE["The antechamber"]
  FE_CHAMBERS["The four chambers"]
  FE_UPPER["The upper gallery"]

  FE_ANTE --- FE_CHAMBERS
  FE_ANTE --- FE_UPPER
```
