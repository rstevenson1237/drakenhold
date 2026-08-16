<!-- Tier 2 · Peak 3 · Spirit and the Dead · the regions in the block and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  HA["HA · Thaldun"]
  HB["HB · Nurmor"]
  HC["HC · Sigdun"]
  HD["HD · Zarkel"]
  HE["HE · Sigaz"]

  HA --- HB
  HA --- HC
  HC --- HD
  HD --- HE
```
