# HY4-ACES-LOOP-PLAN brief — the fleet plans Hy4's redo, multi-stage, think-tank method (seat: meituan/longcat-2.5:free)

**You are the fleet's ACES think-tank PLANNING lane — the mission's second stage.** The operator's mission, verbatim: the gist Hy4 made based on Nemo's plan lacked the quality asked for (compared with the regroup memo). The remedy: (1) Kanari researched how to equip Hy4 (`HOW-EQUIP-HY4-20261117.md`, committed `753ead5dd4`) — DONE; (2) THE REST OF THE FLEET takes that research and PLANS an ACES think-tank loop — **multi-stage for Hy4 to take on** — so Hy4 produces the memo-grade deliverable and the fleet PEAKS Hy4's performance in the process. You are stage 2. The head fires stage 3 (Hy4 running the loop) when your plan lands.

## Read first (all in the study realm)
1. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HOW-EQUIP-HY4-20261117.md` — the Kenari research (your primary input: the equipment list, the bar, the risks).
2. `/root/.hermes/skills/autonomous-ai-agents/think-tank/SKILL.md` — the mechanism-of-mechanisms spine (classify -> choose -> probe -> evaluate -> adopt or park -> standardize -> verify) and the rig's knowledge-building contract.
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-MEMO-20261116.md` — the CALIBER BAR: the deliverable Hy4 must match (structure, register, receipts, no meta, opportunities).
4. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-FIRST-RIDE-ASSESSMENT-20261117.md` — ride 1's measurements (including the read-gate defect now fixed in the harness — the loop must assume the fix is live).
5. The scribe route: the store at `http://127.0.0.1:24282` (POST /save_memory, /get_memory — `memory_name` + `content`); the loop's cells should be named `rig-hy4-loop-*`.

## What your plan artifact must contain (`HY4-ACES-LOOP-PLAN-20261118.md`)
1. **The loop** — named stages (suggest the family: spine-assembly -> draft -> critique -> revision -> verification -> landing; adjust with the research's evidence), each with: the stage's seat (Hy4 itself vs a matrix seat vs the Kenari beam-vs-dots A/B), the input, the output artifact, the EXIT GATE (what must be verifiably true for the stage to pass), the scribe cell holding its bytes, and its receipt.
2. **The peaking plan** — how we MEASURE Hy4's performance rising across stages (the critique's deltas landing in revision, recipe/register adherence, receipt accuracy vs the spine, visible-answer length under the reasoning cap) — measurement named per stage, not vibes.
3. **The board wiring** — who critiques (a seat that did NOT draft), who verifies (isolated), seat diversity, the blind doctrine.
4. **The firing brief** — EXACT harness commands, stage by stage (model id, brief path, artifact path, rounds, logfile), launch order sequential, with the loop-state line `CONTINUE + Hy4 rides when the plan lands`.
5. **Risks + refusals** — the flattening risks (single-shot temptation, cap starvation, register drift, receipt drift) with named counters; anything the research flagged as a CREATOR-GAP stays a gap.

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 4); ≤6,000 chars per write; claims trace to your reads (where not read: "not confirmed"). No commits till the artifact is complete, then commit + push (`HY4-ACES-LOOP-PLAN-20261118.md` on the study branch), then stop. RFC quiet; no /root/.hermes writes.
