<!-- Tier 4 · FA · The warren · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FA_WARREN["FA · The warren"]
    FA15["FA.15 · The Runners' Ways"]
    FA19["FA.19 · The Scullery Warren"]
    FA20["FA.20 · The Deep Cold Store"]
    FA33["FA.33 · The Vent Gallery"]
    FA21["FA.21 · The Dry-Goods Stores"]
    FA22["FA.22 · Brannek's Tally-Niche"]
    FA25["FA.25 · The Tally Rooms"]
    FA23["FA.23 · The Porters' Quarters"]
    FA24["FA.24 · The Haulers' Yard"]
    FA26["FA.26 · The Bunk Warrens"]
    FA31["FA.31 · The Fallen Run"]
    FA32["FA.32 · The Chute Bottom Access"]
    FA30["FA.30 · The Bypass"]
    FA34["FA.34 · The Old Digging"]
  end

  FA9["FA.9 · The Domed Antechamber"]
  FA13["FA.13 · The Porters' Gate"]
  FA16["FA.16 · The Long Run — Peak 1 Stretch"]
  FA29["FA.29 · The Watching Place"]
  FA27["FA.27 · A Survivor's Cache"]
  FC15["FC.15 · The Bypass Mouth"]
  FB4["FB.4 · Khorven, the Vent Chimney"]

  FA9 --- FA15
  FA13 --- FA15
  FA15 --- FA16
  FA15 --- FA19
  FA15 --- FA21
  FA15 --- FA29
  FA15 --- FA32
  FA16 --- FA23
  FA16 --- FA26
  FA16 -.- FA34
  FA19 --- FA20
  FA20 --- FA33
  FA21 --- FA25
  FA21 -.- FA22
  FA23 --- FA24
  FA24 --- FA25
  FA24 -.- FA34
  FA26 --- FA27
  FA26 --- FA29
  FA26 --- FA31
  FA26 -.- FA30
  FA26 -.- FA34
  FA30 -.- FC15
  FA33 -.- FB4
```
