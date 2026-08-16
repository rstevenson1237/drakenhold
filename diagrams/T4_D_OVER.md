<!-- Tier 4 · D · The overlook · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph D_OVER["D · The overlook"]
    D1["D.1 · The Overlook"]
    D2["D.2 · The Guard Outpost"]
    D3["D.3 · The Outpost Cache"]
    D4["D.4 · The Watch Log"]
  end

  B9["B.9 · The Last Rise"]
  D5["D.5 · The Near Booth"]
  D10["D.10 · The Charter Camp"]

  B9 --- D1
  D1 --- D2
  D1 --- D5
  D1 --- D10
  D2 --- D4
  D2 -.- D3
```
