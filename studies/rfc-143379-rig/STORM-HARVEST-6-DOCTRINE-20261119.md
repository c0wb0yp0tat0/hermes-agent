# STORM-HARVEST-6 — FLEET DOCTRINE + THE MONEY LAW: parallel teams, two-way doors, small-model recipes

Scribe-record of the CTO-side web storm (wave 3, the doctrine wave). The recipe's operating shapes: how fleets of cheap seats beat single models, the field's version of Bias for Action, and the small-model training receipts that make the ladder's top rung cheap.

## R1 — Parallel teams beat parallel individuals (arXiv 2611.09798, "Test-Time Compute Scales Better with Parallel Agent Teams")
The fleet's theorem, field-proven at 100-agent scale:
- Best-of-N sampling of independent agents saturates quickly (low mean); one large collaborating team stops improving as it grows (no variance gain). **Many small teams in parallel balance high mean with variance.**
- Receipts (12 long-horizon tasks: GPU kernels, formal proofs, exploit development): with a 27B model and a budget of 100 agents, **parallel teams of ten beat 100 parallel agents on 10 of 12 tasks and beat one team of 100 on all four tasks tested**; at equal dollar cost, parallel teams beat a frontier model on half the tasks.
- Translation: the rig's lane fan-out (one seat per lens, merge by a flagship) is the field's parallel-teams shape — the study's own OPUS-2 envelope already runs it.

## R2 — Parameterized sparing: M1-Parallel and Fleet-of-Agents (arXiv 2507.08944; MLR 267/klein25a)
- M1-Parallel: multiple teams in parallel with early-stop (2.2× speedup at preserved accuracy) or aggregation (higher completion); the failure diary is a global memory — failed plans + logs feed the next plan generation.
- FoA (Fleet of Agents): genetic-type particle filter over agents exploring a search tree; **~35% of the cost of previous SOTA at +5% absolute quality**; FoA+LLaMA3.2-11B **surpasses LLaMA3.2-90B solo** — the free tiers' theorem, receipted: coordinated small seats beat an uncoordinated big seat.
- Translation: the rig's copycat-harness IS FoA's particle filter — multiple cheap seats exploring, selection by evidence — with the write-window/429 discipline as the fitness function's guard.

## R3 — PANDA's governance (arXiv 2609.38482)
- Decentralized collectives: agents discover each other's capabilities, self-organize into small teams per task; star/chain/mesh topologies chosen per task; web-of-trust governance with no centralized service; infrastructure failures trigger dynamic replanning.
- Receipts: scales to thousands of agents; matches SOTA accuracy at up to 8× efficiency; sustains 100% task completion under faults where existing systems fail.
- Translation: the fleet's self-hosted runners + fork-web + trust-gated posts are PANDA's web-of-trust — already built, now field-named.

## R4 — The money law (the two-way door doctrine, AWS/Amazon doctrine)
- The canonical framing (AWS Executive Insights, Jassy 2020 keynote): most decisions ARE two-way doors (reversible, low cost of undo) and get wrongly treated as one-way; **"with about 70% of the data you wish you had — waiting for 90% or more means you are likely moving too slow."**
- The one-way/two-way test governs where to Dive Deep vs Bias for Action; reversible decisions are precisely where experimentation multiplies learning ("the learning that comes from these decisions is often invaluable, and the cost of undoing it if it is a mistake is low").
- Translation: the study's two-way-door sprints are this doctrine, already operationalized — the 70% rule is the anti-gate the fleet runs; the storm's every document is built to keep doors two-way (each fire names its reversibility and rollback).

## R5 — The small-model ladder's receipts (the top rung is now cheap)
- **Agentic-DPO** (arXiv 2607.10601): offline, no environment rollouts, no reward model — converts expert trajectories into state-conditioned preferences; τ-bench 21.7% → **41.4% at 9B** (matching online GRPO at the same backbone); Qwen3.5-2B on StableToolBench 57.1% → **90.9%**.
- **MemRL** (arXiv 2601.03192): non-parametric — RL on episodic memory, **no weight updates**; two-phase retrieval filters noise; reconciles stability-plasticity (the forgetting problem Lenton named), improving continuously at runtime on HLE, BigCodeBench, ALFWorld, Lifelong Agent Bench.
- **OPD-Evolver** (arXiv 2606.17628): slow-fast co-evolution; fast loop runs a four-level memory hierarchy (trajectories → tips → skills → tools) with outcome-calibrated memory attribution; slow loop distills into the policy via on-policy self-distillation; **OPD-Evolver-9B challenges QWEN3.5-397B and STEP-3.5-FLASH** — memory-management internalized.
- **Tmax** (terminal agent recipe, 9B): 27% on Terminal-Bench 2.0 with a simple outcome-only RL recipe and an open dataset 2.5× larger than prior terminal-agent datasets.
- **DeepSearch-World** (arXiv 2607.07820): verifiable-environment self-distillation — 420K multi-hop tasks; scaffold process supervision converts teacher trajectories into ReAct supervision; 11 evolving rounds; **DeepSearch-World-9B: +48.1 HotpotQA, +37.6 GAIA** — self-evolution from its own verified experience, no proprietary teacher.
- Translation: the ladder's top rung (weights) no longer needs labs — the receipts are 4B/9B/27B open models trained cheaply on own-trajectories; Continental-ARC's 0.45/0.27 weights numbers (Qwen3.5-9B + GLM teacher) are now reproducible rig-side with the same weight class.

## What fires from this
- The doctrine wave completes the recipe's four corners: **harness (process) + memory (episodic) + weights (content) + fleet (parallel-teams economics)** — and the two-way door is the operating law that lets the sequence fire without self-gates.
- The fleet's strategic identity gets its receipts: coordinated cheap seats beat big uncoordinated seats (FoA), parallel teams beat both solo agents and one big team (parallel-teams), and the field's open recipes make the weight rung a two-way door too.
- The connect-the-dots map (the next document) draws from all six harvests: the dots are the receipts, the lines are the doctrine.
