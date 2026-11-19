# L-1 — LUNA MIDDLEWARE PROBE DESIGN (CERTIFY LINEAGE) — 2026-11-19

Artifact: `L-1-PROBE-DESIGN-20261119.md` · Lane: probe design (L-1) · Mission envelope: LUNA-MIDDLEWARE-MISSION-20261119.md.

**Mission (binding):** prove the agnostic quality of the doc-chain middleware — its governance bridge (release-point governor + write-time discipline) and its abstention fight (restored record → the seat answers instead of refuses) — using **Luna (gpt-6-luna)** as the demonstrating seat, NOT Luna's capability. Luna is an instrument; the middle is the subject. Small-scale, long enough to gather data, never busting economics. Null is directed at the public dismissal, non-adversarial.

**Seat reality (CERTIFY-class transfer, named & falsifiable):** the read-gap (truncation destroying non-re-observable facts) bites hardest on tool-shy models; the substrate's recovery (CERTIFY: A 0/200 → B 200/200, C 199/200) transfers to Luna. So the bridged Luna should show the same channel-effect shape: raw-truncated Luna loses the fact; bridged Luna recovers it; oracle Luna can use it when shown.

---

## 1. The arms (field vocabulary, applied to the seat)

Same reader (gpt-6-luna), same episodes, one factor varied at a time. Fresh store per episode; mirror identical task id/input grid/cut-point across arms; judge frozen and never shown which arm produced which answer.

| Arm | What it is | Field role | Seat measurement |
|---|---|---|---|
| **A — RAW-TRUNCATED-LUNA** | History cut at the cut-point (12), no record, no notes. | The raw baseline: measures the truncation penalty on the tool-shy seat. | Accuracy; abstention rate (refusals/hedges/"I can't"/empty); token in/out; cache-hit rate. |
| **B — BRIDGED-LUNA** | Same reader + the substrate's verbatim record + the governor (compaction + extraction-to-notes + retry gating + release-point gate). | The treatment: the governance bridge + abstention fight. | Accuracy; abstention rate; **governance compliance** (every record interaction carries its witness row — F1; every compaction decision passes the release-point gate — F2); cache-hit rate; cost-per-success. |
| **C — ORACLE-LUNA** | Same reader, but the prompt contains ONLY the evidence turns (evidence-only, no record). | The upper bound: can the seat use the fact when shown. Separates model error from substrate error. | Accuracy; abstention rate; (no cache-hit logging needed — no record reads). |

Episode selection: ~200 episodes per arm drawn **exclusively** from the non-re-observable-fact class (the class where the record matters). Oracle evidence turns = the exact facts that were non-re-observable. No leakage: episode set, judge, prompt wording, random seed fixed across arms.

Failure classes pre-armed (same as CERTIFY lineage):
1. **Compaction cliff** — log compaction count per episode in arm B; a compaction that destroys the fact is a miss (verify record survives compaction, not just that compaction is silent).
2. **Attribution failure** — B < C → the fact was delivered but the reader couldn't use it → reshape to the retriever, not the store.
3. **Regime reversal** — A outscores B → the governor's extra steps cost more than the record saves → trim governor steps.
4. **Mis-scoring** — frozen judge checked on a 20-episode control set before the run; <90% → run NULL, judge refrozen, re-run. (F3 machinery, inherited.)
5. **Stale-confident** — B answers confidently from the record but the record is stale/wrong → tie governor's retry to a recorded freshness/validity check (write-time assert).

---

## 2. The abstention axis (new measurement)

Every arm's answers classified on the refusal/hedge spectrum vs answered-with-content:

| Classification | Form | Count per arm |
|---|---|---|
| **R** — refusal | "I can't", "I'm not able to", explicit refusal | r_A, r_B, r_C |
| **H** — hedge | "I think...", "might", hedged certainty | h_A, h_B, h_C |
| **E** — empty | no content, prompt-loop, empty | e_A, e_B, e_C |
| **A** — answered-with-content | substantive answer | a_A, a_B, a_C |

**Abstention rate** per arm = (R+H+E) / 200. Headline measurement: **B's abstention rate ≤ A's** — the middleware's fight is the seat answering instead of refusing. This is reported per arm and as a delta (B−A), scaled to the small-N economics.

---

## 3. The governance axis (second new measurement)

In arm B only, every record interaction carries its witness: each F1 checkpoint row is logged verbatim with (question_id, record_ref, guard_feedback, timestamp, responder_id). Every compaction decision passes the release-point gate (F2): the gate logs (compaction_event_id, guard_outcome, release_hold, re-run flag, payload_hash). **Governance compliance** = (interactions carrying a witness) / (total record interactions) and (compaction decisions passing the gate) / (total compaction decisions) — reported **as a rate, never assumed**. The bridge is measured as compliance, not capability.

---

## 4. The decision rule (pre-committed, verbatim)

Specified **before the run**, no post-hoc swaps:

1. Run 200 episodes per arm (A, B, C) on the same frozen reader, same judge, same episode set. Control judge check (F3) must pass (≥90% on 20 episodes) or the run is NULL; cache-hit logging mandatory for all arms or the economics are unreadable (inconclusive).
2. Normalize: accuracy A, B, C (percentage of correct). Cache-hit rates logged. Cost-per-success = total cost / correct.
3. **CERTIFY** iff BOTH hold:
   - (i) **B − A ≥ 20 points** (the bridged seat must recover the bulk of the truncation channel-loss by a pre-set, meaningful margin — the field's measured channel-effect shape is the anchor; 20 points is the pre-committed non-trivial fraction keeping us honest), AND
   - (ii) **B ≥ 0.85 × C** (the bridged seat tracks the oracle; "delivers what the reader can use," not merely "beats truncation").
4. **FALSIFY** iff B − A < 20 points (the seat does not recover the bulk of the gap) OR (B < 0.85×C AND B ≤ A) (the record actively hurts).
5. **INCONCLUSIVE** iff: control judge check fails; cache-hit logging missing for any arm; or C − A < 5 points (the oracle itself failed to separate — the episode class is too easy, the guardrail broken, the comparison carries no information — the leg is re-shaped, not the claim talked away).

**Ceiling rule:** CERTIFY carries only the episodic, episode-scale claim (durable record survives compression within a session; the agent re-reads rather than re-asks). It does NOT certify lifetime learning, weight-level skill, or generalization to unseen rules — the module's own floor says no overclaim.

---

## 5. Scale + restraint (operator's mandate)

- **Episode count per arm:** 200 (A, B, C), mirroring the field's full-scale pre-committed rule. Logic: small-scale, long enough to gather data, never busting economics.
- **Headline economics:** arm A ≈ $0.30–0.50/episode; arm B ≈ $0.35–0.60/episode (governor adds a measured few steps, measured not assumed); arm C ≈ $0.05–0.20/episode (free endpoint, oracle). **Total ≤ ~$260** (if the governor's extra steps are cached, B approaches A's cost-per-success, which is the whole claim). Because Luna is the seat, Luna's own per-run cost ($0.406/run, +33% over raw Sol) is absorbed into the arm B/C lines — one small arm, explicitly costed, not double-counted.
- **Falsification by bust:** if arm B's total spend exceeds ~$260, the leg is inconclusive and the governor steps are trimmed — a finding, not a surprise.
- **Rollback:** every run is a fresh store; arm A is the rollback baseline (no governor). If the middleware misbehaves, drop the governor — the seat is intact. No persistent state persists across episodes.

---

## 6. Compose-check table (FIRED / ABSENT, one evidence line each)

| Compose-check | Status | One evidence line |
|---|---|---|
| Deconstruct | FIRED | Claim ground: STORM-HARVEST/R2 (92.5-pt truncation gap; oracle as model-vs-substrate separator); LUNA-MIDDLEWARE-MISSION-20261119.md. |
| Sense | FIRED | Reframing's locus: middleware quantity with LUNA as instrument; read-gap class bites hardest on tool-shy seats; bridge that holds on hardest case is agnostic by demonstration. |
| Choose | FIRED | Arm vocabulary A/RAW-TRUNCATED-B / B/BRIDGED-LUNA / C/ORACLE-LUNA from the CERTIFY lineage; one-factor-at-a-time law. |
| Calibrate | FIRED | 200 episodes/arm; same read; frozen judge + 20-episode control set (F3 mis-scoring gate, ≥90%); abstention classifier spec; governance compliance rate. |
| Probe | FIRED | Decision rule pre-committed verbatim (CERTIFY iff B−A≥20 AND B≥0.85C; FALSIFY iff B−A<20 OR (B<0.85C AND B≤A); INCONCLUSIVE otherwise). |
| Review | FIRED | Stranger re-read + 3–4 adversarial pushbacks + termination (two no-change re-reads) per the AoA-on-different-base protocol. |
| Record | FIRED | Abstention counts + governance compliance rate + cache-hit + cost-per-success + judge seed + episode set + compaction counts, all in the run ledger **before** results are read. |
| Compose-check | FIRED | Boundary rule: episodic claim only; no overclaim to lifetime learning or weight-level skill (field's own floor). |

---

## 7. Deliverable state (for the run ledger)

- [x] Arms defined (A/B/C, 200 episodes each, one-factor-at-a-time, fresh store, no leakage, judge frozen).
- [x] Pre-committed decision rule stated verbatim (CERTIFY / FALSIFY / INCONCLUSIVE).
- [x] Abstention axis instrumented (R/H/E/A classification, abstention rate per arm, B−A headline).
- [x] Governance axis instrumented (F1 witness rows + F2 release-point gate, compliance rate, not assumed).
- [x] Oracle seat named: SambaNova free gpt-oss-120b for arm C (or local-LM fallback with void oracle + two-arm revert — documented).
- [x] Cost rows complete: A $0.30–0.50, B $0.35–0.60, C $0.05–0.20; ~$260 ceiling; Luna's $0.406/run absorbed into B/C lines.
- [x] Failure classes pre-armed (compaction cliff, attribution failure, regime reversal, mis-scoring, stale-confident).
- [x] Compose-check table: all eight checks FIRED with one evidence line each.

**LANE-1 VERDICT:** the probe design is fireable as written. The seam exercised: one factor at a time — the record (and the governor) varied against the truncated baseline on identical episodes on a tool-shy seat. The run's own outcome is the certification.
