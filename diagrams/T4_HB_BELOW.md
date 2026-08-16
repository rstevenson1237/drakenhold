<!-- Tier 4 · HB · Below the tiers · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HB_BELOW["HB · Below the tiers"]
    HB14["HB.14 · The Blank Wall"]
    HB15["HB.15 · The Niche"]
    HB16["HB.16 · The Lance"]
    HB17["HB.17 · The Survivors' Burials"]
    HB19["HB.19 · The Marked Descent"]
    HB20["HB.20 · The Older Course"]
  end

  HB11["HB.11 · The Guard Gallery"]
  HB12["HB.12 · The Late Burials"]
  HA21["HA.21 · The Survivors' Burials"]
  J2["J.2 · The Marked Descents"]

  HB11 --- HB14
  HB12 --- HB17
  HB14 --- HB17
  HB14 --- HB19
  HB14 --- HB20
  HB15 -.- HB20
  HB15 --- HB16
  HB17 -.- HA21
  HB19 -.- J2
```
