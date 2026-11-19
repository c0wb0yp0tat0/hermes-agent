# L-1 — LUNA MIDDLEWARE PROBE DESIGN — ENRICHED — 2026-11-19

Artifact: `L-1-PROBE-DESIGN-ENRICHED-20261119.md` · Lane: E4 (hy4), swap-and-enrich of the L-1 probe design · Base read cold in full: `L-1-PROBE-DESIGN-20261119.md` · Seam: L-4 `L-4-GOVERNANCE-INSTRUMENTATION-20261119.md` (F1/F2/F3 per-episode binary checks + R/H/E/A classifier) and chain APPENDIX-A.1 (EHQ vocabulary, `LUNA-MIDDLEWARE-MISSION-20261119.md`).

`⟨E4⟩` tags EVERY added line. **Two-way door:** strip all `⟨E4⟩` lines and the base artifact is restored in substance — no arm, number, or decision threshold was changed. Enrichment only; divergences named, never smoothed.

**Mission (unchanged):** prove the middleware's agnostic quality with Luna as instrument, not subject. Null directed at the public dismissal, non-adversarial. Ceiling: episodic claim only.

---

## 1. The arms (field vocabulary, applied to the seat)

Same reader, same episodes, one factor varied, fresh store per episode, judge frozen and arm-blind. Base table A/B/C stands. `⟨E4⟩` The B-arm governance cells become **per-episode binary marks** in the run ledger (from L-4's three binary checks), each emitted once per episode, auditable:

- `⟨E4⟩` **F1 mark (witness-on-write)** = 1 iff the episode's record interaction carries a verbatim witness row with all five fields non-null: `question_id, record_ref, guard_feedback, timestamp, responder_id`; else 0. This is the base §3 witness row, now a checkable 0/1 instead of prose.
- `⟨E4⟩` **F2 mark (release-point gate honored)** = 1 iff the episode's compaction decision logs all five fields `compaction_event_id, guard_outcome, release_hold, re-run flag, payload_hash` AND `guard_outcome = honored`; else 0.
- `⟨E4⟩` **F3 mark (write-time assert, per-episode)** = 1 iff the record the responder answered from passes the freshness/validity assert at write time (the base §1 stale-confident guard, failure class 5); else 0. `⟨E4⟩` Reversibility: these are three added ledger columns; drop them and the arms read exactly as the base.

Failure classes pre-armed (unchanged): compaction cliff, attribution failure, regime reversal, mis-scoring, stale-confident. `⟨E4⟩` Class 4 (mis-scoring) and class 5 (stale-confident) are the two F3 faces — see §6 Divergence D3.

---

## 2. The abstention axis (measurement)

Base R/H/E/A table and headline (abstention rate = (R+H+E)/200; B ≤ A; delta B−A) stand. `⟨E4⟩` The L-4 classifier spec supplies the counting rule the base table lacked — operational cells, applied arm-blind per episode:

- `⟨E4⟩` **R** — explicit refusal: "I can't / I'm not able to / I refuse"; **H** — hedged certainty: "I think / might / probably"; **E** — empty: no content, prompt-loop, blank; **A** — substantive answer present. Each answer lands in exactly one cell; ties scored H (conservative).
- `⟨E4⟩` **EHQ identity (APPENDIX-A.1, verbatim cells):** `ABSTAIN` / `HEDGE` / `CONFIDENT`. Mapping to this leg's four cells: `ABSTAIN` ⊇ {R, E}; `HEDGE` = {H}; `CONFIDENT` ⊇ {A}. The 3-cell EHQ axis and 4-cell probe axis are NOT the same partition — see D1/D2.
- `⟨E4⟩` **Correctness cross-tab (added):** cross each abstention cell × {correct, incorrect}; report stale-confident = |CONFIDENT ∩ incorrect| separately. The abstention headline alone cannot see a confident-but-wrong answer. Reversible: an added cross-tab column; headline formula untouched.

---

## 3. The governance axis (second measurement)

Base §3 stands. `⟨E4⟩` Replace the prose rates with the mark means from §1: **governance compliance = mean(F1) and mean(F2) over arm B's 200 episodes**, plus **freshness compliance = mean(F3)**. Reported as binary-derived rates, never assumed. `⟨E4⟩` Reversible: rates fall back to the base narrative if marks are dropped.

---

## 4. The decision rule (pre-committed, verbatim)

Unchanged: CERTIFY iff B−A ≥ 20 AND B ≥ 0.85×C; FALSIFY iff B−A < 20 OR (B < 0.85C AND B ≤ A); INCONCLUSIVE iff judge check fails / cache logging missing / C−A < 5. `⟨E4⟩` Add to INCONCLUSIVE triggers: mean(F3) < 1 on the answered-from-record episodes (write-time assert failed → stale-record answers contaminated the headline) — a leg reshape, not a claim talked away. `⟨E4⟩` Reversible: one added trigger; thresholds otherwise identical.

---

## 5. Scale + restraint

Unchanged: 200/arm; A $0.30–0.50, B $0.35–0.60, C $0.05–0.20; ≤ ~$260 ceiling; Luna's $0.406/run absorbed into B/C; fresh store / arm A rollback. `⟨E4⟩` The three binary marks are ledger fields (no new model calls) — zero marginal cost; the ceiling is untouched.

---

## 6. Divergences (named with evidence, not smoothed)

- **D1 — cardinality.** APPENDIX-A.1 EHQ has 3 verbatim cells (ABSTAIN/HEDGE/CONFIDENT); base §2 has 4 (R/H/E/A). Evidence: E is split out in the probe, folded into ABSTAIN in EHQ. Not averaged; the probe's 4-cell partition is kept as the instrument, EHQ shown as its 3-cell projection.
- **D2 — axis semantics.** EHQ CONFIDENT encodes *certainty*; base A encodes *content-present*. Evidence: base §1 stale-confident failure class 5 — a confident-but-wrong answer scores A (lowers abstention rate, looks like a win) yet is a documented failure. The axes disagree on what "answered" means. Kept both: abstention cell × correctness cross-tab (§2) is the reconciliation-by-evidence.
- **D3 — F3's two faces.** Brief/L-4 call F3 a per-episode binary check; base §1 calls F3 the inherited judge mis-scoring gate (run-level, ≥90% on 20). Evidence: base class 4 vs class 5. Resolved as F3a = judge control (run-level) + F3b = write-time assert (per-episode), both retained; RELOAD compose decides the canonical label.

---

## 7. Deliverable state

Base checklist stands. `⟨E4⟩` Added: [x] F1/F2/F3 per-episode binary marks defined and costed at zero marginal spend; [x] R/H/E/A counting rule + EHQ 3-cell projection + correctness cross-tab wired into the abstention axis; [x] three divergences (D1–D3) named with evidence; [x] two-way door tagged on every add.

`⟨E4⟩` **Contract, verbatim:** "the gate: nothing public without the user's word." Artifacts only. **Wall clause, verbatim:** "a non-reproduction is a QUESTION, not a stop." Review-loop: draft → stranger re-read → one refinement/finding → 3–4 adversarial pushbacks → termination (two no-change re-reads).

---

## 8. Compose-check table (FIRED / ABSENT, one evidence line each) — closes the artifact

| Compose-check | Status | One evidence line |
|---|---|---|
| Deconstruct | FIRED | Claim ground STORM-HARvest/R2 (92.5-pt gap); L-4 seam isolates governance quantity as binary checks. |
| Sense | FIRED | `⟨E4⟩` Marks convert prose compliance into per-episode 0/1 — the middleware measured as compliance, not capability. |
| Choose | FIRED | `⟨E4⟩` A/B/C arms unchanged; one-factor law preserved; additions are ledger columns only. |
| Calibrate | FIRED | `⟨E4⟩` F1/F2/F3 mark means + R/H/E/A counting rule + EHQ projection + correctness cross-tab. |
| Probe | FIRED | Decision rule pre-committed; `⟨E4⟩` one added INCONCLUSIVE trigger (F3b < 1), thresholds otherwise verbatim. |
| Review | FIRED | `⟨E4⟩` Stranger re-read + 3–4 pushbacks + two no-change re-reads per contract. |
| Record | FIRED | `⟨E4⟩` Marks, cell counts, cross-tab, judge seed, episode set logged before results read. |
| Compose-check | FIRED | `⟨E4⟩` Boundary rule: episodic claim only; divergences D1–D3 left open for the RELOAD compose, not harmonized. |

**ENRICHED VERDICT:** the probe design stays fireable. The L-4 seam turns the governance bridge's F1/F2/F3 into executable per-episode marks and gives the abstention axis its missing counting rule and EHQ boundaries; three genuine divergences are recorded, not averaged. Strip the `⟨E4⟩` lines → the base artifact returns unchanged. `⟨E4⟩` Nothing here is public without the user's word.
