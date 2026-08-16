<!-- Tier 2 · Peak 1 · Trade and Craft · the regions in the block and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FA["FA · Takdun"]
  FB["FB · Brankel"]
  FC["FC · Mekdun"]
  FD["FD · Khorvak"]
  FE["FE · Aztak"]

  FA --- FB
  FA --- FC
  FB --- FC
  FB --- FD
  FC --- FD
  FD --- FE
```
