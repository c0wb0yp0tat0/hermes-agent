# HY4-ACES-LOOP leg C — runner tooling, the A/B, and the firing map (seat: kenari beam-1-0:free)

**You are fleet planning leg C — a PARALLEL planning lane for the ACES think-tank loop that equips Hy4's redo.** Your dimension: the RUNNERS THEMSELVES — which matrix seats reliably carry which loop stages (tool-call fidelity), the Kenari beam-vs-dots A/B, the scribe cell map, and the exact firing commands for the runner-rotated loop.

## Read first
1. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HOW-EQUIP-HY4-20261117.md` — the Kenari research (the equipments; the CREATOR-GAP on split ratios).
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-FIRST-RIDE-ASSESSMENT-20261117.md` — ride 1's measurements (emission parsing PASS, read-gate defect now FIXED in the harness, token-cap behavior).
3. If `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-20261118.md` exists when you read (leg A, longcat, running in parallel), ALIGN with it.

## Produce `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-ACES-LOOP-PLAN-C-20261118.md`:
- `## The seat map` — per loop stage, the recommended runner: the seat, its known behavior (from the research + ride-1 receipts), and why; the tool-heavy stages (critique, verification) go to the seats with the steadiest tool-call fidelity.
- `## The beam-vs-dots A/B` — the Kenari comparison design (beam-1-0:free vs dots-3-note-preview:free): the micro-task, the degraded run, the pass bar, and where the winner slots into the loop. Zero cost, both free.
- `## The scribe cell map` — the named cells the loop uses (`rig-hy4-loop-*`), which stage writes which cell, and the byte-identity check at each handoff.
- `## The firing map` — the exact harness commands, stage by stage (model id, brief path, artifact path, rounds, logfile), in launch order, with the gate between stages.
- `## The closing line` — one sentence.

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 4); ≤6,000 chars per write; claims trace to reads ("not confirmed" where not). Commit + push the artifact when complete (the git verbs work from the study repo), then stop. RFC quiet.
