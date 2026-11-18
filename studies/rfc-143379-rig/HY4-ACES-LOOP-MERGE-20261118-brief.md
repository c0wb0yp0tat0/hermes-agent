# HY4-ACES-LOOP-MERGE brief — the coordinated synthesis of legs A, B, C into THE canonical loop plan (seat: mistralai/mistral-nemo, paid)

**You are the MERGE lane — the planning stage's coordination point, and the last planning step before Hy4 rides.** The operator's standard: true synergy, not stitching — the three fleet legs planned their dimensions under one mission; you reconcile their outputs into ONE canonical plan the firing stage obeys. You do not invent; you reconcile by evidence. Where the legs conflict, you resolve by the evidence (the receipts, the research, the memo), and you NAME each resolution in your artifact.

## Your inputs (read all four)
1. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HOW-EQUIP-HY4-20261117.md` — the Kenari research (the equipment base).
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-20261118.md` — leg A (longcat): the loop's main design (stages, gates, cells).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-B-20261118.md` — leg B (solar): the board, runner rotation, executable gates, the 9-item quality-bar checklist.
4. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-C-20261118.md` — leg C (kenari beam): NOTE — leg C landed as a TBD SKELETON (267 B); its intended dimensions (seat map, the beam-vs-dots A/B, scribe cell map, firing map) must be RECOVERED from its brief (`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-C-20261118-brief.md`) and from legs A and B, which already carry the firing map, the board/rotation, and the scribe cells. Do not treat C's TBDs as gaps the plan lacks — recover and reconcile.

THE HARNESS'S TRUE COMMAND FORMS (leg C could not locate them; do not repeat the hunt):
- Standard ride: `python3 /root/scripts/copycat-harness.py --model <id> --brief <path> --artifact <path> --rounds <n> --logfile <path>`
- Kenari rides additionally export: `HARNESS_ENDPOINT=https://kenari.id/v1/chat/completions` and `LM_API_KEY=$KENARI_API_KEY` (read from `/root/.hermes/.env`).
- Model ids verified live: hy4 `tencent/hy4-flash:free` (Nous endpoint) · solar `upstage/solar-mini4:free` · stepfun `stepfun/step-3.7-flash:free` · longcat `meituan/longcat-2.5:free` · kenari `beam-1-0:free` (dots candidate: `dots-3-note-preview:free` — id seen in kenari's catalog, not yet probe-verified, mark NOT-CONFIRMED until probed).

## The merge contract (binding)
- ONE canonical artifact: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-FINAL-20261118.md` with sections: `## The loop` (named stages, each with seat, input, output, exit gate — reconciled across legs), `## The board and rotation` (the seat map CORRECTED to the true seats: Hy4 = tencent/hy4-flash:free — leg B's table mislabeled it solar-mini4; pin every seat to its real model id), `## The firing map` (one exact harness command per stage, sequential, from leg C reconciled against A's gates), `## The scribe cells`, `## The peaking measurements`, `## The conflicts resolved` (each conflict: the two positions, the evidence that settled it), `## Open items` (CREATOR-GAPs and anything unverifiable).
- CONFLICT PROTOCOL: disagreement between legs -> resolve by the evidence (the research, the memo, the receipts); if the evidence cannot settle it, it becomes an OPEN ITEM, never a silent pick.
- Nothing in the final plan may name a seat without its model id; nothing may promise a capability the harness has not shown (no web tools, no unbounded outputs).

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 3); ≤6,000 chars per write; claims trace to the four inputs ("not confirmed" where not). Commit + push the final artifact (git verbs from the study repo), then stop. RFC quiet.
