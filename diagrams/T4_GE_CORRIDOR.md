<!-- Tier 4 · GE · The corridor · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GE_CORRIDOR["GE · The corridor"]
    GE1["GE.1 · The Head of the Ramp"]
    GE2["GE.2 · The Stately Corridor"]
  end

  GD16["GD.16 · The Ramp to the Lair"]
  GE3["GE.3 · The Crater"]
  GE6["GE.6 · The King's Chambers"]
  GE7["GE.7 · The Queen's Apartments"]
  GE9["GE.9 · The Servants' Way"]

  GE1 --- GD16
  GE1 --- GE2
  GE2 --- GE3
  GE2 --- GE6
  GE2 --- GE7
  GE2 --- GE9
```
