<!-- Tier 4 · FA · The Peak 1 pocket · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FA_POCKET["FA · The Peak 1 pocket"]
    FA27["FA.27 · A Survivor's Cache"]
    FA28["FA.28 · The Buried"]
    FA29["FA.29 · The Watching Place"]
  end

  FA15["FA.15 · The Runners' Ways"]
  FA16["FA.16 · The Long Run — Peak 1 Stretch"]
  FA26["FA.26 · The Bunk Warrens"]

  FA15 --- FA29
  FA16 --- FA29
  FA26 --- FA27
  FA26 --- FA29
  FA27 --- FA28
  FA27 --- FA29
```
