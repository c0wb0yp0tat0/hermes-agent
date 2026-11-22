# MAIN-LOOP-ROUND3-20261122 — the primary pilot-readiness improver loop's THIRD round: the C1a–C6a checkpoints adjudicated

*Seat: `meituan/longcat-2.5:free` — PIN-READ-BACK VERIFIED at the fire. Branch `study/rfc-143379-rig-20261105`.*
*Contract: the brief (`plan/tank/briefs/BRIEF-MAIN-LOOP-ROUND-20261122.md`) + the two predecessor rounds (`MAIN-LOOP-ROUND-20261122.md` bd8c59df95 — the six eats +10; `MAIN-LOOP-ROUND2-20261122.md` 1135dbfa55 — the six continuations +12) + the master folds §7-ai→§7-aq + the targets' sources.*
*Envelope: nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · write ONLY under `studies/rfc-143379-rig/` · all LOCAL paths via `read_file`/`terminal` (never `web_extract`) · NEVER push · never `checkout --`/`stash`/`rm -rf` · index-lock → wait ~10s, retry once.*
*THE PLAN GUARD: the plan, the sealed artifacts, the crons, and the anchors are NEVER altered — the improvements land as the readiness's measured rows and design-rows.*
*Armament: `think-tank` (spine) + `agent-work-review` + `investigation-documentation` — loaded and used; the rest of the catalog named-and-refused (an unarmed lane is a finding).*
*THE WALL CLAUSE: a non-reproduction is a QUESTION with receipts, never a guess, never a silent pass.*

---

## 0. THE INPUT (read IN FULL, in order)

1. **The two predecessor rounds** — `MAIN-LOOP-ROUND-20261122.md` (bd8c59df95: the queue's six eats → +10 measured rows; the readiness PARTIALLY-COVERED with six continuations C1–C6 named; convergence 0 consecutive zero-delta) + `MAIN-LOOP-ROUND2-20261122.md` (1135dbfa55: the six continuations → +12 measured rows; the Kaizen's perpetuity proven; the NEXT SPIN's targets C1a–C6a armed).
2. **The master's folds §7-ai → §7-aq** — §7-ai (the enriched round 69f165f79f) · §7-aj (MISSION-2's field case) · §7-ak (MISSION-3's falsifier audit) · §7-al (the settlement re-fire #4) · §7-am (MISSION-4's sizing arc) · §7-an (MISSION-5's Mandate consideration) · §7-ao (the settlement re-fire #5 — the content-question answered) · §7-ap (the main loop's round, +10) · §7-aq (the continuation round, +12, the next spin C1a–C6a armed).
3. **The targets' sources** — the canary phase-1 spec + its ARM-3b audit + the rung-1 receipt (§7-ae/§7-af) · the read-path regression artifact + its brief · the weights pre-reg + the settlement re-fire record (fires #3/#4) · the falsifier audit (FB-1…FB-8) · the MISSION-5 consideration + sanity (the headroom-sweep question) · the lane-C verification-readiness + the AoA + the lane-CA audit (G2/G3/G4).
4. **The anchors** — `/root/.hermes/memories/MEMORY.md` + `USER.md`, one pass (the register; the GATE LAW's final form: the word gates ONLY public writes outside PR #1 + deep deletions/money — internal doors act, never wait).

---

## 1. THE ROUND'S MISSION

The six checkpoints **C1a–C6a** as the targets, each adjudicated for its **MEASURED improvement** (target → change → raw delta). Every improvement names its target; the **not-for-its-sake gate** held (each row names the measured property it moves); an improvement-less checkpoint = the first zero-delta candidate, recorded honestly (the PARK-candidate, never a forced close). The plan and the sealed artifacts are untouched — the rows below are the readiness's measured rows and design-rows.

---

## 2. THE PER-CHECKPOINT ADJUDICATIONS (target → change → raw delta)

### C1a — the canary-spec's runbook/settle-conditions' next state — **+2 rows**

**Target:** the spec's §0 runbook + §9 settle-conditions' next state (after the ARM-3b audit's DEFECTS-NAMED + the rung-1 receipt's PARTIALLY-COVERED).

**Receipts (re-derived at the bytes):**
- `canary-phase1-spec-20261122.md:18` — §0's count check: “Measured gates = 9 (§3). Judgment fixtures = 5 (§6).”
- `canary-phase1-spec-20261122.md:117` — §3's own count: “**Count = 14 measured gates** (G1–G14).”
- `canary-phase1-spec-20261122.md:159,161,173` — §6's header “F1–F5” + its count line “Count = 5.”, yet **F6 exists** as a paragraph at `:173` (the judgment-layer next rung).
- `canary-phase1-spec-20261122.md:212,225` — §9's settle-conditions: “8 of 8 mapped; 0 dropped.”

**Change (the rows landed):**
- **R1 — the runbook's count-check correction row.** The spec's §0 count-check is stale against the spec's own §3/§6: **gates 9 → 14** (G1–G14) and **fixtures 5 → 6** (F1–F6; §6's header + count line + the F6 row). The spec's bytes are untouched — the correction lands as an append-only design-row (history never rewritten; the gate values are unchanged).
- **R2 — the settle-conditions' next-state row.** The 8 AoA conditions (§9's 8/8 crosswalk) mapped to their rung-2 gate targets: conditions 5/6/7 → **G2/G3/G4 (OPEN)**; the verdict PARTIALLY-COVERED stands until they fire with receipts + the voice-check A4 passes 0-hit + EXT-6's independent row is in (F6).

**Raw delta:** **+2 rows.** The runbook's count-check accuracy moves 2 stale counts → 0 (named); the settle-conditions' next-state moves unmapped → mapped (8/8 with their gate targets). The measured property: the spec's internal count-consistency + the settle-conditions' verdict-moving mapping.

---

### C2a — the G14-carrier's regression suite's state — **+2 rows**

**Target:** the read-path regression suite (the G14 read-path-restore gate's carrier).

**Receipts (re-derived at the tree):**
- `tests/tools/test_memory_read.py` — **ABSENT on disk** (`ls` → No such file) and in **every commit** (`git log --all -- <path>` → 0). The suite exists as the design block in `READ-PATH-TESTS-20261119.md`; the contract's success signal (the materialized file) is **not landed**.
- The suite's RED-before-GREEN pin `af16e3ab16` **carries `read`** (`tools/memory_tool.py:258` `if action == "read":` + the enum at `:406`/`:436`) but is **NOT an ancestor of HEAD** (`git merge-base --is-ancestor af16e3ab16 HEAD` → **NO**).
- The study HEAD's `_STORE_ACTIONS` = `{add, replace, remove, patch}` — **no `read`** (grep 0; the only "read" hits are comments/config reads).

**Change (the rows landed):**
- **R3 — the suite's materialization-state row.** The suite is a **design-only** artifact (0 materialized test files); the contract's success signal is absent. The state is named, not silently carried.
- **R4 — the pin-vs-HEAD divergence row.** The suite's RED-before-GREEN pin is **not on the study branch**; its “the real store on the current head passes it” claim is **FALSE at the study HEAD** (RED at HEAD / GREEN at the pin). The **G14 HOLD re-verified: HOLD holds** (the study HEAD's store has no `read`).

**Raw delta:** **+2 rows.** The suite's state moves undescribed → measured (absent + pin-divergent); the G14 HOLD's re-verification moves asserted → receipted. The measured property: the suite's materialization state + the pin's ancestry.

---

### C3a — the settlement's next-fire pre-reg question — **+3 rows**

**Target:** the weights-rung settlement's next-fire pre-registration — the logger's content-receipt + the harness-vs-seat hint, the question sharpened, the fire's condition named.

**Receipts (fire #4's ledger + seatlog, `WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md` §F4):**
- 14/20 HTTP 200, every 200 `content = null` with `reasoning_tokens = 24 = completion_tokens = max_tokens` (the REASONING-EXHAUSTION-24 seam, §F4.9 OI-1).
- 6/20 HTTP 429 **upstream-capacity** (`retry-after = 30` constant rolling), distinct from fire #3's fair-share fixed-epoch class (§F4.9 OI-2).
- The unchanged harness reads JSON `content: null` as a **seat-reason empty** (`battery_luna.py:170` `.get("content","")` → `None`; `:204–206` `if not txt: reason = "harness" if reader_error else "seat"`).

**Change (the rows landed):**
- **R5 — the logger's content-receipt shape row.** The next fire's per-call logger must capture: HTTP status · the responding-model echo · `usage.completion_tokens` + `usage.completion_tokens_details.reasoning_tokens` · a **content-presence flag** (null vs "") · `content_sha256` · `content_head`. (The fire-#4 seatlog's fields, generalized as the pre-registered shape.)
- **R6 — the harness-vs-seat hint row.** The classification seam named: a null-content 200 is a **VOID** (the seat's own usage: 24/24 reasoning), **not a measured abstention**; the pre-reg must keep the **content-presence test DISTINCT from the abstention test** (the harness's seat-reason classification is the seam, source-read).
- **R7 — the fire's condition row.** The settling evidence sharpened: **a fire where the flagship emits VISIBLE CONTENT within the dry-run's 24-token budget** (C measurable), or a **pre-reg-level budget/seat amendment** (the head's call; the harness + bars immutable here).

**Raw delta:** **+3 rows.** The next-fire pre-reg question moves broad → sharp (the logger shape + the hint + the condition named). The measured property: the settling evidence's specificity.

---

### C4a — FB-1's execution-readiness — **+2 rows**

**Target:** FB-1's test-shape + the read-back's real wiring — the execution path's state.

**Receipts (re-derived at the tree):**
- `tools/write_gate.py` — **ABSENT at the study HEAD** (`git cat-file -t HEAD:tools/write_gate.py` → fatal).
- `verify_post_write` **defined** at the battery `30f08c2a0f:tools/write_gate.py:557` and at `pr-139606` `d1bdb4582c:tools/write_gate.py:650`.
- The **only production call site on the whole fork** = `pr-139606:tools/memory_tool.py:366-367` (the single-op path); **ZERO** call sites at the battery branch's `memory_tool.py` and at the study HEAD (grep 0).
- The batch branch returns `apply_batch` directly (battery `:337` / study HEAD `:270`).

**Change (the rows landed):**
- **R8 — FB-1's test-shape row.** The falsifier (inject a silent `_write_file` loss; assert `operations=[{patch}]` returns a non-success or a disk-attestation) + the guard shape (re-read the target from disk after `apply_batch`, or wire `verify_post_write` into the batch branch, mirroring `pr-139606:366-367`) + the landing-site (the batch branch, or `MemoryStore._batch`).
- **R9 — the read-back's real wiring state row.** **0 call sites at the study HEAD** (the module is absent) + **0 at the battery**; **1 at pr-139606** (single-op only) — the batch path is unwired on every tree. FB-1's execution path is named: the battery lane's (the harness lives on the battery branch; no installs).

**Raw delta:** **+2 rows.** FB-1's execution-readiness moves designed → wired-state-measured (the execution path's state named with per-tree receipts). The measured property: the read-back's real wiring.

---

### C5a — the headroom-alarm's design-rows' integration-state — **+3 rows**

**Target:** the headroom-sweep's unattended-surface question resolved + the alarm-design ledger's integration.

**Receipts:**
- `/root/.hermes/scripts/headroom-sweep.sh:19` — `rm -rf "$d"` over `/root/.hermes/kanban/workspaces` clones/sandboxes **older than 48h**; the job's own prompt guard: “NEVER prune `/root/.lmstudio` or any `*.gguf`”.
- `jobs.json` — the 11th script-bearing entry (`interval` 360m, `model = upstage/solar-mini4:free`); Hermes runs a non-`no_agent` job's `script` as a **pre-run wake-gate** (`cron/scheduler.py:2291-2295`).
- `MISSION-5-SANITY-20261122.md` §1/§6 — the opened QUESTION + the corrected inventory; the GATE LAW (`MEMORY.md:19` — deep deletions are word-gated).

**Change (the rows landed):**
- **R10 — the adjudication row.** headroom-sweep **COUNTS as an unattended surface AND sits in the word-gated deep-deletion class** → the alarm-design names it as a **deep-deletion-class watch** (a violation-alarm, never a gate); its own scope guard (48h age + the model-home exclusions) is carried.
- **R11 — the corrected inventory boundary row.** **11 script-bearing jobs** (the 10 no-agent + headroom-sweep); row 6's write-surface widened (the three `/tmp` removals, `:45`); row 9's network widened (`inference-api.nousresearch.com` + the harness's `bash -lc` + local scribe).
- **R12 — the integration-state row.** The watch rides the rulebook's violation-alarm (exit-1 NEW rows) + the anchor-rot-watcher's +0-decay freshness; the **policy-sha256 checkpoint is a to-be-built instrument** (the anchor-rot-watcher has no sha256 logic); the manifests' tree bearer is still absent (named gap).

**Raw delta:** **+3 rows.** The alarm-design ledger's completeness moves the headroom-sweep uncarried → carried (adjudicated + integrated). The measured property: the alarm ledger's inventory completeness.

---

### C6a — the G2/G3/G4 closure-conditions' state — **+3 rows**

**Target:** the armor's G2/G3/G4 closure conditions.

**Receipts:**
- `lane-c-verification-readiness-20261121.md` §6 — G1 PASS; **G2/G3/G4 OPEN** by construction.
- `aoa-audits-20261121.md` §7 — settle-conditions 5 (independence/G2), 6 (readiness/G3), 7 (stewardship/G4).
- `canary-phase1-spec-20261122.md` §3 G4 row — “Registry was empty → G4 rule-with-no-rows; A5 seed row + one-run-per-pin pending”; the spec-audit O4 — “A5 seed pending”.
- **No pin-registry file on disk** (a filename search returns none; the schema lives as a design in the AoA/lane-CA/OPUS).
- E1's one-command base-diversity check; E2's pin-registry schema + `verify_pin.py`.

**Change (the rows landed):**
- **R13 — G2's base-diversity inventory row.** The family's pinned bases enumerated (the compose base `upstage/solar-mini4:free` — shared by the three audits, the named shared-route constraint; the AoA `qwen4-max`; the main-loop rounds hy4/solar/longcat) + E1's one-command check named as the decidable gate; **G2 stays OPEN** (stage-3 per-unit pinning + ARM 4's distinct-base run + a blind panel on the first numeric landing).
- **R14 — G3's C1–C9 checklist row.** The nine conditions with their done-whens (lane-C §4) + the voice-check A4 grep gate; **G3 stays OPEN** (unfulfilled).
- **R15 — G4's pin-registry seed row.** The schema (`pin_id, owner, base/heap, budget, receipt_sha, expires_at`) + the seed values (rung-1 canary pin `fc8b9934…`/`5747a90e…`; owner = the rotation receipt's R-C executor; `receipt_sha` = **BOTH** keys `25606ba9…` + `f1ed5b0d…`; `expires_at` = the rung-2 window) + the `verify_pin.py` re-derivation gate (E2); the registry file is **ABSENT** → **G4 stays rule-with-no-rows**, the seed is the next action.

**Raw delta:** **+3 rows.** The closure-conditions' state moves carried-unmapped → mapped-with-states (G2/G3/G4 each with its closure condition + its current state). The measured property: the armor's closure-condition coverage.

---

## 3. THE CONVERGENCE STATE

| Round | Commit | Measured rows | Zero-delta checkpoints |
|---|---|---|---|
| 1 | bd8c59df95 | +10 | 0 |
| 2 | 1135dbfa55 | +12 | 0 |
| 3 (this) | (this landing) | **+15** | **0** |

- **Consecutive zero-delta rounds: 0** → the **PARK is NOT triggered**. The loop's perpetuity holds: three consecutive measured rounds (+10, +12, +15), the improvement-loops running as the main task.
- **The not-for-its-sake gate:** each row names its measured property — count-check accuracy (C1a) · suite materialization state + pin ancestry (C2a) · pre-reg sharpness (C3a) · wiring state (C4a) · alarm-ledger completeness (C5a) · closure-condition state (C6a). No row is a restatement; no checkpoint was closed by decree.
- **The first zero-delta candidate:** none this round — all six checkpoints carried a measured improvement.

---

## 4. THE READINESS'S NEW-STATE + THE NEXT SPIN's TARGETS

**The readiness's new-state: PARTIALLY-COVERED.** All six checkpoints carried as measured rows; none closed by decree. The open surfaces, named: the canary's rung-2 gates (G2/G3/G4) · the G14 restore · the settlement's visible-content fire · FB-1's battery execution · the headroom watch's integration · the armor's independence/readiness/stewardship gates.

**THE NEXT SPIN's targets (named — never “waiting”):**
- **C1b** — the spec's review-round lands (the count-check correction applied as an append-only row; the rung-2 gates fire) → the spec's verdict moves toward COVERED.
- **C2b** — the read-path regression suite **materializes** on the study HEAD (`tests/tools/test_memory_read.py`) → the suite GREEN at HEAD / the G14 restore lands.
- **C3b** — the next fire's **pre-registration lands** (the logger's content-receipt shape + the budget/seat decision) → the settlement's next fire at a visible-content window.
- **C4b** — FB-1's test-shape **executes in the armor battery** (the lost-write injection + the batch wiring) → the armor's G1/G2 close.
- **C5b** — the headroom watch **integrates** (the policy-sha256 checkpoint built; the manifests' tree bearer landed).
- **C6b** — the G2/G3/G4 closure conditions **land** (the pin-registry file + `verify_pin`; the base-diversity run; the C1–C9 done-whens) → the armor's verdict moves READY-WITH-NAMED-SEAMS → READY.

---

## 5. THE REGISTER

- **Hard lines ✓:** nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · writes ONLY under `studies/rfc-143379-rig/` · all LOCAL paths via `read_file`/`terminal`, never `web_extract` · NEVER push · never `checkout --`/`stash`/`rm -rf` · index-lock → wait ~10s, retry once.
- **Plan guard ✓:** the plan, the sealed artifacts, the crons, and the anchors untouched; the improvements land as this record's measured rows and design-rows.
- **Emission contract ✓:** this file exists at `plan/tank/MAIN-LOOP-ROUND3-20261122.md` with the per-checkpoint adjudications + the delta + the convergence + the new-state + the next targets inside; written FIRST, then committed, then its sha reported.
- **Termination check ✓:** the round completes with the next targets named; 0 consecutive zero-delta → no PARK; the loop never parks itself while improvements exist.
- **Anchor ✓:** `MEMORY.md` + `USER.md` read; the GATE LAW's final form — the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait.

## 6. COMPOSE-CHECK (8 marks)

| # | Mark | State | Evidence |
|---|---|---|---|
| 1 | deconstruct | FIRED | the two predecessor rounds + the master folds §7-ai→§7-aq + the targets' sources read in full (§0) |
| 2 | sense | FIRED | the six checkpoints C1a–C6a each adjudicated target → change → raw delta (§2) |
| 3 | choose | FIRED | measured improvements only; the improvement-less/zero-delta candidate assessed (none) (§3) |
| 4 | calibrate | FIRED | every receipt re-derived at the bytes/tree (the spec's counts, the absent test file, the pin's ancestry, the wiring call-sites, the headroom script, the absent registry) |
| 5 | probe | FIRED | the tree probed read-only (`git show`/`grep`/`cat-file`/`merge-base`; `ls`; `jobs.json`; `headroom-sweep.sh`) — no installs, no writes outside the deliverable |
| 6 | review | FIRED | the adversarial lens applied: each row's measured property named; no row a restatement; the not-for-its-sake gate held |
| 7 | record | FIRED | this deliverable at its path with the adjudications + the delta + the convergence + the next targets |
| 8 | compose-check | FIRED | this table + the register (§5) inside the file |

*Facimus semper — the round renders on the receipts; the receipts are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a guess, never a silent pass. The loop's next spin is named: C1b–C6b. — kanban-pilot <pilot@rig.local>, 2026-11-22, round three.*
