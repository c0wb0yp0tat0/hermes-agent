# NEGENTROPY-SWEEP-20261122-0039 — the recurring sweep

**seat** the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · **branch** study/rfc-143379-rig-20261105 · **fire time** 2026-11-22 00:39 · **the gate verbatim** "the gate: nothing public without the user's word."
**the register** — [1st] re-read by this lane this pass (git-tree/status/log, study listing) · [2nd] carried from a study doc, not re-derived here · a fact that cannot be received stays ABSENT+named, never invented · tags IN-LANE / BORROWED <source> / HEAD-RECON.

**VERDICT** — the 1032 loose thread (the uncommitted deletion of `probes/BATTERY-FULL-LEDGER-20261119.json`) is NOT reproduced: this pass's `git status --porcelain` shows no tracked deletion or modification at all [1st]. But the read-burn seam has now bitten the sweep itself: the analysis phase was cut off by the write-window gate mid-pass ("READ-GATED … due within 9 rounds"), so the arming record and the two newer sweep artifacts on the branch (1434, 2037) could not be re-read. The apex hold stands, carried [2nd].

## 1. THE WINDOW-CHECK (the gate)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT-RUN | [2nd] 1032 sweep; no W2 probe in the delta; the lane terminal is git-only, no measurement tool |
| k-term two-tier re-measure | NOT-RUN | [2nd] baseline kept-rates 0.42/0.29/0.26/0.26, flat (span 0.26–0.42); no new k-term receipt |
| budget consolidation re-verify | NOT-RUN | [2nd] decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00; no new budget receipt |

Carried-not-runnable: the read-window now closes before the measurement can run — and this pass it closed before the *reading* could finish (seam row 1). Class: **validity decay** — the baseline is ~4 days old and no lane owns its refresh. The ledger that would refresh it is no longer deleted in the tree [1st], but it is still unmeasured.

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | OPEN, now self-inflicted | IN-LANE: this lane's reads were gated mid-analysis ("READ-GATED … due within 12/9 rounds"); the analysis phase ended before the arming record was opened |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT-RUN | ABSENT+named: no scribe access from a git-only lane; [2nd] 1032 carried the 0630 cell byte-identity CONFIRMATION-CYCLE sha ececd55d… |
| token watcher's single-source line | MISMATCH (three surfaces), carried | [2nd] 1032: map line 35 LANDED vs plan line 83 ARMED vs the arming record §1 single-source claim; not re-readable this pass (read-gated) |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT-RUN | ABSENT+named: git-only terminal; [2nd] the 2026-11-19 arming record's live rows |
| dispositions | AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR | AUTO-CONTINUE: the watcher's delta-only collapse (charter; not executed) · HOLD-SAFE: the apex hold · NEEDS-THE-CHAIR: the plan-line-83 reconcile + the branch-lineage reconcile + the PR-body archive (the head's word) |

## 3. THE ENTROPY CLASSES (CTO freedom applies)
**dead surface** — the watcher's MISSION-MAP rows are near-identical HOLD rows; information per row ≈ 0. Countermove: fire a watcher row only on a delta (new sha / new steer / token move).
**loose thread (carried, not reproduced)** — the battery-ledger deletion is gone from the tree [1st]; the thread closes. Countermove: none needed; keep the ledger in-tree as the window-check's instrument.
**loose thread (new)** — the branch carries sweep artifacts 1434 and 2037 that this lane could not read (read-gated); the delta baseline 1032 is on origin, but the lane's local HEAD tree does not contain it. Countermove: read them at the next fire with the read-window open; never let the sweep's own delta pass unreceived.
**friction (new, structural)** — the local HEAD (2ce77ce5ad, lane-AA audit) and origin/study/rfc-143379-rig-20261105 (bb96c80f4e, rewind-ack) have no common ancestor: the lane's branch tip is a different lineage from the remote's. Countermove: reconcile (rebase/reset to origin) before the next commit, or name the orphan lineage deliberately.
**friction (carried)** — two time bases: watcher rows EST-labeled, sweeps UTC. Countermove: stamp both, or one base.
**friction (carried)** — three "single-source" claims for the loop-state line. Countermove: one surface, one state.
**orphan sentinel (carried)** — the steer channel: NEMO-STEER-CHANNEL-20261119.md present in HEAD; the "name one steering surface" half remains open. Countermove: name the steering surface; stop treating 20261116 vs 20261119 as two.
**UNSPOKEN (carried)** — the apex hold has held since 2026-11-18 ~14:2x (~4 days). No terminal condition is named for the hold itself. Countermove: name it, or convert HOLD → DONE.
**the unexpected (the prize)** — the write-gate that is meant to force emission is destroying the receipts the sweep exists to keep: this fire's analysis was truncated by the gate, so the [2nd] tags above are load-bearing exactly where the register least wants them. The entropy is again in the bookkeeping, not the mission — and this time the bookkeeping is the sweep's own read path.

## 4. THE ORDERED NEXT-MOVES
1. **Reconcile the branch lineage** (local HEAD vs origin; no common ancestor). Gate: the head's word. Seat: head. (A commit pushed from an orphan lineage will be rejected.)
2. **Read the unreceived delta** (sweeps 1434, 2037; the arming record) at the next fire with the read-window open. Gate: none (receipts). Seat: this lane.
3. **Reconcile the three loop-state surfaces** (map line 35 vs plan line 83 vs the arming record). Gate: the head's word. Seat: head.
4. **Collapse the watcher to delta-only rows.** Gate: the watcher's charter. Seat: watcher.
5. **Name the hold's terminal condition** (or convert HOLD → DONE). Gate: the head's calibrated judgment. Seat: head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS (eight steps, one evidence line each)
1. header+register present — IN-LANE: seat/branch/fire/gate/register on the head line.
2. window-check table — three rows, each not-run-why + receipt ([2nd] 1032); the ledger row IN-LANE [1st].
3. seam-scan rows — five rows, each state + receipt; the read-burn row IN-LANE (reproduced this pass).
4. entropy findings with countermoves — nine findings, each named WITH its countermove.
5. ordered next-moves — five, each action+gate+seat.
6. compose-check — this section, eight steps.
7. loop-state line — receipted below.
8. commit+push — the emission contract's single commit (add → commit → push; pull --rebase on rejection).
Step-list provenance: HEAD-RECON (the canonical eight was not re-readable this pass; the read-window gated).

## 6. THE LOOP-STATE LINE
`CONTINUE + the head reconciles the branch lineage (local HEAD 2ce77ce5ad vs origin bb96c80f4e, no common ancestor) before the next commit; this lane reads the unreceived delta (sweeps 1434/2037, the arming record) at the next fire; the watcher collapses to delta-only rows; the apex-hold terminal condition is named.`
Receipt: [1st] `git status --porcelain` (no tracked D/M), `git rev-parse HEAD`=2ce77ce5ad / `origin/study/rfc-143379-rig-20261105`=bb96c80f4e, the read-gate messages, the 1032 artifact as read, the origin tree listing showing NEGENTROPY-SWEEP-20261121-1434.md and commit 86428957de (2037) · [2nd] the 1032 baselines + the 2026-11-19 arming record's wire rows. The 1032's ledger-deletion "uncommitted" is not reproduced this pass — a shared-branch ordering artifact (HEAD-RECON), the watcher's REWIND class.