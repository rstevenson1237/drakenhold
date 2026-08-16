<!-- Tier 4 · J · The tunnel · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph J_TUNNEL["J · The tunnel"]
    J1["J.1 · The Great Tunnel"]
    J2["J.2 · The Marked Descents"]
    J3["J.3 · The Hidden Descents"]
    J4["J.4 · The Sealed Shafts"]
    J5["J.5 · The Middens"]
    J6["J.6 · The Burnt-Out Torch"]
  end

  J7["J.7 · The Flooded Galleries"]
  J10["J.10 · The Exhausted Workings"]
  J13["J.13 · The Natural Cavern"]
  J16["J.16 · The Draught Reading"]
  FB14["FB.14 · The Marked Descent"]
  HB19["HB.19 · The Marked Descent"]
  FB4["FB.4 · Khorven, the Vent Chimney"]
  FD16["FD.16 · The Slag Channel"]
  GB20["GB.20 · The Broken Floor"]
  J14["J.14 · The Vent System"]
  J22["J.22 · The Driven Ground"]

  J1 --- J2
  J1 --- J3
  J1 --- J4
  J1 --- J5
  J1 --- J6
  J1 --- J7
  J1 --- J10
  J1 --- J13
  J1 --- J16
  J2 --- FB14
  J2 --- HB19
  J3 -.- FB4
  J3 -.- FD16
  J3 -.- GB20
  J3 --- J14
  J5 --- J22
```
