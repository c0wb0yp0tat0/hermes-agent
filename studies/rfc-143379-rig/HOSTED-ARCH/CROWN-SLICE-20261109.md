# THE CROWN-SLICE — Hosted-Custom-Code Architecture, Synthesized Whole
**Date:** 2026-11-09 · **Register:** plain, evidence-carrying · **Limit:** ~10 min read · **Status:** design artifact, direct-applicable

## Doctrine (one line)
The architecture is the assistant's *residence* — a brain versioned in the repo, a body unmetered in the rig — not a CI system. GitHub is the spine; the runner is the arm. Every surface below serves that, or it doesn't belong.

---

## 1. THE FULL-LOOP — one page

```
  ┌──────────────┐   push / PR   ┌──────────────┐   dispatch label   ┌──────────────┐
  │   code dev   │ ─────────────► │   GitHub     │ ─────────────────► │  Avrea runner│
  │ (local edit) │               │  (spine)     │  (probe trigger)  │  (arm)       │
  └──────────────┘               └──────┬───────┘                   └──────┬───────┘
        ▲                               │                                 │
        │                               │  workflow_run / status          │  pull
        │                               ▼                                 ▼
  ┌────┴─────────┐               ┌──────────────┐                   ┌──────────────┐
  │ next-code    │ ◄── report ── │  results     │ ◄── artifacts ─── │ build/run/   │
  │ iteration    │               │  (return)    │                   │ report       │
  └──────────────┘               └──────────────┘                   └──────────────┘
```

**Surfaces (four slices, each a distinct responsibility):**
- **Transport** — how code + intent cross the wire (git push, PR, dispatch label, artifact upload). Stateless; the only surface that touches the network boundary.
- **Execution** — the runner pulling, building, running, reporting. Where the body lives; unmetered, self-hosted.
- **Models** — the local-LM engine + model weights + probe battery, treated as *hosted-executed artifacts*, not infrastructure.
- **Return** — results/artifacts → report → next-code iteration. Closes the loop; the only surface that feeds back into code dev.

**Perpetual loop:** dev → host → pull-build-run-report → return → iterate. Each pass leaves evidence (artifacts, logs, verdict). The loop is the product; a single run is just one tick.

**Precedent (dispatch-label-probe):** a label on a PR dispatches a probe run; the runner executes; results attach to the PR. This is the canonical trigger shape — reuse it for every probe battery, don't invent new triggers.

---

## 2. THE LOCAL-LM's PLACE

The local-LM is not "the model server somewhere." It is three *hosted-executed artifacts* that travel through the loop like any other code:

| Artifact | What it is | Where it lives | How it's exercised |
|---|---|---|---|
| Engine | llama.cpp / serving binary | repo (pinned version + build flags) | runner builds it |
| Models | GGUF weights (hash-pinned) | runner cache / artifact store, referenced by hash in repo | runner loads per probe |
| Battery | probe definitions + expected-shape checks | repo (`probes/`) | runner runs; results returned |

**Consequence:** the local-LM is reproducible from the repo. A probe result is a function of (engine commit, model hash, battery version, runner env). Nothing ambient. If you can't reproduce from the repo alone, it isn't a result — it's an anecdote.

**Where it sits in the loop:** Models slice. It is consumed by Execution (runner) and reported by Return. It never sits on Transport's side of the boundary as a service.

---

## 3. THE PARTITIONED-HEAD's RESIDENCE — abstract shape (honest, open questions)

The destination: a dedicated head-layer assistant whose *brain* is versioned in the repo and whose *body* runs unmetered on the runner, connected by this spine.

- **Brain (repo):** prompts, memory, skills, tool definitions, decision logic — all versioned, diffable, reviewable. This is what gets PR'd and reviewed.
- **Body (runner):** inference execution, tool execution, long-running work, probe batteries — unmetered, self-hosted, not billed per token.
- **Spine (this architecture):** the four slices above, connecting brain ↔ body. The loop is the nervous system.

**Mounting (abstract):** the assistant's runtime is a repo-resident program that the runner executes; its state checkpoints land back in the repo (or a repo-referenced store) via Return. The head layer is *partitioned* — reasoning/planning in the brain, execution in the body — so neither side carries the other's cost.

**Open questions (not resolved, must not be faked):**
1. **State residency.** Does assistant state (memory, conversation) live in the repo (git-tracked, slow, auditable) or in a runner-side store referenced by hash (fast, needs sync)? Tradeoff: auditability vs. latency. Undecided.
2. **Trigger granularity.** One dispatch per task vs. a persistent runner session the brain drives? Affects cost and concurrency. Undecided.
3. **Failure semantics.** When the body fails mid-task, does the brain retry, replan, or escalate? No policy yet.
4. **Multi-head.** One assistant per repo, or many heads sharing one runner? Resource contention unknown.
5. **Secrets.** How does the body get credentials without baking them into the brain/repo? Not addressed by current slices.

These are the crown's honest edges. The architecture is a *direction*, not a finished design.

---

## 4. THE CROWN-VERDICT — adoption shape

**What gets built first (single, smallest vertical slice that proves the loop):**
A repo with one probe battery + one dispatch-label trigger + one runner that pulls, builds, runs, and posts a report back to the PR. Nothing else. If that loop closes end-to-end with evidence, the architecture is real; until then it's a sketch.

**Sequence:**
1. **Week 1 — Transport + Execution.** Dispatch label → runner pull-build-run → artifact upload. Prove the arm moves. (Precedent exists: dispatch-label-probe.)
2. **Week 2 — Models slice.** Pin engine + model hashes in repo; runner loads by hash; probe battery runs against local-LM; results returned. Prove the LM is a hosted-executed artifact.
3. **Week 3 — Return loop closure.** Report → PR comment → next-code iteration evidenced by a second commit driven by the first run's output. Prove the loop is perpetual, not one-shot.
4. **Week 4+ — Partitioned-head mounting.** Only after 1–3 close. Tackle the five open questions one at a time, each gated on evidence from the prior step.

**First-release contents (minimal, no extras):**
- `probes/` — one battery, one model target
- `.github/workflows/` — one dispatch-label-triggered workflow
- `runner/` — pull/build/run/report script (self-hosted Avrea)
- `docs/crown-slice.md` — this document
- Pinned engine version + model hash manifest
- **Explicitly NOT in v1:** multi-head, persistent sessions, secrets management, state-sync policy. Each is a later slice gated on evidence.

**Exit criterion for "first release done":** a PR with the dispatch label produces a report comment that a human (or the next code commit) acts on. Loop closed once = architecture adopted.

---

## One-paragraph synthesis
Build the smallest end-to-end loop first — dispatch label in, report out — treating the local-LM (engine + pinned models + probe battery) as hosted-executed artifacts in the repo, not as ambient infrastructure. That loop *is* the assistant's residence in embryo: brain versioned, body unmetered, connected by the spine. Mount the partitioned head only after the loop closes, and only one open question at a time. The architecture's elegance is not in its completeness but in the fact that one loop, closed with evidence, is worth more than five slices described.
