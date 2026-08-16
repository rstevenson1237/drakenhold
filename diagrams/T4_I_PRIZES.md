<!-- Tier 4 · I · The prizes and the drop · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph I_PRIZES["I · The prizes and the drop"]
    I13["I.13 · The FE Run"]
    I14["I.14 · The GD Run"]
    I15["I.15 · The Crater Descent"]
    I16["I.16 · The Undefended Approach"]
  end

  I7["I.7 · The Assessment"]
  I8["I.8 · The Ladder-Stairs"]
  I12["I.12 · The Fallen Runs"]
  FE7["FE.7 · The Scorched Gallery"]
  GD12["GD.12 · The Orphaned Run"]
  GE3["GE.3 · The Crater"]

  I7 -.- I13
  I7 -.- I14
  I7 -.- I16
  I8 --- I15
  I12 -.- I13
  I12 -.- I14
  I12 -.- I16
  I13 -.- FE7
  I14 -.- GD12
  I15 --> GE3
```
