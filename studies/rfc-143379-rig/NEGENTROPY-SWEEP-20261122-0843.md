# NEGENTROPY-SWEEP-20261122-0843

**seat:** copycat lane — the recurring negentropy-sweep ride (cadence 2h, no_agent arm)
**branch:** study/rfc-143379-rig-20261105
**fire time:** 2026-11-22 08:43
**the gate (verbatim):** "the gate: nothing public without the user's word."
**the register:** [1st] = re-read by this lane this pass (git-tree / branch log / read-tool bytes) · [2nd] = carried from a study doc, not re-derived here · ABSENT + named = not received, never invented. Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)
| # | item | state | receipt |
|---|------|-------|---------|
| W2 | W2-isolation settle-condition | NOT-RUN — no isolation ride armed; the windowed items are head/operator-gated | [2nd] 0642 §1 |
| K | k-term two-tier re-measure — baseline kept-rates 0.42/0.29/0.26/0.26 (span 0.26–0.42, FLAT); the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it | NOT-RUN — no re-measure lane this fire | [2nd] 0642 §1 |
| B | budget consolidation re-verify — decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00 | NOT-RUN — carried ordering unchanged | [2nd] 0642 §1 |

All three carried [2nd]; none re-derived (read-gated this pass). The window stays open.

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|------|---------------|---------|
| read-burn harness-deadline | OPEN — the read tool is served from the **scribe cell** (page metadata `source: scribe-cell`); the harness deadline can burn the ride before the cell is warm | IN-LANE (read-tool metadata, this pass) |
| fold check: scribe cell → get_memory byte-compare | NOT CLEAN — the cell's MISSION-MAP (scribe-cell source) ends at the 2026-11-21 ~09:0x row; the wire's committed map blob is 07228046 vs local dcf2077a | IN-LANE |
| fold check: served `?raw=1` grep | NOT-RUN (read-gated) | ABSENT + named |
| token watcher's single-source line | OPEN — ARM-EXECUTE §1 → NEGENTROPY-ARM-EXECUTE-20261119.md; the MISSION-MAP loop-state line 35 + NIGHTSHIFT-PLAN line 83 still name the OLD mission's tokens (STAGE-1-fires / STAGE-3-IN-FLIGHT) | [2nd] 0642 §2 + IN-LANE (map tail) |
| machine-layer wire-checks (scribe tunnel / runners / Harbor / local-LM) | NOT-RUN — read-gated; no ps/runlog ride | ABSENT + named |
| dispositions | HOLD (the watcher rows read "NO DISPATCH — hold, not hold-safe"); AUTO-CONTINUE / NEEDS-THE-CHAIR unused | IN-LANE (map tail) |

## 3. THE ENTROPY CLASSES (CTO freedom)
- **dead surface:** the MISSION-MAP loop-state line (line 35) + NIGHTSHIFT-PLAN-20261118 line 83 still fire the OLD mission's tokens; the new sequence's loop-state lives only in the watcher's log rows. *Countermove:* the head-side's fold rowed the gate-class "fixed at the template" (7ac9b69ea4) — the map's line 35 is the untouched half.
- **loose thread (the prize):** the branch RE-DIVERGED after 0642's "resolved" receipt. local HEAD 506162ced4 (7 head-side commits) vs wire 4d83d62faf (2 watcher commits); merge-base 6c49affd58. 0642's "merge-base = HEAD" is stale. *Countermove:* the watcher's temp-index commit-tree builds on the wire tip and leaves "the head-side's local line … never the watcher's to push" — two parallel lines, neither merged.
- **loose thread:** the root loop-state token `loop-state-0f23bc3b-token.txt` — ABSENT (not in HEAD, not on disk). *Countermove:* the single-source line is the ARM-EXECUTE doc; the root token stays orphan.
- **loose thread:** the gauge's provenance — the watcher asserts "gauge — stage tokens unchanged" but no file names the gauge. *Countermove:* name the gauge source in the next watcher row.
- **friction:** the read path itself lags the wire (scribe cell vs committed map) — the sweep's own evidence plane is the stale surface. *Countermove:* warm the cell from the wire tip before the fold check.
- **UNSPOKEN:** the "phantom-branch class" is no longer phantom — it is a real two-line split, and the head-side's 7 commits (the improver-loop + fold work) are local-only; they reach the wire only if the head-side pushes. The branch's "single source" is fractured by design.

STORM-CONTEXT corroboration (class, never adoption): DISCERN's write-gate L0 = the read-gate this pass (content-reads blocked once the write-window opened) [IN-LANE]; SPA-DREAM's read path = the scribe-cell read tool [IN-LANE]; SELD's read-side evidence-plane verifier = the fold check [IN-LANE]; the four-misc three-state delegation = the AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR dispositions [IN-LANE].

## 4. THE ORDERED NEXT-MOVES
1. **Land this artifact** (the gate). seat: copycat lane.
2. **Reconcile the branch divergence** — push the head-side's 7 commits OR rebase the wire onto them; the watcher's temp-index posture leaves them un-pushed. gate: the branch's single-source line. seat: head-side.
3. **Advance the map's loop-state line 35 + plan line 83** to the new sequence's token. gate: the map's token. seat: head-side.
4. **W2 / k-term / budget** — NEEDS-THE-CHAIR (no lane armed). seat: chair.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. artifact-on-disk — this write; receipt: the path below.
2. sha256 vs banked — the prior sweep's banked shas (0642 §5) carried [2nd]; this artifact's sha lands with the commit.
3. placeholder-scan — 0 hits by construction (no TBD/XXX tokens written).
4. register hand-separation — every row tagged [1st]/[2nd]/ABSENT above.
5. quote-not-assert — the gate quoted verbatim; no paraphrase.
6. the gate — nothing public; artifact-only; upstream QUIET.
7. the loop-state line — §6.
8. commit+push — the terminal receipt.

## 6. THE LOOP-STATE LINE
`CONTINUE + reconcile the branch divergence (push the head-side's 7 local commits onto the wire tip 4d83d62faf, or rebase the wire onto them) and advance the MISSION-MAP loop-state line 35 to the new sequence's token` — receipted: local HEAD 506162ced4, wire 4d83d62faf, merge-base 6c49affd58 [1st].