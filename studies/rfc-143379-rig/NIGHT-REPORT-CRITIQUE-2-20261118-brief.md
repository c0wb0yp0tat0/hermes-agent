# NIGHT-REPORT-CRITIQUE-2 brief — the cold rubric critic, window-proof (seat: stepfun/step-3.7-flash:free)
scribe-cell: rig-night-run-critique

**This is the critic's re-fire under the two-way door. The prior fire ghosted: it tried to finish its reads after the write-window closed (rounds 4+ are read-gated until the artifact exists) and never wrote. Your discipline is time-boxed reads, then write.**

## The read plan (binding — reads happen ONLY in rounds 0-3; the window closes at round 4 and nothing after is free)
- Round 0: read `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/THE-NIGHT-REPORT-20261118.md` (the draft, about 23,600 bytes — the tool returns a truncated view; that is the WHOLE view you get; accept it).
- Round 1: read `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/RIG-NIGHT-RUBRIC-20261118.md` (the six checks).
- Round 2: one more read, your choice: a second pass at the report's tail if the first view was cut, or the exemplar's opening (`HITL-MEMO-20261116.md`) for the temperature sample. Choose the tail if you did not see it; mark what stays unseen as not confirmed.
- Round 3: WRITE your skeleton (the six checks + the verdict line). From round 4 the window is open: every further round is a write round. No more reads after round 3.

## The verdict artifact: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NIGHT-REPORT-CRITIQUE-20261118.md`
- `## The checks` — the six (listen, stranger, temperature, voice, facts, ask), each PASS or FAIL with at least one quoted line from the report as evidence, and the rewrite the revision should make for any FAIL.
- `## The length question` — the draft is about three thousand nine hundred words against a brief target of five to eight thousand. Verdict with both sides named; name which sections could honestly take more.
- `## Not-confirmed` — anything the truncated view hid, listed plainly.
- `## The strongest lines` — three sentences that would survive a reader's highlight, quoted.
- `## The verdict` — one line: PASS / PASS-WITH-DELTAS / FAIL.

## Disciplines (binding)
One tool call per round; ≤6,000 chars per write; every verdict carries a quoted line; write rounds only after round 3; no git verbs; stop when complete. The harness folds, the scribe holds the bytes, and the revision stage waits on your deltas.
