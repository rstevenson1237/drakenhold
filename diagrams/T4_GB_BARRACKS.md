<!-- Tier 4 · GB · The barracks half · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GB_BARRACKS["GB · The barracks half"]
    GB1["GB.1 · The Stairwell Foot"]
    GB2["GB.2 · The Arena"]
    GB9["GB.9 · The Benches"]
    GB10["GB.10 · The Fallen Ground"]
    GB8["GB.8 · The Soldiers' Quarters"]
    GB6["GB.6 · The Muster Office"]
    GB7["GB.7 · The Planning Rooms"]
    GB3["GB.3 · The Formation"]
    GB4["GB.4 · Karn Rudgir"]
    GB5["GB.5 · The Armoury"]
  end

  GA6["GA.6 · The Domed Antechamber"]
  GB11["GB.11 · The Prison Gate"]
  GA17["GA.17 · The Armoury Support"]

  GB1 --- GA6
  GB1 --- GB2
  GB2 --- GB3
  GB2 --- GB6
  GB2 --- GB8
  GB2 --- GB9
  GB2 --- GB10
  GB2 --- GB11
  GB3 --- GB4
  GB3 --- GB5
  GB5 --- GA17
  GB6 --- GB7
```
