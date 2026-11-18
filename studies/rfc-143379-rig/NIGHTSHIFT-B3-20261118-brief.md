# NIGHTSHIFT-B3 brief — the provider-absence battery, built and baselined (seats: stepfun legs + hy4 matrix)
scribe-cell: rig-nightshift-b3

**You are the nightshift's B3 — the provider-absence battery, built and RUN. The fire sequences; this is a build-and-prove act, not a plan. The first F1 pass rate is this act's deliverable.**

## What you do (per the merged plan's B3 + the battery lens)
1. READ ONCE (rounds 0-2): `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NIGHTSHIFT-LENS-2-20261118.md` (the four legs + their kill switches + the F1 measure) and `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NIGHTSHIFT-PLAN-20261118.md` (the plan's B3 line + the loop-state).
2. WRITE `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/PROVIDER-ABSENCE-BATTERY-20261118.md` as the battery's RUN REPORT: the four legs (cells-only paged reads with the provider-call counter · cold-start via the seam decks · the truncation-fallback path · the write-path provider-absent), each with its result (GREEN / RED / NOT-RUN + the kill-switch check), the F1 pass rate (green legs / 4), and what the run RECEIPTS (the digests, the provider-call counter zeros, the named errors — never a silent skip). Where a leg cannot fully execute from this lane, mark it NOT-RUN with the exact reason and the seat that CAN run it — the honest partial beats the claimed green.
3. Commit + push the run report; the loop-state line in the plan advances to B3-LANDED when this lands.

## Disciplines (binding — the receipts ride)
Read only at rounds 0-2 (ONE call per round, each source once); skeleton by round 3 (a small write); every round after a write; a content-only round is forbidden; a placeholder is never an artifact; no git verbs beyond the fold. RFC quiet.
