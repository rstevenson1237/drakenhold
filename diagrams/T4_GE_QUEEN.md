<!-- Tier 4 · GE · The Queen's end · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GE_QUEEN["GE · The Queen's end"]
    GE7["GE.7 · The Queen's Apartments"]
    GE8["GE.8 · The Queen's Correspondence"]
    GE9["GE.9 · The Servants' Way"]
  end

  GE2["GE.2 · The Stately Corridor"]
  GA22["GA.22 · The Capillary Maze"]

  GE2 --- GE7
  GE2 --- GE9
  GE7 --- GE8
  GE7 --- GE9
  GE9 -.- GA22
```
