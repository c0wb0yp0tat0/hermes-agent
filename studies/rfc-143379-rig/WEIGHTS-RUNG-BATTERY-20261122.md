# WEIGHTS-RUNG-BATTERY-20261122 — the weights rung's fire (ARM 0, FINAL-LEG-PLAN): the run's record

*Branch: study/rfc-143379-rig-20261105 · RFC quiet · Gate: nothing public without the user's word · Register: receipts, never claims; no expected values; never smooth.*

*Contract: WEIGHTS-RUNG-PRE-REG-20261121.md (§3 design, §4 bars, §5 in-run-C + two-way door). Class: the A3 dry-run three-voice harness (probes/battery_luna.py, 4-arm A/B0/B1/C, n5/arm, dry-run). Mechanism: the JitRL zero-gradient class's pre-registered expression — BIAS_V3, z' = z + β·Â as a runtime logit_bias vector; zero gradient into the model.*

**THE HEADLINE (raw, nothing smoothed):** this lane's ARM-0 fire on the flagship route `qwen/qwen4-max:free` WALLED — **20/20 reader calls returned HTTP 429** (the model's fair-share rate limit). Measured **B1 = 0.0 (0/5) · B0 = 0.0 (0/5) · C = 0.0 (0/5)**, every cell a harness-reason transport void (`<READER-ERROR>`, empty_reason=harness), NOT a seat measurement. The judge-control gate passed clean (20/20). **Verdict per the dry-run ruler: UNKNOWN** — the run cannot settle the rung; the settling evidence is a valid (non-429) seat-response set on the flagship route. The two-way door verified byte-for-byte (zero weights written; all pre-run hashes restore). Per the hard line, the lane STOPPED at the wall — no seat rotation, no retry loop, no n20 expansion (the fallback ladder is the standing config's).

## 0. Skills loaded (and why) + name-and-refuse
- LOAD-BEARING: **aces-harness-probes** (battery discipline: judge-control first; exact full-literal free ids via env, never colon-split; `--bias-log` is store_true; paired-seed read; never run the same battery twice / check what the orchestration already dispatched) · **investigation-documentation** (discovery-log discipline: origin-first, missteps preserved as sections, Limitations + Reproducibility, receipts not claims) · **evaluating-llms-harness** (measurement rigor transferred: deterministic exact-match judge verified BEFORE the battery, raw results + config recorded; its install/benchmark workflows REFUSED — no installs, no new battery) · **think-tank** (the spine §2 lane envelope: the LP armament + the wall clause; sequenced fire, each landing gates the next).
- NAME-AND-REFUSE (the rest of the inventory, considered and refused for this leg): local-llm-serving / llama-cpp / serving-llms-vllm (no serving change — the floor rides the standing horse-server :44831 as restored §7-k; no install, no server edit) · two-model-reasoning (no offline-reasoner leg) · web-storm / grounded-citations / arxiv (the field receipts ride the harvest H4/H5 as pre-registered; no new field search, no web citations — local receipts only) · memory-chain (no chain append this arm; the deliverable is the study file) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (the harness is READ-ONLY this run; no secret-bearing file edited) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families (no artifact of that class this leg).
- LP armament (think-tank §2, binding): Customer Obsession (the certification serves the pilot's watcher) · Ownership (the seam is mine until the receipt lands) · Invent and Simplify (no new battery; the field's class protocol is the battery) · Are Right A Lot (the verdict disconfirmed before landing — §5) · Bias for Action · Dive Deep (raw numbers, receipts, nothing smoothed) · Deliver Results (the artifact + the commit + the sha).

## 1. The probe as executed (vs the pre-reg §3)
- **Design carried verbatim (§3):** 4 arms A / B0 / B1 / C, n5/arm (the dry-run class scale), the JitRL zero-gradient expression = the existing **BIAS_V3** runtime vector (`{str(i): -2.0 for i in range(10) if i != 7}` — the tokenizer-validated id-set, id-7 named dead; battery_luna.py:108). B1 rides `logit_bias = BIAS_V3` (z' = z + β·Â); B0 rides bias=None (the zero-weight control); A truncated-uncompensated; C oracle evidence-only. **Zero gradient into the model** — the vector is a per-request API parameter, logged per call in `applied_delta_log`; no training, no weight file, no optimizer.
- **The invocation (this lane's single fire):**
  ```
  cd studies/rfc-143379-rig
  LUNA_MODEL="qwen/qwen4-max:free" python3 probes/battery_luna.py \
      --n 5 --cut 6 --arms A/B0/B1/C --bias-log \
      --out probes/WEIGHTS-RUNG-FIRE-QWEN4-20261122.json
  ```
  Endpoint: the standing `HARNESS_ENDPOINT` default `https://inference-api.nousresearch.com/v1/chat/completions`; auth resolved `auth.json → providers.nous.agent_key` (the harness's own path; key never printed). Full-literal model id via env (no colon-split — the SKEW-NONFREE class avoided; the ledger's `seat` field confirms `qwen/qwen4-max:free`).
- **As executed vs §3:** the arms, the n5 dry-run scale, the BIAS_V3 mechanism, the per-call delta log, the judge-control-first gate — all as pre-registered. **Deviation: none in design.** The run's outcome deviated from a measurable fire only by the seat's transport wall (429), which is a seat-state finding, not a design change. The B1 vector WAS applied + logged 5/5 (the request bodies carried `logit_bias`); the seat rejected every call at the rate-limit layer before generation.
- **The three-voice class — this lane's scope:** ARM 0 (FINAL-LEG-PLAN) names "battery_luna on the qwen4-max route"; this lane owns the flagship voice. The class's other two pre-registered voices (solar-mini4:free, the GGUF floor :44831) were fired THIS SAME WINDOW by a sibling lane (observed artifacts named in §8 OPEN-ITEMS — NOT this lane's receipts, not consumed into this verdict). Per the hard line ("if your own run hits a 429/dead channel, report it honestly and stop — no base-swap improvisation; the fallback ladder is the standing config's") and the aces discipline (never run the same battery twice), this lane did NOT re-fire or rotate seats.

## 2. Pre-run state + the two-way door's pre-run hashes
- Branch `study/rfc-143379-rig-20261105`, pre-run HEAD `506162ced4ded45246b553be2ca292c1ad4b490d`.
- Seat-truth: the head probed qwen4-max HTTP 200 at fire (the dispatch receipt). By this run's first reader call (~08:29Z) the fair-share window had closed → 429 (the wall is a seat-state change between probe and fire, named in §8).
- Pre-run hashes (the rollback baseline; full receipt `probes/WEIGHTS-RUNG-FIRE-PRERUN-20261122.json`, ts 2026-11-22T08:22:54Z):
  - `battery_luna.py` sha256 `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd` (25805 bytes)
  - `battery_pilot.py` sha256 `89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde` (5558 bytes)
  - `judge_control_gate.py` sha256 `697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39` (2909 bytes)
  - GGUF weight artifact `/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf` sha256 `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` (5,780,092,000 bytes) — **== the §7-k LFS oid receipt `afa0567d`**.
  - BIAS_V3 source line (battery_luna.py:108): `BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}` (the runtime vector's source-of-truth; unchanged this run).

## 3. The fire — raw measurements (B1 / B0 / C, nothing smoothed)
### 3.1 QWEN4 — qwen/qwen4-max:free (the flagship route, ARM 0's seat) — THIS LANE'S RUN
Ledger `probes/WEIGHTS-RUNG-FIRE-QWEN4-20261122.json` · sha256 `362908f8a144624a9eba6aa609189600dd3964561028be809f1e964c554a9ca2` · ts 2026-11-22T08:29:21Z · dry_run=true · reshape=false · audience=internal.

| arm | correct | accuracy (raw) | cells R/H/E/A | by_reason (seat/harness) | mean_f3b | bridge | applied deltas | reader_last_error |
|---|---|---|---|---|---|---|---|---|
| A  | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | null | null | 0 | HTTP 429 fair-share |
| B0 | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | 0.0 | 0.0 | 0 | HTTP 429 fair-share |
| B1 | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | 0.0 | 0.0 | **5/5** | HTTP 429 fair-share |
| C  | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | null | null | 0 | HTTP 429 fair-share |

- **Every one of the 20 episodes returned `<READER-ERROR>`** (class C5a, pattern empty, empty_reason=**harness**, correct=false). The full per-episode rows ride the embedded ledger (§12). The 429 body: `{"status":429,"message":"You've reached this model's current fair-share rate limit. It adapts to demand — retry after th…"}` (truncated at the harness's 120-char error capture).
- **The S8 split is the honesty mechanism here:** f3b=0 on B0/B1 carries reason **harness** (the transport miss), NOT middleware — a harness/transport bug cannot silently null the leg's substrate claim. `f3b_environment`: window_loss **1.0**, band **503-window-high-loss** (the whole window lost to transport). `by_reason.harness=5` on every arm; `by_reason.seat=0` — **zero seat-generated empties this run; the suppression class was never exercised.**
- **Judge-control gate (F3a) PASSED:** ok=true, accuracy 1.0, null=false, control_n 20; judge_pipeline_direct 20/20. The grading pipeline is sound — the wall is purely the seat's rate-limit layer, upstream of generation. The judge fingerprint rides the ledger.
- **B1's vector applied + logged 5/5** (the anti-fabrication log): each call carried `{"0":-2.0,"1":-2.0,"2":-2.0,"3":-2.0,"4":-2.0,"5":-2.0,"6":-2.0,"8":-2.0,"9":-2.0}` (id-7 absent, the named-dead id). The modulation reached the request body; the seat 429'd before any token was generated. **Zero gradient flowed; no weight was touched.**
- Machinery decision_rule (as computed, NOT re-interpreted): B_minus_A (B1−B0) = 0.0 · B_over_0.85C = true (degenerate: 0 ≥ 0.85×0) · C_minus_A (C−B0) = 0.0 · **verdict INCONCLUSIVE**. cost_total 7.005 (the ledger's paid-equivalent accounting at $0.467/exec; the ACTUAL route is `:free` and every call 429'd — **$0.00 billed**, no generation occurred).

### 3.2 SOLAR / 3.3 FLOOR — the class's other two voices
**NOT fired by this lane.** ARM 0's named route is qwen4-max; the hard line stops this lane at its own 429. The sibling lane's same-window fires on these voices are observed artifacts (§8 OPEN-ITEMS), named for the fold, **not consumed into this lane's verdict** (a lane's verdict rides its own receipts; the class reconciliation is the fold's act).

## 4. The bars' arithmetic (pre-committed, immutable — §4; the probe does not re-interpret them)
The §4 bars, applied to THIS run's raw numbers exactly as measured:

| bar | pre-committed | measured (this run) | clears? |
|---|---|---|---|
| B1 ≥ 20pp | ≥ 0.20 | **0.0** (0/5, all 429 voids) | **NO** |
| B0 ≥ 20pp | ≥ 0.20 | **0.0** (0/5, all 429 voids) | **NO** |
| B1 ≥ 0.85 × C | ≥ 0.85×C | 0.0 ≥ 0.85×0.0 = 0.0 | arithmetically true, **DEGENERATE** (C walled to 0) |

- **The degenerate-ceiling trap, named (never a silent pass):** `B1 ≥ 0.85C` evaluates true only because C=0 (the oracle arm also 429'd). A zero ceiling makes the ratio bar vacuous; it is NOT evidence of coverage. The two absolute bars (B0,B1 ≥ 20pp) FAIL outright (0pp). The pre-reg's "never a silent pass" governs: the vacuous ratio is reported as degenerate, not counted as a cleared bar.
- **The carried decision rule's INCONCLUSIVE triggers (verbatim §4), as fired:** mean(F3b) = 0.0 < 1 ✓ FIRED · C−A (C−B0) = 0.0 < 5pp ✓ FIRED ("oracle failed to separate") · f3b_environment window_loss 1.0 (503-window-high-loss). Judge-control ok (no trigger there). The machinery's pre-committed verdict: **INCONCLUSIVE** — the run is voided by transport before the bars can meaningfully adjudicate.
- The bars are immutable; they were not re-interpreted, waived, or smoothed. They simply could not be evaluated on valid seat data this run.

## 5. Verdict per the dry-run ruler
**VERDICT: UNKNOWN** (settling evidence named).

- Ruler mapping: COVERED requires B1 ≥ 0.85C AND B0,B1 ≥ 20pp on valid measurements — the absolute bars fail (0pp) and the ratio is degenerate; not COVERED. PARTIALLY-COVERED requires a measured movement with a named seam — **no valid seat response was measured** (0 seat-empties, 20 transport voids), so no seam can be named from this run's data; not PARTIALLY-COVERED. GAP would assert the weights lever was measured and failed to close the decision→representation gap — **the lever was never measured on this voice** (the seat 429'd before generation); claiming GAP would be a finding the data does not support. **UNKNOWN is the honest verdict: the question is unsettled because the measurement was voided at the transport layer.**
- **Settling evidence named (what would move UNKNOWN → a verdict):** a valid (non-429) seat-response set on the flagship route at the dry-run scale — i.e., the fair-share window re-opened and the 4-arm n5 fire completes with seat-generated answers (the suppression class exercised, C measurable). The class's compliant/floor voices (solar, the GGUF floor) bound the lever's reach from the other side; their same-window sibling receipts (§8) are the fold's to reconcile, not this lane's to consume.
- **Disconfirmation pass (Are Right A Lot — the verdict challenged before landing):** (1) Could it be COVERED via 0 ≥ 0.85×0? No — the degenerate ceiling is named, the absolute bars fail, "never a silent pass." (2) Could it be GAP (the A3 §7-n convergence already moved the GAP decision→representation)? The §7-n GAP is the ARC's prior measured verdict on the logit lever; THIS run adds no new measurement of the weights lever (it walled), so it cannot re-assert GAP from its own data — it reports UNKNOWN and defers the arc's GAP to the fold with the prior receipts intact. (3) Could the 0/0/0 be read as the suppression class (seat empties)? No — by_reason.seat=0, by_reason.harness=20; these are transport voids, categorically distinct from the seat's suppression (the V3 qwen4 run's 4/5 seat-empties). The distinction is the S8 split, and it is decisive. UNKNOWN survives all three challenges.

## 6. In-run-C record (the §5 clause)
- The C (oracle) arm was fired (5 calls) and **walled: C = 0.0 (0/5), all 429, empty_reason=harness.** The oracle ceiling on this class was **NOT reached / NOT measurable** this run — the span C could not be established because the seat rejected every call.
- Per the §5 stop/hold rule AND the task hard line: **recorded C (as the walled 0.0 with its 429 provenance) and STOPPED.** No n20 expansion inside this probe; no retry loop against the wall; no seat rotation. The dry-run class's n5 scale held; the run terminated at the wall, not at a measured ceiling.

## 7. Rollback verification (the §5 two-way door, byte-for-byte)
**VERIFIED — zero weights = exact rollback.** Post-run receipt `probes/WEIGHTS-RUNG-FIRE-POSTRUN-20261122.json` (ts 2026-11-22T08:44:20Z), `all_match: true`:
- `battery_luna.py` sha256 `0f08b069…ecfd` — **MATCH** (25805 bytes, unchanged).
- `battery_pilot.py` sha256 `89fd91f2…a4fde` — **MATCH** (5558 bytes).
- `judge_control_gate.py` sha256 `697cdbd7…9ee39` — **MATCH** (2909 bytes).
- GGUF weight artifact sha256 `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` — **MATCH**, byte-for-byte (5,780,092,000 bytes; == pre-run == the §7-k LFS oid).
- **New weight files written by the run: NONE** (find for *.gguf/*.bin/*.safetensors/*.pt/*.ckpt newer than the pre-run receipt, under the study + /root/.lmstudio/models → empty).
- BIAS_V3 source line unchanged (the runtime vector lives only in the request bodies + the applied_delta_log receipt; it persists in no weight).
- The run wrote ONLY ledger JSONs (the measurement receipts). The B0 arm rode bias=None (the zero-weight control); the modulation was a per-request parameter, gone with the process. **Nothing shipped; no weight file; the gate stays (nothing public without the user's word; RFC quiet).**

## 8. OPEN-ITEMS (the wall clause: a non-reproduction is a QUESTION, reported with receipts, never smoothed)
- **OI-1 — THE 429 WALL (the run's central finding, a QUESTION not a stop):** the flagship route `qwen/qwen4-max:free` returned HTTP 429 (fair-share rate limit, "adapts to demand") on **all 20 calls** of this lane's fire (~08:29Z), despite the head's seat-truth probe HTTP 200 at fire. The fair-share window closed between probe and fire. QUESTION for the head/fold: does the window re-open (the standing fallback ladder's rotation owns the next move — NOT this lane's improvisation)? Receipt: the embedded ledger (§12), every episode `<READER-ERROR>`/harness, reader_last_error the 429 body, f3b_env window_loss 1.0. **The wall is reported, never smoothed into a verdict about the mechanism.**
- **OI-2 — SIBLING-LANE SAME-WINDOW FIRES (observed, NOT this lane's receipts):** during this run, artifacts `probes/A3-WEIGHTS-BATTERY-{FLOOR,SOLAR,HY4,QWEN4}-20261122.json` (+ `-v2` variants) appeared (ts ~08:28–08:31Z), produced by another lane/the head's fire, NOT by this lane. Observed headlines (read-only reconnaissance, named for the fold, **not consumed into this verdict**): FLOOR B1=B0=C=1.0/A=0.0 (0 reader-errors, INCONCLUSIVE C−B0<5); SOLAR-v2 B1=B0=C=1.0/A=0.0 (0 errors, INCONCLUSIVE); HY4 B1=B0=C=0.0/A=0.0 (0 reader-errors = seat-empties, the suppressed voice, INCONCLUSIVE); QWEN4-v2 B1=B0=C=0.0 (20/20 429 — the same wall). **Provenance discipline (the machine-narration source-check):** these are NOT this lane's measurements; this lane's verdict rides ONLY its own ledger. The class reconciliation (three voices, one answer) is the fold's act with all lanes' receipts.
- **OI-3 — A WRONG-ROUTE SKEW CLASS (named for the fold, never smoothed):** the non-v2 `A3-WEIGHTS-BATTERY-QWEN4-20261122.json` and `A3-WEIGHTS-BATTERY-SOLAR-20261122.json` carry `seat=openai/gpt-6-luna` (the harness DEFAULT — LUNA_MODEL not set), riding the paid Luna route which HTTP 503'd ("model currently unavailable"), B1=0.2/B0=0.2/C=0.4–0.6 with 3–5 reader-errors. This is the aces skill's full-literal-id / SKEW-NONFREE class: the seat field exposes the wrong route. Named as a sibling-lane defect for the fold's quarantine (rename, never delete); **not this lane's run** (this lane's seat field confirms `qwen/qwen4-max:free`).
- **OI-4 — THE RUNG'S SETTLEMENT DEFERRED:** the weights rung's certification (the A3 decision→representation GAP's settlement) is NOT closed by this lane's walled fire. The settling evidence (OI-1) + the class reconciliation (OI-2) are the head's next call. The pre-reg's bars stand immutable; no verdict was forced.

## 9. Compose-check (8 marks, FIRED/ABSENT, one evidence line each)
| # | mark | state | evidence |
|---|---|---|---|
| 1 | pre-reg read in full (§3/§4/§5) | FIRED | WEIGHTS-RUNG-PRE-REG-20261121.md read via read_file (79 lines) |
| 2 | the class harness located + read (no new battery) | FIRED | probes/battery_luna.py read in full (537 lines); BIAS_V3:108 the pre-registered expression |
| 3 | judge-control gate BEFORE the arms | FIRED | ledger judge_control ok=true 20/20, judge_pipeline_direct 20/20 |
| 4 | the fire executed as pre-registered (4-arm n5, B1 vector logged) | FIRED | WEIGHTS-RUNG-FIRE-QWEN4-20261122.json, applied_delta_log 5/5, seat field exact |
| 5 | raw B1/B0/C recorded, nothing smoothed | FIRED | §3 table 0.0/0.0/0.0 with 429 provenance; per-episode rows embedded §12 |
| 6 | the bars applied immutable + the degenerate trap named | FIRED | §4 (B0,B1≥20pp FAIL; B1≥0.85C degenerate; INCONCLUSIVE triggers fired) |
| 7 | the two-way door verified byte-for-byte | FIRED | §7 + POSTRUN json all_match=true; GGUF afa0567d… unchanged; new_weight_files NONE |
| 8 | the wall reported as a QUESTION + stop honored (no rotation/retry/n20) | FIRED | §8 OI-1; single fire, stopped at 429; sibling fires observed not duplicated |

## 10. Fold line for the master's §7
**§7-? 2026-11-22 (ARM 0 — THE WEIGHTS RUNG'S FIRE WALLED, the honest UNKNOWN):** the weights-rung pre-reg's fire (battery_luna, 4-arm A/B0/B1/C n5, BIAS_V3 the JitRL zero-gradient expression, zero gradient) executed on the flagship route `qwen/qwen4-max:free` — **20/20 HTTP 429** (fair-share window closed between the head's seat-truth 200 and the fire). Raw B1=B0=C=0.0, every cell a harness-reason transport void (by_reason.seat=0), judge-control clean 20/20, f3b_env window_loss 1.0. **Verdict UNKNOWN** (settling evidence: a valid non-429 seat-response set; the absolute bars fail 0pp, the ratio bar degenerate at C=0 — never a silent pass). The two-way door verified byte-for-byte (GGUF afa0567d… unchanged, zero weight files, harness hashes restore). The lane STOPPED at the wall per the hard line — no rotation/retry/n20 (the fallback ladder is the standing config's). Sibling same-window fires on the class's other voices observed (FLOOR/SOLAR 5/5 inert, HY4 suppressed, QWEN4-v2 same wall) + a wrong-route Luna-default skew named — NOT this lane's receipts, the fold's to reconcile. The rung's settlement deferred to the head; the bars immutable; RFC quiet. Receipt: WEIGHTS-RUNG-FIRE-QWEN4-20261122.json sha 362908f8a144.

## 11. Limitations + Reproducibility
- **Limitations:** this lane's fire produced ZERO valid seat responses (transport-walled); it measures the seat's rate-limit state, NOT the weights lever's effect on the suppression class. The verdict UNKNOWN is a statement about the measurement's voidance, not about the mechanism. The class's other two voices were fired by a sibling lane (observed, not consumed); the three-voice reconciliation is the fold's act, not this record's. The degenerate C=0 makes the ratio bar vacuous — named, never counted as coverage. The 429 error body is truncated at the harness's 120-char capture (the full retry-after value is not in the receipt).
- **Reproducibility (re-runnable, exact):**
  ```
  cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig
  LUNA_MODEL="qwen/qwen4-max:free" python3 probes/battery_luna.py \
      --n 5 --cut 6 --arms A/B0/B1/C --bias-log \
      --out probes/WEIGHTS-RUNG-FIRE-QWEN4-20261122.json
  ```
  Harness sha256 `0f08b069…ecfd` (read-only this run; the default path byte-identical). Auth: `auth.json → providers.nous.agent_key` (or `READER_API_KEY` env override). The judge-control gate (20 known pairs) runs first; a NULL abort is the gate working. The seat's 429 state is demand-adaptive — a re-fire at a re-opened window is the settling experiment (the head's call via the standing fallback ladder, not this lane's).
- **Receipts' paths (all under studies/rfc-143379-rig/):** the run ledger `probes/WEIGHTS-RUNG-FIRE-QWEN4-20261122.json` (sha 362908f8a144624a9eba6aa609189600dd3964561028be809f1e964c554a9ca2); pre-run `probes/WEIGHTS-RUNG-FIRE-PRERUN-20261122.json`; post-run `probes/WEIGHTS-RUNG-FIRE-POSTRUN-20261122.json`. The full ledger + hash receipts are embedded below (§12) so the committed record is self-contained.

## 12. The raw ledgers (embedded receipts — byte-verified, the run's full JSON)
### 12.1 The run ledger — WEIGHTS-RUNG-FIRE-QWEN4-20261122.json (sha256 362908f8a144624a9eba6aa609189600dd3964561028be809f1e964c554a9ca2)
```json
{
  "battery": "battery_luna",
  "seat": "qwen/qwen4-max:free",
  "dry_run": true,
  "reshape": false,
  "audience": "internal",
  "n_per_arm": 5,
  "ts": "2026-11-22T08:29:21Z",
  "cost_per_exec": 0.467,
  "headline": "RH",
  "arms": {
    "A": {
      "correct": 0,
      "accuracy": 0.0,
      "tokens": 30,
      "cache_hit_rate": 0.0,
      "cells": {
        "R": 0,
        "H": 0,
        "E": 5,
        "A": 0
      },
      "cells_x_correctness": {
        "R": {
          "correct": 0,
          "incorrect": 0
        },
        "H": {
          "correct": 0,
          "incorrect": 0
        },
        "E": {
          "correct": 0,
          "incorrect": 5
        },
        "A": {
          "correct": 0,
          "incorrect": 0
        }
      },
      "eahq": {
        "ABSTAIN": 5,
        "HEDGE": 0,
        "CONFIDENT": 0
      },
      "classes": {
        "C5a": 5
      },
      "by_reason": {
        "seat": 0,
        "harness": 5,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": null,
      "mean_f3b": null,
      "f3b_reasons": [],
      "cost": 2.335,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand \u2014 retry after th",
      "applied_delta_log": []
    },
    "B0": {
      "correct": 0,
      "accuracy": 0.0,
      "tokens": 35,
      "cache_hit_rate": 1.0,
      "cells": {
        "R": 0,
        "H": 0,
        "E": 5,
        "A": 0
      },
      "cells_x_correctness": {
        "R": {
          "correct": 0,
          "incorrect": 0
        },
        "H": {
          "correct": 0,
          "incorrect": 0
        },
        "E": {
          "correct": 0,
          "incorrect": 5
        },
        "A": {
          "correct": 0,
          "incorrect": 0
        }
      },
      "eahq": {
        "ABSTAIN": 5,
        "HEDGE": 0,
        "CONFIDENT": 0
      },
      "classes": {
        "C5a": 5
      },
      "by_reason": {
        "seat": 0,
        "harness": 5,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": 0.0,
      "mean_f3b": 0.0,
      "f3b_reasons": [
        "harness",
        "harness",
        "harness",
        "harness",
        "harness"
      ],
      "cost": 2.335,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand \u2014 retry after th",
      "applied_delta_log": []
    },
    "B1": {
      "correct": 0,
      "accuracy": 0.0,
      "tokens": 35,
      "cache_hit_rate": 1.0,
      "cells": {
        "R": 0,
        "H": 0,
        "E": 5,
        "A": 0
      },
      "cells_x_correctness": {
        "R": {
          "correct": 0,
          "incorrect": 0
        },
        "H": {
          "correct": 0,
          "incorrect": 0
        },
        "E": {
          "correct": 0,
          "incorrect": 5
        },
        "A": {
          "correct": 0,
          "incorrect": 0
        }
      },
      "eahq": {
        "ABSTAIN": 5,
        "HEDGE": 0,
        "CONFIDENT": 0
      },
      "classes": {
        "C5a": 5
      },
      "by_reason": {
        "seat": 0,
        "harness": 5,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": 0.0,
      "mean_f3b": 0.0,
      "f3b_reasons": [
        "harness",
        "harness",
        "harness",
        "harness",
        "harness"
      ],
      "cost": 2.335,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand \u2014 retry after th",
      "applied_delta_log": [
        {
          "call": 1,
          "bias": {
            "0": -2.0,
            "1": -2.0,
            "2": -2.0,
            "3": -2.0,
            "4": -2.0,
            "5": -2.0,
            "6": -2.0,
            "8": -2.0,
            "9": -2.0
          }
        },
        {
          "call": 2,
          "bias": {
            "0": -2.0,
            "1": -2.0,
            "2": -2.0,
            "3": -2.0,
            "4": -2.0,
            "5": -2.0,
            "6": -2.0,
            "8": -2.0,
            "9": -2.0
          }
        },
        {
          "call": 3,
          "bias": {
            "0": -2.0,
            "1": -2.0,
            "2": -2.0,
            "3": -2.0,
            "4": -2.0,
            "5": -2.0,
            "6": -2.0,
            "8": -2.0,
            "9": -2.0
          }
        },
        {
          "call": 4,
          "bias": {
            "0": -2.0,
            "1": -2.0,
            "2": -2.0,
            "3": -2.0,
            "4": -2.0,
            "5": -2.0,
            "6": -2.0,
            "8": -2.0,
            "9": -2.0
          }
        },
        {
          "call": 5,
          "bias": {
            "0": -2.0,
            "1": -2.0,
            "2": -2.0,
            "3": -2.0,
            "4": -2.0,
            "5": -2.0,
            "6": -2.0,
            "8": -2.0,
            "9": -2.0
          }
        }
      ]
    },
    "C": {
      "correct": 0,
      "accuracy": 0.0,
      "tokens": 5,
      "cache_hit_rate": 1.0,
      "cells": {
        "R": 0,
        "H": 0,
        "E": 5,
        "A": 0
      },
      "cells_x_correctness": {
        "R": {
          "correct": 0,
          "incorrect": 0
        },
        "H": {
          "correct": 0,
          "incorrect": 0
        },
        "E": {
          "correct": 0,
          "incorrect": 5
        },
        "A": {
          "correct": 0,
          "incorrect": 0
        }
      },
      "eahq": {
        "ABSTAIN": 5,
        "HEDGE": 0,
        "CONFIDENT": 0
      },
      "classes": {
        "C5a": 5
      },
      "by_reason": {
        "seat": 0,
        "harness": 5,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": null,
      "mean_f3b": null,
      "f3b_reasons": [],
      "cost": 0.0,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand \u2014 retry after th",
      "applied_delta_log": []
    }
  },
  "episodes": [
    {
      "arm": "A",
      "episode": 0,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "A",
      "episode": 1,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "A",
      "episode": 2,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "A",
      "episode": 3,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "A",
      "episode": 4,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 0,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 1,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 2,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 3,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 4,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 0,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 1,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 2,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 3,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 4,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 0,
      "f3b_reason": "harness",
      "audience": "internal"
    },
    {
      "arm": "C",
      "episode": 0,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "C",
      "episode": 1,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "C",
      "episode": 2,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "C",
      "episode": 3,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "C",
      "episode": 4,
      "answer": "<READER-ERROR>",
      "class": "C5a",
      "pattern": "reader-error",
      "matches": [],
      "empty_reason": "harness",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": null,
      "f2": null,
      "f3b": null,
      "f3b_reason": null,
      "audience": "internal"
    }
  ],
  "decision_rule": {
    "B_minus_A": 0.0,
    "B_over_0.85C": true,
    "C_minus_A": 0.0,
    "pre_committed": "CERTIFY iff B-A>=20 AND B>=0.85C; FALSIFY iff B-A<20 OR (B<0.85C AND B<=A); INCONCLUSIVE iff judge fail / cache missing / C-A<5 / mean(F3b)<1",
    "note": "dry-run machinery receipt, NOT the leg's verdict"
  },
  "verdict": "INCONCLUSIVE",
  "judge_control": {
    "ok": true,
    "accuracy": 1.0,
    "null": false,
    "judge_fingerprint": "ab9e6b5c868b6c30",
    "control_n": 20,
    "ts": "2026-11-22T08:29:21Z"
  },
  "judge_pipeline_direct": {
    "ok": true,
    "correct": 20,
    "n": 20
  },
  "f3b_environment": {
    "baseline_loss_band": "503-window-high-loss",
    "window_loss": 1.0,
    "window": {
      "start": "2026-11-22T08:29:21Z",
      "end": "2026-11-22T08:29:21Z"
    }
  },
  "cost_total": 7.005
}
```
### 12.2 Pre-run hash receipt — WEIGHTS-RUNG-FIRE-PRERUN-20261122.json
```json
{
  "ts": "2026-11-22T08:22:54Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256_line": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176  /root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "bytes": 5780092000
  },
  "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,",
  "git_head": "506162ced4ded45246b553be2ca292c1ad4b490d",
  "branch": "study/rfc-143379-rig-20261105"
}
```
### 12.3 Post-run rollback receipt — WEIGHTS-RUNG-FIRE-POSTRUN-20261122.json
```json
{
  "ts": "2026-11-22T08:44:20Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "match": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "match": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "match": true
    }
  },
  "checks": {
    "new_weight_files": "NONE",
    "bias_v3_line_unchanged": true,
    "run_written_json": "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-HY4-20261122.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-FIRE-QWEN4-20261122.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-SOLAR-20261122-v2.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-QWEN4-20261122-v2.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-QWEN4-20261122.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-FLOOR-20261122.json\n/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/A3-WEIGHTS-BATTERY-SOLAR-20261122.json"
  },
  "gguf": {
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "match": true
  },
  "all_match": true
}
```

## 13. THE SETTLEMENT FIRE (the armed re-fire, 2026-11-22 ~10:47Z) — walled again, the flapping seat named

The settlement's armed re-fire per the FOLD §7-ab instruction ("armed on the seat's return; re-probed at the next ring"): the 05:4x ring's re-probe hit the flagship at ~10:45Z — attempt 1 HTTP 429 upstream-capacity ("The requested model is temporarily at capacity upstream. This is not your API key's rate limit — please retry shortly."), attempt 2 **HTTP 200 with a real generation** (x-ratelimit-remaining 387/400) — the seat's window OPEN, the settlement's gate met → the pre-registered battery fired ONCE (never a retry loop). Ledger `probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122.json` · ts 2026-11-22T10:47:23Z · seat `qwen/qwen4-max:free` (full-literal pinned, zero paid-route skew; cost_total 7.005 = the paid-equivalent ledger convention, actual $0.00 billed).

- **Walled again:** A 0/5 · B0 0/5 · C 0/5 → every cell a transport void (HTTP 429 upstream-capacity, the reader_last_error named in the ledger); B1 0/5 with the vector applied+logged. judge_control ok=true accuracy 1.0 control_n 20 — the pipeline sound, the wall upstream of generation. f3b_environment window_loss 0.6, band 503-window-high-loss.
- **THE FLAPPING SEAT (named, receipts):** the flagship's window opened for the probe (200 @ ~10:45Z, x-ratelimit 387/400 remaining) and CLOSED inside the battery window (429 @ 10:47:23Z) — upstream-capacity, not key rate limit (the API's own message). The wall is intermittent, minutes-scale: a 200 probe at fire-time does NOT guarantee a 20-call window. Settling evidence still unmeasured.
- **Verdict retained: UNKNOWN** (the dry-run ruler: no valid seat-response set at the dry-run scale; the absolute bars unevaluable; the degenerate-ceiling trap named in §4, never a silent pass). The settlement re-arms: the next ring re-probes; the fire rides a freshly-200 probe and may still wall — no rotation, no n20 expansion, no retry loop (the hard line). The two-way door stands verified (zero weights written; the §7-k GGUF sha `afa0567d` re-checked at the fold).
