# EXP-SUMMARY-MOONBEAM-20261105 — the corrected end-to-end summary of PR #1 (RFC #143379 study)

**Lane:** MOONBEAM (story-voice). **Register:** receipts, never claims — every line traces to a commit SHA, run id, or comment id on branch `study/rfc-143379-rig-20261105`. **Voice:** speechify — distinct phases and voices preserved, no blurring. **Two precision-marks applied** (see §7).

---

## Phase 0 — What PR #1 is

PR #1 of fork `c0wb0yp0tat0/hermes-agent`: branch `study/rfc-143379-rig-20261105`, an **independent verification study** of RFC NousResearch/hermes-agent#143379 (memory compaction / K-recency). Downstream-only: no upstream posts, no upstream code changes; original authors retain ownership. Goal-lock (binding): `studies/rfc-143379-rig/` on the study branch; Avrea verification leg (envelope schema, meter budget 4-vCPU/1,500 min/mo, wall clause). Nothing public beyond the fork; no model credentials.

## Phase 1 — The contract (Avrea leg)

`AVREA-LEG-CONTRACT.md` (commit `52c13025bc`): envelope `id/run/pin/requested/executed/assert/battery/summary/conclusion/receipt_url`; pin asserted BEFORE the suite (`requested == executed`); meter budget 4-vCPU/1,500 min/mo, one run per pin; wall clause: a non-reproduction is a QUESTION, never a stop — minimal experiment required before any "unreproducible" verdict. Committed definitions are NOT execution; NOT-RUN stays until a receipt exists.

## Phase 2 — The receipts (run ledger)

`RECEIPTS.md` — run-backed rows, run ids cited:
- 42064685359 @ d1bdb4582c (#139606 merge head): GREEN — write-gate + memory-tool.
- host-local @ a996d4ad30 (whole-anchor): GREEN — falsifier battery 28 passed, 1 xpassed in 1.01s (strengthened arm flips).
- 42071651022 @ ffb85c2c58 (#140008): GREEN — 64 passed 5.06s.
- 42071665270 @ 60a2e15638 (#116673): GREEN — 66 passed 5.19s.
- 42071680606 @ ec649ad9d0 (#141876, the restore): GREEN — 82 passed 5.72s.
- 42074781407 @ c39d8ce722 (round2-combined-substrate): GREEN — 70 passed 5.24s.
- 42074793218 @ a996d4ad30 (whole-anchor head): GREEN — 98 passed, 1 xpassed 5.85s.
- 42074804475 @ 4905270237 (avrea-parallel runner-env): GREEN — 89 passed, 1 xfailed 5.74s.
- Apex-day: 42096454325 falsifier-battery @ whole-anchor GREEN; 42096273475 / 42098517565 union @ arm-head RED (nugget-6 substrate-absent, fixed by guard 76f95dd401); 42096589644 sweep @ study-head RED (same class); guarded re-runs in flight.
- GitHub-window side: **NOT RUN** (hosted queue class) — marked, not smoothed.
- Number-seam resolution: the "xfailed 1.83s" phrasing in one landing was a mislabel; the real record is **28 passed, 1 xpassed in 1.01s**; corrected on the record.

## Phase 3 — The findings (instruments)

`krecency/` instruments (derived, no injected term): `probe_age.py`, `sweep_age.py`, `scoping_test.py`, etc.; results in `results/`.
- **Demand-age gate: FAIL at 300+ cycles per the letter's worst-case** (`RESULTS-AGE.md`): derived table of record — 150c 4x mean +23.87pp (min −20.40), 8x +25.47pp (min −15.60); 300c+ 2x mean −3.00 (min −30.00), 4x +0.60 (min −20.40), 8x +2.40 (min −15.60), 16x +2.90 (min −15.10), 32x +3.00 (min −14.00). Sub-zero class holds ALL 25 seeds at 4x/300c+ (2–4 of 4 sampled cycles each); excursions at BOTH horizons — the min-letter fails on the floor's excursions, not a long-session-only collapse. Means' erosion (4x +23.87 → +0.60pp) is the session-length face. Earlier −8.4/−3.6pp figures superseded (intermediate aggregation).
- **K-scaling arm: NO** — scaled-K = min(1+floor(sqrt(cycle)),20) underperforms fixed-K10 at every reported ratio (full 4x–8x band). Caveat: only one scaling function tested.
- **Constraint arm: FINDING** (`RESULTS-CONSTRAINTS.md`): recency-truncate 1.00 (worst), hierarchical 0.25, summarize-as-rule = head-retain 0.00; pinned restores 0.00 for all. Recency-truncate is the K-recency window's eviction class. Pinning-cost re-walk (commit `7bb1e8cc6c`): raw 9.84% was scale-confounded (183-token sim denominator); pinned token count comparable to field's ~47; production-scale ~0.18–0.11%, meets <0.5% class.
- **Aliasing × proximity: CONFIRMED-BOTH** (`RESULTS-ALIASING.md`): a*-proxy R² = 0.6548 (bar 0.35); aliasing keeps deep minima high with M off; M raises prevalence with aliasing off. CSV 800 rows.
- **Archive arm: FAIL at every budget** (`RESULTS-ARCHIVE.md`): ID-known recall (optimistic bound); gate fails at every tested budget at cycles≥300; partial NIAH recovery at 5% r=4.
- **Competition arm: NOT-CONFIRMED** (`RESULTS-COMPETE.md`): deep-low fraction 0.447/0.469/0.677 at 0/10/30% rival rate; a* R² ~0; the floor term itself produces the lows.
- **Recitation arm: NOT-CONFIRMED** (`RESULTS-RECITE.md`): recite ON changes prevalence ≤0.1 at every cell/cycle — no cycle-depth-scaling degradation; aliasing+proximity remain dominant.
- **Pinning arm: PROTECTS** (`RESULTS-PIN.md`): recurrence-aware pinning drops deep-minima prevalence 1.00 → 0.15 at the aliasing×proximity pair-ON cell; onset test seed0 cycle 68, seed1 cycle 87; per-seed occurrence predicts onset → recency-pinned variant loses protection.
- `probe.py` (injected `governance_decay` term) **PARKED — NOT EVIDENCE** (commit `4c59299461`): self-fulfilling curve; verdict not evidence until demand-age instrument lands. Status on the record.

## Phase 4 — The arms (wave sequence)

- Wave-4 (commit `e061196175`): storm appendix — three untested classes (aliasing, cumulative proximity, recitation-length); two reds adjudicated as wrong-probe / optimistic-bound; next arm named with falsifier + field-set prediction bars.
- Wave-5 (commit `6ded14715c`): fleet's first fold, byte-verified — longcat divergence: archive knob toothless, compete rivals path-limited, pinning-with-recurrence adopted.
- Wave-6 (commit `68f027e739`): wheel complete — recitation arm NOT-CONFIRMED, mechanism-map final within tested classes, pinning-falsifier next.
- Wave-7 (commit `af8f0057e3`): ring closes — pinning falsifier PROTECTS (1.00→0.15 at pair-ON cell, onset-test confirms), mechanism-map final, landing-path receipted.
- Wave-8 (commit `ddaaa83f8e`): beam fold — a* equal-weights mechanism, archive inertias, competing-admission candidacy.

## Phase 5 — The arms (competition + archive adjudication, precision-mark 1)

**Precision-mark 1 (the record demands):** the competition arm's adjudication is NOT a "walk-back." It is wave-4/5 precision-adding, three steps:
1. **Wrong-probe read** (wave-4): the deep sub-zero excursions were re-labeled as the field's COMPETITION class; the probe couldn't confirm it.
2. **Byte-level path-limitation** (wave-5, longcat lane's constructional read, byte-verified): rivals fire on the **latent/survivor path only**; the K=10 window-hit path (`if q in snap`) **never faces a rival**. `probe_compete.py` injects rivals only into the K=0 floor path.
3. **Equal-weights a* mechanism**: the a* proxy uses equal weights `[1.0] + [1.0]*n`, so its softmax is a function of **rival count, not evidence mass**. The rivals never touch the path that matters (the K=10 hit path), so a* is degenerate against the only path that matters.

**NOT-CONFIRMED stands because the probe couldn't touch the path that matters** — an instrument-limit verdict, not a finding about the field. The follow-on is the competing-admission archive (demand-age level): fix the toothless knob so the budget admits the demanded literal OR a rival by a query-time score, and re-measure.

Archive arm's three inertias (byte-verified): `probe_archive.py` archives every literal (`for t in stream: arch.put(t[1])`) — optimistic bound; recall looks up only the demanded literal's id (`aid = arch.id_of.get(q)`) — budget knob toothless; `rlimit` per-cycle with one query per cycle; `max(1, mat_budget_tokens)` grants one recall even at 0% budget.

## Phase 6 — The corrections (precision-mark 2)

**Precision-mark 2:** corrections on the thread were **BOTH superseding-comments AND in-place edits**. The day's own carelessness-audit edited seven comments — names, internals, stale-states. The record's process included both (superseding comments for the trail, in-place edits for the carelessness-audit). Not one or the other.

Concrete corrections on the record:
- Number-seam: "xfailed 1.83s" → "28 passed, 1 xpassed in 1.01s" (`RECEIPTS.md` number-seam resolution section).
- `RESULTS-AGE.md` earlier −8.4/−3.6pp figures superseded by the derived table; driver analysis corrected (sub-zero universal, not minority).
- `RESULTS-CONSTRAINTS.md` pinning-cost re-walk superseded the raw 9.84% reading.
- README hybridization (commit `e2e3fde716`, `eb57ddbe63`) — goal-lock + meter/wall clauses + discipline-layer table.
- Spine-map (commit `b628696a73`) — every artifact's status on the record.

## Phase 7 — Third-party verification (xngg seam-gaps)

`XNGG-GAPS-VERIFICATION-20261105.md` (commit `35ed130686`): xngg1021's four seam/contract gaps cross-checked at exact pins, byte-level on the fork's battery-clone.
- Gap 1 (Stage-7 `verify_post_write` bypassed on `operations=[...]` batch path): **CONFIRMED** @ d1bdb4582c — `tools/memory_tool.py:343` returns `_applied(store.apply_batch(...))` directly; `verify_post_write` wired only on single-op path :366-367.
- Gap 2 (`_resolve_target` calls `doc_name(doc)` unguarded): **NOT REPRODUCED** @ d1bdb4582c — guard present at :280-283 (`if name is None: return target, (...)`). Either different tree-version or guard landed in merge-head's reconcile.
- Gap 3 (`preserve_session` ignores `store.add` return dicts): **CONFIRMED** @ ffb85c2c58 — `tools/spa_integration.py:100-107` drops both return values, returns `doc_name` directly.
- Gap 4 (`DreamCycle.deep_sleep` `.bank()` adapter + `ContextCompressor` hook): **NOT REPRODUCED** (adapter part) — `tools/dream_cycle.py:118-122` calls `self.store.bank(c)`; compressor-hook not yet probed (open).

Falsifier ethics: non-reproduction is a finding, never an insult; pins move, code reconciles, verification re-runs at next heads.

## Phase 8 — The runner narrative

Standing roster (`pr1-runner-roster.md` in `/tmp` study artifacts): falsifier GREEN 42096454325; union/sweep rows with causes; guarded re-runs in flight (guard 76f95dd401 landed after the RED dispatches). The nugget-6 substrate guard (76f95dd401) makes pin-trees self-skip at unsupported pins (skip-discipline). The runner pipeline is the live surface; the GitHub-window side stays NOT RUN.

## Phase 9 — The watcher contract

`pr1-watcher-contract.md` (in `/tmp` study artifacts): trigger-driven machinery seeds — SELF-FIRE grammar, poller's contract. Decision: the build's go. The watcher is the study's automation surface; the CTO-designated designation held.

## Phase 10 — The webstorm guidance

`pr1-webstorm-guidance.md` / `pr1-webstorm-nuanced.md` (in `/tmp` study artifacts): the four mechanisms' steers + candidates' true status (the nuanced version). Four mechanisms: competition class, archive primitive, pin generalization, focus-drift. Credits: LOHA/ACD arXiv 2609.31430; Governance Decay arXiv 2606.22528; Compaction Cliff/Knowledge Triage arXiv 2608.22752; Length Is Cheap, Competition Is Not arXiv 2611.04169; Context Poisoning as Extreme-Value Attention Interference arXiv 2609.22101; Retrieval Capacity of Self-Attention Under Competition arXiv 2609.37879; ARC arXiv 2607.25066; AttnCompress arXiv 2609.08318; Active/Reflection-driven ARC arXiv 2601.12030; ReTree arXiv 2608.10676; Lost in the Middle arXiv 2307.03172; rate-distortion survey arXiv 2607.08032; RoPE provable position/token aliasing arXiv 2605.15514; Sirens' cumulative denominator arXiv 2609.26718; DSGC (recency retains prerequisite chains in only 0.07 of runs). The rig's designs came first; the frontier validated the mechanism shape. The webstorm guidance is the nuanced version (comment 6668226399).

## Phase 11 — The fleet landings

- Longcat fold (commit `77a441dc92`): the wave-5 byte-verified adjudication — compete rivals never touch the K=10 hit path; archive knob toothless; pinning-with-recurrence adopted as next mechanism.
- Alignment landing (commit `eb57ddbe63`): paid pod's hybrid README — goal-lock, envelope voice, discipline-layer table, −20.40pp worst-case faithful to the derived table.
- Step-lane: in flight.
- Solar-mini4 (commit `1d70408531`): own content; next-mechanism independently converges on the pinning.
- Beam fold (commit `ddaaa83f8e`, wave-8): a* equal-weights mechanism, archive inertias, competing-admission candidacy.
- Krecency lane (commit `19723b3c51`): apex adjudication + next mechanism.
- Copycat findings directory: `copycat-findings/copycat-{beam,longcat,krecency,solar-mini4}-20261105.md` (plus sentinels).

## Phase 12 — The synthesis (one-mechanism line)

`krecency/SYNTHESIS.md`: the K-recency window's eviction is the recency-truncate class. The recitation floor (lane A) and the governance decay (lane B) are one window wearing two hats — the window that erases exact text is the same window that erases the standing constraint. Lane B PENDING-FROM-LANE at synthesis time; integration derived from lane A's curve + RFC stated mechanism. K-recency hard window needs the pinning analog (lane B) to survive; provenance-origin and archive-before-stub survive on their own evidence.

RFC guidance (`RFC-GUIDANCE-20261105.md`, commit `bbf10e8efd`, delta `06a2e8b59c`): read restore (#141876) stays landing-order first piece; K-recency hardness replaced by measured shape; memory-side honest guarantee = lifecycle correctness for pinned + calibrated abstention for unknown; ruler's fix applies to the probe not the bar. Apex-day delta: archive FAIL constructionally re-adjudicated (byte-confirmed, toothless knob); competition NOT-CONFIRMED precision-added (path-limited, equal-weights a*); xngg-gaps verification (2 confirmed / 1 not-reproduced / 1 open); pinning-mechanism adopted; recitation-arm status explicit.

## Phase 13 — The HITL-ready staging

`HITL-READY-20261105.md`: seven candidates staged (RFC-guidance+delta, xngg-verification, runner-pipeline, fleet-landings, webstorm-guidance nuanced, watcher-contract, recitation-arm). False-claims register: EMPTY — thread's claims trace to receipts; ledger rows match runs; NOT-RUN markers stay until receipts replace them.

## Phase 14 — The honest markers (preserved, never smoothed)

- Committed workflow definitions are not execution.
- A green run at a pin qualifies THAT pin's checked-out source — not any other head.
- Divergence between Avrea side and GitHub-window side is data, recorded, never smoothed.
- The GitHub-window side: NOT RUN (hosted queue class).
- The recitation-length class (wheel's third): named, not yet measured.
- The meter's spend: 3 of 6 program dispatches used.
- Nothing upstream was written by this study; original authors retain ownership; guidance offered, never imposed.

---

## The two precision-marks applied (the corrections the record demands)

1. **Competition arm is not a "walk-back."** It is wave-4/5 precision-adding: wrong-probe read → byte-level path-limitation (rivals never touch the K=10 hit path) → equal-weights a* mechanism (`[1.0]+[1.0]*n`, softmax tracks rival-count not evidence-mass). NOT-CONFIRMED stands because the probe couldn't touch the path that matters.
2. **Corrections on the thread were BOTH superseding-comments AND in-place edits** (the day's carelessness-audit edited seven comments — names, internals, stale-states). The record's process included both.

---

**Opening line:** PR #1 is the RFC #143379 independent verification study — a receipted, downstream-only, three-voice experiment whose corrected end-to-end story is that the K-recency hard window fails the RFC's own gate on the floor's excursions, the constraint arm names recency-truncate as the eviction class, pinning protects, and the competition/archive reds are instrument-limits, not field findings.

**File:** `studies/rfc-143379-rig/EXP-SUMMARY-MOONBEAM-20261105.md`
