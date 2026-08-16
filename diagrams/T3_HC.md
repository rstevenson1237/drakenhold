<!-- Tier 3 · region HC · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  HC_CELLS["The cells and side chambers"]
  HC_CHAPEL["The chapel"]
  HC_DIG["The excavation"]

  HC_CHAPEL --- HC_CELLS
  HC_CHAPEL --- HC_DIG
```
