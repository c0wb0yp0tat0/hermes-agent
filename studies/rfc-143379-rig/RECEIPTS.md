# RECEIPTS — the rig's Avrea-leg receipt ledger (RFC #143379 study)

Every row is run-backed: the run id, the pin, requested == executed asserted in-run, the real numbers. A committed workflow definition is NOT execution; NOT RUN stays NOT RUN until the receipt exists.

| Pin | What it is | Run | requested == executed | Battery | Conclusion |
|---|---|---|---|---|---|
| d1bdb4582cd5d16be6a6b486f696f8240c222b96 | #139606 merge head (the seven-stage write-gate acceptance pipeline) | [42064685359](https://github.com/c0wb0yp0tat0/hermes-agent/actions/runs/42064685359) | PASS — asserted in-run (requested_sha == executed_sha == d1bdb4582…) | **117 passed, 10 skipped in 6.49s** (write-gate + memory-tool; the 10 skips = the doc-chain probes absent at this pin, `-rs` reasons recorded) | **GREEN** |
| a996d4ad3039e280dc21e9b558f5a44c081dda42 | the whole-anchor structural resolution ("the strengthened arms flip GREEN") | host-local run, 2026-11-05 | (local checkout of fixes/falsifier-battery-20261104) | **28 passed, 1 xpassed in 1.01s** (the 11 falsifier arms: nugget 1–6, the mutated substring-orphan case, the #141876 composition arms) | **GREEN** — the xpassed IS the strengthened arm's flip |
| ffb85c2c58 | #140008 head (session preservation + dream cycle) | — | — | — | **NOT RUN** |
| 60a2e15638 | #116673 head (the bounded read — MEMORY.md anchors a doc chain) | — | — | — | **NOT RUN** |
| ec649ad9d | #141876 head (the read restore — the RFC's landing-order first piece) | — | — | — | **NOT RUN** |
| the GitHub-window side | the hosted ubuntu-latest queue | — | — | — | **NOT RUN** (the hosted queue class on this account; the Avrea side is the live surface) |

## The honesty markers
- A green run at a pin qualifies THAT pin's checked-out source — not any other head, not the upstream composition.
- Skipped counts ride their `-rs` reasons, never silent.
- The 300+ cycle long-session gate at 4×–8× (the RFC's hard gate): NOT RUN on a fixed ruler — the probe's scope bug is acknowledged and the RFC's own measurement protocol forbids a certifying run on the old probe.
- Divergence between the Avrea side and the GitHub-window side is data, recorded, never smoothed.
