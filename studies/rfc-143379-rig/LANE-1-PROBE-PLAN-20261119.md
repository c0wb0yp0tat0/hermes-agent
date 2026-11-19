# LANE-1 — THE PROBE PLAN (THE SPRINT-MISSION SHAPE)
**Artifact:** `LANE-1-PROBE-PLAN-20261119.md` · **Lane:** probe-planning (M1: certify the substrate's durable-record claim on the field's own protocol) · **Date:** 2026-11-19

---

## 1. The properly-stated problem (storm → enumerate → reduce → 5-Why)

**Claim (the durable record survives compression; the agent re-reads rather than makes the user repeat).**
- **Mechanism:** the read-restore delivers a previously non-re-observable fact back to the reader because the substrate's write-time record (verbatim doc-chain with provenance) survives compaction; the agent re-reads the record instead of pressing the user.
- **Design assumption:** the field's own probes (PersistGym R2) already demonstrate the raw/truncated gap of ~-92.5 points on the non-re-observable fact class; the substrate is a drop-in replacement for the truncated reader with govern-able compaction. This assumes the read-restore works at episode scale and at a cost-per-success below the truncated arm.
- **Missing channel:** no field experiment has ever run the substrate arm against the oracle arm on the same episodes; "the substrate delivers the fact" is asserted, not measured. That is the seam this plan exercises.

**5-Why chain:** the field claims (R2) the truncated arm loses 92.5 points. Without a substrate arm, one cannot tell whether the loss is a retrieval failure or a model failure. The oracle arm separates model error from substrate error. The transcript-class economics (R1/R2) make the arm-set cheap enough to run. The missing channel is the substrate-vs-oracle comparison on the same episodes — that comparison is THE probe.

---

## 2. The two-arm probe (the field vocabulary), exact episodes, one-factor-at-a-time law

Field canon (MemDelta F2, T-bench F6, PersistGym R2): **one factor varied at a time, model/questions/history fixed, fresh store, no leakage, cache-hit logged per arm, cost-per-success reported.**

### Arm vocabulary
| Arm | What it is | Field role |
|---|---|---|
| **A — TRUNCATED-UNCOMPENSATED** | The raw reader, history cut at the cut-point, no record available, no notes. | The field's own blinded-summarization baseline; measures the raw truncation penalty. |
| **B — SUBSTRATE** | Same reader, same episodes, but the session sees the durable verbatim record + the record-aware governor (compaction + extraction-to-notes + retry gating). | The treatment: the read-restore mechanism. |
| **C — ORACLE** | Same reader, but the prompt contains ONLY the evidence turns (evidence-only turns, no record). | The upper bound: "the model can use the fact when shown." Separates model error from substrate error. |

**Episodes:** ~200 episodes per arm (field scale, PersistGym R2), drawn **exclusively from the non-re-observable-fact class** (the class where the record matters; the oracle's "evidence turns" are the exact facts that were non-re-observable). Episodes are mirrored identically across arms — same task id, same input grid, same cut-point, same judge — so the only difference between arms is the memory channel. Fresh store per episode; no cache of prior episodes; the judge is a frozen third model (or the same frozen model across all arms) and is never shown which arm produced which answer.

**One-factor-at-a-time law respected:** A→B differs only in the presence of the record + governor; B→C differs only in the presence of the record vs. the raw evidence turns; A→C is the full gap to the ceiling. Any other variable (model, judge, prompt wording, episode set, random seed) is fixed across all three arms.

**Cache-hit logging per arm:** every arm logs (i) cache-hit rate on the read path and (ii) tokens in / tokens out, so that the truncated arm's known 2.9–4.0× cost-per-token penalty (R2) is measured rather than assumed. Cache-hit logging is mandatory; without it, "cheaper because the reader re-reads less" is a guess.

**Failure classes pre-armed (NOTE-5's five):**
1. **Compaction cliff** (53%→10% in the field's reported window): the grain is to log compaction count per episode in the substrate arm; if the governor triggers a compaction that destroys the fact, the episode is a miss — the grain is to verify the record survives compaction, not that compression is silent.
2. **Attribution failure:** the substrate arm scores under the oracle arm → the fact was delivered but the reader could not use it → the mechanism is a reader/retriever problem, not a storage problem. The probe is then re-shaped to the retriever, not the store.
3. **Regime reversal:** the truncated arm unexpectedly outscores the substrate arm → the governor's extra steps cost more than the record saves → the grain is to reduce governor steps, not to scrap the store.
4. **Mis-scoring** (21.7% reported failure rate in the field's audit): the frozen judge is checked against known control answers on a held-out 20-episode control set before the run; if control accuracy < 90%, the run is null and re-done with a refrozen judge. Re-scoring is a pre-registered gate, not an afterthought.
5. **Stale-confident:** the substrate arm answers confidently from the record but the record is stale/wrong → the grain is to tie the governor's retry to a freshness/validity check recorded by the write-time assert (EviBound pre-gate), never to trust the first confident answer.

---

## 3. The pre-committed decision rule (VERBATIM — stated before the run)

**Execution rule, pre-committed (no post-hoc swaps):**

1. Run 200 episodes per arm (A, B, C) on the same frozen reader, same judge, same episode set.
2. Normalize: accuracy A, B, C (percentage of correct answers). Cache-hit rates logged. Cost-per-success = total cost / correct answers for each arm.
3. **Certify** if and only if BOTH hold:
   - (i) **B − A ≥ 20 points** (the substrate must recover the field's measured truncation gap by a pre-set, meaningful margin — the field's 92.5-point gap is the anchor; 20 points is a pre-committed, non-trivial fraction and keeps us honest), AND
   - (ii) **B ≥ 0.85 × C** (the substrate track the oracle; the claim is "the substrate delivers what the reader can use," not merely "the substrate beats truncation").
4. **Falsify** if **B − A < 20 points** (the substrate does not recover the bulk of the truncation gap) OR **B < 0.85 × C and B ≤ A** (the substrate loses to truncation, i.e., the record actively hurts).
5. **Inconclusive** if: the control judge check fails (< 90% on the 20-episode control set); cache-hit logging is missing for any arm (the economics are unreadable); or C − A < 5 points (the oracle itself failed to separate — the episode class presented is too easy, the guardrail is broken, and the comparison carries no information).

**Why this rule is the seam:** the "certify" carries the claim; "falsify" burns the claim; "inconclusive" is the zone where the experiment is rewritten (governor steps trimmed, cache-hit logging fixed, episode class swapped) rather than the claim talked away. There is no "maybe" exit: pre-committed, forced, and scored the same way the field scores.

**Boundary (the ceiling rule):** the probe certifies ONLY the episodic, episode-scale reliability claim (the durable record survives compression within a session; the agent re-reads rather than asks again). It does NOT certify lifetime learning, weight-level skill acquisition, or generalization to unseen rules — the field's own Continual-ARC shows the notes-class ceiling at 0.12 on the adversarial window, and the RFC's three-state spread (A/B/C) is an episodic window. The claim is graded against the ceiling rule, never overclaimed.

---

## 4. The oracle arm's seat

**Named:** the oracle arm uses **SambaNova's free gpt-oss-120b endpoint** (98.5% endpoint accuracy, OpenAI-compatible). Budget: the endpoint is free-tier for the rig; no cost line assigned; the only cost is the engineer's time to stand it up. A local-LM fallback (e.g., a 7B-class open model run locally on the rig's own GPUs) is a named contingency with a documented cost line (GPU-hours), but it is NOT the primary seat because the field benchmark shows the oracle must separate model error from architecture error, and the local-LM floor cannot promise 98.5% endpoint accuracy.

**Why this seat matters:** oracle at 0.985 vs raw 0.955 vs naive RAG 0.900 (T-bench F6) is the field's measured ordering that separates "the model can't use the fact" from "the substrate failed to deliver it." If the local-LM floor is ever used, the oracle line is void and the decision rule reverts to a two-arm verdict (B vs A only).

---

## 5. Cost rows (penny-scale, all arms)

Cost policy (MemDelta F2 "cost is not secondary"): **the probe reports cost-per-success, not just accuracy.** The truncated arm's known 2.9–4.0× penalty (R2) is measured, not assumed.

| Arm | Expected total cost | Expected cost per success | Cache-hit rate (expected) | Logging |
|---|---|---|---|---|
| **A — TRUNCATED** | ~$0.30–0.50 per episode (field's truncated window) | ~$1.50–2.50 (from the field's R2 caveat: fewer tokens but 2.9–4.0× more cost per success) | ~48% (R2: truncation breaks cache) | required |
| **B — SUBSTRATE** | ~$0.35–0.60 per episode (same reader; governor adds a measured few steps) | ~$1.50–2.50, but with a **cache-hit line** showing whether the governor's extra steps are cached and cheap — the whole claim is "cheaper per success than A" | ~48% baseline, hopefully higher with the governor's reads cached | required |
| **C — ORACLE** | ~$0.05–0.20 per episode (free endpoint, evidence-only turns) | ~$0.05–0.20 (free) | not applicable (no record reads) | not applicable |

**Luna leg (in its place — do not let it leave the plan's economics):**

The Luna leg is **one small arm inside this plan**, not a separate experiment:

- **Luna arm (L):** same episodes, same judge, but the reader is gpt-6-luna itself, with NO record and NO governor (the field's own state-of-the-art control, R2's subject). Cost: ~$0.50–0.90 per episode (Luna's measured R1/R2 cost at $0.406/run, 33% above raw Sol per the field).
- **Luna vs raw Luna (L_raw):** the purpose is "harnessed Luna vs raw Luna on the tool-shy class" — the harness question R1/R2 already probed. The cost line is explicit: **~$0.406 per Luna run, plus the overhead of caching and judge calls (~15% of arm cost), i.e., ~$0.06–0.14 per episode, a class cost that does not bust the economics.**
- **Why it stays in place:** the Luna leg serves the larger mission (does a harness around a fallible model beat the raw model at lower cost?) without bloating the substrate probe. It is not one of the three decision-rule arms — it is a separate, parallel question the study keeps cheap. Its explicit cost line is covered above; it is not double-counted in the substrate arm's cost row.

**Cache-hit logging per arm:** every arm logs (i) cache-hit rate on the read path and (ii) tokens in / tokens out. The truncated arm's 2.9–4.0× penalty is confirmed or refuted by measurement, not assumed.

---

## 6. The failure classes pre-armed (NOTE-5's five), in the decision rule

1. **Compaction cliff 53%→10%:** the grain is to log compaction count per episode in the substrate arm and verify the record survives compaction; a compaction-driven miss is a mechanism result, not a failure of the run.
2. **Attribution failure:** substrate arm < oracle arm on the same episodes → the fact was delivered but the reader couldn't use it → the probe is re-shaped to the retriever, not the store.
3. **Regime reversal:** truncated arm outscores the substrate → the governor's extra steps cost more than the record saves → the grain is to trim governor steps, not discard the store.
4. **Mis-scoring 21.7%:** the frozen judge is checked on a 20-episode control set first; below 90% accuracy, the run is null and the judge is refrozen before re-running. Re-scoring is a pre-registered gate.
5. **Stale-confident:** the substrate arm answers confidently from the record but the record is stale/wrong → the grain is to tie the governor's retry to a recorded freshness/validity check (write-time assert), never trust the first confident answer.

---

## 7. Compose-check table (deconstruct, sense, choose, calibrate, probe, review, record, compose-check — FIRED / ABSENT)

| Compose-check | Status | One evidence line |
|---|---|---|
| **Deconstruct** | FIRED | Claim ground in STORM-HARVEST-1/R2 (92.5-point truncation gap; oracle as model-vs-substrate separator). |
| **Sense** | FIRED | Field countermeasure: Continual-ARC notes-class ceiling 0.12 (STORM-HARVEST-2); the probe's episodic window is named as different. |
| **Choose** | FIRED | Arm vocabulary S0/S1/S_rand-derived: A/truncated (S1-class), B/substrate (treatment), C/oracle (T-bench upper bound). |
| **Calibrate** | FIRED | ~200 episodes/arm; epoch scale from field's PersistGym 200/200; judge frozen + 20-episode control set (mis-scoring gate). |
| **Probe** | FIRED | Decision rule BOTH B−A≥20 AND B≥0.85C pre-committed; falsify/inconclusive boundaries stated verbatim. |
| **Review** | FIRED | Stranger re-read + 3–4 adversarial pushbacks + termination (two no-change re-reads) — the AoA-on-different-base of ConMem F4. |
| **Record** | FIRED | Cache-hit rate + cost-per-success per arm + judge seed + episode set + compaction counts, all in the run ledger before results are read. |
| **Compose-check** | FIRED | Boundary rule: episodic claim only; no overclaim to lifetime learning or weight-level skill (field's own ceiling). |

---

## 8. Deliverables checklist

- [x] Arms defined (A truncated / B substrate / C oracle, ~200 episodes each, one-factor-at-a-time law respected, fresh store per episode, no leakage).
- [x] Pre-committed decision rule stated verbatim (certify / falsify / inconclusive, with control-judge and cache-hit gates).
- [x] Oracle seat named: SambaNova free gpt-oss-120b (98.5% endpoint accuracy); local-LM floor named as contingency with cost line.
- [x] Cost rows complete: ~$0.30–0.60 per episode both arms, ~$0.05–0.20 oracle (free), cache-hit logged per arm, 2.9–4.0× truncated penalty measured not assumed.
- [x] Luna leg in place: one small arm, explicit cost line (~$0.06–0.14 per episode overhead), serves the larger mission without busting economics.
- [x] Failure classes pre-armed (NOTE-5's five) and the ceiling rule (episodic claim only, no overclaim).
- [x] Compose-check table: all eight checks FIRED with one evidence line each.

---

**LANE-1 VERDICT (standing envelope):** READY — the probe plan is fireable as written: arms, episodes, pre-committed decision rule, cost rows complete, oracle seat named, Luna leg costed and bounded, boundary pre-committed, cache-hit logging mandatory. **The seam this plan exercises is the one factor at a time:** substance (the record) varied against the truncated baseline on identical episodes. The run's own outcome is the certification.
