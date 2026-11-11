# NEXT-CHECKIN-PLAN-20261111 — the operator's morning day-sprint agenda

**id:** NEXT-CHECKIN-PLAN-20261111 · **kind:** one-shot planning record (day-side input, two-way door) · **from:** copycat lane (RFC #1433379 apex mission) · **to:** operator @ morning check-in + head as executor · **status:** COMPOSED / NOT LOCKED · **date:** 2026-11-11 ET (post-midnight) · **branch:** study/rfc-1433379-rig-20261105 · **head:** 37e997239d (local == remote)

## 1. OBJECTIVE
Run the day on the bought frame: land the B06-A/B briefs on the fresh kenari pool, harden the harness, fold 11-05 + earliest rows, and ratify the plan-stage list (6-11) — in that order, each with a receipt.

## 2. SOURCE-LOCK
- **Branch:** `study/rfc-1433379-rig-20261105` · **head:** `37e997239d` (local == remote; all walk-back commits on-remote).
- **Homebase:** fork PR `c0wb0yp0tat0/hermes-agent#1` (nothing posted to thread by this lane).
- **Fold's position:** nights 11-09→10, 11-08, 11-07 FOLDED (`CYCLES/B08-A/B`, `B07-A/B/C`, `B06-C`, `DEATH-METRICS-20261110.md` with 16 measured classes); 11-06's BUDGET lens landed (`B06-C`, commit `79ca769aa6`); STATE+ARC (`CYCLES/B06-A-STATE-ARC-20261111.md`) + MECHANISMS (`CYCLES/B06-B-MECHANISMS-RECEIPTS-20261111.md`) staged with the CYCLE-CLAUSE, awaiting the fresh kenari pool; 11-05 (12 files) + earliest rows AHEAD; ETA band ~2-4 days.
- **Seats/pool (measured):** Nous trio alive, free — `upstage/solar-mini4:free`, `meituan/longcat-2.5:free`, `stepfun/step-3.7-flash:free`; Kenari 50 calls/day account-wide, reset exactly 00:00 UTC, fresh pool ~19:00 ET prior evening; budget-shaped fan 1-2 K-lanes/day; each seat 5/min window.
- **K-fire shape:** `HARNESS_ENDPOINT=https://kenari.id/v1/chat/completions` · `HARNESS_RETRY_CODES=403,429,500,502,503` · `HARNESS_CALL_DELAY=2` + browser UA + `LM_API_KEY` from `/root/.hermes/.env` · `--rounds 24`; logs at `/root/workspace/drop/backwards-audit/logs/` with `.err` captures.
- **Plan-stage items:** `PREPAREDNESS-20261111.md` at `/root/workspace/drop/backwards-audit/` — 1-5 immediate mission; 6 communication-form hybrid (three layers, one schema, plan-stage ratification w/ triggers); 7 full-cycle audit; 8-11 storm-confirmed, falsifier-checked (day-side meter; minimum day-playbook: digest → sprint → assessment → handoff; six readiness gates mapped to ledger receipts, NOT-READY falsifier inside, decision support never a proxy; rotation-handoff receipt).
- **Open-verification:** fold's cycle-section must verify the B06 landings' DAY-SIDE sections; walk's fold rows post to the homebase at the fold; roadmap/project-level refresh OWED at plan stage.

## 3. THE ORDERED SPRINT LIST
*(dependency-ordered; pool-first; door-type two-way on every item — nothing locked)*

### S1 — B06-A STATE+ARC on the fresh kenari pool (POOL-FIRST)
- **Handle:** brief `CYCLES/B06-A-STATE-ARC-20261111.md` (staged, CYCLE-CLAUSE attached) → fire on kenari, `--rounds 24`, K-fire shape above; logs `/root/workspace/drop/backwards-audit/logs/` + `.err`.
- **Pool math:** 1 K-lane ≤ ~25-35 calls; pool 50/day, reset 00:00 UTC (fresh ~19:00 ET prior evening); leave ≥15 calls headroom for S2.
- **Door:** two-way — if pool is cold/dry, lane PARKs (never retry) and re-enters on next day's pool.
- **Benefit:** lands the 11-06 STATE+ARC report — the fold's own lineage chain gains its 11-06 node.

### S2 — B06-B MECHANISMS+RECEIPTS on the fresh kenari pool
- **Handle:** brief `CYCLES/B06-B-MECHANISMS-RECEIPTS-20261111.md` (staged) → same fire shape; second K-lane only if S1 left ≥15 calls and pool healthy (1-2 K-lanes/day fan).
- **Door:** two-way — if calls <15 after S1, B06-B defers to next pool day; S1's landing stands alone.
- **Benefit:** mechanisms + receipts companion to S1 — the 11-06 night's budget/mechanism pair closes.

### S3 — Nous trio parallel (no K collision): fold 11-05 + earliest rows
- **Handles:** seats `upstage/solar-mini4:free`, `meituan/longcat-2.5:free`, `stepfun/step-3.7-flash:free` (all alive, free; 5/min window each); artifacts: 11-05's 12 files (the moonbeam night) + the thread's earliest rows; artifact dirs under `studies/rfc-1433379-rig/`.
- **Door:** two-way — any seat 429s → rest ~6 min (measured) then re-fire once; PARK never retry.
- **Benefit:** clears the AHEAD backlog toward the ~2-4 day ETA band.

### S4 — Harness hardening set (repair-then-drop + write-clamp)
- **Handle:** the hardened fire shape itself (retry-codes, call-delay, browser UA, full endpoint, `--rounds 24`) applied to S1/S2; repair-then-drop + write-clamp verified by the `.err` captures in `/root/workspace/drop/backwards-audit/logs/`.
- **Door:** two-way — drop only after the repair shows green on the pool; clamp is a standing clause (every write ≤6,000 chars; skeleton first).
- **Benefit:** the DEATH-METRICS classes 1/5/6/8/13 stay dead instead of recurring.

### S5 — Surface-health arm, one owner (pin-sweep + state-self-heal)
- **Handle:** pin-sweep (probe-before-pin at fan time) + state-self-heal (atomic write tmp+os.replace; startup self-heal check OWED); owner = one named seat, no split.
- **Door:** two-way — if pins drift, PARK the fan and re-probe.
- **Benefit:** kills classes 2/3/10/11 at t=0 — the day starts with live seats.

### S6 — Gist enrichment from B07-B's material
- **Handle:** `CYCLES/B07-B-KIT-GAINS-20261110.md` material → enrich the gist rows.
- **Door:** two-way.
- **Benefit:** the fold's gist layer carries the 11-07 kit gains.

### S7 — Plan-stage ratification (items 6-11) + roadmap refresh
- **Handle:** `PREPAREDNESS-20261111.md` items 6 (communication-form hybrid: three layers, one schema; plan-stage ratification with triggers), 7 (full-cycle audit), 8-11 (day-side meter; minimum day-playbook digest → sprint → assessment → handoff; six readiness gates mapped to ledger receipts, NOT-READY falsifier inside, decision support never a proxy; rotation-handoff receipt); roadmap/project-level refresh OWED.
- **Door:** two-way — ratify or amend at check-in; nothing locked.
- **Benefit:** the plan stage's owed deliverables land with the day.

## 4. THE VERIFICATION GATES (what each landed item must show before it rows)
1. **B06-A/B landings:** artifact on branch under `CYCLES/` + `.err` capture clean + commit hash recorded; DAY-SIDE section present (fold's cycle-section verifies it).
2. **Fold rows:** walk's fold rows post to the homebase (PR `c0wb0yp0tat0/hermes-agent#1`) at the fold — not before.
3. **Nous folds:** per-night fold artifact with commit + receipts; no silent round-4 death (stderr captured).
4. **Harness set:** repair-then-drop + write-clamp evidenced by the `.err` files; retry-set fired without class-5 403.
5. **Surface-health:** pin-sweep probes all green before fan; state-self-heal check run at startup.
6. **Plan-stage:** each of 6-11 shows its receipted row; roadmap refresh stamped.
7. **NOT-READY falsifier:** if any gate's evidence is absent, the item rows NOT-READY with the missing receipt named — decision support, never a proxy for the gate.

## 5. THE CHECK-IN ROW (draft — radio tier-1 shape)
- **RFC1433379-RIG-ENVELOPE-CHECKIN-20261111** · oss-factory meta: branch `study/rfc-1433379-rig-20261105` @ `37e997239d` · homebase PR `c0wb0yp0tat0/hermes-agent#1` · pool: kenari 50/day reset 00:00Z, fresh ~19:00 ET prior · Nous trio alive/free.
- **Speakable lines:**
  1. Walk-back position: 11-09→10, 11-08, 11-07 folded; 11-06 budget lens landed; B06-A/B staged and pool-ready; 11-05 + earliest rows ahead; ETA ~2-4 days.
  2. Day's sprint: B06-A then B06-B on the fresh kenari pool (1-2 K-lanes, ≥15-call headroom), Nous trio folding 11-05 + earliest rows in parallel.
  3. Hardening rides along: repair-then-drop + write-clamp + `.err` captures; surface-health pin-sweep + state-self-heal with one owner.
  4. Plan-stage: items 6-11 ratify + roadmap refresh owed; communication-form hybrid (three layers, one schema) with triggers.
  5. Gates: each landed item shows artifact + commit + clean `.err` + DAY-SIDE section before it rows; fold rows post to the homebase at the fold only.
  6. Next beats: fold 11-05 → earliest rows → plan stage → full-cycle audit; NOT-READY falsifier inside every gate.
- **Receipts:** all on branch `study/rfc-1433379-rig-20261105`; artifact `NEXT-CHECKIN-PLAN-20261111.md`; fold rows at the fold.

## 6. DISPOSITION — honest markers
- **OWED:** roadmap/project-level refresh (plan stage); fold's cycle-section verification of the B06 landings' DAY-SIDE sections; walk's fold rows at the fold; gist enrichment from B07-B.
- **WAITS:** 11-05 + earliest rows (Nous trio, S3); items 8-11 (plan stage); full-cycle audit (item 7) after the folds.
- **NOT DONE HERE:** nothing locked, nothing posted to the thread, no pool calls spent — the plan is day-side input only.
- **ETA band:** ~2-4 days to completion, unchanged.