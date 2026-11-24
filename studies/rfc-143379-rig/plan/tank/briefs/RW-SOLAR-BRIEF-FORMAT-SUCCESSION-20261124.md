# FLEET-BRIEF SUCCESSOR-SOLAR — VERIFY THE FORMATTING OF THE POSTED NOTE

*Seat (pin): `upstage/solar-mini4:free` — the SUCCESSOR follows Nemo's posting and audits the live comment's formatting (the operator: "then have a successor make sure the formatting is right (like you usually do)"). Fire: AFTER Nemo's posting receipt is on the branch (gated — you audit the posted comment, never air). Branch: `study/rfc-143379-rig-20261105`.*

## The mission

The interim note has been posted to RFC #143379 by Nemo (row id in `RW-INTERIM-NOTE-POSTED-20261124.md`). YOUR job: verify the LIVE comment is GitHub-standard formatting — exactly the pass the head has run on every posted comment today — and if a formatting defect exists, silently PATCH the same comment (the `gh api --method PATCH .../issues/comments/<id>` route; same comment, never a new one).

## The checks (each with a command + receipt)

1. **Fetch the live comment** (`gh api repos/NousResearch/hermes-agent/issues/comments/<id>` — the id from Nemo's receipt) and compare its body to the committed note (`RW-INTERIM-NOTE-20261124.md`): byte-identical is the base condition (content must NOT have drifted in the post).
2. **Formatting audit** on the live body:
   - Mentions render: `@kvnloo` un-backticked (pings).
   - One em-dash per sentence max (audit the note's lines: line 1 (the open) has none, line 3 has one, line 5 has none — count and confirm ≤1 each).
   - The footer is the LAST line, italic (`*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*`), nothing after it.
   - No stray markdown (stray `**`, broken emphasis, accidental code spans): scan the body for unbalanced markers.
   - No raw URLs if none were intended (the note has none — confirm zero).
3. **If any defect:** PATCH the same comment with the corrected body (the committed note's bytes whatever the defect), fetch back, byte-verify. If clean: state CLEAN.
4. **The record:** the audit result, the receipts, the final byte-identical verification.

## The required artifact

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-FORMAT-20261124.md`

1. The verdict: CLEAN / PATCHED (with what).
2. The checks' rows with receipts.
3. The final live-vs-committed byte-identical confirmation (or the defect + its fix).
4. The pair's one-liner.

## Write-window

`write-window: 8` — fetch + greps first, the record by round 7, deepened after. NO stub markers.

## The hard lines (binding)

- PATCH ONLY the posted comment (same id, no new comment, no other write). Never touch anything else on the RFC surface.
- No installs. All reads LOCAL + the gh api reads of the comment. `git add` + commit locally — NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: byte-identical verification is the floor; a formatting defect unpatched is a fail.

## The emission contract

Exit 0 = the record EXISTS on disk, re-read, committed; the report names the sha. No tool-call syntax in the final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the wall clause) · gist-formatting-match (the register standard) · the formatting pass the head has run all day (the succession).
**Refused:** any other write · web reads · installs · memory-chain · config/gateway · coding legs · fan-outs · creative families.

## The LP envelope

- **Customer Obsession:** the pair's reviewed bytes appear on the thread, rendered right.
- **Ownership:** the seam is yours until the record is on disk, re-read, committed.
- **Are Right A Lot:** the fetch-back decides; a claimed clean with a marker imbalance is a note.
- **Bias for Action:** fetch now, audit now.
- **Dive Deep:** countable receipts.
- **Deliver Results:** the succession pass, verdict-ridden.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the live comment's bytes — before any verdict.
