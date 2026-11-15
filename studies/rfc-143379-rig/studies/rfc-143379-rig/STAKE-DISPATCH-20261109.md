# STAKE-DISPATCH-20261109 — Dispatch Slice (DISPATCH Suite, 4-hour Sprint)

Status: operative. Nothing public. Compose-check pending.

## 1. G-arcs' Theta-Table (meters' operative suite)

| # | G-arc | Meter | θ (declared) | Dispatch template | Owner |
|---|-------|-------|--------------|-------------------|-------|
| G1 | ACES-improperly-loop end-to-end | meter: ACES-RUNNER (loop re-entry) | θ ≥ 0.60 | DISPATCH {driver: sprint-lead, trigger: loot-ACES-loop-misfired, target: ACES-RUNNER, owner: sprint-lead, deadline: +90m, fold-boundary: ≤30m} | sprint-lead |
| G2 | Driver-ratio gate certified | meter: GATE-KEEPER (named-drivers/total-tracks) | θ ≥ 0.75 | DISPATCH {driver: envelope-owner, trigger: loot-window-freeze, target: GATE-KEEPER, owner: envelope-owner, deadline: +120m, fold-boundary: ≤30m} | envelope-owner |
| G3 | Dispatch-triggered meters live | meter: METER-BUS (meter firing) | θ ≥ 0.50 | DISPATCH {driver: meter-owner, trigger: loot-zero-dispatch-retired, target: METER-BUS, owner: meter-owner, deadline: +60m, fold-boundary: ≤30m} | meter-owner |
| G4 | Fan-scale + per-mechanism fold-banking | meter: FANOUT-HANDLER (un-banked fanout) | θ ≥ 0.65 | DISPATCH {driver: fanout-owner, trigger: loot-handoff-fanout-unbanked, target: FANOUT-HANDLER, owner: fanout-owner, deadline: +150m, fold-boundary: ≤30m} | fanout-owner |

## 2. Dispatch-Rules (operative)

1. θ declared up-front: every meter declares its threshold θ before operation; no retroactive thresholding.
2. meter_tick: IF value crosses θ → emit DISPATCH {driver, trigger, target, owner, deadline +30m, fold-boundary ≤30m}; ELSE log-only.
3. Dispatch names owner + item + deadline: every DISPATCH carries driver (named owner), target (item), deadline (explicit +30m from tick).
4. Fold-boundary ≤30m: each dispatch's fold must close within 30m; 8 folds max per dispatch.
5. telegram = operator-override, not dispatch: Telegram messages are operator overrides; they never count as a DISPATCH emit.
6. Meters that never fire are retired: a meter with zero DISPATCH emits across its full window is retired (removed from active suite; no re-arm without re-declaration).

## 3. Retirement-Rule

- Trigger: meter has zero DISPATCH emits for its declared window.
- Action: retire meter (mark retired, remove from active theta-table, log reason).
- Re-arm: retired meter may only re-enter via fresh θ declaration + new dispatch-template + new owner.

## Compose-check

- [ ] all 4 G-arcs present with θ, dispatch-template, owner
- [ ] dispatch-rules operative text exact (6 rules)
- [ ] retirement-rule present (trigger/action/re-arm)
- [ ] fold-boundary ≤30m, 8 folds max
- [ ] nothing public
