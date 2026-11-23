# LANE-BA AUDIT — CROSS-AUDIT BRIEF 1 (the canary phase-1 skeleton)

**Artifact under test:** `studies/rfc-143379-rig/plan/tank/lane-b-phase1-design-20261121.md` — sha256 `5d4015f20de2475845a914b238394ddd9380a7796bfaa8e76f17e7e54ea077d4`, 214 lines, read cold in full.
**Ground (read cold, in full):** `master-page/study-archive-20261120/CANARY-CELLS-20261120.json` (sha256 `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2`; byte-identical to `studies/rfc-143379-rig/probes/CANARY-CELLS-20261120.json`) · `master-page/study-archive-20261120/OPUS-NM3-CANARY-20261120.md` · `studies/rfc-143379-rig/PILOT-VERDICT-20261121.md` · `studies/rfc-143379-rig/night-20261121/FINAL-LEG-PLAN-20261121.md` (arms 3 + 6) · `studies/rfc-143379-rig/KIT-METHOD-CARDS-20261121.md`.
**Seat:** `meituan/longcat-2.5:free` @ `p0tat0` · **Branch:** `study/rfc-143379-rig-20261105` · **RFC:** quiet · **Hard lines held:** nothing public · no installs · local reads only · write only under the study.
**Method:** re-derive every claimed gate/number against the cell ledger; the wall clause — a non-reproduction is a **QUESTION**, never a defect.

---

## VERDICT: **DEFECTS-NAMED**

The skeleton is runnable, measured, revertible, egress-disciplined and judgment-layer-equipped **in substance**: all eight gates' cell-derived numbers re-derive **exactly**; the fifteen items are named; the ten revert points are real, each with a trigger and a mechanism; the judgment layer F1–F5 is consistent with `PILOT-VERDICT-20261121.md` and `FINAL-LEG-PLAN-20261121.md`. **Seven defects are named** — none fatal, all revertible/additive. The two that matter: the egress section asserts a **false byte equality** (D1), and the fail-safe grid names **gates G9–G15 that the brief never defines** (D2).

---

## 1 · RECEIPTS — every claimed gate/number re-derived from the cell ledger

Command receipts (this host, read-only):

```
$ sha256sum probes/CANARY-CELLS-20261120.json \
           /root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json
25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2  probes/CANARY-CELLS-20261120.json
25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2  /root/workspace/master-page/.../CANARY-CELLS-20261120.json
$ sha256sum plan/tank/lane-b-phase1-design-20261121.md
5d4015f20de2475845a914b238394ddd9380a7796bfaa8e76f17e7e54ea077d4  plan/tank/lane-b-phase1-design-20261121.md
```

| Gate | Artifact claim | Cell field (ground) | Cell value | Re-derived | Status |
|---|---|---|---|---|---|
| G1 | pin `fc8b9934…`; safetensors `5747a90e…`; bytes `641,262,336` | `pinned_repo_sha`, `model_safetensors_sha256`, `model_bytes` | `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` · `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c` · `641262336` | exact | **PASS** |
| G2 | load `0.95s`; params `319,028,736`; logits `[1,4,129280]`; argmax `49969`; max diff `0.0` < `1e-6` | `load_seconds`, `param_count`, `logits_shape`, `argmax_next_token`, `deterministic_max_abs_diff`, `determinism_tolerance` | `0.95` · `319028736` · `[1,4,129280]` · `49969` · `0.0` · `1e-06` | exact; `0.0 < 1e-6` → `deterministic_within_tolerance=true` | **PASS** |
| G3 | MIT verified live; `license_compatible_private_repo=true` | `license`, `license_compatible_private_repo` | `"MIT (verified live from the HF model card: license: mit; …)"` · `true` | exact | **PASS** |
| G4 | sole route `nm3-canary-r1-20261120`; bytes `647,716,330`; secondary `0` | `egress_route`, `egress_bytes`, `egress_secondary_downloads` | `"private repo release nm3-canary-r1-20261120 (sole route)"` · `647716330` · `0` | exact | **PASS** |
| G5 | `tmpfs-venv@PVE-host` (kernel `7.0.14-16-pve`); boundary named | `sandbox_env_id` | `"tmpfs-venv@PVE-host (kernel 7.0.14-16-pve); isolation boundary: ephemeral venv in /tmp (RAM-backed, reboot-pruned), model files pulled ONLY via the private-release route; no rig disk state touched; no production seat; no HF download in the sandbox"` | verbatim | **PASS (assertion)** — see Q1 |
| G6 | record-first five gate fields; mapping unchanged on re-read | cell record-first clause + `OPUS §2(1)` + `OPUS §7` | — | gate substance traceable; **anchor defective** | **PASS / anchor re-mapped** — D3 |
| G7 | **R1 LANDED** (receipt complete; rung-2 armed) | `OPUS §4` (Verdict) + `OPUS §6` (review-loop) | "Verdict: **R1 LANDED** (receipt complete). Rung-2 conditions ARMED" | traceable | **PASS** (phrase seam D6) |
| G8 | compose-check 8 marks, all FIRED, mark 2 via proxy | `OPUS §5` | M1–M8 all FIRED; "All 8 marks FIRED (mark 2 via proxy)" | exact | **PASS** |

**Items 1–15 traceability.** Items 1–8 trace exactly to the cell fields above. Items 9–12 trace to `KIT-METHOD-CARDS-20261121.md` card first-uses (card 1 → the pilot verdict; card 2 → the ACES trigger; card 3 → the court-verification spine's execution ledger; card 4 → the night-shift plan's gates) — all four named, none invented. Item 13's **receipt anchor is mis-named** (D4). Items 14–15 are OPEN and correctly named as open. Item 15's "five gate fields" is a numbering conflation (D7).

**Revert points R1–R10 — re-verified directly against the artifact's own §3 table** (not against any summary):

| # | Gate | Trigger (artifact) | Mechanism (artifact) | Real? |
|---|---|---|---|---|
| R1 | Cell install | sha mismatch, or load fails | sandbox torn down; install additive, deleted on revert | ✓ |
| R2 | Model load | `load_seconds` above barrier, or params ≠ `319,028,736` | load is a probe; forward never runs on a bad install | ✓ |
| R3 | Determinism | max abs diff ≥ `1e-6` | run recorded as probe, never a verdict; never burns rung-2 | ✓ |
| R4 | License | `license_compatible_private_repo` false | release route untouched | ✓ |
| R5 | Egress | `egress_secondary_downloads > 0` | one-way store; a second download aborts | ✓ |
| R6 | Isolation | envelope contract not verifiable | boundary named and checked at run time | ✓ |
| R7 | Gate-state file | any gate fails | file additive + revisioned; last PASS revision is the rollback | ✓ |
| R8 | Capture home | the fold lands the file | fold additive | ✓ (naming D4) |
| R9 | Judge-gate re-reads | a re-read shows drift | evaluator's verdict row carries the independent read | ✓ |
| R10 | ACES trigger | the loop fires | termination receipted twice over | ✓ |

All ten are named with a trigger and a mechanism; none is a bare "failed". The revert rule ("a failed gate freezes the run's verdict row at PARTIAL / GAP and re-arms the same item at the next ring — never a silent skip, never a re-run with different values") is a real two-way door.

**Egress disposition §4.** Rules 1, 3, 5 trace to `egress_route` / `sandbox_env_id`; rule 4's reference is the cell; rule 6 is the evaluator schedule. **Rule 2 is defective (D1).** The sole-route discipline itself is held: one store, byte-counted, secondary `0`.

**Judgment layer F1–F5.** F1's vocabulary (LANDED/PARTIAL/GAP/QUESTION/REVERTED/CLOSED) is a gate-state vocabulary consistent with `PILOT-VERDICT` ("a GATE STATE, not an identity"). F2's schedule (per-ring re-read, per-landing independent row, before-any-claim receipt, 6 h ACES) is consistent with `FINAL-LEG-PLAN` THE CRONS + THE ACES-TRIGGER. F3's no-gate doctrine matches `PILOT-VERDICT` THE TWO-WAY DOOR. F4's grid is **defective (D2)**. F5's receipt stamp matches card 1.

---

## 2 · DEFECTS NAMED (each with receipt + fix; all revertible/additive)

| # | Where | Defect | Receipt | Fix |
|---|---|---|---|---|
| **D1** | §4 rule 2 (line 103) | Asserts `egress_bytes` = the model's bytes (`647,716,330`). **False equality**: cell `model_bytes` = `641,262,336`; `egress_bytes` = `647,716,330`; delta = **6,453,994 bytes**. | cell lines 8 + 27 | State `egress_bytes` = the **release's** byte count; record the delta as release-over-model overhead. The cell stays the reference. |
| **D2** | §5 F4 (lines 156–157) | The fail-safe grid names **G9–G12 (cards)** and **G13–G15 (continuity)**. The brief defines **only G1–G8** (§2). Gates G9–G15 do not exist. | artifact §2 gate table (G1–G8 only) | Map the grid rows to the artifact's **items 9–15**, or define G9–G15 explicitly. Grid rows must reference gates that exist. |
| **D3** | §2 G6 receipt (line 69) | Anchor `PILOT-VERDICT-20261121.md §2` — that file has **no numbered §2**; its headings are unnumbered (THE VERDICT / THE EVIDENCE TOWER / THE START LINE / THE TWO-WAY DOOR). | `PILOT-VERDICT-20261121.md` headings | Re-anchor G6 to the cell's own record-first wall clause + `OPUS §2(1)` + `OPUS §7`. Gate substance unchanged. |
| **D4** | §0 line 12 · item 13 · R8 | "the kit folder: the four cards + the audit + the sceptic". The cards + audit + sceptic sit at the **study root** (`KIT-METHOD-CARDS-20261121.md`, `KIT-AUDIT-20261107.md`, `KIT-SKEPTIC-20261107.md`); `kit/` holds only `RELEASE-CONDITION-20261121.md` + `READ-UX-SHAPE-20261121.md`. | `ls kit/` + `ls KIT-*.md` on the branch | Rename to "the study root's kit cards + audit + sceptic"; keep `kit/` as the capture home. Additive rename, no verdict change. |
| **D5** | item 9 (line 48) | Card 1 marked **RUNNING**, but card 1's first use is the pilot verdict — which **already landed** (`PILOT-VERDICT-20261121.md` exists; card 1 names it "the canonical instance"). | `KIT-METHOD-CARDS-20261121.md` card 1 | Mark card 1 **FIRED** (first use landed); the canary's own first certified use is the RUNNING part. |
| **D6** | §2 G7 (line 70) | "Verdict row at the named commit" — `OPUS §4`/`§6` name **no commit**. The phrase is borrowed from `FINAL-LEG-PLAN` ARM 1's gate. | `OPUS §4` + `§6` | Drop "at the named commit" or name the commit. Substance (R1 LANDED) unchanged. |
| **D7** | §5 F2 (line 136) | "the five gate fields (G1–G5)" conflates the **cell's** five fields with the artifact's gate numbers. The cell's field (1) is the sandbox envelope = artifact **G5**; the mapping is a permutation, not an identity. | `OPUS §2` five fields vs artifact §2 G1–G5 | Say "the cell's five gate fields" and give the mapping (cell 2→G1, 3→G2, 4→G3, 5→G4, 1→G5). |

**No defect found in:** the cell-derived numbers (all exact), the item list's coverage, the revert points' reality, the egress sole-route discipline, or the judgment layer's consistency with the pilot verdict.

---

## 3 · EXTENSIONS — new continuation points (each named, measured, revertible)

**EXT-1 · Gate-state file schema (items 13/14, OPEN).** Draft the operator's read surface so the first landing is nameable. The schema must carry a **dual sha anchor**, because the cell's internal `cells_sha256` (`f1ed5b0db75d8d91…`) is the **pre-addendum** hash the lane read, while the post-addendum file's actual sha is `25606ba915710df2…` (`OPUS §7`):

```json
{ "kit": "canary-phase1", "version": 1, "ring": 1,
  "started_at": "…", "ended_at": "…",
  "cells": { "internal_cells_sha256": "f1ed5b0db75d8d91…",
             "file_sha256": "25606ba915710df2…",
             "env": { "sandbox_env_id": "tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)",
                      "added_utc": "2026-11-20T04:45:00Z" } },
  "items": [ { "id": 1, "state": "FIRED", "measured": {}, "receipt": { "artifact": "…", "sha": "…", "cmd": "…" } } ],
  "verdict_rows": [ { "ring": 1, "state": "LANDED", "measured": {}, "revision": 1 } ],
  "drifts": [ { "gate": "G1", "field": "model_bytes", "cell_value": 641262336, "brief_value": 641262336, "delta": 0, "ts": "…" } ],
  "closed": [] }
```

**Measured:** the row shape derives from the artifact's §1/§2 tables + the cell ledger; the dual anchor is the `OPUS §7` receipt. **Reverted:** additive; the last PASS revision is frozen per R7; the draft lives in this audit, never in the verdict row.

**EXT-2 · Egress equality repair + run-time re-receipt (§4 rule 2 / thread 6).** The pilot's egress receipt must record **both** counts and their delta, and must never assert the false equality:

```
model_bytes   == cell model_bytes            (641,262,336)
egress_bytes  == cell egress_bytes           (647,716,330)
delta         = egress_bytes - model_bytes   (6,453,994)   # release-over-model overhead
egress_secondary_downloads == 0
```

**Measured:** the pilot re-derives sha256 + byte counts from the pulled file; the cell is the immutable reference. **Reverted:** additive receipt row; a mismatch rewrites G4 to PARTIAL and stops the ring (R5).

**EXT-3 · Fail-safe grid renumbering (F4 / D2).** Corrected grid, referencing gates that exist:

| Gate | Fate pre-named | If the fold breaks |
|---|---|---|
| G1–G5 (cell battery) | continue → hold-safe → need-the-chair | item re-arms at next ring; verdict row freezes at PARTIAL/GAP |
| G6–G8 (record) | continue → hold-safe | record rewritten from bytes, never narration |
| items 9–12 (cards) | continue → hold-safe → need-the-chair | the card's first use is a probe; its receipt shape is re-measured |
| items 13–15 (continuity) | continue → need-the-chair | capture home folds additively; the open thread is named, not hidden |

**Measured:** the rows map 1:1 onto the artifact's §1 items. **Reverted:** additive; the grid is a draft row, not a gate.

**EXT-4 · Isolation-envelope measurement (G5 / item 6 / thread 2).** The cell's `sandbox_env_id` was added at `2026-11-20T04:45:00Z` — **after** the run ended (`finish_utc` 04:41:43Z). It is a named assertion, not a run-time measurement. The pilot's first ring measures it mechanically:

```
[ -f /tmp/venv/bin/python ] && mountpoint -q /tmp && [ "$(stat -f -c %T /tmp)" = "tmpfs" ]
# + a pull audit during load: ss -tn + ps, asserting no HF/safetensors fetch
```

**Measured:** the probe is the measurement; the verdict row is rewritten to PARTIAL iff it fails. **Reverted:** additive verdict row; no statement is closed by a measurement that was not run.

**EXT-5 · Kit-home exact-name map (item 13 / D4).** The capture home, by exact name and location:

- study root: `KIT-METHOD-CARDS-20261121.md` (the four cards) · `KIT-AUDIT-20261107.md` · `KIT-SKEPTIC-20261107.md`
- `kit/`: `RELEASE-CONDITION-20261121.md` · `READ-UX-SHAPE-20261121.md`

**Measured:** `ls` on the branch. **Reverted:** additive rename; no file moves, no verdict change.

---

## 4 · WALL-CLAUSE QUESTIONS (non-reproductions — QUESTIONS, never defects)

- **Q1 (G5 / item 6):** the sandbox envelope is a **cell annotation added post-run** (04:45:00Z > 04:41:43Z), not a measurement. QUESTION for the pilot's first ring; answered by EXT-4's probe, not by this pass.
- **Q2 (rung 2):** `V3-3.4B-small` (sha `415501bd…`) is armed but has **no cell-ledger ground**. QUESTION for the rung-2 window plan; answered by the next cell.
- **Q3 (dispatch path):** the brief's ground path `audit/PILOT-VERDICT-20261121.md` **does not exist**; the file is at the study root. Read there. A dispatch-path defect, not an artifact defect.
- **Q4 (ring cadence):** "rings 40–60 min" traces to the cross-audit plan (`STAGE-PLAN-CROSSAUDIT-20261123.md` §E1/§G), not to the named `FINAL-LEG-PLAN` ground (which names the 2 h / 1 h / 6 h crons). Grounding note; the cadence is real.

---

## 5 · UNVERIFIABLE LIST (what only `pve1`'s on-disk state can confirm)

- The **actual sandbox envelope** at run time (EXT-4) — the cell is an annotation.
- The **run-time egress receipt** (EXT-2) — the pilot must produce it.
- The **rung-2 cell** (Q2) — no ledger entry yet.
- The **live PR #1 status** and the **kit folder's exact contents at the compose host** — verified here on `p0tat0`'s tree, not on `pve1`.

---

## 6 · PRIOR-PASS NOTE (append-only honesty)

The previously committed version of this deliverable (`7190c0efda`, 2026-11-21) was written against a different draft: its "Revert points R1–R10" section describes R1 as "no gate-state file → verdict row PARTIAL…", which **does not correspond** to the current artifact's §3 table (R1 = Cell install / sha mismatch / sandbox torn down). This pass re-derives R1–R10 directly from the artifact's own table (§1 above). The prior pass is superseded by this file; no lane text outside this deliverable is rewritten.

---

## 7 · NUMBER-SEAM SUMMARY

- All **8 gates'** cell-derived numbers re-derived **exactly**; no claim failed re-derivation.
- The **one false numeric identity** is D1 (`egress_bytes` = the model's bytes) — delta 6,453,994 bytes.
- The **one undefined-gate set** is D2 (G9–G15).
- The **one bad citation** is D3 (`PILOT-VERDICT §2`).
- D4–D7 are naming/state seams; all revertible.

**END OF DELIVERABLE — `plan/tank/lane-ba-audit-20261121.md` · verdict DEFECTS-NAMED · wall clause held (Q1–Q4 are QUESTIONS, not stops).**
