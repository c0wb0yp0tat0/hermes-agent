# DEEP-LOOKS-NETWORK-20261106 — the fork-network's mission-map reading (E-5: the governance-line's feeder + the compaction-line's sibling)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork). **Seat:** the handoff's E-5 deep-looks — the network's two wildcard forks read as the mission-map's next rung. **Register:** receipts, never claims. **The read's honesty-wall (binding):** both network repos were read **READ-ONLY from the staged READMEs only**; nothing was written to either fork's surface. The `agent-governance-toolkit` README is ~19K chars and the harness caps `read_file` at 12,000 chars per call — **only its head is certified here** (the banner, the "What This Is (and Isn't)" block, the 0.1ms policy-check line, the 26.67%→0.00% benchmark claim, the "Get Started in 90 Se…" truncation). Everything below the cap is named as UNREAD and never inferred. The `hermes-toolperf-evals` README is fully read (it is ~3K chars, under the cap). Every mapping below is a **hypothesis from the README's surface**, not a code-certified fact — the code-reads are named next-passes.

---

## [Executive Summary]

Two network forks, two lanes, one verdict each:

1. **`agent-governance-toolkit` (AGT)** — the governance-line's feeder. Its README's *head* gives three concrete enforcement mechanisms (deterministic pre-execution policy check; zero-trust identity; execution sandboxing) plus a named benchmark discipline (prompt-safety 26.67% violation vs deterministic 0.00%). Mapped onto the study's eight OWASP-gap fold-drafts: **three fold-drafts gain a concrete pattern from the head alone** (ASI-02 capability scoping, ASI-03 identity/privilege on write admission, ASI-05 code-execution gating), **five stay named-only** (ASI-01, ASI-04, ASI-07, ASI-08, ASI-10) because the head does not name their mechanism. The wall: the README's *enforcement-pattern* body (the section that would map ASI-01/04/07/08/10) is below the 12K cap — **UNREAD**.
2. **`hermes-toolperf-evals`** — the compaction-line's sibling. Its README gives the A/B eval shape in full (9 error-inducing cases, baseline-tree vs fixes-tree, arms differing only by `PYTHONPATH`, 2 models × 3 reps, ATOF-scored, mean-of-≥3-reps discipline). Mapped onto the ladder-battery: the battery **already does better on medians-over-runs (3 runs, medians reported) and on real-cell ground-truth (the probe-banks' byte-verified expected-facts)**; it **borrows the baseline-vs-fixes arm discipline, the deterministic success-marker, and the crash-retry-on-resume rule**. The wall: the harness's own `abeval/README` (parameterized) and `METHODOLOGY.md` are not staged — the A/B shape is certified only at the top-level README's granularity.

**The one-line verdict:** the governance-feeder gives the fold-drafts **three concrete patterns and five named-only walls** (head-capped), and the toolperf sibling gives the ladder-battery **three borrow-candidates it mostly already exceeds** — the mission-map's next rung is read, the code-reads are the named next-pass.

---

## [Analysis Brief]

### (a) The read-side's certified surface (what the READMEs actually say)

#### AGT — certified head (the 12K cap's reach)
- **Positioning:** "Runtime governance for AI agents — deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents. Covers all 10 OWASP Agentic risks with 13,000+ tests." (header block)
- **The pipeline (the README's own ASCII):** `Agent Action ──► Policy Check ──► Allow / Deny ──► Audit Log    (< 0.1 ms)`.
- **The boundary:** "Sits between your agent framework and the actions agents take. Every tool call, resource access, and inter-agent message is evaluated against policy *before* execution. Deterministic — not probabilistic." And: "This is not a prompt guardrail or content moderation tool. It governs agent *actions*, not LLM inputs/outputs."
- **The benchmark:** prompt-based safety ("please follow the rules") has a 26.67% policy-violation rate in red-team testing; AGT's deterministic application-layer enforcement: **0.00%**. (Cites `docs/BENCHMARKS.md` — not staged, not read.)
- **The compliance badge:** "OWASP Agentic Top 10 — 10/10 Covered" (links `docs/OWASP-COMPLIANCE.md` — not staged, not read).
- **The adapters:** AWS Bedrock, Google ADK, Azure AI, LangChain, CrewAI, AutoGen, OpenAI Agents, 20+ more; Python · TypeScript · .NET · Rust · Go.
- **UNREAD (named, never inferred):** everything after "Get Started in 90 Se…" — the quick-start, the policy-definition schema, the identity model's detail, the sandbox's mechanism, the audit-log's shape, and the per-ASI enforcement-pattern sections. The README's head names the *mechanisms* but not their *implementation patterns*; the fold-draft mapping below is therefore a **head-only** mapping.

#### hermes-toolperf-evals — fully read (under the cap)
- **The A/B harness (`abeval/`):** "9 error-inducing benchmark cases, baseline-tree vs fixes-tree (arms differ only by `PYTHONPATH`), 2 models × 3 reps, ATOF-scored. This is the harness behind the published before/after numbers. Parameterized."
- **The 9 cases:** `err_python_env`, `err_replay_patch`, `err_ambiguous_edit`, `err_case_search`, `err_hidden_search`, `err_big_output`, `err_multi_dir`, `err_inline_script`, `err_big_file_read` — "each derived from a mined production waste class, with a sandbox fixture and a deterministic success marker."
- **The run discipline:** `./run_all.sh <baseline-tree> <fixes-tree> [reps] [models...]`; "The harness shells out to the `hermes` CLI; any provider model id works. Startup crashes (nonzero exit, empty output) retry on resume instead of being recorded as data points. Report the mean of ≥3 reps per cell; n=3 deltas under a few percent are noise."
- **The data's provenance:** "Built from production session-DB mining (~1.5M messages), a schema token audit, and NVIDIA NeMo Relay ATOF traces for ground-truth turn accounting."
- **The canonical dataset:** `results/2026-08-06_rerun/` — "pinned SHAs, meta.jsonl per cell, full ATOF traces, regeneration instructions, and an honest readout vs the Aug 2 published numbers."
- **The headline numbers:** −21% LLM turns · −29% tool calls · tool errors and retry-after-error → 0 · −33% result bytes into context · −23% wall clock (weak model); strong model parity.
- **The in-product twin:** "The A/B harness also ships inside hermes-agent at `scripts/toolperf_abeval/` (landed in PR #79162); this repo is the canonical home for the full eval set."

---

### (b) The mapping — AGT's mechanisms → the study's L0 write-gate spec + the eight OWASP-gap fold-drafts

**The study's write-gate spec (the target).** From `GOVERNANCE-OWASP-MAPPING.md` §(b): the gate's design mechanisms are **budget-enforcement, acceptance-pipeline, effect_key replay, at-most-once admission, landmark-gate** — covering ASI-06 fully and ASI-09 partially. The eight GAPs (ASI-01, 02, 03, 04, 05, 07, 08, 10) are the fold-drafts' object. From `GOVERNANCE-FOLD-DRAFTS.md`: each draft's fold-candidate is a **named control requirement + a one-line concrete candidate** (e.g. ASI-03: "record principal on each write; enforce write-permission per principal").

**The mapping table (mechanism → fold-draft → status):**

| AGT mechanism (README section) | Study's line / spec / arm | Fold-draft status | Evidence (receipt) |
|---|---|---|---|
| **Deterministic pre-execution policy check** — "Every tool call, resource access, and inter-agent message is evaluated against policy *before* execution. Deterministic — not probabilistic." (`What This Is (and Isn't)`) | The write-gate's **acceptance-pipeline** + the fold-drafts' shared "policy-based action interception at write time" shape | **ASI-01 GAINS A CONCRETE PATTERN** (the pre-execution policy check IS the goal-hijack gate's shape: evaluate the action against policy before admitting the write) | README head, the ASCII pipeline + the "before execution" line |
| **Zero-trust identity** — "zero-trust identity" (header) | ASI-03's "record principal on each write; enforce write-permission per principal" | **ASI-03 GAINS A CONCRETE PATTERN** (zero-trust identity is the principal-authentication/authorization pattern the draft names) | README header block |
| **Execution sandboxing** — "execution sandboxing" (header) | ASI-02's "bind each write to an allowed tool/capability set" + ASI-05's "scan/block executable content in derived memory" | **ASI-02 and ASI-05 GAIN A CONCRETE PATTERN** (sandboxing = least-privilege capability scope + code-execution containment) | README header block |
| **Allow / Deny decision + Audit Log** — the ASCII pipeline's verdict + log (`What This Is (and Isn't)`) | The write-gate's **acceptance-pipeline** verdict + the audit-log the fold-drafts imply but do not name | **ASI-04 / ASI-07 STAY NAMED-ONLY** (the head names the audit-log's existence, not provenance-tracking or integrity-signature patterns) | README head, the ASCII pipeline |
| **"Governs agent actions, not LLM inputs/outputs"** — the boundary line | The write-gate's **action-level** (not content-level) enforcement scope | **ASI-08 / ASI-10 STAY NAMED-ONLY** (the head does not name circuit-breaker/backpressure or kill-switch/loop-detection) | README head, the boundary paragraph |
| **OWASP 10/10 badge + `docs/OWASP-COMPLIANCE.md`** (not read) | The eight fold-drafts' completeness claim | **UNREAD — the compliance doc is the natural mapping source and is not staged** | badge link only |

**The honest count:** of the eight fold-drafts, **three gain a concrete pattern from the certified head** (ASI-01 pre-execution policy check; ASI-02/05 sandboxing-as-capability-scope; ASI-03 zero-trust identity). **Five stay named-only** (ASI-04, ASI-07, ASI-08, ASI-10, plus ASI-09's strengthening) because the head names the *mechanism family* but not the *enforcement pattern* the draft needs. The README's enforcement-pattern body — the section that would map the five — is **below the 12K cap and UNREAD**.

**The wall (binding):** the AGT README is the **surface, not the code**. The "0.00% violation" and "10/10 covered" are the README's *claims*, not receipts this study ran. The `docs/OWASP-COMPLIANCE.md` and `docs/BENCHMARKS.md` are the natural next-pass reads — **neither is staged in `e5-ground/`**. No AGT code was read; no AGT surface was written.

---

### (c) The mapping — hermes-toolperf-evals' A/B shape → the ladder-battery's design

**The ladder-battery's current state (the target).** From `EVAL-LADDER-BATTERY-20261106.md`: 5 fixtures × 3 runs at substrate-pin `a996d4ad3039…` (compressor + judge `deepseek/deepseek-v4-flash-0731`); recovery medians **4.50 / 3.25 / 4.67 / 1.00 / 0.00**; medians-over-runs reported (single runs are noise); the two rebuilt real cells (deep-compaction 1.00, high-density 0.00) are the depth-cell and density-cell floors; the probe-banks (`PROBE-BANKS-20261106.md`) byte-verify every expected-fact in the fixture's bytes (deterministic, no model).

**The mapping table (A/B mechanism → ladder-battery's design):**

| hermes-toolperf-evals mechanism (README section) | Ladder-battery's design | Borrow / already-better | Evidence (receipt) |
|---|---|---|---|
| **Baseline-tree vs fixes-tree, arms differ only by `PYTHONPATH`** (`Layout`, `abeval/`) | The battery runs one substrate-pin (`a996d4ad3039…`) — a **single-arm** design | **BORROW-CANDIDATE:** a baseline-vs-fixes arm would let the battery measure the composition-fix's delta at each rung, not just absolute recovery | toolperf README, `abeval/` row |
| **Mean of ≥3 reps per cell; n=3 deltas under a few percent are noise** (`Running the A/B eval`) | The battery reports **medians over 3 runs** and treats single runs as noise | **ALREADY-BETTER:** the battery's median-over-runs is the stronger statistic (robust to the outlier the mean admits); the toolperf README's "mean" is the weaker form | EVAL-LADDER-BATTERY §(a); toolperf README |
| **Deterministic success marker per case** (`The 9 A/B benchmark cases`) | The probe-banks' byte-verified expected-facts (deterministic, no model) | **ALREADY-BETTER:** the banks certify the ground-truth *presence* in the fixture bytes — a stronger ground-truth than a success-marker | PROBE-BANKS-20261106; toolperf README |
| **Startup crashes retry on resume, not recorded as data points** (`Running the A/B eval`) | The battery's 15 runs all executed (no crash-retry rule named) | **BORROW-CANDIDATE:** an explicit crash-retry-on-resume rule would harden the battery against provider-window flakes | toolperf README |
| **ATOF-scored ground-truth turn accounting** (`Layout`, `results/`) | The battery's judge is `deepseek/deepseek-v4-flash-0731` (a model-judge, not a trace-accounting) | **BORROW-CANDIDATE (wall):** ATOF turn-accounting is a *trace-grounded* judge; the battery's model-judge is cheaper but less grounded. The battery's judge-config is a named trade-off, not a defect | EVAL-LADDER-BATTERY §(a); toolperf README |
| **Pinned SHAs + meta.jsonl per cell + regeneration instructions** (`results/2026-08-06_rerun/`) | The battery's label `ladder-20261106-a996d4ad` + the pin + the 15 per-run JSONs | **PARITY:** both pin the substrate and archive per-cell metadata; the battery's scratch-copy is the same discipline | EVAL-LADDER-BATTERY §(a) |
| **Production session-DB mining (~1.5M messages) → the waste classes** (`headline`) | The battery's fixtures are real cells mined from the rig's own sessions | **PARITY:** both derive cases from production mining, not synthetic invention | toolperf README; PROBE-BANKS-20261106 |

**The honest count:** the ladder-battery **already does better** on the two disciplines that matter most (medians-over-runs; byte-verified ground-truth). It **borrows** three things: the baseline-vs-fixes arm discipline, the crash-retry-on-resume rule, and (as a named trade-off, not a defect) the trace-grounded judge. The toolperf harness's *shape* is the battery's natural A/B sibling; the battery's *statistics* are the stronger form.

**The wall (binding):** the toolperf README is the **surface, not the code**. The `abeval/README` (parameterized), `METHODOLOGY.md`, and `results/2026-08-06_rerun/` are the natural next-pass reads — **none is staged in `e5-ground/`**. No toolperf code was read; no toolperf surface was written.

---

### (d) The borrow-candidates with the honest walls

**From AGT (governance-line):**
1. **The pre-execution policy check as the ASI-01 goal-hijack gate's pattern** — the README's "evaluated against policy *before* execution" is the fold-draft's exact shape. *Wall:* the policy-schema (what a policy *is*, how it's defined) is UNREAD; the pattern is certified only as a sentence, not a schema.
2. **Zero-trust identity as the ASI-03 write-admission pattern** — the header names it; the identity model's detail (principal types, token format, verification) is UNREAD.
3. **Execution sandboxing as the ASI-02/ASI-05 capability-scope + code-execution pattern** — the header names it; the sandbox's mechanism (namespace? seccomp? capability-drop?) is UNREAD.
4. **The audit-log as the ASI-04/ASI-07 provenance/integrity substrate** — the ASCII pipeline names the log; the log's schema (does it carry provenance? signatures?) is UNREAD. *This is the highest-VOI next-pass: `docs/OWASP-COMPLIANCE.md` is the natural mapping source and is not staged.*

**From hermes-toolperf-evals (compaction-line):**
1. **The baseline-vs-fixes arm** — the battery's single-arm design could gain a fixes-tree arm to measure the composition-fix's per-rung delta. *Wall:* the battery's fixtures are real cells, not error-inducing cases; the arm's construction (which fixes? which baseline?) is a design question, not a README-read.
2. **The crash-retry-on-resume rule** — a direct, cheap hardening. *Wall:* the battery's 15 runs all executed; the rule is a guard, not a measured need.
3. **The trace-grounded judge (ATOF)** — a named trade-off vs the battery's model-judge. *Wall:* the battery's judge-config is already pinned and receipted; switching judges is a new instrument, not a borrow.

**The code-reads (named next-passes, gated on a candidate earning it):**
- AGT: `docs/OWASP-COMPLIANCE.md` (the eight ASI enforcement-patterns — the natural mapping source), `docs/BENCHMARKS.md` (the 0.00% claim's receipt), the policy-schema + identity-model + sandbox sections (the UNREAD body).
- toolperf: `abeval/README` (the parameterized harness), `METHODOLOGY.md` (the targets' derivation), `results/2026-08-06_rerun/` (the canonical dataset's regeneration).

---

### (e) The CREATOR-GAPs (what the READMEs leave unresolved)

**AGT:**
- **GAP-1 (the cap's wall):** the enforcement-pattern body — the section that would map ASI-04/07/08/10 — is below the 12K read-cap and UNREAD. The head names the mechanism families; the patterns are not certified.
- **GAP-2 (the claim's receipt):** the "0.00% violation" and "10/10 covered" are the README's claims; `docs/BENCHMARKS.md` and `docs/OWASP-COMPLIANCE.md` are not staged. The claim is a *pointer*, not a receipt.
- **GAP-3 (the action-vs-content boundary):** AGT "governs agent actions, not LLM inputs/outputs" — the write-gate's memory-writes are *content* admissions. The mapping is a **shape-borrow** (pre-execution policy check), not a direct transfer; the content-vs-action seam is unresolved by the README.

**hermes-toolperf-evals:**
- **GAP-4 (the harness's parameterization):** the top-level README says "Parameterized — see its README"; `abeval/README` is not staged. The A/B shape is certified only at the top level.
- **GAP-5 (the judge's ground):** the battery's model-judge vs the harness's ATOF trace-accounting — the trade-off is named, not measured. Which judge is *right* for the ladder-battery's per-rung recovery is an open instrument question.
- **GAP-6 (the strong-model parity):** the harness's headline says "Strong model: parity (it already recovers in one turn — which is why weak-model runs are the signal)." The ladder-battery runs one compressor + one judge model; the weak-model signal's transfer to the battery's model-config is unmeasured.

---

## [Recommendation/Action Plan]

**One reversible next action:** stage the two network repos' companion docs (`docs/OWASP-COMPLIANCE.md` + `docs/BENCHMARKS.md` for AGT; `abeval/README` + `METHODOLOGY.md` for toolperf) into `e5-ground/` and re-run this lane's mapping against the staged bodies — the five named-only fold-drafts (ASI-04/07/08/10 + ASI-09) are the specific target. **Success criterion:** each of the eight fold-drafts carries either a concrete pattern cited to a staged section, or an explicit "stays named-only — the pattern is not in the staged surface" marker. No code-read of either network repo until a candidate earns it.

---

## [Next Steps/Exploration]

- The AGT compliance-doc read is the highest-VOI next-pass (the eight ASI enforcement-patterns are its natural home).
- The toolperf `METHODOLOGY.md` read would certify the A/B harness's parameterization (the battery's baseline-vs-fixes arm design rides on it).
- The governance-line's next mechanism: the fold-drafts' five named-only controls (ASI-04/07/08/10 + ASI-09) are the open seam — the compliance-doc read is the seam's next rung.

---

## [Artifact]

- **File:** `studies/rfc-143379-rig/DEEP-LOOKS-NETWORK-20261106.md`
- **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public).
- **The read's honesty-wall:** the AGT README is certified only to the 12K cap (head); the toolperf README is fully read; no network-repo surface was written; no network-repo code was read.
- **Register:** receipts, never claims — every mapping above is a hypothesis from the staged README's surface, with the code-reads named as the next-pass.