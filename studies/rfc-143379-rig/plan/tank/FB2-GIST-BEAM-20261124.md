# FB2 GIST BEAM REPORT — 2026-11-24

**Verdict: CLEAN-WITH-NOTES**

The gist at `plan/tank/FB2-PRESENTATION-GIST-20261124.md` (29 lines, read cold in full) is one clean single scroll. The six checks land with the countable receipts below; the notes block carries the tweaks for the head.

## The six checks

### 1. The style's the match — PASS, one header note

- **Em-dash cadence:** 3 em-dashes in the whole document, one per sentence — line 21 (`not greps — `), line 25 (`recovered — `), line 29 (`sealed — `). Zero sentences carry more than one em-dash; not a storm.
- **The "the X" noun phrases:** present and load-bearing — `the promise`, `the build`, `the fleet`, `the spec`, `the loops`, `the wall items`, `the code bases`, `the closures`, `the doors`, `the hold-back class's release`, `the RFC #143379 surface`, `the posting decision`.
- **Bold headers:** all six beats present — **the promise**, **the build**, **the loops**, **the execution**, **the closures**, **the doors**. The fifth beat reads `the closures`; the gist-formatting-match standard names the fifth beat `the reshape` → **NOTE 1**.
- **Bookend close:** present — "More to come." (short, forward-leaning).
- **Honesty line in the doors beat:** present — the doors beat names what remains plainly ("Three things wait on the operator's word"), frames all three as the pair's two-way doors, and closes warm.

### 2. The metadata's absent — PASS

Case-insensitive grep receipts on the gist text:

| token | hits |
|---|---|
| `this gist` | 0 |
| `one scroll` | 0 |
| `see below` | 0 |
| `fires on` | 0 |
| `staged` | 0 |
| `the word` | 0 |

Zero matches on all six = pass. No process notes, no staging talk, no "fires on the word," no self-description.

### 3. The holds are held — PASS

- **Hold-back content-hint tokens:** zero hits (the sealed clause's tokens and the test-name class both absent; the gist carries the clause only — "one hold-back class" / "ONE class, withheld").
- **RFC surface:** no posting language, no "will post," no kvnloo-facing framing; the gist is written for the pair. ("The posting decision is the pair's" names the door, per the composer brief.)
- **State words vs the records:** `recovered` = the acceptance row and C4's verbatim recovered; `resolves` = `b6ff7dae` resolved to its real form; `standing` = the standing doors named as standing. Matches the study's records.

### 4. The ear's kindness — PASS

- **Full 40-hex, each exactly once:**
  - `268bb09147eaf948ece6a1beecd92a2268a5fc95` → 1 hit (line 5; later mentions use `268bb091`)
  - `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` → 1 hit (line 5; later mentions use `a9c65dc4`)
  - `b6ff7dae98d19f565764e773e0da96aaee18fbf2` → 1 hit (line 25; earlier mention uses `b6ff7dae`)
- **No long identifier mid-sentence after its first mention:** every repeat use is the 8-hex name (`268bb091`, `a9c65dc4`, `b6ff7dae`) or the fold's 9-hex `aced3e1cf7`.
- **Short sentences, one clause per breath:** the longest sentence is the promise beat's colon-list; the rest are short declaratives.
- **No dash-chains:** max one em-dash per sentence (see check 1).
- **No tangled tokens voiced mid-sentence:** the probe flags ride as inline receipts (`FIRST_SURVIVED_SECOND_ADD=False` / `=True`), not as spoken tangles.

### 5. The handles are proper — PASS with one note

- The gist carries one person-reference: "KvNloo's acceptance is row 7122500729" (line 5). It is the full name, not shorthand, and `@kvnloo` does not appear anywhere (so the quotation-context rule is not triggered). But the row's own words ride after a colon unquoted → **NOTE 2**.
- No other handles; `hy`, `solar`, `longcat` appear as the fleet's own lane names (the build beat), which is the document's internal register.

### 6. The one-document shape — PASS

- One document at the artifact path; no parallel files, no branching structure inside the doc.
- It points at the study's files by path as the room beneath — `FB2-FAILING-CASE-SPEC-20261124.md`, `SCHEDULED-WAKE-READ-20261124.md`, `FLEET-AUDIT-LONGCAT-20261124.md`, `FB2-GREENSIDE-VERIFY-LOOP3-20261124.md`, `FB2-EXECUTION-RECEIPTS-20261124.md`, `plan/tank/briefs/` — without re-telling them.

## Notes

1. **Line 23 — `**the closures**`.** The standard's fifth beat is `**the reshape**`. Fix: rename the header to `**the reshape**` (the beat's own first sentence already says "kaizen reshape" is loop three's business; the closures content stays in the paragraph under it).
2. **Line 5 — "KvNloo's acceptance is row 7122500729: nothing runs on MAIN until the spec is on the thread."** If the row's line is carried, the standard wants it quoted and attributed to the row. Fix: set the row's words in quotes attributed to row 7122500729 (or drop the name and leave "the acceptance row").

## The pair's line

Yes — the gist is ready for the pair's eyes as-is apart from the two header/handle tweaks above; with those applied it is a clean single scroll.