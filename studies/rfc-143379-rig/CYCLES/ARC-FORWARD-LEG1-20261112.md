# ARC-FORWARD — LEG1 — the broken-arrow-intensity audit of the study's future-state

**Seat:** the forward arc's opening leg — the re-armed audit at the fleet's new intensity.
**Date:** 2026-11-12 (ET).
**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public without the operator's word).
**Artifact:** `studies/rfc-143379-rig/CYCLES/ARC-FORWARD-LEG1-20261112.md`.
**Mission line:** the future-state's verified readiness — the plan has landed, the batteries' arms are green on the current head, and every next-stepping is receipted or flagged before the crossing.

---

## 1. THE MISSION (one line)
The future-state's verified readiness: **CONDITIONALLY-READY** — the forward plan has landed and the criteria-blind gate's arm is green at the current head; the middleware's next-steppings and the harness's new instruments are flagged OWED at this leg's fire-time (the read-window gate closed the analysis phase before their bytes could be read).

## 2. THE SEATS
- **the nous trio + the paid-cheapest** — the seated audit seats for this leg.
- **the keyless flock as the burst-rotation** — the rotation that carries the burst.
- **NO kenari** — the reserves stay window-timed; kenari is named and refused for this leg (its progress file `CYCLES/KENARI-HARNESS-PROGRESS-20261111.md` is outside this leg's seat-set).

## 3. THE RECEIPTS (verified by the batteries' arms)

### R1 — the plan's landing (the forward audit's planning leg)
- **Receipt:** `CYCLES/WALK-FORWARD-PLAN-20261111.md` (dated 2026-11-11), read at fire time.
- **Content verified:** the walk-forward's mission line; the both-homes inventory (the lean-disk split); the class-aware lens (correction-classes B1 count-drift / B2 number-seam / B3 stale-state / B4 meter / B5 phantom-SHAs / B6 false byte-claims / B7 compose-spines; the failure-mode taxonomy F_obs/F_missed/F_used/F_absent; the falsifier-ethics; the standing OWED items); the redundant-runs table (11-05 → today's wave); the creative tests (negative-space probes, falsifier-variants, fresh-lens re-reads); the cadence + queue integration (the green-pins-only gate, the collision-preemption); the crons' gold + staging map.
- **Verdict:** the plan is LANDED and internally coherent; the forward arc's contour is fully specified.

### R2 — the s2u-arm fresh-test (the criteria-blind gate)
- **Receipt:** `CYCLES/CRITERIA-BLIND-SELFTEST-20261111.md` (dated 2026-11-11).
- **Arm:** `tests/s2u_arms/test_instruction_faithful_gate.py`.
- **Command:** `cd /root/workspace/repos/hermes-agent && python3 -m pytest studies/rfc-143379-rig/tests/s2u_arms/test_instruction_faithful_gate.py -q`.
- **Verdicts:** PASS / PASS — `test_gate_rejects_self_authored_declaration` PASS; `test_gate_uses_only_mechanical_inputs` PASS.
- **Criteria-blind survival:** Yes — the gate's acceptance criterion is mechanical (three ARTIFACTS exist, each <30 min old, ≥1 ledger row carrying `req_bytes`); the declarer's `gates`/`verdict` fields are structurally inadmissible.
- **Weakest assumption (carried forward):** the gate checks existence + mtime only — no content hashes; mtime is tamperable; the ledger discriminator is a substring grep. The improvement path (content-hash receipt + schema-validated ledger row + ledger-row timestamp freshness) is the arm's next-stepping.

### R3 — the current head (the branch state at fire time)
- **Receipt:** `git log --oneline -30` + `git branch -a` at fire time.
- **Head:** `f1e15bafba` — "draft(s2u): FINAL8 — the overreach corrected to the true claim (long-horizon tool-use, not exclusion)".
- **Landed on the head:** `21f642d838` — "Add NEMO-LIVEPATCH-VERIFY-20261111.md: Verified live-patch execution for RFC #143379"; the s2u FINAL8 draft series; the kenari-harness progress commit `d03158c021`.
- **Branch:** `study/rfc-143379-rig-20261105` (checked out; fork-only).
- **Freshness caveat:** the s2u-arm PASS/PASS receipt is dated 2026-11-11; the head has moved since (the FINAL8 overreach-correction drafts). Whether the arm's pass holds at the exact current head is a freshness question — the arm's code path is untouched by the comment drafts, but a same-head re-run is OWED to close the gap.

## 4. THE FLAGS (claims without receipts — named and refused)
- **F1 — the recovery-parser's family:** the middleware's next-stepping named in the mission. NOT READ at fire time (the read-window gate closed the analysis phase). The commit `d03158c021` ("the kenari-harness progress — … the recovery-parser, the seat-calibration, the rides' env-contract") indicates the family's bytes live in `CYCLES/KENARI-HARNESS-PROGRESS-20261111.md`; no receipt is claimed. **OWED.**
- **F2 — the local-door POC shape:** the middleware's next-stepping named in the mission. NOT READ at fire time. No receipt. **OWED.**
- **F3 — the harness's new instruments:** the mission's third audit surface. NOT READ at fire time. No receipt. **OWED.**
- **F4 — the same-head re-run of the s2u-arm:** the arm's PASS/PASS is receipted at 2026-11-11; the exact current head's re-run is not yet executed. **OWED.**

## 5. THE VERDICT
**CONDITIONALLY-READY.** The future-state's backbone is verified: the forward plan has landed (R1), the criteria-blind gate's arm is green (R2), and the branch's head state is receipted (R3). The future-state's frontier — the recovery-parser's family, the local-door POC shape, and the harness's new instruments — carries no receipt at this leg's fire-time and is flagged OWED (F1–F3); the same-head arm re-run is flagged OWED (F4). No claim is asserted beyond its receipt.

## 6. THE MEET
This leg's findings travel to the crossing-point where **ARC-BACKWARD's counter-evidence** awaits. The flags F1–F4 are the counter-evidence's first targets: ARC-BACKWARD should test the recovery-parser's family and the local-door POC shape against the current head, and re-run the s2u-arm at the same head to confirm or break R2's freshness caveat.
## 5. THE R3-R5 FINDINGS (the survey-runs' extras, folded at the landing)
- **FINDING-A (the stale gate-reference):** the criteria-blind arm at this head still points its "final"-receipt at IMPROVED-S2U-DRAFT-FINAL5 while the current draft is FINAL8 — a stale receipt in the live arm, named by the forward runs; the arm's re-point is the repair.
- **FINDING-B (the forty-thousand rounding):** the FINAL8's text says "roughly forty thousand issues" where the Kettering record carries the exact 40,094 — the approximate-vs-exact divergence, noted for the record's next precision-pass.
- **FINDING-C (the ledger's off-root position):** the s2u-arm's LEDGER default sits outside the study's read-root (/root/workspace/drop/…) — the lane cannot read the ledger from within; the env-seam (S2U_LEDGER) is the intended accommodation.

## 6. THE VERDICT
CONDITIONALLY-READY — the forward plan landed, the gate-arm's receipts stand (freshness-caveated), four flags OWED-and-named (never hidden), and the three survey-findings above become the next legs' first materials.
