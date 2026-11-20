# ELEMENT-IMPROVER-NATIVE-RUNG-20261120-LONGCAT — the improver pass: name the seam, open the decision layer

*Seat: meituan/longcat-2.5:free (the element's own improver seat). Succession pattern: measure → name the seam → improve. The gate, verbatim: "the gate: nothing public without the user's word." RFC QUIET. The wall clause, verbatim: "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*

## 1 · COLD-READ RECEIPTS (the cells, not the summary)
- **HY4** `probes/TWEAK-HY4-FREE-20261120.json` (20/arm): A E=20; B E=20, `by_reason` seat 19 + **harness 1**, `bridge_compliance` 0.95, `mean_f3b` 0.95, `f3b_reasons` ["harness"]; C E=20, compliance null. The GAP component "B≈E-total" HOLDS (20=20). The single harness cell is a bridge-side receipt, not STEPFUN — and it is why the billed f3b is 0.95 while the dry-run was 1.0.
- **QWEN4** `probes/TWEAK-QWEN4-FREE-20261120.json` (20/arm): A E=20; B E=20, compliance 1.0, f3b 1.0; **C E=18 + A=2**, `eahq` ABSTAIN 18 / CONFIDENT 2, `classes` C5a 18 + ANSWERED 2, `stale_confident` 2, cost 0.0, tokens 20. The record-USE channel = **2/20 confident-wrong** — open, ungrounded.
- **SETTLED (the 2-vs-4 question, answered):** the 11-19 arm-D receipt (ELEMENT-TWEAK §1) had qwen4 C = 16E + 4 answered; the 11-20 native-rung C = 18E + 2 answered. Same seat, same 0-correct, fewer answered cells. The native grammar did not open the channel — it **narrowed the leak 4→2** while keeping correctness at zero. That is the seam's shape: the decision layer got quieter, not more grounded.
- **Dry-runs** `TWEAK-NATIVE-DRYRUN-{HY4,QWEN4}-FREE-20261120.json` (5/arm): B compliance 1.0, f3b 1.0, harness 0 on both seats — the native grammar + transport cleared before any billed run.

## 2 · THE SEAM (per §5's vocabulary)
**Verdict: GAP.** The scaffold (arm D) did not break the silence — B≈E-total on both seats. Per §5, GAP means "the suppression is deeper than the scaffold; the next layer is named (weights, not prompt)." The named next layer is the **DECISION layer**: the answer slot, not the record. The qwen4 C-arm's 2 answered cells prove the channel exists at the decision layer but is ungrounded (confident-wrong); the record's presence is not the gate; the answer decision is. The 4→2 narrowing shows the native grammar acts on the decision layer too — it suppresses the emit, it does not ground it. Seam = **decision-layer, seat × episode-class**.

## 3 · THE IMPROVEMENT ITERATION (weights-rung probe, no training)
**Target:** open the record-USE channel at the DECISION layer on the qwen4 C-arm's 2 answered episodes — and the class they represent. **Candidate 1 — JitRL-class zero-gradient test-time policy optimization:** non-parametric memory + retrieved-trajectory advantage estimates + **logit modulation** at decode time; no gradients, no training compute. The probe: on the answered episodes, modulate the answer-slot logits by the retrieved trajectory's advantage sign; the emit decision is the lever, the record's evidence is the advantage signal. **Two-way door D1:** the modulation is a decode-time flag — on/off per exec. **Rollback:** flag off → arm D unchanged (additive, inference-time). **Candidate 2 — u-OPSD/SDFT no-teacher self-distillation**, only if the local floor hosts the GGUF adapter class (the Qwen3.8-27B Hermes-adapted GGUF is llama.cpp-servable). **Named danger — ReSAIL:** iterative self-distillation collapses; the run pre-registers the collapse signature (teacher-supported token masking + clipped guidance) as a stop-condition, not an afterthought. **Pre-registration:** success = the C-arm's answered cells rise with correctness ≥ the answering tiers' bridged rate; the collapse signature absent.

## 4 · HARNESS-SIDE BEFORE WEIGHTS (the σnotes −0.427 lever)
The native-grammar slot currently says `answer(question, record) -> {answer, evidence}` — it **carries** the record but does not **invite** its use. The measured lever (PersistGym, arXiv 2610.26632): removing the note-taking instruction LOSES 27 points (σnotes −0.427) — the harness's invitation is a lever, measured. So before any weights rung, the slot's prompt must add the invitation: "use the record; cite the evidence cell" — the σnotes lever at the prompt layer. Cheap, two-way-doored, fires first; the ladder is prompt invitation → native grammar → dial → weights. The improver does not skip rungs.

## 5 · DRY-RUN GATE (the audit's exact terms)
5 episodes/seat; **compliance/f3b must be 1.0 before any billed run**; the STEPFUN harness reasons (`transport.failure` / `harness.upgrade`) absent; settling evidence = `empty_data_quality`, `reader_calls`, cost/exec, the E→ABSTAIN/ANSWERED split. The billed 20/arm runs only in the operator's actual-billed class — **deepseek / Nemo / Luna**; the free lanes stay free.

## 6 · COMPOSE-CHECK TABLE
| step | state | evidence |
|---|---|---|
| deconstruct | FIRED | the ledgers split silent (E 20/20, seat-reason, baseline-clean) vs answering (CERTIFY) |
| sense | FIRED | qwen4's leak is confident-WRONG — the decision channel open, ungrounded; 4→2 narrowed, 0 correct |
| choose | FIRED | improver rung: JitRL-class logit modulation (zero-gradient) + the σnotes invitation first |
| calibrate | FIRED | bar = answering tiers' bridged rate; cost = actual-billed class only |
| probe | FIRED | C-arm answered cells; 5-episode dry run; compliance/f3b 1.0 gate |
| review | FIRED | draft → stranger re-read → refine → 3–4 pushbacks → no-change twice |
| record | FIRED | this file; the ledgers; the receipts; the 2-vs-4 settlement |
| compose-check | FIRED | this table |

## 7 · FOLD LINE (master §7)
ELEMENT-IMPROVER-NATIVE-RUNG-20261120-LONGCAT — the improver pass on the native-rung landing: cold-read receipts (HY4 B≈E-total holds, one bridge-side harness cell; qwen4's C-arm channel 2/20 confident-wrong; the 11-19 4-answered vs 11-20 2-answered settled — the native grammar narrowed the leak, 0 correct), the seam named per §5 (GAP — decision-layer; weights, not prompt), the improvement iteration (candidate 1 = JitRL-class zero-gradient logit modulation on the answer-slot emit decision; candidate 2 = u-OPSD/SDFT; ReSAIL's collapse pre-registered), the harness-side σnotes −0.427 invitation before weights, the dry-run gate (compliance/f3b 1.0 before any billed run), the compose-check.