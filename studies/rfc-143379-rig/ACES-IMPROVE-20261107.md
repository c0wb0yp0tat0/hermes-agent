# ACES-IMPROVE-20261107 — the IMPROVE-PASS ledger on PR #1 (2026-11-07)

**Seat:** `stealth/crouton-alpha` (the alpha; probed live 01:34). **Lane:** copycat lane, leg 1 — THE IMPROVE-PASS. **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the PR). **Register:** receipts, never claims — each named improvement carries commit/row id + quoted bytes. **Do NOT fix:** the improve-pass names; the audit verifies; the review composes. **Round-budget:** 40.

**Ground (cold-read):** branch `git log --oneline ebd83ba508..HEAD` (8 landings, 2026-11-06→11-07) + artifacts named by those commits. Thread ground (`gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments`) was briefed as ground but no `gh` tool is available in this lane's toolset (git/read/write only) — improvements below are receipted to branch commits/files, not thread row-ids; the audit leg must close the thread-row receipt gap.

---

## CLASS-COUNTS

| Class | Count |
|---|---|
| Landings cold-read (branch commits since `ebd83ba508`) | **8** |
| Named improvements (numbered IMP-1…) | **14** |
| Seams (numbered SEAM-1…) | **7** |
| Corrections (claim contradicted by a later landing's bytes) | 3 |
| Sharpenings (claim true but loose/underspecified) | 7 |
| Additions (a gap a landing revealed and no predecessor named) | 4 |

The 8 landings: `3ba8998840` PLAN · `9285c866af` AUDIT · `c54c1bc614` AOA · `d760fcae90` W2-RUN-DESIGN · `173540a7b9` ADVANCE-D · `0f0d7f1183` ADVANCE-B · `7b994549d9` ADVANCE-C · `5fdf311069` APEX-OF-APEXES.

---

## THE LEDGER — claim → improvement → receipt

### Landing 1 — NEXT-SHIFT-PLAN-20261107 (`3ba8998840`)

| # | The landing's claim | The improvement named | Receipt (quoted bytes) |
|---|---|---|---|
| IMP-1 (SEAM-1, addition) | §1 THE GOALS carries rows 1–5: D re-fire, swap-rotations, matrix/Avrea/feed-back, citation-tests, free-tier hunt — presented as the shift's measurable outcomes. | **Restore the 6th arm to the goals table:** the 3-of-7 sessions messages-timestamps re-check (PARTIAL close) is a handoff arm with no goal row, no settle-condition, no closing receipt. Add row 6 or state its explicit deferral. | Plan §1 rows 1–5 vs handoff PART2 "six arms: 1 D's bounded-skeleton re-fire · 2 swap-rotations · 3 matrix→Avrea→feed-back · 4 citation-tests · 5 free-tier hunt · 6 the 3-of-7 sessions re-check" — AoA spot-check A: `c54c1bc614` §2A "6 arms named in the handoff; 5 rows in the plan's" |
| IMP-2 (SEAM-2, sharpening) | "the Avrea runner's ultimate process runs at pinned head" — head invoked, hex not stated. | **Pin the exact HEAD hex** in the feed-back row (liveness edge: local head ≠ remote head is lesson-10 class). | Audit `9285c866af` §1 row 3: `"pinned head" is invoked but the plan does not state *which* head — the liveness edge (local head ≠ remote head) is the class of the handoff's lesson 10` |
| IMP-3 (sharpening) | Fleet/seat frame: "Seat: `meituan/longcat-2.5:free`" for the plan lane while §0 re-apex says apex-roles ride the flagship `reflection/beam-1.0-501b-a23b:free`. | **Disambiguate seat vs apex-role designation** — the plan's own seat is a volume-quartet seat, not the flagship; later landings re-seat to flagship/alpha. State per-lane seat explicitly so the audit's seat-check does not misread it. | Plan header `Seat: meituan/longcat-2.5:free` vs §0 `every apex-role rides the free flagship reflection/beam-1.0-501b-a23b:free`; APEX `5fdf311069` re-seats: `the alpha as the common denominator on every leg, the flagship carrying the apex-ROLES` |

### Landing 2 — NEXT-SHIFT-PLAN-AUDIT-20261107 (`9285c866af`, RUN 2 re-fire)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-4 (SEAM-3, sharpening) | Rotation goal CONFIRMED; trigger = "D's landing". | **Name which D-verdict fires the ledger:** SEPARATION-MEASURED vs SEPARATION-REFUTED yields different rotation columns — the ledger's table-header must carry the D-verdict condition, not just "D's landing". | Audit `9285c866af` §1 row 2: `the brief says "the trigger = D's landing". The plan must pin *which* landed verdict fires the ledger — SEPARATION-MEASURED vs SEPARATION-REFUTED yields different rotation columns. Fix: a one-line table-header row naming the D-verdict condition` |
| IMP-5 (sharpening) | W2 confound "either lifted from V or named as the standing wall". | **Sharpen to an either/or with a named wall-id:** lift = verdict-line flip on W2-ISOLATION-STATUS; named = cite the wall (W2) explicitly, so "named" is not an unverifiable prose act. | Audit commit msg `9285c866af`: `one sharpening (W2 confound either/or)`; Audit §1 row 1: `the W2-empty-answer confound is either lifted from V or named as the standing wall` |
| IMP-6 (addition — audit's own gap) | Overall READY-FOR-THE-NEXT; two seams + one sharpening logged. | **The audit missed the arm-count gap (IMP-1).** Its row-by-row check inherited the plan's 5-row frame and never reconciled against the handoff's 6 arms. Improvement for the audit method: every goal-table audit must first reconcile row-count against the source's arm list. | AoA `c54c1bc614` §0: `find one GAP the audit missed — the handoff names six next-session arms while the plan's §1 goal table carries five, dropping the 3-of-7 sessions re-check` |

### Landing 3 — NEXT-SHIFT-PLAN-AOA-20261107 (`c54c1bc614`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-7 (SEAM-4, correction) | "vote READY-FOR-THE-NEXT with the seams logged, not blocking"; CTO check COMPLETE-WITH-SEAMS. | **READY must be conditional on IMP-1's row-6 disposition** — a missing measurable goal is not a logged seam, it is an unmeasurable arm; the vote should read READY-ON-ROW-6-DISPOSITION or carry the deferral explicitly, else the next shift inherits an untracked arm. | AoA `c54c1bc614` §0: `the CTO completeness check reads COMPLETE-WITH-SEAMS (goals measurable, doors mostly pinned, state carried in §0 + handoff reference); vote READY-FOR-THE-NEXT with the seams logged, not blocking` |
| IMP-8 (sharpening) | PR-UPDATE envelope text delivered "for the head to post (the harness cannot post)". | **Close the posting loop:** the improvement is a receipt that the head actually posted it (thread row-id), or the text remains an unlanded potential. Name the ack-mechanism, not just the delivery. | AoA `c54c1bc614` §0: `the PR-UPDATE envelope text is delivered below for the head to post` |

### Landing 4 — W2-ISOLATION-RUN-DESIGN-20261107 (`d760fcae90`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-9 (SEAM-5, sharpening) | Pin `c54c1bc614f20bd5e603a4826dc5c80a670a654a`; empties re-derived 2/5/4; window CLOSED (`run_eval.py:81` keys on `api_key`/`base_url`). | **Pin must be re-verified at fire-time, not just at design-time** — the pin is the AoA commit, but ADVANCE-D and the rotations land after it; a stale pin silently re-baselines the experiment. Add a pin-refresh step as the re-fire's first commit (the audit already demands the exact verdict-line as first commit — extend to head-hex). | Run-design `d760fcae90` §2: `Pin: head c54c1bc614f20bd5e603a4826dc5c80a670a654a (study branch study/rfc-143379-rig-20261105, ls-remote-verified at 00:15 ET)`; §1: `eval-runtime LLM-window CLOSED` |
| IMP-10 (sharpening) | Expected-verdict matrix CONFIRMED/REFUTED/SEPARATION-UNMEASURED; REFUTED names "the probe-judge's empty-answer scoring path" as next candidate. | **Pre-register the REFUTED follow-up as its own runnable spec** (judge's empty-answer rule relaxed), so a REFUTED verdict does not strand the shift without a priced next step — the matrix currently prices only the H1 branch. | Run-design `d760fcae90` §4: `the design names the next isolation candidate: the probe-judge's empty-answer scoring path` |

### Landing 5 — SWAP-A-ADVANCE-D-20261106 (`173540a7b9`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-11 (SEAM-6, correction) | The probe-loop diff is quoted as "the exact quoted probe-loop shape (from the committed `run_eval.py` probe-loop)" and the 3-run command is given against `run_eval_config_no-guard.json`. | **Byte-verify the quoted diff against the committed `run_eval.py` and land the config file** — the quoted shape is presentational code (`load_handoff_preamble()`), not shown as a `git diff` against the actual file; and the config JSON the command-line requires does not exist on the branch yet. A runnable spec must ship both bytes, or the re-fire improvises them (the exact failure the spec exists to prevent). | ADVANCE-D `173540a7b9` §2: `Exact quoted probe-loop shape (from the committed run_eval.py probe-loop):` + `if runtime.get("api_key") and runtime.get("base_url"): system_preamble = load_handoff_preamble()`; §3: `--config run_eval_config_no-guard.json --label "W2-NoGuard-run1"` (no such file in the advance's stat) |

### Landing 6 — SWAP-A-ADVANCE-B-20261106 (`0f0d7f1183`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-12 (sharpening) | Two-tier seam: high-keep ≥0.60 (observed 0.75) vs low-keep 0.26–0.42 (observed 0.29); "the refinement CHANGES the single-number presentment but CONFIRMS the flat-class ordering". | **Reconcile the tier numbers against the neighbours in the same table** — the low tier is quoted as 0.26–0.42 with observed 0.29, while the run-design's W2 tier is 0.29 and ADVANCE-C reads the k-term as flat 0.26–0.42; the seam's numbers must be presented as one canonical table (per-probe k_p, n, presence-bytes) shared by B, C, and the run-design, or each leg's "observed" drifts. | ADVANCE-B `0f0d7f1183` §1: `high-keep tier (≥ 0.60) … low-keep tier (0.26–0.42) … observed 0.75 … observed 0.29`; run-design §2: `empty-answer-suppressed (W2) probes keep at 0.29` |

### Landing 7 — SWAP-A-ADVANCE-C-20261106 (`7b994549d9`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-13 (SEAM-7, correction) | MINIMUM-RESERVE = decision-core (weight 3.00 > 2.83 > 2.33 > 2.00), necessary-but-not-sufficient; sufficiency complement = next-action/forward-intents block; mechanism-caveat: weight is descriptive, k-term flat (Wall W5). | **State the falsifier as a priced experiment, not a caveat** — the rule rests on loss-geometry + generative-root (W7) while the mechanism (differential keep-rates) is contradicted by the flat k-term; the improvement is the named measurement that would promote the rule from descriptive to mechanistic (or retire it), with the exact k_p split that would settle it. The commit msg says "the falsifier stated in advance" — the falsifier must be findable as one line, not distributed across §1–§2. | ADVANCE-C `7b994549d9` §1: `The priority-order is descriptive (loss-geometry), not mechanistic: the k-term does NOT separate the classes — kept-rates are flat 0.26–0.42 across the four classes`; §0: `the falsifier stated in advance` |

### Landing 8 — APEX-OF-APEXES-20261107 (`5fdf311069`)

| # | The landing's claim | The improvement named | Receipt |
|---|---|---|---|
| IMP-14 (addition) | Six movements in fire-order; "leg D = pending on the same rotation"; read-burn seam named. | **Correct the leg-D status line and price the read-burn seam:** leg D has already landed as a runnable spec (`173540a7b9`), so the apex's "pending" is stale at its own head — re-designate D as landed-awaiting-window. And the read-burn seam (the score's self-named risk) needs its settle-condition (a read-budget per leg, or the seam is decorative). | APEX `5fdf311069` ground-read: `leg D = pending on the same rotation` vs ADVANCE-D `173540a7b9` (already on branch at APEX's head); APEX commit msg: `six movements, read-burn seam` |

---

## SEAMS (consolidated — the 7 the landings revealed)

| Seam | What joins badly | Revealed by |
|---|---|---|
| SEAM-1 | Handoff's 6 arms vs plan's 5 goal rows (IMP-1) | AoA `c54c1bc614` §2A |
| SEAM-2 | "Pinned head" without a hex (IMP-2) | Audit `9285c866af` §1 row 3 |
| SEAM-3 | Rotation trigger without a named D-verdict (IMP-4) | Audit `9285c866af` §1 row 2 |
| SEAM-4 | READY vote on a missing measurable goal (IMP-7) | AoA `c54c1bc614` §0 |
| SEAM-5 | Design-time pin vs fire-time head (IMP-9) | Run-design `d760fcae90` §2 + ADVANCE-D landing after it |
| SEAM-6 | Quoted diff + missing config ≠ runnable bytes (IMP-11) | ADVANCE-D `173540a7b9` §2–§3 |
| SEAM-7 | Descriptive weight vs flat mechanism (IMP-13) | ADVANCE-C `7b994549d9` §1 |

**The through-line the ledger names:** every seam is a *pinning* failure — an arm without a row, a head without a hex, a trigger without a verdict-name, a diff without bytes, a weight without a mechanism. The night's prose is strong; its receipts are one pin short at each joint. The audit leg verifies each IMP against the bytes; the review composes the fixes. **Nothing here is fixed — by design.**

---

NEXT-LAUNCH: stealth/crouton-alpha || /root/.hermes/cache/scratch/pr1-rotation/briefs/aces-audit-brief-20261107.md || /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/ACES-AUDIT-20261107.md || 40 || /root/.hermes/cache/scratch/copycat-mission/aces-audit-20261107-run.log
