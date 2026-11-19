# MISSION-SHAPING — the storm-sprint's thinking-shapes (how we shape, with the findings), 2026-11-19

The document that carries the process itself: how this fleet thinks about a mission before any brief fires. It IS the shaping — the shapes in order, each grounded in the web storm's receipts, then the real problems, then the lens, then the run. Teams and orchestrations read this and shape the same way. It precedes the connect-the-dots map; it is the map's spine.

---

## PART 1 — THE SHAPES (the process, in order — this is how we think)

**SHAPE-1 · STORM FIRST.** Before shaping, fire the CTO-side web storm — the head's own lens: cross-referenced field evidence on the mechanism underneath the work, cited by source, mapped to the rig's shapes. The storm is not research-for-its-own-sake; it is the receipt-bank the shaping reads. *The day's hardest problem is the default target.*

**SHAPE-2 · ENUMERATE.** Lay out the raw material as one-line problem statements. No narrative, no decoration — the list is the material. The session's failures, the field's findings, the gaps, the seams.

**SHAPE-3 · REDUCE (Kettering).** Merge to 2-3 master statements. If two trace to the same root, they merge — the reduction IS the point; five un-merged statements are a pass that didn't happen. Then the separation test (mission-shaping): each master's verb (certify / synchronize / adopt) must be mutually exclusive and comprehensive — different mechanisms stay separate, same-mechanism merges.

**SHAPE-4 · THE ULTIMATE 5-WHY.** On the load-bearing master, chain to the root — each Why driven by the prior, verified at its own level with cited evidence. Terminate at a SYSTEM-DESIGN fact, never at a person. The convergence of the practice-root and the subject-root is the finding.

**SHAPE-5 · THE LENS (the full LP substrate, not the flattened envelope).** Re-read the masters through all 14 old-school Leadership Principles + the LOOP. The LOOP's verdict comes first: what feedback edge is deleted from this plan? Then per-master: Customer Obsession (who's hurt, before internals), Are Right A Lot (the disconfirmation demanded), Dive Deep (audit into the record the same day), Earn Trust (benchmark against the best), Insist on the Highest Standards (defects don't ship), Bias for Action (ONE reversible act), Frugality (constraints breed resourcefulness), Invent and Simplify (the field's simpler form of OUR mechanism), Have Backbone (name the compromise), Deliver Results (key inputs on the actual clock).

**SHAPE-6 · STAMP.** The masters restated under the substrate, each with target + the reversible act. The stamp is what the fleet runs on: measurable, receipted, two-way-doored.

**SHAPE-7 · THE LOOP-CLOSING CLAUSE.** The countermeasure that wires the closing edges into the plan's shape — so the next external door is a scheduled read, not a storm-discovery.

---

## PART 2 — THE FINDINGS (the web storm's receipts, the ground the shapes read)

The two storm waves, condensed with their numbers (full receipts in STORM-HARVEST-1..6 on the branch):

- **The harness seat is field-verified for episodic reliability.** Behavioral harness: Luna 3/10 → 10/10 at $0.273/run — 33% under unharnessed Sol $0.406 (Jain/Fowler). PersistGym: full history 200/200 vs truncated-with-one-non-re-observable-fact 7.5% — **the read's class costs 92.5 points** on the accused model itself; failures cluster 5 steps after compaction; the truncation costs **2.9–4.0× more** while using fewer tokens (caching 94% → 48%). ARC-AGI-3: Astra 62.7% (Standard harness) → 99.9% (Provider Adapter) — memory handling, not raw reasoning.
- **The dial is free.** Same model: low 37.7 → medium 61 → max 86.7 (ARC-AGI-1, Luna). Teknium's chart measured one unwrapped point (medium). Laddering (start low, escalate) beats fixed top effort.
- **The adversary is named, and the bench is open.** Continuity-ARC (Lenton/Unify): Hermes Agent listed among learners that "didn't memorize anything of value." Notes kept saved at most **0.12** of reset-spend on met tasks, ~chance on new; weights saved **0.45/0.27**. Verification contract: public stream → PR (reported) → their rerun on **50 private rules at an undisclosed seed** (verified). ~$100 Luna-class budget cap; input-logging must be OFF or void. Anything allowed except baked-in ARC data — "memory, programs, tools, a cache, training the weights; compute logged, never scored."
- **The middle path exists.** NCE (native context editing): +5.6 avg points over harness compaction, −36% tokens; the same edits as tool-calls scored BELOW plain compaction — native grammar is the lever. The release-point rule: "release a block only when the teacher can cite the event that ended its use."
- **The economics are the harness's.** Cache-hit rate is the most consequential cost variable (κ≈0.1); byte-stable prefix + compaction designed with caching. **Harness leverage r=0.99: the weaker the model, the more the harness improves its quality — the free tiers' seat, quantified.** Truncation is the most expensive way to save tokens.
- **The recipe's ladder is published.** The ceiling rule: process failures (blocked calls, loops, exhausted budgets) → harness evolution; content failures (poor delivered plan) → weight training. SIA: harness+weights unified (+25.1% LawBench). Co-Harness: HarnessCritic attributes failures to prompt/schema/skill/middleware and validates diffs before accept — the rig's verdict loops, formalized. ClawLoop: self-improvement with NO external teacher.
- **The fleet theorems.** Parallel teams of 10 beat 100 parallel agents on 10/12 tasks — many small teams balance mean + variance. Coordinated small seats beat big uncoordinated seats at ~35% of cost (FoA: LLaMA3.2-11B > LLaMA3.2-90B solo). Weight-rung receipts are 4B/9B-cheap now: Agentic-DPO (τ-bench 21.7 → 41.4 at 9B, offline), MemRL (RL on episodic memory, NO weight updates), OPD-Evolver-9B vs 397B giants, DeepSearch-World-9B (+48.1 HotpotQA, no proprietary teacher).
- **The money law.** Two-way doors: most decisions are reversible and should fire at ~70% of the data; gates are the anti-pattern.

---

## PART 3 — THE PROBLEMS (Kettering, the real kind)

**The enumeration (12, from the record + the findings).** The read's removal still stands (23 RED, `Unknown action 'read'` on main); 6,275 lines of compensation churn stack on a ~30-line subset; the compaction is ungoverned (the 92.5-point class, the post-compaction cluster); the K-recency long-session gate FAILs at 300 cycles with a broken ruler (probe scope bug, −9.2..+10.2pp spread); the RFC's acceptance criteria are unratified ("the team's to confirm"); the rig's strongest proof is self-reported (~799×, storm-sourced interpretation); the field's instruments exist and named us unanswered; PersistGym's protocol is pennies and unrun; free-tier seats are windowed (00:00 UTC resets, 4-day offers) but dispatch treats them as evergreen; coordination surfaces disagree (tracking ref vs ls-remote, spawn-counts vs process tree, watcher tokens vs landings); the release-point rule is un-adopted; the 70% law is violated by planning gates.

**The masters.**
- **M1 — THE EVIDENCE CHAIN IS UNCERTIFIED.** The substrate's core claim (the durable record survives compression, re-readable) rests on self-run batteries, a broken ruler, unratified bars, self-reported marathons — while the field's certification instruments are open, cheap, and name our house unanswered. Verb: **certify.**
- **M2 — THE ORCHESTRATION'S RESOURCE-TRUTH IS UNRELIABLE.** Windowed seats treated as evergreen; surfaces that disagree about what landed. Motion planned without a true calendar or a true ledger. Verb: **synchronize.**
- **M3 — THE GOVERNANCE SEAMS ARE UN-ADOPTED.** The field's release-point rule and the fleet's own 70% law: doctrine on paper, not wired in. Verb: **adopt.**

**The ultimate 5-Why (M1, the load-bearing):** uncertified because verification is self-run and self-referenced → because the posture was room-first (the RFC's stated purpose: the designers in the room see what the connections enable) → because the habit is build-and-prove-internally-first (the pilot promise) → because the plan's verification vocabulary is entirely rig-owned (batteries, gates, probes — no mechanism consumes an external bench) → **SYSTEM-DESIGN FACT: the plan has no open door for external verification instruments discovered mid-mission — the evidence chain is closed by shape, not by choice.**

---

## PART 4 — THE LENS (the full old-school substrate over the masters)

**The LOOP's verdict:** the RFC's verification vocabulary is checklist-shaped; the doctrine is loop-shaped; a feed-forward checklist cannot close a feedback system. The deleted closing edges are Earn Trust (benchmark-against-best — the benches existed, found only by storm) and Dive Deep (the broken ruler found, its reading tabulated anyway, then disqualified — the disqualification must land in the record the same day).

**The stamps.**
- **M1-STAMPED:** the customers (the "you're not listening" user; the pilot's inheritors) are hurt by an un-stamped claim; Are Right A Lot demands the disconfirmation run — PersistGym's protocol at pennies, or Continual-ARC's public stream + verify; the unratified criteria are defects sent down the line. **Reversible act: run the PersistGym two-arm probe now.**
- **M2-STAMPED:** every coordination hang is a Dive Deep violation; evergreen planning against windowed seats is hope, not delivery; the window-calendar line + single-surface ledger are the enforcement; depleting a seat before reset is Frugality exercised. **Reversible act: the window-calendar line in every mission plan; ls-remote truth before every landing.**
- **M3-STAMPED:** the release-point rule IS the field's simpler form of archive-before-stub — Invent and Simplify says adopt it (never "not invented here"); the planning gates that violate the 70% law are Have Backbone's unspoken compromise. **Reversible act: wire both as named probes with reversibility + rollback.**

**The loop-closing clause (the lens's deliverable):** the envelope gains ONE standing clause — *every mission re-reads its verification vocabulary when the field's doors open; each newly-arrived external instrument (bench, protocol, contract) is consumed as a first-class leg with a named budget, or explicitly refused with its why.*

---

## PART 5 — THE RUN (what the fleet does with this)

1. The pair's storms and this document are the ground — already landed, scribed, byte-verified, on the branch.
2. **The free tiers join within their windows** — the storm-of-storms: parallel copycat missions across the fleet's code bases, runners, and forks, each on a preliminary deep-planning phase for the sprint — one seat per lens, shared envelope, named merge; their powerhouses fire full-bore in their windows, never paced around.
3. Each fire is **modeled on the historical two-way-door sprints** — but not constrained by them: this is a whole new synthesis (the recipe's four corners: harness + memory + weights + fleet).
4. Every brief names its **reversibility and rollback**; the sequence does not stop until the goals are accomplished; the documentation IS the spine it runs on.
5. The next document in the series: **the connect-the-dots map** — the free tiers' run sheet over these shapes, findings, problems, stamps, and clauses.

*The reduction is analysis; this doc is the record; both outlive the session.*
