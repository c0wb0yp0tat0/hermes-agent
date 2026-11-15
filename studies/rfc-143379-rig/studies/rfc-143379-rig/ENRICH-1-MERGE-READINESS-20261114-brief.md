# ENRICH-1 MERGE-READINESS PREP brief — 2026-11-14 (the apex enrichment leg, chair-gated: stage only, nothing public)

**You are the apex-enrichment lane** (the operator's charter: "not only mission success but the most successful version of the success possible"). Your ring: the read-restore door's ULTIMATE success — not a decision-prep (that's R1, done) but the **merge-readiness package** for the fix's landing, staged in-realm and chair-gated. You prepare; the chair decides; nothing posts.

## The door's live state (HEAD-RECON 2026-11-14, all three vehicles verified OPEN/unmerged via gh)
- **#141876** (the memory `read` restore — the wound's fix; ~12-line `MemoryStore.read`, head af16e3ab16) — OPEN, mergeable UNKNOWN, not merged.
- **#11548** (minimal dispatcher, branch fix/116564-descr @ d3a6e577) — OPEN, not merged.
- **#116673** (bounded read + doc-chain; head 60a2e15638) — OPEN, not merged.
- The read action was removed in 56ee8a5cc6 (14-line deletion, Feb); current main answers "Unknown action 'read'". The hold: comment 6787192097 (RFC-143379-RECORD §82, 11-11): "We are holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives with the community rather than let the hold become indefinite." R1's evidence (READ-RESTORE-DECISION-PREP-20261114.md) carries the label trail, the queue shape, the fabrication class (6/6, 12/12), and the two-vehicle state. R3 (in flight) folds the FINAL5-8 draft chain whose ask = the label-follow-the-body re-read.

## Grounding (each at most once; ABSENT stays ABSENT + named; no archaeology)
1. This brief, twice.
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/READ-RESTORE-DECISION-PREP-20261114.md` — R1's frame (read once).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/CYCLES/IMPROVED-S2U-DRAFT-FINAL5-20261111.md` — FINAL5 (read once, if needed).
4. The steer channel — before EVERY round; act on the newest unacknowledged STEER-<id>.
5. Do NOT web, do NOT gh (git-only terminal) — the remote states above are the head's receipt; anything more registers OWED.

## Deliverable (the artifact — skeleton by round 3, one section per write ≤6,000 chars, commit+push once at the END)
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/ENRICH-1-MERGE-READINESS-20261114.md`:
1. **THE ACCEPTANCE BATTERY** — the testable definition of "the read-restore landed right": the red/green runs (the exact 6/6 fabrication repro + the 12/12 clean-refusal repro against a scratch store, per the record's R1 reproduction; the restore's head-returns-entries check), the schema-safe edge (the doc-chain bounded read), the non-regression line (the memory path's existing ops unchanged), and the battery's runnable commands (exact specs — they run machine-side, not in-lane; register OWED with each command string).
2. **THE VEHICLE RECOMMENDATION** — the merge-path read: one anchor (#141876) with the bounded read (#116673) tied to its acceptance battery (R1's own recommendation shape — hold the status, not the brake); what #11548's role is (dispatch bootstrap vs read) and the recommendation to the chair; the shipping shape (one PR, one battery, one label change P4→P2) vs the split-shape (per-vehicle ships).
3. **THE CHAIR PACKAGE** — the ONE page the chair reads to decide: the wound (3 lines), the evidence (the label trail + fabrication numbers, cited to R1), the options (R1's A/B/C condensed), the acceptance battery's size (estimated runs/cost), the word-gate note (this package crosses to the public ONLY on the operator's word — the move is: restate the hold with the battery attached, or ship the split).
4. **THE RISK REGISTER** — what a stalled merge costs (the ~17K-issue drift extrapolation, R1's numbers), what a rushed merge costs (regression on the memory path), the two-vehicle churn risk, the label-lottery risk on a rescope.
5. **THE OWED REGISTER** — machine-side specs: running the battery's red/green commands, fetching #141876's mergeability/checks, the final merge dispatch (chair-gated).
6. **Loop-state line**: `CONTINUE + <what's next after the chair's word>` or `HOLD + CHAIR-GATE` + a NEXT-LAUNCH block naming the next in-realm leg ONLY if it needs no chair word.

## Boundaries (binding)
- kenari READ-ONLY; RFC QUIET; **nothing public — this package is staged for the chair; the crossing is the operator's word alone**; no service changes; no `/root/.hermes` writes; git-only terminal — runs register OWED with exact command strings, never faked.
- ONE tool call per round (the hardened harness); no drop/ paths; ABSENT stays ABSENT + named; receipts tagged + stamped (IN-LANE / BORROWED / HEAD-RECON); the write-window's discipline (after the first write KEEP WRITING; commit once at the end).
