# NEGENTROPY-SWEEP-20261122-1446

seat: copycat lane — the recurring negentropy-sweep harness ride (no_agent arm)
branch: study/rfc-143379-rig-20261105 (local HEAD 4e5980100a; wire origin/study/rfc-143379-rig-20261105)
fire time: 2026-11-22 14:46 UTC
the gate: "the gate: nothing public without the user's word."
register: [1st] re-read by this lane this pass · [2nd] carried from a study doc, not re-derived · ABSENT+named · tags IN-LANE / BORROWED <source> / HEAD-RECON

## 1. THE WINDOW-CHECK (the gate)

| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | not-run — needs the isolation run's eval readout; terminal is git-only in-lane | [2nd] BORROWED NEGENTROPY-SWEEP-20261122-0441 §1 |
| k-term two-tier re-measure (baseline kept-rates 0.42/0.29/0.26/0.26, flat) | not-run — same | [2nd] BORROWED 20261122-0441 §1 |
| budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | not-run — same | [2nd] BORROWED 20261122-0441 §1 |

The standing contradiction (the sweep's core): the budget's class ordering presupposes differential keep-rates; the k-term's kept-rates are flat (0.42/0.29/0.26/0.26, span 0.26–0.42). The ordering may be measuring the wrong axis. Countermove: the two-tier re-measure — tier-1 = the budget's class axis, tier-2 = a keep-rate axis — to separate "class ordering" from "keep-rate ordering". Receipt: [2nd] BORROWED 20261122-0441 §1/§4.

## 2. THE SEAM-SCAN (every fire)

| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | reads worked this fire (read_file/list_dir succeeded until the write-gate at ~round 20); the seam is latent — the harness gates reads once the write-window opens | IN-LANE |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | not-run — needs the scribe tunnel / served stack; terminal git-only | ABSENT in-lane |
| token watcher single-source | arm script `substrate/monitors/negentropy-sweep-arm.sh` (seat probe → brief restore → duplicate-fire guard → nohup harness, --rounds 40); nightshift watcher commits HOLD rows (6afcddea4e "HOLD row (gauge — stage tokens unchanged, no dispatch; FIRES-FIELD: 0)"); the named token file `NEGENTROPY-LOOP-20261122` is ABSENT on the branch | IN-LANE + ABSENT |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | not-run — terminal git-only | ABSENT in-lane |
| dispositions | HOLD-SAFE — the arm holds; no public action; the gate holds | [2nd] BORROWED 20261122-0441 |

## 3. THE ENTROPY CLASSES (CTO freedom)

- DEAD SURFACE — the empty sentinel field: `git ls-tree -l` shows ~27 empty blobs (e69de29) named `*.md.sentinel` (NEGENTROPY-SWEEP-*, NEXT-SHIFT-PLAN-*, SWAP-A-ADVANCE-*, TRACK1-*, W2-ISOLATION-*). Countermove: one cleanup commit removing the empty sentinels (or a single `.sentinels/README`). IN-LANE.
- LOOSE THREAD — the absent loop-state token: `NEGENTROPY-LOOP-20261122` (named by the ARM file §2 as the watcher's `.last_complete`) is in neither the wire tree nor the studies dir. Countermove: land the token file on the branch or strike the reference — a named-but-absent source is the silent-skip class. IN-LANE + ABSENT.
- LOOSE THREAD — superseded contract: `tmp-artifacts/pr1-watcher-contract.md` (2026-11-05) seeds a PR-#1 comment-driven watcher convention the rig has superseded. Countermove: a one-line SUPERSEDED banner or an archive move. IN-LANE.
- FRICTION POINT — the read-gate budget: the harness closes reads at the write-window ("due within 13 rounds"), so a lane that burns reads early loses the delta baseline. Countermove: read the delta baseline FIRST (round 1). IN-LANE.
- UNSPOKEN — the wire/local skew: the wire is ahead of local HEAD (wire carries NEGENTROPY-SWEEP-20261121-0429 and -1032; local HEAD is 4e5980100a). "The last artifact on the branch" is ambiguous (two candidates). Countermove: the sweep names its delta baseline explicitly (the wire's latest) and logs the skew. IN-LANE.
- UNSPOKEN — the seat-probe silent-skip: the arm's seat probe failure exits 0 ("SKIPPED: the alpha's seat did not answer"), so a chronically dead seat yields a run of invisible skips that read as healthy. Countermove: a visible FAIL row after N consecutive seat-probe skips (the brief-absent path already fails loudly; the seat path should match). IN-LANE.
- THE PRIZE (unexpected) — the flat k-term: the budget's class ordering (3.00 > 2.83 > 2.33 > 2.00) and the k-term's flat kept-rates (0.42/0.29/0.26/0.26) cannot both be the operative axis. The unspoken: the budget may be ordering classes that are not differentially keepable. Countermove: the two-tier re-measure. [2nd] + IN-LANE.

## 4. THE ORDERED NEXT-MOVES

1. Name the delta baseline: the sweep cites NEGENTROPY-SWEEP-20261121-1032.md as the wire's latest and logs the local/wire skew. Gate: the branch. Seat: the sweep.
2. Re-measure the k-term two-tier (tier-1 class axis, tier-2 keep-rate axis). Gate: the eval harness (not in-lane). Seat: the eval lane.
3. Clean the empty sentinel field. Gate: the branch. Seat: the sweep.
4. Resolve the absent token: land NEGENTROPY-LOOP-20261122 or strike the ARM reference. Gate: the branch. Seat: the head/arm.
5. Make the seat-probe skip visible after N consecutive skips. Gate: the arm. Seat: the arm.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

1. delta baseline read — NEGENTROPY-SWEEP-20261121-1032.md + NEGENTROPY-ARM-EXECUTE-20261119.md (IN-LANE).
2. window-check — three standing items carried [2nd], not-run (git-only terminal).
3. seam-scan — five rows, one receipt each (IN-LANE / ABSENT).
4. entropy classes — seven findings, each named with its countermove.
5. ordered next-moves — five, each with action / gate / seat.
6. compose-check — this section, eight steps.
7. loop-state line — §6.
8. commit+push — the branch (pending this write).

## 6. THE LOOP-STATE LINE

CONTINUE + the k-term two-tier re-measure (the eval lane's next fire; tier-1 the budget's class axis, tier-2 a keep-rate axis) — receipt: [2nd] BORROWED 20261122-0441 §4 + IN-LANE §3.