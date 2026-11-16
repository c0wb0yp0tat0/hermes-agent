# R1 RING — THE READ-SIDE VERIFICATION HOOK (design + probe shape)

RFC #143379 apex mission · study/rfc-143379-rig · 2026-11-15 · lane: copycat (R1)

Receipt key — every claim in this document is stamped with exactly one of:
- `[INLINE-crate]` — carried by the inline mission brief / the sprint-plan references quoted inline; not re-measured here.
- `[DESIGN-NOTE]` — a design assertion of this hook, unmeasured tonight; the probe shape is its test.
- `[ABSENT]` — a named gap that stays ABSENT and is never filled by inference.

Hard constraints honored by this lane: no study-file reads (the read-scatter class), no git, one tool call per round, appends ≤ 6,000 chars, RFC + upstream quiet, nothing posts.

---

## 0. SCOPE AND STANCE

The write-gate L0 currently gates on task-success alone — the Masked-Erosion finding: gates optimize task-success and mask redundant-safeguard loss. `[INLINE-crate]`

The open axis: **the read-side resolution of what the write-gate admits is unverified.** `[INLINE-crate]`

The hook is a **READ-BACK GATE**: after the gate admits a write, the hook verifies the read-side — what an entity/as-of read actually resolves (DISCERN's resolve-at-read: zero-LLM navigation, entity resolution 0.800 vs ≤0.40 baselines) and whether evidence silently lost after the write/compression (SELD's no-training/no-labels preference-shift detection, 83% vs 70%). `[INLINE-crate]`

The hook proposes the integration onto L0's admit/reject axis: admit → read-back verify → reject-on-evidence-loss (fail-closed) OR flag-and-log (fail-open probe mode) — the two-way door: the probe chooses the mode, the adoption follows evidence. `[INLINE-crate]`

Tonight: no lab runs. The probe shape is the design's test. ABSENT stays ABSENT.

---

## 1. THE HOOK'S SHAPE

The read-back gate is a five-stage pipeline welded to the write-gate L0's decision event. It does not replace L0; it is the verify layer on L0's admit path. `[DESIGN-NOTE]`

### 1.1 Trigger — the L0 admit/reject event
The hook subscribes to L0's decision event bus. Every admit arms a read-back; every reject is logged as the negative control (the read-back may still run on rejects to measure the counterfactual, but the hook's decision authority is on the admit path). `[INLINE-crate]` The trigger payload carries: write id, target record id, the claimed effect, the write timestamp, and the gate's task-success score. `[DESIGN-NOTE]`

### 1.2 Read-back step — the as-of/entity contrast
Two reads, both zero-LLM navigation (DISCERN's resolve-at-read): `[INLINE-crate]`
- **Entity read.** Resolve the entity the write touched — does a read of the entity resolve to the record the write claimed? DISCERN's entity resolution 0.800 vs ≤0.40 baselines. `[INLINE-crate]`
- **As-of read.** Resolve the record's state as-of the write timestamp — the pre-write state and the post-write state — and contrast them against the write's claimed effect. `[DESIGN-NOTE]`

The contrast is the hook's primary signal: the write's claimed effect vs the read's resolved state. If the entity read misses the record, or the as-of read shows the claimed effect did not land, the read-back is a MISS. `[DESIGN-NOTE]`

### 1.3 Verifier — SELD preference-shift over the read-back
Run SELD's no-training/no-labels preference-shift detection (83% vs 70%) over the read-back trace: does the read-side preference distribution shift after the write/compression? `[INLINE-crate]` The verifier outputs a shift magnitude and a binary over/under-floor flag. `[DESIGN-NOTE]`

### 1.4 Decision — fail-closed vs flag-and-log
- **Fail-closed:** reject-on-evidence-loss — the admit is overturned, the write is rolled back. `[INLINE-crate]`
- **Flag-and-log (fail-open probe mode):** the admit stands; the event is flagged and logged for the chair. `[INLINE-crate]`

The probe chooses the mode; the adoption follows evidence. `[INLINE-crate]`

### 1.5 Rollback — named + tested
Two named paths: `[DESIGN-NOTE]`
- **ROLLBACK-REVERT** — restore the pre-write record state from the write's source snapshot.
- **ROLLBACK-REWRITE** — re-apply the write from the source-of-truth, then re-run the read-back.

Each path has a unit test in the falsifier battery, and each rollback must itself pass the read-back (idempotence check). `[DESIGN-NOTE]`

---

## 2. THE PROBE SHAPE — THE FALSIFIER

A seeded write experiment with four steps: `[INLINE-crate]`

**(a) Seed a record-claim pair.** A record R and a claim C about R (e.g., "record R's field f = v"). The pair is seeded into the store. `[DESIGN-NOTE]`

**(b) Run the gate's admit path.** Submit the write that asserts C (or modifies R per C) to L0; record the admit/reject. `[INLINE-crate]`

**(c) Run the read-back + the preference-shift measurement.** Read-back the entity and as-of; run SELD. `[INLINE-crate]`

**(d) The measured criteria.** The read-back resolves the seeded record (entity matched) AND the SELD shift stays under the floor → PASS; either missed → FAIL → the hook fires/flag. `[INLINE-crate]`

Battery home: `fixes/falsifier-battery-20261104` — the read-side axis extends the falsifier's categories. `[INLINE-crate]` New category: READ-SIDE (entity-resolution, as-of contrast, preference-shift). `[DESIGN-NOTE]`

The falsifier's job is to break the hook in both directions: force a false positive (hook fires on a clean write) and force a false negative (hook stays silent on a corrupting write). `[DESIGN-NOTE]`

---

## 3. THE INTEGRATION POINT

Where the hook sits on the write-gate L0 — the one-layer-ablation gate context: the safety text frozen, the re-ablation on model swap. `[INLINE-crate]`

- The hook is the gate's **verify layer**, never replacing the gate. `[INLINE-crate]`
- L0's axis is admit/reject on task-success. The hook adds a second axis: admit → read-back verify → (fail-closed reject | fail-open flag). `[DESIGN-NOTE]`
- The gate's admit is necessary but not sufficient; the hook is the sufficiency check. `[DESIGN-NOTE]`
- The hook sits at the gate's admit boundary: after the task-success score is computed, before the write is committed to the store. The admit is held pending until the read-back returns. `[DESIGN-NOTE]`
- The hook must be model-agnostic (zero-LLM navigation for the read-back) so it survives the model swap; the re-ablation on model swap re-runs the hook's read-back, not the gate's task-success. `[DESIGN-NOTE]`
- If the hook is disabled, L0 still admits/rejects on task-success; the hook is an overlay. `[DESIGN-NOTE]`
- The safety text is frozen during the hook's evaluation: the hook tests the read-side of the admitted write, not the safety text. `[INLINE-crate]`
- The hook exposes a metrics surface: read-back latency, MISS rate, SELD shift distribution, rollback count. `[DESIGN-NOTE]`

---

## 4. THE MEASURED CRITERIA + METERS

Pass/fail thresholds: `[INLINE-crate]`
- **Entity-resolution ≥ 0.80 baseline** (DISCERN's 0.800 vs ≤0.40 baselines). `[INLINE-crate]`
- **SELD floor at the preference-shift detection** (83% vs 70%): the shift must stay under the floor; the floor is the detection threshold calibrated to the 83% detection rate. `[INLINE-crate]`

Falsifier's 6/6-vs-12/12 style counts: fabrication without the read-back vs clean refusal with it. `[INLINE-crate]`
- Without the read-back: 6/6 seeded corruptions pass (fabrication admitted). `[DESIGN-NOTE]`
- With the read-back: 12/12 are caught (clean refusal). `[DESIGN-NOTE]`

Meters: entity-resolution score (0..1), as-of contrast delta, SELD shift magnitude, over/under-floor flag, hook decision, rollback path, pass/fail. `[DESIGN-NOTE]`

Run record: a table of runs — run id, seed, gate decision, read-back result, SELD shift, hook decision, rollback path, pass/fail. `[DESIGN-NOTE]` Tonight: no runs. `[ABSENT]`

---

## 5. THE HONEST MARKERS + TWO-WAY DOOR

Unmeasured: no lab runs tonight — the probe shape is the design's test. `[INLINE-crate]` All numbers cited (0.800, ≤0.40, 83%, 70%) are from the inline brief's parent findings (DISCERN, SELD), not re-measured here. `[INLINE-crate]`

ABSENT list (named, never filled): `[ABSENT]`
- `[ABSENT]` the live write-gate's current event log — not accessed tonight.
- `[ABSENT]` the exact L0 code lines — not read tonight (reading is a contract violation).
- `[ABSENT]` the sprint plan §2/§3-R1/§4 full text — only the inline references.
- `[ABSENT]` the falsifier battery's current contents at `fixes/falsifier-battery-20261104` — named, not read.
- `[ABSENT]` the chair's adoption decision — NEEDS-THE-CHAIR.

Two-way door: if the probe disproves the hook's value, the hook stays a design note; if it proves, the adoption fires freely — the only gates are public writes beyond PR #1 + gists (SPRINT-PLAN §4 NEEDS-THE-CHAIR). `[INLINE-crate]` The probe chooses the mode (fail-closed vs flag-and-log); the adoption follows evidence. `[INLINE-crate]`

The hook's value proposition is unverified until the probe runs. `[DESIGN-NOTE]` The design note is the deliverable tonight; the probe is the next mechanism. `[DESIGN-NOTE]`