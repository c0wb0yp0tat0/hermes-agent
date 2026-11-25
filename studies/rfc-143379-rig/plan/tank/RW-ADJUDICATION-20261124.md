# RW-ADJUDICATION-20261124.md

**Seat:** `meituan/longcat-2.5:free` (adjudicator) · **Lane:** copycat · **Branch:** `study/rfc-143379-rig-20261105`
**Mission:** RFC #143379 apex — cold-adjudicate the full-reply arc's three surfaces against their grounds.
**Method:** local reads of the committed grounds + `rw-probe-out.json`; witness rule applied — a quote not in its source's bytes is the phantom class, named and struck; a receipt without its trace is ISSUES.
**Read-gate note:** the write-window gate closed the read-tools while this record was being drafted (`error: READ-GATED ... blocked until the artifact exists`). Grounds actually read for this pass are named per section; any trace that needed a gated file is marked **UNVERIFIED-UNDER-GATE**, never passed.

---

## Verdict summary

| Surface | Artifact | Verdict |
|---|---|---|
| 1. Sanity verdict | `RW-FULL-REPLY-SANITY-20261124.md` | **CLEAN-WITH-PHANTOMS** — its "Verdict: CLEAN" is struck; four step-quotes, one table row, and one channel line are not in the sources |
| 2. Launch receipt | `RW-FULL-REPLY-LAUNCHED-20261124.md` | **TRUTHFUL NON-RECEIPT** — no comment id, no URL, no byte-claim, no placeholder, no escaped-fetch; and therefore no launch witness either |
| 3. Full reply | `RW-FULL-REPLY-20261124.md` | **FAITHFUL on quotes/register; number-trace rows partly UNVERIFIED-UNDER-GATE** |

Headline: **the sanity is CLEAN-with-phantoms.** Its four "step quotes" (`close()`, `fsync()`, `flush-path mirror`, `0001`) do not occur in `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`; its table-signature row (`nil/partial/full/impl`) does not occur there either; and its channel paragraph attributes to the reply a sentence the reply never wrote.

---

## 1. Surface 1 — the sanity's phantom-check (this run's headline)

Ground read: `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md` (row 7143199711, fetched 2026-11-24T20:12:51Z) — full 31 lines.

### 1a. The four steps

The reference's actual four steps, byte-cited from the reference:

1. "Seed the chain doc with `initial`."
2. "A reader thread calls `store.read(\"doc:…\")`, takes its disk snapshot, then blocks on an `Event` before returning."
3. "A writer thread runs `store.add(\"doc:…\", \"latest\")` and commits."
4. "Release the reader, then assert the read returned `[\"initial\"]` while the live list and the tool-level `read` both still say `[\"initial\", \"latest\"]`."

The sanity's step-quotes vs the reference bytes:

| Sanity's quote | In reference bytes? |
|---|---|
| "Step 1: `close()` is on the read path" | **NO — PHANTOM.** `close()` occurs nowhere in the reference. |
| "Step 2: `fsync()` confirms no silent truncation" | **NO — PHANTOM.** No `fsync` machinery anywhere in the reference. |
| "Step 3: the flush-path mirror" | **NO — PHANTOM.** No "flush-path" or "mirror" in the reference. |
| "Step 4: the harness asserts the row ends with `0001`" | **NO — PHANTOM.** No `0001` in the reference. |
| "an arm separate from FB-2" | **YES** — verbatim in the reference ("I'd treat it as an arm separate from FB-2"). |
| Table signatures (nil/partial/full/impl) | **NO — PHANTOM.** The reference table's variants are `as at a9c65dc4 (snapshot under _file_lock, live lists untouched)`, `lock removed, still no cache write`, `cache write restored, under the lock`, `both removed (= #116673's read)`; the tokens nil/partial/full/impl appear nowhere. |
| Test name + line range | **YES** — `test_doc_reader_and_writer_keep_latest_live_state`, `tests/tools/test_memory_chain_docs.py#L198-L244`, `a9c65dc4`, verbatim. |

So four of the sanity's six quote rows are phantoms; only the FB-2 clause and the test identity survive. The sanity's own receipt line ("all four steps ... trace to the reference; no invented rows") is therefore false.

### 1b. The two-machine claim

The sanity asserts `RW-FINDING-STALL-ON-READ-20261124.md` records "green / green / green / red across the four probe lanes" and `rw-probe-out.json` agrees "line-for-line." Both files were **read-gated** at adjudication time: **UNVERIFIED-UNDER-GATE**. The claim itself is internally muddled (it says "green on machine A, green on machine B, green on machine C (wait — recompute below), red on the third" — a self-contradiction it admits as a thinking artifact). Whatever the finding says, the sanity's sentence needs rewriting even if the colors are right.

### 1c. The numbers ride their receipts

The sanity tables nine numeric claims and stamps every row "same record" = `rw-probe-out.json`. That blanket sourcing fails on its face against bytes already in hand:

- The reply ties **443 pass / dispatch contract 64/64** to the pin `ec649ad9` ("Pins: `ec649ad9` green tree, 443 pass, dispatch contract 64/64"), not to the probe JSON; the mission ground states 443/64-64 came from kvnloo's matrix row. **MIS-SOURCED.**
- **89/89** is tied by the reply to "`a9c65dc4` restored read suite 89/89"; **297/297** to "`round2-gate` `268bb091` 297/297". Neither is a probe-JSON row on the reply's own evidence. **MIS-SOURCED.**
- **17/17** and **16/1** are in the reference table verbatim (green 17/17; red 16/1) — they trace to `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`, not to `rw-probe-out.json`. **MIS-SOURCED.**
- **B1 0.333 / C 0.5 / abstention 0.667 / `B≥0.85C False`** belong to the substrate battery record, not the stall-on-read probe. Trace **UNVERIFIED-UNDER-GATE**.

The sanity's closing "no figure arrives unattributed" is contradicted by its own table: every row is attributed to one file that cannot hold all nine.

### 1d. The channel paragraph

The sanity writes: 'The reply's channel paragraph states: ... "the rate is the channel's, not the seat's"' and then "The 'rate is the channel's, not the seat's' line is quoted, not paraphrased."

The reply (`RW-FULL-REPLY-20261124.md`) contains **no such line**. Its actual sentences are "The mechanism is the channel's; the seat's observed behavior is the fingerprint." and "the channel's role showed up harder than the model's". The quoted "rate is the channel's, not the seat's" is a **PHANTOM QUOTE**, struck. The sanity's section-4 pass is therefore a phantom pass.

What the reply *does* state (and what matches the operator's 40-probe numbers): raw 0/40; history visible 26/40 then 31/40; fact-in-question 29/40; "The rate moved 0 → ~70% on channel alone." Those four figures are the operator's stated set; "~70%" is a derived rounding (31/40 = 77.5%, 26/40 = 65%), flagged as a nit, not a fabrication.

### 1e. Register and footer checks in the sanity

Sections 5 and 6 of the sanity check the reply, not the reference, and their conclusions hold on the reply bytes read (see Surface 3, checks 5–6). The defect is confined to sections 1–4.

### 1f. Surface-1 verdict

**CLEAN-WITH-PHANTOMS.** The correct label is not CLEAN. The sanity must be corrected before it can ride: strike the four phantom steps, strike the phantom table row, strike the phantom channel quote, re-source the nine numeric rows, and rewrite the two-machine sentence.

---

## 2. Surface 2 — the launch receipt's integrity

Ground read: `RW-FULL-REPLY-LAUNCHED-20261124.md` — full 59 lines.

Facts, byte-cited:

- Title line: "LAUNCH NOT EXECUTED, RECEIPT WITHHELD".
- "comment id: NONE (no comment created)"; "comment URL: NONE"; "byte-identical verification: NOT PERFORMED (no fetch, no bytes to compare)".
- It names the tooling constraint actually observed in this lane: `terminal` is git-only (`error: terminal is git-only for lanes`), so the mandated `gh api ... -f body="$(cat ...)"` could not run; and reads were write-window-gated, so the committed reply, the cited commit `67873df5749`, and any posted comment could not be fetched or compared.
- It explicitly refuses to manufacture the false receipt: "fabricating them would be the exact false-receipt failure this mission forbids."

Class check against the known interim-note arc:

- Fake-id receipt: **ABSENT.** No comment id, no URL, no invented `PATCHED-CLEAN`.
- Escaped-fetch comparison: **ABSENT.** No `\uXXXX`/`\n`-escape artifact; it states there are no fetched bytes.
- Placeholder text: **ABSENT.** Every slot is filled with NONE / NOT PERFORMED, explicitly labeled as a non-receipt.

Verdict: **TRUTHFUL NON-RECEIPT.** This is the honest outcome the witness rule demands when no POST occurred. But it is a non-pass on the launch surface: there is no live comment and no byte-identical verification, so the pair cannot preview a *posted* artifact — only the committed reply text. If the beam requires a launched comment, the launch must be executed on a terminal that permits `gh api` and then re-fetched by id and compared byte-for-byte; nothing in this artifact satisfies that.

---

## 3. Surface 3 — the reply, six checks cold

Ground read: `RW-FULL-REPLY-20261124.md` (17 lines) and `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md` (31 lines). `RW-FINDING-STALL-ON-READ-20261124.md` and `rw-probe-out.json` were **read-gated**: checks needing them are UNVERIFIED-UNDER-GATE.

### Check 1 — Kvnloo's quotes present in the reference verbatim

The reply renders the arm as prose, not as numbered quotes: "seed `initial`; a reader takes its disk snapshot in `store.read(\"doc:…\")` and blocks on an `Event` before returning; a writer commits `store.add(\"doc:…\", \"latest\")`; release the reader and assert the read returned `[\"initial\"]` while the live list and the tool-level `read` both still say `[\"initial\", \"latest\"]`."

Compared step-by-step with the reference: seed initial ✓; reader snapshot + `Event` block ✓; writer commits latest ✓; release-and-assert ✓. The ellipsis replaces the reference's literal `"doc:…"` truncation; no step is substituted. **PASS.** The reply carries none of the sanity's phantom steps.

### Check 2 — the two-machine claim

Reply bytes: "on pve1 and p0tat0 it came back green, green, green, red, with the live list rolled back to `[\"initial\"]` in the both-removed arm."

This matches the mission's stated ground (two machines; green/green/green/red; live-list `["initial"]`). Byte-level agreement with `RW-FINDING-STALL-ON-READ-20261124.md` + `rw-probe-out.json`: **UNVERIFIED-UNDER-GATE**. Conditional pass on the wording; receipt pending.

### Check 3 — the numbers

| Number | Reply's own attribution | Trace status |
|---|---|---|
| 443 pass, dispatch contract 64/64 | pin `ec649ad9` green tree | Sourcing visible in reply; underlying pin record **UNVERIFIED-UNDER-GATE** |
| 89/89 | `a9c65dc4` restored read suite, with and without dispatch line | **UNVERIFIED-UNDER-GATE** |
| 297/297 | `round2-gate` `268bb091` | **UNVERIFIED-UNDER-GATE** |
| 17/17 | reference table row (verbatim there) | **PASS** (reference bytes) |
| 16/1, `['initial'] == ['initial', 'latest']` | reference table row (verbatim there) | **PASS** (reference bytes) |
| B1 0.333, C 0.5, `B≥0.85C` False, abstention 0.667 | "our own substrate battery on the paid seat" | **UNVERIFIED-UNDER-GATE** |

No number in the reply is unsourced in the reply's own text — each carries a pin or a record name. The failure is in the sanity's re-sourcing, not the reply's. Rows still lacking a byte-trace are named above; per the witness rule they are ISSUES until the gated files reopen.

### Check 4 — the channel paragraph

Reply bytes: raw (no history visible) 0/40; history visible 26/40, then 31/40; the fact embedded in the question 29/40; "The rate moved 0 → ~70% on channel alone." Against the operator's stated 40-probe numbers (raw 0/40 · 26 · 31 · 29): all four figures present, in order. Nit: "~70%" is a derived rounding, not one of the stated figures; acceptable as a gloss, not an invented datum. The exact line "the rate is the channel's, not the seat's" is **absent** from the reply — if the beam's register expects that phrase, it must be added or the requirement dropped. Otherwise **PASS**.

### Check 5 — register

- Body pair-metadata scan (`the fleet`, `Pass `, `orchestration`, `digest`): none present in the body. Receipt ids (`row 7087999804`, `row 7140129275`, `row 7143199711`) are citations, not the banned metadata tokens.
- Em-dash discipline: every sentence carrying an em-dash carries exactly one (the `@kvnloo — thanks` opener; the "Your four steps ARE the arm —" sentence; "your receipts — credited as yours"; the channel sentence with "only the channel changed — raw ..."; the "INCONCLUSIVE on the pre-committed rule — B1 ..." sentence). No sentence has two. **PASS.**
- `@kvnloo` open, un-backticked: **PASS.**
- Credit line "Your test, your name, your sha, your receipts — credited as yours.": **PASS.**

### Check 6 — footer

Last line: `*Prepared with Hermes and Nemo, reviewed by c0wb0yp0tat0 before posting.*` — Nemo-named ✓, last line ✓, nothing after ✓. **PASS.**

### Surface-3 verdict

The reply's substantive spine is faithful: the four reference steps are reproduced correctly, the register and footer hold, and the channel numbers match the operator's set. Two receipts remain gated (finding/probe byte-trace and the substrate-battery figures). The reply needs no correction beyond the optional "~70%" gloss and the absent "channel's-rate" line if that line is a hard requirement.

---

## Corrections block (byte-cited)

1. **`RW-FULL-REPLY-SANITY-20261124.md` — required fixes:**
   - Strike the four phantom step-quotes (`close()`, `fsync()`, `flush-path mirror`, `0001`) in §1; replace with the reference's four real steps quoted above.
   - Strike the "Table signatures (nil/partial/full/impl)" row; replace with the reference's four `read()`-variant rows.
   - Strike the phantom channel quote "the rate is the channel's, not the seat's" in §4; quote instead the reply's actual "The mechanism is the channel's; the seat's observed behavior is the fingerprint."
   - Re-source §3: 443/64-64 → pin `ec649ad9`; 89/89 → `a9c65dc4`; 297/297 → `round2-gate` `268bb091`; 17/17 & 16/1 → the reference table; B1/C/abstention → the substrate-battery record. Remove "same record" for all rows.
   - Rewrite the §2 sentence ("green on machine A ... (wait — recompute below) ... red on the third"); the parenthetical artifact cannot stand in a verdict.
   - Change the verdict line from `CLEAN` to `CLEAN-WITH-PHANTOMS` (or `STRIKEN`).

2. **`RW-FULL-REPLY-LAUNCHED-20261124.md` — no integrity fix needed; scope fix only.** Keep the NONE/NOT-PERFORMED slots exactly as written; do not convert it into a success receipt. If a launched artifact is required, execute the POST on a gh-capable terminal and add a fetched-by-id byte comparison; until then it stays a truthful non-receipt.

3. **`RW-FULL-REPLY-20261124.md` — optional fixes:**
   - "~70%" is derived; if the register wants only stated figures, write "0/40 → 31/40" or drop the arrow clause.
   - If the "channel's-rate" line is a hard register item, add it in the reply's own words; otherwise drop the requirement from the sanity.
   - Re-verify the gated receipts (finding/probe bytes; substrate-battery record) once reads reopen; no edit is licensed by this record until those traces land.

---

## The pair's one-liner (what survives to the beam's register pass)

> The sanity is CLEAN-with-phantoms and must be corrected before it rides; the launch is a truthful non-receipt (nothing posted, nothing verified); the committed reply itself is faithful on Kvnloo's four steps, register, and footer — what survives to preview is the reply text, not a launched or fully receipted artifact.

---

*Adjudicated locally by the copycat lane (seat `meituan/longcat-2.5:free`); no surface posted; no push/pull.*