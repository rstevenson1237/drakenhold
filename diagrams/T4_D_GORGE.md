<!-- Tier 4 · D · The gorge · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph D_GORGE["D · The gorge"]
    D5["D.5 · The Near Booth"]
    D6["D.6 · The Drain Outfall"]
    D7["D.7 · The Three Spans"]
    D8["D.8 · The Far Booth"]
    D9["D.9 · The Broken Ground"]
    D11["D.11 · The Climbing Road"]
  end

  D1["D.1 · The Overlook"]
  D10["D.10 · The Charter Camp"]
  B4a["B.4a · The Drain Mouth"]
  E1["E.1 · The Guard Wall"]

  D1 --- D5
  D10 --- D5
  D5 --- D6
  D5 --- D7
  D6 -.- B4a
  D7 --- D8
  D7 -.- D11
  D8 --- D9
  D8 --- D11
  D9 --- D11
  D11 --- E1
```
