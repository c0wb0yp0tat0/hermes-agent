# RUN-A-LEG GUIDE — volunteer runner onboarding (the RFC #143379 homebase)

**Welcome, and thank you.** You can run a verification leg of our study from a GitHub-hosted runner in about 10 minutes — no Hermes install needed, no self-hosted runner needed. This is the whole path, copy-paste style. When you finish a leg, post your result back on PR #1 (the link at the bottom) and we'll fold it into the ledger.

## What you're doing, in one line
You run the same pinned-verification workflow the rig's own runner runs — on GitHub's free hosted runners — and report the verdict back to the homebase thread.

## Part 1 — the fork (once, ~2 minutes)
1. Go to `github.com/c0wb0yp0tat0/hermes-agent` → **Fork** (your own copy).
2. On YOUR fork: **Settings → Actions → General → Actions permissions → select "Allow all actions and reusable workflows"** — Actions are DISABLED by default on a fork, so you must enable them: Settings → Actions → General → Actions permissions → select "Allow all actions and reusable workflows" → Save. (Or open the Actions tab and click "I understand my workflows, go ahead and enable them".)
3. Open the **Actions** tab of your fork — the workflow list includes `rig-hosted-verify-avrea (the parallel verification surface)` among the fork's other workflows (the fork carries the full workflow set; ours is the one you run).

## Part 2 — the dispatch (each leg, ~1 minute)
1. Actions tab → click the workflow name → **"Run workflow"** (right side).
2. **Branch:** `main`.
3. **head_sha:** paste a full 40-character SHA. Take one from the most recent rows on the PR thread (the SHAs our receipts cite, e.g. `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` — any full SHA the thread names). The workflow pins and verifies exactly that commit.
4. Click **"Run workflow"**. That's the whole dispatch.

## Part 3 — the read (~5 minutes, while it runs)
1. Open the run (the Actions tab shows it) → the **"Avrea full-suite (main)"** job.
2. The job has TWO matrix arms: `ubuntu-latest` (yours — runs on GitHub's hosted runners) and `avrea-ubuntu-latest` (our self-hosted label — it will sit **pending / eventually fail** on your fork because you don't have that runner; **that is expected — ignore the avrea-arm entirely**).
3. Open the **ubuntu-latest arm** → scroll to the step **"The verification battery (write-gate + memory-tool + falsifier-battery)"** → read its last pytest line, e.g. `2 failed, 82 passed, 8 skipped, 1 xfailed in 3.87s`.
4. Also copy the **run's URL** (the `github.com/<you>/hermes-agent/actions/runs/<id>` link).

## Part 4 — the report-back (the whole value, ~2 minutes)
Post a comment on **PR #1** (`github.com/c0wb0yp0tat0/hermes-agent/pull/1`) in this exact shape:

```
## RUNNER-ROW (volunteer, GitHub-hosted) — <short name or handle>
- run: <the run id>
- url: <the run's link>
- arm: ubuntu-latest (the avrea-arm pending = expected on a fork)
- pin: <the 40-char SHA you dispatched>
- battery summary: <the pytest line, verbatim>
- requested == executed pin discipline: the pin you dispatched is the pin the run verified (record both if they ever differ)
```

That's the whole leg. The homebase reconciles your row against the ledger's receipts — the divergence is the data, and every independent execution strengthens the study.

**The loop:** each leg you complete earns the next task — the homebase hands the next one as a new gist via the same path (fork → dispatch → report). The guide you're reading is task one; the board (PR #1) is where the loop lives.

## Part 5 — the deeper leg (optional, when you want more signal)
The study also measures a 5-fixture ladder battery (the compression-eval repo). Same fork pattern: fork `c0wb0yp0tat0/hermes-compression-eval`, clone it locally, then from the repo root:

**Needs first:** provider credentials configured (`hermes setup` or the provider env vars; `run_eval.py` raises without a configured provider) and the `hermes-agent` checkout on the path (`compressor_driver` locates it) — see the compression-eval README.

```bash
pip install -r requirements.txt 2>/dev/null || true
python3 run_eval.py --fixtures config-build-competitive-scouts,debug-session-feishu-id-model,feature-impl-context-priority,fixture-deep-compaction-real,fixture-high-density-real --runs 3 --label volunteer-<yourname>-<date>
```

Then report the per-fixture medians from `results/<label>/summary.json` — one line per fixture (fixture name, median overall, n runs) — as an addendum to your RUNNER-ROW (not the single battery-summary line). Each independent run of this battery adds a row to the ladder's evidence.

## The ground rules (the homebase's contract, in brief)
- The fork only — no upstream repos, no upstream posts.
- Every report is receipts-only: the run link, the pin, the verbatim summary line. Claims without the run-link don't ride.
- Ask anything in the PR thread — the scout answering is the same machinery that maintains the ledger.

**PR #1 (the homebase):** https://github.com/c0wb0yp0tat0/hermes-agent/pull/1
