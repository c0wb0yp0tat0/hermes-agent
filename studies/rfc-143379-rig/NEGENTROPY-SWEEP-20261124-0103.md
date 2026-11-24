# NEGENTROPY-SWEEP-20261124-0103

seat: recurring negentropy-sweep lane (scheduled sweep ride, cadence 2h, no_agent arm)
branch: study/rfc-143379-rig-20261105 · HEAD 5c315184be ("task: arm-01-c fixes: drop unused churn counters, make lease typecheck read-only", head) [IN-LANE]
fire time: 2026-11-24T01:03Z
the gate, verbatim: "the gate: nothing public without the user's word."
register: [1st] = re-read by this lane this pass (git status/log/ls-files, dir listings) · [2nd] = carried from a study doc, not re-derived here · otherwise ABSENT + named. Tags: IN-LANE / BORROWED <source> / HEAD-RECON. Nothing invented; nothing silently passed.

## 1 THE WINDOW-CHECK (carried [2nd]; no measuring seat rode this fire)
| standing item | state this fire | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT RUN — why: the scheduled sweep is harness-only; no measurement lane in this ride. Settle-condition text ABSENT+named (prev artifact unreadable this pass, see §2 seam). | [2nd] BORROWED last-sweep baseline |
| k-term two-tier re-measure | NOT RUN — why: same. Baseline carried: kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat; the budget's class ordering presupposes differential keep-rates, the flat k-term contradicts it. | [2nd] BORROWED; IN-LANE note below |
| budget consolidation re-verify | NOT RUN — why: same. Carried ordering: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. | [2nd] BORROWED |
IN-LANE note on the flat k-term: a flat keep-rate across tiers means history buys no value differential — the memory-economy arbitration rho=(V−λH)/b degenerates (no V spread per H tier), so the tier ordering cannot be justified from keep-rates alone. STORM MemCredit class corroboration; design stays ours. All three items roll open to the next fire that has a measuring seat.

## 2 THE SEAM-SCAN
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline seam | OPEN. The write-window opened while the previous sweep artifact (studies/rfc-143379-rig/studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261124-0012.md) was unreachable: read_file refused the path as outside allowed roots, and once the gate opened all terminal content-reads (incl. git show) were blocked. The lane fires blind on its own delta baseline. | IN-LANE (this pass) |
| fold checks: scribe cell → get_memory byte-compare; served ?raw=1 grep | NOT RUN — no fold seat rode this pass. Visible residue: SCRIBE-WITNESS-REGISTRY.log dirty at snapshot B (see §3). | [2nd] standing rows + IN-LANE residue |
| token watcher single-source line | ABSENT + named — the loop-state token's file was not reachable before the read-gate; single-source stays an assumption, not a receipt. | IN-LANE (unread) |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | ABSENT + named — read-gated this pass. | IN-LANE (unread) |
| dispositions | this lane AUTO-CONTINUE (artifact + local commit); every public action HOLD-SAFE; cycle-body reaper ownership NEEDS-THE-CHAIR. | IN-LANE |

## 3 THE ENTROPY CLASSES (core)
- DEAD SURFACE: 74 tracked FLEET-CYCLE-BODY-*.md sitting at repo root, one body per cycle [IN-LANE: git ls-files 'FLEET*']; six .sentinel files for abandoned sweeps 0003–0008 [IN-LANE: status snapshot A]. Countermove: one index row per cycle; bodies belong under studies/ (the fold already moved 2026-11-23T144139Z there); prune sentinels at the fold.
- LOOSE THREADS: (a) four FLEET-CYCLE-BODY files deleted-but-uncommitted at snapshot A [IN-LANE]; (b) SCRIBE-WITNESS-REGISTRY.log modified-uncommitted at snapshot B [IN-LANE]; (c) nine untracked artifacts at snapshot A (sweep 0012, the six sentinels, ARM-EXECUTE 1120/1121/1122, FLEET-CYCLE-SERVICE, CLAWBACK + EMERGENCE-INTERFERENCE briefs) all absent from untracked at snapshot B — committed or reaped mid-pass [IN-LANE]. Countermove: fold lands its rows as commits before the next fire; sweep receipts carry observe-time, not just fire-time.
- FRICTION POINT: mid-pass tree mutation — the deletion set changed between two observations minutes apart, so a receipt can go stale inside one fire. That is validity decay in the machine layer (STORM "validity decay" class, corroboration only). Countermove: stamp receipts with both fire time and observation time.
- UNSPOKEN: the tree is not clean while the compose-check narrative assumes landed state; and the "no_agent arm" label coexists with a live writer mutating the worktree — the arm name understates the concurrency.
- UNEXPECTED (the prize): an unnamed background reaper/restorer of cycle bodies is acting on this branch. Snapshot A had 2026-11-24-050539Z deleted; snapshot B has it gone from the deletion set and 2026-11-23T144139Z newly deleted [IN-LANE]. No brief read this pass names the owner. Countermove: name it (fold cron vs stray writer), give it a receipt row, make its mutations land as commits rather than worktree drift. Until named: NEEDS-THE-CHAIR.
- STORM-CONTEXT corroboration (class-level, never adoption): SELD read-side evidence-plane verifier = this register's [1st]/[2nd] split; DISCERN write-gate L0 = the artifact write itself; AskALCF commit gate = the local commit closing this lane; CoMem fidelity-ladder = keep the last landed sweep, treat sentinels as L0 noise; Reward-Driven Collider AIMD = the fold's send-all phase is a wide envelope whose only brake is the gate line — the sweep logs the envelope.

## 4 THE ORDERED NEXT-MOVES
1. fold — commit or restore the four deleted FLEET-CYCLE-BODY bodies. Gate: local only. Seat: fold.
2. fold — land or revert the dirty SCRIBE-WITNESS-REGISTRY.log. Gate: compose-check. Seat: fold.
3. chair — name the cycle-body reaper owner. Gate: nothing public without the user's word. Seat: chair.
4. sweep (next fire) — read NEGENTROPY-SWEEP-20261124-0012.md at its landed path before adjudicating the delta. Gate: read-window. Seat: sweep.
5. CTO — run the three windowed measurements (W2 isolation, k-term two-tier, budget consolidation) when a measuring seat rides. Gate: window. Seat: CTO.

## 5 THE COMPOSE-CHECK + RECEIPT STAMPS
Canonical eight-step list: ABSENT + named (master brief §7 / loop-state token — read-gated this pass; not reconstructed here). Stamps evidenced by this artifact:
1. gate verbatim present in header — IN-LANE.
2. register with hand-separation present — IN-LANE.
3. receipts-not-claims honored: every row tagged IN-LANE / BORROWED / ABSENT+named — IN-LANE.
4. nothing invented; unreachable facts named, not silently passed — IN-LANE.
5. artifact written to the contracted path — IN-LANE (this write).
6. one-section-per-write respected; ≤6,000 chars per write — IN-LANE.
7. commit-before-exit: this lane's final step, LOCAL only (push/pull denied by rig) — IN-LANE (pending this commit).
8. loop-state line receipted in §6 — IN-LANE.

## 6 THE LOOP-STATE LINE
CONTINUE + fold commits-or-restores the four deleted FLEET-CYCLE-BODY bodies and lands-or-reverts SCRIBE-WITNESS-REGISTRY.log before the next fire; the sweep then re-reads NEGENTROPY-SWEEP-20261124-0012.md at its landed path. Receipt: IN-LANE snapshots A/B, this pass.