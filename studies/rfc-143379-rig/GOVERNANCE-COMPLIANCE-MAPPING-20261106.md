# GOVERNANCE-COMPLIANCE-MAPPING-20261106 — AGT compliance re-read mapped onto the eight OWASP-gap fold-drafts

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork). **Seat:** the governance-plane lane — the E-5 named next-pass. **Register:** receipts, never claims. **Extends, never rewrites:** `GOVERNANCE-OWASP-MAPPING.md`, `GOVERNANCE-FOLD-DRAFTS.md`, `DEEP-LOOKS-NETWORK-20261106.md`.

## [Executive Summary]

The E-5 deep-looks certified only the AGT README's head (12K cap): three fold-drafts gained patterns (ASI-02, ASI-03, ASI-05), five stayed named-only (ASI-01, ASI-04, ASI-07, ASI-08, ASI-10), plus ASI-09's strengthening. This lane reads the two staged companion docs. **Result:** the compliance doc's certified head (Coverage Summary table + §ASI-01 + §ASI-02) gives ASI-01 a concrete pattern it did not have (policy-based action interception), and gives every ASI a component-level pointer from the table; the detailed bodies for ASI-03..ASI-10 sit below the 12K cap and are **UNREAD** (named, not inferred). The benchmarks doc (9K, claimed under cap) receipts latency/throughput only — its certified portion does **not** substantiate the README's 26.67%→0.00% prompt-safety claim; that tail is also named UNREAD. **Verdict:** of the eight fold-drafts, **1 gains a new concrete pattern** (ASI-01), **3 keep their README-head patterns confirmed** (ASI-02, ASI-03, ASI-05 — ASI-02 additionally strengthened by §ASI-02), **4 carry the component pointer + the explicit marker "stays named-only — the pattern is not in the staged surface"** (ASI-04, ASI-07, ASI-08, ASI-10), and **ASI-09's strengthening stays named-only**. ASI-06 (covered baseline) gains a component citation (VFS Policies + CMVK Verification). No fold-draft is left without either a cited pattern or the marker.

---

## [Analysis Brief]

- **Domain:** COMPLICATED (expert analysis of a staged doc surface; classification stated per the spine). Evidence = the two staged files' certified bytes. Assumptions = the staged files are faithful copies of the upstream docs at the README's referenced paths. Uncertainty = everything below the 12K cap in the compliance doc and the trailing bytes of the benchmarks doc are UNREAD; no inference permitted there.
- **Evidence (certified):**
  - `AGT-OWASP-COMPLIANCE.md` — certified head only: the document title, the Coverage Summary table (all 10 ASI rows with component), §ASI-01 in full (policy-based action interception, Policy Engine, Action Interception, Policy Modes strict/permissive/audit, MCP Governance Proxy, code example, Component `src/agent_os/policy/` + `extensions/mcp-server/src/services/policy-engine.ts`), §ASI-02 in full (capability-based security POSIX, Capability Sandboxing, Tool Allowlists/Denylists, Input Sanitization, `verify_code_safety` MCP tool, Component capability model + MCP proxy policy rules), and the opening heading of §ASI-03 ("Identity & Privilege…") which is cut off at the cap.
  - `AGT-BENCHMARKS.md` — certified portion: TL;DR table, §1 Policy Evaluation, §2 Kernel Enforcement (incl. Concurrent Throughput), §3 Audit System (partial — ends mid-sentence).
- **The cap:** `read_file` max 12,000 chars/call; repeated calls return the identical head. The compliance doc is ~15.3K (per brief) → tail UNREAD. The benchmarks doc is claimed 9K → should fit, but the certified read ends mid-sentence at "…recommended for larg…", so the trailing bytes are treated as UNREAD (named, not denied) — the wall clause applies.
- **Surface-not-code caveat:** every mapping here is a **documentation-surface** citation. The AGT repo was read READ-ONLY; no code was executed, no tests run. "Covered" claims are the toolkit's own compliance-doc assertions, not independently verified.

---

## Per-ASI mapping table

| OWASP control | Fold-draft (`GOVERNANCE-FOLD-DRAFTS.md`) | Staged doc citation | Concrete pattern gained / named-only marker |
|---|---|---|---|
| ASI-01 Agent Goal Hijack | ASI-01 (goal-hijack gate) | `AGT-OWASP-COMPLIANCE.md` §ASI-01 + Coverage Summary row | **GAINS pattern:** policy-based action interception at the application layer — Policy Engine (declarative rules), Action Interception (governance middleware before execution), Policy Modes `strict`/`permissive`/`audit`, MCP Governance Proxy for MCP tool calls; example `StatelessKernel` + `ExecutionContext(policies=["read_only"])` denying `delete_database`; Component `src/agent_os/policy/`, `extensions/mcp-server/src/services/policy-engine.ts`. Fold-candidate sharpened: gate writes whose content contradicts the pinned goal/policy envelope, mirroring the policy-mode deny-by-default. |
| ASI-02 Tool Misuse & Exploitation | ASI-02 (tool-misuse capability scoping) | `AGT-OWASP-COMPLIANCE.md` §ASI-02 + Coverage Summary row | **Pattern confirmed & strengthened:** capability-based security (POSIX-style explicit grants read/write/execute/network); Tool Allowlists/Denylists (strict mode blocks `run_shell`, `execute_command`, `eval`); Input Sanitization (command-injection detection, shell-metacharacter blocking); `verify_code_safety` MCP tool; Component capability model + MCP proxy policy rules. (E-5 README-head pattern retained.) |
| ASI-03 Identity & Privilege Abuse | ASI-03 (identity/privilege on write admission) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: AgentMesh — DID Identity & Trust Scoring); §ASI-03 body **UNREAD** (cut at cap) | **Pattern rests on E-5 README head ("zero-trust identity") + component pointer only.** Component: AgentMesh — DID Identity & Trust Scoring. Compliance-doc detailed enforcement pattern is below the cap → UNREAD; no code-level detail certified. Fold-candidate unchanged (record principal on each write; enforce write-permission per principal). |
| ASI-04 Agentic Supply Chain Vulnerabilities | ASI-04 (supply-chain provenance of memory inputs) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: AgentMesh — AI-BOM (model + data + weights provenance)); §ASI-04 body **UNREAD** | **stays named-only — the pattern is not in the staged surface.** Only a component name + one-line summary (AI-BOM: model + data + weights provenance) is certified; the detailed enforcement pattern (how AI-BOM is attached/gated) is below the cap → UNREAD. Component pointer added to fold-candidate for follow-up code-read. |
| ASI-05 Unexpected Code Execution | ASI-05 (code-execution gating on derived memory) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: Agent Runtime — Execution Rings); §ASI-05 body **UNREAD** | **Pattern rests on E-5 README head ("execution sandboxing") + component pointer.** Component: Agent Runtime — Execution Rings. Compliance-doc detailed pattern below cap → UNREAD. Fold-candidate unchanged (scan/block executable content in derived memory before admission). |
| ASI-06 Memory & Context Poisoning | (covered baseline; not a gap) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: Agent OS — VFS Policies + CMVK Verification); §ASI-06 body **UNREAD** | **Baseline retained; component citation gained.** Component: Agent OS — VFS Policies + CMVK Verification (cross-model verification named in the component label). Fold-drafts note's "add CMVK-style cross-model verification" is corroborated at the component-name level; the enforcement detail is below the cap → UNREAD. |
| ASI-07 Insecure Inter-Agent Communication | ASI-07 (inter-agent comms integrity for shared memory) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: AgentMesh — IATP + Encrypted Channels); §ASI-07 body **UNREAD** | **stays named-only — the pattern is not in the staged surface.** Only component name + one-line summary (IATP + Encrypted Channels); detailed pattern (handshake, integrity checks, signatures) below cap → UNREAD. |
| ASI-08 Cascading Failures | ASI-08 (cascading-failure containment in write pipelines) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: Agent SRE — Circuit Breakers + SLOs); §ASI-08 body **UNREAD** | **stays named-only — the pattern is not in the staged surface.** Component name + one-line summary only; detailed pattern (breaker thresholds, SLO wiring, backpressure) below cap → UNREAD. (Note: benchmarks doc §2 receipts circuit-breaker check at 0.0005 ms / 1.83M ops/sec — a latency receipt, not an enforcement pattern; see benchmark receipt below.) |
| ASI-09 Human-Agent Trust Exploitation | (strengthening — currently PARTIAL via landmark replication) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: Agent OS — Approval Workflows); §ASI-09 body **UNREAD** | **stays named-only — the pattern is not in the staged surface.** Component name only (Approval Workflows); no concrete approval-gate mechanism (human-in-the-loop, escalation, timeout) certified. Strengthening from PARTIAL → full remains a fold-candidate, not a gained pattern. |
| ASI-10 Rogue Agents | ASI-10 (rogue-agent kill-switch on write loops) | `AGT-OWASP-COMPLIANCE.md` Coverage Summary row (component: Agent Runtime — Kill Switch + Ring Isolation); §ASI-10 body **UNREAD** | **stays named-only — the pattern is not in the staged surface.** Component name + one-line summary only; detailed pattern (kill-switch trigger, ring isolation mechanics, suspension) below cap → UNREAD. |

---

## Benchmark receipt — the 0.00% claim's staged basis

- **The claim (README head, certified by E-5):** "Prompt-based safety … has a 26.67% policy violation rate in red-team testing. AGT's deterministic application-layer enforcement: 0.00%." The README links `docs/BENCHMARKS.md` for the 26.67%.
- **What the staged benchmarks doc (`AGT-BENCHMARKS.md`) actually receipts (certified portion):**
  - Policy evaluation: single rule 84,489 ops/sec, p50 0.011 ms; 100-rule 32,025 ops/sec, p50 0.030 ms.
  - Kernel enforcement (allow) 9,668 ops/sec, p50 0.103 ms; (deny) 10,239 ops/sec, p50 0.097 ms.
  - Concurrent throughput: ~47K ops/sec stable from 50 to 1,000 concurrent agents.
  - Circuit breaker check: 1,828,845 ops/sec, p50 0.001 ms.
  - Audit: write 285,202 ops/sec (p50 0.002 ms); serialization 343,548 ops/sec.
- **Verdict on the 0.00% claim:** the staged benchmarks doc's certified portion is a **latency/throughput** benchmark (policy eval, kernel, audit, concurrency). It does **not** contain the prompt-safety red-team violation rates (26.67% / 0.00%) in its certified portion. Therefore the 0.00% claim's staged receipt is **not substantiated by the certified bytes here** — it remains a README claim with a link to `docs/BENCHMARKS.md`, whose relevant section (if any) is in the **UNREAD tail** (see wall W2). **Do not treat 0.00% as receipted** until the tail or the upstream file is read.
- **Corollary for the fold-drafts:** the <0.1 ms per-action enforcement cost (receipted above) is the only performance number that can be cited for the write-gate fold-candidates. The 26.67%→0.00% safety number stays a claim, not a receipt.

---

## Walls

- **W1 — Read cap (compliance doc).** `AGT-OWASP-COMPLIANCE.md` is ~15.3K; `read_file` caps at 12,000 chars/call and re-reads return the identical head. Certified: title + Coverage Summary table + §ASI-01 + §ASI-02 + the opening heading of §ASI-03. **UNREAD:** the bodies of §ASI-03 through §ASI-10 (including any closing/limitations sections). No inference was made from them. The tail's existence and size are named; its content is not.
- **W2 — Benchmarks tail.** `AGT-BENCHMARKS.md` is claimed ~9K (under cap) but the certified read ends mid-sentence at "…external append-only stores (e.g., OpenTelemetry export) are recommended for larg…". Trailing bytes (and any prompt-safety red-team section) are **UNREAD**. Treated as unread per the wall clause rather than asserted absent.
- **W3 — Surface, not code.** All citations are documentation surface. The AGT repo was read READ-ONLY; no source was executed, no tests run. "Covered" is the toolkit's own assertion. The component paths (`src/agent_os/policy/`, etc.) are doc-cited pointers, not verified file reads.
- **W4 — E-5 non-rewrite.** The E-5 mapping (three gained + five named-only, from the README head) is preserved; this file extends it with component pointers and one new gained pattern (ASI-01). Nothing in E-5 is contradicted or removed.
- **W5 — Honesty marker discipline.** Four of the eight fold-drafts + ASI-09's strengthening carry the explicit marker "stays named-only — the pattern is not in the staged surface." They are NOT upgraded to "covered" on the strength of a component name alone.

---

## CREATOR-GAPs

- **CG-1:** ASI-04 (AI-BOM), ASI-07 (IATP), ASI-08 (Circuit Breakers + SLOs), ASI-10 (Kill Switch + Ring Isolation) — component names certified, enforcement patterns UNREAD below the cap. These need a code-read next-pass (the AGT repo's `src/` + the compliance doc's tail) to gain concrete patterns; until then they stay named-only.
- **CG-2:** ASI-03, ASI-05, ASI-06, ASI-09 — same: component pointer only; detailed bodies UNREAD.
- **CG-3:** The 26.67%→0.00% prompt-safety claim has no receipt in the certified benchmarks bytes; the claim's basis is in the UNREAD tail (or the upstream `docs/BENCHMARKS.md`). Either read that file or downgrade the claim to "unreceipted" in any downstream citation.
- **CG-4:** The compliance doc asserts "Mappings in place for all 10 risk categories" and "13,000+ tests" — these are the toolkit's own claims; not independently verified here (surface-not-code, W3).

---

## Recommended next moves for the #139606-line's fold-drafts

1. **Fold ASI-01 now** using the gained pattern: add a goal-hijack gate at write time — policy-based action interception with `strict` (deny-by-default) policy mode, mirroring `StatelessKernel` + `ExecutionContext(policies=[...])`, rejecting writes whose content contradicts the pinned goal/policy envelope. Cite `AGT-OWASP-COMPLIANCE.md` §ASI-01.
2. **Strengthen ASI-02** with the certified §ASI-02 detail: bind each memory write to an allowed capability set; reject writes implying out-of-scope tool use (esp. `run_shell`/`execute_command`/`eval`); add `verify_code_safety`-style pre-admission scan. Cite §ASI-02.
3. **Hold ASI-03, ASI-05, ASI-06 as component-cited, pattern-pending**: keep the E-5 README-head patterns; add the component pointers (DID Identity & Trust Scoring; Execution Rings; VFS Policies + CMVK Verification) as follow-up code-read targets.
4. **Keep ASI-04, ASI-07, ASI-08, ASI-09 (strengthening), ASI-10 as named-only** with the marker until a code-read next-pass (CG-1/CG-2) lands concrete enforcement patterns. Do not upgrade on component names alone.
5. **For any downstream citation of the 0.00% number**, either read the benchmarks tail / upstream `docs/BENCHMARKS.md` (CG-3) or cite it as "unreceipted claim." Cite only the receipted <0.1 ms/action enforcement cost in the meantime.
6. **Code-read next-pass** (named, not executed here): read `src/agent_os/policy/`, the AgentMesh AI-BOM/IATP/DID modules, and the Agent Runtime execution rings / kill switch — the surfaces named in the Coverage Summary — to convert component pointers into concrete patterns. This is the named next-pass from E-5 and remains open.

---

## Artifact

Path: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/GOVERNANCE-COMPLIANCE-MAPPING-20261106.md`

**One-line verdict:** the compliance re-read gains ASI-01 a concrete pattern (policy-based action interception) and confirms ASI-02, while ASI-03/04/05/06/07/08/09/10 stay component-cited or named-only behind the cap's wall, and the 0.00% claim is not receipted by the certified benchmarks bytes.