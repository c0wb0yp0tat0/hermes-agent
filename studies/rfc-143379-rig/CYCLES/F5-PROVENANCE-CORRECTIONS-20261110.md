# F5 — Provenance Defects' Corrections
**Date:** 2026-11-10 (ET) · **Seat:** lane F5 of the 2026-11-10 audit-wave fleet · **Branch:** study/rfc-143379-rig-20261105 · **Role:** harness-lane (copycat seat)
**Rule applied:** the error-text is removed; the correction row explains it. No false PASS stands.

---

## 0 — Scope of this ledger

Three provenance defects were flagged by the SANITY lens (1-flag): the S3-SWAP gap
attributions are mis-sourced; and FOLD-1's §3 grader-citations cite a directory while
S2-LANE-A's PASS rests on an unfilled receipt. This ledger records each defect, the
bytes that prove it, and the corrected form. Every correction is a removal + replacement
row; no retroactive fill-in is permitted.

**Bytes quoted come from disk** (read-instant 2026-11-10). Commit SHAs referenced: FOLD-1
`628a5ece5c`, S3-SWAP `40b46904c2`, S3-SPLIT-D `d629635f00`.

---

## 1 — Defect #1: S3-SWAP's gap attributions are mis-sourced

### 1a — "fingerprint-integrity unconfirmed — surfaced by the byte-keyed G5–G7 leg (seat C's lane)"

**Original text (S3-SWAP §1, 2026-11-10):**
```
1. **fingerprint-integrity unconfirmed** — surfaced by the byte-keyed G5–G7 leg (seat C's lane).
```

**Finding (bytes say):**
- The string `fingerprint` has **zero (0) hits** in any of the five S2-LANE-*.md artifacts
  (S2-LANE-A, B, C, D, E — 2026-11-09). A gap cannot be "surfaced by" a seat that never
  names the term. The byte-keyed G5–G7 leg (S2-LANE-C) populated 3/3 fields and carries no
  fingerprint-integrity claim, confirmed or otherwise. The S3-SWAP attribution is
  self-generating: the swap argues its own attributions are load-bearing ("moving a
  different seat would break the byte-keyed provenance chain") — so the mis-attribution is a
  provenance defect, not a wording slip.

**Corrected form:**
```
Gap #1 — fingerprint-integrity: **unsourced — strike the attribution**.
The term "fingerprint" appears in no S2-LANE seat's landed text; no seat surfaced it.
The gap remains on the record as unconfirmed, with its owner (seat C) re-run pending
independent-witness line, but the "surfaced by seat C" attribution is removed.
```

### 1b — "1 needs-definition seed — surfaced by the gate-scan leg (seat B's lane)"

**Original text (S3-SWAP §1, 2026-11-10):**
```
2. **1 needs-definition seed** — surfaced by the gate-scan leg (seat B's lane).
```

**Finding (bytes say):**
- The term `needs-definition` (including the phrase "needs-definition seed") has **zero
  hits in any of the five S2-LANE-*.md artifacts**. It appears **only** in
  `S3-SPLIT-D-20261110.md`, whose row 7 defines the genuine needs-definition seed:
  - problem-statement: `meter "fold count per phase" lacks an independent-witness line`
  - seed-status: `needs-definition`
  - evidence-pointer: `orchestration §3 grader clause; S3 fold receipt; S2-LANE-D row 7`
- S3-SPLIT-D's row 7 is the actual carrier of the needs-definition seed (Lane D's SOFT-pool
  row 7: "meter 'fold count per phase' lacks independent-witness line", no receipt on disk).
  The gate-scan leg (S2-LANE-B) never names "needs-definition"; the swap invented the
  attribution to seat B. Recontextualizing: the needs-definition seed is a fold-count
  meter problem owned by Lane D, not a gate-scan problem owned by Lane B.

**Corrected form:**
```
Gap #2 — 1 needs-definition seed: **re-source to Lane D's SOFT-pool row 7**
(S2-LANE-D-20261109.md, row 7: meter "fold count per phase" lacks independent-witness
line; S3-SPLIT-D row 7 seed-status = needs-definition). The attribution "surfaced by the
gate-scan leg (seat B's lane)" is removed; the gap is owned by lane D with seed-status
needs-definition, per S3-SPLIT-D row 7.
```

### 1c — "fleet-baseline's phase-bound scaling — surfaced by the fleet-baseline leg (seat E's lane)"

**Original text (S3-SWAP §1, 2026-11-10):**
```
3. **fleet-baseline's phase-bound scaling** — surfaced by the fleet-baseline leg (seat E's lane).
```

**Finding (bytes say):**
- This attribution is **correct**. S2-LANE-E (fleet-baseline leg) is the only S2-LANE seat
  that records fleet-scaling and phase-bound scaling claims (concurrency-per-seat
  ≥1.5× per phase, measured at phase boundaries). No other S2-LANE seat surfaces this gap.
- **No correction required.** Retained verbatim.

---

## 2 — Defect #2: FOLD-1 §3 grader-citations cite a directory, not named files

### 2a — §3 "Artifact-path (receipt)" column names `studies/rfc-143379-rig/CYCLES/` (a directory) for all five lanes

**Original text (FOLD-1 §3, 2026-11-10):**
```
| Lane | Commit | Artifact-path (receipt) | Cert-receipt binding |
| A | `c58fea0e99` | studies/rfc-143379-rig/CYCLES/ (C44-pilot receipt) | cert receipt for C44-pilot PASS |
| B | `5f6647e540` | studies/rfc-143379-rig/CYCLES/ (gate-scan receipt) | cert receipt for gate-scan |
| C | `c649708e51` | studies/rfc-143379-rig/CYCLES/ (G5–G7 receipt) | cert receipt for byte-keyed fields |
| D | `876cbd0eb7` | studies/rfc-143379-rig/CYCLES/ (SOFT-pool receipt) | cert receipt for SOFT-pool |
| E | `dd1922088b` | studies/rfc-143379-rig/CYCLES/ (fleet baseline receipt) | cert receipt for fleet baseline |
```

**Finding (bytes say):**
- `studies/rfc-143379-rig/CYCLES/` is a **directory**, not an artifact path. It resolves to
  the parent folder of the five per-leg receipts. A citation that points at a directory
  names no receipt. Each lane's receipt is a **named file**, and each file's commit hash is
  the binding key. The directory citation is the "exact per-lane artifact filenames"
  ambiguity that FOLD-1 §5's webstorm ride already flagged ("residual: per-lane artifact
  filenames are approximate pending independent read — flagged in §3"). The §3 citation is
  therefore not a receipt; it is a pointer-to-a-folder.

**Corrected form (named-file citations, verbatim from disk):**
```
| Lane | Commit | Named artifact path (receipt) | Cert-receipt binding |
| A | `c58fea0e99` | studies/rfc-143379-rig/CYCLES/S2-LANE-A-20261109.md | cert receipt for C44-pilot PASS |
| B | `5f6647e540` | studies/rfc-143379-rig/CYCLES/S2-LANE-B-20261109.md | cert receipt for gate-scan |
| C | `c649708e51` | studies/rfc-143379-rig/CYCLES/S2-LANE-C-20261109.md | cert receipt for byte-keyed fields |
| D | `876cbd0eb7` | studies/rfc-143379-rig/CYCLES/S2-LANE-D-20261109.md | cert receipt for SOFT-pool |
| E | `dd1922088b` | studies/rfc-143379-rig/CYCLES/S2-LANE-E-20261109.md | cert receipt for fleet baseline |
```

---

## 3 — Defect #3: Lane-A's PASS over an unfilled receipt

### 3a — S2-LANE-A run-signature block is entirely placeholder while §3 asserts "PASS"

**Original text (S2-LANE-A-20261109.md, §1 run-signature):**
```
```text
build status: [compile/link result]
lint:        [lint result]
test:        [test verdict, browser engine]
acceptance:  [acceptance-pass result, against the plan's own params]
```
```

**Original text (S2-LANE-A-20261109.md, §2 receipts-arch schema-row):**
```
| executed-evidence | [receipt hash / tail of log] |
| run-receipt | [receipt-id + schema-row] |
```

**Original text (S2-LANE-A-20261109.md, §3 adoptability verdict):**
```
**PASS** — the mergeable pass is alignable with the plan's own acceptance-params,
executed-evidence is clean, and the receipts-arch schema-row records the receipt. No
blocking root-cited defect found.
```

**Finding (bytes say):**
- Every executed-evidence value is a **placeholder bracket** (`[compile/link result]`,
  `[lint result]`, `[test verdict, browser engine]`, `[acceptance-pass result...]`).
  There is no executed value — no compile/link status, no lint result, no test verdict, no
  acceptance-pass result. The §2 schema-row is also empty placeholders (`[receipt hash /
  tail of log]`, `[receipt-id + schema-row]`).
- §3 nonetheless asserts a definitive PASS over an executed-evidence receipt with **zero
  executed values**. A PASS asserted over a receipt whose executed-evidence block is
  entirely bracketed-placeholder is a receipt with no bearing values — the audit rule is
  explicit: "executed-evidence is clean" can only be read after the actual run values are
  present. As written, the PASS is standing on an unfilled receipt.
- Per the audit rule, the correction is **not** a retroactive fill-in. The executed values
  were never recorded in this artifact. The PASS must be struck and the line re-opened
  pending real executed-evidence.

**Corrected form:**
```
Lane-A verdict: **PASS struck / re-opened pending executed-evidence**.
- Remove: §3's definitive "PASS" assertion and the "executed-evidence is clean" clause
  that rests on placeholder brackets.
- Replace with: S2-LANE-A's C44-pilot step is EXECUTED-IN-NAME-ONLY; the executed-evidence
  block is empty (all values bracketed-placeholder). Re-open the adoptability verdict
  pending the record of real compile/link, lint, test, and acceptance-pass results from a
  run at the plan's actual acceptance-params. The verdict must not be re-asserted until
  those executed values are present in the artifact.
```

---

## 4 — Correction ledger (defect → bytes → correction)

| # | Defect (original) | Bytes (finding) | Correction |
|---|---|---|---|
| D1a | S3-SWAP §1: "fingerprint-integrity unconfirmed — surfaced by the byte-keyed G5–G7 leg (seat C's lane)" | `fingerprint` = 0 hits in all five S2-LANE-*.md | **Strike:** unsourced; remove attribution. |
| D1b | S3-SWAP §1: "1 needs-definition seed — surfaced by the gate-scan leg (seat B's lane)" | `needs-definition` = 0 hits in five S2-LANE; only in S3-SPLIT-D row 7 | **Re-source:** to Lane D's SOFT-pool row 7. |
| D1c | S3-SWAP §1: "fleet-baseline's phase-bound scaling — surfaced by the fleet-baseline leg (seat E's lane)" | fleet-scaling claimed only by S2-LANE-E | **Retained:** attribution correct. |
| D2 | FOLD-1 §3: five lanes cite `studies/rfc-143379-rig/CYCLES/` (directory) | directory ≠ named artifact path; no receipt named | **Correct to named files:** the five per-leg artifact paths, verbatim. |
| D3 | S2-LANE-A §3: "PASS ... executed-evidence is clean" over placeholder run-signature + empty schema-row | all executed values bracketed-placeholder; zero executed values | **Struck:** PASS → re-opened pending executed-evidence; no retroactive fill-in. |

---

## 5 — Re-sourced attributions (summary)

| Gap | Original attribution (S3-SWAP §1) | True carrier (byte-direct) | Corrected attribution |
|---|---|---|---|
| fingerprint-integrity unconfirmed | seat C's byte-keyed G5–G7 leg | **Unsourced** — no S2-LANE seat names "fingerprint" | **Strike:** attribution removed; gap stays unconfirmed pending seat-C re-run + witness line |
| 1 needs-definition seed | seat B's gate-scan leg | **Lane D's SOFT-pool row 7** (`S2-LANE-D-20261109.md` row 7; `S3-SPLIT-D-20261110.md` row 7 seed-status = needs-definition) | **Re-source to seat D** |
| fleet-baseline phase-bound scaling | seat E's fleet-baseline leg | seat E (only S2-LANE that records fleet-scaling claims) | **Retain** |

---

## 6 — Named-file citations (FOLD-1 §3 replacement)

Per the correction in §2, FOLD-1 §3 now cites the five named per-leg artifacts
(verbatim from disk), each keyed to its commit hash:

- A → `studies/rfc-143379-rig/CYCLES/S2-LANE-A-20261109.md` (`c58fea0e99`)
- B → `studies/rfc-143379-rig/CYCLES/S2-LANE-B-20261109.md` (`5f6647e540`)
- C → `studies/rfc-143379-rig/CYCLES/S2-LANE-C-20261109.md` (`c649708e51`)
- D → `studies/rfc-143379-rig/CYCLES/S2-LANE-D-20261109.md` (`876cbd0eb7`)
- E → `studies/rfc-143379-rig/CYCLES/S2-LANE-E-20261109.md` (`dd1922088b`)

The directory citation `studies/rfc-143379-rig/CYCLES/` is removed from §3.

---

## 7 — Lane-A verdict (final)

**PASS struck / re-opened pending executed-evidence.**

The executed-evidence block of S2-LANE-A (§1 run-signature and §2 schema-row) contains
**zero executed values** — every entry is bracketed-placeholder. §3's definitive PASS over
that receipt is removed. The line re-opens at the plan's actual acceptance-params; a new
executed-evidence block (compile/link, lint, test, acceptance-pass) must be recorded
before the adoptability verdict is re-asserted. No retroactive fill-in is permitted.
