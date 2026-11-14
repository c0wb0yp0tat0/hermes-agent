# READ-RESTORE DECISION-PREP — 2026-11-14 (chain leg, seat: solar) — R1

## 0. FILE INVENTORY (stamped read — each file read once, on disk, at 2026-11-14)
- CYCLES/RFC-143379-RECORD-20261111.md — full issue body + thread, end to end
- CYCLES/RFC-143379-BODY-20261111.md — RFC #143379 body draft
- CYCLES/IMPROVED-S2U-DRAFT-FINAL5-20261111.md — audit flags + quantified severity
- REFS/BRIEF-AUDIT-S2U.md — audit-of-S2U brief (HEAD-STAGED, REFS pocket)
- REFS/S2U-MISSION-PLAN-NUANCE-20261111.md — mission plan nuance
- REFS/ADOPTIONS-20261112.md — adoptions ledger
- REFS/CROWN-SLICE.md — crown-slice framing
- NEMO-DAY-PLAN-20261114.md — corrected plan (C1/C3/C6 ring table)
- NEMO-STEER-CHANNEL-20261114.md — mid-flight steering (read pre-compose)

## 1. THE EVIDENCE — label trail, two vehicles, the hold
- THE WOUND: read action removed upstream (56ee8a5cc6, 2026-02-19, 14-line deletion). On current main the memory path answers `Unknown action 'read'` (RECORD body, confirmed jfugalde 10-24). Restore head (#141876, c0wb0yp0tat0, HEAD `af16e3ab16`) returns entries + usage line on the first try (executed jfugalde).
- THE GAUGE on disk: 106 commits / 6,275 lines (3,541 + 2,734) since `56ee8a5cc6`. True debt is a SUBSET — four `~30-line` hand-back echo sites in `tools/memory_tool_store.py` (:322 `_failure_with_entries`, :124 `closest_entries`, :481/:488 replaced-entry fields, :328-:336 batch-abort echo) plus a fifth echo in `tools/memory_tool.py` (:157 `_validate_single_op`). A ~12-line `MemoryStore.read` (#141876 @ :369) pays for them.
- CLASS SPLIT (record-legit): SEVEN silently-dropped-value tickets NOT the read (#99957, #105243, #49195, #105248, #140935 one-shot; #110126, #50132 output-cap) — own fixes in flight. THREE memory-content-lifecycle tickets THE read serves (#116673 bounded read / anchored doc chain; #135039 write-time budget; #69264 curation skill).
- LABEL TRAIL (six moves, reading events not issue events): P2 at birth (10-23 03:36Z, alt-glitch, 2 min after post) → P3 (10-24 01:06Z) → quantification comment landed 79 min after that P3 → c2h5oh sequence (P2 removed → P3 added → P4 added → P3 removed). Events endpoint exposes none of the final changes. P4 = residue, not fresh judgement.
- QUEUE SHAPE (exact-label counts 11-11, sample-verified against substring-collision class): P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173. P4 = smallest bucket. P2/P3 ~18,586. RFC's label sits two bands below the queue's real center of gravity.
- LABEL FIELD (report pulse): 24/120 P4-labeled (comp/agent count, P4's own set) 10-23; 34 comments of verified work = thread datapoint, baseline-first. Category moved six times with zero substance change; "instruction-faithful criteria are the fix."
- FABRICATION CLASS: 6/6 fabrications without the read path (reproduced twice); 12/12 clean refusals with one non-punitive sentence of abstention ("a system that cannot read should say so, never guess").
- TWO VEHICLES, ONE GAP, NEITHER MERGED: #11548 (minimal dispatcher, branch fix/116564-descr intact at d3a6e577, closed-by-author) vs #116673 (schema-safe read + doc-chain, closed-by-author 2026-10-10, merged=false; head verified 60a2e15638, GitHub mergeability pending). FIX NOT MISSING — UN-MERGED.
- HOLD (verbatim, RFC-143379-RECORD §82, comment 6787192097, 2026-11-11): "We are holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives with the community rather than let the hold become indefinite."
- READ-RESTORE DOOR (corrected definition): RFC #141876 = memory `read` restoration. Located.

## 2. THE DECISION FRAME — what the chair must decide
- OPTION A — CONTINUE THE HOLD: keep holding for #141876 on the record; condition: fix lands soon or we discuss alternatives. For: record is honest; redness is auditable; community trust in form. Against: |stuck|+dithering; a ~12-line restore is cheap and unmerged; queue's largest drift class ignores a "hold."
- OPTION B — ALTERNATIVES-WITH-COMMUNITY (record-named path): the verbatim hold exit. For: honest, bounded, releases pressure; keeps a seat for the undersigned. Against: names no option yet; discard-by-default is also a form of indefinite hold; needs a mechanism before any community call.
- OPTION C — RESCOPE/SPLIT OFFER: split the read door into the restore itself (12-line `MemoryStore.read`) + the bounded read (#116673) + governed compaction, each with its own ticket/PR. For: each piece is scoped; the chair gets a decision per ship; the 6,275-line stack edges toward closure. Against: more work, more labels, more movement; the wrong split is a new label lottery.
- EFFECTIVE LIGAMENT between A/B/C: the hold is a status, not a destination. Next state = what the chair does with it.
- RISK REGISTER: 
  - R1 form-loss (do not re-read, guess) — anchored by the 6/6 + 12/12 evidence.
  - R2 indefinite hold — exactly what comment 6787192097 names as the failure mode ("rather than let the hold become indefinite").
  - R3 two-vehicle churn — #11548 vs #116673 both open; the chair must pick ONE anchor before more drift.
  - R4 label drift on a rescope — "instruction-faithful criteria" remains the only anchor.
- OPEN QUESTIONS ONLY THE CHAIR CAN ANSWER: (1) should the chair treat the P4 label itself as the signal to re-triage, or only as residue of a reading? (2) is the chair committing the restore to a ship whose acceptance battery is agreed, or streaming it? (3) does the chair want the bounded read (#116673, Finn763) pulled into the same ship, or left to its own road? (4) is a community discussion the fallback, and if so, when? (5) does the chair want the FRAME to carry the 34-comment arc and fabrication-class numbers as a standing section, or only as receipts?

## 3. THE RECOMMENDATION — the lane's read, not the chair's decision
Read the record with the numbers: the wound is real (Unknown action 'read' on main, verified by jfugalde), the cost is measurable (6,275-line stack, ~30-line core, 6/6 + 12/12 reproduction), the label is a reading artifact (six moves, no substance change), and the fix is not missing — it is unmerged. Recommendation of the lane: KEEP THE HOLD STATUS (option A), but convert it from passive patience to an active clock: restate the verbatim condition in the decision-PREP, bind the next state to a chair decision within the round-count window, and open the alternatives-with-community thread (option B) as the pre-agreed escape hatch so the hold cannot become indefinite. Pick ONE ship anchor — the restore (#141876) — and tie the bounded read (#116673) to its acceptance acceptance battery rather than letting the two vehicles drift as separate labels. In short: hold the status, not the brake; let the condition govern.

## 4. THE OWED REGISTER — what could not verify (stamped, exact run spec for the head)
- remote PR states (#141876, #11548, #116673) — OWED via gh CLI; run spec: `gh pr view 141876 --json state,mergeable,commits --repo hermes-agent` plus `gh pr view 11548 --json state,mergeable`; repeats next round.
- thread pagination / full comment set — OWED via `gh api repos/.../issues/143379/comments --paginate`; the 34-comment arc is from the record, not re-derived.
- local repo reads IN-LANE: branch integrity (#141876 head af16e3ab16, #116673 60a2e15638 / #11548 d3a6e577), working tree clean. NOT re-checked against remote.
- source tags on all reads: IN-LANE (on-disk file reads), BORROWED (this brief's quoted conditions), HEAD-RECON (executions wired to named artifacts).
- no /root/.hermes writes; no service changes; RFC upstream QUIET; nothing public.

## 5. LOOP-STATE + NEXT-LAUNCH
LOOPER-STATE: CONTINUE + DECISION-READY (the chair holds the decision; the lane holds the frame).
NEXT-LAUNCH (per corrected plan's ring table): R2 — name the ship anchor and the acceptance battery. Brief path: `studies/rfc-143379-rig/CYCLES`; seat: solar; logdir: `studies/rfc-143379-rig/logs/20261114/`.
