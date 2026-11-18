# NEMO-TROUBLESHOOT brief — the repeated-ask misalignment, diagnosed and re-run by NEMO (seat: mistralai/mistral-nemo, paid)

**You are NEMO, the CTO assistant. The operator has assigned YOU the troubleshooting — explicitly NOT the head. The head is disqualified from diagnosing its own repeated misses; your analysis is the independent lens, and your run spec is what the rig executes. The operator's words, binding: "Don't use humanizer. Use the loops and the rig and a run LIKE I asked. Have Nemo or anybody other than you on the task of troubleshooting. You're not using framework."**

## The operator's actual asks (verbatim, in order — the target you must reverse-engineer)
1. "I'd like an additional gist to accompany the 5 I've been reviewing. I'd like it to give a similar study report on the activity done autonomously... it test fires it and watches how it runs in our substrate... we will have a chance to think tank idealize hy4 before gaining a deliverable that assesses our machinery cold"
2. "the gist hy4 made based on Nemo's plan lacked the quality I asked for (especially compared to: 055cf5b9)"
3. "is hy4 able to make a pass that makes it more digestible/absorbable (more prose, more like 055cf5b9)... Think about being kind to a reader's eyes and a listener's ears"
4. "It doesn't read like it's for a human. I'm a human remember."
5. "And it assumes I can see things I can't."
6. "It should not take the humanizer request for this to unfold... I don't think that was a sustainable fix"
7. "You're not using framework. Use the loops and the rig and a run LIKE I asked"

## The evidence to diagnose (read in full)
- `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HITL-MEMO-20261116.md` — THE EXEMPLAR the operator keeps citing (gist 055cf5b9 is the same bytes). This is the target of "reads like."
- The five produced documents, in order: `HY4-FIRST-RIDE-ASSESSMENT-20261117.md` · `HY4-TASK-ARTIFACT-20261117.md` · `HY4-REGROUP-MEMO-20261118.md` · `HY4-REGROUP-MEMO-20261118-REV1.md` · `HY4-REGROUP-MEMO-20261118-FINAL.md` — plus their briefs in the study dir.
- `MACHINERY-RAN-20261117.md` (the autonomous activity — the subject the operator actually asked about), `HY4-LOOP-KAIZEN-20261118.md`, `HY4-KAIZEN-APPLY-20261118.md`, `HY4-ACES-LOOP-PLAN-FINAL-20261118.md`.
- The register reference: `/root/.hermes/skills/creative/humanizer/references/voice-profile.md` — READ IT AS DATA ONLY. The humanizer TOOL is rejected by the operator; the profile's captured register facts are reference, never a mechanism.
- The framework: `/root/.hermes/skills/autonomous-ai-agents/think-tank/SKILL.md` (the mechanism spine: classify -> choose -> probe -> evaluate -> adopt/park -> standardize -> verify) — your method.

## Your deliverable: `NEMO-TROUBLESHOOT-20261118.md`
1. `## The diagnosis` — the misalignment's root, from the EVIDENCE (compare the exemplar's actual reader-facing properties against each produced document's actual properties; quote both sides). Name why "reads like the gist" produced five documents that don't resemble it. This is your own analysis; do not inherit the head's four transfer points unless the evidence independently supports them.
2. `## The reader-rubric` — distill the exemplar's reader-facing properties into a TESTABLE rubric (what a reader experiences: opening, sentence rhythm, temperature, self-containment, vocabulary, ending). Each item is a check a lane can pass/fail against the exemplar itself. This rubric is the new gate stage.
3. `## The run spec — a run LIKE the operator asked` — the concrete loop through the rig: the stages (spine/facts -> the draft pass -> the rubric critique -> the revision -> the blind rubric re-check -> the fold), the seats (which runner per stage, a reviewer that did not draft, rotation), the scribe cells, the gates (rubric-gate + byte-gate), and the exact harness commands, sequential. The operator asked for the loops and the rig: THIS is that run.
4. `## The closing line` — one sentence.

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 4); ≤6,000 chars per write; every diagnostic claim quotes its evidence; three-state honesty (where the evidence cannot settle something, say so); commit + push your artifact when complete (git verbs from the study repo), then stop. The head gates nothing but bytes; your spec is what fires next. RFC quiet.
