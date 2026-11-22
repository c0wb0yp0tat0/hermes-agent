# CANARY PHASE-1 DESIGN — RUNNABLE BRIEF (LANE B)

Date: 2026-11-21 (the canary's phase-1 brief; the day of the final leg's last invent-and-simplify ring)
Seat (named rotation): kenari reserve beam (`reflection/beam-1.0-501b-a23b`) — R-C executor (select leg, probe-before-use, STEER-10); verifier pair (Conflict-1, non-author): longcat + solar-mini4
Branch: study/rfc-143379-rig-20261105 · **RFC: quiet** · **Gate: the gate — nothing public without the user's word**
Doors: the fork only · nothing public beyond PR #1 · the operator's word gates only the posting surfaces (the court's posting, the RFC's surface, the autopilot's pilot gate, the voice-check's shape)
The pilot gate: standing sets only; no human word needed for the pilot to run
The canary's rung-1 candidate: `kshitijthakkar/deepseek-v4-mini-300M-from-flash`
The canary's pinned repo sha: `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`
The canary's safetensors sha (cell plan): `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c`
The canary's egress sole route: private repo release `nm3-canary-r1-20261120` (sole route)
The method cards' home: `studies/rfc-143379-rig/KIT-METHOD-CARDS-20261121.md` (the kit folder: the four cards + the audit + the sceptic, by exact names)
The wall clause: **a non-reproduction is a QUESTION, not a stop — simplify until the seam is exercised**

---

## 0 · ENVELOPE — scope, clock, doors

**What this brief covers.** The canary's full phase-1 spec, assembled from the cells' ledger + the rung-1 receipt + the judgment-layer mechanization: the named items, the measured gates, the revert points, the sole-egress discipline, the pre-committed verdict vocabulary, the out-of-band evaluator's schedule, the no-gate doctrine. One document; the pilot runs it as a bounded canary behind standing sets.

**What this brief does NOT cover.** The RFC-facing inventions — the read-gap fix's design, the doc-chain's UX, the compaction's release condition — belong to the post-pilot fix-delivery phase, AFTER the pilot runs. This leg invents nothing public; it wires what the kit already certifies.

**The standing doors (the pilot needs no human gate):**
- the fork only (external verification instruments may land, blind-panel style);
- nothing public beyond PR #1's thread;
- RFC quiet;
- the user's word is the only gate beyond the standing sets;
- landings verified before claims (verify → fold → row).

**The clock.** Rings run 40–60 min; the re-grounding crons ride every 2h; the cadence cron every hour; the ACES-trigger stands at the 6-hour mark (no check-in → the improve/audit/review loop fires over the landings themselves — the kaizen spine, the loop improving the loop).

**The end-state this leg targets.** The pilot kit, ready: the canary's brief audited by the rotation (gate: the audit's marks + the pilot's receipt), the kit's certifications closed behind phase-1, the verification independent, the egress sole-route discipline held, the RFC-facing inventions parked after the pilot.

---

## 1 · THE CANARY'S ITEMS (named items, each a gate state)

| # | Item | State | Receipt anchor |
|---|---|---|---|
| 1 | Rung-1 cell identity (candidate + pinned repo sha) | FIRED | `CANARY-CELLS-20261120.json` cell; pin `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` |
| 2 | Model sha match (safetensors) | FIRED | `5747a90e…` vs pin `fc8b9934…`; bytes `641,262,336` |
| 3 | Load + minimal forward + determinism | FIRED | load `0.95s`; params `319,028,736`; logits `[1,4,129280]`; argmax `49969`; max abs diff `0.0` (< `1e-6`) |
| 4 | Licensing attestation | FIRED | `license: mit` (verified live from the HF model card); `license_compatible_private_repo=true` |
| 5 | Egress single-route, byte-counted, zero secondary | FIRED | sole route `nm3-canary-r1-20261120`; bytes `647,716,330`; secondary `0` |
| 6 | Sandbox env contract | FIRED (verified from cell; pilot re-verifies at run) | `tmpfs-venv@PVE-host`; isolation boundary named; no rig disk state; no prod seat; no HF download in sandbox |
| 7 | Record-first wall clause | FIRED | field (1) recorded as "not confirmed" first; closed head-side only after the cell carried the key |
| 8 | Two-way door / rollback | FIRED | sandbox torn down; LFS one-way; rollback = no commitment made |
| 9 | Method card 1 as canary's first certified use (the pilot's judgment-layer first-catches) | RUNNING | `KIT-METHOD-CARDS-20261121.md` card 1 + `PILOT-VERDICT-20261121.md` (the canonical instance) |
| 10 | Method card 2 (improvement-loop honest termination) | RUNNING | the ACES trigger at the 6-hour mark (standing) |
| 11 | Method card 3 (byte-verified receipt meter + out-of-band evaluator) | RUNNING | the court-verification spine's execution ledger (the night's instance) |
| 12 | Method card 4 (fail-safe grid + fold-and-re-anchor) | RUNNING | the night-shift plan's gates (the standing instance) |
| 13 | Capture home for the canary's phase | FIRED | the kit folder: cards + audit + sceptic, by exact names |
| 14 | Gate-state file (the operator's read surface) | OPEN | the field-facing moment = the rung-1 canary's receipt on the operator's read |
| 15 | Judge-gate (per-ring re-read of the five gate fields) | OPEN | the evaluator's schedule (section 5) |

The four method cards are the canary's certified first uses; they ride the pilot exactly as the kit owns them (the cards' receipt shapes are measurable; no card is invented here).

---

## 2 · MEASURED GATES (the start line, measured 2026-11-20 04:41:38Z → 04:41:43Z)

| # | Gate | Measured | Verdict | Receipt |
|---|---|---|---|---|
| G1 | Model sha == pinned repo sha (safetensors) | pin `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`; safetensors `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c`; bytes `641,262,336` | **PASS / CONFIRMED** | cell fields `model_safetensors_sha256`, `model_bytes`, `pinned_repo_sha` |
| G2 | Load + minimal forward + determinism | load `0.95s`; params `319,028,736`; logits `[1,4,129280]`; argmax `49969`; max abs diff `0.0` (< `1e-6`) | **PASS** | cell fields `load_seconds`, `param_count`, `logits_shape`, `argmax_next_token`, `deterministic_max_abs_diff` |
| G3 | Licensing attestation | MIT verified live from HF model card (`license: mit`); `license_compatible_private_repo=true` | **PASS** | cell field `license` |
| G4 | Egress single-route, byte-counted, zero secondary | sole route `nm3-canary-r1-20261120`; bytes `647,716,330`; secondary `0` | **PASS** | cell fields `egress_route`, `egress_bytes`, `egress_secondary_downloads` |
| G5 | Sandbox env contract (envelope) | `tmpfs-venv@PVE-host` (kernel `7.0.14-16-pve`); isolation boundary named; model pulled ONLY via the private-release route; no rig disk state; no prod seat; no HF download in sandbox | **PASS** (assertion, verified from cell; pilot re-measures at run) | cell field `sandbox_env_id` |
| G6 | Record-first five gate fields | field mapping unchanged a second cold re-read; no invention introduced | **PASS** | `PILOT-VERDICT-20261121.md` §2 |
| G7 | Verdict row at the named commit | **R1 LANDED** (receipt complete; rung-2 conditions armed) | **PASS** | `OPUS-NM3-CANARY-20261120.md` §4 + §6 |
| G8 | Compose-check table (8 marks) | all 8 FIRED (mark 2 via proxy) | **PASS** | `OPUS-NM3-CANARY-20261120.md` §5 |

**The cell battery rule.** A pilot run is a battery, not a demo: every gate above is measured, named, and recorded raw. Nothing is smoothed, nothing carried from the lane's narration.

---

## 3 · REVERT POINTS (the revertible design)

Every gate gets a named revert point. The revert discipline: the pilot runs in a ram-backed sandbox (`/tmp`, reboot-pruned); model files pulled ONLY via the private-release route; no rig disk state; no production seat; no HF download in the sandbox. **The rollback is no commitment made.**

| # | Gate | Revert point | Trigger | Mechanism |
|---|---|---|---|---|
| R1 | Cell install | remove the repo; nothing persisted | sha mismatch, or load fails | the sandbox is torn down; the install is additive and deleted on revert |
| R2 | Model load | abort before any forward | load_seconds above the barrier, or params != `319,028,736` | the load is a probe; the forward never runs on a bad install |
| R3 | Determinism | no assertion pass | max abs diff ≥ `1e-6` | the run is recorded as a probe, never a verdict; the run never burns rung-2 resources |
| R4 | License | no egress | `license_compatible_private_repo` is false | the model is not compatible; the release route is untouched |
| R5 | Egress | no secondary downloads | `egress_secondary_downloads > 0` | the store is one-way, byte-counted; a second download aborts the run |
| R6 | Isolation | sandbox torn down | the envelope contract not verifiable | the isolation boundary is named and checked at run time |
| R7 | Gate-state file | last-good revision frozen | any gate fails | the file is additive and revisioned; the last PASS revision is the rollback point |
| R8 | Capture home | deletion reverts | the fold lands the file; nothing behind it | the fold is additive (the kit folder shape — cards + audit + sceptic) |
| R9 | Judge-gate re-reads | no gate written without a measured receipt | a re-read shows a drift | the evaluator's verdict row carries the independent read |
| R10 | The ACES trigger | the improver loop stops on a measured plateau (no-change twice) | the loop fires | the termination is itself receipted, twice over |

Revert rule: a failed gate freezes the run's verdict row at PARTIAL / GAP and re-arms the same item at the next ring — never a silent skip, never a re-run with different values.

---

## 4 · EGRESS SOLE-ROUTE DISCIPLINE (the cells' egress cells)

The canary's egress is a single-route rule, from the cells' ledger:

1. **The sole route.** Private repo release `nm3-canary-r1-20261120`; this is the only egress a canary phase-1 run may use. No mirror, no secondary copy on the rig.
2. **The egress form.** One-way store, byte-counted: `egress_bytes` = the model's bytes (`647,716,330` for the rung-1 cell), `egress_secondary_downloads` = `0`.
3. **The pull rule.** Model files are pulled ONLY via the private-release route. The sandbox never reaches HF for the model files.
4. **The verification rule.** At run time the pilot must produce its own egress receipt: the model's checksum == the pinned sha; the byte count == the cell's; the secondary count == `0`. The egress receipt is written by the pilot, not carried from the lane.
5. **The no-state rule.** No rig disk state touched; no production seat; no HF download in the sandbox. The sandbox envelope is the isolation boundary; the pilot re-measures it at run (G5).
6. **The audit rule.** The verification is independent: an out-of-band read of the release (the evaluator's schedule, section 5) re-checks the bytes against the cell plan without the lane narrating them.

The egress cells' discipline is the cells' own: one store, byte-counted, sole-route, no secondary, no mirror, no state.

---

## 5 · JUDGMENT-LAYER MECHANIZATION (the fixtures)

The judgment layer is the boundary class (the head's calls). The pilot's gates are standing sets — the pilot fires as a bounded canary behind them; no human word is needed to run. The three fixtures are pre-committed in this brief; each already exists in the kit and rides the canary as a named instrument.

### F1 — The pre-committed verdict vocabulary

Every verdict is a **gate state**, revisable by evidence, never a one-way commitment. The vocabulary is fixed here, with its receipt shape and its two-way door:

| Verdict row | When it fires | Receipt shape | Two-way door |
|---|---|---|---|
| **LANDED** | The gate's measured value is at its named bar | the measured count + the command that produced it | revised by evidence at the next row |
| **PARTIAL** | The gate is at the bar minus a named seam | the seam named + the measured gap | a normal row; the seam becomes the next finding |
| **GAP** | The gate cannot be measured in the pilot's hands | the missing measurement named | the grid re-arms the item at the next ring |
| **QUESTION** | A non-reproduction — the seam must be exercised | the seam named + the measurement asked for | the lane simplifies until the seam is exercised |
| **REVERTED** | A revert point fired mid-run | the revert point + the trigger | the revert is the row's own fold |
| **CLOSED** | The finding is settled | the settlement's receipt | closed by the record's correction machinery |

The pilot's verdict rows land in the gate-state file (item 14) with their revisions; nothing is committed to the record without its bytes.

### F2 — The out-of-band evaluator's schedule

The evaluator reads real-world state, not the lane's narration (the byte-verified meter: a measured count + the command that produced it; an evaluator's verdict row with its independent read).

- **At each ring (40–60 min):** the evaluator re-reads the five gate fields (G1–G5) from the record, comparing the live values against the cell plan; a drift row is written, never a claim.
- **At every landing:** the independent evaluator's verdict row with the independent read (the longcat + solar-mini4 pair, Conflict-1, non-author).
- **Before any claim lands:** the evaluator's row must carry a receipt the lane did not write (the same rule that caught the arc's fabrications).
- **The ACES trigger (6-hour mark):** the improver loop stops on a measured plateau (no-change twice); the termination is receipted twice over; the loop's own form is the gift.

### F3 — The no-gate doctrine

- The pilot's gates are the standing sets above — the pilot runs without a human word.
- The operator's word gates only the posting surfaces: the court's posting, the RFC's surface, the autopilot's pilot gate, the voice-check's shape. All named; all waiting; none on this leg's critical path.
- The fork is open for external verification instruments (blind-panel style, when the independence layer lands in stage 3).
- The pilot gate never needs a human word; the pilot gate is the estimate's own receipt.

### F4 — The fail-safe grid (per gate)

Every gate in this brief has a pre-named fate; the grid's row per gate; the fold lands deterministically and the anchor re-roots the chain:

| Gate | Fate pre-named | If the fold breaks |
|---|---|---|
| G1–G5 (cell battery) | continue → hold-safe → need-the-chair | the item re-arms at the next ring; the verdict row freezes at PARTIAL/GAP |
| G6–G8 (record) | continue → hold-safe | the record is rewritten from bytes, never narration |
| G9–G12 (cards) | continue → hold-safe → need-the-chair | the card's first use is a probe; the card's receipt shape is re-measured |
| G13–G15 (continuity) | continue → need-the-chair | the capture home folds additively; the open thread is named, not hidden |

### F5 — The receipt stamp

Every claim lands with its receipt in the same breath: the artifact + sha at the moment of landing + the command that produced it + the evaluator's independent row.

---

## 6 · THE AUDIT PASS (the gate for this leg)

The gate for ARM 3 (the canary's full phase-1 spec): the rotation's audit pass, held by the verifier pair (longcat + solar-mini4), non-author adjudicators of record.

**The audit's battery.** The audit re-reads the canary's phase-1 brief cold, with the same discipline as the read-restore suite (42/42):

- every item in the brief is traceable to a receipt (the kit's audit rule: receipts, never claims);
- every gate has a measured value (the cell battery, section 2);
- every revert point is named (section 3);
- every egress item is a sole-route rule (section 4);
- every judgment-layer fixture has a receipt shape + a two-way door (section 5).

**The audit's verdict.** The brief passes at LEVEL 1 when every item, gate, revert point, egress rule, and judgment fixture above is present with its receipt anchor; at LEVEL 2 when the pilot's own receipt (the rung-1 canary's receipt on the operator's read) is on record. The audit's marks are rows, not a verdict of the pilot's worth.

---

## 7 · THE CANDIDATE SEQUENCE (the ramp)

| Rung | Candidate | State | The canary's condition |
|---|---|---|---|
| 1 | `kshitijthakkar/deepseek-v4-mini-300M-from-flash` (pin `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`) | **FIRED** — R1 LANDED, receipt complete | rung-2 conditions armed |
| 2 | V3-3.4B-small (sha `415501bd…`) | **ARMED** — defined + ready, never promised | the ramp's battery (GAP-3's 300+ gate) armed; the pilot's phase-1 does not burn rung-2 tokens, it holds the rung-2 conditions until rung-2's window |

**The ramp discipline.** Each rung arms the next; a rung that fails does not burn the next; the failed rung's revert points are the ramp's rollback (section 3). The pilot's phase-1 holds rung 2's candidate in the record, armed but unburned, as the first open thread (section 9).

---

## 8 · THE END-STATE (the canary's phase-1 target)

- the canary's phase-1 brief audited by the rotation (gate: the audit's marks + the pilot's receipt);
- the kit's certifications closed behind phase-1 (the four method cards + the capture home + the gate-state file + the judge-gate);
- the verification independent (the out-of-band evaluator's schedule);
- the egress sole-route discipline held (the sole-route rule from the cells' ledger);
- the RFC-facing inventions (read-gap fix's design, doc-chain UX, compaction's rule) parked after the pilot — not this leg;
- the loop's last gift is the loop's own form (the kaizen spine; the night's own pattern: each flaw becoming the next finding's receipt).

---

## 9 · OPEN THREADS / CONTINUATION POINTS

1. **Rung-2 battery:** the V3-3.4B-small (sha `415501bd…`) is armed but not fired; the pilot's phase-1 holds it until its own window. The open thread is the timing + the gate that fires rung-2.
2. **The isolation-boundary seam:** field (1) "not confirmed from cells" was closed head-side only after the cell carried `sandbox_env_id`, but the pilot's phase-1 run must re-verify the envelope contract at run time (the cell's assertion is a receipt, not a measurement). The open thread is the measured isolation check.
3. **The gate-state file's shape:** the operator's read surface (the field-facing moment = the rung-1 canary's receipt on the operator's read). The exact shape of the gate-state file is open; the pilot's phase-1 holds the shape as an open thread and the first landing drafts it.
4. **The method-cards canary-first card:** card 1 (two-way-door verdict + receipt stamp) as the pilot's first certified use — the trial run of the canary's judgment-layer first-catches is the next leg's open thread.
5. **The judge-gate re-reading schedule:** the per-ring re-read of the five gate fields — the first re-read's cadence is an open thread (the rings 40–60 min; the 6-hour ACES trigger).
6. **The egress cell's verification at run time:** the sole-route byte-counted check on the record — the pilot must produce its own egress receipt (bytes + sha + command), not carry the rung-1 one.

---

*Facimus semper — the canary's phase-1 design is a gate state, revisable by evidence; its receipts are the record's. Nothing public beyond PR #1. RFC quiet.*
