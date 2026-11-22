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
