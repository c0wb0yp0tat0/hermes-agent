# CTO-FREEDOM-HARVEST-20261120 — the steer's first fan-out (distilled, receipted)

*The CTO-freedom webstorm's first pass (2026-11-20, the night of the native-rung fire). Four classes fanned, mechanisms distilled, receipts first-hand. Backend note: searxng down (ECONNREFUSED) — served by the keyless tier (exa/parallel); the ladder's trigger, not a null.*

## C1 — THE F6 DOOR'S EXACT TERMS (Continual-ARC submit, first-hand)
- **Admission:** run on the public stream → PR the run directories (results/arc1/… with submission.json; check_result.py rebuilds schedules, no network) → open an ISSUE with the "Verify my learner" form (track, system name+contact, public repo+commit, learner import class, every model named with reasoning effort, budget, GPUs if training).
- **Verified:** they rerun on the private set, fresh undisclosed seed, sandboxed machine (no public network, no set, no key), tracking proxy; then two frozen tests (reset + bare-model comparison; flags when reset plays below the bare model).
- **The budget is a LADDER, not a cap:** "$5 to 1,000" whole dollars (ARC-AGI-3 ≥114 + 21/model) + GPU budget $5–10,000 (Modal pricing) for weight-training learners. Invoiced on the issue, Stripe; OpenRouter 5.5% fee. THE DOOR ENGAGES AT **$5** — the two-way door is literally priced.
- **The one hard constraint:** "We cannot verify a system whose code cannot be shared" — a public repo + commit + import path. THE RIG'S OWN STAGING-HOME (the fork, PR #1) IS PUBLIC — the door is reachable from the study's existing surface.
- **Calibration:** Claude Opus 5.5 ≈95–100% of the private sets; Kimi K3.1 Pro (their endpoint's model) 30% / 27% — the sets read hard; the leaderboard point sits beside the public stream's, never as the same measurement.
- **Allowed ("anything else"):** memory, programs, tools, cache, training the weights; compute logged, never scored; ARC data baked in = void (the pre-registered dead-ends stand).

## C2 — THE WEIGHTS-RUNG (the element's next layer per §5, "weights, not prompt")
- **JitRL** (arXiv 2601.18510) — Just-In-Time RL: TRAINING-FREE test-time policy optimization — non-parametric memory + retrieved-trajectory advantage estimates + LOGIT MODULATION. The zero-gradient rung: the suppression's weight-level lever without any training compute.
- **SDFT** (ICML 2026, PMLR 306) — Self-Distillation Fine-Tuning: a demonstration-conditioned model as its OWN teacher (in-context), on-policy signals, less catastrophic forgetting than SFT. The no-teacher receipt, formalized.
- **u-OPSD** (arXiv 2608.06296) — unsupervised on-policy self-distillation: majority-vote pseudo-solutions under a self-consistency threshold — geniune self-distillation with NO external supervision. The master's "no-teacher self-distillation" receipt, now a recipe.
- **ReSAIL** (arXiv 2609.39306) — the known collapse mode of iterative self-distillation + mitigations (teacher-supported token masking, clipped guidance) — the danger to NAME in any weights-rung run.
- **Experience internalization** (arXiv 2606.04703) — principle-level beats instance-level; step-wise injection; off-policy context-distillation is the more stable supervision — WHAT to distill when the rung fires.

## C3 — THE ADAPTER LEVERAGE (the live production receipt, doubled)
- harness-hub/Qwen3.8-27B-hermes-adapted — LoRA trained with RL INSIDE Hermes Agent (TRL AsyncGRPOTrainer + custom RL envs + OpenEnv + safeagents), Apache-2.0, correctional pens: 29.4→43.1 SWE-bench Pro hard51 (+13.7, p=0.092), 44.7→58.8 Terminal-Bench 2.1 (p=0.029), thinking-off ≈ xhigh at 3.5–4.4× fewer tokens.
- **A GGUF exists** (319 MB adapter, llama.cpp-servable) — the rig's LOCAL FLOOR can serve the adapter class; the recipe publishes Friday.
- @_lewtun's line is the mechanism-in-one: "train a LoRA adapter to be good at each harness separately and swap them at runtime" — per-harness adapters, the seat's own native form (the element's native-grammar rung is the same lever at the prompt layer).

## C4 — THE ARC/HARNESS RECEIPTS (verified + the frontier moved)
- arcprize.org/blog/astra: Astra 62.7% Standard → **99.9% Provider Adapter** ($18.8K, high) — the master's receipt VERIFIED first-hand (the numbers hold).
- arXiv 2610.26632 (PersistGym): the decomposition — σloss 0.860, σnotes **−0.427**, σreplay 0.567 — removing the note-taking instruction LOSES 27 points, native reasoning replay recovers them: the record's PRESENCE + the harness's invitation to use it are levers, measured.
- **The frontier moved (Nov 17, 2026):** GPT-6.2 Astra·Sol 100.00% ARC-AGI-3, Gemini 4 Carbon 99.09%, Claude Fable 5.2 97.72% — the master's receipts date; re-verify before any public use.

## THE STEERS (what the work takes from this)
1. F6's packet skeleton: admission = issue + PR + submission.json, budget ladder $5 up, code-public requirement met by the fork. The study's claim can be submitted at the floor price.
2. The element's next rung (per §5): the weights layer — candidates named: JitRL (zero-gradient, first probe), u-OPSD/SDFT (no-teacher distillation), ReSAIL's collapse caveat; local floor can host the adapter-class (GGUF).
3. The harness note-instruction lever (σnotes −0.427) feeds the native-grammar rung's design — the slot must INVITE the record's use, not just carry it.
