<!-- Tier 3 · region FC · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FC_DISPATCH["The dispatch floor"]
  FC_GATED["Behind the craftsmen's gate"]
  FC_HALLS["The four halls"]

  FC_DISPATCH --- FC_GATED
  FC_DISPATCH --- FC_HALLS
```
