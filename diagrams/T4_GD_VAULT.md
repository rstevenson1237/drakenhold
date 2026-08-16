<!-- Tier 4 · GD · The sundered vault · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GD_VAULT["GD · The sundered vault"]
    GD3["GD.3 · The Sundered Vault"]
    GD4["GD.4 · The Working Hoard"]
    GD12["GD.12 · The Orphaned Run"]
    GD8["GD.8 · The First Sub-Vault"]
    GD9["GD.9 · The Second Sub-Vault"]
    GD10["GD.10 · The Third Sub-Vault"]
  end

  GD1["GD.1 · The Ramp Checkpoint"]
  GD7["GD.7 · The Weighing Floor"]
  I14["I.14 · The GD Run"]

  GD1 --- GD3
  GD3 --- GD4
  GD3 --- GD7
  GD3 --- GD8
  GD3 --- GD9
  GD3 --- GD10
  GD3 --- GD12
  GD12 -.- I14
```
