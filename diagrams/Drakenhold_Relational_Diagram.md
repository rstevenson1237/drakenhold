# DRAKENHOLD — SETTING RELATIONAL DIAGRAM

*Procedure step 6. Companion to the Setting Outline and the region files. One overview graph of the whole setting, then one detail graph per grouping. Diagrams are authoritative: the Connections section in each region file is checked against them.*

---

## EDGE VOCABULARY

Not a closed list. New types are proposed and added here rather than coined in passing.

| Type | Mermaid style | Meaning |
|---|---|---|
| open | solid line, plain label | Walk it. No key, no climb, no trick. |
| gated by tile | solid line, `[tile]` | A whole carved stone tile in a matching receptacle grants passage. |
| gated by rod | solid line, `[rod]` | A runed metal rod of the stated tier makes the mechanism act. |
| hidden | dashed line, `[hidden]` | Physically there and unmarked. Found by searching the right place. |
| secret | dashed line, `[secret]` | Concealed on purpose, and knowing it exists is itself a discovery. |
| vertical | any line, `[vert]` | Climb, fall, ramp or shaft. Movement costs and encumbrance bite. |
| one-way | arrow, single-headed | Passable in the stated direction only. |
| conditional — mechanism | dotted line, `[mech]` | Opens only once something is restored, relit or re-sequenced. |
| conditional — faction | dotted line, `[faction]` | Opens only at a stated relation level, or by toll, escort or bargain. |
| conditional — size | dotted line, `[size]` | Passable only by the small, the unarmoured or the desperate. |

---

## 1. OVERVIEW — THE SETTING ENTIRE

Groupings rather than every edge. The four detail graphs below resolve each box.

```mermaid
graph TD
    subgraph APPROACH
        A["A · Thornhaven<br/>SAFE d6"]
        B["B · Ironwood Trail<br/>WILD d10"]
        C["C · Goblin Camps<br/>WILD d6"]
        D["D · River Crossing<br/>WILD d8"]
        E["E · Girkel, Outer City<br/>WILD d8"]
    end

    subgraph PEAKS
        F["PEAK 1 · F<br/>Trade and Craft<br/>FA FB FC FD FE"]
        G["PEAK 2 · G<br/>Authority and the Dragon<br/>GA GB GC GD GE"]
        H["PEAK 3 · H<br/>Spirit and the Dead<br/>HA HB HC HD HE"]
    end

    S["S · Servants' Passages<br/>within FA / GA / HA"]
    I["I · Brynaz, the Skybridge<br/>WILD d6"]
    J["J · Mordrak, the Lost Caverns<br/>WILD d8"]

    A ---|open| B
    B ---|open| C
    B ---|open| D
    D ---|"open · toll · faction"| E
    E ==>|"open · the broken doors"| F

    F ---|"open · Processional of the Living"| G
    G ---|"open · Processional of the Dead"| H

    F --- S
    G --- S
    H --- S

    F -.-|"tile · FD terminus"| I
    G -.-|"tile · GD terminus"| I
    H -.-|"tile · HD terminus"| I

    F -.-|vert| J
    G -.-|vert| J
    H -.-|vert| J

    I -.->|"one-way · the crater"| G
```

**Reading it.** Everything above the peaks is the road in, and it is a single chain with one branch. Everything below and around them is the answer to a locked door: the Skybridge is the horizontal cheat, the servants' passages are the lateral one, and the Lost Caverns are the vertical one. **FA is the only opening to the outside world.** Every other way in — the Skybridge termini, the crater, the hidden descents — is a way *out* first, discovered from inside, and only becomes an entrance on a second visit.

---

## 2. DETAIL — THE APPROACH

```mermaid
graph LR
    A["A · Thornhaven"]
    WF["Wyla Fenn's grove"]
    FS["The haunted farmstead"]
    B["B · Ironwood Trail"]
    WS["Three waystones"]
    CU["The silted culvert"]
    WY["Collapsed waystation"]
    C["C · Goblin Camps"]
    OB["The owlbear's den"]
    D["D · River Crossing"]
    OV["Overlook and outpost"]
    BR["The bridge · far booth"]
    E["E · Girkel, Outer City"]
    FA["FA · Takdun"]

    A ---|"open · one hour"| WF
    A ---|"open · half that"| FS
    A ---|open| B
    B --- WS
    B --- CU
    B -.-|hidden| WY
    B ---|"open · off the trail"| C
    C ---|"open · west of all three"| OB
    B ---|open| D
    D --- OV
    D --- BR
    BR ---|"faction · toll or blood"| E
    E ==>|"open · the great doors, broken"| FA
```

*Held for the location pass on B: the culverted dwarven drain, and the waystones' two unheard-of destinations. The drain's far end is likeliest to surface on the near bank at D rather than at E — the Outer City is a long way off and the river lies between.*

---

## 3. DETAIL — PEAK 1 (F), TRADE AND CRAFT

```mermaid
graph TD
    E["E · Girkel"]
    FA["FA · Takdun<br/>Main · DANGEROUS d10"]
    FB["FB · Brankel<br/>Under · WILD d8"]
    FC["FC · Mekdun<br/>L2 · DANGEROUS d10"]
    FD["FD · Khorvak<br/>L3 · DANGEROUS d10"]
    FE["FE · Aztak<br/>L4 · DANGEROUS d8"]
    S["S · Servants' Passages"]
    I["I · Skybridge"]
    J["J · Lost Caverns"]
    GA["GA · Grathdun"]

    E ==>|"open · the broken doors"| FA
    FA ---|"open · Processional of the Living"| GA
    FA ---|"open · mouths at the antechamber"| S
    FA ---|"vert · stairwell down"| FB
    FA ---|"vert · the great ramp"| FC
    FA -.->|"hidden · vert · kitchen service chute"| FB
    FC ---|"vert · the great ramp"| FD
    FD ---|"vert · the great ramp"| FE
    FB -.-|"vert · size · the vent chimney"| FD
    FC -.-|"mech · vert · chute dispatch"| FB
    FC -.-|"mech · vert · chute dispatch"| FD
    FD -.-|"tile · western terminus"| I
    FE -.-|"mech · vert · an intact run, approach lost"| I
    FB -.-|"vert · size · chimney, marked descent"| J
    FD -.-|"secret · vert · a magma channel"| J
    S -.-|"secret · bypasses a gate above"| FC
```

**Notes.** The dispatch floor on FC is the level's puzzle and also its map: correct sequencing opens a hidden access that appears on no plan, and wrong sequencing strands a party between FB and FD. The chimney is the peak's spine — it is the only thing touching the Under Level, Level 3 and the caverns at once, and it is the flow that relighting the forge depends on.

---

## 4. DETAIL — PEAK 2 (G), AUTHORITY AND THE DRAGON

```mermaid
graph TD
    FA["FA · Takdun"]
    GA["GA · Grathdun<br/>Main · DANGEROUS d10"]
    GB["GB · Karmor<br/>Under · DANGEROUS d10"]
    GC["GC · Azdun<br/>L2 · DANGEROUS d8"]
    GD["GD · Valdmor<br/>L3 · DANGEROUS d8"]
    GE["GE · Azith<br/>L4 · DANGEROUS d4"]
    DC["GB deep cells<br/>separately gated"]
    S["S · Servants' Passages"]
    I["I · Skybridge"]
    J["J · Lost Caverns"]
    HA["HA · Thaldun"]

    FA ---|"open · Processional of the Living"| GA
    GA ---|"open · Processional of the Dead"| HA
    GA ---|"open · mouths at the antechamber"| S
    GA ---|"vert · stairwell down"| GB
    GA ---|"vert · the great ramp"| GC
    GC ---|"vert · the great ramp"| GD
    GD ---|"vert · the great ramp"| GE
    GB -.-|"rod · secret · hidden and separately gated"| DC
    GD -.-|"tile · faction · central terminus"| I
    GD -.-|"mech · vert · an intact run, past the checkpoint"| I
    I -.->|"one-way · vert · down through the crater"| GE
    S -.-|"secret · into the corridor, past the crater"| GE
    GB -.-|"vert · marked descent"| J
    DC -.-|"secret · vert"| J
```

**Notes.** The direct horizontal route between peaks runs through the dragon's counting house, and the counting house is held by people who assess before they reach. That is the design. GC's balcony has no Skybridge access and is drawn with none. The crater is the one place the outside gets in, and it gets in on top of the dragon — the edge is one-way for a reason.

*Ratified this pass: the deep cells descend into J. It is how the Elder Wyrm came up, it is how the Runemasters learned the yoke without hauling their subject the length of the marked descent, and it is why the mad Runemaster has had something to listen to for thirty-two years.*

---

## 5. DETAIL — PEAK 3 (H), SPIRIT AND THE DEAD

```mermaid
graph TD
    GA["GA · Grathdun"]
    HA["HA · Thaldun<br/>Main · DANGEROUS d8"]
    HB["HB · Nurmor<br/>Under · DANGEROUS d6"]
    HC["HC · Sigdun<br/>L2 · DANGEROUS d8"]
    HD["HD · Zarkel<br/>L3 · DANGEROUS d6"]
    HE["HE · Sigaz<br/>L4 · DANGEROUS d4"]
    OR["HD observation rooms<br/>heavily gated"]
    NI["HB · the niche<br/>Torvin Ganthur, the lance"]
    S["S · Servants' Passages"]
    I["I · Skybridge"]
    J["J · Lost Caverns"]

    GA ---|"open · Processional of the Dead"| HA
    HA ---|"open · mouths at the antechamber"| S
    HA ---|"vert · stairwell down"| HB
    HA ---|"vert · the great ramp"| HC
    HC ---|"vert · the great ramp"| HD
    HD ---|"vert · the great ramp"| HE
    HB -.-|"secret · the name is the key"| NI
    HC -.->|"mech · vert · the excavation, unfinished"| HD
    HD ---|"rod · Runemaster tier, or the circuit run honestly"| OR
    OR -.-|"secret · does not use the ramp"| HE
    HD -.-|"tile · eastern terminus"| I
    HB -.-|"vert · marked descent"| J
    S -.-|"hidden · the survivors' own burials"| HB
```

**Notes.** Peak 3 is the only peak whose internal routes are all earned rather than walked. The circuit can be run honestly for a rod or cheated from the observation rooms, and the shortcut costs more than the road. The kobold chieftain's excavation is a live edge that completes on a clock whether or not the party touches it — accelerating, redirecting or collapsing it are three different campaigns, and one of them hands HE to something that cannot read what it finds.

---

## 6. DETAIL — THE THREE ANSWERS

The Skybridge, the servants' passages and the Lost Caverns exist so that no gate is final. Each answers a different axis.

```mermaid
graph TD
    subgraph HORIZONTAL["I · Brynaz — the Skybridge (open air, exposure, weather)"]
        FD2["FD"] -.-|tile| SPAN["The great span"]
        SPAN -.-|"tile · faction"| GD2["GD"]
        SPAN -.-|tile| HD2["HD"]
        SPAN --- RUNS["Vertical runs, ladder-stairs,<br/>observation posts, attack points"]
        RUNS -.->|"one-way · the crater"| GE2["GE"]
        RUNS -.-|"mech · intact, no approach left"| FE2["FE · Aztak<br/>otherwise a single-entrance cul-de-sac"]
        RUNS -.-|"mech · intact, no approach left"| GD3["GD · Valdmor<br/>arrives past the checkpoint"]
    end

    subgraph LATERAL["S · Servants' Passages (within FA / GA / HA)"]
        SF["Peak 1 zone<br/>kitchens, stores, porters"]
        SG["Peak 2 zone<br/>clerks, court staff, holding"]
        SH["Peak 3 zone<br/>funerary, vestries, Runemaster service"]
        SF ---|"open · a main run"| SG
        SG ---|"open · a main run"| SH
        SF -.-|"secret · bypasses a gate above"| FC2["FC"]
        SG -.-|secret| GE3["GE"]
        SH -.-|hidden| HB2["HB"]
    end

    subgraph VERTICAL["J · Mordrak — the Lost Caverns (the great tunnel)"]
        TUN["The great tunnel<br/>beneath F, G and H"]
        TUN --- T1["Flooded galleries"]
        TUN --- T2["Exhausted workings"]
        TUN --- T3["Natural cavern"]
        TUN --- T4["The vent system"]
        TUN --- T5["The vein"]
        TUN --- T6["The deep dark"]
        TUN -.-|"vert · marked"| FB2["FB"]
        TUN -.-|"vert · marked"| GB2["GB"]
        TUN -.-|"vert · marked"| HB2b["HB"]
        TUN -.-|"vert · size · hidden"| FB3["FB chimney"]
        TUN -.-|"vert · secret"| FD3["FD channel"]
        TUN -.-|"vert · secret"| DC2["GB deep cells"]
        T4 -.-|mech| FD4["FD forge flow"]
    end
```

**The rule the three encode.** Every gate in Drakenhold has at least one answer that is not the gate. A party that cannot pay the Lizardmen's toll can go under the mountain or over it; a party that cannot open a Royal lock can come at the room from a direction the room was never defended against. The cost is always the same shape — the alternate route is longer, darker, or watched by something worse.

---

## AUDIT

Checked against the Gazetteer this pass:

- **FA is the sole exterior entrance.** GA and HA have none; E connects only to FA. Held.
- **GC has no Skybridge access.** The balcony is a nobles' balcony. Held, and drawn with no edge to I.
- **One ramp up, one stairwell down between peak levels.** Held. All additional vertical edges are chutes, chimneys, channels or excavations, and each is typed.
- **The servants' passages interconnect all three peaks.** Placed as edges SF–SG–SH, and as the second internal cross-connection alongside the Processionals.
- **Six previously unwritten routes placed:** FB chimney to FD and to J; FD channel to J; HD observation rooms to HE; servants' route into GE past the crater; hidden descents into J from each peak.
- **The two orphaned Skybridge runs are placed:** one into FE, which is otherwise reachable only by the FD ramp, and one into GD, which arrives inside the vaults without passing the Lizardman checkpoint. Both are intact and both have lost their approach; restoring either is a mechanism problem and each is a major prize.
- **Ratified this pass:** the deep cells descend into J; the yoke was learned in GB from the Elder Wyrm still in the building; the wyrms below and the Drakmorith above are the same story told from two ends.
- **Graph legibility.** The overview will not stay readable as routes accumulate, and sub-region nodes (S, the deep cells, the observation rooms, the niche) are carried deliberately rather than pruned. Held as-is to preserve detail; the overview collapses to a simpler shape once the per-region diagrams exist to hold the specifics.
- **HE has no edge except from HD.** The dragon never came, nothing has been carried out in thirty-two years, and the only ways in are the ramp and the observation-room route. This is deliberate and is why HE pays what it pays.
