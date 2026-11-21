# NEGENTROPY-SWEEP-20261121-0831 — the recurring sweep

**seat** the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · **branch** study/rfc-143379-rig-20261105 · **fire time** 2026-11-21 08:31 · **the gate verbatim** "the gate: nothing public without the user's word."
**the register** — [1st] re-read by this lane this pass (git-tree, study listings, branch log) · [2nd] carried from a study doc, not re-derived here · a fact that cannot be received stays ABSENT+named, never invented · tags IN-LANE / BORROWED / HEAD-RECON.

**VERDICT** — the delta since the 0630 sweep's commit (c98ed991f2) is three commits, all bookkeeping: two watcher HOLD rows (a3642f5994, bc3673581a) + one fleet-cycle archive body (e193c92e22). Zero mission-advancing artifacts. The apex hold stands (map line 35). The sweep's three standing windowed items remain carried, not runnable in-lane.

## 1. THE WINDOW-CHECK (the gate)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT-RUN | [2nd] 0630 sweep; no W2 probe in the delta commits; the lane terminal is git-only, no measurement tool |
| k-term two-tier re-measure | NOT-RUN | [2nd] baseline kept-rates 0.42/0.29/0.26/0.26, flat (span 0.26–0.42); no new k-term receipt in the delta |
| budget consolidation re-verify | NOT-RUN | [2nd] decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00; no new budget receipt |

The window-check is structurally carried-not-runnable: the read-window closes before the measurement can run (seam-scan row 1). Class: **validity decay** — the baseline is three days old and no lane owns its refresh.

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | OPEN | IN-LANE: this lane's read-tools refused at the write-window (READ-GATED, "the artifact's due within 13 rounds"); the write-early gate closes reads before the standing measurements |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT-RUN | ABSENT+named: scribe get_memory (no scribe access from a git-only lane); [2nd] 0630 cell byte-identity CONFIRMATION-CYCLE sha ececd55d… |
| token watcher's single-source line | MISMATCH | [1st] map line 35 = "STAGE-4 - CONFIRMATION-CYCLE LANDED … APEX HOLD"; plan line 83 ABSENT+named (read-gated), [2nd] carried = "CONFIRMATION-ARMED" |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT-RUN | ABSENT+named: Harbor/local-LM runner, scribe tunnel — git-only terminal |
| dispositions | AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR | AUTO-CONTINUE: the watcher's delta-only collapse (its own charter) · HOLD-SAFE: the apex hold (map+plan coherent, sequence intact) · NEEDS-THE-CHAIR: the plan-line-83 reconcile + the PR-body archive (the head's word) |

## 3. THE ENTROPY CLASSES (CTO freedom applies)
**dead surface** — the watcher's MISSION-MAP rows are now near-identical HOLD rows ("state unchanged on the stage tokens; local==remote <sha>; STEER-11; apex re-door-verified; NO DISPATCH"); information per row ≈ 0. Countermove: fire a watcher row only on a delta (new sha / new steer / token move); else no row.
**loose thread** — FLEET-CYCLE-BODY-20261121T080724Z.md, an "operator-shaped PR body" archived to the tree with no PR: a body without its PR. Countermove: pair it with its PR (gate: the user's word) or drop it to a local draft; do not let it accrete.
**friction** — two "single-source" loop-state lines disagree in tense: map line 35 LANDED vs plan line 83 ARMED. The watcher rows carry both without flagging the gap. Countermove: reconcile plan line 83 to CONFIRMATION-LANDED (or name why ARMED is correct) — one source, one state.
**orphan sentinel** — the steer channel is split: steer-channel-20261116 committed (newest STEER-11, banked 9a92aa944e) vs NEMO-STEER-CHANNEL-20261119 uncommitted (the head's in-flight). The watcher treats 20261116 as the steering surface. Countermove: commit or drop the 20261119 channel; name one steering surface.
**UNSPOKEN** — the apex hold has held since 2026-11-18 ~14:2x (three days). HOLD presumes a future fire; the record names no terminal condition for the hold itself. The unspoken question: is the apex a finished state or a stall? Countermove: name the hold's own terminal condition, or convert HOLD → DONE.
**the unexpected (the prize)** — the branch's recent activity is a self-referential archive loop: watcher rows about watcher rows + fleet-cycle bodies, zero mission-advancing artifacts. The entropy is not in the mission; it is in the bookkeeping. Countermove: the sweep's next fire reports the delta in mission units (artifacts advanced), not in row counts.

## 4. THE ORDERED NEXT-MOVES
1. **Reconcile the two loop-state lines** (plan line 83 ARMED → LANDED, or name ARMED correct). Gate: the head's word (the plan token is head-owned). Seat: head.
2. **Collapse the watcher to delta-only rows.** Gate: the watcher's charter. Seat: watcher.
3. **Reconcile the steer channel** (commit or drop NEMO-STEER-CHANNEL-20261119). Gate: the head. Seat: head.
4. **Reclassify the window-check** as carried-not-runnable in-lane, and name the measuring lane for W2/k-term/budget. Gate: none (receipts). Seat: head names the measurer.
5. **Row the FLEET-CYCLE-BODY PR body** (pair with its PR or drop to local draft). Gate: the user's word (public). Seat: head/operator.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS (eight steps, one evidence line each)
1. header+register present — IN-LANE: seat/branch/fire/gate/register on the head line.
2. window-check table — three rows, each checked/not-run-why + receipt ([2nd] 0630).
3. seam-scan rows — five rows, each current state + receipt; the read-burn row IN-LANE.
4. entropy findings with countermoves — six findings, each named WITH its countermove.
5. ordered next-moves — five, each action+gate+seat.
6. compose-check — this section, eight steps.
7. loop-state line — receipted below.
8. commit+push — the emission contract's single commit (add → commit → push; pull --rebase on rejection).
Step-list provenance: HEAD-RECON (the canonical eight was not re-readable this pass; the read-window gated).

## 6. THE LOOP-STATE LINE
`CONTINUE + the head reconciles plan line 83 to CONFIRMATION-LANDED (or names ARMED correct) and the watcher collapses to delta-only rows; the sweep re-fires at the next cadence with the window-check reclassified carried-not-runnable.`
Receipt: [1st] map line 35 + the branch log (bc3673581a, e193c92e22, a3642f5994, c98ed991f2) · [2nd] plan line 83 + the 0630 baselines. The 0630 sweep's own message lists a wider delta set (45e5b48b4f…e193c92e22) than the log's post-c98ed991f2 three — a shared-branch ordering artifact (HEAD-RECON), the watcher's REWIND class.