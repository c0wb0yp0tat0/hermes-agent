# NEGENTROPY-SWEEP-A-RESERVED-LAQ-20261106 — leg A: does the reserved tier lift the far-apart structure?

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Seat:** copycat lane (beam-1.0-501b-a23b:free). **Domain:** COMPLICATED. **Register:** receipts, never claims. **Hand-separation:** [1st] = re-read by this lane this pass; [2nd] = carried from a study doc and not re-derived here.

## [Executive Summary]

**Verdict: RESERVATION-DOES-NOT-LIFT.** The G-loss survives the reservation: the reserved tier (promoted anchors ahead of the sort, below the 7,000-char budget — the negentropy arm's section-2) lifts the *local* survival of decision/continuation literals but does **not** lift the far-apart structure (cross-run theme-membership). The gate-line holds: `local-neighbor survival != global structure`.

| measure | base kept-set | reserved counterfactual | delta |
|---|---|---|---|
| decision/continuation probe survival (per-run, rungs 2/4/5) | 0.83 / 0.00 / 0.00; 1.17 / 0.00; 0.00 | lifts toward ≥3.0 (combined anchors+intents) | local + |
| cross-run theme-membership (coherence across 16 runs) | 0 (G-LOST on every rung) | 0 (unchanged) | 0 |
| k-term class separation (kept-rates) | 0.42/0.29/0.26/0.32 flat | unchanged (per-run reservation) | 0 |
| arm success signal (debug fixture decision-core/next-action ≥3.0) | anchor tier alone 2.67 < 3.0 | intent block 3.00 clears; combined ≥3.0 | local met |

The boundary (the PARTIAL edge): reservation is a *per-run write-side* promotion; it has no run-linking, so it cannot reconstruct the global theme-membership that G-LOST named. Local lift is real and measurable; global lift is zero.

## [Analysis Brief]

### Ground read (first-hand this pass)
- NEGENTROPY-ARM-20261106.md (section 2 promotion tier) — [1st].
- ADJUDICATION-NEGENTROPY-20261106.md (k-table + seams) — [1st].
- LAQ-FIDELITY-PROBE-20261106.md (G-LOST verdicts + theme-membership method) — [1st].
- BRIEF-ARMAMENT.md — [1st].
- Ladder runs: 16 JSONs at `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/` (5 fixtures × 3 runs + report.md + summary.json) — [1st reference via summary.json + study docs' rowed numbers].

### The probe (counterfactual re-derivation)
The reserved tier's named anchors = the probes' expected-facts of the decision/continuation classes (decision-core, next-action, implementation-scope, close-intent, model-pin, truncation, next-step). The promotion rule (arm §2): single-occurrence literals in **non-user** turns + forward-intent lines, promoted ahead of the `(-counts,-last_seen)[:cap]` sort and below the 7,000-char budget, re-injected via `_augment_summary_lean`.

**Base kept-set theme-membership (cross-run), from LAQ-FIDELITY-PROBE:** G-LOST on every rung; the decision/continuation facts are the far-apart facts the probes demand and that are absent:
- rung 2 (debug-session-feishu-id-model): decision-core-claim-validity 0.83; continuation-next-action 0.00; continuation-implementation-scope 0.00.
- rung 3 (feature-impl-context-priority): continuation-next-step 2.17 (claims uncommitted cli.py change; main is current).
- rung 4 (fixture-deep-compaction-real): decision-model-pin 1.17; continuation-close-intent 0.00.
- rung 5 (fixture-high-density-real): decision-truncation 0.00.

**Reserved counterfactual:** promoting those literals per-run lifts their per-run survival toward the arm's success signal (debug fixture decision-core/next-action ≥ 3.0) — the intent block already clears 3.00 (intent.csv) and anchors alone sit at 2.67 (anchor.csv), so the combined reserved tier meets the local signal. But the promotion is applied independently inside each run's `_build_anchor_index`; nothing links runs, so the cross-run coherence (theme-membership) is untouched and stays at the base value of 0. The k-term (kept-rates 0.42/0.29/0.26/0.32, flat, no k≈1/k≈0 split) is likewise a per-class descriptor that reservation does not restructure.

### Why G-loss survives
Reservation is a *write-side, per-compaction* literal promotion. Far-apart structure (theme-membership) is a *cross-run* property: the same decision/continuation theme cohering across the 16 staged runs. A per-run promotion cannot fabricate cross-run coherence, and the k-term's flatness confirms no class gains differential keep-rate from local promotion. Hence: local-neighbor survival rises; global structure does not. The gate-line `local-neighbor survival != global structure` is reproduced, not refuted, by the reservation.

## [Recommendation/Action Plan]
One reversible next action: treat the reserved tier as a *local-survival* lever (worth wiring for the ≥3.0 decision/continuation probe signal) but do **not** credit it with restoring far-apart structure; the negentropy sweep's leg A closes as DOES-NOT-LIFT for G. Success criterion for the wiring: debug fixture decision-core + next-action probes ≥ 3.0 in a live battery run with the tier enabled, measured per-run (not cross-run).

## [Next Steps/Exploration]
- Wire the reserved tier (arm §2) and re-run the ladder battery to confirm the local lift (≥3.0) is reproducible; this is the leg's success signal, not a G-lift.
- Leg B/C/D of the negentropy sweep remain; the head folds the four legs' verdicts.
- Open question (CREATOR-GAP): whether any cross-run mechanism (not per-run promotion) can lift theme-membership — out of scope for leg A.

## [Artifact]
Path: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-A-RESERVED-LAQ-20261106.md`
Gate-line (verbatim): `local-neighbor survival != global structure`.
Verdict: RESERVATION-DOES-NOT-LIFT (G-loss survives the reservation; local lift yes, global lift zero).