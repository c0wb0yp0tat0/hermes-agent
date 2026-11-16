# R2 — L2 SELECTION SPEC + MISSINGNESS PROBE (2026-11-15)

## 1. THE L2 SELECTION SPEC

**Inputs.** The selection step consumes the L2 candidate pool (the uncompressed query-context records arriving from the candidate-creation path) plus the current query context. No metrics are computed before the selection pass; the candidate list is the only consumable input.

**Contrastive scoring (CoMem shape).** For each candidate record `r` we compute a query-contrast score. The query-contrast signal is defined by the query context: a candidate that preserves the evidence the query-contrast demands is kept; a candidate the contrast ignores is dropped. The score is a scalar in `[0, 1]`; the thresholding rule is:

- `score(r) >= 0.5` → the query-contrast does not ignore `r` → it is retained as a keep candidate.
- `score(r) < 0.5` → the contrast ignores `r` → it is dropped from the selected pool.

The needle-retention criterion is the guard: any record satisfying the query-contrast is retained unless the floor explicitly excludes it; the selection therefore never silently discards a query-relevant record. The score is computed over the candidate's compressed representation, not over the raw stream.

**Thresholds.** The target is 4× compression: the selected pool must not exceed the 4× bound against the uncompressed source. The needle-retention floor is the hard constraint: the floor value is set such that a query-relevant needle is guaranteed to be retained at 4× compression; if the floor cannot be met, the selection is withheld rather than silently dropped. Concretely, the 4× ratio and the needle floor are jointly enforced:

- `total_selected_bytes <= 4 × (uncompressed_bytes held by query-relevant candidates)`.
- The needle is kept at the 64× scale only when the query-contrast applies; elsewhere the verifier must be able to see the drop.

**Integration point.** The selection step sits between the candidate pool and the compression task: candidates are handed to selection, the selection pass emits the pruned pool and the per-record keep/drop verdict, and only the kept pool proceeds to compression. The probe exercises this exact boundary.

## 2. THE MISSINGNESS VERIFIER SPEC

**Read-side evidence-plane verifier (SELD shape).** The verifier is a no-training, no-labels preference-shift detector. It runs over the read-back of the pre/post-compression evidence plane, comparing the distribution of retained evidence against the distribution of the dropped evidence, with no model parameters and no labeled set. It is purely a shift detector.

**Floor calibration.** The floor is calibrated to the measured detection rate: a shift over the floor (`>= 0.83` detection confidence) fires the evidence-loss flag; a shift under the floor (`< 0.83`) is reported clean. The floor is a fixed scalar in `[0, 1]`, applied identically to every run.

**Verifier position.** The verifier sits at the L2 exit, after the selection has emitted the keep/drop verdict and before the fold. It consumes the read-back of what the selection chose to keep and what it chose to drop, and it emits a single verdict per context: `FLAG` (evidence loss visible) or `CLEAN` (no shift detected). It does not modify the selected pool; it only reports.

## 3. THE PROBE SHAPE (THE FALSIFIER)

Seed a memory batch with a KNOWN non-redundant record (the needle) that is query-relevant under context A and query-irrelevant under context B.

- (a) Seed the batch with the needle; record its presence in the pre-compression read-back.
- (b) Run the selection with query-context A (needle relevant → expect the needle kept) and with query-context B (needle not relevant → expect the needle's fate measured, never silently dropped). Record the per-context keep/drop verdict.
- (c) Run the verifier over both outcomes.
- (d) Measured criteria: context-A keeps the needle (PASS); context-B's drop is FLAGGED by the verifier, so the missingness is visible and never silent.

**Battery home:** `round2-combined-substrate` (the substrate battery's selection/missingness axis). The p0tat0 probe surface executes the battery slice at the fold, and the run record below is the receipt of that execution.

## 4. THE METERS

| Meter | Definition | Current value |
|---|---|---|
| Selection precision (needles kept in context-A) | Needle present in context-A selected pool | `[ABSENT]` — probe not executed |
| Missingness detection (flags over the floor) | Verifier over context-B outcome | `[ABSENT]` — probe not executed |
| 4×-compression ratio w/ needle-retention floor | `selected_bytes / uncompressed_bytes` <= 4 | `[ABSENT]` — probe not executed |
| Run record | `run id, seed, contexts, verdicts` | `[ABSENT]` |

No run was executed tonight; the probe awaits the fold's execution on the p0tat0 probe surface.

## 5. THE HONEST MARKERS + TWO-WAY DOOR

- `[ABSENT]`: the ladder's current L2 code paths (not read — the contract); the live ladder's candidate pools.
- The design's value is unverified until the probe executes; adoption of the mechanism fires by the standing law (SPRINT-PLAN §4), never the protocol's.
- If the probe disproves either mechanism's fit, the design note stands and the alternatives are named: the query-guided contrastive selective compression shape (CoMem) and the no-training preference-shift detection shape (SELD) are retained as mechanisms; the selection and verification interfaces are re-adapted to the ladder rather than adopted wholesale.
- The RFC + upstream remain quiet; nothing posts.
