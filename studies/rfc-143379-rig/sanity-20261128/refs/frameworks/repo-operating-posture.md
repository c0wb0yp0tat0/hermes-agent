# Repository Operating Posture — mechanism-of-mechanisms as a doctrine practice ground

> This is a private practice repo. It holds the mechanism-of-mechanisms framework
> AND reflects how that framework is actually lived. What follows is the operate-level
> contract for the repo itself: why it exists, what doctrine it reflects, how it stays
> current, and the two-way-door posture that governs private changes to it.

## Why this repo exists

This repository is the practice ground for the mechanism-of-mechanisms framework.
It is where the framework is written down AND where it is demonstrated on itself.
The framework is the doctrine; this repo is one place where that doctrine is kept
current, auditable, and honest about what it has earned versus what it still marks
as a `CREATOR-GAP`.

The framework lives in:
- `CONCEPTS.md` — the mechanism model, spine, status vocabulary, and design commitments.
- `schemas/dispatch-envelope.md` — the worker contract: operating principles, reasoning
  protocol, required response sections, and integrity rules.
- `docs/invention-kb-map.md` + `docs/method-cards.md` + `mechanisms/CATALOG.md` — the
  reconciled 40-mechanism, 8-family inventory with trigger, essence, failure-risk,
  rollback, and success-signal.
- `docs/graditum-ferociter-profile.md` — the portable load order and dispatch rules.
- `workflows/minimal-run.md` — the smallest runnable spine.
- `agents/` — provider-neutral agent behavior and adapter contract.
- `validation/` — run-artifact contract checker, repository-level checker, and the
  responsibility-tracker automation validator.
- `docs/nousresearch-responsibility-tracker.md` + `scripts/update_responsibility_tracker.py`
  + `schemas/` + `validation/validate_responsibility_automation.py` — the Copilot-built
  responsibility tracker with refresh workflow and live data (generated from public
  GitHub data for `NousResearch/hermes-agent`).

## What doctrine this repo reflects

### The spine
The repo is built on the controlled-learning spine documented in `CONCEPTS.md`:

```text
classify -> choose -> probe -> evaluate -> adopt or park -> standardize -> verify
                                     ^                         |
                                     +------ meta-review ------+
```

The minimum spine (`workflows/minimal-run.md`) is: deconstruct → sense → choose →
calibrate → probe → review → record → compose-check. Every material task in this repo
starts there; optional mechanisms are selected by value of information, never all 40
as always-on.

### The dispatch envelope
Every worker or subagent dispatch in this repo is primed with `schemas/dispatch-envelope.md`:
the six operating principles (Customer Obsession, Ownership, Bias for Action, Deliver
Results, Learn and Experiment, Self-Reference), the 5-step reasoning protocol, the five
required response sections, and the binding integrity rules. The envelope is the lane
contract; the head layer (`head-supervisor-think-tank`) orchestrates and folds.

### The inventory
The repo carries the reconciled 40-mechanism, 8-family inventory with explicit status
vocabulary (`described` / `referenced` / `contracted` / `capability-tested` / `routine-tested`
/ `portable` / `proven-value` / `parked`). A mechanism is not proven because it sounds
useful; status claims carry evidence appropriate to their level.

### The learning loop (ACES)
The repo is kept current through the ACES cycle applied to itself:

- **Assess** — read the repo against the earned doctrine; itemize what it reflects and
  what it does not (this document is one such assessment).
- **Create** — make targeted, structure-preserving additions or edits; subtract where
  possible; never invent mechanisms — extract what is documented and label the rest
  `CREATOR-GAP`.
- **Evaluate** — run the 3-lane blind rotation (primary free tiers + the preferred
  deepseek-flash co-base where the leg genuinely needs it) and adjudicate cold before
  anything lands.
- **Sustain** — keep the ACES contract visible, re-read the posture doc on a named
  cadence, and let new findings re-enter the plan loop rather than riding along as
  inline patches.

### The LP anchor
The behavioral root of this framework is the 14 Amazon Leadership Principles as a closed,
self-reinforcing loop (see `OLD-SCHOOL-AMAZON-LPS.md` in the mission-flow tree for the
anchor). The dispatch envelope's operating principles, the spine's design commitments, and
the head-supervisor skill's rule-to-LP map all trace back to that anchor. The repo does not
redistribute the full LP text; it points at the anchor and keeps the relationship visible
so the shape of the envelope has a stated reason to be shaped that way.

### The landing conventions
- **status = reality** — a mechanism is reported `FIRED / DORMANT / MIS-FIRED / CORRECTLY-ABSENT`
  with observable evidence, never a bare claim.
- **tracker altitude** — the responsibility tracker (`docs/nousresearch-responsibility-tracker.md`)
  is generated from a machine-readable schema + registry, validated by
  `validation/validate_responsibility_automation.py`, and refreshed by
  `scripts/update_responsibility_tracker.py`; the tracker stays at the altitude of what
  the schema says, not what a live run improvises.
- **single-writer fold** — workers write distinct artifacts or deltas under `runs/`;
  only the parent (or designated fold step) updates a shared index.
- **two-way door** — every significant change to this repo is a two-way door with a named
  rollback; private-repo changes are silent under greenlight; nothing in this repo is a
  one-way door, including merges to main. Real one-way doors are public surfaces only.
- **evidence over self-report** — a passing validator means the artifact contract is
  well-formed, not that the reasoning was correct; the repo keeps that distinction explicit.

## Two-way-door posture for this private repo

- This is a PRIVATE repo. Private-repo writes and merges are TWO-WAY DOORS — silent under
  greenlight, structure-preserving, backup-first.
- Step-0 backup gate FIRST: before any multi-file edit, snapshot every distinct file by
  relpath (namespaced to avoid basename collisions), assert the snapshot count equals the
  source tree file count, and only then edit.
- Do not break the refresh workflow (`scripts/update_responsibility_tracker.py` + the
  generated tracker/docs/state/digest) or the validators (`validation/validate_run.py`,
  `validation/validate_repository.py`, `validation/validate_responsibility_automation.py`).
- Anything public is a real one-way door and needs explicit word. This doc and the edits it
  authorizes stay private.
- Every dispatch passes the price gate and carries an explicit `max_tokens`.

## How this repo stays current (the ACES contract for the repo itself)

1. **Assess** — when the repo's reflection of the earned doctrine needs a look, an
   assessment runs the spine: deconstruct the ask, classify the domain, probe the repo as
   it actually is, record what reflects and what gaps. The assessment writes a HITL decision
   doc in the schema envelope shape (Executive Summary / Analysis Brief / Recommendation-Action
   Plan / Next Steps-Exploration / Artifact) plus the Assess findings, the Create plan, the
   Evaluate record (rotation verdicts + cold-read adjudication), and the Sustain leg.
2. **Create** — approved changes are structure-preserving additions or light calibration
   edits; the tracker and validators are left intact; new doctrine is not invented — existing
   doctrine is surfaced, and anything unresolved is labeled `CREATOR-GAP`. When the user's
   steer calls for building, the repo's Copilot agent infrastructure (.github/agents/,
   the refresh automation pattern) is the building tool; builds follow the proven template:
   agent-built, workflow-wrapped, validator-gated, refresh-automated.
3. **Evaluate** — the rotation is the standard, not an optional stage. A batch is not complete
   until the 3-lane blind rotation (primary free tiers + preferred co-base where needed) has
   run and the head has adjudicated cold.
4. **Sustain** — the posture doc is re-read on a named cadence; the repo's own composition
   check runs; new findings re-enter the plan loop; the tracker refresh workflow and the
   validators keep running. The self-application gate (`.github/workflows/self-application-gate.yml`,
   `validation/validate_self_application.py`, `examples/self-application-fixture/`) is the
   repo's mechanism-stack self-test: it exercises the minimum spine on a bounded fixture and
   confirms the stack still fires on every push or pull request to main. The gate is the
   repo's answer to "does the stack still work on itself?" — run on every merge, silent under
   greenlight, two-way door with rollback by deleting `runs/self-application-gate-001/`,
   `examples/self-application-fixture/`, `.github/workflows/self-application-gate.yml`, and
   `validation/validate_self_application.py`.

## Tracker / refresh reality note

The committed tree carries the full responsibility-tracker automation path:
`schemas/responsibility-clusters.schema.json`, `schemas/nousresearch-responsibility-clusters.json`,
`examples/nousresearch-responsibility-fixture.json`, `docs/nousresearch-responsibility-tracker.md`,
`docs/nousresearch-responsibility-digest.md`, `docs/nousresearch-responsibility-state.json`,
`scripts/update_responsibility_tracker.py`, and `validation/validate_responsibility_automation.py`.
The README currently describes the repo as holding "a Copilot-built responsibility tracker
(refresh workflow, live data)"; that description matches the committed automation path and the
generated tracker artifacts.

## HITL decision-doc shape

Repo-level doctrine decisions are recorded in the schema-envelope shape:

- `[Executive Summary]` — what was concluded or produced.
- `[Analysis Brief]` — problem domain, evidence, assumptions, uncertainty, alternatives.
- `[Recommendation/Action Plan]` — one selected next action, its reversibility, its success
  criterion.
- `[Next Steps/Exploration]` — follow-ups, open questions, what would change the conclusion.
- `[Artifact]` — path to the durable output, or `BLOCKED` with the exact missing input.

The doc carries the Assess findings, the Create plan, the Evaluate record (rotation verdicts +
cold-read adjudication), and the Sustain leg. Prose lives inside those sections; the schema is
the skeleton, the prose is the flesh.

## What this doc does not do

- It does not add new mechanisms to the framework. The framework's inventory is documented in
  `docs/invention-kb-map.md`, `docs/method-cards.md`, and `mechanisms/CATALOG.md`; this doc
  reflects that inventory, not expands it.
- It does not claim portability or proven value for the framework beyond what the committed run
  records and evidence plan already claim.
- It does not touch the refresh workflow or the validators. Those are left exactly as they are.
