# NEGENTROPY-SWEEP-20261122-1848

seat: recurring negentropy-sweep lane (copycat harness ride, cadence 2h, no_agent arm)
branch: study/rfc-143379-rig-20261105 · wire tip bb3b33c7b7 (2026-11-22 10:33:19 -0500)
fire time: 2026-11-22 18:48 UTC
the gate: "the gate: nothing public without the user's word."
register: [1st] = re-read by this lane this pass · [2nd] = carried from a study doc · ABSENT+named = not received. Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition (200/200 + model-judge 20/20) | not-run this window; done at L0 08:1x / L2 20:5x, but the wire's newest row (10:1x CADENCE) shows the settlement's refire #4 FIRED INCONCLUSIVE at the 200-sweep → the "done" is stale | BORROWED 1446 finding + wire MISSION-MAP tail [2nd] |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat) | not-run; no probe landed this window; the flat k-term still contradicts the budget's class ordering | BORROWED 1446 finding [2nd] |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | not-run; carried | BORROWED 1446 finding [2nd] |

The window-check's own source is the last sweep artifact (1446), 4h stale vs this fire; the live posture is the wire MISSION-MAP tail. Countermove in §3.

## 2. THE SEAM-SCAN
- read-burn harness-deadline seam — the 20261122-1814 arm patch (seat slot stamped per run id) + contents:write permission + process-scoped askpass landed; the arc 63/65/66/67 FAILURE → 68 `45037661047` SUCCESS. IN-LANE: terminal refused a non-git read ("terminal is git-only for lanes") → the push URL must ride GIT_ASKPASS, never host git-config mutation. BORROWED wire CADENCE row [2nd] + IN-LANE refusal.
- fold checks — read_file served the arm/brief/ARM from the scribe cell (source: scribe-cell) this pass [1st]; the loop-state token file receipts/loop-state-negentropy.jsonl is ABSENT on the branch (git ls-tree) → no byte-compare possible for the sweep's own loop-state line. ?raw=1 grep not-run (curl refused). The scribe-cell read path is the read-side evidence-plane verifier (SELD class).
- token watcher single-source line — name NEGENTROPY-LOOP-20261119-v2; its file ABSENT. A second name NEGENTROPY-LOOP-20261122 appears only in this lane's brief text, in no branch file → phantom.
- machine-layer wire-checks — scribe :24282 / Harbor :44831 / SSH 192.168.1.241: not-run (terminal git-only) → ABSENT + named; carried [2nd].
- dispositions — HOLD-SAFE (map coherent, sequence template intact); wire: "NO DISPATCH beyond the armed settlement fire — the sanity rides its seat; the FOLD/HY sequence holds." BORROWED wire CADENCE row [2nd]. The read-gate closure at 13 rounds is the write-gate L0 (DISCERN class); the commit-after-artifact order is the evidence-gated commit gate (AskALCF class).

## 3. THE ENTROPY CLASSES
- dead surface — the rig tree is 21,946 files with 157 empty (0-byte) [1st, git ls-tree -r -l]; the spine-dir subset was not re-counted (read-gate closed). Countermove: a standing `ls-tree -r -l | awk '$4==0'` census row, spine dirs only.
- loose threads — (a) the token file absent while its name is the watcher's standing single-source line: the sweep's loop-state line has no receipt file. (b) the phantom NEGENTROPY-LOOP-20261122 brief name. (c) the delta baseline (1446) is 4h stale; the wire MISSION-MAP tail is the live posture. Countermove: land the file or strike the name; stamp the token name from the watcher's output, not the brief; read the wire MISSION-MAP tail each fire.
- friction points — terminal is git-only for lanes: every curl/ssh wire-check is carried [2nd] forever. Countermove: a git-only wire-check set (ls-remote + ls-tree -r -l + cat-file) as the lane's native probes → wire-checks [1st] again.
- UNSPOKEN — the sweep's cadence gap (0441 → 1446 → 1848) means the 16:5x fire left no artifact; "every fire" is only as real as the arm's seat probe. Countermove: the arm receipts a skipped fire (stub bytes) so the cadence is auditable.
- PRIZE (unexpected) — the window-check's source is itself a stale single-source: 1446 says W2 "done", but the wire's newest row says the settlement refire #4 was INCONCLUSIVE. The sweep's gate section is reading a 4h-old artifact as the live state. Countermove: the window-check reads the wire MISSION-MAP tail + the settlement ledger each fire, and marks the last-sweep-artifact as [2nd] explicitly.

## 4. THE ORDERED NEXT-MOVES
1. Land receipts/loop-state-negentropy.jsonl (or strike the name) — gate: the single-source line resolves to a byte-receipted file — seat: negentropy-sweep.
2. Re-gate the settlement refire #4 (INCONCLUSIVE) on the W2 two-tier — gate: 200/200 + judge 20/20 — seat: settlement.
3. Adopt the git-only wire-check set — gate: every wire-check [1st] — seat: negentropy-sweep.
4. Arm a skipped-fire stub receipt — gate: every scheduled fire leaves bytes — seat: negentropy-sweep arm.
5. Run the spine-dir empty-file census — gate: row spine dirs only — seat: negentropy-sweep.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. header (seat/branch/fire/gate) — IN-LANE, this file.
2. gate verbatim — "nothing public without the user's word" — IN-LANE.
3. register tags — [1st]/[2nd]/ABSENT used per row — IN-LANE.
4. window-check table — 3 rows, each receipted — BORROWED 1446 + wire [2nd].
5. seam-scan rows — 5 rows, current state + receipt — IN-LANE + [2nd].
6. entropy classes — every finding named WITH its countermove — IN-LANE.
7. ordered next-moves — action/gate/seat each — IN-LANE.
8. loop-state line — CONTINUE + next move, receipted — IN-LANE.
(list form HEAD-RECON: the eight-step compose-check carried from the 1446 artifact, not re-derived.)

## 6. THE LOOP-STATE LINE
CONTINUE + land receipts/loop-state-negentropy.jsonl (or strike the watcher's single-source name) and re-gate the settlement refire #4 on the W2 two-tier. Receipt: this artifact on study/rfc-143379-rig-20261105; delta baseline NEGENTROPY-SWEEP-20261122-1446.md (6f4b1c6b0d); wire tip bb3b33c7b7.