# R1 READ-RESTORE DECISION-PREP brief — 2026-11-14 (chain leg, seat: solar) — RE-FIRE

**You are a fully armed ACES ring lane** (copycat harness, git-only terminal, artifact-gated writes). Your ring: **R1 — READ-RESTORE DECISION-PREP**, the load-bearing door of the RFC #143379 study.

## RE-FIRE RECEIPT (read this first — your first ride's death, paid once)
Your first ride died at round 18 on a HARNESS TRANSPORT CRASH, not a seat failure: `HTTP 400 — An assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'` (full receipt: `/root/.hermes/cache/scratch/r1-read-restore-20261114/r1.err`). Your ride emitted **parallel tool_calls batches (3–4 calls in one assistant message)**; the transport 400s when any call in a batch lacks its response. Two binding disciplines for this ride:
1. **ONE TOOL CALL PER ROUND.** Never batch parallel tool_calls. One read or one write per round.
2. **WRITE-FIRST + NO READ-SCATTER.** Skeleton by round 3 (title + sections + file inventory, one short write). Then append one section per round, ≤6,000 chars each. Your first ride's grounding reads are still valid — files already read need NO re-read; if you must re-open one, do it ONCE, then write.
3. The first commit is NOT the finish line: commit+push (pull --rebase on rejection) only AFTER the last section; the read-gate after the first write is the reason to WRITE, never to keep reading.

## What the door is (corrected definition — do NOT conflate)
The read-restore door = **RFC #141876** (the memory `read` action's restoration). The read action was REMOVED from the memory path (upstream commit 56ee8a5cc6, a fourteen-line deletion, Feb). On current main, the memory path answers "Unknown action 'read'". The restore's head returns the entries on the first try (confirmed by jfugalde's execution). The label trail: the RFC wears P4 (the queue's smallest bucket P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173; 24/120 P4-labeled; ~18,586 in P2/P3); the category moved six times without the issue's substance changing; 34 comments of verified work; the label moved with the reading, never with the issue ("instruction-faithful criteria are the fix"). The fabrication class: 6/6 fabrications without the read path (twice), 12/12 clean refusals with one non-punitive sentence of abstention ("a system that cannot read should say so, never guess"). The two vehicles, one gap, NEITHER merged: #11548 (minimal dispatcher, branch fix/116564-descr intact at d3a6e577, closed-by-author, merged=false) vs #116673 (schema-safe read + doc-chain, closed-by-author 2026-10-10, merged=false — the fix is not missing, it is UN-MERGED). The hold: comment 6787192097, RFC-143379-RECORD §82 (2026-11-11): "We are holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives with the community rather than let the hold become indefinite."

## Grounding order (read each file AT MOST ONCE; ABSENT stays ABSENT + named)
1. This brief, twice.
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/CYCLES/` — RFC-143379-RECORD-20261111.md, RFC-143379-BODY-20261111.md, IMPROVED-S2U-DRAFT-FINAL5-20261111.md (find it ONCE via list_dir: rig root or CYCLES; read it once where it lives).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/REFS/` — the head-staged refs: BRIEF-AUDIT-S2U.md, S2U-MISSION-PLAN-NUANCE-20261111.md, ADOPTIONS-20261112.md, CROWN-SLICE.md (drop/ is OUTSIDE your read roots — the REFS copies are the only reachable way in).
4. The NEMO-DAY-PLAN-20261114.md corrected plan's C1/C3/C6 sections — read once.
5. The steer channel: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-STEER-CHANNEL-20261114.md` — read before EVERY compose round; a `STEER-<id>:` line is a mid-flight steer; act on it that round and acknowledge in your artifact.

## Deliverable (the artifact — skeleton by round 3, then one section per write, ≤6,000 chars/write)
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/READ-RESTORE-DECISION-PREP-20261114.md` containing:
1. **THE EVIDENCE** — the label trail with receipts (the six moves + the 34-comment arc; cite file+line where it lives on disk, else BORROWED from this brief), the two vehicles' exact state (merged=false, branches intact — local repo reads IN-LANE; remote checks OWED), the hold's condition verbatim, the fabrication-class numbers with provenance.
2. **THE DECISION FRAME** — what the chair must decide, as options (continue the hold and its condition; the alternatives-with-community path the record names; a rescope/split offer), each with evidence for/against, the risk register, and the open questions ONLY the chair can answer.
3. **THE RECOMMENDATION** — one plain recommendation, honestly labeled the lane's read, never the chair's decision.
4. **THE OWED REGISTER** — what you could not verify (remote PR states, thread pagination, gh reads) with the exact run spec for the head.
5. **Loop-state line** at the tail: `CONTINUE + <next ring's name>` or `NO-IMPROVEMENTS + confirmation cycle` — plus a NEXT-LAUNCH block naming the next leg per the corrected plan's ring table (brief path + seat + logdir; probe at fire).

## Boundaries (binding)
- Kenari READ-ONLY; RFC upstream QUIET (decision-PREP — nothing posts anywhere); nothing public; no service changes; no `/root/.hermes` writes; git-only terminal — runs register OWED, never faked.
- The write-window: your artifact's existence opens the gate — after your first write, KEEP WRITING and commit+push ONLY after the last section.
- Receipts: every claim carries a source tag (IN-LANE / BORROWED / HEAD-RECON) + read-time stamps; absence only from a stamped read.
- The absent-target rule: never invent a file or fact; ABSENT stays ABSENT + named.
