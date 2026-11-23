# STAGE-PLAN-BATTERIES-20261123 — the verification-batteries' matrix-plan

*Planner: PLANNER-3, seat `meituan/longcat-2.5:free` (slice 3/4 of the stage's planning-fleet). This document is the PLAN only — no battery is fired, no probe run, no verdict rendered here. The proxy approves or reloops.*
*Study branch: `study/rfc-143379-rig-20261105` · Date: 2026-11-23 · Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/STAGE-PLAN-BATTERIES-20261123.md`.*
*Hard lines (binding, carried in every fire brief): nothing public · **RFC #143379 quiet · #5320 quiet · #157065 quiet** · NO installs · ALL LOCAL reads via `read_file` / `git` (never `web_extract`) · never push · never `git checkout --` / `git stash` / `git rm -rf` · master append-only · commit as `kanban-pilot <pilot@rig.local>`, study paths only.*
*Wall clause (binding, verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*
*Armament (settled-shapes-is-the-contract): **think-tank** (the spine: classify → choose → probe → evaluate → adopt-or-park → standardize → verify) + **agent-work-review** (the adversarial second lens: re-derive the load-bearing numbers from tree bytes, hunt overclaims, challenge the inherited receipts). The rest named-and-refused (§8).*

---

## §0 THE REGISTER (the one-pass input, read in full, tree-first)

**The batteries' records read in full (all `read_file`, LOCAL):**
- `WEIGHTS-RUNG-PRE-REG-20261121.md` (99 L) — the settlement's pre-registration: §3 design, §4 bars, §5 in-run-C + two-way door.
- `OPUS-A3-WEIGHTS-DRYRUN-20261120.md` (74 L) — the A3's dry-run class protocol: 4-arm A/B0/B1/C n5, the B0/B1 expected-state row, in-run-C, the verbatim CERTIFY bars.
- `WEIGHTS-RUNG-BATTERY-20261122.md` (892 L, incl. §13/§14 settlement fires #1/#2) + `WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md` (3,284 L, fire #3) — the UNKNOWN record, the per-call seatlog, the two-way door's byte-verification.
- `plan/tank/SETTLEMENT-FIRE5-20261123.md` (185 L) — the just-landed fire #5: the content-bearing window, the void's totality falsified, TARGET-1..4.
- `plan/tank/OPUS-PILOT-KIT-20261121.md` (231 L) — the pilot kit's launch package (the spine/face/armor; the gather's compose).
- `plan/PILOT-KIT-PLAN-20261121.md` (the pilot-kit-plan) + `plan/tank/briefs/GATHER-BRIEF-20261121.md` + `plan/tank/briefs/CROSS-AUDIT-BRIEFS.md` — the gather/cross-audit contracts.
- The master's folds: `MISSION-BRIEF-MASTER-20261119.md` §7-h..§7-n (the A3 arc), §7-z/§7-ac/§7-af/§7-ai/§7-al/§7-an/§7-ao/§7-ap/§7-aq/§7-ar/§7-as/§7-at/§7-au/§7-av (the weights rung's fires #0–#5 + the readiness repair), §7-bn (fire #5's fold).
- The harness: `probes/battery_luna.py` (537 L, read in full), `probes/battery_pilot.py`, `probes/judge_control_gate.py`; `probes/A3-B1P-SIGMA-QWEN4-20261121.md` (the B′ control's NOT_RUN ledger).
- The gate-battery's artifact: `kanban-pilot-workdir/.worktrees/t_2a6b031f/docs/mission-flow/GAP-3-300-gate-battery/` (`run-record.md`, `verdict-row.md`, `ledger.json`, `battery.py`).
- The sibling slices (the stage's planning-fleet): `plan/tank/STAGE-PLAN-CROSSAUDIT-20261123.md` (PLANNER-1) + `plan/tank/STAGE-PLAN-FLEETMATRIX-20261123.md`.

**The load-bearing pins (tree-verified, carried):** harness `battery_luna.py` sha256 `0f08b06936db875376869e168ae3f30398bc46da6bfba2caa38b78f0f556ecfd` (25,805 B) · `battery_pilot.py` `89fd91f23ff91155f0bc285f8a4f001681b8409cc8faead31a279551bbea4fde` (5,558 B) · `judge_control_gate.py` `697cdbd74e2325bace122d01959abae0a665de5959b9e82b95ab656a94f9ee39` (2,909 B) · GGUF `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` (5,780,092,000 B) · `BIAS_V3` source line `battery_luna.py:108` = `{str(i): -2.0 for i in range(10) if i != 7}` (id-7 named dead) · the harness reader's `max_tokens = 24` (`battery_luna.py:160`).

---

## §1 THE BATTERIES' MATRIX (four batteries + two supporting instruments)

Each row = one battery's firing-design. The count is **4 batteries**; the shared judge-control pre-gate and the element/palette legs are supporting instruments, not batteries.

| # | Battery | Firing-design (verbatim bars / mechanism) | Seat(s) | Status |
|---|---|---|---|---|
| **B1** | **The A3-arc battery** (the dry-run class protocol) | 4-arm **A / B0 / B1 / C**, n5/arm (`dry_run` auto at n≤5), cut 6. **A** = baseline, no record-invitation, bias=0. **B0** = the current harness shape, bias vector = 0 (exact rollback state). **B1** = the JitRL-modulated shape, `z′ = z + β·Â`, **zero gradients**, riding `logit_bias = BIAS_V3`. **C** = evidence-only oracle, **re-measured IN-RUN** (never carried-over-vacuous). Judge-control gate **F3a FIRST** (20 known pairs, deterministic exact-match); a NULL aborts unread. Per-episode **f3b** (0/1/1.0); exact-match judge; gate clean = `f3b = 1.0` **and** `harness = 0`; baseline-clean; `C − A < 5 → INCONCLUSIVE`. **Bars (verbatim):** `CERTIFY iff B1−B0 ≥ 20pp AND B1 ≥ 0.85C` · `FALSIFY iff B1−B0 < 20 OR (B1 < 0.85C AND B1 ≤ B0)` · `INCONCLUSIVE iff judge fail / cache missing / C−A < 5 / mean(F3b) < 1`. Runs: B1 dry-run V1/V2/V3 (qwen4 / hy4 / solar / floor), the **B′ sigma-notes control** (one-string invitation, env-gated `HARNESS_SIGMA_NOTE=1`, additive + revertible, **excluded from the CERTIFY arithmetic**), the weights dry-run. | hy4 first (the named powerhouse); qwen4 re-probe at fire; the local-floor GGUF host; solar | fires landed; receipts on disk (`probes/A3-*`) |
| **B2** | **The weights-rung battery (`battery_luna`)** — the settlement's pre-registered fire | The same harness, pre-registered unchanged. 4-arm A/B0/B1/C n5, `BIAS_V3` the zero-gradient expression, per-call `applied_delta_log`. **Bars (pre-reg §4, immutable):** `B0 ≥ 20pp` · `B1 ≥ 20pp` · `B1 ≥ 0.85C` · `B1 − B0 ≥ 20pp`; in-run-C; the degenerate-ceiling trap named (`B1 ≥ 0.85C` true only at C=0 is **degenerate, never a silent pass**). Two-way door: zero weights = exact rollback. | the flagship `qwen/qwen4-max:free` (ARM 0); sibling voices `solar-mini4:free` + the GGUF floor | fires #0–#5 landed; all **UNKNOWN** (transport-walled / void) |
| **B3** | **The A/B0/B1/C n5 settling battery** (TARGET-2) | The **full 4-arm A/B0/B1/C n5** fired at a **content-bearing window** on the seated voice, with a **max_tokens budget that leaves room for visible content** (the reasoning-exhaustion-24 seam — a plan-owner's call; a lane may NOT alter the harness) + the **per-call content-receipt** (`content_head` + `content_sha256` + `reasoning_tokens` + `max_tokens`, TARGET-1's repair). Then the immutable bars `B1 ≥ 20pp · B0 ≥ 20pp · B1 ≥ 0.85C` on a **valid seat-response set with C measurable**. The single run that can move UNKNOWN → COVERED / PARTIALLY-COVERED / GAP. | the seated voice at a content-bearing window — `tencent/hy4-flash:free` (the fire-#5-proven content-bearing voice) primary; `qwen/qwen4-max:free` the re-probed alternate; the floor (Nemo) the unmetered repeatability leg | **NOT FIRED** — the head's next-ring call via the standing fallback ladder |
| **B4** | **The gate-battery** (GAP-3's 300+ gate battery) | **7 rungs:** `config` · `Gate S` · `junction completeness (J3/J4)` · `read-side decision gate` · `channel choice (2611.19700)` · `resolution variance (2611.23068)` · `300+ gate criterion`. The bar: **anchor-full wall, ≥0pp at 300+ cycles, 4–8×, logged-miss discriminator**. Model-execution rows recorded **BLOCKED** if quota is exhausted — never fabricated. Certification = **NOT-YET-CERTIFIED** until the candidate mechanism is executed over the 300+ cycles (the M1 stamp certifies persistence of the iterate-do-not-one-shot method, **not** the gate). | **Nemo (`meituan/longcat-2.5:free`)** — the sole-capacity leg (unmetered; the 429s do not touch it); the support seats for repeatability | 3 PASS / 4 BLOCKED; verdict-row landed |

**The two supporting instruments (not counted as batteries):**
- **The shared judge-control pre-gate (F3a).** 20 known pairs, deterministic exact-match, runs FIRST inside every battery before any seat call; a NULL aborts the run unread. It is the honesty mechanism that separates a grading-pipeline defect from a seat/transport wall. Receipt: `judge_control.ok`, `accuracy 1.0`, `control_n 20`, `judge_pipeline_direct 20/20`.
- **The element/palette batteries** (`BATTERY-ELEMENT-FLEET-{HY4,QWEN4,SOLAR,STEPPFUN,LONGCAT}`, `BATTERY-ELEMENT-3OLTAN-{DP,NEMO}`, the REAL ledgers) — the five-seat palette's empirical map; the 4/4 suite is the repeatability check. Ridden by 3oltan + the local floor (241), never the main fleet.

**The seam named (never smoothed):** the fleet-matrix slice assigns `battery_luna` to the **Nemo-heavy** leg (§3.5), while the weights-rung pre-reg pins ARM 0 to the **flagship window** (`qwen/qwen4-max:free`). The reconciliation: the flagship-class **window seat** is the weights-rung's primary (the pre-reg's ARM 0, fires #0–#5); Nemo is the **unmetered repeatability/floor leg** (the GGUF host + the heavy gate-battery volume). The two are different instruments, not a conflict — recorded here so no lane silently re-seats the rung.

---

## §2 THE SEAT-ASSIGNMENTS + THE CONTENT-BEARING-WINDOW GATE

### 2-a Seat-assignments (per battery, exact designations)

| Battery | Primary seat | Alternate / repeatability | Rationale |
|---|---|---|---|
| **B1** A3-arc | `tencent/hy4-flash:free` (first arm) | `qwen/qwen4-max:free` (re-probe at fire) · the local-floor GGUF host · `upstage/solar-mini4:free` | the A3 pre-reg's §3 seat truth: hy4 the named powerhouse; qwen4 was at capacity at the 2026-11-20 probe — a walled moment is never a doctrine |
| **B2** weights-rung | `qwen/qwen4-max:free` (full-literal free id via env, never colon-split — the SKEW-NONFREE class avoided) | `upstage/solar-mini4:free` · the GGUF floor | ARM 0's seat; the flagship's window is the clock |
| **B3** settling | `tencent/hy4-flash:free` (the fire-#5-proven content-bearing voice) | `qwen/qwen4-max:free` (re-probed) · the floor (Nemo) | the content-bearing window is stochastic (fire #5: 1/20 possible, not guaranteed); the seat is re-probed at fire |
| **B4** gate-battery | `meituan/longcat-2.5:free` (Nemo, unmetered) | the support seats (repeatability) | the 300+ cycle volume is unmetered; the fair-share envelope does not cap it; never the main fleet |

### 2-b The content-bearing-window gate (the probe-caveat, binding at EVERY fire)

> **The probe-caveat: 200-with-emptiness — a fire WITHOUT the content-verification is a VOID-CLASS fire.**

- **The caveat's evidence:** fire #4 produced 14×HTTP-200 with `reasoning_tokens = completion_tokens = max_tokens = 24` and `content = null` (the reasoning-exhaustion-24 void); fire #5, at a fresh window, produced **HTTP 200 + visible content + 16 reasoning-tokens**, PIN-READ-BACK VERIFIED. The void's **totality is falsified** and reclassified **window-conditional/stochastic** — a content-bearing window is reachable, and the settling experiment must run the full battery at one.
- **The gate (every fire carries BOTH):**
  1. **The dispatch probe** — a REAL question (never a dry-run stub) posed to the exact pinned seat at a fresh window, at a **max_tokens budget that leaves room for visible content** (the harness's `max_tokens = 24` is the seam; the probe's budget is a plan-owner's call). Positive-token read: grep the expected reply token, never the absence of failure strings. PIN read-back verified (the seat echoes its own id).
  2. **The per-call content-receipt** — `content_head` + `content_sha256` + `reasoning_tokens` + `max_tokens` recorded per call, so the void/content split is graded at the **cell level** instead of collapsing `null → seat-empty` (TARGET-1's repair; closes fire #5's OI-3).
- **The void-class rule:** a fire lacking (1) or (2) is a **VOID-CLASS fire** — its verdict is **UNKNOWN**, its bars are **unevaluable**, and it is **never counted** as a settlement. A 200 probe at fire-time does NOT guarantee a battery window (the flapping seat: a 200 probe and a 429 inside the same battery, minutes-scale).
- **The seat-truth rule:** every reader call's status + responding model recorded; `responding_model = None` on a 429 (no generation) is distinct from a seat-empty. The S8 split (`by_reason.harness` vs `by_reason.seat`) is the honesty mechanism: a harness/transport bug cannot silently null the leg's substrate claim.

---

## §3 THE RECEIPTS' FORM (the raw calls, the shas, the two-way door's live-verification)

**Every fire lands a raw receipt at its named path, in this shape:**

1. **The raw calls — the per-call seatlog (JSONL, flushed per call).** One row per reader call: `seq · arm · HTTP status · responding_model · retry-after (s) · logit_bias presence + vector · request_model · max_tokens · temperature · prompt sha256 + line-count · content_head + content_sha256 · reasoning_tokens · ts_start · ts_end`. The B1 block's `logit_bias` must equal `BIAS_V3` on exactly the B1 seqs (the anti-fabrication log; zero gradient flowed).
2. **The shas — the harness + weight baseline.** `battery_luna.py` `0f08b069…ecfd` · `battery_pilot.py` `89fd91f2…a4fde` · `judge_control_gate.py` `697cdbd7…9ee39` · `BIAS_V3` line 108 unchanged · GGUF `afa0567d…` (== the §7-k LFS oid) · the git HEAD/pin at fire. The runner **hash-gates** these BEFORE firing (`baseline_ok` must be true or the fire aborts — never fire on an altered harness).
3. **The two-way door's live-verification (executed, byte-for-byte).** Pre-run + post-run hash receipts; `all_match: true`; **new weight files: NONE** (scan `*.gguf/*.bin/*.safetensors/*.pt/*.ckpt` newer than the pre-run receipt → empty); the GGUF mtime pre-dates every fire; the B0 arm rode `bias=None` (the zero-weight control). The modulation was a per-request parameter, gone with the process.
4. **The verdict row (the battery's own ruler).** The raw per-arm table (`correct · accuracy · cells R/H/E/A · by_reason{seat,harness} · mean_f3b · bridge · applied deltas · reader_last_error`) + the bars applied immutable + the degenerate-ceiling named + the verdict ∈ {COVERED, PARTIALLY-COVERED, GAP, UNKNOWN} + the settling evidence named.
5. **The content-receipt (the gate's proof).** The dispatch probe's PIN echo + `content_head` + `reasoning_tokens` + `max_tokens`; the per-cell content/null split. **A fire without this row is void-class.**
6. **The commit.** `kanban-pilot <pilot@rig.local>`, study paths only, on the current HEAD re-checked at commit; never push; the master's append-only.

**The honesty rule:** receipts are the record's, never claims. A NOT_RUN ledger (no cells, no expected values written, zero tokens spent) is the honest admission — never a smoothed verdict. A committed workflow definition is NOT execution; a battery is "run" only when the raw PASS/FAIL receipt exists.

---

## §4 THE SEQUENCING (which batteries fire before/after the cross-audit's lanes)

The stage's spine: **brainstorm → cross-audit (three blind lanes) → AoA → GATHER**. The cross-audit's lanes (lane-BA audits B's design · lane-AA audits A's form · lane-CA audits C's layer) are a **parallel fan**; the AoA fires only on **3 verified landings**; the gather composes the OPUS launch package (the spine + the face + the armor).

| Phase | Battery legs | Ordering law |
|---|---|---|
| **BEFORE the cross-audit's lanes** | **B1** (the A3-arc runs) + **B2** (the weights-rung's `battery_luna`) | These are the **existing verification legs** — their receipts are on disk and are the **ground/subject** the cross-audit's lane-CA re-derives (the verification-readiness layer audits the batteries' reality). A confirmation leg never precedes the artifact it confirms. |
| **IN PARALLEL with the cross-audit's lanes** | **B4's structural rungs** (`config`, `Gate S`, `channel choice`) + the **element/palette legs** | Independent deterministic/structural rows; no dependency on the audits. Their receipts feed the palette map + the gate-battery's certification. |
| **AFTER the cross-audit's lanes + the AoA, BEFORE the gather** | **B3** (the settling battery) + **B4's model-execution rungs** (junction completeness, read-side decision gate, resolution variance, 300+ gate) | B3 needs the readiness layer's verified verdict + TARGET-1's content-receipt repair landed first; B4's model rows need the independence layer. Both are the **certification legs** whose verdicts ride INTO the gather's launch package. |
| **INTO the gather** | all batteries' verdicts + receipts | the gather's launch package holds the spine + the face + the armor; the batteries' certification rows are the armor's measured core. |

**The never-double-fire discipline (binding at every phase):** a seat that 429s is not re-fired the same leg same window; the retry-after is honored; no rotation beyond the standing config; no n20 expansion; no harness edit; no `max_tokens` alteration by a lane (a plan-owner's call only). A battery's leg carries its own pin and its own landing row — a matrix run is a battery, not a demo (every gate measured, named, recorded raw).

---

## §5 THE FAILURE-CLASSES (each's handling)

| Class | Definition | Handling |
|---|---|---|
| **UNKNOWN-class** | The measurement is **voided at the transport layer** — no valid seat-response set at the dry-run scale (fires #0–#5: 20/20 or 0/20 transport voids, `by_reason.seat = 0`). | Verdict **UNKNOWN**; the **settling evidence named** (a valid non-429 seat-response set with C measurable); the bars **immutable and unevaluable**; the wall reported as a **QUESTION with receipts**; the lane **STOPS at the wall** — no rotation, no retry loop, no n20, no re-fire at the named reset. The degenerate ceiling (`B1 ≥ 0.85C` at C=0) is named, never a silent pass. |
| **VOID-class** | A fire **WITHOUT the content-verification** — the 200-with-emptiness caveat (the reasoning-exhaustion-24 null). | The fire is **void-class**: verdict **UNKNOWN**, bars **unevaluable**, **never counted** as a settlement. The content-receipt (`content_head` + `content_sha256` + `reasoning_tokens` + `max_tokens`) must be carried (TARGET-1). A 200 probe at fire-time does NOT guarantee a battery window. |
| **429-class** | The seat's rate-limit layer, **two message classes**: **fair-share** (key-level, demand-adaptive, carries a named `retry-after` reset — e.g. 384s→371s → a fixed epoch ≈ 13:29:35Z) vs **upstream-capacity** (provider-level, "not your API key's rate limit — retry shortly", no named reset). | **Never-double-fire**; the `retry-after` honored; the window-loss class named; the re-fire gate goes to the **chair** (the W2 pre-reg amendment + the k-term W2-empty-suppressed tier settlement) — named, never self-gated. The flapping seat (a 200 probe and a 429 inside one battery, minutes-scale) is a named class, four receipts. |
| **NOT_RUN-class** | No cells exist (a git-only lane, no callable reader seat, a write-gate wall). | The honest NOT_RUN ledger: the precondition receipt recorded first, the treatment fully specified + revertible, **zero expected values written**, zero tokens spent. Never a smoothed verdict. |
| **BLOCKED-class** | The instrument exists; the model-execution row is quota-walled. | Recorded **BLOCKED** (never PASS/FAIL, never fabricated); the certification stays **NOT-YET-CERTIFIED**; the open item names the quota-free rerun. |

---

## §6 THE CONVERGE-CONTRACT INTO THE GATHER

1. **The receipt shape (the envelope).** `id: <runner-id>_<run-id>_<pin> · run: <GitHub run id> · pin: <exact SHA, the checkout's target> · requested: <the dispatch's head_sha> · executed: <git rev-parse HEAD after checkout> · assert: requested == executed (hard, before the suite) · battery: <the test set actually collected at the pin> · summary: <pytest tail: N passed / M failed / K skipped / xpassed> · conclusion: <success | failure> · receipt_url: <the run page>`.
2. **The convergence verdict.** Every battery cell carries a raw receipt (or a NOT-RUN/BLOCKED-with-reason). The converge states the grid's truth — the certification leg's verdict ∈ {COVERED, PARTIALLY-COVERED, GAP, UNKNOWN} + the raw bars + the content-receipts + the two-way door's live-verification + the failure-classes' QUESTIONs — **never a fabricated "all verified."**
3. **The gather's held launch package.** The batteries' certification rows are the **armor's** measured core: the spine (the canary's phase-1 brief, corrected) + the face (the one outside-watcher-visible receipt, provenance-tagged) + the armor (the verification-readiness layer: base-diversity ≥2 distinct pinned bases, the blind-panel protocol, C1–C9 as checkable done-whens, the seeded pin registry). The handoff gate is **CLOSED / GATED, not released**.
4. **The settle-conditions.** The certification closes only when a **full 4-arm A/B0/B1/C n5 battery, fired at a content-bearing window, clears the immutable bars on valid seat data with C measurable** (B3). Until then the rung's settlement is **deferred**, the bars immutable, the question named.
5. **The seams that re-enter the plan loop.** Any NEW finding surfaced at any fire does NOT ride along as an inline patch — it re-enters plan → head decision → leg audit rotation → cold-read adjudication → amend, then re-execute. Executors never self-amend on new findings.

---

## §7 THE NAMED ACTS (every step a named act with its receipt)

- **ACT-1 (the pre-gate, every battery):** the judge-control gate F3a runs FIRST (20 known pairs, exact-match); a NULL aborts unread. **Receipt:** `judge_control.ok` + accuracy + fingerprint.
- **ACT-2 (the content-gate, every fire):** the dispatch probe (real question, content-bearing budget, PIN read-back) + the per-call content-receipt. **Receipt:** the probe's PIN echo + `content_head` + `reasoning_tokens` + `max_tokens`; the per-cell content/null split.
- **ACT-3 (the A3-arc + weights-rung legs):** the existing receipts boarded (B1/B2); the bars applied immutable; the verdicts COVERED/PARTIAL/GAP/UNKNOWN on the record. **Receipt:** the raw per-arm tables + the applied-delta log + the per-call seatlog.
- **ACT-4 (the settling battery, B3):** the full 4-arm n5 at a content-bearing window, the content-receipt carried, the bars applied on a valid seat-response set with C measurable. **Receipt:** the single run's ledger + the bars' arithmetic + the verdict.
- **ACT-5 (the gate-battery, B4):** the 7 rungs; the structural rungs' deterministic rows + the model-execution rungs' measured rows (or BLOCKED-with-quota). **Receipt:** the verdict row + the ledger + the certification state.
- **ACT-6 (the two-way door, every fire):** the pre/post-run hash receipts, `all_match: true`, new_weight_files NONE. **Receipt:** the door JSONs.
- **ACT-7 (the converge):** the grid readout, the certification verdict, the envelope/verdict, the handoff-clip to the gather. **Receipt:** the converge-contract's measured verdict + the handoff-gate CLOSED/GATED.

Every act's receipt is the record's; acts do not fire without a receipt.

---

## §8 NAME-AND-REFUSE

- **Arm (think-tank + agent-work-review):** the spine and the adversarial second lens — classify → choose → probe → evaluate → adopt-or-park → standardize → verify. The matrix is designed within this spine.
- **Refuse (the rest, considered, not loaded):** `aces-harness-probes` (its operative disciplines — judge-control FIRST, full-literal free ids via env, `--bias-log` store_true/vestigial, paired-seed read, never run the same battery twice — are carried verbatim in the batteries' designs and were verified against the harness source read in full) · `evaluating-llms-harness` / `local-llm-serving` / `llama-cpp` / `serving-llms-vllm` (no install, no serving change) · `two-model-reasoning` (no offline-reasoner leg) · `web-storm` / `grounded-citations` / `arxiv` (no field search, LOCAL receipts only) · `memory-chain` (no chain append this slice) · `hermes-agent` / `hermes-gateway-ops` (no config/gateway change) · `safe-file-editing` (designs only) · `systematic-debugging` (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families. A lane that does not arm is a finding — this plan arms only.

---

## §9 HARD LINES + EMISSION CONTRACT

- **nothing public** · **RFC #143379 + #5320 + #157065 QUIET** · **NO installs** · **ALL LOCAL reads** (read_file / git, never web_extract) · **never push** · never `git checkout --` / `git stash` / `git rm -rf` · the master's append-only · the plan, the sealed artifacts, the crons, the anchors, the collaborator's branch **UNALTERED** · the plan-stage's ladder tool names rowed as they resolve, envelope-formed.

**The emission contract:** this file is written FIRST (the batteries' matrix + the fires' designs + the content-verification's gate + the receipts' forms + the converge-contract), then committed as `kanban-pilot <pilot@rig.local>` **ONLY this file, ONLY the study path**, then the sha reported. A parse-fragment-only response has NOT landed — the file is the landing. Exit 0 = the deliverable on disk first, then the report's sha. No execution — the PLAN only; the proxy approves or reloops.

---

*Facimus semper — the plan is a gate state, revisable by evidence; its receipts are the record's.* — the verification-batteries' matrix-plan (slice 3/4 of the stage's planning-fleet; the batteries' legs across the stage).
