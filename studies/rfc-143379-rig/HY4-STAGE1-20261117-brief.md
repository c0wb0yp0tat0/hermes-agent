# HY4-STAGE-1 brief — Hy4 flash's first ride, in the kit's substrate (tencent/hy4-flash:free)

**You are the test subject of a test within a test.** This is Hy4 flash's first task — planned into the kit's own machinery: read, write, a tool-call cycle, and an honest artifact. The harness is watching how a reasoning model runs in this substrate: your tool emissions must parse, your writes must land, your claims must trace.

## The task (kit-native — no web, no outside world; the file system and the study's own files are your whole surface)
1. READ `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-SPINE-20261105-1116.md` — the day-one section (the fifth of November, UTC). 
2. READ `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-MEMO-20261116.md` — its Part 1 day-one section.
3. VERIFY the day-one row count from the spine itself (count the day's rows as the record presents them — the count must be the rows' own, re-derived by your read, not quoted from the memo).
4. EXTRACT the first three landings of the day as the spine names them, each with its receipt id.
5. WRITE the artifact `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-ARTIFACT-20261117.md`:
   - one title line;
   - `## Day one, counted` — the verified day-one row count, stated with the rule you counted by;
   - `## The first three landings` — the three landings with their receipts;
   - `## The closing line` — one sentence: what Hy4 flash's first ride verified on its own read, or the exact words "not confirmed" for any claim the rows did not carry.

## Disciplines (binding)
One tool call per round. Write-first: a skeleton artifact by round 3. ≤6,000 chars per write; one section per write after the skeleton. The read-gate is the reason to KEEP WRITING: when a read returns, write the next section. Never guess a count — if the rows do not support it, write "not confirmed" and say why. No git commands, no commits, no pushes — the fold belongs to the head. No /root/.hermes writes; no network beyond the study's own surface. When the artifact is complete, stop.

## What the machinery will measure (not your concern — but know it is being watched)
Emission-format parsing on a reasoning model · tool-call pairing · the 8192 max_tokens cap's effect on your visible answer · rounds to land · the fold · cadence without silent gaps. Your job is the honest artifact; the harness's job is carrying you.
