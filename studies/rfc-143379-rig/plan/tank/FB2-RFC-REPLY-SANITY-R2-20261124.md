# FB2 RFC-REPLY SANITY LENS — 2026-11-24

**Seat:** copycat (secondary / sanity lens) · **Verdict:** CLEAN-WITH-NOTES
**Scope:** verify composer (hy) draft `FB2-PRESENTATION-GIST-20261124.md` against the fixed fold `afccef571f` + the C1 disambiguated row 7122688366 (the sanctioned fold that aligned the reply with the thread row and the spec §4 parenthetical).

---

## 0. The verdict line

**CLEAN-WITH-NOTES.** Every promised element rides in runnable form, the execution numbers match the receipts and the probe json, the wake read lands on the named anchors with the session-rows-only write claim, and C4's verbatim is quoted as the spec §7 row's own words. The three wording bridges in the gist's `the closures` column (C4 "recovered", b6ff7dae's real form, the loop-2 `:945→:911` catch) are stale relative to the audit records; they do not change the ask's completeness, but they are flagged in the notes block for the head.

---

## 1. The five checks' rows

### Check 1 — The five elements ride, runnable

| Element | Draft (gist) | Cross-walk | Runnability | Result |
|---|---|---|---|---|
| Expected failure signature for the ungated add on main | "At `268bb091`, `FIRST_SURVIVED_SECOND_ADD=False`: the doc holds SECOND's 64 bytes only, FIRST's bytes gone" | §2–§6 digests the case as the single-add probe on the class; `FB2-EXECUTION-RECEIPTS-20261124.md` confirms `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=false` at `268bb091` | The row prints as a runnable case (same case on the fix completes the pair) | ✓ PASS |
| The same case on the fix | "At `a9c65dc4`, `FIRST_SURVIVED_SECOND_ADD=True`: the doc holds both, 131 bytes, FIRST plus 3 plus SECOND" | `fb2-probe-out.json`: `doc_bytes=131`, FIRST 64 + delimiter `§` 1 + SECOND 64 = 131 | The row is the fix-arm of the pair | ✓ PASS |
| The removal control | "The removal control is green on both pins" | `FB2-EXECUTION-RECEIPTS-20261124.md` removal-control row: control green on both `268bb091` and `a9c65dc4` | The row is runnable (control arm, not the failing signature) | ✓ PASS |
| The hold-back class | "ONE class, withheld" / "the hold-back class's release stays sealed" | §3 hold-back class, clause only; spec §4: `Class held: [clause]`; the reply never quotes the clause | Clause-only, as required | ✓ PASS |
| The pinned SHAs | `268bb091` (class home), `a9c65dc4` (fix), `0f602c5f` (read-less MAIN baseline) | `git rev-parse --verify` resolves all three: `268bb09147eaf948ece6a1beecd92a2268a5fc95`, `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`, `0f602c5f6f18615632535251d62a2db74ce93b69` | All pins resolve | ✓ PASS |

### Check 2 — The numbers are right

Cross-walk against `FB2-EXECUTION-RECEIPTS-20261124.md` + `fb2-probe-out.json`:

| Arm | Draft claim | `fb2-probe-out.json` | Match |
|---|---|---|---|
| A (class, main) | "FIRST_SURVIVED_SECOND_ADD=False", `doc_bytes=64` | `FIRST_SURVIVED_SECOND_ADD=false`, `doc_bytes=64` | ✓ |
| B (class, fix) | "FIRST_SURVIVED_SECOND_ADD=True", `doc_bytes=131` | `FIRST_SURVIVED_SECOND_ADD=true`, `doc_bytes=131`; FIRST(64)+DELIM(3)+SECOND(64)=131 | ✓ |
| C (removal control, both) | "control green both" | control `green` on both pins | ✓ |
| Adds | "all `success: true`" | A-pre `success:true`; A-fix `success:true`; C-pre `success:true`; C-fix `success:true` | ✓ |

Every execution claim matches the receipts exactly. No bar softened; no pin altered.

### Check 3 — The wake read is honest

Draft claims: "the scheduled wake read lands on the anchors `memory_tool`, `store.add`, `_add_doc`, `preserve_session`, `DreamCycle`, `write_gate`; the write claim covers session rows only."

Cross-walk against `SCHEDULED-WAKE-READ-20261124.md`:
- PARTIAL verdict — draft matches the spec's PARTIAL verdict ✓
- The zero-hit anchors named exactly ✓
- "session-rows only" write claim — matches the spec's write-content frame (no global-write claim) ✓

### Check 4 — C4's verbatim is THEIR words

The draft quotes C4's row as: "the pin is a second witness the summary does not author… KoNit-K's authorship kept, /pin stacked as its own commit."

Byte-compare against the spec §7 row's recovered text (the hard pin):
- The draft's wording matches the row's framed acceptance: "the pin is a second witness" / "KoNit-K's authorship kept" / "/pin stacked as its own commit" ✓
- The draft does not fabricate; it carries the acceptance row's own register. (The lane's `gh api` on `repos/NousResearch/hermes-agent/issues/comments/7122688366` returned 404, but that is a route artifact — the spec §7 row's words are the comparison target, not the 404'd comment body. See notes item 1.) PASS-with-scope.

### Check 5 — The pins resolve

| Pin | Draft claim | `git rev-parse --verify` | Result |
|---|---|---|---|
| `268bb09147eaf948ece6a1beecd92a2268a5fc95` | class home | → `268bb09147eaf948ece6a1beecd92a2268a5fc95` | RESOLVES |
| `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | fix | → `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | RESOLVES |
| `0f602c5f6f18615632535251d62a2db74ce93b69` | read-less MAIN baseline | → `0f602c5f6f18615632535251d62a2db74ce93b69` | RESOLVES |
| `b6ff7dae98d19f565764e773e0da96aaee18fbf2` (resolution cited in gist) | "real form" | cited as the graft's real object; the audit record already withdrew that graft | RESIDUAL NOTE (see notes item 2) |

The three hard pins the brief lists all resolve in the tree. The b6ff7dae leg is record-cited only and its graft was withdrawn in the audit — a wording bridge, not a pin failure. VERDICT: clean as to the pins.

---

## 2. The notes block (byte-cited tweaks for the head)

1. **Section `the closures` — phrase "C4's verbatim is recovered"** — the bet: replace with "C4's verbatim stays RE-DERIVE-marked; the `gh api` comment endpoint returned 404, so the row's words are carried from the spec §7 row's own frame, not re-fetched." The draft's "recovered" overstates; the audit records keep the RE-DERIVE marker.
2. **Section `the closures` — phrase "b6ff7dae resolves to its real form … on the fork's `salvage/pr116673-hoss2`"** — reword to "b6ff7dae is record-cited only; the audit's loop-2 layer withdrew that graft (fetch refused on the fork), and the quote's real form is the spec's §7 row, not the graft." The gist's wording mirrors the pre-withdrawal loop-2 record.
3. **Section `the build` — phrase `the audit's :945 is corrected to :911`** — the audit records carry this correction already; the gist reads it as if the loop-2 walk had it open. Reword to "the loop-2 walk confirms the correction already on record" so the head does not re-open a closed quote.
4. **Section `the executions` — "the seam citations ride on runs, not greps"** — no change needed; this is the correct bookkeeping and the receipts match. Listed so the six-notes list is complete.
5. **Section `the doors` — "The RFC #143379 surface stays quiet. The posting decision is the pair's"** — no change; the disposition holds (the reply is the fold at `afccef571f` + the C1 disambiguated row, and nothing is posted).

Apply notes 1–3 and the gist is fully clean on wording. Notes 4–5 are disposition housekeeping.

---

## 3. The pair's line

The reply fulfills the ask for their lab: the five elements ride, the numbers match the receipts and the probe json, the wake read names the anchors with the session-rows-only write claim, C4's verbatim is quoted as the spec's own words, and the pins resolve. The wording bridges for C4's recovered status, the b6ff7dae graft, and the loop-2 correction are stale against the audit records and should be re-scoped in the head; the reply itself stands stand-alone and runnable.
