<!-- Tier 4 · GC · The chambers · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GC_CHAMBERS["GC · The chambers"]
    GC6["GC.6 · The Chancery"]
    GC7["GC.7 · The Bypass Mouth"]
    GC8["GC.8 · The Petition Rooms"]
    GC11["GC.11 · The Order"]
    GC12["GC.12 · The Rod Schedule"]
    GC13["GC.13 · The Steward's Rooms"]
    GC14["GC.14 · The Seventh Chair"]
  end

  GC2["GC.2 · The Throne Room"]
  GC3["GC.3 · The Struck Surfaces"]
  GC5["GC.5 · The Burned Wing"]
  GA26["GA.26 · The Bypass"]
  GC9["GC.9 · The Name Beneath"]
  GB12["GB.12 · The Cell Corridors"]

  GC2 --- GC6
  GC2 --- GC8
  GC3 --- GC6
  GC3 --- GC8
  GC5 --- GC6
  GC6 --- GC7
  GC6 --- GC11
  GC6 --- GC12
  GC6 --- GC13
  GC7 -.- GA26
  GC8 -.- GC9
  GC11 --- GC13
  GC13 --- GC14
  GC13 -.- GB12
```
