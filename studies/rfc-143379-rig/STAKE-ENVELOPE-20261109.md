# STAKE-ENVELOPE-20261109 — Mission-Frame (ENVELOPE Slice, 4-hour Sprint)

Status: operative. Nothing public. Compose-check pending.

## 1. Loot-Triggered Goals (G-arcs)

| # | G-arc | Loot-trigger | θ | Named driver | Dispatch target | Deadline | Fold-boundary |
|---|-------|--------------|---|--------------|-----------------|----------|---------------|
| G1 | ACES-improperly-loop end-to-end | loot: ACES loop mis-fired in prior run (improper re-entry) | θ ≥ 0.60 | driver: sprint-lead | dispatch: ACES-RUNNER | +90m | fold ≤ 30m per dispatch |
| G2 | Driver-ratio gate certified | loot: windows with named-drivers/total-tracks below certified ratio froze | θ ≥ 0.75 | driver: envelope-owner | dispatch: GATE-KEEPER | +120m | fold ≤ 30m per dispatch |
| G3 | Dispatch-triggered meters live | loot: zero-dispatch meters retired | θ ≥ 0.50 | driver: meter-owner | dispatch: METER-BUS | +60m | fold ≤ 30m per dispatch |
| G4 | Fan-scale + per-mechanism fold-banking | loot: HANDOFF-FANOUT artifacts un-banked | θ ≥ 0.65 | driver: fanout-owner | dispatch: FANOUT-HANDLER | +150m | fold ≤ 30m per dispatch |

## 2. Phases (ascending envelope)

- Phase 0 (t=0): loot triage + goal seeding (G1–G4 seeded, drivers named).
- Phase 1 (t≤60m): G3 meters live; G1 loop run initiated.
- Phase 2 (t≤120m): G2 ratio gate certified; freeze-rule armed.
- Phase 3 (t≤150m): G4 fan-scale + fold-banking complete.
- Phase 4 (t≤240m): compose-check + envelope close.

Gate: a phase advances only when all prior-phase goals meet θ-threshold.

## 3. Driver-Ratio Gate (freeze-rule)

For any window W: ratio = named_drivers(W) / total_tracks(W).
Certified ratio R = 0.5 (half).
If ratio < R → W FREEZES: no dispatch, no phase advance, escalate to sprint-lead.
Freeze persists until ratio ≥ R via re-naming or track retirement.

## Compose-check

- [ ] all 4 G-arcs present with θ, driver, dispatch, deadline, fold
- [ ] phases ascending and gated
- [ ] freeze-rule exact
- [ ] nothing public
