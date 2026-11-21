# NEGENTROPY-SWEEP-20261121-1836 — the recurring sweep

- SEAT: the recurring negentropy-sweep lane (scheduled harness ride, no_agent arm, cadence 2h)
- BRANCH: study/rfc-143379-rig · FIRE TIME: 2026-11-21 18:36 EST
- THE GATE (verbatim): "the gate: nothing public without the user's word."
- THE REGISTER: [1st] = re-read by this lane this pass (git-tree / ls-tree / branch logs); [2nd] = carried from a study doc, not re-derived; ABSENT + named = a file/fact that could not be received. Tags: IN-LANE / BORROWED <source> / HEAD-RECON.

## 1 · THE WINDOW-CHECK (the gate)
| Item | State | Receipt |
|---|---|---|
| W2-isolation settle-condition | NOT RUN — gated on the W2 isolation arm's land; no window opened this pass | [2nd] 1434 sweep; the arm's land is the trigger |
| k-term two-tier re-measure | NOT RUN — surface ABSENT. `probes/BATTERY-FULL-LEDGER-20261119.json` absent at HEAD [1st]; successor `probes/A3-BP-A-PLAIN-QWEN4-20261121.json` is `dry_run: true`, `reshape: false`, no kept-rate field [1st] | IN-LANE ls-tree + read |
| budget consolidation re-verify (3.00 > 2.83 > 2.33 > 2.00) | NOT RUN — carried; the new `audit/COST-LEDGER-20261121.md` is a token-economics ledger, not the budget's class-ordering re-verify | [2nd] 1434; IN-LANE read of COST-LEDGER |

## 2 · THE SEAM-SCAN
| Seam | Current state | Receipt |
|---|---|---|
| read-burn harness-deadline | OPEN THIS PASS — the read-gate fired mid-analysis ("write-window is open; the artifact's due within 13 rounds"); the sweep's own read-burn is the seam it watches, and it bit this fire | IN-LANE (the READ-GATED refusal) |
| fold (a) artifact on disk | PENDING — written by this fire | IN-LANE |
| fold (b) scribe cell → get_memory byte-compare | NOT RUN — terminal is git-only; no get_memory | IN-LANE |
| fold (c) served `?raw=1` grep | NOT RUN — terminal is git-only | IN-LANE |
| fold (d) commit + push | PENDING | IN-LANE |
| fold (e) row to PR #1 | N/A — sweep lanes are artifacts-only; never posts | IN-LANE |
| token watcher single-source line | BROKEN — registry fragmented to 4 surfaces: root, `audit/`, `court/`, `probes/` [1st]; the arming names `NEGENTROPY-ARM-EXECUTE-20261119.md` as the single source [2nd]; the map `NIGHTSHIFT-STATE-MAP-20261121.md` is ABSENT [1st] | IN-LANE ls-tree |
| machine-layer wire-checks | NOT RUN (git-only); carried: scribe :24282 REACHABLE, Harbor :44831 LIVE, SSH 192.168.1.241 REACHABLE | [2nd] ARM-EXECUTE §4 |
| dispositions | HOLD-SAFE — artifacts only; nothing public | IN-LANE |

## 3 · THE ENTROPY CLASSES
- **Dead surface — the map's mis-receipt.** The 1434 sweep cited `night-20261121/NIGHTSHIFT-STATE-MAP-20261121.md` (lines 35, 95-97) as committed. At HEAD it is ABSENT; `night-20261121/` holds only the four BRIEFs + `NIGHTSHIFT-PLAN-20261121.md` [1st]. Countermove: re-derive the map's facts from the plan; never cite the map again.
- **Loose thread — the 4-surface registry.** Four `SCRIBE-WITNESS-REGISTRY.log` copies (root/audit/court/probes) [1st]; the arming standardized ONE token source. A row landing in one copy and not the others is a silent divergence. Countermove: name root canonical, mirror the rest.
- **Loose thread — the 1434 sweep's double-landing.** Two registry rows for `NEGENTROPY-SWEEP-20261121-1434.md`, different hashes (8d52e023…, c5cce51a…) [1st]. Same filename, two versions; the append-only log can't tell which is the landing. Countermove: record the FINAL hash once; amend via a new timestamped file.
- **Friction — the k-term surface is still ABSENT and its successor is a dry-run.** [1st] Countermove: rebuild the kept-rate ledger or re-scope the window item to the dry-run's actual fields (accuracy / cache_hit_rate / cost) and retire the k-term framing.
- **Loose thread — the dirty tree.** `git status`: `M MISSION-BRIEF-MASTER-20261119.md`, `?? audit/MASTER-HITL-GIST-HEAD-DRAFT-20261121.md` [1st]. The 1434 "clean tree" claim is stale. Countermove: `git add` ONLY the artifact path; never swallow the head's draft.
- **Loose thread — the COST-LEDGER's TUNE lever is unrowed.** The new ledger names per-lane standing-context duplication (31:1 prompt:completion; longcat 815,205 prompt tokens) and recommends TUNE [1st, BORROWED COST-LEDGER §6]. No follow-up rows it. Countermove: row it as a next-move.
- **UNSPOKEN — the LOSS-LADDER's 0.65 contradiction.** At depth 0.65 the window keeps only the user-stated head (anchors/receipts 0.000); 0.8 is the minimum for anchors' markers; receipts stay 0.000 at every depth [1st, BORROWED LOSS-LADDER]. The rig's 0.65 band is head-only. Countermove: name it to the compression/budget work.
- **NEEDS-THE-CHAIR — the untracked head-draft.** `audit/MASTER-HITL-GIST-HEAD-DRAFT-20261121.md` is the RFC's public surface; the gate is the user's word [1st]. Countermove: the chair's, never the sweep's.
- **Storm-context (corroboration of class, not adoption):** DISCERN's write-gate L0 bit this fire (the read-gate); SELD's read-side evidence-plane maps to the fold checks; AskALCF's commit gate maps to the commit+push; the four misc (compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation) are noted for the next arc.

## 4 · THE ORDERED NEXT-MOVES
1. Re-derive the map's facts from the plan; retire the map citation. Gate: next window-check. Seat: sweep.
2. Name root the canonical registry; mirror/merge the other three. Gate: the fold. Seat: head.
3. Rebuild or re-scope the k-term surface. Gate: the window-check. Seat: budget lane.
4. Row the COST-LEDGER TUNE lever (per-lane prompt footprint). Gate: next arc. Seat: ACES/economics.
5. Commit this artifact with `git add` of ONLY the artifact path. Gate: the commit. Seat: sweep.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- deconstruct: FIRED — the window-check + seam-scan + entropy classes, each receipted.
- sense: FIRED — the delta since 1434 read at HEAD (ls-tree, reads).
- choose: FIRED — the map mis-receipt named, not smoothed.
- calibrate: FIRED — live receipts (ls-tree, git status, the READ-GATED refusal); no estimate.
- probe: FIRED — the k-term surface probed (ABSENT) and the successor read.
- review: FIRED — the dirty tree + double-landing named as seams.
- record: FIRED — this file; commit + push below.
- compose-check: FIRED — the next sweep re-checks this fire's rows.

## 6 · THE LOOP-STATE LINE
`CONTINUE + re-derive the map's facts from the plan and retire the map citation (next window-check).` Receipt: this artifact, committed + pushed.