# WORKER B — DECISION BRIEF v2 — Walled-Blind Compression Pilot

> Scope: independent research on the six open decision classes — lossless adoption,
> wave-7 instrument repair, larger-n permanence run (R5), replication, local-LM
> judge port, and ordering — against current field evidence. Companion to the
> six-pager (DRAFT, owner's pen pending) and the wave-6 finding. All online claims
> carry their URL. Nothing here changes a frozen value; every recommendation is
> forward-only.
>
> Method: web discovery + primary-source reading via the browser harness
> (qutebrowser CDP on 127.0.0.1:9222, `goto_url`/`wait_for_load`/targeted `js()`
> extraction). No page required CAPTCHA/login bypass; none attempted.

---

## A. Adopting ~52% lossless format-level compression for agent envelopes

**Posture: PARK with trigger — hold as a recommendation, do not implement now.**

### Evidence from the field

1. **Format is a behavioral variable, not a cosmetic one.** "Does Prompt Formatting
   Have Any Impact on LLM Performance?" (arXiv:2411.10541) reports large,
   statistically significant performance spreads between plain-text, Markdown,
   JSON and YAML prompt formats — e.g. MMLU 59.7 (JSON) vs 50.0 (Markdown) for one
   model; FIND 15.9 (plain text) vs 5.2 (Markdown) for another. The authors find
   the sensitivity is general across skill domains, not tied to task difficulty.
   Implication: a transform that preserves *semantics* byte-for-byte is not
   guaranteed to preserve *behavior*; format-level compression is still a
   treatment.
2. **Format-removal is mostly safe on average but model-sensitive in the details.**
   "The Hidden Cost of Readability: How Code Formatting Silently Consumes Your
   LLM Budget" (arXiv:2508.13666) removes whitespace/indentation/newlines from
   FIM code prompts across 10 LLMs: ~24.5% input-token reduction with performance
   largely unchanged on average — but per-element ablations show sharp
   model-specific failures (e.g. Gemini-1.5 Pass@1 falls 67.2% → 11.1% in C++
   when individual formatting elements are removed). The average hides the
   sensitive model.
3. **Compression benefit is operating-window-dependent.** "Prompt Compression in
   the Wild" (arXiv:2604.02985, 30,000+ end-to-end runs, 7B–70B models, three GPU
   classes) finds response quality "statistically unchanged" only inside a
   matched window of prompt length, compression ratio and hardware; outside it
   the compression step dominates and cancels latency gains; the largest gains
   appear beyond ~5k-token prompts. The envelopes in this pilot are short
   doctrine texts; a 52.9% token cut may buy little or no latency/cost in that
   regime. The paper's profiler exists precisely because the break-even point is
   not a given.
4. **Semantic compression increases hallucination; load-bearing words are hard to
   predict.** "An Empirical Study on Prompt Compression for LLMs" (ICLR 2025,
   arXiv:2505.00019) shows all six studied compressors raise hallucination
   (altered-semantic and information-loss types), with information loss the
   primary trigger, and concludes "even words that seem less informative can play
   notable roles". This study targets token-pruning/semantic compression rather
   than format-only edits, but it sets the burden of proof for any compression
   claim: fidelity must be demonstrated on the *behavior that consumes the
   envelope*, not on text similarity.
5. **Adoption discipline in production evals.** Anthropic's agent-evals guidance
   ("Demystifying evals for AI agents", anthropic.com/engineering/demystifying-evals-for-ai-agents)
   distinguishes capability evals (low pass rate, hill to climb) from regression
   evals (~100% pass rate, run continuously to catch drift after launch), and
   notes an eval at 100% "tracks regressions but provides no signal for
   improvement". Its framework: tasks × multiple trials per task (outputs vary),
   graders over transcripts and outcomes. CI gating practice (Langfuse,
   langfuse.com/resources/engineering/ai-agent-evaluation and
   /golden-dataset-evaluation; DeepEval/Confident AI; Galtea,
   galtea.ai/blog/llm-evaluation-complete-guide) is uniform: a versioned golden
   dataset + evaluators + a threshold gate that fails the pipeline on regression,
   run on every PR that touches prompts or models. Galtea gives concrete norms:
   ~50 items detect large regressions, ~200 give confidence on 3–5% changes,
   >500 is diminishing returns.

### Recommended posture and preconditions

PARK. The W1 result (52.9% savings, fidelity 12/12, positive control biting) is a
well-measured *capability* result — one task family, one rubric, one point in
time, one stack. The field evidence above says the safe unit of adoption is not
the wave result but the ongoing regression signal. Preconditions before any
envelope-format change ships:

1. **Wave-7 instrument repair is complete** (decision B) — a fidelity claim
   graded by an instrument with a known-blind deletion control and a drifting
   Part-2 anchor is not a clean basis for a permanent stack change.
2. **A regression suite exists on the actual downstream behavior**: envelope →
   sub-agent behavior grading (the B1–B6 behaviors), not reference-text
   similarity; versioned dataset, threshold gate, run on every envelope-format
   change (Langfuse/Galtea pattern).
3. **The transform is byte-exact and pinned**: the format-level edit is specified
   mechanically (like the existing deletion logs), token measurement under the
   pinned tokenizer (cl100k_base), and the compressed envelope is a versioned
   artifact with rollback — matching the golden-dataset version-pinning practice.
4. **The saving buys something**: a break-even check for envelope-sized prompts
   (arXiv:2604.02985 operating-window logic); if the prompt is short, the
   adoption argument must rest on something other than latency/cost.
5. **Graduation, not declaration**: after adoption, the W1-style fidelity check
   becomes a continuously run regression eval (Anthropic's capability→regression
   graduation).

Reasoning: a single 12/12 fidelity pass at n=12 carries a 95% CI of roughly
74–100% true fidelity (exact binomial; SE logic per Cameron Wolfe, below) — the
result is genuine and consistent with no damage, but it does not bound rare
format-sensitivity failures of the kind arXiv:2411.10541 and arXiv:2508.13666
document. Adoption without a regression net converts a measurement into a
permanent config change on evidence that the field treats as a starting point.

---

## B. Wave-7 instrument repair (B4 deletion control + Part-2 anchor drift)

**Posture: DO NOW — top priority, as forward-only amendments under §7.**

### Evidence from the field

1. **LLM judges being blind to material changes is a documented, common failure
   mode — not an anomaly.** "Know Thy Judge" (Eiras et al., arXiv:2503.04474,
   also MLR v296) shows safety judges' false-negative rates jump by up to 0.24
   under *stylistic* re-renderings that human annotators rate 0.99–1.0 label-
   identical, and adversarial output modifications can fool some judges into
   classifying 100% of harmful outputs as safe. The DEL-b4 outcome (amputee
   graded "fullest version" 15/15) is the same phenomenon: judge-level
   perturbation blindness. The field's answer is meta-evaluation of the judge
   itself, including perturbation testing at temperature 0.
2. **Negative controls must be load-bearing under the rubric that will grade
   them.** DeepChecks' calibration guide (deepchecks.com/llm-judge-calibration-automated-issues/)
   treats a rubric as a control system: dimensions, scoring anchors, failure
   conditions, disallowed behaviors, weighting — and lists the standard judge
   biases (position, verbosity, self-preference, instruction-following) with
   mitigations (order randomization, both-permutation averaging, cross-model and
   ensemble judging, human calibration sets). The W6 recommendation (a deletion
   span the Part-2 rubric actually penalizes, or an explicit Part-2
   hedge-required cue) is exactly the "failure conditions in the rubric" fix; the
   field adds: verify the control bites before the wave counts on it.
3. **Pairwise judging is more sensitive than single-answer scoring.** Zheng et
   al. (NeurIPS 2023, arXiv:2306.05685) established position/verbosity/self-
   enhancement biases and ~80% LLM-human agreement for pairwise preference; the
   Berkeley large-scale judge study (arXiv:2606.19544) reports position-flip
   rates of 25–50% across judges and that position-swap debiasing raises
   within-judge consistency from ~60% to ~85%. A deletion control graded as a
   *paired comparison* (amputee vs intact reference) forces the judge to
   articulate the difference and is harder to pass vacuously than a single
   rubric score.
4. **Raw agreement overstates judge quality; chance-corrected agreement is the
   standard.** "Reliability without Validity" (arXiv:2606.19544; 21 judges, 9
   providers, ~541,000 judgments) finds kappa deflation of 33–41 percentage
   points between exact-match agreement and Cohen's kappa on MT-Bench across all
   21 judges, and a "consistency–bias paradox": test–retest reliability >0.95
   coexisting with position bias >0.10 (Qwen 3 8B, Gemini 2.5 Flash) — "the most
   reproducible judges are among the least valid". The pilot's inter-rater 6/6
   (100% raw agreement on Part 5) should be reported with chance-corrected
   agreement going forward; 6/6 on a skewed scale is weaker evidence than it
   looks.
5. **Reference/golden answers are maintenance objects, and drift is expected.**
   Galileo's calibration practice (galileo.ai/blog/calibrate-llm-judge-human-annotations)
   treats judge calibration as continuous: golden datasets capture a snapshot,
   production moves; kappa trends decide re-calibrate vs rebuild; silent model
   updates and distribution shifts erode anchors. Langfuse's golden-dataset
   guidance versions datasets and supplies reviewer-corrected expected outputs.
   The B4 Part-2 drift (P2=3 vs frozen 13/15) is therefore a *maintenance event*,
   and the W6 handling (report loudly, never patch retroactively) matches the
   field norm; the repair is a versioned re-anchoring, not a correction.
6. **Sequential success criteria are standard replication/instrument practice.**
   The FORRT replication handbook (forrt.org/replication-handbook/execution_replications.html):
   success criteria declared in advance; "if there is a manipulation check, it
   can be defined that it has to work for the replicability to actually be
   evaluated"; amendments preserved with version history. A deletion control that
   failed to bite on one of four behaviors is a failed manipulation check on
   that behavior — it must bite before that behavior's results carry weight.

### Recommended repair design (all as pre-committed amendments, forward-only)

1. **B4 deletion control:** choose a deletion span that the current B4 Part-2
   rubric's anchors penalize (per W6 rec), add the explicit Part-2 hedge-required
   cue, and grade DEL-b4 as a paired comparison against the intact reference
   (Zheng et al. / Berkeley position-swap evidence), keeping the docked-and-named
   decision table (amendment-002 shape) so "undocked-near-ceiling" can never
   read as PRESERVED. Before the wave runs, verify the control bites on a dry
   run — the instrument must be seen failing when it should (Know Thy Judge
   perturbation logic applied to the control itself).
2. **Anchor:** re-verify the B4 reference answer bytes and re-pin the Part-2
   anchor under the current rubric text as a numbered amendment that explicitly
   records the old datum and the reason (Galileo re-calibrate-vs-rebuild;
   Langfuse versioning). Never re-grade frozen cells.
3. **Inter-rater:** add Cohen's kappa alongside raw agreement (arXiv:2606.19544);
   keep the wall and per-grader order shuffling; add position-swap consistency on
   the decision cells.

Reasoning: every remaining decision (R5, adoption, replication) inherits this
instrument. The field's sequential-gate logic (FORRT) says a manipulation check
that fails on one behavior caps what that behavior's results can support — which
is precisely why the six-pager already reads B4 relative-to-ref. Repair is cheap,
already drafted, and parked only behind the owner's pen.

---

## C. Larger-n permanence run (R5)

**Posture: SKIP as framed; if a permanence claim is ever required, reframe with a
power-justified n and an equivalence/smallest-effect design.**

### Evidence from the field

1. **The field's statistical norms for LLM evals.** Cameron Wolfe's "Applying
   Statistics to LLM Evaluations" (cameronrwolfe.substack.com/p/stats-llm-evals)
   compiles the current standard: report the standard error with the mean (CLT);
   use *clustered* standard errors when items are not independent — with a
   worked example where clustering triples the SE; prefer paired-difference
   analysis when comparing two conditions; bootstrap adds nothing under the CLT
   but is the fallback at small n. The pilot's cells are clustered by behavior
   (b1/b2/b4/b6) and by grader, so naive SEs understate uncertainty.
2. **What the numbers resolve at pilot scale.** With a Bernoulli SE of
   sqrt(p(1−p)/n): near-ceiling p≈0.95 at n=12 (W1) gives SE≈0.063, i.e. a 95%
   CI of roughly ±12.6 points — consistent with the exact-binomial lower bound
   of ~74% for 12/12. At n=25 cells (W5/W6 scale) the CI is ±9 pp; reaching ±2 pp
   needs n≈460. The P7 decision bands (0.10–0.20 rubric deltas, "MARGINAL") sit
   *inside* this noise: one integer rubric step is ~0.067 of the 0–15 scale.
   Power arithmetic (two-sample mean comparison, α=0.05, 80% power, σ≈0.9 on
   integer part scores): detecting a 0.10 mean delta needs roughly 1,200 cells
   per arm; 0.20 needs ~320 per arm; pass-rate deltas (0.95→0.85) need ~140 per
   arm. The pilot's observed deviations (±1 integer on P2/P5) are at the edge of
   what the instrument can measure at any practical n.
3. **Practical sample-size norms.** Olamendy's statistical-reality writeup
   (medium.com/@juanc.olamendy/the-statistical-reality-of-llm-evaluation-...):
   "a 90% score on 20 examples might represent anywhere from 75% to 98%"; 200–500
   curated examples for high-stakes comparisons; bootstrap 500–1000 iterations;
   meta-evaluation of the pipeline itself (10 identical runs, temperature 0,
   coefficient of variation < 0.05). Galtea: ~200 items give statistical
   confidence on 3–5% changes; >500 diminishing returns. Anthropic: multiple
   trials per task because outputs vary.
4. **Replication-specific sizing.** FORRT: replication samples should be *larger*
   than the original, because a useful replication must be able to rule out
   smaller effects or support the null (small-telescopes framework, equivalence
   testing with a smallest effect size of interest).

### Recommended posture

SKIP as a "permanence run". The six-pager already disclaims permanence; no
decision in the record needs it. If the owner later wants a permanence claim,
the field-compliant form is: (a) choose a smallest effect size of interest
before the run (a 0.10 delta is not resolvable at practical n — pick the
MARGINAL band's top or admit the claim is out of instrument reach); (b) size the
run from that (hundreds of cells per arm with behavior-clustered SEs, per-cell
integer variance); (c) pre-commit the success criteria (FORRT); (d) grade with
kappa-validated judges (decision E). Reframing the question as an equivalence
test is cheaper than a significance run and matches what the pilot actually
claims ("no material degradation").

---

## D. Replication as validation — when is a methodology "proven"?

**Posture: DO NOW — run the second application; it converts the pattern claim
from "one data point" to "proven" under field norms, at low cost.**

### Evidence from the field

1. **Definitions.** The National Academies' *Reproducibility and Replicability in
   Science* (2019, nationalacademies.org/read/25303/chapter/8) defines
   replicability as "obtaining consistent results across studies aimed at
   answering the same scientific question, each of which has obtained its own
   data"; validity should be judged "in the context of an entire body of
   evidence, rather than an individual study or an individual replication";
   replication "may be a matter of degree, rather than a binary result". There is
   no magic number of replications in the standard; the unit is the independent
   application with its own data.
2. **What counts as a successful replication.** FORRT: pre-registered success
   criteria and analysis plan; sequential criteria (manipulation checks first);
   Registered Reports where possible; deviations documented with version history.
   A replication that cannot fail by its own declared criteria proves nothing.
3. **Base rates argue for independent verification, cheaply.** Kapoor &
   Narayanan (*Patterns*, 2023, arXiv:2207.07048) found data leakage affecting
   329 papers across 17 fields, and in their reproducibility study every claimed
   ML-superiority result in civil-war prediction failed to reproduce once
   leakage was corrected. Field estimates of strict replication for new-method
   claims run 1–10% (LessWrong synthesis, lesswrong.com/posts/j4FnzvwTnReC3bH5y);
   the Reproducibility Project: Psychology found replication effects roughly half
   the original magnitudes (per FORRT). Independent application is the standard
   cost of confidence, and it is cheap when the artifact is a documented
   procedure rather than a model.
4. **The pattern's own claim is field-compliant.** The replicable-pattern doc
   says the pattern "becomes a proven pattern the second time it's applied to a
   different decision" — consistent with the Academies' body-of-evidence framing:
   one successful application is a case report; two independent applications
   (own data, own supervisors/graders, pre-committed success criteria) is the
   first defensible "proven" claim, and it stays a matter of degree afterward.

### Recommended posture

Treat the next application of the mechanism to a *different* orchestration
decision as the replication event, with: (a) pre-committed success criteria
(FORRT) written before the new data exists; (b) at least one element changed
(supervisor model, graders, or both) so it is a genuine independent application
with its own data — the local-LM port (decision E) is the natural carrier; (c)
the W1-equivalent verdict as the primary criterion (same verdicts on the same
frozen packs), with instrument controls (confab + deletion teeth) as sequential
gates that must bite first. A failed replication is informative, not fatal —
per the Academies, a single failed replication does not refute; it triggers
instrument inspection, which this pilot's own history shows is where the value
is.

---

## E. Local small-model judges (Qwen3-4B / Qwen3-8B) for this grading

**Posture: DO NOW, scoped to the replication leg — never as a re-grade of frozen
waves; with calibration and jury structure per field practice.**

### Evidence from the field

1. **Panels of small models beat single large judges.** Cohere's "Replacing
   Judges with Juries" (arXiv:2404.18796): a panel (PoLL) of several smaller
   models outperforms a single large judge across three judge settings and six
   datasets, shows less intra-model bias (disjoint model families), at over 7×
   lower cost. For the pilot, this maps directly onto the existing consult-lens
   design: the walled graders become a jury of local models.
2. **Small-model judging has a capacity floor and a mode requirement.** Jayarao
   et al., "Explicit Reasoning Makes Better Judges" (arXiv:2509.13332, Qwen3
   0.6B/1.7B/4B): thinking mode gives ≈+10.5 points accuracy at 1.82× FLOPs
   versus 7-shot ICL's +4.5 points at 8.16×; thinking models are more robust
   under position/bandwagon/identity/verbosity biases (≈91% vs ≈85%
   consistency); reference-based judging and rubrics help but do not close the
   gap; critically, Qwen3-0.6B fails to beat 50% accuracy on hard judge tasks —
   "smaller models may lack the capacity for challenging evaluations". Implication
   for the pilot: Qwen3-4B/8B in thinking mode is workable; anything below ≈1B is
   not; rubric + ref-anchors are load-bearing, not decoration.
3. **Reliability ≠ validity; calibrate against human gold with chance-corrected
   agreement.** Berkeley's "Reliability without Validity" (arXiv:2606.19544):
   across 21 judges and ~541,000 judgments, exact-match agreement overstates
   chance-corrected discrimination by 33–41 pp; judge rankings shift up to 14
   positions across benchmarks; and the specific models the pilot plans (Qwen3
   8B; Gemini 2.5 Flash) exhibit the consistency–bias paradox — test–retest
   >0.95 with position bias >0.10. Raw self-consistency is not the target metric;
   agreement with human gold (kappa), plus position-swap consistency, is.
4. **Calibration protocol norms.** Olamendy: validate the judge against 150–250
   human-labeled examples (dev/test split, >80% agreement target); separate the
   judge from the generator. Galtea: 30–50 domain-expert binary labels calibrate
   a judge; verify Pearson r > 0.7 against expert verdicts; binary pass/fail
   beats Likert scales (low variance); off-the-shelf judges are not calibrated
   for free. Galileo: IRR (Cohen's kappa / Krippendorff's alpha) as the
   north-star metric, monitored continuously; stratified sampling of disagreement
   tails. Know Thy Judge: perturbation-test the judge (temperature 0) before
   trusting it.
5. **Self-preference is real.** Zheng et al. (arXiv:2306.05685) documented
   self-enhancement bias; DeepChecks lists self-preference among the four core
   judge biases with cross-model judging as the mitigation; community
   blind-grading experiments show same-family judges favoring their own family by
   roughly a point (r/LocalLLaMA 22k-judgment study). The pilot's wall already
   mitigates this (graders never see generator identity, order shuffled per
   grader); the local port must keep the wall intact — that is the load-bearing
   feature, not the choice of judge.

### Recommended posture

Use Qwen3-4B/8B (thinking mode) as walled graders on the replication leg, with:
(a) a calibration gate before the leg counts — 30–50 gold items per behavior
graded by the domain expert, chance-corrected agreement (kappa) at or above the
pilot's existing 6-of-6-equivalent standard, and position-swap consistency
check; (b) jury structure for decision cells (≥3 diverse small models, PoLL
design; the consult-lens mechanism already provides this shape); (c) the confab
and deletion controls retained on every batch (teeth that must bite — Know Thy
Judge logic); (d) temperature 0 and serial dispatch (already the wave-6 pacing
fix). Never re-grade frozen waves with new judges: that would break the
frozen-record discipline, and the field's drift evidence (Galileo; Berkeley)
shows different judges are different instruments.

---

## F. Ordering — sequence that minimizes risk under frozen-record discipline

Evidence base: forward-only amendment norms (FORRT: amendments with preserved
version history; success criteria declared in advance; manipulation checks as
sequential gates); CI-regression practice (Anthropic, Langfuse, Galtea: a change
ships only when the regression net says so); calibration-before-trust (Galileo,
DeepChecks, Know Thy Judge); replication-as-body-of-evidence (National
Academies).

**Recommended sequence:**

1. **Wave-7 instrument repair (B) — first.** Every later measurement inherits
   the instrument. FORRT's sequential-gate logic: a manipulation check that does
   not bite on B4 caps what B4 results can support. Cost is low, the draft
   exists, and it is the only item currently blocked on the owner's pen. All
   fixes enter as numbered, forward-only amendments (§7); no frozen value
   touched.
2. **Six-pager sign-off — immediately after.** The record closes at wave 6 with
   the repaired-instrument caveats stated; the sign-off is the gate that
   unblocks 3–5. Sign-off text should record that R5, adoption, and replication
   are separate commitments, not debts (already the draft's stance).
3. **Local-LM port + replication (E + D) — together, next.** The port is the
   cheapest true independent application: same sealed packs, different
   supervisor, different graders, pre-committed success criteria. It produces
   the "second application" that converts the pattern claim from one data point
   to proven-under-field-norms, and it does the judge-capability question
   empirically (with the calibration gate above) instead of by argument. It also
   de-risks decision A: if verdicts replicate on local judges, the stack claim
   broadens from "one cloud grader set" to "model-agnostic".
4. **R5 permanence run (C) — only on explicit trigger, and only in reframed
   form.** If the owner decides a permanence claim is required, it must be
   power-justified (hundreds of cells/arm for 0.20-delta resolution), clustered
   by behavior, kappa-graded, equivalence-framed, pre-committed — not a
   mechanical re-run of the same grid at larger n. Absent that requirement,
   skip: the record already disclaims permanence, and the field norm (FORRT) is
   that permanence-style claims need larger samples and sharper criteria than
   the exploratory run.
5. **Lossless adoption (A) — last, gated.** Adoption ships only after: instrument
   repaired; regression suite on envelope-consumer behaviors exists and is green;
   transform specified byte-exactly; break-even on envelope-sized prompts
   demonstrated. Then it lands as a versioned format change with rollback and a
   graduated regression eval. This ordering follows the CI-gating norm directly:
   the change is a prompt change, and prompt changes ship against a regression
   net, not a single wave.

**Why this ordering:** it respects the frozen record (nothing retroactive;
everything forward-only), it front-loads the cheapest uncertainty reducers
(repair, then independent application) ahead of the expensive ones (R5) and the
irreversible one (adoption), and it matches the field's sequential-gate pattern:
instrument → manipulation checks bite → replication with declared criteria →
claims with justified power → permanent change behind a regression gate.

---

## Sources cited (all read or verified during this research)

- arxiv.org/html/2411.10541v1 — "Does Prompt Formatting Have Any Impact on LLM Performance?"
- arxiv.org/html/2508.13666v1 — "The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget"
- arxiv.org/html/2604.02985v1 — "Prompt Compression in the Wild: Measuring Latency, Rate Adherence, and Quality for Faster LLM Inference"
- arxiv.org/html/2505.00019v1 — "An Empirical Study on Prompt Compression for Large Language Models" (ICLR 2025)
- anthropic.com/engineering/demystifying-evals-for-ai-agents
- langfuse.com/resources/engineering/ai-agent-evaluation ; langfuse.com/resources/engineering/golden-dataset-evaluation
- galtea.ai/blog/llm-evaluation-complete-guide
- arxiv.org/html/2503.04474v1 — "Know Thy Judge: On the Robustness Meta-Evaluation of LLM Safety Judges" (MLR v296)
- deepchecks.com/llm-judge-calibration-automated-issues/
- arxiv.org/html/2606.19544v1 — "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models"
- arxiv.org/abs/2306.05685 — "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023)
- galileo.ai/blog/calibrate-llm-judge-human-annotations
- cameronrwolfe.substack.com/p/stats-llm-evals — "Applying Statistics to LLM Evaluations"
- medium.com/@juanc.olamendy/the-statistical-reality-of-llm-evaluation-what-works-what-doesnt-and-when-it-matters-7d9ba6ecdfca
- forrt.org/replication-handbook/execution_replications.html — FORRT Replication Handbook, ch. 6
- nationalacademies.org/read/25303/chapter/8 — Reproducibility and Replicability in Science (2019), ch. 5
- arxiv.org/abs/2207.07048 — Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-based Science" (*Patterns*, 2023)
- lesswrong.com/posts/j4FnzvwTnReC3bH5y — "What we know about machine learning's replication crisis"
- arxiv.org/abs/2404.18796 — Verga et al., "Replacing Judges with Juries" (Cohere, PoLL)
- arxiv.org/html/2509.13332v1 — "Explicit Reasoning Makes Better Judges" (Qwen3 thinking-mode study)

## Method notes

- Discovery via web_search; primary reading via the browser harness
  (BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use, goto_url + wait_for_load +
  targeted js() innerText extraction). One page (Galtea) needed a cached-file
  fallback read after the cookie banner truncated the extract. No CAPTCHA/login
  walls encountered; none bypassed.
- Power/CI arithmetic in §C is derived from the CLT/Bernoulli standard-error
  formulas presented in the cited statistics sources (Wolfe; Olamendy), applied
  to the pilot's published numbers (12/12 fidelity, 21–25 cells, 0.10–0.20
  decision bands, integer rubric steps). These are computations, not citations.
