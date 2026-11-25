# FLEET-BRIEF HY — LAUNCH THE FULL REPLY (what we shaped, properly)

*Seat (pin): `tencent/hy4-flash:free` — the composer-turned-launcher. The operator's word (2026-11-24): "it would be more value add if you launched what we shaped properly so ask hy to do that." The full reply (`RW-FULL-REPLY-20261124.md`, committed 67873df5749) is the shaped artifact; YOUR job is the LAUNCH — post it to the RFC #143379 thread, byte-exact, verified. This public write is the operator's explicit word. Branch: `study/rfc-143379-rig-20261105`. Fire: now.*

## The mission

1. Read `studies/rfc-143379-rig/plan/tank/RW-FULL-REPLY-20261124.md` — the exact bytes (the @kvnloo open through the Nemo-named footer).
2. POST it as a comment on RFC #143379: `gh api repos/NousResearch/hermes-agent/issues/143379/comments -f body="$(cat studies/rfc-143379-rig/plan/tank/RW-FULL-REPLY-20261124.md)"` — via the `terminal` tool with exactly that command shape (raw bytes through `$(cat …)`).
3. Fetch the comment back by its id, verify body == committed reply byte-for-byte (real characters, real line breaks — no `\uXXXX` escapes, no `\n` as text). The false-receipt class of the interim arc must not repeat: an escaped-fetch comparison is a failure.

## The artifact

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-FULL-REPLY-LAUNCHED-20261124.md` — the comment id + URL, the byte-identical verification receipt, the timestamp, one line: nothing else was posted.

## Write-window

`write-window: 8` — post first, verify, receipt by round 7.

## Hard lines

- POST ONLY the full reply to RFC #143379. No other surface, no PR #1 comment, no gist change, no other write.
- No installs. All reads LOCAL. `git add` + commit locally, NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: the fetched bytes decide — real chars, real breaks, byte-identical to the committed reply.

## Emission

Exit 0 = the receipt EXISTS on disk, re-read, committed; the report names the sha + the comment id. No tool-call syntax in final words.
