# LUNA-LEG-AOA-20261119-R2-brief.md — the audit-of-audit, re-fired (a third base verifies the auditor — re-derive against the corrected digest)

*You are the AUDIT-OF-AUDIT over the Luna leg's record and its independent audit — the RE-FIRE. The first pass landed PASS-1 with evidence lines that misquote the record (its rows 1–2 read "B 8/40 (0.20)" where the ledgers hold 19/40 and 23/40; its decision-rule rows carried the PILOT's numbers as the fire's). The head's verification UPDATE appended to `LUNA-LEG-AOA-20261119.md` carries the corrected digest. THIS brief repeats the corrected record so your re-derivations verify against it — reads are confirmation, never reconstruction. Read the audit + its UPDATE + the corrected digest, complete the PENDING eighth mark, and render the true verdict.*
*The gate: "the gate: nothing public without the user's word." RFC QUIET. Record-first; ABSENT stays ABSENT + named.*

write-window: 16

## THE CORRECTED DIGEST (the head's verified re-derivation, IN-LANE from the ledgers — verify by reading, never by repeating the old quotes)
- **Fire R1** (`probes/BATTERY-LUNA-LEDGER-20261119.json`): A 0.0 (E 40/40); B **19/40 = 0.475** (cells E 14 / A 26 — answered 26); C 29/40 = 0.725 (E 10 / A 30). B_minus_A **0.475**; B_over_0.85C False (0.475 < 0.61625); mean_f3b **0.9** (4 harness reasons); verdict INCONCLUSIVE.
- **Fire R2** (`-R2.json`): A 0.0 (E 40/40); B **23/40 = 0.575** (cells E 9 / A 31 — answered 31); C 29/40 = 0.725 (E 7 / A 33). B_minus_A **0.575**; B_over_0.85C False; mean_f3b **0.925** (3 harness reasons); verdict INCONCLUSIVE.
- **Pilot (VOID)** (`BATTERY-LUNA-PILOT-RESHAPE-20261119.json`): A 0.0 (E 20); B 0.1 (3/20 answered, 17 harness-class empties); C 0.25 (5/20 answered, 11 harness-class); route 503-window — VOID, not a measurement.
- **Pilot R2** (`-R2.json`): B **8/20 = 0.4** (10/20 answered); C 16/20 = 0.8; mean_f3b 0.85 (3 harness); the reshape's paired same-seed verdict: B′ 8/20 vs banked R1 10/20, R2 9/20 → NO GAIN.
- **Economics** (`probes/BATTERY-FULL-LEDGER-20261119.json` → `luna_leg_20261119`): shadow_total_usd **112.08** (the planning estimate, 4 runs incl. the VOID) vs the account's actual **$61.99** (the operator's billing telemetry) — the two classes, labeled, never merged.
- **The S7 split** (re-verify from the ledgers' arm blocks): headline_abstention (R+H)/N = 0.0 on every arm vs sensitivity_abstention 1.0/0.35–0.225/0.25–0.175 — the seat abstains BY SILENCE; the report-back says it in prose.
- **The champion row** (`SPRINT-FIRE-SEQUENCE-20261119.md` §33 UPDATE): arm A stands, the INCONCLUSIVE pair is the honest row; the reshape joins the dead-end registry.
- **The report-back** (`REPORTBACK-NULL-PROSE-20261119.md`): the tone contract's seven rules vs the draft — checked by the audit; DRAFT-NOT-POSTABLE tail.

## YOUR DUTY (the AoA's questions, re-fired)
1. **Did the audit hold?** Its verdict (AUDIT-FINDINGS 1 — PASS-grade, the single finding in the input set) vs the corrected record: re-verify the audit's re-derived claims against the digest above; any residual misquote, any verdict softer/harder than the record.
2. **The PASS-1's own seams:** its PENDING eighth mark (the economics two classes + S7 split — complete it now, IN-LANE); the misquote rows corrected by the UPDATE — did the UPDATE's corrected numbers hold on your read?
3. **What did the audit (and the AoA pass-1) miss?** The synthesis chain + the machinery (PARTIALLY-COVERED, BORROWED — the third base's seam); anything the two passes smoothed over.
4. **The verdict line:** `AOA-CONFIRMS` (both the audit and this pass hold against the corrected record) / `AOA-FINDINGS <n>` (each finding: evidence + fix-seed — the improver cycles' input set).

## THE DELIVERABLE
`LUNA-LEG-AOA-20261119.md` — REWRITE the file with the complete AoA: the compose-check table (all eight marks, FIRED/ABSENT with the corrected evidence lines), the receipt stamps (IN-LANE / BORROWED / HEAD-RECON), the findings numbered with fix-seeds, the verdict line. (The PASS-1 + the UPDATE stay in git history — append-only above is preserved; the file's final form supersedes them.)

## THE CONTRACT (binding)
The gate verbatim · the stack-order clause · the review-loop (draft → stranger re-read → refine one pass per finding → 3–4 adversarial pushbacks → termination: no-change re-read twice) · one tool call per round · skeleton by ~round 4 · real content only (never a stub marker; an unfinished pass is the honest partial with NOT-CONFIRMEDs named) · ≤6,000 chars per write · commit before exit (add → commit → push; pull --rebase on rejection; do not exit until the commit succeeded).
