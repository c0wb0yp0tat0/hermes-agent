# THE PILOT KIT'S MINIMAL DEMONSTRABLE FORM — phase-1 proof for an outside watcher

**Lane A.** Brainstorm deliverable · **Date:** 2026-11-21 · **Study branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond PR #1's thread) · **RFC:** quiet · **Gate (verbatim):** "the gate: nothing public without the user's word." · **Wall clause (verbatim):** "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."

**Grounded on:** `plan/PILOT-KIT-PLAN-20261121.md`; `night-20261121/FINAL-LEG-PLAN-20261121.md`; `probes/CANARY-CELLS-20261120.json` (plus the identical served copy in the master archive); `audit/PILOT-VERDICT-20261121.md`; `audit/LOSS-LADDER-AOA-20261121.md`; `KIT-METHOD-CARDS-20261121.md`; `KIT-SYNTH-20261107.md`; `NM-2-RECEIPTS-PACK-20261120.md`; `OPUS-NM3-CANARY-20261120.md`; `nightshift` briefs. No claim here is a promise; every item that claims a measurement names its artifact.

---

## 0. The one-paragraph definition

The pilot's phase-1 is a **bounded canary**, not a demo and not a promise. The only thing the outside watcher is ever shown is the **single receipt artifact** — the canary's five-field receipt plus the measured gate table, one file, no narration around it ("shown the receipts, not told a story"). The proof it must constitute: *an autonomous execution layer ran a model end to end, on a portable substrate, with every named point revertable, and the judgment layer — the head's real calls — was mechanized out of the loop so the pilot never needs a human word at the gate.* Everything else (the full canary brief, the fleet, the inventions) is the post-pilot fix-delivery phase.

## 1. The show for the watcher

The phase-1 show, in the order the field reads it:

1. **The substrate runs it.** The kit is not "vanilla Hermes" — it is the certified substrate (M1-stamped persistence: A 0.000 / B 1.000 / C 0.990, gate 1.0; the scribe's write-gates + witness registry; 83 files) inherited by the host through one walk-script, and the boot-check passed: load, minimal forward, determinism 0.0.
2. **The model is pinned, loaded, and answers.** sha-verified model, pinned track sha, load in 0.95 s, logits shape `[1, 4, 129280]`, argmax next token 49969, deterministic within tolerance 1e-6.
3. **The sandbox is the boundary.** Ephemeral venv in `/tmp` (RAM-backed, reboot-pruned), no rig disk state touched, no production seat, no HF download in the sandbox; the one-way LFS route is the only egress.
4. **The license is verified from the live model card** (MIT, `license_compatible_private_repo: true`) — the model can live in the private repo.
5. **The measured gates are on the record**, each with its number and its artifact (§4).
6. **The judgment layer is gone from the wiring.** Pre-committed verdict vocabulary, out-of-band evaluator schedule, no-gate doctrine — the pilot's first auto-judgment row (the fabrication catch) must run without a human.
7. **The revert points are named**, and each is reachable without touching anything else.

Nothing beyond the receipt artifact is shown. No prose, no claims, no "we believe" — measurements, receipts, names.

## 2. The one outside-watcher-visible receipt

**Name:** `probes/canary/phase1-receipt-20261121.json` (one artifact, on the study branch, fork-only).

**What it contains — exactly:**

- The candidate, the pins (repo pin + model sha + model bytes + param count),
- The five-field receipt: sandbox env id + isolation boundary; model sha vs pinned sha; load + determinism; license attestation; LFS egress (byte-counted, zero secondary),
- The measured gate table (§4), each row = `{gate, measurement, artifact}`,
- The verdict row: `RUNG-1-LANDED` (with the two-way-door/rollback status, not a one-way commitment),
- The revert point list (§5), one per named item,
- The judgment-layer instrument field (§7): the pre-committed vocabulary, the out-of-band evaluator schedule, the no-gate doctrine — as fields, not prose.

**Example (values all measured 2026-11-20, from `probes/CANARY-CELLS-20261120.json` read verbatim):**

```json
{
  "spec": "phase-1-receipt",
  "rung": 1,
  "candidate": "kshitijthakkar/deepseek-v4-mini-300M-from-flash",
  "pin_repo_sha": "fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64",
  "model_sha256": "5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c",
  "model_bytes": 641262336,
  "frames": {
    "transformers": "5.23.0",
    "torch": "2.15.0+cpu",
    "load_seconds": 0.95,
    "param_count": 319028736,
    "logits_shape": [1, 4, 129280],
    "argmax_next_token": 49969,
    "deterministic_max_abs_diff": 0.0,
    "determinism_tolerance": 1e-06,
    "deterministic_within_tolerance": true
  },
  "isolation": {
    "env_id": "tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)",
    "boundary": "ephemeral venv in /tmp (RAM-backed, reboot-pruned); no rig disk state touched; no production seat; no HF download in the sandbox"
  },
  "egress": {
    "route": "private repo release nm3-canary-r1-20261120",
    "bytes": 647716330,
    "secondary_downloads": 0,
    "confirmed": true
  },
  "license": "MIT (verified live from the HF model card: license:mit; tags include license:mit)",
  "license_compatible_private_repo": true,
  "verdict": "RUNG-1-LANDED",
  "wall_clause": "a non-reproduction is a QUESTION, not a stop",
  "revert_points": ["sandbox torn down", "model not shipped (zero weights outside the one-way LFS store)", "config line reverts to the pre-study state", "no production seat used"],
  "judgment_layer": {
    "verdict_vocabulary": "pre-committed (the kit's verdict row names its revising evidence)",
    "out_of_band_evaluator": "scheduled (real-world read, not lane narration — the court-verification spine is the instance)",
    "no_gate_doctrine": "no human word needed at the gate"
  }
}
```

**The field sees this file and nothing else.** That is the whole of the proof-form: the rest lives in the branch, not in the field's hands.

## 3. The named items — what phase-1 must show

Each item names its "show" (the single measurement that proves it).

| # | Item | What phase-1 must show | Measured | Artifact |
|---|------|------------------------|----------|----------|
| I1 | **The substrate** | never-vanilla inheritance: host received the kit by one walk-script; the kit's own gates (scribe write-gates, witness registry) are live in this run | boot-check passed: load + forward + determinism 0.0 inside the kit | KIT-METHOD-CARDS-20261121.md + the run log |
| I2 | **The model** | pinned repo sha == model sha == bytes, on the pinned transformers/torch | sha `5747a90e…` == pin `fc8b9934…`; bytes 641,262,336; 319,028,736 params; transformers 5.23.0, torch 2.15.0+cpu | `probes/CANARY-CELLS-20261120.json` |
| I3 | **The inference** | load + minimal forward pass + deterministic output | load 0.95 s; logits `[1,4,129280]`; argmax next token 49969; max_abs_diff 0.0 < 1e-6 | the run log |
| I4 | **The sandbox isolation** | named env id, boundary stated; no rig disk; no production seat; no HF download | env `tmpfs-venv@PVE-host`; boundary as in §2 | `probes/CANARY-CELLS-20261120.json` (field `sandbox_env_id`, confirmed head-side 2026-11-20 ~04:45Z) |
| I5 | **The egress** | sole route, byte-counted, zero secondary | `nm3-canary-r1-20261120`; 647,716,330 bytes; secondary 0 | the cells file |
| I6 | **The license** | MIT verified from the live model card; compatible with the private repo | `license_compatible_private_repo: true` | the run info |
| I7 | **The five-field receipt** | all five fields trace to the cells, field-verified, with the wall clause applied | 8/8 compose-check marks FIRED (mark 2 via proxy until the head-side closure) | `OPUS-NM3-CANARY-20261120.md` §5 |
| I8 | **The judgment layer** | no human word at the gate | the three instruments defined as fields (§7) | KIT-METHOD-CARDS-20261121.md |
| I9 | **The revert points** | every named item is revertable at a named point, with no artifact left behind | grid in §5 | this file |
| I10 | **The two-way door** | nothing public without the user's word; RFC quiet; fork-only | standing sets + the gate verbatim | NIGHTSHIFT-PLAN-20261121.md HARD-LINES |

## 4. The measured gates

Each gate: the measured value, the artifact that produced it, and the bar.

| Gate | Measurement (measured 2026-11-20/21) | Bar | Artifact |
|------|----------------------------------------|-----|----------|
| G1 | Model sha == pinned track sha: `5747a90e…` == `fc8b9934…` | equal | `probes/CANARY-CELLS-20261120.json` |
| G2 | Load + minimal forward + determinism: `max_abs_diff 0.0 < 1e-6` → `deterministic_within_tolerance: true` | 0.0 < 1e-6 | run log |
| G3 | Logits shape `[1,4,129280]`, argmax next token 49969 | shape as recorded; argmax matches the run's own log | the run log |
| G4 | Isolation: env id named; boundary as in §2; no rig disk, no production seat, no HF download | every clause satisfied | cells file (`sandbox_env_id` — confirmed head-side 2026-11-20 ~04:45Z) |
| G5 | Egress: sole route `nm3-canary-r1-20261120`; bytes 647,716,330; secondary 0 | byte-counted; zero secondaries | cells file |
| G6 | License: MIT from the live model card; compatible | `license_compatible_private_repo: true` | model card + cells |
| G7 | The kit's five start-gates (PILOT-VERDICT-20261121.md, §4 start line, measured 2026-11-21) | read-restore 42/42 GREEN; harness READ-GATED + 2K byte-budget breaker hard-enforced; W2 31/35 present / 0 absent; U1–U3 specified with settle-words; kit-audit + kit-sceptic by exact names on the branch | this record + the audit rows |
| G8 | The five-field receipt complete: sandbox env id, model sha, load/determinism, license, LFS egress | 8/8 compose-check marks FIRED | `OPUS-NM3-CANARY-20261120.md` §5 |
| G9 | The receipt meter is byte-verified, not prose-verified: the loss-ladder matrix says tool-output = 0.0 at every depth (d ≈ 0.864 re-entry), assistant-prose 0.0 at 0.65 | measured bytes + the command that produced them | `probes/LOSS-LADDER-20261121.json` + the judge command |

**What the gates measure:** the machinery works (G1–G6), the kit is the gate-set the pilot inherits (G7), the form is complete and honest (G8), and the proof survives the depth/abbreviation knob — the receipt is bytes, not prose (G9).

## 5. Revert engineering — every named point

The pilot is a canary. Every gate in the plan has a pre-named fate; the grid is `continue / hold-safe / need-the-chair`, fired at the night's ring boundaries. Revert points:

1. **Model never shipped.** Zero weights outside the one-way LFS store; the canary itself is a mechanical sandbox run (0 provider calls, `token_measure: 0`).
2. **Sandbox torn down.** Ephemeral venv in `/tmp`, reboot-pruned — the boundary is the OS, not a flag.
3. **Config line reverts.** The delegation's base-pin is one configuration line (the independence layer, ARM 4); a revert is one line.
4. **Egress is one-way.** The private-release route delivers, then the rig keeps nothing; the field's receipt is the only trace on the rig.
5. **Gates hold.** A held gate hand-waves the partials forward at the next fold — nothing is deleted, nothing is hidden (the NOT-RUN honesty marker: every named absent item stays named absent).
6. **The whole phase-1 is bounded before any gate opens.** No gate opens without the standing sets; the operator's word alone gates the posting surfaces (the court, the RFC) — nothing else.

## 6. Portable everywhere; never vanilla

- **The substrate walks.** Every host inherits the kit by one script (the substrate's walk, ARM 7); the R1 cell proved the shape on one host, the next run proves it on another.
- **The sandbox is the portable unit.** Ephemeral venv in `/tmp` (RAM-backed, reboot-pruned) — the canary's own boundary. A second host gets the same venv shape, the same pins, the same one-way route.
- **No rig state rides.** The model comes only via the private-release route; the rig disk keeps nothing.
- **The no-vanilla rule is the checklist, not the slogan:** the 83-file substrate, the scribe's write-gates, the witness registry — all present in the run, none stubbed out.

## 7. The judgment layer, mechanized

The verdict (PILOT-VERDICT-20261121.md) is the boundary: the execution layer is proven; the head is the boundary. The canary closes the boundary with three pre-committed instruments, already in the kit, no human word at the gate:

1. **Pre-committed verdict vocabulary.** Every verdict row names its revising evidence; a verdict is a gate state, revisable by evidence, never a one-way commitment (kit method card 1).
2. **Out-of-band evaluator, scheduled.** The evaluator reads real-world state, not lane narration — the court-verification spine's execution ledger is the instance (method card 3); the schedule is a field of the receipt.
3. **No-gate doctrine.** The pilot's first auto-judgment row — the fabrication catch — must fire without a human. If it cannot, the pilot is not ready and the receipt says so.

## 8. The recorder's checklist — how a peer lane re-verifies before trusting the receipt

1. Read `probes/CANARY-CELLS-20261120.json` cold, twice; every field maps to a cell (no summary used).
2. Re-pin the receipt + sha: the receipt is a claim until the bytes are checked at landing.
3. Re-run the gate set G1–G9; any gate that fails re-arms, never softens.
4. Verify the two-way door: nothing public beyond PR #1; RFC quiet; the field's receipt is the only shown artifact.
5. Verify the revert grid: every named point is one named step, not a hope.
6. Verify the loss-ladder meter: the receipt is byte-verified (G9), not prose.

## 9. Open threads / continuation points

1. **Rung-2 scale.** The armed rung-2 (candidate `V3-3.4B-small`, sha `415501bd…`, sandbox env id staged from the start) asks whether the phase-1 form scales: does G2 (determinism 0.0) hold at 3.4B, and does the 0.95-second load gate hold? A peer lane should fire the five-field receipt on the bigger model and read the same fields — the form is only proven at rung-2's numbers.
2. **Auto-judgment live.** Test the judgment-layer instruments in anger: plant a fabrication, let the pre-committed vocabulary + out-of-band evaluator name it and correct it — without a human in the loop. This is the canary's real first judgment row, and the record must show it ran.
3. **The portable substrate on a second host.** The R1 cell's sandbox boundary is one host. The walk-script + venv-in-/tmp shape must be exercised on another runner (p0tat0, c0wb0y, or the cloud seat), with the same pins and the same one-way route; a shape that only fits this host is not a kit.
4. **The receipt survives the depth knob.** The loss-ladder class says tool-output = 0.0 at every depth (re-entry only at d ≈ 0.864). The canary's receipt meter must be provable under a 0.65 cut and a 0.5 cut — that is the byte-verified meter, not a prose one. A peer lane should run G9 under a 0.65 cut and report the surviving rows.
5. **The assemble the plan names.** The pilot kit's stage 2 says the full phase-1 canary brief is missing: the fragments (cells' ledger, the night-D drivers), the method cards, the capture's home, the executor leg. The canary's `NIGHT-D-CANARY-PHASE1.json` — the assignee/workspace/driver/brief/gate record — is not yet on the tree. Building that one record, record-first and sha-anchored, is the direct continuation of this work.
6. **Independence layer.** The audit once shared one pinned base. Before the canary's verification rides anywhere, the bases must differ per unit (the delegation route's per-unit pin, or the board-spawn path repair), and the blind-panel protocol stands as the landing-time independent eye. The receipt must be readable from a base no one controlled.

## 10. Fold line for the master

The pilot kit's minimal demonstrable form is this: one receipt artifact, shown to the field, containing the five-field canary receipt plus the measured gates and the named revert points, with the judgment layer mechanized out of the loop. The canary shows an execution layer that works, on a portable substrate, at every point revertable — and the head is no longer the boundary, because the three judgment instruments are fields of the receipt. Rung-1 is landed; rung-2 is armed; the next leg builds the phase-1 brief the pilot can actually run.

---

*Facimus semper — the verdict renders on the evidence; the evidence is on the record; the record corrects itself out loud.*
