# THE DEPLOYABLE END-TO-END PLAN — RFC-143379-RIG 4-HOUR SPRINT

**Status:** DIRECT-APPLICABLE. Nothing public. **Mission name:** RFC-143379-rig ACES proper end-to-end, 4-hour sprint (staging-build).

## 1. MISSION FRAME

**Loot-triggers (G-arcs):**

| G-arc | Loot-trigger | θ | Named driver | Dispatch target | Deadline | Fold-boundary |
|---|---|---|---|---|---|---|
| G1 | ACES loop mis-fired in prior run (improper re-entry) | ≥0.60 | sprint-lead | ACES-RUNNER | +90m | ≤30m |
| G2 | windows with named-drivers/total-tracks below certified ratio froze | ≥0.75 | envelope-owner | GATE-KEEPER | +120m | ≤30m |
| G3 | zero-dispatch meters retired | ≥0.50 | meter-owner | METER-BUS | +60m | ≤30m |
| G4 | HANDOFF-FANOUT artifacts un-banked | ≥0.65 | fanout-owner | FANOUT-HANDLER | +150m | ≤30m |

**Driver-ratio gate (freeze-rule):** R = 0.5. ratio = named_drivers(W)/total_tracks(W). If ratio < R → W FREEZES (no dispatch, no phase advance; escalate to sprint-lead). Persists until ratio ≥ R via re-naming or track retirement. **Phase gate:** a phase advances only when all prior-phase goals meet θ-threshold AND their rings hold receipts.

**Role-load checklist (t≤5m):** each window must load METER-BUS / GATE-KEEPER / FANOUT-HANDLER roles and seed receipt-templates; verify all three roles present before any dispatch. Missing role → freeze + escalate.

## 2. OPERATIVE SEQUENCE

**Phases (ascending, gated):**
- Phase 0 (t=0): loot triage + goal seeding (G1–G4 seeded, drivers named). Fan-out 1 (no fan).
- Phase 1 (t≤60m): G3 meters live; G1 loop run initiated. Fan-out 3 (METER-BUS ×3), density 1×.
- Phase 2 (t≤120m): G2 ratio gate certified; freeze-rule armed. Fan-out 6 (GATE-KEEPER ×2 sub ×3), density 2×.
- Phase 3 (t≤150m): G4 fan-scale + fold-banking complete. Fan-out 9 (FANOUT-HANDLER ×3 sub ×3), density 3×.
- Phase 4 (t≤240m): compose-check + envelope close. Fan-out 1 (close), density 1×.

**Bandwidth rule (hard):** total concurrent fan-outputs in any 30m window ≤ 3 × (named drivers in that window). Named drivers per window: G1 sprint-lead, G2 envelope-owner, G3 meter-owner, G4 fanout-owner. Freeze-threshold: ratio of named_drivers(W)/total_tracks(W) < 0.5 → window freezes. Excess freezes until sub-mission split.

**Fold-banking:** fold every ≤30m per dispatch (hard cap). Each fold writes `HANDOFF-FANOUT-<mechanism>-<YYYYMMDD-HHMM>.md` in `studies/rfc-143379-rig/`. Compounding per mechanism (not per window); mechanism closes only when HANDOFF-FANOUT holds (a) fan-width used, (b) cross-check verdicts, (c) standing gaps, (d) next-dispatch pointer. Each phase-gate receipt path must be named in the HANDOFF-FANOUT fold.

**Dispatch-rules (operative):** 1. θ declared up-front. 2. meter_tick: value crosses θ → emit DISPATCH {driver, trigger, target, owner, deadline +30m, fold-boundary ≤30m}; ELSE log-only. 3. Every DISPATCH carries driver + target + deadline. 4. Fold-boundary ≤30m; 8 folds max per dispatch. 5. Telegram = operator-override, never counts as DISPATCH emit. 6. Meters with zero DISPATCH emits across their window are retired (re-arm only via fresh θ + new template + new owner).

**Telegram cadence:** evidence-cadence every 3–5 turns OR on artifact-completion. Payload exactly: CHANGED / EVIDENCE / NEXT-BLOCKER. Prompts ≤2 lines, one artifact path. Handoff ≤6 lines (GOAL/DONE/NEXT/BLOCKER/ARTIFACT-PATH). Fold-override: `override: <dispatch-id> <action>` with action ∈ {hold, skip, reroute:<target>, pause-sprint} — applies only at fold boundaries.

## 3. LAUNCH SEQUENCE (first hour, exact)

1. t=0: byte-closures check — requested SHA == git rev-parse HEAD (hard); prior ring's receipt path exists; byte-equality verified on candidate diff vs pinned head. No new work until closed.
2. t≤5m: seed G1–G4, name drivers. Verify driver-ratio ≥ 0.5; else freeze + escalate. Role-load checklist complete (METER-BUS/GATE-KEEPER/FANOUT-HANDLER + receipt-templates seeded).
3. t≤10m: arm METER-BUS (G3, θ≥0.50) — first threshold-watch begins.
4. t≤30m: first fold (HANDOFF-FANOUT-METER-<ts>.md) banks Phase 1 fan output + cross-check verdict + gaps + next-dispatch pointer + phase-gate receipt paths.
5. t≤60m: G3 meters live verified (≥1 DISPATCH emit or retired with reason); G1 loop run initiated. Evidence-cadence at artifact-completion.

## 4. FAIL-MODES PRE-DECLARATION

- **Freeze-rule activation:** ratio < 0.5 in any window → freeze, escalate, no dispatch/advance until ratio ≥ 0.5.
- **Retirement-rule:** meter with zero DISPATCH emits → retired; re-arm only via fresh θ + new template + new owner.
- **Canary run-receipt:** a ring's landing earns dispatch-credit ONLY with its receipt. No receipt → no credit → no advance. Claims only what the run's log shows.
- **Operator-override:** `override: <dispatch-id> <action>`; actions hold/skip/reroute/pause-sprint; at fold boundaries only; append-only audit; operator precedence; head acknowledges via CHANGED: override applied.
- **Partial-fold rollback:** if a fold writes partially (missing any of fan-width/cross-check/gaps/next-dispatch/receipt-paths), roll back the entire fold, re-run from last clean fold; no partial credit.
- **SHA-mismatch halt:** if requested SHA != git rev-parse HEAD at byte-closures check, halt all work; escalate to sprint-lead; no dispatch until SHA aligned.

## 5. METRICS

- **Loop-metering:** ring landing earns dispatch-credit ONLY with receipt; credit per-ring per-G-arc; the only path to phase advance.
- **Driver-ratio gate:** R = 0.5, certified (G2) by Phase 2.
- **ACES leg-sequence (fixed, no skip/reorder):** improve → audit → review → AoA. Base-swaps rotation width 4 (A: prior improve; B: prior audit; C: prior review; D: prior AoA). Byte-preconditions close before new work. Terminal = no-change-confirmation (candidate == prior committed state byte-for-byte AND audit+review+AoA all no-change); non-no-change re-enters at improve (proper re-entry).
- **Fan-topology:** 1/3/6/9/1; cross-check density 1×/2×/3×/1×; fold ≤30m; HANDOFF-FANOUT per mechanism.

**Compose-check:** all 4 G-arcs present; phases gated; freeze-rule exact; dispatch-rules operative; retirement-rule present; fan-widths ≤3×B; fold ≤30m; leg-sequence fixed; base-swaps width 4; byte-preconditions close; terminal no-change; loop-credits receipt-gated; nothing public.

**End-state:** envelope close at t≤240m with compose-check PASS and all rings holding receipts.
## 6. REFINED-PASS-2 — the audit-II's three pins (cold-executability)
- **Receipt-template's schema (pinned):** every ring's receipt carries exactly {ring-id, g-arc, receipt-path, artifact-sha256, land-timestamp} — the template's a five-field row; seeds land with the role-load checklist at t<=5m.
- **Receipt-path's convention (pinned):** receipts live at `studies/rfc-143379-rig/receipts/<ring-id>-<HHMM>.md` — the path's deterministic, a claim without the path's a claim without evidence.
- **Byte-closure's command (pinned):** the check executes `git rev-parse HEAD` (must equal the requested SHA) + `sha256sum <candidate-artifact>` vs the pinned head's artifact-hash + `git diff --stat` against the pinned head (must be empty for the untouched surfaces) — the triple's the closure's receipt.
