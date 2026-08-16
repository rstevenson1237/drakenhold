<!-- Tier 4 · HA · The Peak 3 warren · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HA_WARREN["HA · The Peak 3 warren"]
    HA15["HA.15 · The Funerary Preparation Rooms"]
    HA16["HA.16 · The Cold Rooms"]
    HA32["HA.32 · The Vent Gallery"]
    HA18["HA.18 · The Runemasters' Service Warren"]
    HA19["HA.19 · The Scholars' Stair"]
    HA31["HA.31 · The Listening Place"]
    HA20["HA.20 · The Tenders' Quarters"]
    HA33["HA.33 · The Wrong Mouth"]
    HA25["HA.25 · The Collapsed Quarter"]
    HA26["HA.26 · The Rerouted Way"]
    HA28["HA.28 · The Older Course"]
    HA30["HA.30 · The Bypass"]
  end

  HA8["HA.8 · The Processional of the Dead"]
  HA10["HA.10 · The Domed Antechamber"]
  HA13["HA.13 · The Cold Run — Peak 3 Terminus"]
  HA14["HA.14 · The Long Run — Peak 3 Stretch"]
  HA17["HA.17 · The Vestries"]
  HC15["HC.15 · The Instruction Rooms"]
  HA23["HA.23 · The Long Watch"]
  HA21["HA.21 · The Survivors' Burials"]
  HA22["HA.22 · The Pocket"]
  HC7["HC.7 · The Bypass Mouth"]

  HA8 --- HA33
  HA10 --- HA15
  HA10 --- HA18
  HA13 --- HA15
  HA14 -.- HA28
  HA15 --- HA16
  HA15 --- HA20
  HA15 --- HA25
  HA16 --- HA32
  HA17 --- HA20
  HA18 --- HA19
  HA19 --- HC15
  HA18 --- HA20
  HA18 --- HA31
  HA18 -.- HA30
  HA20 --- HA23
  HA20 --- HA33
  HA21 --- HA26
  HA22 --- HA26
  HA25 --- HA26
  HA25 -.- HA28
  HA28 -.- HA32
  HA30 -.- HC7
```
