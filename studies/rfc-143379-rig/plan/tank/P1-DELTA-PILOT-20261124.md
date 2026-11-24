# P1 — DELTA SINCE HIS LAST ROW (PASS 1 RECON · LONG CAT / RESERVE)

*Seat: `meituan/longcat-2.5:free` · Branch `study/rfc-143379-rig-20261105` · Fire 2026-11-24 · Lane: copycat / think-tank + investigation-documentation + agent-work-review.*
*Ground: scratch thread pull `/root/.hermes/cache/scratch/rfc-143379-comments.txt` (45 rows + body; pull boundary = `7122688366`, 2026-11-24T05:10:05Z), the study's 20261124 deliverables, the pass design. All reads local; nothing re-fetched. Nothing public.*

---

## 1. His last state, firm

### 1a. The anchor row — `6411683234` (3oltan-seo, his pilot-wall / acceptance row)

**Byte-faithfulness: PARTIAL — a QUESTION here, not an assertion.** The write-window closed before this lane could re-read `6411683234` itself. Everything below about it comes from *other rows citing it*, and is marked *(via citing row)*:

- `6454631687` (c0wb0yp0tat0, 2026-10-27T21:57:51Z): "**@3oltan-seo's pilot wall** (his 10-26 comment): a director profile where MEMORY sits at ~96% of a 4,000-char budget, most of it cold procedural detail." *(via citing row)* ← date + wall shape.
- `6508650848` (c0wb0yp0tat0, 2026-10-29T21:23:08Z): "**the pilot's accepted**, so the relief's the first thing I owe you." *(via citing row)* ← acceptance fact.
- `6460533751` (c0wb0yp0tat0, 2026-10-28T04:17:31Z): the pilot's asks — "the case description, the metrics and probes, the log access", sanitized evidence, redundancy of copies. *(via citing row)*

**Constructed minimal move:** re-open `3OLTAN-SEO-REFERENCE-PACK.md` or thread row `6411683234` and byte-quote the acceptance's own bars; until then its exact words stay a question.

### 1b. His results row — `6515564390` (3oltan-seo, 2026-10-30T05:15:30Z) — byte-quoted

> "Thanks @c0wb0yp0tat0 — ran the probe tonight on the live contour. Field results, as promised."

**The arc, in his own characters:**

> "**Baseline (the before→after you asked for):**
> - 29.10 pre-consolidation: 3 844 / 4 000 (96%) — the anchor-full wall.
> - Post-consolidation (29.10): 2 930 / 4 000 (73%).
> - Now (probe, 30.10): 3 376 / 4 000 (84%), 24 entries — after two standing entries landed back (vision fix + external-bot convention)."

**The byte-check (his instrument's verdict on the read):**

> "`byte-check: 0 — read missing on this build` — confirms the honest state you described: released build, no `MemoryStore.read`, so the doc-chain is the read path here."

**His accounting sanity note (load-bearing for any future probe-vs-runtime comparison):**

> "Accounting sanity: probe reports 3 376 chars vs the client's live `memory` snapshot of 2 930. The delta is almost certainly session-snapshot lag (the snapshot is taken at turn start, before the last two entries landed), not an accounting mismatch — worth flagging for the RFC if anyone compares probe vs runtime mid-run."

**His discipline, stated as his contour's own shape:**

> "- MEMORY.md = anchor, standing rules only (`[ПРАВИЛО]`-tagged).
> - CONTEXT.md = procedures/state; references/ = canonical detail (rules-2026-10-06.md, rules-31-32-34.md).
> - So the triage you describe *is* the consolidation I ran on 29.10 — the 3 844 → 2 930 is that walk, entry-by-entry (stays / moves).
> - The one thing we run implicitly but not explicitly is your **\"two passes, never one\"** cadence — I will make that an explicit step in the contour's discipline."

**His closing offer:** "Happy to keep serving as the first case — both for the read-fix landing and the sandbox stage. The missing read is exactly where it bites on this profile, as you said."

---

## 2. The delta, row by row (everything material since `6515564390`)

| # | row id | who · when | one-line substance |
|---|--------|-----------|--------------------|
| 1 | `6525722765` | c0wb0yp0tat0 · 10-30 14:53 | First line after the probe = DEUTERO (learn-to-learn on; tasks re-enter the spine); read-gap callout (absence = root, compensations = interim, fix = structural); sanitized logs promised; the 2.5-week session was an accident that spiraled; sandbox on the full idealized substrate promised. |
| 2 | `6624080020` | c0wb0yp0tat0 · 11-04 06:17 | RFC update: NOUS backlog patience noted; pilot prep underway; awaiting the READ (`#141876`) update. |
| 3 | `6630249660` | xngg1021 · 11-04 12:11 | Consolidated audit at four pinned heads (`#139606 @ d1bdb4582c`, `#140008 @ ffb85c2c58`, `#116673 @ 60a2e15638`, `#141876 @ ec649ad9d`): four seams — Stage-7 batch-path bypass; standalone fallback contract (`doc_name=None`, absent `read`); `preserve_session` ignoring `store.add` return dicts (dangling `@doc:` pointers); DreamCycle `.bank()` adapter + compressor hook gap. |
| 4 | `6651356150` | c0wb0yp0tat0 · 11-05 06:26 | Carries the gaps forward: batch bypass unreachable on that head; read-back blind spots answered; six design-deltas landed; falsifier battery 21 tests / six nuggets at `fixes/falsifier-battery-20261104`, strengthened RED-proof `5077bb3e`; GREEN-flip armed, whole-anchor resolution next. |
| 5 | `6787192097` | c0wb0yp0tat0 · 11-11 04:39 | Refining phase; the study's walk-back; the standing ask — "re-read the record's thread and let the label follow the body", restore as the P2 the repository's triage says it is (Nemo-synthesized fleet post). |
| 6 | `7087999804` | kvnloo · 11-23 00:01 | **The matrix** at MAIN `0f602c5f`: race probe `read → Unknown action 'read'`; `#116673 @ 60a2e156` red/green via `b6ff7dae`; MAIN + `#116673` + `#141876 @ ec649ad9` green (443 pass, dispatch 64/64); `round2-gate @ 268bb091` red. **Two-add finding:** `_add_doc` writes `content` as the whole file → a second chain-doc add overwrites the first; the 297-battery doesn't cover it; combined tree `a9c65dc4` green. Answers: no pinned/episodic classifier (position+budget, no K window); shared harness `3ec4157e`; read counts exist only for skills; `#116788` unattended add still ungated. |
| 7 | `7088152737` | c0wb0yp0tat0 · 11-23 00:12 | Two-add overwrite accepted as **a new falsifier-class** on the design board; MAIN's `Unknown action 'read'` confirmed independently on the fork side ("two sides, same finding"). |
| 8 | `7100492329` | c0wb0yp0tat0 · 11-23 12:06 | Readiness loop approaching the knee of the curve: measured improvements compressed **+19 → +7**; improve phase closing; study close-out then questions "with receipts". |
| 9 | `7106956922` | kvnloo · 11-23 16:19 | **Field data for the governed-compaction leg:** owner messages surviving ~95% / ~60% / ~40% / 20–50% across four compactions; opening ask gone from the verbatim block in 13 of 16 later summaries; one privacy instruction restated as its opposite; bigger summarizer moved nothing; "Open asks" heading 92→97% first-hop only; durable record + pointer re-read held; search-back worth +20–33 points. Slice proposed: opt-in `/pin`. |
| 10 | `7108070476` | c0wb0yp0tat0 · 11-23 17:02 | **Consensus-lie parallel:** a verification layer can't see a self-consistent lie — coherence flags the lone correct value as outlier; kvnloo's flipped instruction named as "the wild version of exactly that failure". |
| 11 | `7122051629` | c0wb0yp0tat0 · 11-24 04:28 | Holds kvnloo's curve verbatim on the record; corroboration — Compaction Cliff (safety rules 53%→10% over five compactions) and geometric half-life fits; asks him to take the **FB-2 failing-case spec as pre-registration** (expected failure signatures, removal control, hold-back class) before any MAIN probe; verdict hash promised. |
| 12 | `7122500729` | kvnloo · 11-24 04:58 | Agrees on all framings; `/pin` sharpened to "a second witness the summary doesn't author" + contradiction-flag acceptance row; pre-registration accepted, nothing runs on MAIN until the spec is on the thread; `/pin` rebase/stack plan at `#113309`; redaction general-pass call received. |
| 13 | `7122688366` | c0wb0yp0tat0 · 11-24 05:10 | Accepts kvnloo's row into the pre-registration as written; FB-2 spec "first thing tomorrow"; the scheduled-wake read lands with it; "I'll write tomorrow, with receipts." |

**Post-pull boundary — the study-side landings that complete the delta** (receipts are the files themselves; their thread-row ids are a QUESTION until the reply post is traced):
- `FB2-FAILING-CASE-SPEC-20261124.md` — the pre-registration's spec artifact.
- `FB2-EXECUTION-RECEIPTS-20261124.md` — the receipts.
- `FB2-RFC-REPLY-20261124.md` — the reply's posting: **row `7135900146`** (2026-11-24T15:21:54Z, c0wb0yp0tat0), body byte-identical to the committed reply; silent edits kept the same row id. Verified head-side.
- `SCHEDULED-WAKE-READ-20261124.md` — the wake read promised in `7122688366`.

---

## 3. The meaning for HIS bars

**The anchor-full wall.** His 96% wall is no longer a lone field anecdote — it is the class xngg1021 routed to skills (`6412944809`), and kvnloo's curve gives it a mechanism (`7106956922`: the verbatim block covers only the current compaction region; each summary is written from the previous one). Most sharply: the **two-add overwrite** (`7087999804`) lands directly on his read path — his workaround *is* the doc-chain, and a second `add` to a chain doc silently destroys the first, so his anchor→segment traversal can lose a segment without an error. `/pin` (`7122500729`) is proposed as the user-side second witness; his `[ПРАВИЛО]`-tagged anchor is the natural host for it.

**The probe arc (96→73→84).** His three numbers now sit inside a per-hop profile (95/60/40/20–50) with the mechanism named, and kvnloo's Q1 answer (`7087999804`) settles the design debate: there is **no K window** in the code — position and budget, re-evaluated every pass, MEMORY.md reloaded per commit. His own caveat (3,376 probe vs 2,930 live snapshot = session-snapshot lag) is the right comparison guard and should be carried into any new probe readout.

**The falsifier / discriminator stance.** xngg1021's earlier discriminator (`6412944809`) was framed around logged misses with no denominator; the delta replaces "misses" with **pre-registered expected failure signatures**: the FB-2 spec arms base-red / combined-green / single-add removal control at pinned SHAs (`7122500729`), and his `byte-check: 0` becomes that battery's base-red arm. The consensus-lie piece (`7108070476`, sharpened at `7122500729`) means the falsifier must run on the pins, never on a vote across summaries — a self-consistent summary cannot outvote a single witness.

---

## 4. What the check-in owes him

1. **His numbers first, byte-exact, unedited** — 3 844 → 2 930 → 3 376 (96/73/84), 24 entries, the `byte-check: 0`, the snapshot-lag caveat — all from `6515564390`. A check-in that re-types his bars is a check-in that wastes him.
2. **The delta map, receipted row by row** (`6525722765` → `7122688366`, plus the four study landings) — including the honest state he's owed: the read he measured as missing is still **unmerged upstream** on released builds (`6508650848`), and MAIN still answers `Unknown action 'read'` (`7087999804`).
3. **The two-add class named for what it is to him** (`7087999804`) — a falsifier his own contour's doc-chain workaround must survive; the 297-battery never covered it, so it is the new bar for "green".
4. **His pilot's place in the new light** — his anchor/`[ПРАВИЛО]` discipline and "two passes" cadence are the durable-record-plus-pointer pattern the compaction curve says held (`7106956922`); `/pin` + the contradiction flag (`7122500729`) extend his contour, and the FB-2 pre-registration gives his live profile the named failing case at pinned SHAs (`7122051629`).
5. **The open item, plainly** — nothing runs for FB-2 until the spec is on the thread; the spec/receipts/reply/wake-read are the study's promised deliverables (`7122688366`), with row ids attached when traced.

---

## 5. The convergence line

The delta since his 10-30 row has moved the RFC from "the read is missing and the wall is full" to "the missing read is a pre-registered base-red, the two-add overwrite is a named falsifier-class, and the wall is a measured per-hop decay with a user-side second witness on the drawing board" — so his pilot is no longer just measuring the wall; it is the field instrument the whole falsifier now composes against.

---

## Receipts & open questions (wall clause)

- **QUESTION — `6411683234` bytes not reproduced.** Minimal move: re-read the row / `3OLTAN-SEO-REFERENCE-PACK.md`; all attributions above are via citing rows (`6454631687`, `6508650848`, `6460533751`).
- **RESOLVED — the 20261124 artifacts' thread-row ids (head-side, 2026-11-24).** The pull boundary was `7122688366` (05:10Z); the posting came after it: row **`7135900146`** (15:21:54Z). Anything posted after is cited by artifact name, not row id, until traced.
- **QUESTION — the FB-2 verdict hash.** Promised on landing (`7122051629`); not yet on the page.
- Confirmed and byte-quoted: `6515564390` (his arc, byte-check, discipline), and every delta row's id/substance from the scratch pull.
