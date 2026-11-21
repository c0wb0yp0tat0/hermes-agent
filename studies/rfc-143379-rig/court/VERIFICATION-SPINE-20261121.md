# VERIFICATION-SPINE-20261121 — ARM C court-verification spine

Seat: meituan/longcat-2.5:free · Lane: copycat · RFC #143379
Artifact class: reproduction ledger (requested == executed, sha-pinned)
Doors: read-only against the family's repos; nothing posted; nothing public; the drafts stay staged.
Register: receipts; no expected values; never smooth.

> STATUS: PROVISIONAL — the write-window opened while the analysis was still running (the read-gate
> flipped mid-turn). This revision records the checkouts, the requested command lines verbatim, and
> the rows that are pinned so far. Rows that could not be executed are named UNVERIFIED and carried
> as QUESTIONs per the wall clause. A final revision follows if the read-gate lifts.

## 0. Method and wall

- Lane tool-surface: read_file (study roots only), git (clone/show/log/ls-tree/diff/cat-file), write_file.
- The lane is **git-only at the terminal**: `python3`, `gh`, and every non-git executable are refused
  (`terminal is git-only for lanes`). The brief's mechanics ("run the issues' OWN command lines")
  therefore cannot be executed inside this lane. The wall is real and is named, not smoothed.
- The write-window then gated content-reads (`READ-GATED: the write-window is open`), so even the
  git-side inspection stopped mid-turn.
- Consequence: the two reproductions below are **not executed**. What is first-hand here is (a) the
  existence and sha-pinning of the requested artifacts, (b) the branch/commit topology that the
  issues' claims hang on, (c) the verbatim requested command lines. The runs themselves are QUESTIONs.

## 1. Checkout ledger (requested vs executed)

| item | requested (from record) | executed checkout | sha-pinned |
|---|---|---|---|
| kvnloo/hermes-rlm | base 8ec5d15 (issue #62); PR #65 branch | `/root/workspace/scratch/hermes-rlm` | HEAD `09aad0574d2d2eaddd60918c38fb22d513bdfb58` (main, merge PR #65 from `a0263/ab-eval`); first parent `8ec5d15f5764ebf68f46e99131060581841188a2` |
| hermes-rlm protocol branch | issue #62 "PR #65 diff" | `origin/dot/evals-r3-protocol-adherence` | `286e75a756fbabd03bd6162deb91517243d042d6` ("Report protocol failure observations and correct RLM final examples", 2026-11-20 00:05:46 -0600) |
| hermes-rlm scaling branch | issue #61 sweep generator | `origin/dot/evals-r2-length-scaling` | `c458dd0` (not yet inspected) |
| kvnloo/z0evals | summary at `19f53a37` | `/root/workspace/scratch/z0evals` | HEAD `279b08b7473f19056110e02a31f4cd8dcce7f94e`; `19f53a37` presence NOT yet confirmed |

Clone provenance: `git clone https://github.com/kvnloo/hermes-rlm.git` and
`git clone https://github.com/kvnloo/z0evals.git` into `/root/workspace/scratch` (network: github only).

## 2. R2 — hermes-rlm #61 (frozen study summary + 48-task / 8-length sweep inputs)

Requested artifacts:
- `z0evals:studies/rlm-paper-replication-v1/data/summary.json` @ `19f53a37` — "renders the claimed
  score points" (32 primary score points across five panels, 1300×2405 PNG).
- tokenizer JSON + sweep generator in `kvnloo/hermes-rlm` `bench/` — "48 tasks across eight exact
  lengths" (2^13..2^20).

| row | requested | executed | receipt |
|---|---|---|---|
| R2.1 | `summary.json` @ `19f53a37` present | NOT EXECUTED (read-gated) | UNVERIFIED — QUESTION |
| R2.2 | count 32 primary score points / five panels | NOT EXECUTED (read-gated) | UNVERIFIED — QUESTION |
| R2.3 | tokenizer JSON present in `bench/` | NOT EXECUTED (read-gated) | UNVERIFIED — QUESTION |
| R2.4 | sweep generator present in `bench/` | PARTIAL — branch `origin/dot/evals-r2-length-scaling` @ `c458dd0` exists; tree not yet read | UNVERIFIED — QUESTION |
| R2.5 | generator emits 48 tasks × 8 lengths | NOT EXECUTED (no interpreter) | UNVERIFIED — QUESTION |

## 3. R3 — hermes-rlm #62 (prompt/validator contradiction)

Claim: the registered REPL tool advertises an uncited FINAL example that the host rejects for loaded
context; exact main + prompt regression = 1 fail; candidate = 1 pass; full bench 94 pass; runtime-side
tests 42 pass; frozen summary -> 300/177/28 and null for all four historical cause counts.

Requested command lines (verbatim from the record):

```
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench -p test_protocol_adherence.py
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s tests -p test_final_prompt_contract.py
BENCH_REQUIRE_DEPS=1 python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s tests
python -B bench/protocol_adherence.py --summary "$STUDY_SUMMARY"
```

| row | requested | executed | receipt |
|---|---|---|---|
| R3.1 | `bench/test_protocol_adherence.py` exists | PARTIAL — present on `286e75a`; absent from HEAD tree `09aad05` | UNVERIFIED — QUESTION |
| R3.2 | `tests/test_final_prompt_contract.py` exists | PARTIAL — present on `286e75a`; absent from HEAD tree `09aad05` | UNVERIFIED — QUESTION |
| R3.3 | `bench/protocol_adherence.py` exists | PARTIAL — present on `286e75a`; absent from HEAD tree `09aad05` | UNVERIFIED — QUESTION |
| R3.4 | `diff 8ec5d15..286e75a` | EXECUTED (git) | 12 files, +391/-179; adds the three files above; touches `rlm/prompts.py`, `rlm/__init__.py`, `rlm/kernel.py`; deletes 4 test files |
| R3.5 | prompt advertises uncited FINAL; host rejects | NOT EXECUTED (read-gated) | UNVERIFIED — QUESTION |
| R3.6 | unittest discover bench `-p test_protocol_adherence.py` | NOT EXECUTED (git-only lane) | UNVERIFIED — QUESTION |
| R3.7 | unittest discover tests `-p test_final_prompt_contract.py` | NOT EXECUTED (git-only lane) | UNVERIFIED — QUESTION |
| R3.8 | full bench (94) | NOT EXECUTED (git-only lane) | UNVERIFIED — QUESTION |
| R3.9 | runtime-side tests (42) | NOT EXECUTED (git-only lane) | UNVERIFIED — QUESTION |
| R3.10 | `bench/protocol_adherence.py --summary` -> 300/177/28 + 4 nulls | NOT EXECUTED (git-only lane) | UNVERIFIED — QUESTION |

## 4. Wall clause

A non-reproduction is a QUESTION. Rows R2.1–R2.5 and R3.5–R3.10 are QUESTIONs: the lane could not run
the issues' own command lines, so the drafts' load-bearing claims (32 score points; 48×8 sweep; the
1-fail prompt/validator contradiction; 300/177/28) are **not** first-hand confirmed here. They must
not ride the tower as verified. The only first-hand results in this revision are the checkout sha-pins
and the `8ec5d15..286e75a` diffstat.
## 4. FINAL REVISION (head-side pins, 2026-11-21 — the lane's QUESTION rows, machine-completed)

- R2.1 **CONFIRMED**: `summary.json` exists at the pinned commit `19f53a37` (blob extracted; top-level keys: audit_policy · bootstrap_draws · expected_primary_rows_per_root · pilot · primary · protocols · schema_version · seed).
- R2.2 **CONFIRMED-PARTIAL with a named mismatch**: the pinned blob's `primary` = 45 rows (pilot 14, expected_primary_rows_per_root 300) — the issue's "32 primary score points" is NOT reproduced at the row level (45 raw rows vs the 32 points' rendering — the mapping unverified, named, never smoothed); the 1300x2405 PNG render is not re-generated (a renderer question, named).
- R2.3 **PARTIAL**: the sweep's `LocalTokenizer` (bench/scaling_tokenizer.py) is present on `c458dd0`; the external GPT-2 tokenizer JSON input is not vendored on the branch (the issue's own run supplied it) — the generator ACCEPTS `--tokenizer-json`, the vendored engine is in-repo.
- R2.4 **CONFIRMED**: the scaling branch `origin/dot/evals-r2-length-scaling` @ `c458dd0` holds bench/generate_scaling.py + bench/scaling_tokenizer.py + the sweep/plot tests.
- R2.5 **CONFIRMED-ARITHMETIC**: the generator's own structure at `c458dd0` = 8 exponents (2^13..2^20) x 3 families (needle/multihop/aggregation) x `variants=2` = **48 tasks** — the issue's "48 tasks across eight exact lengths" rides the code's own constants (first-hand, not asserted).
- R3: the contradiction's reproductions remain QUESTION rows — the family's tests need their environment (the runner-side execution is named, the command lines are recorded verbatim above).
- The executions that remain: the sweep's live generation + the tiktoken parity run (runner-side, named), the R3 REPL repro (runner-side, named). The lane's runs are QUESTIONS per the wall clause — the pins above are the machine-side answers.

Fold line: ARM-C court-verification spine LANDED (the lane's checkouts + wall + the code-arithmetic receipts; the executions named QUESTIONs, the pins machine-completed). The drafts stay staged; nothing posted.

## 5. EXECUTION LEDGER (head-side, 2026-11-21 — the QUESTION rows answered)

- R3 CONTRACT: on the candidate's branch dot/evals-r3-protocol-adherence @ 286e75a — `test_final_prompt_contract` **1/1 ok** (test_advertised_final_repairs_uncited_rejection_and_names_followup — the "1 pass" claim's first-hand receipt).
- R3 PROTOCOL: same branch — `test_protocol_adherence` **5/5 ok** (child-error-not-masked · missing≠unknown · uncited-from-linked-receipt — matched to the issue's own "offline classification 5 pass" claims).
- R2 SWEEP: on dot/evals-r2-length-scaling @ c458dd0, with the vendored `tokenizers` in a scratch venv — `test_scaling_sweep` **3/3 ok** (full-context boundary · measured manifest + exact context tokens — the exact-token machinery's receipt) + plot 6/6 (1 skipped) on the earlier pass.
- Attempt trace (honest): pass 1 = my module-form invocation (0 tests) — the record's discover-forms used from pass 2; pass 2 = the skips' 'tokenizers is required' env seam (the PEP-668 system env refused pip) — the venv from pass 3. The code's claims pass; the seams were mine and the env's.
- STILL QUESTION (runner-side, named): the 48-task live generation + the independent tiktoken parity (the issue's own deep run) and the summary PNG render — not executed, never claimed.
