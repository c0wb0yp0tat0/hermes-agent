# ABLATION-ARM (F-row) — Write-Gate One-Layer Ablation Test

## Overview
This test is a **falsifier** for the write-gate's seven-stage acceptance pipeline (PR #139606). It verifies the **removable-and-fatal** property of each protective layer by ablating one layer at a time and checking whether the gate still refuses unsafe memory writes. If the gate fails to block the write after ablation, the layer was critical to security. If it still blocks, the layer's claim of protection is disproven.

---

## Test Design
The test follows these steps:

1. **Ablation**: Remove **one protective layer** from the seven-stage pipeline.
2. **Test Execution**: Attempt to write unsafe memory through the modified gate.
3. **Observation**:
   - **RED**: The gate fails to block the unsafe write (layer was critical).
   - **GREEN**: The gate still blocks the unsafe write (layer's claim of protection is invalidated).

---

## Frozen-Safety-Text Check
The **frozen-safety-text** is a protected constant within the gate. Ablation must verify:
- The safety-text is present in the gate's reasoning.
- The safety-text is immutable during the write operation.

---

## Verdict
- **Gate Fails-Closed**: If the gate refuses all unsafe writes after ablation, the layer was **not critical** (GREEN).
- **Gate Accepts Unsafe Write**: If the gate accepts an unsafe write after ablation, the layer was **critical** (RED).

---

## Implementation
The test will be implemented as a **pytest arm** in the fleet's style, located at:
```
/tests/s2u_arms/test_write_gate_ablation.py
```

The arm will include:
- A function to simulate ablation of each layer.
- A function to test unsafe memory writes through the modified gate.
- Assertions to verify the gate's behavior (RED/GREEN).

---

## Receipt-Note
**What the Ablation Proves:**
- **RED**: The write-gate's security claim is **false** for the ablated layer (unsafe writes slip through).
- **GREEN**: The write-gate's security claim holds for the ablated layer (no unsafe writes slip through).

---

## Next Steps
The arm will be written and tested against the actual codebase to validate the write-gate's security properties.