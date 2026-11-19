# LUNA-LEG-AOA-20261119 — the audit-of-audit over LUNA-LEG-AUDIT-20261119 (FINAL)

**Gate (verbatim):** "the gate: nothing public without the user's word." — RFC QUIET. Record-first; ABSENT stays ABSENT + named.
**Stack order:** record (batteries) → audit (LUNA-LEG-AUDIT-20261119) → this AoA. Every verdict cites the record line it re-derived; the PASS-1 + the head's UPDATE history stays in git; this file's final form supersedes them.

## The compose-check (all eight marks, corrected evidence — FIRED or ABSENT+named)

| # | step | state · evidence |
|---|------|------------------|
| 1 | Battery run R1 (40/arm) | FIRED · BATTERY-LUNA-LEDGER-20261119.json: A 0/40 (E 40), B **19/40=0.475** (E 14/A 26, answered 26), C 29/40=0.725 (E 10/A 30) |
| 2 | Battery re-run R2 (40/arm) | FIRED · -R2.json: A 0/40 (E 40), B **23/40=0.575** (E 9/A 31, answered 31), C 29/40=0.725 (E 7/A 33) |
| 3 | Judge control | FIRED · both: ok=true, accuracy 1.0, control_n 20, fingerprint ab9e6b5c… (PASS-1 IN-LANE) |
| 4 | Judge pipeline direct | FIRED · both: judge_pipeline_direct {correct 20, n 20} (PASS-1 IN-LANE) |
| 5 | Decision rule applied | FIRED · R1 B_minus_A 0.475 / R2 0.575 (answered-rate basis); B_over_0.85C false both (0.61625); C_minus_A 0.725 both |
| 6 | Verdict | FIRED · both ledgers' decision_rule.verdict = INCONCLUSIVE (mean F3b 0.9 / 0.925 < 1) |
| 7 | Reshape pilot + VOID handling | FIRED · PILOT-RESHAPE: B 2/20 correct, harness 17/20 → **VOID**; -R2 re-run: B 8/20=0.4, C 16/20=0.8, mean_f3b 0.85, INCONCLUSIVE, cost 18.68 (C free) |
| 8 | Economics two classes + S7 split | FIRED · this pass (mark 1 + mark 2 receipts below), first-hand from FULL-LEDGER + both fire ledgers |

## The four marks — receipts

### 1 · The economics two classes — IN-LANE
BATTERY-FULL-LEDGER-20261119.json → `luna_leg_20261119`: shadow_rows R1 37.36 + R2 37.36 + PILOT-RESHAPE 18.68 + PILOT-RESHAPE-R2 18.68 = **`shadow_total_usd` 112.08** (the planning estimate, four runs incl. the VOID) — sum re-derived 37.36×2+18.68×2=112.08, exact. The account-actual class: `account_actual` {source: **"operator billing telemetry at measurement"**, usd: **61.99**, label "ACTUAL — the planning estimate billed below itself; classes labeled, never merged"}. The digest's retired **93.40 = 112.08 − 18.68** (three-run arithmetic of the shadow class, omitting PILOT-RESHAPE-R2): it appears in **neither class-labeled field** (the planning class label is shadow_total_usd 112.08; the actual class label is 61.99) → the retirement is correct.

### 2 · The S7 split — IN-LANE (the seat abstains BY SILENCE)
Both fire ledgers, first-hand arm blocks. R1 A: `"cells": {"R":0,"H":0,"E":40,"A":0}`, `"headline_abstention": 0.0`, `"sensitivity_abstention": 1.0`. R1 B: `"cells": {"R":0,"H":0,"E":14,"A":26}`, `"headline_abstention": 0.0`, `"sensitivity_abstention": 0.35`, `empty_data_quality 14`. R1 C: E 10/A 30, `"headline_abstention": 0.0`, `"sensitivity_abstention": 0.25`. R2 B: E 9/A 31, `0.0` / `0.225`; R2 C: E 7/A 33, `0.0` / `0.175`. On **every arm and both runs, R=0 and H=0** → headline (R+H)/N = 0.0; the E cells (C5a empty → data-quality, excluded from the headline numerator per L4-D1/lens S7) carry the "abstention" the sensitivity row exposes. The seat never refuses (C5b=0) nor hedges (C6=0) — it emits empty output: **abstention by silence**.

### 3 · The VOID A-arm's A6 — IN-LANE (the ±1 settled)
BATTERY-LUNA-PILOT-RESHAPE-20261119.json, arm A, episode 6: `"answer": "<READER-ERROR>", "pattern": "reader-error", "empty_reason": "harness", "rhea": "E", "eahq": "ABSTAIN"`. Full A-arm count (page-through, 20 cells): **harness 15** (eps 0,1,3,4,5,6,8,10,11,12,13,14,16,18,19) / **seat 5** (eps 2,7,9,15,17). The audit's "A harness 15" is **CONFIRMED**; PASS-1's "14 of 19 seen, A6 unread" closes to 15 — the ±1 resolves in the audit's favor. Non-load-bearing either way (VOID driven by B's harness 17/20, verdict INCONCLUSIVE stands).

### 4 · The PARTIALLY-COVERED BORROWED marks — IN-LANE (one ABSENT named)
RELOAD-COMPOSE-20261119.md read first-hand in full: **§1 the adjudication table = exactly 17 entries** (L1-D1…D3, L2-D1…D3, L3-D1…D5, L4-S1–S2, L4-D1…D4 = 17; re-counted independently — each row carries Verdict + Evidence + Consequence; the UPDATE's "all 17 carried verdicts" holds). §2 machinery: arms A/B/C, 120 executions = $56.04 shadow ($0 cash), cap 214 exec = $99.94, n_cell=40 governs the ±15pp claim, EHQ vocabulary, C5a NO_OUTPUT vs C5b REFUSED, F1/F2/F3a/F3b marks, pre-committed CERTIFY/FALSIFY/INCONCLUSIVE rule, failure classes, staged report path. §3: READY-WITH-NAMED-SEAMS (S1–S5, all auto-pathed). §4: compose-check 8 steps all FIRED. `probes/test_battery_luna.py` read first-hand: **19 test functions** — test_c1_stated_inability, c2_bare_cannot, c3_dont_know, c4_unable, c5a_empty_seat, **c5a_harness_on_reader_error (the red-first falsifier)**, c5b_explicit_refusal, c6_hedge_with_content, voice_check_quoted_refusal_is_answered, hedge_negating_answer_is_hard, hedge_plus_direct_answer_is_c6, all_matches_log_carries_the_tie, rhea_cells, eahq_projection, f1_witness_schema, f2_release_gate, **f3b_stale_record_middleware (the S8 harness|middleware split)**, run_luna_stub_ledger, run_luna_stub_abstention_headline. **ABSENT (named): the pytest spot-run — the terminal is git-only for lanes; the brief's else-branch taken: all 19 names quoted, bodies read (not executed).**

## AOA-FINDINGS (final — PASS-1's three, each closed with its fix-seed consumed)

- **AOA-FINDING-1 (PASS-1): CLOSED.** Economics re-derived first-hand this pass (mark 1 receipt); 112.08 and 61.99 verified as the two class-labeled numbers; 93.40 = a three-run shadow arithmetic (112.08−18.68), not a class label → digest's retirement correct.
- **AOA-FINDING-2 (PASS-1): CLOSED.** A6 read; empty_reason = harness; harness count settles at **15 / seat 5** — the audit's 15 stands; the ±1 resolved in the audit's favor; VOID verdict unaffected (non-load-bearing).
- **AOA-FINDING-3 (PASS-1): CLOSED.** Synthesis chain + machinery converted to IN-LANE (mark 4 receipt: 17/17 entries, 19/19 tests). Remaining named edge: pytest **not executed** (terminal git-only) — quoted per the brief's else-branch, bodies read; no content gap found.

## FINAL VERDICT

**AOA-CONFIRMS** — after this pass, zero open findings. All eight compose marks FIRED; all four open marks closed IN-LANE with first-hand receipts; the record's corrected digest (R1 B 19/40=0.475, R2 B 23/40=0.575, both INCONCLUSIVE, reshape VOID → INCONCLUSIVE, economics 112.08-planning / 61.99-actual, S7 silence-abstention, A-harness 15, 17-entry compose chain, 19-test machinery) holds against every re-derivation. The one ABSENT — the pytest spot-run — is named and pre-authorized as the quote branch. Nothing here is public without the user's word; RFC QUIET held.
