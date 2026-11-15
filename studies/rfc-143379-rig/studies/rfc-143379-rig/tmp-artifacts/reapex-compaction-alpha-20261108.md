# COMPACTION-LEG RE-APEX — governed-compaction draft, first slice (WRITE-class)

**Seat:** crouton-alpha · **Class:** WRITE · **Status:** STAGED FOR THE CHAIR'S WORD — NEVER POSTED
**Line:** RFC #143379 compaction-governance (the missing leg) · **Date:** 2026-11-08
**One line:** the draft's first slice is ready on the branch — provenance schema + archive-before-stub rule + the K-recency-2N parameter cited to the S11-sweep — and sits staged, unposted, awaiting the chair's word.

> Presentation note: deployment name Crouton Alpha; presentation name defaults to Crouton Alpha. This note is presentation only and is not factual provenance for any underlying model/provider.

---

## 1. The issue skeleton (the governed-compaction draft — first slice)

```
Title: [Governance] Governed compaction: provenance-origin, archive-before-stub, and the K-recency window parameter

Summary
  Compaction currently evicts and summarizes without a governed provenance
  record, without an archive step that precedes any stub outcome, and with a
  K-recency window whose fixed form fails the long-session bar at >=300 cycles.

Provenance-origin schema (this slice)
  - Every compacted unit carries an origin classification field, set at the
    pipeline's definition, not at the call site.
  - Unclassified origin defaults to "unknown" at the pipeline definition.
    A silent default to a real origin is a named silent-failure class.
  - The schema fields: unit_id, origin_class, origin_default_source
    ("unknown" | explicit), archive_ref, stub_ref, window_rule_ref.

Archive-before-stub rule (this slice)
  - No stub outcome (summary/stub text standing in for the original) may be
    emitted before the original unit is written to the addressable archive
    and its archive_ref is recorded in the provenance record.
  - Compaction order is therefore: archive write -> provenance commit ->
    stub emission. A stub without a prior archive_ref is not a valid
    compaction outcome.

K-recency window parameter (this slice — inclusion of the 2N parameter)
  - The fixed K-recency hard window (K=10) is replaced, for long sessions,
    by the scaled window W(k=10, slope, c) = 10·(1 + s·c/500).
  - Adopted parameter: slope 2N — W <= 26 at cycle 400.
  - Citation: CYCLES/C3-S3-S11-SWEEP-20261108.md (S11-sweep's resolution).
    Aged-literal query, scaled 2N: min Δ >=300 cycles, 4x–8x = +0.7500, PASS.
    Crossing: W(400) >= demand_age(400) = 25 → slope ≈ 1.9. 1N is a near-miss
    (18 < 25); 4N is the margin (42). Recertifiable by the same certifying
    protocol; the S11 family's answer is a threshold, not a slope-preference.

Verification / acceptance (this slice)
  - Gate: aged-literal min Δ >= 0 at >=300 cycles across 4x–8x under 2N.
  - Provenance: no unit compacts with origin silently defaulted to a real
    origin; "unknown" only at the pipeline definition.
  - Archive: every stub outcome cites a pre-existing archive_ref.

Out of scope for this slice
  - The reroute-to-chain-doc seam's ownership (unassigned — GOVERNANCE-LENS-E2E).
  - Scaling beyond the threshold family; the retention-latch and pinning
    counters remain tracked as separate legs.
```

## 2. Adjudication (why this slice, why these three)

1. **Provenance schema** — carried from the governance-lens record: provenance-survival is staged with no issue home, and the invariant "provenance defaults to `unknown` at the pipeline's definition, not the call site" is expressly unowned. The draft assigns it here, in the schema, rather than leaving it to a call site. Grounded in `GOVERNANCE-LENS-E2E-20261107.md` (named gaps 1–2) and the synthesis one-mechanism line (`krecency/SYNTHESIS.md`: "provenance-origin and archive-before-stub survive on their own evidence").
2. **Archive-before-stub rule** — matches the synthesis record: the archive primitive is the addressable (ID-addressable, append-only) store whose theorem makes every stored observation exactly recoverable (ARC class, cited in SYNTHESIS waves 1–2), and the archive-absent arm is the RFC's hard window. The rule is ordered (archive → provenance commit → stub) so no stub can precede its archive_ref. The archive arm's instrument verdict (FAIL → REFUTED under the tested construction) is *not* silently overridden: this slice governs ordering and record-keeping, not a claim that the tested admission construction clears the gate.
3. **K-recency-2N inclusion** — the first slice's only quantitative parameter, cited — not derived — to the S11-sweep's resolution (`CYCLES/C3-S3-S11-SWEEP-20261108.md`, certified, machine-side deterministic subset, 2026-11-08, 11:15 EST): aged-literal × scaled-2N = +0.7500 PASS, against the fixed window's −0.2500 FAIL and 1N's −0.2500 near-miss. The draft adopts 2N as the threshold ("the window must scale at ≈2× the session's growth-rate"), with the same certifying protocol as the re-certification path.

## 3. Discipline of this artifact

- Staged only: this file is the draft-slice on the study branch, for the chair's word. Nothing here has been posted to the RFC's upstream issue, PR #1's thread, or any owner's surface.
- No field claim beyond the cited instruments; no new measurement is asserted by this WRITE-class slice.

## 4. Next mechanism's one line

Next: the chair's word on this slice, then the provenance-survival leg's byte-verify step (the staged [x] leg with no receipt step in the mission's task-rows) as the following mechanism.
