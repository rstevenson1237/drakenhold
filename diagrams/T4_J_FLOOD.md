<!-- Tier 4 · J · The flooded galleries · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph J_FLOOD["J · The flooded galleries"]
    J7["J.7 · The Flooded Galleries"]
    J8["J.8 · The Drowned Working"]
    J9["J.9 · The Outfall"]
  end

  J1["J.1 · The Great Tunnel"]
  D6["D.6 · The Drain Outfall"]

  J1 --- J7
  J7 --- J8
  J7 --- J9
  J9 -.-> D6
```
