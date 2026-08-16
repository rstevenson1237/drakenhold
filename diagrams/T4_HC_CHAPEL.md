<!-- Tier 4 · HC · The chapel · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HC_CHAPEL["HC · The chapel"]
    HC1["HC.1 · The Ramp Head"]
    HC2["HC.2 · The Chapel Proper"]
    HC3["HC.3 · The Sigil Walls"]
    HC4["HC.4 · Vekkut"]
    HC5["HC.5 · What He Carried Up"]
    HC6["HC.6 · The Loyalists' Camp"]
    HC7["HC.7 · The Bypass Mouth"]
    HC14["HC.14 · The Vestry"]
    HC16["HC.16 · The Refectory"]
  end

  HA10["HA.10 · The Domed Antechamber"]
  HD1["HD.1 · The Ramp Head"]
  HC8["HC.8 · The Cells"]
  HC10["HC.10 · The Copied Wall"]
  HC9["HC.9 · The Listening Cell"]
  HC12["HC.12 · The Excavation Face"]
  HC20["HC.20 · What He Saw Coming Up"]
  HA30["HA.30 · The Bypass"]

  HC1 --- HA10
  HC1 --- HD1
  HC1 --- HC2
  HC2 --- HC3
  HC2 --- HC4
  HC2 --- HC6
  HC2 --- HC8
  HC2 --- HC14
  HC2 --- HC16
  HC3 --- HC10
  HC4 --- HC5
  HC4 --- HC9
  HC4 --- HC12
  HC4 --- HC20
  HC6 --- HC12
  HC6 --- HC16
  HC7 -.- HA30
  HC7 --- HC8
  HC16 --- HC20
```
