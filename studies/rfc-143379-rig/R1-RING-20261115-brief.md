# R1 RING — THE READ-SIDE VERIFICATION HOOK (design + probe shape) — 2026-11-15

## The contract (hard)
- **READING ANYTHING IS A CONTRACT VIOLATION** (the read-scatter class, receipted four times tonight). Everything you need is inline. Round 1 = write the skeleton; afterwards write only.
- ONE TOOL CALL PER ROUND. NEVER run git. Appends ≤ 6,000 chars.
- The artifact: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/R1-READSIDE-HOOK-20261115.md`

## THE DESIGN TARGET (inline — the sprint's CREATOR-GAP invention, per SPRINT-PLAN §2/§3-R1)
The write-gate L0 currently gates on task-success alone (the Masked-Erosion finding: gates optimize task-success and mask redundant-safeguard loss). The open axis: **the read-side resolution of what the write-gate admits is unverified.** The hook = a READ-BACK GATE: after the gate admits a write, the hook verifies the read-side — what an entity/as-of read actually resolves (DISCERN's resolve-at-read: zero-LLM navigation, entity resolution 0.800 vs ≤0.40 baselines) and whether evidence silently lost after the write/compression (SELD's no-training/no-labels preference-shift detection, 83% vs 70%). The hook proposes the integration onto L0's admit/reject axis: admit → read-back verify → reject-on-evidence-loss (fail-closed) OR flag-and-log (fail-open probe mode) — the two-way door: the probe chooses the mode, the adoption follows evidence.

## THE DELIVERABLE — five sections:
1. **THE HOOK'S SHAPE** — the read-back gate: trigger (a write-gate L0 admit/reject event), the read-back step (the as-of/entity contrast), the verifier (SELD preference-shift over the read-back), the decision (fail-closed vs flag-and-log), the rollback (the write is reverted or re-written from the source — named + tested).
2. **THE PROBE SHAPE (the falsifier)** — a seeded write experiment: (a) seed a record-claim pair; (b) run the gate's admit path; (c) run the read-back + the preference-shift measurement; (d) the measured criteria: the read-back resolves the seeded record (entity matched) AND the SELD shift stays under the floor → PASS; either missed → FAIL → the hook fires/flag. The battery home: `fixes/falsifier-battery-20261104` (the read-side axis extends the falsifier's categories).
3. **THE INTEGRATION POINT** — where the hook sits on the write-gate L0 (the one-layer-ablation gate context: the safety text frozen, the re-ablation on model swap) — the hook as the gate's verify layer, never replacing the gate.
4. **THE MEASURED CRITERIA + METERS** — the pass/fail thresholds (entity-resolution ≥ 0.80 baseline; the SELD floor at the preference-shift detection), the falsifier's 6/6-vs-12/12 style counts (fabrication without the read-back vs clean refusal with it), the run record.
5. **THE HONEST MARKERS + TWO-WAY DOOR** — what's unmeasured (no lab runs tonight — the probe shape is the design's test), the ABSENT list (the live write-gate's current event log, the exact L0 code lines — named, never filled), and the door: if the probe disproves the hook's value, the hook stays a design note; if it proves, the adoption fires freely — the only gates are public writes beyond PR #1 + gists (per SPRINT-PLAN §4 NEEDS-THE-CHAIR).

## Binding
- Receipts stamped per claim (INLINE-crate / DESIGN-NOTE / ABSENT). ABSENT stays ABSENT + named.
- The RFC + upstream stay QUIET. Nothing posts.
- End: verify the file > 8,000 chars with all five sections; then stop. No git.
