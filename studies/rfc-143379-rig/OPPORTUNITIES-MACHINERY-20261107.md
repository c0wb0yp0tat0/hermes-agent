# OPPORTUNITIES-MACHINERY-20261107.md — lower-priority opportunities (machinery surface)

1. Surface: 16 live crons. Opportunity: add a cron-surface audit lane (idle/stale cron detection, dedup of overlapping schedules, failure-retry caps). Value: reduces recurring cron drift and silent no-ops; frees operator attention. Dependency: cron list + last-run timestamps access; cron-surface-ops skill.

2. Surface: copycat-harness.py knobs. Opportunity: expose a knob for chunked/batched writes and a dry-run mode for over-budget writes instead of hard refuse. Value: eliminates recurring write-gate REFUSE char-cap (500/10000) failures. Dependency: harness source edit + tests; write-gate contract.

3. Surface: 31 forks' motion (gh api). Opportunity: a fork-status sweep that flags forks with upstream drift > N commits or stale PRs, auto-labels. Value: prevents fork rot; surfaces mergeable work. Dependency: gh api rate budget; fork list inventory.

4. Surface: known mine classes (char-cap over-budget writes, anchor-drift stale entries, model-404 free-periods, telegram dual-stack failures, ENOSPC, otel timeouts, managed-worker sync-rpc). Opportunity: a mine-class registry with per-class detector + suggested lane, so new occurrences auto-route. Value: converts recurring pain into tracked, addressable items. Dependency: MINES-20261107.md as seed; detector hooks in logs.

5. Surface: untapped doctrine (substrate→surface→amplifier build order). Opportunity: wire the build order into mission-shape planning templates as a required section. Value: prevents surface-first/amplifier-first builds that skip substrate. Dependency: mission-shape template edits; doctrine source.

6. Surface: anchor-drift stale entries. Opportunity: a stale-entry reaper that re-validates staged entries before write, auto-refreshing anchors. Value: reduces anchor-drift refusals and re-reaching. Dependency: write-gate anchor validation code.

7. Surface: model-404 free-periods (Ornith). Opportunity: a model-availability probe + fallback chain in inference config. Value: graceful degradation on free-period end. Dependency: model registry; provider config.

8. Surface: telegram dual-stack failures. Opportunity: transport health-check with IPv4 fallback as first-class retry, logged. Value: fewer ConnectError outages. Dependency: telegram gateway transport code.

9. Surface: ENOSPC / disk-full. Opportunity: host-storage recovery lane wired into gateway exit diag (auto-pause non-essential writes). Value: prevents gateway crashes from disk-full. Dependency: disk-lockdown-recovery skill; storage thresholds.

10. Surface: otel timeouts (port 3000). Opportunity: trace export backoff + queue with drop-on-overflow and status metric. Value: observability lane degrades gracefully instead of timing out. Dependency: otel exporter config.

11. Surface: managed-worker sync-rpc on event loop. Opportunity: move WorkerPersistenceError path to async/off-loop execution. Value: removes synchronous_rpc_on_event_loop recurrence. Dependency: managed worker code; async refactor.

12. Surface: scratch prune removing working artifacts. Opportunity: artifact allowlist / protected paths in prune. Value: stops loss of in-progress work. Dependency: prune script config.

Count: 12. Top machinery opportunity: chunked/batched writes for char-cap over-budget (copycat-harness write-gate knob) — directly addresses the top recurring mine pattern.
