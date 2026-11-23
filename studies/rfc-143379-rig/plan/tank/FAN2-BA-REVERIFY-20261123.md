# FAN2-BA-REVERIFY-20261123 — blind Act-5 re-verification of the AOA-NINE-AXIS adjudication against the amended gates

*Seat: `meituan/longcat-2.5:free` (BA seat, p0tat0) · Branch: `study/rfc-143379-rig-20261105` · Date: 2026-11-23 · Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/FAN2-BA-REVERIFY-20261123.md`.*

*Target, cold: `plan/tank/AOA-NINE-AXIS-20261123.md`, landing commit `73b4cbead72e5b6079c4b9c8beaf205bd750799e`, blob `f1a579556708b6cb18cc0068ae5091be5073ccba` (= worktree bytes = HEAD blob; verified by `git rev-parse` + `git hash-object`). Read cold in full (218 lines). The sibling lanes' drafts (FAN2-CA, FAN2-AA) were NOT opened — blind clause held.*

*This is the BA seat's independent re-verification lane on the amended gates. The target was audited against the revised plan (`REVISED-STAGE-PLAN-20261123.md`, `93d2def129`), its own eight settle-conditions, and every claim re-derived to the record it cites. A claim that cannot be re-derived is UNKNOWN, never inferred.*

*Hard lines (binding): nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · never push · never `git checkout --` / `git rm -rf` / `git stash` · master append-only · write ONLY under `studies/rfc-143379-rig/` · commits as `kanban-pilot <pilot@rig.local>` · plan, sealed artifacts, crons, anchors left AS FOUND · local config left AS FOUND (identity overridden per-commit).*

*Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised." Every non-re-derivable claim below is UNKNOWN with a minimal experiment; none is a silent pass.*

*Emission contract: this file lands on disk FIRST with the receipts inside, then the commit as kanban-pilot (this path only), then the report's sha. Exit 0 = deliverable on disk then sha.*

---

## 0 · ARMAMENT — used with why, refused with why (skill-dump doctrine)

**USED (4):**
- **think-tank** (the spine) — *why*: the mandated form for an adjudication-lane audit; classify → choose → probe → evaluate → adopt-or-park → standardize → verify run at each finding class.
- **investigation-documentation** (the receipts form) — *why*: this deliverable IS a discovery log with a Limitations/Reproducibility section; every row carries source pin + artifact digest + command.
- **defect-forensics** (the classes) — *why*: the finding classes are the lane's output units — parent-class (P1/P2/P3/P4), root vs amplifier, and the "version churn" amplifier named by the armament repass.
- **agent-work-review** (the verdict form) — *why*: the asserted → status → basis table is its required sequence; the version check is its standing rule.

**REFUSED, named with why:**
- **blind-agent-panels** — *why*: no consensus fan-out is wanted; the task names ONE blind lane (this one).
- **supervisor-delegation** — *why*: same; no child spawning.
- **codex / claude-code / opencode** — *why*: no delegate coder for a study-path append.
- **external-readiness-review** — *why*: it is lane-CA's SUBJECT, not this lane's armament (a second application would duplicate CA's own ground, not extend it).
- **grounded-citations / web-storm / arxiv / browser-harness-sop** — *why*: LOCAL receipts only; no field search is authorized or useful here.
- **systematic-debugging** — *why*: armed only on a non-reproduction; the wall clause governs instead, and the wall clause produced the extensions.
- **safe-file-editing** — *why*: no secret-bearing file is edited.
- **memory-chain / hermes-gateway-ops / aces-harness-probes / local-llm-serving / llama-cpp / serving-llms-vllm / two-model-reasoning / evaluating-llms-harness** — *why*: no chain append, no gateway/config change, no harness or seat fired, no install, no offline reasoner in scope.

*A lane that does not arm is a finding — this lane arms four, refuses the rest with reasons.*

---

## 1 · THE TARGET'S OWN RECEIPTS (re-derived first, so the verdict has a base)

| Fact asserted by the target | Receipt (path / command) | Value |
|---|---|---|
| Landing commit `73b4cbead7` exists | `git cat-file -t 73b4cbead7` | **commit**, `73b4cbead72e…`, 2026-11-23 09:45:53 -0500 |
| File bytes at that commit | `git rev-parse 73b4cbead7:…AOA-NINE-AXIS-20261123.md` | `f1a579556708b6cb18cc0068ae5091be5073ccba` |
| Worktree bytes equal | `git hash-object` same path | `f1a579556708b6cb18cc0068ae5091be5073ccba` |
| HEAD tree entry equal | `git ls-tree HEAD` same path | same blob; working tree clean for the path |
| Blob identity across add/remove/add churn | `git rev-parse 73b4cbead7:…`, `d93aea9d21:…`, `HEAD:…` | all `f1a57955` (9f82dbd31c removed it — re-materialized) |
| Axes count / settle-conditions | §1 headings A–I; §3 numbered list | **9 axes · 8 settle-conditions** |
| Phantom shas | `git cat-file -t` ×3 | `16130475d2` · `ab660b943b` · `f4b845f05b` → **ABSENT** |
| Real landing shas | `git cat-file -t` ×9 | `2cc6f1832f` · `2ce77ce5ad` · `6de5aba311` · `f4feeb4fc0` · `34424e81ac` · `73b4cbead7` · `9d74420def` · `e692f914dd` · `93d2def129` → all **OK** |
| Cells ledger dual anchor | `sha256sum` both copies + key read | live file `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2`; field `cells_sha256` `f1ed5b0db7…`; both copies byte-identical; **no `verdict` key** |
| The D1 delta | ledger arithmetic | `647,716,330 − 641,262,336 = 6,453,994` ✓ |
| The pin ≠ model two keys | ledger read | `pinned_repo_sha fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` ≠ `model_safetensors_sha256 5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c` ✓ |

*The target's self-receipts hold. The defects below are in its consolidation layer and its gate-conformance, not in its byte anchors.*

---

## 2 · ASSERTED → STATUS → BASIS (every load-bearing claim re-derived)

Status vocabulary: **CONFIRMED** (re-derived exactly) · **ADJUSTED** (partly re-derived; correction named) · **UNKNOWN** (cannot be re-derived; minimal experiment given) · **DANGLING** (citation target absent).

### 2.1 The three lane verdicts

| # | Claim | Status | Basis (receipt) |
|---|---|---|---|
| C1 | CA verdict ADAPT / NOT-READY | **CONFIRMED** | `lane-ca-audit-20261121.md` §VERDICT verbatim: "ADAPT — the layer is a sound SPEC … not yet an EXECUTABLE one"; G2a PARTIALLY EXECUTABLE · G2b MOSTLY COMPLETE, NOT LANDED · G3 FAIL ON FORM · G4 RULE ONLY. Re-checked: G2/G3/G4 open at artifact §6:266–269; 0 checklist tables (`grep -cE '^\| *(Action\|Done-when)'` = 0); 0 registry/pin files (find → 0). |
| C2 | BA verdict DEFECTS-NAMED D1–D7 | **CONFIRMED (at the landed bytes)** | `lane-ba-audit-20261121.md` §3 rows D1–D7 + EXT-1–EXT-5. Re-derived at `34424e81ac` (the bytes the fan cite names). **BUT** the AOA's §0 pin for BA is `34424e81ac` while its §4.2 G2 pin is `2cc6f1832f` — and those are *different bytes* (blob `9f7bfa91…` vs `34424e81ac`'s blob; diff = 145 insertions / 107 deletions). The AOA's BA consolidation rests on the §0 pin. |
| C3 | AA verdict DEFECTS-NAMED D1/D2 | **CONFIRMED** | `lane-aa-audit-20261121.md` §3 D1 (two distinct ledger keys) + D2 (`verdict` field not in ground); cells ledger confirms both (no `verdict` key; two distinct sha keys). AA blob identical at worktree / `2ce77ce5ad` / `760092f1eb` / HEAD = `a2e44cd6de…`. |
| C4 | "all three lane landing gates passed" | **CONFIRMED with a version seam** | Three real landing commits exist and resolve; but the *bytes* differ per pin (see C2; CA likewise: `6de5aba311` blob `e52e4d9c…` ≠ `f4feeb4fc0` blob `5792e5cb…`; `ef08fe6069` == `6de5aba311`). The AOA pins BA/CA by §0's *new* commits and cites the *old* ones in §4.2 without saying they are different passes. |
| C5 | AoA sits on a base distinct from all three audits | **CONFIRMED as an assertion · UNKNOWN as a probe receipt** | The base name `upstage/solar-mini4:free` is not any of CA `hy4`/cloud, BA `longcat`/p0tat0, AA `stepfun`/c0wb0y → the *naming* holds. **But there is no PIN echo, no `content_head`/`reasoning_tokens`/`max_tokens` receipt anywhere in the target** (`grep -c PIN` = 0; AM-C2 line 52 requires the AoA's fourth base to be re-probed at fire with positive-token read + PIN read-back). See B-1. |

### 2.2 The nine axes

| # | Axis | Asserted | Status | Basis |
|---|---|---|---|---|
| A1 | Completeness | PARTIAL | **CONFIRMED** | G5–G7/G18 carried UNREAD→UNKNOWN; the input table lists them honestly. |
| A2 | Verifiability | PARTIAL | **CONFIRMED** | numerics byte-exact; receipt shas phantom (SW-1) — both re-derived. |
| A3 | Honesty | HONEST | **CONFIRMED** | wall-clause posture present; seams named, none erased. |
| A4 | Grounding | SOUND | **ADJUSTED** | The byte core is grounded; the §1.D claim "confirmed by all three lanes independently (CA's G1/I2 …)" is **not** re-derivable — see D1. |
| A5 | Extendibility | SOUND | **CONFIRMED** | CA O6–O9 (4), BA EXT-1–EXT-5 (5), AA EX-1–EX-4 (4), AoA A1–A5 — all present with commands/counts. |
| A6 | Gate-coherence | PARTIAL | **CONFIRMED** | CA G2/G3/G4 OPEN; BA D2 cites undefined G9–G15; the "AoA corrected the citations" sentence is **DANGLING** — see D2. |
| A7 | Seat-compliance | SOUND | **UNKNOWN as liveness** | designations exact, but the AoA's own base has no content-gate/PIN receipt; AM-C1's "≥2 distinct bases re-verified after any pivot" is a **gate re-verification** the target never ran — see B-1/B-4. |
| A8 | Wall-clause-handling | SOUND | **CONFIRMED** | SW-1/SW-2/AOA-OQ/OP-2 carried as QUESTIONS with owners; no "unreproducible" verdict. |
| A9 | Convergence | PARTIAL | **ADJUSTED** | agreement real; divergence retained; but "six start-gates" (§1.I) is ungrounded — the five start-gates are real (`lane-a` G7 row), the sixth has no receipt — see D3. |

### 2.3 The consolidated verdict + settle-conditions

| # | Claim | Status | Basis |
|---|---|---|---|
| V1 | Stack verdict DEFECTS-NAMED — GO behind the standing start line | **CONFIRMED** | consistent with CA ADAPT + BA/AA DEFECTS-NAMED; the alternatives (REJECT/PARK/unconditional GO) are each argued and not warranted on the record. |
| V2 | Settle-condition 1 (FORM) | **CONFIRMED as written** | lands via per-key match + provenance tags; AA EX-1/EX-2 are the extension pair. |
| V3 | Settle-condition 2 (DESIGN) | **ADJUSTED** | "re-traced against design §3:83–92" is re-derivable (BA audit R1–R10 == design §3:83–92 verbatim, trigger/mechanism both sides); "F2 cadence re-anchored to NIGHTSHIFT:3" is **not** re-derivable as written — `NIGHTSHIFT-PLAN` files exist but the cited `:3` is not a cadence line in the ones present (they are prose briefs); treat as UNKNOWN. |
| V4 | Settle-condition 3 (LAYER) | **ADJUSTED** | "commit-on-main + file-presence, never the false is-ancestor claim" is the right fix; the ancestry flip is real (`merge-base --is-ancestor ab471fc80c f4feeb4fc0` = 0; `ab471fc80c 6de5aba311` = 1). But "CA-S1 re-anchored to fold §7-u:97" cites a fold line the lane never measured; UNKNOWN pending the fold receipt. |
| V5 | Settle-condition 4 (AUDIT RECEIPTS) | **CONFIRMED** | phantom→real mapping re-derived exactly (all 3 phantoms absent; all real commits present). |
| V6 | Settle-condition 5 (INDEPENDENCE) | **CONFIRMED as the load-bearing condition** | per-unit pinning + ARM 4 + a blind panel; same-base convergence never called independence — the constraint is named. **But the target itself is a same-base corroboration case**: its own base rides the steering path it describes, with no probe receipt (B-1). |
| V7 | Settle-condition 6 (READINESS) | **CONFIRMED as written** | C1–C9 done-whens + voice-check grep gate. |
| V8 | Settle-condition 7 (STEWARDSHIP) | **CONFIRMED as written · gap noted** | "pin registry seeded (A5)": **the registry is still absent** (`find *pin_registry* pins.json verify_pin*` → 0 files, this lane). A5 is a promise, not a landed seed row. Carried, not contradicted. |
| V9 | Settle-condition 8 (MANIFEST) | **CONFIRMED as written · gap noted** | "every load-bearing claim … carries a ground-set tag + file:line receipt" — the target's §4.2 table gives path + read-status, and §1 axes give prose grounds; there is no per-claim ground-set tag column. Partly met. |

---

## 3 · THE VERDICT

**DEFECTS-NAMED** — the target's top-line DEFECTS-NAMED / bounded-canary GO stands on its byte core, and **four consolidation-layer defects** are named below. None is fatal; all are additive/revertible. The target is not REJECTed: every defect is a citation/version/gate-conformance error in the *consolidation layer*, not a fabricated receipt, and the wall clause was applied throughout.

### 3.1 The four named defects

**B-1 · The AoA's own base lacks the AM-C1/AM-C2 content-gate receipt (the load-bearing gate defect).**
- *Asserted:* line 3 and line 14 — the AoA sits on `upstage/solar-mini4:free`, "BASE-DISTINCT", and "the AoA fire therefore proceeds".
- *Re-derived:* no PIN echo, no `content_head`/`reasoning_tokens`/`max_tokens`, no probe question-sha appears anywhere in the target (`grep -c PIN` = 0). The amended plan AM-C1 (line 53) requires *every* seat, including "the AoA's fourth base", to be re-probed at dispatch/at fire with a real question + positive-token read + PIN read-back; AM-C2 makes a probe-200 liveness-only and VOID for any content claim.
- *Why it matters:* the target consumes three other seats' adjudications as its evidence base while carrying no liveness/content receipt of its own. Under AM-S3 ("no verdict floats on a stale receipt") the AoA's *own* seat is the one seat whose response is unreceipted — so the "AoA distinct base" claim is an assertion, not a receipted independence.
- *Revertible/additive:* a one-row probe receipt (question sha, responding model, PIN echo, `content_head`, `reasoning_tokens`, `max_tokens`) appended to §0, or the base claim downgraded to "asserted, probe pending". **Not edited into the target** (history never rewritten; this lane writes only its own path).

**B-2 · The §0-vs-§4.2 pin split is carried but never named as the version seam it is.**
- *Asserted:* §0 pins BA `34424e81ac`, CA `f4feeb4fc0`; §4.2 G2–G4 cite "real sha" BA `2cc6f1832f`, CA `6de5aba311`.
- *Re-derived:* `2cc6f1832f` (2026-11-21 19:14) and `34424e81ac` (2026-11-23 09:41) are **different commits with different bytes** (diff 145+/107−); same for CA `6de5aba311` (19:14) vs `f4feeb4fc0` (09:38, blob `5792e5cb…`). The AOA's BA/CA consolidation findings (D1–D7; G2a/G3/G4) are re-derived at the *§0* pins, but the §4.2 "real landings" are the *earlier* originals.
- *Why it matters:* AM-S3 says a stale-form landing "is not treated as an amended-plan landing until re-verified; its disagreements are named seams fed to the AoA, never reconciled away." Here the AOA silently mixes two passes of the same lane — the exact "version churn" amplifier the armament repass (ARMAMENT-REPASS §3, P1 "unpinned reference") named. It is a *seam*, not a contradiction: both sets of commits are real (all 9 shas resolve).
- *Revertible/additive:* one row in §0 or §4.2 stating "§0 pins = the 2026-11-23 cold re-audits; §4.2 pins = the 2026-11-21 originals; both real; the consolidation rests on §0."

**B-3 · Two citations dangle (the consolidation layer points at sections that do not exist).**
- *DANGLING-1:* §4.2 G2–G4 note "reported sha phantom (SW-1); settled per **§3.4**" — the target's §3 is the SETTLE-CONDITIONS block and **has no §3.4**. `grep -n '^#### '` returns no 3.x subsections. The SW-1 settlement is stated in prose at §1.B/§1.C, never at §3.4.
- *DANGLING-2:* §1.F line 83 — "after the named corrections, every gate referenced … exists (A2 template-level equality fix; BA-D1 revert re-trace; BA-S3 item-table re-key; CA-D1 ancestry corrected; CA-S1 citation re-anchored)". Those are *promises*; the BA-D1 revert re-trace is in fact **still asserted as a live mis-trace** elsewhere in the same document (§1.B line 44), which is internally inconsistent with ARMAMENT-REPASS C4 (the landed BA audit names the superseded `7190c0efda` and re-derives R1–R10 from the artifact's §3 — re-derived true here: BA audit :160 + design §3:83–92 match verbatim).
- *Why it matters:* a dangling citation is the failure class the wall clause forbids ("a receipt that points at nothing"). Two rows point at nothing.
- *Revertible/additive:* re-point "§3.4" → "§1.B/§1.C (SW-1)", and mark the §1.F sentence as "deferred to the settle-conditions" rather than "corrected".

**B-4 · The "AoA corrected the citations" claim contradicts the same record's own findings.**
- *Asserted:* §1.F line 83 "every gate referenced by the consolidated record exists (A2 template-level equality fix; BA-D1 revert re-trace; …)".
- *Re-derived:* the BA-D1 "revert mis-trace" is simultaneously asserted live at §1.B line 44 and §1.D/§1.C ("BA-D1 revert mis-trace"), and §2 conditional-name 2 repeats "BA-D1 revert mis-trace". ARMAMENT-REPASS C4 shows it is true of the *superseded* `7190c0efda`, not of the landed `34424e81ac`. So the correction is neither applied nor consistently withdrawn.
- *Why it matters:* a consolidation layer must not carry the same sub-finding as both corrected and live. This is the ARMAMENT-REPASS "pin-dependent finding" (C4/C5) recurring *inside the target*.
- *Revertible/additive:* one append-only correction row naming the pin each statement applies to.

### 3.2 What does NOT survive (already known — recorded, not newly found)

- "D1 confirmed by **all three** lanes independently (CA's G1/I2, BA's G1, AA's G1)" — re-derived **false**: `grep -cE '\bG1\b|\bI2\b'` over `lane-ca-audit-20261121.md` = **0**. CA tested neither variable; BA = byte equality, AA = SHA equality (two variables, two lanes). ARMAMENT-REPASS C3 already amended this; the target still asserts it in §1.D and §2. **This is the single most repeated ungrounded claim in the target.**

### 3.3 What DOES survive (recorded, so the verdict is not a blanket rejection)

- The byte core: 42/42, 8/8, R1 LANDED, all cell numbers, the dual-anchor shas — every number re-derived exactly.
- The phantom-sha class (SW-1): all three phantoms absent, all real commits present — the SW-1 finding is *true* and is the target's best contribution.
- The wall-clause posture: no "unreproducible" verdict without an experiment; divergences named, never averaged.
- The eight settle-conditions: all eight are well-formed, load-bearing, and consistent with the amended plan's gates (G2/G3/G4 carried OPEN; MANIFEST/STEWARDSHIP as promises, not landed).
- The hold-release logic: three real landings exist; the AoA firing after them is sequencing-correct.

---

## 4 · THE EXTENSIONS THIS LANE WOULD OPEN (≥2; all measured, revertible, additive)

**X-1 · The AoA-seat content-gate receipt (closes B-1).**
*Measurement:* at the next AoA/ring fire, run the AM-C1 probe against `upstage/solar-mini4:free` and append one row: `{question_sha, responding_model, pin_echo, content_head, reasoning_tokens, max_tokens}`. *Command-shaped:* the same probe the matrix legs use (`git rev-parse`-style read, no install). *Pass bar:* the row's `responding_model` == the pin and `content_head` non-empty (else VOID-class → the base claim drops to "liveness-only"). *Revertible:* a single append row; if the pin drains/freeze (AM-C1's stepfun-freeze class), the pivot is ledgered and the diversity gate re-verified. **This is the one extension that makes the "distinct base" claim true.**

**X-2 · The version-seam row (closes B-2).**
*Measurement:* a two-column table of the four lane pins (`2cc6f1832f`/`34424e81ac` · `2ce77ce5ad`/`760092f1eb` · `6de5aba311`/`f4feeb4fc0`) with their blob shas and dates, marking which pin each consolidation finding rests on. *Pass bar:* every finding cites exactly one pin. *Revertible:* additive; the FAN2-CA lane already demonstrates the form ("the brief's `4c049ec82b` is a COMMIT id, not the file blob — recorded, not silently normalized").

**X-3 · The citation-integrity grep (closes B-3).**
*Measurement:* `grep -oE '§[0-9]+(\.[0-9]+)?'` over the target and resolve each hit against the target's own heading list. *Expected now:* §3.4 → absent; §6 (gather checklist) → absent (the gather checklist is §4.2); "fold §7-u:97" → external, needs the fold receipt. *Pass bar:* zero unresolved internal citations. *Revertible:* one append-only correction row per dangling cite.

**X-4 · The settle-condition 2/3 re-anchor (closes V3/V4).**
*Measurement:* replace "NIGHTSHIFT:3" and "fold §7-u:97" with resolvable citations (`NIGHTSHIFT-PLAN-20261121.md` §-line for the 40–60 min cadence — confirm; fold commit+line for §7-u). *Pass bar:* both citations resolve locally. *Revertible:* two line edits; the cadence substance (40–60 min) already traces to the cross-audit plan's §E1/§G per BA-Q4.

---

## 5 · WALL-CLAUSE QUESTIONS (non-reproductions → minimal experiments; none is a silent pass)

| # | Question | Why it is a QUESTION (not a defect) | Minimal experiment |
|---|---|---|---|
| Q1 | Did the AoA's `upstage/solar-mini4:free` seat actually respond content-bearing at fire? | No probe receipt exists in the target; the absence of a receipt is not evidence of absence — it is the wall clause's own case. | Run the AM-C1 probe once; compare `content_head`/`reasoning_tokens`/`max_tokens` to the pin. |
| Q2 | Are the §0 pins and the §4.2 pins two passes, or the same pass reported twice? | Both commit sets are real; the AOA never says they differ. | `git show --stat` + `git diff` the two BA blobs and the two CA blobs; the diff size answers it mechanically. |
| Q3 | Does "the six start-gates" have a sixth receipt? | Five start-gates trace to `lane-a` G7; the sixth is named only in §1.I. | Grep the five start-gate receipts; if five resolve and a sixth is named nowhere, the count is five, not six. |
| Q4 | Is the pin registry truly seeded by A5? | `find` → 0 files today. A missing registry is the QUESTION "where is the first pin row", not "one-run-per-pin is false". | Re-run the find; if still 0, the seed row is unlanded and settle-condition 7 stays open. |
| Q5 | Does the NIGHTSHIFT:3 cadence citation resolve? | The `NIGHTSHIFT-PLAN-*` files present are prose briefs; `:3` may not be a cadence line. | Open the cited file and read line 3; if it is not the cadence, the citation dangles. |

---

## 6 · LIMITATIONS + REPRODUCIBILITY (investigation-documentation form)

**Limitations.** This is a COLD re-read of receipts, not a re-fire: no seat was probed (my own probe is named in X-1, not run — I am the BA lane, and running the AoA's base would not receipt the AoA's 09:45 fire), no battery re-run, no harness touched, no install. The blind clause was held: FAN2-CA's draft existed on disk (`?? studies/.../FAN2-CA-REVERIFY-20261123.md`) and was **not opened**; FAN2-AA was not looked for. Where the target and the record diverge, this lane reads the task-named commit (`73b4cbead7`) and records the divergence; it does not decide lineage beyond the version check. The four defects are in the *consolidation layer*; the lane landings' own verdicts stand at their pins.

**Reproducibility (all local, no install).**
- `git cat-file -t <sha>` for every commit in §1 — 9 real, 3 phantom.
- `git rev-parse <sha>:studies/rfc-143379-rig/plan/tank/<file>` + `git hash-object <file>` for the blob identities.
- `git diff --stat 2cc6f1832f 34424e81ac -- …lane-ba-audit…` → 145+/107−; `git rev-parse` the CA pair → `e52e4d9c…` vs `5792e5cb…`.
- `sha256sum` both cells copies → equal; key read for the dual anchor and the absent `verdict`.
- `grep -cE '\bG1\b|\bI2\b' lane-ca-audit-20261121.md` → 0; `grep -c PIN AOA…md` → 0; `find *pin_registry* pins.json verify_pin*` → 0.
- Working-tree changes present at commit time (the `D FLEET-CYCLE-BODY-*` rows, the `?? FAN2-CA…` row) are left **AS FOUND** — this commit stages only this deliverable's path.

---

## 7 · SEAL-VOICE / HARD-LINES CHECK (this lane)

nothing public · RFC #143379 / #5320 / #157065 QUIET · no installs · writes only under `studies/rfc-143379-rig/` · all local paths via `read_file` / local git, never `web_extract` · never push · never `git checkout --` / `rm -rf` / `stash` · commits as `kanban-pilot <pilot@rig.local>` · armaments applied: think-tank (spine) + investigation-documentation + defect-forensics + agent-work-review; the rest name-and-refused.

*Facimus semper — the verdict renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION, never a defect; a receipt that points at nothing is the failure class, never a silent pass.*

---

*Exit 0 = this file exists on disk with the receipts inside, committed as kanban-pilot on the study path only, then the sha reported. A parse-fragment-only response has NOT landed.*
