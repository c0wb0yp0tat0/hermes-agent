# SWAP-A-ADVANCE-A-20261106 — leg A's seam advanced: what mechanism other than per-run promotion could lift the GLOBAL structure?

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Seat:** copycat lane (beam-1.0-501b-a23b:free) — the SWAP-1 rotation's swap-leg, head's fold pending. **Domain:** COMPLICATED. **Register:** receipts, never claims. **Hand-separation:** [1st] = re-read by this lane this pass; [2nd] = carried from a study doc and not re-derived here.

## [Executive Summary]

**Verdict: PER-RUN PROMOTION IS NOT THE ONLY LEVER, BUT NO SINGLE CANDIDATE IS YET LICENSED TO LIFT GLOBAL STRUCTURE; THE HIGHEST-VOI CANDIDATE IS A CROSS-RUN THEME-INDEX BUILT AT READ TIME, NOT AT WRITE TIME.**

The ground is settled by two receipts (both [1st] this pass):
- `NEGENTROPY-SWEEP-A-RESERVED-LAQ-20261106.md`: reservation is a *per-run write-side* promotion; it lifts local decision/continuation survival toward ≥3.0 (intent block 3.00 clears; anchors 2.67) but leaves cross-run theme-membership at 0 on every rung. Local lift is real; global lift is zero.
- `LAQ-FIDELITY-PROBE-20261106.md`: G-LOST on every rung; the k-term is flat (kept-rates 0.42/0.29/0.26/0.32) — no differential by class, so no global theme structure exists in the kept-set at all.

Therefore leg A's CREATOR-GAP is not "promotion was too weak" — it is "promotion is the wrong *axis*": any mechanism that only writes per-run cannot reconstruct a cross-run relation. The lift must come from a mechanism that is (a) cross-run by construction, or (b) read-side, where multiple runs' states are jointly available. This artifact names the candidate-planes, each as a method-card (trigger / essence / failure-risk / success-signal), and orders them by VOI.

**The candidate-plane ranking (VOI order):**

| rank | candidate-plane | axis | VOI | why |
|---|---|---|---|---|
| 1 | Cross-run theme-index (read-time build) | cross-run + read-side | HIGHEST | only candidate that is cross-run by construction; directly targets theme-membership; no write-side cost; falsifiable against the ladder's 16 runs |
| 2 | Inter-run anchor-sharing (run-linked literals) | cross-run + write-side | HIGH | lifts the per-run reserved tier into a shared pool; but still write-side; depends on run-identity being stable |
| 3 | Global-summary build (across runs) | cross-run + summary-side | MEDIUM-HIGH | targets the summary_text that probes read; but judge-gated and empty-answer-confounded (Wall W2) |
| 4 | Run-linking / run-graph (explicit links between runs) | cross-run + meta | MEDIUM | enables 1–3 but is infrastructure, not a lift mechanism itself |
| 5 | Cross-run cue-conditioned completion (RippleMem-class) | read-side + cue | MEDIUM | read-side repair of the read-gap; fits session_search recovery footer; does not itself create global structure |
| 6 | Provenance-origin / archive (query-time recall) | query-side | LOW (refuted) | archive class refuted under tested construction (competing-admission still fails gate); query-blind admission |

**Recommendation (one line):** build the cross-run theme-index at read time first (rank 1), measured against the ladder's cross-run theme-membership probe (success-signal: coherence > 0 across the 16 runs, k-term differential by class), before spending on write-side run-linking (rank 2) or global-summary (rank 3).

## [Analysis Brief]

### Ground read (first-hand this pass)
- `NEGENTROPY-SWEEP-A-RESERVED-LAQ-20261106.md` (Executive Summary + Analysis Brief + the probe table) — [1st].
- `LAQ-FIDELITY-PROBE-20261106.md` (Executive Summary + §1 + §2) — [1st].
- `NEGENTROPY-ARM-20261106.md` (Executive Summary + code facts C1–C5 + the reserved-tier design) — [1st].
- `ADJUDICATION-NEGENTROPY-20261106.md` (four verdicts + k-seam) — [1st].
- `SEAM-INTEGRATION-20261106.md` (the latch mapping + falsifier) — [1st].
- `NETWORK-LINE-ANCHORCHAIN-20261106.md` (anchor-chain mechanics + RippleMem borrow) — [1st].
- `PROBE-BANKS-20261106.md` (the bank-protocol + the two cells) — [1st].
- `RFC-GUIDANCE-20261105.md` (the measured verdicts + landing-path) — [1st].
- `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` (four classes + weights + walls W1–W7) — [1st].
- `BEARINGS-FRONTIER.md` (open edges E1–E5) — [1st].
- `SELF-PERPETUATING-LOOP-ARCHITECTURE.md` (the cycle + invariants) — [1st].
- `copycat-findings/copycat-*.md` (six lanes' adjudications + next mechanisms) — [1st].
- `krecency/RESULTS-{RETENTION,SEAMMECH,ANCHOR,INTENT,COMPOSE,SEAMFIX,SEAMINT,CROSSINGS,AUDIT}.md` — [1st].
- `rungs/fixture-deep-compaction-real.json`, `rungs/fixture-high-density-real.json` — [1st reference via PROBE-BANKS byte-shapes].

### The settled facts (the ground the candidates must beat)
1. **Local lift is real, global lift is zero.** Reservation lifts per-run decision/continuation survival toward ≥3.0 (intent 3.00 clears; anchors 2.67) but cross-run theme-membership stays 0 (G-LOST on every rung). The gate-line holds: `local-neighbor survival != global structure`.
2. **The k-term is flat.** Kept-rates 0.42/0.29/0.26/0.32 across the four classes; no k≈1 vs k≈0 split. A global theme structure would demand differential keep-rates by class; the uniform k-term contradicts that mechanism.
3. **Reservation is per-run write-side.** It is applied independently inside each run's `_build_anchor_index`; nothing links runs. Code facts (from `NEGENTROPY-ARM`): C1 `:1045` `_build_anchor_index` (harvests all roles, per-pattern counts/last_seen, `ranked = sorted(counts, key=lambda v: (-counts[v], -last_seen[v]))[:cap]`, stops at 7_000); C2 `:1031-1039` `_ANCHOR_PATTERNS` has no timestamp/session-id/model-name/null-literal pattern; C5 `:3669-3680` `_augment_summary_lean` appends the anchor block. The pattern-blindness (C2) is the write-side gap the RippleMem seam names.
4. **The cross-run facts the probes demand are absent.** From `LAQ-FIDELITY-PROBE`: rung 2 decision-core-claim-validity 0.83, continuation-next-action 0.00, continuation-implementation-scope 0.00; rung 3 continuation-next-step 2.17; rung 4 decision-model-pin 1.17, continuation-close-intent 0.00; rung 5 decision-truncation 0.00.
5. **The three-block composition clears local probes.** Derivations (~120 tokens) + time-anchors (~60) + forward-intents (~60) = ~240 tokens (~2.4% of 10K) clears all 5 probes (0/5 below 3.0, median 3.33 reproduced). This is the *per-run* ceiling; it does not touch cross-run coherence.
6. **Archive class is refuted under tested construction.** Competing-admission fix (admit demanded literal OR rival by query-time score) does not clear the gate (worst-case min stays sub-zero at 4x/8x across budgets 0/1/5% and rival_rate 0/0.3). So query-side recall is not the lever.
7. **Pin class works.** Recurrence-aware pinning drops deep-minima prevalence 1.00 → 0.15 at the confirmed aliasing×proximity pair. Exact-literal pinning is the gate's convergent answer on the demand-age arm.
8. **RippleMem borrow is PARTIAL.** Cue→completion fits the read side (session_search recovery footer); the write-side reservation is not supplied by it. Seam = cue key = reserved literal (C1 patterns lack timestamp/session/model/null literals).

### The CREATOR-GAP named
The negentropy arm's design (`NEGENTROPY-ARM`) is a *write-side reservation* mechanism. It was designed to reserve literals per-run. Its success signal is per-run (debug fixture decision-core/next-action ≥ 3.0). It never had a cross-run success signal because the mechanism has no cross-run component. The CREATOR-GAP is: **the arm invented a per-run reservation tier but never invented the cross-run relation that the global structure requires.** Filling the gap means inventing a mechanism whose *output* is a cross-run relation, not a per-run survival.

## [The candidate-planes — method-card form]

Each card: **Trigger** (when it fires), **Essence** (what it does), **Failure-risk** (how it could fail / what would refute it), **Success-signal** (the measurable bar it must clear).

---

### Plane 1 — Cross-run theme-index (read-time build)

**Trigger:** at read time, when a continuation/decision probe is issued against a run whose compressed state is available; the index is built jointly over the *set* of runs in the ladder (or session-group), not per-run.

**Essence:** instead of each run building its own `_build_anchor_index` over its own messages (C1, per-run), build a single index over the *union* of runs' retained anchors, keyed by theme (the four classes: decision-core, continuation, exact anchors, scope boundaries). The index records, for each theme-class literal, which runs contain it and at what position. The compressed state presented to a probe is then augmented not with "this run's reserved literals" but with "the theme's cross-run membership" — i.e., the set of runs that share this literal, which is exactly the coherence the LAQ probe measures.

**Failure-risk:**
- Could collapse into a per-run index with extra bookkeeping if the join key is not theme but literal-string; then it reproduces the flat k-term and adds nothing.
- Could be confounded by run-identity instability (different sessions, different fixtures) — the index must key on theme-class, not on raw literal equality across incompatible fixtures.
- Could be judge-gated / empty-answer-confounded (Wall W2) if the probe reads `summary_text` and the answer is empty; the index must be readable as a structured block, not prose.
- Could be expensive: union over 16 runs × (anchor budget) may exceed the 7,000-char budget if not capped; needs its own budget (suggest: a fraction of the per-run budget, e.g., 20% reserved for cross-run index).

**Success-signal:** cross-run theme-membership coherence > 0 across the 16 runs (currently 0 on every rung); k-term differential by class (kept-rates no longer flat 0.42/0.29/0.26/0.32 — at least one class must separate); and the LAQ probe's below-3.0 count must drop below the base on at least one rung. Falsifier: if coherence stays 0 after the index is built and readable, the plane is refuted (the structure is not in the anchors).

**VOI: HIGHEST.** It is the only candidate that is cross-run by construction and directly targets the measured failure (theme-membership = 0). It is cheap to falsify (offline, over existing 16 JSONs) and does not require a live provider.

---

### Plane 2 — Inter-run anchor-sharing (run-linked literals)

**Trigger:** when a run's `_build_anchor_index` produces a reserved literal that matches a literal already reserved in a prior run (same theme-class), the new run's reserved set is *augmented* with the prior run's linked anchors (not re-promoted from scratch).

**Essence:** add a run-linking layer to the per-run reservation tier: a shared pool of reserved literals keyed by theme-class, so that a literal reserved in run N becomes available to run N+1's compressed state. This is the write-side analogue of Plane 1 — it keeps the per-run machinery (C1/C5) but makes the reserved set *cumulative across runs* rather than independent. The link key is the theme-class + the literal (or a normalized form), and the pool is persisted (analogous to the anchor-chain's INDEX → segments, `NETWORK-LINE-ANCHORCHAIN`).

**Failure-risk:**
- Run-identity must be stable and known at write time; if runs are anonymous/unlinked (as in the ladder's 3-runs-per-fixture), the link fails silently and the pool never accumulates.
- Could amplify errors: a wrong literal reserved in one run propagates to all linked runs.
- Could still be local in disguise: if the pool is queried per-run but never read jointly, the cross-run coherence is never actually measured by the probe (the probe reads one run at a time).
- Budget: each run's reserved set grows with the pool; the 7,000-char cap becomes a binding constraint sooner.

**Success-signal:** the reserved set's *intersection* across runs (shared literals) grows monotonically with run index within a fixture-group; cross-run theme-membership coherence > 0; and the k-term shows differential keep-rates. Falsifier: if the intersection stays empty (no shared literals across runs), the plane is refuted — the runs do not share literals and linking cannot help.

**VOI: HIGH.** It directly extends the existing (working) reservation tier into cross-run space, reusing C1/C5. But it is write-side and depends on run-identity stability, which the ladder does not guarantee.

---

### Plane 3 — Global-summary build (across runs)

**Trigger:** when a session-group (or the whole ladder) has completed its runs, build a single summary over the *union* of runs' messages, using the same `_augment_summary_lean` path but fed the cross-run union rather than a single run.

**Essence:** the probes read `summary_text` (per-run). If the summary is built per-run, the probe can only see per-run facts. Building the summary over the union of runs' messages makes cross-run facts visible in the summary_text of every run (or of a designated "global" run). This is the summary-side analogue: instead of reserving literals, change *what the summary is built from*.

**Failure-risk:**
- Judge-gated and empty-answer-confounded (Wall W2): if the answer is `""`, the summary's content does not matter; the probe fails regardless.
- Could dilute per-run signal: a global summary is less relevant to any single run's probe, lowering per-run survival even as it raises cross-run coherence.
- Could exceed budget: union of 16 runs' messages is large; compaction is what produces the summary, so the input to the global build must itself be compacted first (circular).
- Could be gamed: the probe's expected-facts are per-run; a global summary may contain the fact but in a context the probe's judge does not credit.

**Success-signal:** cross-run theme-membership coherence > 0 AND per-run below-3.0 count does not regress (currently 0/5 on the three-block composition; must stay ≤ 1/5). Falsifier: if per-run survival regresses below the three-block baseline (3.33 median), the plane trades local for global and is refuted as a net gain.

**VOI: MEDIUM-HIGH.** It targets the summary_text the probes actually read, but carries Wall W2 and a per-run-regression risk that must be measured, not assumed.

---

### Plane 4 — Run-linking / run-graph (explicit links between runs)

**Trigger:** at run creation time (or at ladder-battery assembly time), record a link edge between runs that share a fixture, a theme, or a session-group.

**Essence:** a meta-layer that records which runs are related (same fixture, same theme-class, same session-group). It does not itself lift structure; it *enables* Planes 1–3 by providing the join key. Without it, Plane 2's shared pool has no accumulation and Plane 1's index has no grouping.

**Failure-risk:**
- Infrastructure without a lift mechanism: if built alone, it produces no measurable change in theme-membership (success-signal would be trivially "links exist").
- Could impose a false taxonomy: linking by fixture may not correspond to thematic relation (the ladder's fixtures are different domains).
- Could be premature: the join key (theme-class) is not yet validated as stable across runs.

**Success-signal:** not measured by theme-membership directly; measured by whether Planes 1–3 can be built on top of it. Standalone success = the link graph's edges correlate with shared reserved-literals (intersection > 0 on linked pairs, ≈ 0 on unlinked pairs). Falsifier: if linked pairs show no more shared literals than unlinked pairs, the linking key is wrong.

**VOI: MEDIUM.** It is an enabler, not a lift. Build it only if Plane 1 or 2 needs it; do not build it speculatively.

---

### Plane 5 — Cross-run cue-conditioned completion (RippleMem-class, read-side)

**Trigger:** at read time, when a probe (or session_search) issues a cue, the read path completes the cue against the *joint* set of runs' anchors, not against one run's anchor index.

**Essence:** the RippleMem borrow (from `NETWORK-LINE-ANCHORCHAIN`) is cue → completion, read-side. Today it fits the session_search recovery footer (one run at a time). Extend it to a cross-run cue: the cue is matched against all runs' reserved literals, and the completion returns the theme-class members across runs. This is the read-side analogue of Plane 1 without building a persistent index — it computes the cross-run relation on demand.

**Failure-risk:**
- Could be slow: on-demand matching over 16 runs per cue; needs caching or pre-computation (which collapses into Plane 1).
- Could over-return: a cue may match many runs' literals, flooding the context; needs a cap (the 7,000-char budget analogue).
- Does not create global structure; it *exposes* it. If the structure is not in the anchors (Plane 1's falsifier), this plane returns nothing useful.
- Pattern-blindness (C2): cues for timestamp/session/model/null literals never match because no pattern captures them.

**Success-signal:** same as Plane 1 (coherence > 0, k-term differential) but measured per-cue rather than per-index. Falsifier: if on-demand matching returns the same per-run result as the single-run anchor index (no cross-run gain), the plane adds nothing over Plane 1 and should be dropped in favor of the index.

**VOI: MEDIUM.** It is a cheaper-to-prototype variant of Plane 1 (no persistent index), but likely collapses into Plane 1 once caching is needed. Prototype it only if Plane 1's index-build proves too expensive.

---

### Plane 6 — Provenance-origin / archive (query-time recall)

**Trigger:** at query time, recall the demanded literal from an archive by its ID.

**Essence:** archive all literals at write time; at query time, recall by ID. The optimistic bound (archive every literal) is already tested.

**Failure-risk:** refuted under tested construction (competing-admission fix does not clear the gate: worst-case min stays sub-zero at 4x/8x across budgets 0/1/5% and rival_rate 0/0.3). The admission is query-blind (field AUC 0.63–0.66); the budget knob is toothless (admits only the demanded literal's ID, never a competing one). The archive class is closed.

**Success-signal:** none available under current construction; would require a construction change (e.g., query-aware admission) that is not in scope.

**VOI: LOW.** Do not pursue unless a new admission mechanism is invented. Carried here for completeness and to close the class.

---

## [The VOI ordering — the full rationale]

The VOI is computed on three axes: (a) does the candidate target the measured failure (theme-membership = 0)? (b) is it falsifiable offline against the existing 16-run ladder? (c) does it reuse working machinery (C1/C5, the three-block composition, the anchor-chain)?

| rank | plane | targets failure? | offline-falsifiable? | reuses machinery? | VOI |
|---|---|---|---|---|---|
| 1 | Cross-run theme-index | yes (directly) | yes (16 JSONs) | yes (anchor index + augment) | HIGHEST |
| 2 | Inter-run anchor-sharing | yes (via shared pool) | partially (needs run-ids) | yes (reservation tier) | HIGH |
| 3 | Global-summary build | yes (via summary_text) | partially (judge-gated) | yes (augment path) | MEDIUM-HIGH |
| 4 | Run-linking / run-graph | no (enabler) | yes (link correlation) | no (new layer) | MEDIUM |
| 5 | Cross-run cue-conditioned completion | yes (on-demand) | yes (per-cue) | yes (RippleMem) | MEDIUM |
| 6 | Provenance / archive | no (query-side) | no (refuted) | no | LOW |

**The ordering's justification (one paragraph):** Plane 1 is first because it is the only candidate that is (a) cross-run by construction, (b) falsifiable offline against the exact artifact that named the failure (the 16-run ladder), and (c) a direct reuse of the working per-run machinery (C1's anchor index + C5's `_augment_summary_lean`), just fed the union instead of one run. Plane 2 is second because it extends the working reservation tier into cross-run space but is write-side and depends on run-identity stability that the ladder does not guarantee. Plane 3 is third because it targets the summary_text the probes read but carries Wall W2 (empty-answer confound) and a per-run-regression risk. Plane 4 is fourth because it is an enabler with no standalone lift. Plane 5 is fifth because it is a cheaper prototype of Plane 1 that likely collapses into it. Plane 6 is last because the class is closed.

## [The path (the next moves, in order)]

1. **Build Plane 1 (cross-run theme-index) as an offline probe over the 16 ladder JSONs** — no live provider, no code change to the compressor. Measure: coherence > 0 on at least one rung; k-term differential by class; below-3.0 count drop. This is the falsifier for the whole candidate set.
2. **If Plane 1 clears its success-signal**, promote it to a read-side augmentation in `_augment_summary_lean` (C5) — feed the cross-run index into the per-run summary as a structured block, below the 7,000-char budget (suggest 20% reserved for cross-run, 80% for per-run).
3. **If Plane 1 fails (coherence stays 0)**, the structure is not in the anchors; escalate to Plane 3 (global-summary build) and accept the Wall W2 / regression risks, measuring both.
4. **Build Plane 4 (run-linking) only if Plane 2 is attempted** — do not build it speculatively.
5. **Do not pursue Plane 6** unless a new admission mechanism is invented.

## [The honest walls (carried, not invented)]

- **W2 (empty-answer confound):** applies to Plane 3 (global-summary) and to any probe that reads `summary_text` with an empty answer. Plane 1 avoids it by reading the index as a structured block.
- **W5 (k-term flat):** the baseline k-term (0.42/0.29/0.26/0.32) is the failure signature; any candidate that does not move it has not lifted global structure.
- **W6 (full-budget scalar judge-gated):** Plane 1's success-signal uses coherence (a structural measure), not the judge-gated scalar, so it avoids W6.
- **Pattern-blindness (C2):** `_ANCHOR_PATTERNS` has no timestamp/session/model/null pattern. Planes 1 and 2 inherit this; if the cross-run structure lives in those literals, the index must add patterns (or the literals must be extracted by a different mechanism). This is a known sub-gap inside Plane 1's success.

## [Recommendation/Action Plan]

- **The one next mechanism (leg A's CREATOR-GAP filled):** the cross-run theme-index, built at read time over the union of runs' retained anchors, keyed by theme-class. It is the only candidate that is cross-run by construction, falsifiable offline, and a direct reuse of the working machinery.
- **The falsifier (the failable check):** build the index over the 16 ladder JSONs; if cross-run theme-membership coherence stays 0, the plane is refuted and the structure is not in the anchors — escalate to Plane 3.
- **The path:** Plane 1 probe (offline) → if clears, read-side augmentation in C5 → if fails, Plane 3 with Wall W2 accepted.

## [Artifact]

- Path: `studies/rfc-143379-rig/SWAP-A-ADVANCE-A-20261106.md`
- Branch: `study/rfc-143379-rig-20261105`
- Ground: `NEGENTROPY-SWEEP-A-RESERVED-LAQ-20261106.md` + `LAQ-FIDELITY-PROBE-20261106.md`
- Seat: copycat lane (beam-1.0-501b-a23b:free), SWAP-1 rotation swap-leg.
- Hand-separation: [1st] = re-read by this lane this pass; [2nd] = carried from study docs and not re-derived.
- Register: receipts, never claims.
