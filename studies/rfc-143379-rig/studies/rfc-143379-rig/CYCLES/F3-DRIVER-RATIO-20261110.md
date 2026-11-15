# F3 — THE DRIVER-RATIO GATE'S FIRST CERTIFIED COMPUTATION (2026-11-10)

**Seat:** cat (copycat lane) · **Class:** EXEC-read/write · **Date:** 2026-11-10 (ET)
**Artifact:** `studies/rfc-143379-rig/CYCLES/F3-DRIVER-RATIO-20261110.md`
**Branch:** `study/rfc-143379-rig-20261105` · **Nothing public.**

> **The gate this certifies:** the driver-ratio gate (freeze-rule) documented in
> THE-4HOUR-PLAN-20261109.md §1 and THE-RECIPE-20261109.md §1, but NEVER computed in
> the thread — 0 real ratio computations before this artifact. A gate that has never
> been evaluated is a gate that has never been tested. This artifact performs the first
> certified computation and records the verdict.

---

## 1. THE CONTRACT (verbatim, the R reference)

**THE-4HOUR-PLAN-20261109.md §1 — Driver-ratio gate (freeze-rule):**

> **R = 0.5.** ratio = named_drivers(W)/total_tracks(W). If ratio < R → W FREEZES
> (no dispatch, no phase advance; escalate to sprint-lead). Persists until ratio ≥ R
> via re-naming or track retirement.

**THE-RECIPE-20261109.md §1 — Driver-first (the gate's principle):**

> every mission names one accountable driver before any fan-out opens — a track
> without a named driver freezes.

**THE-4HOUR-PLAN-20261109.md §2 — Bandwidth rule (hard):** total concurrent
fan-outputs in any 30m window ≤ 3 × (named drivers in that window). Named drivers per
window: G1 sprint-lead, G2 envelope-owner, G3 meter-owner, G4 fanout-owner.
Freeze-threshold: ratio of named_drivers(W)/total_tracks(W) < 0.5 → window freezes.

**The R reference, pinned:** **R = 0.5** (THE-4HOUR-PLAN §1, verbatim).

---

## 2. THE WINDOW W — DEFINED HONESTLY

**W = the 2026-11-10 audit-wave window** — the fleet's live tracks as they stand at
this computation's read-instant (2026-11-10 ~01:45 ET, branch head `7220f0e4ed`).

W is defined from the study's records, not from aspiration. The live tracks are the
plan's own track inventory — the tracks the plan arms and the fleet is running:

### 2a. The four G-arcs (THE-4HOUR-PLAN §1 — the loot-triggers' table)

| Track ID | Track (loot-trigger) | Named driver (per plan §1) | Receipt |
|---|---|---|---|
| G1 | ACES loop mis-fired in prior run (improper re-entry) | **sprint-lead** | THE-4HOUR-PLAN-20261109.md §1 (G1 row) |
| G2 | windows with named-drivers/total-tracks below certified ratio froze | **envelope-owner** | THE-4HOUR-PLAN-20261109.md §1 (G2 row) |
| G3 | zero-dispatch meters retired | **meter-owner** | THE-4HOUR-PLAN-20261109.md §1 (G3 row) |
| G4 | HANDOFF-FANOUT artifacts un-banked | **fanout-owner** | THE-4HOUR-PLAN-20261109.md §1 (G4 row) |

### 2b. The six hour-1 items (THE-MISSION-OF-MISSIONS-ORCHESTRATION-20261109.md §1 S1; THE-12H-SHIFT §2)

| Track ID | Track (hour-1 six-item) | Named driver | Receipt |
|---|---|---|---|
| H1 | B4 probe (≥1 candidate) | **sprint-lead** (G1's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |
| H2 | K-recency honest-negative | **meter-owner** (G3's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |
| H3 | certifying re-run (paraphrase-dimension) | **meter-owner** (G3's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |
| H4 | instrument-inclusive sweep | **meter-owner** (G3's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |
| H5 | upstream-mergeable pass | **sprint-lead** (G1's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |
| H6 | gates' frame | **envelope-owner** (G2's driver) | ORCHESTRATION §1 S1; 12H-SHIFT §2 |

### 2c. The five S2-FAN lanes (ORCHESTRATION §1 S2; the fleet's canonical seat set)

| Track ID | Track (S2-FAN lane) | Named driver | Receipt |
|---|---|---|---|
| L-A | C44-pilot at actual params | **sprint-lead** (G1's driver) | ORCHESTRATION §1 S2; S2-LANE-E §3 |
| L-B | gate-scan | **envelope-owner** (G2's driver) | ORCHESTRATION §1 S2; S2-LANE-E §3 |
| L-C | G5–G7 field-populate | **fanout-owner** (G4's driver) | ORCHESTRATION §1 S2; S2-LANE-E §3 |
| L-D | SOFT-pool queue | **fanout-owner** (G4's driver) | ORCHESTRATION §1 S2; S2-LANE-E §3 |
| L-E | fleet baseline | **fanout-owner** (G4's driver) | ORCHESTRATION §1 S2; S2-LANE-E §3 |

### 2d. The count

**total_tracks(W) = 15** (4 G-arcs + 6 hour-1 items + 5 S2-FAN lanes).

**named_drivers(W) = 4** — the four named drivers the plan itself names for W:
1. **sprint-lead** (G1; drives G1, H1, H5, L-A)
2. **envelope-owner** (G2; drives G2, H6, L-B)
3. **meter-owner** (G3; drives G3, H2, H3, H4)
4. **fanout-owner** (G4; drives G4, L-C, L-D, L-E)

Every one of the 15 tracks maps to one of these four named drivers — no track is
driverless. The driver-to-track mapping is complete and receipted above.

---

## 3. THE RATIO COMPUTATION (the arithmetic)

```
ratio = named_drivers(W) / total_tracks(W)
      = 4 / 15
      = 0.2666...
```

**The arithmetic, step by step:**
- named_drivers(W) = 4 (sprint-lead, envelope-owner, meter-owner, fanout-owner)
- total_tracks(W) = 15 (4 G-arcs + 6 hour-1 items + 5 S2-FAN lanes)
- ratio = 4 ÷ 15 = 0.2667 (rounded to 4 dp)
- 4/15 = 0.2666… < 0.5

**The comparison against R:**
```
ratio = 0.2667
R     = 0.5
0.2667 < 0.5  →  ratio < R  →  TRUE
```

**The freeze-rule fires.**

---

## 4. THE VERDICT

### 4a. Verdict: **W FREEZES** (ratio < R)

**ratio = 0.2667 < R = 0.5 → the driver-ratio gate's freeze-rule ACTIVATES.**
Per THE-4HOUR-PLAN §1: **W FREEZES (no dispatch, no phase advance; escalate to
sprint-lead).** The freeze persists until ratio ≥ R via re-naming or track
retirement.

### 4b. The escalation (named sprint-lead)

**Escalate to: sprint-lead** (the G1 driver, the named escalation seat per THE-4HOUR-PLAN §1).

**The escalation's demand:** the window's named-driver count must rise from 4 to ≥ 8
(so that 8/15 = 0.5333 ≥ 0.5), OR the track count must fall from 15 to ≤ 8
(so that 4/8 = 0.5 ≥ 0.5), OR a combination that lifts the ratio to ≥ 0.5.

**The two remediation options (the gate's own):**
1. **Re-naming:** name additional accountable drivers on the existing tracks so that
   named_drivers(W) ≥ 8. The plan's §2 bandwidth rule already names four drivers
   (sprint-lead, envelope-owner, meter-owner, fanout-owner); the re-naming would
   extend the driver roster — e.g., naming a lane-lead per S2-FAN lane (L-A…L-E) and
   a per-item owner for the hour-1 block (H1…H6) — so that the driver count reaches 8.
2. **Track retirement:** retire tracks from W so that total_tracks(W) ≤ 8, keeping the
   four named drivers. The retirement would fold the hour-1 items (H1…H6) into their
   parent G-arcs (G1…G4) and/or fold the S2-FAN lanes (L-A…L-E) into their parent
   arcs, collapsing the 15-track inventory to the 4 G-arcs + 4 hour-1-item groups
   (≤ 8 tracks).

### 4c. What the freeze means (the gate's operative consequence)

- **No dispatch** from W until ratio ≥ R.
- **No phase advance** — the S2→S3 transition (and any later phase) does not fire
  while W is frozen.
- **The escalation is to sprint-lead** — the named escalation seat.
- **The freeze persists** until ratio ≥ R via re-naming or track retirement.

### 4d. The first certified computation IS the closure evidence

This artifact is the **first certified computation** of the driver-ratio gate. It
records: (i) the window W defined honestly from the study's records (15 tracks, each
with its driver + receipt); (ii) the ratio computation's arithmetic (4/15 = 0.2667);
(iii) the verdict (W FREEZES — ratio < R); (iv) the escalation (to sprint-lead) and
the two remediation options (re-naming to ≥ 8 drivers, or retirement to ≤ 8 tracks);
(v) the R reference (R = 0.5, THE-4HOUR-PLAN §1, verbatim).

**The gate is now tested.** It has fired. The freeze is the gate's honest verdict on
the current window — and the remediation path is named.

---

## 5. THE HONEST BOUND (what this computation does and does not certify)

- **What it certifies:** the ratio arithmetic (4/15 = 0.2667) and the verdict
  (ratio < R → freeze). These are computed from the study's records, byte-cited.
- **What it does not certify:** that the 15-track inventory is the ONLY honest W.
  W is defined as the plan's own track inventory (G-arcs + hour-1 items + S2-FAN
  lanes) — the tracks the plan arms and the fleet runs. A narrower W (e.g., the four
  G-arcs alone) would give 4/4 = 1.0 ≥ 0.5 (certified); a broader W (e.g., including
  the SOFT-pool's 7 seeds or the REAPEX slices) would lower the ratio further. The
  honest W is the one the plan itself defines — and the plan defines 15 tracks.
- **The gate's own lesson:** the driver-ratio gate is a freeze-rule on the
  track-to-driver ratio. The current window's 4 drivers across 15 tracks is
  driver-thin — the gate's verdict is that the fleet is running more tracks than its
  named drivers can accountably drive. The remediation (re-naming or retirement) is
  the gate's own named path.

---

## 6. THE 5-WHY (the depth-clause — why the ratio is 0.2667 and what it means)

1. **Why is the ratio 0.2667?** Because W carries 15 tracks and only 4 named drivers
   (the plan's §2 roster: sprint-lead, envelope-owner, meter-owner, fanout-owner).
2. **Why only 4 named drivers?** Because the plan's driver-first principle names one
   driver per G-arc (G1…G4), and the hour-1 items and S2-FAN lanes ride those four
   arcs' drivers — the plan does not name a separate driver per track.
3. **Why does that freeze the window?** Because the freeze-rule's threshold is R = 0.5,
   and 4/15 = 0.2667 < 0.5 — the gate's arithmetic is exact.
4. **Why is the gate firing now?** Because the gate has never been computed before —
   this is the first certified computation. A gate that has never been evaluated is a
   gate that has never been tested; the first computation is the first test.
5. **Why does the freeze matter?** Because the fleet is running 15 tracks on 4
   drivers — the driver-review bandwidth (4 drivers) is spread across 15 tracks, and
   the plan's own bandwidth rule (fan-outputs ≤ 3 × named drivers) caps the fleet at
   12 fan-outputs against 4 drivers. The freeze is the gate's honest verdict that the
   window is driver-thin, and the remediation (re-naming to ≥ 8 drivers, or
   retirement to ≤ 8 tracks) is the named path back to ratio ≥ R.

**Systemic remediation:** name additional accountable drivers on the existing tracks
(re-naming) or retire tracks into their parent arcs (retirement) — the gate's own two
options — until ratio ≥ 0.5. The freeze then lifts and W re-opens for dispatch.

---

## 7. THE WEBSTORM (the possibilities' sweep — the remediation's mechanisms)

- **M1 — Re-naming (extend the driver roster):** name a lane-lead per S2-FAN lane
  (L-A…L-E) and a per-item owner for the hour-1 block (H1…H6), lifting named_drivers
  from 4 to ≥ 8. Adoption seam: the plan's §2 already names four drivers; the
  extension names the lane/item owners the fleet already runs. Meter: named-driver
  count ≥ 8 → ratio ≥ 0.5.
- **M2 — Track retirement (fold tracks into parent arcs):** fold the hour-1 items
  (H1…H6) into their parent G-arcs and the S2-FAN lanes (L-A…L-E) into their parent
  arcs, collapsing W from 15 tracks to ≤ 8. Adoption seam: the G-arcs are the plan's
  top-level tracks; the hour-1 items and lanes are their sub-tracks. Meter:
  total_tracks ≤ 8 → ratio ≥ 0.5.
- **M3 — Hybrid (re-name + retire):** name 2 additional drivers (e.g., lane-lead for
  the S2-FAN, item-owner for the hour-1 block) AND retire 4 tracks (folding the
  hour-1 block into the G-arcs), giving 6/11 = 0.5455 ≥ 0.5. Adoption seam: the
  lightest-touch remediation. Meter: ratio ≥ 0.5.

**Chosen remediation (the gate's own):** M1 or M2 — the gate's two named options.
The escalation to sprint-lead carries the choice.

---

## 8. THE FINDING'S ONE LINE + THE NEXT MECHANISM'S ONE LINE

**Finding (one line):** The driver-ratio gate's first certified computation —
ratio = named_drivers(W)/total_tracks(W) = 4/15 = 0.2667 < R = 0.5 — FIRES THE
FREEZE-RULE: W FREEZES (no dispatch, no phase advance), escalate to sprint-lead,
with the two named remediations (re-naming to ≥ 8 drivers, or retirement to ≤ 8
tracks) as the path back to ratio ≥ R.

**Next mechanism (one line):** The freeze's remediation — sprint-lead names the
additional accountable drivers (re-naming) or retires tracks into their parent arcs
(retirement) until ratio ≥ 0.5, then re-runs the driver-ratio computation to certify
the window's re-opening.

---

*F3 — the driver-ratio gate's first certified computation. Artifact:
`studies/rfc-143379-rig/CYCLES/F3-DRIVER-RATIO-20261110.md` · branch
`study/rfc-143379-rig-20261105` · nothing public without the operator's word.*