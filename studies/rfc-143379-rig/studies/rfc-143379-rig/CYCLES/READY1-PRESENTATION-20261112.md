# READY-1 Operator Presentation: One-Layer Ablation Test for Write-Gate Security

### What It Is
The **one-layer-ablation** test is a falsifier designed to verify the security of the seven-stage write-gate acceptance pipeline (PR #139606). The test removes **one protective layer** from the pipeline and checks whether the gate still refuses unsafe memory writes. If the gate fails to block the write after ablation, it proves the layer was critical to security. If it still blocks, the layer’s claim of protection is disproven.

The **frozen-safety-text** is a protected constant within the gate, whose presence is critical for the gate’s logic. Ablating this layer means stripping away its safeguards and observing whether the gate remains secure.

---

### Why It Matters
The seven-stage write-gate pipeline is the final barrier against unsafe memory writes. To ensure its reliability, we must confirm that **no single layer is redundant**. This test provides empirical evidence that the gate’s protection is **removable-and-fatal**—meaning the removal of any layer must break the gate’s ability to refuse unsafe writes. This is the core of the R&D round’s purpose: to falsify the gate’s security claims.

---

### How It Works
1. **Ablation**: Remove one layer from the seven-stage pipeline. This could be a validation step, a checksum, or the frozen-safety-text check.
2. **Test Execution**: Attempt to write unsafe memory through the modified gate.
3. **Observation**:
   - If the gate **fails to block the write**, the layer was critical to security.
   - If the gate **still blocks the write**, the layer’s claim of protection is invalidated.

This is a **falsification test**: if the gate passes, the layer’s necessity is disproven; if it fails, the layer’s importance is confirmed.

---

### What It Proves
- **Security Property Load-Bearing**: If the gate fails-closed under ablation, it proves the layer was essential to preventing unsafe writes.
- **Falsification of Redundancy**: If the gate still blocks writes after ablation, the layer’s contribution to security is disproven, and the gate’s design may need revision.

---

### Adoption Status
- **Public Comment**: The test proposal was parked in the post-gate phase (public discussion).
- **Internal Battery-Arm Version**: The internal version of this test (row F) was adopted for further validation. This version includes stricter controls and additional safeguards to ensure robustness.

---

### Ask
**Adopt the one-layer-ablation test as a standard falsifier for all future write-gate iterations.** This ensures that no layer of protection is assumed to be redundant, and the gate’s security is rigorously validated.