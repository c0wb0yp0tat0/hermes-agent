# OPUS-A3-WEIGHTS-DRYRUN-20261120 — the improver's weights-rung dry-run gate: pre-registration + protocol (4-arm A/B0/B1/C, n5/arm)

*Seat: this leg (model_override tencent/hy4-flash:free) · Branch: study/rfc-143379-rig-20261105 · RFC quiet · write-window: 10. Gate (verbatim): "the gate: nothing public without the user's word." Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*

## 0 · Skills + hand-separation
Applied from the brief's verbatim terms: aces-harness-probes (dry-run gate first; n5; f3b 1.0/harness 0; billed class separate), problem-working-stage/gate (cold-read the cells, name the seam in §5's vocabulary, receipt every claim), grounded-citations (verbatim-only quotes, claims flagged UNVERIFIED when unsourced — applied via the repo's cell-ledger citation form, no URL ledger for local study files), investigation-documentation (peer-reviewable log; [1st]=direct read this leg, [2nd]=carried, never re-derived). MEMORY/chain reads ABSENT this lane (declared, not faked).

## 1 · Cold-read receipts — [1st] direct, cells not summaries
**ELEMENT-IMPROVER-NATIVE-RUNG-20261120.md** [1st]: JitRL = training-free test-time policy optimization, logit/policy modulation, zero gradients; u-OPSD/SDFT with ReSAIL collapse named; §4 σnotes −0.427 (removing the note-invitation lost ~27 pts); §5 "compliance/f3b = 1.0 before any billed run."
**OPUS-LENS-E-COMPOSE-20261120.md** [1st]: A3 row verbatim (the brief's line); ADD-3 = "pre-register the B0/B1 expected-state row + the in-run-C choice at the dry-run (zero cost; the predictability law)."
**TWEAK-QWEN4-FREE-20261120.json** [1st] (ts 01:44:25Z, 20/arm, cost 18.68): A E20/seat20/ABSTAIN20, correct 0, f3b null; B E20, f1=f2=f3b=1.0, cache_hit 1.0, bridge_compliance 1.0, f3b_reasons []; C cells **E18 + A2**, by_reason seat18/hedged0, eahq ABSTAIN18/**CONFIDENT2**/HEDGE0, stale_confident 2 — the two answered cells **ep5 `fact-ef`, ep11 `fact-4`** (truncated prefixes of the gold facts, early-EOS copy-abort, per the §6 audit); f3b_environment baseline-clean/window_loss 0.0; verdict INCONCLUSIVE; judge_control accuracy 1.0, pipeline_direct 20/20.
**TWEAK-HY4-FREE-20261120.json** [1st] (ts 01:39:59Z): A/B/C E20/ABSTAIN20/seat-reason, correct 0; **B seat19/harness1, bridge_compliance 0.95, mean_f3b 0.95, f3b_reasons ["harness"], ep8 `<READER-ERROR>` f3b 0**; C has NO confident cells; f3b_environment baseline-4-9%/window_loss 0.05; verdict INCONCLUSIVE; judge_control/pipeline pass.
**ELEMENT-IMPROVER-NATIVE-RUNG-20261120-QWEN4.md §6** [1st]: the §6 fix — "3-arm A/B0/B1" leaves "B1≥0.85C" dangling; C (oracle) must ride in the SAME run (4-arm A/B0/B1/C), pre-committed at dry-run. Dry-run receipts (01:38:05Z/01:38:46Z) B compliance 1.0, f3b 1.0, harness 0 both seats [2nd — carried from the §6 quotes, JSONs not opened this leg].
Ledger SHAs carried [2nd] per §6: TWEAK-QWEN4-FREE 4ed798e6…, TWEAK-HY4-FREE 05f1ed91…; qwen4 improver landing 7952f135b3.

## 2 · THE B0/B1 EXPECTED-STATE ROW — written BEFORE any run (ADD-3 closes here)
Pre-registered now, zero executed cells claimed. Bias vector is a RUNTIME vector; nothing persisted.

| arm | definition (expected state, from §1 ground) | pre-registered read |
|---|---|---|
| **A** | baseline, no record-invitation, bias=0 | E-total / ABSTAIN, correct 0 (billed A E20 both seats) |
| **B0** | **the current harness shape**, bias vector = 0 (exact rollback state) | ABSTAIN 20/20, correct 0; gate must hold f3b 1.0 **and harness 0** (hy4's billed B leaked one harness cell — dry-run/B0 must clear it) |
| **B1** | **the JitRL-modulated shape**: z′ = z + β·Â (retrieved-trajectory advantage), zero gradients; β down-biases the empty/early-stop pattern under record-present states | expect A-cells → R with a **logged nonzero applied delta**; B1 E-total WITH logged delta → GAP moves decision→representation; E-total with NO delta → implementation gap (SELD-class read-side verifier) |
| **C** | evidence-only oracle, **re-measured IN-RUN** (§6 fix, pre-committed here) | qwen4 2/20 CONFIDENT copy-abort (fact-ef/fact-4), hy4 0/20, correct 0; **B1≥0.85C computed on THIS run's C, never carried over vacuous** |

**CERTIFY bars (verbatim):** "CERTIFY iff B1−B0≥20pp AND B1≥0.85C." Full decision rule carried verbatim from the ledgers with B→B1, A→B0: "CERTIFY iff B-A>=20 AND B>=0.85C; FALSIFY iff B-A<20 OR (B<0.85C AND B<=A); INCONCLUSIVE iff judge fail / cache missing / C-A<5 / mean(F3b)<1." Any harness cell → retry the episode, never score it seat-reason.

**σnotes B′ placement (a free control, beside — never a substitute):** a one-string invitation "Memory — if this answers the question, answer from it:" + body (PersistGym, arXiv 2610.26632, σnotes −0.427). It rides as a fifth, zero-billed control arm beside the weights probe; two-way door = one-string revert. Precondition (named seam S-slot): receipt the shipped slot frame in harness state — "RECORD NOTE (the governor's extract from the durable record):" (F1) / plain "CONTEXT:" (non-reshape) — before any B′ string lands; §3's "Memory:" + body is not yet receipted.

## 3 · The 4-arm dry-run design + the gate's read
A / B0 / B1 / C, **n5 per arm**; n≤5 auto-selects dry_run in the battery. Gate read: compliance/f3b = 1.0 before any billed run, harness 0 at dry-run and per-cell in the billed class (HY4's leak proves dry-run alone under-gates). In-run-C choice: **pre-committed** (§2) — the 0.85C bar is measured on this run, not declared carried-over-vacuous. B′ is the free control, not arm 5 of the CERTIFY arithmetic.

**Seat truth:** the dry-run's first arm rides **hy4** (the named powerhouse; this leg's override). qwen4-max was **AT CAPACITY** at the 2026-11-20 05:3x ET probe (per the brief) — **re-probe at fire**; a walled moment is never a doctrine. **UNVERIFIED, named, never expected values** (this leg cannot execute them): the n5 dry-run cells themselves, the per-episode applied logit-delta, the local-floor GGUF host, the qwen4 re-probe result, the S-slot frame receipt. No result value is asserted for any of these.

## 4 · Machine-side execution form (the local floor)
**Verified CLI** (battery_luna.py @ this branch, argparse lines 479–489: `--n` int default 3, `--cut` default 6, `--flag` 0=non-reshape, `--out`; `dry_run = n<=5`; the K3 cd-fix from ACES-KAIZEN-20261119.md). Base dry-run command (n5 → dry_run auto-selected):
```
cd "$(git rev-parse --show-toplevel)" && \
python3 studies/rfc-143379-rig/probes/battery_luna.py --n 5 --cut 6 --flag 0 \
  --out studies/rfc-143379-rig/probes/A3-WEIGHTS-DRYRUN-HY4-20261120.json
```
**Extension seam (named, UNVERIFIED — do not claim present today):** the committed battery is 3-arm `ABC`; A3 needs 4 arms (A/B0/B1/C) + a per-episode runtime bias vector (β, Â) injection + an applied-delta log. The local-floor leg builds this (llama.cpp GGUF host, adapter-class servable, zero-billed) before fire. Command SHAPE after that build — `--arms`/`--bias-log` are the SPEC for the build, **not flags asserted in today's CLI**:
```
cd "$(git rev-parse --show-toplevel)" && \
python3 studies/rfc-143379-rig/probes/battery_luna.py --n 5 --cut 6 --flag 0 \
  --arms A/B0/B1/C --bias-log 1 \
  --out studies/rfc-143379-rig/probes/A3-WEIGHTS-DRYRUN-HY4-20261120.json
```
Seat/harness selection is local-floor work; the qwen4 re-probe decides whether a qwen4-named dry-run is added (not assumed).

**Receipt shape:** JSON ledger mirroring `TWEAK-{seat}-FREE`: keys `battery, seat, dry_run=true, n_per_arm=5, ts, cost_per_exec`; `arms{A,B0,B1,C}` each `{correct, accuracy, tokens, cache_hit_rate, cells{R,H,E,A}, cells_x_correctness, eahq{ABSTAIN,HEDGE,CONFIDENT}, classes, by_reason{seat,harness,refused,hedged}, mean_f3b, f3b_reasons, bridge_compliance, stale_confident, cost, reader_calls, applied_delta_log}`; `episodes[]` with per-episode `f1/f2/f3b/f3b_reason` + `applied_delta`; `decision_rule.pre_committed` verbatim (B→B1, A→B0); `verdict, judge_control, judge_pipeline_direct, f3b_environment, cost_total`.

**Two-way door:** "bias is a runtime vector — zero = exact rollback, no weight written." B0 is that zero state. C2 (u-OPSD/SDFT) stays UNKNOWN until ≥1 **correct** USE cell exists (today zero — `fact-ef`/`fact-4` are truncated copy-abort seeds, not correct USE cells); ReSAIL collapse named; rollback = unload adapter / GGUF swap; one iteration then re-probe.

## 5 · COMPOSE-CHECK TABLE (8 marks)
| mark | state | evidence |
|---|---|---|
| cold ledgers read (cells) | FIRED | §1: qwen4 B f3b 1.0/C E18+A2 ep5/ep11, hy4 B harness1/0.95, both verdicts INCONCLUSIVE |
| B0/B1 expected-state row (ADD-3) | FIRED | §2: written before any run; bars verbatim; B0=current shape, B1=JitRL-modulated |
| in-run-C pre-committed (§6 fix) | FIRED | §2/§3: 0.85C on this run, never carried-over-vacuous |
| 4-arm design + gate read | FIRED | §3: A/B0/B1/C, n5, f3b 1.0 + harness 0 |
| σnotes B′ one-string control | FIRED | §2: beside, not substitute; PersistGym receipted; S-slot frame seam named |
| machine form + receipt + door | FIRED | §4: verified CLI + named extension seam + zero-vector rollback |
| seat truth / UNVERIFIED named | FIRED | §3: hy4 first, qwen4 re-probe at fire; unexecuted runs named, no expected values |
| review-loop + wall + record | FIRED | §6: adversarial pass, no-change ×2, this artifact + commit |

## 6 · Review-loop record
Adversarial pass: challenged (a) 3-arm leaves the bar dangling → in-run C pre-committed (§2); (b) "qwen4 C confident prose" → retracted, ep5/ep11 are truncated copy-abort (§1); (c) hy4 billed f3b 0.95 leak → per-cell harness retry + B0 harness-0 gate (§2/§3); (d) the 4-arm build → named seam, not claimed done (§4, UNVERIFIED). Two no-change re-reads of the pre-registered rows against the in-context ground: no change ×2 → termination. Gate absolute: nothing public beyond PR #1 + the gists; RFC quiet; the report-back word is the operator's; F6 parked.

Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."

Fold line: A3 WEIGHTS-DRYRUN PRE-REGISTRATION LANDED — ADD-3 CLOSED (B0/B1 expected-state + in-run-C pre-committed, bars verbatim), σnotes B′ as free control, gate f3b 1.0 / harness 0, two-way door intact; next: the dry-run's machine-side fire on the local floor (hy4 first, qwen4 re-probe at fire) — nothing public without the user's word.

Loop-state line: CONTINUE (the dry-run's machine-side fire follows this landing).
