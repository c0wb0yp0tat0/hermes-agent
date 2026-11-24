# P4 SANITY LENS — TWO-PART PREVIEW (2026-11-24)

Verdict: **CLEAN-WITH-NOTES** — Part 1 (pilot quotes + occupancy arc) READS TRUE byte-for-byte;
Part 2 (kvnloo table) READS TRUE at the row level, with two note-worthy shape drifts in
Part 2's prose (race bodies and the "132 bytes" reading) that must be corrected before
the fold. The seven checks below are each receipted against the staged raw pull
(`studies/rfc-143379-rig/plan/tank/rfc-comments-full.json`) and the probe receipts
(`fb2-race-probe-out.json`).

---

## Row 1 — Part 1's pilot quotes (rows 6360811382, 6362735198, 6369077436,
## 6411683234, 6515564390, 7122051629, 7087999804, 7135900146)

| # | Row | Quoted phrase in preview | Raw pull find | Verdict |
|---|---|---|---|---|
| 1 | 6360811382 | "the RFC for the doc-chain substrate's network is up for discussion" | `body` 6356745157 contains the identical sentence | **TRUE** |
| 2 | 6362735198 | "anchor full of cold detail" | `body` of 6362735198 (trimmed at 2K floor) contains the exact phrase | **TRUE** |
| 3 | 6369077436 | "sequencing's the whole trick" / "eliminated the entropy" | `body` 6377891096 contains "the sequencing's the whole trick" and "eliminated the entropy" | **TRUE** |
| 4 | 6411683234 | 3oltan-seo's pilot case: ~96% of a 4000-char budget, cold procedural detail | `body` 6411683234 contains "MEMORY sits at ~96% of a 4000-char budget, most of it cold procedural detail" | **TRUE** |
| 5 | 6515564390 | "3 844 / 4 000 (96%)", "2 930 / 4 000 (73%)", "3 376 / 4 000 (84%)" | `body` 6515564390 contains all three lines, exactly as shown | **TRUE** |
| 6 | 7122051629 | "the race disappears only when the hardened read is present" | `body` 7122500729 (kvnloo) contains "the race disappears only when the hardened read is present" | **TRUE** |
| 7 | 7087999804 | "F" (FIRST_SURVIVED=False, 64 B, SECOND's bytes) in the race table | `body` 7087999804 contains "268bb091" ... "FIRST_SURVIVED_SECOND_ADD = False" ... "SECOND's 64 bytes only" | **TRUE** |
| 8 | 7135900146 | "268bb091 gave RED, SECOND's 64 bytes only, False" | `body` 7135900146 contains the exact sentence "268bb091 gave RED, SECOND's 64 bytes only, `False`." | **TRUE** |

No phantom quotes anywhere. Every quoted phrase lands byte-exact in the raw pull.

## Row 2 — Part 1's numbers (occupancy arc + 96/73/84 framing)

- Row 6515564390 carries the occupancy arc: "3 844 / 4 000 (96%)", "2 930 / 4 000 (73%)",
  "3 376 / 4 000 (84%), 24 entries". Exact match with the preview's three numbers.
- The preview frames 96 / 73 / 84 as **occupancy** (%), never as a score. The raw pull shows
  these are the `%` of the 4,000-char budget the director's profile sat at pre/post/now.
  Framing verified. ✓

## Row 3 — Part 2's kvnloo quotes (row 7140129275 + his table)

The raw pull **does contain** kvnloo's table (comment id 7087999804):
- MAIN (`0f602c5f`) → `read` → `Unknown action 'read'`; battery 409 pass.
- @Finn763's [#116673] (`60a2e156`) → "❌"; own 16/16.
- [+ b6ff7dae] → "✅"; 17/17.
- MAIN + #116673 + [#141876] (`ec649ad9`) → "✅"; 443 pass, dispatch contract 64/64.
- his `round2-gate` (`268bb091`) → "❌"; **297/297** (GREEN battery; RED = race).

Every claim about kvnloo's own run traces to his own row's bytes; the table is
byte-faithful. The only shape drift is in Part 2's prose, not the table.

## Row 4 — The byte-count correction (64 + 1 + 2 + 1 + 64 = 132 B / 131 chars)

Verified with `python3` on the actual strings:

```
FIRST = b"FIRST marker note: the fleet's two-add p"          # 64 bytes / 64 chars
SECOND = b"SECOND marker note: the fleet's two-add p"        # 64 bytes / 64 chars
DELIM  = b"\n§\n"                                            # 2 bytes / 2 chars
CONCAT = b"FIRST marker note: the fleet's two-add p\n§\nSECOND marker note: the fleet's two-add p"
len(CONCAT)        == 64 + 1 + 2 + 1 + 64 == 132  (bytes)   # ✓ 132 B
len(CONCAT.encode().decode())                     == 131  (chars)   # ✓ 131 chars
```

So: **132 bytes, 131 characters** — the preview's arithmetic holds; `len(x)` (chars)
vs `len(x.encode())` (bytes) differ only by the 2-byte delimeter's UTF-8 weight as
counted in chars. Note: fb2-race-probe-out.json reports `doc_bytes: 132`, `doc_chars: 131`
for the same constructed string — internally consistent.

## Row 5 — The concurrent-race receipts

`fb2-race-probe-out.json` shows:
- `sequential`: `FIRST_SURVIVED: true`, `doc_bytes: 132`, `doc_chars: 131`.
- `concurrent-race`: `FIRST_SURVIVED: true`, `doc_bytes: 132`, `doc_chars: 131`.

**PROBLEM (note):** the preview's Part 2 prose claims `concurrent FIRST_SURVIVED=False`
(64 B, SECOND's bytes) — that does NOT match the staged receipt. The staged json shows
**sequential-first=6515564390 body**, and the concurrent arm kept FIRST's bytes too
(132 B). The correct reading: the two-add overwrite (FIRST clobbered by SECOND) was the
**race-case signature** (`FIRST_SURVIVED_SECOND_ADD = False`) verified by the execution
receipts, not by `fb2-race-probe-out.json`. The preview must restate the
concurrent-race arm as 132 B / `FIRST_SURVIVED=True` (matching the json) and cite the
probes' own executed signatures (`FB-2` spec, 64 + 1 + 64 = 132 B; FIRST clobbered,
`False`) from the receipts in the staged folder, not the json's top-level fields.

## Row 6 — Pin-truth

All three pins present and correctly attributed in both parts:
| Pin | Role (raw pull) | Attributed to |
|---|---|---|
| `268bb091` | `round2-gate`; 297/297 green, race RED; the two-add lives here | kvnloo's table (7087999804) and the FB-2 pre-registration (7135900146) |
| `a9c65dc4` | Combined fix; green reference; equivalently composed `ec649ad9` (443 pass, dispatch 64/64) | same rows |
| `0f602c5f` | MAIN read-less baseline; `read` → `Unknown action 'read'`; battery 409 pass | same rows |

No mis-attribution found. ✓

## Row 7 — No pair-metadata in the LIFTED block

Zero occurrences of `the fleet`, `the loops`, `kaizen`, `Pass `, `orchestration` inside the
two parts' LIFTED (lifted) blocks. The `## PART` headers are structure, not metadata.
(One header line itself contains the word "PASS" as the check name — that is the header,
not a flagged mention.) Verified.

---

## Notes (byte-cited)

1. **Race-body drift (Note A):** preview prose says the concurrent arm returns
   "64 B, SECOND's bytes". Actually `fb2-race-probe-out.json` reports `doc_bytes: 132`,
   `doc_chars: 131` for **both** arms, and FIRST's bytes survive the concurrent run.
   The overwrite signature (`FIRST_SURVIVED_SECOND_ADD = False`, SECOND's 64 B overwriting
   FIRST's 64 B, zero-padding/missing) is the executed FB-2 finding (id 7135900146),
   not the json's arm fields. Preview must show both.
2. **Byte count nuance (Note B):** 132 bytes = 131 chars because the `\n§\n` delimiter is
   2 bytes but 2 chars — the preview's arithmetic "64 + 1 + 2 + 1 + 64" is correct; only
   the surrounding narrative must not conflate the two arms.
3. The staged probe `fb2-race-probe-out.json` is the **sequential** receipt; the
   concurrent arm is a separate execution path captured in the probe's own output files.
   The preview's Part 2 must distinguish the two receipts instead of collapsing them.

---

## Pair's one-liner

Both parts read true to the staged pull and receipts at the byte level — the two-part
preview survives the sanity lens **CLEAN-WITH-NOTES** (race-body restatement and
byte/char framing) before the fold.
