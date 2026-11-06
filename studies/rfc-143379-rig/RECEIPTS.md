# RECEIPTS — the rig's Avrea-leg receipt ledger (RFC #143379 study)

Every row is run-backed. A receipt cites the run id, the pin, the asserted equality, and the conclusion. Nothing is claimed before its receipt exists; NOT RUN stays NOT RUN.

| Date (UTC) | Pin | Run | requested == executed | Conclusion | Notes |
|---|---|---|---|---|---|
| 2026-11-05 | d1bdb4582cd5d16be6a6b486f696f8240c222b96 (#139606 merge head) | 42064685359 | PASS (asserted in-run) | **GREEN** | write-gate + memory-tool battery at the pin; the first composition pin, receipted |
| 2026-11-05 | a996d4ad3039e280dc21e9b558f5a44c081dda42 (whole-anchor resolution head) | (host-local run) | (local checkout) | **GREEN** | falsifier battery: 28 passed, 1 xpassed in 1.01s — the strengthened arm flips |
| 2026-11-05 | ffb85c2c5880672237e1a48bea383f634df70985 (#140008) | 42071651022 | PASS — requested == executed == ffb85c2c5880672237e1a48bea383f634df70985 | **GREEN** | 64 passed in 5.06s — write-gate + memory-tool + falsifier-battery at the pin |
| 2026-11-05 | 60a2e1563802368b46018bba2a70f11de31a6b0a (#116673) | 42071665270 | PASS — requested == executed == 60a2e1563802368b46018bba2a70f11de31a6b0a | **GREEN** | 66 passed in 5.19s — write-gate + memory-tool + falsifier-battery at the pin |
| 2026-11-05 | ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a (#141876) | 42071680606 | PASS — requested == executed == ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a | **GREEN** | 82 passed in 5.72s — write-gate + memory-tool + falsifier-battery at the pin |
| — | the GitHub-window side | — | — | **NOT RUN** | the hosted queue class — the ubuntu-latest runs queued forever on this account; the Avrea side IS the live surface |

## The number-seam resolution (the battery's truth)
The falsifier battery at the whole-anchor head records **28 passed, 1 xpassed in 1.01s** — an xpassed (an expected-failure that PASSED) is the strengthened arm flipping GREEN on the resolution. The "xfailed 1.83s" phrasing that appeared in one landing was a mislabel, corrected on the record.

## The honesty markers
- Committed workflow definitions are not execution.
- A green run at a pin qualifies THAT pin's checked-out source — not any other head.
- Divergence between the Avrea side and the GitHub-window side is data, recorded, never smoothed.
| 2026-11-05 | c39d8ce722d4c5d43a3aa2ea3e71f698f500d870 (round2-combined-substrate, the offering lineage) | 42074781407 | PASS — requested == executed == c39d8ce7… | **GREEN** | 70 passed in 5.24s — the write-gate + memory-tool battery at the lead |
| 2026-11-05 | a996d4ad3039e280dc21e9b558f5a44c081dda42 (fixes/falsifier-battery-20261104, the whole-anchor head) | 42074793218 | PASS — requested == executed == a996d4ad… | **GREEN** | 98 passed, 1 xpassed in 5.85s — the full battery incl. the falsifier arms; the xpassed = the strengthened flip |
| 2026-11-05 | 490527023765ffd901e72d85fc43e60560e5aabd (avrea-parallel, the runner-env head) | 42074804475 | PASS — requested == executed == 49052702… | **GREEN** | 89 passed, 1 xfailed in 5.74s — the improver-audit's runner-env figure now VERIFIED on the lead itself |


## RECEIPTS 2026-11-05 (the apex day's rows)
| When | What | Result | Evidence |
|---|---|---|---|
| 19:43Z | falsifier-battery @ the whole-anchor (a996d4ad30) - the first dedicated falsifier run | GREEN | run 42096454325 |
| 19:43Z | union @ the arm-head (a3a9fb8ccd) | RED | run 42096273475 - the nugget-6 substrate-absent class (fixed: the guarded falsifier into the pin-trees, 76f95dd401) |
| 19:44Z | sweep @ the study-head (35ed130686) | RED | run 42096589644 - the same class; the sweep re-runs carry the guard |
| 19:50Z | union @ the arm-head (re-run) | RED | run 42098517565 - the pin-tree still unguarded at dispatch; the guard landed after (76f95dd401) |
| 20:26Z | union @ the study-head (76f95dd401, first guarded attempt) | RED | run 42103142238 - the strengthened-nugget's missing guard + the landing's same-step env (both fixed: 537b069343 + b5e21403de) |
| - | the xngg-gaps verification (4 gaps at the pins) | 2 CONFIRMED / 1 not-reproduced / 1 partially-open | XNGG-GAPS-VERIFICATION-20261105.md (35ed130686) |
| - | the alignment's hybrid README (the paid pod's product) | landed, fidelity-checked | eb57ddbe63 |
| - | the fleet's first fold (the longcat divergence) | landed + byte-verified | 77a441dc92 + the wave-5 (6ded14715c) |

| 01:50Z | union @ the guarded head (d6619c3654) - avrea surface | RED | run 42146442559 - 5 failed / 16 passed / 72 skipped (the guards firing; the 5's names captured next run via -rf) |
| 01:50Z | union @ the pre-guard head (91e31669c7) - the HOSTED window (the NOT-RUN line's first fire) | RED | run 42146330495 - the write-class at its pin, the window now opened |
