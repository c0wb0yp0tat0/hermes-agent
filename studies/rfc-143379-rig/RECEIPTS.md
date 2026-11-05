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
