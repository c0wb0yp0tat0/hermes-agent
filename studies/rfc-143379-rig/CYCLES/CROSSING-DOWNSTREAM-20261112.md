# CROSSING-DOWNSTREAM — the walk-back's second leg (the aftermath's fingerprints)

**Leg:** CROSSING-DOWNSTREAM-20261112 (2026-11-12, ET) · **Seat:** downstream-to-origin re-audit · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Gate:** nothing public without the operator's word · **Audit window:** 2026-11-05 → 2026-11-12 (the nights, their landing ring, the adoption-line) read backward-from-the-end.

**Mission line:** this leg reverses the arrow. The backward leg 1 (ARC-BACKWARD-LEG1) re-verified the nights from the middle; this leg walks from the landing ring — the comment's final form, the proof-reads, the adoption-line, the fleet's new surfaces — back across the whole duration to the seek-to-understand's birth (RFC #143379, the P2→P3→P4 trail). It asks what the upstream traveler cannot see: the aftermath's fingerprints on the middle, the final form's shadow on the early choices, the patterns the origin-side cannot see because they are only visible from the far end.

---

## 1. THE SEATS (the downstream anatomy)

| Seat | What it guards |
|---|---|
| **The comment's final form** | The landing ring: the deliverable that carries the nights' verdicts to the record. Its shape is the map of what the crew believed mattered at the end. |
| **The verification / proof-reads** | How the landing was checked: the receipts, the re-derivations, the hashes that had to agree. |
| **The adoption-line** | The ARC-landings: which mechanisms were picked up, which surfaces were rebuilt, which ones were left behind. |
| **The fleet's new surfaces** | Where the work migrated after the nights: the rewritten state, the new lanes, the renamed contracts. |
| **The seek-to-understand's birth** | RFC #143379 and the P2→P3→P4 trail: the origin. Seen reversed, this is where the aftermath's pressure first begins to show. |

---

## 2. WHAT IS ONLY VISIBLE FROM THE FAR END

The upstream traveler starts at the origin and walks forward: birth → nights → landing → adoption. They see each stage as it happens. They can describe the NIGHTS as events that happened, because they are inside them.

This seat walked from the END. From here, the past is not a sequence of events but a structure that the end holds together. What becomes visible only from downstream:

### 2.1 The nights' claims are held together by the landing ring, not by their own internal logic
Every claim in the nights — K-recency FAIL, E1/E2 REFUTED-BY-REPLICATION, E3 CELL-DEPENDENT, E4 SEAM-CONFIRMED — is a local statement about the bytes of that night. But the reason those statements survive into the record is that the landing ring re-derived them against the current head and banked their receipts. The nights do not stand on their own; they stand on the landing ring's re-verification. The downstream seat sees that the landing ring is the load-bearing wall, and that the nights are rooms built against it.

### 2.2 The final form's shadow on the early choices
The early choices (the P2→P3→P4 trail, the first summaries, the first "corrected" records) were made when the landing ring did not yet exist. Later, when the landing ring materialized as a re-verification discipline, it re-colored what the early choices meant. A claim that looked like progress in real time can look, from downstream, like a mis-step that the landing ring had to correct. The shadow is not a judgment — it is a structural fact: the early choices were legible in a different frame than the final frame.

### 2.3 The membership record's correction is the clearest example of the shadow
The early membership record carried the header `MEMBERSHIP-CONFIRMED`. The landing ring re-derived the record against the bytes and found it REFUTED-BY-REPLICATION (hard-coded `SEEDS_ONSET`, honest-blind R²=0.0000; corrected CSV 0.4/0.1, 160 rows). From downstream, this is the clearest demonstration of why the landing ring was necessary: the early frame verified the claim against the original authorship, while the end's frame verified it against the bytes. The two frames disagreed; only the end's frame holds.

### 2.4 The corrections are not "things that went wrong" — they are the landing ring doing its job
The three structural corrections — number-seam, meter citation, copycat directory — and the stale-state flag pointing to `HITL-READY` cand. 3 are often written as corrections to mistakes. Downstream, they are visible as the landing ring's normal operation: re-verification against current bytes. The nights were dense and fast; the landing ring is slow and careful. Their difference is not a failure of either; it is the reason the study can claim reproducibility.

### 2.5 The fleet's new surfaces are the landing ring's children, not the nights' triumphs
The adoption-line (ADOPTION-20261112.md and its siblings) is where the mechanisms got their afterlife. The downstream seat reads the adoption-line as a map of what the end valued: mechanisms that survived re-verification were picked up; mechanisms that could not be re-derived were refused (OVH, stale headers, the archive claim). This is not the nights' verdict — it is the landing ring's verdict, re-stated as the culture's next surface.

---

## 3. THE RECEIPTS (re-derived from the far end)

### 3.1 The landing ring re-derives the nights
- **K-recency gate** — FAIL, all horizons ≥300, worst −20.40pp @ 4×. Reproducible at the current head. The gate is the night's most durable claim: it survives because the landing ring re-derived it, not because the night's prose was persuasive.
- **Aliasing × proximity** — CONFIRMED-BOTH, R²=0.6548. A property of the pair, not a meter artifact. Downstream, this reads as the most honest finding: it has no corrective machinery attached.
- **E1 / E2** — REFUTED-BY-REPLICATION, on the mechanism, not the sample. With hard-coded onsets removed (2c3a5402dd), the metric drops to 0.00. The downstream seat reads this as the clearest refutation in the study: it does not depend on the sample, only on the mechanism.
- **E3** — CELL-DEPENDENT. Small+old cell 1.00 across every variant; other quadrants 0.00. Pattern recurrence-free.
- **E4** — SEAM-CONFIRMED (81% tiny+old lost). Load-bearing receipt = `RESULTS-PIN`. The brief-carried name is downstream-settled; the mechanism-name is corrected (the four-lens "agreement" leans on two different things: echo + distinct leans).
- **Membership V1** — REFUTED-BY-REPLICATION. Corrected record: CSV (0.4/0.1), 160 rows, hard-coded onsets removed. The header `MEMBERSHIP-CONFIRMED` is stale.
- **AOA family** — 14/18 phases match; rotation efficacy CONFIRMED; catch-D directory count corrected (3→4 files, pin 5a28a17ca2 banked); residual is the register count, not the method. Seam 2 and Seam 3 CONFIRMED; Seam 1 REFUTED then re-verified.
- **OVH** — REFUSED as ungrounded: historical driver records carried no bytes on the branch. The downstream seat treats this as the landing ring's first, strict act: no receipt, no claim.

### 3.2 The landing ring's corrections
1. **Number-seam** — `xfailed 1.83s` → `28 passed, 1 xpassed in 1.01s`; resolved to whole-anchor host-local row truth.
2. **Meter citation** — corrected to `AVREA-LEG-CONTRACT.md` (the 4-vCPU/1,500 is stale README/old-contract framing); README harmonization is the remedy.
3. **Copycat directory** — counted 3; 4 exist. Listing to four + a step.
4. **Stale-state** — "guarded re-runs in flight" lives in `HITL-READY` cand. 3.
5. **Membership** — corrected CSV; header retired.
6. **Audit-of-audit** — the AoA reproduced the summary's directory count (Catch D); the audit is a genuine second voice with one register gap.

---

## 4. THE AoA CROSSING (what this leg feeds)

This leg's deliverable is the downstream perspective: the aftermath's fingerprints on the middle, the final form's shadow on the early choices. It feeds the crossing as the counter-evidence to ARC-FORWARD's aggregate.

**This leg's one line:** the nights are not self-standing — they are rooms built against the landing ring's re-verification; the early choices were legible in a different frame than the final frame; and the adoption-line is the landing ring's verdict restated as the fleet's next surface. The crossing waits on the three prerequisite pins (A3 closure, cycle-stage lane fired, runner idle-fill gate operational) and on the triples sharing the same E3/E4 verdict on the current head.

---

## 5. THE VERDICT (downstream seat)

- **REPRODUCIBLE (byte-grounded):** the nights' durable claims (K-gate FAIL, aliasing CONFIRMED-BOTH, E1/E2 REFUTED-BY-REPLICATION, E3 CELL-DEPENDENT, E4 SEAM-CONFIRMED, membership V1 REFUTED, AOA CONFIRMED) survive because the landing ring re-derived them; the two refused records (OVH, archive claim, stale header) are refused because no receipt lives on the branch.
- **THE SHADOW (the downstream insight):** the early choices were made in the nights' frame, and the landing ring's frame is a different one. The adoption-line is the landing ring's verdict, not the nights'.
- **The crossing:** pending the three prerequisite pins and the triples' shared verdict.

**The one line this leg feeds into the crossing:** the past's claims are re-verified — the nights are rooms built against the landing ring, the early choices were framed in a different frame, and the adoption-line is the landing ring's verdict as the fleet's new surface. The crossing waits on the three prerequisite pins and on the triples' shared E3/E4 verdict.

---

*This file is the downstream seat's deliverable. It is written to the artifact path `CYCLES/CROSSING-DOWNSTREAM-20261112.md` on the study branch `study/rfc-143379-rig-20261105`, fork-only, with no public output without the operator's word.*
