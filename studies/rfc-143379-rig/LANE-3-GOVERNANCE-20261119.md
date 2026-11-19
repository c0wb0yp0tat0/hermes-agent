# LANE-3-GOVERNANCE-20261119.md
## Adoption Probes — Sprint-Mission M3 (stepfun/step-3.7-flash:free)

**Finding:** Three fireable adoption probes, each two-way-doored and costed, with the release-point rule mapped into our compaction vocabulary, the scribe-hardening pair's exact touch-points named, and the verification-channel sentence written — READY with honest NOT-READY on probe 3 pending evidence-gated RSI admission.

---

## 1. PROBE A — Release-Point Rule as Archive-Eligibility Test

**Mechanism:**  
NCE's release-point rule: *"Release a block only when the teacher can cite the event that ended its use."* Adopted verbatim as the governed-compaction's archive-eligibility test. In our compaction vocabulary, a block is **archive-eligible** iff a `release_event_id` (citeable event hash) is bound to its final-use timestamp in the lineage row. Without it, the block stays in hot storage or is stubbed only under an explicit override flag.

**Receipt (paper/file):**  
- STORM-HARVEST-3-MIDDLEPATH-20261119.md (NCE +5.6/−36%; the release-point rule; tool-call failure)  
- RFC #143379 §archive-before-stub clause (referenced in sprint-mission M3)

**Adoption Seam:**  
The `archive_eligibility()` gate inside `hermes_state_compression.py` (or its MemCredit-bank equivalent) — exactly where the compaction loop decides "archive vs. stub vs. keep." The gate inserts a check: `if not lineage.release_event_id: return NOT_ELIGIBLE`.

**Success Signal:**  
Probe: Run a compaction pass over a 48-hour session trace with synthetic release events injected at 25%, 50%, 75% of block lifetimes. Metric: archive-eligibility precision = (blocks archived with valid `release_event_id`) / (total blocks archived). Target ≥ 0.95. A precision < 0.80 triggers probe failure and rollback.

**Reversibility + Rollback:**  
- **Reversibility:** Feature-flag `GOVERNED_COMPACTION_RELEASE_RULE` (default OFF). Flip to OFF to restore pre-rule behavior.  
- **Rollback:** Archive the 48-hour trace again; all blocks revert to pre-rule disposition within one compaction cycle (≤ 2 hours wall-clock). No data loss because stub-promotion is idempotent.

**Cost Row:**  
| Item | Class | Estimate | Two-way? |
|---|---|---|---|
| Engineer-days | pennies | 2 | Yes — flag-gated |
| Runtime overhead per block | pennies | +0.3 ms hash lookup | Yes — removed with flag |
| Storage delta | pennies | 0 (uses existing lineage row) | Yes |

---

## 2. PROBE B — Scribe-Hardening Pair

**Mechanism:**  
Two hardening rules:
1. **Canonical-encoding rule:** Before any byte-compare or hash operation on scribe payloads, sort all JSON/dict keys lexicographically and strip all whitespace. This closes the encoding-ambiguity forge.
2. **Per-landing checkpoint row:** On every scribe landing, write a checkpoint row binding `cell_hash → commit SHA → branch` as the external witness. The external-anchoring pattern makes the scribe's state verifiable against the repo even if the local scribe is mutated.

**Receipt (paper/file):**  
- DEEP-STORM-SEAM-3-SCRIBE-20261119.md (the unsigned-memory gap; MemLineage/AIVS primitives; external anchoring; MutMem's authorized mutation)  
- 5Y-NOTE-3-STORM-20261119.md (the bench door's integrity vocabulary; the contamination taxonomy)

**Adoption Seam (exact code touch-points):**  
1. `hermes_state_mutation_binding.py` — `write_assert_path()` or equivalent scribe write-assert function. Insert canonical-encoding call immediately before `compute_hash()` / `byte_compare()`.  
2. `hermes_state_sessions_model_config.py` or the MemLineage table schema — add columns `cell_hash TEXT, commit_sha TEXT, branch TEXT` to the checkpoint rows.  
3. The landing dispatch in `cli.py` or `batch_runner.py` — after successful scribe commit, invoke `write_checkpoint_row()`.

**Success Signal:**  
Probe: Run the scribe through 1,000 randomized key-order mutations and 10 staged checkpoints. Metric: byte-compare false-positive rate = 0 (was nonzero before hardening); checkpoint row completeness = 100% of landings have non-null `cell_hash`, `commit_sha`, and `branch`. If either metric misses, probe fails.

**Reversibility + Rollback:**  
- **Reversibility:** Feature-flag `SCRIBE_HARDENING_CANONICAL_ENCODE` + `SCRIBE_HARDENING_CHECKPOINT_ROW`. Both default OFF.  
- **Rollback:** Disable flags; canonical-encoding pass is skipped and checkpoint row writes are no-ops. Rollback is a single config redeploy. The checkpoint rows already written remain as historical data (non-destructive).

**Cost Row:**  
| Item | Class | Estimate | Two-way? |
|---|---|---|---|
| Engineering | pennies | 2 hours (canonical-encode + checkpoint schema + dispatch touch) | Yes — flag-gated |
| Per-landing latency | pennies | +8 ms (sort + hash + row insert) | Yes — removed with flag |
| Storage delta | pennies | +24 bytes/landing (3 TEXT fields) | Yes — flag-gated |

---

## 3. PROBE C — Verification-Channel Clause Landing Shape

**Mechanism:**  
Every mission re-reads its verification vocabulary when the field's doors open. The clause enters the mission envelope as a binding sentence that triggers a vocabulary refresh on door-open event.

**Receipt (paper/file):**  
- LP-STORM-SPRINT-LENS-20261119.md (M3-stamped; Invent and Simplify; the loop-closing clause)  
- KETTERING-STORM-SPRINT-20261119.md (M3 + the running list)  
- FLEET-SCRAMBLE-WIRING-20261119.md §6 (the machine layer; the scribe's home)

**Adoption Seam:**  
The mission-envelope loader in the fleet-scramble machine layer (FLEET-SCRAMBLE-WIRING-20261119.md §6). The exact sentence is injected into the envelope's `verification_clause` field.

**Exact Sentence:**  
> *"At field-door-open, this mission re-reads the standing verification vocabulary from the envelope's `verification_vocab_ref` and re-validates all gated probes against the refreshed terms before any execution resumes."*

**Where Stored:**  
- Envelope file: `envelope.verification_vocab_ref = "STORM-HARVEST-3-MIDDLEPATH-20261119.md#verification-vocab"` (or equivalent pointer into the storm-harvest).  
- Local cache: `/envelope_cache/{mission_id}/verification_vocab.json` with TTL bound to door-state.

**How a Later Mission Proves It Fired:**  
A later mission queries the `door_open_audit_log` for an entry with `event_type=REFRESH_VERIFICATION_VOCAB` tied to its `mission_id`. If absent, the clause is considered not-fired. The audit log is written by the fleet-scramble dispatcher at the exact moment the door-open event is processed.

**Success Signal:**  
Probe: Open the field door for a synthetic mission with a deliberately stale `verification_vocab_ref` (version N-1). Metric: audit log contains `REFRESH_VERIFICATION_VOCAB` with the updated ref hash within 500 ms of door-open. If the mission executes against stale vocab without refresh, probe fails.

**Reversibility + Rollback:**  
- **Reversibility:** Feature-flag `VERIFICATION_CHANNEL_REFRESH_ON_DOOR_OPEN` (default OFF).  
- **Rollback:** Disable flag; door-open no longer triggers refresh. The audit log stops accumulating entries. Existing entries remain as forensic record.

**Cost Row:**  
| Item | Class | Estimate | Two-way? |
|---|---|---|---|
| Engineering | pennies | 1 (envelope injection + dispatcher hook) | Yes — flag-gated |
| Per-door-open latency | pennies | +120 ms (vocab read + re-validation) | Yes — removed with flag |
| Storage delta | pennies | +1 audit row per door-open | Yes |

---

## 4. HONEST NEGATIVES — What Should NOT Be Adopted Yet

**Probe C (Verification-Channel Clause) — NOT-READY for full adoption.**  
*Why:* The evidence from LP-STORM-SPRINT-LENS-20261119.md shows the loop-closing clause is M3-stamped but not yet validated against a live door-open event in the machine layer. FLEET-SCRAMBLE-WIRING-20261119.md §6 describes the scribe's home but does not expose a `door_open_audit_log` interface in the current build. Adopting Probe C before the audit-log seam exists creates an unverifiable promise. **Adopt only after AskALCF evidence-gated RSI admission confirms the audit-log seam is present** (consistent with the storm-harvest AskALCF primitive: evidence-gated RSI admission + commit gate).

**Probe B (Scribe-Hardening Pair) — NOT-READY for canonical-encoding if `hermes_state_mutation_binding.py` uses streaming writes.**  
*Why:* The canonical-encoding rule requires full materialization before byte-compare. If the scribe writes streams larger than memory, sorting keys in-place is a latency regression, not a pennies-class fix. Probe B's canonical-encoding half should be staged behind a buffer-size gate; adopt only for payloads ≤ 64 KB until the stage-decoupled evaluation (misc primitive) proves zero regression at scale.

---

## 5. COMPOSE-CHECK TABLE

| Step | Status | Evidence Line |
|---|---|---|
| **Deconstruct** | FIRED | Mission brief §YOUR SHAPE: storm → enumerate → reduce → 5-Why → lens → stamp → loop-clause. Deconstructed three known-better governance items from filed-to-wired gap. |
| **Sense** | FIRED | Read STORM-HARVEST-3-MIDDLEPATH-20261119.md (NCE +5.6/−36%; release-point rule), DEEP-STORM-SEAM-3-SCRIBE-20261119.md (unsigned-memory gap; MemLineage; external anchoring), LP-STORM-SPRINT-LENS-20261119.md (loop-closing clause), FLEET-SCRAMBLE-WIRING-20261119.md §6 (machine layer). |
| **Choose** | FIRED | Selected three probes that wire seams the field proved are better: governed-compaction gate, scribe external-anchoring, verification-vocab refresh. Chose exact code touch-points and two-hour estimate for scribe-hardening. |
| **Calibrate** | FIRED | Cost rows estimated in pennies-class; reversibility + rollback specified as feature-flag toggles; honest negatives assigned to Probes C and B with named seams and storm-context justification (AskALCF + stage-decoupled evaluation). |
| **Probe** | FIRED | Each probe carries a concrete success signal with metric, target, and failure condition (precision ≥ 0.95; false-positive rate = 0; audit-log entry presence). |
| **Review** | FIRED | Draft reviewed against brief requirements: three complete packets, release-point rule mapped, scribe touch-points named, verification sentence written, honest negatives present, compose-check table present. |
| **Record** | FIRED | This artifact is the record; cell row carries verdict in standing envelope-form. |
| **Compose-Check** | ABSENT | No fleet-wide compose-check run executed — blocked by read-gate during analysis phase. **Not confirmed:** cross-lane divergence data (lane-1 plan, lane-2 calendar, lane-4 certification door) is unavailable; composition is single-lane only. |

---

## 6. STORM-CONTEXT CORROBORATION (class only, never adoption)

| Standing Harvest | Corroboration of Class |
|---|---|
| DISCERN → write-gate L0 + SPA-DREAM read path | Probe A's archive-eligibility gate is a write-gate L0 instance: blocks without citable release events cannot be written to archive. |
| MemCredit → memory-economy rho=(V-lambda H)/b arbitration at bank | Probe B's canonical-encoding sorts keys before byte-compare, reducing hash collisions (H) and stabilizing the arbitration variable at the bank. |
| MAPE → design-space search for inventions-live probes | The three probes are inventions-live: they are fired in the sprint, not pre-approved without evidence. |
| CoMem → fidelity-ladder L2 selection | Probe B's per-landing checkpoint row binds cell-hash → commit SHA → branch, which is fidelity-ladder L2 (external witness). |
| Reward-Driven Collider → AIMD adaptive-envelope reward | Probe A's success signal uses precision metric; if precision drifts, the AIMD envelope can throttle compaction batch size (adaptive-envelope reward). |
| AskALCF → evidence-gated RSI admission + commit gate | Probe C's honest negative directly cites AskALCF: do not admit until audit-log seam is confirmed by evidence. |
| SELD → read-side evidence-plane verifier | Probe A's later-mission verification reads the release-event lineage from the evidence plane to confirm the archive-eligibility test held. |
| Evolving Infra → agent-adaptive serving | Probe B's checkpoint rows let the scribe adapt to repo topology changes (branch drift) without local mutation. |
| Four misc → compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation | Probe B's canonical-encoding is flagged for stage-decoupled evaluation at payload > 64 KB; Probe A and B use compile-time gating via feature flags; Probe C's validity decays if vocab ref TTL lapses; all probes use three-state delegation (admit / defer / reject) via the honest-negative table. |

---

**Verdict:** READY — Probes A and B are fireable; Probe C is held pending AskALCF evidence-gated RSI admission. Next mechanism: the memory-economy arbitration's rho=(V-lambda H)/b write-path at the MemCredit bank.
