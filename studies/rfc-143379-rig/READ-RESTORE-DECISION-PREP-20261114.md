
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
