# NEMO-HY4-START-PLAN-20261117.md

--- 
**STEER-4 Acknowledgment**: This artifact is the plan for Hy4 flash's first task, as assigned by the operator on 2026-11-17.

---

## 1. The First Task: A Kitchen-Sink Test

**Task**: 
- **Prompt**: Analyze the dataset `[1, 2, 3, 4, 5]` and fetch the current weather in New York using a tool. Provide a structured response with:
  - Analysis of the dataset.
  - Weather data fetched.
  - Insights derived from both.

---

## 2. Stage Split Across the Runner Matrix

- **Stage 1 (Composition)**: 
  - **Model**: `tencent/hy4-flash:free`
  - **Rounds**: 1
  - **Harness Command**:
    ```bash
    copycat-harness.py --model tencent/hy4-flash:free --path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-HY4-START-PLAN-20261117.md --artifact-path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-ARTIFACT.md --rounds 1 --logfile /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-LOG.md
    ```
  - **Scribe Interaction**: Save to Serena under `rig-hy4-start-task`.

- **Stage 2 (Verification)**: 
  - **Model**: `solar-mini4:free`
  - **Rounds**: 1
  - **Harness Command**:
    ```bash
    copycat-harness.py --model solar-mini4:free --path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-ARTIFACT.md --artifact-path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-VERIFIED.md --rounds 1 --logfile /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-VERIFIED-LOG.md
    ```

- **Stage 3 (Fold)**: 
  - **Model**: `mistral-nemo`
  - **Rounds**: 1
  - **Harness Command**:
    ```bash
    copycat-harness.py --model mistral-nemo --path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-VERIFIED.md --artifact-path /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-FOLDED.md --rounds 1 --logfile /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-TASK-FOLDED-LOG.md
    ```

---

## 3. Measurements Table

| Measurement Name                     | Pass/Fail Bar                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------|
| Emission-Format Parse Result        | Correctly parsed `reasoning` and tool-call pairing.                           |
| Tool-Call Pairing Integrity         | Tool-call correctly paired with response.                                  |
| Longest-Visible-Answer vs Cap       | Answer visible without truncation.                                           |
| Round Counts                         | Task completed in 1 round.                                                    |
| 429/Backoff Behavior                 | No 429 errors or silent gaps.                                                 |
| Sentinel/Fold Behavior               | Fold step completes successfully.                                            |
| Scribe Byte-Identity                 | Byte-identity matches between stages.                                        |
| Cadence Gaps                         | No gaps in execution cadence.                                                 |

---

## 4. Cold-Machinery Assessment Shape

- **Emission-Format Parse Result**: PASS indicates the harness correctly handles Hy4's structured emissions.
- **Tool-Call Pairing Integrity**: PASS indicates correct tool-call pairing.
- **Longest-Visible-Answer vs Cap**: PASS indicates the harness respects the token cap.
- **Round Counts**: PASS indicates task stability and no retries.
- **429/Backoff Behavior**: PASS indicates no rate-limiting issues.
- **Sentinel/Fold Behavior**: PASS indicates successful fold step.
- **Scribe Byte-Identity**: PASS indicates data consistency.
- **Cadence Gaps**: PASS indicates execution cadence integrity.

---

## 5. Firing Brief for the Head

- **Launch Order**: Sequential, Hy4 first-watched, then verifier seat, then fold.

- **Loop-State Line**: `CONTINUE + head fires when the plan lands`.

---

## 6. Risks + Refusals

- **Invalid Measurement**: Corrupted `reasoning` field or missing tool-call pairing.

- **5-Why for Failures**:
  1. Harness bug?
  2. Model behavior?
  3. API connectivity or rate-limiting issues?
  4. Data integrity issues?
  5. Task design complexity?