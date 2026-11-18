# NEMO-SCRIBE-WRITE-PLAN: Unification of Lane Writes and Scribe Contract

## THE VERDICT
The unification is **clean** if the scribe tunnel (`http://127.0.0.1:24282`) is reachable from the lane's write tool (`write_file`). The current design allows post-hoc discovery of stubs and truncation-starvation classes, but the scribe's contract (cell-based byte verification) can be enforced **at write time** without architectural gating.

---

## The Design
### Candidate (a): Assert Lane Writes into Scribe Cells at Write Time
- **Changes**:
  - Modify the `write_file` tool to **immediately** send the artifact's bytes to the scribe's `save_memory` endpoint.
  - If the scribe's cell does not match the lane's bytes, the lane reports a **named mismatch** (e.g., `SCRIBE_MISMATCH`) and rolls back the write.
- **Acceptance Test**:
  - Every lane write must trigger a scribe cell update and verification. If the cell's content does not match, the lane fails the round with a `SCRIBE_MISMATCH` flag.

### Candidate (b): Run Placeholder-Scan at Every Write
- **Changes**:
  - Integrate the placeholder-scan logic into the `write_file` tool, not just the fold step.
  - If a stub marker (e.g., beam's 288-byte placeholder) is detected during a write, flag it immediately with `STUB_DETECTED`.
- **Acceptance Test**:
  - Stub markers must be flagged **during the write**, not after the fold. The lane's round must fail if a stub is written mid-run.

### Candidate (c): Read-Side Fallback to Scribe Cells
- **Changes**:
  - Modify the file-read logic to **fall back to the scribe's cell** if the file read truncates.
  - If a lane reads a truncated file, it must query the scribe's cell for the full bytes.
- **Acceptance Test**:
  - Truncated reads must resolve to the scribe's cell content. The lane must not proceed with incomplete evidence.

---

## The Patch Spec
1. **Lane Write Tool (`write_file`)**:
   - Add a pre-write hook to send bytes to the scribe's `save_memory` endpoint.
   - Append a post-write hook to verify the cell's content against the written bytes.
   - If mismatch: **flag `SCRIBE_MISMATCH`** and roll back.

2. **Placeholder-Scan Integration**:
   - Embed the placeholder-scan logic in `write_file` to detect stubs during the write.
   - If stub detected: **flag `STUB_DETECTED`** and halt the write.

3. **Read-Side Fallback**:
   - Modify the file-read logic to check the scribe's cell if the file read truncates.
   - Use the cell's content to reconstruct the full artifact.

---

## The Two-Way Door
- **Flag Name**: `SCRIBE_MISMATCH` (for byte mismatches), `STUB_DETECTED` (for stubs).
- **Off Value**: `None` (no flag).
- **Rollback**: Immediate lane round failure and artifact deletion.

---

## The Risks
1. **Performance Overhead**:
   - Risk: Sending every write to the scribe may slow down the system.
   - Counter: Batch scribe writes during fold steps or use async I/O.

2. **Network Dependency**:
   - Risk: Scribe tunnel downtime could halt all writes.
   - Counter: Implement local caching with periodic syncs to the scribe.

3. **Stub Detection False Positives**:
   - Risk: Non-stub artifacts may be flagged as stubs.
   - Counter: Refine placeholder-scan logic with adaptive thresholds.

---

## THE LOOP-STATE LINE
**Unified write-scribe contract via immediate byte verification and stub detection at write time.**
**Next: Implement candidate (a) with async scribe hooks and evaluate performance.**