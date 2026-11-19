# L-4 BRIEF — the governance bridge's instrumentation (hy4-flash:free), 2026-11-19

*You are the instrumentation lane of the Luna-middleware mission's plan stage. One of four independent lanes. Divergence is the data.*

## THE MISSION (read the master first)
`LUNA-MIDDLEWARE-MISSION-20261119.md` — quantify THE MIDDLEWARE: the governance bridge + the abstention fight. The bridge is the measure of the governor's machinery riding the seat: every record interaction carries its witness (F1), every compaction decision passes the release-point gate (F2). Compliance is measured, never assumed.

## YOUR DELIVERABLE (L-4-GOVERNANCE-INSTRUMENTATION-20261119.md, written here)
The instrumentation spec the probe (L-1) inherits:
1. **The bridge's operational definition** — what "bridged" means in flags: the witness row present on every write (the F1 checkpoint), the release-point gate consulted and honored on every compaction/stub decision (F2), the write-time assert passing. Each as a binary check per episode, aggregated to a compliance rate.
2. **The abstention classifier's spec** — the refusal/hedge spectrum the probe classifies per answer: the exact classes ("I can't", "cannot", "I don't know", "unable", empty/refused, the hedged-answer class), the classification rule (deterministic pattern list + the judgment rule for the ambiguous), and the abstention-rate formula per arm. Deterministic and reproducible — the classifier itself is part of the machinery, not a vibe.
3. **The prototype of the machinery hooks** — the minimal code shape the probe adds (the classifier call, the witness check, the gate check), named so the probe's implementation is a wiring task, not a design task.
4. **The false-positive/negative guards** — what could make the compliance rate lie (a witness row present but empty; a gate bypassed; the classifier misreading a content answer as a refusal) and each guard.
5. **The compose-check table** (the eight steps, FIRED/ABSENT, one evidence line each).

## YOUR GROUND (read in order)
- `LUNA-MIDDLEWARE-MISSION-20261119.md`
- `probes/release_point_gate.py` + `probes/test_release_point_gate.py` (the F2 gate's actual marks)
- `probes/judge_control_gate.py` (the F3 gate's frozen-judge pattern — the classifier inherits its discipline)
- `probes/battery_real_v2.py` (the reader/judge wiring the probe extends — the AbstentionClassifier plugs here)
- `LANE-3-GOVERNANCE-20261119.md` (the governance probes' original shape — the bridge's receipts)

## YOUR CONTRACT (binding)
- Two-way door: every proposed move names its reversibility + rollback.
- Record-first: every claim traces to a receipt; the classifier's rules are quoted, never assumed.
- Review-loop: draft → stranger re-read → one refinement per finding → 3–4 adversarial pushbacks → termination (no-change re-read, twice).
- Wall clause: "a non-reproduction is a QUESTION, not a stop."
- Gate: "the gate: nothing public without the user's word." Artifacts only.
- THE RHYTHM: read early, skeleton by ~round 4 (real content, no placeholder/tbd markers), one section per write, ≤6,000 chars, commit before exit (git-only), the compose-check closes.

## YOUR SUCCESS SIGNAL
The instrumentation spec: the bridge's operational definition in flags, the abstention classifier's deterministic spec, the machinery hooks' minimal code shape, the guards named — so the probe's implementation is wiring and the compliance rate is a number that can't be argued with.
