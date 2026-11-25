# Worker C — Fresh-Eyes Review: Walled-Blind Compression Evaluation (Waves 1–6)

**Deliverable:** skeptical first-reader review of three documents, updated against online research into 2026 evaluation-reporting standards and the prompt-compression literature. Prepared 2026-08-19. English, flat neutral tone.

**Materials reviewed in full:**
1. `loop-closure-six-pager-DRAFT.md` (142 lines) — close-out narrative ("six-pager")
2. `hermes-replicable-pattern.md` (346 lines) — the abstracted pattern, primary artifact ("pattern doc")
3. `wave6-grading-finding.md` (183 lines) — sealed evidence ("finding")

**Evidence conventions.** `[DOC]` = grounded in the three documents (quotes with section references). `[ONLINE]` = grounded in cited web sources (URL in the evidence index, §6). `[UNVERIFIABLE]` = asserted in the documents but not checkable from the documents or cited sources (the underlying repo, prereg files, manifests, scripts, and grader packs were not accessible to this reviewer). No other machine was accessed.

---

## 1. What the three documents claim

The six-pager is a decision memo: waves 1–6 of a pre-registered, walled-blind evaluation of prompt-envelope compression for Amazon Leadership Principles doctrine in a sub-agent delegation stack, concluding (a) lossless format-level compaction achieved 52.9% token savings at 12/12 fidelity (W1) and is "a real stack candidate," and (b) lossy/semantic compaction "is falsified for this doctrine and stack" — HURT at ≤60% retention, cliff at 40%, standing rule KEEP FULL PROSE (six-pager §3).

The pattern doc abstracts the mechanism — pre-registration with forward-only amendments, sealed lottery, deterministic mechanical generation, walled grading, teeth gates, deletion audit, locked decision rules, inter-rater discipline, consult loop, verify-on-disk — as a reusable discipline "written for replication: the Stanford knowledge-lab share and any future wave" (pattern doc header). It explicitly disclaims that the compression experiment succeeded: "The experiment's verdict was NO ADOPTION — KEEP FULL PROSE. The pattern is the deliverable" (pattern doc header).

The finding is the wave-6 record: 17/17 real cells PASS near-ceiling, confabulation controls 4/4 bit, deletion controls 3/4 bit (b4 INCONCLUSIVE — the B4 deletion gate is blind), inter-rater 6/6 HIGH, manifest seal round-trips, B4 Part-2 anchor drift reported loudly and not patched.

The claim architecture has three layers that must be evaluated separately: (i) instrument claims (the grading apparatus works and can fail), (ii) results claims (compression effects on doctrine fidelity), (iii) pattern claims (the discipline transfers to other decisions). Most of the review's findings live in the seams between these layers.

---

## 2. Part 1 — Fresh-eyes review

### 2.1 What a skeptic challenges first, and whether the docs answer it

**C1. The measurement instrument is not identified.** The walled-blind design protects graders from label leakage; it does not identify the graders. Nowhere in the three documents is the grader model/version/sampling configuration for W1–W6 stated. `[DOC]` The pattern doc names only the replication target ("Qwen3-4B @ :8080, Qwen3-8B as the replacement driver," §7) and identifies one consult lens as Qwen3-4B (§5b); the finding's infrastructure note mentions a "local-LM grader backend" without naming it (finding §2). The B4 anchor drift (P2=3 vs frozen 13/15) is itself evidence that grader leniency drifts across waves, so grader identity is not a formality. **Not answerable from the docs.** A 2026 reviewer treats model identification as a reproducibility requirement (see §3.1).

**C2. "No movement" at 20–40% in W6 vs. HURT at 30% in W5 — not reconciled.** `[DOC]` Pattern doc §5: W5 "30-reserved HURT on Part 2 (branch truncation)." Finding §1: wave-6 "compression at 20% → 30% → 40% produces no PASS↔FAIL movement and no sub-threshold base anywhere — essentially no effect, consistent with wave-5"; b2-30-reserved graded 15/15 Δ0. Either W5's HURT was a decision-rule category on a rubric-passing cell (possible under P7 — a cell can PASS the rubric and still be HURT, as b2-40-reserved at 12/15 illustrates), or the same 30% point moved from HURT to clean PASS between waves. The docs never state which, and the "consistent with wave-5" reading is asserted, not demonstrated. **Partially answerable** only by the W5 grading file, which is not attached. This is the single most load-bearing unresolved discrepancy.

**C3. The pre-committed HURT predicate is not applied to W6 real cells.** `[DOC]` P7 defines HURT, inter alia, as "Part 1/2 drops > 0.20" (pattern doc §7). Finding §3 tables show b6-20-unreserved P2=1 against an anchor of 3 (−2 on a 0–3 scale, ≈ −0.67) and b2-40-reserved with P2/P3/P5 all −1 (−0.33). Yet the finding's aggregate posture is "compression does not materially degrade content integrity on this batch at the measured points" (finding §8), and the decision table in finding §4 is applied only to DEL controls, never to real cells. Either the 0.20 threshold's unit is not the part scale (the unit is undefined anywhere in the docs), or real cells are exempt from the HURT rule (also unstated). Under the plainest reading, wave-6's own real-cell deviations would be HURT findings, which would contradict the "no effect" headline. A skeptic reads this as the locked rule not being invoked where it would bite. **Not answerable from the docs** — requires the frozen rulebook text and `apply_rulebook.py`, neither attached.

**C4. W1's teeth evidence is ambiguous to the point of contradiction.** `[DOC]` Six-pager §3: "positive control caught 0/12 (teeth)." Pattern doc §5: "control caught 0/12 (teeth: the instrument CAN fail)." Under P5's own definitions, a positive control that does not bite (base ≥ 10) makes a point INCONCLUSIVE ("indistinguishable at the ceiling") — yet W1 is declared PASS/GENUINE. Two readings are possible: (a) 0 confabulations were caught across 12 cells, meaning the planted controls were missed and W1's teeth evidence failed; (b) the phrase means the 12 cells contained no confabulation and a separate control batch fired. Reading (a) contradicts P5; reading (b) is unsupported by the text. Either way the W1 validity line needs one sentence of clarification before sharing. **Not answerable from the docs.**

**C5. Arithmetic check fails.** `[DOC]` Pattern doc §5: "confab controls 7/7 across the last two waves." The same document records W5 "controls caught 4/4" and W6 "Confab controls 4/4 bit" — 4 + 4 = 8. Trivial, but it is exactly the kind of number a first reader re-checks, and it fails.

**C6. Sample structure: point estimates without variance.** `[DOC]` Each cell is one variant, one generation, one grader (inter-rater covers 6 of 25 cells, Part 5 only, per finding §2 and limitation e). "No effect" claims rest on ≈4 cells per compression point per wave, with near-ceiling scores. The docs acknowledge small n and explicitly disclaim permanence (six-pager §6: "Near-ceiling scores at this n are consistent with a real finding, but not with a permanence claim") — credit — but no sampling budget, no repeated generations, no statistical treatment is anywhere described. The ceiling problem is partially handled by the teeth gate; the fact that the instrument caught 3/4 amputees in W6 shows it can fail, which is the best evidence in the record that the ceiling is not total blindness.

**C7. The auditor is the audited.** `[DOC]` P6 is titled "Deletion audit (supervisor only)": the entity that draws the lottery, holds the seals, and ships the packs also audits itself byte-level. The wall protects graders from the treatment; nothing protects the supervisor's own steps except seal round-trips and the advisory consult lenses. The docs' honest answer is partial: seals prove non-mutation, consult legs proved useful (SharpSME's amendment-002 predates any grade), but a skeptic still asks who checks the checker, and the answer is "the same supervisor, assisted." This is a trust-model statement the shareable doc should make explicit rather than implicit.

### 2.2 What a rigorous outsider requires that is missing

Judged against current reporting expectations (full literature in §3.1), the shareable artifact lacks:

1. **Artifact availability.** The prereg + amendments, rubric full text, doctrine file, reference answers, cell packs, lottery briefs, and scripts (`apply_rulebook.py`, `audit_cellcheck.py`, `fill_manifest.py` are named but not shipped) are all referenced by name only. A reader cannot re-run or re-derive anything from the three files alone. `[DOC]` None of the three documents admits this.
2. **Grader-model identification.** No model names, versions, temperatures, or sampling parameters for the W1–W6 grading legs. `[UNVERIFIABLE]`
3. **Baseline definitions.** "Fidelity 12/12" is never defined (rubric base is 12, PASS = base ≥ 9; what exactly 12/12 denotes is left implicit). The reference answer itself is graded 12/15 in W6 and 13/15 in the frozen W5 datum — the "reference" moves between graders, which is precisely why the B4 drift matters. W2's "flat hedge baseline" (pattern doc §5) is unexplained.
4. **Cost accounting.** No token, compute, wall-clock, or dollar figures for any wave. The six-pager's "the cost of using it again is one prereg + one consult batch" (§4) is a process estimate, not a cost accounting. NeurIPS checklist-style compute disclosure is table stakes in 2026.
5. **Failure-mode escalation rules.** The anti-patterns list (pattern doc §8) is genuinely good and unusual — but there is no stated procedure for what happens when a teeth gate fails at batch level (W1's ambiguous control would be the test case) or when a decision-rule category and a rubric category conflict on a real cell (C3).
6. **Generality limits, quantified.** One doctrine, one stack, one grader pool, cloud-backed graders with the local port explicitly untested ("The claim to test on the new rig: the pattern's results replicate … regardless of which model sits in the supervisor seat," pattern doc §7 — correctly framed as a hypothesis, not a result). Nothing about transfer across doctrine types (e.g., legal, safety, style) or envelope sizes.

What is **not** missing (credit where due): pre-registration with forward-only amendments; sealed lottery never re-drawn; positive and negative controls in every batch with pre-committed thresholds; inter-rater with a locked 80% bar; byte-level deletion audit with a documented writer-violation catch (W5 b4-30 reword); dissents preserved verbatim; a limitations section that names its own blind spots (B4 deletion gate, anchor drift); and explicit non-claims ("no adoption claim, no permanence claim, no generalizability claim," six-pager §6). By the categories of the ReproEvalCard audit (see §3.1), this record is ahead of most published LLM-pipeline papers on randomness control and trace discipline — as far as the three documents attest.

### 2.3 The strongest claim the record supports

> On one doctrine (Amazon Leadership Principles), one orchestration stack, and the specific grader instrument used across waves 1–6, mechanically-generated deletion-based lossy compression of the doctrine envelope at 40–60% retention produced detectable, named damage in blind grading — loss of load-bearing qualifiers and hedge/reversibility behavior, the parts of the doctrine that carry its force — while a single 12-cell batch of lossless format-level compaction showed no fidelity loss at 52.9% token savings. The standing no-adoption posture (KEEP FULL PROSE) is therefore justified for this doctrine/stack pair, and the instrument demonstrated it can fail where damage exists (confab controls 4/4, deletion controls 3/4 in W6).

Every element of that sentence is `[DOC]`-grounded (six-pager §3, finding §§1/4/8, pattern doc §5). It claims exactly the scope the evidence supports: one doctrine, one stack, one instrument, one transform family, small n, near-ceiling — and it makes no claim about other doctrines, other compressors, other graders, or permanence.

### 2.4 Where the documents overstate and understate

**Overstatement.**
- "Lossy/semantic compaction **is falsified** for this doctrine and stack" (six-pager §3). "Falsified" exceeds what a near-ceiling, n≈4-per-point, one-transform-family, one-instrument result can support, even scoped to doctrine and stack — especially while the B4 deletion control is acknowledged blind and the B4 anchor is acknowledged drifted. The pattern doc's softer framing ("NO ADOPTION — KEEP FULL PROSE") is the right register.
- "a reusable pattern for **any** local-LM orchestration decision" (six-pager §4 headline) — immediately self-corrected one paragraph later ("one data point … Generalizability is *unproven*"), so the overreach is acknowledged in the same document, but the headline invites the challenge.
- The standing rule "KEEP FULL PROSE for lossy paths" (six-pager §3, pattern doc §5) is stated unconditionally while only deletion-based lossy compression was tested. Section 3.2 shows the literature's fidelity-preserving lossy methods were not sampled; the rule should be scoped to "lossy compression by deletion, as tested."
- "The instrument's track record: … confab controls 7/7 across the last two waves" (pattern doc §5) — arithmetic, see C5.

**Understatement.**
- The W5→W6 30%-point discrepancy (C2) is not surfaced anywhere; the docs call W6 "consistent with wave-5" without discussing the one point that moved.
- The non-application of the P7 HURT rule to real cells (C3) is not surfaced; the "honest extent of compression movement" paragraph (finding §3) lists the deviations without classifying them under the locked rules.
- The B4 anchor drift is reported loudly (credit) — but its consequence is confined to a caveat: every B4 "PRESERVED" cell in the wave-6 tables is graded under a more lenient Part-2 standard, so the headline "17/17 PASS" includes four B4 cells whose scale differs from the frozen baseline. The finding's §5.4 does state this; the six-pager's summary table does not.
- No document states that external reproduction is currently impossible from the shared materials alone.

### 2.5 Would I sign off on sharing the pattern doc — as-is?

**No, as-is; yes, conditionally.** The pattern doc is the strongest of the three documents — its discipline is real, its limitations are candid, and its core posture (the pattern is the deliverable, not the verdict) is the correct one for external sharing. But as a first reader I would not yet hand it to a Stanford knowledge-lab, because the lab's first five minutes would reproduce C1–C5 (grader identity absent, HURT rule unapplied, W1 teeth ambiguity, arithmetic, W5/W6 tension), and the credibility cost of those five minutes exceeds the cost of fixing them. Conditions in §5.

---

## 3. Part 2 — Online research, folded in

### 3.1 What a 2026 reviewer expects of an evaluation write-up (table stakes)

- **NeurIPS checklist (mandatory, desk-reject without it).** Reproducibility avenue required for every contribution; code/data/instructions with exact commands; hyperparameter disclosure; compute disclosure ("type of compute … amount of compute required for each of the individual experimental runs as well as estimate the total compute"); asset documentation with license and limitations. NeurIPS 2026 formatting instructions are already published. `[ONLINE: neurips.cc/public/guides/PaperChecklist; media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip]`
- **ReproEvalCard (ACL 2026, short paper).** A reporting standard for reproducible evaluation of LLM pipelines, motivated by an audit of 55 pipeline papers (2022–2025): **75% missing randomness controls, 61% missing intermediate execution traces, 37% missing evaluation prompts**. `[ONLINE: aclanthology.org/2026.acl-short.22.pdf]`
- **Empirical reproducibility audits.** A 2025 study of 85 LLM-centric software-engineering papers: only 29 reported temperature, 14 reported other sampling parameters, 50 reported prompts; failed reproductions traced to missing scripts, non-executable artifacts, and deprecated API endpoints. `[ONLINE: arxiv.org/html/2510.25506v2]`
- **Domain reporting standards.** MI-CLEAR-LLM (2025 update) defines minimum reporting items for LLM accuracy evaluations in healthcare, with model identification called "essential for reproducibility." `[ONLINE: pmc.ncbi.nlm.nih.gov/articles/PMC12683746/]` The living "LLM Guidelines" similarly require limitations sections covering non-determinism and generalizability. `[ONLINE: llm-guidelines.org/guidelines/limitations/]`
- **Agent-specific norms.** ICML 2026 runs a workshop on "Failure Modes in Agentic AI: Reproducible Triggers, Trace …" — trace-based reproducibility for agent loops is the emerging norm. MLR-Bench (NeurIPS 2025) found coding agents produce fabricated or invalidated experimental results in ~80% of cases — which is the strongest argument *for* the sealed-audit-trail style this project practices. `[ONLINE: icml.cc/virtual/2026/workshop/54094; neurips.cc/virtual/2025/poster/121719]`

**Map to the documents.** Against these expectations, the docs are *ahead of the field* on randomness control (seeded lottery, sealed, never re-drawn; per-grader answer shuffling with recorded seeds), trace discipline (deletion logs, byte-subsequence audit, manifest seals with recomputed SHA-256), and pre-committed decision rules — precisely the categories the ReproEvalCard audit finds missing in most published work. They *fail* the field's expectations on: grader-model identification (absent — worse than the 29/85 temperature-reporting rate, which is itself a failing bar), artifact availability (referenced, not shipped), full prompt/rubric text in the shareable artifact (rubric described, not included), and cost/compute disclosure (absent). A one-page checklist mapping the pattern to these categories would be the cheapest credibility upgrade available.

### 3.2 Does the compression literature support "KEEP FULL PROSE — lossy hurts"?

The literature has two branches, and the experiment sits cleanly inside one of them:

**Optimistic branch (compression can preserve performance).** LLMLingua (EMNLP 2023) reports maintained reasoning/summarization/dialogue capability at up to 20× compression on GSM8K/BBH/ShareGPT/Arxiv. `[ONLINE: microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/]` LLMLingua-2 (ACL 2024 Findings) formulates compression as token classification "to guarantee the faithfulness of the compressed prompt to the original one." `[ONLINE: llmlingua.com/llmlingua2.html]` RECOMP (ICLR 2024) trains extractive/abstractive compressors for RAG and reports compression down to ~6% with minimal loss, transferring across LMs. `[ONLINE: arxiv.org/abs/2310.04408]` "Prompt Compression in the Wild" (arXiv, April 2026 — 30,000 runs, five open models, three GPU classes) finds quality "statistically unchanged" on summarization/code/QA *within a matched operating window*, with up to 18% end-to-end speedup and 75% memory reduction; outside that window the compression overhead cancels the gains. `[ONLINE: arxiv.org/html/2604.02985v1]`

**Cautionary branch (lossy compression degrades, sometimes invisibly).** Nagle et al. (NeurIPS 2024) formalize a rate-distortion limit: lossy prompt compression has a fundamental rate-distortion trade-off for black-box LMs — information needed for the query can be lost at low rates, changing outputs. `[ONLINE: arxiv.org/abs/2407.15504]` An ICLR 2025 empirical study of six compression methods across 13 datasets finds compression "has a greater impact on LLM performance in long contexts compared to short ones." `[ONLINE: iclr.cc/virtual/2025/33335]` Most pointedly for this project, the April 2026 in-the-wild study reports that on code tasks "significant drops in edit similarity suggest that even slight compression harms model outputs" while surface metrics look fine — i.e., *subtle damage invisible to coarse metrics is the field's own documented failure mode*, exactly the failure mode this experiment's walled-blind grading was built to expose. `[ONLINE: arxiv.org/html/2604.02985v1, §4.3]` And for the W1 lossless/format-level claim: "Does Prompt Formatting Have Any Impact on LLM Performance?" finds formatting sensitivity is a general model characteristic across domains and skills, and Lost in the Middle (TACL 2024) shows position changes degrade long-context performance — so format-level changes are *not* trivially safe, and W1's 12/12 fidelity is a genuine empirical result, not a tautology. `[ONLINE: arxiv.org/html/2411.10541v1; arxiv.org/abs/2307.03172]`

**Alignment verdict.** The experiment's negative result aligns with the cautionary branch and is fully consistent with the field's method- and task-dependence. What it does **not** do is falsify lossy compression in general: the optimistic branch's methods (perplexity/token-classifier pruning, task-trained extractive/abstractive compressors, summarization) were never tested — the experiment sampled exactly one family, deterministic span deletion (T1–T7), against exactly one doctrine. The docs' unconditional "KEEP FULL PROSE for lossy paths" and the six-pager's "falsified for this doctrine and stack" both outrun the tested transform family; the defensible statement is "deletion-based lossy compression, as implemented here, hurts this doctrine at ≤60% retention; fidelity-preserving compression methods were not evaluated." That scoped statement also happens to be the one the evidence supports, so the correction costs nothing. Conversely, the experiment's methodological contribution — that blind grading surfaces damage coarse fidelity metrics miss — is directly corroborated by the wild study's edit-similarity finding, which strengthens the case for sharing the *pattern* even while the *verdict* is scoped down.

### 3.3 What credible sharing to a knowledge-lab looks like in 2026

Credible external methodology-sharing, per current practice, has three components the docs partially or fully lack:

1. **Runnable artifacts.** RECOMP, as a typical example, ships code, data, prompts, and model weights with commands (`[ONLINE: github.com/carriex/recomp]`); security-venue Artifact Evaluation awards reproducibility badges only for code + datasets + documentation with setup and execution instructions (`[ONLINE: arxiv.org/html/2603.06862v1, §II-A]`). The pattern doc names its scripts but ships none.
2. **Structured self-disclosure.** A checklist- or card-style document (NeurIPS checklist, ReproEvalCard, model/data cards, MI-CLEAR-LLM) that a stranger can check off. The pattern doc's ten pillars are a better *method*, but they are not a *disclosure format* — the missing items in §2.2 are exactly what the checklist formats force out.
3. **Auditable negative results.** MLR-Bench's ~80% fabrication rate for agent-produced experimental results (`[ONLINE: neurips.cc/virtual/2025/poster/121719]`) makes pre-registered, sealed, honest-negative work scarce and valuable. The pattern doc's willingness to ship a "NO ADOPTION — KEEP FULL PROSE" verdict with preserved dissents and named limitations is, by current community standards, the most credible thing in the package — provided the unresolved flags (C1–C5) are closed first.

---

## 4. Consolidated verdict and conditions

**Verdict: do not share as-is; share after closure of the items below.** The pattern is real and the honest-negative posture is exemplary; the package is not yet externally reproducible, and its internal inconsistencies (W5/W6 tension, unapplied HURT rule, W1 teeth ambiguity, 7/7-vs-8/8) would each generate a challenge in the first reading.

**Required before sharing (blocking):**
1. Attach the artifact bundle: prereg + amendments, full rubric, doctrine file, reference answers, cell packs, lottery briefs, deletion logs, `apply_rulebook.py`/`audit_cellcheck.py`/`fill_manifest.py`, with a README containing exact run commands and environment pins (mirrors NeurIPS checklist item 4 / ReproEvalCard).
2. Pin the grading instrument: model names, versions, temperature/sampling parameters for every W1–W6 leg; state the tokenizer pin already exists (tiktoken cl100k_base v0.14.0) and extend the same discipline to models.
3. Define the HURT threshold unit and state explicitly whether real-cell deviations are classified under P7; if b6-20-unreserved (P2 3→1) and b2-40-reserved (P2/P3/P5 −1) are not HURT under the frozen rule, say why, in the rulebook's terms.
4. Reconcile W5's "30-reserved HURT" with W6's clean 30% cells, or state the discrepancy as a limitation (it currently reads as either a contradiction or an unacknowledged rubric/grader change between waves).
5. Resolve the W1 control line ("caught 0/12" vs. P5's teeth definitions) in one sentence.
6. Add a cost/compute section (tokens, time, cost per wave and total) and fix the 7/7-vs-8/8 arithmetic.

**Recommended before sharing (non-blocking but cheap):**
7. Scope the standing rule to "deletion-based lossy compression as tested"; add one sentence noting fidelity-preserving compressors (LLMLingua-2-style, RECOMP-style) were not evaluated.
8. Add a one-page 2026-style reproducibility checklist (§3.1) mapping the pattern to NeurIPS-checklist/ReproEvalCard categories.
9. State the trust model explicitly: the supervisor audits itself; external verification currently rests on seals plus consult lenses.
10. Include the wave-6 B4 caveat in any summary table (the six-pager's table omits it).

**The single strongest claim, at exactly the right scope** (from §2.3): deletion-based lossy compression of Amazon Leadership Principles doctrine at 40–60% retention produces named, blind-graded damage to doctrine-faithful output on this stack, while one lossless format-compaction batch showed no loss at 52.9% savings; KEEP FULL PROSE is justified for this doctrine/stack pair; the instrument can fail and was seen failing. That claim survives every challenge above, and it is worth sharing.

---

## 5. Evidence index

**Documents reviewed (DOC):**
- `/root/.hermes/webui/attachments/eee3a9a516db/loop-closure-six-pager-DRAFT.md`
- `/root/.hermes/webui/attachments/eee3a9a516db/hermes-replicable-pattern.md`
- `/root/.hermes/webui/attachments/eee3a9a516db/wave6-grading-finding.md`

**Online sources (ONLINE):**
- NeurIPS Paper Checklist Guidelines — https://neurips.cc/public/guides/PaperChecklist
- NeurIPS 2026 formatting instructions (checklist required) — https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip
- ReproEvalCard (ACL 2026) — https://aclanthology.org/2026.acl-short.22.pdf
- MI-CLEAR-LLM 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12683746/
- LLM Guidelines, limitations — https://llm-guidelines.org/guidelines/limitations/
- Reflections on Reproducibility of Commercial LLM Performance in SE Studies — https://arxiv.org/html/2510.25506v2
- ICML 2026 Workshop: Failure Modes in Agentic AI — https://icml.cc/virtual/2026/workshop/54094
- MLR-Bench (NeurIPS 2025) — https://neurips.cc/virtual/2025/poster/121719
- Prompt Compression in the Wild (arXiv:2604.02985, Apr 2026) — https://arxiv.org/html/2604.02985v1
- LLMLingua (Microsoft Research blog, EMNLP 2023) — https://www.microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/
- LLMLingua-2 (ACL 2024 Findings) — https://llmlingua.com/llmlingua2.html
- RECOMP (ICLR 2024) — https://arxiv.org/abs/2310.04408 ; code: https://github.com/carriex/recomp
- Fundamental Limits of Prompt Compression (NeurIPS 2024) — https://arxiv.org/abs/2407.15504
- An Empirical Study on Prompt Compression for LLMs (ICLR 2025 workshop) — https://iclr.cc/virtual/2025/33335
- Does Prompt Formatting Have Any Impact on LLM Performance? — https://arxiv.org/html/2411.10541v1
- Lost in the Middle (TACL 2024) — https://arxiv.org/abs/2307.03172
- Supporting Artifact Evaluation with LLMs — https://arxiv.org/html/2603.06862v1

**Not cited:** the "Losing Faith in Faithfulness" summarization-shortening paper could not be located via search in this session; claims about summarization-shortening fidelity are therefore grounded only in the verified sources above, not in that title.
