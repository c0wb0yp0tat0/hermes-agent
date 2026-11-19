# LUNA-LEG-AUDIT-20261119 — independent audit, RE-FIRE (full)

Base: the Luna-middleware leg's work-product on `study/rfc-143379-rig-20261105`. The first ride's stub (READ-IN-PROGRESS) is superseded; the stub stays in history as the refusal receipt. Gate: "nothing public without the user's word." RFC QUIET. Record-first; ABSENT stays ABSENT + named.

## Input set read (the audit's receipts)
`BATTERY-LUNA-LEDGER-20261119.json` + `-R2.json` (fire arms/episodes/verdict tails) · `BATTERY-LUNA-PILOT-RESHAPE-20261119.json` (VOID pilot) + `-R2.json` (B′ + tail) · `BATTERY-FULL-LEDGER-20261119.json` (fold `luna_leg_20261119`) · `RETRIEVER-RESHAPE-20261119.md` (verdict tail) · `REPORTBACK-NULL-PROSE-20261119.md` (cold read) · paged episode windows (per-arm counts tallied row by row).

## RE-DERIVE results

**1. Fire (IN-LANE).** R1/R2 ledgers: A 0/40=0.0 both (E40/A0, ABSTAIN 40, C5a 40, headline_abstention 0.0, sensitivity_abstention 1.0, cost 18.68) · B R1 19/40=0.475 answered 26, R2 23/40=0.575 answered 31 (stale_confident 7/8, bridge_compliance 0.9/0.925) · C 29/40=0.725 both (answered 30/33) · decision_rule tails x2: B_minus_A 0.475/0.575 ≥ 0.20 ✓; B_over_0.85C false both (0.475/0.575 < 0.61625) ✓; verdict **"INCONCLUSIVE" x2**, trigger mean_f3b 0.9/0.925 < 1.0 (harness x4/x3); judge_control 1.0 n20 + judge_pipeline_direct 20/20 both; cost_total 37.36 each. ✓

**2. Reshape (IN-LANE).** `-R2.json`: B′ 8/20=0.4, answered 10/20, mean_f3b 0.85, INCONCLUSIVE, cost_total 18.68 (A 9.34+B 9.34; C free). RETRIEVER-RESHAPE verdict tail (cites ledger rows): same seeds 0-19 — banked R1 10/20, R2 9/20 correct; answered 15/20, 12/20 → **NO GAIN**, dead-end registry, receipt `-R2.json`. First pilot (VOID): A/B/C harness 15/17/11 (READER-ERROR empties, row tallies), C 0.25, C_minus_A 0.25, INCONCLUSIVE; judge_control 1.0 n20 + pipeline 20/20 → the oracle control exonerated the flag (route flakiness, not judge health). ✓

**3. Economics (IN-LANE — ONE SEAM).** Fold: shadow_rows 37.36+37.36+18.68+18.68 → **shadow_total_usd 112.08**; account_actual **61.99** ("ACTUAL — the planning estimate billed below itself; classes labeled, never merged"); planning_estimate 0.467/exec; receipts [1][2][4][5]; fold arithmetic exact. **SEAM:** the digest wrote "R1 37.36 + R2 37.36 + pilots 18.68x2 = 93.40" — wrong (sum 112.08); 93.40 = total minus the VOID pilot, which the record does NOT exclude. The primary receipt governs: 112.08.

**4. Report-back (IN-LANE, cold).** Tone held: dismissal's case stated first; gratitude-first to builders; plain terms (240 questions, two identical runs); boundary honest ("never matched" 72.5%; "opening question, not a closing argument"); narrow claim ("a fact about the machinery"; "assumption, not a settled result"); every number reported; rerun is the next step; **DRAFT-NOT-POSTABLE — "the operator's word is the only key"** (gate held in artifact). "Agnostic" unqualified: never used. Two-class honesty: $61.99 actual (telemetry, inside the pre-committed $100 gate) vs $0.467 planning rows — both reported, never merged. Zero refusals/hedges across 240 (HEDGE 0 in every arm block read). ✓

## Theater / integrity
- No self-fuel: reshape (N1/P1/F1 behind RESHAPED_NOTE, default-rollback) recorded NO GAIN in the dead-end registry, not spun; the VOID run kept its label + cost in the shadow rows; verdict classes honestly INCONCLUSIVE x2, never CERTIFY. ✓
- **S7 split (abstains BY SILENCE):** A arms headline_abstention (R+H)/N = 0.0 vs sensitivity_abstention = 1.0 (E 40/40) — the headline would read "no abstention" against 100% silence; B arms 0.0 vs 0.35/0.225. Both fields coexist in every arm block; the report-back says "the silence was the abstention". Seam named, not papered. COVERED.
- Gate: nothing public beyond PR #1 (BORROWED); report-back's DRAFT-NOT-POSTABLE, operator-gated (IN-LANE). Seat-neutral NULL end; no vindication/denouncement. ✓
- Two-way doors named: RESHAPED_NOTE rollback = old view; the $6.60 pilot-budget fallback; the reopen condition (B′ gain toward C). ✓
- ABSENT, named: the F6 cert door packet / the operator's word (chair-gated) — the pilot rode the pre-committed gate (RETRIEVER-RESHAPE §0). ✓

## Compose-check (coverage)
| Item | Verdict | Stamp |
|---|---|---|
| Fire results | COVERED | IN-LANE (arms + verdict tails) |
| Reshape (B′, VOID, NO GAIN) | COVERED | IN-LANE (pilot files) + reshape verdict tail |
| Economics | COVERED — ONE SEAM | IN-LANE (fold); FINDING-1 |
| Mission (middleware, seat-neutral, NULL end) | COVERED as BORROWED | BORROWED `LUNA-MIDDLEWARE-MISSION-20261119.md`; no-overclaim corroborated IN-LANE (report-back) |
| Synthesis chain (RELOAD-COMPOSE 17, CTO-lens S6/S7/S8+A1/A2/A3, H1-H4, CONFIRMED-NO-IMPROVEMENTS, CHAMPION-ROW-FOLD+appends) | PARTIALLY-COVERED | BORROWED (named files, not re-read — the AoA lane's third base) |
| Machinery (`battery_luna.py`, tests 26/26 GREEN, R2 RED-before-GREEN) | PARTIALLY-COVERED | BORROWED (named); tests not re-run by this audit — seam named |
| Report-back staged face | COVERED | IN-LANE (cold read) |
| Gate / integrity / S7 split | COVERED | IN-LANE (ledger fields + report-back) |

## Findings
**FINDING-1 — digest/record arithmetic seam on the shadow total.** Evidence: the digest wrote "37.36+37.36+18.68x2 = 93.40"; the primary receipt `luna_leg_20261119.shadow_total_usd` = **112.08** (4 rows sum exactly). Fix-seed (the NEXT leg's seed, never my implementation): the AoA feed carries the record's two class-labeled numbers only — shadow 112.08 (planning estimate, 4 runs incl. the VOID) and actual 61.99 (account telemetry) — and the digest's 93.40 is retired as head-arithmetic error, never propagated.
No finding on the leg's work-product: every leg-named number re-derived matched the record.

## Overall verdict
**AUDIT-FINDINGS 1** — the leg's work-product is PASS-grade across every re-derived claim; the single finding sits in the audit's input set (FINDING-1), not in the leg's record. Gate held; report-back DRAFT-NOT-POSTABLE by design.

## Audit-of-audit input set (reads this + the leg's record, on a third base)
`LUNA-LEG-AUDIT-20261119.md` (incl. the stub predecessor in history) · `LUNA-MIDDLEWARE-MISSION-20261119.md` · the four ledgers · `BATTERY-FULL-LEDGER-20261119.json` · `RETRIEVER-RESHAPE-20261119.md` · `REPORTBACK-NULL-PROSE-20261119.md` · `RELOAD-COMPOSE-20261119.md` · `READY-WITH-NAMED-SEAMS` · head closing H1–H4 · `CONFIRMED-NO-IMPROVEMENTS-20261119.md` · `CHAMPION-ROW-FOLD-20261119.md` + appends.
