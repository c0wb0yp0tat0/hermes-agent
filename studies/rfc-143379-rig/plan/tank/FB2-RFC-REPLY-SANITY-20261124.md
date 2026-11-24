# FB2 RFC-REPLY SANITY REPORT — 2026-11-24

**Verdict: CLEAN-WITH-NOTES**

## The verdict line

**CLEAN-WITH-NOTES** — the five elements ride, runnable; the execution numbers match the receipts; the wake read is honest; the three cited pins resolve. One defect: the C4 quote is a truncated reproduction that drops a substantive clause of the flagged contradiction (the "check runs on the pins, never on a vote across summaries" clause). The reply must reproduce the spec §7 row's text byte-for-byte, including that clause.

## The five checks' rows

### Check 1 — Five elements ride, runnable

**RECEIPT: PASS (all bars pre-registered, none softened).**
- (a) Expected failure signature for the ungated add on MAIN: `FIRST_SURVIVED_SECOND_ADD = False` — whole-file overwrite, SECOND's 64 bytes only. In-spec.
- (b) Same case on the fix: `FIRST_SURVIVED_SECOND_ADD = True` — FIRST's bytes survive, 131 bytes, both present. In-spec.
- (c) The removal control: one add round-trips green on all three pins; RED there invalidates the probe. In-spec, with the pre-fix leg honestly marked RE-DERIVE in the spec loop-2 record.
- (d) The hold-back class: one clause only, withheld; signature deliberately not written where a runner can read it. In-spec.
- (e) The pinned SHAs: `0f602c5f6f18615632535251d62a2db74ce93b69` (MAIN full form), `268bb09147eaf948ece6a1beecd92a2268a5fc95`, `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` — all printed.

### Check 2 — The numbers are right

**RECEIPT: PASS (byte-exact vs the probe json).**
- `268bb091` (pre-fix, two-add): `doc_bytes: 64`, `FIRST_SURVIVED_SECOND_ADD: false` → RED `False`/64 B. Match.
- `a9c65dc4` (fix, two-add): `doc_bytes: 131`, `FIRST_SURVIVED_SECOND_ADD: true` → GREEN `True`/131 B. Match.
- 131 = 64 (FIRST) + 3 (newline) + 64 (SECOND) → the reply's "64+3+64" is the byte-accurate composition. Match.
- Control (single-add) red-green on both pins: receipt states green on `268bb091` and `a9c65dc4`. Match.
- All `add_results`: `success: true` in the json's four arms. Match.

### Check 3 — The wake read is honest

**RECEIPT: PASS.**
Reply's wake passage: "PARTIAL at `8ba4b344766e50c2e3eeaba84f4349276a1be021`. The scheduled wake reads `state.db`/`state.py` and writes its own session rows, but hits zero on every memory-store anchor — `memory_tool`, `store.add`, `_add_doc`, `preserve_session`, `DreamCycle`, `write_gate`. The memory-store write path is untouched, so the wake cannot disturb it."
Matches `SCHEDULED-WAKE-READ-20261124.md` exactly: PARTIAL verdict, zero-hit anchors named verbatim, session-rows-only write claim. No softening, no added anchor. Pass.

### Check 4 — C4's verbatim is their words (byte-level)

**RECEIPT: FAIL (truncated reproduction).**
Reply's quote: `"the pin is a second witness the summary does not author… KoNit-K's authorship kept, /pin stacked as its own commit."`
Spec's §7 row verbatim: `"the pin is a second witness the summary does not author, and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it. The ledgers move with your rebase, KoNit-K's authorship kept, /pin stacked as its own commit."`

Byte-compare: the reply's quote is the spec's text **truncated at the first ellipsis**, dropping the clause `"and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it."` That clause is the substance of the contradiction-flagged row (C4) — the vote-across-summaries point is precisely what the contradiction marks. The ellipsis signals a gap to the runner; the spec's row is a run-on single sentence ending in the KoNit-K authorship clause. The reply must reproduce the full sentence, flag preserved, not a summarized abridgement.

### Check 5 — The pins resolve

**RECEIPT: PASS (three cited pins resolve; the fourth is not cited).**
- `0f602c5f6f18615632535251d62a2db74ce93b69` (MAIN full form): `git cat-file -t` → **commit** (REAL; the spec's §6 full form for 0f602c5f is correct). The loop-2 record's catch was that the *grafted* 40-hex `b6ff7dae6f18…` (which shares 0f602c5f's tail) is not an object — the reply does not cite the graft, only the real 40-hex, which resolves.
- `268bb09147eaf948ece6a1beecd92a2268a5fc95`: commit (pin of the failing case). Resolves.
- `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`: commit (pin of the fix). Resolves.
- The fourth pin, `b6ff7dae` (full form `b6ff7dae98d19f565764e773e0da96aaee18fbf2`, parent `60a2e156`): this remains **record-cited only** in the loop-2 record (pre-fix removal-control leg, RE-DERIVE marked pending R2). The reply cites only the three pins above — no b6ff7dae. Nothing to resolve. Notes the graft (`b6ff7dae6f18…`) remains withdrawn in the record.

## Notes block

1. **C4 quote — byte-cited tweak required.** The reply's C4 quote reproduces the spec §7 row's opening clause but collapses the middle via ellipsis, deleting the "check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it" clause. That clause is the flagged contradiction's content. The runner must see the row's full sentence as written, contradiction flag intact, not a compressed paraphrase. Fix the head: reproduce `the pin is a second witness the summary does not author, and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it. The ledgers move with your rebase, KoNit-K's authorship kept, /pin stacked as its own commit.` — byte-for-byte, flag preserved.

2. **No other notes.** The ungated signature, the fix signature, the removal control, the hold-back clause, the three pins, the RED/GREEN/64-131-byte/control-green/success:true claims, the PARTIAL wake read with the six zero-hit anchors, and the session-rows-only write claim all match their receipts. The reply's run-cold claim (base-red at 268bb091, combined-green at a9c65dc4, single-add control green on all three pins) is exactly what the probe json shows.

## The pair's line

**Does this reply fulfill the ask for their lab?** It delivers a fully pre-registered, run-cold verification skeleton with exact execution receipts, an honest wake read, and all pins resolving — but the C4 quote truncates the flagged contradiction, so a lab runner would carry a softened bar (the vote-across-summaries clause would be silently dropped). Repair the quote byte-for-byte, then the reply fulfills the ask; otherwise the lab inherits a cleaner-looking but incomplete verification. The bar is passable; the quote needs one closing, not an ellipsis.

---
*Sources cross-walked: FB2-FAILING-CASE-SPEC-20261124.md §2–§6 (five elements, pins, signatures); FB2-EXECUTION-RECEIPTS-20261124.md + fb2-probe-out.json (RED False/64 B at 268bb091, GREEN True/131 B at a9c65dc4, 64+3+64, control green both, all success:true); SCHEDULED-WAKE-READ-20261124.md (PARTIAL, six zero-hit anchors, session-rows-only write); spec loop-2 verification record (0f602c5f cat-file commit; 268bb091 commit; a9c65dc4 commit; b6ff7dae record-cited; grafted 40-hex withdrawn); spec §7 row C4 text (byte-level compare). C4 thread row: working route `gh api repos/NousResearch/hermes-agent/issues/comments/7122688366` — endpoint reachable in the operator's route; the loop-2 record's 404 was a route artifact and is superseded.*
