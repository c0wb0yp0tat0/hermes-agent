# HY4-ACES-LOOP — leg B: critique/verification wiring + runner rotation

Seat: upstage/solar-mini4:free. Parallel planning lane for the ACES think-tank loop that equips Hy4's redo. Leg B holds the board (who critiques, who verifies, seat rotation, gates), not the model wiring. The plan is the loop's governance wiring: producer never judges its own product; every stage exits through a byte-checked gate; the fleet rotates through seats per ride.

## The board

The board is a three-seat, fixed-rotation council. One artifact is drafted, critiqued, revised, verified by three distinct seats. The producer's base is structurally disqualified from judging its own product — self-verification is an echo, not a check — and the rule is explicit in every brief.

| Seat | Role in the loop | Drafted? | Critiqued? | Revised? | Verified? |
| ---- | ----------------- | -------- | ---------- | -------- | --------- |
| Hy4 (solar-mini4) | Draft stage 1 (drafter) | Yes | — | — | — |
| Independent verifier | Critique stage 2 (byte-citation checks) | No | Yes | — | No |
| Third eye | Revision stage 3 + verification stage 4 | No | No | Yes | Yes |

Seat rotation is not a per-stage shuffle; it is a per-ride rotation of the *fleet*, while the board's three seats stay fixed on the same artifact path: stage 1 = Hy4's base; stage 2 = independent verifier's base (never Hy4's); stage 3+4 = a third seat not used at drafting. In leg B the runner seats rotate through stages across rides, so stage re-use is impossible by construction, not by hope.

Rule (board's standing clause): a base that drafted an artifact may not sign its critique, revision, or verification of that artifact; the writer's seat is the first door closed to the writer's base.

## The runner matrix rotation

Fleet fates the loop's five stages (spine-assembly, draft, critique, revision, verification) each ride. No stage re-uses a seat that drafted that stage on the same artifact. The rotation is staged across the loop's campaign rounds.

| Stage | Draft seat (primary) | Critique seat | Revision seat | Verification seat |
| ----- | -------------------- | ------------- | ------------- | ----------------- |
| 1 Spine-assembly | planner lane (kenari beam) | — | — | — |
| 2 Draft | Hy4 flash (upstage/solar-mini4) | independent verifier (not Hy4's base) | third eye | third eye |
| 3 Critique | — | independent verifier | third eye | third eye |
| 4 Revision | — | — | third eye | third eye |
| 5 Verification | — | — | — | third eye |

Concrete rotation schedule (per campaign round):
1. Round 1: Hy4 drafts, independent verifier critiques, third eye revises + verifies.
2. Round 2: a different fleet seat (e.g., kenari beam or stepfun) drafts the next artifact; Hy4 (the first drafter) sits on its critique as the independent verifier only where the brief permits, otherwise excluded. The drafting seat is always a new base.
3. Round 3: a third fleet seat drafts; the two earlier seats rotate into verify seats, never re-drafting their own product.
4. Rides repeat: each new artifact gets a fresh rotation of the fleet; Hy4 never signs its own critique/revision/verification, and the seat that drafted a stage never touches the next stage's output as that stage's judge.

Scribe byte-holding is the scribe's lane (stage-agnostic): a designated non-producer path persists bytes at every stage, so the draft, critique, revision, and final artifact all live on the study path with commit receipts. The runner rotates; the scribe holds.

## The gates

Every stage exits through a gate that is executable — a byte-citation, a checklist pass, or a re-derived count, named per stage. A gate that cannot be checked is not a gate.

| Stage | Exit gate | Check |
| ----- | --------- | ----- |
| 0 Spine-assembly | Envelope complete: To/From/Date/Re precede argument; "How to read" contract present; one-breath thesis present; parts 1–9 in fixed order; opportunities named; read map present. | Byte-citation of each section against spine artifact path; re-derived count of sections = 9 (or pinned count) |
| 1 Draft | All parts drafted; voice-readable pass (complete punctuation, spelled-out measures, no stumble); delivered within per-stage output budget (no truncation from 8192 reasoning cap) | Full text read of draft; token ledger recorded; reasoning field closes with a tail |
| 2 Critique | Every finding cites a byte (path + anchor); no un-cited assertion survives unflagged; quality-bar checklist itemized with per-item verdicts | Re-run the checklist against the draft bytes; every citation resolves to a path+byte range |
| 3 Revision | Each critique item marked resolved or parked-with-reason; no new un-cited assertion in revision | Diff cited: every change traced to a critique item; re-check of citations in revision |
| 4 Verification | All quality-bar items green, or an explicit CREATOR-GAP list for the remainder; receipt list fully resolved or listed as GAP; final artifact + assessment sidecar committed | Byte-citation of final artifact; independent re-read of bars; receipts re-derived, none silently dropped |

Gates are not advisory: a stage that cannot pass its gate is re-run (re-run the draft rather than patch), and a stage that cannot be checked is returned as an explicit CREATOR-GAP list rather than a silent pass.

## The quality-bar checklist

Executable critique checklist, from the operator's memo properties, in order of the "How to read" contract.

1. Decision-first envelope: To / From / Date / Re precede any argument. (check: header bytes present before body)
2. "How to read" contract: every claim traces to a receipt; no metadata; no apologetic framing; readable aloud; measures spelled out. (check: contract section present + sample claim traceable)
3. One-breath single-sentence thesis up front. (check: exact one-sentence present in opening block)
4. Numbered Parts in fixed order (Part 1 through Part 9). (check: part markers in order, count pinned)
5. Receipt discipline: every claim carries a pointer (file path, commit, or measurement); no assertion without source. (check: monospace citation list attached; all citations resolve to byte ranges)
6. Register: complete punctuation, spelled-out measures, readable aloud without stumbling. (check: read-aloud pass; per-measure spelled out)
7. No metadata and no apologetic framing ("I think", "sorry", "just", hedging filler). (check: scan for flagged tokens)
8. Ends in named opportunities, not generic next steps. (check: opportunities section names ≥2 named opportunities with named record references)
9. Read map at the end routing to source artifacts. (check: read map present with each route pointing to a path+anchor)

The checklist is the critique stage's executable contract: each item gets a green/amber/red verdict with a byte range for every red; the itemized checklist is committed to `<slug>-critique.md` as the gate's receipt.

## The closing line

The loop's board is fixed (drafter, independent critic, third-eye verifier), the runner matrix rotates through the five stages so no stage re-uses a producer's base, and every stage exits only through a byte-checked gate — a memo-grade artifact is one the board could have disagreed with and could not.
