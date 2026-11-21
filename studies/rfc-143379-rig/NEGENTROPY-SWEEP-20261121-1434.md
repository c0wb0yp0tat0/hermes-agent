# NEGENTROPY-SWEEP-20261121-1434

**seat** · the copycat lane of the recurring negentropy-sweep (the scheduled sweep's harness ride, cadence 2h, no_agent arm)
**branch** · study/rfc-143379-rig-20261105 @ 73435bea2b (HEAD this pass)
**fire time** · 2026-11-21 14:34 UTC
**the gate** · "the gate: nothing public without the user's word."
**the register** · [1st] re-read this pass: the map tail (`NIGHTSHIFT-STATE-MAP-20261121.md`), `NIGHTSHIFT-PLAN-20261118.md` line 83, `probes/A3-BP-A-PLAIN-QWEN4-20261121.json`, git ls-files/log/status. [2nd] carried: the prior sweep's verdict/findings (via the map's rows — its own artifact is ABSENT), the arming record. **ABSENT + named**: `probes/BATTERY-FULL-LEDGER-20261119.json` (the k-term re-measure's surface), `NEGENTROPY-SWEEP-20261123-1233.md` (the prior sweep artifact — the map's name is date-ahead of this fire, a mis-receipt or a future-scheduled sweep). Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)

| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT RUN — gated | IN-LANE: the map's rows carry the arm record (APEX-ISOLATION + L1-STEP4-JUDGE-LIVE); the settle is the isolated L1 step-4 judge. No new measurement; the gate (user word) holds. |
| k-term two-tier re-measure | NOT RUN — surface ABSENT | IN-LANE: the ledger `probes/BATTERY-FULL-LEDGER-20261119.json` is gone at HEAD (read_file: No such file; deleted in 501f7d6f14). The named successor `probes/A3-BP-A-PLAIN-QWEN4-20261121.json` exists (467 lines) but is a dry-run battery_luna receipt — arms A/B/C, verdict INCONCLUSIVE, "dry-run machinery receipt, NOT the leg's verdict" — it carries no kept-rate structure. The prior sweep's next-move #1 (byte-verify the successor or restore the ledger) is UNFULFILLED. Baseline carried [2nd]: kept-rates 0.42/0.29/0.26/0.26 spanned 0.26–0.42, flat. |
| budget consolidation re-verify | NOT RUN — no new measurement | BORROWED <1032/1233>: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. Carried. |

## 2. THE SEAM-SCAN (every fire)

| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | LIVE | IN-LANE: this pass hit the write-gate — read-tools and terminal content-reads refused intermittently (a combined terminal command refused; the prior sweep artifact read returned ABSENT). The SIGKILL-at-3.5h class stands; the write-window is the bound. |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | PARTIAL | IN-LANE: every read_file this pass returned page metadata `source: scribe-cell` — the scribe cell serves the reads. The byte-compare itself NOT RUN (no terminal content-read). |
| token watcher single-source line | BROKEN — 3→4 surfaces | IN-LANE: map line 35 (`NIGHTSHIFT-STAGE-4 … APEX HOLD`) and `NIGHTSHIFT-PLAN-20261118.md` line 83 (`CONFIRMATION-ARMED … the apex hold`) both carry the OLD apex-hold tokens, closed by the pair's fire 2026-11-20 per the map's own rows; the arming record §1 writes the pair off but the surfaces persist. AND the registry fragmented: `SCRIBE-WITNESS-REGISTRY.log` now sits at top-level + `court/` + `probes/` (3 in HEAD) + `audit/` (untracked) = 4 surfaces. |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT RUN | BORROWED <map rows>: the last receipts are the Harbor/local-LM folds; the terminal content-reads refused this pass. |
| dispositions | AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR | IN-LANE: AUTO-CONTINUE the audit legs' folds (the tree's untracked `audit/*`); HOLD-SAFE the W2-isolation + k-term (blocked); NEEDS-THE-CHAIR the W2 settle (the gate). |

## 3. THE ENTROPY CLASSES (CTO freedom applies)

**dead surface.** The k-term ledger is deleted and its named successor is a different instrument (a dry-run battery, not the kept-rate ledger). The re-measure's surface is effectively unnamed. *Countermove:* restore `probes/BATTERY-FULL-LEDGER-20261119.json` from git history (it existed at 9c4e4181a5) or re-run the two-tier with the same schema; name the surface.

**loose thread — the sweep's own chain is broken.** The prior sweep artifact `NEGENTROPY-SWEEP-20261123-1233.md` is ABSENT from HEAD; the map's rows are now the sweep's only receipt. The recurring lane's own landing is unrowed. *Countermove:* commit the sweep artifact (this one) and fold the prior verdict in from the map's rows (done here).

**loose thread — the registry fragmented.** Four `SCRIBE-WITNESS-REGISTRY.log` surfaces (top-level, `court/`, `probes/`, `audit/`). The single-source line the 1032/1233 named is now a multi-source drift. *Countermove:* one registry; the others written off or symlinked.

**loose thread — the audit fleet's in-flight files.** Untracked: `audit/BRIEF-GOAL-VERDICT.md`, `audit/BRIEF-LEG5-CROSSCHECK.md`, `audit/SCRIBE-WITNESS-REGISTRY.log`. The prior sweep's "clean tree" receipt is stale. *Countermove:* the GOAL-AUDIT/HARNESS-FOLD legs land them; the tree is not clean.

**stale artifact / superseded brief.** `NIGHTSHIFT-PLAN-20261118.md` line 83's apex-hold token is superseded by the pair's fire. *Countermove:* strike or write off the line; the arming record §1 claims to, the surface persists.

**orphan sentinel.** The map's line 35 token (`APEX HOLD`). Same countermove.

**friction point.** The read-burn/write-gate: the lane cannot run the fold byte-compare. *Countermove:* the scribe-cell read path (it served every read this pass).

**UNSPOKEN.** The window-check's two gated items (W2-isolation, budget) can never close under "nothing public without the user's word" — they are sentinels to report, not tasks to run. Only the k-term re-measure is ungated (a read-side measurement) and it is blocked solely by the missing surface. The sweep should re-class the gated pair as sentinels and spend its motion on the k-term. *Countermove:* re-class + restore the ledger.

**UNSPOKEN (the prize).** The prior sweep's next-move #1 named the successor as the k-term's replacement and called it "unverified" — but the successor is a dry-run battery, not the ledger. The naming itself was a mis-mapping; the re-measure's surface was never actually named. The sweep's "next move" has been pointing at the wrong file. *Countermove:* name the surface by its schema (kept-rates), not by its filename.

## 4. THE ORDERED NEXT-MOVES

1. **Restore the k-term ledger** — `git show 9c4e4181a5:…/BATTERY-FULL-LEDGER-20261119.json` (or re-run the two-tier). *Gate:* the kept-rate structure byte-present. *Seat:* this lane.
2. **Land the prior sweep's verdict** — fold it into the branch. *Gate:* the artifact exists at HEAD. *Seat:* this lane / the head.
3. **Write off the two stale apex-hold tokens** (map line 35, plan line 83). *Gate:* one loop-state source. *Seat:* the head / the arm.
4. **Consolidate the four registry surfaces.** *Seat:* the head.
5. **Land the untracked audit files** (BRIEF-GOAL-VERDICT, BRIEF-LEG5-CROSSCHECK, audit registry). *Seat:* the audit legs.
6. **W2-isolation settle** — NEEDS-THE-CHAIR. *Gate:* the user's word. No auto-path.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

| step | evidence |
|---|---|
| 1 header+register | seat/branch/fire/gate/register present; ABSENT+named ×2 |
| 2 window-check | 3 rows, each checked/not-run-why + receipt |
| 3 seam-scan | 5 rows, each state + receipt |
| 4 entropy classes | 9 findings, each named WITH countermove |
| 5 next-moves | 6 moves, each action/gate/seat |
| 6 compose-check | this table |
| 7 loop-state | the line below |
| 8 commit+push | the branch commit (this artifact) |

## 6. THE LOOP-STATE LINE

`CONTINUE + restore probes/BATTERY-FULL-LEDGER-20261119.json from git history and byte-verify the kept-rate structure (the k-term re-measure's surface); the W2-isolation stays NEEDS-THE-CHAIR under the gate.` — receipt: IN-LANE (git ls-files/log, read_file ABSENT, plan line 83).