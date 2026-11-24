# Deep-Assessment Research Plan — the "News Is Missing You" compilation

**Plan owner:** worker-A (Deep-Review Plan Architect)
**Status:** PLANNING ONLY. **No network activity was performed to produce this plan.** Every planning decision below is grounded in three local files:
- `source-part1.md` — 2026-08-23 original compile: 14 items (#1–#14), cross-cutting synthesis, astrobiology appendix, primary-sources note.
- `source-part2.md` — 2026-08-27 Part 2 sweep: 8 new stories (A1–A8), update checks on items #1–#14, Section C (Hermes/AI news, incl. item #14 update).
- `source-medium-article.md` — G.W. Brown, "The News Is Missing You" (the published essay this review will eventually feed).

**Registry notation used throughout:** `P1-#n` = Part 1 items #1–#14; `P2-A#` = Part 2 new stories A1–A8; `P2-B#n`/`P2-C` = Part 2 update notes and Section C; `AO-#` = claims that appear **only** in the Medium article (they trace to the 2026-08-21 compile, which is **not present in the workspace** and carries no verification record in these files).

---

## 1. OBJECTIVES of the deep review

The deep-review team should accomplish exactly four things. Each is testable.

**O1 — Re-verify every carried claim against primary sources, end to end.**
Re-read (or, for AO-items, obtain and read) the primary source behind every figure, confidence level, and "what would change it" field in all 22 compile items (P1-1–14, P2-A1–8) and every article-only claim (AO). Done when: a claim-level registry exists in which each fact maps to a named primary source, an access date, and a pass/fail status, and **no** High-confidence claim is resting on a secondary summary. Test: every registry row has a status in {verified, revised, retracted, unverifiable}.

**O2 — Reconcile the three documents into one consistent fact base.**
Resolve the internal inconsistencies already visible across the files (listed in §7.2) and reconcile the Medium article — which cites the 2026-08-21 compile ("25 analyst-grade stories") — against the two compilations in hand. Done when: a single diffed registry exists showing where Part 1, Part 2, and the article agree, diverge, or cite different sources for the same claim. Test: zero unresolved cross-document discrepancies in the registry.

**O3 — Test the five candidate "bigger stories" (§2) as falsifiable hypotheses, not assertions.**
For each candidate, assemble a written evidence brief containing (a) supporting items, (b) the strongest contradicting/alternative reading, and (c) a provisional verdict: **supported / plausible / not supported / coincidence-not-structure**. Done when: all five briefs exist with explicit negative-case sections. Test: each brief can be read independently and says what evidence would overturn its verdict.

**O4 — Produce a publication-ready article brief for the next Medium essay.**
Output = article brief (structure, which bigger stories carry, which items anchor them, confidence tags per carried claim, alternatives section) + a fact-check appendix (every claim carried into the essay with its source and status) + a kill-list of items that failed verification. Done when: the brief is written and passes a human gate (§5, Gate 3). Test: every paragraph of the draft essay maps to a registry row.

A fifth, guardrail objective: **O5 — Never exceed the approved research footprint.** All networked work happens only inside an explicitly approved Footprint Declaration per phase (§6). Test: the search/visit log matches the approved footprint with zero exceptions.

---

## 2. THE CANDIDATE BIGGER STORIES

These five hypotheses are drawn from both compilations and the article. Item numbers are the evidence base. Each is a **Medium-confidence inference at planning time** (individual items are mostly High; the *connection* between them is not yet established — that is what Phase 2 tests).

### BS-1. The verification-layer collapse: the cost of the trust economy is invisible until it is totaled
**Evidence items:** P1-1 (NK laptop farm), P1-2 (trust economy / 7× insider surge), P1-7 (seafood fraud ~1-in-5), P1-8 (forced labor in mineral chains), P1-12 (420 recalls / 40M items), P2-A1 (jalapeño outbreak), P2-A2 (sprouts dual-pathogen), P2-A7 (Boston Scientific / healthcare cyber wave), plus AO-1 (cyclospora), AO-2 (OT/PLC water lockouts), AO-3 (seven injectable-drug particulate recalls), AO-4 (fishing-vessel forced labor), AO-5 (prison labor), AO-6 (dental insurer breach + 252 hacking/IT breaches).
**Connecting thesis (from the Part 1 synthesis):** the weak point of the systems running modern life is no longer the machine but the human/institutional layer that verifies, secures, and allocates — hiring verification (P1-1, P1-2), food labeling and import verification (P1-7, P2-A1, P2-A2, AO-1), product-safety verification (P1-12, AO-3), labor verification (P1-8, AO-4, AO-5), access control (AO-2), health-sector integrity (P2-A7, AO-6). All reduce to: **a legitimate actor with a legitimate credential or a legitimate label is now the failure mode.**
**NOT yet established:** (a) a shared causal root vs. coincidental clustering — the article itself flags the seven-recall cluster as "coincidental clustering, or a systemic manufacturing and QC failure… not yet established"; (b) attribution of the OT/PLC attacks (financial vs. state-sponsored; FBI has not attributed — per the article); (c) any quantifiable common driver (consolidated manufacturing, inspection cuts, cost pressure, import-verification gaps) across the food/device/drug clusters; (d) whether the Sinaloa-based food outbreaks (P2-A1, AO-1) share an import-verification failure mode with the seafood-fraud item (P1-7).
**Open questions:** Is there a measurable single mechanism (e.g., verification/audit under-investment, "safety was de-funded") or is the compile's "same broken-verification shape" a rhetorical device? Which of these failures would survive a primary-source re-read that strips the framing?

### BS-2. The resource squeeze: one minerals base, one buildout, five fronts
**Evidence items:** P1-3 (AI power + water walls), P1-4 (China critical-mineral stranglehold), P1-8 (forced labor inside mineral chains), AO-7 (first U.S. deep-seabed mining permit, TMC USA), AO-8 (24 new CCZ amphipod species in the mining zone), AO-9 (DAC vs. renewables cost-equivalence), AO-11 (ice-core library as climate-record banking), and P1-9 (dams/water infrastructure) as the domestic water side.
**Connecting thesis:** the AI + energy-transition buildout runs on a critical-minerals base that is (a) geographically concentrated in one country's refining capacity (P1-4), (b) partly coerced labor (P1-8), (c) now being pursued in a new frontier — the deep seabed — in the same zone where new families of life are still being discovered (AO-7 + AO-8, the article's flagship "two stories that never appear together"), all while the buildout hits grid power, water, and (now) regulatory walls at home (P1-3, plus the P2-B update: Spain 8/25, PA 8/18, TX 8/4, NY 7/14, Monterey Park Jun — the power/water wall becoming a *regulatory* wall).
**NOT yet established:** (a) whether coerced-labor minerals demonstrably enter Western AI/data-center/defense supply chains — the compile relies on the DOL ILAB list and the Part 2 UFLPA note (43 companies incl. five Xinjiang aluminum producers, Jul 31 2026), but company-level sourcing disclosures are absent; (b) whether seabed mining *substitutes for* or *supplements* the Chinese refining chokepoint — the article's own claim; (c) whether the "two stories never printed together" (mining vs. biodiversity) is a coverage gap that can be demonstrated, not just asserted; (d) the actual allocation decision data behind "who gets the water and power."
**Open questions:** Does TMC USA's legal strategy (NOAA "full compliance" ruling; Canada/UNCLOS exposure) hold? Does the forced-labor→minerals→buildout chain survive company-level evidence or stay at the "two stories never run together" level?

### BS-3. The no-photograph problem: the news misses what cannot be photographed or counted
**Evidence items:** P1-5 (water "bankruptcy" framing shift), P1-9 ($165B dam bill, 92,000 dams), P1-6 (population-scale adolescent harm), P1-12 (recalls as one pattern), P1-13 (90% AI-paper signal), P2-A3 (shingles/dementia under-scoped), P2-A4 (depression neurogenesis mechanism), plus AO-3 (seven recalls as pattern), AO-11 (ice-core library "not an emergency"), AO-12 (JWST Quintet), AO-15 (doubly charmed baryons — "prediction confirmed after 60 years"), AO-16 (Migdal effect — "a door, not a result"), AO-20 (Aquiry civilization).
**Connecting thesis (the meta-thesis the essay rests on):** each of these is a slow, distributed, no-single-photograph problem; the news is "single-story, brand-shaped, image-driven, allergic to counting, allergic to framing shifts"; "you cannot see bankruptcy in a rain gauge."
**NOT yet established — and this is the load-bearing weakness:** the thesis is a claim *about the news*, and neither compilation contains any measurement of media coverage. It is asserted, not tested. The deep team must not treat the meta-thesis as established; it needs a countable content-analysis method (outlet × item × frame × volume) before it can be called evidence.
**Open questions:** Is "the news misses X" falsifiable, and what would falsify it (a counter-example where a no-photograph problem *was* covered, at scale)? Is the pattern an artifact of the analyst's own sampling — stories were selected *because* they fit the frame (selection bias)? What is the baseline coverage of, say, FAO Technical Paper 742, the UNU-INWEH report, or the ASDSO dam data, measured, not guessed?

### BS-4. AI in three roles at once: attacker, remedy, defendant
**Evidence items:** P1-1 (deepfakes in hiring), P1-2 (AI-enabled fraud: FBI IC3 first AI-fraud category $893.3M/22,364 complaints; Entrust 1-in-5 biometric fraud; IBM 1-in-4 breaches AI-enabled), P1-13 (AI-written papers; Nature 8/25/26 AI-detection feature as the "remedy" side), P2-C (Hermes Bot Mode 8/17 + v0.20.3/0.20.5; The New Stack 8/24; TechCrunch $1.5B valuation talks 7/13; Alabama/OpenAI probe 8/25; WikiHow v. OpenAI 8/24; Sagan estate suit 8/25; Brazil TikTok fine cross-listed under P1-6).
**Connecting thesis:** AI simultaneously (a) defeats the verification layer (deepfakes, AI papers, AI-enabled breaches), (b) is proposed as the fix (AI-detection software, "self-improving agents," Bot Mode), and (c) is the target of a fast-growing regulation/litigation wave. The verification layer is both the problem and the proposed solution — an arms race the news reports one battle at a time.
**NOT yet established:** whether AI-detection tools actually work (the Nature 8/25/26 feature is the in-window test and must be read as the evidentiary core); whether the regulatory wave (probes, fines, lawsuits) is substantive or symbolic; whether the Hermes/agent-commerce material (P2-C) belongs in the general pool at all — per the Part 2 method it is deliberately kept **separate**, and the deep team must preserve that stream separation in the essay brief.
**Open questions:** Does "AI defeats verification" and "AI restores verification" resolve into one story or two? What is the measured accuracy of current AI-detectors, and does it support P1-13's 90% figure as crisis vs. artifact?

### BS-5. Population-scale evidence vs. reporting integrity
**Evidence items:** P1-6 (social media/adolescent harm, 7 evidence lines), P1-11 (100M-person drug/stroke meta-analysis), P2-A3 (shingles/dementia, 509,926 analyzed / **8,843 vaccinated** / GSK funding), P2-A4 (495,037-cell hippocampal map), P2-A5 (mitochondria eye injection — preprint, single patient), P2-A8 (mRNA vaccine Phase III — headline-only, no survival data), P1-10 (sunlight entanglement) as the pure-science contrast.
**Connecting thesis:** population-scale evidence is now being produced for major health questions, but the reporting systematically races ahead of the caveats — interim results without survival endpoints (P2-A8), tiny treatment groups inside huge datasets (P2-A3), preprints reported as results (P2-A5), observational data reported as causal (P2-A3, P1-11), and a "90%" headline that is possibly a definitional artifact (P1-13). The same "headline outruns the caveat" pattern repeats across the health/science pool.
**NOT yet established:** whether the pattern is systematic or a handful of items the compile happened to include; methodology quality of each study (confounding control in P1-11; trial status of P2-A3); whether the population-scale-but-under-reported claim in P1-6 survives a media-coverage check.
**Open questions:** Is this a genuine "reporting-integrity" bigger story, or is it three separate science-writing caveats that should not be welded together? Should the science pool (P1-10, P1-11, P2-A4/5/6/8) feed the essay at all, or is it a separate essay's material (the Part 2 method kept it in its own pool)?

---

## 3. RESEARCH PROTOCOL

### 3.1 Source hierarchy (binding order of evidentiary weight)
1. **Primary government / institutional** — .gov advisories, agency outbreak pages, committee/congressional reports, UN/institutional reports, regulatory lists (FDA/CDC/FBI/EPA/CISA, ITRC, IEA, DOL ILAB, UNU-INWEH, FAO, PIRG), company statements, court/regulatory filings.
2. **Peer-reviewed literature** — the journal paper itself, read directly (methods, sample, funding, endpoints), not the press release or news summary.
3. **Industry / sector analyses** — Entrust, IBM X-Force, Z2Data, Sightline, Ecovadis, PKWare/Corestream, PJM/Goldman market data: usable for figures, but treated as self-interested where the firm has a product to sell.
4. **Media** — used to *locate* primaries and to timestamp events, never as the evidentiary basis for a figure. A number sourced only to a news article is downgraded one confidence tier.
5. **Self-published / social / marketing** — pricing pages, X posts, company claims: verified against the actual product/price table before any claim is carried; the compile's own treatment of P1-14 is the model (marketing math checked against the real price list).

**Rule:** every carried claim must trace to tier 1 or tier 2. Tiers 3–5 may corroborate but cannot establish.

### 3.2 Per-story verification checklist
For each item: (verify) = what must be re-read/re-checked at the top tier; (Δ) = what would change confidence. AO-items have no verification record in these files — they are **provisionally unverified** until the 2026-08-21 compile is obtained or they are re-verified from their stated primaries (CDC/FDA cyclospora pages; FBI/EPA/CISA PLC advisory 7/30/26; FDA July–Aug 2026 recall list; UChicago/ACLU Captive Labor report; Outlaw Ocean Project; HSC "China's Fishing Offensive"; CECC "From Bait to Plate"; NOAA/TMC filings; NOC/ZooKeys; Communications Sustainability study; UW/NOAA acidification paper; Concordia ice-core library; Nature Astronomy JWST Quintet; Science LHS 1140b; Science QT45; CERN LHCb; Nature Migdal; Science dendrites; Nature Biotechnology oesophagus; Light: Science & Applications quantum battery; Nature Aquiry).

**Trust / cyber cluster**
- **P1-1** (verify) ITRC H1 2026 report; FBI NK-IT advisory; State Dept 11-country joint advisory (7/31/26); the "18 of 20 Fortune 500" claim — the compile names an "independent threat hunter" but not the analyst or the sampling method, a sourcing gap; the unnamed federal agency (unverifiable by design; note P2-B1 pins it to Deputy Assistant Director Todd Hemmen's 7/28 conference + Federal News Network 8/10). (Δ) per-company attribution; agency named; FBI attribution of intent.
- **P1-2** (verify) ITRC 21-vs-3 insider events; FBI IC3 AI-fraud category ($893.3M / 22,364); Entrust 1-in-5; IBM 1-in-4 / +56%; PKWare/Corestream analyses; 1,803 breaches / 471M notices. (Δ) ITRC year-end reconciliation; attribution of specific insider events.
- **P2-A7** (verify) Reuters 8/26 + Boston Scientific statement; the "wave" list (Abbott, Stryker, Medtronic, Clover, Novo Nordisk, West Pharm) — check each against a source; attacker unnamed. (Δ) scope/materiality determination; named attribution.
- **AO-2** (verify) FBI/EPA/CISA PSA 7/30/26; 7-state count; PLC models (MicroLogix 1100/1400). (Δ) FBI attribution (financial vs. state) — currently unconfirmed.
- **AO-6** (verify) breach notification records; the dental-insurer 15M figure "varies by source and should be treated as approximate" — the article itself flags it; the 252 hacking/IT breaches ledger. (Δ) consistent cross-source case counts.

**Food / product-safety cluster**
- **P1-7** (verify) FAO Technical Paper 742: ~20%/30%/38.1% mislabeling rates; sample basis (25,000+). (Δ) FAO revisions; regional enforcement data.
- **P1-12** (verify) PIRG "Safe At Home in 2026": 420 recalls / 40M items / 12 deaths / 50+ models; cross-check CPSC database. (Δ) CPSC enforcement data; category breakdowns.
- **P2-A1** (verify) CDC fast-facts 8/21 (431 cases / 32 states / 57 hospitalized / 0 deaths); FDA outbreak page; Coast Citrus Distributors traceback; FDA Major Product Recalls; FSIS alert. (Δ) final source/scope determination; case-count trajectory.
- **P2-A2** (verify) CDC 8/24 (55 / 15 / 4 / 0, two dual infections); FDA recall 8/22 (Everything Sprouts / Calco). (Δ) source confirmation; additional lots/brands.
- **AO-1** (verify) CDC cyclospora counts (15,716 confirmed, 11,841 pending, 1,180 prior-season baseline, 828 hospitalized, 2 deaths); Taylor Farms de Mexico traceback; recall 7/17/26; the 7/18 border-sample false positive (FDA re-review 7/19); "no confirmed product positive ever." (Δ) CDC formal source attribution; state additions.
- **AO-3** (verify) FDA July–Aug 2026 recall list; the seven manufacturers (B. Braun, Fresenius Kabi, Baxter, American Regent, Sunny Pharmtech, Liebel-Flarsheim, Long Grove); particulate types; Class II status. (Δ) systemic-vs-coincidence determination — the article states this is not yet established; this is one of the highest-value single checks in the whole review.

**Resources / supply chain cluster**
- **P1-3** (verify) Sightline Climate (50% of planned 2026 U.S. AI data centers delayed; ~1,000× per-task energy); PJM (bills +44%; capacity auction $29→$329); Goldman Sachs inflation claim; Guardian 6/8/26; UT Austin (9% of Texas water by 2040); UN (9.3T liters); WRI. Also fold in the P2-B regulatory-wall update (Spain 8/25; PA 8/18; TX 8/4; NY 7/14; Monterey Park Jun) with Reuters 8/25/26 as primary. (Δ) PJM year-end data; regulatory decisions' effects.
- **P1-4** (verify) IEA Global Critical Minerals Outlook 2026; ISIS Peddling Peril Index; Z2Data (60% mining / 91% downstream / ~99% gallium / 72% top refiner share; 5×/3× price gaps; $6.5T/yr; $300B+ graphite). (Δ) non-Chinese refining buildout; IEA model revisions.
- **P1-8** (verify) DOL ILAB List of Goods (Xinjiang aluminum 17–20%; DR sugar $131M+); Ecovadis 27M figure. **Also resolve the Part 2 flag:** whether the UFLPA entity-list expansion (43 companies incl. five Xinjiang aluminum producers, 7/31/26; HRW 8/5) was captured — the compile's forced-labor item predates/omits it. (Δ) ILAB list updates; company-level sourcing disclosures.
- **P1-9** (verify) Bulletin of the Atomic Scientists 5/11/26; ASCE Report Card; ASDSO ($165.2B / 92,000 dams / 64-yr average / 18% high-hazard; Michigan Cheboygan + Bellaire near-misses). (Δ) a large dam failure; federal repair-funding action.
- **AO-7** (verify) TMC USA consolidated application (5/1/26); NOAA "full compliance" ruling; executive order basis; ISA Secretary-General Leticia Carvalho statement; Canada/UNCLOS articles 137–139 exposure; 65,000 km² (amended from 25,000) and USA-B 122,000 km² / ~1.02B tonnes. (Δ) permit issuance; tribunal action; Canada's position.
- **AO-8** (verify) NOC/ZooKeys special issue 3/24/26; Mirabestiidae/Mirabestioidea; ISA "One Thousand Reasons"; ">90% of CCZ species unnamed." (Δ) peer confirmation of new-family claim.
- **AO-9** (verify) Communications Sustainability study (5/4/26; BU/PSE/Harvard; 22 grid regions, 2020–2050); DAC vs. wind/solar cost-equivalence; "breakthrough" scenario (800 kWh, $100/ton). (Δ) independent replication of the cost model.
- **AO-10** (verify) UW/NOAA Nature Communications boron-isotope reconstruction (California Current + Salish Sea amplification). (Δ) replication.

**Health / science pool**
- **P1-6** (verify) WHR 2026 Ch.3 (5h/day average; 1-in-4 13–14yo at 7+; 40/47 PISA declines 2015–2018; 34/35 loneliness); CDC youth mental health; HHS Surgeon General advisory. Fold in P2-B: Mosseri trial testimony (Reuters 8/25) and Brazil/ByteDance fine (Reuters 8/25). (Δ) new randomized or natural-experiment evidence.
- **P1-10** (verify) Optica paper (vol 13, pp 1508–1514). **Resolve the institution inconsistency:** Part 1 credits University of Ottawa + NRC Canada; Part 2 credits Univ. Ottawa + Max Planck Institute for the Science of Light. (Δ) replication; engineering toward space-borne source.
- **P1-11** (verify) Cambridge / International Journal of Stroke meta-analysis; amphetamines +174% (under-55), and the Part 2 additions cocaine +96%, cannabis +37% — confirm against the paper; confounding control; the 100M+ sample basis. (Δ) meta-analysis reconciliation; confounding-control details.
- **P2-A3** (verify) Annals of Internal Medicine paper (Hayes et al.); 509,926 / 8,843 vaccinated / 24% lower dementia risk over 4 years / GSK funding disclosure. (Δ) trial confirmation; non-facility-cohort replication — the paper itself says trials are needed; the compile's "Medium-High association, causal not established" should be retained.
- **P2-A4** (verify) Nature Medicine (10.1038/s41591-026-04571-8) 8/21/26; 495,037 cells; "pattern separation" claim; Columbia newsroom + Nature news 8/25. (Δ) replication; human interventional evidence.
- **P2-A5** (verify) preprint (8/10/26) + Nature news 8/24 (d41586-026-02616-z); single patient; transient light response ~4 weeks. (Δ) peer review; replication; longer follow-up — currently **Medium**, must not be reported as more.
- **P2-A6** (verify) Nature Astronomy (s41550-026-02945-z) 8/25/26; Nature (s41586-025-09900-4); UWA newsroom. (Δ) deep spectra (Balmer absorption/breaks) across many LRDs — "High that LRDs host black holes; Medium on the specific black-hole-star mechanism."
- **P2-A8** (verify) Moderna/Merck announcement 8/19/26 (intismeran + Keytruda, adjuvant high-risk melanoma); Reuters/STAT/Nature/CNBC coverage; **no overall-survival data, no detailed numbers** — the honest read is headline-only interim. (Δ) full data release at medical meeting; survival endpoint.
- **P1-13** (verify) the Nature "90%" claim's underlying methodology — whether detector-based, self-reported, or style-based; this is the compile's own flagged gap (its only Medium-confidence general item). Also read the in-window Nature 8/25/26 AI-detection feature (d41586-026-02569-3). (Δ) methodology disclosure; detector accuracy data.
- **P1-14 / P2-C** (verify) the X post (x.com/nousresearch/status/2090432358969196548); Hermes Cloud price table; x.ai Grok Bot pricing; VentureBeat/eesel. **Resolve the timeline inconsistency:** Part 2 states Bot Mode was "announced Aug 17, 2026" yet frames the section as "the week after the original compile's Aug 20 post" — Aug 17 precedes Aug 20; dates must be reconciled. Verify Bot Mode in v0.20.3 and the v0.20.5 (v2026.8.19) release. (Δ) actual pricing/inference-cost data for working (non-idle) agents.

### 3.3 Confidence rubric (carried from the compilation method)
Every registry row keeps the compile's High/Medium/Low scheme, each with an explicit "what would change it":
- **High** — claim rests on a tier-1/2 primary source read directly, internally consistent, no material contradiction found. *Would change:* primary-source revision/retraction; a contradicting primary source; identification of a transcription/interpretation error in the compile.
- **Medium** — claim rests on tier-3/4 sources, or on a headline/press release ahead of the underlying data (preprint, interim results, marketing math, unnamed subjects), or on a primary not yet read directly. *Would change:* reading the underlying primary; peer review/replication; full data release; named attribution.
- **Low** — single self-published/tier-5 source, unverifiable figure, or an inference the source does not make. *Would change:* corroborating primary appears, or the claim is dropped.

**Hard rules:** no claim may be upgraded a tier during this review; it may only be downgraded or confirmed. The "bigger stories" (§2) are all Medium-confidence *hypotheses* until Phase 2 produces briefs; they never inherit High from their component items.

---

## 4. DEEP-DIVE TEAM STRUCTURE

Six roles. Scope per role; no role edits another's items without the synthesis/editor logging it.

1. **Verification analyst (lead)** — owns the claim-level registry (§3.2), the source hierarchy, access logs, and the P1/P2/AO reconciliation. Scope: every tier-1 re-read, every "Δ" check, and the inconsistency-fix list (§7.2). Not responsible for new-angle research.
2. **Cyber / infrastructure-beat analyst** — P1-1, P1-2, P2-A7, AO-2, AO-6, and the OT/PLC + insider-surge + healthcare-wave evidence for BS-1 and BS-4. Scope: attribution questions (unnamed actors), the "wave" claims, and whether the seven-recall cluster (AO-3, shared with #4) has a systemic driver.
3. **Resource / supply-chain analyst** — P1-3, P1-4, P1-8, P1-9, P2-A1, P2-A2, AO-1, AO-7, AO-8, AO-9, AO-10; owns BS-2 and the food/safety half of BS-1. Scope: UFLPA gap resolution; seabed legal exposure; import-verification failure modes; the power/water regulatory wall.
4. **Health / science-beat analyst** — P1-6, P1-10, P1-11, P1-13, P2-A3, P2-A4, P2-A5, P2-A6, P2-A8, and the AO science items (AO-11–20); owns BS-5 and the science half of BS-3. Scope: methodology reads (sample, funding, endpoints, confounding), preprint vs. peer-reviewed discipline, and whether the science pool belongs in this essay at all.
5. **Media-pattern / framing analyst** — owns BS-3. Scope: design and run the countable content-analysis (outlet × item × frame × volume) that tests "the news misses X"; negative-case sampling (find no-photograph problems that WERE covered); quantify selection bias in the compile's own method. This role exists precisely because the meta-thesis is currently asserted, not measured.
6. **Synthesis / editor** — owns the five bigger-story briefs, the kill-list, the Medium essay brief, the fact-check appendix, and stream separation (Section C Hermes/AI kept out of the general pool, per Part 2 method). Scope: adjudicate cross-role conflicts, preserve the compile's "journalism-analyst hybrid" voice (narrative lede, unspun facts, twist, confidence), and draft O4's deliverable. Approves nothing without the human gates (§5).

---

## 5. PHASES + GATES

Each phase ends in a **gate that requires human (analyst/owner) sign-off** before any subsequent phase starts. No phase runs on the coat-tails of the previous one's approval.

**Phase 0 — Inventory & baseline (local-only; zero network)**
- Build the claim-level registry across P1 (14 items), P2 (8 new + update notes + Section C), and the AO list; assign IDs, current confidence, source list, and verification status (verified-in-files / needs-re-read / unverified-AO / inconsistent).
- Diff the three documents; log every cross-document discrepancy (§7.2) and every AO item's missing verification record.
- **Done when:** registry complete; discrepancy list complete; footprint declaration drafted. **Gate 0:** human signs the registry + the Phase 1 Footprint Declaration (§6) — no networked research before this.

**Phase 1 — Verification of existing items (networked, under Phase 1 footprint)**
- Execute §3.2 checklists in tier order; resolve the inconsistency list; obtain or re-verify AO primaries; update every "Δ" field.
- **Done when:** every registry row has a status {verified, revised, retracted, unverifiable} and every High claim traces to a tier-1/2 primary read directly. **Gate 1:** human sign-off on the verified fact base; no item passes to synthesis without a status. Items that fail verification get a provisional kill-list entry now.

**Phase 2 — New-angles research on the bigger stories (networked, under Phase 2 footprint)**
- Test BS-1–BS-5 per §2's open questions; the media-pattern analyst runs the BS-3 content analysis; negative-case and coincidence-check sections mandatory in every brief; the §7.1 invalidation risks are actively hunted, not avoided.
- **Done when:** five evidence briefs exist, each with supporting + contradicting evidence and a verdict {supported, plausible, not supported, coincidence-not-structure}; the verified fact base is unchanged (no new claims admitted without a registry row). **Gate 2:** human sign-off on the five theses — this is the decision point where a "bigger story" can be killed for being a coincidence.

**Phase 3 — Synthesis + article brief (local-only)**
- Draft the Medium essay brief: which bigger stories carry, which items anchor them, confidence tags, alternatives, kill-list; write the fact-check appendix mapping every paragraph to a registry row; preserve stream separation (P2-C material stays separate per Part 2 method).
- **Done when:** brief + appendix + kill-list complete and internally consistent with the registry. **Gate 3:** human sign-off on the final brief before anything is published; corrections to the already-published "The News Is Missing You" (if Phase 1 finds errors in its carried claims) are flagged to the owner as a separate decision.

---

## 6. FOOTPRINT & INTEGRITY CONTROLS

The owner is ISP-accountable and has explicitly required sign-off before any networked research. This plan enforces that with six hard controls:

1. **Zero network in planning.** This plan was produced entirely from the three local files. The deep team inherits that posture: no phase starts networked.
2. **Per-phase Footprint Declaration.** Before Phase 1 and Phase 2, a written declaration stating: search domains and query classes, the specific primary-source sites to visit, expected volume of requests, no downloads of executable content, no login-gated scraping, no purchases, no personal-data collection, no contact with human subjects. **No network work of any kind occurs before the owner signs the current phase's declaration.**
3. **No delegated fan-out.** No sub-agent, script, or automation may initiate network requests beyond the approved declaration. Any expansion (new domain, new query class, new source family) requires a fresh declaration and fresh approval. A search/visit log is kept and compared against the declaration at each gate; exceptions are blocking defects.
4. **Primary-source-first.** Tiers 1–2 establish; tiers 3–5 only locate or corroborate (§3.1). A claim carried on a secondary source alone is a registry defect.
5. **No speculative sources.** No anonymous tips, no AI-generated sources, no invented URLs, no "we assume X published Y." Every source is logged with name, access date, and URL; every AO item sourced to its stated primary or marked unverified.
6. **Full audit trail + stream separation.** All searches, visits, and reads are logged and retained for the owner. The Part 2 stream separation (general news+science vs. Hermes/AI news) is preserved through to the essay brief; P2-C material is never blended into the general pool.

---

## 7. RISKS & OPEN QUESTIONS

### 7.1 Risks that could invalidate the synthesis
- **The pattern is a sampling artifact (highest risk).** The compile's method selects stories that fit the "trust economy / no-photograph" frame, so the pattern may be manufactured by selection. BS-3's entire load-bearing claim ("the news misses these") is unmeasured. Mitigation: the media-pattern analyst's content analysis + mandatory negative-case sections; if coverage of these items is actually normal, the meta-thesis collapses from "the news is missing you" to "a curated selection of under-covered items."
- **Coincidence-not-structure.** The seven-injectable-recall cluster (AO-3), the food-outbreak wave (P2-A1/A2/AO-1), and the healthcare-cyber wave (P2-A7) may each be statistical coincidence — the article itself concedes the recall cluster is "not yet established." If none resolves to a shared mechanism, BS-1 loses its strongest examples.
- **Transcription/attribution errors in the compiles.** Already visible: P1-10's institution mismatch (Ottawa+NRC vs. Ottawa+Max Planck), P1-14/P2-C's Bot-Mode timeline (Aug 17 vs. "after the Aug 20 post"), and P1-8's likely UFLPA gap. If one key figure (e.g., 18-of-20 Fortune 500, the 7× insider surge, the 90% AI-paper share) is wrong, every bigger story anchored on it weakens.
- **Unverifiable-by-design claims.** Unnamed subjects (federal agency in P1-1; attacker in P2-A7), the FDA false-positive drama (AO-1), the "bankruptcy" framing (P1-5 — definitional, possibly not measurable), and the 15M dental-breach figure the article itself calls approximate. These cannot be confirmed; the brief must say so rather than paper over it.
- **The 08-21 compile gap.** The published article is built on the 2026-08-21 compile, which is not in the workspace. Until it is obtained or its AO items are re-verified, a large share of the essay's material is unverified in this review's records.

### 7.2 Internal inconsistencies already logged (must be resolved in Phase 0/1)
1. P1-10 vs. P2-B#10 — institutional attribution differs (NRC Canada vs. Max Planck Institute for the Science of Light).
2. P2-C — Bot Mode "announced Aug 17, 2026" vs. the framing "in the week after the original compile's Aug 20 post"; dates conflict.
3. P2-B#8 — UFLPA entity-list expansion (43 companies, 7/31/26, five Xinjiang aluminum producers) likely postdates/omits P1-8's forced-labor item; gap flagged in the source itself ("Worth checking whether the original compile captured the UFLPA list expansion").
4. P1-11 vs. P2-B#11 — Part 2 adds cocaine +96% and cannabis +37% figures absent from Part 1; confirm against the paper.
5. Article-vs-files — the article's AO items (cyclospora, OT/PLC, seven recalls, prison labor, dental breach, seabed, DAC, ice cores, etc.) have no verification record in either compile file; also the article's byline date ("3 days ago" relative to its extraction) versus the compile dates should be pinned for the correction decision.

### 7.3 Remaining unverifiable / open
- Attribution of the OT/PLC attacks and the healthcare-cyber attackers (state vs. criminal) — may remain open indefinitely; brief must carry it as open.
- Whether "bankruptcy" is a measurable state or a durable framing — possibly definitional forever.
- Whether seabed mining proceeds (permit expected Q1 2027) — a forward call, not a verifiable fact.
- Whether the AI-detection "arms race" (BS-4) resolves in any direction — depends on future releases.
- Whether the shingles/dementia and mRNA-vaccine items graduate from association/interim to causal/full — depends on trials and data releases the team cannot run.

---

*End of plan. Produced from local files only; no network activity; no external facts asserted beyond the three sources.*
