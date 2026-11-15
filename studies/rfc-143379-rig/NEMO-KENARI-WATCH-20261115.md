# NEMO-KENARI-WATCH-20261115

## THE VERDICT LINE
**BLOCKED** — The seat requires **launch seam fixes** and **pacing enforcement** before proceeding.

## §1 THE LOG READ — The Seat's Behavior on This Ride
The live log (`apex-loop-v2.log`) reveals the following key observations about the **kenari/dots-3-note-preview:free** seat:

1. **Write-First Tendency**: The assistant begins each round by reading grounding files and narrates reasoning before executing calls, adhering to the **write-first** contract. However, the transport enforces a **single-call discipline** during the write-window, which may limit efficiency.

2. **Launch Seam Issues**: The log confirms prior **F6-class failures** (missing logdir) and **404 base-endpoint failures**, resolved in this ride. The current ride (`LOOP-V2`) is live on the correct endpoint (`HARNESS_ENDPOINT=https://kenari.id/v1/chat/completions`), but stability across multiple rounds remains unconfirmed.

3. **Strengths**: The seat adheres to the **write-first discipline** and narrates reasoning clearly, ensuring transparency.

4. **Sticking Points**:
   - **Multi-call trimming** limits parallelism.
   - **No explicit pacing** (5-RPM/50-daily constraints) or reserve-rate limits are enforced.
   - **No confirmation of fine-tuning** across multiple rounds.

## §2 THE SEAT-TUNING CONTRACT
To recalibrate the seat, the following tuning contract is proposed:

1. **Brief-Shape Deltas**:
   - Add explicit **pacing instructions** (e.g., `PACE: Enforce 5 requests per minute and 50 daily; log violations`).
   - Clarify the **write-window knob** (e.g., `WRITE-WINDOW: 3 rounds max per write cycle`).
   - Confirm the **narrate-first** behavior aligns with the **write-first** contract.

2. **Launch Seam Fixes**:
   - Enforce the **FULL endpoint** (`HARNESS_ENDPOINT=https://kenari.id/v1/chat/completions`).
   - Ensure the **logdir precondition** exists before firing.

3. **Verification**:
   - Run **2 consecutive rounds** without launch errors to confirm stability.
   - Ensure reasoning is narrated before every call.

**VERDICT**: The seat is **not yet FIT** for sustained rides. It requires **named tweaks** for pacing and launch seam, followed by **2 stable rounds** to confirm fine-tuning.

## §3 THE WATCH'S CONTINUATION CONTRACT
The next Nemo-watch fire will adhere to:

- **Rules**:
  1. **Launch seam fixes** (FULL endpoint + logdir).
  2. **Pacing compliance** (5-RPM/50-daily enforced).
  3. **Stability** (2 consecutive rounds without errors).

- **EXIT condition**: The seat is **fine-tuned** after **N=2 consecutive rides** without contract violations.

## §4 THE COMPOSE-CHECK + RECEIPT STAMPS
- **IN-LANE**: All observations and tuning proposals are derived from the **live log** and **briefs** (`APEX-LOOP-20261115-brief.md`, `SPRINT-PLAN-20261115.md`).
- **BORROWED**: None.
- **HEAD-RECON**: None.

## THE LOOP-STATE LINE
**BLOCKED** — The seat requires **launch seam fixes** and **pacing enforcement** before proceeding. The next kenari dispatch must include:
```
CONTINUE + kenari/dots-3-note-preview:free (with FULL endpoint + logdir + pacing contract)
```