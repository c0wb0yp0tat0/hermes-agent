# NEGENTROPY-SWEEP-20261121-1032 — the recurring sweep

**seat** the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · **branch** study/rfc-143379-rig-20261105 · **fire time** 2026-11-21 10:32 · **the gate verbatim** "the gate: nothing public without the user's word."
**the register** — [1st] re-read by this lane this pass (git-tree, study listings, branch log) · [2nd] carried from a study doc, not re-derived here · a fact that cannot be received stays ABSENT+named, never invented · tags IN-LANE / BORROWED <source> / HEAD-RECON.

**VERDICT** — the delta since the 0831 sweep's commit (de2514084f) is four commits, all NIGHTSHIFT-WATCH HOLD rows (44f8a5c6c5 ~03:4x, 197a60a9a4 ~04:1x, 61aa7c974c ~04:4x, 267d2b9a20 ~05:1x; the watcher's rows are EST-labeled). Zero mission-advancing artifacts. The apex hold stands (map line 35, [1st]). The three standing windowed items remain carried, not runnable in-lane. New this fire: the working tree carries an uncommitted deletion of `probes/BATTERY-FULL-LEDGER-20261119.json` — the window-check's likeliest measuring surface.

## 1. THE WINDOW-CHECK (the gate)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT-RUN | [2nd] 0831 sweep; no W2 probe in the delta; the lane terminal is git-only, no measurement tool |
| k-term two-tier re-measure | NOT-RUN | [2nd] baseline kept-rates 0.42/0.29/0.26/0.26, flat (span 0.26–0.42); no new k-term receipt in the delta |
| budget consolidation re-verify | NOT-RUN | [2nd] decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00; no new budget receipt |

Carried-not-runnable: the read-window closes before the measurement can run (seam row 1). Class: **validity decay** — the baseline is ~3.5 days old and no lane owns its refresh. The ledger that would refresh it is deleted in the working tree ([1st] `git status --porcelain`: ` D studies/rfc-143379-rig/probes/BATTERY-FULL-LEDGER-20261119.json`; the file is present in HEAD).

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | OPEN | IN-LANE: this lane's terminal went git-only mid-pass (compound reads refused: "terminal is git-only for lanes"); the write-early gate closes reads before the standing measurements |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT-RUN | ABSENT+named: scribe get_memory (no scribe access from a git-only lane); [2nd] 0831 carried the 0630 cell byte-identity CONFIRMATION-CYCLE sha ececd55d… |
| token watcher's single-source line | MISMATCH (three surfaces) | [1st] map line 35 = "NIGHTSHIFT-STAGE-4 - CONFIRMATION-CYCLE LANDED … APEX HOLD"; [1st] plan line 83 = "CONFIRMATION-ARMED …"; [1st] NEGENTROPY-ARM-EXECUTE-20261119.md §1 claims to be THE single source — three surfaces, two states |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT-RUN | ABSENT+named: git-only terminal; [2nd] the 2026-11-19 arming record's live rows (scribe tunnel REACHABLE, Harbor :44831 LIVE, SSH 192.168.1.241 REACHABLE) |
| dispositions | AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR | AUTO-CONTINUE: the watcher's delta-only collapse (its charter; not yet executed) · HOLD-SAFE: the apex hold (map+plan coherent, sequence intact) · NEEDS-THE-CHAIR: the plan-line-83 reconcile + the ledger restore + the PR-body archive (the head's word) |

## 3. THE ENTROPY CLASSES (CTO freedom applies)
**dead surface** — the watcher's MISSION-MAP rows are near-identical HOLD rows ("state unchanged on the stage tokens; local==remote <sha>; NO DISPATCH"); information per row ≈ 0, and this fire's delta is four of them. Countermove: fire a watcher row only on a delta (new sha / new steer / token move); else no row.
**loose thread** — the working tree carries three uncommitted items: ` D probes/BATTERY-FULL-LEDGER-20261119.json` (the k-term/budget measuring surface), ` M SCRIBE-WITNESS-REGISTRY.log`, `?? tmp-artifacts/runner-recon-20261120.log`. A tracked ledger deleted uncommitted is a fold-check-relevant item. Countermove: commit or restore the ledger; row the recon log; never let the baseline's instrument leave the tree silently.
**loose thread (carried)** — FLEET-CYCLE-BODY-20261121T080724Z.md: an "operator-shaped PR body" archived with no PR. [2nd] 0831; no delta commit rows it. Countermove: pair with its PR (gate: the user's word) or drop to a local draft.
**friction** — two time bases on one branch: the watcher's rows are EST-labeled (~03:4x–05:1x) while the sweeps are UTC (08:31, 10:32); a reader must convert to order them. Countermove: stamp every row with both, or one base.
**friction** — three "single-source" claims for the loop-state line (map line 35, plan line 83, the arming record §1). Countermove: one surface, one state; the others reference it.
**orphan sentinel (carried, partly resolved)** — the steer channel: [1st] NEMO-STEER-CHANNEL-20261119.md is present in HEAD (last touch c378fc6b55), so the 0831's "uncommitted" is not reproduced this pass; the "name one steering surface" half remains open. Countermove: name the steering surface; stop treating 20261116 vs 20261119 as two.
**UNSPOKEN** — the apex hold has held since 2026-11-18 ~14:2x (~3.5 days). HOLD presumes a future fire; the record names no terminal condition for the hold itself. Is the apex a finished state or a stall? Countermove: name the hold's own terminal condition, or convert HOLD → DONE.
**the unexpected (the prize)** — the entropy is not in the mission; it is in the bookkeeping. This fire's delta is four watcher rows about watcher rows, and at the same moment the one artifact that could break the validity-decay (the battery ledger) is deleted uncommitted in the working tree. The sweep's next fire should report the delta in mission units (artifacts advanced), not row counts.

## 4. THE ORDERED NEXT-MOVES
1. **Restore or commit the battery ledger** (`BATTERY-FULL-LEDGER-20261119.json`). Gate: the head's word. Seat: head. (It is the window-check's measuring surface.)
2. **Reconcile the three loop-state surfaces** (map line 35 LANDED vs plan line 83 ARMED vs the arming record's single-source claim). Gate: the head's word (the plan token is head-owned). Seat: head.
3. **Collapse the watcher to delta-only rows.** Gate: the watcher's charter. Seat: watcher.
4. **Name the hold's terminal condition** (or convert HOLD → DONE). Gate: the head's calibrated judgment. Seat: head.
5. **Reclassify the window-check** as carried-not-runnable in-lane, and name the measuring lane for W2/k-term/budget. Gate: none (receipts). Seat: head names the measurer.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS (eight steps, one evidence line each)
1. header+register present — IN-LANE: seat/branch/fire/gate/register on the head line.
2. window-check table — three rows, each checked/not-run-why + receipt ([2nd] 0831); the ledger row IN-LANE.
3. seam-scan rows — five rows, each current state + receipt; the read-burn row IN-LANE.
4. entropy findings with countermoves — eight findings, each named WITH its countermove.
5. ordered next-moves — five, each action+gate+seat.
6. compose-check — this section, eight steps.
7. loop-state line — receipted below.
8. commit+push — the emission contract's single commit (add → commit → push; pull --rebase on rejection).
Step-list provenance: HEAD-RECON (the canonical eight was not re-readable this pass; the read-window gated).

## 6. THE LOOP-STATE LINE
`CONTINUE + the head restores/commits the battery ledger and reconciles the three loop-state surfaces (map line 35 LANDED vs plan line 83 ARMED vs the arming record's single-source claim); the watcher collapses to delta-only rows; the sweep re-fires at the next cadence with the window-check reclassified carried-not-runnable.`
Receipt: [1st] the branch log (de2514084f..HEAD = 44f8a5c6c5, 197a60a9a4, 61aa7c974c, 267d2b9a20), map line 35, plan line 83, `git status --porcelain` (ledger D / registry M / recon log ??), NEMO-STEER-CHANNEL-20261119.md in HEAD · [2nd] the 0831 baselines + the 2026-11-19 arming record's wire rows. The 0831's steer-channel "uncommitted" is not reproduced this pass — a shared-branch ordering artifact (HEAD-RECON), the watcher's REWIND class.