# GOVERNANCE-LENS-E2E-20261107 — Governance-Line Lens on MISSION-8H-V3

**Lens:** the governed compaction (staged) + the provenance-survival leg.
**Ground:** MISSION-8H-V3-20261107.md + RFC-READ-20261107.md (cold read).

## Verdict: GAPS

The mission serves the governance line only indirectly — governance is folded into
Track C (machinery standing) and Track D (read-gate watch), with no dedicated
governance track, even though governance is one of the RFC's four lines. The
provenance-survival leg is marked [x] staged but has no issue home, and the
unowned invariant (caller provenance defaulting to "unknown" at the pipeline's
definition) remains unassigned.

## Named gaps

1. **No dedicated governance track** — governance (provenance-origin classification,
   archive-before-stub, K-recency hard window) is not a first-class track; it rides
   inside Track C's fold-points. The governed compaction issue is not yet opened
   (opportunity 6), so the governance track has no home.
2. **Unowned invariant** — opportunity 11 (provenance defaults to "unknown" at the
   pipeline's definition, not the call site) is "unowned because everyone assumes
   someone else will do it"; the mission does not assign it.
3. **Reroute-to-chain-doc seam ownership ambiguous** — open question (RFC-READ)
   unassigned between this pipeline's follow-up and governed compaction's home
   (opportunity 10).
4. **Provenance-survival leg staged but not tracked** — marked [x] staged in RFC-READ
   but no receipt/byte-verify step names it in the mission's task-rows.
5. **Silent-failure classes not calibrated** — Track C's failure-calibration lane
   names composed-state falsification's failure-modes, but the governance-line
   silent-failure classes (provenance defaulting to a real origin) are not in the
   calibrated list.

## Compose-check table

| Line (RFC four lines) | Mission track coverage | Governance-line seam | Status |
|---|---|---|---|
| Restore | Track 1 (composed) + Track D | n/a (not governance) | covered |
| Network | Track 1 (composed) + Track D | n/a (not governance) | covered |
| Governance | Track C (folded) + Track D (read-gate) | provenance-survival staged; issue unopened; unowned invariant | GAPS |
| Compaction | Track C (failure-calibration) | K-recency window scaling open; long-session gate FAIL | GAPS |

## Top gap
The governed compaction issue is not yet opened and the provenance-default invariant
is unowned — governance has no home and no assigned owner in the mission.
