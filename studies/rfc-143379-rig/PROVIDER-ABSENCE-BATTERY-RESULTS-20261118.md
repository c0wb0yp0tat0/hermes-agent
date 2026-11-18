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
