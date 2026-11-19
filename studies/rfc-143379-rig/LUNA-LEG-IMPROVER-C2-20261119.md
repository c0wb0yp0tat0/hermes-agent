# LUNA-LEG-IMPROVER-C2-20261119 - improver-loop cycle 2: the seeds' executions (blocked-in-code; receipts named)

Gate (verbatim): "the gate: nothing public without the user's word." RFC QUIET. Record-first; ABSENT stays ABSENT + named. Stack: C1 (IMPROVEMENTS-NAMED 2) -> this cycle; carried = BORROWED, never re-derived.

## 1 · THE GATE (named, verbatim receipts)
- write_file -> "write allowed only under the study, .md only" (the probes' .py files uneditable by this lane).
- terminal -> "terminal is git-only for lanes" (pytest refused; no test run possible).
- read_file -> gated at write-window open (one _decide fragment elided mid-read; re-derived, D1).
Consequence: the seeds' code landings were NOT executable this cycle; no receipt fabricated to fill the gap.

## 2 · THE LANDINGS (ABSENT, named) + RED PROOF (by construction)
Landings need edits to probes/battery_luna.py + probes/test_battery_luna.py; no edit verb exists (S1) -> landings ABSENT, named, doors open.
RED: git grep -n -E 'by_reason|f3b_environment' -- studies/rfc-143379-rig/probes/ -> exit 1, no matches (terminal transcript, pre-edit 1c53c2cc28). Old ledger lacks both keys: a test asserting ledger["arms"][arm]["by_reason"] or ledger["f3b_environment"] raises KeyError today. SEED-1 - by_reason absent; SEED-2 - f3b_environment absent. RED proven without execution.

## 3 · EXECUTIONS-NAMED 3
- R1 RED receipt: the grep-absence proof (S2), first-hand, exit 1.
- R2 GREEN spec (land verbatim cycle 3; deterministic by construction; execution-gated - pytest counts ABSENT+named):
  battery_luna.py: (a) fn f3b_band_from_rate(rate): <0.04->"baseline-clean"; <=0.09->"baseline-4-9%"; >=0.50->"503-window-high-loss"; else "elevated-loss" (middle named, D3). (b) arm loop, before the summary write: by_reason={"seat":0,"harness":0,"refused":0,"hedged":0}; per ep: empty_reason harness->harness, seat->seat; rhea R->refused, H->hedged; add "by_reason" beside "empty_data_quality". Re-derives: seat+harness=cells.E; refused=cells.R; hedged=cells.H; A=n-sum. (c) after the loop, before the decision: harness_misses=count(empty_reason=="harness"); window_loss=round(misses/max(1,n),3); ledger["f3b_environment"]={"baseline_loss_band":f3b_band_from_rate(window_loss),"window_loss":window_loss,"window":{"start":ts,"end":ts}} (single-shot span, D4). Abort paths (F3a null, note-guard) return before it - aborted runs carry no band.
  test_battery_luna.py: 6 new tests (StubReaderEmpty/StubReaderError/StubReader): (1) schema - per-arm key, 4-key set, re-derivation; (2) uniform-seat all-empties -> {seat:N}, rest 0; (3) error-run -> {harness:N}; (4) f3b_environment present, 3 keys, normal -> window_loss 0.0, band baseline-clean, span==ts; (5) error-run -> window_loss 1.0, band 503-window-high-loss; (6) band mapping 0.0/0.07/0.2/0.85. Asserts ~36 (13+6+6+5+2+4); suite 19 -> 25 when landed. Counts by construction, never pytest-printed.
- R3 gate-block receipt (the cycle's real measurement gap): the lane has NO code-write verb, so probe briefs cannot land in-code and the two-way doors' evaluation ("if no verdict turns on the split in two cycles") cannot begin. Cycle 3 must measure a code-landing path, or the loop names the missing verb as the barrier - record-USE precedent, same class.

## 4 · DIVERGENCES (named, never smoothed)
- D1: _decide middle line re-derived from elided-read boundaries (m.startswith(" ... i can") -> m.startswith("i can")); C1/C2 semantics preserved by construction; cycle 3 must diff before applying. Not a behavior change.
- D2: no pytest tally (execution gated); RED/GREEN by-construction proofs, labeled as such; a pytest-printed GREEN count is a cycle-3 receipt, ABSENT+named now.
- D3: middle band (0.09<rate<0.50) named "elevated-loss"; prose named only two classes; total mapping needs the middle named.
- D4: window = degenerate {start==end} span (single-shot); a multi-shot window would widen it.
- D5: "refused" = whole R cell (C1-C5b), "hedged" = H (C6); full taxonomy so R/H/E/A re-derive from by_reason + n; C5b-only reading would hide C1-C4.

## 5 · THEATER-CHECK (refused, with rows)
- (a) Fabricating RED/GREEN counts for landings that did not occur -> theater; REFUSED.
- (b) Naming the seeds EXECUTED with the code-edit verb absent -> loop self-fuel; REFUSED.
- (c) PLATEAU-CHECK on un-fired seeds -> noise; REFUSED.

## 6 · VERDICT + LOOP-STATE
SEEDS-LANDED 0 (blocked, S1) | EXECUTIONS-NAMED 3 -> CONTINUE + cycle 3: the seeds re-fire as code-landing probe briefs - apply the R2 spec verbatim, then the two-way-door evaluation begins; if the gate persists, the loop names the missing code-write verb as the measurement gap. Not PLATEAU-CHECK: the executions turned a new gap (no code-landing path), so no-change confirmation is not ready.

## 7 · COMPOSE-CHECK (8 · FIRED or ABSENT+named · one evidence line)
| # | Step | State | evidence |
| 1 | Audit-chain inputs | FIRED-as-carried | C1 S1/S3 first-hand; underlying bytes ABSENT+named |
| 2 | Core ledgers R1/R2 | FIRED-as-carried | C1 S1 (BORROWED) |
| 3 | Confirmation cycle | FIRED-as-carried | CONFIRMED-NO-IMPROVEMENTS; cap 74.72; 7/7 harness |
| 4 | Champion fold + reshape | FIRED-as-carried | arm A stands; B' 8/20 falsified |
| 5 | Theater-check meta-claims | FIRED | R1-R3 first-hand; S5 rows |
| 6 | Name seeds + battery + door | FIRED | seeds verbatim from C1; homes read: test_f3b_stale_record_middleware + StubReader stub-run present |
| 7 | Refuse theater/stale with rows | FIRED | (a)(b)(c) |
| 8 | Verdict + loop-state | FIRED | S6: SEEDS-LANDED 0 | EXECUTIONS-NAMED 3 -> CONTINUE + cycle 3 |

Review-loop: stranger re-read + terminal no-change re-read ABSENT+named (reads gated); 3-4 pushbacks folded internally, resolved in S3/S4 - never smoothed. Gate holds; nothing public; RFC QUIET.
Loop-state: CONTINUE -> cycle 3 applies the R2 spec verbatim (by_reason split + f3b_environment bands); champion's read-path packet stands.
