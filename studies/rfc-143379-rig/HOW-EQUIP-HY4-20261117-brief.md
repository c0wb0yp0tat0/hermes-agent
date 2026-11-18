# HOW-EQUIP-HY4 brief — research: equipping Hy4 flash for memo-grade deliverable production (seat: kenari beam-1-0:free)

**You are the research lane the operator dispatched inside the 00:00 UTC window.** The question, exactly: how do we equip **Hy4 flash** (tencent/hy4-flash:free — a reasoning model: 1M context, function calling, structured outputs, a `reasoning` field its replies carry) so it produces **memo-grade deliverables** — the caliber of the operator's regroup memo (the decision-first, receipted, hour-class, voice-readable document: no metadata, no apologetic framing, every claim traceable, ending in named opportunities)? The first ride produced a correct-but-thin artifact; the second ride must produce the deliverable the operator is aiming for, and the fleet must peak Hy4's performance in the process.

## The task
1. READ the target-caliber document to internalize the bar: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-MEMO-20261116.md` (its structure: envelope, how-to-read, one breath, parts, opportunities, read map; its register: complete punctuation, spelled-out measures, readable aloud) — then skim `HY4-FIRST-RIDE-ASSESSMENT-20261117.md` (what the first ride measured) and `NEMO-HY4-START-PLAN-20261117.md` (the plan the first ride executed).
2. READ the operator's own method for the fleet's knowledge-building rig: `/root/.hermes/skills/autonomous-ai-agents/think-tank/SKILL.md` (the mechanism-of-mechanisms spine: classify -> choose -> probe -> evaluate -> adopt or park -> standardize -> verify) and `/root/workspace/repos/mechanism-of-mechanisms` (the mechanism repo — read-only; do not invent mechanisms; label unresolved things CREATOR-GAP).
3. RESEARCH and DISTILL — from the mechanism repo and the study's own receipts — the concrete equipments that would let a reasoning model like Hy4 produce memo-grade work: staged composition (the multi-stage loop vs single-shot), the brief-envelope discipline, tool-call/self-verification cadence, reasoning-budget management (its thinking burns the 8192 cap), receipt discipline, and the operator's quality bars.
4. WRITE `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HOW-EQUIP-HY4-20261117.md`:
   - `## The bar` — the target-caliber document's properties, named from your read (not from memory).
   - `## The equipments` — the concrete techniques/mechanisms, each with: what it is, why it matters for Hy4 specifically, and how the fleet wires it (the stage, the seat, the receipt).
   - `## The multi-stage loop` — a concrete ACES think-tank loop design for Hy4: named stages (suggest: spine-assembly -> draft -> critique -> revision -> verification/assessment), each with its seat, its input/output, its exit gate, and where the scribe holds bytes.
   - `## The risks` — what could flatten the quality (reasoning-tail collapse, cap starvation, single-shot temptation, receipt drift) and the counter each.
   - `## The closing line` — one sentence: what equipping Hy4 is really about.

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 4); ≤6,000 chars per write; every claim about the target doc traceable to your read — where you did not read it, write "not confirmed". No commits, no pushes — the fold belongs to the head. When the artifact is complete, stop.
