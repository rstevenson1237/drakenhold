<!-- Tier 2 · Peak 2 · Authority and the Dragon · the regions in the block and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  GA["GA · Grathdun"]
  GB["GB · Karmor"]
  GC["GC · Azdun"]
  GD["GD · Valdmor"]
  GE["GE · Azith"]

  GA --- GB
  GA --- GC
  GA --- GE
  GB --- GC
  GC --- GD
  GD --- GE
```
