<!-- Tier 3 · region HB · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  HB_BELOW["Below the tiers"]
  HB_DESCENT["The descent"]
  HB_GUARD["The guard gallery"]
  HB_MIDDLE["The Runemaster and guild galleries"]
  HB_ROYAL["The royal gallery"]

  HB_GUARD --- HB_BELOW
  HB_DESCENT --- HB_ROYAL
  HB_DESCENT --- HB_GUARD
  HB_ROYAL --- HB_GUARD
  HB_MIDDLE --- HB_GUARD
  HB_ROYAL --- HB_MIDDLE
```
