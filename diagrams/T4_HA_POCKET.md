<!-- Tier 4 · HA · The Peak 3 pocket · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HA_POCKET["HA · The Peak 3 pocket"]
    HA21["HA.21 · The Survivors' Burials"]
    HA22["HA.22 · The Pocket"]
    HA23["HA.23 · The Long Watch"]
    HA24["HA.24 · What They Took Down"]
    HA29["HA.29 · The Crypt Access"]
  end

  HA20["HA.20 · The Tenders' Quarters"]
  HA26["HA.26 · The Rerouted Way"]
  HB17["HB.17 · The Survivors' Burials"]
  HB3["HB.3 · The Crypt Access"]

  HA20 --- HA23
  HA21 --- HA26
  HA21 --- HA29
  HA21 -.- HB17
  HA22 --- HA23
  HA22 --- HA24
  HA22 --- HA26
  HA29 -.- HB3
```
