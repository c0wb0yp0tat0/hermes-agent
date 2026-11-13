# SEAM-INTEGRATION-20261106 — the retention-latch's real-compaction integration (E-2, design-implication arm)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only). **Seat:** the seam's design-implication arm. **Register:** receipts, never claims. **Ground read:** `krecency/RESULTS-RETENTION.md`, `krecency/RESULTS-SEAMMECH.md`, `PROBE-BANKS-20261106.md`, `krecency/RESULTS-SEAMFIX.md`, `krecency/RESULTS-COMPOSE.md`, `krecency/RESULTS-INTENT.md`, `krecency/RESULTS-SEAMINT.md` + `probe_seamint.py`/`results/seamint.{csv,json}`.

## 1. The latch (the standing invention, receipted)

From `krecency/RESULTS-RETENTION.md`: small+old-aware retention at the death-cell — r=1.0 (full retention) drops deep-minima prevalence 1.00 → 0.00, below the 0.15-bar; r ∈ {0.0,0.25,0.5} stay 1.00 (RETENTION-PARTIAL at intermediate). Cost-line: reserved set = 3 tiny-aged literals (≤3 tokens, age ≥ threshold); token-budget = 3 tokens. r is a parameter; reserved set defined by the small+old class.

Mechanism (from `krecency/RESULTS-SEAMMECH.md`, MECHANISM-MULTI): (a) semantic-distance absorption — tiny facts are low-salience anchors that evaporate into the summary; (b) retention priority of the compressor's ordering — `agent/context_compressor.py:_build_anchor_index` ranks anchors by `(-counts[v], -last_seen[v])[:cap]` (frequency+recency), so single-occurrence tiny facts lose the cap race; `_build_verbatim_user_section` scopes verbatim retention to user turns (short anchors in assistant/tool turns not preserved); `_fresh_compaction_message_copy` drops sidecar ordering hints. Seam (E4): SEAM-CONFIRMED — tiny+old 17/21 lost (81%).

## 2. The mapping — latch mechanism → real fixtures' construction

The latch's reservation (r=1.0 survival of tiny-aged literals) maps onto the compressor's build path at two code-cited surfaces:

- **`_build_anchor_index` (frequency+recency cap):** the latch would add a reservation tier — tiny+old literals (≤3 tokens / ≤3 words, introduced before the continuation) promoted into the anchor index *ahead of* the `(-counts, -last_seen)[:cap]` race, so single-occurrence tiny anchors are not evicted by the cap. This is the latch's actual lever (mechanism (b)).
- **`_build_verbatim_user_section` (user-turn scope):** the latch's tiny-aged literals that live in assistant/tool turns (the death-cell's exec-time/next-action anchors) are not verbatim-preserved today; the reservation would need to widen verbatim scope beyond user turns, or add a sidecar retained-literals block. This is the latch's secondary lever (mechanism (a) — semantic absorption).
- **`_fresh_compaction_message_copy`:** the reservation must survive the fresh-copy step (sidecar hints are dropped today); the latch must be re-injected post-copy, not pre-copy.

**Cell mapping (PROBE-BANKS-20261106, the real ground):**
- Cell A (deep-compaction, `fixture-deep-compaction-real.json`, 8 msgs, small+old class): the latch's target class lives here. The probes the latch would have to lift: A5 (session start stamp `2026-10-07T12:33:05`, a clock anchor, tiny+old), A9 (user open 77 chars), A10 (user close 188 chars) — these are the "tiny+old" literals the seam-mechanism names (exec-time, next-action, scope class). Continuity/decision probes B8/B10 in the bank-protocol's recall/artifact/decision/continuation banks are the continuation-point probes the latch must move.
- Cell B (high-density, 2 msgs, dense stream): NOT the latch's class — density shape, not depth; the latch's tiny+old reservation has no purchase here (no compaction-path turns to age). The latch is a depth-cell instrument only.

## 3. The falsifier, stated in advance

Counterfactual that refutes the integration: **the reserved tiny-aged literals' survival fails to lift the continuation/decision probes in the real cell's own terms** — i.e., with the latch's reservation applied, the below-3.0 probe count (exec-time, decision-core, next-action, scope, recall) does not drop below the seam-arc's honest-blind bar of 3.33 median / 0 below-3.0, OR the real-cell probes (A5/A9/A10 class, B8/B10 continuation/decision) do not move. Equivalently: if `pin+retention-latch` prevalence == `literal-pin` prevalence on the real ground (no delta), the latch is refuted as a distinct lever. (This is exactly what `RESULTS-SEAMINT.md` measures.)

## 4. Cost-line re-measurement at real loads

- Synthetic death-cell (RESULTS-RETENTION): 3 tiny-aged literals, 3 tokens.
- Real streams (`probe_seamint.py`, 147 `request_dump_*.json`, mined SHA/path/flag literals, stream_len 15,702, recurrence threshold ≥3 → PINNED 293): RESERVED = {v : len(v) ≤ 6} = **26 literals**. `results/seamint.json`: reserved_set_size 26.

So the 3-token figure does **not** survive real loads: the reserved set balloons 3 → 26 (≈ 8.7×). The synthetic cost-line was measured at the death-cell's tiny literal budget; the real stream's tiny-literal population is an order of magnitude larger, and the latch's reservation would carry ~26 short literals, not 3. (Token cost of 26 short literals ≈ 26–52 tokens depending on literal length, vs the synthetic 3 tokens — still small in absolute terms, but the "3-token" claim is not transportable.)

## 5. Minimal diff-shape vs the 3-block composition

The seam-arc's fix-composition (RESULTS-INTENT / RESULTS-COMPOSE) is three blocks:
- derivations-block ~120 tokens (inferential chains' keeps)
- time-anchors ~60 tokens (absolute clock facts)
- forward-intents ~60 tokens (stated next-steps)
- total ~240 tokens / 2.4% of a 10K context; seam cleared (0/5 below 3.0, median 3.33).

Where would the latch's reservation sit relative to that composition?

- **Option A — a fourth block (reserved-literals block):** add a ~26–52-token block of tiny-aged literals alongside the three. This is the latch's natural shape (r=1.0 survival = verbatim retention of the reserved set). But the seam is already CLEARED (0/5 below 3.0) by the three blocks; a fourth block has no residual to lift — it would be additive cost with no measured benefit on the real ground (RESULTS-SEAMINT: pin+retention-latch == literal-pin == 0.00).
- **Option B — modification of the verbatim-reservation's construction:** fold the reserved tiny-aged literals into the existing verbatim block (user-turn scoped → widen to assistant/tool turns for tiny anchors), rather than a new block. This avoids a fourth block but still pays the 26-literal cost and still has no measured lift over the pin.
- **Option C — fold into the time-anchor block:** tiny clock anchors (A5-class) are already time-anchors; no separate reservation needed.

Judged against PROBE-BANKS' receipted facts: the latch's reservation is subsumed by the composition's time-anchor block (clock facts) plus the literal-pin (recurrence ≥3 covers the high-value anchors). The reserved set (len ≤6, any recurrence) overlaps the pinned set on the high-recurrence tiny anchors; the non-overlapping tail (single-occurrence tiny literals) is exactly the semantic-absorption class that the derivations block already addresses via inferential chains. So the latch adds no independent block.

## 6. The real-ground measurement (RESULTS-SEAMINT)

`krecency/RESULTS-SEAMINT.md` (commit 43fb643bc5, `probe_seamint.py`, `results/seamint.csv`):

| variant | deep_minima_prevalence | reserved_set_size |
|---|---|---|
| none | 0.80 | 26 |
| literal-pin | 0.00 | 26 |
| pin+retention-latch | 0.00 | 26 |

Verdict: **LATCH-NOOP**. The literal-pin alone already carries the real conversation streams (0.00); the latch's standing redundancy is named — a finding, not a failure. The falsifier (§3) fires: `pin+retention-latch` prevalence == `literal-pin` prevalence (0.00 == 0.00), no delta; the latch does not drop prevalence below the pin-alone floor.

## 7. Verdict: PARK-WITH-REASON

**PARK** the retention-latch as a distinct adoption (do not add a fourth block; do not modify the verbatim-reservation's construction for this). Reason, receipted:

1. **Redundancy on real ground:** literal-pin reaches 0.00 on real streams; latch adds no prevalence gain (RESULTS-SEAMINT LATCH-NOOP).
2. **Cost-line non-transportability:** 3 tokens (synthetic death-cell) → 26 reserved literals (real streams); the latch's headline cost claim does not survive real loads, and the real cost is ~9× with no measured benefit.
3. **Subsumption by the cleared composition:** the 3-block composition already clears the seam (0/5 below 3.0); the latch's target class (tiny+old) is covered by the time-anchor block (clock facts) + the literal-pin (recurrence) + the derivations block (inferential chains). No residual for a fourth block to lift.
4. **Mechanism-level caveat (from RESULTS-SEAMFIX):** the seam-mechanism's deeper driver is semantic-distance absorption, which ordering/re-ranking alone does not counter; the latch (retention) addresses retention priority (mechanism (b)) but not absorption (mechanism (a)). The three-block composition addresses absorption via derivations; the latch would duplicate, not complement.

**Adoption-candidate status:** the latch remains the record's first standing *invention* (r=1.0 at the death-cell, RESULTS-RETENTION) and is retained as a documented mechanism + death-cell receipt, but it is **not** adopted into the real compaction build path. It is parked, with the reason above, pending a future cell where literal-pin does *not* already reach 0.00 (e.g., a cell dominated by single-occurrence tiny anchors with no recurrence to pin) — at which point the latch's reservation would be re-tested against its falsifier (§3).

## 8. Honest walls (named, not smoothed)

- **Live-provider full-eval is the gate's next, not this arm's.** The composition's 0/5-below-3.0 and the latch's LATCH-NOOP both ride synthetic/simulated probes and mined-stream literals, not a live provider eval. The latch's adoption decision is only as good as those. The real gate is the full-eval at the provider window (per EXP-SUMMARY-NIGHT-20261106).
- **Depth-vs-density separation not certified by bytes.** Per PROBE-BANKS honest wall + EXP-REBUILD-CERT: the banks certify fact presence only; the latch's Cell A (deep) vs Cell B (dense) applicability rides the battery at substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`.
- **Reserved-set size (26) is mined-literal dependent.** It depends on the `request_dump_*.json` mining (SHA/path/flag regexes) and the `len ≤ 6` threshold; a different mining or threshold re-derives a different number. The 3-token synthetic figure and the 26-literal real figure are not the same measurement; do not conflate.
- **Single-occurrence tiny anchors are unaddressed by both pin and latch-in-composition.** If a future cell shows these driving losses, the latch is the candidate to revive — but only after re-running §3's falsifier on that cell.

## 9. One-line verdict + next mechanism

PARK-WITH-REASON: the retention-latch is redundant on the real ground (literal-pin already 0.00; 3→26 reserved literals; no delta vs pin), so no fourth block is added to the 3-block composition; the next mechanism is the live-provider full-eval at the substrate pin (the gate's next, not this arm's). Artifact: `studies/rfc-143379-rig/SEAM-INTEGRATION-20261106.md`.
