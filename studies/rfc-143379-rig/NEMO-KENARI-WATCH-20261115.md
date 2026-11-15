# NEMO-KENARI-WATCH-20261115

## THE VERDICT LINE
**BLOCKED** — The seat requires explicit tuning to adhere to the mission's constraints.

## §1 THE LOG READ — the seat's behavior on this ride
The **dots-3-note-preview:free** seat's behavior in the current ride (`apex-loop-v2.log`) is as follows:

- **Round 0**: The assistant begins by reading the grounding files sequentially due to transport restrictions (G7 class).
- **Rounds 1-14**: The assistant repeatedly attempts to verify artifacts and grounding files, violating the "ONE tool call per round" discipline and the "no hunting" rule by repeatedly checking the same files.

**Strengths**:
- Correctly identifies the need to read grounding files and verify artifacts.

**Sticking Points**:
- **Transport Restrictions**: Unable to execute multi-calls, leading to inefficient sequential reads.
- **Tool Discipline Violation**: Repeated use of `terminal` for non-git tasks, violating mission constraints.
- **Redundancy**: Repeatedly checks the same files without progress.

## §2 THE SEAT-TUNING CONTRACT
To recalibrate the seat for the next kenari fire, the following adjustments are required:

1. **Brief-Shape Deltas**:
   - Explicitly state that the assistant must adhere to the "ONE tool call per round" rule.
   - Emphasize the "write-first" discipline for concise, single-write finding files.

2. **Write-Window Knob**:
   - Strictly limit calls to one per round, avoiding multi-calls or redundant checks.

3. **Pacing**:
   - Respect the 5-RPM/50-daily rate limits and avoid unnecessary calls.

4. **Launch Seam**:
   - Use `read_file` and `list_dir` for file operations, avoiding `terminal` for non-git tasks.

**Verdict**: The seat is **not yet FIT** for independent operation. It requires explicit tuning.

## §3 THE WATCH'S CONTINUATION CONTRACT
- **Checklist Before Dispatch**:
  1. Verify adherence to the "ONE tool call per round" rule.
  2. Ensure no violation of the "no hunting" rule.
  3. Confirm correct tool usage for file operations.

- **EXIT Condition**: The seat is fine-tuned after **3 consecutive rides** without violating the above rules.

## §4 THE COMPOSE-CHECK + RECEIPT STAMPS
- **IN-LANE**: All observations derived from the current ride's log and the brief.
- **BORROWED**: None.
- **HEAD-RECON**: None.

## THE LOOP-STATE LINE
**BLOCKED** — The next kenari dispatch must include a revised brief emphasizing the "ONE tool call per round" rule and avoiding redundant calls.