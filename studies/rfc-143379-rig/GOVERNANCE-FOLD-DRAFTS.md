# GOVERNANCE-FOLD-DRAFTS.md — the eight OWASP-gap controls' staged fold-drafts

**Status:** on-branch finding only (no public post). Staged evidence for the #139606-line. Each draft is one page: control requirement · write-gate current state · concrete fold-candidate · evidence-links. Nothing here is posted anywhere.

## ASI-01 Agent Goal Hijack
- **Requirement:** an agent's goal/policy must not be overridden by untrusted content (memory, tool output, context).
- **Write-gate current state:** no policy-based action interception at write time; the gate covers budget/enforcement/acceptance/effect_key/at-most-once/landmark only (ASI-06).
- **Fold-candidate:** add a goal-hijack gate — policy-based action interception at write time, rejecting writes whose content contradicts the pinned goal/policy envelope.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-01 GAP; RFC-GUIDANCE DELTA-3 authority rule (authority never lifts itself).

## ASI-02 Tool Misuse & Exploitation
- **Requirement:** tool capabilities scoped to least privilege; memory writes cannot smuggle tool misuse.
- **Write-gate current state:** no capability scoping on memory writes.
- **Fold-candidate:** tool-misuse capability scoping on memory writes — bind each write to an allowed tool/capability set; reject writes implying out-of-scope tool use.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-02 GAP.

## ASI-03 Identity & Privilege Abuse
- **Requirement:** who may write must be authenticated/authorized; privilege not abused via memory.
- **Write-gate current state:** no identity/privilege check on write admission.
- **Fold-candidate:** identity/privilege on write admission — record principal on each write; enforce write-permission per principal.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-03 GAP; RFC-GUIDANCE DELTA-3 authority rule.

## ASI-04 Agentic Supply Chain Vulnerabilities
- **Requirement:** provenance of memory inputs tracked; untrusted supply-chain content flagged.
- **Write-gate current state:** no provenance tracking on memory inputs.
- **Fold-candidate:** supply-chain provenance of memory inputs — attach source/provenance metadata; gate writes lacking trusted provenance.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-04 GAP.

## ASI-05 Unexpected Code Execution
- **Requirement:** derived memory must not trigger code execution.
- **Write-gate current state:** no code-execution gating on derived memory.
- **Fold-candidate:** code-execution gating on derived memory — scan/block executable content in derived memory before admission.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-05 GAP.

## ASI-07 Insecure Inter-Agent Communication
- **Requirement:** shared memory integrity across agents; tampering detected.
- **Write-gate current state:** no inter-agent comms integrity check on shared memory.
- **Fold-candidate:** inter-agent comms integrity for shared memory — integrity checks/signatures on cross-agent shared memory writes.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-07 GAP.

## ASI-08 Cascading Failures
- **Requirement:** write pipelines contain failures; no cascade.
- **Write-gate current state:** no containment in write pipelines.
- **Fold-candidate:** cascading-failure containment in write pipelines — circuit-breaker/backpressure on write loops; isolate failing writes.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-08 GAP.

## ASI-10 Rogue Agents
- **Requirement:** rogue agents can be stopped from writing.
- **Write-gate current state:** no kill-switch on write loops.
- **Fold-candidate:** rogue-agent kill-switch on write loops — per-agent write-rate/loop detection with automatic admission suspension.
- **Evidence-links:** GOVERNANCE-OWASP-MAPPING.md §(c) ASI-10 GAP.

## Notes
- ASI-06 (Memory & Context Poisoning) remains the covered baseline (budget-enforcement, acceptance-pipeline, effect_key replay, at-most-once admission, landmark-gate). ASI-09 (Human-Agent Trust Exploitation) partial via landmark-gate replication-before-CONFIRMED; strengthen to full human-approval gate is a separate fold.
- All drafts staged on branch only; nothing public posted.

## APPENDIX-20261106 — the three resolved patterns (head-side fold, cited to GOVERNANCE-CODE-RESOLUTION-20261106.md)
- **ASI-04 (Agentic Supply Chain) RESOLVED:** the enforcement-patterns staged from `agent-governance-toolkit` `templates/policies/starters/healthcare.yaml` — `:138` `asi04-supply-chain-tool-enumeration` · `:147` dependency-poisoning · `:156-157` plugin-hijack (the `install_tool|register_mcp|add_plugin|load_extension` condition) — the provenance-tracking rule the FULL-marker said was absent now exists in the policy-surface. (S-1: the policy-template is the RULE-SURFACE; its enforcement in the service-layer remains to be receipted.)
- **ASI-07 (Insecure Inter-Agent Communication) RESOLVED:** the integrity-rule staged from `agent-mesh/src/agentmesh/`: `encryption/ratchet.py` `:363-380` (ChaCha20Poly1305 AEAD, `_encrypt` random-nonce + `_decrypt` tag-mismatch raise, `:267/:280` AAD-bound header) — the shared-memory tampering's integrity-rule the marker said was absent now cites code. (S-1: the encryption's key-rotation + the mesh's cross-agent usage remain to be receipted.)
- **ASI-10 (Rogue Agents) RESOLVED [the marker-corrected: FULL:47 had GAINED already]:** the kill-switch's shape staged from `agent-hypervisor/src/hypervisor/security/kill_switch.py` `:28-36` (the six KillReasons incl. BEHAVIORAL_DRIFT + QUARANTINE_TIMEOUT) · `:129` `kill(...)` · `:144-157` the substitute-handoff · `:171-173/:200-233` the timeout-guarded termination-callback. (S-1: the hypervisor's CALLING-surface's wiring remains.)
- The cardinal S-1 warning (the apex's own): no fold-draft's code-citation cites the benchmark's `verify.py` table as OWASP evidence — the 0.00%-claim's baseline is a SIMULATED LLM (`random.random()`), mis-fired as evidence.
