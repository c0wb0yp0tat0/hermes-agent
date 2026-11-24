# Verification Report — Walled-Blind LLM Compression Experiment vs. Published Literature

**Worker:** A (independent verification pass, v2)
**Date:** 2026-08-19
**Method:** web_search discovery → page reading via the browser-harness (`BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use`, targeted `js()` extraction, `goto_url` + `wait_for_load`; one retry per page; no CAPTCHA/login walls encountered; one PDF fetch failed via firecrawl and was replaced with the anthology landing page). Claims below are checked against primary sources (arXiv HTML, ACL Anthology, peer-reviewed venues) and research-lab/engineering analyses where noted. Every online claim carries its URL.
**Sources read (primary):** arXiv:2604.02985 (Prompt Compression in the Wild), arXiv:2604.13066 (lossless dictionary-encoding compression), arXiv:2508.19282 (CORE), arXiv:2310.05736 (LLMLingua), arXiv:2403.12968 (LLMLingua-2), arXiv:2407.15504 (rate–distortion limits), arXiv:2306.05685 (LLM-as-a-judge, Zheng et al.), arXiv:2406.07791 (position-bias systematic study), arXiv:2506.22316 (scoring bias), arXiv:2601.03444 (grading scale), arXiv:2508.13666 (code-formatting token cost), arXiv:2505.00019 (empirical compression study), arXiv:2605.19196 (Reflect judge meta-evaluation), arXiv:2408.02442 (format restrictions), arXiv:2307.03172 (lost in the middle), arXiv:2401.03729 (butterfly effect of prompt edits), ACL 2026 SRW PolyJudge-Uncertain, CHI 2024 "I'm Not Sure, But…", PMC medical-summary judge study, plus engineering analyses (TianPan LLM-judge ceiling, eugeneyan LLM-evaluator survey, r/mlops ceiling/inter-rater field report, LessWrong prompt-imperativeness study).

---

## 1. Summary verdicts

| # | Claim (doc-quoted, anchored) | Verdict |
|---|---|---|
| C1 | Lossless format-level compaction: "52.9% token savings, fidelity 12/12 vs 12/12" | **Partially supported / plausible, unproven at this magnitude for prose** |
| C2 | Lossy semantic compression: "HURT at ≤60%; cliff at 40%" | **Supported as task-specific outcome; contradicted as a general law; internally inconsistent across the experiment's own waves** |
| C3 | "load-bearing qualifiers (B2) and hedge/reversibility behaviors die first" | **Supported in direction by literature on hedging sensitivity; the pilot's rubric makes this partly self-fulfilling** |
| C4 | Wave-6 near-ceiling is genuine because "confab controls 4/4 bit; deletion control 3/4" | **Partially supported. Controls are the right instrument and do bite; the literature says judge sensitivity is partial and dimension-dependent, near-ceiling compresses reliability, and the experiment's own B4 anchor drift is the classic leniency-drift failure mode** |

---

## 2. C1 — Lossless format-level compaction: 52.9% savings at 12/12 fidelity

**Doc anchor:** "W1 | Lossless (format-level) compaction | **52.9% token savings, fidelity 12/12 vs 12/12**; positive control caught 0/12 (teeth) — PASS/GENUINE".

**Field evidence:**

1. *Lossless prompt compression is a documented, published category, but with specific preconditions.*
   - **CORE** (arXiv:2508.19282v3, https://arxiv.org/html/2508.19282v3): RL-trained compressor achieves a "compression ratio of 3%" (≈97% token reduction) with *no* performance degradation and +3.3 average EM on RAG QA — "lossless" in the downstream-task sense, but it requires a trained compressor and is measured on retrieval QA, not on prose fidelity.
   - **Lossless Prompt Compression via Dictionary-Encoding** (arXiv:2604.13066v1, https://arxiv.org/html/2604.13066v1): LLMs learn encoding keys in-context; up to 80% compression with exact-match >0.99 (template-based) and Levenshtein >0.91 (algorithmic) on LogHub 2.0 logs; "compression ratio explains less than 2% of variance in similarity metrics". The precondition is **repetitive, structured data** — the dictionary mechanism exploits redundancy. Non-repetitive prose is not this regime.
   - Both confirm that ~50–80% reduction at zero *measured* loss is achievable in the published record — under the conditions of redundancy (dictionary encoding) or trained compressors + downstream-task metrics (CORE). The pilot's mechanism (deterministic format-level edits on doctrine prose, fidelity judged by walled LLM graders on a rubric) is a different mechanism and measurement than either.
2. *Format-level token overhead in the published record is real but the closest measured figure is ~25%, not ~53%.*
   - **"The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget"** (arXiv:2508.13666v1, https://arxiv.org/html/2508.13666v1): removing indentation/newlines yields an average **24.5% input token reduction** with maintained performance across 10 LLMs on fill-in-the-middle code completion; output-token reductions are negligible. This is the closest published analog to "format-level, lossless": format removal is behaviorally safe in their setting, and savings are substantial — but 24.5% for code formatting is well below 52.9%.
   - Community measurements of serialization-format overhead (markdown vs JSON ≈15% token difference; YAML vs JSON ≈20–30%; https://community.openai.com/t/markdown-is-15-more-token-efficient-than-json/841742; https://david-gilbertson.medium.com/llm-output-formats-why-json-costs-more-than-tsv-ebaf590bd541) are not peer-reviewed and are about structured serialization, not prose markdown.
   - A 52.9% figure for markdown-heavy doctrine prose (headers, bullets, bold, links, whitespace) is *plausible* — tokenizers spend tokens on markdown syntax and whitespace — but no published study reports a comparable number for prose; the pilot's W1 number stands on its own instrument.
3. *"Format is behaviorally inert" is not established — format changes measurably alter model behavior.*
   - **Format restrictions on generation** degrade reasoning, and stricter formats degrade more (arXiv:2408.02442v1, https://arxiv.org/html/2408.02442v1).
   - **Prompt-imperativeness experiment** (n=900 factorial): prompt phrasing shifts hedging with Cohen's d up to 2.67 (https://www.lesswrong.com/posts/vBDupg8iPqgdwhFzz/demands-are-all-you-need-prompt-imperativeness-drastically; non-peer-reviewed, flag as weak source).
   - **Butterfly Effect of Altering Prompts** (arXiv:2401.03729, https://arxiv.org/html/2401.03729v2): "even the smallest of perturbations, such as adding a space at the end of a prompt, can cause the LLM to change its answer" — the strongest caution that format-level edits are not guaranteed inert, even when graders see no fidelity loss on a 5-part rubric.
   - Counterpoint from the same literature: 2508.13666 shows formatting removal is safe *on code tasks*, and "Prompt Compression in the Wild" (arXiv:2604.02985v1, https://arxiv.org/html/2604.02985v1) found LLMLingua-quality "statistically unchanged" on summarization/code/QA within its operating window — so "format removed, behavior preserved" is a documented outcome in some settings.
4. *The pilot's own record weakens the headline number.*
   - Per the pilot's own docs, **W2 (format arms) achieved 28.6%/12.9% savings vs the 52.9% target and was declared INCONCLUSIVE** ("flat hedge baseline"). The 52.9% is therefore a single-wave measurement that the experiment itself did not reproduce. The six-pager still leads with "52.9% at 12/12" as the deliverable answer. This is an internal-replication gap the reader should weigh.
   - W1's control line "positive control caught 0/12 (teeth)" is ambiguous as written: 0/12 can mean (a) zero plants and zero false alarms (instrument returns clean zeros — a valid negative-control property) or (b) twelve plants missed (instrument blindness). The docs' "(teeth: the instrument CAN fail)" suggests (a), but the phrasing reads like (b). Reporting hygiene issue, not necessarily a data error.

**Verdict:** Plausible and in-family with the published record (lossless compression at 50–80% documented under redundancy/trained-compressor conditions; format removal documented as safe at ~25% for code), but the specific 52.9%-at-12/12 for prose is not documented anywhere in the literature I found, the mechanism differs from every published lossless system, and the pilot's own W2 did not reproduce the savings.

**Implication:** Treat W1 as a promising pilot result, not an established finding. Before any stack adoption of format-level compaction: (a) replicate the savings on a second corpus with a pinned tokenizer (the docs pin cl100k_base — good), (b) test behavior effects beyond the rubric (the butterfly-effect and format-restriction results say format edits can move outputs the rubric won't see), and (c) expect published analogs to sit closer to 25% than 53% for prose.

---

## 3. C2 — Lossy semantic compression: "HURT at ≤60%; cliff at 40%"

**Doc anchor:** "W3–5 | Lossy (semantic) compression ≤60% | **HURT at ≤60%; cliff at 40%**; load-bearing qualifiers (B2) and hedge/reversibility behaviors die first". (W5 later relocates: "true cliff located between 20% and 30%".)

**Field evidence:**

1. *Lossy compression damage is documented as task-dependent, with sharp drop-offs — cliffs are real but not universal, and not at fixed ratios.*
   - **Prompt Compression in the Wild** (arXiv:2604.02985v1): summarization stays robust up to ~5.7×; few-shot classification drops up to 52% (TREC, LSHT-ZH); synthetic/structured tasks collapse (passage counting <20% → <4.5%; passage retrieval below 50% because "the structural cue of paragraph numbering… is lost through compression"); code edit-similarity drops "even at low compression ratios". Authors conclude "LLMLingua-2 is unsuitable for compressing structured synthetic datasets". This is the single best published demonstration that (a) sharp, near-cliff degradation at moderate ratios exists, and (b) it is content- and task-specific — exactly the pilot's claim, but at ~3.7× average reduction (≈73%), far later than the pilot's 40%.
   - **LLMLingua** (arXiv:2310.05736v2, https://arxiv.org/html/2310.05736v2): "up to 20x compression with little performance loss"; practitioner summary reports GSM8K EM −1.44/−1.52 at 14×/20× and "performance reaches a plateau and drops quickly" (https://www.prompthub.us/blog/compressing-prompts-with-llmlingua-reduce-costs-retain-performance). The degradation curves in this family are gentle at low-moderate ratios and sharp at high ratios.
   - **An Empirical Study on Prompt Compression** (arXiv:2505.00019v1, https://arxiv.org/html/2505.00019v1): across 13 datasets and six methods, "prompt compression has a greater impact on LLM performance in long contexts compared to short ones. In the Longbench evaluation, moderate compression even enhances LLM performance" — i.e., moderate lossy compression is often *benign or helpful* on standard benchmarks. This is the strongest published counterweight to "lossy ≤60% always HURT": the pilot's doctrine setting is far more sensitive than benchmark-average behavior.
   - **Rate–distortion theory** (arXiv:2407.15504v1, https://arxiv.org/html/2407.15504v1, NeurIPS 2024): distortion grows as rate falls, in expectation — smooth, not cliff-shaped; current methods sit "far from the theoretical limit"; query-awareness is critical. The theory says there is no free lunch and no universal cliff; cliffs are emergent properties of specific content/query pairs.
   - **Lost in the Middle** (arXiv:2307.03172v2, https://arxiv.org/html/2307.03172v2): context use is position-dependent (U-shaped; GPT-3.5-Turbo mid-context performance below its closed-book 56.1%) — a reminder that *where* content is deleted modulates damage; a fixed ratio is a poor proxy for damage in short doctrine envelopes.
2. *Why the pilot's early cliff (≤60%, worst at 40%) is credible for this specific task:* the pilot's rubric requires hedging (Parts 3/5 "hedge-required") and load-bearing qualifiers, and the hedging literature (C3 below) shows hedge behavior is among the most prompt-sensitive behaviors in LLMs. A fidelity metric that penalizes hedge loss will register damage earlier than task-accuracy metrics. This reconciles the pilot's early cliff with the benchmark literature's later cliffs: different dependent variables.
3. *Internal inconsistency across the pilot's own waves:* the docs report the cliff at 40% (W3), then between 20% and 30% (W5), then "compression 20→30→40% essentially no effect (matches W5)" with 17/17 near-ceiling PASS (W6). W6's "no effect at 40%" sits in direct tension with W3's "cliff at 40%" and with W5's HURT at 30%-reserved (W5: "30-reserved HURT on Part 2"; W6: all 30%-reserved cells PASS 14–15/15). The wave-6 document attributes this to rubric amendment-002 (relative-to-ref anchors) plus its own documented grader leniency drift (B4 P2=3 vs frozen 13/15) — which is precisely the mechanism the judge-calibration literature warns about (see C4). A reader cannot take "cliff at 40%" and "no effect at 40%" as simultaneously established facts; the cliff location is rubric- and wave-dependent.

**Verdict:** Supported as a *task-specific* outcome — the literature documents sharp fidelity collapses under lossy compression and content-type dependence, and a hedge-penalizing rubric plausibly registers damage early. Contradicted as a general law — benchmarks show moderate lossy compression is frequently neutral or beneficial, and theory predicts smooth, not cliff-like, average behavior. The 40% cliff is not replicated by the pilot's own later waves.

**Implication:** "KEEP FULL PROSE" is a defensible standing rule *for this doctrine and this stack*; it should not be exported as a general claim. Next step: pre-commit the cliff test to the *reserved-sentence* protocol (W5-style) with the amended rubric, and report the W3-vs-W6 discrepancy as an open question rather than folding it into "matches wave-5". If lossy compression is ever re-tested, the published record says the interesting region is task-dependent, so test on the actual downstream envelope task, not on rubric-fidelity alone.

---

## 4. C3 — "Load-bearing qualifiers/hedges die first"

**Doc anchor:** "the behaviors that die first (B2 qualifiers, hedging) are exactly the ones that make doctrine useful"; "B2 mechanism (load-bearing qualifiers) is the leading explanation for where HURT originates — explanation, not proof".

**Field evidence:**

1. *Hedging is highly prompt-sensitive — consistent with "hedges die first" under any input perturbation.*
   - **Prompt imperativeness study** (n=900, 3×2×3): imperative phrasing reduced hedging with F(2,882)=361.72, p<.001, η²p=.451; largest on subjective questions (M=2.38→0.43, Cohen's d=2.67); Claude hedges most (https://www.lesswrong.com/posts/vBDupg8iPqgdwhFzz/demands-are-all-you-need-prompt-imperativeness-drastically). Non-peer-reviewed (student project on LessWrong) — flag, but the direction matches peer-reviewed work.
   - **"I'm Not Sure, But…"** (CHI 2024, https://dl.acm.org/doi/fullHtml/10.1145/3630106.3658941): natural-language uncertainty expressions measurably change user reliance/trust; "the precise language used matters"; general-perspective hedges have weaker, non-significant effects — hedges are functional, content-carrying devices, not decoration.
   - **PolyJudge-Uncertain** (ACL 2026 SRW, https://aclanthology.org/2026.acl-srw.33/): judges prefer the assertive answer in **1,276/1,280** pairwise cases when answers are equally correct and differ only in style ("assertiveness preference").
2. *But the pilot's rubric makes "hedges die first" partly self-fulfilling.* The rubric explicitly requires hedging ("hedge-required: Parts 3 and 5 ≠ 0"), so any hedge-stripped variant *must* fail Part 5 by construction; the wave-6 hedge-stripped confab controls "FAIL on two independent grounds (P5=0 on the hedge-required behavior AND base below threshold)". Published judges, by contrast, *prefer* assertive answers (PolyJudge 1,276/1,280; "tone sycophancy" in the LLM-judge bias literature, e.g. https://mbrenndoerfer.com/writing/position-bias-in-llm-judges). The pilot's rubric is a deliberate normative inversion of the documented judge default. That is a legitimate design choice for doctrine fidelity, but it means the "qualifiers die first" finding is a statement about *this rubric's* sensitivity, not about what compression does to doctrine usefulness in general.
3. *"Load-bearing" in the published record:* the nearest published constructs are (a) structural cues whose loss flips task outcomes (paragraph numbering in Passage Retrieval, class-indicative patterns in TREC/LSHT-ZH — arXiv:2604.02985v1) and (b) minimal-perturbation sensitivity (arXiv:2401.03729). No published study I found isolates "load-bearing qualifiers" as a named compression failure class; the pilot's B2 mechanism is a reasonable hypothesis consistent with (a)/(b) and with hedging-sensitivity, but the docs themselves label it "explanation, not proof".

**Verdict:** Directionally supported (hedges and qualifiers are documented as high-sensitivity, functional elements; their loss under compression is consistent with published findings); the specific B2 mechanism is unverified in the literature and, as implemented, is partly a rubric artifact.

**Implication:** Keep the B2 mechanism as a hypothesis, not a result. To make it load-bearing for doctrine: pre-commit a test that varies the *rubric's* hedge requirement (e.g., score variants with and without the hedge-required rule) and show B2 damage persists under the non-hedge rubric; otherwise the "damage" may be the rubric's own construction. Also report hedge-stripped outcomes against the published assertiveness-preference baseline so readers can calibrate.

---

## 5. C4 — Wave-6 instrument validity: 17/17 near-ceiling genuine; controls 4/4 confab, 3/4 deletion

**Doc anchor:** "17/17 real cells PASS near-ceiling… confab controls 4/4 bit; deletion control 3/4… near-ceiling scores *can* be an artifact of a broken instrument. The deletion control and confab controls are what proved this result real."

**Field evidence:**

1. *Walled/blind, reference-anchored single-answer grading is the documented best practice — the pilot's mechanism matches it.*
   - **Zheng et al.** (arXiv:2306.05685v4, https://arxiv.org/html/2306.05685): names position, verbosity, and self-enhancement biases; GPT-4 pairwise consistency when swapping order is 65.0% (i.e., ~35% of judgments flip with position), Claude-v1 23.8% (75% biased to first); "repetitive list" verbosity attack defeats Claude-v1 and GPT-3.5 in 91.3% of cases; adding a reference answer cuts judge failure on math from 14/20 to 3/20. The pilot's walled-blind, reference-anchored, single-answer rubric grading is exactly the mitigation family this paper recommends.
   - **Judging the Judges** (arXiv:2406.07791v9, https://arxiv.org/html/2406.07791v9; IJCNLP 2025): 15 judges, 150k instances; position bias is systematic, judge- and task-dependent, strongest when the quality gap between candidates is smallest — the pilot's near-ceiling cells (all high-quality variants) are precisely the regime where judge bias is worst, which is why blinding matters.
   - **Scoring Bias in LLM-as-a-Judge** (arXiv:2506.22316v3, https://arxiv.org/html/2506.22316v3): scoring judges are disrupted by rubric/score-ID/reference perturbations; mitigation includes careful score rubrics and reference-answer selection — again, the pilot's design choices (frozen rubric, ref-anchors) are the recommended ones.
2. *Planted controls are a legitimate, emerging meta-evaluation method — but judge sensitivity to planted faults is partial and dimension-dependent, exactly what the pilot observed.*
   - **Reflect** (arXiv:2605.19196v1, https://arxiv.org/html/2605.19196v1): meta-evaluation by controlled interventions on known failure types; "even the best-performing models achieve overall accuracies below 55%" on fine-grained failure detection; **evidence omission is a named failure class that holistic judges systematically miss** — the pilot's B4 deletion-control blindness (an amputated hedge-drop graded "fullest version" 15/15) is the published-normal failure mode, not an anomaly.
   - **PMC medical-summary study** (https://pmc.ncbi.nlm.nih.gov/articles/PMC12786185/): LLM judges caught only 2/9 hallucinations that experts caught, and missed a large numeric error — real-world judges miss planted/real faults frequently. The pilot's confab controls biting 4/4 on a *fabricated doctrine requirement* (a whole invented clause, not a subtle rewording) is plausible and better than typical published sensitivity, but the plants are the easy class of fault; deletion/omission is the hard class (3/4, with B4 blind).
   - **LLM-evaluator survey** (https://eugeneyan.com/writing/llm-evaluators/): GPT-3.5-turbo achieved 58.5% accuracy distinguishing factual from hallucinated summaries; evaluators struggle with implicit hallucinations. Blind-spot work exists as a named research area ("Finding Blind Spots in Evaluator LLMs", arXiv:2406.13439; "LLMs Instead of Human Judges?", arXiv:2406.18403).
   - **Situational-awareness evals** (Laine et al., arXiv:2407.04694) use planted knowledge/control questions as standard practice — planted-control methodology is established, and the pilot's use of it is the right instinct.
3. *The near-ceiling interpretation is weaker than the docs claim: ceiling effects compress reliability, and the experiment's own data contain the classic leniency-drift signature.*
   - **Field data on ceiling effects** (r/mlops Multivac project, 10 months of blind peer eval, https://old.reddit.com/r/mlops/comments/1rfb7kl/): "ceiling effects compress inter-rater reliability"; at near-ceiling scores, "the 1.54-point spread between strictest and most lenient judge is roughly 3.5x the spread between rank-1 and rank-9 models. The judges are generating more variance than the respondents." A 6/6 inter-rater agreement *at ceiling* is exactly what this predicts — agreement at the top of the scale is cheap.
   - **LLM-Judge Ceiling analysis** (https://tianpan.co/blog/2026-04-28-llm-judge-ceiling-auto-eval-human-correlation): judge–human agreement is highest in the easy middle and "collapses on the long tail"; per-slice kappa can be ~0.2 where decisions live; self-inconsistency (intra-rater Krippendorff α 0.3–0.8) means "fair-to-slight agreement with itself" for some judges; a 2026 RAND study is cited with >50% judge error rates on adversarial bias evals. Near-ceiling PASS clusters are low-discrimination regions by construction.
   - **Leniency/score drift is documented and matches the pilot's own B4 anchor drift:** scoring-bias work (2506.22316), leniency-strictness differences between judges (https://www.channel.tel/blog/llm-judge-12-biases), and grading-scale effects on human-LLM agreement (arXiv:2601.03444v1, https://arxiv.org/html/2601.03444v1: scale choice "substantially shifts human-LLM agreement"; pooled reliability masks heterogeneity). The pilot's wave-6 ref-anchor leg read B4 Part-2 at P2=3 vs the frozen 13/15 (P2=1) datum — the instrument drifted toward leniency within the run, and the docs correctly refused to patch it. That drift is *evidence for* the ceiling-as-leniency reading, not merely a footnote: if graders drifted on the reference anchor, "17/17 near-ceiling" contains the same drift.
   - *Statistical power:* 17 real cells, all PASS, base 10–12 of a 12-point gate, deviations of at most −1 integer on one or two parts. A null result at n=17 with a coarse 0–3-per-part rubric cannot distinguish "no effect" from "instrument cannot see the effect" — the docs' own concession ("consistent with a real finding, but not with a permanence claim") is the right scope; the stronger claim ("controls proved this result real") overreaches because the controls exercised only Part-1 sensitivity (confab) and deletion sensitivity on 3 of 4 behaviors, not the P2/P5 dimensions where the small deviations live.
4. *What the controls do and don't prove:* they prove the graders are not wholly blind (they dock planted confabs 4/4 and name deleted qualifiers 3/4), which is meaningful evidence against blanket instrument blindness. They do not prove the near-ceiling is a genuine "no movement" finding, because (a) judge sensitivity is documented as partial and fault-class-dependent (Reflect <55%; medical 2/9; omission blindness), (b) ceiling compresses inter-rater agreement (Multivac field data), and (c) the anchor drift shows leniency drift within the same wave. The B4 blindness is not a bug to be surprised by — it is the predicted outcome for hedge-deletion faults under judges with an assertiveness preference (PolyJudge 1,276/1,280).

**Verdict:** Partially supported. The *controls* are the right instrument and match emerging meta-evaluation practice; their biting (4/4, 3/4) is genuine evidence against total blindness. The *interpretation* (controls prove 17/17 is real, not instrument blindness) is not defensible at the strength stated: the published record says judge sensitivity is partial, ceiling effects inflate agreement, and the pilot's own anchor drift is the leniency signature that ceiling-effect literature predicts.

**Implication:** Report wave-6 as "instrument not blind; sensitivity demonstrated on two fault classes; null result with low power; leniency drift documented" — that is a strong, honest finding. The B4 deletion-control redesign already queued for wave-7 is the right next step; add (a) a rubric-perturbation check (score a subsample under a deliberately stricter rubric to measure drift), (b) per-slice agreement metrics rather than a single 6/6, and (c) power analysis for the "no effect" claim (what effect size could 17 cells detect?). Consider a human/SME grading subsample: every ceiling-effect source in this report ultimately recommends calibrating LLM judges against human raters, and the pilot has SMEs in the consult loop but does not bind their grades.

---

## 6. Cross-cutting internal-consistency findings (from the pilot's own documents)

1. **52.9% not replicated internally:** W2 format arms achieved 28.6%/12.9% savings (INCONCLUSIVE). The flagship lossless number is a single-wave result.
2. **Cliff location shifts across waves:** 40% (W3) → between 20% and 30% (W5) → "no effect at 20–40%" (W6). These are not the same finding restated; they are different outcomes under different rubrics, and the wave-6 document's "matches wave-5" gloss papers over W5's own HURT at 30%-reserved.
3. **Anchor drift is the load-bearing caveat:** the B4 ref-anchor leg fired (P2=3 vs frozen 13/15) and was correctly not patched; every near-ceiling "PRESERVED" in wave-6 must be read relative-to-ref under drifted graders, as the wave-6 document itself says. This caveat should migrate to the six-pager's headline wave-6 row, not live only in §6.
4. **W1 "positive control caught 0/12" is ambiguous** as written (zero plants / zero false alarms vs twelve plants missed). Clarify in the record.
5. **Methodology strengths the record should keep:** pre-registration with forward-only amendments, sealed manifests, byte-level audit, deterministic mechanical transforms, walled graders, ref-anchors, and loud limitation-reporting (B4) are all aligned with or ahead of published practice; nothing in this report suggests the mechanism itself is unsound.

---

## 7. Sources (URLs for every online claim)

**Compression systems & studies**
- https://arxiv.org/html/2604.02985v1 — Prompt Compression in the Wild (ECIR 2026): task-dependent quality; structured/synthetic collapse; rate adherence; latency.
- https://arxiv.org/html/2604.13066v1 — Lossless Prompt Compression via Dictionary-Encoding (60–80%, exact match >0.99, repetitive-data precondition).
- https://arxiv.org/html/2508.19282v3 — CORE: lossless RAG compression at 3% ratio, +3.3 EM.
- https://arxiv.org/html/2310.05736v2 — LLMLingua (up to 20×, little loss).
- https://arxiv.org/html/2403.12968 — LLMLingua-2 (2–5×, faithful token classification).
- https://www.prompthub.us/blog/compressing-prompts-with-llmlingua-reduce-costs-retain-performance — plateau-then-drop curves, GSM8K −1.44/−1.52 at 14×/20×.
- https://arxiv.org/html/2505.00019v1 — Empirical study, 6 methods/13 datasets; long-context sensitivity; moderate compression helps LongBench.
- https://arxiv.org/html/2407.15504v1 — Rate–distortion fundamental limits (NeurIPS 2024).
- https://arxiv.org/html/2307.03172v2 — Lost in the Middle.
- https://arxiv.org/html/2508.13666v1 — Code-formatting token overhead (24.5% input; safe to remove).
- https://arxiv.org/html/2408.02442v1 — Format restrictions degrade reasoning.
- https://arxiv.org/html/2401.03729v2 — Butterfly effect of prompt perturbations (a space can flip answers).
- https://community.openai.com/t/markdown-is-15-more-token-efficient-than-json/841742 ; https://david-gilbertson.medium.com/llm-output-formats-why-json-costs-more-than-tsv-ebaf590bd541 — format token overhead (non-peer-reviewed).

**Judge bias / meta-evaluation**
- https://arxiv.org/html/2306.05685 — Zheng et al., LLM-as-a-judge (position 65%/23.8% consistency; verbosity 91.3% failure; reference prompt 3/20; >80% human agreement).
- https://arxiv.org/html/2406.07791v9 — Judging the Judges: systematic position-bias study (150k instances).
- https://arxiv.org/html/2506.22316v3 — Evaluating Scoring Bias in LLM-as-a-Judge.
- https://arxiv.org/html/2601.03444v1 — Grading-scale impact (0–5 best; pooled reliability masks heterogeneity).
- https://arxiv.org/html/2605.19196v1 — Reflect: judge meta-evaluation by controlled interventions (<55% accuracy; omission blindness).
- https://aclanthology.org/2026.acl-srw.33/ — PolyJudge-Uncertain: judges prefer assertive answers 1,276/1,280 pairwise.
- https://eugeneyan.com/writing/llm-evaluators/ — LLM-evaluator survey (58.5% hallucination discrimination; reference-based grading).
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12786185/ — Medical summaries: judges caught 2/9 hallucinations.
- https://tianpan.co/blog/2026-04-28-llm-judge-ceiling-auto-eval-human-correlation — LLM-judge ceiling; per-slice agreement; intra-rater α 0.3–0.8.
- https://old.reddit.com/r/mlops/comments/1rfb7kl/observations_on_llmasjudge_calibration_in/ — field data: ceiling compresses inter-rater reliability; judge spread > model spread.
- https://www.channel.tel/blog/llm-judge-12-biases — leniency/strictness across judges.
- https://mbrenndoerfer.com/writing/position-bias-in-llm-judges — position/verbosity/tone-sycophancy synthesis.
- https://www.lesswrong.com/posts/vBDupg8iPqgdwhFzz/demands-are-all-you-need-prompt-imperativeness-drastically — imperativeness × hedging (n=900; non-peer-reviewed).
- https://dl.acm.org/doi/fullHtml/10.1145/3630106.3658941 — "I'm Not Sure, But…" (CHI 2024): uncertainty expressions change reliance/trust.
- https://arxiv.org/abs/2407.04694 — Me, Myself and AI (SAD): planted-knowledge eval methodology.

**Methodology notes / limitations of this verification**
- Browser-harness reads succeeded for all target pages; one PDF (aclanthology 2026.acl-srw.33.pdf) timed out via firecrawl and was replaced by the anthology abstract page; Reddit read via old.reddit.com. No CAPTCHA/login walls encountered.
- Source-quality flags: LessWrong imperativeness study and r/mlops field report are non-peer-reviewed; the OpenAI community forum and Medium token-overhead posts are practitioner reports; all are marked as such above and are used only for direction, not as primary numbers.
- arXiv:2604.02985 exists and was read in full (abstract, §4.3–4.5, conclusion) — the reference the pilot's docs imply is real.
