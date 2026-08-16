<!-- Tier 4 · FD · The galleries · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FD_GALLERIES["FD · The galleries"]
    FD6["FD.6 · The Production Galleries"]
    FD7["FD.7 · The Line of Work"]
    FD8["FD.8 · The Stock Rooms"]
  end

  FD2["FD.2 · The Forge Floor"]
  FD5["FD.5 · The Order Post"]
  FC5["FC.5 · The Rising Chutes"]
  FC21["FC.21 · The Hidden Access"]

  FD2 --- FD6
  FD5 --- FD6
  FD6 --- FD7
  FD7 --- FD8
  FD8 -.- FC5
  FD8 -.- FC21
```
