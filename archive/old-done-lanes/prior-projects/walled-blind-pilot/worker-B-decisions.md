# DECISION BRIEF — Walled-Blind Compression Experiment
## Evidence-based decisions for the single-threaded owner (Ryan)

Status: research brief, prepared 2026-08-19 by independent investigator (Worker B). Not a summary of the six-pager, pattern doc, or wave-6 finding — those are used only as the statement of the open decisions. Every posture below is grounded in external sources listed inline and in the source list (§8). Tone: flat, neutral.

Scope of open decisions: (D1) adopting the ~52.9% lossless format-level compression; (D2) wave-7 instrument repair (B4 deletion control, B4 Part-2 anchor); (D3) larger-n permanence run (R5); (D4) replication as validation of the pattern; (D5) the local-LM judge port; (D6) ordering, under the frozen-record discipline (forward-only amendments, no retroactive changes).

---

## D1 — Adopting ~52.9% lossless format-level compression for agent envelopes

### Evidence from the field

**A pre-registered production compression trial exists and is directly on-point.** "Prompt Compression in Production Task Orchestration: A Pre-Registered Randomized Trial" (arXiv:2603.23525, Mar 2026) ran a six-arm, pre-registered RCT of prompt compression on production multi-agent task orchestration (358 complete-case Claude Sonnet 4.5 runs, 59–61 per arm, CONSORT-style reporting, a priori G\*Power planning). Findings: moderate compression (r≈0.5, the closest analog to this experiment's 52.9%) delivered a 27.9% mean total-cost reduction while sitting on the empirical cost–similarity Pareto frontier (embedding response-similarity ≥ 0.85); aggressive compression (r=0.2) was Pareto-dominated (higher cost *and* lower similarity); light compression (r=0.8) increased net cost in a pilot (output expansion 1.33× negating input savings). Its headline: **"compress more is not a reliable production heuristic," and output tokens must be treated as a first-class outcome** — net cost, not input savings, is the decision variable. It also documents the *ecological validity problem*: compression thresholds established on academic benchmarks do not transfer to production instruction distributions (their H5 threshold-alignment test was inconclusive on production data).

**Compression cliffs are task-type- and structure-dependent.** LLMLingua and successors (arXiv:2310.05736; LongLLMLingua arXiv:2310.06839; LLMLingua-2; Selective Context arXiv:2310.06839-family work, Li et al. 2023) report large ratios (up to 20×) with small benchmark loss, but also a plateau-then-drop ("not advisable above ~20×"), and benchmark-specific cliffs — the TAAC program the production trial extends found code tasks cliff below r=0.55 and CoT below r=0.70 (arXiv:2603.23525 §1.1). Structure-dense content is the fragile class: token pruning degraded text-to-SQL join accuracy from 0.63 to 0.37 while extractive methods held (industry survey, neuraltrust.ai prompt-compression guide). Format-level/manual restructuring (removing redundant prose, structured lists) is reported as the safest class — typically 20–40% reduction with zero quality loss — but always with per-task validation.

**Eval-driven development practice says adoption is an engineering decision gated by evals, not a research verdict.** Anthropic's "Demystifying evals for AI agents" (Jan 2026) frames regression evals as the precondition for shipping any behavior-affecting change (prompts, model swaps, orchestration logic), notes graders "require calibration with human graders for accuracy," and warns that "an eval at 100% tracks regressions but provides no signal for improvement" — near-ceiling suites detect regressions, not gains. Langfuse's evaluation-strategy guidance (2026) is explicit about the deployment loop: offline baseline → experiments → **CI gate** (a quality regression fails the build like a broken unit test; deterministic gates preferred) → production monitoring with sampled evaluators → close the loop by promoting only on experiment-plus-approval, with rollback. DeepEval's eval-driven-development material makes the same point: regression tests over a golden dataset run on every prompt/model/architecture change. Industry write-ups on shipping compression consistently recommend: start conservative, validate on a small traffic slice, ramp only while metrics hold, keep rollback (neuraltrust.ai; thread-transfer.com). Psychometrics adds a caution directly relevant here: near-ceiling distributions compress away sensitivity (ceiling-effect literature, e.g. Terwee et al. 2007 15%-rule; PMC2778494) — "no PASS↔FAIL movement at ceiling" is evidence against *large* damage only.

**What this means for the 52.9% number specifically:** W1's 12 cells support "lossless compaction is *plausibly* safe for this doctrine on this stack," not "safe in production." The wave-6 data (−1 integer deviations at 40% compression) show even mechanical format changes can move rubric scores. The field's comparable evidence base (the production trial) used ~60 cells per arm on real production instructions, and its own authors call that underpowered for null claims (planned 211/arm).

### Recommended posture: DO NOW, as a gated engineering change — not as a standing rule, and not "implement immediately"

The recommendation-in-the-six-pager ("a real stack candidate") is consistent with the field, but the field's precondition list is non-negotiable and this experiment already supplies most of it:

**Preconditions before any envelope format flips to the compressed form:**
1. **Per-domain regression eval.** The walled-blind protocol is the eval; run a sealed-packs regression pass on the actual envelope domain (real sub-agent tasks, real downstream outcomes), not only the doctrine cell corpus. Pre-registered decision rule: no PASS↔FAIL movement and no MARGINAL-band regressions on reserved cells vs. the frozen refs.
2. **Net-cost model, not input savings.** Measure output-token behavior and total cost (input+output) on the pilot slice; the production trial's output-expansion paradox (arXiv:2603.23525 §3.1, §4.1) makes input-only accounting actively dangerous. The 52.9% is an input-side number.
3. **Canary + rollback.** Ship to a small traffic slice first; promote only while the regression gate and monitoring hold; keep the full-prose envelope one re-label away.
4. **Monitoring.** Sampled judge scoring on production envelopes (the W6 instrument, serial dispatch) plus alerting on score distribution shifts (flat distribution = judge stopped discriminating — Deepchecks calibration guide).
5. **Respect the standing rule.** KEEP FULL PROSE for lossy paths is untouched by this decision; D1 concerns the format-level envelope only.

**Reasoning:** Production prompt-compression evidence supports moderate (~50%) compression as the empirically good operating point — this experiment's number is squarely in the field's safe zone — but every credible source conditions adoption on per-domain validation, regression gating, monitoring, and rollback, and warns that benchmark-derived safety does not transfer. The rig to satisfy those conditions already exists here; the cost is one prereg + one gated rollout, not a research program. Skipping the preconditions would turn a well-measured result into an unmeasured production change, which is precisely what eval-driven-development practice exists to prevent.

---

## D2 — Wave-7 instrument repair (B4 deletion control blind; B4 Part-2 anchor drift)

### Evidence from the field

**Negative-control design is a mature methodology, and it is explicit that a control that fails to bite is a design defect, not a pass.** The canonical treatment — Lipsitch, Tchetgen Tchetgen & Cohen, "Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies" (Epidemiology 2010; PMC3053408) — argues negative controls are the routine laboratory precaution for detecting *suspected and unsuspected* sources of spurious inference, distinguishes exposure- vs outcome-controls, and specifies the conditions under which a control is informative (it must be constructed so the hypothesized mechanism is forced to operate on it). A scoping review of the negative-control literature (J Clin Epidemiol 2023; Sciencedirect S0895435623003189) confirms the three uses — bias detection, calibration, correction — with detection as the primary one. Applied here: DEL-b4 did not force the mechanism (the hedge-drop span is not load-bearing under B4's Part-2 rubric as the grader applied it), so the control could not detect. The repair direction the field supports is exactly what the wave-7 draft already proposes: redesign the span so the rubric's load-bearing elements are amputated (or add an explicit Part-2 hedge-required cue), i.e., make the control's bite condition coincide with what the grader's rubric actually rewards. Anthropic's eval guidance carries the same principle at the task level: "make sure the problems are hard enough for the model" — a control that is too easy (or too far from the rubric's teeth) grades blind.

**Anchor drift is a known, named failure mode with a known remedy.** The judge-drift/rubric-drift literature (e.g., rubric-based eval analyses, medium.com/adnanmasood rubric-drift write-up; Deepchecks "LLM-as-a-Judge Calibration," Mar 2026; LangChain "How to Calibrate LLM-as-Judge") defines rubric drift as the effective meaning of a criterion shifting as examples and anchors accumulate, making historical scores incomparable. The prescribed detection mechanism is exactly what this experiment already built: **periodic recalibration against a frozen historical labeled set — if re-grading historical items produces different scores, drift has occurred.** The wave-6 ref-anchor leg is that mechanism, and it fired. The prescribed remedy is equally standard: re-verify/re-establish the anchor (either recalibrate the rubric's B4 Part-2 anchor under current text, or re-examine the reference answer bytes), then pin the corrected anchor in the rubric so the next wave cannot drift — and, where comparability matters, consider score recalibration (affine/Platt-style) or an explicit comparability caveat. The wave-6 handling (frozen datum stands; divergence reported; repair queued as a pre-committed amendment) matches the field's strongest practice: do not patch drift silently — the FORRT replication handbook and preregistration norms (Brandt et al. 2014; Willroth & Atherton 2024) treat post hoc correction as the cardinal sin; forward-only amendment is the sanctioned path. One additional field note: judge score drift (same answer, different score tomorrow — Deepchecks) and prompt sensitivity of judges mean the *grader leg* as well as the *anchor* should be pinned (judge model version + rubric version recorded per wave) — the wave-6 finding already records judge identity implicitly; making it an explicit manifest field is cheap and standard.

### Recommended posture: DO NOW — this is the smallest, highest-leverage pen stroke available

**Preconditions:**
1. Wave-7 proceeds as a pre-committed amendment via §7 (the draft already exists with the A1/A2 consult objections folded; the field supports both the redesign and the anchor re-verification as amendment items, never retroactive patches).
2. The B4 deletion control redesign is accepted as a *fix*, not a re-run: the DEL-b4 INCONCLUSIVE stays on the record; wave-7 introduces the corrected control for forward waves (P2 pillar of the pattern: "a non-firing transform is accepted, not re-drawn" — same logic applies to a non-biting control).
3. Anchor resolution: re-verify the reference answer bytes AND re-establish the B4 Part-2 anchor under the current rubric; pin the winner in the rubric; record the frozen 13/15 datum's status (superseded vs. reaffirmed) explicitly in the manifest.
4. Keep the solo/serial dispatch pacing fix (524 timeouts are infrastructure, not grades).

**Reasoning:** Every downstream decision (D1 adoption evidence, R5 permanence, D5 judge port) reads through this instrument. A blind deletion control on B4 and an unanchored B4 Part-2 mean the B4 family's numbers carry a comparability caveat that only wave-7 can retire. The field's negative-control literature says a non-biting control is a defect to fix; the drift literature says re-verify the reference against frozen labels and pin it. Both fixes are cheap, pre-committed, and already drafted. Doing anything else first means building on an instrument with a known blind spot.

---

## D3 — Larger-n permanence run (R5)

### Evidence from the field

**Sample-size norms for LLM evals are now quantitative, and the current n is far below them.** Miller, "Adding Error Bars to Evals" (arXiv:2411.00640, Anthropic, Nov 2024) gives the field's sample-size formula: n = (z_α/2 + z_β)² (ω² + σ²_A/K_A + σ²_B/K_B) / δ², with a worked example: detecting δ = 0.03 at 80% power needs n ≈ 969 → "new evals should contain at least 1,000 questions"; and resampling answers (K = 1 → 10) cuts the minimum detectable effect from 13.2% to 7.5% at fixed n = 198. Practitioner analyses agree: with 100 examples the minimum detectable effect at 80% power is ~10–12 percentage points; ~500–1,000 examples detect ~5-point differences (tianpan.co, 2026); a 2-point delta needs ~6,300/arm, a 7-point delta ~480/arm (dev.to eval-sizing analysis, 2026). The production compression trial planned n = 211/arm (G\*Power, medium f) and realized 59–61/arm after API censoring — and its authors explicitly warn that their null claims are underpowered and must be read cautiously (arXiv:2603.23525 §2.7.5).

**Applied to the 0.10–0.20 rubric-delta thresholds:** the P7 rulebook thresholds (within 0.10 of reference = PRESERVED; 0.11–0.20 = MARGINAL) are below what n ≈ 17 cells can resolve. Under Miller's formula with plausible variance for 0–3 part scores (between-cell variance term ω² ≈ 0.2–0.4), detecting a 0.10 mean delta at 80% power needs on the order of 80–400 cells (paired), a 0.20 delta roughly 20–100. For pass-rate-style deltas (binomial, p ≈ 0.85), a 10-point delta needs ~150–200 per arm; a 20-point delta ~70 per arm (standard two-proportion power; consistent with the practitioner numbers above). The wave-6 observed deviation class (−1 integer step ≈ 0.33 scale points on a 0–3 part) sits at the boundary of what 17 cells can even see — W6 can honestly claim "no PASS↔FAIL movement," not "no effect ≥ 0.10."

**Ceiling effects cap what any n buys.** Near-ceiling distributions (17/17 PASS, 12–15 of 15) compress the scale's discrimination at the top (psychometrics: ceiling-effect rule of thumb ≈ 15% of scores at the maximum, Terwee et al. 2007; PMC2778494). A larger-n run on the same near-ceiling rubric will detect regressions better but still cannot measure *improvement* headroom; if the permanence question is "does compression ever hurt at the margin," the rubric's sensitivity at the ceiling is part of the instrument design to state up front.

**Replication norms also argue for larger n, not the original n.** The FORRT replication handbook (§6.2) is explicit that informative replications need *larger* samples than originals (small-telescopes: 2.5× original for 80% power, 4.5× for 95% power, because a replication must be able to rule out the original's effect, not merely re-find it).

### Recommended posture: PARK WITH TRIGGER — size it to the question, and only with sign-off

**Trigger:** the permanence claim becomes load-bearing. Concretely: (a) D1 adoption moves past canary and becomes a standing stack property, (b) the 52.9% figure is quoted externally (Stanford share, write-up), or (c) the wave-7-repaired instrument produces a result the team wants to treat as settled for this domain.

**Preconditions (when triggered):**
1. Wave-7 must land first — R5 on a blind B4 control and drifting anchor inherits both limitations.
2. Size from the decision, not from habit: paired design, judge resampling K ≥ 3–5 (cuts MDE ~2× at fixed n — Miller), and n on the order of 100–400 cells per arm if 0.10 deltas matter, 20–100 if only 0.20 deltas matter; report standard errors per the Miller recommendations (SE with every mean, paired differences, clustered SEs if cells are grouped by behavior).
3. Pre-commit the permanence criterion (e.g., "no part drops ≥ 0.10 at any point ≤ 52.9% savings, 80% power") in the prereg; a permanence claim is a null claim and needs the power to support a null.
4. Keep it a separate commitment with its own prereg and manifest — it must not touch frozen wave-1–6 values.

**Reasoning:** The field's numbers are unambiguous that 17 cells (or 12 for W1) cannot support a permanence claim at the rulebook's own 0.10 threshold; the production-compression literature's own null claims at ~60/arm are called underpowered. But R5's value is conditional — if nothing downstream needs the permanence claim, the run is optional forward work, matching the six-pager's own framing ("not a hidden debt"). The trigger discipline converts that optionality into a decision rule instead of a habit.

---

## D4 — Replication as validation ("the pattern is proven the second time")

### Evidence from the field

**The empirical replication base is the sobering half of this question.** The Reproducibility Project: Psychology (Open Science Collaboration, Science 2015, doi:10.1126/science.aac4716) found 97% of original studies reported significant effects but only 36% of replications did, with replication effects averaging half the magnitude of originals; Many Labs 2 reported ~50%. The lesson generally drawn is not "distrust everything" but that *single demonstrations are weak evidence* and effect sizes shrink on replication — which is precisely why the six-pager's posture ("one successful application" = case study, not proven pattern) is the field-aligned reading.

**Standards bodies are concrete about how many replications count as evidence.** The What Works Clearinghouse single-case design standards (WWC, ies.ed.gov/ncee/wwc/Document/229 and wwc_scd_key_criteria_011017.pdf) — the closest formal analog to a "pattern proven by repeated application on small units" — require, for an evidence rating: **at least 5 studies meeting design standards, conducted by at least 3 different research teams at 3 different institutions, with ≥ 20 cases combined**; within a study, "strong evidence" requires **at least three demonstrations of the effect**. Applied by analogy: one end-to-end application (W1–W6) is a demonstration; the pattern's own bar ("proven the second time") matches the *minimum* of the field's evidentiary ladder, not the top. The FORRT replication handbook adds the methodological rules: replication success criteria must be pre-specified (what counts as success/failure, stated in advance), deviations must be documented, and replications need larger samples than originals (see D3).

**For a methodology (vs. a result), the validation question is different and the bar is lower.** The pattern doc's replication target — "the same discipline with a different supervisor model and local endpoints" — is a *methodology transfer* claim, and its test is whether the same frozen packs yield the same verdicts. The literature on judge/model transfer (see D5) supports this as a testable equivalence claim rather than an article of faith, provided: same sealed packs, same rubric text, pre-registered verdict-equivalence criteria (e.g., per-cell verdict match rate ≥ threshold, no PRESERVED↔HURT flips on controls), and no re-drawing.

### Recommended posture: DO NOW, but sequenced — replication is the second application, and it is cheap here

**Preconditions:**
1. Pre-specify replication success criteria before running (FORRT): per-cell verdict agreement, control-bite agreement, seal round-trip, and what counts as failure.
2. The second application must be on a *different decision domain or at minimum a different task family* to test generalizability, not just the same packs twice (the pattern doc's own §4: "proven the second time it's applied to a different decision"; WWC's 3-team/3-institution rule is the strong-form target, and this rig cannot claim that — it can claim independent applications within one team).
3. Record the replication as its own prereg + manifest line; no amendments to waves 1–6.

**Reasoning:** The field says one demonstration is a case study, three is strong evidence, and five-plus across independent teams is evidence-based practice. The pattern doc's "second time" bar is the honest minimum — it converts the pattern from case study to replicated-in-one-setting. Given the rig exists and the cost is one prereg + one consult batch, the second application is the single cheapest validity upgrade available to this program. Note the boundary: replication validates the *pattern*; it does not by itself validate any compression result (that's D1/D3's job).

---

## D5 — Local small-model judges (Qwen3-class) for this grading

### Evidence from the field

**Small-model judges work, with three well-documented conditions: panels, calibration, and a capacity floor.**

*Panels beat single judges.* Verga et al., "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models" (arXiv:2404.18796, NeurIPS 2024): a panel of many smaller models outperforms a single large judge across three judge settings and six datasets, exhibits less intra-model bias (composition of disjoint model families), and costs >7× less. The position-bias study literature (e.g., "Judging the Judges: A Systematic Study of Position Bias," IJCNLP 2025; CALM bias framework, arXiv:2410.02736) independently supports majority voting across capable judges: instances where judges disagree are exactly the hard, bias-prone ones, and they are rare (<5%); agreement across multiple judges is the reliability signal.

*Capacity floor is real and quantifiable.* "Thinking Small Models are Efficient LLM Judges" (arXiv:2509.13332, Sep 2025) — a systematic study of Qwen3 models (0.6B/1.7B/4B) on RewardBench — found the 0.6B model fails to exceed 50% accuracy on hard judge tasks (sometimes below random); the 4B in *thinking mode* gains ~10.5 points over non-thinking at <2× FLOPs (vs. +4.5 points for 7-shot ICL at >8× FLOPs), and thinking-mode judges hold ~91% consistency under induced biases (positional, bandwagon, identity, diversity) vs ~85% for non-thinking. Their explicit conclusion: **a model-capacity threshold is a prerequisite for reliable judging; very small models should not be deployed as automated judges.** Rubric-guided judging, reference-based judging, and n-best aggregation help non-thinking models but do not close the gap. Related: Prometheus (arXiv:2310.08491) shows a fine-tuned 7B/13B judge can match or exceed GPT-4 on a domain — but only when fine-tuned on that domain; off-the-shelf small models do not carry that guarantee.

*Calibration against a human-gold set is the standard precondition.* MT-Bench established the reference point: GPT-4-as-judge reaches >80% agreement with humans, i.e., human–human agreement level (arXiv:2306.05685). The calibration literature (LangChain calibration guide; Deepchecks calibration analysis, Mar 2026; Anthropic "Demystifying evals") is uniform: judge scores must be validated against human-labeled examples before trust, judges drift (same answer, different scores across time/versions), and judge model + prompt versions must be tracked. This experiment already holds a locally unique asset for this: **the sealed wave-1–6 packs with frozen verdicts function as a domain-specific gold set** — a Qwen3 judge's agreement with those frozen verdicts is a direct, cheap calibration measurement for this exact task, before it grades anything new.

**Application to this program's plan (Qwen3-4B @ :8080; Qwen3-8B driver):** the field's conditions map cleanly: (1) use thinking mode (the 4B is the smallest model the study still found competent; non-thinking mode is measurably worse); (2) run judges as a jury (multiple Qwen variants / cross-family local models, majority verdict) rather than single legs, since single-judge legs are exactly where bias and variance live; (3) calibrate each judge against the frozen packs before trusting its grades; (4) keep the rubric + reference-anchor conditioning (both are supported mitigations in 2509.13332 and 2306.05685); (5) keep the serial-dispatch pacing fix — the 524 problem is infrastructure and would bite local endpoints harder under concurrency. One caution the pattern doc already encodes: the TRUEST lens (Gwen, 4B) is a consult lens, not a grader; the field evidence supports keeping advisory lenses advisory and putting panels + calibration on the grading path.

### Recommended posture: DO NOW, gated on wave-7 and on judge calibration

**Preconditions:**
1. Wave-7 first: porting to local judges on an instrument with a blind B4 control and drifting anchor would entangle judge effects with instrument effects.
2. Judge calibration pass before any grading duty: run each candidate local judge on the sealed wave packs; report agreement with frozen verdicts; pre-commit a minimum agreement bar (the MT-Bench 80% human-agreement figure is the field's reference level for trust).
3. Jury aggregation for graded cells (≥ 3 diverse local judges, majority verdict), not single-judge grading; inter-rater discipline (P8) retained and extended.
4. Thinking mode for all judge legs; rubric + reference-anchor conditioning retained; judge model version and prompt version recorded per wave (drift tracking).

**Reasoning:** The local-LM port is well supported by the field — panels of small models are a mainstream, validated evaluation pattern, and the specific Qwen3-4B in thinking mode is on the right side of the capacity threshold the literature documents. The failure modes are all known and all cheap to prevent: single-judge bias (jury), uncalibrated scores (frozen-pack calibration), non-thinking degradation (thinking mode), and version drift (manifest tracking). Done with those preconditions, the port doubles as D4's replication vehicle: same packs, new judges, same verdicts expected.

---

## D6 — Ordering the decisions (frozen-record-safe sequence)

### Evidence from the field

The field's two governing constraints: (a) **no post hoc correction** — preregistration norms (Brandt et al. 2014; FORRT §6.1) and the drift literature treat retroactive fixes as the cardinal error, and forward-only amendment as the sanctioned path; (b) **evidence before exposure** — eval-driven development (Anthropic 2026; Langfuse 2026) requires regression gates and monitoring before behavior-affecting production changes. Dependencies between the decisions, per the evidence above: D2 repairs the instrument that D3, D4, and D5 all read through; D5 (port) is D4's cheapest replication vehicle and needs a fixed instrument; D1's adoption evidence is strongest when read through a fixed instrument but is otherwise independent of R5 (canary + monitoring can carry it); R5 is only triggered by a permanence need.

### Recommended sequence (each step is a discrete pen stroke; nothing touches frozen values)

| # | Decision | Action | Gate / trigger |
|---|----------|--------|----------------|
| 1 | **D2 — Wave-7 instrument repair** | Sign the wave-7 prereg amendment (already drafted, consult objections folded); run B4 control redesign + anchor re-verification; pin the corrected anchor | Owner's pen; pre-committed amendment; no retroactive changes |
| 2 | **D5 — Local-LM judge port** | Calibrate Qwen3 judges against sealed wave packs; jury aggregation; thinking mode; serial dispatch | Wave-7 landed; calibration agreement bar met on frozen packs |
| 3 | **D4 — Second application (replication)** | Use the ported rig on a *different decision* with pre-specified success criteria; independent prereg + manifest line | Port calibrated; decision available (the pattern's "second time" bar) |
| 4 | **D1 — Lossless adoption, gated** | Per-domain regression eval → CI-style gate → canary slice → net-cost monitoring → promote with rollback; standing rule KEEP FULL PROSE untouched | Eval gates pass on the envelope domain; canary metrics hold; rollback one re-label away |
| 5 | **D3 — R5 permanence run (parked)** | Separate prereg; paired design, K ≥ 3–5 judge resampling, n sized to the 0.10/0.20 question (≈100–400 / ≈20–100 cells per arm); SE reporting | Only if permanence becomes load-bearing (adoption beyond canary, external quote, or post-wave-7 result to settle); explicit sign-off |

Rationale for the order: wave-7 first because every subsequent measurement reads through it (D2 is the only item that *repairs* evidence quality rather than consuming it). Port + replication next because they are cheap and they convert the pattern from case study to replicated method — the field's minimum bar (D4). Adoption gated after that, because the adoption evidence base (D1's preconditions) is strongest read through a fixed instrument and the field's practice is canary-plus-gate rather than wait-for-permanence. R5 last and conditional, because it is the only step whose value depends on a downstream need that may never arise; parking it with a trigger respects the six-pager's "not a hidden debt" framing while giving the owner a written decision rule instead of a vague future.

**Frozen-record integrity check:** Step 1 is an amendment (forward-only, pre-data). Steps 2–5 are new preregs and new manifest lines. No frozen wave-1–6 value is re-graded, re-drawn, or re-interpreted; the B4 13/15 datum stands or is superseded only by the wave-7 amendment's explicit anchor decision. The B4 relative-to-ref caveat stays on the record regardless of wave-7's outcome.

---

## Sources

1. arXiv:2603.23525 — Prompt Compression in Production Task Orchestration: A Pre-Registered Randomized Trial (2026).
2. arXiv:2411.00640 — Miller, Adding Error Bars to Evals (2024).
3. Anthropic — Demystifying evals for AI agents (engineering blog, Jan 2026).
4. Langfuse — How to build an LLM evaluation strategy; LLM Evaluation: Methods, Best Practices, Roadmap (2026).
5. DeepEval — Eval Driven Development (blog).
6. arXiv:2310.05736 (LLMLingua); arXiv:2310.06839 (LongLLMLingua); LLMLingua-2; Selective Context (Li et al. 2023); industry surveys (neuraltrust.ai, prompthub.us, thread-transfer.com).
7. Lipsitch, Tchetgen Tchetgen & Cohen — Negative Controls (Epidemiology 2010; PMC3053408); negative-controls scoping review (J Clin Epidemiol 2023).
8. Rubric/judge drift: medium.com/adnanmasood rubric-based evals; Deepchecks LLM-as-a-Judge Calibration (2026); LangChain How to Calibrate LLM-as-Judge.
9. arXiv:2404.18796 — Verga et al., Replacing Judges with Juries (NeurIPS 2024).
10. arXiv:2509.13332 — Thinking Small Models are Efficient LLM Judges (2025).
11. arXiv:2310.08491 — Prometheus; arXiv:2306.05685 — MT-Bench / Judging LLM-as-a-Judge.
12. arXiv:2410.02736 — CALM, Quantifying Biases in LLM-as-a-Judge; IJCNLP 2025 — Judging the Judges (position bias).
13. Open Science Collaboration 2015, Science 349: aac4716; Many Labs 2.
14. WWC Single-Case Design Technical Documentation and Key Criteria (ies.ed.gov/ncee/wwc/Document/229; wwc_scd_key_criteria_011017.pdf).
15. FORRT Replication Handbook, §6 Execution of Replications.
16. Ceiling effects: Terwee et al. 2007 (15% rule); PMC2778494.
17. Practitioner power analyses: tianpan.co (2026); dev.to eval-set sizing; Serdar et al. 2020 (PMC7745163).
