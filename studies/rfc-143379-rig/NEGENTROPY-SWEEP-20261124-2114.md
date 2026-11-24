# NEGENTROPY-SWEEP-20261124-2114

- seat: copycat lane, recurring negentropy-sweep ride (RFC #143379 apex mission)
- branch: rig/rfc-143379-fold-p0tat0-republish-again-writes-20261124 @ e505c7429de
- fire time: 20261124-2114 · cadence 2h · no_agent arm
- the gate, verbatim: "the gate: nothing public without the user's word." — nothing posts, upstream stays QUIET, artifacts only.
- register: **[1st]** re-read by this lane this pass (git log/tree/status, study listings) · **[2nd]** carried from a study doc, not re-derived · ABSENT + named when unreceivable. Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)

| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition: P2 (REGROUP) + P2b (DISCERN-5D) + P3 (LANES-6) all landed | **PARTIAL** — P2 LANES-6 reply row says "lane finding **pending**"; a `P3-LANES6-FINDING-20261124.md` is present on disk but no commit found by path-history (`git show HEAD:<path>` → absent; `git log --all -- <path>` empty). Landing state indeterminate. | IN-LANE (disk listing vs object store disagree; named, not adjudicated) |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42 flat) | **NOT RUN** — third consecutive fire; no lane owns it; sweep has no read window (see §3 friction F5) | [2nd] 5fe6d71157f §1; IN-LANE: no commit since |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | **NOT RUN** — needs a read window; same blocker | [2nd] 5fe6d71157f §1 |

## 2. THE SEAM-SCAN (every fire)

| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline seam (max-chars > total) | **STILL UNVERIFIED** — no wire-check commit since 1913. HEAD's newest runner artifact (548c3e20ff7) is an *execution* receipt (green/green/green/red, live-list rollback), not the deadline wire-check. | IN-LANE (log scan) |
| fold check: scribe cell → get_memory byte-compare | **NOT RUN** this fire | IN-LANE |
| fold check: served `?raw=1` grep | **NOT RUN** this fire | IN-LANE |
| token watcher single-source line | token `hermes_loop_state` (receipt `yu83n24zb…`); source of truth = ARM-EXECUTE file per arming §1; **no `loop-state` file exists anywhere tracked** (grep → 0) → ABSENT + named | [2nd] NEGENTROPY-ARM-EXECUTE-20261119 §1; IN-LANE grep |
| machine layer: scribe tunnel / runners / Harbor / local-LM | **NOT WIRE-CHECKED** this fire | IN-LANE |
| dispositions | read-burn → **HOLD-SAFE**; W2 → **NEEDS-THE-CHAIR** until P3 landing adjudicated; nested/untracked plane → **AUTO-CONTINUE** (land-or-archive) | IN-LANE |

## 3. THE ENTROPY CLASSES (CTO freedom)

**Dead surface — D1.** `studies/rfc-143379-rig/studies/` untracked nested plane (~666 files: `NEGENTROPY-ARM-20261106`, `NEMO-WIRE-RISK-TO-BASE-20261119`, scans, old briefs) — mis-rooted duplicates, never swept, never purged; 1913 flagged it, unchanged. *Countermove:* land-if-load-bearing else `mv` to an untracked `.archive/` scratch; stop the ambiguity.

**Loose threads — L1.** Unrowed landings sitting untracked beside HEAD: `NEGENTROPY-SWEEP-RECURRING-brief.md` (its own receipt claims "this template's home is the branch" — false here), `REMAINING-STORM-QUEUE.md`, `NESTED-MISSION-DISPATCH-20261124.md`, `SCRIBE-WITNESS-REGISTRY.log` (+ duplicate at `plan/tank/`), `/root/workspace/repos/race-probe-20261124.py`. *Countermove:* one disposition row each; land the recurring brief first.

**Orphan sentinels — O1.** 81 tracked `.sentinel`; pair-audit against base docs **not completed this fire** (read gate closed mid-scan) — ABSENT + named. Live symptom: the guard that would catch a duplicate key is unbuilt while `SCRIBE-WITNESS-REGISTRY.log` already exists twice (root + tank), i.e. drift in a non-sentinel file. *Countermove:* duplicate-key reject script + pair audit.

**Friction — F1 (the prize).** The rig's read/write-window split defeats the sweep's own mandate: read-tools refused mid-analysis with "the write-window is open — the analysis-phase is over," exactly as 1702 and 1913 recorded. Consequence: any window-check item needing a read (k-term re-measure, budget re-verify, sentinel pair-audit, byte-compare fold check) **cannot close inside this lane**. *Countermove:* re-home the re-measures to a read-window lane, or pre-stage their inputs as [2nd] fixtures in the arming record so the sweep only stamps, never reads.

**UNSPOKEN — U1.** The two-tier k-term flatness (0.26–0.42) contradicts the budget's presupposed class ordering; three fires have recorded it and no seat has answered. *Countermove:* chair rules once — flat-is-the-finding (drop the ordering) or re-measure; do not carry a fourth time.

## 4. THE ORDERED NEXT-MOVES

1. Land-or-archive the untracked operating docs (recurring brief first). gate: artifact-only. seat: head.
2. Adjudicate `P3-LANES6-FINDING-20261124.md` (land or mark unrowed) and strike the stale "pending" row. gate: chair. seat: head.
3. Build the sentinel duplicate-key guard + pair-audit the 81. gate: none (script). seat: coder.
4. Read-burn harness-deadline wire-check (max-chars>total / total=0), both receipts. gate: artifact. seat: runner.
5. Re-home k-term + budget re-measures off-sweep. gate: arming record updated. seat: head.
6. Prune/land nested `studies/` plane. gate: fold review. seat: head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

1. register fixed — this file tags every claim [1st]/[2nd], IN-LANE/BORROWED/HEAD-RECON.
2. receipts not claims — tree-vs-object discrepancy left named, not smoothed.
3. absence named — loop-state file, pair-audit, wire-checks all ABSENT + named.
4. CTO freedom held — no adoption of storm-context designs; only corroboration of class.
5. gate verbatim — quoted in header, nothing public.
6. one section per write, ≤6,000 chars per write — honored.
7. delta vs baseline 5fe6d71157f stated per row, not re-narrated.
8. commit locally, never push — final step.

## 6. THE LOOP-STATE LINE

`CONTINUE + land-or-archive the untracked operating docs (recurring brief first) and build the sentinel duplicate-key guard.` Receipt: IN-LANE HEAD e505c7429de; [2nd] baseline 5fe6d71157f.