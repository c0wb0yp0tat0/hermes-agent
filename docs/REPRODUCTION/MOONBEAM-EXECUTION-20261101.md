# MOONBEAM-EXECUTION-20261101 — the round's executed legs

*Moonbeam's execution loop, on the improver's plan (PLANNING-LOOP-ROUND-20261101.md). In-scratch only: no pushes, nothing public, the landings are the user's word. Disk at the end.*

## MISSION

Execute the plan's five legs — implement, test at the published head, assemble the round, hold the integrity. The plan's contract: adopt both humble-pass candidates (JUnit-node receipt parsing + no-clobber injection guard) as the staging-side and grading-side of the certification discipline; close the four humility gaps (source-dirtiness record, lock-refresh retention, held-out identifier set, self-test suite + receipt JSON); land the certification-window readiness. Everything in-scratch. Nothing public. Nothing pushed.

## RUN'S HOME

`/root/.hermes/cache/scratch/pilot-kit-20261029/night1030/followup/moonbeam-exec/` (writable, idempotent, two-way). Deliverable: `/root/workspace/drop/deepdive-mission-flow/MOONBEAM-EXECUTION-20261101.md`.

## LEG 1 — LEG-DISCIPLINE: JUnit-node receipt parser

**File:** `moonbeam-exec/junit_receipt_parser.py`

**What it does:** parses actual `<testcase>` nodes, not summary counters; quotes skip reasons verbatim; never over-generalizes a skip into a capability-absence claim. Per-case receipt shape (`CaseReceipt`: classname, name, status, skip_reason, failure_text, error_text). Receipt-level counts (passed/failed/errors/skipped/total) derived from nodes. 1:1 reconciliation against an independent regex re-parse. Contract rejects forged counters (summary vs nodes mismatch), duplicate IDs, stale XML (ET vs independent count mismatch).

**Test command:**
```
cd moonbeam-exec && python3 -m pytest test_no_clobber_guard.py test_gaps.py test_gates.py -q
# parser exercised via fixture run:
python3 junit_receipt_parser.py fixture-junit.xml
```

**Fixture:** `fixture-junit.xml` — Kevin's table shape (5 pass / 0 fail / 0 err / 1 skip), skip reason verbatim: "No chain-document support in this exact head: specifically the expected orphan_doc_names/read API capability check. This does not establish that every chain capability is absent, nor that the recovery invariant passed."

**Receipt (output excerpt):**
```
passed=5 failed=0 errors=0 skipped=1 total=6
RECONCILE: True counts reconcile 1:1
INDEPENDENT_REPARSE: {'passed': 5, 'failed': 0, 'errors': 0, 'skipped': 1, 'total': 6}
SECOND-BASE-REPARSE: AGREE
```

**Contract checks (verified):**
- forged counter (skip hidden, summary skipped=0 vs node skipped=1): rejected — "forged/summary counter mismatch".
- duplicate identity `a::b` twice: rejected — "duplicate test case identity".
- skip reason appears verbatim in `skip_reasons_verbatim` with no generalization beyond it.

**Status:** FIRED (measured). Success signal met: 1:1 reconciliation + verbatim skip + second-base re-parse agreement + forged/duplicate rejection.

## LEG 2 — LEG-GUARD: no-clobber staging guard + self-test suite + receipt JSON

**Files:** `moonbeam-exec/no_clobber_guard.py`, `moonbeam-exec/test_no_clobber_guard.py`

**What it does:** pre-flight guard. Absent path → inject only into a fresh output dir (refuse if output dir exists). Existing path without pinned mode → refuse with named reason, exit 1, no receipt, worktree clean. Already-pinned mode → byte-identity check on consent fixture (refuse on drift), probe-superset check (four encoding-freshness defs + five base defs + consent parametrization), skip injection and run candidate's own copy (`probe_source: candidate-in-tree`, `injection: skipped`).

**Test command:**
```
cd moonbeam-exec && python3 -m pytest test_no_clobber_guard.py -q
```
**Result:** `7 passed in 0.03s` — measured RED/GREEN on synthetic fixtures:
- refuse on existing path without pinned (named reason, exit 1, no receipt)
- pinned skip on byte-identical (skip injection, receipt written)
- refuse on drifted fixture sha
- refuse on missing encoding defs
- inject on absent + fresh dir
- refuse on existing output dir
- worktree clean on refusal (bytes unchanged)

**Receipt JSON** (`guard-receipt.json`): mode=pinned, probe_source=candidate-in-tree, injection=skipped, receipt_written=true, worktree_clean=true, exit_code=0; source hashes runner_probe `773f309e…`, runner_scenarios `b9aeac99…`; runner_selftest reference `RUNNER-SELFTEST-20261026.json`.

**Status:** FIRED (measured). Success signal met: refuse-on-mismatch and skip-on-match both measured; zero fabricated/empty landing files across the suite; every refusal produces a named reason and no receipt.

## LEG 3 — LEG-GAPS: source-dirtiness record, lock-refresh retention, held-out identifier set

**File:** `moonbeam-exec/gaps.py`, `moonbeam-exec/test_gaps.py`

**What it does:**
- `EnvQualification` record: env_identity, tracked_source_dirty, lock_state, lock_check_exit, canonical_lock_rejected. `record_source_dirty` writes the receipt (separately provisioned env, source untouched, dirty=false).
- `retain_lock_refresh`: retains the lock refresh as a non-pushed artifact (`pushed=False` always), records path + diff_lines + sha256 + receipt json. Non-pushed discipline held.
- Held-out identifier set: `HELD_OUT_IDENTIFIERS` (3 pairs, extended from S1's single rename); `run_held_out_probe` applies each rename and records whether the replacement persisted with `staged=False`.

**Test command:**
```
cd moonbeam-exec && python3 -m pytest test_gaps.py -q
```
**Result:** `4 passed, 1 warning in 0.02s`.

**Receipts:**
- `env-qualification-receipt.json`: env_identity="separately-provisioned-compatible-pm", tracked_source_dirty=false, lock_state="checked", lock_check_exit=0, canonical_lock_rejected=true.
- `rfc-out/lock-refresh.patch`: 7718 diff lines (synthetic 7,716-line refresh), `pushed=False`, sha256 recorded, receipt json written beside it.

**Status:** FIRED (measured). Success signal met: tracked_source_dirty recorded; lock refresh retained as non-pushed artifact with path recorded; held-out identifier set used (3, not single rename).

## LEG 4 — LEG-GATES: storm's READY shapes wired in

**File:** `moonbeam-exec/gates.py`, `moonbeam-exec/test_gates.py`

**What it does:** `RetryBudget` (max_attempts=2, delay_s=15.0 — the retry budget 2/15s), `CircuitBreaker` (failure threshold, reset timeout, open/half-open/closed), `StageGate` (VERIFY-before-ADVANCE: advances only after verify() returns True), `health_aware_assign` (healthy candidates only), `run_with_retry` (retries across the budget).

**Test command:**
```
cd moonbeam-exec && python3 -m pytest test_gates.py -q
```
**Result:** `6 passed in 0.02s`.

**Receipts (measured):** retry budget 2/15s (can_retry False after 2 consumes); breaker opens at 3 failures and blocks; breaker resets on success; stage-gate refuses advance on False verify; health-aware assignment filters unhealthy; retry succeeds after one failure.

**Status:** FIRED (measured).

## LEG 5 — LEG-CERT: certification-window readiness

**File:** `moonbeam-exec/cert.py`

**What it does:** builds the certification receipt from the (b)-extended probe's JUnit XML at node level; derives `required_green` from parsed nodes (encoding_freshness 7/7); records independent re-parse agreement; carries tracked_source_dirty and lock_refresh_path; verdict CANDIDATE-READY (NOT CERTIFIED until guard passes + nodes parse — the default holds).

**Test command:**
```
cd moonbeam-exec && python3 cert.py fixture-cert.xml b84150e9be 4e5bfc5d
```
**Fixture:** `fixture-cert.xml` — Kevin's green JUnit shape: 7 cases (3 defs × 2 targets + 1 standalone), 0 failures, 0 errors, 0 skipped.

**Receipt (`cert-receipt.json`):**
```
encoding_freshness_passed=7 encoding_freshness_total=7
required_green=True
verdict=CANDIDATE-READY
independent_reparse_agrees=True
node_counts={passed:7, failed:0, errors:0, skipped:0, total:7}
tracked_source_dirty=False
lock_refresh_path=rfc-out/lock-refresh.patch
```

**Status:** CANDIDATE-READY (not certified — the guard passes on synthetic fixtures; the published-head run and improver pass remain, per LOOP5's verdict). Success signal for the leg met on the fixture: encoding_freshness 7/7 + required_green: true + independent re-parse agreement.

## FULL SWEEP RECEIPT

```
cd moonbeam-exec && python3 -m pytest -q
# 17 passed, 1 warning in 0.03s
```
Files: `junit_receipt_parser.py`, `no_clobber_guard.py`, `gaps.py`, `gates.py`, `cert.py` + fixtures + tests. All syntax-clean (lint ok). No public writes. No pushes. No source changes to any shared repo.

## ASSEMBLED ROUND (listener's register)

- the round's plan executed leg by leg — discipline, guard, gaps, gates, cert — each with its own receipt, each measured, each on disk.
- the humility became the harness: node-level receipts instead of summary counters, byte-identity guard instead of silent overwrite, source-dirty recorded instead of skipped, held-out set instead of single rename, self-tests with measured RED/GREEN instead of prose verdicts.
- the certification window opens on evidence both labs can count identically: 7/7 encoding freshness, required_green true, independent re-parse agreeing, tracked_source_dirty false, lock refresh retained not pushed.
- the verdict stays honest: CANDIDATE-READY, not certified. The published-head run and the improver's formal pass (channel was dark; landed from the verified record per stalled-lane doctrine) still stand between here and certified. NOT CERTIFIED remains the default until the guard passes and the nodes parse on the real head.
- nothing public. nothing pushed. the gist's edit, the morning comment, the ENTRY append — all still the user's word.

## PRESENTATION'S HARMONIZATION (the night's record, in its own voice)

What this execution changes in the night's record — new statuses, doors, lines:

- **New status — JUnit-node receipt discipline: FIRED (measured).** Was ADOPT (companion, not yet wired). Now wired in scratch with 1:1 reconciliation, verbatim skip, forged/duplicate/stale rejection. Seam: certification readiness check + improver pass.
- **New status — no-clobber guard: FIRED (measured).** Was ADOPT-CANDIDATE. Now self-tested (7/7 synthetic) with measured refuse-on-mismatch and skip-on-match, receipt JSON with source hashes mirroring RUNNER-SELFTEST-20261026.json. Seam: lane-runner probe-staging.
- **New status — humility gaps: FIRED (measured).** Source-dirtiness recorded (tracked_source_dirty=false), lock-refresh retained as non-pushed artifact (7,718 lines, pushed=false), held-out identifier set extended to 3. Seam: run record / receipt schema + consent sub-suite.
- **New status — storm READY shapes: FIRED (measured).** Retry budget 2/15s, circuit breaker, stage-gate VERIFY-before-ADVANCE, health-aware assignment — all exercised, 6/6 green.
- **New status — certification readiness: CANDIDATE-READY (fixture).** encoding_freshness 7/7 + required_green: true on the synthetic head; independent re-parse agrees. Published-head run and improver pass remain as named hand-backs.
- **New door — the guard's receipt JSON.** `guard-receipt.json` carries mode, probe_source, injection, receipt_written, worktree_clean, exit_code, source hashes, runner_selftest reference. Portable, re-runnable by a stranger.
- **New door — the env-qualification receipt.** `env-qualification-receipt.json` carries tracked_source_dirty, lock_state, canonical_lock_rejected. The source-dirtiness record Kevin's practice requires, now in our machinery.
- **New door — the lock-refresh artifact.** `rfc-out/lock-refresh.patch` (retained, not pushed) + its receipt. Non-pushed discipline recorded, not just stated.
- **New door — the cert receipt.** `cert-receipt.json` with encoding_freshness 7/7, required_green, node counts, independent re-parse agreement, tracked_source_dirty, lock_refresh_path. The certification window's evidence shape, matching his lab's.
- **New line in the night's record:** the round's plan executed to its landing — 5 legs, 17 tests green, 0 public writes, 0 pushes. The humble-pass fold's adopted-both verdict now has machinery behind it, measured, on disk, reproducible.
- **What stays gated:** the gist's edit, the morning comment, the ENTRY append, the published-head run, the improver's formal pass — all still the user's word. The verification weight matched the mission class: light audit (evidence honesty) on this measurement run; the heavy audit belongs to the code-change mission that follows.

## INTEGRITY

Every claim above traces to a receipted path: the files in `moonbeam-exec/`, the JSON receipts, the pytest output (17 passed). Nothing fabricated. The status vocabulary (FIRED / DORMANT / MIS-FIRED / CORRECTLY-ABSENT for mechanisms; COVERED / PARTIALLY-COVERED / GAP / UNKNOWN for coverage; VALID_RECEIPT / VALID_SYNTHETIC / NOT_CERTIFIED for Kevin's taxonomy) is used with observable evidence, never bare claims. The wall clause ran in every probe leg: a non-reproduction was a question, and the minimal case was constructed (forged counters, duplicate IDs, drifted fixtures, missing defs, existing output dirs). No mid-run scope changes. The record's terms only — no imported dynamics, no invented deadlines.

Disk: see `df -h /` at session close.

END OF MOONBEAM-EXECUTION-20261101