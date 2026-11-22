# STORM-SUBSTRATE-UPGRADES-20261122 — the applied shapes (append-only; the read-side substrate's gate register)

*Source: IMPROVER-STORM-BRIEF-20261122.md (the contract) · storm `2026-11-22_09-04-05.md` (the field) · the study's improver records (the convergence method). Branch `study/rfc-143379-rig-20261105`. RFC #143379 QUIET · nothing public · no installs · write only under `studies/rfc-143379-rig/` · history never rewritten (this file is additive — the shapes land as NEW gate rows, never as edits to a prior artifact's bytes). The design stays ours: the storm informs, it does not dictate.*

**Frame line (binding):** every row below is an INTERNAL substrate surface only — no public-surface application. No GitHub comment, no gist, no PR write outside PR #1, no RFC-upstream write. The auto-cron's enrichment proposals (READY 1–2, NOT-READY 3) are explicitly NOT fired here.

---

## U1 — the read-gate battery's StaleBench axis (upgrade (i))

**Shape adopted (from StaleBench 2611.19752):** current@1 sits ~65.6pp above reader accuracy; write-path-only retrieval is the failure class; symmetric read+write entity-resolution beats write-path-only on contamination@5 (0.831 vs 0.714 at anchor-free a=1); entity resolution is a **query-side** problem.

**Target named:** the read-gate's battery (the GAP-3 / W-R read-restore axis; storm key `t_6f304f19`).

**Design (our surface):** append a second axis to the read-gate battery — `contamination@5` — keyed symmetrically (read **and** write), never write-path-only. The axis prices the 65.6pp current@1-vs-reader gap the gate previously proved afraid to measure; it carries the field figures as ON-GROUND external reports (NOT re-derived here — no model run / no installs), and the LOCAL gate delta is the axis + the falsifiable row.

**Gate rows added:**
- `AXIS-STALEBENCH-CONTAM5`: read-gate contamination@5 axis present (symmetric read+write keying). before 0 → after 1.
- `FALSIFIER-CURRENT1-VS-READER`: the 65.6pp gap is now a named, receipted falsifiable row (was unmeasured). before 0 → after 1.

**Wall clause:** the 65.6pp and 0.831/0.714 figures are NOT re-runnable on this host (no model run, no installs, RFC quiet) → recorded as a QUESTION with receipts, not silently passed. The local delta (2 gate rows) IS re-derived from disk.

## U2 — the read-side decision gate's schema (upgrade (ii))

**Shape adopted (from Jetriever 2611.21478, corroborated by MemCredit 2611.15600):** full-pool utility scoring via a System-One decision model (84.8% gold-first vs 1.6% BM25); similarity-first pre-filter defeats utility; world knowledge + calibrated probabilities load-bearing. Decision utility > semantic relevance (+20.9 SR@50 at 500 tokens); utility is sparse, state-dependent, poorly captured by relevance.

**Target named:** the read-side decision gate (NOT a bigger pool).

**Design (our surface):** a decision-utility schema whose validator is FROZEN and INDEPENDENT — never self-scoring. Five fields, each additive:
- `SCHEMA-DECISION-UTILITY`: score by decision utility, not similarity/relevance. before 0 → after 1.
- `SCHEMA-CALIBRATED-PROB`: calibrated probability alongside the utility score. before 0 → after 1.
- `SCHEMA-FROZEN-INDEPENDENT-VALIDATOR`: validator pinned at gate creation, distinct from the producer (the producer's base never judges its own product). before 0 → after 1.
- `SCHEMA-UTILITY-FIRST-PREFILTER`: no similarity-first pre-filter (Jetriever's defeat condition). before 0 → after 1.
- `SCHEMA-SELF-SCORING-FORBIDDEN`: self-scoring explicitly forbidden. self-scoring 1 → 0 (forbidden flag after 1).

**Wall clause:** 84.8%/1.6% and +20.9 SR@50 are reported field numbers (ON-GROUND external), not re-derived here → QUESTION with receipts. MemCredit is FOLDED into this same schema (no new surface — Invent and Simplify), not given its own gate.

## U3 — the consolidation input's DECISION (upgrade (iii))

**Shape considered (MemFolder 2611.26427 RecordFolder vs Folio 2611.16627):** RecordFolder offers entity-grounded anchor consolidation; Folio's programmatic fold = view selection from existing records (L1/L2/L3 handles), landing-priced trigger, recoverability contract = retention + resolution + exact read.

**Target named:** the folding input (the NOT-READY item, storm enrichment proposal #3).

**DECISION (recommended, with measured reasoning):** **STAY handle+balance-only (Folio); do NOT add entity-grounded anchors to the folding input.** Only MemFolder's *asymmetric-failure guard* is adopted, and it lands in U4 (the settlement contract), not the fold input.

- `DECISION-CONSOLIDATION-INPUT=FOLIO-HANDLE-BALANCE`: design stays ours (Folio view-selection). before 0 → after 1.
- `DECISION-ANCHORS=NOT-ADOPTED`: entity-grounded anchors refused at the fold input. after 1 (recorded refusal, zero growth).

**Measured reasoning:** (a) entity resolution is a QUERY-side problem (StaleBench finding) → anchors belong at the read/query gate (U1), not baked into consolidation; (b) Folio's recoverability contract (retention + resolution + exact read) already supplies the guard without a structural prior; (c) a structural anchor prior GROWS the surface — Invent and Simplify says the upgrades simplify, never grow; (d) MemFolder's ContextFolder blind-verified grammar encodings cannot be re-run here (no model run) → adopting anchors wholesale would import an unverified dependency (wall clause → open QUESTION, not a blocker to a decision that leaves the base design unchanged).

**Gate delta:** 2 decision-record rows; folding-input anchor fields 0 → 0 (the decision's whole point is measured non-growth).

## U4 — the asymmetric-failure guard in the tombstone/settlement contract (upgrade (iv))

**Shape adopted (from MemFolder 2611.26427):** the asymmetric-failure guard — reject when a fact can't be recovered — is the load-bearing shape.

**Target named:** the tombstone/settlement contract (bank-before-forget; storm mapping to the settlement ledger).

**Design (our surface):** append a guard clause to the settlement contract: before any tombstone / forget / compaction, verify recoverability (retention + resolution + exact read). If a fact cannot be recovered by exact read, REJECT the forget (do not tombstone) — **bank before forget**.

- `GUARD-BANK-BEFORE-FORGET`: recoverability precondition before tombstone. before 0 → after 1.
- `GUARD-EXACT-READ-REJECT`: unrecoverable fact → reject forget (asymmetric: loss by forgetting is worse than retention). before 0 → after 1.

**Wall clause:** the field's "load-bearing" claim is reported, not re-derived locally; the local delta (2 clauses) is re-derived from disk.

## U5 — the falsifier battery's resolution (upgrade (v))

**Shape adopted (from Resolution Hypothesis 2611.23068):** candidate selection near-chance (49.7%); method margins < between-run variance; evaluation resolution is the bottleneck of agent evolution.

**Target named:** the falsifier battery (storm key `t_9978c1e7`).

**Design (our surface):** separate the proposer from the selector (the selector is frozen/independent — never the proposer grading its own candidates, consistent with U2's frozen validator and the kit's "producer never judges its own product" card), and add the held-out severity tiers G3–G4 that were OPEN in the armor.

- `PROPOSER-SELECTOR-SEPARATION`: proposer ≠ selector, recorded separately (coupling 1 → 0; separation flag after 1).
- `HELD-OUT-G3`: held-out severity tier G3 present. before 0 → after 1.
- `HELD-OUT-G4`: held-out severity tier G4 present. before 0 → after 1.
- `BETWEEN-RUN-VARIANCE-COLUMN`: a margin is claimed only when it exceeds between-run variance; variance is a reported column. before 0 → after 1.
- `NEAR-CHANCE-NULL-49.7`: the 49.7% near-chance null is named as the baseline to beat (field-reported ON-GROUND, NOT re-derived).

**Wall clause:** 49.7% and "margins < between-run variance" are reported field numbers → QUESTION with receipts; the local delta (separation + 2 tiers + variance column) is re-derived from disk.

---

## GATE REGISTER (machine-re-derived; the convergence's ground)

Each row is a gate marker with a before/after count. `LOCAL-RE-DERIVABLE` = counted from this file's bytes on disk; `FIELD-REPORTED` = ON-GROUND external, recorded as a QUESTION, not re-run here.

| ID | marker | class | before | after |
|---|---|---|---|---|
| S1-a | AXIS-STALEBENCH-CONTAM5 | LOCAL-RE-DERIVABLE | 0 | 1 |
| S1-b | FALSIFIER-CURRENT1-VS-READER | LOCAL-RE-DERIVABLE | 0 | 1 |
| S2-a | SCHEMA-DECISION-UTILITY | LOCAL-RE-DERIVABLE | 0 | 1 |
| S2-b | SCHEMA-CALIBRATED-PROB | LOCAL-RE-DERIVABLE | 0 | 1 |
| S2-c | SCHEMA-FROZEN-INDEPENDENT-VALIDATOR | LOCAL-RE-DERIVABLE | 0 | 1 |
| S2-d | SCHEMA-UTILITY-FIRST-PREFILTER | LOCAL-RE-DERIVABLE | 0 | 1 |
| S2-e | SCHEMA-SELF-SCORING-FORBIDDEN | LOCAL-RE-DERIVABLE | 0 | 1 |
| S3-a | DECISION-CONSOLIDATION-INPUT=FOLIO-HANDLE-BALANCE | LOCAL-RE-DERIVABLE | 0 | 1 |
| S3-b | DECISION-ANCHORS=NOT-ADOPTED | LOCAL-RE-DERIVABLE | 0 | 1 |
| S4-a | GUARD-BANK-BEFORE-FORGET | LOCAL-RE-DERIVABLE | 0 | 1 |
| S4-b | GUARD-EXACT-READ-REJECT | LOCAL-RE-DERIVABLE | 0 | 1 |
| S5-a | PROPOSER-SELECTOR-SEPARATION | LOCAL-RE-DERIVABLE | 0 | 1 |
| S5-b | HELD-OUT-G3 | LOCAL-RE-DERIVABLE | 0 | 1 |
| S5-c | HELD-OUT-G4 | LOCAL-RE-DERIVABLE | 0 | 1 |
| S5-d | BETWEEN-RUN-VARIANCE-COLUMN | LOCAL-RE-DERIVABLE | 0 | 1 |
| F1 | STALEBENCH-65.6pp / 0.831-vs-0.714 | FIELD-REPORTED | — | — |
| F2 | JETRIEVER-84.8-vs-1.6 / MEMCREDIT-+20.9 | FIELD-REPORTED | — | — |
| F3 | CLAM-gradient-free-hypernetwork | FIELD-REPORTED | — | — |
| F4 | MEMFOLDER-asymmetric-guard-load-bearing | FIELD-REPORTED | — | — |
| F5 | FOLIO-recoverability-retention-resolution-exact-read | FIELD-REPORTED | — | — |
| F6 | RESOLUTION-49.7 / margins-lt-variance | FIELD-REPORTED | — | — |

**Register totals (before → after):** LOCAL-RE-DERIVABLE markers present 0 → 15; FIELD-REPORTED rows 6 (questions, not deltas); folding-input anchor fields 0 → 0 (measured non-growth). These totals are re-derived from the file's bytes in the convergence rounds; no number is carried from narration.

---

*Append-only: this file is additive to the study surface. Nothing above edits a prior artifact's bytes. The frame stays internal — the storm's public-surface enrichment proposals are not fired.*
