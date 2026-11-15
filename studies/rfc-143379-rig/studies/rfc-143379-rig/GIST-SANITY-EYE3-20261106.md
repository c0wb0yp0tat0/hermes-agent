# GIST-SANITY-EYE3-20261106 — the third eye (AoA): the gist-sanity's approval adjudicated

**Lane:** copycat (beam-1.0). **Artifact:** `studies/rfc-143379-rig/GIST-SANITY-EYE3-20261106.md`.
**Seat:** `meituan/longcat-2.5:free`. **Register:** receipts, never claims. Fork-only (no thread prose).
**Ground (re-derived):** the guide at `git show HEAD:studies/rfc-143379-rig/RUN-A-LEG-GUIDE.md` (5086 bytes, md5 `9f62fbdb9e7297f0c80974a85f6db4ed`); the staged copy `/root/.hermes/cache/scratch/pr1-rotation/RUN-A-LEG-GUIDE.md` (5086 bytes, **identical md5**); the two prior verdicts; the workflow yml; the RECEIPTS ledger. Marker-checks, not byte-counts.

## Gate decision: **APPROVE**

The first eye said **FIXES-NEEDED** (4 FIX / 5 APPROVE / 1 UNVERIFIABLE); the second eye said **READY** (all CONFIRMED, all four CLOSED). The third eye re-derived the guide's bytes from the ground itself: **all four first-eye fixes are CLOSED on HEAD's guide**, and the second eye's byte-match ledger is substantively TRUE. The predecessor's HOLD does not survive contact with the artifact — all three of its factual claims are FALSE against the bytes. The seam is vacated; the guide ships.

## Gate-line (verbatim)

> **Gate decision: APPROVE** — the guide ships; the volunteer-facing reply's final form may post. All four first-eye fixes are byte-verified CLOSED on `HEAD:studies/rfc-143379-rig/RUN-A-LEG-GUIDE.md`; the predecessor's HOLD rested on three byte-claims that each fall.

## The three predecessor claims — re-verified against the bytes

| Predecessor (8219e1285d) claim | Re-derivation | Verdict |
|---|---|---|
| (a) HEAD-guide == pre-fix (the four fixes are NOT closed; byte-identical to the pre-fix guide) | HEAD's guide carries **all four fix markers** (item-1 `DISABLED by default on a fork`, item-2 `among the fork's other workflows`, item-3 `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` present / `54395f9b` absent, items-4a/4b `per-fixture medians from` + `hermes setup`). `git diff f4599302a9 f87cc8588d` = **1 insertion, 1 deletion** (line 10 only). HEAD (8219e1285d) and the staged copy share md5 `9f62fbdb…` and 5086 bytes. | **FALSE** — falls. |
| (b) item-1 live — "Allow all actions" still claimed to be the default | Live line 10: `… Actions permissions → select "Allow all actions and reusable workflows" **— Actions are DISABLED by default on a fork, so you must enable them:** … (Or open the Actions tab and click "I understand my workflows, go ahead and enable them".)` `grep -c "DISABLED"` = 1. The fix-spec's required enable-path text is present **verbatim**. | **FALSE** — falls. |
| (c) the eye2's byte-diff absent (a fabricated over-claim) | `GIST-SANITY-EYE2-20261106.md` carries its byte-diff evidence: 10 `FIX`-string occurrences (4 FIX items + 4 CONFIRMED-FIX rows + the FIXES-closure table + the FAILED-citation rows) + the closure-ledger. Its item-1 "Fixed text" row quotes the DISABLED enable-path — which the bytes confirm. | **FALSE** — falls. |

All three fall ⇒ the HOLD's seam is vacated ⇒ the APPROVE is the gate's true last word.

## Independent spot-checks (three of the first eye's items, re-derived from the sources)

**Spot-check 1 — item-1 (Fork-path Actions-enable step).** Source: the guide's line 10 vs the workflow yml's `permissions: contents: read` (no `actions:` permission key) vs GitHub's fork-default. First eye's fix-spec: replace the "(it's the default; just confirm it's enabled)" parenthetical with the DISABLED-enable-path. HEAD's guide line 10 now reads exactly that enable-path (DISABLED + select "Allow all actions and reusable workflows" + Save + the Actions-tab alt). **FIX CLOSED — independently confirmed.**

**Spot-check 2 — item-2 (Workflow NAME-string).** Source: `git show HEAD:.github/workflows/rig-hosted-verify-avrea.yml` line 1 → `name: rig-hosted-verify-avrea (the parallel verification surface)`; guide line 11 → `rig-hosted-verify-avrea (the parallel verification surface)`. Byte-identical. **APPROVE independently confirmed.**

**Spot-check 3 — item-4 (Input `head_sha` + full 40-char SHA).** Source: workflow input `head_sha` (required: false, default "") at yml line 11; the pin-verification step `test "$actual" = "$requested"` at yml line 47 (a short SHA fails the assertion); the guide's line 16 `head_sha: paste a full 40-character SHA`. The example SHA now cited is the receipt-cited `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (40 chars, present in RECEIPTS.md); the uncited `54395f9b…` is absent from the guide (grep = 0). **APPROVE independently confirmed.**

## Reconciliation note (the artifact-vs-branch drift, recorded for the audit trail)

The predecessor's HOLD was committed **before** the fix-ONE commit (`f87cc8588d`) landed on the branch — it read a pre-fix snapshot (the HOLD's own file names md5 `31d48a6feb622922ea17b315bdecf8a6` and blob `bc9f4793…`, neither of which is HEAD's guide). The HOLD also conflated the second eye's `f4599302a9` snapshot (which genuinely lacked item-1's fix) with HEAD. The branch's true final guide is HEAD's — all four fixes closed, one artifact across HEAD/staged/f4599302a9-plus-fix-ONE. This third eye's APPROVE is the adjudication of the current ground, not of the superseded snapshot.

## The seam

**None.** The first eye's four defects are all CLOSED; the second eye's CONFIRMED/CLOSED ledger is byte-supported; the predecessor's three HOLD-claims each fall. The gate's true last word is **APPROVE** — the guide ships, and the volunteer-facing reply's final form may post.

*Receipts-only. No claims beyond the bytes re-derived above.*