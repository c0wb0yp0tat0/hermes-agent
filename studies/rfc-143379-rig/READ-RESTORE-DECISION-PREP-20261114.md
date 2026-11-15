
## §1 THE EVIDENCE

**1.1 Label trail.** The issue carried six category label moves; the substance
of the issue never changed across those moves. P4 is the queue's smallest
bucket (P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173); 24 of
the 120 are P4-labeled (the brief's count). The label moved with the reading, never with
the issue — the lane's finding: instruction-faithful criteria are the fix.
(IN-LANE from audit draft §4/§10; BORROWED bucket counts from brief.)

**1.2 Fabrication class.** Six of six fabrications occurred without the read
path (twice observed); twelve of twelve clean refusals carried one non-punitive
abstention sentence: "a system that cannot read should say so, never guess."
(IN-LANE from verified comment set 34 of verified work; HEAD-RECON RFC-
143379-RECORD-20261111.md + IMPROVED-S2U-DRAFT-FINAL5-20261111.md.)

**1.3 Two vehicles, one gap — neither merged.** #11548 (minimal dispatcher,
branch fix/116564-descr intact at d3a6e577, closed-by-author, merged=false)
vs #116673 (schema-safe read + doc-chain, closed-by-author 2026-10-10,
merged=false). The fix is not missing; it is UN-MERGED. (IN-LANE local repo
reads; BORROWED from brief §2.)

**1.4 Root-cause attribution.** The PR-head collection error at `5b31ccb7d5`
(#139606) is a stale-base artifact predating `95610a5db4`'s pathlib fix — NOT
a read-bug. The verified rebase is `ffc651bd11` ⊕ head `60a2e15638`. (IN-LANE
from record §"the root-cause" §4; HEAD-RECON RFC-143379-RECORD-20261111.md.)

**1.5 Hold condition (verbatim).** RFC-143379-RECORD §82, comment 6787192097
(2026-11-11): "We are holding for the read-restore PR (#141876)… if the fix
does not land soon, we will discuss alternatives with the community rather than
let the hold become indefinite." (HEAD-RECON.)

## §2 THE DECISION FRAME

The chair must choose among three explicit options. Each carries evidence for
and against, a risk register, and open questions only the chair can answer.

**Option A — Continue the hold and keep its condition.**
- Evidence for: The vehicle exists un-merged (#116673 head `60a2e15638`); the
  fixing is real (verified rebase `ffc651bd11` ⊕ head); the hold is bounded
  (condition clause sets a deadline).
- Evidence against: The fix has been un-merged since 2026-10-10; the hold
  risks becoming indefinite if the condition's "soon" is not enforced.
- Risk register: Indefinite hold if community momentum fades; opportunity cost
  while the fix sits un-merged.
- Open question: How soon is "soon" — does the chair have a hard date?

**Option B — Alternatives-with-community path.**
- Evidence for: The hold's own condition clause explicitly names this path if
  the fix does not land soon; the risk that the hold becomes indefinite is real.
- Evidence against: The fix is verified and un-merged; abandoning the hold for
  alternatives wastes a real solution.
- Risk register: Community fragmentation if alternatives split focus; loss of
  verified work if #116673 is abandoned for a new approach.
- Open question: What is the community's appetite for alternatives given the
  un-merged fix?

**Option C — Rescope/split offer.**
- Evidence for: The minimal-dispatcher vehicle (#11548) and the schema-safe
  read vehicle (#116673) could be split; one could land while the other stays
  hold.
- Evidence against: Splitting may reintroduce the read-bug risk if the schema-
  safe read path is delayed; the two vehicles address the same root cause.
- Risk register: Partial fix leaves the read path exposed; coordination cost
  of split review.
- Open question: Which half stays, and which half moves forward alone?

## §3 THE RECOMMENDATION

The lane's read: **Option A — continue the hold and keep its condition**, with
a 72-hour hard deadline enforced by the chair. The evidence is clear: the fix
is real, it is un-merged, and the hold's own condition clause provides an exit.
The lane does not choose the chair's decision; it recommends the path that keeps
the verified fix in play while bounding the hold's duration. If the fix does
not land within 72 hours, the lane recommends the chair trigger Option B per
the hold's own condition.

## §4 THE OWED REGISTER — what is NOT yet verified

**4.1 Remote PR states.** #11548 and #116673 merged=false confirmed IN-LANE from
local repo reads (branch d3a6e577 intact; #116673 head `60a2e15638` per the audit
draft §2); the remote PR state (issue tracker / API) OWED — run spec for the head:

  ```
  gh pr view 11548 --json state,merged,headRefName,baseRefName,additions,deletions
  gh pr view 116673 --json state,merged,headRefName,baseRefName,additions,deletions
  ```
  (remote check — git-only terminal; not yet executed.)

**4.2 Thread pagination / events endpoint.** The record states the API events
endpoint exposes none of the final label changes — confirmed IN-LANE from the
audit draft §4/§10; the thread's full comment set (34 of verified work) is read in
RFC-143379-RECORD-20261111.md + IMPROVED-S2U-DRAFT-FINAL5-20261111.md. PAGINATION
OWED only if the chair wants the raw events; not needed for the decision.

**4.3 Execution cells (PR head vs substrate vs experimental).** The three-state
spread (PR head collection error / substrate cleanly absent / experimental 35/35
green) is confirmed IN-LANE from RFC-143379-RECORD §"the current condition" + the
brief's receipt. The PR head `5b31ccb7d5` (#139606) collection error is now
attributed to a stale base predating `95610a5db4`'s pathlib fix — per the record
§"the root-cause" §4, a stale-base artifact, not a read-bug; the verified
rebase `ffc651bd11` ⊕ head `60a2e15638` (IN-LANE).

**4.4 Brake line.** This leg posts NOTHING (RFC upstream QUIET per the head).
No commits to upstream branches; the two vehicles' states are copied here, never
touched. All verification goes through the register in §4.1.

## §5 LOOP STATE + NEXT LAUNCH

**Loop-state line:** `CONTINUE + READ-RESTORE decision-prep` — the hold's
condition is met and the evidence stands; the next leg acts on the chair's
decision.

**NEXT-LAUNCH block** (per the corrected plan's ring table — NEMO-DAY-PLAN
§5.1 C3 door-correction):

- Ring leg to fire next: the chair's decision leg (this document gates it).
- Communicated as: the chair's post-gate decision. If it names the community path,
  the runner is **READ-RESTORE → alternatives-with-community**; if it picks
  continue, the runner re-checks the hold's condition. The next launch is gated
  on the chair's post-review command; this lane does not post.

---

*Receipt ledger — every claim carries a source tag: IN-LANE (the rig's own trace),
BORROWED (this brief), HEAD-RECON (record-side, stamped 2026-11-14). Files read
exactly once: RFC-143379-RECORD-20261111.md, RFC-143379-BODY-20261111.md,
IMPROVED-S2U-DRAFT-FINAL5-20261111.md, BRIEF-AUDIT-S2U.md,
S2U-MISSION-PLAN-NUANCE-20261111.md, ADOPTIONS-20261112.md,
CROWN-SLICE.md, NEMO-DAY-PLAN-20261114.md, NEMO-STEER-CHANNEL-20261114.md.
Drop/ is OUTSIDE the read roots — never claimed; the REFS/ copies are the only
reachable way in.*
