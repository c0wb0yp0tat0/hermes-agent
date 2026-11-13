# RESTORE-LENS-E2E-20261107 — Restore-Line End-to-End

**Lens:** Restore-Line (#141876 c0wb0yp0tat0, verified-but-unmerged; read-path's seam).  
**Ground:** MISSION-8H-V3-20261107.md + RFC-READ-20261107.md (read cold).  
**Question:** does the 8-hour mission's shape serve the restore-line's real state; does the merge-composition track fit?

## Verdict: GAPS

The mission's shape *partially* serves the restore-line. Track 1 (Merge-Composition Falsification) centers #141876 in a composed state, which is the right *direction* — composition is the only path that can land the verified read. But the mission's acceptance criteria stop at "composed branch staged (not published)" and never close the restore-line's actual need: **#141876 is verified-but-unmerged on current main, where the tool still answers "Unknown action 'read'"**. Staging a composed branch does not restore the read on main. The mission treats composition as a falsification exercise, not a landing.

## Named gaps (restore-line)

1. **No landing step.** Track 1 verification ends at "composed branch staged (not published)". The restore-line's need (read works on main) is never satisfied by staging alone; no track owns moving from staged composed branch → merge decision. The operator's word is the gate, but no PROPOSAL/decision surface is named for landing #141876.
2. **Read-path seam under-specified.** xngg1021's seam-gap-4 (doc=/read fallback) is the restore-line's own seam, but the harness spec (compose.sh → test-suite.sh → claim-check.sh → receipt-emit.sh) has no read-path-specific assertion (e.g., `read` action returns entries + usage line on composed head). The verified-but-unmerged behavior is not byte-verified by the harness.
3. **Unconditional-restore ask dropped.** 3oltan-seo asks restore unconditionally; the mission's gated, fork-only, staged posture means the read stays broken on main for the field pilot (director profile at ~96% of 4k-char budget) for the whole 8 hours.
4. **Stale-base collection error not in scope.** The collection error (closed by rebase, missing `from pathlib import Path`) is #141876's only real bug and is already fixed — but no track verifies the rebase landed; the "verified by execution" claim rests on a head SHA (`ec649ad9d`) that the mission never re-checks against disk.
5. **No per-PR regression assertion for the read action.** seam-gap-3 re-runs each PR's individual tests, but #141876's individual test is the read action itself; if that test isn't in the suite, the composed branch can be "green" while the read is still broken. The harness does not name the read action as a required test.

## Value (what the mission does give the restore-line)

- Centers #141876 in composition; without composition there is no landing path at all.
- Byte-verify habit makes the "verified by execution" claim auditable against disk (head SHA, test output).
- Fold-points give the read-path seam a reporting cadence (hours 2/4/6/8).
- Die-fallback clause stages outside-gate experiments (e.g., unconditional restore patch) as proposals rather than firing unattended.

## Compose-check table (Track 1 acceptance vs restore-line)

| Seam gap (xngg1021) | Track 1 acceptance | Restore-line read | Status |
|---|---|---|---|
| seam-gap-1 clean apply across 3 PRs | compose.sh exit 0 | #141876 must apply on top of #116673 without conflict (landing order per jfugalde) | FITS, but conflicts both ways today — mission cannot assume clean apply |
| seam-gap-2 composed tests pass | test-suite.sh green | read action returns entries + usage line on composed head (byte-verified) | NOT NAMED in acceptance — gap |
| seam-gap-3 no per-PR regression | claim-check.sh | #141876's read action must still answer (not "Unknown action 'read'") | IMPLICIT only — not asserted |
| seam-gap-4 receipts evidence composition | receipt-emit.sh ≥4 rows | need-id → task trace must include restore need (#141876) → read action | FITS if restore need-id is in the ledger |
| Byte-verify habit | every claim verified against disk | head SHA re-check (`ec649ad9d`) + read output on disk | FITS |
| Composed branch staged (not published) | final verification | does NOT restore read on main | GAP — no landing step |

## Missed angles

- The read action's own regression test is not named as a required seam assertion.
- Landing decision (approve/reject/defer) for #141876 is not a tracked deliverable; only staging.
- 3oltan-seo's field-pilot dependency on the read (anchor-full wall) is not in the acceptance criteria.
- The "verified by execution" claim is not re-verified at mission start (head SHA check) as a named task.

## FINAL SUMMARY
- file: /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/RESTORE-LENS-E2E-20261107.md
- verdict: GAPS
- top gap: Track 1 stages a composed branch but never lands #141876, so the read stays "Unknown action 'read'" on main for the whole 8 hours.