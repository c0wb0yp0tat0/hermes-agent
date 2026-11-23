# REVERIFY-AMS3-20261123.md — AM-S3's COLD RE-VERIFICATION of the stale-form landings

*Seat: `tencent/hy4-flash:free` (hy), PIN-READ-BACK VERIFIED at the fire · Branch: `study/rfc-143379-rig-20261105` · Date: 2026-11-23 · Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/REVERIFY-AMS3-20261123.md`.*

*This file is the revision-pass's Act 1 (RE-GROUND / STALE-FORM RE-VERIFICATION, AM-S1/AM-S3) of `REVISED-STAGE-PLAN-20261123.md` (landing `93d2def129`, itself folded at `cfed8b30f9`). It re-verifies the pre-revision landings COLD against the amended gates — same artifacts, same commits, receipts-first — and renders no new execution, opens no downstream act, and writes nothing public. A stale-form landing is not amended in place and is not an amended-plan landing until re-verified; its disagreements are named seams fed to the AoA, never "reconciled away."*

*Hard lines (binding): nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · all local reads via `read_file` / local git · never push · never `git checkout --` / `git rm -rf` / `git stash` · master append-only · commit as `kanban-pilot <pilot@rig.local>` · write only under the study · local config left AS FOUND (identity overridden per-commit).*

*Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*

*Armament line (settled-shapes-is-the-contract): **think-tank** (the spine: classify → choose → probe → evaluate → adopt-or-park → standardize → verify) + **agent-work-review** (the adversarial second lens, applied in this file's §0 method: full reads → extraction → consistency matrix → arithmetic re-derivation → identifier cross-check → epistemic scoping → asserted → status → basis; **verify the CLASS, not the flagged instance**). Named-and-refused (considered, not loaded): blind-agent-panels / supervisor-delegation / think-tank-feedback (no consensus fan-out) · codex / claude-code / opencode (no delegate coder for a study-path append) · investigation-documentation (this is a re-verification ledger, not a discovery log) · aces-harness-probes · evaluating-llms-harness · local-llm-serving · llama-cpp · serving-llms-vllm (no install, no harness/serving change — the B1 fire is re-READ, not re-FIRED) · two-model-reasoning (no offline-reasoner leg) · web-storm / grounded-citations / arxiv / browser-harness-sop (no field search — LOCAL receipts only) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no secret-bearing file edited) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families. A lane that does not arm is a finding — this re-verification arms only these two.*

*Emission contract: this file lands on disk FIRST with the re-verifications inside, then the commit as `kanban-pilot` (this path only), then the report's sha. A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.*

---

## 0. Scope, method, and the four amended gates

### 0.1 What was re-read COLD this pass (all via `read_file` / local git)

| # | Artifact | Pin / landing commit | Role in this re-verification |
|---|---|---|---|
| A | `plan/tank/REVISED-STAGE-PLAN-20261123.md` | `93d2def129` (fold `cfed8b30f9`) | the amended gates (AM-C1 / AM-F3 / AM-B1 / AM-S3) and the revised execution order |
| B | `plan/tank/lane-ca-audit-20261121.md` | `f4feeb4fc0` (task-named; supersedes `ef08fe6069` / AoA-cited `6de5aba311`) | fan landing — verdict ADAPT / NOT-READY |
| C | `plan/tank/lane-ba-audit-20261121.md` | `34424e81ac` (task-named; supersedes `7190c0efda` / AoA-cited `2cc6f1832f`) | fan landing — verdict DEFECTS-NAMED (D1–D7) |
| D | `plan/tank/lane-aa-audit-20261121.md` | `760092f1eb` on the branch line (`2ce77ce5ad` is the AoA-cited sibling send; **identical blob** `a2e44cd6…`, verified this pass) | fan landing — verdict DEFECTS-NAMED (D1/D2) |
| E | `plan/tank/MATRIX-LEGRUNS-20261123.md` | `9d74420def` | matrix-legs landing — R 4/4 PASS · P S7 present · C chain-docs+read present · H NOT-RUN |
| F | `plan/tank/B1-A3-ARC-FIRE-20261123.md` | `f32f5ab716` | B1 fire — UNKNOWN / VOID-class, 4 bars NOT EVALUABLE |
| G | `plan/tank/AOA-NINE-AXIS-20261123.md` | `73b4cbead7` (fold `9d56caa557`) | the AoA's settle-conditions + the gather's inputs' readiness (§4 below) |

**Agent-work-review method applied (the class, not the flagged instance).** (i) *Full reads* — all seven artifacts above read to their last line. (ii) *Extraction* — each landing's verdict and load-bearing receipts pulled into §2. (iii) *Consistency matrix* — the landing commits and reported shas cross-checked across all seven docs (§3's identifier seams); the phantom shas `ab660b943b` / `16130475d2` / `f4b845f05b` do **not** resolve in local git (verified: `git rev-parse --verify` → fatal), confirming the AoA's SW-1 class — the class is "report-sha vs landing-sha divergence," swept across all three lanes, not just the flagged instance. (iv) *Arithmetic re-derivation* — B1's decision arithmetic (`B_minus_A = 0.0`; `B_over_0.85C = true` only degenerately at `C = 0`; `C_minus_A = 0.0`) and the matrix's grep-counts (`0/2/0/0`) re-checked against the docs' own decision rules. (v) *Identifier cross-check* — see §3. (vi) *Epistemic scoping* — no landing is promoted to PASS/COVERED beyond its receipts; each verdict's grounding class (DOC / SKILL / LOCAL / seat-response) is stated in §2. (vii) *Unverifiable list* — §3.4 lists what only the owning host can confirm.

### 0.2 The four amended gates, stated plain (quote-faithful to the REVISED plan's §2)

- **AM-C1 (per-fire seat liveness), CROSSAUDIT §2.1:** every seat — BA `meituan/longcat-2.5:free`@p0tat0 · AA `stepfun/step-3.7-flash:free`@c0wb0y · CA `tencent/hy4-flash:free`@cloud · the AoA's fourth base — is **re-probed at dispatch and at every fire** (REAL question, positive-token read + PIN read-back); `stepfun-freeze` and `qwen's-end` are one liveness class; a drained/frozen pin is never re-fired in the same window; the **base-diversity gate (≥2 distinct pinned bases; AoA distinct from all three; re-verified after any pivot)** is a named constraint, never a silent pass.
- **AM-F3 (study-proper fork-set), FLEETMATRIX §2.2:** the matrix's forks are **every locally-held `hermes-agent` branch carrying a substrate arm** — the eight rows re-derived in the plan (study HEAD · `pr-139606` · `pr-141876` · `a9c65dc4` · `re-cut-write-gate-surgical` · `r2gate` · `r2cs`/`r2cs-sync` · `origin/fix/restore-read-action`). **Named-and-refused:** the full `/root/workspace/repos/` suite, all phone-side tooling, the unrelated `origin/*` feature families; wire refs are **watch refs, not legs**; F-16 (no single fork carries the full combination) stays named.
- **AM-B1 (void-class content-gate), BATTERIES §2.3:** a fire **without** (item 1) the real-question dispatch probe at a content-bearing budget with PIN read-back **AND** (item 2) the per-call content-receipt is **VOID-CLASS → verdict UNKNOWN, bars unevaluable, never a settlement**; catalog class, not anomaly; three receipts cited (fire #4's 14×200/24/24/null · fire #5's 200+content+16-tokens · B1's A3-arc fire's 4 probes at 256/128 + 20 cells all null, reproduced at 10× budget). `reasoning == completion == max_tokens` with null content = void at **any** budget; the degenerate ceiling `0 ≥ 0.85×0` at C=0 stays named and refused.
- **AM-S3 (cold-verification form), SEQUENCE §2.4:** pre-revision landings re-verified **cold against the amended gates** — same artifacts, same commits, receipts-first; **version check** (a second send may supersede the first — flag it, never assume); seams named, **none "reconciled away"**; no verdict floats on a stale receipt.

**The two questions the fan re-verification must answer (per the mandate).** Q-A: *were the seats probed at fire?* Q-B: *were any landing's grounding-dependent claims affected by the amended fork-set?* Each is answered explicitly in §2.1–§2.3.

---

## 1. Re-verification ledger — outcomes at a glance

| Landing | Commit re-verified | Gates applied | Outcome | One-line ground |
|---|---|---|---|---|
| fan CA | `f4feeb4fc0` | AM-C1 · AM-F3 · AM-S3 | **CONFIRMED** | ADAPT/NOT-READY stands cold; document-grounded audit, no seat fired, no matrix-fork ground; four seams + 7 questions kept open |
| fan BA | `34424e81ac` | AM-C1 · AM-F3 · AM-S3 | **CONFIRMED** | DEFECTS-NAMED (D1–D7) stands cold; cell-ledger audit, no seat fired; 7 defects + 4 questions kept open |
| fan AA | `760092f1eb` (= `2ce77ce5ad` bytes) | AM-C1 · AM-F3 · AM-S3 | **CONFIRMED** | DEFECTS-NAMED (D1/D2) stands cold; four-file ground audit, no seat fired; 2 defects + 3 open items kept open |
| matrix-legs | `9d74420def` | AM-F3 · AM-F2 · AM-B1 · AM-S3 | **ADJUSTED-NEEDS** (AFFECTED-named by AM-F3) | the four run forks' receipts stand; 4 of 8 amended arms unrun; identifier seams + F-16 + remote columns named |
| B1 fire | `f32f5ab716` | AM-B1 · AM-B2 · AM-B3 · AM-S3 | **CONFIRMED** | the fire already ran WITH the content-gate and returned UNKNOWN/VOID-class — exactly the amended gate's prescribed outcome |

---

## 2. THE COLD RE-VERIFICATIONS

### 2.1 Fan lane-CA — `f4feeb4fc0` — **OUTCOME: CONFIRMED**

**Stale-form verdict under re-check.** ADAPT / NOT-READY with named seams: four guarantees scored (G2a base-diversity PARTIALLY EXECUTABLE — wrong measurable `runner/heap` vs pinned model base; G2b blind-panel MOSTLY COMPLETE, NOT LANDED — two skill controls absent; G3 FAIL ON FORM — zero `(Action | Artifact | Done-when)` tables; G4 RULE ONLY, NOT ENFORCEABLE — registry/verifier absent). Evidence classes are explicitly labeled in the artifact's own legend: DOC-GROUNDED / SKILL-GROUNDED / LOCAL-VERIFIED / UNVERIFIABLE-FROM-GROUND; 16 receipt rows R1–R16; 4 extensions O6–O9; 7 wall-clause questions Q-THE-NORTH / Q-R2 / Q-ab471fc80c / Q-model-sha / Q-fold / Q-panel-row / Q-registry.

**Q-A — were the seats probed at fire?** **NO seat was fired in this landing.** CA is a cold audit of the verification-readiness *spec* (`lane-c-verification-readiness-20261121.md`, sha `0df5c57b…`) against four named ground docs and two skills; no seat-response enters any of its four verdicts. Its only live/external claim is R8 (`model sha 415501bd…` = staged pin / live-HF / byte-identical), which the artifact itself marks **UNVERIFIABLE (online) → question, not disputed** (§E R8, §G Q-model-sha) — a question, never a consumed content claim. **Standing vs AM-C1:** the per-fire re-probe and PIN-read-back obligation attaches to *seat-fired evidence*; this verdict rests on no such evidence, so AM-C1 changes nothing in its standing. The clause is not waived for the *next* fan (Act 5) — that fan must still fire on probed pins; it simply does not retroactively alter a document audit. **Note the reinforcement, not a conflict:** AM-C1/G4 requires "≥2 distinct **pinned bases**," which is precisely the correction CA's G2a/O6 asks for (fix the variable from runner/heap to model-base ID) — the amended gate adopts CA's finding; it does not overturn it.

**Q-B — grounding-dependent claims vs the amended fork-set?** **No effect.** AM-F3 governs the *matrix's* substrate-arm forks; CA audits a readiness spec whose ground is PILOT-KIT-PLAN §3-L3/§4-Stage3 · FINAL-LEG ARM 4 · LOSS-LADDER-AUDIT · MASTER-HITL-GIST-AOA — none is a matrix fork, none is in the refused repos-suite or phone-side set. Adding `re-cut-write-gate-surgical` / `r2gate` / `r2cs` / `origin/fix/restore-read-action` to the matrix adds nothing to, and removes nothing from, CA's ground. The study-proper scope rule is therefore **consistent** with CA's verdict; no claim is re-grounded and none is dropped.

**Seams named — NONE reconciled away:** G2a variable mismatch (O6) · G2b two missing skill controls (O9) · G3 zero checklist tables (O8) · G4 empty registry + two unit conflicts (O7) · Q-THE-NORTH · Q-R2 · Q-ab471fc80c (real ancestor, not in named ground) · Q-model-sha (external, unverified) · Q-fold · Q-panel-row · Q-registry · AoA-side CA-D1 false-ancestry · CA-S1 citation · CA-S2 classification seam (two answered questions overclassified as defects) · **version seam:** AoA §4.2 cites CA's landing as `6de5aba311` (earlier 78-line send) while the task names `f4feeb4fc0` (later, superseding 114±44-line send, read here) — the two are not ancestor/descendant; the later send governs this re-verification, the divergence is flagged, not smoothed.

**Outcome: CONFIRMED.** The ADAPT/NOT-READY verdict stands cold under all four amended gates; every seam above remains an open QUESTION with its receipt.

### 2.2 Fan lane-BA — `34424e81ac` — **OUTCOME: CONFIRMED**

**Stale-form verdict under re-check.** DEFECTS-NAMED, seven revertible defects: D1 false egress-byte equality (`egress_bytes 647,716,330` ≠ `model_bytes 641,262,336`, delta **6,453,994**) · D2 fail-safe grid names undefined G9–G15 · D3 mis-anchored `PILOT-VERDICT §2` · D4 kit-folder misnomer · D5 card-1 state · D6 named-commit phrase · D7 five-field conflation; 5 extensions EXT-1–EXT-5; 4 wall-clause QUESTIONS Q1–Q4. All 8 gates' cell numbers re-derived exactly; R1–R10 real.

**Q-A — were the seats probed at fire?** **NO seat was fired in this landing.** BA is a cold re-derivation of the canary phase-1 design against `CANARY-CELLS-20261120.json` (sha `25606ba9…`; both copies byte-identical) and four named ground docs. The `meituan/longcat-2.5:free`@p0tat0 line in its header is the *audit lane's identity*, not a probe receipt — no seat answer, number, or evaluator row from a live window enters D1–D7. **Standing vs AM-C1:** unchanged — AM-C1 probes seat-fired evidence; this verdict rests on cell-ledger bytes, and its "UNVERIFIABLE list" (§5: run-time sandbox envelope, run-time egress receipt, rung-2 cell, live PR #1 status) is explicitly deferred to the owning host, never asserted as verified here. That is the correct AM-C1/C2 epistemic posture, not a liveness violation.

**Q-B — grounding-dependent claims vs the amended fork-set?** **No effect.** BA's ground is the cells ledger + OPUS-NM3-CANARY + PILOT-VERDICT + FINAL-LEG ARM 3/6 + KIT-METHOD-CARDS — a canary cell ledger, not a matrix fork. The amended study-proper fork-set neither adds a fork this verdict leans on nor excludes a ground it used; the refused repos-suite and phone-side tooling are already absent from BA's ground. Consistent, no re-grounding.

**Seams named — NONE reconciled away:** D1–D7 (each with receipt + revertible fix) · Q1 sandbox envelope is a post-run annotation (04:45:00Z > 04:41:43Z) · Q2 rung-2 has no cell ground · Q3 dispatch-path `audit/PILOT-VERDICT` does not exist · Q4 cadence grounded in CROSSAUDIT not FINAL-LEG · the AoA-side BA-D1 revert-grid mis-trace · SW-1 phantom reported sha (`16130475d2`, does not resolve) · **version seam:** AoA §4.2 cites BA's landing as `2cc6f1832f` (earlier 134-line send) while the task names `34424e81ac` (later, superseding 145±107-line send, read here); not ancestor/descendant — later send governs, divergence flagged.

**Outcome: CONFIRMED.** The DEFECTS-NAMED verdict stands cold; all seven defects and four questions remain open with receipts.

### 2.3 Fan lane-AA — `760092f1eb` — **OUTCOME: CONFIRMED**

**Stale-form verdict under re-check.** DEFECTS-NAMED with extensions: D1 G1/I2 false equality (cells `pinned_repo_sha fc8b9934…` ≠ `model_safetensors_sha256 5747a90e…`) · D2 ungrounded `verdict` field (`RUNG-1-LANDED` absent from ground); G8/G9 partials honestly kept as OP-1/OP-2; 4 extensions EX-1–EX-4; 3 open items OP-1/OP-2/OP-3. The AoA calls AA "the cleanest of the three."

**Q-A — were the seats probed at fire?** **NO seat was fired in this landing.** AA is a cold audit of the lane-A minimal-demonstrable artifact against the brief's four-file ground (CANARY-CELLS ledger · PILOT-VERDICT · LOSS-LADDER-AOA · PILOT-KIT-PLAN §1/§2). The `stepfun/step-3.7-flash:free`@c0wb0y line is the lane identity; no live seat response feeds D1/D2. **Standing vs AM-C1:** unchanged — no seat-fired evidence in the verdict; the `stepfun-freeze` liveness class that AM-C1 names is a *future-dispatch* concern for any re-fire of this lane, not a defect in a document audit. Nothing inherited, nothing to re-probe retroactively.

**Q-B — grounding-dependent claims vs the amended fork-set?** **No effect.** AA's ground is the canary ledger + pilot verdict + loss-ladder AoA + pilot-kit plan; D1's two hashes are ledger keys, D2's verdict field is a document-vs-ground mismatch. No matrix fork is in the ground; the amended fork-set's additions/refusals are orthogonal to both. Consistent, no claim re-grounded.

**Seams named — NONE reconciled away:** D1 false equality (EX-1) · D2 ungrounded verdict field (EX-2) · OP-1 G8 compose-check cites `OPUS-NM3-CANARY §5` outside the four-file ground · OP-2 G9 bytes+command absent from AoA (EX-4) · OP-3 equality repair · AoA-side AA-S1 dangling citations · AA-S2 KIT-SYN typo · SW-1 phantom reported sha (`ab660b943b`, does not resolve) · **version seam:** the AoA-cited landing `2ce77ce5ad` and the branch-line landing `760092f1eb` are sibling sends with **identical file bytes** (`git rev-parse <c>:<path>` = `a2e44cd6…` at both; worktree `git hash-object` = `a2e44cd6…`) — the bytes are reconciled by the file, the **identifier divergence is kept as a named seam**, not erased.

**Outcome: CONFIRMED.** The DEFECTS-NAMED verdict stands cold; D1/D2, OP-1–OP-3 and the identifier seam remain named.

### 2.4 Matrix-legs — `9d74420def` — **OUTCOME: ADJUSTED-NEEDS (AFFECTED-named by AM-F3)**

**Stale-form rows under re-check.** pve1 column boarded: R `leg:R-read-restore` @ `pr-141876`/`6609dacba9` = 4/4 PASS on the N10 re-scope (baseline packet 4/4 FAIL, receipted) · P `leg:P-write-gate` @ `pr-139606`/`d1bdb4582c` = S7 present (grep-counts HEAD/pr-139606/pr-141876/a9c65dc4 = `0/2/0/0`, rows `:367`/`:650`) · C `leg:C-chain-docs` @ `a9c65dc4`/`a9c65dc43d` = chain-docs + read present (blob `7d447366…`, 14 `test_` methods) · H negative control @ study HEAD = NOT-RUN-with-reason (no read arm). F-16 gap confirmed at the tree; handoff CLOSED/GATED; remote columns (p0tat0 / c0wb0y / cloud) named ready-to-dispatch, not measured.

**Re-check vs AM-F3 (the load-bearing effect).** The landing ran the **OLD four-hero-fork table** (study HEAD · pr-139606 · pr-141876 · a9c65dc4). AM-F3 re-derives the fork-set as **eight arms**: the four above plus **`re-cut-write-gate-surgical` `9811e52752`** · **`r2gate`/`round2-gate` `268bb09147`** · **`r2cs` `c39d8ce722` / `r2cs-sync` `42198f5e6d`** · **`origin/fix/restore-read-action` `ec649ad9d0`**. All four *run* forks remain inside the amended set, so their four receipts **stand** (tree bytes do not change under a scope amendment). But as a **landing against the amended gate**, the grid covers **4 of 8 arms** — the four equivalent/sync arms named in AM-F3 have no leg row anywhere in `MATRIX-LEGRUNS`. The verdict is therefore **ADJUSTED-NEEDS**: the receipts are not void, but the landing cannot be entered as "the amended matrix" until those four arms' legs are dispatched (study-proper only; phone-side and repos-suite still named-and-refused; wire refs still watch refs, not legs).

**Re-check vs AM-B1's content-gate (scoped, not applied).** The pve1 legs are deterministic local **tree greps and test executions**, not seat-firing legs; no HTTP-200-with-null-content seat response exists in any cell, so the void-class content-gate is **not triggered** here (AM-F2's "seat-firing leg" condition is not met). This is an honest scoping statement, not a waiver: any *future* arm that fires a seat must carry AM-F2's content-gate row or a NOT-RUN-with-reason. Void-class remains a B1/battery concern (§2.5), not a matrix-leg defect.

**Re-check vs AM-S3 (version check).** Two identifier seams are named and kept: (a) the plan's `pr-141876` label `6609dac951` resolves to no object; the leg used `6609dacba9…` (tree-resolved, no fetch); AM-F3 **retains both values as a seam** — this re-verification does likewise. (b) The study ref is cited as `f652b71b4e` (plan pin), `f32f5ab716` (leg's current HEAD), and `9d56caa557` (AM-F3's revision-time ref) — three values, all receipted, none silently assumed.

**Seams named — NONE reconciled away:** F-16 full combination untested on any single fork · the four unrun amended arms (surgical write-gate / r2gate / r2cs+r2cs-sync / origin restore-arm) · remote-runner columns unmeasured (cross-runner determinism UNKNOWN) · identifier seams `6609dac951` vs `6609dacba9` and the three study-ref values · chmod-000 branch unexercised under root · two non-fatal import stderr tracebacks (environment noise, no install) · the write-gate arm's broken read arm (F-15) · handoff CLOSED/GATED.

**Outcome: ADJUSTED-NEEDS** — with the four unrun arms and every seam above AFFECTED-named and retained; no receipt is voided, no gap smoothed.

### 2.5 B1 fire — `f32f5ab716` — **OUTCOME: CONFIRMED**

**Stale-form verdict under re-check.** Battery-verdict **UNKNOWN / VOID-class + no valid seat-response set**; harness verdict INCONCLUSIVE (machinery receipt, not the battery verdict). The fire ran **WITH** the content-gate: item 1 = FAIL — 4 real-question dispatch probes (budgets 256, then 128×3) all HTTP 200, `content = null`, `reasoning = completion = max_tokens`, `finish = length`, PIN echo absent (no content in which to echo); item 2 = PRESENT — all 20 seat calls receipted at cell level (`content_head`/`content_sha256`/`reasoning_tokens`/`completion_tokens`/`max_tokens`/bias vector/prompt sha). 4 immutable bars NOT EVALUABLE; degenerate ceiling `0 ≥ 0.85×0` at C=0 named and refused; judge-control 20/20 (`ok=true`, fingerprint `ab9e6b5c868b6c30`); `BIAS_V3` delta log on ids 0–6,8,9 with **id 7 correctly dead**; two-way door byte-identical (3 harness shas baseline=post, GGUF `afa0567d…`, `new_weight_files=[]`, `zero_gradient=true`); verdict disconfirmed ×6; B2 firing-position UNCHANGED/NOT ADVANCED.

**Re-check vs AM-B1's amended form (the direct hit).** AM-B1 re-asserts the void rule as a **catalog class** and cites **three** receipts — fire #4 (14×200, 24/24/null), fire #5 (200+content+16 tokens, PIN-verified), and **B1's own A3-arc fire**. This landing **is** the third cited receipt and it already applied the amended rule in full: real-question probe at a content-bearing budget (256/128 ≫ harness 24) + PIN read-back attempted + per-call content-receipt — item 1 FAIL, item 2 PRESENT ⇒ VOID-CLASS ⇒ UNKNOWN, bars unevaluable, never a settlement. The amended clause does not change the verdict; it **adopts** it. AM-B2's "just raise `max_tokens` is a falsified fix" is this fire's own finding (256 consumed entirely by reasoning, no content — OI-2); AM-B3's "mechanically READY, verdict-readiness UNKNOWN, B2 NOT ADVANCED" is this fire's §7 verbatim. The window-conditional reading (fire #5) is **not** converted to a seat-constant and the void is **not** smoothed into GAP/COVERED — the wall clause holds.

**Seams named — NONE reconciled away:** OI-1 fire #5's content-bearing window not reproduced (QUESTION: rare stochastic state vs question/budget-conditioned) · OI-2 budget fix falsified · OI-3 f3b/content seam (`mean_f3b=1.0` coexists with `content=null`) · OI-4 correctness ungraded at C=0 · OI-5 fleet concordance / settlement NOT closed · the four bars stay NOT EVALUABLE and the degenerate ceiling stays refused · B2 stays NOT ADVANCED · version note: this record's HEAD at write is `34424e81ac…` (the superseded BA line) while its landing commit is `f32f5ab716` — both receipted, neither silently reconciled.

**Outcome: CONFIRMED.** The UNKNOWN/VOID-class verdict is exactly what the amended gate prescribes; the fire is not re-run (no install, no harness change) and every seam remains open with its receipt.

---

## 3. Consistency matrix, identifier cross-check, and the explicit unverifiable list

### 3.1 Cross-landing consistency matrix (asserted → status → basis)

| Claim / number | Status | Basis |
|---|---|---|
| CA ADAPT / NOT-READY, BA DEFECTS-NAMED (D1–D7), AA DEFECTS-NAMED (D1/D2) | **CONSISTENT** | §2.1–§2.3 vs AoA §0 / §2; all three landing files re-read at their task-named commits |
| "42/42 GREEN · 8/8 compose-check · R1 LANDED · cells numbers exact" | **CONSISTENT** | BA §1 / AA §2 / AoA §1.I — byte-level agreement, never converted to an independence claim |
| D1 false equality (`fc8b9934…` pin ≠ `5747a90e…` model; `641,262,336` ≠ `647,716,330`) | **CONSISTENT** | confirmed independently by CA G1/I2, BA D1, AA D1 and the cells ledger |
| B1 `B_minus_A=0.0`, `C_minus_A=0.0`, `B_over_0.85C=true` degenerate, judge-control 20/20 | **CONSISTENT** | B1 §3.3 / §4 / §5 vs AM-B1/B3; re-derived against the doc's own decision rule |
| Matrix grep-counts `0/2/0/0`, R 4/4 PASS, H NOT-RUN | **CONSISTENT** | MATRIX-LEGRUNS §2/§3 vs §6 reproduce commands |
| Reported shas (`ab660b943b` / `16130475d2` / `f4b845f05b`) | **DISCREPANCY (SW-1, class)** | `git rev-parse --verify` → fatal for all three; real landing commits resolve; AoA §3.4 settles them; mechanism kept open |
| Landing commits: task-named `f4feeb4fc0` / `34424e81ac` vs AoA-cited `6de5aba311` / `2cc6f1832f` | **DISCREPANCY (version seam)** | local git resolves both; task-named sends are later and supersede; AA's two sends are byte-identical (`a2e44cd6…`) |
| Matrix fork coverage vs AM-F3's 8 arms | **DISCREPANCY (ADJUSTED-NEEDS)** | 4 of 8 arms have leg rows; four equivalent/sync arms unrun |

### 3.2 Identifier cross-check (same event, different hash across docs → flag, never assume)

1. **SW-1 (class):** three phantom report-shas do not resolve; the AoA itself names the real commits. Verified this pass with local git; the class (report-sha vs landing-sha) is swept across all three lanes.
2. **Version seam CA/BA:** task-named superseding sends (`f4feeb4fc0`, `34424e81ac`, 2026-11-23) vs AoA-cited earlier sibling sends (`6de5aba311`, `2cc6f1832f`); not ancestor/descendant. The re-verification reads the **task-named** bytes; the divergence is flagged.
3. **Version seam AA:** `760092f1eb` (branch line) vs `2ce77ce5ad` (AoA-cited) — same file bytes (`a2e44cd6…`); identifier divergence kept.
4. **Pin seams:** `pr-141876` `6609dac951` (unresolvable label) vs `6609dacba9` (tree-resolved) — both retained per AM-F3/G10; study ref `f652b71b4e` / `f32f5ab716` / `9d56caa557` — three receipted values.
5. **B1 write-HEAD vs landing:** `34424e81ac…` (HEAD at B1 write) vs `f32f5ab716` (B1 landing) — both receipted.

### 3.3 Epistemic scoping (no overclaim)

- No stale-form landing is promoted to an amended-plan PASS or COVERED verdict; each keeps its own vocabulary (ADAPT / DEFECTS-NAMED / UNKNOWN / ADJUSTED-NEEDS).
- The fan's document audits are **not** recast as seat-independent verification: the AoA's shared-route constraint (three audits rode one pinned base at the earlier fan) stays named; AM-C1/G4's per-fire diversity remains an open requirement for any re-fire.
- AM-F3's scope expansion is a **coverage** finding, not a claim that the four run legs are wrong.
- The B1 fire was **re-read**, not re-fired; no harness, budget, GGUF, or install was touched.

### 3.4 Explicit unverifiable-from-this-pass list (the file wins on the owning host)

- The run-time sandbox envelope and egress receipt (BA §5 / EXT-2/EXT-4) — only pve1's on-disk run state confirms; not asserted verified here.
- Live PR #1 status and the compose host's kit-folder contents (BA §5).
- The phantom-sha mechanism (SW-1): why three lanes reported shas that point at nothing — mechanism question kept open, never guessed.
- R8's live-HF model sha (CA) — external/online, unverified by this LOCAL-only pass; question with receipt.
- The remote matrix columns (p0tat0 / c0wb0y / cloud) and cross-runner determinism — the legs are named ready-to-dispatch, not measured.
- Whether fire #5's content-bearing window is a rare stochastic state (B1 OI-1) — QUESTION with bounded receipts, not a mechanism claim.

---

## 4. THE REVISED-EXECUTION — re-verification verdict and the next act

**Re-verification verdict.** The four stale-form landings are re-verified COLD and none is converted to an amended-plan landing: the **fan's 3/3 are CONFIRMED** (their document-grounded verdicts stand under AM-C1/AM-F3/AM-S3 — no seat fired, no matrix-fork ground, all seams retained), the **B1 fire is CONFIRMED** (UNKNOWN/VOID-class is exactly AM-B1's prescribed outcome), and the **matrix-legs are ADJUSTED-NEEDS** (four receipts stand; AM-F3's other four arms unrun). **No seam was reconciled away** (§2/§3 enumerate them).

**Next act per the revised order.** Act 1 (this file) closes the RE-GROUND/RE-VERIFICATION gate; the next act is **Act 2 — PER-FIRE SEAT LIVENESS PROBE (AM-C1/AM-C2/AM-B2)**, then **Act 3 — RUNNER/REGISTRY VERIFICATION (AM-F1)**, which are the prerequisites for **Act 4 — BATTERY FIRES IN AMENDED ORDER** and **Act 5 — CROSS-AUDIT FAN + LANDING GATES**. The re-fire fan of Act 5 must carry a fresh real-question probe + PIN read-back + per-call content-receipt at each seat (AM-C1/C2/C3, G1–G5); it cannot reuse these stale-form fan landings as its evidence. This file **authorizes no execution** — every act above remains gated on proxy approval and the owner-beat law (G8).

**The gather's inputs' readiness — AoA settle-conditions (AoA §3 / §4.2), read against this re-verification.** The AoA's required-sources checklist carries G1–G4, G8–G17 as PASS; **G5 (fleet-matrix plan), G6 (batteries plan), G7 (record-mine), G18 (battery receipts) remain UNKNOWN/UNDEFINED** and are **not** converted to PASS. This re-verification does not change that: it re-read the four plans and the landings (AoA §4.2 G5/G6 were unread *at AoA time*; they are now on the record via the REVISED plan's §0/§2), but the AoA's eight settle-conditions are **still open** — (1) FORM A1/A2 · (2) DESIGN BA-D1/S1/S3/S5/S6 · (3) LAYER CA-D1/S1/S2 · (4) AUDIT RECEIPTS SW-1 · (5) INDEPENDENCE G2 · (6) READINESS G3 · (7) STEWARDSHIP G4 · (8) MANIFEST A3. Per the AoA's own law, "until 1–4 close, the stack verdict stays ADAPT," and settle-condition 5 is the one that makes the verification claim true. **Therefore the gather's inputs are NOT acceptance-ready**: the stack verdict stays **DEFECTS-NAMED / ADAPT**, the handoff stays **CLOSED / GATED**, the AoA/CONVERGE (Act 6) and MATRIX-LEGS+GATHER (Act 7) do not open, and no battery UNKNOWN is promoted to PASS. The real landing shas (CA `f4feeb4fc0` · BA `34424e81ac` · AA `760092f1eb`/`2ce77ce5ad`) are carried as receipts with the phantom-sha question kept open; the identifier seams of §3.2 are fed to the AoA, none smoothed.

---

## 5. Compose-check (marks, FIRED/ABSENT, one evidence line each)

| # | Mark | State | Evidence |
|---|---|---|---|
| 1 | four amended gates read in full | FIRED | §0.2 — AM-C1/AM-F3/AM-B1/AM-S3 from `REVISED-STAGE-PLAN-20261123.md` (read in full) |
| 2 | fan 3/3 re-verified cold (Q-A/Q-B answered each) | FIRED | §2.1–§2.3 — CA/BA/AA at task-named commits; no seat fired, no fork-set ground, seams kept |
| 3 | matrix-legs re-verified vs AM-F3 + AM-B1 | FIRED | §2.4 — 4/8 arms, ADJUSTED-NEEDS, scoping of content-gate, identifier seams |
| 4 | B1 fire re-verified vs AM-B1's amended form | FIRED | §2.5 — UNKNOWN/VOID-class CONFIRMED, no re-fire |
| 5 | armament line loaded + rest named-and-refused | FIRED | header — think-tank + agent-work-review only |
| 6 | version check + identifier cross-check; seams named, none reconciled | FIRED | §3.1–§3.2 — SW-1 class, version seams, pin seams, all retained |
| 7 | next act + gather readiness per AoA settle-conditions | FIRED | §4 — Act 2 next; G5–G7/G18 UNKNOWN; verdict ADAPT; handoff CLOSED/GATED |
| 8 | hard lines + emission contract | FIRED | header + §6; disk-first, commit only this path, never push, RFC quiet |

---

## 6. Limitations, hard lines, and emission contract

- **Limitations:** this is a COLD re-read of receipts, not a re-fire; no seat was probed, no battery re-run, no harness touched. The identifier seams (SW-1 class, version seams, pin seams) are flagged with local git but their *mechanisms* are kept as questions (the file wins on the owning host). Where the AoA and the task name different landing commits, this file reads the **task-named** bytes and records the divergence — it does not decide which lineage is canonical beyond the version check.
- **Reproducibility (all local, no install):** `git rev-parse --verify <sha>` on every commit in §0.1/§3.2; `git show --stat <sha> -- <path>` for the superseding-send relation; `git rev-parse <sha>:<path>` / `git hash-object <path>` for the AA byte identity; `git merge-base --is-ancestor` for the sibling (non-ancestor) relation. All study paths via `read_file`, never `web_extract`. Working-tree changes present at commit time (the D/M/?? rows in `git status`) are left **AS FOUND** — this commit stages only this deliverable's path.
- **Emission contract (binding):** this file was written on disk FIRST with all five re-verifications inside, then staged and committed as `kanban-pilot <pilot@rig.local>` with **only this path**, on the current HEAD re-checked at commit, never pushed; master append-only; the plan, sealed artifacts, crons, anchors and sibling plates left AS FOUND; local config left AS FOUND (identity overridden per-commit because `user.name`/`user.email` are `|| true`). A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.

*Facimus semper — the re-verification renders on the receipts; the receipts are on the record; the record corrects itself out loud. The stale-form landings stand or adjust on the amended gates, and no seam is reconciled away. Nothing public; RFC #143379 / #5320 / #157065 quiet.*
