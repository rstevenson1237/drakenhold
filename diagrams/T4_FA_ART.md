<!-- Tier 4 · FA · The arteries · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FA_ART["FA · The arteries"]
    FA16["FA.16 · The Long Run — Peak 1 Stretch"]
    FA17["FA.17 · The Seal"]
    FA18["FA.18 · The Ash Run Head"]
  end

  FA9["FA.9 · The Domed Antechamber"]
  FA15["FA.15 · The Runners' Ways"]
  FA23["FA.23 · The Porters' Quarters"]
  FA26["FA.26 · The Bunk Warrens"]
  FA29["FA.29 · The Watching Place"]
  FA34["FA.34 · The Old Digging"]
  GA10["GA.10 · The Long Run — Peak 2 Stretch"]
  GA12["GA.12 · The Ash Run — Peak 2 Terminus"]

  FA9 --- FA16
  FA15 --- FA16
  FA16 --- FA17
  FA16 --- FA18
  FA16 --- FA23
  FA16 --- FA26
  FA16 --- FA29
  FA16 -.- FA34
  FA17 -.- GA10
  FA18 --- GA12
```
