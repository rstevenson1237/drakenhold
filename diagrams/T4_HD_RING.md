<!-- Tier 4 · HD · The circuit · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HD_RING["HD · The circuit"]
    HD4["HD.4 · The Circuit"]
    HD5["HD.5 · The Trial of Weight"]
    HD6["HD.6 · The Trial of the Word"]
    HD7["HD.7 · The Trial of the Dark"]
    HD8["HD.8 · The Trial of the Post"]
    HD9["HD.9 · The Trial of Refusal"]
    HD10["HD.10 · The Grant"]
  end

  HD2["HD.2 · The Receiving Room"]
  HD11["HD.11 · The Observation Rooms"]
  HC12["HC.12 · The Excavation Face"]

  HD2 --- HD4
  HD4 --- HD5
  HD5 --- HD6
  HD6 --- HD7
  HD7 --- HD8
  HD8 --- HD9
  HD9 --- HD10
  HD10 --- HD4
  HD4 -.- HD11
  HD10 -.- HD11
  HD4 -.- HC12
```
