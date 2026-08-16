<!-- Tier 4 · HB · The royal gallery · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HB_ROYAL["HB · The royal gallery"]
    HB4["HB.4 · The Royal Gallery"]
    HB5["HB.5 · The Empty Interments"]
    HB6["HB.6 · Baldrun Azkelith's Place"]
  end

  HB2["HB.2 · The Tiering"]
  HB7["HB.7 · The Runemaster Gallery"]
  HB9["HB.9 · The Grave-Goods"]
  HB10["HB.10 · The Interment Record"]
  HB13["HB.13 · The Watch That Stayed"]
  HB18["HB.18 · The Thickening"]

  HB2 --- HB4
  HB4 --- HB5
  HB4 --- HB7
  HB4 --- HB9
  HB4 --- HB10
  HB4 --- HB13
  HB4 --- HB18
  HB5 --- HB6
```
