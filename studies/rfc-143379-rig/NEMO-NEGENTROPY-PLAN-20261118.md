# NEMO-NEGENTROPY-PLAN-20261118

## THE PLAN VERDICT LINE
`NEGENTROPY-PLAN-20261118 - STANDARDIZE the runtime credential check gate, PARK the launch-stub scribe marker, and CLEANSE the empty scribe cell and disk headroom; successor implements the runtime credential verification and W2-isolation re-run.`

---

## The Class, Named
The night's instances map onto the following entropy classes:
- **Dead Surface:** The empty scribe cell `rig-the-night-assessed` (81 chars) from a killed run.
- **Loose Threads:** The seventeen untracked inputs committed in `f098cce8fc` and the disk at 91% with the 92% runner-workspace guard next.
- **Friction Points:** The unmeasured runtime credential values (`api_key`/`base_url`) required to pass the gate in `run_eval.py` (line 81).
- **Unspoken Opportunities:** The need to standardize the runtime credential check gate and the launch-stub scribe marker to prevent future ambiguity.

---

## The Rules to Standardize
1. **Fire-Time Input Commit:**
   - **Rule:** Commit all inputs at the time of fire to avoid loose threads.
   - **Evaluation:** This rule already exists in the sweep's practice (e.g., `f098cce8fc`).
   - **Verdict:** **STANDARDIZE** (already in practice).
   - **Testable Check:** Verify that all inputs are committed before the next sweep.

2. **Launch-Stub Scribe Marker:**
   - **Rule:** Add a visible stub marker for never-folded runs to ensure traceability.
   - **Evaluation:** This rule does not yet exist in the sweep's practice.
   - **Verdict:** **PARK** (not critical but useful for traceability).
   - **Testable Check:** Implement a marker (e.g., a timestamped stub file) for runs that are not folded.

3. **Sweep on Standing Cadence:**
   - **Rule:** Conduct sweeps on the standing cadence (e.g., 2-hour intervals) rather than on request.
   - **Evaluation:** This rule already exists in the sweep's practice (e.g., `NEGENTROPY-SWEEP-20261116-1937`).
   - **Verdict:** **STANDARDIZE** (already in practice).
   - **Testable Check:** Confirm that sweeps continue on the standing cadence.

---

## The Cleanse List
1. **Empty Scribe Cell:**
   - **Action:** Replace the empty scribe cell `rig-the-night-assessed` with a timestamped stub or placeholder.
2. **Disk Headroom:**
   - **Action:** Monitor disk usage and ensure it does not exceed the 92% runner-workspace guard.

---

## The Successor Brief
The successor will:
1. Implement the runtime credential verification to measure the values of `api_key`/`base_url`.
2. Re-run the W2-isolation settle-condition per the on-branch spec.
3. Artifact name: `NEGENTROPY-RUNTIME-VERIFY-202611XX.md`.
4. Gate: The successor fires only after the runtime credential verification passes and the W2-isolation re-run completes.

---

## THE LOOP-STATE LINE
`NEGENTROPY-LOOP-20261118 - STANDARDIZE runtime credential check gate, PARK launch-stub scribe marker, CLEANSE empty scribe cell and disk headroom; successor verifies runtime credentials and re-runs W2-isolation.`