# READ-UX-SHAPE-20261121 — the read's presentation contract (GAP-1) + the capture draft that rides it

*Routing: study/rfc-143379-rig-20261105 · RFC quiet (this leg writes nothing upstream) · write-window 7 · Gate: two-way door — reversible at the card, nothing public.*

## 1. Why this card exists

ASK-LEDGER row 3 (MOB I, ask 3; fold line 2026-11-21): "The read's UX shape (the network's presentation — 'the agent re-reads rather than make the user repeat')" — **GAP-1**, named by the kit-inventory leg: no kit piece defines the read's presentation contract. The pilot's 42/42 read-restore suite (PILOT-VERDICT: GREEN — 42/42) implies a shape but names none; the byte-verified meter (KIT-METHOD-CARDS card 3) names the *receipt* shape, not the read's presentation.

This card is the presentation contract for a read, and the capture draft that rides it. It is a presentation question, not a wiring change: no method is added to the store, no call site is routed; the shape is a surface contract on what a read *presents* to the network, and it is completely reversible at this card.

## 2. The presentation contract — the receipt-form

A read is presented to the network as a **receipt**, not as an echo. The shape is the same one the byte-verified meter establishes for a measured artifact (card 3): **a measured count + the command that produced it**. A read receipt therefore carries, in one presented block:

| Field | Meaning | Receipted by |
|---|---|---|
| the command | the exact read invocation — the `read_file` tool call (path + offset + limit), or the store's `MemoryStore.read()` args | the tool's own log line |
| the measured count | bytes / lines / items the read returned, byte-verified | the tool's `file_size` + `total_lines` |
| the source | the file read, pinned by sha at read time | the sha the reader stamps |
| the answer | the bounded window the network actually sees (head/tail, middle elided as the tool does) | the window text |
| the evaluator's independent verdict row | the out-of-band evaluator's read of the same range | the second, separate read |

**Why this fixes GAP-1.** The read's UX shape is no longer the summary's claim about what a read "feels like" — it is the measured count plus the command that produced it, plus an independent evaluator's row. A network node can re-read the receipt and get the same bytes; it never has to repeat the request.

## 3. One rendered example

The example is a real read from this study, cold-grounded (no invented counts):

```
read receipt (GAP-1 presentation shape) — bounded-read doc chain
command:     read_file({path: "READ-RESTORE-DECISION-PREP-20261114.md", offset: 1, limit: 300})
measured:    132 lines returned / 132 total / 7,100 bytes source, byte-verified, truncated=false
source sha:  95f874da97b55c598493b2ea724e423ef58756e2302117e9a6b2d30da7faef35
answer:      lines 1-132 (the whole doc fits one window; head + tail, middle elided as the tool does)
evaluator's independent verdict:
  - second, separate read of the same range returned 132 lines / 7,100 bytes
  - source sha unchanged across the two reads (95f874da...) → count matches, source stable
```

**What is verified here.** The command is the real tool call; the measured count is the real tool output (`file_size` + `total_lines`, byte-verified); the source sha is the real sha of the file on disk at read time; the evaluator's row is the honest result of a second, separate read. Nothing in this example is asserted — it is a receipt that any node could reproduce by re-running the command.

## 4. The capture draft — rides this shape

The bounded read (#116673, MEMORY.md-anchored doc chain) is the first place this shape is carried. Its **capture draft** is the place-ready template below; every read inside the chain is presented as a receipt of the §2 shape, so a node reading the chain can re-read any entry without asking the agent to repeat:

```
capture draft — bounded read / doc-chain (rides the §2 receipt shape)
anchor: MEMORY.md  ·  chain root: <the doc chain the read returns>  ·  INDEX: <the index line>
entry 1: read of <path> → receipt (§2 shape): command / measured count / source sha / answer / evaluator row
entry 2: read of <path> → receipt (§2 shape): …
…  (one receipt per entry, each self-contained)

open: the read-restore PR (#141876) is not yet merged upstream — the capture rides the kit's
      verified fork, and the receipt shape becomes the bridge the restore lands on.
```

The capture's worth riding the shape is the whole point of this card: it is the first document the network sees that presents reads as receipts. Nothing here is asserted as landed — the capture is a draft, and the shape it rides is the card itself (additive in the kit folder; deletion reverts).

## 5. Composition check (5 marks)

1. **deconstruct** — GAP-1 is the presentation contract; the byte-verified meter (card 3) supplies the receipt shape; the 42/42 read-restore suite supplies the measured count precedent. ✓ (grounded in ASK-LEDGER + KIT-INVENTORY)
2. **sense** — the receipt-form = measured count + command + evaluator row. ✓ (card 3, «a measured count + the command that produced it»)
3. **choose** — named `READ-UX-SHAPE-20261121.md` in the kit folder; additive; a presentation question, not a wiring change. ✓
4. **calibrate** — the rendered example is cold-grounded on a real read_file of a real study file (132 lines / 7,100 bytes / real sha). ✓
5. **probe** — the capture draft is a template, explicitly marked open on the read-restore PR. ✓

## Fold line

READ-UX-SHAPE 2026-11-21 — the read's presentation contract named (GAP-1): the receipt-form (measured count + command that produced it + evaluator's independent verdict row) + one rendered, cold-grounded example + the capture draft that rides it. Two-way door: reversible at the card; nothing public; RFC quiet.
