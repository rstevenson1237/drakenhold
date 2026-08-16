<!-- Tier 1 · the setting · the region blocks and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  APPROACH["The approach"]
  PEAK_1["Peak 1 · Trade and Craft"]
  PEAK_2["Peak 2 · Authority and the Dragon"]
  PEAK_3["Peak 3 · Spirit and the Dead"]
  I_AND_J["The Skybridge and the Lost Caverns"]

  APPROACH --- PEAK_1
  PEAK_1 --- PEAK_2
  PEAK_1 --- I_AND_J
  PEAK_2 --- PEAK_3
  PEAK_2 --- I_AND_J
  PEAK_3 --- I_AND_J
  I_AND_J --- APPROACH
```
