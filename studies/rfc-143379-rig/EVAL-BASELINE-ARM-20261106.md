# EVAL-BASELINE-ARM-20261106 — the ladder-battery's baseline-vs-fixes attribution arm: protocol shape + feasibility verdict (PARTIALLY-SHAPED)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Seat:** the baseline-arm lane (opus-5.5, the paid seat's first shaped loop). **Gate-line:** the gate: nothing public without the user's word. **Register:** receipts, never claims — every claim traced to the run-JSONs at `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/`, the eval repo's tree (`/root/workspace/repos/hermes-compression-eval`), the ledger (`RECEIPTS.md`), or the named records. **First/second-hand separation:** the eval repo's tree and staged copies = first-hand; every other repo's surface (hermes-agent depths, hermes-agent_battery, hermes-compression-eval's root files) = **UNREAD under the harness roots** (read-tool refused: "path outside the allowed roots"), named, never inferred.

## [Executive Summary]

**The deliverable is ONE statement with ONE mechanism:** the protocol's shape **is** its feasibility verdict — the attribution logic (baseline leg → fixes leg → per-fixture pair → median-vs-median delta) is the single mechanism both design and verdict exercise (the mission's separation test applied: one mechanism, one deliverable).

**The verdict: PARTIALLY-SHAPED**, seam named at the letter: **the fixes leg's pin does not exist on the record yet** — the ladder's runs all sit on ONE substrate-pin (`a996d4ad3039e280dc21e9b558f5a44c081dda42`, receive `fixes/falsifier-battery-20261104`); the record carries NO receipt of the mechanism-under-test's head (the compression-changes' landed pin). The five medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00 (summary.json of `ladder-20261106-a996d4ad`) are **fixes-leg-only data**; the baseline leg's numbers (any of them) DO NOT EXIST on the record. The seam's anchor for the audit: **the fixes-pin's absence is the first-write-to-verify**, and the protocol's cost-shape (the paid/free distribution) waits on the harness's run-cost surface, which the harness roots left unread.

The protocol that follows is the runnable shape: (1) the baseline leg = the same five live fixtures at the **pre-feature pin** (`d1bdb4582cd5d16be6a6b486f696f8240c222b96` per the ledger's first row), availability VERIFIED, honest wall if absent; (2) the fixes leg = the same five fixtures at the **mechanism's landed head** (to-be-receipted); (3) the run schema = fixed pairs (baseline.headers × fixes.headers at one pin each), 3 runs/fixture (the ladder's discipline, summary.json `runs_per_fixture: 3`), runs interleaved by pair, label `baseline-arm-<date>`; (4) the comparison metric = median-vs-median per fixed pair, `Δ = fixes.M − baseline.M`, with the receipted walls (the run-window's availability, the n=3 noise-no-signal, the 09:11Z runner/env flip); (5) the success-signal = `Δ ≥ +0.50` median points on the SAME fixed fixture-pair with ZERO score-flips, and the attribution claimed only when the deltas' sign tracks the mechanism's advertised direction; (6) the cost-shape = the cheapest-first ladder: 15 baseline + 15 fixes runs (30), the paid/free distribution is READER-GATED on the harness's cost surface (UNREAD); (7) the seams = the fixes-pin's absence, the paired-Δ variance's magnitude (n=3), the run-cost surface. **ATTRIBUTION-DOMAIN: COMPLICATED** (timing/pinning where expertise intervenes — the ceiling honored: PARTIALLY-COVERED with the seam NAMED, never COVERED, never GAP, never UNKNOWN: GAP would require the missing leg's hook to be unanswerable, UNKNOWN would require a settle-condition, and the evidence exists for the partial shape).

The one-line verdict: **the arm is PARTIALLY-SHAPED with the seam NAMED (the fixes leg's pin), and the protocol below is the runnable shape that closes it.**

## [Analysis Brief]

### (a) The attribution question, verbatim, and the host

> can the battery's runs attribute a fixture's delta to the mechanisms under test (the compression changes), rather than to substrate drift, run variance, or the pin's age?

The host that must answer it is the eval harness at `/root/workspace/repos/hermes-compression-eval` (first-hand, tree-verified): `run_eval.py` + `compressor_driver.py` + the fixtures under `probes/` + the `results/ladder-20261106-a996d4ad/` run JSONs + `summary.json`. The harness runs a fixture's `pre_*` context through a compressor model under a substrate pin, judges each probe-dimension on a 0–5 scale, and reports medians over N runs per fixture (`runs_per_fixture: 3` in summary.json). **The σ-sources the question names are the protocol's inputs, never assumptions** (ground-3): substrate drift (the pin's tree vs the mechanism's tree), run variance (the 3-run medians), the pin's age (the commit-distance between the baseline and the fixes pins), plus the named runner/env side (the 09:11Z flip).

### (b) The protocol's six parts

#### (b1) The baseline leg — the pin WITHOUT the mechanism: its practical form = the SAME live fixtures at the PRE-FEATURE pin, availability VERIFIED, honest wall if unavailable

- **The baseline pin (named):** the pre-feature head `d1bdb4582cd5d16be6a6b486f696f8240c222b96` (ledger row 1 of RECEIPTS.md: "#139606 merge head", run `42064685359`, G, "write-gate + memory-tool battery at the pin; the first composition pin, receipted"). Its practical form is the same five live fixtures (config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority, fixture-deep-compaction-real, fixture-high-density-real — the five fixture files under the eval repo's `fixtures/`, ladder-results receipted) run through the SAME harness at `d1bdb4582c…` with the same judge constant — the only varied input is the pin's source-tree: the pre-feature composition head without the compression changes.
- **Availability VERIFIED, not assumed:** the ledger owns a GREEN (PASS run 42064685359, "requested == executed == d1bdb4582c…") for the pin itself — but a green receipt qualifies THAT pin's checked-out source (RECEIPTS.md, the honesty markers: "A green run at a pin qualifies THAT pin's checked-out source — not any other head"); the battery's run at that pin is NOT YET EXECUTED. The protocol's first run MUST re-verify the pin with the eval harness itself before any baseline run is counted — same practice as the ladder's gate: "RUNGS-REBUILD landed" (EVAL-LADDER-BATTERY-20261106 header). If the pin cannot be checked out (gone, rewritten, A/B-different), the honest wall: name the substitute pin + the substitution's effect on the Δ, or name the leg UNMEASURABLE — never a silent substitute.
- **Why same fixtures:** the question is per-fixture attribute-ability. A different fixture-set would confound the fixture's own variance with the mechanism's delta; the pairing must hold the fixture constant and vary only the pin (per E-5's borrow: "arms differing only by `PYTHONPATH`", hermes-toolperf-evals-README).

#### (b2) The fixes leg — the mechanism's head: THE SEAM

- The ladder's runs all sit on ONE substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42` (`fixes/falsifier-battery-20261104`, EVAL-LADDER-BATTERY-20261106 freshness row; the whole-anchor head, RECEIPTS.md a996d4ad rows 19:43Z…GREEN). The five medians **belong to the fixes leg for the fixtures they cover** — 4.50 / 3.25 / 4.67 / 1.00 / 0.00 (summary.json, fixtures in order: config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority, fixture-deep-compaction-real, fixture-high-density-real).
- **BUT the ledger carries NO receipt of "the mechanism under test's landed head"** as a distinct pin — no row names a compression-changes pin with a GREEN receipt that DIFFERS from the substrate pin. The protocol therefore cannot name the fixes leg's pin from the record. Its practical form: the same five fixtures at the head whose commit lands the compression changes (in this repo family: whatever hermes-agent tree the changes ship in), its receipt = a GREEN (PASS, requested == executed) for THAT pin in the eval harness.
- **This is the seam the audit leg must attack FIRST** — quoted, not asserted: the Δ's fixes-side is undefined until the pin exists.

#### (b3) The run schema — the pairs, the runs-per-fixture, the label-branching

- **The pairs (fixed, not crossed):** one pair per fixture, `pair_f = (baseline_pin.run_f, fixes_pin.run_f)` — the same fixture f at the two pins. Crossed pairing (baseline-fixture-A vs fixes-fixture-B) would be a comparison of different streams, not of the mechanism; the ladder's depth-vs-density separation already measured the five fixtures ARE different streams (the 1.00 / 0.00 floors), so pairs must be within-fixture by construction.
- **Runs per fixture:** 3 (the ladder's `runs_per_fixture: 3`, summary.json; the battery reads medians over runs — "single runs are noise; medians are the signal", EVAL-LADDER-BATTERY). **Run count is the one knob the protocol can turn** — a variance-based bump to 5 is the documented fallback, per E-5's "n=3 deltas under a few percent are noise" (hermes-toolperf-evals-README) the σ-managed choice.
- **The label-branching:** the ladder's label embeds pin+date (`ladder-20261106-a996d4ad`); the arm's labels embed BOTH legs — `baseline-arm-<date>` for the pair-set (the convention the battery already uses for run-labels; the arm's runs are one labeled set). Per-run JSONs carry `fixture_name` + `run_index` (ladder-results run-1 JSONs receipted).
- **Interleave rule (guard against drift-within-the-window):** alternate baseline/fixes runs of the same pair within the same provider window; if a run's window closes (provider-window-closed row in EVAL-LADDER-BATTERY), the completed half-pair is dropped from the Δ unless its mate can be run in the same window class — the protocol's variance's handling is the windows' shape, receipted, never assumed.

#### (b4) The comparison metric — the deltas' attribution: median-vs-median with the walls; the variance's receipt

- **The metric:** per pair, `Δ_f = fixes.M_f − baseline.M_f` (median overall per fixture, the summary.json overall_median field). Median-vs-median is the ladder's own reading (the per-rung recovery median table in EVAL-LADDER-BATTERY; the report.md per-fixture `overall` column).
- **The walls the attribution must clear (each a named, receipted gate):**
  1. **The run-window wall** — runs are non-deterministic (3-run medians; the five fixtures' medians 4.50/3.25/4.67 are spread, and the real cells sit at 1.00/0.00). The protocol: Δ only over pairs whose runs are receipted (per-run JSON, `run_index`, timestamp in the JSON) and whose windows are same-class.
  2. **The no-signal wall** — a Δ in |Δ| < 0.50 median points is UNATTRIBUTED (noise band = half a judge-point; same reasoning as the E-5 "n=3 deltas under a few percent are noise").
  3. **The runner/env wall** — the 09:11Z flip was classed runner/env-side: "the pin's checksum-match proved the substrate, the env diverged" (ground-3, RECEIPTS.md honesty: divergence between envs is data, recorded, never smoothed). A Δ that appears WITH a runner/env divergence concurrent is UNATTRIBUTED until the env is held constant or the divergence is receipted.
  4. **The sign-track wall** — the Δ may only be attributed to the mechanism if its sign tracks the mechanism's advertised direction (the compression changes' claim: better retention/recovery on the continuation/decision/small+old classes — the E-3 measured class). A sign that TRACKS the noise or a sign REVERSED from the mechanism's direction is attributed to substrate age, not to the mechanism.
- **The variance's receipt:** every pair's Δ carries the run-count + the per-run spread (min/max of the 3 medians when available from run-JSONs' per-run scores — the run JSONs' dimension scores are the raw receipts); the protocol refuses to report a Δ without its runs' spread, because "medians are the signal" only when the spread is narrow.

#### (b5) The success-signal — what a future battery run must show to claim the mechanism's effect

A future battery run claims the compression changes' effect iff, on the SAME fixed fixture-pairs:
- `Δ_f ≥ +0.50` median points for the fixture-pairs the mechanism claims to help (the continuation/decision/small+old class = deep-compaction-real + the native cell class the ladder carried), AND
- zero score-flips (no baseline-median over the fixes-median on any claimed pair), AND
- the walls (b4) all cleared — same-window runs, spread-narrow, no concurrent runner/env divergence, sign tracking the mechanism's direction.

**Without (b4)'s walls, the same Δ is substrate-drift-or-variance, NOT the mechanism.** The success-signal is the FAILURE to claim; the ladder's honest-walls discipline (the depth-vs-density separation "held with honest walls", ground-3) is the arm's template.

#### (b6) The cost's shape — the total runs, the time, the paid/free distribution

- **Total runs:** 30 — 15 baseline (5 fixtures × 3) + 15 fixes (5 × 3). The existing ladder-20261106-a996d4ad run-set (15 runs, all fixes-leg, receipted in results/) can serve as the fixes leg's data IF its pin is the mechanism's head; otherwise 15 more fixes runs. The baseline 15 are NET-NEW.
- **Time:** same order as the ladder's battery (15 runs executed 2026-11-06, EVAL-LADDER-BATTERY freshness row) — the arm doubles it on the first pass: 2× the ladder's run-set.
- **The paid/free distribution: READER-GATED — UNREAD.** The distribution's shape (which fixtures/models are paid via the provider window vs free) lives in the harness's run-cost surface, which the harness roots left UNREAD ("path outside the allowed roots" — the eval repo's ROOT files run_eval.py/compressor_driver.py/README.md and the eval repo's fixtures were read-blocked; the staged results and the repo's tree were readable). The seam names it; the audit leg's second base can read the harness roots and fill the distribution's shape — one of the two seams to attack.

### (c) The variance's sources — the protocol's inputs (ground-3, all receipted)
1. **The small+old class** — E-3 (RESULTS-E3-CONTINUATION-20261106): the continuation/decision losses (exec-time 0.17, next-action 0.67, scope 1.00 — the small+old anchors) concentrate loss in cell A (the deep-compaction-real fixture) — the class the mechanism claims to fix.
2. **The depth-vs-density separation held** — the battery's honest walls: deep ≠ dense (rung 2 vs rung 4-5), and the dense cell is the floor, not the deep one.
3. **The pin's age / env flips** — the 09:11Z flip classed runner/env-side (pin checksum-match proved the substrate; the env diverged) — the wall (b4.3).
4. **Judge/scoring** — the ATOF judge is a named trade-off (E-5's borrow-list; the ladder uses per-probe dimension 0–5 medians, the summary.json fields) — the scoring surface is the receipt, never a prior.

## [Recommendation/Action Plan]

**One reversible next action:** write the arm's paired-run manifest (`fixture → baseline-pin | fixes-pin` for each of the five fixtures) and re-verify the baseline pin with the eval harness — the pin's availability is the attribute-ability's first gate.

**Its success criterion:** the manifest lists the pre-feature pin `d1bdb4582c…` as VERIFIED-AT-RUN (a PASS, requested == executed) in the eval harness, or the substitution + its effect named on the record.

## [Next Steps/Exploration] — the seams the audit leg should attack first

1. **FIRST — the fixes leg's pin:** the record lacks a distinct mechanism-head pin with a GREEN receipt. The audit's first read: the study's git history + RECEIPTS.md for a land-commit of the compression changes — or the honest conclusion that the fixes leg's pin is undefined and the arm's inventory is the blocker.
2. **The paired-Δ variance's magnitude (n=3):** the battery shows 4.50/3.25/4.67 medians with wide per-run spread (the real cells' floors); the audit should read the per-run spread from the ladder run-JSONs to size the noise band, and confirm or reject the ±0.50-Δ threshold.
3. **The run-cost surface:** the paid/free distribution waits on the eval repo's roots (UNREAD here) — the audit can read `run_eval.py` + `compressor_driver.py` + the provider-window mechanics to fill (b6)'s cost-shape.

## [Artifact]

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/EVAL-BASELINE-ARM-20261106.md` — committed + pushed on `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork; no POST/PATCH beyond the branch's push; the gate: nothing public without the user's word).

**EVAL-BASELINE-ARM verdict: PARTIALLY-SHAPED — the seam NAMED (the fixes leg's pin does not exist on the record; the run-cost surface UNREAD). Protocol's shape: baseline = pre-feature pin `d1bdb4582c…` (VERIFIED at run), fixes = the mechanism's landed head (to-be-receipted), pairs fixed within-fixture, 3 runs/fixture interleaved, Δ = median-vs-median with the four named walls, success-signal = Δ ≥ +0.50 with zero flips and the walls cleared, cost = 30 runs first-pass with the paid/free distribution gated on the harness's run-cost surface.**
