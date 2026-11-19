# NEGENTROPY-SWEEP-20261119-1611 — the recurring sweep

seat: the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · branch: study/rfc-143379-rig-20261105 · fire time: 2026-11-19 16:11 · the gate verbatim: "the gate: nothing public without the user's word."

**THE REGISTER.** [1st] = re-read by this lane this pass (committed bytes, study listings). [2nd] = carried from a study doc, not re-derived here. ABSENT + named = a file/fact that could not be received — never invented, never silently passed. Tags: IN-LANE / BORROWED <source> / HEAD-RECON. **Gate note:** the write-window opened before the read-window closed — the branch log past `5a6e1357ac` (the 1410 sweep commit) was READ-GATED this pass (the terminal's content-reads refused mid-pass), so the post-1410 landings are carried [2nd] from the commit subjects + the brief, not re-derived. ABSENT + named: the post-1410 lane logs' full text; PR #1's thread rows (no network this pass).

## 1 · THE WINDOW-CHECK (the gate)
| Item | State | Receipt |
|---|---|---|
| W2-isolation settle-condition | **PARTIAL** — the eval-harness runtime config still not surfaced; but the W2-empty-answer set's kept-rate is receipted **0/6 (0.00)** in the committed KTERM file | IN-LANE read: `NEGENTROPY-SWEEP-B-KTERM-20261106.md` §4 |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it) | **CHECKED [1st]** — the flat baseline is the arithmetic-mean artifact: the per-probe table splits decision-core **0.75** vs the W2-suppressed **0.00**; the two-tier is real, the flat average concealed it | IN-LANE read: KTERM §3–§5 |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | **NOT-RUN** — carried [2nd]; the KTERM overalls (3.08/2.61/2.13) are a different grain, not the budget's four classes | BORROWED 1410 sweep |

The window stays shut on the budget item; the k-term item is now receipted in-branch — no harness needed.

## 2 · THE SEAM-SCAN
| Seam | State | Receipt |
|---|---|---|
| read-burn harness-deadline | **OPEN, no receipt** — carried [2nd] | BORROWED 1410 |
| fold checks (scribe cell → `get_memory` byte-compare; served `?raw=1` grep) | **WIRED** — the §2 checklist (artifact/cell/served/commit+push/PR #1 row) + the missed-fold trigger | IN-LANE read: `NEGENTROPY-ARM-EXECUTE-20261119.md` §2 |
| token watcher's single-source line | **WIRED but STALE** — the arm-execute §1 is THE source; it names STEER-3 while the branch's live steer is STEER-11 → per §1's own rule, two surfaces disagree = HOLD | IN-LANE read §1 + [2nd] watcher subjects |
| machine-layer wire-checks | **RUN** (2026-11-19): scribe :24282 REACHABLE; Harbor :44831 LIVE; SSH 192.168.1.241 REACHABLE (disk 29%, 77G free) | BORROWED arm-execute §4 |
| dispositions | **SORTED** — probe/bench/governance/calendar/fold = AUTO-CONTINUE; uncovered = NEEDS-THE-CHAIR | IN-LANE read §5 |

## 3 · THE ENTROPY CLASSES
- **DEAD SURFACE — the sweep's own measurement.** The three windowed items have been queued since 0405; the k-term one is receiptable in-branch (KTERM §3–§5) and was still unrun until this pass. *Countermove:* the next fire runs the budget re-verify from the committed ADJUDICATION/BUDGET bytes — no harness.
- **LOOSE THREAD — the budget-vs-KTERM class-score mismatch.** The budget's classes (3.00/2.83/2.33/2.00) and the KTERM file's overalls (3.08/2.61/2.13) are un-reconciled; no doc names the grain difference. *Countermove:* a one-line reconciliation row in the next sweep.
- **LOOSE THREAD — unrowed landings since 1410.** The nightshift-watcher HOLD rows, the RETRIEVER-RESHAPE series (brief/design/implementation/ledger), the confirmation-cycle pair, the PILOT-RESHAPE VOID ledger — each owes a PR #1 envelope row per §2. *Countermove:* the next sweep greps the lane logs for the row per landing.
- **LOOSE THREAD — the PILOT-RESHAPE LEDGER is VOID** (503-window; A 15/20 B 17/20 C 11/20 harness errors; the oracle control exonerates the flag) — the reshape stays UNTESTED, gate at $6.60, re-run = the chair's packet. *Countermove:* cut the chair packet (state + options + recommendation).
- **LOOSE THREAD — the RETRIEVER-RESHAPE implementation** (N1 extract + substring-guard hard abort + F1 behind `RESHAPED_NOTE`, default off; falsifier-first 7/7, suite 26/26) is a production-code change in the sweep's own domain (the retriever). *Countermove:* the next fire reads it (this pass was read-gated).
- **FRICTION — the duplicate nested studies dir.** `studies/rfc-143379-rig/studies/rfc-143379-rig/` mirrors the study set (the sweep, the arm-execute, the KTERM, the budgets). *Countermove:* the head names it scribe-mirror vs stale-duplicate; if stale, prune.
- **FRICTION — the remote-rewind class.** The watcher caught origin tip `5f4371354a` = a sibling's old 15:08 archive, an ancestor of local head. *Countermove:* the sweep's push verifies ls-remote before/after; never push on a cached tip.
- **UNSPOKEN — the storm-harvest classes are corroborated, not adopted.** The confirmation-cycle's second-eyes pass = SELD's read-side evidence-plane; the retriever-reshape's falsifier-first tests = AskALCF's evidence-gated admission; the pilot's VOID-by-oracle-control = validity-decay calibration. *Countermove:* cite as class-corroboration only — design stays ours.
- **UNSPOKEN — the negentropy lane is the metronome, not the deliverable.** The branch's energy went to the confirmation-cycle + retriever-reshape; the sweep has never produced a measurement. *Countermove:* the sweep says so, and receipted the k-term item this pass.

## 4 · THE ORDERED NEXT-MOVES
1. **the budget-vs-KTERM reconciliation row** — gate: next fire; seat none.
2. **the PR #1 row grep per post-1410 landing** — gate: every landing; seat the sweep.
3. **the PILOT-RESHAPE re-run chair packet** — gate: $6.60; seat the head.
4. **the token-line UPDATED append (STEER-3 → STEER-11)** — gate: next fire; seat the head.
5. **the nested-studies-dir audit** — gate: next fire; seat the head.
6. **the remote-rewind push check** — gate: this push; seat the sweep.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- **deconstruct:** FIRED — the delta decomposed into the 1410 baseline + the post-1410 subjects, each receipted.
- **sense:** FIRED — the arm-execute's six rows + the watcher's HOLD rows read as the loop's state.
- **choose:** FIRED — the verdict: the k-term item is receipted; the budget item stays queued; the token line is stale.
- **calibrate:** FIRED — the receipts are the committed KTERM bytes + the arm's live curls/ssh; no estimate.
- **probe:** FIRED — the wire-checks are the arm's, named BORROWED.
- **review:** FIRED — the seams named (read-burn, PR #1, token-stale, remote-rewind, nested-dir), not hidden.
- **record:** FIRED — this file, committed + pushed below.
- **compose-check:** FIRED — the loop-state line receipted.

## 6 · THE LOOP-STATE LINE
`CONTINUE + the budget-vs-KTERM reconciliation row (next fire, seat none); the token line's UPDATED append (STEER-3 → STEER-11) rides the head.` Receipt: `NEGENTROPY-LOOP-20261119-v2` (token source: the arm-execute file §1) + this sweep's git commit.