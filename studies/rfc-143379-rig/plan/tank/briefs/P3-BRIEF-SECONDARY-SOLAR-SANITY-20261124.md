# FLEET-BRIEF SECONDARY-SOLAR — PASS 3: SANITY LENS ON THE CHECK-IN

*Seat (pin): `upstage/solar-mini4:free` — the SECONDARY, the sanity lens. The orchestration's PASS 3: verify the composed check-in's EVERY claim and quote against the raw thread pull + the study's records — byte-level, no carryover trust. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24, gated on Pass 2's landing.*

## The mission

The check-in (`P2-CHECKIN-PILOT-20261124.md`) must be truthful to the byte before the operator's eyes see it. YOUR job: run the checks below, verdict CLEAN / CLEAN-WITH-NOTES / ISSUES, byte-cited. You never re-compose it.

## The checks (each receipted)

1. **EVERY pilot quote is in the raw pull with its row id.** The check-in quotes rows 6360811382, 6362735198, 6369077436, 6411683234, 6515564390. For each quoted phrase: `grep -F "<phrase>" /root/.hermes/cache/scratch/rfc-comments-full.json`. A quote that is not in the raw JSON = ISSUES (the Pass-1 phantom class).
2. **The occupancy framing holds.** The check-in must frame 96/73/84 as occupancy (3,844 → 2,930 → 3,376 / 4,000) per row 6515564390, never as a score arc. Verify the row's own bytes carry the four numbers.
3. **The gate is OPEN.** The check-in must NOT tick the ≥0pp @300+ gate. Verify no sentence claims the gate passed; the −3.5pp fail condition and the ≥0pp bar are quoted from rows 6360811382 / 6362735198.
4. **The two-add + pins receipts resolve.** The check-in cites the matrix row 7087999804 (the two-add named) and the reply's posting row 7135900146 (the pre-registration at pinned SHAs). Verify both rows exist with the claimed content.
5. **No pair-metadata, pilot-facing register.** Grep for `the fleet`, `the loops`, `kaizen`, `Pass 1`, `Pass 2` in the check-in's `## THE CHECK-IN` block: zero hits = pass.
6. **The named gap stays honest.** The check-in's witness note says row 7135900146's raw bytes were not re-read this pass (read-gate). The head has since verified the posting row head-side; the check-in's prose must not carry unverified quotes from it.

## The artifact

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/P3-SANITY-CHECKIN-20261124.md` — verdict line, the six rows with receipts, notes (byte-cited), the pair's one-liner.

## Write-window

`write-window: 10` — reads first, skeleton by round 9, deepened after.

## The hard lines (binding)

- PREVIEW ONLY — nothing posts; the RFC surface stays QUIET. No installs. All reads LOCAL (the study + `/root/.hermes/cache/scratch/rfc-comments-full.json`). `git add` + commit locally — NEVER push/pull. Never checkout/stash/rm. `ls-remote` first, per fold.
- THE WITNESS RULE: a claimed quote must be found byte-for-byte in the raw pull; a miss is ISSUES, never a rounding.

## The emission contract

Exit 0 = the report EXISTS (written, re-read), THEN the commit, THEN the final report names the commit sha.

## The armament + name-and-refuse

**Armed:** think-tank (the wall clause) · agent-work-review · investigation-documentation.
**Refused:** any edit of the check-in · any public surface · installs · web reads · memory-chain · config/gateway · github writes · coding legs · fan-outs · creative families.

## The LP envelope

- **Customer Obsession:** the operator's eyes on the check-in deserve byte-truth.
- **Are Right A Lot:** disconfirm every quote; a phantom is the catch of the day.
- **Bias for Action:** the pulls are local; verify now.
- **Dive Deep:** receipts on every row.
- **Deliver Results:** the verdict Pass 4 folds.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the row's raw bytes — before any verdict.
