<!-- Tier 4 · HD · The centre · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HD_CENTRE["HD · The centre"]
    HD11["HD.11 · The Observation Rooms"]
    HD12["HD.12 · The Scattered Notes"]
    HD13["HD.13 · Wyla Fenn's Assessment"]
    HD14["HD.14 · The Hidden Piece"]
    HD15["HD.15 · The Leadership's Equipment"]
    HD16["HD.16 · The Way Up"]
  end

  HD4["HD.4 · The Circuit"]
  HD10["HD.10 · The Grant"]
  HE3["HE.3 · The Way Down From Observation"]

  HD4 -.- HD11
  HD10 -.- HD11
  HD11 --- HD12
  HD11 --- HD13
  HD11 --- HD14
  HD11 --- HD15
  HD11 --- HD16
  HD16 -.- HE3
```
