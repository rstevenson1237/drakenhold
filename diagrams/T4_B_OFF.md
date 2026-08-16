<!-- Tier 4 · B · Off the road · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph B_OFF["B · Off the road"]
    B10["B.10 · The Webbed Thickets"]
    B11["B.11 · The Collapsed Waystation"]
    B12["B.12 · The Sprite Hollow"]
    B13["B.13 · Fenn's Boundary"]
  end

  B2["B.2 · The First Waystone"]
  A12["A.12 · The Cutting Ground"]
  A13["A.13 · Wyla Fenn's Grove"]
  B5["B.5 · The Second Waystone"]
  B7["B.7 · The Turning"]
  B8["B.8 · The Third Waystone"]
  B9["B.9 · The Last Rise"]

  B2 --- B13
  B13 --- A12
  B13 --- A13
  B5 --- B10
  B5 --- B11
  B10 --- B11
  B10 --- B7
  B8 --- B12
  B12 --- B9
```
