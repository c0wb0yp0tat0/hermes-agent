# NEGENTROPY-SWEEP-20261119-1410 — the recurring sweep

seat: the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · branch: study/rfc-143379-rig-20261105 · fire time: 2026-11-19 14:10 · the gate verbatim: "the gate: nothing public without the user's word."

**THE REGISTER.** [1st] = re-read by this lane this pass (git-tree bytes, study listings, branch logs). [2nd] = carried from a study doc, not re-derived here. ABSENT + named = a file/fact that could not be received — never invented, never silently passed. Tags: IN-LANE / BORROWED <source> / HEAD-RECON. **Gate note:** the write-window opened before the read-window closed — the 0405 sweep artifact and `SPRINT-FIRE-SEQUENCE-20261119.md` were READ-GATED this pass, so they are carried [2nd] from the brief + the branch log, not re-read. ABSENT + named: the 0405 artifact's full text; the sprint fire-sequence body; PR #1's thread rows (no network this pass).

## 1 · THE WINDOW-CHECK (the gate)
| Item | State | Receipt |
|---|---|---|
| W2-isolation settle-condition | **NOT-RUN** — no receipt in the 65-commit delta that the eval-harness runtime config surfaced; the delta's probes are the battery leg (`probes/BATTERY-*.json`), a different surface | IN-LANE: `git rev-list --count dc233806c1..HEAD` = 65; `git ls-files` |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it) | **NOT-RUN** — carried [2nd]; the contradiction stands | BORROWED 0405 sweep (via brief) |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | **NOT-RUN** — carried [2nd] | BORROWED 0405 sweep (via brief) |

The window is shut: the three measurements stay queued; the sweep does not fake a measurement.

## 2 · THE SEAM-SCAN
| Seam | State | Receipt |
|---|---|---|
| read-burn harness-deadline | **OPEN, no receipt** — carried [2nd]; the delta names no harness-deadline config | BORROWED 0405 |
| fold checks (scribe cell → `get_memory` byte-compare; served `?raw=1` grep) | **WIRED** — checklist (artifact / cell / served / commit+push / PR #1 envelope row) + the missed-fold trigger | IN-LANE read: `NEGENTROPY-ARM-EXECUTE-20261119.md` §2 |
| token watcher's single-source line | **WIRED** — the arm-execute file §1 is THE source; token `NEGENTROPY-LOOP-20261119-v2`; two surfaces naming different stages = HOLD | IN-LANE read §1 |
| machine-layer wire-checks | **RUN** (2026-11-19, the arm's live receipts): scribe :24282 REACHABLE; Harbor :44831 LIVE; SSH 192.168.1.241 REACHABLE (disk 29%, 77G free) | BORROWED `NEGENTROPY-ARM-EXECUTE` §4 |
| dispositions | **SORTED** — probe / bench / governance / calendar / fold = AUTO-CONTINUE; uncovered = NEEDS-THE-CHAIR | IN-LANE read §5 |

## 3 · THE ENTROPY CLASSES
- **DEAD SURFACE — the sweep's own cadence.** 0405 was sensor-only and the recurring brief lived untracked in scratch and was LOST; the branch ran a full sprint (65 commits) while the sweep went dark. *Countermove:* the brief is now repo-tracked (`624e8d31f9`) and the cron arm restores it — the dead surface is closed; this artifact is the proof.
- **LOOSE THREAD — unrowed landings.** The delta's landings (SPRINT F1b–F7, LUNA FIRE, CTO-LENS, RELOAD) each owe a PR #1 envelope row per §2; PR #1 is ABSENT + named (no network this pass). *Countermove:* the next sweep greps the lane logs for the PR #1 row per landing.
- **LOOSE THREAD — the OPUS-2 plan set.** PLAN-A..H briefs + records + ENVELOPE (17 files) are cut; the arm-execute's dispositions name probe/bench/governance/calendar, not the OPUS-2 set. *Countermove:* the next sweep marks each OPUS-2 plan dispatched / undispatched.
- **LOOSE THREAD — brief/record pairs.** `NEGENTROPY-ARM-EXECUTE-20261119-brief.md` sits beside its record; `NEMO-NEGENTROPY-ARM-20261119-brief.md` beside the PLAN. *Countermove:* named, no action — brief = the ask, record = the receipt; the pair is the norm.
- **FRICTION — the seat-envelope quirk.** Nemo's STAGE-2 ride aborted on the seat's JSON-envelope quirk; the base-swap doctrine rides the frame on the seat that carries it. *Countermove:* named, pre-armed (never retry the same lane).
- **FRICTION — the Nov-20 Cloudflare deprecation (tomorrow).** The deprecated set (kimi-k2.6 / glm-5.2 / deepseek-v4-flash-0731) is confirmed live. *Countermove:* no new legs to the deprecated set after 2026-11-20; re-survey at dispatch.
- **UNSPOKEN — the negentropy lane is the metronome, not the deliverable.** The branch's energy went to the sprint's battery (F4-FULL: A 0/200, B 200/200, C…); the sweep has never produced a measurement. *Countermove:* the sweep says so, and queues the three windowed measurements as the loop's own deliverable.
- **UNSPOKEN — the storm-harvest classes are corroborated, not adopted.** The battery's arms are the MAPE design-space search; the fold's served-verify is the SELD read-side evidence-plane; the bench door's three-state trigger is the three-state delegation; the commit gate is AskALCF's evidence-gated admission. *Countermove:* cite as class-corroboration only — design stays ours.

## 4 · THE ORDERED NEXT-MOVES
1. **the fire's hold-audit** — Nemo re-dispatch per STEER-3, ground = `NEGENTROPY-ARM-EXECUTE-20261119.md`; gate = the token's next line; seat Nemo.
2. **the window's three measurements** — gate = the eval-harness runtime config surfaces; seat none.
3. **the PR #1 row grep per landing** — gate = every landing; seat the sweep.
4. **the OPUS-2 dispatch-state audit** — gate = next sweep; seat the head.
5. **the Nov-20 deprecation gate** — gate = 2026-11-20; seat the head / lane-2.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- **deconstruct:** FIRED — the delta decomposed into 65 commits + the tracked set, each receipted.
- **sense:** FIRED — the arm-execute's six rows read as the loop's state.
- **choose:** FIRED — the verdict: the window stays shut; the loop's next is the hold-audit.
- **calibrate:** FIRED — the receipts are the git log + the arm's live curls/ssh; no estimate.
- **probe:** FIRED — the wire-check results are the arm's, named BORROWED.
- **review:** FIRED — the seams named (read-burn, PR #1, OPUS-2, Nov-20), not hidden.
- **record:** FIRED — this file, committed + pushed below.
- **compose-check:** FIRED — the loop-state line receipted.

## 6 · THE LOOP-STATE LINE
`CONTINUE + the fire's hold-audit (Nemo re-dispatch per STEER-3, ground = NEGENTROPY-ARM-EXECUTE-20261119.md; the window's three measurements stay queued).` Receipt: `NEGENTROPY-LOOP-20261119-v2` (token source: the arm-execute file) + this sweep's git commit.