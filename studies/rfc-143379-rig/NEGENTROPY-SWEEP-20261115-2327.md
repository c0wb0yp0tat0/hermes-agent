# NEGENTROPY SWEEP — 2026-11-15 (rig #143379 standing current, slot 2327) — READ-RESTORE DECISION-PREP

## Landing this pass (stamped)
- **Brief passed in:** R1-READ-RESTORE-DECISION-PREP-20261114.md (rig root). The chair's door is the read-restore corridor: MemoryStore.read #141876 head `af16e3ab16`, the unmerged PR container `#116673` (Finn763, rebase head `ffc651bd11` clean/mergeable on 10-24/25), and the 3-condition hold from the RFC record §82.
- **Read cold (stamped):** rig root list (dir is the only artifact root); the two CYCLES siblings + REFS head-staged files. All stays below are the brief's own receipts; I did not re-derive them from the repo beyond the named commits — remote PR/gh state is NOT verified, and the brief marks that OWED.
- **Receipts (stamped):** IN-LANE = R1 brief + CYCLES/REFs siblings (read once, at this pass); HEAD-RECON = bug reports in the RFC body/record (stamped here). Nothing against the ledger's claim; the ledger supported the read-gate entry, not the artifact's content.

## What's old (stale / die)
- **The substrate's read is dead by construction:** `MemoryStore.read` absent on current main (removal 56ee8a5cc6, 2026-02-19), read-action battery RED (23/35), PR-head cell a collection error (#139606 `5b31ccb7d5`). This is a fact on the record — not contested.
- **The two in-play vehicles are BOTH unmerged and both open:** #141876 restore (c0wb0yp0tat0, head af16e3ab16) and the bounded-read container #116673 (Finn763, head ffc651bd11). The RFC says "the two vehicles, one gap, NEITHER merged" — that state still holds on the record. No branch fix/deletion has landed since.
- **The hold's condition is verbatim on the record:** RFC-143379-RECORD §82 (2026-11-11), comment 6787192097: "We are holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives with the community rather than let the hold become indefinite."
- **The fabrication class is measured, not predicted:** 0/6 fabrications without the read path; 12/12 clean refusals with exactly one non-punitive abstention sentence ("a system that cannot read should say so, never guess").

## What can die (regenerables)
- The **experimental cell** (uncommitted 14 lines + untracked battery = 35/35 green) is a staging artifact, not a ship — it is regenerable and must not be retained as evidence of landed state.
- The **six-move label trail / six migrations** are records, not artifacts — clone/clear as superseded once the chair's decision record is in the study.
- The **106-commits / 6,275-lines** total is a stack measurement, not the debt; the ~30-line four-site subset is the defensible core. Neither is a branch to prune.

## What the chain must carry
One dated bullet, the only durable thing worth keeping:
- **The chair's decision point, not the lane's answer:** the read-restore gate is a held decision (hold → alternatives-with-community, or a rescope/split offer), and the open question "why the read crashes on the PR head specifically" is verified closed only by execution (collection error was the stale base — jfugalde's run + Finn763's rebase #116673 head ffc651bd11, clean/mergeable). Nothing public; all of this stays local.

## The rig in one line
Read-restore is the standing gate: #141876 unmerged, #116673 unmerged, and the only remaining movement fires by the standing law call on the §82 hold — with the formulation "a system that cannot read should say so, never guess" as the sober framing for the abstention class.

## Next launch
- **Probe:** PLAYBACK — rerun the read-action battery once on the substrate and once on the #141876 head (with a clean clone, stamped) to confirm the three-state spread (RED/collection-error/green) before the chair decides; next ring per the corrected plan's ring table.

## OWED (no ghost reads, no service calls)
- Remote PR/gh state (num comments, mergeability of #141876/#116673, any new landing), thread pagination past comment 6787192097 — exact run spec:
  - `gh pr view 141876 --json number,title,state,mergeable,headRefName,comments` and `gh pr view 116673 --json number,title,state,mergeable,headRefName,comments`
  - thread tail: `gh api repos/<owner>/<repo>/pulls/141876/comments --paginate` then point at the last page's newest comment id.
  - Run spec stamped when executed.
