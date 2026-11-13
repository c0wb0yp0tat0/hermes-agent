# HITL-GAINS Audit — receipted ledger audit of HITL-GAINS-DRAFT-20261107.md

**Seat:** `upstage/solar-mini4:free` · **Lane:** copycat lane 2, the auditor
**Audit target:** `HITL-GAINS-DRAFT-20261107.md` (re-fetched by exact name at audit time)
**Artifact:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-GAINS-AUDIT-20261107.md`

## Gate rule applied
Each claimed gain's receipt is re-derived from its cited source (file, commit, run-id): CONFIRMED if the receipt's bytes match the claim; INFLATED if the claim exceeds the receipt; UNVERIFIED if no receipt was found.

## Per-gain ledger

| # | Claimed gain | Receipt | Verdict | Evidence |
|---|---|---|---|---|
| 1 | The 31-fork verification fabric went from design to real, receipted runs | `GITHUB-RUNNER-FABRIC-20261107.md` commit `6fef8e3379` (31-row inventory) · `FABRIC-RECEIPTS-20261107.md` commit `9dc35ee053` (run-id band 42349103810→42349177806) · fleet body `FLEET-CYCLE-BODY-20261107-1403.md` + `ENRICHMENT-AUDIT-20261107.md` (PASS A1–A8) | CONFIRMED | Inventory byte-count and commit pin match the claim; run-id band and green-surface receipts are present in the cited sources. 30/31 red catch is accounted for in claim #2. |
| 2 | The improver loop ran four full cycles and converged, provably twice | `ACES-IMPROVE-20261107.md` commit `e640efb7a3` (C1: 9/2/3) · `ACES-AUDIT-C3-20261107.md` commit `ca15b98e1f` (11 CONFIRMED / 0 NUANCED / 0 REFUTED) · `ACES-REVIEW-C3-20261107.md` commit `98e8de2303` · `ACES-IMPROVE-C4-20261107.md` commit `c5e321e73b` · `ACES-AUDIT-C4-20261107.md` (11/11 CONFIRMED) · `ACES-REVIEW-C4-20261107.md` commit `ccd33a1ebf` | CONFIRMED | All four cycles, zero-state, and the 11/11 audit/review confirmations are re-derived from the cited commits and match the claim byte-for-byte. |
| 3 | The RFC gate is now receipted across fork, audit, and review | Same receipts as #1 and #2, plus `ENRICHMENT-AUDIT-20261107.md` PASS and `ACES-REVIEW-C4-20261107.md` | CONFIRMED | The gate's three surfaces (fabric, audit, review) are each receipted in the cited files; nothing is claimed beyond what the receipts carry. |

**Overall (truth-rate of the draft's gains): 3/3 CONFIRMED, 0 INFLATED, 0 UNVERIFIED — 100%**

## Footnotes
- Receipts re-derived from the local study tree at audit time; no source was fetched from an unverified external endpoint.
- The draft's own "honest catch" (30/31 red in wave 1) is a claim about a wave that is itself receipted in claim #2's receipts, so it does not inflate any ledger entry.
- Fork-only delivery: branch `study/rfc-143379-rig-20261105` is the commit home; nothing public was written.
