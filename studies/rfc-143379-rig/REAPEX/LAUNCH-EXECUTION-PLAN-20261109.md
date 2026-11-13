# SOLAR — THE GOAL-DRIVEN LAUNCH'S EXECUTION-PLAN
# Seat: launch-execution (the mission's /goal-driven part)
# Date: 2026-11-09
# Doctrine: solar DOES the launch's goal-driven part; the clock restarts at its
# beginning; the teams set it up so the operator's word fires the max.

## 1. LAUNCH-SEQUENCE — exact first-fires

### 1.1 Meters' arming-rows (G0-G4 thetas + owners)
| Gate | Theta (meter) | Owner | Armed state at T-? |
|------|---------------|-------|---------------------|
| G0   | θ0 = mission-intent lock (single-sentence goal locked) | SOLAR (launch) | armed at T-0 (always on) |
| G1   | θ1 = dispatch-route primed (target surface + payload hash) | DISPATCH | armed T-15m |
| G2   | θ2 = first-hour block loaded (6 items, timed) | SOLAR | armed T-10m |
| G3   | θ3 = go/no-go surface live (operator-visible, single signal) | OPS-CONSOLE | armed T-5m |
| G4   | θ4 = mission-clock re-anchor ready (t=0 trigger wired) | CLOCK | armed T-2m |

### 1.2 Dispatch-triggers' first-emissions (on go)
1. t=0+0s  — G0 fires: mission-intent broadcast to all lanes (single sentence, immutable for the hour).
2. t=0+5s  — G1 fires: first dispatch emitted to primary lane (payload hash verified).
3. t=0+15s — G2 fires: first-hour block item #1 begins (see 1.3).
4. t=0+30s — G3 fires: go/no-go surface flips to GREEN-LOCKED (operator sees confirmed).
5. t=0+45s — G4 fires: mission-clock re-anchor broadcast; all lanes adopt t=0.

### 1.3 First-hour's six-item block (literal times, t=0 = clock restart)
| # | Time | Item | Owner | Exit criterion |
|---|------|------|-------|----------------|
| 1 | t=0+0m  | Intent broadcast + clock re-anchor | SOLAR | all lanes ACK t=0 within 60s |
| 2 | t=0+10m | First dispatch lands on target surface | DISPATCH | delivery receipt logged |
| 3 | t=0+20m | First verification probe (read-back of item 2) | VERIFY | probe returns match |
| 4 | t=0+35m | Mid-hour checkpoint: drift check vs intent | SOLAR | drift = 0 or flagged |
| 5 | t=0+50m | Second dispatch (follow-on, conditional on #3 pass) | DISPATCH | gate cleared |
| 6 | t=0+58m | Hour-close: seal log, hand to next hour's plan | SOLAR | sealed artifact committed |

## 2. MISSION-CLOCK's RESTART-POINT

- What marks t=0: the operator's go-signal (single signal, see §3) crossing the
  threshold on the go/no-go surface. Not a timer. Not a deploy. The operator's
  word is the only event that sets t=0.
- What fires exactly then (t=0+0s):
  - G0 mission-intent broadcast (immutable for the hour).
  - Mission-clock re-anchor: all lanes reset their local clocks to t=0.
  - First-hour block item #1 begins.
- Pre-t=0 state: meters armed per 1.1; no dispatch emitted; clock holds at T-0
  (idle, not running). The clock does not run before the operator's word.

## 3. OPERATOR's WORD's MECHANISM (go/no-go surface)

- What the operator sees: a single console surface (OPS-CONSOLE, G3) showing
  - the locked mission-intent sentence (G0)
  - the six-item first-hour block with owner + exit criterion (G2)
  - meter status row G0-G4 (armed / not-armed)
  - one button: GO. One button: NO-GO.
- The single signal that fires everything: operator presses GO.
  - On press: G3 flips to GREEN-LOCKED, G4 fires the clock re-anchor, and the
    §1.2 sequence begins. No other input is required; no second confirmation.
  - NO-GO: surface stays AMBER, nothing fires, clock stays idle, meters remain
    armed. Operator may re-press GO later; same single-signal semantics.
- Hard rule: no partial fire. GO either fires the full §1.2 sequence or fires
  nothing. There is no "soft launch."

## APPLICABILITY
Direct-applicable. The fire-sequence, t=0's contents, and go-trigger above are the
exact execution contract for this launch. No further decomposition required.
