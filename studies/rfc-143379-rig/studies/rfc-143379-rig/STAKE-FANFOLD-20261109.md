# STAKE-FANFOLD-20261109 — Fan-Topology + Fold-Banking (FAN+FOLD Slice, 4-hour Sprint)

Status: operative. Nothing public. Compose-check pending.

## 1. Fan-Topology (phase fan-widths + cross-check density + bandwidth rule)

Driver review bandwidth unit (B) = one driver can fully review 3 fan outputs per 30m fold window (≈ 3 parallel agents, cross-checked). Fan-scale rule: fan-out ≤ 3 × B per phase; beyond that, split into sub-missions.

| Phase | Fan-out (agents) | Cross-check density (reviewers per fan) | Mechanism | Fold artifact |
|-------|------------------|----------------------------------------|-----------|---------------|
| Phase 0 — loot triage | 1 driver (no fan) | n/a (driver seeds goals) | goal-seeding | none (seed fold) |
| Phase 1 — G3 meters live | 3 (METER-BUS ×3) | 1 reviewer per fan (driver) | meter-build | HANDOFF-FANOUT-METER-<ts> |
| Phase 2 — G2 ratio gate | 6 (GATE-KEEPER ×2 sub-missions ×3) | 2 reviewers per fan (driver + skeptic) | gate-cert | HANDOFF-FANOUT-GATE-<ts> |
| Phase 3 — G4 fan-scale + fold-banking | 9 (FANOUT-HANDLER ×3 sub-missions ×3) | 3 reviewers per fan (blind/skeptic/truster) | fanfold-ops | HANDOFF-FANOUT-FANFOLD-<ts> |
| Phase 4 — compose-check | 1 driver (close) | driver + independent check | close | HANDOFF-FANOUT-CLOSE-<ts> |

Bandwidth rule (hard): total concurrent fan-outputs in any 30m window ≤ 3 × (named drivers in that window). If exceeded → freeze the excess fan until a sub-mission split opens bandwidth. Density ladder: Phase 1 = 1×, Phase 2 = 2×, Phase 3 = 3× (max), Phase 4 = 1×.

## 2. Fold-Banking (mechanics)

- Cadence: fold every ≤ 30m per dispatch (hard cap; no fold deferred past 30m).
- Artifact contract: each fold writes `HANDOFF-FANOUT-<mechanism>-<YYYYMMDD-HHMM>.md` in `studies/rfc-143379-rig/`, one per mechanism that ran in that window. Mechanism = the named fan mechanism (METER, GATE, FANFOLD, CLOSE, plus legacy AOA/AUDIT/VETT where revived).
- Compounding rule: autonomous rings (fleet cycles, negentropy sweeps) must emit/append into the mechanism's HANDOFF-FANOUT artifact for that window; rings do not close a window without banking into the handoff. Compound-learning banks per mechanism, not per window — a mechanism's HANDOFF-FANOUT accumulates across windows until the mechanism closes.
- Triad demotion: blind/skeptic/truster is a review sub-step inside a fan (cross-check density ≥ 2), not a top-level fan. Top-level fans are mechanism-scoped and multi-agent.
- Close condition: a mechanism closes only when its HANDOFF-FANOUT contains (a) fan-width used, (b) cross-check verdicts, (c) standing gaps, (d) next-dispatch pointer.

## Compose-check

- [ ] fan-widths per phase present and bounded ≤ 3×B
- [ ] cross-check density ladder present (1×/2×/3×/1×)
- [ ] bandwidth rule numeric (≤ 3 fan-outputs per driver per 30m)
- [ ] fold cadence ≤ 30m stated
- [ ] HANDOFF-FANOUT-<mechanism> naming stated
- [ ] compounding rule stated (per mechanism, not per window)
- [ ] triad demoted to review sub-step
- [ ] nothing public
