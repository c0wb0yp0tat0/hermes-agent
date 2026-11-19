# STORM-HARVEST-1 — The harness field: what the field proved about harness-over-model

Scribe-record of the CTO-side web storm (wave 1 of 2). Every claim carries its receipt; nothing here is the RFC's vetted truth — it is the storm's source, pending enrichment.

## The question
Can a cheap, fallible model be made reliable by the substrate around it — not by the weights? And is that the same question the RFC asks?

## R1 — The behavioral-harness experiment (Martin Fowler / Naresh Jain, Oct 2026)
Same API service built twice: bare vs harnessed (control + verification + guarded post-conditions).
- **3/10 passes bare → 10/10 harnessed** on Luna class. One-sided Fisher exact p < 0.01.
- Harnessed run: $0.273/run — **33% cheaper than unharnessed Sol** at $0.406. The harness bought BOTH correctness and cost.
- Jain's line: "Luna came remarkably close on its own — 94.8% of checks passed; it was stumbling over subtle edge cases." Reliability, not capability.
- Receipt: martinfowler.com (Naresh Jain interview), Oct 2026.

## R2 — "When the harness decides success" (PersistGym, arXiv 2610.26632)
Pre-registered probe on **gpt-6-luna itself**; the read-restore question, run by the field:
- Full history: **200/200**. Truncated window with one *non-re-observable* fact: **7.5% — chance level. −92.5 points.**
- One note-taking sentence at the cut-point rescued it to **28.5%**.
- Compaction finding: **failures clustered in the five steps after a compaction.**
- Economics: dropping turns broke caching (94% cached → 48%), so truncation cost **2.9–4.0× more** while using *fewer* tokens.
- Translation: the 14-line read removal (56ee8a5cc6) turned recoverable into non-recoverable; the field's probe measured the penalty of that class on the accused model itself.

## R3 — The memory layer beats the reasoning dial (ARC-AGI-3 harness gap, $26K verification scale)
- Astra 62.7% (Standard harness) → **99.9% (Provider Adapter: reasoning replay + compaction + extraction-to-notes)**. Same weights, different memory rules.
- Even at reasoning `none` with tools: 96.7%. "Memory handling, not raw reasoning, is doing most of the work."
- The adapter's "extract to external store" step is a scribe-cell in field dress.
- Receipt: docs.google.com/document/d/1n0aFg9GIPowYDnX_WY5yPdFrqMCM70SsZ0R3UxCBxQI (ARC Prize verification).

## R4 — The effort dial (the Teknium-chart nuance)
- Teknium's chart (Luna medium effort, 6.24 steps / 38 solved) is **one point on a free dial** — medium, unwrapped.
- ARC's own effort ladder (Luna): low 37.7% → medium 61% → max 86.7% (ARC-AGI-1).
- Overthinking is a known failure: Ares (arXiv 2603.07915) — adaptive effort, medium can beat high; laddering start-low-escalate (arXiv 2610.34491) matches or beats fixed top effort everywhere tested.
- The dial and the harness are independent levers; the field stacks them (Jain ran harnessed + low/medium effort).

## What fires from this
- The harness is the reliability lever — field-verified twice over (R1, R2) with receipts and p-values.
- The read-restore's hypothesis is the field's frontier question, already probed with Luna as the witness.
- Probe shape (two-arm, PersistGym protocol): raw-truncated vs substrate on the non-re-observable-fact class, ~200 episodes/arm, cache-hit rates logged on both arms.
- Prediction to falsify: substrate recovers the majority of the 92.5-point gap at *lower* cost-per-success than the truncated arm.
