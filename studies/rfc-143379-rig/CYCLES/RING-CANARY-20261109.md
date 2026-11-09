# RING-CANARY 20261109 — injection-test design + run-receipt
Seat: step
Status: DRAFT / PRE-EXECUTION

## 1. Surface-cohort selection
- **Chosen surface:** learning-watch (15 m cadence).
- **Why safe:** injection is a single marker-line written to a **local file** that the watcher script already consumes; no external-repo touch, no network fetch, no remote mutation. The kit-gate 30 m cadence is excluded to keep the blast-radius minimal and the confirmation window tight.
- **Marker file path:** `studies/rfc-143379-rig/CANARY/local-marker.txt` (inside the repo tree, readable by the watcher, never pushed to a remote).
- **Watcher behavior:** at every 15 m cycle the learning-watch script opens `local-marker.txt`, reads the first token on the first line, and emits a structured log line.

## 2. Known-change design
- **Marker format:** exact string `RING-CANARY-20261109:PASS` on line 1 of `local-marker.txt`.
- **Injection step:** step writes the marker-line into the local file using `write_file` or equivalent filesystem touch; no `git commit`, no remote push.
- **Idempotency:** the marker is appended/replaced atomically (single write) so the watcher never sees a partial line.

## 3. Confirmation-rule (within-cadence fire)
- **Rule:** within the next 15 m learning-watch cycle, the emitted log must contain the literal token `RING-CANARY-20261109:PASS` as a field match.
- **Pass condition:** one cycle, one match.
- **Failure condition:** zero matches within 1 cycle → injection fault or watcher blindness → escalate to kit-gate 30 m for cross-check.

## 4. Rollback
- **Post-confirmation action:** immediately remove the marker-line from `local-marker.txt` (restore file to empty or prior content).
- **Verification:** subsequent cycle emits absence-of-marker; receipt is marked `ROLLED-BACK`.

## 5. Compose-check
- [x] Artifact path: `studies/rfc-143379-rig/CYCLES/RING-CANARY-20261109.md`
- [x] No public URLs, no remote mutation.
- [x] Local-only marker file, within existing watcher input contract.
- [x] Confirmation bounded by watcher cadence (15 m).
- [x] Rollback step defined and bounded to single cycle.

## 6. Run-receipt
- `INJECTED`: T0 (local marker written)
- `CONFIRMED`: T0+15 m (watcher log contains `RING-CANARY-20261109:PASS`)
- `ROLLED-BACK`: T0+15 m (marker removed, absence confirmed in next cycle)

---
Mechanism: the injection-test's design + execution-spec (the canary's run-receipt).
Next mechanism: compose the cycle-state summary + confirmation.
