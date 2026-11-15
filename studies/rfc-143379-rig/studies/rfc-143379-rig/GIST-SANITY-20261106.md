# GIST-SANITY-20261106 — run-a-leg guide sanity check (first eye)

**Lane:** copycat (beam-1.0). **Artifact:** `studies/rfc-143379-rig/GIST-SANITY-20261106.md`.
**Register:** receipts, never claims. Ground = staged guide copy + workflow yml (git HEAD) + run_eval.py (git HEAD of hermes-compression-eval) + RECEIPTS.md rows. No thread prose read (thread-ban).

## Executive Summary

The guide is **substantially byte-accurate** on the workflow's identity strings, matrix arms, input name/shape, run-URL shape, and the deeper-leg fixtures/flags. It carries **four real defects** a volunteer would hit: (a) the fork's Actions step claims "Allow all actions" is the default (it is disabled by default on forks), (b) the fork's Actions tab is claimed to show "one workflow" (a fork shows all workflows), (c) the example SHA `54395f9b…` is not a receipt-cited SHA, (d) the deeper leg's "same RUNNER-ROW shape" does not fit a multi-fixture median report. **Verdict: FIXES-NEEDED** (4 FIX, 5 APPROVE, 1 UNVERIFIABLE).

## Analysis Brief

- **Domain:** volunteer onboarding guide correctness (COMPLICATED — expert byte-verification against committed artifacts).
- **Evidence:** `/root/.hermes/cache/scratch/pr1-rotation/RUN-A-LEG-GUIDE.md` (staged guide); `git show HEAD:.github/workflows/rig-hosted-verify-avrea.yml` (workflow, branch `study/rfc-143379-rig-20261105`); `git show HEAD:run_eval.py` in hermes-compression-eval; `studies/rfc-143379-rig/RECEIPTS.md` (ledger rows).
- **Assumptions:** the staged guide copy is the gist's current text; the workflow yml on the study branch is the deployed definition; PR #1 exists.
- **Uncertainty:** PR #1 existence and the gist's live bytes are not verifiable from the repo (UNVERIFIABLE items below).
- **Alternatives considered:** treating the Actions-enable wording as harmless (rejected — a fork's Actions are disabled by default, so a volunteer following "just confirm" would find no runs).

## Per-item APPROVE/FIX/UNVERIFIABLE table

| # | Item | Verdict | Citation | Fix (exact edit) |
|---|---|---|---|---|
| 1 | Fork-path correctness (fork's Actions-enable step) | **FIX** | Guide Part 1 §2: "Settings → Actions → General → Actions permissions → 'Allow all actions' (it's the default; just confirm it's enabled)." Reality: GitHub disables Actions on forks by default; the owner must enable. | Replace parenthetical with: "(Actions are DISABLED by default on a fork — open Settings → Actions → General → Actions permissions → select 'Allow all actions and reusable workflows', then Save; alternatively open the Actions tab and click 'I understand my workflows, go ahead and enable them')." |
| 2 | Workflow NAME-string as guide names it | **APPROVE** | Guide Part 1 §3: `rig-hosted-verify-avrea (the parallel verification surface)`. Workflow yml `name: rig-hosted-verify-avrea (the parallel verification surface)`. Byte-identical. | — |
| 3 | Branch `main` | **APPROVE** | Guide Part 2 §2: "Branch: main". Repo default branch `origin/HEAD → main` (verified). Workflow runs on selected branch; main is the default. | — |
| 4 | Input name `head_sha` + shape full 40-char SHA | **APPROVE** | Guide Part 2 §3: `head_sha` + "full 40-character SHA". Workflow input `head_sha` (required: false, default ""). Pin-verification step asserts `actual == requested`; a short SHA fails the assertion. Example SHA `54395f9b4f0cc1d0a840ec2640580e7af9c4ed25` is 40 chars. | — (but see FIX on example SHA veracity below) |
| 5 | Matrix's `ubuntu-latest` arm EXISTENCE | **APPROVE** | Guide Part 3 §2: `ubuntu-latest` arm. Workflow: `matrix.runner: [avrea-ubuntu-latest, ubuntu-latest]`, `runs-on: ${{ matrix.runner }}`. Arm exists. | — |
| 6 | Avrea-arm expected-pending-on-a-fork claim | **APPROVE** | Guide Part 3 §2: avrea arm "will sit pending / eventually fail … expected — ignore". On a fork no self-hosted runner carries label `avrea-ubuntu-latest`, so the job stays queued until the 45-min `timeout-minutes` fires → fail. `fail-fast: false` lets the ubuntu arm run independently. Claim holds (pending then timeout-fail). | — |
| 7 | Run-URL shape | **APPROVE** | Guide Part 3 §4: `github.com/<you>/hermes-agent/actions/runs/<id>`. Standard GitHub Actions run URL is `https://github.com/{owner}/{repo}/actions/runs/{run_id}`. | — |
| 8 | RUNNER-ROW report-shape fidelity | **APPROVE** (with note) | Guide Part 4 block: run / url / arm / pin / battery summary. Ledger (RECEIPTS.md) columns: Date, Pin, Run, requested==executed, Conclusion, Notes (battery summary lives in Notes, e.g. "82 passed in 5.72s"). The guide's block captures pin, run, url, arm, summary; equality-assertion and verdict are derived by the homebase from the run URL, as the guide states ("The homebase reconciles your row"). Shape is a comment-block variant, not a ledger table row, but all raw inputs the homebase needs are present. | Optional (not required): add `requested == executed: <full SHA>` line to mirror the ledger column; left to head. |
| 9a | Deeper leg fixtures' names | **APPROVE** | Guide Part 5 fixture list: config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority, fixture-deep-compaction-real, fixture-high-density-real. Repo `fixtures/` contains exactly those 5 `.json` files (all also have matching `.probes.json`). | — |
| 9b | run_eval.py command flag-accuracy | **APPROVE** | Guide: `python3 run_eval.py --fixtures … --runs 3 --label volunteer-<yourname>-<date>`. run_eval.py argparse defines `--fixtures`, `--runs` (int, default 3), `--label`; fire path exposes the same. Output lands in `results/<label>/summary.json` (guide's stated path), containing per-fixture medians in `fixtures`. | — |

## Additional FIX items (outside the 9-point set, but volunteer-blocking)

- **FIX (Part 1 §3, "one workflow"):** A fork of hermes-agent carries the full workflow set (tests.yml, lint.yml, …). The Actions tab will NOT show "one workflow"; it shows many. Edit: "the workflow list should include `rig-hosted-verify-avrea (the parallel verification surface)` (among the fork's other workflows)."
- **FIX (Part 2 §3 example SHA):** `54395f9b4f0cc1d0a840ec2640580e7af9c4ed25` does not appear in RECEIPTS.md (receipt-cited SHAs: d1bdb458…, a996d4ad…, ffb85c2c…, 60a2e156…, ec649ad9…, c39d8ce7…, 49052702…). Edit: replace example with a receipt-cited full SHA, e.g. `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a`.
- **FIX (Part 5 report-back):** "report the per-fixture medians … in the same RUNNER-ROW shape" is a mismatch — summary.json holds 5 fixture medians, not one pytest line. Edit: "report the per-fixture medians from `results/<label>/summary.json` (one line per fixture: fixture name, median overall, n runs) instead of the single RUNNER-ROW battery-summary line."
- **FIX (Part 5 env):** The deeper leg needs provider credentials (run_eval requires a configured provider; it raises RuntimeError otherwise) and the hermes-agent checkout on path (compressor_driver locates it). Add a line: "requires `hermes setup` / provider env vars; see compression-eval README."

## UNVERIFIABLE

- **PR #1 existence / URL** (`github.com/c0wb0yp0tat0/hermes-agent/pull/1`): not verifiable from repo files; would settle via GitHub PR list. The guide's report-back target depends on it.
- **The gist's live bytes:** this check ran on the staged copy only; the gist itself (the published secret gist) was not fetched. Head must re-verify the published gist against this copy before posting.

## Overall verdict: FIXES-NEEDED

Four FIX items above (Actions-enable default, "one workflow" claim, example SHA, deeper-leg report shape/credentials). Five APPROVE items (2, 3, 4 name/shape, 5, 6, 7, 9a, 9b) — counting 9a/9b separately. One UNVERIFIABLE (PR #1 / gist live bytes).

### Success criterion for re-check (second eye)
After head applies the four FIX edits, re-run this sanity check: all 9 acceptance items APPROVE, the four additional items resolved, UNVERIFIABLE items settled by head (PR #1 confirmed, gist bytes fetched and diffed). Then third eye (AoA) signs off before the PR reply posts.

## Next Steps / Exploration

- Head applies the four FIX edits to the gist source; second eye (audit) re-verifies; third eye (AoA) signs off; PR reply posts only on three-eyed approval.
- Optional: add a `requested == executed` line to RUNNER-ROW (left to head).

## Artifact

`studies/rfc-143379-rig/GIST-SANITY-20261106.md` (this file).