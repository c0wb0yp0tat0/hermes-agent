# RESULTS-E3-CONTINUATION-20261106 — the continuation-loss pattern-probe (E-3)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork). **Seat:** the handoff's E-3 — WHY the forward-facts evict at the compressed-state's construction. **Gated on:** `SEAM-INTEGRATION-20261106.md` (E-2 verdict — the retention-latch NOOP vs the pin on the real streams). **Register:** receipts, never claims — every figure traced to the suite JSONs, the krecency CSVs, the probe-banks, or the seam documents below.

## (a) Loss-classification — the measured loss-front and the small+old geometry

**Ground.** Three suites (config / debug / feature-impl), 3 runs each, medians reported; krecency per-movement A/Bs sharing one baseline; probe-banks over the two real cells. The measured loss-front (from the suite report legs and the krecency per-movement A/Bs) is content-patterned: the compactors evict discrete tiny+old anchors while the same compaction machinery at the same depth leaves a structurally similar stream clean.

### A. The measured loss-front (suite data, receipted)
| probe | fixture (cell) | overall median | loss class | evidence (run JSON / report) |
|---|---|---|---|---|
| continuation-execution-time | config-build-competitive-scouts (A) | 0.17 | continuation | run-1..3: "The answer is empty, providing no information required by the probe question." (suite-config report) |
| decision-core-claim-validity | debug-session-feishu-id-model (A) | 0.00 | decision | run-1..3: "No answer provided; cannot assess any dimension." (suite-debug report) |
| continuation-next-action | debug-session-feishu-id-model (A) | 0.67 | continuation | run-1..3: "states no further action was requested, but expected facts indicate the next action is to close the PR and implement ourselves" (suite-debug report) |
| continuation-implementation-scope | debug-session-feishu-id-model (A) | 1.00 | continuation | run-1..3: "No answer provided; fails all dimensions." (suite-debug report) |
| recall-upstream-confirmation | debug-session-feishu-id-model (A) | 2.00 | recall | run-1..3: "omits the expected concrete anchor that same user has different Open IDs in different apps" (suite-debug report) |
| decision-saturday-fill | config-build-competitive-scouts (A) | 2.83 | decision (residual) | run-1..3: mis-states the split reasoning (suite-config report) |

Control slice: `suite-feature-impl-context-priority` (A) — overall median 4.67, misses=[] (clean). Same compaction machinery, same depth (44794 → 14021, 68.7%, 69 of 75 msgs retained): the control carries zero below-bar probes. That is the receipts basis for the content-patterned (not uniform) loss — the loss concentrates in the tiny+old anchor facts, not in the architecture.

### B. Small+old geometry (fixture bytes, anchors named at the letter)
- Cell A (`rung/fixture-deep-compaction-real.json`, 8 msgs, model `control-model`): the small+old class — the latch's design target. Exact anchors, each a single-occurrence literal in the fixture's bytes (PROBE-BANKS-20261106 receipted): `session_20261007_123305_f3465b` (A4, 1×), `2026-10-07T12:33:05` (A5, 1×), `control-model` (A6, 1×), `truncated_to: null` (A7, 1×), `/root/.hermes/sessions/session_20261007_123305_f3465b.json` (A8, 1×), user open 77 chars (A9), user close 188 chars (A10), open-message head `Control` (A11). The seam-mechanism (RESULTS-SEAMMECH) names the exec-time/next-action/scope anchors as the below-3.0 probes; the seam-integration (SEAM-INTEGRATION) says the latch's reserved set at real loads = 26 tiny+old literals (≤6 chars), token budget 26 (RESULTS-SEAMINT).
- Cell B (`rung/fixture-high-density-real.json`, 2 msgs, system 30846 chars / user 219239 chars): the dense-stream class — NOT the small+old class; the latch's tiny+old reservation has no purchase there (no compaction-path turns to age).

### C. Cross-tab: the loss-front against the small+old geometry
| probe | fact the probe demands | in the small+old geometry | measured loss (median) |
|---|---|---|---|
| continuation-execution-time | clock-stamp `2026-10-07T12:33:05` (A5) | tiny+old (Cell A) | 0.17 |
| decision-core-claim-validity | `control-model` pin + execution-time class (A6) | tiny+old (Cell A) | 0.00 |
| continuation-next-action | next-action / state-transition anchor | tiny+old (Cell A) | 0.67 |
| continuation-implementation-scope | scope class anchor | tiny+old (Cell A) | 1.00 |
| recall-upstream-confirmation | upstream-confirmation anchor | tiny+old (Cell A) | 2.00 |
| decision-saturday-fill | decision reasoning on openrouter/win | not the small+old class | 2.83 (residual, still below bar) |

Counts from fixture bytes: Cell A anchors (A4–A11) are all single-occurrence, ≤3 tokens, introduced before the continuation → age = old; the bank's receipt ledger greps each literal once in the fixture. Seam (E4, RESULTS-SEAMMECH): tiny+old 17/21 lost (81%); large+old 4; tiny/large+recent 0. Age axis trivially "old" (all probe facts introduced before the continuation). The E-2 arm's NOOP context is held: pin alone floors the REAL streams at 0.00; the latch's 3-token reserved set balloons to ~26 literals at real loads; no delta vs pin (RESULTS-SEAMINT: none 0.80 / literal-pin 0.00 / pin+retention-latch 0.00, reserved_set_size 26/26/26).

## (b) Falsifier's verdict — does the small+old class carry the continuation/decision losses?

The falsifier held by the handoff asked whether the small+old geometry is the class that carries the continuation/decision losses in the native fixtures' measured data. Answers, receipts on receipts:

- **Yes on the geometry.** The continuation/decision probes whose facts are the tiny+old anchors (A5 session-stamp, A9/A10 open/close, A6 model pin) are exactly the probes that evict at the compression front: 0.17 / 0.00 / 0.67 / 1.00. The E-2 arm's measured Cell A is the same class the latch was designed for. RESULTS-SEAMMECH names both drivers from code: `_build_anchor_index` ranks anchors by `(-counts[v], -last_seen[v])[:cap]` (frequency+recency) — single-occurrence tiny facts lose the cap race; `_build_verbatim_user_section` scopes verbatim retention to user turns, so the tiny+old anchors that live in assistant/tool turns are not verbatim-preserved; `_fresh_compaction_message_copy` drops sidecar ordering hints (the reservation must survive the fresh copy, not just pre-copy). The seam's mechanism is therefore absorption plus eviction, gated by age×size.
- **The latch's adoption adds no delta on the real side.** No delta vs pin (RESULTS-SEAMINT, LATCH-NOOP): none 0.80 / literal-pin 0.00 / pin+retention-latch 0.00 with reserved_set_size 26 at every variant. So the small+old class carries the losses (the forward-facts evict because the tiny+old anchors are not anchored into the compressed state), but the latch as built does not lift them — the pin alone floors the REAL streams at 0.00.
- **The krecency per-movement A/Bs pin the mechanism.** Exec-time 0.17 → 3.33 and decision-core 0.00 → 3.00 are recovered by the time-anchor block (~60 tokens: 8 absolute-clock facts at ~6 tokens each + ~12 tokens overhead). Next-action clears only when the forward-intents block (~60 tokens) is layered on top of the sealed composition (derivations ~120 + time-anchors ~60 + forward-intents ~60 = ~240 tokens). Derived-keeps (~120 tokens) lift next-action/scope/recall but leave exec-time 1.33 / decision-core 1.67 below bar. The driving class for exec-time and decision-core is the absolute-clock facts = the tiny+old anchors of Cell A; next-action is the one residual that needs forward-intent (not a time-anchor) — consistent with the seam's verdict that the residual's driver is the forward-intents verbatim lines, not the retention rank.

Verdict: the small+old class carries the continuation/decision losses (the measured loss-front maps onto the tiny+old geometry), and the latch's adoption is a NOOP on the real side — the pin alone reaches 0.00.

## (c) Mechanism's named shape

- **Eviction.** The compaction front ranks by recency/salience (`_build_anchor_index`, `(-counts[v], -last_seen[v])[:cap]`, ~1045): single-occurrence tiny facts lose the cap race; verbatim retention is scoped to user turns (`_build_verbatim_user_section`, ~956), so the tiny+old anchors in assistant/tool turns evaporate; `_fresh_compaction_message_copy` (~344) drops sidecar ordering hints, so a pre-copy reservation must be re-injected post-copy, not pre-copy.
- **Absorption.** The same tiny facts are low-salience anchors whose semantic distance from the retained topic cluster is large — they are absorbed into the summary rather than surviving as discrete anchors (mechanism (a), RESULTS-SEAMMECH).
- **Neither alone rescues.** RESULTS-SEAMFIX (FIX-NOOP): a retention re-rank alone addresses ordering, not absorption, and the tiny+old loss (81%) is gated by age AND size (tiny+recent eviction is 0, so age gates size; large+old 4 vs tiny+old 17 at the same age, so size interacts). The measured shape is MECHANISM-MULTI — both drivers named with code citations, no wall clause triggered.
- **The seam-arc's measured shape.** The dominant driver of the loss-front is eviction+absorption of the tiny+old anchors (Cell A). The residual (next-action) is fixed by the forward-intents block, not by the retention re-rank. The latch's adoption is a NOOP on the real side (RESULTS-SEAMINT), so the mechanism's named shape for the loss-front is: eviction + absorption of the tiny+old anchors, and the remaining gap is a content-supply gap (next-action), not an ordering gap.

## (d) Next-arm recommendation

- **Honest candidate.** Verbatim anchor promotion at the compression front: widen `_build_verbatim_user_section`'s scope to the tiny+old anchors in assistant/tool turns, and re-inject the reservation post `_fresh_compaction_message_copy` (the seam's secondary lever, RESULTS-SEAMMECH §2). NOT a retention re-rank: RESULTS-SEAMFIX already showed ordering alone cannot counter the age×size-gated loss (FIX-NOOP, medians unchanged 4.00 / 4.33 / 4.67).
- **Gate.** Run the A/B without a live provider — the fixture's own bytes are the ground truth (PROBE-BANKS receipted), and the seam-mech / seamfix / seamint receipts (0.00 vs pin) are the controls. The E-2 arm's NOOP context is held: the latch's adoption must reproduce the pin's 0.00 on the REAL streams and then lift exec-time / decision-core / next-action above the 3.0-bar on Cell A's own measure — the pin alone floors at 0.00, so the acceptance bar is lifting the below-3.0 probes, not merely holding the floor.

## Register (receipts, never claims)
- `SEAM-INTEGRATION-20261106.md` — E-2: retention-latch NOOP vs pin on the real streams; pin alone floors the REAL streams at 0.00; latch's 3-token reserved set balloons to ~26 literals at real loads; no delta vs pin.
- `RESULTS-SEAMINT.md` — LATCH-NOOP: none / literal-pin / pin+retention-latch → deep-minima prevalence 0.80 / 0.00 / 0.00; reserved_set_size 26 / 26 / 26 (tiny+old ≤6 chars, real streams).
- `RESULTS-SEAMMECH.md` — MECHANISM-MULTI: tiny+old 17/21 lost (81%); large+old 4; tiny/large+recent 0; `_build_anchor_index` `(-counts,-last_seen)[:cap]` (~1045); `_build_verbatim_user_section` (~956); `_fresh_compaction_message_copy` (~344); mechanism (a) absorption + (b) recency/salience ordering.
- `RESULTS-SEAMFIX.md` — FIX-NOOP: re-ranking alone cannot counter the age×size-gated 81% loss; semantic-distance absorption requires verbatim anchor promotion; medians unchanged 4.00 / 4.33 / 4.67.
- `suite-config-build-competitive-scouts` (3 runs): overall 4.33; below-3.0: decision-saturday-fill 2.83, continuation-execution-time 0.17; pre 25813 → post 21401 (17.1%).
- `suite-debug-session-feishu-id-model` (3 runs): overall 4.00; below-3.0: recall-upstream-confirmation 2.00, decision-core-claim-validity 0.00, continuation-next-action 0.67, continuation-implementation-scope 1.00; pre 27977 → post 10499 (62.5%).
- `suite-feature-impl-context-priority` (3 runs): overall 4.67; misses=[] (clean control; 44794 → 14021, 68.7%).
- `krecency/results/{compose,intent,anchor,infer}.csv` (shared baseline exec-time 0.17 / decision-core 0.00 / next-action 0.67 / scope 1.00 / recall 2.00): time-anchor block ~60 tokens lifts exec-time 1.33→3.33, decision-core 1.67→3.00; forward-intents block ~60 tokens lifts next-action to 3.00; derived-keeps ~120 tokens lift next-action/scope/recall but leave exec-time 1.33 and decision-core 1.67 below bar. Composed budget ~180 tokens (~1.8% of 10K); intent budget ~240 tokens (~2.4%).
- `PROBE-BANKS-20261106.md` — Cell A = deep-compaction real (`fixture-deep-compaction-real.json`, 8 msgs, small+old class, anchors A4–A11); Cell B = high-density (`fixture-high-density-real.json`, 2 msgs, dense class, system 30846 chars / user 219239 chars) with no latch purchase.
- `krecency/SYNTHESIS.md` waves 21–27 — composition contiguity: derivations ~120 / time-anchors ~60 / forward-intents ~60.
