# STORM-HARVEST-4 — The economics seam: caching, compaction, and the harness's dollar

Scribe-record of the CTO-side web storm (wave 2). The storm's fourth facet: the money mechanism underneath the harness debate — because the RFC's target state is not just more correct, it is *structured to be cheaper per success*.

## R1 — The Harness Effect (arXiv 2607.06906)
Controlled swap, 22 locked tasks, 6 models, orchestration-layer the only variable:
- **Cost per task −41%** ($0.21 → $0.12), median wall-clock −44% (48s → 27s), tokens per task −38% (14.2k → 8.8k) — quality unchanged (0.78 → 0.81).
- **Quality per dollar +82%**; task completions per M tokens 54.9 → 92.0.
- Efficiency gains are **model-invariant** (every model's cost fell 33–61%); quality gains depend on model: harness leverage correlates with baseline score at **r=0.99** — the *weaker the model, the more the harness improves its quality*. (The free tiers' seat: the harness is the strongest possible upgrade for exactly the models the rig runs.)
- Formal: agent workloads are **input-dominated (~100:1 input:output)**, and effective input price is `p_in · (1 − h(1−κ))`, κ≈0.1 — cache hit rate h is THE most consequential cost variable, and it is determined by the harness's byte-level stability of the prompt across turns, not by the model or provider.
- Their guidance: a **byte-stable prefix** (tool schemas + stable system prompt + append-only durable transcript) with a volatile tail (clock, listings, plan state, reminders) separated as a *correctness rule, not an optimization*; breakpoints after schema catalog / stable system prompt / last durable turns; measured 99.9% cache reads on an identical-prefix call.
- **Compaction and caching are designed together**: a summarizer that rewrote history every turn would destroy prefix stability; checkpoints are stored as durable rows and the rebuilt prompt becomes the *new cacheable prefix*. Sixty-percent history → typed checkpoint (durable memory: decisions/constraints/rejected approaches; 8-section resumability summary; user requirements preserved VERBATIM; active-skill references) + live tail of 4–12 messages at ≤30% of budget, always retained verbatim.

## R2 — PersistGym's caching numbers (arXiv 2610.26632)
- Dropping turns to truncate broke caching: **94% cached → 48%**, making truncation cost **2.9–4.0× more** while using fewer tokens. Truncation is not saving money — it is the most expensive way to save tokens.
- One note-taking sentence at the cut point preserved the cache AND the fact (R2 in Harvest-1). The write-time note is the economics lever.

## R3 — Claude Code's own documented behavior (code.claude.com/docs/en/prompt-caching)
- Compaction "by design invalidates the conversation layer" — the next request has a new shorter history sharing no prefix with the old one; cache rebuilds on the shorter history.
- `/compact` costs the MOST when resuming an old cold session (no cache left to read → reprocess whole history as uncached input). Compaction before the cache TTL lapses is cheaper than after.

## R4 — Superglue + the breakpoint survey (superglue.ai/blog/prompt-caching; satyajit.si/articles/prompt-caching-harnesses)
- Caching requires **exact prefix match** with immutable, provider-native replay of session history; median cache-hit >92% when designed as a correctness rule.
- Breakpoint placement is decisive: a date flipping at turn 21 turns 59,500 tokens of reads into writes (+19% of session cost on Sonnet 4.6); a timestamp at the top makes every request a full write — **25% more than turning caching off**. Proactive compaction *shortly before* TTL expiry can be cheaper than waiting.

## The synthesis — the RFC's seat in the money
The read-restore + governed compaction is the harness-effect pattern at the memory-store layer:
- The doc-chain's append-only cells + the write-time scribe assert = the immutable replay condition caching demands.
- Archive-before-stub = compaction designed WITH caching (the checkpoint becomes the new cacheable prefix; the K-recency live tail = their "live tail always retained verbatim").
- The truncation-without-note failure (PersistGym's 2.9–4.0×) is the current-compaction path's cost shape; the RFC's target state is the byte-stable one.
- **The probe must log cache-hit rates on both arms** (Prediction: substrate > truncated on both correctness AND cost-per-success; the field's numbers say the truncated arm pays 2.9–4.0× for worse answers).

## What fires from this
- Every brief that fires from this series carries a dollar line: the RFC's target state has an economics argument independent of the correctness argument — the same mechanism both.
- The free tiers' strategic seat, field-quantified: r=0.99 harness leverage means the fleet's cheap seats gain the most from harness discipline — the exact doctrine the rig already runs.
- The K-recency window's own home in the economics: a hard window + governed cut keeps prefix stability that truncation destroys — the governed-compaction issue can carry the Harness-Effect economics as supporting evidence.
