# NEGENTROPY-SWEEP-20261122-0642 — the recurring sweep

**seat:** recurring negentropy-sweep lane (no_agent arm, cadence 2h) · **branch:** study/rfc-143379-rig-20261105 · **fire time:** 2026-11-22 06:42 · **the gate (verbatim):** "the gate: nothing public without the user's word."

**the register (binding):** [1st] = re-read by this lane this pass (git-tree, study listings, branch logs, the read tool's scribe-cell reads); [2nd] = carried from a study doc, not re-derived; ABSENT + named = a file/fact that could not be received, never invented. Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1 · THE WINDOW-CHECK (the gate)
Carried [2nd] from NEGENTROPY-SWEEP-20261122-0441 §1 (BORROWED 0441). This arm has no eval surface; the items stay parked.

| window item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | not-run-why: needs the rig's W2 eval surface; not this sweep's arm | BORROWED 0441 §1 |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it) | not-run-why: needs the k-term harness; the contradiction stands unnamed by any lane | BORROWED 0441 §1 |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | not-run-why: carried ordering, no re-measure | BORROWED 0441 §1 |

## 2 · THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | LIVE this pass: the read-tools refused once the write-window opened (READ-GATED, "the artifact's due within 13 rounds"); the ≤6,000-char/section + write-early discipline is the countermove | IN-LANE |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | the read tool's source is the scribe cell (observed on every study read); the write-time byte-assert is the harness's, not this lane's — this lane can commit, not self-verify | IN-LANE (read source) + BORROWED arming §2 |
| token watcher's single-source line | arming §1 names NEGENTROPY-ARM-EXECUTE-20261119.md as THE line; no UPDATED line appended since 2026-11-19 — unchanged | BORROWED arming §1 |
| root `loop-state-0f23bc3b-token.txt` | ABSENT + named: not in HEAD (`ls-tree HEAD -- <path>` empty; `cat-file` fatal), not on disk (`diff --no-index` "Could not access") | IN-LANE |
| machine-layer wire-checks (scribe tunnel :24282, runners, Harbor :44831, SSH 192.168.1.241) | carried from 0441 (Harbor LIVE, SSH REACHABLE, disk 29%); not re-run — terminal is git-only this pass; stale-by-one-window | BORROWED 0441 §2 |
| dispositions | AUTO-CONTINUE (fold+scribe+rows; calendar re-surveys) / HOLD-SAFE (this sweep: artifacts only, no public move) / NEEDS-THE-CHAIR (the READY verdict; any public move; the RFC upstream's quiet) | BORROWED arming §5–6 |

## 3 · THE ENTROPY CLASSES (the sweep's core)
- **dead surface:** the root `loop-state-0f23bc3b-token.txt` — named by 0441 §5, absent from HEAD and disk. Countermove: track it or strike the reference; the watcher must name one source.
- **loose thread (resolved):** 0441's phantom-branch (local af584b8a0a, empty merge-base vs wire 7f99a01eff). This pass: `git rev-list --count HEAD..FETCH_HEAD` = 1 and `FETCH_HEAD..HEAD` = 0 → merge-base = HEAD cb3e339b22; wire 7a61e7a9b1 = HEAD + 1 (fleet-cycle-body 20261122T063520Z). RESOLVED. Countermove: drop the friction row, keep the resolution receipt. IN-LANE.
- **loose thread (carried-unverified):** 0441's MISSION-MAP local blob c24f07d9… vs wire da45df46… — not re-grepped this pass (read-gated). Countermove: next sweep's first read re-greps the served blob. BORROWED 0441 §5.
- **friction point:** the read-burn seam (§2) — the sweep's own reads are gated at the write-window; the skeleton-by-round-3 rule is the only defense. Countermove: keep it.
- **UNSPOKEN:** the sweep lane cannot verify its own fold — it writes and commits; the scribe cell byte-compare is the harness's assert. The artifact's landing is trusted, not seen. Countermove: the next sweep's first read byte-compares the prior artifact's scribe cell vs disk.
- **UNSPOKEN (the prize):** the gauge's provenance is unnamed. 0441 §6 asserts "gauge stage tokens unchanged (80,131 / 78,455 / 116,972)" and the nightshift-watcher commits repeat "gauge — stage tokens unchanged, no dispatch" — but no readable artifact names the gauge's source file, and the one candidate (`loop-state-0f23bc3b-token.txt`) is ABSENT. The HOLD rests on numbers whose source cannot be received. Countermove: the next watcher UPDATED line names the gauge's source path, or the HOLD is downgraded to HOLD-WITH-NAMED-SEAMS. IN-LANE + BORROWED 0441 §6.
- **storm-context corroboration (class, not adoption):** the dispositions are a three-state delegation (AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR); the parked window items are stage-decoupled evaluation; the unnamed gauge is a validity-decay risk; the read-gate is compile-time gating. The sweep's design stays its own.

## 4 · THE ORDERED NEXT-MOVES
1. Name the gauge's source (or retire the root token file) — gate: the watcher's next UPDATED line — seat: head/watcher.
2. Re-grep the served MISSION-MAP blob vs local (c24f07d9 vs da45df46) — gate: next sweep's read window — seat: sweep.
3. Byte-compare the prior artifact's scribe cell vs disk — gate: next sweep's read window — seat: sweep.
4. Keep the window items parked until the rig's eval surfaces fire — gate: the eval surfaces — seat: rig.
5. Keep write-early (skeleton by round 3, ≤6,000 chars/write) — gate: every fire — seat: sweep.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- deconstruct: FIRED — the six sections, each row receipted (this file).
- sense: FIRED — the 0441 delta + the arming record + the live wire state (merge-base receipt).
- choose: FIRED — the phantom-branch resolved; the gauge provenance named the prize.
- calibrate: FIRED — git rev-parse/rev-list counts, ls-tree, cat-file fatal, diff --no-index; no estimate.
- probe: FIRED — the read-gate hit live; the root token file probed (ABSENT).
- review: FIRED — the ABSENT + named discipline held; nothing invented.
- record: FIRED — this artifact, committed + pushed below.
- compose-check: FIRED — the loop-state line receipts the next move.

## 6 · THE LOOP-STATE LINE
`CONTINUE + the next sweep's first read re-greps the served MISSION-MAP blob (c24f07d9 vs da45df46) and byte-compares the prior artifact's scribe cell vs disk; the gauge's source is named by the watcher's next UPDATED line.` Receipt: IN-LANE (wire merge-base, read-gate, root-token ABSENT) + BORROWED 0441 §5–6, arming §1.