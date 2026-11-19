# MASTER-TEAM-M2-20261119.md — the M2 synchronization plan (2026-11-19)

Workbench for **M2 — THE ORCHESTRATION'S RESOURCE-TRUTH IS UNRELIABLE**. Verb: **synchronize**. Lens (LP M2-STAMPED): the orchestration schedules against imagined evergreen seats and disagreeing surfaces; Dive Deep + Deliver Results demand a true calendar and one trusted ledger. Target: zero window wasted by a misread calendar; zero coordination hang that survives a check-in. RFC QUIET.

## 0. The gate (verbatim, binding)
> "the gate: nothing public without the user's word." · RFC QUIET.
Internally every move is a two-way door (§6); externally nothing goes public/permanent until the user speaks.

## 1. Place in the sequence
Master step 2 — consumes M1's evidence, feeds M3's governance probes. Motion is planned against a TRUE calendar and ledger, never remembered seats.

## 2. THE WINDOW-CALENDAR LINE (a named row in EVERY mission plan)
Fleet truth (brief-sourced): seats are **windowed, never evergreen** — 00:00 UTC resets · 4-day offers · rotating rosters. The roster flipped between probes: earlier longcat+deepseek live / solar·hy4·stepfun·qwen4 walled; 2026-11-19 evening qwen4-max:free · hy4-flash · solar-mini4 · stepfun · longcat ALL live. **A wall at one moment is never a wall forever — re-survey at EVERY dispatch.** No plan fires on cached seat state.

Template (fill fresh at dispatch):
| seat | window_rule | reset_utc | fair_share_envelope | meter_class | last_confirmed | source | status |
|---|---|---|---|---|---|---|---|
| qwen4-max:free | 4-day flagship | 00:00 UTC | per-window share | actual-billed | dispatch | ls-remote | LIVE/WALLED/UNVERIFIED |
| hy4-flash | rotating | 00:00 UTC | per-window share | actual-billed | dispatch | ls-remote | … |
| solar-mini4 | rotating | 00:00 UTC | per-window share | actual-billed | dispatch | ls-remote | … |
| stepfun | rotating | 00:00 UTC | per-window share | actual-billed | dispatch | ls-remote | … |
| longcat | rotating | 00:00 UTC | per-window share | actual-billed | dispatch | ls-remote | … |
| runners | unmetered | n/a | n/a | unmetered | dispatch | process-tree | … |

Invariants: C1 dated-fact (last_confirmed + source; a row older than its window is stale/unfireable). C2 reset-first (read reset clock before the offer; post-00:00 = new window). C3 deprecation-gate (deprecation ≤ T+7 → frozen until re-survey). C4 no arithmetic theater: meter_class carries ONLY the operator's actual-billed class; cost truth is operator telemetry.

## 3. SEAT-SURVEY PROTOCOL (dispatch-time)
S1 availability is a dated fact, observed at dispatch not config. S2 read the LIVE surface, never the cached table. S3 429 from the record: on 429 → back off per recorded policy, mark hot, route to fallback, never retry blind; a cooled seat re-eligible only on fresh evidence. S4 dated tracker (date, source, seat, observation); undated = not evidence. S5 spot-offer triple (price, completion-probability, deadline): pick max completion within budget before deadline; fallback = 429 discipline.

## 4. THE SINGLE-SURFACE LEDGER (one surface per truth, read fresh at dispatch)
| truth | trusted surface | never trust | freshness | reconciles_to |
|---|---|---|---|---|
| what landed | **ls-remote** before every landing | tracking ref / cached table | at landing | commit record |
| what runs | **process-tree** | spawn-counts / remembered count | at check-in | run log |
| watcher intent | **watcher tokens** | token without a landing | at check-in | commit record |

A landing is recorded only when these three agree with the record. A disagreeing surface is a Dive Deep event — logged same day with its fix, never smoothed over.

## 5. TRACKING-REF STALENESS CLASS + FIX
Class: shared-branch write collision. The sibling archiver SHARES this branch; watcher MISSION-MAP rows land as their own commits; lanes fold artifacts — three writers, one branch. A tracking ref (`origin/<branch>`) is a cache of a past observation: a plain `fetch <remote> <branch>` writes FETCH_HEAD and never updates the tracking ref (needs the `+refs/heads/…:refs/remotes/…` refspec). Landing on a stale tracking ref = surfaces disagree about what landed.
FIX (two-writer policy per landing): **ls-remote truth before every landing**; pull --rebase onto the live tip; watcher rows stay on MISSION-MAP; the second landing waits for the first; record parentage. A rebased landing keeps both chains, destroys nothing.

## 6. Two-way doors on every move
calendar-line → config overlay, restore prior table. Ledger rule → dispatcher flag, revert to cached mode. Survey cadence → scheduled job, cancel. Landing → rebase/rollback, last good state is the record (rebase on push rejection, never force). public→private → the gate; revoke re-arms to last private value. cost → actual-billed cap; over-cap records COST-OVER, no re-plan without the word.

## 7. Compose-check (8 steps, FIRED/ABSENT, one evidence line each)
| # | Step | State | Evidence line |
|---|---|---|---|
|1| calendar line in every mission plan | FIRED/ABSENT | reset clock, fair-share envelope, meter class per seat |
|2| seat re-survey at every dispatch | FIRED/ABSENT | dated tracker + live-surface reads |
|3| ls-remote truth before every landing | FIRED/ABSENT | pre-landing ls-remote vs commit record |
|4| process-tree over spawn-counts | FIRED/ABSENT | live processes vs dispatcher count |
|5| watcher tokens reconciled to record | FIRED/ABSENT | token↔landing pairs, no orphans |
|6| tracking-ref staleness fixed | FIRED/ABSENT | two-writer receipt, parentage on rebase |
|7| cost in actual-billed class only | FIRED/ABSENT | telemetry only, no invented rows |
|8| two-way door + gate on every move | FIRED/ABSENT | reversibility named, nothing public without the word |

## 8. Loop-closing + standing harvest
Review-loop: draft → stranger re-read (the disagreeing surfaces) → one refinement per finding → adversarial pushback ("you assumed evergreen" → §2/3; "you guessed limits" → UNVERIFIED, not inferred) → no-change re-read. Wall clause: the gate is a question, not a stop — fire the scaffold, leave unread cells UNVERIFIED. Harvest considered: DISCERN write-gate L0 (written, not posted) + SPA-DREAM read path · MemCredit ρ=(V−λH)/b (stale rows spent, fresh banked) · MAPE (matching = design space, survey = inventions-live probe) · CoMem L2 · Reward-Driven Collider AIMD (cadence: additive on stability, multiplicative cut on shock) · AskALCF evidence-gated admission · SELD read-side verifier · Evolving Infra agent-adaptive serving · four misc (compile-time UNVERIFIED / stage-decoupled calendar vs dispatch / validity decay / three-state LIVE·UNVERIFIED·WALLED).

## 9. Fold for the master's §7
M2's label is fixed: **the orchestration's resource-truth is unreliable** — windowed seats scheduled as evergreen and surfaces that disagree about what landed. Synchronization = a named calendar-line row per seat + one trusted ledger per truth, re-surveyed every dispatch: zero window wasted by a misread calendar; zero coordination hang that survives a check-in. Next leg: M3's governance probes; until M2 ships, motion is planned on imagined seats.
