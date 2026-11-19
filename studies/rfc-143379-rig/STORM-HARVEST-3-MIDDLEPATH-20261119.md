# STORM-HARVEST-3 — The third seat: Native Context Editing and the model-managed memory

Scribe-record of the CTO-side web storm (wave 2). The middle path between harness-memory (RFC's seat) and weights (Lenton's seat): the model editing its own context natively.

## The paper (arXiv 2610.25550, "Editing as Language") + project page (dengyl20.github.io/native-context-editing)
- Context = ordered blocks, each named by a two-token address; 70 reserved tokens (64 address + 3 operators drop/rewrite/append + 2 envelope delimiters + 1 lock marker). The model emits edits in its own output; a task-agnostic runtime executes them at end of turn, so the next prompt is built from the edited context.
- Meaning ships with the model ("as the end-of-sequence token does") and holds in every harness — the opposite of harness-dependent compaction.
- **Training**: recorded trajectories contain no edits, so two teachers annotate them — an offline "release" teacher (assigns each block a release point: the turn after which the teacher can CITE the event that ended its use) and an online edit teacher (sees only released blocks, decides when/how to edit). Evolving-context distillation: each edit executes at end of its turn and later decisions are supervised on the resulting context — matching inference exactly, bridging train-test.
- Teachers: GLM 5.3 for both roles, ~180K annotated trajectories.

## The results (LongCat-Flash-Lite-Sparse, 256K budget)
| Bench | Compaction | Tool-call edits | NCE |
|---|---|---|---|
| Terminal-Bench 2.0 | 32.6 | 32.6 | **38.2 (+5.6)** |
| SWE-bench Verified | 65.2 | 62.4 | **70.0 (+4.8)** |
| SWE-bench Multilingual | 56.0 | 54.3 | **62.3 (+6.3)** |
| SWE-bench Pro | 39.4 | 39.7 | **44.9 (+5.5)** |
| Avg | 48.3 | 47.3 | **53.9 (+5.6), tokens −36%** |

- Budget shrinks: NCE's lead over compaction widens to **+9.0 at 128K, +10.1 at 48K**, tokens −26 to −39%. NCE at 64K matches both baselines at 256K with <40% of their tokens.
- Generalizes to Qwen3.6-35B-A3B (+4.5 avg, −15% tokens).
- **The tool-call baseline is the number worth stopping on**: trained on the IDENTICAL edits, it scores *below* plain compaction (47.3 vs 48.3) and saves only 6% of tokens. The gain is not the edits — it's the model expressing edits in its own grammar. Tool-calling editors underperform because the harness's tool schema sits outside the model's native meaning. (Direct relevance to the read-action restore: the RFC's own tool-vs-native seam.)

## The review-lens caveats (sunny34.com review)
- Every benchmark is code/terminal; no GUI/multimodal evidence.
- The defect-rate audit rests on 40 trajectories. Both teacher roles are the same model (GLM 5.3) — its errors could propagate into labels with no independent check.
- **No run counts or variance reported anywhere** — cannot know if the tabulated gaps exceed run-to-run noise.
- NCE is compared against its own reimplementation of MemAct; no head-to-head against Context-Folding or Sculptor.

## The meta (arXiv 2609.40118 ReCAP; 2607.21503 Agentic Context Management)
- ReCAP: persistent context graphs for memory compaction — a new user request can change which history matters, but re-assessing history requires re-encoding it… exactly the read-restore's cost-shape.
- Agentic Context Management: actively managing what the agent holds is a **lifecycle problem, not a store problem** — deciding what to remember, extracting/structure, choosing the store. The RFC's governed-compaction issue is this same lifecycle, already named.

## What fires from this
- NCE is the model-side answer to the RFC's harness-side governed compaction: the RFC governs the cut-point (provenance-origin classification, archive-before-stub, K-recency hard window); NCE hands the same decision to the model in its own language. Both are "the compaction must be governed by what the task still needs" — the two seats converge on one mechanism.
- The release-point teacher's rule — "a block is released only when the teacher can cite the event that ended its use" — is a falsifiable governance rule the RFC's compaction could adopt as its archive-eligibility criterion.
- The RFC's acceptance criteria get an external bar from the field's own curve: compaction that costs >5-10 points of task success (the NCE-vs-compaction gap at every budget, including the 92.5-point truncation penalty in STORM-HARVEST-1) is the current state of the art it must beat.
- The 5-step-after-compaction failure cluster (PersistGym) and NCE's release-point discipline are the same failure class viewed from both seats — the evidence base for the governed-compaction issue's opening position.
