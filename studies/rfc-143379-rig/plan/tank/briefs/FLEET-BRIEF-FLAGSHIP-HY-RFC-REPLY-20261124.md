# FLEET-BRIEF FLAGSHIP-HY — THE RFC REPLY COMPOSER (the promised test, delivered on the thread)

*Seat (pin): `tencent/hy4-flash:free` — the FLAGSHIP, the reply composer. The operator's words: "This doesn't read as our follow up for kvnloo. It should read as a rfc reply that's actually useful to them and their lab by fulfilling the ask and that its max value add." The REPLY is the promised test itself — the FB-2 failing-case spec in thread form, self-contained, runnable by kvnloo's lab from the comment alone. It is NOT the pair's narrative (the previous gist's arc was the pair's, not theirs). It is NOT posted — it is prepared as the RFC reply's body, staged for the operator's word. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission

Compose the RFC reply — a thread comment to @kvnloo / their lab — that fulfills the ask exactly as promised at row 7122688366: the expected failure signatures for the ungated add on main and the same case on the fix, the removal control, the hold-back class, at pinned SHAs; the scheduled-wake read landing with it. The lab must be able to run the whole pre-registration from YOUR reply alone, cold, at the pins, with the bars fixed before the run and divergences as data.

## The source material (READ these three, quote from them — never re-derive, never paraphrase the bars)

1. `studies/rfc-143379-rig/plan/tank/FB2-FAILING-CASE-SPEC-20261124.md` — the run-cold spec (148 lines, folds `8453c59adc` + `aced3e1cf7`). ITS SECTIONS ARE THE REPLY'S BODY: §2 the ungated-add procedure + RED signature (`268bb091:615` whole-file write, `FIRST_SURVIVED_SECOND_ADD=False`); §3 the fix arm + GREEN signature (three fix arms + the `:911` delimiter join, `=True`); §4 the removal control (single-add on all three pins, green; a red control invalidates the probe); §6 the pinned SHAs (all now verified — `0f602c5f` full form `0f602c5f6f18615632535251d62a2db74ce93b69`, `268bb091…`, `a9c65dc4…`); §7 the four acceptance rows with C4's verbatim.
2. `studies/rfc-143379-rig/plan/tank/FB2-EXECUTION-RECEIPTS-20261124.md` — the promised test ALREADY RUN on our side: A RED 64 B `False` at `268bb091` · B GREEN 131 B `True` at `a9c65dc4` · C control green both. The reply may TELL the lab this — we pre-ran our own pre-registration so their run is a confirm, not an exploration.
3. `studies/rfc-143379-rig/plan/tank/SCHEDULED-WAKE-READ-20261124.md` — the companion: PARTIAL verdict — the wake reads `state.db`/`state.py` and writes its own session rows, but zero hits on every memory-store anchor (`memory_tool`, `store.add`, `_add_doc`, `preserve_session`, `DreamCycle`, `write_gate`); the memory-store write path is untouched.

## The reply's shape (register: useful to their lab; the operator's own register per gist-formatting-match)

- **Open for them, not for us:** address the lab and its question, not the fleet's arc. No "the fleet," no "the loops," no kaizen story, no pair-metadata. The story is the test's delivery.
- **Bold header beats, lab-useful:** `**the pre-registration**` (the five elements as bars) · `**the pins**` (the table, all verified, full forms where abbreviated) · `**the signatures**` (RED arm procedure + expected observation; GREEN arm procedure + expected observation; the control) · `**the acceptance rows**` (C1–C4 with C4's verbatim quoted from their own row) · `**the wake read**` (the PARTIAL verdict with the zero-hit anchors) · `**the ask back**` (what THEIR run confirms: base-red / combined-green / single-add removal control at the pinned SHAs; divergences are data, not renegotiation).
- **The hold-back, by clause only:** ONE class is withheld so a leading hint cannot satisfy the probe on its own; the class is named as existing, never by content or hint. (Their C4 accepted this — "the hold-back class" is their word too.)
- **The receipts ride in:** the run receipts may be cited as already-executed on our side (the `FB2-EXECUTION-RECEIPTS` numbers), so their lab runs a confirm.
- **Em-dash cadence, one per sentence; short declaratives; the "the X" frames.**
- **NO metadata:** no "this reply," no staging, no "the pair," no "study landing," no "more to come" — end on the ask back (what their run confirms + divergences are data).
- **Length:** a thread comment's worth — comprehensive but scannable; every bar it carries is the spec's own wording, tightened for the thread.

## The required artifact — THE REPLY BODY

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-RFC-REPLY-20261124.md`

1. The reply as the thread comment's body (the gist's deliverable).
2. Every bar quoted or tightened from the spec's own wording; every pin verified; C4's verbatim carried; the hold-back by clause only; the wake read's verdict with its anchors.
3. Then verify YOUR OWN reply: re-read it from disk; confirm the five elements present in runnable form; confirm the pins; confirm the hold-back clause-only; confirm zero pair-metadata; confirm the register (for their lab, not for us); commit.

## Write-window

`write-window: 12` — read the three sources FIRST (rounds 1–8), the reply's skeleton by round 11, deepening after. The gated-read trap is known; write early.

## The hard lines (binding)

- This reply is PREPARATION. It is NOT posted — the RFC #143379 surface stays QUIET until the operator's word; kvnloo's door stays closed; the PR #1 thread's rows are the head's alone. The gist it births rides the same rule.
- The hold-back's content is NEVER written into the reply — clause only.
- No installs. All reads LOCAL (git / read_file at the study tree).
- `git add` + `git commit` locally — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only). The branch is shared — `ls-remote` first, per fold.
- Never `git checkout --`, never `git stash`, never `git rm -rf`.

## The emission contract

Exit 0 = the reply EXISTS at the artifact path (written, re-read, receipt-verified), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause) · gist-formatting-match (the register rules above are that skill's, applied) · investigation-documentation (every claim's receipt is a handle).

**Refused:** any posting/write to public surfaces · any install · web reads · memory-chain appends · config/gateway changes · source edits · github-* write verbs · coding legs · fan-outs · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the operator's follow-up to kvnloo — max value to their lab: runnable cold from the thread alone.
- **Ownership:** the reply is yours until it is on disk, re-read, receipt-verified, committed.
- **Invent and Simplify:** one comment, five elements, all bars fixed.
- **Are Right A Lot:** disconfirm every number before it rides — the 64, the 131, the True/False, the pins.
- **Bias for Action:** the sources are folded and local; compose now.
- **Dive Deep:** quote the spec's bars; never soften a bar for the thread.
- **Deliver Results:** the promised test, delivered in reply form.

**THE WALL CLAUSE:** a non-reproduction (a bar that won't trace to the spec, a pin that won't resolve) is a QUESTION with a constructed minimal move — the sibling file, the commit's show, the raw json — before any verdict. A real wall lands with its receipts, named as a finding. And a bar that does NOT match the spec's wording is the catch, not the tightening — the tightenings are for the thread's read, the bars are the spec's own.
