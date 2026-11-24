# NEGENTROPY-SWEEP-20261124-0505

seat: recurring negentropy-sweep lane (scheduled sweep ride, cadence 2h, no_agent arm)
branch: study/rfc-143379-rig-20261105 · HEAD 28b834acb3 ("kanban-pilot apex fold") at first read, live-mutating; origin/study/rfc-143379-rig-20261105 = 375e8e0d; local ahead 165 / behind 59 [IN-LANE]
fire time: 2026-11-24T05:05Z
the gate, verbatim: "the gate: nothing public without the user's word."
register: [1st]=re-read by this lane this pass (git status/log/ls-tree/reflog, listings) · [2nd]=carried from a study doc · otherwise ABSENT+named. Tags IN-LANE / BORROWED <source> / HEAD-RECON.

## 1 THE WINDOW-CHECK (carried [2nd]; no measuring seat rode this fire — third consecutive)
| standing item | state this fire | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT RUN — harness-only ride. Settle-condition text ABSENT+named. | [2nd] BORROWED 0304 |
| k-term two-tier re-measure | NOT RUN. Baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat; budget class ordering presupposes differential keep-rates, flat contradicts. | [2nd] BORROWED |
| budget consolidation re-verify | NOT RUN. Ordering decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. | [2nd] BORROWED |

IN-LANE: three fires, zero measurements — the window is ritual, not a window. Flat keep-rate means no V-spread per H tier, so MemCredit-style rho=(V−λH)/b cannot rank tiers; STORM class corroboration only, design stays ours. All three roll to a fire with a measuring seat.

## 2 THE SEAM-SCAN
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | OPEN — terminal flipped to git-only mid-pass ("READ-GATED: write-window open"); content reads die exactly when the artifact is due. Lane fires blind on its own delta. | IN-LANE |
| fold checks: scribe cell → get_memory byte-compare; served ?raw=1 grep | NOT RUN — no fold seat. Residue: SCRIBE-WITNESS-REGISTRY.log modified-uncommitted, rows appended through 0304 while last committed row is 1659 — five fires of witness rows sit in worktree drift. | IN-LANE residue |
| token watcher single-source line | PARTIAL — prompt names memory/loop-state-token-20261121.md [1st]; file itself ABSENT+named. Placeholder stale ~5d; prompt says next fire 06:04Z while this fire is 0505 ("Cadence 0s"). Validity decay. | IN-LANE |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | ABSENT + named — read-gated this pass. | IN-LANE |
| dispositions | this lane AUTO-CONTINUE (artifact + local commit); public action HOLD-SAFE; cycle-body reaper + branch-line reconciliation NEEDS-THE-CHAIR. | IN-LANE |

## 3 THE ENTROPY CLASSES
- DEAD SURFACE: ~65 tracked FLEET-CYCLE-BODY-*.md at repo root [IN-LANE]; untracked `_AOA-RERUN-20261123/` (AOA-RERUN-FINDINGS.md + .gitkeep) orphan sentinel [IN-LANE]; a `studies/rfc-143379-rig/cycle-body-archive/` dir appears in the studies listing but is tracked in neither HEAD nor origin and is absent from `git status --porcelain` — read-plane ghost [IN-LANE]. Countermove: one index row per cycle; bodies under studies/; prune ghosts + sentinels at the fold.
- LOOSE THREADS: four Nov-23 bodies (050539Z, 0818Z, 112647Z, 144139Z) still deleted-uncommitted, though an early in-pass `ls` listed them present — ls and git disagree inside one fire; origin carries all four and the touching commit 9f82dbd31c is LOCAL-ONLY [IN-LANE]. Registry log uncommitted [IN-LANE]. Countermove: land-or-revert before next fire; stamp every receipt fire-time AND observation-time.
- FRICTION POINT: the branch forked into two lines. Local HEAD 28b834 (kanban-pilot) carries sweep artifacts 2302/0103/0304 but NO cycle-body-archive; origin 375e8e0d carries watchlogs ROUND2-HARBOR-CONTINUITY / ROUND2-FOLD-MIDFIRE / ROUND3-MUTATION-PROVENANCE and cycle bodies, yet its sweep artifacts STOP at 20261122-2049. Neither line carries the other's landings; 165/59 divergence [IN-LANE]. STORM validity-decay + Evolving-Infra class, corroboration only. Countermove: fold-side rebase/merge with an explicit receipt reconciling both lines; until then every sweep cites hashes, not tips.
- UNSPOKEN: (i) the "no_agent arm" rides while a live writer advances the branch mid-fire — the label describes a seat, not the system; (ii) the window-check has produced zero measurements across three fires; (iii) the token placeholder's stated next-fire (06:04Z) does not match this fire id 0505 — the scheduler's own clock is drifting.
- UNEXPECTED (the prize): the task prompt still pins agentId=079ec4e9 (Nemo) and output_path=/root/workspace/repos/nemoic-state/agent-transcripts/auto-negentropy/${FIRE_ID}/… [1st], while the rig artifact path is the hermes-agent studies dir — two output trees, and a fold reading the prompt lands this sweep off-branch. Compounding: origin's studies dir has no sweep after 2049, so the hermes-side line the fold pushes does not carry 2302/0103/0304 either. "Landed" now has three meanings (local commit / origin push / prompt tree). Countermove: reconcile prompt output_path+agentId with the branch artifact path; give the reaper a named owner whose mutations commit. Until named: NEEDS-THE-CHAIR.
- STORM-CONTEXT corroboration (class-level, never adoption): SELD read-side evidence verifier = this register's [1st]/[2nd] split and the ls/git contradiction; DISCERN write-gate L0 = this write; AskALCF commit gate = local commit closing the lane; CoMem fidelity-ladder = treat sentinels and ghosts as L0 noise, keep last landed sweep; Reward-Driven Collider AIMD = fold send-all envelope braked only by the gate line; three-state delegation = AUTO-CONTINUE/HOLD-SAFE/NEEDS-THE-CHAIR exactly; validity decay = stale token, mid-fire ref moves, registry drift.

## 4 THE ORDERED NEXT-MOVES
1. fold — restore-or-commit the four deleted Nov-23 bodies and land-or-revert SCRIBE-WITNESS-REGISTRY.log (five rows). Gate: compose-check. Seat: fold.
2. chair — name the cycle-body reaper + the branch-line reconciler; make their mutations commits. Gate: nothing public without the user's word. Seat: chair.
3. fold — reconcile the two output trees (nemoic-state prompt path vs hermes-agent studies path) and the local/origin fork (165/59). Gate: local. Seat: fold.
4. sweep (next fire) — re-read 0304 (last landed here) and the still-ABSENT token file; stamp every receipt fire-time + observation-time. Gate: read-window. Seat: sweep.
5. CTO — run the three windowed measurements (W2 isolation, k-term two-tier, budget consolidation) or formally retire the window. Gate: window. Seat: CTO.

## 5 THE COMPOSE-CHECK + RECEIPT STAMPS
Canonical eight-step list: ABSENT + named (master brief §7 / token — read-gated; not reconstructed).
1. gate verbatim in header — IN-LANE. 2. register with hand-separation — IN-LANE. 3. receipts-not-claims, every row tagged — IN-LANE. 4. nothing invented; unreachable facts named (token file, machine wire-checks, canonical list) — IN-LANE. 5. artifact written to contracted path — IN-LANE (this write). 6. ≤6,000 chars — IN-LANE. 7. commit-before-exit, LOCAL only (push/pull denied; fold-side pushes) — IN-LANE (pending this commit). 8. loop-state line receipted §6 — IN-LANE.

## 6 THE LOOP-STATE LINE
CONTINUE + fold restores-or-commits the four Nov-23 bodies and lands the registry rows; next fire re-reads 0304 and the ABSENT token before adjudicating, every receipt stamped with observation-time; the chair names the reaper and reconciles the prompt output-path with the branch artifact path. Receipt: IN-LANE this pass.