<!-- Tier 4 · HD · The receiving floor · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HD_FLOOR["HD · The receiving floor"]
    HD1["HD.1 · The Ramp Head"]
    HD2["HD.2 · The Receiving Room"]
    HD3["HD.3 · The Skybridge Terminus"]
  end

  HC1["HC.1 · The Ramp Head"]
  HE1["HE.1 · The Ramp Head"]
  HD4["HD.4 · The Circuit"]
  I4["I.4 · The Eastern Terminus"]

  HD1 --- HC1
  HD1 --- HE1
  HD1 --- HD2
  HD2 --- HD3
  HD2 --- HD4
  HD3 -.- I4
```
