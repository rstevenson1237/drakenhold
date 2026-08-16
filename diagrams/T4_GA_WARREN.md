<!-- Tier 4 · GA · The Peak 2 warren · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GA_WARREN["GA · The Peak 2 warren"]
    GA9["GA.9 · The Clerks' Warrens"]
    GA14["GA.14 · The Record Stores"]
    GA21["GA.21 · A Clerk's Private Cache"]
    GA15["GA.15 · The Court Staff Quarters"]
    GA16["GA.16 · The Holding Rooms"]
    GA17["GA.17 · The Armoury Support"]
    GA24["GA.24 · The Court Vent Gallery"]
    GA22["GA.22 · The Capillary Maze"]
    GA23["GA.23 · The Blocked Run"]
    GA25["GA.25 · The Older Course"]
    GA26["GA.26 · The Bypass"]
    GA27["GA.27 · The Wrong Mouth"]
    GA12["GA.12 · The Ash Run — Peak 2 Terminus"]
    GA13["GA.13 · The Cold Run Head"]
  end

  GA6["GA.6 · The Domed Antechamber"]
  GA7["GA.7 · The Writ-Rooms"]
  GA8["GA.8 · The Holding Approach"]
  GA11["GA.11 · The Second Seal"]
  FA18["FA.18 · The Ash Run Head"]
  HA13["HA.13 · The Cold Run — Peak 3 Terminus"]
  GB5["GB.5 · The Armoury"]
  GA18["GA.18 · The Watchers' Nest"]
  GC7["GC.7 · The Bypass Mouth"]
  GE9["GE.9 · The Servants' Way"]
  GA5["GA.5 · The Monument of the Driving Down"]

  GA6 --- GA9
  GA7 --- GA9
  GA8 --- GA16
  GA9 --- GA14
  GA9 --- GA15
  GA9 --- GA22
  GA11 -.- GA25
  GA12 --- FA18
  GA12 --- GA22
  GA13 --- GA22
  GA13 --- HA13
  GA14 -.- GA21
  GA14 -.- GA25
  GA15 --- GA16
  GA16 --- GA17
  GA17 --- GA22
  GA17 --- GA24
  GA17 --- GB5
  GA18 -.- GA22
  GA22 --- GA23
  GA22 --- GA27
  GA22 -.- GA25
  GA22 -.- GA26
  GA26 -.- GC7
  GA22 -.- GE9
  GA27 --> GA5
```
