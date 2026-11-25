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
