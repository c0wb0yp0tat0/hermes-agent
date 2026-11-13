# HITL-GAINS-SKEPTIC-20261107 — the counter-pass: the non-progress ledger, the calibration, the refutation-test

**Seat:** `meituan/longcat-2.5:free` (copycat lane 3 — THE SKEPTIC). **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Register:** receipts, never claims — every line below traces to a file on this branch, a commit in the branch's log, or the PR's own diff-stat. The draftsman's framing is never reused; the counter's own reads are the ground. **Gate:** nothing public without the user's word. **Date:** 2026-11-07.

> **One-line finding:** The study's real output is a *measured* negative (the K-recency gate FAIL) plus a staged evidence-set for four lines that have not moved — the "progress" is honest preparation, and the one experiment that would convert preparation into arrival (the W2-isolation) is still unmeasured, so the user's concern is right about the *arrival gap* and wrong only if it reads the *waiting* as *drift*.

---

## §1 — THE NON-PROGRESS LEDGER (what has NOT actually advanced)

The ledger is the counter's own enumeration. Each row names the artifact, the marker's exact wording, and the state that has not changed.

### 1.1 The RFC's four lines — STILL STAGED, their gates untouched, the upstream surfaces quiet

**Receipt:** `NEXT-SHIFT-PLAN-20261107.md` (the successor plan, seat `meituan/longcat-2.5:free`), the standing frame quoted verbatim: *"the study's four lines stay **STAGED** (restore #141876 · network #116673 · governance #139606 · compaction #140008)"*. The same frame is carried in `EXP-SUMMARY-NIGHT-20261106.md`: *"the RFC's four lines all STAGED (restore, network, governance, compaction)"*.

The four lines' own staging docs confirm the state, each with its gate named and un-crossed:

| Line | Staging doc | The doc's own status | The gate's state |
|---|---|---|---|
| **restore #141876** | `RFC-GUIDANCE-20261105.md` + `HITL-READY-20261105.md` | darkhorse-bridge bytes, NOT-IN-CHAIN live; candidate staged "decision awaited" | gate holding; no upstream surface opened |
| **network #116673** | `NETWORK-ADOPTION-FOLD-20261107.md` | *"ADOPTION-FOLD — PARK upstream adoption, ADOPT fork-side probe"* | the upstream break-glass gate (the installed build's missing `read`) untouched; the line is *"compensated, not adopted"* |
| **governance #139606** | `GOVERNANCE-FOLD-DRAFTS.md` | *"Status: on-branch finding only (no public post). Staged evidence for the #139606-line."* | 8 OWASP-gap fold-drafts staged; nothing posted; the OWASP mapping's gaps unclosed |
| **compaction #140008** | `EXP-SUMMARY-NIGHT-20261106.md` + the seam-arc docs | fix-spec (delta-7) staged; the 3-block composition's ~240-token heuristic named | the full-eval at the provider-window's return is *"still pending (rungs ready, not run)"* |

**What has NOT advanced:** in the ~2 days since the study's first landing, none of the four lines has crossed from *staged* to *landed*; none of their gates has been touched by an upstream event; the upstream's surface is quiet. `RFC-GUIDANCE-20261105.md` says it plainly: *"Nothing upstream was written by this study."* `FLEET-CYCLE-BODY-20261107-1403.md` repeats it at the head: *"the upstream's surface quiet until the user's word (the authoritative gate — no self-gate, no re-ask beyond it)."* The four lines' *evidence-sets* are complete; their *arrivals* are not. The study has produced a finished case for four lines and moved none of them.

### 1.2 The eval-window's wall — the W2-isolation's SEPARATION-UNMEASURED

**Receipt:** `W2-ISOLATION-STATUS-20261106` (commit `847c61ac4f`) — the verdict-line is **SEPARATION-UNMEASURED** per the wall-clause; the guard-preamble + empty-answer receipts are banked, but the isolate re-run has not executed. The spec exists: `W2-ISOLATION-RUN-DESIGN-20261107` (commit `d760fcae90`, *"the isolate-the-guard experiment's full spec"*). The successor plan's goal #1 names the gap exactly: *"The pre-written spec-skeleton is **FILLED** — the one re-run with probe-answering isolated from the handoff guard lands its separation verdict (SEPARATION-MEASURED or SEPARATION-REFUTED)"* — and its receipt is *"the W2-ISOLATION-STATUS's verdict-line flipped from SEPARATION-UNMEASURED."*

**What has NOT advanced:** the spec is written; the run has not happened. The wall-clause's own terms (`AVREA-LEG-CONTRACT.md`: *"the eval-runtime cannot execute the isolate re-run yet"*) mean the one experiment that would settle whether the W2-empty-answer confound is liftable from the verdict is still unmeasured. The plan's audit (`NEXT-SHIFT-PLAN-AUDIT-20261107.md`) confirms the trigger: *"the W2 eval-window opening (the arm's receipt 3 — `run_eval.py:81` keys on `api_key`/`base_url`; the window is CLOSED at handoff)."* The window is closed; the wall stands.

### 1.3 The harness write-deadline — named, unbuilt

**Receipt:** the successor plan's goal #1 + its audit name the harness as the thing that must exist for the eval-window to open. The audit's finding: *"the plan correctly fails to promise a run on a closed window"* — and the arm's receipt is `run_eval.py:81`'s keying on `api_key`/`base_url`. The harness that would let the isolate re-run execute is **named** (the run-design spec) and **unbuilt** (the eval-window is closed; no receipt row exists for the isolate run).

**What has NOT advanced:** the write-deadline is a named dependency, not a built one. The plan's own acceptance row for goal #1 is the *flip* of the verdict-line; the flip has not occurred. The harness's absence is the binding constraint on the eval-window — the wall that keeps the W2-isolation unmeasured is the harness that has not been written.

### 1.4 The study's upstream-visible delta — a docs/verification PR

**Receipt:** the fork's PR #1 diff-stat, read from the branch: **260 files changed, 178,135 insertions(+), 1 deletion(-)**. The delta's composition, read from `git diff --stat origin/main...HEAD`: the overwhelming majority is `studies/rfc-143379-rig/**` — the study's markdown, the krecency instruments (`probe_*.py`, `sweep_*.py`, `krec_core.py`), and the results CSVs (`sweep.csv` 14,851 lines, `sweep_scaling.csv` 78,201 lines, `sweep_age.csv` 8,251 lines, `compete.csv` 24,751 lines, `competing.csv` 19,801 lines, `archive.csv` 14,851 lines, `recite.csv` 801 lines). The non-study delta is thin: a handful of `tests/falsifier-battery/test_*.py` files, `tests/tools/test_memory_tool.py`, `.github/workflows/` (the fabric-battery workflow), and `.tmp-artifacts/`.

**What an external reviewer would credit as the study's real output:** the **krecency instruments and their measured verdicts** — the gate FAIL at 300+ cycles (all 25 seeds sub-zero at 4x/300c+), the aliasing × cumulative-proximity classes (R² = 0.655), the constraint-pinning arm (0% violation), the archive's ID-known recall as the optimistic bound. Those are the science. The rest is markdown — the study's own record of itself. A reviewer opening PR #1 sees 178k lines of which the substantive, re-derivable core is a few thousand lines of Python + CSV; the remaining ~95% is the study's process narrative. **The PR is a docs/verification PR; it lands no fix to the RFC's four lines.**

### 1.5 The machinery's churn vs the science's output

**Receipt:** the branch's own cycle counts. The ACES improver loop ran **four full cycles** (C1–C4): C1 named 14 improvements → 9 CONFIRMED / 2 NUANCED / 3 REFUTED (`5e0774420b`); C2 4/4/0 (`93ced6090b`); C3 11/0/0 (`ca15b98e1f`); C4 11/11 (`c1965e6871`, `ccd33a1ebf`). The loop's steady state is **zero** — *"NO-IMPROVEMENTS CONFIRMED TWICE"* (`f084af11cf`). The copycat loop likewise converged (`e1d9b0c51b`). The NEGENTROPY sweeps ran three scheduled cycles (0948 / 1149 / 1350). The handoff fanout ran three lenses + an audit + an AoA. The next-shift-plan ran an author + an audit + an AoA. The 31-fork fabric was designed, launched, re-dispatched, and receipted.

**What has NOT advanced (the ratio):** the science's output is the krecency measurements (the gate FAIL), the seam-arc (5/5 → 0/5 on the walked subset), the ladder battery (5 rungs, LADDER-SEPARATED), and the E-3 continuation-loss probe. The machinery's output is the loops, the sweeps, the handoffs, the plans, the fabric, the audits — each receipted, each honest, each *about the study* rather than *about the RFC*. The ACES loop's convergence to zero is the clearest marker: four cycles of machinery produced **zero** new commits since `653f535bfd`. The churn is real; the science's marginal output per cycle is, at the converged state, zero.

### 1.6 The ledger's summary

| # | The non-progress item | The marker's exact state | What would change it |
|---|---|---|---|
| 1 | The four RFC lines | STILL STAGED; gates untouched; upstream quiet | one line's gate touched or crossed |
| 2 | The W2-isolation | SEPARATION-UNMEASURED | the isolate re-run lands its verdict |
| 3 | The harness write-deadline | named, unbuilt; eval-window CLOSED | the harness exists and the window opens |
| 4 | The upstream-visible delta | a docs/verification PR (178k lines, ~95% markdown) | a landed fix, not a staged case |
| 5 | The machinery's churn vs science's output | 4 ACES cycles → 0 commits; 3 sweeps; 3-lens fanouts | a cycle that names a real, landed improvement |

---

## §2 — THE CALIBRATION (the user's concern, honestly read)

The user's concern: *"we're not making the progress it seems / we could be making more."* The honest read splits it into what the concern is RIGHT about and what it is MISSING.

### 2.1 What the concern is RIGHT about

1. **The arrival gap is real.** Four lines staged, none landed; the upstream surface quiet for ~2 days. The "progress" the study reports is preparation, not arrival. The concern's core — that the distance between *staged* and *landed* is not closing — is correct on the branch's own bytes.
2. **The one decisive experiment is unmeasured.** The W2-isolation is the experiment that would tell the study whether its central eval-window confound is liftable. It is unmeasured. The concern that "we could be making more" is sharpest here: the study has a *written spec* for the decisive run and has not run it, because the harness/window is closed.
3. **The harness is the binding constraint and it is unbuilt.** The write-deadline is named in the plan; the plan's audit correctly refuses to promise a run on a closed window. The concern is right that the thing blocking the decisive experiment is a *build*, not a *discovery* — and the build has not been made.
4. **The PR's upstream-visible delta is thin.** 178k lines, ~95% markdown; the substantive core is the krecency instruments. An external reviewer credits the instruments, not the narrative. The concern is right that the study's *public* output is a docs/verification PR, not a fix.
5. **The machinery's marginal output has converged to zero.** Four ACES cycles, two convergences, three sweeps, multiple fanouts — and zero new commits since `653f535bfd`. The concern is right that the loop's steady state is *no improvement*, and that a no-improvement loop, however honestly run, is not a progress engine.
6. **The walls census is large and unclosed.** `HONEST-WALLS-CENSUS-20261106.md` enumerates **40 markers** (8 NOT-RUN, 8 UNMEASURED, 16 WALL-CLAUSED, 8 MARKED-OPEN). The GitHub-hosted window side is NOT RUN; the recitation-length class is NOT RUN; the fleet's independent adjudications are MARKED-OPEN. The concern is right that the wall inventory is long and the settle-conditions are mostly unmet.

### 2.2 What the concern is MISSING

1. **The wait is a gate, not a drift.** The upstream's quiet is the *user's word* as the authoritative gate — `FLEET-CYCLE-BODY-20261107-1403.md`: *"the upstream's surface quiet until the user's word (the authoritative gate — no self-gate, no re-ask beyond it)."* The study is not failing to act; it is *refraining* from acting on a surface it has deliberately fenced. Reading the fence as drift misreads the design. The four lines' staging is the study *holding* its fire until the word — a discipline, not a stall.
2. **The science that DID land is substantive.** The krecency gate FAIL is measured, not asserted: all 25 seeds carry sub-zero deltas at 4x/300c+; the aliasing × cumulative-proximity classes carry R² = 0.655 (bar 0.35); the constraint-pinning arm holds 0% violation; the archive's ID-known recall is named as the optimistic bound. The seam-arc walked to cleared on the walked subset (5/5 → 0/5, blind-audit-reproduced at substance). The ladder battery separated depth from density on real streams (medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00). This is real, re-derivable output — the concern should not be read as "nothing was measured."
3. **The verification breadth is real.** The 31-fork fabric is not a claim about one fork: 31 distinct run-ids, per-fork pins, the checkout-class receipted (`FABRIC-RECEIPTS-20261107.md`, `9dc35ee053`; the 2.0 re-dispatch `2becb714af`). The first wave's 30-of-31 RED is itself accounted for (the inputs-encoding finding, 422→204 on the `-f inputs=` double-escape). The concern should not be read as "no verification happened."
4. **The ACES convergence is a measured stop, not fatigue.** The loop named 0 improvements and had that zero confirmed twice by independent audit — a *measured* stop, with the branch's 0-commit-since-`653f535bfd` as the receipt. The concern is right that zero is not output; it is wrong if it reads the zero as *failure to look*. The loop looked and found nothing — that is a finding about the study's maturity, not a defect.
5. **The standards layer is a real addition.** Delta-8's fleet-verification standard (the reproduction-mandate, the metadata-tiers, the report-isolation +43.4pp lesson) and delta-9's success-formula (the evidence-to-evidence loop) are new, reusable machinery — not churn for its own sake. The concern should not be read as "only process was produced."
6. **The study's own self-catches are honest.** The C1 corrections (IMP-1/6/7 struck on the 5-vs-6 miscount), the rungs 4-5 substance-check (the byte-identical fixtures named as RUNGS-REOPEN), the record's drift correction (`f084af11cf`) — the study catches its own errors and rows them. The concern is right that the *output* is thin; it is wrong if it reads the *honesty* as absent.

### 2.3 The calibration's verdict

The concern is **RIGHT about the arrival gap** (the four lines staged, the decisive experiment unmeasured, the harness unbuilt, the PR thin) and **MISSING the gate's nature** (the wait is the user's word, not drift) and **MISSING the science that landed** (the measured gate FAIL, the seam-arc, the ladder, the fabric). The honest synthesis: the study has done the *measurement* and *staging* work well; it has done the *arrival* work not at all — and the arrival work is gated on the user's word plus one unbuilt harness. The concern is a correct reading of the *arrival* column and an incomplete reading of the *preparation* column.

---

## §3 — THE REFUTATION-TEST (what concrete evidence would settle the concern either way)

The test is stated in advance, with the evidence that would confirm the concern and the evidence that would refute it. Each row names the artifact and the exact flip.

### 3.1 The concern is CONFIRMED if, at the next shift's close:

1. **The four lines remain STAGED** — `NEXT-SHIFT-PLAN-20261107.md`'s standing frame still reads "the study's four lines stay STAGED," and no line's gate has been touched.
2. **The W2-isolation's verdict-line is still SEPARATION-UNMEASURED** — the `W2-ISOLATION-STATUS` has not flipped to SEPARATION-MEASURED or SEPARATION-REFUTED; the isolate re-run has not landed.
3. **The harness write-deadline passes unbuilt** — no receipt row exists for the isolate run; `run_eval.py:81`'s window stays CLOSED; no `run_eval` isolate invocation appears in the branch's log.
4. **The upstream-visible delta stays a docs PR** — PR #1's non-study delta remains the thin set (a handful of tests + the workflow + `.tmp-artifacts/`); no landed fix to any of the four lines appears.
5. **The machinery's marginal output stays zero** — a fifth ACES cycle names 0 improvements again; the branch's commit count since `653f535bfd` stays at zero.
6. **The walls census stays large** — `HONEST-WALLS-CENSUS-20261106.md`'s 40 markers (8/8/16/8) shows no material reduction; the GitHub-hosted window side stays NOT RUN; the recitation-length class stays NOT RUN.

### 3.2 The concern is REFUTED if, at the next shift's close:

1. **A line's gate is touched or crossed** — one of the four lines moves from STAGED to LANDED: the restore's #141876 lands in an installed build, or the network's #116673 break-glass gate opens (the installed build gains `read`), or the governance's #139606 fold-drafts post upstream, or the compaction's #140008 fix-spec becomes a landed fix.
2. **The W2-isolation's verdict-line flips** — the `W2-ISOLATION-STATUS` reads SEPARATION-MEASURED (the confound is liftable) or SEPARATION-REFUTED (the confound is real and named); the isolate re-run's result file is on the branch.
3. **The harness is built and the window opens** — a receipt row for the isolate run exists; `run_eval.py:81`'s window is OPEN; the eval-runtime executes the isolate re-run.
4. **The upstream-visible delta gains a landed fix** — PR #1's non-study delta includes a substantive code change to one of the four lines, not only tests/docs/workflows.
5. **The machinery names a real, landed improvement** — a fifth ACES cycle names a non-zero improvement that survives audit and lands as a commit; the branch's commit count since `653f535bfd` is non-zero.
6. **The walls census shrinks materially** — the 40 markers reduce by a named count; the GitHub-hosted window side lands a receipt; the recitation-length class's prevalence table lands.

### 3.3 The test's binding form

The concern is settled by **the W2-isolation's verdict-line** — it is the single most decisive flip, because it is the one experiment whose result would either lift the eval-window confound (converting the study's preparation into an arrival) or name it as the standing wall (converting the study's waiting into a measured limit). The four lines' staging is gated on the user's word, which is outside the study's control; the W2-isolation is gated on the harness, which is inside the study's control. **The concern is therefore refutable by the study alone, on the W2-isolation, and confirmable by the study alone, on the same.** Everything else in §3.1/§3.2 is secondary to that one flip.

---

## §4 — THE NEXT MECHANISM (the one advance that would convert the ledger)

The counter's own read of the ground names the next mechanism: **the W2-isolation's harness build** — the minimal artifact that opens the eval-window and lets the isolate re-run land its separation verdict. It is the one advance that is (a) inside the study's control, (b) the binding constraint on the decisive experiment, and (c) the flip that would settle the user's concern. The mechanism's receipt: the harness's existence + the isolate run's result file + the `W2-ISOLATION-STATUS` verdict-line flipped from SEPARATION-UNMEASURED.

---

**Artifact:** `studies/rfc-143379-rig/HITL-GAINS-SKEPTIC-20261107.md`. **Branch:** `study/rfc-143379-rig-20261105`. **Gate:** fork-only; nothing public without the user's word. **Seat:** `meituan/longcat-2.5:free`. **Register:** receipts, never claims.