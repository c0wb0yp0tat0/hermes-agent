# FLEET-BRIEF NEMO — THE FORMAT SUCCESSION (audit + patch the posted interim note)

*Seat (pin): `mistralai/mistral-nemo` — the SUCCESSOR (the operator: "Nemo does it" — the successor is Nemo itself, not solar). Fire: 2026-11-24, after the interim note's posting is on the record. Branch: `study/rfc-143379-rig-20261105`.*

## The mission

The interim note posts on the thread — but the posting lane's verification was FALSE: the live body contains literal JSON escape sequences (`\u2014` and `\n` as text) instead of real em-dashes and line breaks. The pair will not let a broken-rendering comment stand. YOUR job — the successor's: audit the live comment's formatting, PATCH the same comment (id 7147011435) with the CORRECTED body — the committed note's exact bytes, real newlines, real characters — then verify the fetch-back is byte-identical to the committed note.

## THE EXACT PATCH COMMAND (the first succession fire's wall: it confirmed the defect but could not construct the patch — this fire carries the command verbatim)

The comment id is **7147011435**. Its body currently contains literal escape sequences (`\u2014`, `\n` as visible text) — the posting lane sent the JSON-escaped spelling instead of the raw text. The correction is a single `gh api` PATCH that sends the RAW file bytes as the body field. Use the shell's command substitution so gh receives the literal file content, not its escaped spelling:

```bash
gh api --method PATCH repos/NousResearch/hermes-agent/issues/comments/7147011435 -f body="$(cat /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-20261124.md)"
```

This is the SAME method the posting lane used successfully for the POST; the only change is the file substituted is the committed note (whose footer must carry Nemo's name — see check 2; if the committed note's footer still reads `*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*` without Nemo, amend it BEFORE the patch by writing the corrected note with the Nemo-named footer, then patch with that file).

Verify with a fetch: `gh api repos/NousResearch/hermes-agent/issues/comments/7147011435 --jq '.body'` — the returned body must contain real `—` characters and real line breaks (NOT the literal strings `\u2014` / `\n`). Compare it against the file's bytes as READ BY PYTHON or by `jq -r .body` — an escaped-fetch comparison (escaped against escaped) is the exact false-receipt class that shipped once already; it must not ship again.

## The checks (each with a command + receipt)

1. **Fetch the live comment**: `gh api repos/NousResearch/hermes-agent/issues/comments/7147011435 --jq '.body'` — confirm the escaped-sequence defect (contains literal `\u2014` / `\n` text instead of rendered characters).
2. **The correction source**: `studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-20261124.md` — the committed note's EXACT bytes (7 lines: the @kvnloo open, the onto-something line, the within-the-hour line, the read-as-approximately line, the footer). That file is the correction's body — real newlines, real em-dashes, no escape sequences.
3. **PATCH the same comment** (never a new one):
   `gh api --method PATCH repos/NousResearch/hermes-agent/issues/comments/7147011435 -f body="<the committed note's exact bytes>"`
   The body MUST be the raw file content — the shell passes real newlines and characters when reading it with $(cat ...). Verify the -f payload carries raw bytes, not their JSON-escaped spelling.
4. **Formatting audit on the patched body** (the full pass, like the head's usual one):
   - The footer names NEMO specifically — the prior day's convention (11-11): "Nemo named, Hermes Agent named, on the operator's behalf." If the committed note's current footer (`*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*`) lacks Nemo's name, amend the footer in the PATCH to `*Prepared with Hermes and Nemo, reviewed by c0wb0yp0tat0 before posting.*` — Nemo named as a seat/machine/instrument, never "her."
   - Mentions render: `@kvnloo` un-backticked.
   - One em-dash per sentence max (lines 1, 3, 5: count).
   - The footer is the LAST line, italic, nothing after it.
   - No stray markdown; no raw URLs (the note has none).
5. **Verify the fetch-back**: the live comment's body now equals the corrected body byte-for-byte (real newlines, real chars, the Nemo footer). That verification is the successor's whole worth.

## The required artifact

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-FORMAT-20261124.md`

1. The verdict: PATCHED / CLEAN — with what.
2. The checks' rows with receipts (the before-state showing the escapes, the patch command, the after-fetch body).
3. The final byte-identical verification vs the corrected body.
4. The pair's one-liner.

## Write-window

`write-window: 8` — fetch + patch first, the record by round 7, deepened after. NO stub markers — a placeholder row is a refused landing.

## The hard lines (binding)

- PATCH ONLY the posted comment (same id 7147011435, no new comment, no other write). Nothing else on the RFC surface.
- No installs. All reads LOCAL + the gh api reads of the comment. `git add` + commit locally — NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: byte-identical verification is the floor; a false "verified" like the one that just shipped is the failure class to catch, not repeat.

## The emission contract

Exit 0 = the record EXISTS on disk, re-read, committed; the report names the sha. No tool-call syntax in the final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the wall clause) · gist-formatting-match (the register standard) · the head's usual formatting pass, carried by the successor.
**Refused:** any other write · web reads · installs · memory-chain · config/gateway · coding legs · fan-outs · creative families.

## The LP envelope

- **Customer Obsession:** the pair's reviewed bytes appear on the thread, rendered right.
- **Ownership:** the seam is yours until the record is on disk, re-read, committed.
- **Are Right A Lot:** the fetch-back decides; the first lane's false verification is the cautionary tale.
- **Bias for Action:** fetch now, patch now.
- **Dive Deep:** countable receipts.
- **Deliver Results:** the succession pass, verdict-ridden.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the live comment's bytes, the committed note's bytes — before any verdict.
