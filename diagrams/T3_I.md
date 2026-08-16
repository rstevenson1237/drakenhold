<!-- Tier 3 · region I · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  I_FACES["The faces"]
  I_PRIZES["The prizes and the drop"]
  I_SPAN["The span"]

  I_SPAN --- I_FACES
  I_FACES --- I_PRIZES
```
