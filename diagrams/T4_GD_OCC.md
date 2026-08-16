<!-- Tier 4 · GD · The occupation · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GD_OCC["GD · The occupation"]
    GD11["GD.11 · The Lizardman Quarters"]
    GD13["GD.13 · The Fallback"]
  end

  GD7["GD.7 · The Weighing Floor"]

  GD7 --- GD11
  GD11 --- GD13
```
