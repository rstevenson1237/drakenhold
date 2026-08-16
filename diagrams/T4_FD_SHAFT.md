<!-- Tier 4 · FD · The chimney and the channels · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FD_SHAFT["FD · The chimney and the channels"]
    FD9["FD.9 · The Chimney Head"]
    FD10["FD.10 · The Flow Gate"]
    FD16["FD.16 · The Slag Channel"]
  end

  FD2["FD.2 · The Forge Floor"]
  FD3["FD.3 · The Banked Channels"]
  FB15["FB.15 · The Chimney Ledges"]
  J3["J.3 · The Hidden Descents"]

  FD2 --- FD9
  FD3 --- FD10
  FD3 --- FD16
  FD9 --- FD10
  FD9 -.- FB15
  FD16 -.- J3
```
