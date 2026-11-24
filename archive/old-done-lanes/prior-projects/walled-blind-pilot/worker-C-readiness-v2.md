# External-Readiness Review — `hermes-replicable-pattern.md` (Stanford knowledge-lab share)

**Reviewer:** Worker C (independent research pass)
**Date:** 2026-08-19
**Artifacts reviewed:** `loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md` (the intended shareable), `wave6-grading-finding.md`
**Method:** independent web research (discovery via search, page reading via a CDP browser harness and direct extraction); every external claim below carries its source URL. No claim in this review rests on the three documents alone.

---

## 0. What the pattern claims, in one paragraph (anchor only)

The pattern is a supervisor-orchestrated experimental discipline for evaluating claims about LLM outputs: pre-registered frozen contracts with forward-only amendments, sealed lotteries over mechanical deletion transforms (T1–T7: drop-hedge, drop-conditional-clause, drop-reversibility-qualifier, load-bearing qualifier, merge, wholesale hedge-drop, shorten example), walled-blind LLM graders on a 5-part × 0–3 rubric with a base-12 PASS gate, positive controls in every batch (confabulation 4/4 bite, deletion 3/4 bite in W6), inter-rater checks, byte-level audit and SHA-256 seals, advisory consult legs, and anti-patterns. It was applied once, to Amazon Leadership Principles doctrine, across waves 1–6 (2026-08-15→18). The experiment's verdicts: lossless format-level compaction 52.9% token savings at 12/12 fidelity (W1); lossy deletion-based compression HURT at ≤60% with a cliff at 40% and no adoption (W3–W6); standing posture KEEP FULL PROSE. The pattern claims to be the deliverable, not the verdict.

---

## 1. Verdict: **share with conditions**

The document is above the typical standard of an internal methodology memo and ahead of most published practice on pre-registration discipline for LLM-agent experiments. It is not yet credible as a standalone external artifact: a Stanford-level reader cannot verify any headline number from the document itself, cannot identify the graders, and cannot locate the rubric. The gap is packaging and validation, not the core idea.

**Conditions (in priority order):**

1. **Ship a replication kit.** The pattern's own promise is "a fresh reader could verify from disk" — but every artifact it cites (prereg contracts, rubric text, lottery briefs, cell files, deletion logs, manifests, grading scripts) lives on a private machine. An outsider has nothing to open. Package: doctrine file, verbatim rubric, transform specs including the lossless (format-level) transform family, one representative cell + log, manifest with seals, `apply_rulebook.py`, and a README with exact commands and environment, archived with hashes and a license. This is the single largest credibility lever; without it, "verify from disk" is an assertion about a disk the reader does not have.
2. **Pin the grader environment.** The 2026 pre-registration literature for AI-agent experiments requires exact model identifiers and version checkpoints, generation parameters (temperature, top-p, top-k, seeds), inference budgets, retry limits, and API version/access date (arXiv:2606.11217). The docs pin the tokenizer (tiktoken `cl100k_base` v0.14.0), lottery seed, and order-shuffle seeds, but never name the grader models, their versions, or sampling parameters ("cloud-backed graders" is all the pattern says). A reviewer cannot tell whether grades came from GPT-4-class or Qwen3-4B, and the literature shows judge behavior is judge- and task-dependent (arXiv:2306.05685; IJCNLP 2025 position-bias study).
3. **Anchor the rubric to humans, at least once.** The field's standard for LLM-as-a-judge is validation against a human gold standard — the MT-Bench methodology established agreement of ~80%+ between GPT-4 judges and human experts, comparable to human–human agreement, as the bar (arXiv:2306.05685). The pattern has no human anchor: inter-rater 6/6 between two LLM graders on one dimension at near-ceiling scores (all 3s) does not establish that the scale measures doctrine fidelity. A 10–20 cell human-grading pilot on one behavior, with agreement reported, would close this.
4. **Add statistical reporting.** NeurIPS-checklist norms require error bars or confidence intervals, stated factors of variability, and disclosed number of runs (neurips.cc/public/guides/PaperChecklist). The docs report integer rubric scores and pass counts with no effect sizes, no intervals, and no grader-variance quantification. State the minimum damage the 0–3/base-12 instrument could detect at n≈17; that number is the honest bound on "essentially no effect."
5. **Position against the compression literature.** As written, the pattern's compression claims exist in a vacuum. One short "related work" section — LLMLingua, LLMLingua-2, Selective Context, LongLLMLingua, the 2025 empirical study, and the 2026 latency/quality study (URLs in §3) — would convert "we found HURT" into "our regime and transform family sit at the pessimistic end of a known task-dependent spectrum," which is where the finding actually belongs.
6. **Public, timestamped pre-registration.** The pattern's seals prove internal immutability, not public commitment. Archive the frozen prereg + amendments with timestamps (or a registered DOI) so the "frozen before data" claim is independently checkable; the 2026 template also asks for pilot-testing history, which the docs currently do not disclose (arXiv:2606.11217).
7. **Compute/cost disclosure.** NeurIPS norms require per-run and total compute, including compute spent outside reported experiments (neurips.cc/public/guides/PaperChecklist). The pattern reports token savings but never the cost of running six waves of grading, which matters for a "runs on a single machine" replication pitch.
8. **Language softening in the six-pager.** "Lossy/semantic compaction is falsified" overreaches the evidence (see §3 and §7). The pattern document's own framing — "NO ADOPTION — KEEP FULL PROSE" for this doctrine and stack — is the right scope and should be the shared wording.

---

## 2. What 2024–2026 evaluation-reporting standards require (table stakes)

The reporting bar for externally shared methodology has three layers, all documented:

**Layer 1 — the conference checklist norm.** The NeurIPS paper checklist (mandatory since 2020, still enforced for 2025/2026 submissions) requires: claims in abstract/intro that match scope and generalization; a limitations treatment of strong assumptions and robustness to their violation; experimental-setting detail (data splits, hyperparameters, how chosen); statistical-significance reporting (error bars suitably defined, factors of variability stated, method of calculation given, SD vs SEM distinguished); compute disclosure (worker type, memory, time, per-run and total, plus any compute beyond the reported experiments); and code/data/instructions reproducing the main results with exact commands and environment (neurips.cc/public/guides/PaperChecklist). The NeurIPS 2026 Main Track Handbook restates the reproducibility-disclosure obligation and makes "evaluation, reproducibility, resources" explicit review criteria (neurips.cc/Conferences/2026/MainTrackHandbook).

**Layer 2 — the artifact-evaluation norm.** ACM artifact review badging distinguishes "Artifacts Evaluated – Functional" (documented, consistent, complete, exercisable, with evidence of verification), "– Reusable" (documented and structured for repurposing), "Artifacts Available" (permanently retrievable), and "Results Validated" (independent reproduction) (acm.org/publications/policies/artifact-review-badging). The pattern's discipline maps onto these badges well on paper — seals and audits are verification evidence — but earns none of them until materials exist outside the private machine. The ML reproducibility program literature reports that reproduction success rises from 4% to 85% when original authors provide assistance, and frames the field's problem as at least partly a reporting problem (arXiv:2003.12206); that asymmetry is exactly the risk of a pattern documented only on its author's disk.

**Layer 3 — the 2026 agent-experiment pre-registration norm.** The most recent relevant standard is the 2026 proposal to make pre-registration standard for experiments with AI agents (arXiv:2606.11217). It catalogues researcher degrees of freedom (prompt × model × decoding × retries × parsing × metric) and requires locking model identifiers and checkpoints, generation parameters, seeds, inference budgets, verbatim prompt text, API versions/dates, quantization/checkpoint hashes for open weights, pilot-testing history, and explicit demarcation of confirmatory vs exploratory analysis. Measured against this template, the pattern is unusually strong on contract freezing, amendment mechanics, and confirmatory/exploratory separation — and weak on exactly two items: pinned model identity and pilot-history disclosure.

**Table stakes, summarized:** reproducibility (code+data+commands), baselines and controls, cost/compute, statistical significance, failure modes and limitations, and explicit scope discipline. The pattern hits controls, limitations, and scope discipline; it misses reproducible materials, statistics, and cost.

---

## 3. The compression verdict against the published literature

The field does not support "lossy compression harms fidelity, keep full prose" as a general statement — it supports a task-, ratio-, method-, and context-length-dependent picture, within which the pattern's negative result is a plausible and defensible data point. An expert would not call the verdict naive; they would call it correctly scoped but under-positioned, and would push back on the word "falsified."

**Evidence that supports the pattern's direction:**

- **Short-context degradation with ratio.** The 2025 empirical study of six compression methods across 13 datasets and three LLMs found "all methods' performance decreases with increasing compression ratios for short contexts" (long contexts are different — moderate compression can help there) (arXiv:2505.00019). The pattern's doctrine envelopes are short prompts, placing it in the degrading regime.
- **Information-loss hallucination.** The same study found "all methods result in some degree of increased hallucination, with information loss being the primary reason," distinguishing altered-semantic from information-loss hallucination (arXiv:2505.00019). This is the mechanism the pattern's confabulation controls detect, and it validates the choice to carry confab controls in every batch.
- **Qualifiers are exactly what entropy-based pruning removes.** LLMLingua removes tokens by information entropy from a small causal LM; LLMLingua-2's authors explicitly argue entropy is a suboptimal compression metric and reframe compression as token classification to guarantee the compressed prompt stays faithful to (a subsequence of) the original (arXiv:2403.12968). Predictable, low-surprise tokens — hedges, qualifiers, conditionals — are the natural deletion candidates for entropy-based methods. The pattern's finding that load-bearing qualifiers (B2) die first is therefore consistent with the field's known failure mode, not an anomaly.
- **Fidelity under compression is a recognized metric.** Selective Context (EMNLP 2023) measures faithfulness directly and reports a 50% context-cost reduction with a .038 faithfulness drop on long-context tasks (arXiv:2310.06201) — same construct as the pattern's rubric, on the other side of the regime boundary.

**Evidence that bounds the verdict:**

- LLMLingua reports up to 20× compression with only a 1.5-point performance drop on its evaluated tasks (GSM8K, BBH, ShareGPT, arXiv) (arXiv:2310.05736); LongLLMLingua reports compressed prompts outperforming originals in long-context scenarios (arXiv:2310.06839); Selective Context reports comparable performance at 50% context reduction (arXiv:2310.06201); and a 2026 ECIR study (thousands of runs, 30,000 queries, three GPU classes) finds LLMLingua can deliver up to 18% end-to-end speed-up with response quality "statistically unchanged" on summarization, code generation, and QA when prompt length, ratio, and hardware are matched (arXiv:2604.02985). The 2025 NAACL survey organizes the whole space and frames current methods' limitations as open research problems (arXiv:2410.12388). None of this literature reports a universal cliff at 40%.

**Why the pattern's negative result still stands, exactly as scoped:** the tested transforms are targeted deletions of the single most load-bearing token classes (hedges, conditionals, reversibility qualifiers) — a pessimistic corner of the compression space by construction, and one the literature rarely evaluates because entropy methods preferentially delete different tokens. A negative result for *that* transform family on *that* content class is not a negative result for lossy compression generally; the pattern document states this scope correctly (mechanical deletions only, "never LLM paraphrase"; verdict scoped to this doctrine and stack). The six-pager's "Lossy/semantic compaction is falsified" drops the scoping. Note also: the 52.9% lossless result sits in a literature gap — format-level compaction is essentially unstudied in the prompt-compression literature, which is dominated by lossy methods; the number is plausible only if the transform list shows what was stripped, which the shareable document does not include. Absence of a literature body is noted, not overclaimed.

---

## 4. Knowledge-lab sharing norms and concrete exemplars

What makes a methodology artifact credible to an outsider lab: public materials, a stated measurement taxonomy, validated instruments, disclosed failure modes, and a maintenance story. Three exemplars, each with a URL:

1. **HELM (Stanford CRFM)** — the in-house exemplar. "A reproducible and transparent framework for evaluating foundation models," with leaderboards spanning scenarios × metrics × models, multimodality, and model-graded evaluation (crfm.stanford.edu/helm/). Its methodology paper taxonomizes scenarios and metrics explicitly, adopts multi-metric evaluation (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency), and ships as an open framework with per-run records and a living-benchmark stance (arXiv:2211.09110; github.com/stanford-crfm/helm). The credibility mechanism is not the paper — it is that every number on the leaderboard traces to a public run spec. Notably, HELM itself uses model-graded evaluation in some suites, so LLM graders are not disqualifying; the norm is that they be specified and validated.
2. **The NeurIPS paper checklist** — the reporting artifact that defines what "methodology write-up" means to reviewers: claims-to-scope matching, limitations, statistics, compute, and reproduction commands (neurips.cc/public/guides/PaperChecklist). A shared pattern that cannot answer these items reads as pre-2020.
3. **ACM artifact review badging** — the vetting norm for artifacts themselves: Functional/Reusable/Available/Results-Validated (acm.org/publications/policies/artifact-review-badging). The pattern's own seal-and-audit machinery is best understood as an attempt to self-administer these badges; an external reviewer will ask which ones it would actually earn.
4. Supporting norms: **model cards** for documenting released artifacts (arXiv:1810.03993) and the **2026 AI-agent pre-registration template** for experiment specification (arXiv:2606.11217). The 2025 reproducibility-in-AI literature adds that statistical rigor items (effect sizes, intervals, pre-registration, code/data sharing) are the current explicit demands (e.g., Statistical Rigor and Reproducibility in the AI Era, PMC12402953).

The pattern document's rhetorical genre — pre-registration, amendment mechanics, byte-level audits, consult dissents preserved — is genuinely aligned with where 2026 norms are heading; the gap is that none of it is externally verifiable yet.

---

## 5. The single strongest claim the combined evidence supports

**Claim, at exact scope:** For short, hedge- and qualifier-heavy doctrine prompts evaluated with a rubric that penalizes qualifier loss and confabulation, mechanical deletion-based (lossy) compression degrades rubric-measured fidelity at ≥40% reduction — with load-bearing qualifier loss as the leading damage class and no measurable effect at 20–30% — while format-level lossless compaction achieved 52.9% token savings at full fidelity in one 12-cell wave. All of it holds for: one doctrine (Amazon Leadership Principles), one orchestrator/grading stack, one rubric, LLM graders with no human anchor, n≈17–21 real cells per decisive wave, and one application of the pattern.

**Why the field supports it:** the short-context degradation regime (arXiv:2505.00019), the information-loss hallucination mechanism (arXiv:2505.00019), and the entropy-pruning/qualifier-vulnerability link (arXiv:2403.12968) all point the same direction; the cliff location and the lossless number are the parts that are not independently corroborated and must stand on the pattern's own (currently unsharable) materials.

**What the field does not support:** any generalization to other doctrines, longer contexts, entropy-based or learned compressors, other grader families, or other rubric thresholds. Selective Context (arXiv:2310.06201), LongLLMLingua (arXiv:2310.06839), and the ECIR 2026 study (arXiv:2604.02985) show quality-preserving or quality-improving compression in other regimes.

---

## 6. The three questions a Stanford reviewer asks first

**Q1. "What exactly was compressed, and can I verify the headline numbers?"**

- *What the docs say:* lossless = format-level compaction, 52.9% savings, fidelity 12/12 (W1); lossy = the T1–T7 deletion transforms; tokenizer pinned (cl100k_base v0.14.0); every number cites on-disk artifacts that "round-trip" seals.
- *What the field says:* the norm is exact commands + environment + data + code for the main results (neurips.cc/public/guides/PaperChecklist), and artifact availability is a badge criterion (acm.org/publications/policies/artifact-review-badging).
- *The honest gap:* the shareable document contains no transform spec, no rubric text, no doctrine text, no cell data, and no code. "Verify from disk" is unfulfillable from outside; and 52.9% from "format-level" changes is a number the field would probe (typical formatting-whitespace savings are far smaller; the transform list must show what was stripped). This is the single most likely reason for a skeptical first read.

**Q2. "Who are your graders, and is the rubric a valid instrument?"**

- *What the docs say:* walled-blind LLM subagents; 5-part × 0–3 rubric, base-12 gate; inter-rater 6/6 (100%) on Part 5 across six cells; confab controls 4/4 and deletion controls 3/4 in W6; grader order counterbalanced; one documented non-bite (B4 deletion control) reported as INCONCLUSIVE.
- *What the field says:* LLM judges are acceptable but must be validated against human judgment (the MT-Bench bar: >80% agreement, human-level) and their known biases (position, verbosity, self-enhancement, limited reasoning) must be addressed (arXiv:2306.05685); judge behavior varies by judge and task (IJCNLP 2025 position-bias study, aclanthology.org/2025.ijcnlp-long.18); judge identity and sampling parameters must be pinned (arXiv:2606.11217).
- *The honest gap:* no human anchor exists for the rubric; grader model IDs/versions/temperatures are absent from the shareable docs; inter-rater covers one dimension only, at the ceiling, where 6/6 is weak evidence; and "stable eye" (one grader per behavior) confounds grader identity with treatment. The controls are genuinely good — they show the instrument can fail — but they do not establish that the scale measures what it claims to measure.

**Q3. "How sensitive is the instrument, and what does 'no effect' mean statistically?"**

- *What the docs say:* W6 was built precisely to test the near-ceiling reading; 17/17 real cells PASS with essentially no compression effect at 20→30→40%; the two negative-control families bit (4/4, 3/4), supporting "the instrument can fail"; B4 anchor drift and the B4 deletion-gate blindness are reported loudly; small n, no permanence claim.
- *What the field says:* statistical-significance reporting — error bars, CI, stated variability factors, number of runs — is checklist-level table stakes (neurips.cc/public/guides/PaperChecklist); 2025 rigor commentary asks for effect sizes alongside intervals (PMC12402953). The empirical compression literature shows measurable degradation exists at moderate ratios in short contexts (arXiv:2505.00019), so "no effect" is a sensitivity claim, not a given.
- *The honest gap:* with an integer 0–3 scale, base-12 gate, and 17 real cells, the minimum detectable damage is unknown and unreported; no confidence interval, effect size, or grader-variance estimate exists; and one of four behaviors (B4) is unverified at the negative-control level because its deletion control is blind. The docs' own limitations section is unusually honest about most of this — the missing piece is quantification.

---

## 7. Over/understatement findings

**Overstatements:**
- "Lossy/semantic compaction is falsified" (six-pager §3): overreaches the tested transform family and regime; the literature shows task- and regime-dependent effects, including quality-preserving compression (arXiv:2310.05736, arXiv:2310.06201, arXiv:2604.02985). "Falsified for this doctrine, stack, transform family, and rubric" is what the evidence supports.
- "Inter-rater 6/6 = HIGH" presented as evidence the instrument works: at ceiling, on one dimension, between LLM graders with no human anchor, this is weak validity evidence (arXiv:2306.05685).
- "The discipline survives a supervisor-model swap": asserted, not yet tested; the pattern itself correctly lists replication on the local rig as the open claim.
- The 52.9% lossless figure as a headline: un-auditable without the transform list; at face value it is high for "format-level" changes and will be probed.

**Understatements (the honest side):**
- B4 deletion-gate blindness, B4 anchor drift, the §7.4 no-op cell, and the confab/hedge confound are all documented prominently — this is over-reporting relative to community norms and is the document's strongest credibility asset; it should be kept verbatim in any shareable version.
- The pattern correctly refuses adoption and permanence claims, and correctly presents itself as one successful application.
- Understated relative to risk: the grader-validity gap (no human anchor) and the absence of any public archive are the two things that will cost the most credibility externally, and neither is flagged as a limitation in the pattern document — they are simply absent.

---

## 8. Sources (all URLs verified readable during this review)

- NeurIPS Paper Checklist Guidelines — https://neurips.cc/public/guides/PaperChecklist
- NeurIPS 2026 Main Track Handbook — https://neurips.cc/Conferences/2026/MainTrackHandbook
- Pineau et al., Improving Reproducibility in ML Research (NeurIPS 2019 program) — https://arxiv.org/abs/2003.12206
- Preregistration for Experiments with AI Agents (2026) — https://arxiv.org/html/2606.11217v1
- ACM Artifact Review and Badging — https://www.acm.org/publications/policies/artifact-review-badging
- Mitchell et al., Model Cards for Model Reporting — https://arxiv.org/abs/1810.03993
- HELM (Stanford CRFM) — https://crfm.stanford.edu/helm/ ; methodology paper — https://arxiv.org/abs/2211.09110 ; repo — https://github.com/stanford-crfm/helm
- Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena — https://arxiv.org/abs/2306.05685 ; position-bias follow-up (IJCNLP 2025) — https://aclanthology.org/2025.ijcnlp-long.18.pdf
- Jiang et al., LLMLingua — https://arxiv.org/abs/2310.05736 ; LongLLMLingua — https://arxiv.org/abs/2310.06839
- Pan et al., LLMLingua-2 — https://arxiv.org/abs/2403.12968
- Li et al., Selective Context (EMNLP 2023) — https://arxiv.org/abs/2310.06201
- Li et al., Prompt Compression for LLMs: A Survey (NAACL 2025) — https://arxiv.org/abs/2410.12388
- An Empirical Study on Prompt Compression (ICLR 2025 Building Trust workshop) — https://arxiv.org/abs/2505.00019
- Kummer et al., Prompt Compression in the Wild (ECIR 2026) — https://arxiv.org/abs/2604.02985
- Statistical Rigor and Reproducibility in the AI Era — https://pmc.ncbi.nlm.nih.gov/articles/PMC12402953/
