<!-- Tier 4 · B · On the road · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph B_ROAD["B · On the road"]
    B1["B.1 · The Road Out"]
    B2["B.2 · The First Waystone"]
    B3["B.3 · The Wheel-Rut Reach"]
    B4["B.4 · The Silted Culvert"]
    B4a["B.4a · The Drain Mouth"]
    B5["B.5 · The Second Waystone"]
    B6["B.6 · The Deadfall"]
    B7["B.7 · The Turning"]
    B8["B.8 · The Third Waystone"]
    B9["B.9 · The Last Rise"]
  end

  A1["A.1 · The Landing Gate"]
  B13["B.13 · Fenn's Boundary"]
  D6["D.6 · The Drain Outfall"]
  B10["B.10 · The Webbed Thickets"]
  B11["B.11 · The Collapsed Waystation"]
  C1["C.1 · Ashfoot Camp"]
  C2["C.2 · Wetreed Camp"]
  C3["C.3 · Longmire Camp"]
  B12["B.12 · The Sprite Hollow"]
  D1["D.1 · The Overlook"]

  B1 --- A1
  B1 --- B2
  B2 --- B3
  B2 --- B13
  B3 --- B4
  B4 -.- B4a
  B4a -.- D6
  B4 --- B5
  B5 --- B6
  B5 --- B10
  B5 --- B11
  B10 --- B7
  B6 --- B7
  B7 --- B8
  B7 --- C1
  B7 --- C2
  B7 --- C3
  B8 --- B9
  B8 --- B12
  B12 --- B9
  B9 --- D1
```
