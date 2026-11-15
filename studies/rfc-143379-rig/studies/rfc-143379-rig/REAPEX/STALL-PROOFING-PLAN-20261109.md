# THE STALL-PROOFING'S PLAN — Resilience-Plan (Deep)

Mission-of-missions: survive its failures. Failures are findings; momentum never stalls.

## (1) THE STALL-REGISTRY (every stall-class + mechanized prevention)

| # | Stall-class | Evidence (today) | Prevention (mechanized) |
|---|---|---|---|
| S1 | queued-forever | dispatch rows sit `queued` past TTL; no re-arm | queue-age watchdog: any row `queued` > 30s → auto re-fire with v2 transport; emit `stall+refire` envelope |
| S2 | label-misreads | lane label vs branch mismatch → work lands on wrong lane | label↔branch invariant check at spawn: assert lane-tag == branch-prefix; fail fast, no silent misroute |
| S3 | cadence-lapses | harness pass at 02:31 then 0-byte runs; cadence died | cadence-freshness probe: last-success timestamp; if > N min stale → re-arm harness + re-run |
| S4 | row-drips | rows posted one-at-a-time, momentum bleeds | batch-post rows; drip-detector counts rows/min; below threshold → consolidate + re-fire |
| S5 | fan-waits | deeper-planning fan blocks on head/operator absence | autonomy scope (§3): fan never waits; head/operator optional, not gating |

## (2) LOOP'S SELF-HEALING (watchdog surfaces)

- **queue-age surface**: monitor every queued row's age; threshold 30s; action = re-fire via v2 transport; log `stall+refire`.
- **cadence-freshness surface**: track last successful harness run; threshold 15 min; action = re-arm + rerun harness.
- **fans' liveness surface**: each fan emits heartbeat every 60s; missing heartbeat → supervisor re-spawns fan; no head round-trip.
- **automatic re-arms**: all three surfaces self-trigger; no manual approval; failures recorded as findings (not blockers).

## (3) MO-MENTUM'S GUARANTEE (autonomy scope)

- The loop never waits on the head or the operator's absence.
- Head/operator are optional inputs, never gates: if absent, fan proceeds with last-known directive + receipts.
- Momentum guarantee: at least one forward artifact per cadence tick (row, refire, or finding); a tick with zero artifacts = stall → triggers S1/S3 watchdog.
- Scope boundary: autonomy covers re-arming, re-firing, re-spawning; does NOT cover scope changes (those still require head).

## DIRECT-APPLICABLE

Wire the three watchdog surfaces into the existing harness; thresholds as above; emit envelopes on every re-arm. No prayers.
