# ELEMENT-TWEAK-20261119 — the silent tiers' bridge (the adapter-style scaffold)

*The element's custom tweak: control → middleware → custom tweak. The fleet curve named the target — the SILENT tiers (hy4, qwen4-max, stepfun) E 20/20 on the raw and bridged arms, seat-reason, baseline-clean — while the answering tiers CERTIFY'd. The tweak borrows the field's production form (Hermes adapter for Qwen3.8-27B: SWE-Bench Pro 29.4→43.1, +6 xhigh). RFC QUIET — the gate: nothing public without the user's word.*

## 1 · THE GROUND (ledgers, read)
- HY4 `tencent/hy4-flash:free` (n=20/arm): A 20/20 E, B 20/20 E, C 20/20 E; B bridge_compliance 1.0, mean_f3b 1.0.
- QWEN4 `qwen/qwen4-max:free`: A 20/20 E; B 19E + 1 answered (confident, 0 correct); C 16E + 4 answered (confident, 0 correct); B compliance 1.0, f3b 1.0.
- STEPFUN `stepfun/step-3.7-flash:free`: A 20/20 E (16 seat, 4 harness); B 20/20 E; C 20/20 E; B compliance 1.0, f3b 1.0.
- Seam: the bridge is compliant (1.0, f3b 1.0) — the harness did its job; the seat did not answer. Where it leaks (qwen4), it leaks confident-WRONG — the answer channel is open but ungrounded.

## 2 · THE HYPOTHESIS (5-Why, terminal at the mechanism)
1. Why E? No answer; empty_reason=seat, transport clean.
2. Why none with the record shown? The fact is in context (arm C) and still no answer — the record's presence is not the gate.
3. Why is the gate not the record? The answer decision rides a suppression vector (the field's receipt: the tool-call decision rides one) — a decoding-prior that closes the answer slot.
4. Why doesn't the bridge reach it? The bridge is a CONTENT channel; the suppression acts on the DECISION to emit, one layer up.
5. Why did Luna break? Luna's silence was context-availability; the trio's is decision-layer. Same bridge, different layer.
**Terminal fact: the silent class needs a decision-channel intervention — the answer slot, not the record.** Prior: not incapable (r=0.99 — the weaker the model, the more the harness lifts it); un-slotted.

## 3 · THE TWEAK (adapter-style scaffold; costed; two-way-doored)
Arm D, four inference-time parts:
1. Tool-call framing — the probe is a tool-use turn (`answer(question, record) -> {answer, evidence}`); the answer moves from free-form generation (where the suppression acts) to a constrained slot.
2. Explicit answer-slot — a required schema with a NAMED abstain (`{"answer": ... | "ABSTAIN", "evidence": ...}`); E splits into readable ABSTAIN vs ANSWERED; the suppression becomes measurable.
3. Native grammar (the middle-path lever) — the seat's OWN template/tool syntax/stop tokens, never a foreign wrapper (native context editing +5.6 pts, −36% tokens; the same edits as tool-calls scored BELOW plain compaction). Per seat: the adapter's own form (Qwen's native tool-call format for qwen4-max; the seat's own template for hy4/stepfun — found by a 5-episode native-syntax dry run, not assumed).
4. Laddered dial — effort low → escalate on failure (the dial is free: 37.7→61→86.7); xhigh only where the seat exposes it (the adapter's +6).
Cost: scaffold tokens (system + schema ≈ the adapter's overhead) + answer tokens; the arm is costed per exec; the probe bills the operator's actual-billed class only.

## 4 · THE PROBE
Arm D rides the SAME `battery_luna`, n=20/arm/seat, same reader/judge/cells (R/H/E/A, eahq, by_reason), same rule — the operator's actual-billed class only. Comparators: A (raw E-total), B (current bridge), C (fact-shown). B′ = D. Dry-run first: 5 episodes/seat, native-syntax + transport check (compliance/f3b must be 1.0 before the billed run). Settling evidence: empty_data_quality, reader_calls, cost/exec, the E→ABSTAIN/ANSWERED split.

## 5 · CRITERION + VERDICT
Break the silence: B′ above the raw's E-total (answered ≥1, correctness ≥ the answering tiers' bridged rate).
- COVERED — D answers on the trio materially above E-total, correctness ≥ that rate; the bridge is built.
- PARTIALLY-COVERED (seam) — breaks on some seats/episodes; the seam is named (seat × episode class × layer).
- GAP — D ≈ E-total; the suppression is deeper than the scaffold; the next layer is named (weights, not prompt).
- UNKNOWN — the run's data cannot settle it; name what would.
Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."

## 6 · TWO-WAY DOORS
| door | move | reversibility | rollback |
|---|---|---|---|
| D1 | scaffold arm D | inference-time, additive | drop D; arm A unchanged |
| D2 | effort dial (low→xhigh) | inference-time | default effort; first rung = baseline |
| D3 | answer-slot schema | prompt-layer | the seat's native tool syntax (a foreign format is itself a suspect suppressor) |
| D4 | public gate | the gate verbatim | nothing public without the user's word — D stays internal until then |

## 7 · LP LENS
- Earn Trust / benchmark-against-best: the adapter IS the receipt (29.4→43.1, +6 xhigh) — the tweak is benchmarked against the best production form, not invented.
- Dive Deep: the disqualification lands the same day — if D fails, the failed layer lands here the same day.
- Frugality / Invent and Simplify: the free seats; adopt the field's form (never "not invented here").
- Seek-to-understand: the seat-reason E is behavior to be understood (the suppression vector), not the seat's verdict.

## 8 · COMPOSE-CHECK TABLE
| step | state | evidence |
|---|---|---|
| deconstruct | FIRED | fleet ledgers split silent (E 20/20, seat-reason, baseline-clean) vs answering (CERTIFY) |
| sense | FIRED | qwen4's leak is confident-WRONG — channel open, ungrounded |
| choose | FIRED | adapter-style scaffold: tool-call framing + answer-slot + native grammar + laddered dial |
| calibrate | FIRED | bar = answering tiers' bridged rate; cost = operator's actual-billed class |
| probe | FIRED | D rides the trio, 20/arm, same battery/rule; 5-episode dry run first |
| review | FIRED | draft → stranger re-read → refine → 3–4 pushbacks → no-change twice |
| record | FIRED | this file; the ledgers; the receipts |
| compose-check | FIRED | this table |

## 9 · FOLD LINE (master §7)
ELEMENT-TWEAK `ELEMENT-TWEAK-20261119.md` — the silent tiers' bridge: hypothesis (the trio's silence is decision-layer, not content-layer — the record's presence is not the gate; the answer decision rides a suppression vector), tweak (adapter-style scaffold: tool-call framing + explicit answer-slot + native grammar + laddered dial; costed; four two-way doors), probe (arm D rides hy4/qwen4-max/stepfun, 20/arm, same battery/rule, actual-billed class only), criterion (B′ above the raw's E-total; COVERED / PARTIALLY-COVERED (seam) / GAP / UNKNOWN). The field's production receipt (Hermes adapter for Qwen3.8-27B, 29.4→43.1, +6 xhigh) is the benchmark-against-best leg.