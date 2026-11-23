# NEGENTROPY-SWEEP-20261122-2250 — the recurring sweep's fire (no_agent arm)

**Seat:** the recurring negentropy-sweep lane — the scheduled harness ride (cadence 2h, no_agent arm; probe per `/root/.hermes/scripts/negentropy-sweep-arm.sh`, not seat-pinned this pass). **Branch:** `study/rfc-143379-rig-20261105` · **Fire time:** 2026-11-22T22:50Z · **Gate (verbatim):** "the gate: nothing public without the user's word." · **Register:** receipts, never claims; **[1st]** = re-read by this lane this pass, **[2nd]** = carried from a study doc; unreceivable facts stay **ABSENT + named**; tags IN-LANE / BORROWED / HEAD-RECON. Delta baseline: `NEGENTROPY-SWEEP-20261120-2049.md` [1st read].

## 1. THE WINDOW-CHECK (the gate)
Carried [2nd] from the last sweep; re-checked against the tree this pass [1st: `git ls-tree -r --name-only HEAD | grep …`].

| windowed item | state this fire | receipt |
|---|---|---|
| W2-isolation settle-condition | **ANSWERED-PARTIAL, not settled.** Fire #5 rode a FRESH window (HTTP 200 at spawn): **14/20 HTTP 200 + 6/20 HTTP 429**; the content-void PERSISTS (13 null-200 reasoning-exhaustion + 1 visible-but-INCORRECT `"fact"`). Verdict UNKNOWN. | `WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md` §FIRE #5 (`b00e4a45e4`) [1st] |
| k-term two-tier re-measure | **NOT-RUN.** No k-term/two-tier artifact in the tree [1st: 0 hits]. Baseline [2nd]: kept-rates 0.42/0.29/0.26/0.26 flat (0.26–0.42) — contradicts the budget's differential-keep-rate ordering. | 2049 sweep §1 [2nd] |
| budget consolidation re-verify | **NOT-RUN.** No budget-consolidation study artifact [1st]; tree holds only code/test `budget*` files. Baseline [2nd]: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. | 2049 sweep §1 [2nd] |

Window status: the window did not close; the sweep fired. Fire #5 MOVES the W2 question — from "is the wall structural?" to "does reasoning finish under the immutable 24-token budget?" Answer: once in 20 calls.

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt | disposition |
|---|---|---|---|
| read-burn harness-deadline seam | MISSION-5 SELD write-gate L0 was 11/12 green [2nd]; NEW: MISSION-5 sanity **DEFECTS-NAMED** (`938d1e2239`) → HY gate **APPROVE** (`8c6db54c83`). No new red receipt this fire. | `plan/tank/MISSION-5-SANITY-20261122.md`, `plan/tank/HY-GATE-MISSION5-20261122.md` [1st] | AUTO-CONTINUE |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | **ABSENT + named** — no fold/scribe/get_memory artifact in the tree [1st: 0 hits]. | — | HOLD-SAFE |
| token watcher's single-source line | **ABSENT + named** — the loop-state token's file is not on the branch [1st]. | — | NEEDS-THE-CHAIR (auto-path: name the bearer) |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | Refire #5's two-way door is the live receipt: GGUF `afa0567d…` unchanged (5,780,092,000 B), zero weights, harness hashes restore; live re-hash 18.4s. | refire §F5.2/§F5.8 [1st] | AUTO-CONTINUE |

Dispositions: **AUTO-CONTINUE** (read-burn seam, machine layer) · **HOLD-SAFE** (fold checks — no bearer) · **NEEDS-THE-CHAIR** (token-watcher bearer; headroom-sweep 360m destructive `rm -rf`, an opened MISSION-5 carrier).

## 3. THE ENTROPY CLASSES (CTO freedom applies)
- **Dead surface:** the loop-state token's file — ABSENT, no bearer [1st]. *Countermove:* name the bearer or retire the sentinel.
- **Loose thread — stale artifact shape:** the refire record (76,677 → 184,846 B) now APPENDS fire #4 (`597d4d198a`) and fire #5 (`b00e4a45e4`), but its H1/title still reads "(fire #3)" with **no top-level index pointer**; a reader landing at the top sees a 20/20 wall and must know to scroll to line 2261. The 2049 "headline-vs-commit" catch is RESOLVED-BY-APPEND, but discoverability remains a gap. *Countermove:* a one-line top pointer to the appended fires.
- **Loose thread — orphan sentinel:** `headroom-sweep.sh` = an 11th script-bearing job (`no_agent=null`, model `upstage/solar-mini4:free`) whose destructive pre-run `rm -rf` fires every 360m; MISSION-5 ruled it a carrier, not a fold-gap. Still unmonitored. *Countermove:* keep it a named operator question (deep-deletion-class proximity).
- **Friction point — shared-branch advance:** local HEAD `b00e4a45e4` vs wire `f1e1fb4339` (`git ls-remote origin`) — refs differ; the push will need `pull --rebase`. *Countermove:* the emission contract's rebase clause.
- **UNSPOKEN — the prize:** fire #5's fresh window produced CONTENT on exactly ONE call, a **truncated prefix** of the gold (`"fact"` ⊂ `fact-5feceb66ffc8`), graded `correct=false, stale_confident=1, f1=f2=f3b=1`. So the wall is per-call STOCHASTIC (reasoning 22 vs 24 at temperature 0), not absolute — and the one crack leaks an INCORRECT answer the partial-credit metric rewards. Three premises stack against settlement at n5/dry-run: the budget's differential-keep-rate ordering, the flat k-term, and stochastic-24 exhaustion (C degenerate, 5/5 null). *Countermove:* name both carriers — (i) a PRE-REG-LEVEL budget/seat amendment is the only settling lever (the head's/fold's call, never this lane's improvisation); (ii) the metric-calibration gap (a wrong 4-byte truncation scores full partial-credit).
- **Storm-context (class-level):** write-gate L0 (DISCERN) rides MISSION-5; the stale-headline thread is validity-decay; AUTO/HOLD/NEEDS-THE-CHAIR is three-state delegation. Design stays ours; corroboration only.

## 4. THE ORDERED NEXT-MOVES
1. **Land this artifact + commit + push** — gate: commit succeeds on `study/rfc-143379-rig-20261105`; seat: this lane.
2. **Carry the truncation-metric carrier** (wrong answer scores f1=f2=f3b=1) to the fold — gate: fold's next pass; seat: the fold.
3. **Top-pointer on the refire record** (fires #4/#5 appended; H1 still fire #3) — gate: refire lane's next append; seat: the refire lane.
4. **Re-row the three windowed items** (W2-isolation, k-term two-tier, budget consolidation) — gate: the window; seat: head/fold.
5. **Headroom-sweep 360m destructive `rm -rf`** — gate: the operator's word; seat: NEEDS-THE-CHAIR.
6. **Token-watcher bearer** — gate: the chair names the file; seat: NEEDS-THE-CHAIR.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. Ground read — IN-LANE `read_file` of the 2049 sweep, refire §FIRE #5, MISSION-5 sanity + HY gate.
2. Adjudication formed — IN-LANE: three windowed items re-checked at the tree (k-term/budget 0 hits; W2 answered-partial by fire #5).
3. Register tagged — IN-LANE [1st] (git-tree / ls-remote / read_file) vs [2nd] (carried baselines).
4. Wrote early, one artifact — this file, one write.
5. Commit + push once — pending (emission contract; `pull --rebase` on rejection).
6. Never invented — ABSENT + named: fold checks, loop-state token.
7. Nothing public — RFC #143379 / #5320 / #157065 QUIET; no posts; artifacts only.
8. Loop-state line — §6.

## 6. THE LOOP-STATE LINE
**CONTINUE +** carry the three unrowed windowed items (W2-isolation, k-term two-tier, budget consolidation) and the truncation-metric carrier to the fold's next pass; the token-watcher bearer and the fold-check bearer stay ABSENT + named. Receipt: this artifact + commit on `study/rfc-143379-rig-20261105`.
