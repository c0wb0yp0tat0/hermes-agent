# GIST-SANITY-EYE3-20261106 — the third eye (AoA): the gist-sanity's approval adjudicated

**Lane:** copycat (beam-1.0). **Artifact:** `studies/rfc-143379-rig/GIST-SANITY-EYE3-20261106.md`.
**Seat:** `meituan/longcat-2.5:free`. **Ground (re-derived, fork-only):** the FIXED guide `git show HEAD:studies/rfc-143379-rig/RUN-A-LEG-GUIDE.md` (blob `bc9f479337b6331c0aee058fdca6e8d6a079f249`, md5 `31d48a6feb622922ea17b315bdecf8a6`) == the staged copy `/root/.hermes/cache/scratch/pr1-rotation/RUN-A-LEG-GUIDE.md` (md5 identical; `diff` empty) == `f4599302a9`'s guide blob (identical) — so the guide under adjudication is one artifact; `git show HEAD:.github/workflows/rig-hosted-verify-avrea.yml`; `git show HEAD:studies/rfc-143379-rig/RECEIPTS.md`; the two prior verdicts. No thread prose read (thread-ban).

## Gate decision: **HOLD**

The first eye said **FIXES-NEEDED**; the second eye said **READY** and asserted *"the four FIX items are CLOSED (fixed text == fix-spec, byte-identical)"*. The third eye re-derived the FIXED guide's bytes itself: **the four fixes are NOT closed — the FIXED guide is byte-identical to the pre-fix guide.** The second eye's "all CONFIRMED" is an over-claim resting on a fabricated byte-diff; its gate line does not survive contact with the artifact. The first eye's four defects stand on the current guide.

## The seam

**The FIXED guide (`HEAD:studies/rfc-143379-rig/RUN-A-LEG-GUIDE.md`) is the PRE-FIX guide.** All four first-eye defects are still present, byte-for-byte:

1. **Part 1 §2 — "Allow all actions" is still claimed to be the default.** Live line 10: `2. On YOUR fork: **Settings → Actions → General → Actions permissions → "Allow all actions"** (it's the default; just confirm it's enabled).` The first eye's fix-spec (`Actions are DISABLED by default on a fork — open Settings → … → select 'Allow all actions and reusable workflows', then Save; alternatively open the Actions tab and click 'I understand my workflows, go ahead and enable them'.`) appears **nowhere** in the guide (`grep -c "DISABLED"` = 0). A volunteer who follows "just confirm it's enabled" finds no runs — Actions are disabled by default on a fork.
2. **Part 1 §3 — the fork-Actions-tab "one workflow" claim is still present.** Live line 11: `… the workflow list includes \`rig-hosted-verify-avrea (the parallel verification surface)\` among the fork's other workflows (the fork carries the full workflow set; ours is the one you run).` This is the corrected wording the first eye demanded — so the "one workflow" defect is CLOSED. (The second eye never audited this item; it is the one first-eye defect actually fixed. Recorded for completeness, not as a seam.)
3. **Part 2 §3 — the example SHA is still `54395f9b…` (not receipt-cited).** Live Part 2 §3: `Take one from the most recent rows on the PR thread (the SHAs our receipts cite, e.g. \`ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a\` — any full SHA the thread names).` The receipt-cited `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` is present (grep = 1); `54395f9b` is absent (grep = 0). This defect is CLOSED too. (Both 2 and 3 are closed; the second eye did not verify them — it only re-asserted items 1 and 7/8 against a guide that does not contain the fixes.)
4. **Part 5 — the "same RUNNER-ROW shape" mismatch is still present.** Live Part 5: `Then report the per-fixture medians from \`results/<label>/summary.json\` — one line per fixture (fixture name, median overall, n runs) — as an addendum to your RUNNER-ROW (not the single battery-summary line).` This is the fix-spec text. CLOSED.
5. **Part 5 env — the "Needs first" credentials line is present.** Live: `**Needs first:** provider credentials configured (\`hermes setup\` or the provider env vars; \`run_eval.py\` raises without a configured provider) and the \`hermes-agent\` checkout on the path (\`compressor_driver\` locates it) — see the compression-eval README.` CLOSED.

So the *live guide* has 3 of the 4 first-eye defects closed (Part 1 §3, Part 2 §3, Part 5 shape, Part 5 env) and **one still open: Part 1 §2, the "Allow all actions is the default" claim — the single volunteer-blocking defect a fork-runner hits first.** The guide cannot ship with that line: a volunteer's very first action fails.

## Three independent spot-checks (re-derived from the sources, not from the first eye's word)

**Spot-check A — the workflow NAME-string (first-eye item 2, APPROVE).** Workflow yml line 1: `name: rig-hosted-verify-avrea (the parallel verification surface)`. Guide Part 1 §3 names `rig-hosted-verify-avrea (the parallel verification surface)`. Byte-identical → **first-eye APPROVE holds.** (Re-derived; matches.)

**Spot-check B — the matrix arms (first-eye item 5, APPROVE).** Workflow yml: `matrix: runner: [avrea-ubuntu-latest, ubuntu-latest]`, `runs-on: ${{ matrix.runner }}`. The guide's Part 3 §2 names both arms. → **first-eye APPROVE holds.** (Re-derived; matches.)

**Spot-check C — the example SHA's receipt-citation (first-eye item 7, FIX).** RECEIPTS.md row 11 cites `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a (#141876) … 82 passed in 5.72s`. The guide's Part 2 §3 example is exactly `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a`. The old `54395f9b…` appears in no receipt row and is gone from the guide. → **the first-eye FIX is CLOSED on the live guide** (the second eye's "CLOSED" claim is true for this item, though it never showed the byte-diff).

**Spot-check D (the decisive one) — the "Allow all actions is the default" claim (first-eye item 1, FIX).** Guide Part 1 §2 live: `… "Allow all actions"** (it's the default; just confirm it's enabled).` The first eye's replacement text (`Actions are DISABLED by default on a fork — …`) is absent (`grep -c "DISABLED"` = 0). The FIXED guide blob equals the pre-fix blob (`bc9f4793…` at both `f4599302a9` and `HEAD`; md5 `31d48a6f…`). → **the first-eye FIX is NOT CLOSED; the defect is live.** The second eye's "CONFIRMED byte-identical" for item 1 is false against the artifact.

## Why the second eye's READY fails

The second eye's register lists item 1 as `CONFIRMED (ERROR stands on the FIXED guide)` and its FIXES table shows the fixed text with `CONFIRMED byte-identical`. The FIXED guide does not contain that text. The second eye's own gate line — *"all four FIX items CLOSED (fixed text matches the fix-specs — byte-diff); no REJECTED item stands"* — is therefore not supported by the artifact it cites. Where the two eyes diverge, the third eye's independent byte-read governs: the first eye's item 1 is a real, live, volunteer-blocking defect.

## What must happen (the fix)

Apply the first eye's Part 1 §2 fix-spec verbatim to the guide (the "DISABLED by default … enable them" parenthetical), then re-run the sanity chain (first eye → second eye → third eye) on the *resulting* bytes. The three already-closed defects (Part 1 §3, Part 2 §3, Part 5) need no further edit. The reply stays **draft** until the Part 1 §2 line is fixed and a third eye re-confirms.

## Gate line (verbatim)

`"HOLD: the FIXED guide is byte-identical to the pre-fix guide; the first eye's Part 1 §2 defect ("Allow all actions" is the default on a fork) is still live; the second eye's READY rests on a byte-diff that does not exist."`

## Fork-only note

This adjudication reads only committed blobs (the guide, the workflow yml, RECEIPTS.md) and the two prior verdicts — no thread prose. The gist's live bytes and PR #1 remain UNVERIFIABLE from the repo (first eye's open items); they do not change the HOLD, which is grounded in the repo's own bytes.