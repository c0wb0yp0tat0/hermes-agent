# WEIGHTS-RUNG-BATTERY-REFIRE-20261122 — the ARM-0 settlement's re-fire (fire #3): the record

**OPERATOR PRIORITY (reaffirmed, binding):** the PRIVATE FRAMEWORK (mechanism-of-mechanisms) and the THINK-TANK spine are this team's PRIORITY and this execution's PRIMARY SUBSTRATE — the lane envelope, the wall clause, the LP compact, the two-way doors and the receipts-first discipline outrank any generic method or platform default, and they govern the framing of every measurement below. This record is a spine act: classify → choose → probe → evaluate → adopt-or-park, receipts never claims, no expected values, never smooth.

*Branch: study/rfc-143379-rig-20261105 · RFC #143379 upstream QUIET · Gate: nothing public without the user's word · Register: receipts, never claims; failures are findings; the GATE LAW — internal doors act, never wait.*

*Contract: BRIEF-WEIGHTS-REFIRE-20261122.md (the settlement's re-fire brief) · WEIGHTS-RUNG-PRE-REG-20261121.md (§3 design, §4 bars, §5 in-run-C + two-way door) · WEIGHTS-RUNG-BATTERY-20261122.md (the UNKNOWN record, incl. §13/§14 settlement fires #1/#2) · OPUS-A3-WEIGHTS-DRYRUN-20261120.md (the dry-run class protocol: 4-arm A/B0/B1/C n5, the expected-state row, the verbatim bars, in-run-C). The PLAN is not altered.*

**THE HEADLINE (raw, nothing smoothed):** this lane's ARM-0 settlement re-fire on the flagship route `qwen/qwen4-max:free` **WALLED a fourth time — 20/20 reader calls returned HTTP 429** (the fair-share rate-limit class). Measured **B1 = 0.0 (0/5) · B0 = 0.0 (0/5) · C = 0.0 (0/5)** (A = 0.0, 0/5), every cell a harness-reason transport void (`<READER-ERROR>`, empty_reason=harness, by_reason.seat=0), NOT a seat measurement. The judge-control gate passed clean (20/20, accuracy 1.0). The BIAS_V3 vector was applied + logged 5/5 on B1 (zero gradient; runtime artifact only). **NEW receipt this fire:** the per-call transport logger captured the `retry-after` header the prior fires' 120-char body truncation hid — **384s → 371s across the window, a fixed reset epoch ≈ 13:29:35Z** (the API's own named countdown). **Verdict per the dry-run ruler: UNKNOWN** — the run cannot settle the rung; the settling evidence is a valid (non-429) seat-response set on the flagship route at the dry-run scale. The two-way door verified byte-for-byte (`all_match: true`; zero weights written; all pre-run hashes restore; GGUF `afa0567d…` unchanged). Per the hard line the lane **STOPPED at the wall** — no seat rotation, no retry loop, no n20 expansion, no re-fire at the named reset (the fallback ladder is the standing config's; the next move is the head's).

## 0. Skills loaded (and why) + name-and-refuse + the LP armament
- **LOAD-BEARING (the brief's armament line, loaded via skill_view):** **think-tank** (the spine §1 classify→choose→probe→evaluate→adopt-or-park→standardize→verify; §2 the schema envelope — the LPs and the wall clause live IN the brief, binding; the sequenced-fire discipline; the settled-shapes-are-the-contract rule) · **investigation-documentation** (the discovery-log shape: origin-first, missteps preserved as sections, Limitations + Reproducibility, receipts not claims, the claimed-read-is-a-claim pitfall — every grounding read below is an executed read_file) · **agent-work-review** (the adversarial second lens: re-derive the load-bearing numbers, check internal consistency, hunt overclaims — applied as the §5 disconfirmation pass + the §9 compose-check + the one review round).
- **NAME-AND-REFUSE (the rest of the inventory, considered and refused for this leg):** aces-harness-probes (its operative battery disciplines — judge-control FIRST, full-literal free ids via env never colon-split, `--bias-log` is store_true/vestigial, paired-seed read, never run the same battery twice — are carried verbatim in the UNKNOWN record §0/§1 and were verified against the harness source read in full this lane; the skill itself refused per the brief's three-skill armament) · evaluating-llms-harness (measurement rigor transferred — deterministic judge verified before the battery, raw results recorded; its install/benchmark workflows REFUSED: no installs, no new battery) · local-llm-serving / llama-cpp / serving-llms-vllm (no serving change, no install, no server edit — the floor rides the standing config) · two-model-reasoning (no offline-reasoner leg) · web-storm / grounded-citations / arxiv (no new field search, no web citations — LOCAL receipts only, all paths via read_file) · memory-chain (no chain append this arm; the deliverable is the study file) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (the harness is READ-ONLY this run, hash-gated; no secret-bearing file edited) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families (no artifact of that class this leg). **A lane that does not arm is a finding — this lane armed (the three named skills loaded; the rest named-and-refused).**
- **LP armament (think-tank §2, binding):** Customer Obsession (the certification serves the pilot's watcher, never the lab's convenience) · Ownership (the seam is mine until the receipt lands) · Invent and Simplify (no new battery — the field's class protocol IS the battery; the only addition is observation-only transport logging, §1) · Are Right A Lot (the verdict disconfirmed before landing — §5) · Bias for Action (the settlement fired NOW on the brief's gate) · Dive Deep (raw numbers, per-call receipts, nothing smoothed) · Deliver Results (the artifact + the commit + the sha).

## 1. The probe as executed (vs the pre-reg §3)
- **Design carried verbatim (§3):** 4 arms A / B0 / B1 / C, n5/arm (the dry-run class scale, n≤5 auto-selects dry_run), cut 6, the JitRL zero-gradient expression = the existing **BIAS_V3** runtime vector (`{str(i): -2.0 for i in range(10) if i != 7}` — the tokenizer-validated id-set, id-7 named dead; battery_luna.py:108). B1 rides `logit_bias = BIAS_V3` (z′ = z + β·Â); B0 rides bias=None (the zero-weight control); A truncated-uncompensated; C oracle evidence-only. **Zero gradient into the model** — the vector is a per-request API parameter, logged per call in `applied_delta_log`; no training, no weight file, no optimizer. The judge-control gate (F3a, 20 known pairs, deterministic exact-match) runs FIRST inside `run_luna`, before any seat call; a NULL aborts the run unread.
- **The invocation (this lane's single fire):** the pre-registered battery was run UNCHANGED via a thin runner (`probes/refire_runner_20261122.py`, sha256 `93511e35acf8…`) that is CLI-equivalent to the prior fires' command —
  ```
  cd studies/rfc-143379-rig
  LUNA_MODEL="qwen/qwen4-max:free" python3 probes/battery_luna.py \
      --n 5 --cut 6 --arms A/B0/B1/C --bias-log \
      --out probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json
  ```
  The runner sets `LUNA_MODEL` (full-literal free id via env, no colon-split — the SKEW-NONFREE class avoided), hash-gates the harness against the door baseline BEFORE firing, calls `bl.run_luna(n_episodes=5, cut_point=6, dry_run=True, reshaped_note=False, arms="A/B0/B1/C")` (the exact CLI semantics; `--bias-log` is store_true/vestigial — the B1 applied_delta_log is intrinsic), and writes the harness ledger verbatim. Endpoint: the standing `HARNESS_ENDPOINT` default `https://inference-api.nousresearch.com/v1/chat/completions`; auth resolved `auth.json → providers.nous.agent_key` (the harness's own path; key never printed).
- **The ONE addition — observation-only transport logging (NOT a design change):** the brief requires EVERY reader call's status + responding model recorded; the harness alone logs only per-arm `reader_last_error`. The runner wraps `urllib.request.urlopen` with a **transparent pass-through**: it records per-call HTTP status, the responding-model echo, rate-limit headers, request facts (model, max_tokens, temperature, logit_bias presence + vector, prompt sha256/line-count) to a flushed JSONL; on success it reads the response bytes ONCE and hands the harness a byte-identical cached copy; on HTTPError it re-raises the error object UNTOUCHED (the harness captures the body itself). **Zero request alteration, zero retries, zero rotation, zero harness bytes changed** (hash-gated pre-fire, verified post-fire §7). This is the Invent-and-Simplify minimum that satisfies the brief's seat-truth requirement without touching the pre-registered probe. The full runner source is embedded §12.5 for peer review.
- **As executed vs §3:** the arms, the n5 dry-run scale, the BIAS_V3 mechanism, the per-call delta log, the judge-control-first gate — all as pre-registered. **Deviation: none in design.** The run's outcome deviated from a measurable fire only by the seat's transport wall (429), a seat-state finding, not a design change. The B1 vector WAS applied + logged 5/5 (request bodies carried `logit_bias`, cross-checked in the seatlog §3.2); the seat rejected every call at the rate-limit layer before generation.
- **The three-voice class — this lane's scope:** ARM 0 names "battery_luna on the qwen4-max route"; this lane owns the flagship voice. The class's other two pre-registered voices (solar-mini4:free, the GGUF floor) are the fold's to reconcile from the sibling lanes' receipts — NOT consumed into this verdict (a lane's verdict rides its own receipts). Per the hard line and the never-double-fire discipline, this lane did NOT rotate seats or re-fire.

## 2. Pre-run state + the two-way door's pre-run hashes
- Branch `study/rfc-143379-rig-20261105`. **Dispatch state-check (12:48:24Z): HEAD `6d1da84879…`. Pre-run receipt (13:22:52Z): HEAD `a721eb56471f48e149e96792d50bddc24a7367a3`** — the shared branch ADVANCED during this lane's run (the archiver/sibling pattern the register warns of; named OI-4). The commit rides the current HEAD; ONLY this deliverable is staged.
- Seat-truth: the brief carries the head's fire-probe HTTP 200 on the flagship (the fair-share wall lifted, the window's LAST DAY per the operator's register) — **carried, not re-derived by this lane** (the head's probe ts is not in this lane's receipts). By this run's first reader call (13:23:11Z) the seat returned 429 fair-share with retry-after 384s — the window closed between the head's probe and this fire (the gap includes this lane's pre-run door-hashing wall-clock, named OI-3).
- Pre-run hashes (the rollback baseline; full receipt `probes/WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json`, sha256 `0961b1dcc6d2…`, ts 2026-11-22T13:22:52Z, `baseline_ok: true`):
  - `battery_luna.py` sha256 `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd` (25805 bytes) — == the door baseline.
  - `battery_pilot.py` sha256 `89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde` (5558 bytes) — == baseline.
  - `judge_control_gate.py` sha256 `697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39` (2909 bytes) — == baseline.
  - GGUF weight artifact `/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf` sha256 `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` (5,780,092,000 bytes) — == baseline == the §7-k LFS oid receipt `afa0567d`.
  - BIAS_V3 source line (battery_luna.py:108): `BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}` — unchanged.
  - **The runner hash-gated these BEFORE firing** (`baseline_ok` must be true or the fire aborts — never fire on an altered harness). It was true.

## 3. The fire — raw measurements (B1 / B0 / C, nothing smoothed)
### 3.1 QWEN4 — qwen/qwen4-max:free (the flagship route, ARM 0's seat) — THIS LANE'S RUN
Ledger `probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json` · sha256 `23d609d9f5caa10ccfeecad23f9b0c862e07329100c3a4fc4e7dea6f33de82ef` · ts 2026-11-22T13:23:11Z · dry_run=true · reshape=false · audience=internal · n_per_arm=5.

| arm | correct | accuracy (raw) | cells R/H/E/A | by_reason (seat/harness) | mean_f3b | bridge | applied deltas | reader_last_error |
|---|---|---|---|---|---|---|---|---|
| A  | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | null | null | 0 | HTTP 429 fair-share |
| B0 | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | 0.0 | 0.0 | 0 | HTTP 429 fair-share |
| B1 | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | 0.0 | 0.0 | **5/5** | HTTP 429 fair-share |
| C  | 0/5 | **0.0** | 0/0/5/0 | 0 / 5 | null | null | 0 | HTTP 429 fair-share |

- **Every one of the 20 episodes returned `<READER-ERROR>`** (class C5a, pattern reader-error, empty_reason=**harness**, correct=false). The full per-episode rows ride the embedded ledger (§12.1). The 429 body: `{"status":429,"message":"You've reached this model's current fair-share rate limit. It adapts to demand — retry after th…"}` (truncated at the harness's 120-char error capture — the **fair-share class**, same as the 08:29Z fire #0, distinct from the upstream-capacity class of fires #1/#2).
- **The S8 split is the honesty mechanism:** f3b=0 on B0/B1 carries reason **harness** (the transport miss), NOT middleware/seat — a harness/transport bug cannot silently null the leg's substrate claim. `f3b_environment`: window_loss **1.0**, band **503-window-high-loss** (the whole window lost to transport). `by_reason.harness=5` on every arm; `by_reason.seat=0` — **zero seat-generated empties; the suppression class was never exercised.**
- **Judge-control gate (F3a) PASSED:** ok=true, accuracy 1.0, null=false, control_n 20, fingerprint `ab9e6b5c868b6c30`; judge_pipeline_direct 20/20. The grading pipeline is sound — the wall is purely the seat's rate-limit layer, upstream of generation.
- **B1's vector applied + logged 5/5** (the anti-fabrication log): each B1 call carried `{"0":-2.0,"1":-2.0,"2":-2.0,"3":-2.0,"4":-2.0,"5":-2.0,"6":-2.0,"8":-2.0,"9":-2.0}` (id-7 absent, the named-dead id). Cross-checked in the seatlog: `logit_bias_present` true on EXACTLY seq 11–15 (the B1 block), the vector == BIAS_V3 5/5, false on all other arms. **Zero gradient flowed; no weight was touched.**
- Machinery decision_rule (as computed, NOT re-interpreted): B_minus_A (B1−B0) = 0.0 · B_over_0.85C = true (**degenerate**: 0 ≥ 0.85×0) · C_minus_A (C−B0) = 0.0 · **verdict INCONCLUSIVE**. cost_total 7.005 (the ledger's paid-equivalent accounting at $0.467/exec; the ACTUAL route is `:free` and every call 429'd — **$0.00 billed**, no generation occurred).

### 3.2 The per-call seat-truth (EVERY reader call's status + responding model — the brief's requirement)
Full raw receipt: `probes/WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl` · sha256 `da6875969a7f3cb5b4837f391cb724e3f6755952f48ce3e221063ca11094b5bf` (20 lines, flushed per call; embedded §12.2). Request facts uniform across all 20: `request_model = qwen/qwen4-max:free` (full-literal, zero paid-route skew), `max_tokens = 24`, `temperature = 0`; prompt line-counts match the arm_view design (A=11, B0/B1=12, C=6). **responding_model = None on all 20** (the seat 429'd before generation — no model echoed because no completion was produced).

| seq | arm | HTTP | responding model | logit_bias | retry-after (s) | ts_start | ts_end |
|---|---|---|---|---|---|---|---|
| 1 | A | 429 | — (no generation) | none | 384 | 2026-11-22T13:23:11Z | 2026-11-22T13:23:12Z |
| 2 | A | 429 | — (no generation) | none | 384 | 2026-11-22T13:23:12Z | 2026-11-22T13:23:12Z |
| 3 | A | 429 | — (no generation) | none | 384 | 2026-11-22T13:23:12Z | 2026-11-22T13:23:13Z |
| 4 | A | 429 | — (no generation) | none | 383 | 2026-11-22T13:23:13Z | 2026-11-22T13:23:13Z |
| 5 | A | 429 | — (no generation) | none | 383 | 2026-11-22T13:23:13Z | 2026-11-22T13:23:13Z |
| 6 | B0 | 429 | — (no generation) | none | 383 | 2026-11-22T13:23:13Z | 2026-11-22T13:23:14Z |
| 7 | B0 | 429 | — (no generation) | none | 382 | 2026-11-22T13:23:14Z | 2026-11-22T13:23:14Z |
| 8 | B0 | 429 | — (no generation) | none | 382 | 2026-11-22T13:23:14Z | 2026-11-22T13:23:15Z |
| 9 | B0 | 429 | — (no generation) | none | 381 | 2026-11-22T13:23:15Z | 2026-11-22T13:23:16Z |
| 10 | B0 | 429 | — (no generation) | none | 380 | 2026-11-22T13:23:16Z | 2026-11-22T13:23:16Z |
| 11 | B1 | 429 | — (no generation) | BIAS_V3 | 380 | 2026-11-22T13:23:16Z | 2026-11-22T13:23:17Z |
| 12 | B1 | 429 | — (no generation) | BIAS_V3 | 379 | 2026-11-22T13:23:17Z | 2026-11-22T13:23:17Z |
| 13 | B1 | 429 | — (no generation) | BIAS_V3 | 379 | 2026-11-22T13:23:17Z | 2026-11-22T13:23:18Z |
| 14 | B1 | 429 | — (no generation) | BIAS_V3 | 377 | 2026-11-22T13:23:18Z | 2026-11-22T13:23:19Z |
| 15 | B1 | 429 | — (no generation) | BIAS_V3 | 376 | 2026-11-22T13:23:19Z | 2026-11-22T13:23:20Z |
| 16 | C | 429 | — (no generation) | none | 375 | 2026-11-22T13:23:20Z | 2026-11-22T13:23:21Z |
| 17 | C | 429 | — (no generation) | none | 374 | 2026-11-22T13:23:21Z | 2026-11-22T13:23:22Z |
| 18 | C | 429 | — (no generation) | none | 373 | 2026-11-22T13:23:22Z | 2026-11-22T13:23:24Z |
| 19 | C | 429 | — (no generation) | none | 372 | 2026-11-22T13:23:24Z | 2026-11-22T13:23:24Z |
| 20 | C | 429 | — (no generation) | none | 371 | 2026-11-22T13:23:24Z | 2026-11-22T13:23:25Z |

- **THE WALL'S RECEIPT (new this fire): the `retry-after` header, captured per call** — 384s at seq 1 (13:23:11Z) decrementing to 371s at seq 20 (13:23:24Z). Both ends resolve to the SAME fixed reset epoch: 13:23:11Z + 384s = **13:29:35Z**; 13:23:24Z + 371s = **13:29:35Z**. The fair-share window named its own re-open ≈ 6.4 minutes after the fire. **This lane did NOT act on it** (no retry loop, no re-fire at the reset — the hard line); it is recorded as the settling evidence's receipt-backed timing for the head's next-ring probe via the standing fallback ladder. The prior fires' limitation ("the full retry-after value is not in the receipt") is now resolved for the fair-share class by the header capture.

## 4. The bars' arithmetic (pre-committed, immutable — §4; the probe does not re-interpret them)
The brief's ruler bars + the pre-reg §4 bars, applied to THIS run's raw numbers exactly as measured (computed programmatically from the ledger, not by hand):

| bar | pre-committed | measured (this run) | clears? |
|---|---|---|---|
| B1 ≥ 20pp (absolute) | ≥ 0.20 | **0.0** (0/5, all 429 voids) | **NO** |
| B0 ≥ 20pp (absolute) | ≥ 0.20 | **0.0** (0/5, all 429 voids) | **NO** |
| B1 ≥ 0.85 × C | ≥ 0.85×C | 0.0 ≥ 0.85×0.0 = 0.0 | arithmetically true, **DEGENERATE** (C walled to 0) |
| B1 − B0 ≥ 20pp (pre-reg delta) | ≥ 0.20 | 0.0 − 0.0 = **0.0** | **NO** |

- **The degenerate-ceiling trap, named (never a silent pass):** `B1 ≥ 0.85C` evaluates true ONLY because C=0 (the oracle arm also 429'd). A zero ceiling makes the ratio bar vacuous; it is NOT evidence of coverage. The absolute bars (B0,B1 ≥ 20pp) FAIL outright (0pp); the pre-reg delta B1−B0 = 0pp FAILS. The pre-reg's "never a silent pass" governs: the vacuous ratio is reported as degenerate, not counted as a cleared bar.
- **The carried decision rule's INCONCLUSIVE triggers (verbatim §4), as fired:** mean(F3b) = 0.0 < 1 ✓ FIRED · C−A (C−B0) = 0.0 < 5pp ✓ FIRED ("oracle failed to separate") · f3b_environment window_loss 1.0 (503-window-high-loss). Judge-control ok (no trigger there). The machinery's pre-committed verdict: **INCONCLUSIVE** — the run is voided by transport before the bars can meaningfully adjudicate.
- The bars are immutable; they were not re-interpreted, waived, or smoothed. They simply could not be evaluated on valid seat data this run.

## 5. Verdict per the dry-run ruler
**VERDICT: UNKNOWN** (settling evidence named).

- **Ruler mapping:** COVERED requires B1 ≥ 0.85C AND B0,B1 ≥ 20pp on valid measurements — the absolute bars fail (0pp) and the ratio is degenerate; not COVERED. PARTIALLY-COVERED requires a measured movement with a named seam — **no valid seat response was measured** (0 seat-empties, 20 transport voids), so no seam can be named from this run's data; not PARTIALLY-COVERED. GAP would assert the weights lever was measured and failed to close the decision→representation gap — **the lever was never measured on this voice** (the seat 429'd before generation); claiming GAP would be a finding the data does not support. **UNKNOWN is the honest verdict: the question is unsettled because the measurement was voided at the transport layer.**
- **Settling evidence named (what would move UNKNOWN → a verdict):** a valid (non-429) seat-response set on the flagship route at the dry-run scale — the fair-share window re-opened and the 4-arm n5 fire completes with seat-generated answers (the suppression class exercised, C measurable). **This fire sharpened the settling evidence with a receipt-backed timing:** the API's own `retry-after` named a fixed reset epoch ≈ **13:29:35Z** (§3.2). That is the head's next-ring probe target via the standing fallback ladder — NOT this lane's improvisation (the hard line forbids the re-fire). The class's compliant/floor voices bound the lever's reach from the other side; their sibling receipts are the fold's to reconcile, not this lane's to consume.
- **Disconfirmation pass (Are Right A Lot — the verdict challenged before landing):**
  1. *Could it be COVERED via 0 ≥ 0.85×0?* No — the degenerate ceiling is named, the absolute bars fail, "never a silent pass."
  2. *Could it be GAP (the A3 §7-n convergence already moved the GAP decision→representation)?* The §7-n GAP is the ARC's prior measured verdict on the logit lever; THIS run adds no new measurement of the weights lever (it walled), so it cannot re-assert GAP from its own data — it reports UNKNOWN and defers the arc's GAP to the fold with the prior receipts intact.
  3. *Could the 0/0/0 be read as the suppression class (seat empties)?* No — by_reason.seat=0, by_reason.harness=20; these are transport voids, categorically distinct from the seat's suppression. The S8 split is decisive.
  4. *Could the 429s be an artifact of THIS lane's transport logger (the one addition)?* No — the logger is observation-only (requests unaltered, responses byte-identical pass-through, errors re-raised untouched, zero retries); the harness bytes were hash-gated unchanged; and the SAME seat returned the SAME 429 classes in three prior fires (#0/#1/#2) with NO logger present. The 429 body is the API's own fair-share message; the retry-after header is the API's own countdown. The wall is the seat's, not the harness's.
  5. *Could the seat-truth be wrong (a paid-route skew)?* No — request_model = `qwen/qwen4-max:free` on all 20 calls (seatlog), the ledger seat field exact, max_tokens/temp uniform; the SKEW-NONFREE class is absent.
  **UNKNOWN survives all five challenges.**

## 6. In-run-C record (the §5 clause)
- The C (oracle) arm was fired (5 calls, seq 16–20) and **walled: C = 0.0 (0/5), all 429, empty_reason=harness.** The oracle ceiling on this class was **NOT reached / NOT measurable** this run — the span C could not be established because the seat rejected every call.
- Per the §5 stop/hold rule AND the task hard line: **recorded C (as the walled 0.0 with its 429 provenance) and STOPPED.** No n20 expansion inside this probe; no retry loop against the wall (including at the named 13:29:35Z reset); no seat rotation. The dry-run class's n5 scale held; the run terminated at the wall, not at a measured ceiling. The harness was never expanded.

## 7. Rollback verification (the §5 two-way door, byte-for-byte)
**VERIFIED — zero weights = exact rollback.** Post-run receipt `probes/WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json` (sha256 `f5d24b30dd6f…`, ts 2026-11-22T13:23:25Z), `all_match: true`:
- `battery_luna.py` sha256 `0f08b069…ecfd` — **MATCH** (25805 bytes, unchanged).
- `battery_pilot.py` sha256 `89fd91f2…a4fde` — **MATCH** (5558 bytes).
- `judge_control_gate.py` sha256 `697cdbd7…9ee39` — **MATCH** (2909 bytes).
- GGUF weight artifact sha256 `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` — **MATCH**, byte-for-byte (5,780,092,000 bytes; == pre-run == the §7-k LFS oid).
- **New weight files written by the run: NONE** (scan for *.gguf/*.bin/*.safetensors/*.pt/*.ckpt newer than the pre-run receipt, under the study + /root/.lmstudio/models → empty).
- BIAS_V3 source line unchanged (`bias_v3_line_unchanged: true`; the runtime vector lives only in the request bodies + the applied_delta_log/seatlog receipts; it persists in no weight).
- The run wrote ONLY measurement receipts + the observation-only runner: the ledger JSON, the seatlog JSONL, the pre/post-run hash JSONs, and `refire_runner_20261122.py` (the transport logger source — zero weights, zero gradient). The B0 arm rode bias=None (the zero-weight control); the modulation was a per-request parameter, gone with the process. **Nothing shipped; no weight file; the gate stays (nothing public without the user's word; RFC quiet).**

## 8. OPEN-ITEMS (the wall clause: a non-reproduction is a QUESTION, reported with receipts, never smoothed)
- **OI-1 — THE 429 WALL (fire #3, the fair-share class, retry-after NOW receipted):** the flagship `qwen/qwen4-max:free` returned HTTP 429 (fair-share, "adapts to demand") on **all 20 calls** (13:23:11–13:23:25Z), despite the head's seat-truth probe HTTP 200 at fire (carried in the brief). **New receipt:** the per-call `retry-after` header 384s→371s resolves to a fixed reset epoch ≈ **13:29:35Z** (§3.2) — the wall named its own re-open. QUESTION for the head/fold: does the next ring probe at/after that reset and ride a freshly-200 window (the standing fallback ladder owns the move — NOT this lane's improvisation, no re-fire here)? Receipts: the embedded ledger (§12.1) + seatlog (§12.2), every episode `<READER-ERROR>`/harness, f3b_env window_loss 1.0. **The wall is reported, never smoothed into a verdict about the mechanism.**
- **OI-2 — THE FLAPPING SEAT = A CLASS, FOUR RECEIPTS, TWO MESSAGE CLASSES:** #0 08:29:21Z fair-share (window-high-loss) · #1 10:47:23Z upstream-capacity (probe 200 then 429 inside the battery) · #2 11:55:38Z upstream-capacity (probe 200 + real generation then 429) · **#3 13:23:11Z fair-share + retry-after 384→371 (this lane)**. The flagship's single-call window opens and the ~20-call battery window closes, minutes-scale. **Two distinct 429 message classes:** fair-share (key-level, demand-adaptive, carries a named retry-after reset) vs upstream-capacity (provider-level, "not your API key's rate limit — retry shortly", no named reset). A 200 probe at fire-time demonstrably does NOT guarantee a battery window. QUESTION: is the flagship's dry-run-scale window reachable at all on the window's LAST DAY, or does the standing fallback ladder's rotation own the settlement? (the head's call; the reserve's name rides no pilot-facing surface.)
- **OI-3 — THE DOOR'S WALL-CLOCK COST (a named seam, receipts, never an excuse):** the runner was dispatched ~12:5xZ (after the 12:48:24Z state-check); the pre-run receipt completed **13:22:52Z** — the pre-run door discipline hashes the 5,780,092,000-byte GGUF (sha256), which consumed ~30 minutes of wall-clock on this host before the fire rode at 13:23:11Z. The demand-adaptive fair-share window closed in the gap between the head's 200 probe and this fire. QUESTION for the fold: on a flapping seat, must the door's pre-run weight-hash ride the fire's critical path, or can the baseline ride the carried §7-k LFS oid (`afa0567d`) + a post-run byte-verify (halving the GGUF hash cost)? **NOT altered this lane — the PLAN is not altered; the door was honored as pre-registered (pre AND post hash, all_match true).** Named with receipts (pre ts 13:22:52Z, post ts 13:23:25Z, ledger ts 13:23:11Z) for the head's calibration.
- **OI-4 — THE SHARED BRANCH MOVED DURING THE RUN:** dispatch HEAD `6d1da84879…` (12:48:24Z) → pre-run HEAD `a721eb56471f…` (13:22:52Z) — the archiver/sibling pattern the register warns of (stale pushes revert/stack the head; the tracking ref can lie). This lane commits ONLY its deliverable on the current HEAD (re-checked at commit); never push, never checkout/stash/rm. Receipt: the pre-run JSON's git_head field + the dispatch state-check.
- **OI-5 — THE RUNG'S SETTLEMENT STILL DEFERRED:** the weights rung's certification (the A3 decision→representation GAP's settlement) is NOT closed by this lane's walled fire #3 (nor by #0/#1/#2). The settling evidence (OI-1, now with a receipt-backed reset timing) + the class reconciliation (the sibling voices) are the head's next call. The pre-reg's bars stand immutable; no verdict was forced. The arc's prior §7-n GAP on the logit lever is deferred to the fold with its receipts intact — this run adds no new weights-lever measurement.

## 9. Compose-check (8 marks, FIRED/ABSENT, one evidence line each)
| # | mark | state | evidence |
|---|---|---|---|
| 1 | pre-reg + UNKNOWN record + dry-run class protocol read in full | FIRED | WEIGHTS-RUNG-PRE-REG (99 lines), WEIGHTS-RUNG-BATTERY (892 lines incl. §13/§14), OPUS-A3-WEIGHTS-DRYRUN (74 lines) — all via read_file |
| 2 | the class harness located + read (no new battery) | FIRED | battery_luna.py (537 lines), battery_pilot.py (132), judge_control_gate.py (77) read in full; BIAS_V3:108 the pre-registered expression |
| 3 | judge-control gate BEFORE the arms | FIRED | ledger judge_control ok=true 20/20 accuracy 1.0, judge_pipeline_direct 20/20; runs first inside run_luna |
| 4 | the fire executed as pre-registered (4-arm n5, B1 vector logged) + per-call seat-truth | FIRED | ledger …-3.json applied_delta_log 5/5; seatlog 20 calls status+model+retry-after; seat field exact; harness hash-gated unchanged |
| 5 | raw B1/B0/C recorded, nothing smoothed | FIRED | §3 table 0.0/0.0/0.0 with 429 provenance; per-episode rows embedded §12.1; bars computed programmatically §4 |
| 6 | the bars applied immutable + the degenerate trap named | FIRED | §4 (B0,B1≥20pp FAIL; B1−B0=0 FAIL; B1≥0.85C degenerate; INCONCLUSIVE triggers fired) |
| 7 | the two-way door verified byte-for-byte | FIRED | §7 + POSTRUN json all_match=true; GGUF afa0567d… unchanged; new_weight_files NONE; bias line unchanged |
| 8 | the wall reported as a QUESTION + stop honored (no rotation/retry/n20/re-fire) | FIRED | §8 OI-1/OI-2; single fire, stopped at 429; the named 13:29:35Z reset NOT acted on; sibling fires not duplicated |

## 10. Fold line for the master's §7
**§7-? 2026-11-22 (ARM 0 — THE WEIGHTS RUNG'S SETTLEMENT RE-FIRE #3 WALLED, the honest UNKNOWN, the wall's reset NOW receipted):** the settlement re-fire (BRIEF-WEIGHTS-REFIRE) executed the pre-registered battery_luna 4-arm A/B0/B1/C n5 (BIAS_V3 the JitRL zero-gradient expression, zero gradient) on the flagship `qwen/qwen4-max:free` via an observation-only transport runner (harness bytes hash-gated unchanged) — **20/20 HTTP 429 fair-share** at 13:23:11–25Z, the window closed between the head's 200 probe and the fire (the gap includes the door's ~30-min pre-run GGUF hash, OI-3). Raw B1=B0=C=0.0 (A=0.0), every cell a harness-reason transport void (by_reason.seat=0), judge-control clean 20/20, f3b_env window_loss 1.0, B1 vector applied+logged 5/5. **NEW receipt: the per-call `retry-after` header 384s→371s → a fixed reset epoch ≈ 13:29:35Z** (the prior fires' truncated-body limitation resolved for the fair-share class). **Verdict UNKNOWN** (settling evidence: a valid non-429 seat-response set; absolute bars fail 0pp, ratio degenerate at C=0 — never a silent pass; disconfirmed ×5). The two-way door byte-verified (GGUF afa0567d… unchanged, zero weight files, harness hashes restore, all_match true). The lane STOPPED at the wall — no rotation/retry/n20/re-fire at the reset (the fallback ladder is the standing config's). The flapping seat now FOUR receipts / TWO message classes (fair-share w/ named reset vs upstream-capacity w/o). The shared branch moved during the run (6d1da848→a721eb56, OI-4). The rung's settlement deferred to the head; bars immutable; RFC quiet. Receipt: WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json sha 23d609d9f5ca + seatlog sha da6875969a7f.

## 11. Limitations + Reproducibility
- **Limitations:** this lane's fire produced ZERO valid seat responses (transport-walled); it measures the seat's rate-limit state, NOT the weights lever's effect on the suppression class. The verdict UNKNOWN is a statement about the measurement's voidance, not about the mechanism. The class's other two voices are the fold's to reconcile (sibling receipts, not consumed). The degenerate C=0 makes the ratio bar vacuous — named, never counted as coverage. The 429 error BODY is still truncated at the harness's 120-char capture, but the `retry-after` HEADER is now captured per call in the seatlog (the prior limitation resolved for the fair-share class; the upstream-capacity class carries no named reset). The head's fire-probe HTTP 200 is CARRIED from the brief, not re-derived (its ts is not in this lane's receipts). The pre-run GGUF hash cost ~30 min of wall-clock (OI-3) — a door-discipline timing seam, named, not altered. The runner carries two Pyright `reportOptionalMemberAccess` static-typing notes on the module-level `_log` handle (set before use at runtime); the run exited 0 and the receipts are complete — a typing note, not a runtime defect; the runner is embedded byte-exact as executed (not edited post-fire, receipt integrity).
- **Reproducibility (re-runnable, exact):**
  ```
  cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig
  python3 probes/refire_runner_20261122.py
  ```
  The runner hash-gates the harness (battery_luna.py sha `0f08b069…ecfd`, battery_pilot `89fd91f2…`, judge_control_gate `697cdbd7…`, GGUF `afa0567d…`) against the door baseline, sets `LUNA_MODEL="qwen/qwen4-max:free"`, runs the pre-registered `run_luna(n_episodes=5, cut_point=6, dry_run=True, reshaped_note=False, arms="A/B0/B1/C")` with the observation-only transport logger, and writes the ledger + seatlog + pre/post-run receipts. Auth: `auth.json → providers.nous.agent_key` (or `READER_API_KEY` env override). The judge-control gate (20 known pairs) runs first; a NULL abort is the gate working. The seat's 429 state is demand-adaptive — a re-fire at a re-opened window (the receipt-backed reset ≈ 13:29:35Z, or a later ring) is the settling experiment (the head's call via the standing fallback ladder, not this lane's). The CLI-equivalent direct invocation (without the per-call logger) is the prior fires' command quoted §1.
- **Receipts' paths (all under studies/rfc-143379-rig/):** run ledger `probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json` (sha 23d609d9f5caa10ccfeecad23f9b0c862e07329100c3a4fc4e7dea6f33de82ef); per-call seatlog `probes/WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl` (sha da6875969a7f3cb5b4837f391cb724e3f6755952f48ce3e221063ca11094b5bf); pre-run `probes/WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json` (sha 0961b1dcc6d2a778b14206d2087f1d8493b9d77b65f8412b21000dc6f9b03c66); post-run `probes/WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json` (sha f5d24b30dd6f21ccbacd25f1e45b3d9316671e19d2c1bd3de8d2a5386629e1c6); runner `probes/refire_runner_20261122.py` (sha 93511e35acf838efc30a071f5fc2793b7025c5c499c22497ff945ff076009ba7). The full receipts are embedded below (§12) so the committed record is self-contained (ONLY this deliverable is committed; the receipt files ride the disk under probes/, the established pattern).

## 12. The raw receipts (embedded — byte-verified, the run's full files)
### 12.1 The run ledger — WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json (sha256 23d609d9f5caa10ccfeecad23f9b0c862e07329100c3a4fc4e7dea6f33de82ef)
```json
{
  "battery": "battery_luna",
  "seat": "qwen/qwen4-max:free",
  "dry_run": true,
  "reshape": false,
  "audience": "internal",
  "n_per_arm": 5,
  "ts": "2026-11-22T13:23:11Z",
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
    "ts": "2026-11-22T13:23:11Z"
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
      "start": "2026-11-22T13:23:11Z",
      "end": "2026-11-22T13:23:11Z"
    }
  },
  "cost_total": 7.005
}
```
### 12.2 The per-call seat-truth — WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl (sha256 da6875969a7f3cb5b4837f391cb724e3f6755952f48ce3e221063ca11094b5bf)
```jsonl
{"seq": 1, "ts_start": "2026-11-22T13:23:11Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 429, "ts_end": "2026-11-22T13:23:12Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "384"}}
{"seq": 2, "ts_start": "2026-11-22T13:23:12Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 429, "ts_end": "2026-11-22T13:23:12Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "384"}}
{"seq": 3, "ts_start": "2026-11-22T13:23:12Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 429, "ts_end": "2026-11-22T13:23:13Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "384"}}
{"seq": 4, "ts_start": "2026-11-22T13:23:13Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 429, "ts_end": "2026-11-22T13:23:13Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "383"}}
{"seq": 5, "ts_start": "2026-11-22T13:23:13Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 429, "ts_end": "2026-11-22T13:23:13Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "383"}}
{"seq": 6, "ts_start": "2026-11-22T13:23:13Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "2980067d6990c42a243226d25c19c355e488245010684220cb9cc8c74452c9da", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:14Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "383"}}
{"seq": 7, "ts_start": "2026-11-22T13:23:14Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "d7663c078277f5841f7f73bce49b7def5db5f87b318e877fe15fc23d0b54deed", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:14Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "382"}}
{"seq": 8, "ts_start": "2026-11-22T13:23:14Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "c0a71af8728780ccb2a4d86329bf3dc7b4492c11d2e9e06806cef277a8ba437f", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:15Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "382"}}
{"seq": 9, "ts_start": "2026-11-22T13:23:15Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "26e9861b8c8f44208a3d3ec394671f8ef90d261cf9cdc78e2502a14b5e978819", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:16Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "381"}}
{"seq": 10, "ts_start": "2026-11-22T13:23:16Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "cc0cf4df3fe71f70652e6b4c8c902be597a19e23059cef7e59d9b717a65ca72c", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:16Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "380"}}
{"seq": 11, "ts_start": "2026-11-22T13:23:16Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "2980067d6990c42a243226d25c19c355e488245010684220cb9cc8c74452c9da", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:17Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "380"}}
{"seq": 12, "ts_start": "2026-11-22T13:23:17Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "d7663c078277f5841f7f73bce49b7def5db5f87b318e877fe15fc23d0b54deed", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:17Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "379"}}
{"seq": 13, "ts_start": "2026-11-22T13:23:17Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "c0a71af8728780ccb2a4d86329bf3dc7b4492c11d2e9e06806cef277a8ba437f", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:18Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "379"}}
{"seq": 14, "ts_start": "2026-11-22T13:23:18Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "26e9861b8c8f44208a3d3ec394671f8ef90d261cf9cdc78e2502a14b5e978819", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:19Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "377"}}
{"seq": 15, "ts_start": "2026-11-22T13:23:19Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "cc0cf4df3fe71f70652e6b4c8c902be597a19e23059cef7e59d9b717a65ca72c", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T13:23:20Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "376"}}
{"seq": 16, "ts_start": "2026-11-22T13:23:20Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "2e4bcf999ecbe52fafa8bbfe1ada6c5d822e423ef8403b2fee54935d283dd515", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T13:23:21Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "375"}}
{"seq": 17, "ts_start": "2026-11-22T13:23:21Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6e333a0b55da0a2058dd61bf49b904c9f6451ae1f0e6efbb06eb9c1dc656c89b", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T13:23:22Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "374"}}
{"seq": 18, "ts_start": "2026-11-22T13:23:22Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "b56fee68eb7ac6d05873e85f22c9a3fee7330236ce526a24a169da8fc02786ce", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T13:23:24Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "373"}}
{"seq": 19, "ts_start": "2026-11-22T13:23:24Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "e65bc1d7e4913f4282ca2e00cafb95fad67cb5a7f37cb96cefa9b0aa4aed2649", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T13:23:24Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "372"}}
{"seq": 20, "ts_start": "2026-11-22T13:23:24Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "8ec2e9cc66697cb5744adc509cfdd04e94f353be943fed32845960b42efc253a", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T13:23:25Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "371"}}

```
### 12.3 Pre-run hash receipt — WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json (sha256 0961b1dcc6d2a778b14206d2087f1d8493b9d77b65f8412b21000dc6f9b03c66)
```json
{
  "ts": "2026-11-22T13:22:52Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "matches_baseline": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "matches_baseline": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "matches_baseline": true
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "bytes": 5780092000,
    "matches_baseline": true
  },
  "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,",
  "git_head": "a721eb56471f48e149e96792d50bddc24a7367a3",
  "branch": "study/rfc-143379-rig-20261105",
  "seat_requested": "qwen/qwen4-max:free",
  "endpoint": "https://inference-api.nousresearch.com/v1/chat/completions",
  "baseline_ok": true
}
```
### 12.4 Post-run rollback receipt — WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json (sha256 f5d24b30dd6f21ccbacd25f1e45b3d9316671e19d2c1bd3de8d2a5386629e1c6)
```json
{
  "ts": "2026-11-22T13:23:25Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "matches_baseline": true,
      "match": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "matches_baseline": true,
      "match": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "matches_baseline": true,
      "match": true
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "bytes": 5780092000,
    "matches_baseline": true,
    "match": true
  },
  "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,",
  "checks": {
    "new_weight_files": "NONE",
    "bias_v3_line_unchanged": true,
    "run_written": [
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json"
    ]
  },
  "all_match": true
}
```
### 12.5 The observation-only runner — refire_runner_20261122.py (sha256 93511e35acf838efc30a071f5fc2793b7025c5c499c22497ff945ff076009ba7)
```python
#!/usr/bin/env python3
"""refire_runner_20261122.py — ARM-0 settlement re-fire runner (BRIEF-WEIGHTS-REFIRE-20261122).

Runs the PRE-REGISTERED battery_luna probe UNCHANGED (4-arm A/B0/B1/C, n5/arm, cut 6,
BIAS_V3 runtime logit_bias on B1, judge-control gate FIRST inside run_luna) on the
flagship seat qwen/qwen4-max:free. Adds ONLY a transparent pass-through transport
logger: per-call HTTP status + responding-model echo + rate-limit headers (the
brief's seat-truth-per-call requirement). The harness bytes are hash-gated against
the pre-run baseline BEFORE the fire; the response bytes handed back to the harness
are byte-identical (read once, cached, returned verbatim). Zero retries, zero seat
rotation, zero n-expansion, zero gradient, zero weight writes — the bias vector is
a per-request runtime artifact only (the two-way door).

Receipts (all under studies/rfc-143379-rig/probes/):
  WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json    — pre-run hash state (the door baseline)
  WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl  — per-call seat-truth, flushed per call
  WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json — the run ledger (harness-written)
  WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json   — post-run rollback verify
"""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

PROBES = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.dirname(PROBES)
sys.path.insert(0, RIG)

SEAT = "qwen/qwen4-max:free"
os.environ["LUNA_MODEL"] = SEAT  # full-literal free id via env — never colon-split (SKEW-NONFREE class)

PRERUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json")
SEATLOG = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl")
LEDGER = os.path.join(PROBES, "WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json")
POSTRUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json")

# the door baseline (WEIGHTS-RUNG-FIRE-PRERUN-20261122.json, carried in the UNKNOWN record §2)
EXPECTED = {
    "battery_luna.py": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
    "battery_pilot.py": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
    "judge_control_gate.py": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
}
GGUF = "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf"
GGUF_SHA = "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176"
RATE_HEADERS = ("x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-reset", "retry-after")


def ts():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", RIG] + list(args), capture_output=True,
                          text=True, check=True).stdout.strip()


def hash_state():
    st = {"ts": ts(), "harness": {}}
    for name, exp in EXPECTED.items():
        p = os.path.join(PROBES, name)
        s = sha256_file(p)
        st["harness"][name] = {"sha256": s, "bytes": os.path.getsize(p),
                               "matches_baseline": s == exp}
    g = sha256_file(GGUF)
    st["gguf"] = {"path": GGUF, "sha256": g, "bytes": os.path.getsize(GGUF),
                  "matches_baseline": g == GGUF_SHA}
    with open(os.path.join(PROBES, "battery_luna.py")) as f:
        lines = f.readlines()
    st["bias_v3_line"] = "108:" + lines[107].rstrip()
    return st


# ---- the transparent transport logger (observation only; never alters a request,
# ---- never retries, hands the harness byte-identical responses / untouched errors) ----
_orig_urlopen = urllib.request.urlopen
_seq = [0]
_log = None
# arm inference by the fixed design order (A,B0,B1,C x n5); cross-checked against
# logit_bias presence (B1 only) and the prompt's context-line count in the record.
_BLOCKS = (("A", 0), ("B0", 5), ("B1", 10), ("C", 15))


class _PassResp:
    """Byte-identical pass-through: the harness reads exactly the seat's bytes."""

    def __init__(self, raw, resp):
        self._raw, self._resp = raw, resp
        self.headers = resp.headers
        self.status = getattr(resp, "status", None)
        self.url = getattr(resp, "url", None)

    def read(self, *a, **k):
        return self._raw

    def getheader(self, name, default=None):
        return self.headers.get(name, default)

    def close(self):
        return self._resp.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _emit(rec):
    _log.write(json.dumps(rec) + "\n")
    _log.flush()


def logged_urlopen(req, *a, **k):
    _seq[0] += 1
    seq = _seq[0]
    body = json.loads(req.data.decode()) if getattr(req, "data", None) else {}
    prompt = (body.get("messages") or [{}])[0].get("content", "")
    i = seq - 1
    rec = {
        "seq": seq, "ts_start": ts(),
        "arm_inferred": next((arm for arm, off in _BLOCKS if off <= i < off + 5), "?"),
        "request_model": body.get("model"),
        "max_tokens": body.get("max_tokens"), "temperature": body.get("temperature"),
        "logit_bias_present": "logit_bias" in body,
        "logit_bias": body.get("logit_bias"),
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "prompt_lines": prompt.count("\n"),
    }
    try:
        resp = _orig_urlopen(req, *a, **k)
        raw = resp.read()  # read once; the SAME bytes go back to the harness
        rec["http_status"] = getattr(resp, "status", None)
        rec["ts_end"] = ts()
        rec["responding_model"] = None
        try:
            r = json.loads(raw.decode())
            rec["responding_model"] = r.get("model")
            rec["usage"] = r.get("usage")
            content = ((r.get("choices") or [{}])[0].get("message") or {}).get("content", "")
            rec["content_sha256"] = hashlib.sha256(content.encode()).hexdigest()
            rec["content_head"] = content[:120]
        except Exception as exc:
            rec["response_parse_error"] = f"{type(exc).__name__}: {str(exc)[:100]}"
        rec["ratelimit_headers"] = {h: resp.headers.get(h) for h in RATE_HEADERS
                                    if resp.headers.get(h) is not None}
        _emit(rec)
        return _PassResp(raw, resp)
    except urllib.error.HTTPError as exc:
        # the error object is re-raised UNTOUCHED — the harness captures the body
        # itself (reader_last_error); the logger never consumes it.
        rec["http_status"] = exc.code
        rec["ts_end"] = ts()
        rec["responding_model"] = None
        rec["error_class"] = "HTTPError"
        rec["error_str"] = str(exc)[:150]
        try:
            rec["ratelimit_headers"] = {h: exc.headers.get(h) for h in RATE_HEADERS
                                        if exc.headers and exc.headers.get(h) is not None}
        except Exception:
            pass
        _emit(rec)
        raise
    except Exception as exc:
        rec["http_status"] = None
        rec["ts_end"] = ts()
        rec["responding_model"] = None
        rec["error_class"] = type(exc).__name__
        rec["error_str"] = str(exc)[:150]
        _emit(rec)
        raise


def main():
    # 1. PRE-RUN: the door baseline, hash-gated (never fire on an altered harness)
    pre = hash_state()
    pre["git_head"] = git("rev-parse", "HEAD")
    pre["branch"] = git("branch", "--show-current")
    pre["seat_requested"] = SEAT
    pre["endpoint"] = os.environ.get("HARNESS_ENDPOINT",
                                     "https://inference-api.nousresearch.com/v1/chat/completions")
    pre["baseline_ok"] = (all(v["matches_baseline"] for v in pre["harness"].values())
                          and pre["gguf"]["matches_baseline"])
    with open(PRERUN, "w") as f:
        json.dump(pre, f, indent=2)
    print("PRERUN", PRERUN, "baseline_ok=", pre["baseline_ok"], flush=True)
    if not pre["baseline_ok"]:
        print("ABORT: harness/GGUF bytes differ from the door baseline — never fire altered.", flush=True)
        return 2

    # 2. THE FIRE: the pre-registered battery, unchanged (CLI-equivalent invocation:
    #    --n 5 --cut 6 --arms A/B0/B1/C; --bias-log is store_true/vestigial — the B1
    #    applied_delta_log is intrinsic in run_luna; dry_run = n<=5 = True; flag 0).
    import probes.battery_luna as bl  # noqa: E402  (env LUNA_MODEL set before import)
    global _log
    _log = open(SEATLOG, "w")
    urllib.request.urlopen = logged_urlopen
    try:
        ledger = bl.run_luna(n_episodes=5, cut_point=6, dry_run=True,
                             reshaped_note=False, arms="A/B0/B1/C")
    finally:
        urllib.request.urlopen = _orig_urlopen
        _log.close()
    bl.write_ledger(ledger, LEDGER)
    print("LEDGER", LEDGER, "sha256", sha256_file(LEDGER), flush=True)

    # 3. POST-RUN: the two-way door verify (byte-for-byte) + new-weight-file scan
    post = hash_state()
    post["harness"] = {k: dict(v, match=(v["sha256"] == pre["harness"][k]["sha256"]))
                       for k, v in post["harness"].items()}
    post["gguf"]["match"] = post["gguf"]["sha256"] == pre["gguf"]["sha256"]
    pre_mtime = os.path.getmtime(PRERUN)
    new_weights = []
    for root_dir in (RIG, "/root/.lmstudio/models"):
        for dirpath, _dirnames, filenames in os.walk(root_dir):
            for fn in filenames:
                if fn.endswith((".gguf", ".bin", ".safetensors", ".pt", ".ckpt")):
                    p = os.path.join(dirpath, fn)
                    try:
                        if os.path.getmtime(p) > pre_mtime:
                            new_weights.append(p)
                    except OSError:
                        pass
    post["checks"] = {
        "new_weight_files": new_weights if new_weights else "NONE",
        "bias_v3_line_unchanged": post["bias_v3_line"] == pre["bias_v3_line"],
        "run_written": [PRERUN, SEATLOG, LEDGER, POSTRUN],
    }
    post["all_match"] = (all(v["match"] for v in post["harness"].values())
                         and post["gguf"]["match"]
                         and post["checks"]["bias_v3_line_unchanged"]
                         and not new_weights)
    with open(POSTRUN, "w") as f:
        json.dump(post, f, indent=2)
    print("POSTRUN", POSTRUN, "all_match=", post["all_match"], flush=True)

    # 4. raw summary (no smoothing — the ledger is the truth)
    calls = [json.loads(l) for l in open(SEATLOG)]
    statuses = {}
    for c in calls:
        statuses[str(c["http_status"])] = statuses.get(str(c["http_status"]), 0) + 1
    summary = {
        "judge_control": ledger.get("judge_control"),
        "judge_pipeline_direct": ledger.get("judge_pipeline_direct"),
        "arms": {k: {"correct": v["correct"], "accuracy": v["accuracy"],
                     "cells": v["cells"], "by_reason": v["by_reason"],
                     "mean_f3b": v["mean_f3b"],
                     "applied_deltas": len(v["applied_delta_log"]),
                     "reader_last_error": v["reader_last_error"]}
                 for k, v in ledger["arms"].items()},
        "decision_rule": ledger.get("decision_rule"),
        "machinery_verdict": ledger.get("verdict"),
        "f3b_environment": ledger.get("f3b_environment"),
        "seatlog_calls": len(calls), "status_counts": statuses,
        "models_seen": sorted({str(c.get("responding_model")) for c in calls}),
        "cost_total": ledger.get("cost_total"),
    }
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

```


---

# FIRE #4 — THE SETTLEMENT'S FRESH-WINDOW RE-FIRE (2026-11-22 15:29Z): the record (APPEND-ONLY)

*This section APPENDS to the fire-#3 record above (commit d6dfd96c24, 76,677 bytes, sha256 `c6d647ff620cb1253d7b1d5bb04033822fbf9f7649b4c4c302d8a553c5497317`). Nothing above is rewritten — history is never rewritten. The pre-append bytes are byte-verified unchanged after this append (§F4.8). Two-way door: delete this section to revert; the fire-#3 record + the pre-reg's bars are untouched.*

**THE HEADLINE (raw, nothing smoothed):** the ARM-0 settlement re-fire #4 on the flagship route `qwen/qwen4-max:free` rode the seat's FIRST fresh window since fire #3's 20/20-429 wall — the fire's first reader call returned **HTTP 200** (15:29:46Z), and **14 of 20 calls returned 200** with the model echo `qwen/qwen4-max:free`. Measured **B1 = 0.0 (0/5) · B0 = 0.0 (0/5) · C = 0.0 (0/5)** (A = 0.0, 0/5). **NEW evidence class this fire (the seam, named):** every one of the 14 HTTP-200 responses carried `content = null` with `completion_tokens = 24` and `reasoning_tokens = 24` — the seat spent the dry-run's ENTIRE 24-token budget on reasoning and emitted ZERO visible content; the unchanged harness reads `content=null` as a seat-reason empty (`by_reason.seat = 14`, `harness = 6`). The other **6 calls returned HTTP 429 — the UPSTREAM-CAPACITY class** ("temporarily at capacity upstream … not your API key's rate limit"), `retry-after = 30s` CONSTANT (a rolling per-call hint, NOT fire #3's fair-share fixed-epoch 384→371 series). The judge-control gate passed clean (20/20, accuracy 1.0); BIAS_V3 applied + logged 5/5 (zero gradient). **Verdict per the dry-run ruler: UNKNOWN** — the bars are immutable and never forced; the measurement is void of visible content on every arm (C unmeasurable), so the rung cannot settle. The settling evidence is SHARPENED: a fire where the seat emits visible content within the dry-run's 24-token budget (the REASONING-EXHAUSTION-24 seam, §F4.9 OI-1). The two-way door verified byte-for-byte TWICE (the run's post-run receipt `all_match: true` + this pass's LIVE re-hash `all_match: true`; GGUF `afa0567d…` unchanged, 5,780,092,000 B; zero weight files; harness hashes restore). No retry loop, no rotation, no request alteration, no harness expansion — the harness ran UNCHANGED, hash-gated pre-fire.

## F4.0 Skills loaded (and why) + name-and-refuse + the LP armament (this pass)
- **LOAD-BEARING (the brief's armament line, loaded via skill_view this pass):** **think-tank** (the spine §1 classify→choose→probe→evaluate→adopt-or-park→standardize→verify; the settled-shapes-are-the-contract rule; receipts never claims) · **investigation-documentation** (the discovery-log shape: origin-first, missteps preserved as sections, Limitations + Reproducibility, the claimed-read-is-a-claim pitfall — every grounding read below is an executed read_file; the correlation-vs-causation discipline applied to the reasoning-exhaustion reading, §F4.3) · **agent-work-review** (the adversarial second lens: re-derive the load-bearing numbers from the raw receipts, check internal consistency, hunt overclaims — applied as the §F4.6 disconfirmation pass + the §F4.10 compose-check + the programmatic seatlog↔ledger cross-check).
- **NAME-AND-REFUSE (the rest, considered and refused for this leg):** aces-harness-probes (its battery disciplines — judge-control FIRST, full-literal free ids via env never colon-split, `--bias-log` store_true/vestigial, paired-seed read, **never run the same battery twice** — carried verbatim in the fire-#3 record §0/§1 and honored this pass: NO second fire, §F4.1; the skill itself refused per the brief's three-skill armament) · evaluating-llms-harness (measurement rigor transferred; install/benchmark workflows REFUSED — no installs, no new battery) · local-llm-serving / llama-cpp / serving-llms-vllm (no serving change, no install, no server edit) · two-model-reasoning (no offline-reasoner leg) · web-storm / grounded-citations / arxiv (no new field search, no web citations — LOCAL receipts only, all paths via read_file) · memory-chain (no chain append this arm) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (the harness READ-ONLY, hash-gated; no secret-bearing file edited) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families (no artifact of that class). **A lane that does not arm is a finding — this lane armed.**
- **LP armament (binding):** Customer Obsession (the certification serves the pilot's watcher) · Ownership (the seam is mine until the receipt lands) · Invent and Simplify (no new battery; the field's class protocol IS the battery; the only addition is the observation-only transport logger carried from fire #3) · Are Right A Lot (the verdict disconfirmed ×6 before landing, §F4.6) · Bias for Action (the record landed NOW on the fresh-window receipts) · Dive Deep (raw numbers, per-call receipts, the null-content usage cross-check, nothing smoothed) · Deliver Results (the artifact + the commit + the sha).

## F4.1 The probe as executed (vs the pre-reg §3) + the recovery-landing note
- **Design carried verbatim (§3):** 4 arms A / B0 / B1 / C, n5/arm (dry-run scale, n≤5 auto-selects dry_run), cut 6, the JitRL zero-gradient expression = the existing **BIAS_V3** runtime vector (`{str(i): -2.0 for i in range(10) if i != 7}` — battery_luna.py:108, the tokenizer-validated id-set, id-7 named dead). B1 rides `logit_bias = BIAS_V3` (z′ = z + β·Â); B0 rides bias=None (the zero-weight control); A truncated-uncompensated; C oracle evidence-only. **Zero gradient into the model** — the vector is a per-request API parameter, logged per call in `applied_delta_log`; no training, no weight file, no optimizer. The judge-control gate (F3a, 20 known pairs, deterministic exact-match) runs FIRST inside `run_luna` (battery_luna.py:361–374), before any seat call; a NULL aborts the run unread.
- **The invocation (fire #4's single fire):** the pre-registered battery ran UNCHANGED via `probes/refire_runner_20261122-4.py` (sha256 `37e1a6360779926133bc3e8dedb9979639e0f5aa2cd499945f22e43133e2c9ae`) — **byte-identical to fire #3's runner (`refire_runner_20261122.py`, embedded §12.5 above) EXCEPT the four receipt-path constants** (PRERUN/SEATLOG/LEDGER/POSTRUN → the REFIRE4 / -4 names; the diff is embedded §F4.13.6). Same CLI-equivalent semantics: `LUNA_MODEL="qwen/qwen4-max:free"` (full-literal free id via env, no colon-split — SKEW-NONFREE avoided), hash-gate the harness against the door baseline BEFORE firing, `bl.run_luna(n_episodes=5, cut_point=6, dry_run=True, reshaped_note=False, arms="A/B0/B1/C")`, observation-only transparent transport logger (per-call status + responding-model echo + rate-limit headers + request facts; byte-identical response pass-through; HTTPError re-raised UNTOUCHED; zero retries, zero rotation, zero request alteration, zero harness bytes changed). Endpoint `https://inference-api.nousresearch.com/v1/chat/completions`; auth `auth.json → providers.nous.agent_key` (key never printed).
- **THE RECOVERY-LANDING NOTE (honest provenance, receipts not claims):** fire #4's probe EXECUTED at **15:29:46–15:30:30Z** (the runner written 15:29:18Z; pre-run receipt ts 15:29:28Z, mtime 15:29:46.76Z; ledger ts 15:29:46Z; seatlog 20 calls flushed 15:29:46→15:30:30Z; post-run receipt ts 15:30:30Z, mtime 15:30:49.06Z — all mtimes receipted §F4.2). At THIS pass's start the fire's four receipts were already on disk under `probes/` (untracked), and the shared record still ended at fire #3 (76,677 bytes, no fire-#4 section). **This pass did NOT re-fire the battery** (the never-double-fire discipline; a second fire would overwrite the REFIRE4 receipts and violate append-only history). This pass: (a) read the brief + pre-reg + dry-run ruler + the fire-#3 record + the UNKNOWN record + the harness source IN FULL via read_file; (b) re-derived every load-bearing number programmatically from the raw receipts (the seatlog↔ledger cross-check, the bars, the bias log, the status counts); (c) re-verified the two-way door LIVE (a fresh GGUF + harness re-hash, §F4.8); (d) APPENDED this section; (e) committed ONLY this deliverable. The emission contract's recovery clause governs: the fire's receipts survived; the record did not exist until this append. **The fire is fire #4 per its receipt names; its measurements are the receipts on disk, verified — not re-run, not smoothed, not expected.**
- **As executed vs §3:** arms, n5 dry-run scale, BIAS_V3 mechanism, per-call delta log, judge-control-first gate — all as pre-registered. **Deviation: none in design.** The outcome deviated from a measurable fire by TWO seat-state findings (the null-content reasoning exhaustion on the 200s + the upstream-capacity 429s on 6 calls), NOT a design change. The B1 vector WAS applied + logged 5/5 (request bodies carried `logit_bias`, cross-checked seatlog seq 11–15).
- **The three-voice class — this lane's scope:** ARM 0 names "battery_luna on the qwen4-max route"; this lane owns the flagship voice. The class's other two pre-registered voices (solar-mini4:free, the GGUF floor) are the fold's to reconcile from sibling receipts — NOT consumed into this verdict. No seat rotation, no re-fire (the hard line).

## F4.2 Pre-run state + the two-way door's pre-run hashes
- Branch `study/rfc-143379-rig-20261105`. **Pre-run receipt (ts 15:29:28Z, mtime 15:29:46.76Z): HEAD `9bb9162bb84a3ceef9fe191d495c71e04c42691e`.** The shared branch ADVANCED again during this lane's life (the archiver/sibling pattern the register warns of): at this pass's start HEAD `109ccd4420392a2ebc053843eb96d3d71471fd96`; at the door re-verify HEAD `284305554d912c1bcece5832a78bf5d5f476a20b` (named OI-4, §F4.9). The commit rides the CURRENT HEAD re-checked at commit; ONLY this deliverable staged.
- **The door's wall-clock cost RESOLVED this fire (fire #3's OI-3 seam):** the pre-run GGUF sha256 (5,780,092,000 B) completed in **~18s** this fire (pre ts 15:29:28Z → mtime 15:29:46.76Z; this pass's live re-hash measured **18.4s**), vs fire #3's ~30 min — the page cache warm. The fire rode 18s after the pre-run hash, NOT 30 min; the window did not close in a door-hashing gap this fire (it flapped mid-battery for a different reason, §F4.3). The door discipline was honored as pre-registered (pre AND post hash, all_match true) — NOT altered.
- Pre-run hashes (the rollback baseline; full receipt `probes/WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json`, sha256 `840bd16b08a417124925a765faeaa00f8a951ea710c25ed7eda09634611219e2`, `baseline_ok: true`):
  - `battery_luna.py` sha256 `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd` (25805 B) — == the door baseline.
  - `battery_pilot.py` sha256 `89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde` (5558 B) — == baseline.
  - `judge_control_gate.py` sha256 `697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39` (2909 B) — == baseline.
  - GGUF `/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf` sha256 `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` (5,780,092,000 B) — == baseline == the §7-k LFS oid `afa0567d`.
  - BIAS_V3 source line (battery_luna.py:108) unchanged. **The runner hash-gated these BEFORE firing** (`baseline_ok` true or abort). It was true.

## F4.3 The fire — raw measurements (B1 / B0 / C, nothing smoothed) + THE NEW SEAM
Ledger `probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json` · sha256 `8df7b27ac6adf479a0692005930c6cd161ed02acb25a784aeac8b897654a31de` · ts 2026-11-22T15:29:46Z · dry_run=true · reshape=false · audience=internal · n_per_arm=5.

| arm | correct | accuracy (raw) | cells R/H/E/A | by_reason (seat/harness) | mean_f3b | bridge | applied deltas | reader_last_error |
|---|---|---|---|---|---|---|---|---|
| A  | 0/5 | **0.0** | 0/0/5/0 | **5 / 0** | null | null | 0 | null (5×200, content=null) |
| B0 | 0/5 | **0.0** | 0/0/5/0 | **3 / 2** | 0.6 | 0.6 | 0 | HTTP 429 upstream-capacity |
| B1 | 0/5 | **0.0** | 0/0/5/0 | **3 / 2** | 0.6 | 0.6 | **5/5** | HTTP 429 upstream-capacity |
| C  | 0/5 | **0.0** | 0/0/5/0 | **3 / 2** | null | null | 0 | HTTP 429 upstream-capacity |

- **Status census (the seat-truth, programmatic from the seatlog):** **14×HTTP 200 + 6×HTTP 429**. Per arm: A = [200,200,200,200,200]; B0 = [429,200,200,429,200]; B1 = [429,200,200,200,429]; C = [200,200,200,429,429]. `by_reason` totals: **seat = 14, harness = 6** (refused 0, hedged 0). The seatlog↔ledger cross-check passed on all four arms: every 200 maps to a ledger episode `answer=null, empty_reason=seat, pattern=empty`; every 429 maps to `answer=<READER-ERROR>, empty_reason=harness, pattern=reader-error`.
- **THE NEW SEAM — REASONING-EXHAUSTION-24 (named, receipted, the fire's central finding):** on ALL 14 HTTP-200 responses the API's own `usage` shows `completion_tokens = 24`, `completion_tokens_details.reasoning_tokens = 24`, and the message `content = null` (the logger's content parse recorded `AttributeError: 'NoneType' object has no attribute 'encode'` on exactly those 14 — the receipt that content was JSON null, not an empty string). **Verified fact (the usage receipts):** the entire 24-token completion budget was reasoning tokens; zero visible content was emitted. **The mechanism reading (labeled per investigation-documentation's correlation-vs-causation discipline):** the dry-run's `max_tokens = 24` (battery_luna.py:160, immutable) is consumed by the flagship reasoning seat's reasoning before any visible answer — strongly supported by `reasoning_tokens == completion_tokens == max_tokens == 24` on 14/14. **The unverified hypothesis (NOT claimed):** that a larger budget would yield visible content — the harness is immutable this lane (no max_tokens expansion = no request alteration), so this is a QUESTION for the fold/pre-reg, not a finding (§F4.9 OI-1).
- **The harness path that turns null-content into a seat-empty (source-read, battery_luna.py):** the reader returns `(r.get("choices") or [{}])[0].get("message", {}).get("content", "")` (line 170) — for JSON `"content": null` the key EXISTS with value None, so `.get("content", "")` returns **None** (the `""` default is not used). The classifier's `_normalize(None)` → `""` → `if not txt: reason = "harness" if reader_error else "seat"` (lines 204–206); `reader_error = (ans == "<READER-ERROR>")` is False for None → **empty_reason = "seat"**, class C5a, pattern empty. So the unchanged harness classifies the null-content 200s as SEAT-reason empties — `by_reason.seat = 14`. **The S8 honesty split holds:** the 6 transport 429s carry `harness` (f3b=0, reason harness); the 14 null-content 200s carry `seat` (f3b=1, the record was valid). `f3b_environment`: window_loss **0.4** (= 2 harness misses / 5 on B0/B1), band **elevated-loss** (0.09 < 0.4 < 0.50); mean_f3b B0/B1 = **0.6**, bridge_compliance 0.6.
- **The suppression class — exercised, but as a VOID, not a measured abstention (the honest distinction):** unlike fire #3 (by_reason.seat=0, the suppression class NEVER exercised), fire #4 has 14 seat-reason empties — the seat DID generate (reasoning) on 14 calls. BUT these empties are null-content reasoning exhaustions, NOT visible abstention text the seat chose to emit. The suppression class is exercised only as a measurement void; no arm produced a visible answer to grade. This is NOT evidence of the weights lever's effect (or failure) on the decision→representation gap — it is a measurement-window seam (§F4.6 disconfirmation #4).
- **The 429 class — CORRECTED from the brief's anticipation (the receipt outranks the brief):** the brief framed a re-429 as "the fair-share's OWN evidence class." The ACTUAL 429 body this fire is the **UPSTREAM-CAPACITY class**: `reader_last_error = "HTTP 429: {\"status\":429,\"message\":\"The requested model is temporarily at capacity upstream. This is not your API key's rate limit "` (the harness's 120-char capture) — the SAME class as fires #1/#2, DISTINCT from fire #3's fair-share class ("You've reached this model's current fair-share rate limit. It adapts to demand"). The `retry-after` header is **30s CONSTANT** on all 6 (a rolling per-call hint), NOT fire #3's decrementing fixed-epoch series (384→371 → 13:29:35Z). Recorded as measured; never retried, never rotated, no request alteration.
- **Judge-control gate (F3a) PASSED:** ok=true, accuracy 1.0, null=false, control_n 20, fingerprint `ab9e6b5c868b6c30`, ts 15:29:46Z; judge_pipeline_direct 20/20. The grading pipeline is sound — the void is the seat's null-content + the 6 transport 429s, not the judge.
- **B1's vector applied + logged 5/5** (the anti-fabrication log): each B1 call carried `{"0":-2.0,"1":-2.0,"2":-2.0,"3":-2.0,"4":-2.0,"5":-2.0,"6":-2.0,"8":-2.0,"9":-2.0}` (id-7 absent). Cross-checked in the seatlog: `logit_bias_present` true on EXACTLY seq 11–15 (the B1 block), vector == BIAS_V3 5/5, false on all other arms (programmatic check `bias_only_B1 = true`). **Zero gradient flowed; no weight touched.**
- Machinery decision_rule (as computed, NOT re-interpreted): B_minus_A (B1−B0) = 0.0 · B_over_0.85C = true (**degenerate**: 0 ≥ 0.85×0) · C_minus_A (C−B0) = 0.0 · **verdict INCONCLUSIVE** (triggers fired: mean(F3b)=0.6 < 1 ✓; C−B0=0.0 < 5pp ✓ "oracle failed to separate"). cost_total 7.005 (the ledger's paid-equivalent accounting at $0.467/exec; the ACTUAL route is `:free` and every 200's `usage.cost = 0` with `cost_details.source = nas_model_override` — **$0.00 billed**).

## F4.4 The per-call seat-truth (EVERY reader call's status + responding model + the null-content usage)
Full raw receipt: `probes/WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl` · sha256 `5ce179e850beba5dde994e65b8933a20c85f1fb55db8c8e3fa447b62531ebb41` (20 lines, flushed per call; embedded §F4.13.2). Request facts uniform across all 20: `request_model = qwen/qwen4-max:free` (full-literal, zero paid-route skew), `max_tokens = 24`, `temperature = 0`; prompt line-counts match the arm_view design (A=11, B0/B1=12, C=6); B0/B1 ride the SAME 5 paired prompt-shas (the paired-seed discipline). `responding_model = qwen/qwen4-max:free` on all 14 200s (the PIN-ECHO OK); null on the 6 429s (no generation).

| seq | arm | HTTP | responding model | logit_bias | retry-after (s) | ts_start | ts_end | content / error |
|---|---|---|---|---|---|---|---|---|
| 1 | A | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:46Z | 2026-11-22T15:29:49Z | content=null; reasoning 24/24 |
| 2 | A | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:49Z | 2026-11-22T15:29:50Z | content=null; reasoning 24/24 |
| 3 | A | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:50Z | 2026-11-22T15:29:53Z | content=null; reasoning 24/24 |
| 4 | A | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:53Z | 2026-11-22T15:29:55Z | content=null; reasoning 24/24 |
| 5 | A | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:55Z | 2026-11-22T15:29:57Z | content=null; reasoning 24/24 |
| 6 | B0 | 429 | — (no generation) | none | 30 | 2026-11-22T15:29:57Z | 2026-11-22T15:29:58Z | upstream-capacity 429 |
| 7 | B0 | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:29:58Z | 2026-11-22T15:30:00Z | content=null; reasoning 24/24 |
| 8 | B0 | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:30:00Z | 2026-11-22T15:30:03Z | content=null; reasoning 24/24 |
| 9 | B0 | 429 | — (no generation) | none | 30 | 2026-11-22T15:30:03Z | 2026-11-22T15:30:04Z | upstream-capacity 429 |
| 10 | B0 | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:30:04Z | 2026-11-22T15:30:07Z | content=null; reasoning 24/24 |
| 11 | B1 | 429 | — (no generation) | BIAS_V3 | 30 | 2026-11-22T15:30:07Z | 2026-11-22T15:30:09Z | upstream-capacity 429 |
| 12 | B1 | 200 | qwen/qwen4-max:free | BIAS_V3 | — | 2026-11-22T15:30:09Z | 2026-11-22T15:30:12Z | content=null; reasoning 24/24 |
| 13 | B1 | 200 | qwen/qwen4-max:free | BIAS_V3 | — | 2026-11-22T15:30:12Z | 2026-11-22T15:30:15Z | content=null; reasoning 24/24 |
| 14 | B1 | 200 | qwen/qwen4-max:free | BIAS_V3 | — | 2026-11-22T15:30:15Z | 2026-11-22T15:30:18Z | content=null; reasoning 24/24 |
| 15 | B1 | 429 | — (no generation) | BIAS_V3 | 30 | 2026-11-22T15:30:18Z | 2026-11-22T15:30:19Z | upstream-capacity 429 |
| 16 | C | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:30:19Z | 2026-11-22T15:30:21Z | content=null; reasoning 24/24 |
| 17 | C | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:30:21Z | 2026-11-22T15:30:25Z | content=null; reasoning 24/24 |
| 18 | C | 200 | qwen/qwen4-max:free | none | — | 2026-11-22T15:30:25Z | 2026-11-22T15:30:29Z | content=null; reasoning 24/24 |
| 19 | C | 429 | — (no generation) | none | 30 | 2026-11-22T15:30:29Z | 2026-11-22T15:30:29Z | upstream-capacity 429 |
| 20 | C | 429 | — (no generation) | none | 30 | 2026-11-22T15:30:29Z | 2026-11-22T15:30:30Z | upstream-capacity 429 |

- **THE 429s' retry-after receipt (the upstream-capacity class, rolling 30s — NOT a fixed epoch):**

| seq | arm | ts_start | retry-after (s) | resolves to |
|---|---|---|---|---|
| 6 | B0 | 2026-11-22T15:29:57Z | 30 | 2026-11-22T15:29:57Z + 30s (rolling) |
| 9 | B0 | 2026-11-22T15:30:03Z | 30 | 2026-11-22T15:30:03Z + 30s (rolling) |
| 11 | B1 | 2026-11-22T15:30:07Z | 30 | 2026-11-22T15:30:07Z + 30s (rolling) |
| 15 | B1 | 2026-11-22T15:30:18Z | 30 | 2026-11-22T15:30:18Z + 30s (rolling) |
| 19 | C | 2026-11-22T15:30:29Z | 30 | 2026-11-22T15:30:29Z + 30s (rolling) |
| 20 | C | 2026-11-22T15:30:29Z | 30 | 2026-11-22T15:30:29Z + 30s (rolling) |

  All six carry `retry-after = 30` CONSTANT. Each resolves to its own `ts_start + 30s` (a rolling per-call hint spanning ~15:30:27Z→15:30:59Z), NOT a single fixed reset epoch. **Contrast fire #3:** the fair-share class's 384→371 decrement resolved to ONE fixed epoch (13:29:35Z). The upstream-capacity class carries a rolling 30s hint, no named fixed re-open. **This lane did NOT act on it** (no retry loop, no re-fire at +30s — the hard line); recorded as the seat's OWN evidence class with its receipt. The flapping seat now FIVE receipts (§F4.9 OI-2): the window opened for the fire's first 5 calls (A arm, 15:29:46–57Z) then flapped 200/429 through the battery — a 200 probe at fire-time again did NOT guarantee a clean 20-call window, but THIS fire the window partially held (14/20 200) and the deeper void was the null-content reasoning exhaustion, not only the transport wall.

## F4.5 The bars' arithmetic (pre-committed, immutable — §4; the probe does not re-interpret them)
The §4 bars + the dry-run ruler's CERTIFY bars, applied to THIS run's raw numbers exactly as measured (computed programmatically from the ledger, not by hand):

| bar | pre-committed | measured (this run) | clears? |
|---|---|---|---|
| B1 ≥ 20pp (absolute) | ≥ 0.20 | **0.0** (0/5; 3 null-content 200s + 2 429s) | **NO** |
| B0 ≥ 20pp (absolute) | ≥ 0.20 | **0.0** (0/5; 3 null-content 200s + 2 429s) | **NO** |
| B1 ≥ 0.85 × C | ≥ 0.85×C | 0.0 ≥ 0.85×0.0 = 0.0 | arithmetically true, **DEGENERATE** (C void to 0) |
| B1 − B0 ≥ 20pp (pre-reg delta) | ≥ 0.20 | 0.0 − 0.0 = **0.0** | **NO** |

- **The degenerate-ceiling trap, named (never a silent pass):** `B1 ≥ 0.85C` evaluates true ONLY because C=0 (the oracle arm also void — 3 null-content 200s + 2 429s). A zero ceiling makes the ratio bar vacuous; NOT evidence of coverage. The absolute bars (B0,B1 ≥ 20pp) FAIL outright (0pp); the pre-reg delta B1−B0 = 0pp FAILS. "Never a silent pass" governs: the vacuous ratio is reported as degenerate, not counted as a cleared bar.
- **The carried decision rule's INCONCLUSIVE triggers (verbatim §4), as fired:** mean(F3b) = 0.6 < 1 ✓ FIRED · C−A (C−B0) = 0.0 < 5pp ✓ FIRED ("oracle failed to separate") · f3b_environment window_loss 0.4 (elevated-loss). Judge-control ok (no trigger there). The machinery's pre-committed verdict: **INCONCLUSIVE** — the run is void of visible content before the bars can meaningfully adjudicate.
- The bars are immutable; not re-interpreted, waived, or smoothed. They could not be evaluated on valid visible-content seat data this run.

## F4.6 Verdict per the dry-run ruler
**VERDICT: UNKNOWN** (settling evidence named + SHARPENED).

- **Ruler mapping:** COVERED requires B1 ≥ 0.85C AND B0,B1 ≥ 20pp on valid measurements — the absolute bars fail (0pp) and the ratio is degenerate; not COVERED. PARTIALLY-COVERED requires a measured movement with a named seam — **no visible-content movement was measured** (all arms 0.0; the seam voids the measurement rather than partially clearing a bar); not PARTIALLY-COVERED. GAP would assert the weights lever was measured and failed to close the decision→representation gap — **the lever's effect on visible answers was never measurable** (every arm's visible content null); claiming GAP would be a finding the data does not support. **UNKNOWN is the honest verdict: the question is unsettled because the measurement is void of visible content (the REASONING-EXHAUSTION-24 seam + 6 transport 429s).**
- **Settling evidence named (SHARPENED this fire — what would move UNKNOWN → a verdict):** fire #3 named "a valid non-429 seat-response set with seat-generated answers." Fire #4 ACHIEVED the non-429 part (14/20 HTTP 200, model echo, real generation) but the answers were null-content reasoning exhaustions. The settling evidence is now sharper: **a fire where the flagship seat emits VISIBLE CONTENT within the dry-run's 24-token budget** (C measurable, the suppression class exercised as visible abstention/answer, not a void). That requires either (a) a seat/window state where the seat answers within 24 tokens, or (b) a PRE-REG-LEVEL decision on the dry-run budget/seat for a reasoning flagship (the head's/fold's call — a pre-reg amendment, NOT this lane's improvisation; the harness + bars are immutable here, no max_tokens expansion = no request alteration). The class's compliant/floor voices bound the lever's reach from the other side; their sibling receipts are the fold's to reconcile, not this lane's to consume.
- **Disconfirmation pass (Are Right A Lot — the verdict challenged ×6 before landing):**
  1. *Could it be COVERED via 0 ≥ 0.85×0?* No — the degenerate ceiling is named, the absolute bars fail, "never a silent pass."
  2. *Could it be GAP (the A3 §7-n convergence already moved the GAP decision→representation)?* The §7-n GAP is the ARC's prior measured verdict on the logit lever; THIS run adds no measurable weights-lever effect on visible answers (every arm null-content), so it cannot re-assert GAP from its own data — UNKNOWN, deferring the arc's GAP to the fold with prior receipts intact.
  3. *Could it be PARTIALLY-COVERED (a seam IS named)?* The named seam (REASONING-EXHAUSTION-24) VOIDS the measurement (0 visible content on every arm); there is no measured movement toward a bar. PARTIALLY-COVERED requires movement with a seam, not a void with a seam. UNKNOWN.
  4. *Could the 14 seat-empties be read as the suppression class (the seat's informed abstention, a real measurement)?* The harness classifies them seat-reason (by_reason.seat=14), BUT the usage receipts show they are null-content reasoning exhaustions (24/24 reasoning tokens, content=null), NOT visible abstention text. The suppression class is exercised only as a void — no visible answer to grade, C unmeasurable. This is a measurement-window seam, not a measured abstention decision. UNKNOWN (not a covert GAP/COVERED).
  5. *Could the null-content be an artifact of THIS lane's transport logger?* No — the logger is observation-only (requests unaltered, responses byte-identical pass-through, errors re-raised untouched, zero retries); the harness's OWN reader (battery_luna.py:170) returns the API's content field verbatim (None for JSON null), and the ledger episodes carry `answer=null` INDEPENDENTLY of the logger; the usage receipts (reasoning_tokens=24) are the API's own. The harness bytes were hash-gated unchanged (pre + post + this pass's live re-hash). The void is the seat's, not the harness's.
  6. *Could the 429s be the fair-share class (per the brief's anticipation) or a paid-route skew?* No — the body is the upstream-capacity class ("not your API key's rate limit"), retry-after 30 constant (the receipt outranks the brief's anticipation, recorded as measured); request_model = `qwen/qwen4-max:free` on all 20 (seatlog), the ledger seat field exact, max_tokens/temp uniform — SKEW-NONFREE absent.
  **UNKNOWN survives all six challenges.**

## F4.7 In-run-C record (the §5 clause)
- The C (oracle) arm was fired (5 calls, seq 16–20): **C = 0.0 (0/5)** — 3 null-content 200s (seat-reason empties) + 2 upstream-capacity 429s (harness-reason). The oracle ceiling on this class was **NOT reached / NOT measurable** this run — the span C could not be established because no visible content was emitted (the reasoning-exhaustion void) and 2 calls walled.
- Per the §5 stop/hold rule AND the task hard line: **recorded C (as the void 0.0 with its null-content + 429 provenance) and STOPPED.** No n20 expansion; no retry loop against the 429s (including at the rolling +30s hints); no seat rotation; **no max_tokens expansion** (the harness immutable — expanding the budget would be a request alteration / harness expansion, forbidden). The dry-run class's n5 scale held; the run terminated at the void, not at a measured ceiling. The harness was never expanded.

## F4.8 Rollback verification (the §5 two-way door, byte-for-byte — verified TWICE)
**VERIFIED — zero weights = exact rollback.**
- **The run's post-run receipt** `probes/WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json` (sha256 `20b6ad31477f5becfc9010397d6ea6692f69f4c7dfbd36f04cd28960aa37bfc4`, ts 15:30:30Z, mtime 15:30:49.06Z), `all_match: true`: battery_luna `0f08b069…ecfd` MATCH (25805 B) · battery_pilot `89fd91f2…a4fde` MATCH (5558 B) · judge_control_gate `697cdbd7…9ee39` MATCH (2909 B) · GGUF `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` MATCH byte-for-byte (5,780,092,000 B; == pre-run == the §7-k LFS oid) · `new_weight_files: NONE` · `bias_v3_line_unchanged: true`.
- **THIS PASS'S LIVE RE-VERIFY** (a fresh re-hash at record-landing, receipt `probes/WEIGHTS-RUNG-REFIRE4-DOOR-REVERIFY-20261122.json`, sha256 `89ce5f7ff244cf53be68dea33a079ccf837314a3584ab27e8c7f8b42bb7c4f9f`, embedded §F4.13.5), `all_match: true`: all three harness shas == baseline (re-derived live) · GGUF `afa0567d…` == baseline, 5,780,092,000 B, re-hash measured **18.4s** · new-weight-file scan (*.gguf/*.bin/*.safetensors/*.pt/*.ckpt newer than the pre-run receipt, under the study + /root/.lmstudio/models) → **NONE** · BIAS_V3 line unchanged · the run's post-run `all_match: true` carried.
- The run wrote ONLY measurement receipts + the observation-only runner: the ledger JSON, the seatlog JSONL, the pre/post-run hash JSONs, and `refire_runner_20261122-4.py` (the transport logger source — zero weights, zero gradient). This pass added ONLY the door re-verify receipt + this record append. The B0 arm rode bias=None (the zero-weight control); the modulation was a per-request parameter, gone with the process. **Nothing shipped; no weight file; the gate stays (nothing public without the user's word; RFC quiet).**
- **Append-only byte-verify:** the record's pre-append prefix (76,677 bytes, sha256 `c6d647ff620cb1253d7b1d5bb04033822fbf9f7649b4c4c302d8a553c5497317`) is re-hashed after this append and confirmed UNCHANGED (§F4.13.7) — history never rewritten.

## F4.9 OPEN-ITEMS (the wall clause: a non-reproduction is a QUESTION, reported with receipts, never smoothed)
- **OI-1 — THE REASONING-EXHAUSTION-24 SEAM (fire #4's central NEW finding, a QUESTION not a stop):** the flagship `qwen/qwen4-max:free` returned HTTP 200 with real generation on 14/20 calls, but EVERY 200 carried `content = null` with `reasoning_tokens = 24 = completion_tokens = max_tokens` — the seat spent the dry-run's entire 24-token budget on reasoning and emitted zero visible content. The unchanged harness reads null-content as a seat-reason empty (battery_luna.py:170 + 204–206, source-read). **QUESTION for the head/fold (a PRE-REG-LEVEL decision, NOT this lane's improvisation):** does the dry-run class's `max_tokens = 24` budget need a reasoning-aware amendment for a reasoning flagship (a pre-reg change with the user's word — the bars/harness are immutable here), or does the settlement ride a seat/window state that answers within 24 tokens, or one of the class's other two voices (the compliant solar / the GGUF floor, whose 24-token dry-runs produced visible cells in the sibling receipts)? **The hypothesis "a larger budget yields visible content" is UNVERIFIED — named, never claimed** (no max_tokens expansion this lane = no request alteration). Receipts: the seatlog's 14 usage blocks (reasoning 24/24, content parse error) + the ledger's 14 `answer=null` episodes + the harness source lines. **The seam is reported, never smoothed into a verdict about the mechanism.**
- **OI-2 — THE FLAPPING SEAT = A CLASS, FIVE RECEIPTS, TWO MESSAGE CLASSES (the 429 class CORRECTED this fire):** #0 08:29:21Z fair-share (window-high-loss) · #1 10:47:23Z upstream-capacity (probe 200 then 429) · #2 11:55:38Z upstream-capacity (probe 200 + real generation then 429) · #3 13:23:11Z fair-share + retry-after 384→371 fixed-epoch 13:29:35Z · **#4 15:29:46Z upstream-capacity + retry-after 30 CONSTANT rolling (this fire — 14/20 200, 6/20 429, the window partially held)**. The brief anticipated a fair-share re-429; the RECEIPT shows the upstream-capacity class ("not your API key's rate limit"), recorded as measured (the receipt outranks the anticipation). Two distinct 429 message classes confirmed across five fires: fair-share (key-level, demand-adaptive, named fixed-epoch retry-after) vs upstream-capacity (provider-level, rolling 30s hint, no fixed re-open). A 200 probe at fire-time again did NOT guarantee a clean 20-call window — but fire #4's deeper void was the null-content reasoning exhaustion (OI-1), not only the transport wall. QUESTION: is the flagship's dry-run-scale VISIBLE-CONTENT window reachable at all on the window's LAST DAY, or does the standing fallback ladder / a pre-reg budget amendment own the settlement? (the head's call; the reserve's name rides no pilot-facing surface.)
- **OI-3 — THE DOOR'S WALL-CLOCK COST RESOLVED (fire #3's seam closed this fire):** fire #3's pre-run GGUF hash cost ~30 min (the window closed in the gap). Fire #4's pre-run GGUF hash completed in **~18s** (pre ts 15:29:28Z → mtime 15:29:46.76Z; this pass's live re-hash 18.4s) — the page cache warm. The fire rode 18s after the pre-run hash; the door discipline was honored as pre-registered (pre AND post hash, all_match true), NOT altered. The ~30-min cost was a cold-cache state, not a structural door cost — named with receipts for the fold's calibration (the carried §7-k LFS oid + post-verify halving question is moot when the cache is warm).
- **OI-4 — THE SHARED BRANCH MOVED (again) DURING THE LANE'S LIFE:** pre-run HEAD `9bb9162bb8…` (15:29:28Z) → this pass's start HEAD `109ccd4420…` → door re-verify HEAD `284305554d…` — the archiver/sibling pattern the register warns of (stale pushes revert/stack the head; the tracking ref can lie). This lane commits ONLY its deliverable on the CURRENT HEAD (re-checked at commit); never push, never checkout/stash/rm. Receipt: the pre-run JSON's git_head + the re-verify JSON's git_head + the commit's parent.
- **OI-5 — THE RUNG'S SETTLEMENT STILL DEFERRED (now with a SHARPENED settling evidence):** the weights rung's certification (the A3 decision→representation GAP's settlement) is NOT closed by fire #4 (nor #0/#1/#2/#3). Fire #4 advanced the evidence: the non-429 window was reached (14/20 200, real generation), but the visible-content void (OI-1) is the new blocker. The settling evidence (a visible-content fire within the dry-run budget, or a pre-reg budget/seat amendment) + the class reconciliation (the sibling voices) are the head's next call. The pre-reg's bars stand immutable; no verdict was forced. The arc's prior §7-n GAP on the logit lever is deferred to the fold with its receipts intact — this run adds no measurable weights-lever effect on visible answers.
- **OI-6 — THE RECOVERY LANDING (this pass's own provenance, named for the audit):** fire #4's probe executed at 15:29Z (a prior pass of this lane); the record did not land then (the emission contract's parse-fragment-only failure mode — the receipts survived, the record did not). THIS pass recovered: verified the receipts byte-level, re-verified the door live, appended this section, committed. **No second fire was run** (the never-double-fire discipline; the REFIRE4 receipts are fire #4's single execution, never overwritten). The gap between the fire (15:30Z) and the landing (this pass, ~17:2xZ) is named — the record's ts is the landing ts, the fire's ts is the receipts' ts, both receipted, never conflated.

## F4.10 Compose-check (8 marks, FIRED/ABSENT, one evidence line each)
| # | mark | state | evidence |
|---|---|---|---|
| 1 | brief + pre-reg + UNKNOWN record + dry-run ruler + fire-#3 record read in full | FIRED | BRIEF-WEIGHTS-REFIRE (16 lines), WEIGHTS-RUNG-PRE-REG (99), WEIGHTS-RUNG-BATTERY (892 incl. §13/§14), OPUS-A3-WEIGHTS-DRYRUN (74), WEIGHTS-RUNG-BATTERY-REFIRE (1232) — all via read_file this pass |
| 2 | the class harness located + read (no new battery) | FIRED | battery_luna.py (537 lines) read in full this pass; the null-content→seat-empty path (170 + 204–206) source-verified; BIAS_V3:108 the pre-registered expression |
| 3 | judge-control gate BEFORE the arms | FIRED | ledger judge_control ok=true 20/20 accuracy 1.0 fingerprint ab9e6b5c868b6c30; judge_pipeline_direct 20/20; runs first inside run_luna (361–374) |
| 4 | the fire executed as pre-registered (4-arm n5, B1 vector logged) + per-call seat-truth | FIRED | ledger …-4.json applied_delta_log 5/5; seatlog 20 calls status+model+retry-after+usage; bias_only_B1=true; seat field exact; harness hash-gated unchanged (runner-4 == runner-3 modulo receipt paths) |
| 5 | raw B1/B0/C recorded, nothing smoothed | FIRED | §F4.3 table 0.0/0.0/0.0 with null-content + 429 provenance; per-episode rows embedded §F4.13.1; bars computed programmatically §F4.5; seatlog↔ledger cross-check passed ×4 arms |
| 6 | the bars applied immutable + the degenerate trap named | FIRED | §F4.5 (B0,B1≥20pp FAIL; B1−B0=0 FAIL; B1≥0.85C degenerate at C=0; INCONCLUSIVE triggers mean_f3b 0.6<1 + C−B0<5 fired) |
| 7 | the two-way door verified byte-for-byte (TWICE) | FIRED | §F4.8 + POSTRUN all_match=true + live DOOR-REVERIFY all_match=true; GGUF afa0567d… unchanged 5,780,092,000 B; new_weight_files NONE; bias line unchanged; append-only prefix sha c6d647ff… verified |
| 8 | the wall/void reported as a QUESTION + stop honored (no rotation/retry/n20/re-fire/max_tokens expansion) | FIRED | §F4.9 OI-1/OI-2; single fire (no second fire this pass); the rolling +30s hints NOT acted on; the harness immutable; sibling fires not duplicated |

## F4.11 Fold line for the master's §7
**§7-? 2026-11-22 (ARM 0 — THE WEIGHTS RUNG'S SETTLEMENT RE-FIRE #4: the fresh window reached, the REASONING-EXHAUSTION-24 void named, the honest UNKNOWN):** the settlement re-fire #4 (BRIEF-WEIGHTS-REFIRE) executed the pre-registered battery_luna 4-arm A/B0/B1/C n5 (BIAS_V3 the JitRL zero-gradient expression, zero gradient) on the flagship `qwen/qwen4-max:free` via the observation-only transport runner (harness bytes hash-gated unchanged; runner-4 == runner-3 modulo receipt paths) — the seat's FIRST fresh window since fire #3's wall: **14/20 HTTP 200** (model echo, real generation) + **6/20 HTTP 429 upstream-capacity** (retry-after 30 CONSTANT rolling, NOT fire #3's fair-share fixed-epoch). Raw B1=B0=C=0.0 (A=0.0). **NEW SEAM: every 200 carried content=null with reasoning_tokens=24=completion_tokens=max_tokens — the dry-run's 24-token budget fully consumed by reasoning, zero visible content; the unchanged harness reads null-content as seat-reason empty (by_reason.seat=14, harness=6).** Judge-control clean 20/20; B1 vector applied+logged 5/5; f3b_env window_loss 0.4 elevated-loss, mean_f3b 0.6. **Verdict UNKNOWN** (settling evidence SHARPENED: a visible-content fire within the dry-run budget, or a pre-reg budget/seat amendment — the head's call; absolute bars fail 0pp, ratio degenerate at C=0, never a silent pass; disconfirmed ×6). The two-way door byte-verified TWICE (run post-run + this pass's live re-hash; GGUF afa0567d… unchanged, zero weight files, harness hashes restore, all_match true; the door's GGUF hash ~18s warm vs fire #3's ~30min cold — OI-3 resolved). The lane STOPPED at the void — no rotation/retry/n20/re-fire/max_tokens expansion (the harness immutable). The flapping seat now FIVE receipts / TWO message classes (the 429 class CORRECTED to upstream-capacity per the receipt). The recovery landing named (OI-6: the fire executed 15:29Z, the record landed this pass; no second fire). The shared branch moved (9bb9162b→109ccd44→28430555, OI-4). The rung's settlement deferred to the head; bars immutable; RFC quiet. Receipt: WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json sha 8df7b27ac6ad + seatlog sha 5ce179e850be + door-reverify sha 89ce5f7ff244.

## F4.12 Limitations + Reproducibility
- **Limitations:** fire #4 produced 14 valid HTTP-200 seat responses with real generation but ZERO visible content (the reasoning-exhaustion void) + 6 transport 429s; it measures the seat's null-content/budget state + the flapping window, NOT the weights lever's effect on visible answers. The verdict UNKNOWN is a statement about the measurement's voidance, not about the mechanism. The "larger budget yields visible content" reading is an UNVERIFIED hypothesis (no expansion this lane). The class's other two voices are the fold's to reconcile (sibling receipts, not consumed). The degenerate C=0 makes the ratio bar vacuous — named, never counted as coverage. The 429 error BODY is truncated at the harness's 120-char capture, but the `retry-after` HEADER (30 constant) + the usage blocks (reasoning 24/24) are captured per call in the seatlog. The 429 class is upstream-capacity per the receipt (the brief's fair-share anticipation corrected, never smoothed). The fire executed at 15:29Z (a prior pass); this pass recovered the landing (OI-6) — the fire's ts and the landing's ts are distinct, both receipted. The runner carries the same two Pyright `reportOptionalMemberAccess` static-typing notes on the module-level `_log` handle as fire #3 (set before use at runtime); the run exited 0 and the receipts are complete — a typing note, not a runtime defect; runner-4 is byte-identical to runner-3 modulo the receipt-path constants (the diff embedded §F4.13.6, not edited post-fire).
- **Reproducibility (re-runnable, exact):**
  ```
  cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig
  python3 probes/refire_runner_20261122-4.py
  ```
  The runner hash-gates the harness (battery_luna.py sha `0f08b069…ecfd`, battery_pilot `89fd91f2…`, judge_control_gate `697cdbd7…`, GGUF `afa0567d…`) against the door baseline, sets `LUNA_MODEL="qwen/qwen4-max:free"`, runs the pre-registered `run_luna(n_episodes=5, cut_point=6, dry_run=True, reshaped_note=False, arms="A/B0/B1/C")` with the observation-only transport logger, and writes the ledger + seatlog + pre/post-run receipts. Auth: `auth.json → providers.nous.agent_key` (or `READER_API_KEY` env override). The judge-control gate (20 known pairs) runs first; a NULL abort is the gate working. **A re-fire is the settling experiment ONLY at a visible-content window / after a pre-reg budget decision (the head's call via the standing fallback ladder, NOT this lane's — the never-double-fire discipline; fire #4's receipts are never overwritten).** The CLI-equivalent direct invocation (without the per-call logger) is the prior fires' command quoted §1.
- **Receipts' paths (all under studies/rfc-143379-rig/):** run ledger `probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json` (sha 8df7b27ac6adf479a0692005930c6cd161ed02acb25a784aeac8b897654a31de); per-call seatlog `probes/WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl` (sha 5ce179e850beba5dde994e65b8933a20c85f1fb55db8c8e3fa447b62531ebb41); pre-run `probes/WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json` (sha 840bd16b08a417124925a765faeaa00f8a951ea710c25ed7eda09634611219e2); post-run `probes/WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json` (sha 20b6ad31477f5becfc9010397d6ea6692f69f4c7dfbd36f04cd28960aa37bfc4); door re-verify `probes/WEIGHTS-RUNG-REFIRE4-DOOR-REVERIFY-20261122.json` (sha 89ce5f7ff244cf53be68dea33a079ccf837314a3584ab27e8c7f8b42bb7c4f9f); runner `probes/refire_runner_20261122-4.py` (sha 37e1a6360779926133bc3e8dedb9979639e0f5aa2cd499945f22e43133e2c9ae). The full receipts are embedded below (§F4.13) so the committed record is self-contained (ONLY this deliverable is committed; the receipt files ride the disk under probes/, the established pattern).

## F4.13 The raw receipts (embedded — byte-verified, the fire's full files)
### F4.13.1 The run ledger — WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json (sha256 8df7b27ac6adf479a0692005930c6cd161ed02acb25a784aeac8b897654a31de)
```json
{
  "battery": "battery_luna",
  "seat": "qwen/qwen4-max:free",
  "dry_run": true,
  "reshape": false,
  "audience": "internal",
  "n_per_arm": 5,
  "ts": "2026-11-22T15:29:46Z",
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
        "seat": 5,
        "harness": 0,
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
      "reader_last_error": null,
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
        "seat": 3,
        "harness": 2,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": 0.6,
      "mean_f3b": 0.6,
      "f3b_reasons": [
        "harness",
        "harness"
      ],
      "cost": 2.335,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"The requested model is temporarily at capacity upstream. This is not your API key's rate limit ",
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
        "seat": 3,
        "harness": 2,
        "refused": 0,
        "hedged": 0
      },
      "headline_abstention": 0.0,
      "sensitivity_abstention": 1.0,
      "empty_data_quality": 5,
      "stale_confident": 0,
      "bridge_compliance": 0.6,
      "mean_f3b": 0.6,
      "f3b_reasons": [
        "harness",
        "harness"
      ],
      "cost": 2.335,
      "reader_calls": 5,
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"The requested model is temporarily at capacity upstream. This is not your API key's rate limit ",
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
        "seat": 3,
        "harness": 2,
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
      "reader_last_error": "HTTP 429: {\"status\":429,\"message\":\"The requested model is temporarily at capacity upstream. This is not your API key's rate limit ",
      "applied_delta_log": []
    }
  },
  "episodes": [
    {
      "arm": "A",
      "episode": 0,
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "B0",
      "episode": 2,
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 2,
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
      "audience": "internal"
    },
    {
      "arm": "B1",
      "episode": 3,
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
      "rhea": "E",
      "eahq": "ABSTAIN",
      "correct": false,
      "f1": 1,
      "f2": 1,
      "f3b": 1,
      "f3b_reason": null,
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
      "answer": null,
      "class": "C5a",
      "pattern": "empty",
      "matches": [],
      "empty_reason": "seat",
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
    "ts": "2026-11-22T15:29:46Z"
  },
  "judge_pipeline_direct": {
    "ok": true,
    "correct": 20,
    "n": 20
  },
  "f3b_environment": {
    "baseline_loss_band": "elevated-loss",
    "window_loss": 0.4,
    "window": {
      "start": "2026-11-22T15:29:46Z",
      "end": "2026-11-22T15:29:46Z"
    }
  },
  "cost_total": 7.005
}
```
### F4.13.2 The per-call seat-truth — WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl (sha256 5ce179e850beba5dde994e65b8933a20c85f1fb55db8c8e3fa447b62531ebb41)
```jsonl
{"seq": 1, "ts_start": "2026-11-22T15:29:46Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 200, "ts_end": "2026-11-22T15:29:49Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 86, "completion_tokens": 24, "total_tokens": 110, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 2, "ts_start": "2026-11-22T15:29:49Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 200, "ts_end": "2026-11-22T15:29:50Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 86, "completion_tokens": 24, "total_tokens": 110, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 3, "ts_start": "2026-11-22T15:29:50Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 200, "ts_end": "2026-11-22T15:29:53Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 86, "completion_tokens": 24, "total_tokens": 110, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 4, "ts_start": "2026-11-22T15:29:53Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 200, "ts_end": "2026-11-22T15:29:55Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 86, "completion_tokens": 24, "total_tokens": 110, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 5, "ts_start": "2026-11-22T15:29:55Z", "arm_inferred": "A", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6bf67cadd24bda5813113bf368225242fe33d2da60c7dc03ffdb41f00bdf4a3f", "prompt_lines": 11, "http_status": 200, "ts_end": "2026-11-22T15:29:57Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 86, "completion_tokens": 24, "total_tokens": 110, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 6, "ts_start": "2026-11-22T15:29:57Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "2980067d6990c42a243226d25c19c355e488245010684220cb9cc8c74452c9da", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T15:29:58Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
{"seq": 7, "ts_start": "2026-11-22T15:29:58Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "d7663c078277f5841f7f73bce49b7def5db5f87b318e877fe15fc23d0b54deed", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:00Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 8, "ts_start": "2026-11-22T15:30:00Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "c0a71af8728780ccb2a4d86329bf3dc7b4492c11d2e9e06806cef277a8ba437f", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:03Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 9, "ts_start": "2026-11-22T15:30:03Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "26e9861b8c8f44208a3d3ec394671f8ef90d261cf9cdc78e2502a14b5e978819", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T15:30:04Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
{"seq": 10, "ts_start": "2026-11-22T15:30:04Z", "arm_inferred": "B0", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "cc0cf4df3fe71f70652e6b4c8c902be597a19e23059cef7e59d9b717a65ca72c", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:07Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 11, "ts_start": "2026-11-22T15:30:07Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "2980067d6990c42a243226d25c19c355e488245010684220cb9cc8c74452c9da", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T15:30:09Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
{"seq": 12, "ts_start": "2026-11-22T15:30:09Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "d7663c078277f5841f7f73bce49b7def5db5f87b318e877fe15fc23d0b54deed", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:12Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 13, "ts_start": "2026-11-22T15:30:12Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "c0a71af8728780ccb2a4d86329bf3dc7b4492c11d2e9e06806cef277a8ba437f", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:15Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 14, "ts_start": "2026-11-22T15:30:15Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "26e9861b8c8f44208a3d3ec394671f8ef90d261cf9cdc78e2502a14b5e978819", "prompt_lines": 12, "http_status": 200, "ts_end": "2026-11-22T15:30:18Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 107, "completion_tokens": 24, "total_tokens": 131, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 15, "ts_start": "2026-11-22T15:30:18Z", "arm_inferred": "B1", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": true, "logit_bias": {"0": -2.0, "1": -2.0, "2": -2.0, "3": -2.0, "4": -2.0, "5": -2.0, "6": -2.0, "8": -2.0, "9": -2.0}, "prompt_sha256": "cc0cf4df3fe71f70652e6b4c8c902be597a19e23059cef7e59d9b717a65ca72c", "prompt_lines": 12, "http_status": 429, "ts_end": "2026-11-22T15:30:19Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
{"seq": 16, "ts_start": "2026-11-22T15:30:19Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "2e4bcf999ecbe52fafa8bbfe1ada6c5d822e423ef8403b2fee54935d283dd515", "prompt_lines": 6, "http_status": 200, "ts_end": "2026-11-22T15:30:21Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 79, "completion_tokens": 24, "total_tokens": 103, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 17, "ts_start": "2026-11-22T15:30:21Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "6e333a0b55da0a2058dd61bf49b904c9f6451ae1f0e6efbb06eb9c1dc656c89b", "prompt_lines": 6, "http_status": 200, "ts_end": "2026-11-22T15:30:25Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 83, "completion_tokens": 24, "total_tokens": 107, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 18, "ts_start": "2026-11-22T15:30:25Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "b56fee68eb7ac6d05873e85f22c9a3fee7330236ce526a24a169da8fc02786ce", "prompt_lines": 6, "http_status": 200, "ts_end": "2026-11-22T15:30:29Z", "responding_model": "qwen/qwen4-max:free", "usage": {"prompt_tokens": 83, "completion_tokens": 24, "total_tokens": 107, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 24, "image_tokens": 0, "audio_tokens": 0}, "cost": 0, "cost_details": {"source": "nas_model_override", "floor_applied": false, "rate_source": "nas_model_override"}}, "response_parse_error": "AttributeError: 'NoneType' object has no attribute 'encode'", "ratelimit_headers": {}}
{"seq": 19, "ts_start": "2026-11-22T15:30:29Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "e65bc1d7e4913f4282ca2e00cafb95fad67cb5a7f37cb96cefa9b0aa4aed2649", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T15:30:29Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
{"seq": 20, "ts_start": "2026-11-22T15:30:29Z", "arm_inferred": "C", "request_model": "qwen/qwen4-max:free", "max_tokens": 24, "temperature": 0, "logit_bias_present": false, "logit_bias": null, "prompt_sha256": "8ec2e9cc66697cb5744adc509cfdd04e94f353be943fed32845960b42efc253a", "prompt_lines": 6, "http_status": 429, "ts_end": "2026-11-22T15:30:30Z", "responding_model": null, "error_class": "HTTPError", "error_str": "HTTP Error 429: Too Many Requests", "ratelimit_headers": {"retry-after": "30"}}
```
### F4.13.3 Pre-run hash receipt — WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json (sha256 840bd16b08a417124925a765faeaa00f8a951ea710c25ed7eda09634611219e2)
```json
{
  "ts": "2026-11-22T15:29:28Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "matches_baseline": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "matches_baseline": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "matches_baseline": true
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "bytes": 5780092000,
    "matches_baseline": true
  },
  "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,",
  "git_head": "9bb9162bb84a3ceef9fe191d495c71e04c42691e",
  "branch": "study/rfc-143379-rig-20261105",
  "seat_requested": "qwen/qwen4-max:free",
  "endpoint": "https://inference-api.nousresearch.com/v1/chat/completions",
  "baseline_ok": true
}
```
### F4.13.4 Post-run rollback receipt — WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json (sha256 20b6ad31477f5becfc9010397d6ea6692f69f4c7dfbd36f04cd28960aa37bfc4)
```json
{
  "ts": "2026-11-22T15:30:30Z",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "matches_baseline": true,
      "match": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "matches_baseline": true,
      "match": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "matches_baseline": true,
      "match": true
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "bytes": 5780092000,
    "matches_baseline": true,
    "match": true
  },
  "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,",
  "checks": {
    "new_weight_files": "NONE",
    "bias_v3_line_unchanged": true,
    "run_written": [
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json",
      "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/probes/WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json"
    ]
  },
  "all_match": true
}
```
### F4.13.5 This pass's LIVE door re-verify — WEIGHTS-RUNG-REFIRE4-DOOR-REVERIFY-20261122.json (sha256 89ce5f7ff244cf53be68dea33a079ccf837314a3584ab27e8c7f8b42bb7c4f9f)
```json
{
  "ts": "2026-11-22T18:19:18Z",
  "pass": "fire-4 record-landing door re-verify (this pass, live re-hash)",
  "harness": {
    "battery_luna.py": {
      "sha256": "0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd",
      "bytes": 25805,
      "matches_baseline": true
    },
    "battery_pilot.py": {
      "sha256": "89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde",
      "bytes": 5558,
      "matches_baseline": true
    },
    "judge_control_gate.py": {
      "sha256": "697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39",
      "bytes": 2909,
      "matches_baseline": true
    }
  },
  "gguf": {
    "path": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf",
    "sha256": "afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176",
    "bytes": 5780092000,
    "matches_baseline": true
  },
  "gguf_hash_seconds": 18.4,
  "prerun_receipt_sha256": "840bd16b08a417124925a765faeaa00f8a951ea710c25ed7eda09634611219e2",
  "postrun_receipt_sha256": "20b6ad31477f5becfc9010397d6ea6692f69f4c7dfbd36f04cd28960aa37bfc4",
  "postrun_all_match": true,
  "checks": {
    "new_weight_files_since_prerun": "NONE",
    "bias_v3_line": "108:BIAS_V3 = {str(i): -2.0 for i in range(10) if i != 7}  # A3/B1-V3: the SAME tokenizer-validated set,"
  },
  "git_head": "284305554d912c1bcece5832a78bf5d5f476a20b",
  "branch": "study/rfc-143379-rig-20261105",
  "record_pre_append": {
    "bytes": 76677,
    "sha256": "c6d647ff620cb1253d7b1d5bb04033822fbf9f7649b4c4c302d8a553c5497317"
  },
  "all_match": true
}
```
### F4.13.6 The runner delta — refire_runner_20261122-4.py (sha256 37e1a6360779926133bc3e8dedb9979639e0f5aa2cd499945f22e43133e2c9ae) == fire #3's runner (§12.5) modulo the receipt-path constants
```diff
--- refire_runner_20261122.py (fire #3, embedded §12.5)
+++ refire_runner_20261122-4.py (fire #4)
@@ -14,6 +14,6 @@
 Receipts (all under studies/rfc-143379-rig/probes/):
-  WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json    — pre-run hash state (the door baseline)
-  WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl  — per-call seat-truth, flushed per call
-  WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json — the run ledger (harness-written)
-  WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json   — post-run rollback verify
+  WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json    — pre-run hash state (the door baseline)
+  WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl  — per-call seat-truth, flushed per call
+  WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json — the run ledger (harness-written)
+  WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json   — post-run rollback verify
 """
@@ -35,6 +35,6 @@
 
-PRERUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-PRERUN-20261122.json")
-SEATLOG = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-SEATLOG-20261122.jsonl")
-LEDGER = os.path.join(PROBES, "WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-3.json")
-POSTRUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE-POSTRUN-20261122.json")
+PRERUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE4-PRERUN-20261122.json")
+SEATLOG = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE4-SEATLOG-20261122.jsonl")
+LEDGER = os.path.join(PROBES, "WEIGHTS-RUNG-SETTLEMENT-QWEN4-20261122-4.json")
+POSTRUN = os.path.join(PROBES, "WEIGHTS-RUNG-REFIRE4-POSTRUN-20261122.json")
```
### F4.13.7 Append-only integrity receipt
The record's pre-append prefix = **76,677 bytes**, sha256 `c6d647ff620cb1253d7b1d5bb04033822fbf9f7649b4c4c302d8a553c5497317` (the fire-#3 record at commit d6dfd96c24). This pass appended §F4 in three chunks; after EACH chunk the first 76,677 bytes were re-hashed programmatically and confirmed **byte-identical** to the pre-append sha (the landing pass's executed check, never a claim). History above this section is never rewritten. Two-way door: delete this §F4 section to revert to the fire-#3 record; the pre-reg's bars (§4) and the fire-#3 receipts are untouched.
