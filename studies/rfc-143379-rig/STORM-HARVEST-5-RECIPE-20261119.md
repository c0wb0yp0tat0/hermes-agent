# STORM-HARVEST-5 — THE RECIPE: the field's own synthesis of harness + weights + memory

Scribe-record of the CTO-side web storm (wave 3, the recipe wave). Wave 1 proved the harness seat; wave 2 found the adversary; wave 3 found the field's own synthesis — the recipe's pieces, published back-to-back, every one a shape the rig already runs.

## The ceiling rule (the decisive paper — arXiv 2610.11655, "Harness Evolution Hits a Ceiling")
The field's cleanest diagnostic, and the one that resolves the Jain-vs-Lenton split:
- **Read the failure composition first.** Label failed trajectories by the FIRST signal that fires: **process failures** (blocked calls, loops, exhausted step budgets) vs **content failures** (a delivered plan that is poor).
- **Harness evolution repairs process failures**; the behaviour it instils can be trained into weights; **content failures are what weight training is for.**
- Receipts: a self-evolving harness (LLM proposes edits to its own harness, judge verifies) lifts Qwen3.5-4B held-out 0.16 → 0.30 and Qwen3.5-9B 0.32 → 0.44 on DeepPlanning; delivery rises 55% → 90% for 4B while loops fall.
- **LoRA adapters trained on evolved-harness trajectories internalise the gain** (+0.13 held-out both sizes; on 4B stacking with the harness more than doubles the score; on 9B the adapter alone matches the full evolution line, cutting content failures from a quarter of trajectories to one in twenty).
- **The placebo control is brutal**: an adapter trained on answer-shuffled trajectories falls BELOW the base model — the gain is in the trajectory content, not the act of training. (The study's never-fabricate discipline, field-encoded.)
- The transfer check: WebArena-Lite (+0.09 on 117 unseen tasks) — and there the gain lives in **what the model sees** (two pages of history instead of one); adapters trained on those trajectories add nothing. "Train in the gains that changed what the model writes; keep the harness for the gains that changed what it sees."
- Translation to the rig: the doc-chain is a "what it sees" harness gain; the scribe-cells + fold + skilled memories are the "what it writes" layer. The ceiling rule tells us which lever each of our known failure classes belongs to.

## SIA — the two schools, unified (arXiv 2605.27276; ICML SIA-W)
- The field's own split: the harness-update school (meta-agent rewrites scaffold, weights fixed) and the test-time-training school (RL pipeline updates weights, harness fixed) **operate in isolation**. SIA unifies: a Feedback-Agent observes each trajectory and dynamically selects — at each step — the harness update OR the training-algorithm update, conditioned on task type and reward dynamics.
- Receipts: SIA-W+H beats scaffold-only on all three domains: +25.1% over prior SOTA on LawBench; GPU kernels 1,017 vs 1,161 µs (12.4% faster); +20.4% on single-cell RNA denoising.
- Their one-liner is the recipe's thesis: "Harness updates make the model agentic, shaping how it searches and acts, while weight updates build the domain intuition that no prompt or scaffold can instil."

## Co-Harness — the dual-loop recipe (arXiv 2607.22688)
- Alternates harness optimization and model optimization: an LLM **HarnessCritic** analyzes failed trajectories, attributes each to a structured harness-level cause (prompt ambiguity, tool schema error, missing skill, middleware mismatch), proposes local harness diffs — accepted only if validation rollouts improve the targeted failure mode without regressing held-out behaviours. The improved harness then generates the trajectories the model is fine-tuned on.
- The flywheel, verbatim: "Better harness → better trajectories → stronger model → better harness."
- Receipt: a 200+ hour autonomous case study — recovers from system crashes, improves inference efficiency, discovers ensemble strategies without human intervention.
- Translation: the rig's ACES verdict loops + review-loop discipline are a manually-run HarnessCritic; the envelope machinery is the validation gate; the study's own folds are Co-Harness's "accepted diff" cycle.

## ClawLoop — no external teacher (arXiv 2610.14118)
- Self-improving in general-purpose harness environments **without any external teacher model**: task synthesis (diagnosis-conditioned difficulty growth + agent-free/agent-based validation) → training (SFT/RL) → diagnosis/feedback (capability report feeds the next iteration).
- Receipt: Qwen3.6-27B as the loop model improves on SkillsBench, Claw-Eval-Live, ClawGym-Bench; iteratively refined tasks transfer to Qwen3.5-4B and 9B with gains (data quality validated independently of the loop model).
- Translation: the rig's copycat-harness rounds + free-seat rotation are a distributed ClawLoop; Continual-ARC's "no tuning to the stream" verification is the same no-teacher honesty.

## What fires from this
- The recipe is not three positions debating — it is ONE ladder with a diagnosis rule: **process failures → harness; content failures → weights; gains in what the model writes → train; gains in what it sees → keep in the harness.**
- The study's seat is now field-anchored as the base of the ladder, and the ladder's next rung (weight internalization) is a named, receipted path — not a threat to the doc-chain thesis but its extension.
- Every one of these papers names the rig's shapes (HarnessCritic = verdict loops; validation gate = envelope machinery; no-teacher = self-firing lanes) — the storm's expected meta-finding, now five receipts deep.
