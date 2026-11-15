# LAUNCH-COVERAGE — Slice-B (coverage-table), t=0 launch
Register: plain, evidence-carrying. Direct-applicable. Limit ~10m.

## Coverage-table (item | source-plan | t-window | owner)

| # | Item | Source-plan | t-window | Owner |
|---|------|-------------|----------|-------|
| 1 | Byte-closure triple guard (HEAD==pinned SHA, diff --stat empty, plan sha256 recorded) | Orchestration §1 S0 | T-0 (pre-go) | SOLAR (launch) |
| 2 | Operator `go` on byte-closure triple → S0→S1 | Orchestration §1/§2; Launch §2/§3 | t=0+0s | OPERATOR (via OPS-CONSOLE) |
| 3 | G0 mission-intent lock (single sentence) armed | Launch §1.1 | armed T-0 (always on) | SOLAR |
| 4 | G1 dispatch-route primed (payload hash) | Launch §1.1 | armed T-15m | DISPATCH |
| 5 | G2 first-hour block loaded (6 items) | Launch §1.1 | armed T-10m | SOLAR |
| 6 | G3 go/no-go surface live (single signal) | Launch §1.1 | armed T-5m | OPS-CONSOLE |
| 7 | G4 mission-clock re-anchor ready (t=0 wired) | Launch §1.1 | armed T-2m | CLOCK |
| 8 | t=0+0s G0 fires: intent broadcast + clock re-anchor | Launch §1.2/§2 | t=0+0s | SOLAR |
| 9 | t=0+5s G1 fires: first dispatch to primary lane | Launch §1.2 | t=0+5s | DISPATCH |
| 10 | t=0+15s G2 fires: first-hour item #1 begins | Launch §1.2 | t=0+15s | SOLAR |
| 11 | t=0+30s G3 flips GREEN-LOCKED | Launch §1.2 | t=0+30s | OPS-CONSOLE |
| 12 | t=0+45s G4 fires: clock re-anchor broadcast (lanes adopt t=0) | Launch §1.2 | t=0+45s | CLOCK |
| 13 | First-hour block items 1-6 (intent+anchor; dispatch lands; probe; drift check; second dispatch; seal) | Launch §1.3 | t=0+0m..t=0+58m | SOLAR / DISPATCH / VERIFY |
| 14 | Hour-1 six-item block (B4 probe, K-recency honest-negative, certifying re-run, instrument-inclusive sweep, upstream-mergeable pass, gates' frame) | Orchestration §1 S1; Synthesis §2 | t=0..60 (S1 ARM) | METER-BUS / GATE-KEEPER / FANOUT-HANDLER |
| 15 | Roles load: METER-BUS, GATE-KEEPER, FANOUT-HANDLER | Orchestration §1 S1 | t=0..60 | (role-load) |
| 16 | Lanes A-E arm in parallel (C44-pilot, gate-scan, G5-G7 populate, SOFT-pool queue, fleet baseline) | Orchestration §1 S2 | t=60..90 | (lane owners) |
| 17 | Queue-age watchdog (>30s queued → re-fire v2) | Stall-proofing §1 S1/§2 | t=0+ (continuous) | (watchdog surface) |
| 18 | Label↔branch invariant check at spawn | Stall-proofing §1 S2 | t=0+ (at spawn) | (spawn guard) |
| 19 | Cadence-freshness probe (>15m stale → re-arm) | Stall-proofing §1 S3/§2 | t=0+ (continuous) | (watchdog surface) |
| 20 | Batch-post rows + drip-detector | Stall-proofing §1 S4 | t=0+ (continuous) | (watchdog surface) |
| 21 | Fan liveness heartbeat every 60s; re-spawn on miss | Stall-proofing §2 | t=0+ (continuous) | (supervisor) |
| 22 | Runner-loop arm-probe proof (dispatch label → runner pull/build/run → report) | Runner-loop §3 | Week 1 (post-launch) | (runner) |
| 23 | Synthesis contradiction-scan resolutions (7) land in constitution/recipe/landing | Synthesis §3 | pre-t=0 (armed) | (synthesis) |
| 24 | Constitution gates sequence (evidence → verification → fold) per leg | Synthesis §1 | per-leg, from t=0 | (gates) |

## 5-why (own, depth-clause)
Q1 Why does launch coverage matter? → without it, t=0 fires partial.
Q2 Why partial fire? → items not named/owned/timed slip silently.
Q3 Why slip? → no single table binding source→timing→owner.
Q4 Why no table? → plans live in 5 files; nobody cross-read.
Q5 Why cross-read now? → this slice IS the cross-read; closure = table above.

Systemic remediation: keep this table as the single launch contract; any new t=0 item must land here first or it doesn't fire.

## Webstorm (possibilities sweep)
- Mechanism A: per-plan owner re-verifies their rows at T-5m (gate G3 surface). Adoption seam: G3 meter row already exists. Meter: all 24 rows ACKed before GO enabled.
- Mechanism B: watchdog auto-blocks GO if any row unowned/un timed. Adoption seam: stall-proofing queue-age surface. Meter: GO button disabled until coverage-complete.
- Mechanism C: post-launch, runner-loop receipt re-verifies each item's execution. Adoption seam: runner-loop §2 receipts. Meter: per-item receipt hash on PR.

## DIRECT-APPLICABLE
Fire the §1.2 sequence only; coverage table above is the checklist. No partial fire.
