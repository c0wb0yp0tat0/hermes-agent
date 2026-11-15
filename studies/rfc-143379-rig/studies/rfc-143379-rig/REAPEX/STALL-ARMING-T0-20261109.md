# t=0 WATCHDOG-ARMING — STALL-PROOFING SLICE-C

## Arming Rows

| # | Surface | Metric | Threshold | Cadence | Owner | Action on breach |
|---|---------|--------|-----------|---------|-------|------------------|
| A1 | queue-age | age of any row in `queued` state | 30s | probe every 10s (3x within threshold window) | harness watchdog (auto) | re-fire via v2 transport; emit `stall+refire` envelope |
| A2 | cadence-freshness | seconds since last successful harness run | 15 min (900s) | probe every 60s | harness watchdog (auto) | re-arm harness + re-run; emit `stall+refire` envelope |
| A3 | fan-liveness | seconds since last fan heartbeat | 60s (one missed beat) | fan emits every 60s; supervisor polls every 30s | supervisor (auto) | re-spawn fan; no head round-trip; emit `stall+refire` envelope |

## 5-Why (why the mission could still stall despite these)

1. Why could A1 miss a stall? → probe cadence (10s) < threshold (30s) gives 3 samples; but a row queued at 0s that completes at 29s never trips — borderline OK, but a row queued at 29s and probed at 30s trips at 31s actual. Acceptable slop (1s). Mitigation: threshold measured from enqueue timestamp, not probe time.
2. Why could A2 fail? → "last successful harness run" must be persisted across harness restarts; if state is in-memory only, a restart resets the clock and masks a stall. Mitigation: persist last-success to disk (append-only stamp file) and read on boot.
3. Why could A3 fail? → supervisor itself could die; then no re-spawn. Mitigation: supervisor heartbeat is watched by an external cron (host-level, not in-process) with its own 120s threshold.
4. Why could all three pass yet momentum die? → a tick produces zero artifacts (no row, no refire, no finding) but no single surface trips. Mitigation: momentum-guarantee check counts artifacts per tick; zero → synthetic stall → triggers A1 (re-fire) as the fallback surface.
5. Why does any of this matter if head/operator absent? → it doesn't; autonomy scope (§3) makes surfaces self-triggering with no approval gate. That is the point — these rows are the gate, not the head.

## Webstorm (external sanity)

- Stall-proofing as a pattern: watchdog probes with threshold < cadence-window and self-triggered re-arm is standard (systemd Restart=on-failure, Kubernetes liveness probes). Thresholds of 30s/15min/60s are within normal operational envelopes; no external source contradicts.
- Risk: thundering-herd if many rows age out simultaneously → v2 transport re-fire must be rate-limited (not specified in plan; flag as open item).

## Open items
- Rate-limit on bulk re-fire (A1) — unspecified; recommend max 1 re-fire per 10s per lane.
- Supervisor external cron (A3 mitigation) — not yet wired; needs host-level cron entry.

## DIRECT-APPLICABLE
Wire A1/A2/A3 into existing harness; thresholds as above; emit envelopes on every re-arm. No prayers.
