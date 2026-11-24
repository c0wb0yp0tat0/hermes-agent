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

## HEAD-SIDE FIRE COMPLETION (2026-11-24, after the lane's BLOCKED)

**The wall closed head-side:** sha256 verified — `sha256sum probes/battery_luna.py` = `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd`, byte-matching the ACT4/B1 pin. The operator's word authorized the fire (twice-repeated: "Think tank skill Luna on its substrate harness").

**The fire ran:** `python probes/battery_luna.py --n 5 --arms A/B0/B1/C --bias-log` → exit 0, 308-line raw receipt (`rw-luna-substrate-fire-out.log`). Per the harness's own rule (`dry_run = n <= 5`), this is an **auto dry-run machinery receipt** — the harness's note says so verbatim: *"dry-run machinery receipt, NOT the leg's verdict."* It is a TRUE receipt of the machinery (the harness executed, the reader called 5× per arm, costs registered), not a certifying run.

**The dry-run's measured numbers (the machinery's own):**
- ARM A: correct 0/5, accuracy 0.0, tokens 30, cache 0.0, E:5
- ARM B0: correct 1/5, accuracy 0.2, tokens 35, cache 1.0
- ARM B1: correct 2/5, accuracy 0.4, tokens 35, cache 1.0
- ARM C: correct 4/5, accuracy 0.8, tokens 5, cache 1.0
- Decision rule computed: B_minus_A = 0.2 · B_over_0.85C = **False** (0.4 < 0.68) · C_minus_A = 0.6
- cost_total = 7.005

**Verdict (honest, per the harness's own pre-committed rule): INCONCLUSIVE as a certifying fire — the dry-run is the machinery receipt, not the leg's verdict.** The measured direction is real (B > A on B0/B1, C the strongest), and the one computed gate that matters — B ≥ 0.85×C — reads False on this window; nothing is certified or falsified from a dry-run receipt. What would settle the rung: a **full run with `--n 6` (n > 5 kills the auto dry-run)** on the Luna seat, raw receipt preserved. That run spends real paid-token budget — a money-gate item that waits the operator's explicit word (the pair's standing list: the operator's word gates money).

**Translation (the operator's question):** the months-old harness executes faithfully on the same route today — machinery receipted, decision rule computed, no harness edit, sha intact. Whether the seat certifies the rung stays OPEN until the full-run spend is authorized.

## THE FULL-RUN FIRE (n=6, the leg's verdict; operator's no-gate word, 2026-11-24)

`python probes/battery_luna.py --n 6 --arms A/B0/B1/C --bias-log` → exit 0, raw receipt `rw-luna-substrate-n6-out.log`. The harness's own note: **"the leg's full-run verdict."**

- ARM A: 0.0 (6/6 abstain, 6/6 C5a)
- ARM B0: 0.5 (5 answered, 1 abstain; sensitivity_abstention 0.167)
- ARM B1: 0.333 (2 answered, 4 abstain; sensitivity_abstention 0.667 — the bias pushed to abstention, not the target)
- ARM C: 0.5 (3/3 answered/abstain)
- Decision rule: B_over_0.85C = **False** (0.333 < 0.425) · B_minus_A = -0.167 · C_minus_A = 0.0 → **INCONCLUSIVE** (CERTIFY's B-A≥0.2 unmet; FALSIFY's B<0.85C holds but B>A — the stranded middle, verdict INCONCLUSIVE as written)
- cost_total 8.406

**The translation answer, receipted:** the months-old harness executes faithfully on the same route today — machinery held, sha intact, the decision rule computed on real episodes. What it measured on this channel: Luna on its own instrument lands at chance-or-worse with heavy abstention — the reasoning-exhaustion and abstention profile the PSA named, now at the source. The channel's rate is the channel's: 24-token one-shot probes at temperature 0 with a down-bias that converts to abstention — exactly the "thinks more, tries more, fails more, costs as much" shape, measured before the cost line.
