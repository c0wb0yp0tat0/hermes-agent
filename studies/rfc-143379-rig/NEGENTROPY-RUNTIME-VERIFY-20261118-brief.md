# NEGENTROPY-RUNTIME-VERIFY brief — the successor leg, queued for the runners (executes on a self-hosted runner with full access)

**Why this leg is a runner leg:** the runtime credential verification cannot execute in a git-only harness lane (the value probe needs python + a config read). The runners run on everything; this leg joins their queue and closes under the two-way-door check.

## The job (from the plan's successor brief, NEMO-NEGENTROPY-PLAN-20261118)
1. **Runtime credential verification**: probe whether the eval harness's runtime resolution returns non-empty `api_key` and/or `base_url` — the gate at `run_eval.py` line 81 (`if not runtime.get("api_key") and not runtime.get("base_url"): raise RuntimeError(...)`); the either-or gate passes when at least one is set. Measure the state truthfully: probe `resolve_runtime_provider` / the runtime config the runner can read; if both are absent, the W2-isolation settle-condition stays OPEN and nothing is invented to fill it.
2. **W2-isolation re-run**: per the on-branch spec `W2-ISOLATION-RUN-DESIGN-20261107.md`, run the evaluation once with the credential state now measured; record the outcome with the same verdict vocabulary as the sweep rows (VERIFIED / PARTIAL-with-seam / UNMEASURED + the settle-condition line).
3. **Artifact**: `NEGENTROPY-RUNTIME-VERIFY-20261118.md` — verdict line first, then the probe's receipts (the exact commands + their outputs, quoted), then the W2-isolation outcome, then the loop-state line.
4. **Gate**: the leg closes only when its own check closes — the probe's outputs quoted, the credential state named, the settle-condition re-armed or closed. Two-way door: a partial probe re-runs with its receipt.

## Disciplines (the runner's own)
Run read-only against the repository and its runtime config; quote every command and its output; never guess a value; the artifact lands on the study branch (commit + push with the study identity); RFC quiet; the head checks the leg's bytes at the fold.
