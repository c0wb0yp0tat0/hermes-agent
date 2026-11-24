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
