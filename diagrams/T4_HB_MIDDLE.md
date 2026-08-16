<!-- Tier 4 · HB · The Runemaster and guild galleries · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HB_MIDDLE["HB · The Runemaster and guild galleries"]
    HB7["HB.7 · The Runemaster Gallery"]
    HB8["HB.8 · The Guild Gallery"]
    HB9["HB.9 · The Grave-Goods"]
    HB18["HB.18 · The Thickening"]
  end

  HB4["HB.4 · The Royal Gallery"]
  HB11["HB.11 · The Guard Gallery"]

  HB4 --- HB7
  HB4 --- HB9
  HB4 --- HB18
  HB7 --- HB8
  HB7 --- HB9
  HB7 --- HB18
  HB8 --- HB9
  HB8 --- HB11
  HB8 --- HB18
  HB9 --- HB11
  HB11 --- HB18
```
