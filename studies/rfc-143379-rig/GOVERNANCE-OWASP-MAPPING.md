# GOVERNANCE-OWASP-MAPPING.md — OWASP Agentic Top 10 × rig's L0 write-gate design

**Status:** on-branch finding only (no public post). Feeder for the #139606-line's staged evidence.

## (a) OWASP controls (from fork's OWASP-COMPLIANCE.md)

ASI-01 Agent Goal Hijack · ASI-02 Tool Misuse & Exploitation · ASI-03 Identity & Privilege Abuse · ASI-04 Agentic Supply Chain Vulnerabilities · ASI-05 Unexpected Code Execution · ASI-06 Memory & Context Poisoning · ASI-07 Insecure Inter-Agent Communication · ASI-08 Cascading Failures · ASI-09 Human-Agent Trust Exploitation · ASI-10 Rogue Agents.

## (b) Mapping table — write-gate design mechanisms vs OWASP controls

| OWASP control | Write-gate design mechanism (study records) | Status |
|---|---|---|
| ASI-06 Memory & Context Poisoning | budget-enforcement (write-gate budget, RECEIPTS write-gate battery) | COVERED |
| ASI-06 | acceptance-pipeline (write-gate + memory-tool battery at pins) | COVERED |
| ASI-06 | effect_key replay (effect_key replay / at-most-once admission) | COVERED |
| ASI-06 | at-most-once admission (write-gate admission) | COVERED |
| ASI-06 | landmark-gate (delta-6: landmark-check + replication-before-CONFIRMED) | COVERED |
| ASI-09 Human-Agent Trust Exploitation | landmark-gate replication-before-CONFIRMED (independent review, honest-blind replier) | PARTIAL |
| ASI-01 Agent Goal Hijack | — | GAP |
| ASI-02 Tool Misuse & Exploitation | — | GAP |
| ASI-03 Identity & Privilege Abuse | — | GAP |
| ASI-04 Agentic Supply Chain Vulnerabilities | — | GAP |
| ASI-05 Unexpected Code Execution | — | GAP |
| ASI-07 Insecure Inter-Agent Communication | — | GAP |
| ASI-08 Cascading Failures | — | GAP |
| ASI-10 Rogue Agents | — | GAP |

## (c) Verdict

**GATES-GAPS.** The write-gate's design (budget-enforcement, acceptance-pipeline, effect_key replay, at-most-once admission, landmark-gate) covers only ASI-06 (Memory & Context Poisoning) fully and ASI-09 (Human-Agent Trust Exploitation) partially. Eight OWASP controls (ASI-01, 02, 03, 04, 05, 07, 08, 10) are NOT covered by the write-gate design.

### Fold-candidates for the #139606-line's staged evidence

- ASI-01 goal-hijack gate (policy-based action interception at write time)
- ASI-02 tool-misuse capability scoping on memory writes
- ASI-03 identity/privilege on write admission (who may write)
- ASI-04 supply-chain provenance of memory inputs
- ASI-05 code-execution gating on derived memory
- ASI-07 inter-agent comms integrity for shared memory
- ASI-08 cascading-failure containment in write pipelines
- ASI-10 rogue-agent kill-switch on write loops
- ASI-09 strengthen human-approval gate to full (currently partial via landmark replication)
- ASI-06 keep as covered baseline; add CMVK-style cross-model verification (gap vs fork's VFS/CMVK)

Nothing public posted; finding stays on branch.