# SUBSTRATE-READ-RECEIPT-20261114.md

**Ring:** SB1 — THE READ (nightshift spine ring)
**Seat:** solar · **Probe cadence:** 120m
**Artifact gate:** read-state named; refusal class clean
**Loop-state:** `CONTINUE + SB2 (compensation retire)` · NO NEXT-LAUNCH

---

## 1. THE READ-STATE RECEIPT

The substrate's read spine as it stands at launch. The chair's frame from
`READ-RESTORE-DECISION-PREP-20261114.md` is read once; `R4-GROUND-20261114.md`
is read once (both receipts stamped `IN-LANE / BORROWED <source> / HEAD-RECON`).
Nothing here is re-derived — the day's work is paid; absent evidence stays absent.

**Wound — the read action removed.**
The `read` action was deleted at `56ee8a5cc6`. Current main answers
"Unknown action 'read'" — the substrate's read path is a scarred door. The
six fabrication class (`6/6 fabrications without the read`) opens at the wound;
the twelve-clean class (`12/12 clean refusals`) is only reachable behind the
restore head.

**Restore — OPEN, unmerged.**
`RFC #141876` is the restore. Its head is `af16e3ab16` (OPEN, unmerged).
Per the chair's frame, its head returns entries first-try — the restore
head is the probe seat for the ring: with it applied, the substrate must
answer read on the green path (12/12 clean refusals instead of 6/6
fabrications); without it, the red path holds.

**Vehicles.**
- `#11548 dispatch bootstrap` — OPEN. It is the vehicle that pulls the
  restore head into the dispatch path; status OPEN, first-try dispatch pending.
- `#116673 bounded read` — OPEN. Head `60a2e15638`. The bounded read gate
  that a restored `read` must pass before any entry is returned. Both
  vehicles stay OPEN at launch; the ring probes through them, never past them.

**Hold.**
Comment `6787192097` is the hold that pins the spine. It is a named hold on
the read-state: the door stays OPEN-UNMERGED-HOLD until the chair's decision
packet picks A/B/C. The hold does not block the probe — it blocks the merge.

**Label state.**
Label = P4. No maintainer triage decision has landed; the P4 label is the
free tier of the label chain, awaiting the chair's triage decision. Nothing
public is released while the label is still P4 with no maintainer decision.

**Receipts (stamped, not re-derived):**
- `IN-LANE / BORROWED READ-RESTORE-DECISION-PREP-20261114.md / HEAD-RECON`
- `IN-LANE / BORROWED REFS/R4-GROUND-20261114.md / HEAD-RECON`

---

## 2. THE 6/6 ↔ 12/12 PROBE PLAN (the ring's probe)

The exact runnable spec the night's first probe will execute machine-side.
Registered OWED; never fabricated. The machine-side executes per the
instrument-write rule; the run is a read-only probe of the two states.

**Red (6/6 fabrications without the read):**
Reproduce the scarred state exactly as launched: `56ee8a5cc6` on main,
`read` removed, `#11548` and `#116673` both OPEN. The probe asserts that the
substrate answers "Unknown action 'read'" and emits 6/6 fabrications. This
is the negative class; it must stay red at the wound.

**Green (12/12 clean refusals with the restore head):**
Rebuild the substrate from the restore head `af16e3ab16` (RFC #141876) with
vehicles `#11548` (dispatch bootstrap) and `#116673` (bounded read, head
`60a2e15638`) resolved. The probe asserts that `read` now returns entries
cleanly — the class flips to 12/12 clean refusals, no fabrication.

**Gate:** red is the wound state (always runs first); green is the restore
head state (the probe seat). The probe never writes the substrate — it only
verifies read-state; any mutation is a separate ring and registers OWED.

---

## 3. THE DOOR'S STATE LINE

`READ`  →  **OPEN-UNMERGED-HOLD** — the chair's packets are ready (A/B/C);
the probe reads, the hold pins, the merge waits for the chair's decision.

---

## 4. LOOP-STATE / RELOOP

`CONTINUE + SB2 (compensation retire)` — the next ring is SB2; the wheel's
cadence drives the probe. NO NEXT-LAUNCH: the head dispatches the rings per
the wheel's cadence; the chair's decision packets (A/B/C) wait for the
confirm gate before any public release. Kenari stays READ-ONLY; RFC QUIET.
