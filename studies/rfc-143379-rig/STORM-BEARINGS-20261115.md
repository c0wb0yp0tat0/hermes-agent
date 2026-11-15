# THE LOAD-BEARING FINDINGS MAP
| Mechanism               | On-Disk Location(s)                                                                 | Rig Shape                                                                                     | Receipt                                                                                     |
|-------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **DISCERN**             | Harvest report (arXiv 2611.15729)                                                   | Write-gate L0 + SPA-DREAM read path                                                          | Entity resolution 0.800 vs ≤0.40 baselines; zero-LLM navigation.                          |
| **MemCredit**           | Harvest report (arXiv 2611.15600)                                                   | Memory-economy ρ=(V−λH)/b arbitration at bank, not delivery                                  | 86.9% of interventions move nothing; decision-utility credit assignment.                     |
| **MAPE**                | Harvest report (arXiv 2611.17068)                                                   | Design-space search for inventions-live probes                                             | +12% at 35% serving cost; program evolution of whole memory programs.                       |
| **CoMem**               | Harvest report (arXiv 2611.16384)                                                   | Fidelity-ladder L2 selection algorithm                                                      | 4× matches uncompressed at 4×; contrastive selective compression.                           |
| **Reward-Driven Collider** | Harvest report (arXiv 2611.15885)                                                 | AIMD adaptive-envelope reward path                                                           | Continuous-reward RL.                                                                     |
| **AskALCF**             | Harvest report (arXiv 2611.15700)                                                   | Evidence-gated RSI admission + commit gate                                                  | Two-scope sufficiency + controlled harness training.                                       |
| **SELD**                | Harvest report (arXiv 2611.12903)                                                   | Read-side evidence-plane verifier                                                            | 83% vs 70% silent evidence-loss detection (no-training/no-labels).                           |
| **Evolving Infra**       | Harvest report (arXiv 2611.12304)                                                   | Agent-adaptive PD split + agent-aware KV manager                                             | 4.1× latency, 14× P95 TTFT over Dynamo.                                                  |
| **Together Compiler**   | Harvest report (arXiv 2611.14681 + RTL op 2611.13935 + grammatical-expiration 2609.36457) | Compile-time gating, stage-decoupled evaluation, validity decay                             | RTL op decoupling + SQL-debugging study (three-state delegation).                          |

---

## THE NUANCE
- **DISCERN**: Write-gate L0 blind spot (acceptance-gate) unverified; read-side resolution axis (DISCERN resolve-at-read + SELD) is open.
- **MemCredit**: Decision-utility vs semantic relevance gap (ρ=-0.011 vs 0.176); arbitration at bank (not delivery) is untested.
- **MAPE**: Design-space search lacks live probes for F_used/held-out; Agent Plasticity integration pending.
- **CoMem**: Fidelity-ladder L2 selection algorithm (contrastive) is unpaired with L2 missingness (SELD).
- **Reward-Driven Collider**: AIMD adaptive envelope path is untested; continuous-reward RL is theoretical.
- **AskALCF**: Evidence-gated admission + commit gate is untested; two-scope sufficiency is current baseline.
- **SELD**: Read-side evidence-plane verifier is unpaired with write-gate L0; missingness detection is unvalidated.
- **Evolving Infra**: Agent-adaptive PD split + KV manager is untested; latency/TTFT claims need replication.
- **Together Compiler**: RTL op decoupling and validity decay (grammatical-expiration) are unvalidated in production.

---

## THE TARGET SHAPES
| Shape                          | Current State                                                                 | Open Axis                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Write-gate L0                  | Acceptance-gate blind spot (Masked Erosion)                                  | Read-side verification hook (DISCERN + SELD).                                               |
| Fidelity ladder L2              | Refusal-alignment-under-compression (62.82→10.9%)                           | L2 SELECTION (CoMem) + L2 MISSINGNESS (SELD).                                                |
| Memory economy ρ=(V−λH)/b      | Decision-utility vs semantic relevance (ρ=-0.011)                           | Arbitration at bank (not delivery); validity decay (grammatical-expiration).                |
| RSI admission                  | Two-scope sufficiency                                                        | Evidence-gated admission + commit gate (AskALCF).                                           |
| AIMD adaptive envelope          | Theoretical (continuous-reward RL)                                           | Adaptive-envelope reward path (Reward-Driven Collider).                                      |
| SPA-DREAM read path            | Fold-not-compression, doc-chain anchors                                      | Zero-LLM navigation + as-of/entity contrast (DISCERN).                                      |
| Inventions-live probes         | Design-space search (MAPE)                                                   | F_used/held-out probes (Agent Plasticity).                                                   |
| Agent-adaptive serving         | PD split + KV manager (Evolving Infra)                                        | Agent-aware latency/TTFT validation.                                                         |

---

## THE ENRICHMENT REGISTER
1. **READY**: Comment on PR #139606 (NousResearch/hermes-agent) → Cite DISCERN + SELD, propose read-side verification hook on write-gate admit/reject axis.
   - **Surface**: PR description section.
   - **Edit**: Add bullet: *"Propose integrating DISCERN’s resolve-at-read with SELD’s evidence-plane verifier for write-gate L0 validation."*
   - **Why**: Unverified read-side resolution axis is a critical blind spot.

2. **READY**: Issue proposal "read-side evidence plane for compression-fidelity" (NousResearch/hermes-agent) → Cite SELD + CoMem + L2 missingness.
   - **Surface**: GitHub Issues → "Memory Compression & Fidelity" label.
   - **Edit**: Draft: *"Propose a read-side evidence plane to validate CoMem’s L2 selection against SELD’s missingness detection, ensuring fidelity ladder integrity."*
   - **Why**: Current L2 selection lacks missingness validation.

3. **NOT-READY**: Public storm-fold posting → Requires approval; staging list remains unchanged.

---

## THE OWED LIST
- **ABSENT**: Exact contents of `/root/.hermes/cache/scratch/arxiv-watch/state.json` (Nov-10→12 preprints).
- **ABSENT**: Remote PR states (e.g., #139606’s exact discussion).
- **ABSENT**: Validation of Together Compiler’s RTL op decoupling in production.
- **ABSENT**: Replication of Evolving Infra’s latency/TTFT claims across substrates.