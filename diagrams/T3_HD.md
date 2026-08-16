<!-- Tier 3 · region HD · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  HD_CENTRE["The centre"]
  HD_FLOOR["The receiving floor"]
  HD_RING["The circuit"]

  HD_RING --- HD_CENTRE
  HD_FLOOR --- HD_RING
```
