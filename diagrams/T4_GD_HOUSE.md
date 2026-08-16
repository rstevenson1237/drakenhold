<!-- Tier 4 · GD · The counting house · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GD_HOUSE["GD · The counting house"]
    GD1["GD.1 · The Ramp Checkpoint"]
    GD14["GD.14 · The Holding Room"]
    GD7["GD.7 · The Weighing Floor"]
    GD2["GD.2 · Valdgir, the Skybridge Terminus"]
    GD5["GD.5 · The Tally Room"]
    GD6["GD.6 · Isskavar's Room"]
    GD15["GD.15 · The Skimmers' Cache"]
    GD16["GD.16 · The Ramp to the Lair"]
  end

  GC15["GC.15 · The Treasury Approach"]
  GD3["GD.3 · The Sundered Vault"]
  I3["I.3 · The Central Terminus"]
  GD11["GD.11 · The Lizardman Quarters"]
  GE1["GE.1 · The Head of the Ramp"]

  GD1 --- GC15
  GD1 --- GD3
  GD1 --- GD7
  GD1 --- GD14
  GD2 --- GD7
  GD2 --- I3
  GD3 --- GD7
  GD5 --- GD6
  GD5 --- GD7
  GD6 -.- GD15
  GD7 --- GD11
  GD7 --- GD16
  GD16 --- GE1
```
