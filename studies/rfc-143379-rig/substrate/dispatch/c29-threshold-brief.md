# C29 - THRESHOLD REFINEMENT + EMBEDDING HARDENING (ACES Cycle, Phase 2)
**Anchored Free Lane** — follows C28 segment-split probe

## ANCHOR (required)
- `/root/.hermes/memories/MEMORY.md` — the cornerstone
- `/root/workspace/master-page/memory-chain/001-conventions.md` — self-firing contract + session-surviving arm
- `/root/workspace/master-page/memory-chain/003-routing.md` — routing conventions
- C26 Park verdict: detached-legs UNREACHABLE due to window fragmentation
- C28 Results: segment-split improved to BOUNDARY-ALIGNED (continuing)

## UPSTREAM CHAIN
**C26 PARK:** Window coverage showed detached-legs unreachable at 512/640/768/1024
- Root cause: windows split at content boundaries, not lesson boundaries
- Verdict: PARK (zero delta)

**C27:** Completed positive delta
- Phase 1: no-thinking horse started (:44831)
- Phase 2: template leak investigation
- Phase 3: threshold calibration (0.55→0.60)
- Phase 4: knee probe (min window 2048 chars, threshold 0.60)
- Phase 5: landing complete
- Engine state: UP at :44831 with no-thinking template

**C28 SEGMENT-SPLIT PROBE (completed):**
- Created 25 boundary-aligned segments from 002-lessons.md
- Detached-legs lesson (538 chars) now in single segment c28-seg006.md
- Verdict: CONTINUE to threshold refinement phase

## CURRENT STATE
- Engine: :44831 UP (no-thinking template verified)
- Segments: /root/workspace/master-page/memory-chain/c28-segmented/ (25 files)
- Embedder: /root/.lmstudio/.internal/bridge-api-token.txt available but requires validation
- Threshold: 0.60 calibrated at C27
- WIN_SIZE: 2048 (from C25S2)

## TASK (Phase 2)
Refine threshold and harden embedding for boundary-aligned segments.

**Objective:** Verify that segment-split + threshold 0.60 provides reliable grounded answers.

1. **Window re-probe:** Re-run window-coverage battery at WIN_SIZE=2048 against segmented chain
2. **Threshold tuning:** Calibrate optimal threshold for segment-level context
3. **NOT-IN-CHAIN honesty:** Verify honest refusals for absent facts
4. **Measure delta vs C28:** delta > 0 = CONTINUE, delta = 0 = PARK (C24d)

## CONSTRAINTS
- Use harness-bridge.sh ONLY (never raw engine)
- HARNESS_BLOCK_SIZE=a, HARNESS_WIN_SIZE=2048, HARNESS_CACHE_THRESHOLD=0.60
- Verify embedder authentication works
- Artifact-first: write verdict before summary

## SELF-FIRE CONTRACT (binding)
This brief carries the MEMORY.md anchor + self-fire contract.
- Dispatch: hermes cron create --deliver local --no-agent --script <this_brief> '2m' --repeat 1 --name c29-threshold-refinement
- Co-base diversity: C27 used laguna-s/xs; use poolside/laguna-xs-2.1:free or solar-pro4:free
- Termination: C24d (repeat until no measurable change)

## HANDOFF
Next leg receives: this brief as spec file
Expected deliverable: c29-threshold-results.json + c29-threshold-verdict.txt

---
**SCHEMA ENVELOPE (required)**
```json
{
  "verdict": "CONTINUE|PARK",
  "delta": {"detached_legs": bool, "enospc": bool, "ports": bool, "not_in_chain": bool},
  "next_action": "threshold_refinement|c29|park"
}
```

**METRICS TO VERIFY**
| Metric | Target |
|--------|--------|
| detached_legs_2048 | CORRECT or GROUNDED (not HONEST_REFUSAL) |
| enospc_tail | CORRECT |
| ports_control | CORRECT |
| not_in_chain | CORRECT_REFUSAL |
| latency | < 120s per query |

**ARTIFACTS**
- /root/.hermes/cache/scratch/c29-threshold-results.json
- /root/.hermes/cache/scratch/c29-threshold-verdict.txt