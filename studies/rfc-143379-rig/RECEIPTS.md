# RECEIPTS — the rig's Avrea-leg receipt ledger (RFC #143379 study)

Every row is run-backed. A receipt cites the run id, the pin, the asserted equality, and the conclusion. Nothing is claimed before its receipt exists; NOT RUN stays NOT RUN.

| Date (UTC) | Pin | Run | requested == executed | Conclusion | Notes |
|---|---|---|---|---|---|
| 2026-11-05 | d1bdb4582cd5d16be6a6b486f696f8240c222b96 (#139606 merge head) | 42064685359 | PASS (asserted in-run) | **GREEN** | write-gate + memory-tool battery at the pin; the first composition pin, receipted |
| 2026-11-05 | a996d4ad3039e280dc21e9b558f5a44c081dda42 (whole-anchor resolution head) | (host-local run) | (local checkout) | **GREEN** | falsifier battery: 28 passed, 1 xpassed in 1.01s — the strengthened arm flips |
| — | ffb85c2c58 (#140008) | — | — | **NOT RUN** | receipt lands when the runner lands the pin |
| — | 60a2e15638 (#116673) | — | — | **NOT RUN** | receipt lands when the runner lands the pin |
| — | ec649ad9d (#141876) | — | — | **NOT RUN** | receipt lands when the runner lands the pin |
| — | the GitHub-window side | — | — | **NOT RUN** | the hosted queue class — the ubuntu-latest runs queued forever on this account; the Avrea side IS the live surface |

## The number-seam resolution (the battery's truth)
The falsifier battery at the whole-anchor head records **28 passed, 1 xpassed in 1.01s** — an xpassed (an expected-failure that PASSED) is the strengthened arm flipping GREEN on the resolution. The "xfailed 1.83s" phrasing that appeared in one landing was a mislabel, corrected on the record.

## The honesty markers
- Committed workflow definitions are not execution.
- A green run at a pin qualifies THAT pin's checked-out source — not any other head.
- Divergence between the Avrea side and the GitHub-window side is data, recorded, never smoothed.
