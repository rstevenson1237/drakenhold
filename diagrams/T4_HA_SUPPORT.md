<!-- Tier 4 · HA · Hall support · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HA_SUPPORT["HA · Hall support"]
    HA11["HA.11 · The Vestry Approaches"]
    HA12["HA.12 · The Vessel Stores"]
    HA17["HA.17 · The Vestries"]
    HA27["HA.27 · The Sealed Vestry"]
  end

  HA10["HA.10 · The Domed Antechamber"]
  HA20["HA.20 · The Tenders' Quarters"]

  HA10 --- HA11
  HA11 --- HA12
  HA11 --- HA17
  HA17 --- HA20
  HA17 --- HA27
```
