<!-- Tier 4 · GE · The King's end · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GE_KING["GE · The King's end"]
    GE3["GE.3 · The Crater"]
    GE4["GE.4 · Vermakith"]
    GE5["GE.5 · The Hoard Beneath Him"]
    GE6["GE.6 · The King's Chambers"]
  end

  GE2["GE.2 · The Stately Corridor"]
  I15["I.15 · The Crater Descent"]

  GE2 --- GE3
  GE2 --- GE6
  GE3 --- GE4
  GE3 --- GE5
  GE3 --- GE6
  GE4 --- GE5
  I15 ---|"one-way · down the outer face"| GE3
```
