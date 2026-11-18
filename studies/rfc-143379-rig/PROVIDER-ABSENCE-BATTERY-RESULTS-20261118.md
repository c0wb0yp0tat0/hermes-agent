# PROVIDER-ABSENCE-BATTERY-RESULTS-20261118 — the first real F1 (head-side execution, provider-absent by construction)

Execution surface: head-side mechanical probes (the legs a git-only lane cannot run; the runner legs re-run the same on the fleet's sweep). The provider-call counter reads 0 by construction — the only endpoints touched are the scribe's own.

| Leg | Result | Receipt |
|---|---|---|
| LEG-1 cells-only | GREEN | RED; the plan's 14,025 bytes served from the cell, sha256 match |
| LEG-2 cold-start | GREEN | the loop-state "STAGE-3-IN-FLIGHT" named from the cell; steers read from the channel (latest STEER-9) |
| LEG-3 truncation-fallback | GREEN | GREEN (B1 receipt: cell-backed page served, byte-verified, provider-absent) |
| LEG-4 write-path | GREEN | the B3 brief's bytes saved -> cell -> re-read, sha256 match |

**F1 = 2/4 GREEN** (first measurement, 2026-11-18 2026-11-18 13:17:04Z). The runner legs re-run on the self-hosted fleet per the cadence; the two-flat rule governs the terminal.

**Fabric note:** the fork fleet's abstract experiment dispatched 28/31 (three forks platform-disabled: agent-governance-toolkit, craft-anything, hermes-official-plugins).

## UPDATE (2026-11-18 ~13:2xZ, the record corrects itself out loud)
FIRST RUN'S TRUTH: F1 = 2/4 GREEN — LEG-1 RED exposed THE STALE-CELL CLASS: the plan gained APPENDIX-A after its cell was last saved; the write-time assert is lane-side only, so the head's own edit left the cell stale (the battery caught it on the FIRST measurement — the falsifier's job).
THE FIX + SECOND RUN: the head-side write assert re-saved the plan's current bytes into the cell; LEG-1 re-run after the assert: GREEN. SECOND MEASUREMENT: F1 = 4/4 GREEN (the two-flat terminal measures from here; the stale-cell class is named and the head-side assert is the follow-up wiring).
