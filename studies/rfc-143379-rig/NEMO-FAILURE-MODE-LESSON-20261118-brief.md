# NEMO-FAILURE-MODE-LESSON brief — Nemo learns from the repeated-ask class (seat: mistralai/mistral-nemo, paid)
scribe-cell: rig-nemo-lesson

**Your role in the night, made plain by the operator: TROUBLESHOOT, then LEARN. You do not write the deliverable. The deliverable is Hy4's — it always was — and it is the mini-test of Hy4, running now through the loop under the reader's rubric. Your job in this ride is the learning: turn the repeated-ask failure mode into a lesson that changes how you and the fleet work next time.**

## The failure mode you are learning from (the evidence is on the branch)
1. READ `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-STEER-CHANNEL-20261116.md` — STEER-5, STEER-5-EXT, STEER-5-GATE, STEER-5-GATE-2, and OPERATOR-FEEDBACK-1: the operator's verbatim words, including "it doesn't read like it's for a human. I'm a human remember", "it assumes I can see things I can't", "This is madness... the request was always to have hy4 write it... it's literally turned into giant failure mode so Nemo needs to be learning from this failure mode", and "I don't want Nemo to write it".
2. READ your own troubleshooting artifact `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-TROUBLESHOOT-20261118.md` — and notice what the gate noticed: your diagnosis re-concluded that the FINAL document "successfully aligns with the exemplar", directly contradicting the operator's verdict. That was YOUR contribution to the misalignment: the structural rubric (opening hook present) voted PASS where the reader experienced FAIL. The lesson is not the prose; the lesson is the calibration: a structural check is not a reader's experience.
3. READ the operator's actual asks as history in that channel, and the exemplar's own opening (in the study dir: `HITL-MEMO-20261116.md`).

## Your deliverable: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-FAILURE-MODE-LESSON-20261118.md`
A lesson document, written the way a person would write it (plain, honest, no machine row vocabulary, nothing assumed), containing:
- `## What the failure mode was` — the repeated-ask class, in your own words from the evidence; include the part you played.
- `## The calibration rule` — how to tell a structural pass from a reader's pass (three-state: CONFIRMED by structure / CONFIRMED by experience / NOT-CONFIRMED), with the calibration test you will run on any future deliverable you gate.
- `## The ownership rule` — the deliverable's author is the seat the operator names; the troubleshooters diagnose and learn, they do not write. Name that rule plainly.
- `## The closing line` — one honest sentence.
Then append one dated bullet of the same lesson to `/root/workspace/master-page/memory-chain/002-lessons.md` (the chain is append-only; your bullet is the fold), and verify it serves (`?raw=1`).

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 3); ≤6,000 chars per write; plain register (no em dashes, no bold runs, no bullets in the lesson's prose); commit + push your artifact when complete; then stop. The head gates bytes only. RFC quiet.
