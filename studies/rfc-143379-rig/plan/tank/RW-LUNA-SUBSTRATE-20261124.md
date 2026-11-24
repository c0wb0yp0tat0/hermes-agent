# RW-LUNA-SUBSTRATE-20261124 — weights-rung substrate fire record

**Status: BLOCKED / no harness fire.** This is a receipt of the attempted record, not a simulated or inferred run. No arm outputs, measurements, or verdict from `run_luna` are available. The pre-registered bars remain unchanged and unevaluated.

## Ground read and integrity check

Read locally: `probes/battery_luna.py` (537 lines), `WEIGHTS-RUNG-PRE-REG-20261121.md` (including §4), `plan/tank/B1-A3-ARC-FIRE-20261123.md`, and `OPUS-A3-WEIGHTS-DRYRUN-20261120-brief.md`.

The harness describes a four-arm `A/B0/B1/C` battery, `LunaReader` with temperature 0 and `max_tokens = 24`, `BIAS_V3` on B1, F1/F2/F3b marks, and an `ExactMatchJudge`. Its own verdict is based on the run's B0/B1/C accuracy, judge control, and mean F3b; it is not interchangeable with the rung's outer bars.

The brief requires verifying the harness SHA-256 pin `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd` before firing. The available integrity command was `git hash-object studies/rfc-143379-rig/probes/battery_luna.py`, which returned `dd5a312f7556306898dd8e532bda3d79ffd97c4f` (Git object hash, not SHA-256). It does **not** establish whether the stated SHA-256 matches. A SHA-256 verification receipt was not obtained; therefore the required pre-fire verification is absent, not passed.

## Fire receipt

No `battery_luna.py` invocation was made. No requests were sent to the inference endpoint, and no raw harness JSON/stdout exists for this record. Consequently, there are no observed numbers to quote for any arm, no harness decision-rule result, and no observed F1/F2/F3b state or B1 applied-bias log. The prior B1 fire is precedent only and supplies no Luna arm measurements.

The minimal move required by the wall clause is to run the pinned, unmodified harness in an authorized environment after obtaining a matching SHA-256 verification receipt, with its required seat credentials and operator authorization. The intended pre-registered command shape is `python studies/rfc-143379-rig/probes/battery_luna.py --n 5 --arms A/B0/B1/C --bias-log`; preserve the harness's raw output and ledger, then report their actual per-arm values. This command is a proposed next step, **not** a run receipt.

## Pre-registered bars vs available evidence

The immutable §4 bars are: (1) B0 ≥ 20 percentage points; (2) B1 ≥ 20 percentage points; and (3) B1 ≥ 0.85 × C. None can be measured from this attempt: B0, B1, and C values are absent. Each bar is **NOT EVALUABLE**; no bar is counted as passed or failed. No smoothing or borrowed precedent values are used.

## Seam notes

- **24-token budget:** no call occurred; reasoning exhaustion behavior is **unobserved**.
- **Governance:** F1, F2, and F3b are **unobserved** for this fire; no compliance rate can be reported.
- **Bias log:** B1 did not run; there are no applied-delta readings.
- **Harness decision rule:** no verdict receipt exists. This record does not invent one.

## Verdict and translation

**Verdict: UNKNOWN / BLOCKED — the weights-rung fire is not evaluable on this record; no COVERED, PARTIALLY-COVERED, or GAP measurement is claimed.**

**Translation:** this attempt establishes no evidence about the months-old harness carrying the Luna seat on the same route today; that question remains open until a SHA-256-verified, authorized harness run produces its raw receipts.

**Gate:** PREVIEW ONLY; nothing posted; RFC surface remains quiet.
