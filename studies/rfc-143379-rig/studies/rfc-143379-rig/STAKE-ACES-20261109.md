# STAKE-ACES-20261109 — ACES-LEG Slice (4-hour Sprint, Loop-Contract + Loop-Metering)

Status: operative. Nothing public. Compose-check pending.

## 1. Leg-Sequence (operative text)

The 4-hour sprint runs the ACES improver-loop END-TO-END ACTUALLY PROPERLY.
Leg order is fixed; no leg may be skipped or reordered.

1. **improve** — produce the candidate change (the improver's output).
2. **audit** — independent cross-audit of the candidate (the audit lens).
3. **review** — review of the audit's findings (the review lens).
4. **AoA** — assessment-of-assessment, with the bases' swaps (swap A/B/C/D applied in rotation).

### Base-swaps (rotation width = 4)
- Swap A: base ← prior improve-output
- Swap B: base ← prior audit-output
- Swap C: base ← prior review-output
- Swap D: base ← prior AoA-output
Rotation width = 4 bases; each ring rotates all four before a ring may close.

### Byte-preconditions (closure before new work)
Before any new work begins on a ring, the byte-checks must close:
- requested SHA == executed SHA (hard step, before the suite)
- receipt exists for the prior ring's landing (NOT-RUN stays until the receipt exists)
- byte-equality verified on the candidate's diff vs. the pinned head
No new work until these close.

### Terminal (no-change-confirmation)
The loop terminates only on a no-change-confirmation: the improver's candidate equals the prior committed state byte-for-byte, AND the audit + review + AoA all return no-change. A non-no-change result re-enters the loop at improve (re-entry is proper, not improper — the prior mis-fire was improper re-entry without byte-closure).

## 2. Loop-Metering (G-arcs loop-credits)

- A ring's landing earns the meter's dispatch-credit ONLY with its receipt.
- No receipt → no credit → no phase advance → no dispatch.
- Credit is per-ring, per-G-arc: G1 (ACES-improperly-loop) accrues credit only when the ACES loop's ring lands with a receipt.
- Receipt must claim only what the run's log shows (NOT-RUN stays until the receipt exists).
- Meter's dispatch-credit is the only path to phase advance (Gate: a phase advances only when all prior-phase goals meet θ-threshold AND their rings hold receipts).

## Compose-check

- [ ] leg-sequence fixed: improve → audit → review → AoA
- [ ] base-swaps rotation width = 4 (A/B/C/D)
- [ ] byte-preconditions close before new work
- [ ] terminal = no-change-confirmation
- [ ] loop-credits: ring landing earns dispatch-credit only with receipt
- [ ] nothing public