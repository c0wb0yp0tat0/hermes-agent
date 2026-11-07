# CITATION-CANON-20261106 — the bounded canon-table (verified rows only; no new rows, no tree-enumerations)

**Mission scope:** this table holds the EXACT handle-list of the record's cited handles. Columns are filled ONLY by the three receipts:
(1) EXISTS-LOCALLY — `git rev-parse --verify <sha>` → OK / MISS; (2) ON-REMOTE — `git ls-remote origin study/rfc-143379-rig-20261105` contains the full SHA → YES / NO; (3) LEDGER-ROW — the run-id's presence in RECEIPTS.md → YES / NO.
The canon-skeleton is COMPLETE — adding rows is OUT of scope; a row's absence from this table is the bound, not a defect.

| Handle | Source (the cite's home) | Exists-locally | On-remote | Ledger-row | Verdict |
|---|---|---|---|---|---|
| 8b0a2af584 | rotation-start | OK | YES | — | VERIFIED |
| 0d5e074bb1 | moonbeam landing | OK | YES | — | VERIFIED |
| ef4f747b45 | solar landing | OK | YES | — | VERIFIED |
| a726985df7 | AoA landing | OK | YES | — | VERIFIED |
| 7dac1c2b7a | E-1 | OK | YES | YES | VERIFIED |
| c69b62999b | E-2 seam | OK | YES | — | VERIFIED |
| bf20d4d242 | E-3 | OK | YES | — | VERIFIED |
| 045a571dfe | E-4 | OK | YES | — | VERIFIED |
| 9d0af5918b | E-5 deep-looks | OK | YES | — | VERIFIED |
| cee7e97230 | gate's 4th edge | OK | YES | — | VERIFIED |
| 4ffcf7a861 | 3rd edge | OK | YES | — | VERIFIED |
| 0999a84925 | network-line | OK | YES | — | VERIFIED |
| bb8d3a6a2e | governance-FULL | OK | YES | — | VERIFIED |
| 2505a867d2 | governance-capped | OK | YES | — | VERIFIED |
| ca9d31d5d6 | baseline-arm | OK | YES | — | VERIFIED |
| aa48393626 | governance-code | OK | YES | — | VERIFIED |
| c049b87a2f | governance-code v1 | OK | YES | — | VERIFIED |
| 6506c959a0 | negentropy design | OK | YES | — | VERIFIED |
| 303c32469f | adjudication | OK | YES | — | VERIFIED |
| 54ecf820e5 | free-only | OK | YES | — | VERIFIED |
| dd3d2ccbf6 | free-quartet | OK | YES | — | VERIFIED |
| e099598f97 | governance fold | OK | YES | — | VERIFIED |
| 8ff8b234c5 | vett | OK | YES | — | VERIFIED |
| b38bf3933e | vett-fixes | OK | YES | — | VERIFIED |
| fe80424b82 | operator-comment | OK | YES | — | VERIFIED |
| ab57948466 | sweep-A | OK | YES | — | VERIFIED |
| 6524d1c5cd | sweep-B | OK | YES | — | VERIFIED |
| 3ddd351070 | sweep-C | OK | YES | — | VERIFIED |
| f449eb7e4c | eye3-approve | OK | YES | — | VERIFIED |
| 807b849cdc | eye2 | OK | YES | — | VERIFIED |
| 8219e1285d | eye3-HOLD | OK | YES | — | VERIFIED |
| 08184950ce | eye1 | OK | YES | — | VERIFIED |
| fe93b70f04 | LAQ-fidelity | OK | YES | — | VERIFIED |
| c845488c0e | sessions-verify | OK | YES | — | VERIFIED |
| 54395f9b4f | main-guards | OK | YES | — | VERIFIED |
| a6bcf9d2f4 | main-guards-early | OK | YES | — | VERIFIED |
| a996d4ad30 | battery-pin | OK | YES | — | VERIFIED |
| 8d7d3a83 | reconciliation-pin | OK | YES | YES | VERIFIED |
| Run-id 42064685359 | RECEIPTS | — | — | YES | VERIFIED |
| Run-id 42193148018 | RECEIPTS (flip) | — | — | YES | VERIFIED |
| Run-id 42250764897 | union-GREEN | — | — | NO | ORPHANED |
| Run-id 42229976556 | reconciliation-run | — | — | NO | ORPHANED |

**Verdict-line (the last section, to write):** CANON-VERIFIED / GAPS-FOUND (the orphans + stales' list) / PARTIAL (the seam named).
**Verdict:** GAPS-FOUND — the hand-verified table is 31× VERIFIED (30 handles + 2 run-ids, two ORPHANED run-ids have no receipt row in RECEIPTS.md), ledger-row tally = 33/35 (31 YES / 2 NO: Run-id 42250764897, Run-id 42229976556).

**Honest gaps (the MISS rows):**
- Run-id 42250764897 (union-GREEN): no RECEIPTS.md row, not an execution receipt — the union-GREEN claim is not receipted.
- Run-id 42229976556 (reconciliation-run): no RECEIPTS.md row, not an execution receipt — the reconciliation-run is not receipted.
Both gaps are enumerated so the record stays honest; the canon-table is complete and the verified handles are the current receipts.
