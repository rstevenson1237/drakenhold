<!-- Tier 4 · J · The natural cavern and the vents · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph J_CAVERN["J · The natural cavern and the vents"]
    J13["J.13 · The Natural Cavern"]
    J14["J.14 · The Vent System"]
    J15["J.15 · The Hot Runs"]
    J16["J.16 · The Draught Reading"]
  end

  J1["J.1 · The Great Tunnel"]
  J3["J.3 · The Hidden Descents"]
  J20["J.20 · The Deep Dark"]
  J23["J.23 · The Sunless Water"]

  J1 --- J13
  J1 --- J16
  J3 --- J14
  J13 --- J14
  J13 --- J20
  J13 --- J23
  J14 --- J15
  J14 --- J16
  J16 --- J20
```
