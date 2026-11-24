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
