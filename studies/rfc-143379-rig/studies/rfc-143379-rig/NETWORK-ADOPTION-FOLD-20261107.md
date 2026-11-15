# NETWORK-ADOPTION-FOLD-20261107.md — the network-line's adoption-fold (VOI-next, 2026-11-07 01:35)

**Branch:** `study/rfc-143379-rig-20261105`. **Seat:** `stealth/crouton-alpha`. **Register:** receipts, never claims. **Gate:** fork-only; nothing public without the user's word. **Spine:** classify → choose → probe → evaluate → adopt-or-park → standardize → verify (the mechanism-repo's spine, applied to this line tonight).

**Ground (read in order):** `NETWORK-LINE-ANCHORCHAIN-20261106.md`; `NETWORK-EVIDENCE.md` (NETWORK-EVIDENCE-STRONG, round-10); `GOVERNANCE-CODE-RESOLUTION-20261106.md`; the AGT repo at `/root/workspace/repos/agent-governance-toolkit` (docs + named seams, as pinned there); `DEEP-LOOKS-NETWORK-20261106.md` wildcard-seams section. **The 1M-window rule:** lean — no re-reads beyond the above.

---

## [Executive Summary]

The network-line is at **adopt-or-park, not yet adopt**: the #116673 anchor-chain is verified live on this fork (NETWORK-EVIDENCE-STRONG), but the adoption case waits on the upstream's break-glass gate (the installed build's missing `read`). Tonight the line does not wait passively: it **classifies** the case as gate-blocked-but-fork-provable, **chooses** the smallest fork-side probe (cue-conditioned completion on the read-gap), **probes** it without the upstream's gate, **evaluates** it against the check-in's promises, **adopts** the probe's result as the standing compensation, **parks** the upstream adoption with its settle-condition quoted, and **standardizes** the fork-side pattern tonight. Verdict: **ADOPTION-FOLD — PARK upstream adoption, ADOPT fork-side probe; VERIFY by byte-receipt.**

---

## [Analysis Brief]

### (a) ADOPTION-CASE — state (the gate, the seam, the waiting-condition, quoted)

**Classify:** gate-blocked, fork-provable. The case is not evidence-blocked (NETWORK-EVIDENCE-STRONG) — it is build-blocked: the design is live here, the upstream composition is not installed here.

**The gate (quoted):**
> "Read-gap: memory tool has no `read` (removed 56ee8a5cc6); compensation is read_file on INDEX/segments — a two-way door, **removed when #116673 lands in an installed build** (002:48, 002:28 'upstream merge ≠ officially implemented'). The check-in's bounded read is not yet in the running build." — `NETWORK-EVIDENCE.md` §(b) Deltas

**The seam (quoted):**
> "The anchor `@doc:foobar` at `/root/.hermes/memories/MEMORY.md` points at the doc-chain; the chain's INDEX (`:8789/memory-chain/INDEX.md`) is the upstream entry; the segments (001–010 + 009-cbank + 011-doctrine) carry the durable knowledge." — `NETWORK-LINE-ANCHORCHAIN-20261106.md` Exec Summary

Receipts: `MEMORY.md:1` (`@doc:foobar`, 2007 bytes / 9 lines); INDEX 47 lines, reading order INDEX → matching segment → MEMORY.md tip; `002:42` anchor-is-pointer; `002:48` READ-GAP two-way-door; `002:84` full-table read for minting; INDEX chain-link pointers `@doc:session-cto-20261016`, `@doc:session-rhythm-demo-20261016` (sha256 03057eefd701).

**The waiting-condition (quoted):**
> "The #116673 check-in (run 42071103912 @ 60a2e15638, **66 tests GREEN**) is the bounded-read composition pin." — `NETWORK-EVIDENCE.md` §(b)

Adoption waits until that pin lands in an **installed** build — upstream merge alone does not settle it (002:28). Until then the line's standing state is: **compensated, not adopted** (read_file on INDEX/segments as the two-way door).

**Evaluate (against the pin's promises):** convergences hold live — anchor references / downstream remembers (002:42), append-only discipline, read path is a file op (bounded-read contract). The single delta is the read-gap above. Field-lens (AnchorMem decoupling, RippleMem cue-conditioned completion, Chain-of-Memory dynamic chains) maps onto anchor→INDEX→segment; the named next borrow is cue-conditioned completion.

### (b) NEXT-PROBE — the smallest probe that advances the case WITHOUT the upstream's gate

**Choose:** the fork-side verification shape already named by the anchor-chain — **cue-conditioned completion (RippleMem-class) to repair the read-gap without breaking the anchor**. It requires no upstream gate: it runs entirely on the fork (anchor + INDEX + segments + read_file).

**Probe shape (fork-only):**
1. Pick one live segment task (e.g. a 002 lesson lookup). Starting from `MEMORY.md:1` (`@doc:foobar`), follow INDEX → matching segment via `read_file` only (the current two-way door).
2. Add the cue: a cue-conditioned completion step that, given the anchor + INDEX table row, predicts the matching segment + its receipt line (the segment's signature — e.g. 002:42 / 002:48) *before* the read.
3. Score the probe fork-side: cue-hit rate vs segment-read cost (bytes/lines touched), with the byte-verified expected-fact as ground truth (the probe-bank discipline the ladder-battery already enforces — medians over runs, real-cell ground truth).

**Success condition (pre-registered):** the probe advances the adoption case iff it shows, by byte-receipt, that the read-gap can be closed *functionally* on this fork (cue → segment → receipt, anchor untouched) while the upstream gate remains shut. It does **not** claim upstream adoption; it converts "waiting on gate" into "compensated with a measured shape."

**Adopt-or-park for the probe:** adopt the probe's result tonight as the line's standing compensation (an entry in the compensation-bank pattern, 009-cbank: reversible, removal triggered by the installed build gaining `read`). Park only the upstream adoption (§a), with its settle-condition: installed build contains `read` / bounded read, verified by a live memory-tool read (not by merge).

### (c) AGT-READS' SUCCESSOR — the named code-seams the read would settle (file:line forms)

**Classify:** the E-5 deep-looks left AGT head-capped — three fold-drafts gained a concrete pattern from the README's head (ASI-02, ASI-03, ASI-05), five stayed named-only (ASI-01, ASI-04, ASI-07, ASI-08, ASI-10) because the README's enforcement-pattern body sits below the 12K `read_file` cap (**UNREAD**, never inferred). `GOVERNANCE-CODE-RESOLUTION-20261106.md` is the code-reads' first pass; it resolved three of the five (ASI-04 partial-scope, ASI-07 transport-scope, ASI-10 resolved-with-caveat) and left ASI-08 open, plus ASI-01 untouched. The successor read settles exactly what that pass named — no more, no less.

**Ground pin (first-hand, from the resolution pass):** local clone HEAD = `d93e32c`; `git ls-remote origin` HEAD = `d93e32c526ef…`. **The clone is not stale — no remote drift.** Toolkit surface stayed READ-ONLY (`git show` / `git grep` / `git ls-remote` only). Any successor read must re-pin both before trusting line numbers.

**The seams (each would settle one named-only wall):**

| # | Seam | File:line forms (as pinned) | Settles |
|---|---|---|---|
| S1 | ASI-04 policy-interception deny rules | `templates/policies/starters/healthcare.yaml:134` ("# ASI-04: Supply Chain Risk"), `:138` `asi04-supply-chain-tool-enumeration`, `:147` `asi04-supply-chain-dependency-poisoning`, `:156-157` `asi04-supply-chain-plugin-hijack` (`^(install_tool\|register_mcp\|add_plugin\|load_extension)$`), `:162-163` `asi04-supply-chain-config-mutation` (`^(update_config\|edit_env\|set_env\|modify_registry)$`); evaluated at `agent-governance-python/agent-os/src/agent_os/policies/evaluator.py:179-180` (priority sort, first match), `:341` `re.search`, `:220-223` default fallback | ASI-04 partial-scope → whether memory-input provenance can be gated by a deny-rule pattern (today: artifact/tool-call layer only) |
| S2 | ASI-04 artifact provenance | `agent-governance-python/agent-mesh/src/agentmesh/marketplace/sigstore_provenance.py:66` (`ProvenanceAttestation`), `:90` `to_slsa_statement`, `:320` `verify_provenance`, `:337-348` fail-closed, `:351-352` SHA-256 digest compare, `:364-367` cosign bundle, `:370` `verified=digest_match`; test `agent-mesh/tests/test_sigstore_lifecycle_evidence.py:84` | ASI-04 → whether segment/anchor provenance can adopt digest-compare + fail-closed on the fork's chain |
| S3 | ASI-04 SBOM / lockfile drift | `agent-sre/src/agent_sre/sbom.py:45` (`AgentSBOM`), `:153` `to_spdx`, `:217` `to_cyclonedx`, `:278` `hash_file`; `agent-compliance/src/agent_compliance/supply_chain.py` `scan_lockfile_drift` (~`:811`); test `agent-compliance/tests/test_supply_chain.py` | ASI-04 → dependency-drift detection shape for supply-chain content in memory inputs |
| S4 | ASI-07 transport-scope | (resolution pass: RESOLVED transport-scope — integrity at the transport layer) | ASI-07 → whether cross-agent shared-memory integrity can ride the transport pattern; settle-condition: a memory-write-scoped instance (not found in pass 1) |
| S5 | ASI-10 rogue-agent kill-switch | (resolution pass: RESOLVED — code confirms the doc's GAINED, **caveat: no auto-kill wiring found**) | ASI-10 → the successor read hunts the auto-kill wiring (or certifies its absence at the pinned HEAD) |
| S6 | ASI-08 cascading-failure containment | (resolution pass: code-side pointer only, **stays open for the head to assign**; FULL:45 "stays named-only"; FULL:69 CREATOR-GAP-1 names "ASI-04, ASI-07, ASI-08") | ASI-08 → circuit-breaker/backpressure pattern for write pipelines — the largest remaining named-only wall |
| S7 | ASI-01 goal-hijack (unresolved in pass 1) | fold-draft: `GOVERNANCE-FOLD-DRAFTS.md` ASI-01 (goal/policy envelope vs untrusted content) | ASI-01 → whether a policy-interception pattern at S1's evaluator can be scoped to memory-write admission |

**Seam common to S1–S7 (from the resolution pass, binding on the successor):** every pattern found lives at the *artifact / transport / tool-call* layer. **None is memory-write-scoped.** The fold-drafts' "on memory inputs / shared memory / write loops" wording is an *adaptation* this study would make. The toolkit does not ship it. The successor's job is to settle, per seam, **adapt-or-not** — never to claim the toolkit already covers memory writes.

### (d) CLASSIFY-TO-STANDARDIZE — what standardizes tonight, what parks (with settle-conditions)

| Item | Classify | Tonight | Settle-condition |
|---|---|---|---|
| #116673 anchor-chain live instance (anchor→INDEX→segment) | NETWORK-EVIDENCE-STRONG | **Standardize** as the fork's standing read shape (the compensation is the standard until the gate lifts) | Superseded when the installed build gains `read` (live memory-tool read verified, not merge) |
| Read-gap compensation (read_file on INDEX/segments, 002:48 two-way door) | Compensated delta | **Standardize** — adopted tonight as the standing compensation, banked in the 009-cbank pattern (reversible) | Removed when the installed build gains `read` |
| Cue-conditioned completion probe (§b) | Next-probe, fork-provable | **Probe tonight; adopt result** as the measured compensation once byte-receipted | Probe result adopted into 009-cbank with its removal trigger (installed `read`) |
| Upstream adoption of #116673 bounded read | Gate-blocked | **Park** | Installed build contains `read` / bounded read, verified live (002:28) |
| AGT ASI-04 (S1–S3) | RESOLVED (partial-scope) | **Standardize** the partial-scope finding: pattern exists at artifact/tool-call layer; memory-input provenance is an adaptation, not a shipment | Memory-write-scoped provenance instance found at a re-pinned HEAD, or adaptation adopted by the head |
| AGT ASI-07 (S4) | RESOLVED (transport-scope) | **Standardize** transport-scope finding | Memory-write-scoped integrity instance found, or adaptation adopted |
| AGT ASI-10 (S5) | RESOLVED (with caveat) | **Standardize** GAINED-confirmation + caveat; **park** the auto-kill question | Auto-kill wiring found at re-pinned HEAD, or absence certified there |
| AGT ASI-08 (S6) | Named-only (open) | **Park** — stays open for the head to assign | Head assigns the seam; successor read settles it at a re-pinned HEAD |
| AGT ASI-01 (S7) | Named-only (untouched) | **Park** | Successor read scopes S1's evaluator to memory-write admission, or certifies it cannot |
| AGT ASI-02 / ASI-03 / ASI-05 | Concrete pattern (from README head, E-5) | **Standardize** as head-derived patterns | Code-reads confirm or downgrade them at a re-pinned HEAD |

**Verify (tonight, fork-side):** every standardize-row above carries its receipt in this file (MEMORY.md:1, INDEX, 002:42/48/84, run 42071103912 @ 60a2e15638, AGT HEAD `d93e32c`, and the S1–S7 file:line forms). Nothing above the fork is claimed; nothing public.

---

## [Receipts]

- `NETWORK-LINE-ANCHORCHAIN-20261106.md` — anchor `@doc:foobar` (`MEMORY.md:1`), INDEX `:8789/memory-chain/INDEX.md`, segments 001–010 + 009-cbank + 011-doctrine, 002:42/48/84, NETWORK-EVIDENCE-STRONG.
- `NETWORK-EVIDENCE.md` — §(b) check-in run 42071103912 @ 60a2e15638 (66 GREEN), read-gap delta (002:48, 002:28), convergences.
- `GOVERNANCE-CODE-RESOLUTION-20261106.md` — HEAD `d93e32c` = ls-remote; ASI-04 partial / ASI-07 transport / ASI-10 resolved-no-auto-kill; ASI-08 open; S1–S3 file:line forms; common seam (none memory-write-scoped).
- `DEEP-LOOKS-NETWORK-20261106.md` — wildcard: 3 concrete (ASI-02/03/05), 5 named-only (ASI-01/04/07/08/10), README head certified / body UNREAD below 12K cap.
- `GOVERNANCE-FOLD-DRAFTS.md` — the eight fold-drafts' requirement / write-gate / fold-candidate wording (ASI-01, 02, 03, 04, 05, 07, 08, 10).
