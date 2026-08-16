<!-- Tier 4 · GC · The throne · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GC_THRONE["GC · The throne"]
    GC1["GC.1 · The Ramp Head"]
    GC2["GC.2 · The Throne Room"]
    GC3["GC.3 · The Struck Surfaces"]
    GC4["GC.4 · The Overlook Balcony"]
    GC5["GC.5 · The Burned Wing"]
    GC10["GC.10 · The Line of Kings"]
    GC9["GC.9 · The Name Beneath"]
    GC15["GC.15 · The Treasury Approach"]
  end

  GA6["GA.6 · The Domed Antechamber"]
  GC6["GC.6 · The Chancery"]
  GC8["GC.8 · The Petition Rooms"]
  GD1["GD.1 · The Ramp Checkpoint"]

  GC1 --- GA6
  GC1 --- GC2
  GC2 --- GC3
  GC2 --- GC4
  GC2 --- GC5
  GC2 --- GC6
  GC2 --- GC8
  GC2 --- GC10
  GC2 --- GC15
  GC2 -.- GC9
  GC3 --- GC6
  GC3 --- GC8
  GC5 --- GC6
  GC8 -.- GC9
  GC9 -.- GC10
  GC15 --- GD1
```
