# NEXT-CHECKIN-PLAN-20261111 — the operator's morning day-sprint agenda

**meta**
- id: NEXT-CHECKIN-PLAN-20261111
- kind: day-sprint plan (two-way door; nothing locked — day-side input to the check-in)
- from: the walk-back lane (copycat composition, 2026-11-11 ET post-midnight)
- to: the operator at morning check-in + the head as executor
- status: DRAFT — composes the check-in; the fold row for it is posted by the operator, not this lane

## OBJECTIVE
The morning's sprint goal, one line: put the B06-A/B briefs on the fresh kenari pool and land the B06 landings with day-side sections, while the day-sprint list (harness hardening, surface-health, the plan-stage items) runs in the non-colliding splits — so the check-in rows against a visible, receipted branch position.

## SOURCE-LOCK
- branch: `study/rfc-143379-rig-20261105`
- head: `37e997239d` (local == remote; all walk-back commits on-remote)
- homebase: fork PR `c0wb0yp0tat0/hermes-agent#1`
- frame: the walk-back's position (nights 11-09→10, 11-08, 11-07 folded; night 11-06 BUDGET lens landed; night 11-05 + earliest rows AHEAD; ETA band ~2-4 days) — this plan composes from that frame only; no handle outside the brief is added.

## THE ORDERED SPRINT LIST
(each item: handle + door-type (all two-way) + one-line benefit; ordered pool-first, parallel splits named where the Nous trio and the K-pool do not collide)

1. **K-pool first — B06-A + B06-B on the fresh pool.**
   - handles: `studies/rfc-143379-rig/CYCLES/B06-A-STATE-ARC-20261111.md`, `studies/rfc-143379-rig/CYCLES/B06-B-MECHANISMS-RECEIPTS-20261111.md`; fire shape `HARNESS_ENDPOINT=https://kenari.id/v1/chat/completions`, `HARNESS_RETRY_CODES=403,429,500,502,503`, `HARNESS_CALL_DELAY=2` + browser UA + `LM_API_KEY` from `/root/.hermes/.env`; `--rounds 24`; logs at `/root/workspace/drop/backwards-audit/logs/` with `.err` captures.
   - pool math: 50 calls/day account-wide, resets exactly 00:00 UTC; ~25-35 calls per full lane; budget-shaped fan = 1-2 K-lanes/day; fresh pool starts ~19:00 ET the prior evening.
   - door: two-way. benefit: the B06 landings land with the CYCLE-CLAUSE verified day-side — the fold's immediate mission (PREPAREDNESS items 1-5).

2. **Harness hardening set — repair-then-drop + write-clamp.**
   - handle: the harness's `HARNESS_*` env set named above (the exact set the pool fires use).
   - door: two-way. benefit: the retry/drop behavior and the write-clamp make every subsequent K-lane and Nous call receipted and wall-safe.

3. **Surface-health arm — pin-sweep + state-self-heal, one owner.**
   - handle: the PREPAREDNESS list's surface-health item (one owner named at check-in).
   - door: two-way. benefit: the repo surface the pool writes into stays pinned and self-heals, so the landings' receipts stay verifiable.

4. **Nous trio split (non-colliding with the K-pool).**
   - handles: `upstage/solar-mini4:free`, `meituan/longcat-2.5:free`, `stepfun/step-3.7-flash:free` — ALIVE, free; each seat also a 5/min window.
   - door: two-way. benefit: parallel verification/reading work (the plan-stage items 6-8, the falsifier checks) runs without touching the K-pool budget.

5. **Night 11-05 + the earliest rows — AHEAD.**
   - handle: the night 11-05 (12 files, the moonbeam night) + the thread's earliest rows, per the walk-back's position.
   - door: two-way. benefit: the thread's earliest rows close, shrinking the open fold backlog toward the ~2-4 day ETA band.

6. **The gist enrichment from B07-B's material.**
   - handle: B07-B's material (folded under `studies/rfc-143379-rig/CYCLES/`).
   - door: two-way. benefit: the enrichment feeds the plan-stage items and the check-in's speakable lines.

7. **The plan-stage items — the communication-form hybrid + the full-cycle audit + the storm-confirmed items.**
   - handles: PREPAREDNESS-20261111.md items 6-11 — the three-layer/one-schema communication form (plan-stage ratification with triggers), the full-cycle audit, the day-side meter, the minimum day-playbook (digest → sprint → assessment → handoff), the readiness gates (six gates mapped to ledger receipts, NOT-READY falsifier inside, decision support never a proxy), the rotation-handoff receipt.
   - door: two-way. benefit: the plan stage's owed items are taken in one ordered pass; the roadmap/project-level refresh is OWED at the plan stage (see DISPOSITION).

## THE VERIFICATION GATES
(what each landed item must show before it rows)

- **B06-A/B landings:** each artifact's cycle-section verifies its DAY-SIDE section — the CYCLE-CLAUSE's fold-side obligation, met on the day side; the pool fire's logs (with `.err` captures) show the calls completed under the retry/drop set; no `.err` unaddressed.
- **Harness hardening:** a landed item shows the repair-then-drop path and the write-clamp both exercised — a receipted retry/drop trace and a write that stayed inside the study realm.
- **Surface-health:** pin-sweep output shows the pins resolved; state-self-heal shows the healed state; one owner's name attached to the row.
- **Nous trio work:** each seat's output rows against its own 5/min window; nothing counted against the K-pool's 50/day.
- **11-05 + earliest rows:** each folded row's cycle-section verifies its day-side section (same CYCLE-CLAUSE shape); the fold rows post to the homebase at the fold.
- **Plan-stage items:** each item's falsifier check passes — the readiness gates read as six gates mapped to ledger receipts with the NOT-READY falsifier inside, and decision support never standing in as a proxy for a gate.
- **The walk's fold rows:** posted to the homebase (`c0wb0yp0tat0/hermes-agent#1`) at the fold — the open-verification obligation, closed at the fold, not before.

## THE CHECK-IN ROW DRAFT
(the radio tier-1 shape: envelope + speakable lines + receipts)

**RFC143379-RIG-ENVELOPE-CHECKIN-20261111**
- oss-factory meta: branch `study/rfc-143379-rig-20261105`, head `37e997239d` (local == remote), homebase fork PR `c0wb0yp0tat0/hermes-agent#1`; artifacts under `studies/rfc-143379-rig/CYCLES/`; logs at `/root/workspace/drop/backwards-audit/logs/`.
- speakable lines (5-8):
  1. The walk-back holds: nights 11-09→10, 11-08, 11-07 folded under `CYCLES/` (B08-A/B, B07-A/B/C, B06-C, DEATH-METRICS-20261110.md with 16 measured classes); night 11-06's BUDGET lens landed (B06-C, commit 79ca769aa6).
  2. Night 11-05 (12 files, the moonbeam night) and the thread's earliest rows are AHEAD; ETA band ~2-4 days.
  3. Today's sprint: B06-A/B on the fresh kenari pool first — 50 calls/day, resets 00:00 UTC, 1-2 K-lanes/day, fresh pool from ~19:00 ET the prior evening — with the harness hardening set (repair-then-drop + write-clamp) and the surface-health arm (pin-sweep + state-self-heal, one owner) in the non-colliding splits.
  4. The Nous trio (upstage/solar-mini4:free, meituan/longcat-2.5:free, stepfun/step-3.7-flash:free) runs the parallel verification/reading work outside the K-pool budget.
  5. The plan-stage items run in one ordered pass: the three-layer/one-schema communication form (ratification with triggers), the full-cycle audit, the day-side meter, the minimum day-playbook (digest → sprint → assessment → handoff), the six readiness gates mapped to ledger receipts (NOT-READY falsifier inside; decision support never a proxy), the rotation-handoff receipt.
  6. Next beats: the fold's cycle-section verifies the B06 landings' day-side sections; the walk's fold rows post to the homebase at the fold; the roadmap/project-level refresh is owed at the plan stage.
- receipts: the branch's commit history (head `37e997239d`); `CYCLES/` artifacts; the pool fire's logs with `.err` captures; the homebase PR's fold rows.

## DISPOSITION
(the honest markers — what's OWED, what waits)

- **OWED at the plan stage:** the roadmap/project-level refresh (the open-verification item); the communication-form hybrid's plan-stage ratification with triggers.
- **OWED at the fold:** the fold's cycle-section verifying the B06 landings' day-side sections; the walk's fold rows posting to the homebase.
- **OWED on the day side:** the B06-A/B landings' day-side sections (the CYCLE-CLAUSE's fold-side obligation, met day-side); the surface-health arm's one-owner receipt.
- **Waits on the pool:** the K-briefs fire only while the fresh kenari pool holds (50/day, 1-2 K-lanes/day); a spent pool defers item 1, and the Nous trio split absorbs the day's verification work meanwhile.
- **Waits on the fold:** the 11-05 + earliest rows close at the fold, not the day sprint; the ETA band (~2-4 days) holds only while the pool and the Nous seats stay alive.
- **Nothing locked:** every item is a two-way door — the check-in may re-order, split, or defer any line without cost; the plan is day-side input, not a commitment.