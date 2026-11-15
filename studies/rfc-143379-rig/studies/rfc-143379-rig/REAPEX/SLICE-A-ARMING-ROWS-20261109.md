# SLICE-A — THE ARMING-ROWS (t=0 operative record)
# Seat: launch-execution (solar), first pass, first lens
# Date: 2026-11-09 (t=0, mission FIRED)
# Register: plain, evidence-carrying. Direct-applicable.
# Depth-evidence: 5-why + webstorm (this lane's own), riding the landing.

## 1. ARMING-ROWS — G0-G4 thetas + owners + armed-state

| Gate | Theta (meter) | Owner | Armed state at T-? | Exit to next |
|------|---------------|-------|--------------------|--------------|
| G0 | θ0 = mission-intent lock (single-sentence goal, immutable for the hour) | SOLAR (launch) | armed T-0 (always on) | intent broadcast on GO |
| G1 | θ1 = dispatch-route primed (target surface + payload hash) | DISPATCH | armed T-15m | first dispatch on GO |
| G2 | θ2 = first-hour block loaded (6 items, timed, owner+exit per item) | SOLAR | armed T-10m | item #1 begins at t=0+15s |
| G3 | θ3 = go/no-go surface live (operator-visible, single signal) | OPS-CONSOLE | armed T-5m | flips GREEN-LOCKED on GO |
| G4 | θ4 = mission-clock re-anchor ready (t=0 trigger wired) | CLOCK | armed T-2m | re-anchor broadcast on GO |

Arming invariant: meters arm in order G0→G4 at decreasing T-offsets; no dispatch emitted pre-t=0; clock idle until operator's word.

## 2. DISPATCH-TRIGGERS — first-emissions on GO

| # | t= | Trigger | Emission | Gate |
|---|----|---------|----------|------|
| 1 | t=0+0s | G0 fires | mission-intent broadcast to all lanes (single sentence, immutable for the hour) | G0 |
| 2 | t=0+5s | G1 fires | first dispatch emitted to primary lane (payload hash verified) | G1 |
| 3 | t=0+15s | G2 fires | first-hour block item #1 begins | G2 |
| 4 | t=0+30s | G3 fires | go/no-go surface flips to GREEN-LOCKED (operator sees confirmed) | G3 |
| 5 | t=0+45s | G4 fires | mission-clock re-anchor broadcast; all lanes adopt t=0 | G4 |

Hard rule: no partial fire — GO fires the full sequence or nothing.

## 3. FIRST-HOUR'S SIX-ITEM BLOCK — execution order

| # | Time | Item | Owner | Exit criterion |
|---|------|------|-------|----------------|
| 1 | t=0+0m | Intent broadcast + clock re-anchor | SOLAR | all lanes ACK t=0 within 60s |
| 2 | t=0+10m | First dispatch lands on target surface | DISPATCH | delivery receipt logged |
| 3 | t=0+20m | First verification probe (read-back of item 2) | VERIFY | probe returns match |
| 4 | t=0+35m | Mid-hour checkpoint: drift check vs intent | SOLAR | drift = 0 or flagged |
| 5 | t=0+50m | Second dispatch (follow-on, conditional on #3 pass) | DISPATCH | gate cleared |
| 6 | t=0+58m | Hour-close: seal log, hand to next hour's plan | SOLAR | sealed artifact committed |

Conditional gate: item #5 fires only if item #3 exit criterion (probe returns match) holds.

## 4. DEPTH-EVIDENCE — this lane's own 5-why + webstorm

### 4.1 5-why (root-question: "why must the arming-rows be the first slice, not the plan-as-a-whole?")
1. Why first slice? Because t=0's clock restart is gated on the operator's single GO signal, and GO fires only when meters are armed; arming is the precondition, not the plan.
2. Why meters before dispatch? Because dispatch-triggers' first-emissions are sequenced emissions off armed meters; emitting from un-armed meters would be partial fire, which the hard rule forbids.
3. Why a single signal? Because multi-confirm introduces a second clock anchor; the re-anchor must be one instant or phase timing drifts.
4. Why drift matters? Because phase minutes (0–60/60–240/…) are measured from the restart-point; any ambiguity in t=0 corrupts every downstream gate check (dependency-collapse, compounding-rate, etc.).
5. Why this is systemic: the mission's amplification engine (≥2× growth, ≥2 fan-out) compounds on t=0 integrity; an ambiguous origin propagates as ungraded meters, and ungraded meters do not count toward standing. Remediation: lock arming-rows as the immutable first slice, byte-closure-triple verified before GO.

### 4.2 Webstorm (possibilities sweep, this lens)
- Mechanism A — arm-all-then-fire (chosen): meters arm at T-15→T-2m, GO fires full sequence. Adoption seam: OPS-CONSOLE single surface; meter: all lanes ACK t=0 within 60s.
- Mechanism B — arm-on-demand per gate: each gate arms only when its trigger approaches. Rejected: creates mid-flight arming windows and partial-fire risk; no meter for "armed in time."
- Mechanism C — pre-arm at deploy time: meters armed at deploy, clock runs from deploy. Rejected: clock runs before operator's word, violating restart-point contract (clock does not run before GO).

Chosen: A. Meter: G0-G4 all armed before GO; ACK-within-60s on item #1.

## 5. OPERATIVE STATUS at t=0
- Meters armed per §1 (G0 always-on; G1-G4 at their T-offsets).
- No dispatch emitted; clock idle; surface AMBER until GO.
- Slice-A is the complete operative record for t=0; no further decomposition required.
