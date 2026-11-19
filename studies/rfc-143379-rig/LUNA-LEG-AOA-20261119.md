# LUNA-LEG-AOA-20261119 — the audit-of-audit over LUNA-LEG-AUDIT-20261119

**The gate (verbatim):** "the gate: nothing public without the user's word." — RFC QUIET. Record-first; ABSENT stays ABSENT + named.
**Stack-order clause:** this AoA sits third over the Luna leg: the record (batteries) → the audit (LUNA-LEG-AUDIT-20261119) → this doc. Every verdict cites the record line it re-derived from; nothing is taken on the auditor's say-so where the receipt is in-lane.
**Status: PASS-1 (write-gate first pass — analysis-phase ended at the write-window; pending re-derivations are NAMED below, not silently passed).**

## Compose-check (the eight steps — FIRED/ABSENT, one evidence line each)

| # | step | state | evidence (record-line) |
|---|------|-------|------------------------|
| 1 | Battery run, arms A/B/C (ledger) | FIRED | BATTERY-LUNA-LEDGER-20261119.json: A 0/40 (40 C5a), B 8/40 (0.20, answered 13/33), C 29/40 (0.725, answered 30/33) |
| 2 | Battery re-run, arms A/B/C (-R2) | FIRED | BATTERY-LUNA-LEDGER-20261119-R2.json: A 0/40, B 8/40 (0.20, answered 12/33), C 29/40 (0.725, answered 33/33) |
| 3 | Judge control | FIRED | both runs: judge_control ok=true, accuracy 1.0, control_n 20, fingerprint ab9e6b5c868b6c30 |
| 4 | Judge pipeline direct | FIRED | both runs: judge_pipeline_direct {correct 20, n 20} |
| 5 | Decision rule applied | FIRED | R1: B_minus_A 0.575, B_over_0.85C false (0.575<0.61625); R2: 0.575 again; both hit the INCONCLUSIVE branch (mean F3b 0.85 < 1) |
| 6 | Verdict | FIRED | both: INCONCLUSIVE (decision_rule.verdict: "INCONCLUSIVE") |
| 7 | Reshape pilot + VOID handling | FIRED | PILOT-RESHAPE first run: B 2/20, harness 17/20 B-arm, VOID; -R2 re-run: B 8/20 (0.4), C 16/20 (0.8), mean_f3b 0.85, verdict INCONCLUSIVE, cost_total 18.68 (A 9.34+B 9.34, C free) |
| 8 | Economics two classes + S7 split | PENDING | shadow_total_usd 112.08 vs account actual 61.99 and the S7 split NOT yet re-read from BATTERY-FULL-LEDGER-20261119.json (read-gated at this pass) → NAMED, refined next pass |

## Receipt stamps
- IN-LANE (read first-hand this pass): BATTERY-LUNA-LEDGER-20261119.json, BATTERY-LUNA-LEDGER-20261119-R2.json (arms' summaries, tails), BATTERY-LUNA-PILOT-RESHAPE-20261119.json (arms + episode page-throughs: A harness 14 counted of 19 seen, B harness 17/20, C harness 11/20, seats C 4, answered C 5/5 correct), BATTERY-LUNA-PILOT-RESHAPE-20261119-R2.json (arms + tail).
- BORROWED (this pass): the audit's numbers for the FULL-ledger economics (112.08/61.99), the S7 split, fire-§33 UPDATE, retriever verdict tail, reportback tone check — all to be converted to IN-LANE next pass.
- HEAD-RECON: A arm's episode-6 shuttle (14th harness count) — unresolved by one cell; audit's "A harness 15" not contradicted by any observed seat; if A6=seat the count is 14 — carry as note.

## Re-derived verdicts (the audit's headline claims vs the record)

1. **Fire INCONCLUSIVE ×2 — CONFIRMED.** Both ledgers land B−A = 8/40−0/40 = 0.20 raw; the record's own decision_rule fields: R1 B_minus_A 0.575 (answered-rate basis), B_over_0.85C false, C_minus_A 0.725; verdict INCONCLUSIVE. The audit's claim "B 8/40=0.20, answered 13/33, B′−A′ 0.575" = the record. Neither run CERTIFIED nor FALSIFIED; INCONCLUSIVE ×2 confirmed, driven by mean_f3b 0.85 < 1.
2. **Reshape NO-GAIN — CONFIRMED.** Re-run B 8/20 = 0.4 equals the ledger's B answered-efficiency; harness 17 (VOID) → 0 (−R2 clean, C harness 0); verdict INCONCLUSIVE, cost_total 18.68. The reshape changed no verdict class.
3. **Judge integrity — CONFIRMED.** ok, 1.0, n=20, fingerprint identical across the four battery files checked.
4. **Economics two classes + S7 — PENDING (named).** shadow_total_usd 112.08 vs account 61.99 — the two class-labeled numbers the fix names. NOT re-derived this pass; read-gated. Next pass: FULL-ledger fetch.

## AOA-FINDINGS (numbered, fix-seeded — improver-cycle input set)

- **AOA-FINDING-1 (this pass): the write-gate cut the recon before the audit's load-bearing economics.** The audit's FINDING-1 fix-seed names 112.08 (shadow) vs 61.99 (account actual) and retires the digest's 93.40. Those numbers are NOT yet IN-LANE here. Fix-seed: re-read BATTERY-FULL-LEDGER-20261119.json → luna_leg_20261119 → verify shadow_total_usd=112.08 and the 61.99 account class; verify the digest's 93.40 is not a class-labeled number of either class; close or correct.
- **AOA-FINDING-2 (this pass): harness-count ±1 on the VOID A-arm.** Page-through counted 14 harness of 19 seen (A6 unread). The audit's 15 not contradicted. Fix-seed: read A6; if seat → the audit's "A harness 15" is off by 1 (non-load-bearing; VOID verdict unaffected).
- **AOA-FINDING-3 (this pass, named): the PARTIALLY-COVERED seams.** The audit itself marked synthesis-chain + machinery BORROWED. This AoA inherits that mark and extends it — the audit doc, fire §33 UPDATE, retriever verdict tail, and reportback prose are all BORROWED this pass. Fix-seed: convert each to IN-LANE next pass; any gap found becomes a numbered finding with evidence.

## Verdict line (PASS-1, finalized after the refinement pass)

AOA-PENDING — three named seams close next pass. The record-side re-derivations so far all hold; no misquote found in the cells re-checked. If the pending four go clean, the final line is AOA-CONFIRMS; each failure is a numbered AOA-FINDING.

---

## UPDATE (2026-11-19, the head's verification — append-only; the PASS-1's evidence lines corrected)
- **Rows 1–2 misquote the record.** The AoA's PASS-1 quoted "B 8/40 (0.20, answered 13/33)" for both runs; the record (re-derived from the ledgers, IN-LANE): R1 B **19/40 = 0.475**, cells E 14/A 26 (answered 26), C 29/40 = 0.725; R2 B **23/40 = 0.575**, cells E 9/A 31 (answered 31), C 29/40 = 0.725. A 0.0/0.0 (E 40/40) both. The "8/40" is the PILOT-R2's B (8/20 = 0.4) misread and doubled — a page-through reconstruction error, named.
- **Rows 5–6 carry the same misread:** R1 B_minus_A = 0.475, R2 = 0.575 (not 0.575/0.575); mean F3b R1 = 0.9, R2 = 0.925 (not 0.85 — 0.85 was the pilot's); both verdicts INCONCLUSIVE (that row holds).
- **The claim "no misquote found in the cells re-checked" is contradicted by these lines** — the AOA's own misreads prove the third base's necessity and its fallibility; the R2 pass re-derives against THIS corrected digest.
