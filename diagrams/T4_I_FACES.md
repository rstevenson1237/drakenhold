<!-- Tier 4 · I · The faces · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph I_FACES["I · The faces"]
    I6["I.6 · The Run-Heads"]
    I7["I.7 · The Assessment"]
    I8["I.8 · The Ladder-Stairs"]
    I9["I.9 · The Watchtowers"]
    I10["I.10 · The Attack Points"]
    I11["I.11 · The Guard's Quarters"]
    I12["I.12 · The Fallen Runs"]
  end

  I2["I.2 · The Great Span"]
  I5["I.5 · The Ice Stretch"]
  I13["I.13 · The FE Run"]
  I14["I.14 · The GD Run"]
  I16["I.16 · The Undefended Approach"]
  I15["I.15 · The Crater Descent"]

  I2 --- I6
  I5 --- I6
  I6 --- I7
  I6 --- I8
  I6 --- I12
  I7 --- I8
  I7 --- I12
  I7 -.- I13
  I7 -.- I14
  I7 -.- I16
  I8 --- I9
  I8 --- I10
  I8 --- I11
  I8 --- I15
  I9 --- I10
  I9 --- I11
  I10 --- I11
  I12 -.- I13
  I12 -.- I14
  I12 -.- I16
```
