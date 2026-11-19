# NEGENTROPY-SWEEP-20261119-1812 — the recurring sweep's fire

**Seat:** the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · **Branch:** `study/rfc-143379-rig-20261105` (fork only) · **Fire time:** 2026-11-19 18:12 · **The gate (verbatim):** "the gate: nothing public without the user's word."

**The register (binding):** receipts, never claims. **[1st]** = re-read by this lane this pass (committed bytes via git-tree/HEAD, study listings, branch logs); **[2nd]** = carried from a study doc, not re-derived here. ABSENT + named, never invented. Claims tagged IN-LANE / BORROWED / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)

| # | standing item | state | receipt |
|---|---|---|---|
| W2 | W2-isolation settle-condition (harness-answer vs compressor-preamble) | **NOT-RUN — 3rd fire** | the eval-harness runtime config is **ABSENT + named** (not located before the read-gate closed); the W2-empty-answer set's kept-rate is 0/6 = 0.00 (`NEGENTROPY-SWEEP-B-KTERM-20261106.md` §4) [1st]; 1611 §1 [2nd] |
| K | k-term two-tier re-measure | **CHECKED** (carried) | the flat 0.42/0.29/0.26/0.26 is an arithmetic-mean artifact of the 24/36/22/48 denominators; the two-tier split is rowed: **0.00** (empty-answer) vs **0.26–0.42** (answer-bearing) (KTERM §4) [1st] |
| B | budget consolidation re-verify | **CHECKED [1st] this fire** | `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(a)/(b): 3.0 − baseline median → decision-core **3.00** > clock/exec **2.83** > next-action **2.33** > scope **2.00**; the arithmetic and the ordering reproduce |

**The reconciliation row (1611 next-move #1, landed):** the budget's four numbers are **WEIGHTS** (3.0 − loss-likelihood median); the KTERM/ADJUDICATION numbers are probe-median **SCORES** — different grains, so the ordering clash dissolves. **But a new discrepancy surfaces [1st]:** the ADJUDICATION's carried overalls (2.61 / 2.75 / 3.08 / 2.13) do **not** match the KTERM's [1st] re-derivation (decision-core **3.08** / continuation **2.61** / scope-boundary **2.13** / exact-anchor **—**) in value or order. The ADJUDICATION's row is [2nd] and is superseded. Receipt: `ADJUDICATION-NEGENTROPY-20261106.md` §k-term seam [1st] vs KTERM §2 [1st].

## 2. THE SEAM-SCAN

| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline | unchanged; the sweep's read-burn is its own ≤6,000-char writes + one-tool-call-per-round (a multi-call was trimmed this fire) | `NEGENTROPY-ARM-EXECUTE-20261119.md` §4 [2nd]; IN-LANE |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | carried; the sweep's terminal is git-only, not re-run this fire | arm-execute §4 [2nd] — scribe `get_memory` byte-identical to the scribe-cell file; served copy byte-identical |
| token watcher's single-source line | **STALE — survived a fire**: the arm's §1 token line names **STEER-3**; the branch's live steer is **STEER-11** (banked 9a92aa944e; no STEER-12). Per §1's own rule (two surfaces disagree = HOLD) this is a HOLD trigger; the 1611-ordered UPDATED append is still absent | arm-execute §1 [1st]; `NEMO-STEER-CHANNEL-20261116.md` STEER-11 [1st]; `MISSION-MAP-20261118.md` row 88 [1st] |
| machine-layer wire-checks | carried, dated 2026-11-19: scribe tunnel OK, runners OK, Harbor OK, local-LM 503 (proxy-side) | arm-execute §4 [2nd] |
| dispositions | carried, unchanged: T1/T2/T3/T4/C2/C4 AUTO-CONTINUE; C3/C5 HOLD-SAFE; S1/S2/S3 NEEDS-THE-CHAIR (auto-paths named; packets pre-written, unroweled) | arm-execute §5 [2nd] |

## 3. THE ENTROPY CLASSES

- **Dead surface — the W2 settle-condition.** The eval-harness runtime config is ABSENT + named; the read-gate closed (~round 12) with it unfound. **Countermove:** the head surfaces the config path (or names it out-of-tree); until then W2 stays a wall, not an item.
- **Loose thread (the headline) — the token-line staleness.** STEER-3 → STEER-11 survived the 1611 fire and this one; the "next fire" gate came and went. **Countermove:** the one-line UPDATED append; gate next fire; seat the head.
- **Loose thread — the superseded carried numbers.** The ADJUDICATION rows overalls its own successor (KTERM) re-derived differently. **Countermove:** re-extract the per-probe overalls from the 16 ladder JSONs; row one canonical table; stamp the ADJUDICATION's row SUPERSEDED.
- **Friction point — the two taxonomies.** The budget's four classes and the KTERM's four share names but not definitions (budget "continuation" lumps next-action+scope; KTERM "exact-anchor" has no budget counterpart). **Countermove:** a one-line mapping note in BUDGET §(a).
- **UNSPOKEN — the settle-condition may be permanently out-of-tree.** Three fires (1410/1611/1812) have carried "not-run"; the unspoken reading is that the harness config lives outside the git tree, making W2 a boundary rather than an open item. **Countermove:** name the boundary explicitly instead of re-carrying "not-run" indefinitely.

## 4. THE ORDERED NEXT-MOVES

1. **The token-line UPDATED append** (STEER-3 → STEER-11). Gate: next fire. Seat: the head.
2. **The canonical overalls table** (re-extract from the 16 ladder JSONs; stamp the ADJUDICATION's row SUPERSEDED). Gate: next fire. Seat: the head / lane-B.
3. **The taxonomy note** (budget ↔ KTERM class mapping, one line, BUDGET §(a)). Gate: next fire. Seat: the head.
4. **The W2 settle-condition** (surface the eval-harness runtime config, or name it out-of-tree). Gate: next fire. Seat: the head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

| # | step | evidence |
|---|---|---|
| 1 | artifact written | this file at the artifact path |
| 2 | register tagged | [1st]/[2nd]/IN-LANE/BORROWED throughout |
| 3 | window-check rowed | §1 table, three rows |
| 4 | seam-scan rowed | §2 table, five rows |
| 5 | entropy classes named with countermoves | §3, five findings |
| 6 | next-moves ordered | §4, four moves |
| 7 | loop-state line | §6 |
| 8 | commit + push | the branch's study tip |

## 6. THE LOOP-STATE LINE

`CONTINUE + the token-line UPDATED append (STEER-3 → STEER-11) — gate next fire, seat the head; then the canonical overalls table.` Receipt: arm-execute §1 [1st]; `NEMO-STEER-CHANNEL-20261116.md` STEER-11 [1st]; the 1611 sweep §1/§4 [2nd].