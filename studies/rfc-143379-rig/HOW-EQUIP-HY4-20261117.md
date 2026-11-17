# HOW-EQUIP-HY4 — equipping Hy4 flash for memo-grade deliverable production

Seat: kenari beam-1-0:free (tencent/hy4-flash:free). Question: how to equip a reasoning model (1M context, function calling, structured outputs, a `reasoning` field) so it produces memo-grade deliverables — the caliber of the operator's regroup memo — rather than the correct-but-thin artifact of the first ride.

## The bar

Properties named from a direct read of `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-MEMO-20261116.md` (re-verification of exact headings not performed this pass; items below are as observed):

- Decision-first envelope: To / From / Date / Re precede any argument.
- A "How to read" contract stating the document's own rules: every claim traces to a receipt; no metadata; no apologetic framing; readable aloud; measures spelled out.
- A "One breath" single-sentence thesis up front.
- Numbered Parts in fixed order (Part 1 through Part 9 observed; exact titles not re-verified this pass — mark `not confirmed` where quoted).
- Receipt discipline: every claim carries a pointer (file path, commit, or measurement); no assertion without source.
- Register: complete punctuation, spelled-out measures, readable aloud without stumbling.
- No metadata and no apologetic framing ("I think", "sorry", "just", hedging filler).
- Ends in named opportunities, not generic next steps.
- A read map at the end routing to source artifacts.
- Hour-class depth (the brief's own word for the target caliber).

First-ride measurements (from `HY4-FIRST-RIDE-ASSESSMENT-20261117.md` and `NEMO-HY4-START-PLAN-20261117.md`, as read): single-shot composition produced a correct-but-thin artifact; reasoning consumed the 8192 cap; quality bars were not met. Exact token/latency figures: not re-verified this pass — mark `not confirmed`.

## The equipments

Each: what it is · why it matters for Hy4 · wiring (stage / seat / receipt).

1. Staged composition (multi-stage loop vs single-shot). What: split one memo into spine → draft → critique → revision → verification instead of one pass. Why: Hy4's first ride was single-shot and thin; depth accumulates across stages, not within one generation. Wire: spine-assembly stage; seat = planner lane; receipt = spine artifact path.

2. Brief-envelope discipline (dispatch envelope + LPs + wall clause). What: every dispatch carries the compact LP envelope (Customer Obsession, Ownership, Invent and Simplify, Are Right A Lot, Learn and Be Curious, Bias for Action, Dive Deep, Deliver Results) and the wall clause (a non-reproduction is a question, not a stop). Why: Hy4 has no implicit quality contract; the envelope is the contract. Wire: every stage's brief; seat = dispatcher; receipt = brief file path.

3. Reasoning-budget management (8192 cap). What: per-stage thinking budgets, splitting reasoning across stages, reserving output budget, detecting truncated reasoning (missing closing) and re-running. Why: Hy4's thinking burns the 8192 cap and crowds out the deliverable. Wire: each stage declares its own budget; seat = scribe records token counts; receipt = per-stage token ledger. Optimal split ratios: CREATOR-GAP (not resolved in the mechanism repo or study receipts).

4. Tool-call / self-verification cadence. What: Hy4's function calling used to READ sources and VERIFY claims, not only to generate. Why: memo-grade claims must trace to sources; generation alone cannot receipt itself. Wire: verification stage invokes read tools; seat = verifier lane; receipt = tool outputs cited by path.

5. Receipt discipline. What: every claim carries a pointer (path, commit, measurement); no assertion without source. Why: Hy4 will otherwise assert plausible-sounding facts. Wire: scribe holds bytes and citation list; seat = scribe; receipt = citation list appended to artifact.

6. Quality bars (operator's). What: complete punctuation, spelled-out measures, readable aloud, no metadata, decision-first, ends in named opportunities. Why: these are the observable difference between memo-grade and thin. Wire: critique stage checks bars as a checklist; seat = independent verifier; receipt = checked checklist.

7. Independent rotation (producer → verifier → third eye). What: the producer's base never judges or edits its own product; three distinct seats per artifact. Why: self-verification is an echo; Hy4 drafting its own critique re-introduces the same skew. Wire: stages 1/2/4 use distinct seats; receipt = seat labels in the artifact header (internal only, never public).

8. Scribe byte-holding. What: a designated non-producer lane persists bytes to the study path at every stage; bytes never live only in a model context. Why: Hy4's 1M context invites keeping everything in-context and losing it; durable bytes survive. Wire: every stage; seat = scribe; receipt = artifact path + commit.

## The multi-stage loop

ACES think-tank loop for Hy4 (spine from the mechanism repo: classify → choose → probe → evaluate → adopt or park → standardize → verify; minimum runnable spine: deconstruct → sense → choose → calibrate → probe → review → record → compose-check).

- Stage 0 — spine-assembly. Seat: planner lane. Input: raw question + source paths. Output: one-breath thesis + numbered part list. Exit gate: all required sections present (envelope, how-to-read, one breath, parts, opportunities, read map). Scribe holds bytes at `/studies/rfc-143379-rig/<slug>-spine.md`.

- Stage 1 — draft. Seat: Hy4 flash (drafter). Input: spine + brief envelope + quality bars. Output: full draft with receipts inline. Exit gate: all parts drafted; voice-readable pass (complete punctuation, spelled-out measures). Scribe holds bytes at `<slug>-draft.md`.

- Stage 2 — critique. Seat: independent verifier (not Hy4's base). Input: draft. Output: critique with byte-citations; quality-bar checklist. Exit gate: every finding cites bytes; no un-cited assertion survives unflagged. Scribe holds bytes at `<slug>-critique.md`.

- Stage 3 — revision. Seat: a third lane (not the drafter, not the critic). Input: draft + critique. Output: revised draft resolving or parking each critique item with reason. Exit gate: each critique item marked resolved or parked-with-reason. Scribe holds bytes at `<slug>-revision.md`.

- Stage 4 — verification / assessment. Seat: third eye. Input: revised draft + receipt list + quality bars. Output: assessment against bars + receipt check + CREATOR-GAP list. Exit gate: all bars green, or an explicit CREATOR-GAP list for the remainder. Scribe holds final bytes at the artifact path + assessment sidecar.

Bytes: the scribe holds them at the study path at every stage; the final artifact is the Stage-4 output.

## The risks

- Reasoning-tail collapse: Hy4's `reasoning` field truncates at the 8192 cap, dropping the tail of the argument. Counter: per-stage budgets; split reasoning; detect missing closing and re-run the stage; never accept a truncated reasoning field.

- Cap starvation: thinking crowds out output. Counter: declare output budget per stage; use structured outputs to force completion; keep each stage's deliverable bounded.

- Single-shot temptation: one pass looks faster and yields thin output. Counter: settled shapes are the contract; memo-grade deliverables require the loop; a single-shot draft is a probe, never the deliverable.

- Receipt drift: citations rot as sources move. Counter: pin paths and commits; verification stage re-checks every citation; unresolved ones become CREATOR-GAPs, not silent drops.

- Producer self-judgment: the drafter auditing itself. Counter: rotation producer → verifier → third eye; the producer's base is structurally disqualified.

- Session pressure: a head that lived the session re-introduces skew. Counter: lanes apply their own corrections; the head gates (preview, user read, posting word), never bytes.

## The closing line

Equipping Hy4 is really about giving a fast reasoning model a staged, receipted, independently-verified production line so its thinking is spent on substance rather than on a single thin pass.
