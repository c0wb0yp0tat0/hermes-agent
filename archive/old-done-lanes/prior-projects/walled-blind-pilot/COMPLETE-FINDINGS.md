# COMPLETE FINDINGS — Walled-Blind Compression Experiment (Waves 1–6)

**Compiled:** 2026-08-19 · **Host:** pve-1 · **Purpose:** full, uncondensed review record — every finding from the supervisor's review and all five worker research passes, verbatim from their on-disk deliverables.

---

## How to read this document

This file contains, **in full and unedited**:

| Section | Source file | Status |
|---|---|---|
| PART 0 — Supervisor's review | (this session, reconstructed verbatim) | Operative |
| PART 1 — Worker A, verification vs literature (harness batch) | `worker-A-verification-v2.md` | Operative |
| PART 2 — Worker A, verification (search batch) | `worker-A-verification.md` | Preserved-selected (Worker D audit) |
| PART 3 — Worker B, decision evidence (harness batch) | `worker-B-decisions-v2.md` | Operative |
| PART 4 — Worker B, decision brief (search batch) | `worker-B-decisions.md` | Preserved-selected (Worker D audit) |
| PART 5 — Worker C, external readiness (harness batch) | `worker-C-readiness-v2.md` | Operative |
| PART 6 — Worker C, external readiness (search batch) | `worker-C-readiness.md` | Preserved-selected (Worker D audit) |
| PART 7 — Worker C iteration 2, executable pre-share package | `worker-C-iteration2.md` | Operative — the share-side operative artifact |
| PART 8 — Worker D, audit of the disregarded batch | `worker-D-disregarded-audit.md` | Operative — verdict: PRESERVE-SELECTED |
| PART 9 — Master assessment (consolidation + execution plan) | `00-MASTER-ASSESSMENT.md` | Operative — synthesis layer |

**Provenance notes:**
- The three source documents under review (`loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md`, `wave6-grading-finding.md`) are not re-printed here — they were supplied by the owner and are the object of the review; every finding below cites them.
- "Harness batch" = research executed with the browser-harness method (`BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use`). "Search batch" = web_search/web_extract only. Both sets are preserved; Worker D audited the set-aside (search-batch) reports and their corrections are catalogued in PART 8.
- All online claims in every report carry their source URLs; grounding taxonomy (DOC-GROUNDED / ONLINE-GROUNDED / UNVERIFIABLE) is used per report.
- What remains UNVERIFIABLE from this host (on-disk artifacts on the original host) is stated in PART 0 §5 and PART 9 Part 6.

---

# PART 0 — SUPERVISOR'S REVIEW

*Reconstructed verbatim from the supervisor's review message of 2026-08-19, the first full pass over the three source documents. This review was performed before any worker was dispatched; the workers were blind to it.*

## Scope
Full read of all three; arithmetic re-derived by hand; cross-doc consistency traced claim-by-claim. Byte-level artifacts (seals, logs, audits, directory state) live on the other host — flagged as unverifiable from here rather than asserted.

## Bottom line
Coherent, honestly scoped, internally consistent on every headline number re-derivable from the documents. **One real discrepancy** (manifest seal hash) that needs a byte-level resolution on the other host, plus four minor editorial items. The epistemic discipline holds up to the standard.

## 1. Cross-doc consistency — verified

| Claim | Status |
|---|---|
| W1: 52.9%, 12/12, control caught 0/12 (teeth = can fail) | ✓ six-pager = pattern |
| W3: HURT ≤60%, cliff at 40%, B2 qualifiers die first | ✓ six-pager = pattern |
| W5: NO ADOPTION; 20-reserved PRESERVED; cliff between 20–30% | ✓ |
| W6: 17/17 near-ceiling; confab 4/4; deletion 3/4 (B4 INCONCLUSIVE); inter-rater 6/6 HIGH | ✓ six-pager = pattern = finding |
| B4 drift: ref-anchor P2=3/15 vs frozen 13/15 (P2=1), not patched | ✓ all three |
| Decision record: nothing adopted, KEEP FULL PROSE, G1–G4 open | ✓ six-pager = pattern §4 lifecycle |

## 2. Arithmetic re-derivation — all pass
- 17 real cells = 4 (b1) + 5 (b2) + 4 (b4) + 4 (b6) ✓; 25-cell audit = 17 + 4 DEL + 4 ctrl ✓
- base = P1–P4, total = base + P5 — every row in finding §3–§5 re-summed correctly (bases 10–12, totals 12–15)
- DEL verdicts under amendment-002 table: b1/b2/b6 docked-and-named → HURT ✓; b4 undocked → INCONCLUSIVE ✓ (correctly never PRESERVED)
- ctrl cells: P1=1 dock → TEETH under cl.1 dominance ✓; PASS at bases 9/10, FAIL at 8/7 — matches the rubric (PASS = base ≥ 9, no part 0, P3 & P5 ≠ 0) ✓
- Inter-rater 6/6 ✓; b4-20-unreserved no-op INCONCLUSIVE carried with no weight ✓

## 3. The one real discrepancy — wave-6 manifest seal
- **Finding** (the sealed record, full hash, four places): manifest seal = `6461c201…`, recomputed, round-trips; the post-O3 re-seal is `6461c201…`.
- **Pattern §5b**: the same post-O3 re-seal = `44a18890…`.
- **Six-pager §2**: "wave-6 manifest `44a18890…`; consult leg re-derived seal `6461c201…` — both verify." That labels `6461c201` a consult-leg re-derivation — contradicting the finding, which says it is the manifest's own verified seal.

Two different hashes for what reads as the same file. Unresolvable from the three docs — the discipline's own P10 says the FILE wins. Needs one recomputation on the other host: which hash is the current wave-6 answer-pack manifest seal (minus the seal section, am.§4 boundary)? One of the three docs carries a stale or mislabeled value.

Related question: the six-pager §5 closure added a W6 ledger line to MANIFEST — is that ledger a *different* file from the sealed answer-pack manifest? If the same file, `6461c201` cannot still round-trip post-closure.

## 4. Minor editorial flags
- **W2 row** in the six-pager table is "(per record)" — the only blank in the narrative; fill or footnote before sign-off.
- **Pattern §6**: "The original four items…" then lists **five**.
- **Six-pager §2** calls amendment-001 the "frozen dock predicate" — per the finding header and pattern §6, 001 is the instrument-validity controls amendment; the deletion-dock decision table is **amendment-002's** subject (001 cl.3 originated it). Loose label.
- "Cliff at 40%" (W3–5 merged row) sits next to W5's "true cliff between 20–30%"; a fresh reader could take the coarser number as final — add a pointer.

## 5. Not verifiable from here (on-disk claims)
Lottery seal reproducibility; 8/8 rulebook tests; byte audit 25/25; deletion logs; tokenizer loud-fail; ledger + experiment-conclusion edits; the seal recomputations. Not doubted — outside what these three files can prove.

## 6. Assessment
The genuinely strong parts: no adoption/permanence/generalizability claims; INCONCLUSIVE never counted as PRESERVED; drift reported loudly, never patched; controls in every batch; consult objections recorded and folded forward-only. That's the discipline working as documented.

Recommendation at the time: **resolve the seal discrepancy before the §5/§7 sign-off** — record hygiene, exactly the class of thing the intern leg caught at closure.

*(Later passes added: the grader-identity contradiction [local vs cloud backend — PART 7 §C2.3], the W1 "caught 0/12" ambiguity, cross-wave comparability under amendment-001/002, and the transform-unspecified 52.9% — see Parts 1–9.)*

---


---

# PART 1 — WORKER A (HARNESS BATCH): VERIFICATION REPORT — worker-A-verification-v2.md

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

---

# PART 2 — WORKER A (SEARCH BATCH): VERIFICATION REPORT — worker-A-verification.md

# Independent Verification Report — Walled-Blind LLM Compression Experiment (Waves 1–6)

**Prepared by:** Worker A (independent verification subagent)
**Date:** 2026-08-19
**Scope:** Pressure-test the empirical claims of the walled-blind compression experiment described in `loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md`, and `wave6-grading-finding.md` against the published literature (prompt compression, LLM-as-judge bias, evaluation-control methodology, ceiling effects).
**Method:** Web research only (web_search / web_extract; no browser). All claims below are anchored to published or otherwise citable sources with URLs. Doc quotes are kept minimal; this report is dominated by the external record.
**Status of the four claims tested:**

| # | Claim (as asserted in the docs) | Verdict |
|---|---|---|
| 1 | Lossless format-level compaction saves 52.9% tokens at 12/12 fidelity (W1) | **Plausible / supported, under conditions** — same magnitude published for format-level changes; but "fidelity" was measured with n=12 rubric cells, and format sensitivity literature warns rubric-stability ≠ behavioral-stability |
| 2 | Lossy semantic compression HURT at ≤60% deletion, cliff at 20–40%; load-bearing qualifiers/hedges die first (W3–W5) | **Supported as a conditional, domain-scoped finding** — strongly matches published results for structured/dense text; the unconditional form would be contradicted by the RAG-compression literature, which the docs do not claim |
| 3 | Walled-blind grading + planted confab/deletion controls + inter-rater checks are the right controls (P1–P10) | **Supported** — these are exactly the mitigations the judge-bias literature prescribes; but raw-agreement inter-rater without chance correction, and multi-criterion rubric scores, are weaker than reported |
| 4 | Wave-6 17/17 near-ceiling is a genuine "no movement" result because controls bit (4/4 confab, 3/4 deletion) (W6) | **Partially supported** — the control-bite logic is the right idea, but the instrument's own B4 deletion-control blindness plus documented ceiling-effect and omission-blindness findings mean "genuine, not instrument blindness" is not established for the subtle damage classes; B4-family real cells should be read with the same INCONCLUSIVE caveat the docs applied to the B4 control |

---

## Verification area 1 — Lossless / format-level prompt compression (W1: 52.9% savings, 12/12 fidelity)

**CLAIM (one line):** A pure format-level change (no semantic change) cut envelope token count by 52.9% with zero measured fidelity loss (12/12 vs 12/12), verified by a positive control that bit 0/12.

**FIELD EVIDENCE:**

1. **Format-level savings of ~50% with no accuracy loss are published.** ONTO (arXiv:2604.17512, Apr 2026) reports that converting JSON to a columnar "schema-once, data-many" notation yields **46–51% token reduction** across three synthetic operational datasets, with "no material degradation in LLM task accuracy" on lookup/counting/extraction/aggregation benchmarks (Qwen2.5-7B), and attributes most JSON overhead to repeated field names and structural punctuation. https://arxiv.org/html/2604.17512v1 — This is the closest published analog to the W1 claim, at essentially the same magnitude (46–51% vs 52.9%).
2. **Structural overhead of verbose formats is a recognized, quantified phenomenon.** Practitioner-grade token-efficiency analyses (TOON vs JSON, Tensorlake 2025; MightyBot structured-format survey) document that JSON/XML syntax and repeated keys dominate token counts in structured prompts, and that row-oriented encodings preserve task accuracy when format context is clear. https://tensorlake.ai/blog/toon-vs-json ; https://mightybot.ai/blog/best-structured-prompt-formats-for-llms/ — consistent with a ~50% savings ceiling for boilerplate-heavy envelopes.
3. **"Lossless" in the compression literature is a different, weaker claim.** CORE (arXiv:2508.19282, v4 2026) achieves "lossless context compression" for RAG — defined as *task-performance-lossless* — by training a compressor with reinforcement learning against downstream reward (average EM +3.3 points at extreme compression, e.g., NaturalQuestions 0.3803 EM @ 712 tokens → 0.3947 @ 47 tokens). https://arxiv.org/html/2508.19282v3 — Published "lossless" means "no performance loss," not "no content change," and it requires training on downstream signal. The W1 claim is the stronger (and easier) claim: zero semantic change by construction, so any savings are pure format overhead.
4. **Extractive, deletion-only compression with faithfulness guarantees is a published design.** LLMLingua-2 (arXiv:2403.12968, ACL 2024 Findings) formulates compression as token classification, uses pure extraction (no new words), and "guarantees faithfulness of the compressed prompt to the original content," operating at 2x–5x compression with modest task losses (MeetingBank QA 87.75 original → 86.92 at 3.1x). https://arxiv.org/html/2403.12968v2 — The docs' mechanical deletion discipline matches this design family.
5. **Caution 1: format changes are not behaviorally inert in general.** Sclar et al. (arXiv:2310.11324) show open LLMs are "extremely sensitive to subtle changes in prompt formatting," with performance differences of up to 76 accuracy points across semantically equivalent prompt variants (few-shot, LLaMA-2-13B). https://arxiv.org/abs/2310.11324 — This does not contradict W1 (format-overhead removal in envelopes is not the same as adversarial reformatting), but it means "rubric showed 12/12 both ways, n=12" is a weak probe of behavioral equivalence. LLMLingua's own budget controller (arXiv:2310.05736) compresses demonstrations most aggressively and instructions/questions least, i.e., content-bearing components are treated as load-bearing while redundant structure is not — the same assumption W1 makes.
6. **Caution 2: token savings ≠ latency savings.** "Prompt Compression in the Wild" (arXiv:2604.02985, Kummer et al., ECIR 2026; 30,000+ runs) finds LLMLingua-family compressors achieve up to 18% end-to-end speed-up only in a narrow operating window (unoptimized serving frameworks, prompts >~5k tokens); under vLLM or commercial APIs the compression overhead cancels the gains. https://arxiv.org/html/2604.02985v1 — The docs' W1 is a *token-count* claim, which is legitimate; it should not be read as a latency or cost claim without the wild paper's conditions.

**VERDICT:** **Supported as plausible and precedented.** ~50% format-level token savings at zero measured quality loss is published (ONTO: 46–51%; LLMLingua-2: faithful extractive compression at 2–5x). The 12/12 fidelity result is consistent with the record but is a small-n rubric measurement, and the format-sensitivity literature (Sclar et al.) plus the wild paper's finding that *even slight compression can harm outputs in ways surface metrics miss* argue for a behavioral (downstream-task) probe before adoption.

**IMPLICATION:** W1 is the most defensible claim in the set, but "12/12 fidelity" should be re-verified with (a) a downstream behavioral task on the actual delegation stack (e.g., task accuracy with compressed vs full envelopes), and (b) a larger cell count. The docs' posture — flagged recommendation, not yet implemented — is the correct reading of the evidence.

---

## Verification area 2 — Lossy compression cliffs and "load-bearing qualifiers die first" (W3–W5)

**CLAIM (one line):** Semantic (deletion-based) compression HURT at ≤60% deletion with a cliff at 40%, refined by W5 to a true cliff between 20% and 30% deletion; the first things to die are load-bearing qualifiers (B2) and hedge/reversibility behaviors, and the damage is invisible without blind grading.

**FIELD EVIDENCE:**

1. **Structured/dense text is exactly where published compression fails hardest.** The wild-compression paper (arXiv:2604.02985) is the most on-point published result: "Synthetic tasks exhibit the strongest negative effects" — Passage Counting accuracy drops from below 20% to below 4.5%; Passage Retrieval falls "sometimes to below 50% because it depends on the structural cue of paragraph numbering, which is lost through compression"; the authors conclude "**LLMLingua-2 is unsuitable for compressing structured synthetic datasets**." Code generation shows "significant drops in edit similarity" even at a mild 1.4x ratio; few-shot classification tasks lose up to 52% because "the compression process likely removes class-indicative patterns." https://arxiv.org/html/2604.02985v1 — Doctrine text is structured, dense, and prescriptive; the published record says exactly this class of input degrades under lossy deletion, often at low ratios.
2. **Information-dense tasks degrade steeply at moderate ratios.** LLMLingua-2's own numbers: task-agnostic 3.9x compression on NaturalQuestions (20 documents) drops EM from 75.7 (original) to 48.6 — a 27-point cliff on a knowledge-dense task — while MeetingBank QA at 3.1x loses only ~1 point (87.75 → 86.92), and LongBench-ZH at 5x averages 42.5 → 38.1. https://arxiv.org/html/2403.12968v2 — i.e., the same compressor ranges from near-lossless to catastrophic depending on text density and task; the docs' doctrine task sits on the catastrophic side of this distribution.
3. **Cliffs at extreme ratios are documented; cliffs at mild ratios are documented for specific content classes.** LLMLingua (arXiv:2310.05736): "as the compression ratio increases, especially around 25x-30x, all methods as well as ours will experience a substantial performance drop." https://arxiv.org/html/2310.05736v2 — The wild paper adds the low-ratio cases (code edit-similarity at 1.4x; structured tasks at ~3.7x average). A cliff at 20–30% deletion for dense prescriptive prose is sharper than most published curves, but it is the same phenomenon the wild paper reports for structured tasks, at a comparable ratio.
4. **Counter-evidence (why the claim must stay scoped):** lossy compression frequently *helps* in long-context/retrieval settings. LongLLMLingua (arXiv:2310.06839) reports up to +21.4% on NaturalQuestions with ~4x fewer tokens (GPT-3.5-Turbo), by removing noise from long contexts; CORE improves EM while keeping a small fraction of tokens; the wild paper finds Mistral-7B improves under compression when its 8k context previously truncated the input, and summarization is robust to 5.7x. https://arxiv.org/abs/2310.06839 — The published record therefore supports "lossy hurts" *conditionally*: dense, structured, low-redundancy text where every qualifier carries meaning. The docs explicitly scope the claim to "this doctrine and stack," which is the correct scoping; the claim would be false as a general law.
5. **Hedges/qualifiers as load-bearing content has a long published pedigree.** (a) Biomedical NLP has treated hedging/negation as decision-relevant semantics for over a decade: the BioScope corpus (Vincze et al. 2008) annotates negation and speculation as scoped phenomena; hedge-cue detection was a CoNLL-2010 shared task (Morante & Daelemans 2009; Agarwal et al. 2010). https://rgai.inf.u-szeged.hu/node/105 ; https://aclanthology.org/W09-1304.pdf — (b) Calibration literature shows verbalized confidence/hedging carries real signal: Xiong et al. (arXiv:2306.13063) find verbalized confidence is informative for failure prediction (AUROC ~0.52–0.61) even though models are systematically overconfident (verbalized values cluster in the 80–100% band); "Llamas Know What GPTs Don't Show" (arXiv:2311.08877) shows linguistic confidence markers correlate with correctness. https://arxiv.org/abs/2306.13063 — (c) The wild paper's "class-indicative patterns pruned → classification fails" is the same mechanism as the docs' B2 "load-bearing qualifier lost → behavior degrades": deletion damage concentrates in exactly the tokens that carry discriminative/conditional meaning.
6. **"Damage invisible without blind grading" is consistent with the record.** The wild paper's code result — surface metrics (e.g., pass-rate-style) look stable while edit similarity collapses — is a published instance of compression damage that only shows on a sensitive probe. The docs' claim that HURT was only visible under blind rubric grading is compatible with this.

**VERDICT:** **Supported, with the scoping the docs already assert.** The direction of the finding (lossy deletion hurts dense structured text; qualifiers/conditions are the load-bearing layer; damage can be metric-invisible) matches published results, most directly the wild-compression paper's structured-data findings and the LLMLingua-2 NQ results. What the literature does *not* support is any generalization to noisy/long-context settings, where compression often helps — and the docs do not make that generalization. The "cliff between 20% and 30%" is a sharper cliff than most published curves, which is plausible for this content class but should be reported as a domain-specific result.

**IMPLICATION:** The KEEP FULL PROSE posture is well-grounded for doctrine-bearing envelopes. For the wider orchestration stack, the conditional nature means each envelope class (instructions vs retrieved context vs few-shot exemplars) needs its own compression-vs-fidelity curve; the pattern's own machinery (prereg + cliff location) is the right tool for that, and the pattern document's claim that it "produces trustworthy negatives, locates cliffs precisely" is supported by the literature's demonstrated task-dependence of cliffs.

---

## Verification area 3 — Evaluation-controls practice (blinding, planted controls, inter-rater)

**CLAIM (one line):** Walled-blind grading, planted confabulation controls, deletion controls, ref-anchors, and inter-rater agreement are the right and necessary controls for LLM evaluation, and the absence of blinding is what makes LLM compression damage easy to miss.

**FIELD EVIDENCE:**

1. **The judge-bias literature is unambiguous that unblinded, same-context evaluation is biased.** Zheng et al. (arXiv:2306.05685, MT-Bench/Chatbot Arena): LLM judges exhibit position bias (most favor the first answer; only GPT-4 was consistent >60% of cases), verbosity bias (longer answers preferred even when worse), and self-enhancement bias (GPT-4 favored its own outputs ~10% and Claude-v1 ~25% more often than human-equivalent quality warranted); recommended mitigations are exactly the docs' mechanisms: randomize/swap positions, blind the judge, instruct against verbosity. https://arxiv.org/abs/2306.05685 — Wang et al. (arXiv:2305.17926, ACL 2024): positional bias in GPT-4-as-referee, with a calibration framework. https://arxiv.org/abs/2305.17926 — Panickssery et al. (arXiv:2404.13076, NeurIPS 2024): causal link between an evaluator's self-recognition ability and self-preference; LLMs can identify their own generations and score them higher. https://arxiv.org/abs/2404.13076 — The LLM-as-a-Judge survey (arXiv:2411.15594) frames reliability as the field's open problem, requiring "careful design and standardization." https://arxiv.org/abs/2411.15594
2. **The docs' control package goes beyond typical published practice.** Most published LLM evals (including the MT-Bench work itself) use an unblinded judge with labeled answers. The docs' wall (no labels, no hypothesis, no prior waves), order shuffling per grader, and independent grader legs implement the published mitigations; planted confabulation controls are the LLM-eval analog of **catch trials / instructional manipulation checks**, which are standard in survey methodology precisely to detect inattentive or satisficing raters (Oppenheimer, Meyvis & Davidenko 2009; Thomas & Clifford, "It's a Trap!", SAGE Open 2015). https://journals.sagepub.com/doi/10.1177/2158244015584617 ; https://www.academia.edu/6461937/Instructional_manipulation_checks_Detecting_satisficing_to_increase_statistical_power — Deletion controls as negative controls (instrument must not pass an amputee) are a direct transposition of standard positive/negative-control logic in experimental design; their deployment in LLM eval is still rare enough that the docs' P5/P6/P8 design is above the field's typical bar.
3. **Blinding/counterbalancing is standard in human NLG evaluation, from which LLM-judge practice borrows.** Howcroft et al., "Twenty Years of Confusion in Human Evaluation" (INLG 2020), documents that reliable human evaluation requires standardized definitions, evaluation sheets, and controlled designs (blinding, counterbalancing) — the same discipline the docs apply to model graders. https://aclanthology.org/2020.inlg-1.23/
4. **Two weaknesses in the docs' control implementation, per the literature:**
   - **Inter-rater is raw agreement, not chance-corrected.** The docs report 6/6 = 100% agreement on a 0–3 scale at near-ceiling. At a ceiling distribution (most scores = 3), chance agreement is very high; raw percentage agreement overstates reliability. Chance-corrected agreement (Cohen's kappa / Krippendorff's alpha; reliability criteria in Terwee et al. 2007) is the standard metric, and would be far lower than 100% for this distribution. https://pubmed.ncbi.nlm.nih.gov/17161752/
   - **Multi-part rubric scores may not be independent dimensions.** Hu et al. (arXiv:2402.12055, ACL 2024) find LLM evaluators "confuse different evaluation criteria" and "frequently rely on their own interpretations" rather than the rubric; 18 perturbation types show cross-dimension contamination. https://arxiv.org/abs/2402.12055 — A 5-part rubric graded by an LLM may be effectively one holistic lenient score, which matters for interpreting near-ceiling "all parts 3" patterns.

**VERDICT:** **Supported.** The walled-blind design, planted controls, and independent graders are precisely what the published judge-bias and evaluation-methodology literature prescribes, and they are deployed more rigorously than in most published LLM evals. Two implementation details are weaker than presented: raw-agreement inter-rater without chance correction, and the implicit assumption of rubric-dimension independence.

**IMPLICATION:** Keep the wall and the controls (they are necessary); add kappa/alpha reporting; check per-dimension score correlation to detect criterion confusion; if feasible, use grader models from a different family than writer models (the docs' cloud-backed graders vs local writers already reduces the Panickssery self-preference risk, but the grader/writer model identities should be recorded and disclosed).

---

## Verification area 4 — Near-ceiling instruments (W6: 17/17 near-ceiling, controls bit 4/4 and 3/4)

**CLAIM (one line):** Wave-6's 17/17 near-ceiling with zero real-cell flags is a genuine "no movement" finding, not instrument blindness, *because* the planted confabulation controls bit 4/4 and deletion controls bit 3/4 (B4 INCONCLUSIVE), with inter-rater 6/6 HIGH.

**FIELD EVIDENCE:**

1. **By standard criteria, this instrument has a ceiling effect at these points.** Terwee et al. (2007) define a ceiling effect as present when >15% of respondents achieve the highest score; ceiling effects limit an instrument's ability to detect change/damage. https://www.sciencedirect.com/science/article/abs/pii/S0895435606001740 — 17/17 real cells at base ≥10/12 (most at 14–15/15) is 100% at/near the ceiling, far past the 15% threshold. The near-ceiling is therefore a *measurement property of the instrument at these points*, not an empirical result about compression.
2. **LLM graders are documented as lenient and omission-blind.** (a) Xiong et al. (arXiv:2306.13063): LLMs verbalize confidence predominantly in the 80–100% band and are systematically overconfident — a judge-side prior that pushes rubric scores up. (b) SummEdits (Laban et al., arXiv:2305.14540 / EMNLP 2023): LLMs are poor at detecting planted factual inconsistencies — most models near chance, best model (GPT-4) still 8% below human; edit-type analysis shows negation-related and insertion-type edits are among the hardest for weaker models. https://ar5iv.labs.arxiv.org/html/2305.14540 — (c) Practitioner literature on omissions vs hallucinations (Reiter, Feb 2026) notes omission errors are common, consequential, and under-studied relative to fabrication. https://ehudreiter.com/2026/02/11/dont-ignore-omissions/ — The docs' B4 deletion control failing (a hedge-drop amputee graded 15/15 "fullest version," no deletion named) is a live instance of this documented weakness: LLM graders demonstrably miss exactly the damage class (deleted hedges/qualifiers) that the experiment's W3–W5 findings say is load-bearing.
3. **The control-bite argument is sound but partial.** Confab controls 4/4 and deletion controls 3/4 show the instrument can fail loudly — this genuinely rules out the "instrument grades everything a pass" failure mode. But controls only probe the specific damage classes they plant. The literature (SummEdits: most models near chance on planted edits; wild paper: metric-invisible damage on structured tasks) supports the proposition that there exist damage classes the same judge model will not see. The B4 deletion-control blindness is direct evidence that the grader model misses at least one relevant class *in this very experiment*. So "controls prove the near-ceiling is real" is only established for the probed classes; the conclusion should be: the instrument detects confabulation and gross deletions on 3/4 behaviors, and is demonstrably blind to hedge-drop on the fourth.
4. **Judge drift makes cross-wave near-ceiling comparisons unstable.** Chen, Zaharia & Zou (arXiv:2307.09009): the "same" model service varies substantially over time (GPT-4 prime-number accuracy 84% → 51% between March and June 2023 versions, with instruction-following drift). https://arxiv.org/abs/2307.09009 — The docs' own B4 anchor drift (frozen wave-5 datum P2=1 / 13/15 vs wave-6 reads P2=2–3 / 15/15 by both the pack grader and the independent ref-anchor grader) is consistent with between-wave judge leniency drift, and the docs' choice to freeze the old datum means wave-6 B4 "PRESERVED" scores are measured against a moving standard — which the docs themselves flag.
5. **Criterion confusion can manufacture all-parts-high scores.** Hu et al. (arXiv:2402.12055) show LLM evaluators conflate rubric dimensions; an "all 3s" pattern on a 5-part rubric may be one lenient holistic judgment rather than five independent confirmations. This weakens the reading of "no part below anchor" as multi-dimensional evidence of preservation.
6. **Contextual consistency check:** W6's real cells are mostly 20–30% *reserved* compression (and one 40% reserved), a regime W5 already found PRESERVED. A near-ceiling in W6 is therefore consistent with W5 and does not conflict with the W3–W5 HURT findings (which were about unreserved semantic deletion at 40–60%). The near-ceiling result is not surprising; the open question is only what it proves.
7. **General lesson from benchmark saturation:** MMLU-Redux (arXiv:2406.04127) shows near-saturated benchmarks hide real differences — 6.49% of MMLU questions contain errors, and re-evaluation shifts model rankings. https://arxiv.org/abs/2406.04127 — Near-ceiling scores are precisely where measurement noise and judge leniency dominate; the burden of proof for "no movement" is higher, not lower, at the ceiling.

**VERDICT:** **Partially supported; the strong form is not established.** The 17/17 near-ceiling is a real measurement, and the 4/4 + 3/4 control bites rule out wholesale instrument failure. But (a) by the standard ceiling-effect criterion the instrument lacks resolution at these points; (b) the published record shows LLM graders are omission-blind, and this experiment contains its own instance (B4 amputee graded 15/15); (c) judge drift between waves is documented, and the docs' own anchor drift is an instance; (d) criterion confusion undermines the multi-dimension reading. The defensible conclusion is: "no movement was detected, and the instrument can catch some damage classes — but it demonstrably cannot catch the hedge-drop class on B4, so B4-family near-ceiling PASSes carry the same INCONCLUSIVE caveat the docs applied to the B4 control." The docs' interpretation ("controls prove it is real, not instrument blindness") overstates what the controls can establish; their own B4 limitation section is the more accurate reading of the evidence.

**IMPLICATION:** Before treating "no PASS↔FAIL movement" as a finding: (1) redesign the deletion control so it bites on every behavior (the docs' own wave-7 plan) — until then, real cells of any behavior whose deletion control is blind must be reported INCONCLUSIVE, not PASS; (2) report chance-corrected inter-rater agreement and score distributions (not just means) to make the ceiling visible; (3) re-anchor the rubric each wave against a fresh reference read (the frozen-datum policy preserves integrity but leaves cross-wave comparability broken — the drift must be resolved as an amendment, which the docs already schedule for wave 7); (4) increase n and add harder probes (smaller deletions, more subtle confabs) since ceiling-limited instruments need harder items to discriminate; (5) treat near-ceiling "no movement" as consistent-with-but-not-proof-of preservation, and say so in the conclusion memo.

---

## Cross-cutting observations

1. **Preregistration is an accepted but uncommon practice in ML/NLP, and the docs' version is disciplined.** Kapoor & Narayanan, "Pre-registration for Predictive Modeling" (arXiv:2311.18807), advocate preregistration to prevent data-dependent decisions and test-data reuse, and document its limits (self-selection; does not fix distribution shift; can be gamed by bad-faith actors). https://arxiv.org/html/2311.18807v1 — The docs' frozen contract + forward-only amendments + sealed manifests implement the recommendation correctly; the amendment-002 fix (deletion-dock predicate corrected before grades were read) is exactly the behavior preregistration is meant to enable.
2. **Small n and single-domain limits are real and acknowledged.** The docs' own limitations section (small n; one doctrine; one stack; no permanence/generalizability claims) matches what the literature would advise. Nothing in the external record contradicts the *procedural* claims (seals round-trip, audits pass, controls bit); those are internal artifacts that cannot be verified externally and were not the subject of this review.
3. **The single most decision-relevant external finding:** the wild-compression paper's "LLMLingua-2 is unsuitable for compressing structured synthetic datasets" (arXiv:2604.02985) is a published, independent confirmation of the direction of the docs' core result (lossy compression fails on structured text), and the ONTO paper (arXiv:2604.17512) is an independent confirmation of the magnitude of safe format-level savings (~50%). The experiment's two headline numbers sit inside the published envelope of plausible results.

## Sources (verified during this review)

- Kummer, Jurkschat, Färber, Vahdati. *Prompt Compression in the Wild: Measuring Latency, Rate Adherence, and Quality for Faster LLM Inference.* arXiv:2604.02985 (ECIR 2026). https://arxiv.org/html/2604.02985v1
- Deekeswar. *ONTO: A Token-Efficient Columnar Notation for LLM Input Optimization.* arXiv:2604.17512. https://arxiv.org/html/2604.17512v1
- Pan et al. *LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression.* arXiv:2403.12968 (ACL 2024 Findings). https://arxiv.org/html/2403.12968v2
- Jiang et al. *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models.* arXiv:2310.05736 (EMNLP 2023). https://arxiv.org/html/2310.05736v2
- Jiang et al. *LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression.* arXiv:2310.06839 (ACL 2024). https://arxiv.org/abs/2310.06839
- Cui et al. *CORE: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning.* arXiv:2508.19282. https://arxiv.org/html/2508.19282v3
- Zheng et al. *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* arXiv:2306.05685 (NeurIPS 2023). https://arxiv.org/abs/2306.05685
- Wang et al. *Large Language Models are not Fair Evaluators.* arXiv:2305.17926 (ACL 2024). https://arxiv.org/abs/2305.17926
- Panickssery, Bowman, Feng. *LLM Evaluators Recognize and Favor Their Own Generations.* arXiv:2404.13076 (NeurIPS 2024). https://arxiv.org/abs/2404.13076
- Gu et al. *A Survey on LLM-as-a-Judge.* arXiv:2411.15594. https://arxiv.org/abs/2411.15594
- Hu et al. *Are LLM-based Evaluators Confusing NLG Quality Criteria?* arXiv:2402.12055 (ACL 2024). https://arxiv.org/abs/2402.12055
- Liu et al. *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172 (TACL 2024). https://arxiv.org/abs/2307.03172
- Xiong et al. *Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs.* arXiv:2306.13063 (ICLR 2024). https://arxiv.org/abs/2306.13063
- Shrivastava et al. *Llamas Know What GPTs Don't Show: Surrogate Models for Confidence Estimation.* arXiv:2311.08877. https://www.semanticscholar.org/paper/Llamas-Know-What-GPTs-Don't-Show%3A-Surrogate-Models-Shrivastava-Liang/df9981b9bbfc619652e84cd0eefa595274da2fef
- Laban et al. *SummEdits: Measuring LLM Ability at Factual Reasoning Through the Lens of Summarization.* arXiv:2305.14540 (EMNLP 2023). https://ar5iv.labs.arxiv.org/html/2305.14540
- Sclar et al. *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design.* arXiv:2310.11324 (ICLR 2024). https://arxiv.org/abs/2310.11324
- Chen, Zaharia, Zou. *How is ChatGPT's Behavior Changing over Time?* arXiv:2307.09009 (NeurIPS 2023). https://arxiv.org/abs/2307.09009
- Kapoor & Narayanan. *Pre-registration for Predictive Modeling.* arXiv:2311.18807. https://arxiv.org/html/2311.18807v1
- Gema et al. *Are We Done with MMLU? (MMLU-Redux).* arXiv:2406.04127 (EMNLP 2024). https://arxiv.org/abs/2406.04127
- Terwee et al. *Quality criteria were proposed for measurement properties of health status questionnaires.* J Clin Epidemiol 2007. https://pubmed.ncbi.nlm.nih.gov/17161752/
- Oppenheimer, Meyvis, Davidenko. *Instructional manipulation checks: Detecting satisficing to increase statistical power.* J Exp Soc Psychol 2009. https://www.academia.edu/6461937/Instructional_manipulation_checks_Detecting_satisficing_to_increase_statistical_power
- Thomas & Clifford. *It's a Trap! Instructional Manipulation Checks Prompt Systematic Thinking on Tricky Tasks.* SAGE Open 2015. https://journals.sagepub.com/doi/10.1177/2158244015584617
- Howcroft et al. *Twenty Years of Confusion in Human Evaluation: NLG Needs Evaluation Sheets, Standardised Metrics and their Optimisation.* INLG 2020. https://aclanthology.org/2020.inlg-1.23/
- Vincze et al. *The BioScope corpus.* (2008). https://rgai.inf.u-szeged.hu/node/105 ; Morante & Daelemans, *Learning the Scope of Hedge Cues in Biomedical Texts* (BioNLP 2009). https://aclanthology.org/W09-1304.pdf
- Reiter. *Don't ignore omissions!* (2026-02-11). https://ehudreiter.com/2026/02/11/dont-ignore-omissions/
- Tensorlake. *TOON vs JSON: A Token-Optimized Data Format for Reducing LLM Costs* (2025). https://tensorlake.ai/blog/toon-vs-json

*End of verification report.*

---

# PART 3 — WORKER B (HARNESS BATCH): DECISION BRIEF — worker-B-decisions-v2.md

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

---

# PART 4 — WORKER B (SEARCH BATCH): DECISION BRIEF — worker-B-decisions.md

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

---

# PART 5 — WORKER C (HARNESS BATCH): EXTERNAL-READINESS REVIEW — worker-C-readiness-v2.md

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

---

# PART 6 — WORKER C (SEARCH BATCH): EXTERNAL-READINESS REVIEW — worker-C-readiness.md

# External-Readiness Review: `hermes-replicable-pattern.md` (Stanford knowledge-lab share)

**Prepared by:** independent reviewer (Worker C)
**Date:** 2026-08-19
**Scope:** external-readiness assessment of the pattern document (`hermes-replicable-pattern.md`, "the pattern"), read together with the wave-6 grading finding and the six-pager summary ("the docs"). Assessment is anchored in independent research on (a) 2024–2026 evaluation-reporting standards, (b) the published prompt-compression literature, (c) research-community methodology artifacts. Not a summary of the three documents.

---

## 1. Credibility verdict

**Verdict: SHARE WITH CONDITIONS — not as-is.**

The pattern is internally disciplined, unusually honest about its own failures, and better aligned with 2025–2026 methodological currents than most artifacts at this maturity level. It is also, in its current form, an unverifiable private-filesystem record: every claim cites a hash or a local path (`wave5-PICKUP-ENVELOPE.md`, `~/stanford-knowledge/MANIFEST`), nothing is publicly reachable, no grader model is pinned, and no empirical claim is positioned against the existing compression or LLM-as-judge literature. A Stanford research lab will read the doc as a methods note, not as evidence, until the artifacts behind it are accessible.

**Conditions for sharing (see §7 for the full checklist):**

1. Package a public artifact set (code, frozen prereg + amendments, manifests, seed packs, rubric, raw grades) under a license, with the doctrine-source licensing question resolved (the corpus is derived from Amazon Leadership Principles text — see §2, licensing).
2. Pin and disclose the grader configuration (model identities and versions, decoding parameters, temperature) — currently only "cloud-backed graders" is stated.
3. Add a short related-work / positioning section against the prompt-compression and LLM-as-judge literature, and state plainly which claims are method contributions vs. empirical findings.
4. Add a judge meta-evaluation note: what has been done (internal controls) and what has not (external ground truth, perturbation stress tests), with a plan.
5. Soften the cross-wave inference language ("consistent with wave-5") given that amendment-001/002 changed the grading predicate between waves, and clarify the W1 control line (see §6).
6. Add cost/compute context (the 52.9% savings claim has no latency, price, or compute disclosure behind it).

---

## 2. Gaps against 2026 evaluation-reporting standards

The reference norms that now govern externally shared ML methodology writing: the NeurIPS paper checklist (16 mandatory questions; checklist included in the NeurIPS 2026 style file, desk-reject if missing), ICML author instructions (code availability "taken into account in the decision-making process"), ACM Artifact Review and Badging (Artifacts Evaluated — Functional/Reusable, Artifacts Available, Results Validated), and the Turing Way's reproducibility definition ("data and code available to fully rerun the analysis"). Mapping the docs against the NeurIPS checklist items that are directly applicable:

| Reporting standard (2026 norm) | What the docs have | Gap |
|---|---|---|
| Claims match scope (§1 of checklist) | Pattern correctly disclaims: "What it is not. A claim that the compression experiment succeeded." Six-pager's "lossy/semantic compaction is falsified" is broader than what was tested (see §3, §6). | Wording-level rescoping needed in the six-pager; the pattern is fine. |
| Limitations section (§2) | Strong. B4 deletion-control blindness, anchor drift, small n, no permanence/adoption/generalizability claims. | None of substance. This is the doc's best feature. |
| Experimental reproducibility (§4) | Sealed manifests, SHA-256 round-trips, pinned tokenizer (tiktoken cl100k_base v0.14.0), lottery seeds, byte-level audits. | Seals are verifiable only by someone holding the artifacts; no public artifact, no repo, no DOI, no environment/container pin beyond the tokenizer. Grader model identity and version unspecified ("cloud-backed graders"). |
| Open access to data and code (§5) | None. All paths are local; the shareable doc ships no data, code, or instructions to rerun. | Complete gap. A reviewer cannot exercise anything. |
| Experimental setting / hyperparameters (§6) | Lottery seeds, shuffle seeds, rubric thresholds, tokenizer pinned. | Decoding parameters of graders (temperature, top-p), grader model versions, rubric-builder identity not stated. The 2026 preregistration literature (Vaccaro, arXiv:2606.11217) lists model selection, prompt wording, decoding settings, retry policies, and parsing as the choice surface that must be pinned in agent experiments; the docs pin about half of it. |
| Statistical significance / error bars (§7) | Inter-rater counts, per-cell tables, honest flagging of deviations. | No variance across grader models, no repeated runs, no confidence intervals. W6's "no effect" across 20→30→40% rests on 17 real cells; with 0 failures in 17, the rule-of-three upper bound on the failure rate is ~18% — consistent with a real effect being missed. The docs say "small n" but never quantify the uncertainty. |
| Compute disclosure (§8) | Operational notes (524 timeouts, serial dispatch pacing). | No compute type, memory, runtime, or total-cost figures; no statement of what was tried and dropped. |
| LLM-usage declaration (§16, new for NeurIPS 2026) | The pattern is LLM-native; it says so. | No formal declaration of which LLMs are the measurement instrument (graders), which models were tried and replaced, and how that interacts with validity. |
| Licenses / assets (§12–13) | Nothing. | The graded corpus derives from Amazon Leadership Principles text (proprietary, trademarked source material); the pattern itself has no license. Both need resolution before public release. HELM-style raw-data release would include licenses and terms of use. |
| Conflict-of-interest / authorship transparency (ICML 2026 author instructions) | Owner of record named; no COI or authorship-model statement. | The share will be received as agent-orchestrated research; an explicit statement of human vs. agent authorship roles is expected practice for lab shares. |

**Bottom line:** against 2026 norms the pattern is a strong *protocol description* and a weak *evidence package*. The discipline described is ahead of typical practice; the evidence behind it is not independently reachable, and the statistical and configuration disclosures fall short of what the NeurIPS/ICML checklists now treat as table stakes.

---

## 3. The compression verdict vs. the published literature

**The field does not support a blanket "lossy compression harms fidelity" rule, and the docs do not claim one — but the six-pager's "falsified" framing overreaches, and an expert would see the direction of the finding as expected, not surprising.**

What the prompt-compression literature actually shows (hard-prompt family — token/unit deletion — is the relevant comparison; soft-prompt and paraphrase methods are a different family):

- **Effects are task- and content-dependent.** LLMLingua (EMNLP 2023) reports up to 20x compression "with minimal performance loss" on its evaluated tasks; LongLLMLingua (ACL 2024) reports up to 17.1% *improvement* at ~4x reduction on long-context QA, because aggressive compression removes noise and mitigates lost-in-the-middle effects. LLMLingua-2 (Findings of ACL 2024) reports, with Mistral-7B as target, in-domain MeetingBank QA of 81.75 on compressed vs. 71.27 on original prompts — compression *improved* the score on verbose transcripts — while out-of-domain LongBench drops from 42.5 (original) to 38.1 at 5x, and NaturalQuestions (20 documents) drops from 75.7 to 48.6 at 3.9x. The survey literature (Li et al., arXiv:2410.12388) lists performance degradation as a known open challenge of compression methods.
- **The docs' treatment is a narrow slice of "semantic compression."** The lossy arm was mechanical deletion of qualifier/hedge/conditional spans drawn by lottery — targeted deletion, not entropy-based pruning (LLMLingua), not learned extractive compression (LLMLingua-2), not paraphrase (Nano-Capsulator, CompAct, FAVICOMP). The pattern correctly states "never LLM paraphrase"; the six-pager's headline "lossy/semantic compaction is falsified" does not carry that precision.
- **The direction of the verdict is consistent with the field's dense-content results.** Amazon Leadership Principles doctrine with exemplars is low-redundancy, load-bearing text; deleting hedges and qualifiers from such text degrading rubric-scored fidelity is what the dense-content results in the LLMLingua family would predict. An expert in the field would find the verdict plausible and unsurprising, and would locate the novelty in the *measurement apparatus* (walled blind grading, failing controls), not in the direction of the effect. The claim that the damage was "invisible without blind grading" is the strongest and most defensible part.
- **The lossless 52.9% claim is plausible but at the high end of published ranges, and it is transform-unspecified.** Published format-level savings: ~13–24% input-token reduction from removing code formatting elements (arXiv:2508.13666, with a documented model-dependent exception — Gemini-1.5 degraded); ~47% for markdown-table → minified-JSON in RAG content; 65–90% for HTML → markdown. So 52.9% for markup-heavy prose is credible, but the doc never says what the "format-level compaction" transform was, which makes the headline number unauditable and the "full fidelity 12/12" claim model-dependent (the formatting literature shows fidelity after format stripping varies by model).
- **The grader-reliability literature lands *with* the docs' design — and against it in one place.** The 2026 judge-reliability literature (RAND Judge Reliability Harness, arXiv:2603.05399, ICLR 2026 workshop: "no judge that we evaluated is uniformly reliable"; consistency breaks under simple formatting changes, paraphrasing, verbosity changes) supports the docs' core insight that naive grading misses damage — the B4 case (an amputated cell graded 15/15 "fullest version") is exactly the documented failure mode. The same literature says internal agreement is not validity: the LLM-as-judge survey (arXiv:2411.15594) and the IJCNLP 2025 position-bias study document judge×task-dependent bias and temporal drift. The docs' own W6 provides a live example: both the pack grader and the independent ref-anchor grader agreed with each other (6/6) while both drifted from the frozen B4 datum — agreement was high and correctness drifted in the same direction. The pattern does not include a judge stress-test leg (perturbation suite, ground-truth spot checks), which is the standard the 2026 literature now recommends.
- **Hedge/qualifier load-bearing claim:** consistent with a small but real strand treating hedges as trust-calibration content (e.g., ACM 2025 "Linguistic Uncertainty Markers for Trust Calibration"; the n=900 prompt-imperativeness study showing hedging reduction creates calibration problems). This is human-perception evidence, not LLM-fidelity evidence; it makes the B2 finding plausible, not established.

**Expert reading, stated plainly:** the experiment's verdict is a well-measured instance of a known phenomenon, scoped to one dense corpus, one grader family, one rubric, and one deletion-transform family. The transferable output is the measurement discipline — that is exactly what the pattern claims as its deliverable, and that framing is correct. The six-pager's "falsified" language would not survive contact with a reviewer who knows the LLMLingua-family results showing compression can preserve or improve performance on redundant or noisy context.

---

## 4. Knowledge-lab sharing norms and exemplars

What makes a methodology artifact credible to an outside lab, per the current norms:

1. **The evidence package is public and raw.** Stanford's own CRFM HELM (arXiv:2211.09110; crfm.stanford.edu/helm) is the local exemplar: it releases all raw prompts and completions publicly, evaluates every model on shared scenarios with shared metrics, and is a living, maintained artifact. A Stanford lab will implicitly compare any evaluation artifact to this bar.
2. **The protocol is reviewable independent of its authors.** The Turing Way (book.the-turing-way.org) frames reproducibility as "data and code available to fully rerun the analysis," with compendia and version-pinned environments as the mechanism. NeurIPS's checklist (neurips.cc/public/guides/PaperChecklist) and ACM's badging policy (acm.org/publications/policies/artifact-review-badging — "Artifacts Evaluated — Functional" requires artifacts to be documented, consistent, complete, exercisable) encode the same requirement: the artifact must be runnable by a stranger.
3. **The method is pre-committed and the commitments are dated.** The 2026 preregistration literature for AI-agent experiments (Vaccaro, arXiv:2606.11217) argues preregistration should become standard for exactly this paradigm and catalogs the researcher degrees of freedom that must be pinned (model selection, prompt wording, settings, outcome-contingent redesign), demonstrating with a 2,430-configuration specification curve that conclusions can flip on configuration choices. The pattern's frozen contract + amendment mechanics are the most faithful existing implementation of this recommendation I found in the field — the docs should say this explicitly, because it is their strongest credential.
4. **Licensing and provenance are stated.** Turing Way, NeurIPS checklist item 12, and ACM badging all treat license/terms-of-use documentation as non-negotiable for released artifacts. The docs are silent; the Amazon-doctrine-derived corpus makes this a real issue, not a formality.

---

## 5. The outsider's first three questions

**Q1. "Where is the data and code — can I audit or reproduce any of this?"**

- *Docs say:* every number cites an on-disk artifact and a SHA-256 seal; the stated bar is "a fresh reader could verify from disk." Seals round-trip; audits are byte-level.
- *Field says:* NeurIPS checklist items 4–5 require a reasonable avenue for reproducibility (code/data release or detailed instructions); HELM's norm is full raw-data release; Turing Way requires data+code to rerun; ACM badges require the artifact to be exercisable by a stranger.
- *Honest gap:* total. Verification from a private filesystem is not verification to a third party. A reviewer cannot reconstruct the pipeline, cannot check the seals, and cannot tell which grader models produced the grades. The pattern describes a discipline; it does not deliver the evidence package the discipline was built to protect. This is the single largest credibility deficit.

**Q2. "How do you know the LLM graders measure what you claim — and is n sufficient for a 'no effect' conclusion?"**

- *Docs say:* confab controls bit 4/4 (W6) and 7/7 across the last two waves; deletion controls bit 3/4 with the B4 blind spot reported loudly; inter-rater 6/6 = HIGH; B4 anchor drift caught by a dedicated leg and not patched. Small n and near-ceiling are acknowledged as limitations.
- *Field says:* internal controls of this kind are rare and good, but the 2026 judge-reliability literature (RAND harness; LLM-as-judge survey) is explicit that LLM–LLM agreement is not validity, that judge reliability is domain-specific and must be stress-tested (formatting/paraphrase/verbosity perturbations), and that judges drift over time. With 17 real cells and zero failures, the rule-of-three upper bound on failure rate is ~18%; "essentially no effect" between 20% and 40% is a null result with wide bounds, not a demonstration of equivalence.
- *Honest gap:* partial. The docs have more control discipline than typical LLM-as-judge work — but there is no external ground truth (human-graded anchor set, or a validated rubric against known-good/known-bad responses), no perturbation stress test of the graders, and no quantification of the null. The pattern's §5 "Evidence the instrument works" reads stronger than the limitations in §6 of the wave-6 finding allow.

**Q3. "What does this add over the published compression and evaluation literature — and why is the verdict not already known?"**

- *Docs say:* the mechanism is a reusable pattern for any local-LM orchestration decision; "lossy/semantic compaction is falsified for this doctrine and stack"; lossless compaction saves 52.9% at full fidelity. No related work, no baselines, no cost figures appear in the shareable artifact.
- *Field says:* the direction of the verdict is predicted by the dense-content results in the LLMLingua family; the field also documents cases where lossy compression preserves or improves performance (verbose/noisy contexts), so "keep full prose" as a standing rule would not be accepted as a general conclusion. The genuinely additive contributions — walled-blind grading with failing negative controls, pre-committed decision rules with amendment mechanics, byte-level audits, and the 2026-aligned agent-experiment preregistration — are exactly the parts the docs under-position.
- *Honest gap:* significant. Without a single citation or baseline comparison, the empirical claims float free of the field they sit inside, and the reader cannot tell what the authors believe is novel. The "falsified" framing also invites a comparison to published compressors (LLMLingua-2 etc.) that the design did not run.

---

## 6. Over- and under-statement findings

**Overstatements:**

1. **"Lossy/semantic compaction is falsified for this doctrine and stack"** (six-pager). What was tested: mechanical deletion of specific qualifier/hedge/conditional classes at 20–60% reduction on one doctrine corpus, graded by one LLM-grader family under one rubric. That falsifies the deletion-transform family for that corpus under that instrument; it does not falsify semantic compression as the field defines it (learned extractive, entropy-based, or paraphrase compression). The word "falsified" should be replaced with a scoped statement.
2. **"Consistent with wave-5"** (wave-6 finding). Amendment-001/002 changed the grading predicate (Part-2 anchors moved to relative-to-ref; deletion-dock decision table added) between W5 and W6, yet W6 asserts no PASS↔FAIL movement "consistent with wave-5" while W5's record includes a 30-reserved HURT that W6's 30-reserved cells pass. Cross-wave comparability under a changed instrument is asserted, not demonstrated. The B4 anchor drift is exactly the kind of instrument drift that makes this inference unsafe, and it was reported rather than resolved — which is the honest behavior, but it means the consistency claim needs a caveat.
3. **"Control caught 0/12 (teeth)"** (W1, repeated in pattern §5). As written this is ambiguous: under the pattern's own P5 definition (a docked control = TEETH), a control that catches 0/12 is a non-biting control. If the W1 control was a specificity check on clean lossless cells (correct rejection of 12 clean cells), it should be labeled as such; as printed, a careful reader cannot tell whether the instrument demonstrated sensitivity or failed to fire.
4. **Near-ceiling 17/17 as "instrument-validity" evidence.** Zero failures in 17 cells is weak evidence of equivalence (upper bound ~18% failure rate); the docs hedge this in limitations but the executive summary of the wave-6 finding leads with the 17/17.

**Understatements:**

1. The pattern's genuine novelty is under-claimed: it is, to my knowledge from this review, the most complete working implementation of what the 2026 AI-agent preregistration literature is asking the community to build (frozen contract, amendment mechanics, specification pinning, failing controls). The docs present this as internal discipline; it is a research contribution in its own right and should be positioned as one, with the 2026 preregistration and judge-reliability work cited.
2. The W6 deletion-control result (3/4 bit, with the blind B4 reported loudly rather than re-run) is a better judge-reliability story than the docs tell: the field's 2026 finding is that judges are not uniformly reliable and that reliability must be demonstrated; the docs demonstrate a working negative-control design on the first wave it ran. This is the strongest single piece of evidence that the pattern works, and it is buried in a results table.
3. The 52.9% lossless claim has no cost context. Published format-level savings (13–24% for code formatting; up to ~47% for minified markup) suggest 52.9% is a strong but plausible result; without the transform spec, latency/price numbers, or a comparison to the source format's markup density, the number cannot be evaluated — a missed opportunity, since this is the one immediately actionable finding.

---

## 7. The single strongest claim the combined evidence supports

Stated at exact scope:

> For dense, low-redundancy doctrine prose carried in agent sub-delegation envelopes, mechanically deleting hedge/qualifier/conditional spans at 20–40% token reduction degraded rubric-scored doctrine fidelity under walled-blind LLM grading (earlier waves: HURT at ≤60%, cliff at 40%; fine gradient locating the cliff between 20% and 30%), while a format-level compaction achieved 52.9% token savings at unchanged fidelity — both on one doctrine corpus, one rubric, one LLM-grader family, small n, and both results being findings about that corpus and instrument, not general laws; the transferable output is the pre-registered, walled, negative-controlled evaluation procedure, not the compression verdict.

Every element of that sentence is supported by the docs, and the scoping matches what the field would accept: the direction of the lossy result is consistent with dense-content results in the published compression literature, the lossless magnitude is plausible against published format-level savings, and the claim "the method is the contribution" matches what the 2026 preregistration and judge-reliability literature identifies as the missing norm.

---

## 8. Conditions checklist before sharing

1. Public artifact package: frozen prereg + amendments, lottery seeds, rubric, packs, manifests, raw grades, and the pipeline code, with a license; DOI or repo URL.
2. Resolve licensing/provenance of the Amazon Leadership Principles-derived corpus and state it.
3. Pin grader configuration: model identities + versions, decoding parameters, and the rubric-builder identity; state what was tried and replaced.
4. Add a 5–10 line related-work/positioning note (LLMLingua family, LLM-as-judge reliability, 2026 agent preregistration) and restate claims as method contributions vs. empirical findings.
5. Replace "falsified" with a scoped claim; add a cross-wave comparability caveat given amendment-001/002; clarify the W1 control line.
6. Add a judge meta-evaluation section: what is done (internal controls), what is not (external ground truth, perturbation stress tests à la the RAND harness), and the plan (e.g., wave-7 items).
7. Quantify uncertainty for the near-ceiling null (n, bounds) and add cost/compute context for the 52.9% claim.

---

## Sources consulted (independent research)

- NeurIPS Paper Checklist Guidelines (incl. NeurIPS 2026 style file and LLM-usage declaration): https://neurips.cc/public/guides/PaperChecklist
- NeurIPS 2025 Call for Papers / FAQ: https://neurips.cc/Conferences/2025/CallForPapers
- ICML 2026 Author Instructions: https://icml.cc/Conferences/2026/AuthorInstructions
- ACM Artifact Review and Badging: https://www.acm.org/publications/policies/artifact-review-badging
- The Turing Way, Guide for Reproducible Research: https://book.the-turing-way.org/reproducible-research/reproducible-research/
- Stanford CRFM HELM: https://crfm.stanford.edu/helm/ ; https://arxiv.org/abs/2211.09110
- Li et al., "Prompt Compression for Large Language Models: A Survey," arXiv:2410.12388
- Jiang et al., "LLMLingua," EMNLP 2023 (10.18653/v1/2023.emnlp-main.825); LongLLMLingua, ACL 2024 (2024.acl-long.91)
- Pan et al., "LLMLingua-2," Findings of ACL 2024; arXiv:2403.12968
- Dev et al., "Judge Reliability Harness: Stress Testing the Reliability of LLM Judges," arXiv:2603.05399 (ICLR 2026 workshop)
- "A Survey on LLM-as-a-Judge," arXiv:2411.15594; "A Systematic Study of Position Bias in LLM-as-a-Judge," IJCNLP 2025 (2025.ijcnlp-long.18)
- Vaccaro, "Preregistration for Experiments with AI Agents," arXiv:2606.11217
- "How Code Formatting Silently Consumes Your LLM Budget," arXiv:2508.13666
- "Linguistic Uncertainty Markers for Trust Calibration in AI-Assisted Decision-Making," ACM 2025 (10.1145/3816046.3816231); LessWrong, "Prompt Imperativeness Drastically Reduces Hedging in LLMs" (n=900)

---

# PART 7 — WORKER C ITERATION 2: EXECUTABLE PRE-SHARE PACKAGE — worker-C-iteration2.md

# Worker C — Iteration 2: Executable Pre-Share Package (Nine Condition Specs)

**Author:** Worker C (independent research pass)
**Date:** 2026-08-19
**Iteration-1 verdict:** SHARE WITH CONDITIONS (8 conditions, `worker-C-readiness-v2.md`) + condition 9 (corpus licensing) added in a later review pass.
**Purpose of this document:** turn each condition into a concrete, executable spec an owner can act on without further research. Every condition ends with a checklist of the form: action → artifact → done-when.
**Method:** all four source documents read in full (`loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md`, `wave6-grading-finding.md`, `worker-C-readiness-v2.md`); external pages read via the browser-harness method (`BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use < script.py`, `goto_url` + `wait_for_load` + targeted `js()` extraction, retry-once-then-fallback) and direct extraction; statistics computed from the rubric definitions in the source docs (exact binomial calculations, closed-form intervals — no package dependencies). No CAPTCHA/login was encountered; no page was bypassed.

**Grounding legend (used throughout):**
- **DOC-GROUNDED** — claim rests on the three pattern documents (file + section cited).
- **ONLINE-GROUNDED** — claim rests on an external source read during this pass; URL cited.
- **UNVERIFIABLE** — the source documents do not record this; the spec tells the owner how to produce or estimate it.

---

## C1 — Replication kit

### 1.1 What the condition requires

Iteration 1: "a fresh reader could verify from disk" is unfulfillable because every artifact the pattern cites lives on a private machine (DOC-GROUNDED: pattern §P10, six-pager §1 "verify from disk"). The kit must make the three headline claims independently checkable: (a) 52.9% lossless savings at 12/12 (W1), (b) lossy HURT ≤60% with a 40% cliff (W3–W6), (c) instrument controls (confab 4/4, deletion 3/4, inter-rater 6/6) and seal round-trips.

### 1.2 Exemplars the kit is measured against

- **ACM artifact review badging (v1.1, current):** "Artifacts Evaluated – Functional" = documented, consistent, complete, exercisable, with evidence of verification and validation; "Artifacts Evaluated – Reusable" = same plus careful documentation and structure for reuse; "Artifacts Available" = placed on a public archival repository with a DOI or link plus a unique identifier (ONLINE-GROUNDED: https://www.acm.org/publications/policies/artifact-review-and-badging-current). The kit is designed to earn "Artifacts Available" and "Artifacts Evaluated – Functional" as soon as it exists on a public archive; "Reusable" requires the README and structure below.
- **HELM (Stanford CRFM):** the credibility mechanism is that every leaderboard number traces to a public run spec; the framework ships under Apache-2.0 and documents reproduction of published leaderboards (ONLINE-GROUNDED: https://crfm.stanford.edu/helm/, https://github.com/stanford-crfm/helm, https://crfm-helm.readthedocs.io/en/latest/reproducing_leaderboards/). The pattern kit's equivalent: a claim-to-file mapping table in the README.
- **The Turing Way licensing convention:** content under CC-BY-4.0, code under MIT, license declared in `LICENSE.md` and referenced in the README (ONLINE-GROUNDED: https://book.the-turing-way.org/reproducible-research/licensing/licensing-checklist, https://book.the-turing-way.org/reproducible-research/licensing/). The kit follows this split (see C9 for the third-party text).

### 1.3 Exact file list (v1.0)

| # | File | Content | Source |
|---|------|---------|--------|
| 1 | `doctrine/amazon-doctrine-local-lm.md` | The doctrine text as used, byte-identical to the graded version | On-disk file; DOC-GROUNDED name (wave6 finding §2, §5.1); see C9 for licensing handling |
| 2 | `prereg/wave5-preregistration.md` | Frozen contract (grid, transforms, decision rules, wall, teeth gate, amendment mechanics) | On-disk; DOC-GROUNDED (pattern P1, §7) |
| 3 | `prereg/amendment-001-instrument-validity-controls.md` | Amendment 001, seal `674ca2bf…` | DOC-GROUNDED (pattern §6, six-pager §2) |
| 4 | `prereg/amendment-002-deletion-dock-decision-table.md` | Amendment 002, seal `55d9a858…` | DOC-GROUNDED (pattern §5b, §6; wave6 finding §2 cl.3) |
| 5 | `rubric/rubric-verbatim.md` | The 5-part × 0–3 rubric, verbatim, with per-behavior anchors (B1/B2/B6 all parts 3; B4 Part-2 datum 13/15, P2=1) and PASS gate text (base ≥9, no part 0, Parts 3 & 5 ≠ 0 for hedge-required) | DOC-GROUNDED (pattern P7; wave6 finding §3) |
| 6 | `transforms/lossy-family.md` + `transforms/lossless-family.md` | T1–T7 deletion specs (drop-hedge, drop-conditional-clause, drop-reversibility-qualifier, load-bearing qualifier, merge-two-principles, drop-hedge-category-wholesale, shorten-load-bearing-example), each with the exact span rule and FLAG rule; plus the format-level (lossless) family that produced the 52.9% figure — what was stripped, token deltas per transform, examples | Lossy family DOC-GROUNDED (pattern P2); **lossless family contents UNVERIFIABLE** — the shared docs name "format-level compaction" but list no transform (six-pager §3; readiness review §6 Q1); owner must write it from the on-disk W1 artifacts before shipping |
| 7 | `cells/wave6/` (25 cell files) + `cells/wave6/b1-30-reserved.cell.md` + `b1-30-reserved.log.md` as the designated representative pair | All W6 cells prose-only, plus the representative cell and its deletion log (ref line, transform, byte span, token count, reservation check) | On-disk; log format DOC-GROUNDED (pattern P3); representative pair per iteration-1 condition 1 |
| 8 | `code/apply_rulebook.py` (+ `code/audit_cellcheck.py`, `code/verify_seals.py`, `code/fetch_doctrine.py`) | The deterministic rulebook application, the byte audit, seal recomputation, and (C9) doctrine fetch-and-verify | `apply_rulebook.py` and `audit_cellcheck.py` DOC-GROUNDED (wave6 finding §1, §2); verify/fetch scripts are new |
| 9 | `manifest/MANIFEST.md` + `manifest/seals.json` | The ledger with seal lines, and a machine-readable per-file SHA-256 map including the sealed manifest values (`6461c201…`, `55d9a858…`, `674ca2bf…`) | DOC-GROUNDED (pattern P10, §5; wave6 finding §2 cl.4) |
| 10 | `README.md`, `LICENSE.md`, `NOTICE-THIRD-PARTY.md`, `CITATION.cff` | Entry point, license, third-party attribution (C9), citation metadata | New |

### 1.4 Directory layout

```
walled-blind-pattern-v1.0/
├── README.md
├── LICENSE.md
├── NOTICE-THIRD-PARTY.md
├── CITATION.cff
├── SHA256SUMS                     # per-file hashes of the archive contents
├── doctrine/
│   └── amazon-doctrine-local-lm.md
├── prereg/
│   ├── wave5-preregistration.md
│   ├── amendment-001-…md
│   └── amendment-002-…md
├── rubric/
│   └── rubric-verbatim.md
├── transforms/
│   ├── lossy-family.md
│   └── lossless-family.md
├── cells/
│   └── wave6/
│       ├── b1-20-reserved.cell.md … (25 cells)
│       └── representative/
│           ├── b1-30-reserved.cell.md
│           └── b1-30-reserved.log.md
├── code/
│   ├── apply_rulebook.py
│   ├── audit_cellcheck.py
│   ├── verify_seals.py
│   └── fetch_doctrine.py
├── manifest/
│   ├── MANIFEST.md
│   └── seals.json
└── docs/
    ├── claim-to-file-map.md       # each headline number → command → file
    └── human-anchor-validation.md # C3 output (placeholder until run)
```

### 1.5 Hashing, sealing, archive format

- **Hashing:** SHA-256 per file (already the pattern's convention, pattern P10 and wave6 §2 cl.4). Seal convention pinned in writing: hash over content minus the "Seal section (header + seal line + one surrounding blank)", with the boundary recorded in the manifest (DOC-GROUNDED: pattern §6 item 4, amendment cl.4). `verify_seals.py` recomputes every seal and fails loud on mismatch — same loud-fail philosophy as the tokenizer pin (DOC-GROUNDED: pattern §6 item 5).
- **Archive:** one `walled-blind-pattern-v1.0.zip` (Zenodo's accepted format, see C6) plus a `SHA256SUMS` sidecar. Build deterministically from the live tree with `build_release.sh` so the archive can be re-derived; the release tag in git (or the archive itself) is the frozen object.
- **License:** `LICENSE.md` = CC-BY-4.0 for all original text and methodology; MIT for `code/`; `NOTICE-THIRD-PARTY.md` covers the Amazon LP text and derived cell prose (see C9). This mirrors The Turing Way's content/code split (ONLINE-GROUNDED: https://book.the-turing-way.org/reproducible-research/licensing/licensing-checklist).

### 1.6 README outline (exact sections)

1. What this is / what it is not (copy the pattern doc's own opening framing; one application, no permanence claim)
2. Quick start: 5 commands (verify SHA256SUMS; `pip install -r requirements.txt` with `tiktoken==0.14.0`; run `audit_cellcheck.py`; run `apply_rulebook.py`; run `verify_seals.py`)
3. Claim-to-file map: "52.9% at 12/12" → `cells/wave1/*` + `transforms/lossless-family.md` + command; "HURT ≤60%, cliff 40%" → `cells/wave3-6/*` + rulebook; "controls 4/4, 3/4, 6/6" → `wave6-grading-finding.md` mirror + cell files; "seals round-trip" → `verify_seals.py`
4. Environment: Python version used, tiktoken pin, no network required except optional doctrine fetch (C9)
5. Wall and grading-pack rebuild instructions (who sees what; P4 verbatim)
6. Limitations (B4 deletion control INCONCLUSIVE, B4 anchor drift, §7.4 no-op, small n) — kept verbatim from wave6 §6
7. Licensing and attribution (C9 text)
8. Pre-registration archive links (C6)
9. Citation (`CITATION.cff`)

### C1 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Collect the 10 file items from the live tree and diff each against its cited identity (byte-compare doctrine, rubric, prereg, amendments) | `staging/` tree with verified byte identity | Every file present and byte-identical to what the seals reference |
| Write `transforms/lossless-family.md` from the W1 on-disk artifacts (transform-by-transform token deltas summing to the 52.9% figure) | `transforms/lossless-family.md` | A reader can sum the deltas and reproduce 52.9% on the W1 cells |
| Write `code/verify_seals.py` and `code/fetch_doctrine.py` | Two scripts | `verify_seals.py` recomputes `6461c201…`, `55d9a858…`, `674ca2bf…`; `fetch_doctrine.py` pins the doctrine SHA-256 (C9) |
| Write README per §1.6 outline, incl. claim-to-file map | `README.md` | Each headline number in the six-pager resolves to a file + command |
| Write LICENSE/NOTICE per C9 | `LICENSE.md`, `NOTICE-THIRD-PARTY.md` | Attribution and license scope stated; Amazon text marked third-party |
| Build the release zip + SHA256SUMS from `build_release.sh` | `walled-blind-pattern-v1.0.zip`, `SHA256SUMS` | Archive builds deterministically; hashes stable across two builds |
| Dry-run the README commands on a clean machine (or fresh venv) | Command log | Audit, rulebook, and seal verification all exit 0 from the archive alone |
| Upload to the C6 archive and record the DOI in the README | Archived DOI | DOI resolves to the exact zip |

---

## C2 — Grader pin (fill-in template)

### 2.1 What the 2026 standard requires

The pre-registration template for experiments with AI agents (arXiv:2606.11217, ICML 2026 Spotlight) requires, before data collection: exact model identifiers and version checkpoints (e.g. `gpt-4-0125-preview`, not "GPT-4"); generation parameters (temperature, top-p, top-k, random seeds); inference-budget constraints (max tokens, timeout thresholds, retry limits); API version and access date (because providers change behavior over time); checkpoint hash and quantization scheme for open-weight models; verbatim prompt text (system, user, few-shot); retrieval mechanism if RAG; pre-specified outcome variables, statistical tests, and decision rules; evaluator model version and evaluation prompt plus disagreement/refusal handling; exclusion criteria for malformed/refused responses; pilot-testing history (how many prompt iterations, which models tested, whether preliminary results informed the hypotheses); and confirmatory/exploratory demarcation (ONLINE-GROUNDED: https://arxiv.org/html/2606.11217v1 §4.1–4.4).

### 2.2 What the docs already pin (DOC-GROUNDED)

| Item | Value | Source |
|---|---|---|
| Tokenizer | tiktoken `cl100k_base` v0.14.0, loud-fail | pattern §6 item 5; wave6 §2 cl.5 |
| Lottery seed | `20260818`, never re-drawn | six-pager §2; pattern P2 |
| Order-shuffle seeds | 101/107/113/127/131/139, in `wave6-grading/pack-key.md` | wave6 §2 |
| Inter-rater scope | Part 5 only, 6 reserved cells, ≥5-of-6 = HIGH | pattern P8; wave6 §5.2 |
| Dispatch | solo/serial to stay under 120 s proxy read-timeout; a 524 is never a grade; re-dispatch with a fresh cold grader, same sealed pack | wave6 §2; pattern §7 |
| Rubric + anchors | verbatim rubric; B1/B2/B6 all parts 3; B4 P2=1 (frozen datum 13/15) | pattern P7; wave6 §3 |

### 2.3 The doc-internal contradiction the pin must resolve (DOC-GROUNDED)

The wave-6 finding describes grader legs hitting HTTP 524 on a **"local-LM grader backend"** behind a proxy (wave6 §2), while the pattern document says the run used **"cloud-backed graders"** and lists local endpoints (Qwen3-4B @ :8080, Qwen3-8B) as the *replication target* (pattern §7). The two documents disagree about what actually graded W6. The grader pin cannot be "filled in" — it must first resolve this contradiction against the on-disk pack-key, dispatch logs, and endpoint configuration. This is the strongest concrete evidence for why condition 2 exists.

### 2.4 The fill-in template (one file: `prereg/grader-pin.md`, frozen as amendment-003)

```
GRADER PIN — wave 6 (and, by reference, waves 1–5 where recoverable)
1. RESOLUTION OF LOCAL-vs-CLOUD CONTRADICTION (wave6 §2 vs pattern §7):
   [ ] State which backend(s) graded each wave, citing pack-key/dispatch logs
2. GRADER MODEL (per leg; legs: pack-b1, pack-b2, pack-b4, pack-b6, pack-ctrl,
   pack-ir, pack-ref-b4):
   [ ] Provider / local endpoint
   [ ] Exact model ID and checkpoint (e.g. "Qwen3-4B, <checkpoint/commit>")
   [ ] Open weights: weight-file SHA-256 + quantization scheme; else API version
       + access date (ISO)
3. SAMPLING PARAMETERS (per leg):
   [ ] temperature, top-p, top-k, max_tokens, seed (or "defaults, pinned in
       pack-key.md" with the exact defaults named)
4. INFERENCE BUDGET / RETRIES:
   [ ] max tokens, timeout threshold (120 s proxy), retry limit, re-dispatch
       rule (fresh cold grader, same sealed pack — pattern §7)
5. PROMPT PACK (verbatim, hashed):
   [ ] rubric file hash, doctrine file hash, cell file hash, grader prompt text
       (system + user) archived byte-exact
6. EXCLUSION / REFUSAL RULES:
   [ ] handling for malformed, refused, or FLAG'd grades (pattern P4: stop and
       flag; never improvise)
7. PILOT-TESTING HISTORY (arXiv:2606.11217 §4.2):
   [ ] how many prompt variants were tried pre-freeze, which models, whether
       any preliminary results informed the frozen rubric
8. RAW OUTPUT LOGS:
   [ ] where grade lines and rationales are archived (kit: `cells/wave6/` +
       `docs/grader-logs/`)
```

The template is filed as a forward-only amendment (per P1 mechanics) even though the grades are already recorded; its function is to make the *record* complete, not to change any frozen value. If the W1–W5 backend identity is not recoverable from disk, mark each such field **UNVERIFIABLE** and state it in the README limitations list.

### C2 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Resolve the local-vs-cloud contradiction from disk (pack-key, dispatch logs, endpoint config) | One-line statement per wave in `grader-pin.md` | Each wave has a single named backend with evidence |
| Fill the template fields for every wave; where unrecoverable, mark UNVERIFIABLE | `prereg/grader-pin.md` | No empty fields remain; UNVERIFIABLE entries are explicit |
| Freeze as amendment-003 with a seal, per P1 mechanics | Amendment-003 file + seal in manifest | Seal round-trips via `verify_seals.py` |
| Archive verbatim grader prompts and raw grade lines | `docs/grader-logs/` in the kit | Hash of prompt pack matches the pin |
| Add a one-paragraph "grader identity" note to the pattern doc §7 porting section, quoting the pin | Pattern doc revision | The contradiction is resolved in the shared text, not just the kit |

---

## C3 — Human anchor protocol

### 3.1 Why and what the field bar is

LLM judges are acceptable in published evaluation but must be validated against human judgment; the MT-Bench result is that strong LLM judges reach **over 80% agreement with human preferences — the same level as human–human agreement** (ONLINE-GROUNDED: https://arxiv.org/abs/2306.05685). The pattern has no human anchor; inter-rater 6/6 between two LLM graders on one dimension at the ceiling is not validity evidence (iteration-1 §3, Q2). This spec closes that with a bounded, blinded human-grading study.

### 3.2 Protocol

- **Cells: 15–20 real cells** (within the 10–30 range), stratified across the four behaviors (B1/B2/B4/B6, ~4 each), **plus 3–5 control cells** (the W6 deletion controls DEL-b1/b2/b6 and 1–2 confab controls). Controls are mandatory in the human set: they create score spread, without which agreement statistics are degenerate (see §3.4).
- **Who:** one domain expert (SME) familiar with Amazon Leadership Principles; a second SME if available (two humans give human–human agreement as the reference level, matching the MT-Bench design). Non-author, non-rig personnel.
- **Blinding:** rubric-only, same wall as LLM graders (pattern P4): cell files + rubric + doctrine envelope only; no labels, no lottery, no prior waves, no hypothesis. Human reads cells cold, one pass, scores the same 5-part × 0–3 rubric.
- **Metrics:** per-part raw exact-agreement rate; per-part unweighted Cohen's kappa (4 categories, 0–3); PASS/FAIL agreement; report all three, plus a quadratic-weighted kappa as the ordinal-appropriate complement.
- **Pass bar (pre-committed, in the protocol file):** raw agreement ≥ 80% **and** unweighted kappa ≥ 0.70 (Landis–Koch "substantial"; ONLINE-GROUNDED: https://www.jstor.org/stable/2529310, interpretation table at https://www.ncbi.nlm.nih.gov/books/NBK92287/table/executivesummary.t2/) on the per-part scores, with kappa reported with its approximate 95% CI. At N=20 the CI half-width is roughly ±0.26, at N=30 roughly ±0.21 (computed for κ≈0.65–0.7 — see §3.4), so the bar is interpreted with the interval, not as a point value.
- **Caveats built into the protocol (pre-committed):**
  - On near-ceiling data kappa is **undefined** (observed = chance = 1.0). This is the actual situation for the existing W6 inter-rater data (6/6 on Part 5, all scores 3): κ = 0/0 (DOC-GROUNDED: wave6 §5.2; computed). The anchor study therefore *must* include the control cells so the score distribution has spread; if any part still lacks spread, report raw agreement for that part and mark kappa undefined — never report κ = 1.0.
  - The kappa paradox: with imbalanced PASS/FAIL marginals, high raw agreement can yield near-zero or negative kappa (illustration computed: 20 cells, 85% raw agreement, 19/1 vs 18/2 marginals → κ ≈ −0.07). Hence the bar is set on the per-part ordinal scores, not on the PASS/FAIL binary.
- **How results fold into the pattern without breaking the frozen record:** human grades go to `docs/human-anchor-validation.md` in the kit and a 3–5 line summary in the pattern doc's evidence section ("instrument validity: human-anchor study, κ = …, raw = …, n = …"). **No frozen grade, rubric, or decision value changes** (P1/P10 discipline). If the bar fails, the rubric revision proceeds as a forward-only amendment for future waves; W1–W6 values stand with the limitation recorded.

### 3.3 Where it lives

`docs/human-anchor-protocol.md` (frozen before grading, sealed like a prereg), `docs/human-anchor-validation.md` (results), one paragraph in the pattern doc §5.

### C3 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Write and seal the protocol (cells, raters, blinding, metrics, pass bar, caveats) | `docs/human-anchor-protocol.md` | Sealed before any human grades are read |
| Recruit 1–2 non-author SMEs; brief them rubric-only | Signed-off blinding statement | Raters confirm they saw cells + rubric + doctrine only |
| Build the human pack (15–20 real + 3–5 control cells, no labels) | `docs/human-anchor-pack/` | Pack hashes recorded; labels absent |
| Collect grades; compute raw agreement, unweighted + weighted kappa per part, PASS/FAIL agreement, kappa CIs | `docs/human-anchor-validation.md` | All metrics computed from the raw grade table, script included |
| Adjudicate against the pre-committed bar; write the fold-in paragraph | Pattern doc §5 revision + validation report | Bar met → summary added; bar failed → forward-only amendment filed and limitation recorded |
| Ship both files in the kit (C1) | Kit v1.0 includes anchor files | Present in the release zip |

---

## C4 — Statistical reporting spec

### 4.1 Minimum detectable damage (the honest bound on "no effect")

The instrument's decision surface is per-cell PASS/FAIL under the base-12 gate (PASS = base ≥9, no part 0, Parts 3&5 ≠ 0 for hedge-required behaviors; DOC-GROUNDED: pattern P7). Two sensitivity statements, both computed exactly for this rubric:

**A. Per-cell failure rate the PASS gate can see.** With n independent cells, the probability of observing at least one failing cell under a true per-cell failure rate p is 1−(1−p)ⁿ. Computed values (exact binomial):

| n | 80% power (≥1 failure) | 90% power (≥1 failure) |
|---|---|---|
| 12 (W1) | ≥ 12.6% | ≥ 17.5% |
| 17 (W6 real cells) | ≥ 9.0% | ≥ 12.7% |
| 21 (W5) | ≥ 7.4% | ≥ 10.4% |
| 25 (W6 full pack) | ≥ 6.2% | ≥ 8.8% |

Wording for the pattern doc: "the instrument can detect a per-cell failure rate ≥9% with 80% power at n=17; 'no effect' means no cell failed the pre-committed gate, which bounds damage below this threshold — it does not bound sub-threshold degradation."

**B. Per-part mean shift.** On the 0–3 integer scale, with cell-level SD σ, 80% power at α=0.05 two-sided detects a mean drop of ≈2.80·σ/√n (computed). At n=17: ≈0.34 points for σ=0.5 (a plausible near-ceiling SD given the W6 Part-2 spread of 1–3; DOC-GROUNDED: wave6 §3) and ≈0.20 for σ=0.3. The pattern should state σ assumed and the resulting resolution; per-part means with CIs replace bare integer tables for any future wave.

### 4.2 CI reporting for the headline fidelity claims (computed)

- W1 12/12: Wilson 95% CI **[0.758, 1.000]**; exact Clopper–Pearson **[0.735, 1.000]**; rule-of-three upper bound on failure rate 25%.
- W6 17/17: Wilson 95% CI **[0.816, 1.000]**; Clopper–Pearson **[0.805, 1.000]**; rule-of-three upper bound 17.6%.
- These are one-line additions to the pattern doc §5 evidence table: "12/12 (95% CI 0.76–1.00, Wilson)", "17/17 (95% CI 0.82–1.00, Wilson)". The NeurIPS checklist norm requires error bars or intervals with the method stated and SD vs SEM distinguished (ONLINE-GROUNDED: https://neurips.cc/public/guides/PaperChecklist items 7); Wilson is the stated method, closed form.

### 4.3 Grader-variance estimate

- **What exists:** inter-rater covers Part 5 on 6 reserved cells, all agreements (wave6 §5.2). This yields an observed between-grader difference SD of 0 — a ceiling bound, not evidence of reliability; and kappa is undefined (no spread, §3.4). Report it exactly that way.
- **What to add:** a second full-rubric grader on 6–10 cells across behaviors (can be folded into the C3 anchor study: the LLM second pass is free; the human pass is the anchor). Report per-part exact-agreement rate, mean absolute difference, and SD of per-part differences. Expected magnitude check: the B4 Part-2 anchor drift (wave-6 graders read P2=2–3 vs frozen P2=1; DOC-GROUNDED: wave6 §5.4) is itself a measured between-grader/between-wave difference of ~1.3 points on one part — cite it as the only existing non-zero variance datum.
- **Where:** `docs/grader-variance.md` (kit) + one line in pattern §5.

### 4.4 Clustering caveat

The 17 "real cells" are **not independent observations**: cells are nested within four behaviors, each behavior's cells share reference text (correlated outcomes by construction), and the stable-eye design gives each behavior one grader, confounding grader identity with behavior (DOC-GROUNDED: pattern P4 "stable eye"; wave6 §2 leg table). Consequences, stated in the pattern doc:
- Naive n=17 underestimates uncertainty; the effective sample size lies between 4 (behavior clusters) and 17.
- All pooled statistics must be reported **per behavior** (already the doc's format, wave6 §3) and mechanism claims (e.g., "load-bearing qualifiers die first") must be phrased at the behavior level, n_behaviors=4.
- For paired comparisons across compression levels (the reserved/unreserved and 20/30/40 design), McNemar's test on PASS/FAIL is the correct framework for future waves; in W6 it is inapplicable because every cell passed (no discordant pairs) — state that rather than omit the framework.

### C4 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Add the min-detectable-damage table (§4.1A/B) to the pattern doc limitations section, with the method sentence | Pattern doc §6 revision | Numbers match the exact computations above |
| Add Wilson CIs to the 12/12 and 17/17 claims (method named) | Pattern doc §5 revision | Intervals present and labeled Wilson |
| Produce `docs/grader-variance.md` from the second-grader pass and the B4 drift datum | Kit file | Per-part agreement + difference SD reported; B4 drift cited as variance datum |
| Add the clustering paragraph (effective n, per-behavior reporting, McNemar note) | Pattern doc §6 revision | Text present and consistent with wave6 §3 tables |
| Recompute all values with the archived script (`code/stats.py` in kit) | `code/stats.py` | Numbers reproducible from the script alone |

---

## C5 — Related work (draft paragraphs)

Draft text matching the pattern doc's tone (flat, scoped, no overclaim). Insert as a new "Related work" section after §5; the six-pager gets a two-sentence version. All numbers ONLINE-GROUNDED (abstracts read this pass).

**Paragraph 1 — the lossy-compression landscape.** "Prompt compression methods sit on a task- and regime-dependent spectrum. LLMLingua compresses prompts via entropy-based token pruning and reports up to 20× compression with little performance loss on GSM8K, BBH, ShareGPT, and arXiv tasks (arXiv:2310.05736). LLMLingua-2 reframes compression as token classification, arguing entropy is a suboptimal metric and guaranteeing the compressed prompt is faithful to a subsequence of the original (arXiv:2403.12968). Selective Context reports a 50% context-cost reduction with a 0.038 faithfulness drop on long-context applications (arXiv:2310.06201). A 2025 empirical study of six compression methods across 13 datasets found performance degrades with compression ratio on short contexts, and that all methods increase hallucination, with information loss the primary mechanism (arXiv:2505.00019). A 2026 ECIR study (thousands of runs, 30,000 queries, three GPU classes) found LLMLingua delivers up to 18% end-to-end speed-up with response quality statistically unchanged on summarization, code generation, and QA — when prompt length, ratio, and hardware are well matched; outside that window the compression step dominates (arXiv:2604.02985). None of this literature reports a universal damage cliff at 40%."

**Paragraph 2 — where this experiment sits.** "This experiment occupies a specific corner of that spectrum, by construction. The tested transforms are targeted deletions of the token classes most load-bearing for doctrine fidelity — hedges, conditionals, reversibility qualifiers — applied to short, qualifier-dense prompts, graded with a rubric that penalizes qualifier loss and confabulation. Entropy-based methods preferentially delete different tokens, so the negative result does not generalize to them; it is a negative result for mechanical deletion of qualifier classes on this content. The 40% cliff and the ≤60% HURT verdict are consistent with the short-context degradation regime and the information-loss hallucination mechanism of the 2025 empirical study (arXiv:2505.00019), and the leading damage class (load-bearing qualifiers) is the failure mode the entropy-pruning critique predicts (arXiv:2403.12968)."

**Paragraph 3 — the lossless gap and scope statement.** "Format-level (lossless) compaction is essentially unstudied in the prompt-compression literature, which is dominated by lossy methods; the 52.9% savings figure is presented as a single-wave, single-doctrine result whose auditable transform list ships with this artifact. No general claim about lossy or lossless compression is made: findings hold for this doctrine, this orchestrator/grading stack, this transform family, this rubric, and LLM graders pending the human-anchor study (C3)."

Tone discipline note: the section deliberately uses "negative result for X", never "falsified"; mirrors the pattern doc's "one successful application" framing (DOC-GROUNDED: pattern intro).

### C5 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Insert the three paragraphs (or approved edits) into the pattern doc | Pattern doc "Related work" section | All five citations present with URLs; tone flat |
| Add the two-sentence version to the six-pager §3 | Six-pager revision | No unqualified "falsified" remains (see C8) |
| Verify each cited number against the abstracts before freezing (they match the values above as of 2026-08-19) | Citation check note | Reviewer sign-off on the check note |

---

## C6 — Public, timestamped pre-registration

### 6.1 Honest framing first

Waves 1–6 are complete. A public registration posted now **cannot claim "registered before data"** for those waves. What it can do: (a) make the internally frozen contracts (seals `674ca2bf…`, `55d9a858…`, `6461c201…`, frozen 2026-08-18 per pattern §6 and wave6 §1) publicly verifiable with timestamps; (b) commit future waves to register before data. The cover note must say exactly this. The 2026 agent-experiment preregistration paper explicitly recommends OSF Registries as the platform (ONLINE-GROUNDED: https://arxiv.org/html/2606.11217v1 §5, "We recommend registering studies on established platforms such as OSF Registries before any data collection begins, using templates adapted for AI research").

### 6.2 Options and steps

**Option A — OSF Registries (recommended primary).** Mechanics (ONLINE-GROUNDED: https://help.osf.io/article/330-welcome-to-registrations; https://casrai.org/guides/osf-preregistration):
1. Create OSF account; create a project ("walled-blind-pattern").
2. Upload the frozen files: `wave5-preregistration.md`, `amendment-001`, `amendment-002`, and a filled `grader-pin.md` (C2) + the pilot-history disclosure.
3. Start a registration (Registrations tab → Add a Registration); choose the OSF Preregistration template (general purpose) or Registered Report Protocol; attach the filled 2026 AI-agent template as a supplementary file (the arXiv:2606.11217 template, not an OSF default, is the schema that matches this experiment).
4. Submit; admins get 48 h to approve; auto-approval otherwise; choose public immediately (no embargo needed — the content is the point).
5. The registration number **is a DOI**; record it in the README and pattern doc.
6. Amendments: register the amended contract as a **new registration** of the same project (OSF keeps versioned registrations), or maintain a Transparent Changes document (ONLINE-GROUNDED: https://www.cos.io/initiatives/prereg).

**Option B — Zenodo DOI for the frozen archive (recommended secondary, pairs with C1).** Steps (ONLINE-GROUNDED: https://help.zenodo.org/docs/github/; https://onderzoektips.ugent.be/en/tips/00002267/): upload `walled-blind-pattern-v1.0.zip` + `SHA256SUMS` + the prereg files as a separate record "frozen preregistration W1–W6"; Zenodo mints a version DOI (and a concept DOI across versions); each new version gets a new DOI. Optional: GitHub release → Zenodo auto-archive. Zenodo gives the "permanently available with a unique identifier" property the ACM "Artifacts Available" badge requires (ONLINE-GROUNDED: https://www.acm.org/publications/policies/artifact-review-and-badging-current).

**Option C — arXiv (optional, not a registry).** Post the pattern document itself as a preprint; arXiv timestamps submissions and archives versions immutably, and the paper's template is described in an arXiv paper, but arXiv is not a preregistration registry and cannot mark a contract as frozen-before-data. Use only to give the methodology a citable arXiv ID, after A or B exists.

### 6.3 What exactly to archive

1. The three frozen contract files, byte-identical, with their seal lines and freeze dates.
2. A cover note (`PREREG-COVER-NOTE.md`): states that W1–W6 predate this public registration; that internal freeze dates are evidenced by the seals (2026-08-18, pre-grade per wave6 §1); that grader identity is per `grader-pin.md`; and that future waves register before data.
3. Pilot-testing history disclosure (required by arXiv:2606.11217 §4.2; currently absent from the docs — mark UNVERIFIABLE where the on-disk history is gone).
4. The human-anchor protocol (C3) — register it *before* the anchor grades are read, which is still possible.
5. The DOI/registration URL, quoted in the pattern doc and README.

### C6 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Write `PREREG-COVER-NOTE.md` with the honest framing | Cover note | States post-hoc status, seal dates, future-wave commitment |
| Fill the 2026 AI-agent template (C2 fields + pilot history) | Filled template | Every field answered or marked UNVERIFIABLE |
| Create OSF project + registration; attach files; submit public | OSF registration + DOI | DOI live; README and pattern doc quote it |
| Register the C3 anchor protocol before human grades | Second OSF registration | Registration timestamp precedes first human grade |
| Deposit the release zip on Zenodo | Zenodo record + DOI | DOI resolves; SHA256SUMS included |
| (Optional) post the pattern doc to arXiv and cite the DOIs | arXiv ID | Both DOIs in the preprint |

---

## C7 — Compute/cost disclosure

### 7.1 The norm

NeurIPS checklist item 8: per-experiment worker type (CPU/GPU/cluster/cloud), memory, time of execution; per-run compute and total; and disclosure of compute spent beyond the reported experiments (preliminary/failed runs) (ONLINE-GROUNDED: https://neurips.cc/public/guides/PaperChecklist item 8).

### 7.2 What can be reconstructed vs not

- **Reconstructable (partially):** the rig records per-session input/output token usage in `~/.hermes/state.db` (`session_model_usage` table, read-only) — a mechanism proven on this rig (ONLINE-GROUNDED: browser-harness-sop skill, pve-1 replication notes; token accounting method). If sessions for waves 1–6 are still keyed in that table, per-wave token totals can be summed. Otherwise per-wave token volume must be estimated from pack sizes (cells × legs) — mark the estimate **UNVERIFIABLE**.
- **Not recorded anywhere in the docs:** per-leg wall time, worker memory, model call counts, cloud-vs-local split (see C2 contradiction), compute spent on prereg drafting, lotteries, audits, consult legs, and the wave-7 draft. These are UNVERIFIABLE; the disclosure states them as estimates with a stated method.

### 7.3 The disclosure table template (one row set per wave)

```
Wave | Legs | Cells | Tokens in (sum) | Tokens out (sum) | Wall time | Worker type | Memory | Est. cost
W1   | …    | 12    | …               | …                | …         | local/cloud | …      | …
W6   | 7    | 25    | …               | …                | …         | local-LM backend (wave6 §2); cloud per pattern §7 — resolve per C2 | …
```
- Cost formula (cloud): `cost = Σ legs (tokens_in × price_in/1M + tokens_out × price_out/1M)`; (local): `kWh × electricity rate`, with the model size and quantization stated (Qwen3-4B/Qwen3-8B per pattern §7).
- A second table for non-grading compute: prereg sessions, lottery, audits, consult legs, wave-7 draft — as a single "×N of grading compute" estimate with the method sentence ("estimated from session token logs where present, else from session count × typical session size").
- One line in the pattern doc: "six waves of grading ran ≈X tokens in/Y tokens out across Z legs; total estimated cost $W (method in kit `docs/compute.md`); additional non-grading compute ≈N× grading." This is what makes "runs on a single machine" a checkable claim (iteration-1 condition 7).

### C7 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Query `state.db` `session_model_usage` (read-only) for wave sessions; export token sums | `docs/compute-tokens.csv` | Per-wave token sums or an explicit "not found" per wave |
| Reconstruct leg counts and cell counts per wave from the manifest | Table rows W1–W6 | Matches wave6 §2 leg table and six-pager §3 wave table |
| Write `docs/compute.md` with both tables, formulas, and UNVERIFIABLE marks | `docs/compute.md` | Every number carries a source or "estimated, method stated" |
| Add the one-line cost statement + non-grading-compute factor to the pattern doc | Pattern doc §7 addition | Sentence present; numbers match `compute.md` |
| (Forward) record per-leg wall time, memory, and tokens for every future wave in the manifest | Manifest fields | Recorded at run time, not reconstructed |

---

## C8 — Scoped-claim rewording (exact replacement sentences)

All replacements keep the pattern's own scope variables explicit: doctrine (Amazon Leadership Principles), stack (Hermes supervisor + pinned graders per C2, tiktoken cl100k_base v0.14.0), transform family (T1–T7 mechanical deletions; format-level for lossless), rubric (5-part × 0–3, base-12 gate), n per wave.

**R1. "Lossy/semantic compaction is falsified" (six-pager §3 and deliverable answer #2).**
Replace with: *"Mechanical deletion-based (lossy) compaction is falsified for this doctrine, this orchestrator/grading stack, this transform family (T1–T7: targeted deletion of hedges, conditionals, reversibility qualifiers, and load-bearing qualifiers), and this rubric: HURT at ≤60% reduction, cliff at 40%, load-bearing qualifier loss as the leading damage class, no measurable effect at 20–30% in the near-ceiling validity wave (17/17 PASS). Standing rule for this stack: KEEP FULL PROSE. Generalization to entropy-based or learned compressors, other contexts, other doctrines, other graders, or other rubric thresholds is not claimed."*

**R2. Inter-rater 6/6 = HIGH as instrument-validity evidence (six-pager W6 row; pattern §5 "Inter-rater 6/6 = 100% = HIGH").**
Replace with: *"Inter-rater agreement was 6/6 (100%) on Part 5 across six reserved cells, exceeding the pre-committed 5-of-6 HIGH threshold; this evidences consistency between two LLM graders on one dimension at near-ceiling scores, where Cohen's kappa is undefined. Instrument validity rests on the control record (confab 4/4, deletion 3/4 with B4 INCONCLUSIVE), the byte-level audit (25/25), and the human-anchor study (see validation report)."*

**R3. The 52.9% headline (six-pager §3; pattern §5 W1 row).**
Replace with: *"Format-level (lossless) compaction of this doctrine's envelope prose achieved 52.9% token savings (tiktoken cl100k_base) at 12/12 rubric fidelity (95% CI 0.76–1.00, Wilson) in one 12-cell wave (W1), with the positive control biting 0/12. Single wave, single doctrine, single stack: a candidate, not a permanence claim; the transform list and cells are in the replication kit, so the figure is auditable."*

**R4. Pattern §5b "the discipline survives a supervisor-model swap" (asserted, untested).**
Replace with: *"The claim to test on the replication rig is that the pattern's results replicate (same verdicts on the same frozen packs) under a different supervisor model; this has not yet been run."* (This matches the pattern's own §7 wording; the six-pager's stronger phrasing is the one to fix.)

**R5. Pattern §5 "Lossless compaction works and is safe".** Replace "works and is safe" with "showed no rubric-measured fidelity loss in one 12-cell wave".

### C8 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Apply R1–R5 to the six-pager and pattern doc | Revised documents | No unqualified "falsified", "proves", "is safe", or "survives" claims remain |
| Grep both docs for overreach terms ("falsified", "proves", "safe", "permanence", "generaliz") | Grep log | Terms present only in scoped sentences or the limitations section |
| Keep all honest understatements verbatim (B4 blindness, anchor drift, §7.4 no-op, small n) | Diff of revision | Understatement passages unchanged |

---

## C9 — Corpus licensing (Amazon Leadership Principles)

### 9.1 Findings (ONLINE-GROUNDED, this pass)

- The 16 Leadership Principles are published by Amazon on two official pages: https://www.aboutamazon.com/about-us/leadership-principles and https://www.amazon.jobs/content/en/our-workplace/leadership-principles (both fetched and read this pass; text confirmed present verbatim on both).
- **No open license is declared on either page.** The amazon.jobs page footer carries the standard corporate notice: "© 1996-2026, Amazon.com, Inc. or its affiliates" (verified by fetch of the page source this pass). Default is therefore all-rights-reserved; Amazon holds copyright in the LP text (a corporate, US-published work; the text is short and factual/values-based but original expression).
- The LP text is **widely republished** by third parties (interview-prep sites, career blogs, document-sharing platforms) — e.g., interview and prep sites quote all 16 principles in full. Widespread unlicensed republication is observable practice, but it confers no license and implies nothing about Amazon's enforcement posture. Treat it as noise, not permission.
- Fair use (US, 17 U.S.C. §107) is the relevant legal framework for research use (ONLINE-GROUNDED: https://www.law.cornell.edu/uscode/text/17/107; https://www.copyright.gov/fair-use/; factor summaries at https://ogc.harvard.edu/pages/copyright-and-fair-use). Factor analysis for this corpus: (1) purpose — noncommercial research/replication: favors fair use; (2) nature — published, informational corporate text: favors fair use (factual works are more susceptible to fair use than highly creative works); (3) amount — the whole corpus (~2,000–3,000 words) would be reproduced in a replication kit: **this is the weak factor**; (4) market effect — no licensing market for LP text exists and reproduction does not substitute for any Amazon product: favors fair use. Net: defensible for noncommercial research quoting in the US, with the whole-work reproduction as the exposed point.

### 9.2 Options ranked by risk

**Option 1 — Fetch-and-verify; do not redistribute the doctrine text (LOWEST RISK; recommended default).**
Ship `code/fetch_doctrine.py`: downloads the LP text from the official amazon.jobs page, verifies a pinned SHA-256 (of the exact version used in W1–W6), fails loud on mismatch; record a Wayback Machine snapshot ID as the archival fallback source (https://web.archive.org/). The kit ships the hash, the script, and the citation — not the text. Byte-level determinism is preserved because the transforms operate on the fetched, hash-verified file. Risk: if Amazon edits the page, the fetch fails loudly and the owner re-pins against the Wayback snapshot (a documented procedure, consistent with the pattern's loud-fail philosophy).

**Option 2 — Include the text with a fair-use notice (LOW-MEDIUM RISK; recommended for the optional bundle).**
Ship `doctrine/amazon-doctrine-local-lm.md` inside the archive, clearly marked as third-party quoted material with attribution and a fair-use basis statement (draft below), excluded from the kit's CC-BY-4.0/MIT grants. US-law-dependent; the amount factor is the exposed point; include a contact/takedown line. This preserves offline determinism for readers without network access. If distribution beyond noncommercial research is ever planned, Option 3 applies.

**Option 3 — Request written permission from Amazon (HIGHER RISK / slow; only if broader distribution is planned).**
Amazon's media/legal contacts; outcome uncertain, timeline weeks-to-months. Not a blocker for a research share under Option 1 or 2.

**Option 4 — Paraphrase only (NOT VIABLE for this kit).**
The transforms are byte-span deletions of the exact doctrine text (pattern P3: "variants are pure deletions of reference text… byte span, token count"); paraphrased doctrine would break the deletion logs, the reservation byte-grep (P6), and the audit (25/25 byte_subseq). Replication and paraphrasing are incompatible here.

### 9.3 What to put in the artifact's license/attribution section

`LICENSE.md` (new): "Original methodology text, rubric, and documentation: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/). Code: MIT. The Amazon Leadership Principles text and cell prose quoting or derived from it are NOT covered by these grants; see NOTICE-THIRD-PARTY.md."

`NOTICE-THIRD-PARTY.md` (new), draft text: "This archive includes the Amazon Leadership Principles (16 principles) as quoted material, © 1996–2026 Amazon.com, Inc. or its affiliates, reproduced from the official public pages (https://www.aboutamazon.com/about-us/leadership-principles; https://www.amazon.jobs/content/en/our-workplace/leadership-principles) for noncommercial research and replication purposes under the fair-use provisions of 17 U.S.C. §107. This text is the property of Amazon and is not licensed under this archive's terms; redistribution beyond research use may require Amazon's permission. Grade-cell prose in `cells/` quotes or paraphrases this doctrine and is likewise treated as derived third-party content. For removal or correction, contact [owner]. If the doctrine text is not included (Option 1), this notice instead reads: 'The doctrine text is not redistributed; readers fetch it via `code/fetch_doctrine.py`, which verifies the pinned SHA-256.'"

The NeurIPS checklist item 12 norm requires exactly this: cite the creator of existing assets and state the copyright/terms of the source (ONLINE-GROUNDED: https://neurips.cc/public/guides/PaperChecklist item 12: "If you scraped data from a particular source, you should state the copyright and terms of service of that source").

### C9 CHECKLIST

| Action | Artifact | Done-when |
|---|---|---|
| Decide Option 1 vs 2 and state it in the README | README §7 | Choice recorded with rationale |
| Write `fetch_doctrine.py` + pin the doctrine SHA-256 + record a Wayback snapshot ID | Script + pin file | Fetch verifies hash; snapshot URL recorded |
| Write `LICENSE.md` and `NOTICE-THIRD-PARTY.md` per §9.3 | Both files | Attribution, fair-use basis, and exclusion wording present |
| Mark all cell files quoting/deriving from LP text in the NOTICE | NOTICE coverage list | Every cell file listed or covered by the blanket clause |
| (If Option 2) verify the doctrine file is byte-identical to the graded version before shipping | Diff log | Hash matches the pin |
| Add the one-line licensing statement to the pattern doc (or six-pager footer) | Doc revision | Statement mirrors the NOTICE |

---

## Source list (all URLs read/verified during this pass unless noted)

- arXiv:2606.11217, Preregistration for Experiments with AI Agents (ICML 2026 Spotlight) — https://arxiv.org/abs/2606.11217 ; full text read via harness — https://arxiv.org/html/2606.11217v1
- OSF Registrations help (COS) — https://help.osf.io/article/330-welcome-to-registrations
- CASRAI OSF preregistration guide — https://casrai.org/guides/osf-preregistration
- COS preregistration initiative — https://www.cos.io/initiatives/prereg
- Zenodo GitHub integration — https://help.zenodo.org/docs/github/ ; UGent step-by-step — https://onderzoektips.ugent.be/en/tips/00002267/
- NeurIPS Paper Checklist — https://neurips.cc/public/guides/PaperChecklist (read via harness)
- ACM Artifact Review and Badging v1.1 (current) — https://www.acm.org/publications/policies/artifact-review-and-badging-current ; v1.0 text read via harness — https://www.acm.org/publications/policies/artifact-review-badging
- The Turing Way: Licensing — https://book.the-turing-way.org/reproducible-research/licensing/ ; Data Licenses — https://book.the-turing-way.org/reproducible-research/licensing/licensing-data ; Licensing Checklist — https://book.the-turing-way.org/reproducible-research/licensing/licensing-checklist ; Reproducible Research guide — https://book.the-turing-way.org/reproducible-research/reproducible-research/
- HELM — https://crfm.stanford.edu/helm/ ; repo (Apache-2.0, reproducing-leaderboards docs) — https://github.com/stanford-crfm/helm ; methodology — https://arxiv.org/abs/2211.09110
- Zheng et al., Judging LLM-as-a-Judge with MT-Bench (NeurIPS 2023 D&B) — https://arxiv.org/abs/2306.05685
- Landis & Koch (1977), The Measurement of Observer Agreement for Categorical Data — https://www.jstor.org/stable/2529310 ; kappa interpretation table — https://www.ncbi.nlm.nih.gov/books/NBK92287/table/executivesummary.t2/
- LLMLingua — https://arxiv.org/abs/2310.05736 ; LLMLingua-2 — https://arxiv.org/abs/2403.12968 ; Selective Context (EMNLP 2023) — https://arxiv.org/abs/2310.06201
- An Empirical Study on Prompt Compression (ICLR 2025 Building Trust workshop) — https://arxiv.org/abs/2505.00019
- Prompt Compression in the Wild (ECIR 2026) — https://arxiv.org/abs/2604.02985
- Amazon Leadership Principles (official) — https://www.aboutamazon.com/about-us/leadership-principles ; https://www.amazon.jobs/content/en/our-workplace/leadership-principles (footer © notice verified by page fetch, 2026-08-19)
- 17 U.S.C. §107 (fair use) — https://www.law.cornell.edu/uscode/text/17/107 ; U.S. Copyright Office Fair Use Index — https://www.copyright.gov/fair-use/ ; Harvard OGC fair-use summary — https://ogc.harvard.edu/pages/copyright-and-fair-use
- NeurIPS 2026 Main Track Handbook (cited from iteration 1) — https://neurips.cc/Conferences/2026/MainTrackHandbook
- Statistical Rigor and Reproducibility in the AI Era (cited from iteration 1) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12402953/

*Statistics in C4 computed from the rubric definitions in the source docs (exact binomial power, Wilson and Clopper–Pearson intervals, kappa examples); computation script archived at `code/stats.py` in the kit.*

---

# PART 8 — WORKER D: AUDIT OF THE DISREGARDED BATCH — worker-D-disregarded-audit.md

# AUDIT — Worker A Verification Report & Worker B Decision Brief (disregarded-batch artifacts)

**Auditor:** Worker D (independent audit subagent)
**Date:** 2026-08-19
**Scope:** Independent assessment of two set-aside research reports on their own merits:
- `worker-A-verification.md` (130 lines; literature verification of the experiment's four headline claims)
- `worker-B-decisions.md` (170 lines; decision brief D1–D6 for the single-threaded owner)

**Context documents read in full (for cross-checking):**
- `loop-closure-six-pager-DRAFT.md` (142 lines)
- `hermes-replicable-pattern.md` (346 lines)
- `wave6-grading-finding.md` (183 lines)

**Method:** All five files read in full. Every load-bearing external claim was checked against the cited source: discovery via `web_search`, full-text retrieval via HTTP fetch (arXiv HTML, IES PDFs, PMC/Pubmed) with targeted string extraction, one browser-harness attempt (landed on an arXiv landing page; fell back to direct fetch per SOP). All 25 fetched URLs returned HTTP 200. No CAPTCHA/login walls encountered. Internal doc claims (seals, manifests, lottery, audits) were not re-verified — they are artifacts only the owning host can verify, and neither report claimed to verify them.

**Grounding taxonomy used below:**
- **DOC-GROUNDED** — claim rests on the project's own on-disk record (six-pager / pattern / wave-6 finding).
- **ONLINE-GROUNDED** — claim verified against an external source fetched during this audit.
- **UNVERIFIABLE** — could not be checked from here (internal artifact, or source-specific number not located in fetched text).

---

## 1. VERDICT

**PRESERVE-SELECTED** (both reports).

Neither report is redundant with the source docs or with each other: the three context documents contain **no external literature at all**, and the two reports carry complementary, decision-relevant, independently verified external grounding plus the project's only owner-action menu. Both reports also contain a small number of correctable citation/number errors (Section 4). Preserving them with the corrections below, as annexes to the project record, retains real value; preserving them verbatim as authoritative would propagate a few misstatements; disregarding them entirely would lose the single most on-point external precedent for the compression question (the production RCT), the only quantitative sample-size basis for R5, the only external evidentiary ladder for the "pattern proven" claim, and the only literature anchor for the ceiling-effect and drift critiques.

---

## 2. UNIQUE VALUE INVENTORY

### 2.1 What Worker A adds that exists nowhere else in the project record

| # | Finding | Location | Independent value |
|---|---------|----------|-------------------|
| A1 | ONTO (arXiv:2604.17512) reports 46–51% token reduction for JSON→columnar format with no material accuracy loss — an external magnitude anchor for the W1 52.9% claim | `worker-A-verification.md` §1, item 1; Verdict §1 | VERIFIED (abstract, §5.1 of paper). The only external evidence that ~50% format-level savings at zero measured loss is a published, precedented magnitude for the W1 result |
| A2 | Wild-compression paper (arXiv:2604.02985): "LLMLingua-2 is unsuitable for compressing structured synthetic datasets"; Passage Counting <20%→<4.5%; retrieval "sometimes to below 50%"; classification −52%; code edit-similarity drops even at 1.4× | `worker-A-verification.md` §2, items 1, 6 | VERIFIED. An independent published confirmation of the direction of the W3–W5 HURT finding on structured text — the single most decision-relevant external result for the KEEP FULL PROSE posture |
| A3 | Counter-evidence scoping: LongLLMLingua +21.4% NQ, CORE "lossless" = task-performance-lossless, wild-paper Mistral-7B improvement — lossy compression *helps* in long-context/noisy settings | `worker-A-verification.md` §2, items 3, 4; §2 Verdict | VERIFIED. Keeps the HURT claim honestly scoped as domain-conditional rather than a general law; the docs' own scoping ("this doctrine and stack") is independently supported |
| A4 | Terwee 2007 >15% ceiling-effect criterion applied to the 17/17 near-ceiling; raw-agreement 6/6 inter-rater without chance-correction critique; rubric-dimension independence questioned (Hu et al.) | `worker-A-verification.md` §3, item 4; §4, item 1 | VERIFIED (Terwee; Hu existence). Quantifies why near-ceiling "no movement" is a measurement property of the instrument, and why 100% raw agreement is weaker than reported — neither point exists in the source docs |
| A5 | Judge drift (Chen/Zaharia/Zou: GPT-4 84%→51% Mar→Jun 2023) applied to the B4 anchor drift; omission-blindness literature (SummEdits: GPT-4 8% below human) applied to the DEL-b4 blindness, which the report correctly identifies as a live in-experiment instance of a documented LLM weakness | `worker-A-verification.md` §4, items 2, 4 | VERIFIED. External anchors for two limitations the docs discovered empirically but did not contextualize |
| A6 | Sclar et al. (76 accuracy points across semantically equivalent prompts) as a caution that 12/12 rubric fidelity ≠ behavioral equivalence | `worker-A-verification.md` §1, item 5 | VERIFIED. Supports the report's own recommendation (downstream behavioral probe before adoption) — which independently converges with Worker B's D1 preconditions |
| A7 | Four-claim verdict table with a partial-support reading of the W6 "genuine, not instrument blindness" claim (controls probe only the planted damage classes; B4-family PASS carries the INCONCLUSIVE caveat) | `worker-A-verification.md` head table, §4 Verdict | Internal-consistency check: matches the docs' own limitation language; a defensible scoping of the strongest claim in the set |

### 2.2 What Worker B adds that exists nowhere else in the project record

| # | Finding | Location | Independent value |
|---|---------|----------|-------------------|
| B1 | The pre-registered production compression RCT (arXiv:2603.23525): 27.9% mean total-cost reduction at r≈0.5; aggressive r=0.2 Pareto-dominated on cost and similarity; light r=0.8 output-expansion 1.33× producing net cost increase; "compress more is not a reliable production heuristic"; planned 211/arm vs realized 59–61/arm with explicitly underpowered nulls; H5 threshold-alignment inconclusive | `worker-B-decisions.md` D1, D3 | VERIFIED (all figures verbatim in paper). The most on-point external precedent for this experiment's central question — a pre-registered, walled-adjacent RCT of prompt compression on production multi-agent orchestration. Neither the source docs nor Worker A cite it. It directly shapes D1 (net-cost accounting, canary, per-domain eval) and D3 (n sizing) |
| B2 | Decision menu D1–D6: postures (DO NOW / PARK WITH TRIGGER), preconditions, and a frozen-record-safe ordering table with explicit gates | `worker-B-decisions.md` D1–D6 | The project's only owner-action artifact. The six-pager §5 records decisions; Worker B converts them into executable steps with gates, and checks each step against the frozen-record discipline (amendments forward-only; no frozen value re-graded) |
| B3 | Evan Miller power formula and worked numbers (δ=0.03 → n≈969 → "at least 1,000 questions"; K=1→10 cuts MDE 13.2%→7.5%) applied to the P7 rulebook thresholds (0.10/0.20 deltas) to size R5 at ~20–400 cells per arm | `worker-B-decisions.md` D3 | VERIFIED (formula verbatim; both worked numbers verbatim). The only quantitative sample-size basis in the project; the re-derivation (paired design, Miller formula, ω²≈0.2–0.4) is internally consistent with the formula |
| B4 | WWC single-case design evidentiary standards (≥5 studies, ≥3 research teams, ≥3 institutions, ≥20 cases; ≥3 demonstrations) and FORRT replication norms (small telescopes 2.5×/80% power, 4.5×/95% power) as the external ladder for the "pattern proven the second time" claim | `worker-B-decisions.md` D4 | VERIFIED (both WWC PDFs fetched; FORRT §6.2 fetched). Provides the field's actual evidentiary bar for repeated-application claims — the pattern doc's "second time" framing is shown to be the minimum of the ladder, not the top |
| B5 | Lipsitch negative controls framework + the negative-controls scoping review: a non-biting control is a design defect to fix, not a pass — applied to DEL-b4 | `worker-B-decisions.md` D2 | VERIFIED (PMC3053408; S0895435623003189 both resolve). External validation of the wave-7 repair logic and of the docs' own "never counted PRESERVED" treatment of the blind control |
| B6 | Rubric/judge drift literature with the prescribed remedy (recalibrate against frozen labeled set; pin anchor; forward-only amendment; record judge+rubric versions per wave) | `worker-B-decisions.md` D2 | Existence VERIFIED (Deepchecks, LangChain, medium adnanmasood). Gives the B4 anchor drift a named failure mode and a standard remedy — the docs diagnosed it empirically; Worker B classifies it |
| B7 | Local-judge evidence: Verga PoLL juries (panel > single large judge, >7× cheaper), Qwen3 thinking-mode judges (0.6B below 50% on hard tasks; 4B thinking +10.5 pts at 1.82× FLOPs vs +4.5 pts at 8.16× for 7-shot ICL), Prometheus domain-fine-tuning condition, MT-Bench GPT-4 >80% human agreement | `worker-B-decisions.md` D5 | VERIFIED (all figures located in fetched texts). Turns the Qwen3-4B port from a plan into a gated plan with a documented capacity floor, panel requirement, and calibration precondition; the sealed-packs-as-gold-set calibration idea is a genuinely novel methodological contribution |
| B8 | D6 ordering rationale: wave-7 first because every later measurement reads through the instrument; R5 parked with a trigger; frozen-record integrity check on every step | `worker-B-decisions.md` D6 | Decision-relevant synthesis; consistent with the six-pager's "not a hidden debt" framing and with Worker A's implication that the B4 blind spot must be resolved before B4-family claims are read as PASS |

### 2.3 Convergence worth preserving

Worker A and Worker B were independent of each other and of the wave-7 draft, yet both conclude: (a) the near-ceiling limits what any "no movement" claim can establish; (b) the B4 deletion-control blindness is the central instrument defect and must be fixed before further claims; (c) adoption requires a downstream behavioral/regression eval, not rubric scores alone; (d) chance-corrected inter-rater and score distributions should be reported. This independent convergence is itself evidence-bearing for the owner's decision.

---

## 3. CLAIM SPOT-CHECK

All sources fetched during this audit; "match" = the report's number/attribution matches the fetched source text.

### 3.1 Load-bearing external claims — Worker A

| Claim (report §) | Source checked | Result | Status |
|---|---|---|---|
| ONTO (arXiv:2604.17512, Apr 2026, H. Deekeswar) reports 46–51% token reduction vs JSON across three synthetic operational datasets, no material degradation on lookup/counting/extraction/aggregation, Qwen2.5-7B, "schema-once, data-many" | https://arxiv.org/html/2604.17512v1 | Exists; **all figures verbatim** in abstract + §5.1. One nuance: paper conditions the no-degradation result on "when format context is provided" — omitted from the headline quote (§1 item 1) but acknowledged in §1 item 2 | **MATCH** (minor qualifier omission, see §4.E) |
| Wild paper (arXiv:2604.02985, ECIR 2026, Kummer et al.): up to 18% end-to-end speed-up only when "prompt length, compression ratio, and hardware capacity are well matched"; "LLMLingua-2 is unsuitable for compressing structured synthetic datasets"; Passage Counting <20%→<4.5%; retrieval "sometimes to below 50%" (paragraph numbering lost); classification up to −52% ("removes class-indicative patterns"); code edit-similarity drops at 1.4× ("even slight compression harms model outputs"); summarization robust to 5.7×; Mistral-7B improves when its 8k context truncated; 30,000 queries | https://arxiv.org/html/2604.02985v1 | Exists; all quoted figures **verbatim**. One slip: report says "30,000+ runs"; paper says "thousands of runs and 30,000 queries" (see §4.E) | **MATCH** (one unit slip) |
| LLMLingua-2 (arXiv:2403.12968, ACL 2024 Findings): NQ(20 docs) EM 75.7→48.6 at 3.9×; MeetingBank 87.75→86.92 at 3.1×; LongBench-ZH avg 42.5→38.1 at 5×; "guarantee the faithfulness of the compressed prompt" | https://arxiv.org/html/2403.12968v2 | Exists; all table figures **verbatim**; faithfulness quote near-verbatim | **MATCH** |
| LLMLingua (arXiv:2310.05736): "as the compression ratio increases especially around 25x-30x, all methods as well as ours will experience a substantial performance drop"; budget controller compresses demonstrations most aggressively, instructions/questions least | https://arxiv.org/html/2310.05736v2 | Exists; both **verbatim** | **MATCH** |
| LongLLMLingua (arXiv:2310.06839): up to +21.4% on NaturalQuestions with ~4× fewer tokens (GPT-3.5-Turbo) | https://arxiv.org/abs/2310.06839 | Exists; **verbatim** in abstract | **MATCH** |
| CORE (arXiv:2508.19282): "lossless context compression" for RAG; NQ EM 0.3803 @ 712 tokens → 0.3947 @ 47 tokens; "improves the average Exact Match (EM) score by 3.3 points" | https://arxiv.org/html/2508.19282v3 | Exists; all figures **verbatim** (Table: Top5 Documents row; abstract) | **MATCH** |
| Sclar et al. (arXiv:2310.11324): up to 76 accuracy points across semantically equivalent prompts, LLaMA-2-13B | https://arxiv.org/abs/2310.11324 | Exists; **verbatim** in abstract | **MATCH** |
| Zheng et al. (arXiv:2306.05685): position/verbosity/self-enhancement biases; GPT-4 favors itself 10% higher win rate, Claude-v1 25%; "Only GPT-4 outputs consistent results in more than 60% of cases" | https://arxiv.org/html/2306.05685 | Exists; all **verbatim** in body (§4) | **MATCH** |
| Xiong et al. (arXiv:2306.13063): verbalized confidence informative for failure prediction (AUROC 0.522–0.605); models overconfident; "verbalized confidence values predominantly fall within the 80% to 100% range" | https://arxiv.org/html/2306.13063v2 | Exists; all **verbatim** in abstract/body (§5.1, §B.3) | **MATCH** |
| SummEdits (arXiv:2305.14540): most models near chance; best model GPT-4 "still 8% below estimated human performance" | https://arxiv.org/abs/2305.14540 | Exists; **verbatim** in abstract | **MATCH** |
| Chen, Zaharia & Zou (arXiv:2307.09009): GPT-4 prime-number accuracy 84% → 51% between March and June 2023 versions | https://arxiv.org/abs/2307.09009 | Exists; **verbatim** in abstract | **MATCH** |
| MMLU-Redux (arXiv:2406.04127): 6.49% of MMLU questions contain errors; re-evaluation shows discrepancies | https://arxiv.org/abs/2406.04127 | Exists; **verbatim** in abstract | **MATCH** |
| Panickssery et al. (arXiv:2404.13076): evaluators recognize and favor their own generations (self-preference) | https://arxiv.org/abs/2404.13076 | Exists; title/abstract consistent | **MATCH** |
| Hu et al. (arXiv:2402.12055): LLM evaluators confuse NLG quality criteria | https://arxiv.org/abs/2402.12055 | Exists; title/abstract consistent. Specific "18 perturbation types" not re-verified from body | **MATCH** (18-perturbation detail: not re-verified) |
| Kapoor & Narayanan (arXiv:2311.18807): preregistration for predictive modeling | https://arxiv.org/abs/2311.18807 | Exists. Specific limits list (self-selection; distribution shift; gaming) not located in fetched abstract | **MATCH** (existence); limits list: not re-verified |
| Terwee et al. 2007: ceiling effect present if >15% of respondents achieve highest score | https://pubmed.ncbi.nlm.nih.gov/17161752/ ; https://www.sciencedirect.com/science/article/abs/pii/S0895435606001740 | Exists; 15% rule **verbatim** ("more than 15% of respondents") | **MATCH** |
| Oppenheimer et al. 2009 (IMC); Thomas & Clifford 2015; Howcroft et al. INLG 2020; Morante & Daelemans BioNLP 2009; Reiter omissions post | academia.edu mirror; journals.sagepub.com; aclanthology.org/2020.inlg-1.23; aclanthology.org/W09-1304.pdf; ehudreiter.com/2026/02/11/dont-ignore-omissions/ | All exist (fetched: INLG, W09-1304, Reiter). Oppenheimer cited via a non-authoritative academia.edu mirror URL — paper is real (J Exp Soc Psychol 2009) | **MATCH** (mirror-URL hygiene note, §4.G) |
| Practitioner blogs: Tensorlake TOON, MightyBot structured formats | tensorlake.ai/blog/toon-vs-json; mightybot.ai/blog/best-structured-prompt-formats-for-llms/ | Both exist; descriptions consistent with report's use | **MATCH** (existence) |

### 3.2 Load-bearing external claims — Worker B

| Claim (report §) | Source checked | Result | Status |
|---|---|---|---|
| Production RCT (arXiv:2603.23525, Mar 2026): six-arm pre-registered trial, 358 complete-case Claude Sonnet 4.5 runs, 59–61/arm, corpus of 1,199 instructions; moderate r≈0.5 → 27.9% mean total-cost reduction; aggressive r=0.2 dominated on both cost and similarity; light r=0.8 output expansion e=811/609≈1.33 → net cost increase; "compress more is not a reliable production heuristic" and "output tokens must be treated as a first-class outcome"; planned n=211/arm (G\*Power, f=0.25) vs realized 59–61 → "null results should be interpreted with caution"; H5 "Directional but Quantitatively Inconclusive"; TAAC §1.1: code cliff r=0.55, CoT r=0.70; CONSORT flow reporting | https://arxiv.org/html/2603.23525 | Exists; **every figure and both quoted sentences verbatim**; §2.7.5 power statement verbatim; Finding 6 H5 wording verbatim; §3.2 CONSORT Flow section present | **MATCH** (all) |
| Miller (arXiv:2411.00640): n = (z_α/2 + z_β)²(ω² + σ²_A/K_A + σ²_B/K_B)/δ²; δ=0.03 at 80% power → n≈969 → "new evals should contain at least 1,000 questions"; K_A=K_B: 1→10 cuts MDE from 13.2% to 7.5% | https://arxiv.org/html/2411.00640 | Exists; formula **verbatim**; both worked numbers **verbatim** | **MATCH** |
| WWC single-case design: strong evidence requires ≥5 studies meeting standards, ≥3 different research teams, ≥3 different institutions, ≥20 combined cases; ≥3 demonstrations/attempts per study; Document/229 URL | https://ies.ed.gov/ncee/wwc/Document/229 ; wwc_scd_understanding_IR_011017.pdf ; wwc_scd_key_criteria_011017.pdf | All resolve (HTTP 200). Both PDFs contain the 5/3/3/20 criteria **verbatim**; "at least three attempts with sufficient data points" verbatim in key-criteria doc | **MATCH** |
| Lipsitch, Tchetgen Tchetgen & Cohen, *Negative Controls*, Epidemiology 2010, PMC3053408 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/ ; pubmed 20335814 | Exists; PMC ID resolves to the correct paper | **MATCH** |
| Negative-controls scoping review (J Clin Epidemiol 2023; S0895435623003189) | https://www.sciencedirect.com/science/article/pii/S0895435623003189 | Exists ("Advances in methodologies of negative controls: a scoping review", Yang et al., DOI 10.1016/j.jclinepi.2023.111228) | **MATCH** |
| Terwee 2007 15% rule (D1/D3) | as §3.1 | Verified | **MATCH** |
| FORRT Replication Handbook §6.2: replications need larger samples; small telescopes 2.5× original for 80% power, 4.5× for 95% power | https://forrt.org/replication-handbook/execution_replications.html | Exists; **verbatim**: "2.5 times as large as the original for 80% power… aiming for 95% power… requires a multiple of 4.5" | **MATCH** |
| Verga et al. (arXiv:2404.18796): jury of smaller models beats single large judge; "over seven times cheaper" | https://arxiv.org/html/2404.18796 | Exists; "over seven times cheaper" **verbatim** | **MATCH** |
| "Thinking Small Models are Efficient LLM Judges" (arXiv:2509.13332): Qwen3 0.6B fails to exceed 50% on Chat Hard/Safety, sometimes below random; 4B thinking +10.5 pts at 1.82× FLOPs vs +4.5 pts at 8.16× for 7-shot ICL; thinking consistency 83–91% → 91–94% under induced biases | https://arxiv.org/html/2509.13332 | Exists; all figures **verbatim** (report's "~91% vs ~85%" is a fair compression of the paper's ranges, at the favorable end) | **MATCH** |
| MT-Bench (arXiv:2306.05685): GPT-4-as-judge >80% agreement with humans, human–human level | https://arxiv.org/html/2306.05685 | Exists; **verbatim** ("exceeding 80%… the same level of agreement between humans") | **MATCH** |
| CALM bias framework = arXiv:2410.02736 | https://arxiv.org/abs/2410.02736 | Exists — paper is "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge"; its proposed framework is named **CALM** in the abstract | **MATCH** |
| "Judging the Judges: A Systematic Study of Position Bias" (IJCNLP 2025); disagreement instances rare (<5%), hard/bias-prone; majority voting the reliability signal | https://aclanthology.org/2025.ijcnlp-long.18/ ; arxiv.org/abs/2406.07791 | Exists (IJCNLP 2025, Shi et al.). **Mismatch on the "<5% rare" figure**: the paper reports all-nine consensus on 23.4% of instances, ≤2 disagreements on 58.4%, and extreme disagreement (levels 5–6) "sharply decline to less than 8% of the total". Disagreement is common; extreme disagreement is <8%, not <5%. The "hard instances = high disagreement" reading is correct | **MISMATCH** (see §4.A) |
| Prometheus (arXiv:2310.08491): fine-tuned 7B/13B can match/exceed GPT-4 on a domain when fine-tuned on that domain | https://arxiv.org/abs/2310.08491 | Exists; abstract consistent | **MATCH** |
| Reproducibility Project: Psychology (Science 2015): 97% original significant, 36% replicated, effects ~half magnitude; Many Labs 2 ~50% | PMC5976261 / research.rug.nl PDF; journals.sagepub.com/doi/10.1177/2515245918810225 | 97%/36%/half **verbatim** in PMC; Many Labs 2: 14/28 = 50% replicated | **MATCH** |
| Brandt et al. 2014 preregistration norms | (search) | Exists — but as *The Replication Recipe* (J. Exp. Soc. Psychol. 2014), which advocates preregistration; the canonical "preregistration revolution" paper is Nosek et al. 2018 (PNAS). Attribution slightly loose | **MATCH** (existence); canonical-reference note §4.D |
| Willroth & Atherton 2024 (preregistration deviations) | (search) | Exists ("Best Laid Plans: A Guide to Reporting Preregistration Deviations") | **MATCH** (existence) |
| Selective Context (Li et al. 2023) cited as "arXiv:2310.06839-family work" | — | Selective Context is **arXiv:2310.06262**; 2310.06839 is LongLLMLingua. Family attribution wrong | **MISMATCH** (ID, §4.B) |
| LLMLingua-family "plateau-then-drop ('not advisable above ~20×')" | LLMLingua GitHub / paper | The GitHub README claims "up to 20x compression with minimal performance loss"; the paper's drop threshold is "around 25x-30x". Report conflates the two | **PARTIAL** (§4.C) |
| Practitioner sources: tianpan.co (n=100 → MDE ~10–12 pts; 500–1,000 → ~5 pts); dev.to eval sizing (2-pt delta ≈ 6,300/arm; 7-pt ≈ 480/arm); neuraltrust.ai (text-to-SQL join 0.63→0.37); Langfuse CI-gate practice; DeepEval EDD; Deepchecks/LangChain calibration; Anthropic "Demystifying evals for AI agents" (Jan 2026); medium adnanmasood rubric drift; thread-transfer.com | (search + snippets) | All **exist** (URLs resolve; titles/descriptions consistent). Specific numbers (tianpan, dev.to, neuraltrust) not extracted verbatim; all are consistent with standard two-proportion power math (re-derivable: n=100 at p≈0.85 → MDE ≈ 10 pts; 2-pt delta ≈ 5,000–6,300/arm) | **EXISTENCE CONFIRMED**; numbers plausible, not verbatim-verified |
| PMC2778494 as ceiling-effects support (D3) | https://pmc.ncbi.nlm.nih.gov/articles/PMC2778494/ | Exists — "Investigating Ceiling Effects in Longitudinal Data Analysis" (Wang et al. 2009). Correct as a supplementary ceiling-effects citation, though not the Terwee paper | **MATCH** (existence; identity note) |
| Serdar et al. 2020 sample-size review, PMC7745163 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7745163/ | Exists — "Sample size, power and effect size revisited" | **MATCH** |

### 3.3 DOC-GROUNDED claims (cross-checked against the three context documents, not the web)

Both reports' internal numbers (52.9% / 12-of-12 / 17-of-17 / 4-of-4 confab / 3-of-4 deletion with B4 INCONCLUSIVE / inter-rater 6-of-6 / P7 thresholds 0.10–0.20 / W5 cliff 20–30% / B4 frozen datum 13/15 P2=1 / KEEP FULL PROSE / wave-7 draft items) are **consistent** with the six-pager, pattern doc, and wave-6 finding. No cross-doc discrepancy found between the reports and the source record on any headline number. Worker A's "cliff at 20–40%" (summary table row 2) is a faithful range summary of the docs' "cliff at 40%" (W3–5) refined to "20–30%" (W5). Worker B's "0.10 within reference = PRESERVED; 0.11–0.20 = MARGINAL" matches pattern doc P7.

### 3.4 UNVERIFIABLE (from this host)

Internal artifacts neither report claims to have verified: seal round-trips (`6461c201…`, `55d9a858…`, `674ca2bf…`), lottery reproducibility, byte audits, manifest ledger state, wave-5 baseline re-derivation. Also unverified: the exact body text of tianpan.co / dev.to / neuraltrust.ai numbers (existence confirmed only).

---

## 4. ERROR SCAN

Findings sorted by severity. None changes a headline verdict of either report; all are correctable before external sharing.

**4.A — Worker B D5: misstated figure from "Judging the Judges" (arXiv:2406.07791 / IJCNLP 2025).** Report: "instances where judges disagree are exactly the hard, bias-prone ones, and they are rare (<5%)". Source: full consensus on 23.4% of instances; ≤2 dissenting judges on 58.4%; extreme disagreement (5–6 of 9 judges) "sharply decline[s] to less than 8% of the total". The "hard instances carry the disagreement" reading is supported; the "<5% rare" figure is not — the source's number is <8% for the extreme class, and disagreement overall is the norm, not rare. The report's underlying recommendation (panels, majority verdicts; the paper itself endorses majority voting) survives, but the figure must be corrected or dropped. (Severity: moderate; misquotes a number that changes the flavor, not the direction, of the D5 argument.)

**4.B — Worker B D1: mislabeled paper ID.** "Selective Context arXiv:2310.06839-family work, Li et al. 2023" — 2310.06839 is LongLLMLingua; Selective Context is arXiv:2310.06262. Same research family (Microsoft), wrong ID. (Severity: minor; citation hygiene.)

**4.C — Worker B D1: "not advisable above ~20×" conflates two sources.** The LLMLingua GitHub README claims "up to 20x compression with minimal performance loss"; the paper (arXiv:2310.05736) locates the substantial drop "around 25x-30x". The report's phrasing merges both into one claim. (Severity: minor.)

**4.D — Worker B D6: "Brandt et al. 2014" cited as preregistration norm.** Brandt et al. 2014 is *The Replication Recipe* (JESP), which does advocate preregistration; the canonical reference for preregistration norms is Nosek et al. 2018 (*The preregistration revolution*, PNAS). Attribution loose but not false. (Severity: minor.)

**4.E — Worker A §1: two unit/qualifier slips.** (i) Wild paper described as "30,000+ runs"; the paper says "thousands of runs and 30,000 queries". (ii) ONTO's "no material degradation" is quoted without the paper's condition "when format context is provided" — the report does acknowledge the condition in §1 item 2, so this is a headline-quote truncation, not a substantive error. (Severity: minor.)

**4.F — Worker A §3: "recommended mitigations are exactly the docs' mechanisms… blind the judge"** — the MT-Bench paper's listed mitigations are position swapping and detailed instructions; "blinding the judge" is the report's synthesis, reasonably derived but not a verbatim source mitigation. (Severity: minor; flagged for precision.)

**4.G — Citation hygiene (both).** Worker A links Oppenheimer et al. via an academia.edu mirror rather than the journal; Worker A's source list includes Liu et al. *Lost in the Middle* (arXiv:2307.03172, real) which is never cited in the body; Worker B's "light compression (r=0.8) increased net cost *in a pilot*" — the paper reports the 1.33× expansion for the light arm without the "pilot" qualifier in the located passage. (Severity: cosmetic.)

**4.H — Not errors, noted for the record.** Worker A's verdict on claim 4 ("partially supported") and its B4-family INCONCLUSIVE recommendation agree with the docs' own limitation language — this is corroboration, not contradiction. Worker B's "consistency ~91% vs ~85%" for thinking vs non-thinking judges is a favorable-end compression of the paper's 83–91% → 91–94% ranges, within bounds. Worker B's D3 power estimates ("80–400 cells for 0.10 delta; 20–100 for 0.20") re-derive cleanly from Miller's formula with ω²≈0.2–0.4 and paired design; "on the order of" is honest hedging. Both reports' tianpan/dev.to numbers are plausible against standard two-proportion math.

**Internal-consistency result:** No contradictions found between the two reports and the three context documents on any headline number or limitation. No fabricated sources found anywhere: every source in both reports that was fetched resolved and matched.

---

## 5. RECOMMENDATION

### 5.1 Preserve (fold into the permanent record)

1. **Worker B D1–D6 in full** — as the owner's decision annex (e.g., `decision-brief-D1-D6.md` alongside the six-pager), with corrections 4.A–4.D applied. This is the only artifact that turns the experiment into an action menu with gates, and its load-bearing external claims (production RCT, Miller, WWC, FORRT, Lipsitch, Qwen3-judge evidence) all verified.
2. **Worker A §1–§4 in full** — as a literature-verification annex to `experiment-conclusion.md` (or a `literature-verification-annex.md`), with corrections 4.E–4.G applied. Its four-verdict table is the project's only systematic external anchoring of the claims; the ONTO magnitude anchor, the wild-paper structured-text confirmation, the Terwee ceiling critique, and the kappa/omission-blindness points are all verified and used nowhere else.
3. **Both reports' convergence points** (Section 2.3) should be stated once in the conclusion memo: independent agents converged on wave-7-first, near-ceiling limits, behavioral-probe-before-adoption, and chance-corrected agreement reporting.
4. **The production RCT (arXiv:2603.23525)** should be cited in the six-pager itself — it is the single closest published precedent to the whole experiment, and its 27.9%-at-r≈0.5 / output-expansion-paradox findings materially sharpen D1's net-cost precondition.

### 5.2 Correct before preserving (checklist)

- [ ] 4.A: replace "<5% rare disagreement" with the source's actual figures (23.4% full consensus; <8% extreme disagreement) or drop the sentence.
- [ ] 4.B: fix Selective Context ID to arXiv:2310.06262.
- [ ] 4.C: separate "20× (GitHub README)" from "25x–30x drop (paper)".
- [ ] 4.D: add Nosek et al. 2018 as the canonical preregistration citation alongside Brandt et al. 2014.
- [ ] 4.E: "30,000 queries" (not runs); restore ONTO's "when format context is provided" qualifier in the headline quote.
- [ ] 4.F: mark "blind the judge" as the report's synthesis, not an MT-Bench verbatim mitigation.
- [ ] 4.G: replace the academia.edu mirror with the JESP DOI; drop or wire in the unused Lost-in-the-Middle source entry.

### 5.3 Can be safely disregarded

- The standalone framing of either report as an *authoritative* verification product — both are annex-grade material whose load-bearing content is now folded in with corrections; they should not be quoted externally (Stanford share) without the corrections applied.
- No section of either report is contradicted by the source record, so no section needs to be *suppressed*; the only content that should not propagate is the specific items in 5.2.
- Worker B's D3 numeric ranges (80–400 / 20–100 cells) may be simplified in the annex to "~100–400 per arm for 0.10 deltas" with the Miller derivation kept in a footnote — the exact range is not load-bearing.

### 5.4 Reasoning summary

The set-aside decision was based on these reports being superseded by later work, not on their being wrong. The audit finds: (a) the three context documents contain zero external literature, so the reports' verified external grounding is not duplicated anywhere in the record; (b) every load-bearing claim in both reports that could be checked was found accurate in substance (one misquoted figure, one wrong paper ID, and several minor slips); (c) the two reports are complementary to each other (Worker A: lossless-analog + cliff + ceiling critique; Worker B: production precedent + power math + decision menu) and both are complementary to the source docs. Losing them would cost the project its only decision menu, its only sample-size basis, and its only independent literature confirmation of the two headline numbers. That is genuine value; hence preserve-selected rather than preserve-as-is or disregard.

---

## 6. Sources verified during this audit (all HTTP 200)

arXiv HTML/abs: 2604.17512 (ONTO), 2603.23525 (production RCT), 2604.02985 (wild), 2411.00640 (Miller), 2403.12968 (LLMLingua-2), 2310.05736 (LLMLingua), 2310.06839 (LongLLMLingua), 2508.19282 (CORE), 2306.05685 (MT-Bench), 2404.18796 (Verga), 2509.13332 (Qwen3 judges), 2306.13063 (Xiong), 2406.07791 (Judging the Judges). arXiv abs: 2310.11324, 2305.14540, 2307.09009, 2406.04127, 2402.12055, 2404.13076, 2410.02736, 2310.08491, 2311.18807, 2311.08877. Other: PMC3053408, PMC2778494, PMC7745163, PubMed 17161752 / 20335814 / 38040387, ScienceDirect S0895435606001740 + S0895435623003189, IES WWC Document/229 + two SCD PDFs, FORRT handbook §6, aclanthology 2020.inlg-1.23 + W09-1304, ehudreiter.com omissions post, tensorlake/mightybot/neuraltrust/thread-transfer/tianpan/dev.to/deepchecks/langfuse/deepeval/anthropic/medium-adnanmasood (existence).

*End of audit.*

---

# PART 9 — MASTER ASSESSMENT (CONSOLIDATION + EXECUTION PLAN) — 00-MASTER-ASSESSMENT.md

# MASTER ASSESSMENT — Walled-Blind Compression Experiment (Waves 1–6)
## Consolidated findings + execution plan for the owner (Ryan)

**Date:** 2026-08-19 · **Location:** pve-1 (review host) — all on-disk artifacts live on the original host and remain UNVERIFIABLE from here except the three shared documents.

**Inputs consolidated (all read in full):**
- The three source docs: `loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md`, `wave6-grading-finding.md`
- Supervisor's own document review (seal discrepancy, record hygiene)
- Worker A — verification vs literature (v2 + batch-3 variant: `worker-A-verification-v2.md`, `worker-A-verification.md`)
- Worker B — decision evidence (v2 + batch-3 variant: `worker-B-decisions-v2.md`, `worker-B-decisions.md`)
- Worker C — external readiness (v2 + batch-3 variant + iteration 2: `worker-C-readiness-v2.md`, `worker-C-readiness.md`, `worker-C-iteration2.md`)
- Independent research by three blind sub-agents using the browser-harness (qutebrowser CDP :9222, `uvx browser-use`); every online claim URL-cited in the worker reports.

---

## PART 1 — Evidence status (the four headline claims vs the published record)

| Claim | Status vs literature | Confidence |
|---|---|---|
| Lossless format-level compaction: 52.9% at 12/12 fidelity | **Plausible, now inside a published envelope.** ONTO (arXiv:2604.17512) reports 46–51% format-level savings with no material degradation; format removal for code ~24.5% (arXiv:2508.13666); lossless compression at 50–80% documented under redundancy/trained-compressor conditions. BUT: single-wave (W2 got 28.6%/12.9%, INCONCLUSIVE), transform list never published, 12/12 carries 95% CI 0.76–1.00 (Wilson), and format is a behavioral variable (Sclar: up to 76-point swings; butterfly effect: a space can flip answers). | Medium — auditable only after the transform spec ships |
| Lossy deletion-based compression: HURT ≤60%, cliff at 40% | **Supported as a task-specific outcome; contradicted as a general law.** Structured/dense text is exactly where published compression fails hardest (Prompt Compression in the Wild: passage counting <20%→<4.5%; "LLMLingua-2 unsuitable for structured synthetic datasets"; LLMLingua-2 NQ 75.7→48.6 at 3.9×). But benchmarks also show moderate compression neutral or helpful (long-context; noisy contexts; LongLLMLingua +17.1%). The pilot's own cliff moved: 40% (W3) → 20–30% (W5) → "no effect 20–40%" (W6) — different rubrics, and amendment-001/002 changed the predicate between W5 and W6. | High for "this doctrine/stack/transform family"; the six-pager's flat "falsified" is the one word to fix |
| "Load-bearing qualifiers/hedges die first" | **Directionally supported; partly a rubric artifact.** Hedges/qualifiers are documented high-sensitivity, functional content (prompt-imperativeness study, d=2.67; CHI 2024; BioScope/hedge-cue pedigree; judges prefer assertive answers 1,276/1,280 — the rubric is a deliberate inversion of the judge default). The rubric requires hedging (Parts 3/5 ≠ 0), so "hedges die first" is partly the rubric's own construction. | Medium — needs the rubric-variation test before it becomes load-bearing |
| Wave-6 17/17 near-ceiling is genuine, proven by controls | **Controls right; interpretation overstates.** 17/17 = 100% at ceiling (Terwee rule: >15% at max is a ceiling effect); kappa undefined at 6/6 (all 3s); rule-of-three: 0/17 failures → ≤17.6% failure rate, i.e. the null is low-power; the B4 anchor drift (P2=3 vs frozen 13/15) is the classic leniency-drift signature *within the run*; judge omission-blindness is published-normal (Reflect <55%; medical judges 2/9; SummEdits near chance). The controls (confab 4/4, deletion 3/4) do rule out wholesale blindness — that is the strong, honest claim. | Defensible wording: "instrument not blind; sensitivity demonstrated on two fault classes; null with low power; leniency drift documented" |

**The single strongest claim the combined evidence supports** (Worker C, exact scope):
> For dense, low-redundancy doctrine prose carried in agent envelopes, mechanically deleting hedge/qualifier/conditional spans at 20–40% reduction degraded rubric-scored fidelity under walled-blind grading (cliff between 20–30%), while format-level compaction achieved 52.9% savings at unchanged fidelity — both for one doctrine, one stack, one transform family, one rubric, small n, LLM graders without a human anchor; the transferable output is the pre-registered, walled, negative-controlled evaluation procedure, not the compression verdict.

---

## PART 2 — Instrument status (what wave 6 actually established)

1. **The mechanism is aligned with or ahead of published practice** — walled-blind grading, planted confabulation controls (the LLM-eval analog of instructional manipulation checks), deletion controls (negative-control logic per Lipsitch 2010), ref-anchors, byte audits, forward-only amendments. Nothing in the record suggests the mechanism is unsound.
2. **The near-ceiling null needs its honest bounds:** min-detectable damage at n=17 is a ~9% per-cell failure rate (80% power); per-part mean shift resolution ≈0.34 scale points (σ=0.5). "No effect" means "no cell failed the gate," not "no sub-threshold degradation."
3. **Cells are not independent:** nested in 4 behaviors, stable-eye graders confound grader with behavior; effective n is between 4 and 17; mechanism claims must be phrased at behavior level (n=4).
4. **Inter-rater 6/6 = 100% raw agreement at ceiling is weak evidence** — chance-corrected (kappa) reporting is the standard; the 6/6 should be reported with that caveat, and the "consistent with wave-5" claim needs the cross-wave comparability caveat (predicate changed between waves).

---

## PART 3 — Record hygiene (must be resolved on the original host, on disk, before sign-off)

| # | Finding | Source | Required action |
|---|---|---|---|
| H1 | **Manifest seal contradiction:** post-O3 re-seal is `6461c201…` (wave-6 finding, four places, full hash, recomputed) vs `44a18890…` (pattern §5b) vs six-pager §2 calling `6461c201` a "consult leg re-derived seal" | Supervisor review | One byte-level recomputation; one of the three docs carries a stale/mislabeled value; the FILE wins |
| H2 | **Grader-identity contradiction:** wave-6 finding §2 says 524s hit a "local-LM grader backend"; pattern §7 says the run used "cloud-backed graders" and lists Qwen3 local endpoints as the replication target | Worker C-iter2 (new) | Resolve from pack-key/dispatch logs/endpoint config; fill `grader-pin.md` or mark UNVERIFIABLE |
| H3 | **W1 control line "caught 0/12 (teeth)" ambiguous** — zero plants/zero false alarms vs twelve plants missed | Workers A, C (all variants) | Clarify in the record |
| H4 | **52.9% transform-unspecified** — the lossless family (what was stripped, token deltas per transform) appears nowhere | Workers A, B, C | Write `transforms/lossless-family.md` from W1 artifacts; a reader must be able to sum to 52.9% |
| H5 | Six-pager W2 row "(per record)"; pattern §6 "four items" lists five; amendment-001 labeled "frozen dock predicate" (that's 002's subject) | Supervisor review | Fill/fix |
| H6 | Cross-wave comparability: amendment-001/002 changed the predicate; "consistent with wave-5" asserted, not demonstrated (W5 has a 30-reserved HURT; W6's 30-reserved cells pass) | Worker A, C | Add the caveat; treat the W3-vs-W6 cliff discrepancy as an open question |
| H7 | Wave-7 ledger line added to MANIFEST at closure — confirm whether the ledger and the sealed answer-pack manifest are the same file (determines whether `6461c201` can still round-trip) | Supervisor review | State file identity in the manifest |

---

## PART 4 — The decisions, with field evidence (consolidated)

| Decision | Posture | Key evidence | Preconditions |
|---|---|---|---|
| **D1 — Lossless adoption** | **GATED ROLLOUT** (not park-forever, not immediate). Production RCT (arXiv:2603.23525) puts ~50% compression on the cost–similarity Pareto frontier (27.9% cost cut); aggressive compression is Pareto-dominated; output-token expansion paradox → net cost, not input savings, is the decision variable | RCT + ONTO + eval-driven-development norms (Anthropic, Langfuse, DeepEval CI gates) | Wave-7 done; per-domain regression suite on envelope-consumer behaviors; byte-exact transform spec; net-cost model; canary + rollback; KEEP FULL PROSE untouched |
| **D2 — Wave-7 instrument repair** | **DO NOW — first.** FORRT: a failed manipulation check caps what that behavior's results can support. Know Thy Judge: judge perturbation-blindness is documented-normal. | B4 control: span the rubric actually penalizes + paired comparison (amputee vs intact) + dry-run until it bites. Anchor: re-verify reference bytes, re-pin as numbered amendment. Add kappa + position-swap consistency | Owner's pen; forward-only amendments; DEL-b4 INCONCLUSIVE stays on record |
| **D3 — Human anchor** | **DO NOW, pre-registered.** Every judge-reliability source converges: calibrate against human gold (MT-Bench bar: >80% agreement, kappa ≥0.70 Landis–Koch). 15–20 real + 3–5 control cells, rubric-only blinding, raw + kappa + PASS/FAIL agreement; control cells mandatory (kappa undefined without spread) | Worker C-iter2 §C3 protocol (ready to execute) | Seal protocol before grades; non-author SME(s); no frozen value changes — on failure, forward-only amendment |
| **D4 — Replication (second application)** | **DO NOW, sequenced after D2/D3.** National Academies: body of evidence; WWC strong form = 5 studies/3 teams/3 institutions; the pattern's "second time" is the honest minimum. Replication effects average ~half original magnitude (Repro Project: Psychology 36%) | Worker B | Pre-committed success criteria (per-cell verdict agreement, control-bite agreement, seal round-trip); different decision domain; own prereg + manifest line |
| **D5 — Local-LM judge port** | **DO NOW, as the replication vehicle, with calibration.** PoLL juries beat single judges (>7× cheaper, less bias); Qwen3-4B thinking-mode is on the right side of the capacity floor (0.6B is not); **the sealed wave packs are a ready-made gold set** — calibrate local judges against frozen verdicts before they grade anything | Worker B | Wave-7 done; calibration gate (kappa against frozen packs); jury ≥3 diverse models; thinking mode; temperature 0; serial dispatch; never re-grade frozen waves |
| **D6 — R5 permanence run** | **PARKED with trigger.** Field norms: n≈969 for δ=0.03 (Miller); 0.10–0.20 rubric deltas need ~100–400 cells/arm; ceiling caps what any n buys. Trigger: permanence becomes load-bearing (adoption beyond canary, external quote, or a wave-7 result to settle) | Worker B | If triggered: reframe as equivalence test, power-justified n, K≥3–5 judge resampling, clustered SEs, own prereg |
| **D7 — Stanford share** | **SHARE WITH CONDITIONS, after D2–D5 prerequisites.** The discipline is ahead of 2026 norms — the B4 over-reporting is the best credibility asset; the pattern is arguably the most complete working implementation of what the 2026 AI-agent preregistration literature asks for (under-claimed). Without the kit it is unverifiable | Workers C (all variants) | Replication kit (C-iter2 §C1 file list); grader pin (C2, resolves H2); human anchor (C3); statistics (C4); related work (C5); OSF/Zenodo registration with honest cover note (C6); compute disclosure (C7); scoped rewording R1–R5 (C8); licensing — fetch-and-verify default, fair-use option, never paraphrase (C9) |

---

## PART 5 — Execution plan (action → artifact → done-when)

**Phase 0 — Disk verification on the original host (blocks everything)**
1. Recompute the wave-6 manifest seal; reconcile `6461c201…` vs `44a18890…` → one-line statement per doc
2. Resolve grader identity per wave (local vs cloud) from pack-key/dispatch logs → `prereg/grader-pin.md` (amendment-003, sealed)
3. Confirm ledger vs answer-pack manifest file identity
4. Extract the W1 lossless transform list (token deltas per transform) → `transforms/lossless-family.md`
5. Fill the six-pager W2 row; fix "four items"/five; relabel amendment-001
→ *Done when: every H1–H7 item has a one-line resolution or an explicit UNVERIFIABLE mark*

**Phase 1 — Instrument and record (all forward-only amendments)**
6. Wave-7: B4 deletion-control redesign + paired-comparison grading + dry-run-bites check; B4 Part-2 anchor re-verification and re-pin
7. Human-anchor protocol: seal → register (OSF) → run → `docs/human-anchor-validation.md`
8. Statistics additions to pattern §5/§6 (Wilson CIs, min-detectable-damage table, clustering paragraph, kappa note)
9. Scoped rewording R1–R5 (six-pager + pattern); related-work paragraphs (C-iter2 §C5)
→ *Done when: wave-7 lands with controls biting; anchor report exists; no unqualified "falsified"/"proves"/"is safe" remains*

**Phase 2 — The shareable package**
10. Build the replication kit per C-iter2 §C1 (10 files, layout, SHA256SUMS, build_release.sh, README with claim-to-file map)
11. OSF registration (frozen contracts + cover note + filled 2026 template) + Zenodo DOI for the zip
12. Licensing: `LICENSE.md` + `NOTICE-THIRD-PARTY.md` + `fetch_doctrine.py` (Option 1 default)
13. Compute disclosure from `state.db` token logs → `docs/compute.md`
→ *Done when: kit dry-runs clean on a fresh machine; DOIs resolve; a Stanford reviewer can verify every headline number from the artifact alone*

**Phase 3 — Replication and adoption (after 1–2)**
14. Local-LM port: calibrate Qwen3-4B/8B (thinking, jury) against sealed packs → calibration gate passes
15. Second application on a different decision, pre-committed criteria → pattern becomes "proven" (minimum bar)
16. Lossless adoption: per-domain regression suite → canary → net-cost monitoring → promote with rollback
17. R5: only on trigger; reframed as equivalence test
→ *Done when: verdicts replicate; adoption ships behind a green regression gate; R5 has a written decision rule*

---

## PART 6 — What remains UNVERIFIABLE from pve-1

All on-disk artifacts on the original host: seal recomputations, deletion logs, byte audits (25/25), lottery reproducibility, `state.db` token logs, grader backend configuration, the W1 transform artifacts, the ledger. Nothing in this assessment asserts those as verified; every plan item that depends on them is explicitly gated on Phase 0.

---

## Source index (worker reports, this host)

- `/root/workspace/walled-blind-pilot/worker-A-verification-v2.md` (harness) and `worker-A-verification.md` (search)
- `/root/workspace/walled-blind-pilot/worker-B-decisions-v2.md` (harness) and `worker-B-decisions.md` (search)
- `/root/workspace/walled-blind-pilot/worker-C-readiness-v2.md` (harness), `worker-C-readiness.md` (search), `worker-C-iteration2.md` (executable package — the operative artifact for the share)
- Key external anchors: arXiv:2603.23525 (production RCT), arXiv:2604.17512 (ONTO), arXiv:2604.02985 (compression in the wild), arXiv:2505.00019 (empirical study), arXiv:2306.05685 (MT-Bench judges), arXiv:2606.11217 (2026 agent prereg), arXiv:2603.05399 (RAND judge harness), arXiv:2411.00640 (Miller power), arXiv:2503.04474 (Know Thy Judge), arXiv:2509.13332 (Qwen3 judges), arXiv:2404.18796 (PoLL), NeurIPS checklist, ACM badging, 17 U.S.C. §107
