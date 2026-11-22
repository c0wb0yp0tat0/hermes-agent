# NEGENTROPY-SWEEP-20261122-0441 — the recurring sweep

- **seat:** meituan/longcat-2.5:free (the arm's `NEGENTROPY_SEAT` default; roster-registered 2026-11-19) — [1st] IN-LANE
- **branch:** `study/rfc-143379-rig-20261105` — local HEAD `af584b8a0a`; wire tip `7f99a01eff` — [1st] IN-LANE
- **fire time:** 2026-11-22 04:41 UTC
- **the gate:** "the gate: nothing public without the user's word."
- **register:** [1st] = re-read by this lane this pass (git-tree / branch logs); [2nd] = carried from a study doc, not re-derived; **ABSENT + named** = unreceived, never invented. Tags: `IN-LANE` / `BORROWED <source>` / `HEAD-RECON`.
- **storm-context:** the standing harvest was considered; no adoption — the sweep's design stays its own. One corroboration of class: DISCERN's write-gate L0 is the same seam as the read-burn gate below.

## 1 · THE WINDOW-CHECK (the gate)
Carried [2nd] from `NEGENTROPY-SWEEP-20261122-0240.md` (the delta baseline). No harness byte-verified for a lane this fire; all three stay open.

| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT-RUN — no harness this fire | [2nd] 0240 window-check |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, flat 0.26–0.42) | NOT-RUN — the flat k-term still contradicts the budget's class ordering | [2nd] 0240 |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | NOT-RUN — no harness this fire | [2nd] 0240 |

## 2 · THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | **FIRED this fire** — a non-git terminal call (`ls | wc -l`) was refused ("terminal is git-only for lanes"); the write-window gate then blocked all reads | [1st] IN-LANE |
| fold checks (scribe cell → `get_memory` byte-compare; served `?raw=1` grep) | carried: registry rows 2238 (`781b86d160e95e11`) + 0039 (`6361cd0b5cb226b1`), byte-identical=True | [2nd] 0240 |
| token watcher's single-source line | **RECEIVED this fire** — the token's single source is `NEGENTROPY-ARM-EXECUTE-20261119.md` (its §1 names itself); the 0240 "unreceived" row is a mis-receipt | [1st] IN-LANE |
| machine-layer wire-checks | carried: scribe :24282 REACHABLE, Harbor :44831 LIVE, SSH 192.168.1.241 REACHABLE | [2nd] ARM-EXECUTE §4 |
| dispositions | AUTO-CONTINUE (probe / bench / governance / calendar / fold); NEEDS-THE-CHAIR (READY verdict, public moves, RFC upstream) | [2nd] ARM-EXECUTE §5–§6 |

## 3 · THE ENTROPY CLASSES (the sweep's core)
- **DEAD SURFACE — the phantom-branch class.** Local HEAD `af584b8a0a` is a 14-commit pilot-side tank-lane line; `git merge-base` with the wire is empty; the wire tip names it. *Countermove:* stop treating the local line as the branch — declare it a disposable pilot tank, or rebase onto the wire (blocked by orphan lineage). [1st] IN-LANE + [2nd] `7f99a01eff`.
- **LOOSE THREAD — FLEET-CYCLE-BODY label/file mismatch.** Wire commit `6295dcfb02` is message-labeled `20261122T032905Z`, but the archived file is `FLEET-CYCLE-BODY-20261122T032507Z.md`; the wire tip tree carries `032507Z`, no `032905Z`. *Countermove:* byte-verify each archive's filename against its commit label before push. [1st] IN-LANE.
- **LOOSE THREAD — the 0240 "ABSENT" mis-receipt.** The 0240 artifact names `NEGENTROPY-ARM-EXECUTE-20261119.md` ABSENT; it is committed on both local HEAD and the wire. *Countermove:* re-receive the arming record before naming it absent. [1st] IN-LANE.
- **FRICTION — disk map trails wire map.** `MISSION-MAP-20261118.md` blob `41cbc99f` (local) vs `c498df75` (wire); the wire tip receipts "258 vs 265 lines". *Countermove:* re-sync the map from the wire tree via git, never a disk `ls`. [1st] IN-LANE + [2nd] `7f99a01eff`.
- **FRICTION — the read-burn gate makes the disk-map check un-receivable [1st].** Non-git terminal is refused, so the map must be a git `ls-tree`/`ls-files` single source. *Countermove:* wire the map check to `git ls-tree`. [1st] IN-LANE.
- **UNSPOKEN — the wire posture is "hold, not hold-safe".** The wire tip says "no next stage armed" and "hold, not hold-safe"; no fire-time hold-audit certified it this fire. *Countermove:* the next fire's hold-audit must name each seam explicitly. [2nd] `7f99a01eff` + ARM-EXECUTE §7.
- **UNSPOKEN — the two new wire FLEET-CYCLE-BODY archives are receipts-only.** They archive PR-body state; no lane is named to act on them. *Countermove:* name an owner or mark them reference-only. [1st] IN-LANE.

## 4 · THE ORDERED NEXT-MOVES
1. Re-sync the disk map from the wire tree (`git ls-tree`) — gate: the map blob hash matches the wire; seat: none.
2. Byte-verify the FLEET-CYCLE-BODY archive name vs its commit label — gate: next archive's filename == its message label; seat: none.
3. Resolve the phantom-branch: declare the local pilot tank disposable OR rebase — gate: `merge-base(local, wire)` non-empty, or a written disposal note; seat: head (lineage is a judgment).
4. Re-run the window-check trio when a harness is byte-verified — gate: a live harness receipt; seat: none.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- **deconstruct:** FIRED — six classes, each named with its countermove.
- **sense:** FIRED — the 0240 delta + the wire tip's ~22:3x row read as the baseline.
- **choose:** FIRED — the phantom-branch disposal is the pivot; the rest are receipts.
- **calibrate:** FIRED — git-tree hashes and commit labels, no estimates.
- **probe:** FIRED — the read-burn gate probed live (the refused call).
- **review:** FIRED — the 0240 ABSENT mis-receipt flagged, not hidden.
- **record:** FIRED — this artifact at the named path.
- **compose-check:** FIRED — the loop-state line below.

## 6 · THE LOOP-STATE LINE
`CONTINUE + re-sync the disk map from the wire tree (git ls-tree) and byte-verify the next FLEET-CYCLE-BODY archive name vs its commit label.` Receipt: this artifact + `7f99a01eff`.