<!-- Tier 4 · I · The span · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph I_SPAN["I · The span"]
    I1["I.1 · The Western Terminus"]
    I2["I.2 · The Great Span"]
    I3["I.3 · The Central Terminus"]
    I5["I.5 · The Ice Stretch"]
    I4["I.4 · The Eastern Terminus"]
  end

  FD15["FD.15 · The Skybridge Terminus"]
  I6["I.6 · The Run-Heads"]
  GD2["GD.2 · Valdgir, the Skybridge Terminus"]
  HD3["HD.3 · The Skybridge Terminus"]

  I1 -.- FD15
  I1 --- I2
  I2 --- I3
  I2 --- I6
  I3 -.- GD2
  I3 --- I5
  I5 --- I4
  I5 --- I6
  I4 -.- HD3
```
