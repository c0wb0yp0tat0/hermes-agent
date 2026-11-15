# R1 CONTINUATION — complete the decision-prep (2026-11-15 ~02:15 EST)

## Your task
`READ-RESTORE-DECISION-PREP-20261114.md` exists on the branch with only §4 (THE OWED REGISTER) and §5 (LOOP STATE + NEXT LAUNCH). Your ride composes the MISSING CORE SECTIONS before any commit:

1. **§1 THE EVIDENCE** — the label trail with receipts (the six label moves; P4 = the queue's smallest bucket — P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173; 24/120 P4-labeled; the category moved six times without the issue's substance changing; 34 comments of verified work; the label moved with the reading, never with the issue — "instruction-faithful criteria are the fix"). The fabrication class: 6/6 fabrications without the read path (twice), 12/12 clean refusals with one non-punitive abstention sentence ("a system that cannot read should say so, never guess"). The two vehicles, one gap, NEITHER merged: #11548 (minimal dispatcher, branch fix/116564-descr intact at d3a6e577, closed-by-author, merged=false) vs #116673 (schema-safe read + doc-chain, closed-by-author 2026-10-10, merged=false — the fix is not missing, it is UN-MERGED). The root-cause attribution: the PR-head collection error at `5b31ccb7d5` (#139606) is a stale-base artifact predating `95610a5db4`'s pathlib fix, NOT a read-bug; the verified rebase `ffc651bd11` ⊕ head `60a2e15638`. The hold's condition verbatim: RFC-143379-RECORD §82, comment 6787192097 (2026-11-11): "We are holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives with the community rather than let the hold become indefinite."
2. **§2 THE DECISION FRAME** — what the chair must decide, as explicit options: (A) continue the hold and keep its condition (evidence: the vehicle exists un-merged, the fixing is real, the hold is bounded); (B) the alternatives-with-community path the record names (evidence: the hold's own condition clause; the risk that the hold becomes indefinite); (C) a rescope/split offer (what splits, what stays). Each with evidence for/against, a risk register, and the open questions ONLY the chair can answer.
3. **§3 THE RECOMMENDATION** — ONE plain recommendation, honestly labeled the lane's read, never the chair's decision.

## Binding rules (non-negotiable)
1. ONE TOOL CALL PER ROUND. Never batch parallel tool_calls.
2. Read the existing artifact ONCE (its §4/§5 stay as they are — append §1, §2, §3 in FRONT of §4, or as the file's first sections; do NOT rewrite or delete §4/§5).
3. Write appends ≤ 6,000 chars each. Skeleton §1-§3 by round 3.
4. NO COMMIT until the file carries all five sections (§1 THE EVIDENCE, §2 THE DECISION FRAME, §3 THE RECOMMENDATION, §4 THE OWED REGISTER, §5 LOOP STATE). The prior ride committed with only two sections — that is the exact failure this continuation corrects; the commit is the landing's proof of COMPLETENESS, never an early exit.
5. Receipts stamped on every claim (IN-LANE / BORROWED / HEAD-RECON). ABSENT stays ABSENT + named.
6. The RFC stays QUIET — this ring posts NOTHING. STEER-6's corrections stand (kenari never held; solar/stepfun/longcat live; beam/moonbeam out — no operational effect on this ring; kenari simply unused).
7. On completion: commit + push (`git pull --rebase` on rejection), then verify `git ls-remote` == local.
