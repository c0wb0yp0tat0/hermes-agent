# FLEET-BRIEF NEMO — POST THE INTERIM NOTE (carefully)

*Seat (pin): `mistralai/mistral-nemo` — the PAID seat. The operator's word (2026-11-24): "Have Nemo post it carefully then have a successor make sure the formatting is right." The interim note to kvnloo (committed `4f3784b322f`, `RW-INTERIM-NOTE-20261124.md`) posts to the RFC #143379 thread NOW — the operator's explicit authorization for this public write. The only gate that exists: a public write outside a secret gist or PR #1 — and this one is authorized. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission

1. **Read the committed note**: `studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-20261124.md` — the exact bytes (7 lines: the @kvnloo open, the onto-something line, the within-the-hour line, the read-as-approximately line, the footer). **Post EXACTLY those bytes** — no envelope, no staging notes, no edits, no additions. The body IS the comment.
2. **Post it via gh api** (the harness permits `gh api` — a read gate that also serves writes here): 
   `gh api repos/NousResearch/hermes-agent/issues/143379/comments -f body="<the exact note body>"`
   The operator's word authorizes THIS posting and nothing else. No other surface, no PR #1, no other comment.
3. **Verify the posting**: fetch the comment back by its id and confirm its body is byte-identical to the committed note. A mismatch = the posting failed and must be corrected or the comment deleted — never left wrong.

## Write-window

`write-window: 8` — the post's verification is the artifact's worth; a written receipt by round 7, deepened after. NO stub markers.

## The required artifact — the posting receipt

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-POSTED-20261124.md`

1. The comment id + URL of the post.
2. The verification receipt: the fetched body vs the committed note — byte-identical confirmed (or the correction/revert logged).
3. The exact timestamp.
4. One line: nothing else was posted.

## The hard lines (binding)

- POST ONLY the interim note to the RFC #143379 issue. No PR #1, no gist change, no other comment, no deletion of anything else. One write, the authorized one.
- No installs. All reads LOCAL. `git add` + commit locally — NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: the posted bytes == the committed bytes, verified by fetching; a guessed or edited byte is a fail.

## The emission contract

Exit 0 = the receipt EXISTS on disk, re-read, committed; the report names the sha + the comment id. No tool-call syntax in the final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the wall clause) · the exactness discipline (byte-identical posting is the whole job).
**Refused:** any other write · web reads · installs · memory-chain · config/gateway · coding legs · fan-outs · creative families.

## The LP envelope

- **Customer Obsession:** kvnloo receives exactly what the pair reviewed — nothing more, nothing less.
- **Ownership:** the seam is yours until the posting receipt is on disk, re-read, committed.
- **Are Right A Lot:** the fetch-back is the proof; never trust the posting call's own success alone.
- **Bias for Action:** the note is committed; post now, verify now.
- **Dive Deep:** byte-identical verification.
- **Deliver Results:** the receipt the pair can hold.

**THE WALL CLAUSE:** a non-reproduction (a posting that won't verify byte-identical) is a QUESTION with a constructed minimal move — the comment's fetch, the committed note's bytes — before any verdict. A real wall lands with its receipts, named as a finding.
