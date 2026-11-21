# RELEASE-CONDITION-20261121 — the compaction's release condition (GAP-4) + the gate's pair

*Routing: study/rfc-143379-rig-20261105 · RFC quiet (this leg writes nothing upstream) · write-window 7 · Gate: two-way door — reversible at the card, nothing public.*

## 1. Why this card exists

KIT-INVENTORY-20261121's FINAL SECTION (the kit's gap list) names it: *"the compaction's release-point — no piece names when compaction may release a horizon (the kit's compaction is density-aware, reserving the highest-loss-likelihood anchor as necessary-not-sufficient; the release-point condition is unnamed)."* CROSSCHECK-20261121's Row C2 draws the seam exactly: the F2 release-point **gate** is receipted (precision 1.0, FP 0, completeness 100%) while the **condition** — the rule that names when a horizon may be released — is the gap; *"the gate measures the probe, it does not name the release horizon."* GOAL-VERDICT-20261121 §3 (GAP-4) assigns the card's shape: *"A card that names the release rule the fail-safe grid does not define; the gate is receipted, the condition is the rule the gate does not state — the two seams are separate."*

This card is that rule, pre-committed before any run, with its witnesses and its revert. It is a naming question, not a wiring change: the gate's mechanism (P3-RELEASE-POINT-20261120/F2, wired at `hermes_state_mutation_compress.py:17-25`, flag `GOVERNED_COMPACTION_RELEASE_RULE`) is untouched; the card states the condition the mechanism enforces. Additive in the kit folder; deletion reverts.

## 2. The condition (the rule, verbatim)

> **A horizon may be released only when every block it releases is citable AND the horizon's reserved set survives the release. Citation without reservation is insufficient (a cited block can still lose the non-re-observable fact); reservation without citation is insufficient (an unwitnessed release). Both are necessary; the conjunction is the condition.**

The rule composes the record's two named mechanisms — it invents no third:
- **the gate's rule** (P3-RELEASE-POINT-20261120 §3.1, verbatim): *"release a block only when the teacher can cite the event that ended its use."* Citation = a named event id (`release_event_id`, 16+ hex chars) + `final_use_ts` bound to the block's lineage row; no citation ⇒ held + logged with reason.
- **the kit's reservation** (KIT-INVENTORY gap row; NEGENTROPY-SWEEP-C-BUDGET-20261006 §(c)): the compaction is density-aware — it reserves the highest-loss-likelihood anchor (the minimal reservable unit = the decision-core verdict's verbatim claim), and that reservation is **necessary-not-sufficient** (the W2 empty-answer confound: the anchor survives into `summary_text` yet the answer is empty).

### 2.1 The three tests (each traced)

| # | Test | Reads | Trace |
|---|---|---|---|
| **T1 · CITABLE** | every block the release would archive carries its citation (`release_event_id` 16+ hex + `final_use_ts` bound to the lineage row); the uncited are held, not released | the block's lineage row | P3 §3.1 + §3.2 (arm B: citable → `archive`, uncited → `keep`); `probes/release_point_gate.py::LineageRow.is_archive_eligible` |
| **T2 · ARCHIVED-NOT-STUBBED** | the release is an archive, not a stub: the original stays byte-intact and resolvable — the compacted unit carries a resolvable origin back to its archived original | the archive read-back | the RFC's archive-before-stub clause + its one-way-door flag (*"keep the archive-before the stub, always"*); MASTER-TEAM-M3 §2 wiring point (`hermes_bootstrap.py`: *"deferred blocks stay byte-intact (archive-before-stub), so a deferral is a hold, never a loss"*) |
| **T3 · RESERVED** | the horizon's reserved set survives: the density-aware anchor (the highest-loss-likelihood anchor) is carried onto the child / re-readable after the release | the retention read-back | KIT-INVENTORY gap row; NEGENTROPY-SWEEP-C-BUDGET §(c) (one-anchor necessary-not-sufficient); KIT-SKEPTIC-20261107 (b4) |

**The eligibility inputs that are NOT the condition** (named so they are not confused with it): the provenance-origin classification and the K-recency window stay eligibility inputs; the citation is the gate on top (MASTER-TEAM-M3 §2, "The check").

## 3. The witnesses (what satisfies each test)

| Test | Witness | Receipted by |
|---|---|---|
| T1 | the per-decision gate row `(compaction_event_id, guard_outcome="honored", release_hold, rerun_flag, payload_hash)`, one per compaction decision | `probes/battery_luna.py::check_f2` (fields verbatim) |
| T1 | the citation verifies: the cited `release_event_id` hashes to the block's actual final-use event | the precision bar's numerator (P3 §3.4) |
| T2 | the archive resolves: the compacted unit's origin resolves to the archived original | the provenance read-back (the SJC 83% guard class) |
| T3 | the reserved anchor re-reads: the anchor's verbatim claim re-reads from the child | the retention read-back (the read-restore suite class; PILOT-VERDICT 42/42) |

## 4. The pre-commitment (fixed before any run)

The condition, its witnesses, and the bars below are fixed here, before the run — no post-hoc swaps (the same discipline the F2 bars and the episode set were pre-committed with):

| Bar | Definition | Threshold | First receipted instance |
|---|---|---|---|
| **precision** | of the released blocks, the fraction whose citation verifies | **>= 0.95** (fail < 0.80) | 15/15 = **1.000** (F2 citation arm, `test_citation_arm.py` 4/4) |
| **FP** | releases of blocks with no citable ending event (the silent archive) | **= 0** | **0** |
| **completeness** | of the truly-citable blocks, the fraction released | **= 100%** | 15/15 = **100%** |

- **Episode class** (pre-committed): the non-re-observable-fact class — `make_episode(seed, cut_point=12)` (`probes/battery_pilot.py:31`), `SEEDS = (11, 23, 37)` × `N_TURNS = 10` = **30 episodes**, mirrored verbatim across arms (one-factor law). [P3 §3.3; F2-CITATION-ARM-20261120 §2]
- **Verdict**: **PASS** iff precision >= 0.95 AND FP = 0 AND completeness = 100% · **FAIL** iff FP > 0 OR precision < 0.80 OR completeness < 100% · **INCONCLUSIVE** iff the run's own pre-conditions fail — *rewrite the experiment, never the claim.* [P3 §3.6]

## 5. One rendered instance (cold-grounded, no invented counts)

The condition's first receipted instance is the F2 citation arm's arm-B horizon (P3-F2-BATTERY-RECEIPTS-20261120, the UPDATE row — the actual run, not an expectation):

```
release-condition verdict (GAP-4 shape) — F2 citation arm, arm B (gate ON)
horizon:     the arm's 30 prepared in-place compressions (SEEDS 11/23/37 x N_TURNS 10, cut_point 12)
T1 CITABLE:  15 cited blocks released · 15 uncited held (F2-HOLD, the wired gate verbatim)
T2 ARCHIVED: the release is an archive; the prepared snapshots stay byte-intact (the hold = deferral, not loss)
T3 RESERVED: not receipted by the arm — the arm's payload_hash row names the episode's planted fact, but no retention read-back runs; T3 rides the substrate's read-restore suite (42/42)
witnesses:   per decision, the check_f2 row (compaction_event_id, guard_outcome=honored, release_hold, rerun_flag, payload_hash)
bars:        precision 1.000 (>= 0.95) · FP 0 (= 0) · completeness 100% (= 100%)  ->  PASS
```

**What is verified here, and what is honestly scoped.** The counts are the arm's own receipts (4/4 GREEN; the L3 re-verification `test_citation_arm.py 4/4 passed in 3.64s`, MISSION-BRIEF-MASTER §7-j); the verdict row is the condition's shape applied to them. T1's witness is the arm's. **T3's witness is not the arm's** — the arm does not read retention back; T3 rides the substrate's read-restore suite (PILOT-VERDICT: 42/42 on the fork), and the card says so rather than borrowing the arm's receipt. The condition is stated for the horizon; the horizon-level run that receipts all three tests together is the next instrument, not this card.

## 6. The revert (the two-way doors)

| Move | Reversibility | Rollback |
|---|---|---|
| shadow → enforce | the flag `GOVERNED_COMPACTION_RELEASE_RULE` | flip to `OFF`; held blocks re-admit next cycle, bytes intact [P3 §3.7] |
| the condition's revision | the card is a gate state, revisable by evidence (method-card 1: the two-way-door verdict + the receipt stamp) | a revised card supersedes; the record's own correction machinery carries it |
| the card itself | additive in `kit/`; a naming question, not a wiring change | delete the file |
| public → private | the gate | re-arm to last private value |

## 7. Composition check (5 marks)

1. **deconstruct** — GAP-4's gap row (KIT-INVENTORY) + C2 + GOAL-VERDICT §3; the gate's rule (P3 §3.1) and the reservation (KIT-INVENTORY / SWEEP-C §(c)) are the two named mechanisms composed. ✓
2. **sense** — the condition = citation (necessary) ∧ reservation (necessary), neither sufficient alone; "necessary-not-sufficient" is the record's own phrase. ✓
3. **choose** — named `RELEASE-CONDITION-20261121.md` in the kit folder; additive; the gate's pair (the mechanism's rule), not a new mechanism. ✓
4. **calibrate** — the bars, the episode class, and the verdict rule are the F2 battery's pre-committed values; the rendered instance's counts are the arm's actual receipts. ✓
5. **probe** — T3's witness is honestly scoped (the substrate's 42/42, not the arm's); the revert names the flag flip + the card's deletion. ✓

## Fold line

RELEASE-CONDITION 2026-11-21 — the compaction's release condition named (GAP-4), pre-committed before any run: a horizon may be released only when every block it releases is citable AND the reserved anchor survives; the witnesses (the check_f2 gate row · the citation verification · the archive resolvability · the retention read-back), the bars (precision >= 0.95, FP = 0, completeness 100%), and the revert (the flag flip, bytes intact; the card additive). The gate's pair: the mechanism (P3/F2) is receipted, the condition is now stated. Two-way door: reversible at the card; nothing public; RFC quiet.
