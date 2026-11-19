# SPRINT-FIRE-SEQUENCE-20261119 — THE ONE fire sequence
**Lane:** flagship-synthesis (copycat seat, in its 4-day window — used, not hoarded) · **Rig:** rfc-143379-rig · **Date:** 2026-11-19
**Receipts:** LANE-1/2/3/4, NEMO-ARM-PLAN, NEGENTROPY-ARM-EXECUTE, CTO-FREEDOM-PLAN, MISSION-BRIEF-MASTER read in full (first pass hit the read-gate; wall clause applied, re-read after first write). FLEET-WIRING §1/§6 not re-read — machine layer receipted via ARM-EXECUTE §4; roster rows **not confirmed**.

## THE ORDER (every fire two-way; nothing public without the user's word)
| # | Fire | Window | Reversibility + rollback |
|---|---|---|---|
| F0 | **Re-survey + ledger gate**: Nov-20 deprecation CONFIRMED LIVE (ARM-EXECUTE §3 curl) — no new legs to kimi-k2.6/glm-5.2/deepseek-v4-flash set after 2026-11-20; dispatch reads ls-remote + process-tree fresh (LANE-2 §4), C3 freeze ≤T+7, 429→backoff+fallback never blind. Kenari RESERVE (meter spent); stepfun next stages (CTO §3) | before every dispatch; 00:00 UTC resets | config overlay; restore prior seat table / revert flag |
| F1 | **Probe B scribe-hardening FIRST** — every later landing carries its witness: checkpoint row cell_hash→SHA→branch; canonical-encode gated ≤64 KB (LANE-3 §4) | runners (unmetered) | SCRIBE_HARDENING_* OFF, one redeploy; rows non-destructive |
| F1b | **Read-path regression tests** (LANE-4 §3): tests/tools/test_memory_read.py, ~30 lines, RED-before-GREEN — smallest two-way door, highest reception leverage (jfugalde's missing-tests note) | runners | revert the test commit; additive only |
| F2 | **Probe A release-point archive-eligibility** before arm B: no release_event_id → NOT_ELIGIBLE | runners | GOVERNED_COMPACTION_RELEASE_RULE OFF; ≤2 h cycle, idempotent |
| F3 | **Judge-control gate**: 20-ep control set, frozen judge ≥90% or NULL; cache+token logging armed; ledger before results (LANE-1 §3) | pre-battery | null-and-refreeze, pre-registered |
| F4 | **Three-arm battery** A/B/C ~200 eps each, non-re-observable class, mirrored eps, fresh store, one-factor law; oracle = SambaNova free gpt-oss-120b (20-RPD tap); local-LM fallback voids oracle line → two-arm verdict. **Luna leg INSIDE the probe, never standalone** (CTO §3), ~$0.06–0.14/ep, outside decision rule | qwen4-max 4-day window + runners | read-only vs substrate; inconclusive → rewrite experiment, not claim |
| F5 | **T+4h checkpoint (ADD-1)** — expected-state row: first arms progressing · seats' 429/health rows nominal · folds byte-verified · token agreement. Verdict CONTINUE / RE-BRIEF (seam+fix named) / HOLD (packet). A READ, not steering | T+4h of fire | read-only; RE-BRIEF/HOLD are the rollbacks |
| F6 | **Bench door, route A probe-first door-after** (LANE-4 §1, recommended): ~$45–100 verify cap, input-logging OFF or void; PR=reported → Unify rerun on 50 private rules=verified | after probe lands | state C ($0, not-this-week) is the honest rollback; door stays open |
| F7 | **Hold-audit at fire** (Nemo re-dispatch, STEER-3) + **drift-check by name** (ADD-2): semantic / coordination / behavioral, one line each in verdict. Pre-audit: HOLD-WITH-NAMED-SEAMS (ARM-EXECUTE §7) | at fire | base-swap on seat quirks, never same-lane retry; chair-packets pre-cut (§6) |
| HELD | **Probe C** NOT-READY: door_open_audit_log seam absent (LANE-3 §4). Auto-path: AskALCF admission packet on seam evidence, then fire | — | flag default OFF |

**Folds' cadence:** per landing, ARM-EXECUTE §2 checklist — artifact on disk · cell byte-verified · served-verify · commit+push (ls-remote before/after) · PR #1 envelope row (the HITL update, never skipped) — plus master §7 append. Token single-source = ARM-EXECUTE v2 line; disagreement → watcher HOLDS, head resolves. Post-fire the head's only work is the folds (CTO §4).

## THE VERDICT LINE
**READY-WITH-NAMED-SEAMS.** Seams: (1) Probe C audit-log → AskALCF packet [LANE-3 §4]; (2) encode >64 KB → stage-decoupled evaluation [LANE-3 §4]; (3) UNVERIFIED seat cells → F0 dispatch-time re-survey [LANE-2 §1/§5]; (4) Type-4 distributional contamination open → harness generality + probe's same-class evidence [LANE-4 §2]; (5) FLEET-WIRING roster not confirmed → arming receipts cover the load-bearing wire-checks [ARM-EXECUTE §4: scribe tunnel REACHABLE, Harbor LIVE, SSH REACHABLE 77G free].
Evidence per claim: battery fireable — LANE-1 READY, rule pre-committed verbatim; governance A/B — LANE-3 READY, flags OFF; door — LANE-4 "COSTED and TWO-WAY, fire-after-the-probe"; windows — LANE-2 scaffold, no limit guessed; Nov-20 — live curl grep; arming — ARM-EXECUTE live receipts; checkpoint/champion — CTO ADD-1/2/3.

## APEXES + NO-IMPROVEMENT GATES (loop until no-change-twice)
- **M1 certify:** CERTIFY iff B−A≥20 pts ∧ B≥0.85×C; FALSIFY if B−A<20 ∨ (B<0.85C ∧ B≤A); INCONCLUSIVE if judge<90% ∨ cache-log missing ∨ C−A<5 [LANE-1 §3]. Closed when two frozen re-runs show Δ(B−A)<1 pt, Δ(B/C)<1%, Δcost/success<5%; episodic ceiling binds — no lifetime-learning overclaim.
- **M3 adopt:** A precision ≥0.95 (fail <0.80); B FP=0 ∧ checkpoint completeness 100%; C post-admission audit entry ≤500 ms. Closed at targets, unchanged across two probe passes.
- **M2 synchronize:** re-survey queue drained, zero stale rows fired against, zero blind retries, token/mirror agree; unchanged across two dispatch cycles.
- **Bench door three states (LANE-4 §1):** A probe-first door-after (recommended) / B door-first (NOT recommended) / C not-this-week ($0, honest if probe says not-ready). Closed only at **verified** (Unify rerun) or honest C — reported never counts as a result.
- **Loop:** each landing re-checks its apex; changed metric re-opens (AIMD cadence); two consecutive no-change reads terminate — never a "maybe" exit. Landings decide the next sprint-mission.

## OPUS-OF-OPUSES LINE
**Champion row (ADD-3, per mission-set):** CERTIFY → arm B (substrate + release-point governor + hardened scribe) is champion; else arm A stands and the falsify receipt is the row. **Home:** run ledger (judge seed, episode set, compaction counts, cost rows — LANE-1) + master §7 folds; dead-end registry accumulates falsified classes beside it (AutoScientists pattern). **Pre-registered dead-ends, never re-explored:** regime reversal → trim governor steps NOT scrap store; attribution failure → retriever reshape NOT store; local-LM oracle → void; blind 429 retry → forbidden; door-first route B → not recommended. Next sprint-mission starts from the champion, reads the registry first.

## COMPOSE-CHECK TABLE
| Step | Status | Evidence |
|---|---|---|
| Deconstruct | FIRED | Order / verdict / apex gates / opus line; eight lane receipts reconciled. |
| Sense | FIRED | All ground read (read-gate first pass receipted; re-read post-write); wiring roster marked not confirmed. |
| Choose | FIRED | Witness-first F1→F2→F4; route A over B on LANE-4's receipt; C held on AskALCF — never silently picked. |
| Calibrate | FIRED | 200 eps/arm, 90% judge, ≤64 KB gate, ~$45–100 door, Nov-20 hard line — all receipt-sourced. |
| Probe | FIRED | F0–F7 each names metric + rollback; rule pre-committed before any run. |
| Review | FIRED | Two stranger re-reads; one refinement per finding; pushbacks below. |
| Record | FIRED | This artifact; ledger-before-results inherited; folds per ARM-EXECUTE §2. |
| Compose-check | FIRED | This table; not-confirmed cells named with auto-paths, none estimated. |

## REVIEW-LOOP
Re-read 1 (gated): door/arming/checkpoint unreceipted → CARRIED marks. Re-read 2 (post-write, gate lifted): CARRIED transcribed into F5/F6/F7 + folds' cadence; Luna moved inside probe per CTO; tests packet added F1b. Pushbacks: 1 "Fire waits for perfection" → no: 70% law, seams named, two-way doors (CTO §3). 2 "Probe C should ride the sprint" → unverifiable promise; AskALCF gate is the receipt. 3 "20-pt margin arbitrary" → pre-committed fraction of the 92.5-pt field gap; honesty anchor. 4 "Reported score is a result" → no: reported-vs-verified vocabulary, rerun or nothing (LANE-4 §4). Termination: no-change re-read ×2 — stable.

**ONE LINE:** READY-WITH-NAMED-SEAMS — F0 re-survey → F1 witness → F1b tests → F2 release-rule → F3 judge-gate → F4 battery+Luna in the flagship window → F5 T+4h read → F6 door route A → F7 hold-audit; C held on evidence; folds drive until no-change-twice on every apex. **Next mechanism:** the fire itself — dispatch F0/F1 on the runners and open the battery in this window; the landings pick the next sprint-mission from the champion row.
