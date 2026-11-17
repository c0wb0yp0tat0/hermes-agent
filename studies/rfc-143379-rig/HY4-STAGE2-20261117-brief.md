# HY4-STAGE-2 brief — blind verification of Hy4's first-ride artifact (seat: upstage/solar-mini4:free)

**You are the blind verifier — a SEPARATE seat, isolated by design. You did not compose the artifact; you check it. Evidence, not reasoning: your verdicts come from the files, never from what the artifact claims about itself.**

## The task
1. READ `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-SPINE-20261105-1116.md` (the day-one section, `## 2026-11-05`, UTC). This is the ONLY source of truth for day one.
2. READ the artifact under test: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-ARTIFACT-20261117.md` — a first-ride lane's composition claiming: (a) day one holds 24 rows; (b) the first three landing rows are FLEET-LANDING `longcat` (`issuecomment-6667376392`), ALIGNMENT-LANDING (`issuecomment-6667398149`), FLEET-LANDING `beam` (`issuecomment-6669005033`); (c) the phrase "thirty-two landings" is not confirmed by the rows.
3. VERIFY, cold, against the spine alone:
   - **The count**: re-derive day one's row count yourself — state the rule you counted by (what counts as a row, what is excluded) and the total.
   - **The three landings**: each of the artifact's three rows must exist in the spine with the EXACT receipt id the artifact named. Also check the artifact's parenthetical trio (`beam`, `solar-mini4`, `1d70408531` / `issuecomment-6669119589`) — do those rows exist as named?
   - **The not-confirmed framing**: does the spine anywhere show 32 as a day-one count? If not, the artifact's not-confirmed verdict stands; if yes, it fails.
4. WRITE `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-VERIFIED-20261117.md`:
   - One title line.
   - `## Verdict` — PASS or FAIL per claim (a/b/c), each a line with the re-derived evidence.
   - `## The count, my way` — your own rule + your own total, and the agreement/disagreement with 24.
   - `## Receipts checked` — the ids you found vs the ids the artifact named.
   - `## The closing line` — one sentence: what the first ride's claims survived on the record's own rows.

## Disciplines (binding)
One tool call per round. ≤6,000 chars per write; write-first by round 3. Never assert an id you did not read in the spine; where a claim cannot be checked, write "not confirmed" with the reason. No git commands, no commits, no pushes — the fold belongs to the head. When the verdict artifact is complete, stop.
