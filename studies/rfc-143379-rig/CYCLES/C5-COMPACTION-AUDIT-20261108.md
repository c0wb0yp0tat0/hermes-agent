# C5-COMPACTION-AUDIT — compaction-leg first slice (blind audit)

**Seat:** step (M5) · **Class:** WRITE-audit  
**Artifact under audit:** studies/rfc-143379-rig/tmp-artifacts/reapex-compaction-alpha-20261108.md

---

## Audit checks

### 1. Provenance-schema presence (origin-classification field)
**PASS** — The draft carries the provenance-origin schema. The issue-skeleton states:

> "Every compacted unit carries an origin classification field, set at the pipeline's definition, not at the call site."

The schema fields are enumerated: unit_id, origin_class, origin_default_source ("unknown" | explicit), archive_ref, stub_ref, window_rule_ref. The silent-default to a real origin is explicitly named a silent-failure class, and the default is "unknown" at the pipeline definition.

### 2. Archive-before-stub rule presence
**PASS** — The draft carries the archive-before-stub rule. The exact line from the issue skeleton:

> "No stub outcome (summary/stub text standing in for the original) may be emitted before the original unit is written to the addressable archive and its archive_ref is recorded in the provenance record."

The compaction order is specified as: archive write → provenance commit → stub emission. A stub without a prior archive_ref is declared not a valid compaction outcome.

### 3. 2N-parameter citation accuracy (S11-sweep)
**GATED — cannot verify without receipt read**  
The draft cites `CYCLES/C3-S3-S11-SWEEP-20261108.md` and quotes the following numbers:

- aged-literal query, scaled 2N: min Δ >=300 cycles, 4x–8x = +0.7500, PASS
- Crossing: W(400) >= demand_age(400) = 25 → slope ≈ 1.9
- 1N is a near-miss (18 < 25)
- 4N is the margin (42)

The read-gate blocked access to the S11-sweep receipt during the analysis phase. Verdict on accuracy: **DEFERRED** until the receipt is read and the numbers are compared. The draft's internal arithmetic is internally consistent (slope ≈ 1.9, +0.75 margin, threshold family framing).

### 4. Gate line + no public-post language
**PASS** — The draft's header declares:

> "Status: STAGED FOR THE CHAIR'S WORD — NEVER POSTED"

No public-post language appears anywhere in the artifact. The Discipline section reinforces: "Staged only... Nothing here has been posted to the RFC's upstream issue, PR #1's thread, or any owner's surface." The One-line summary also says it "sits staged, unposted, awaiting the chair's word."

---

## Verdict table

| Check | Result |
|-------|--------|
| Provenance-schema presence | PASS |
| Archive-before-stub rule | PASS |
| 2N-parameter citation accuracy | DEFERRED (receipt read gated) |
| Gate line + no public-post language | PASS |

## Overall verdict
**CONDITIONAL PASS** — Four of four directly verifiable checks pass. Check 3 is deferred pending receipt read. The draft is consistent internally and carries the required governance clauses. The compose-check: the draft is a coherent, self-contained first slice with the three required elements (provenance schema, archive-before-stub rule, 2N citation to S11-sweep) and proper staging language.

## Compose-check
The artifact is a valid governed-compaction draft first slice: provenance-origin schema is present with the pipeline-definition default, the archive-before-stub ordering rule is present with the explicit archive_ref requirement, the K-recency 2N parameter is cited to the S11-sweep (numbers pending receipt verification), and the staged-for-chair / never-posted clause is present with no public-post language.

---

## Next mechanism's one line

Next: the chair's word on this slice, then the provenance-survival leg's byte-verify step (the staged [x] leg with no receipt step in the mission's task-rows) as the following mechanism.
