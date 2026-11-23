# ARMAMENT-REPASS — the three un-grounded landings re-derived through the armament (2026-11-23)

**Author:** kanban-pilot <pilot@rig.local>
**Branch:** `study/rfc-143379-rig-20261105` · HEAD at pass start: `cfed8b30f9dc9c23b12587282419c6b96d51ecfa`
**Deliverable:** this file — `plan/tank/ARMAMENT-REPASS-20261123.md` (new file; no prior version rewritten).
**Landings under re-derivation:** `lane-ba-audit-20261121.md` (BA) · `lane-ca-audit-20261121.md` (CA) · `AOA-NINE-AXIS-20261123.md` (AoA).
**AoA's inputs traced:** BA · AA (`lane-aa-audit-20261121.md`) · CA landings · `STAGE-PLAN-SEQUENCE-20261123.md` §1–§8 · `briefs/CROSS-AUDIT-BRIEFS.md` · `briefs/AOA-BRIEF-20261121.md` · cells ledger (both copies) · `plan/RECORD-MINE-20261121.md` · `STAGE-PLAN-FLEETMATRIX-20261123.md` · `STAGE-PLAN-BATTERIES-20261123.md`.
**ARMAMENT (binding, loaded this pass):** think-tank (the mechanism spine) + agent-work-review + investigation-documentation + defect-forensics (operator addition, 2026-11-23). **Name-and-refused:** every other skill; `blind-agent-panels` and `external-readiness review` are the *subject* of lane-CA's probes, not this lane's armament; no force-fit.
**WALL CLAUSE (verbatim, binding):** a non-reproduction is a QUESTION with receipts, never a stop.
**Hard lines:** nothing public · RFC #143379 / #5320 / #157065 QUIET · no installs · write only under the study · never push · never `git checkout --` / `rm -rf` / stash · commit as `kanban-pilot <pilot@rig.local>` in `/root/workspace/repos/hermes-agent`, **this file only** · all local paths via `read_file`, no `web_extract`.
**Emission contract:** file on disk FIRST with the re-derivations inside; the sha is reported only after the commit lands.

---

## 0 · WHY THIS PASS EXISTS — the armament-gap traced (forensic step 1)

The operator's check found the gap: the BA/CA fan lanes and the AoA were dispatched **without the armament line** — the briefs' texts lacked it, their transcripts show zero spine use. Verified by grep on the record (not asserted from the operator's summary alone):

| Surface | Armament hit | Receipt |
|---|---|---|
| `lane-ba-audit-20261121.md` | **0** spine/armament mentions | `grep -inE 'think-tank\|spine\|agent-work-review\|...'` → only "court-verification spine" as an audited *subject*, not the think-tank spine |
| `lane-ca-audit-20261121.md` | **0** | same grep → empty |
| `AOA-NINE-AXIS-20261123.md` | **CLAIM only** | `:6` "Armament applied: think-tank (the spine) + agent-work-review"; repeated at `:201` — but the transcript carried no skill load and no spine step; the claim is not the application |
| `briefs/CROSS-AUDIT-BRIEFS.md` | **0** | grep → empty |
| `briefs/AOA-BRIEF-20261121.md` | **0** | "spine" at `:30` means *the phase-1 brief as the composition spine*, not the skill |

**The finding, stated plainly:** the three landings' verdicts stood as **DATA** with real receipts, but not as **skill-grounded** verdicts — the discipline that certifies a finding (spine, cross-doc review, discovery-log form, parent-class hunting) had not been executed. The operator's read is **confirmed against the record**; this pass is the re-grounding, not a correction of their assessment (defect-forensics §8, "return the user's own thesis as their read, confirmed — never as your finding").

---

## 1 · THE SPINE RE-DERIVATIONS

Each landing runs the full spine: **classify → choose → probe → evaluate → adopt-or-park → standardize → verify**, with the forensic pass (evidence-trail → byte receipt → parent class), the agent-work-review pass (consistency/accuracy), and the discovery-log form folded into each. Seams are named, never reconciled away.

### 1.1 LANE-BA — `DEFECTS-NAMED` (D1–D7), 2026-11-23 landing `34424e81ac`

- **classify.** *Complicated*, not chaotic: the ground is named and closed (cells ledger + artifact), every gate number re-derives, and the defects are identity/form errors inside a runnable spec. No predictive uncertainty needed; no "establish order first."
- **choose.** Four VOI-maximal probes: (a) cells ledger byte keys, (b) the artifact's §2 gate table, (c) the artifact's §3 R1–R10 revert table, (d) git object store for the cited shas. No other mechanism loaded.
- **probe (executed, read-only).**
  - `sha256sum` both cells copies → `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2`, byte-identical (study `probes/` copy = master-page archive copy). Matches the AoA's dual-anchor claim.
  - Cell keys verbatim: `model_bytes 641262336` · `egress_bytes 647716330` · `egress_secondary_downloads 0` · `load_seconds 0.95` · `param_count 319028736` · `argmax_next_token 49969` · `deterministic_max_abs_diff 0.0` · `determinism_tolerance 1e-06` · field `cells_sha256 = f1ed5b0d…` (pre-addendum anchor).
  - D1 arithmetic re-derived: `647716330 - 641262336 = 6453994` → the audit's **6,453,994-byte delta** is exact; `egress_bytes` is the *release* count, not the model's.
  - Artifact `lane-b-phase1-design-20261121.md` = **214 lines** (matches the audit's header); §2 defines **G1–G8 only** (gate rows at artifact :65–:72); `G9–G15` appear **only** in the F4 fail-safe grid at **:156–:157** → D2 confirmed: the grid names gates the brief never defines.
  - R1–R10: the audit's current landing re-derives all ten **directly from the artifact's own §3 table** (audit §1, rows :42–:55) and explicitly names the superseded prior version at **:160** (`7190c0efda`, 2026-11-21, written against a different draft).
- **evaluate.** Seven defects named, each with receipt + additive fix; all eight gate numbers exact; the sole-route discipline held; no fabricated artifact. The verdict **stands**. The AoA's *separate* BA-D1 "revert mis-trace" finding does **not** survive against the landed version (see §2.2 and §3).
- **adopt-or-park.** Adopt `DEFECTS-NAMED`. Park the four wall-clause QUESTIONS (Q1–Q4) as questions with receipts. Park the AoA's BA-D1 as an **AoA-layer adjustment**, not a BA defect; park the phantom-sha seam (SW-1) as a question about the reporting layer, never about the artifact.
- **standardize.** The named standards: MAP-style **asserted → status → basis** (agent-work-review §Sequence), the **wall clause**, the **byte-provenance equality rule** (no `==` between distinct ledger keys), and the **version-pin rule** (a verdict names the exact commit it audited).
- **verify.** Receipts: `sha256sum` (both copies) · cell-key grep · `python3 -c 'print(647716330-641262336)'` → `6453994` · `wc -l` → 214 · artifact §2 gate-row grep (G1–G8) · artifact :156–:157 · audit :42–:55 and :160 · `git cat-file -e 34424e81ac^{commit}` → EXISTS.

**FORENSIC PASS BA.** Evidence trail: D1 → cells `model_bytes`/`egress_bytes` (artifact §4 rule 2, audit :69); D2 → artifact §2 vs :156–:157; R1–R10 → artifact §3, not any summary. Byte verification: all above. **Parent class: P2 (nominal equality without byte provenance)** — the `"=="` in the artifact's G4/§4 rows and the `pin == model` bar is a template-level class, not a lane error; the lanes named it, the artifact carries it. Dating: observed 2026-11-21 19:14 (`2cc6f1832f`) → re-landed 2026-11-21 23:51 (`7190c0efda`) → harness-fold 23:51:43 (`4912c0ad8f`) → re-materialization 2026-11-22 09:56 (`1c387c9cfe`) → cold re-audit 2026-11-23 09:41 (`34424e81ac`). The **amplified** version drift is the HARNESS-FOLD/SW-2 re-materialization; it exposed the class, it did not create it (defect-forensics §4: root vs amplifier — clean correlation, causation labeled).

**AGENT-WORK-REVIEW BA.** Consistency: audit :34 (G4) cell numbers = ledger bytes exactly; audit :69 delta = re-derived delta; audit :160 names the superseded version, so the current landing does not contradict its own §3. Accuracy: no misquoted figure found. Unverifiable-from-here: live HF model-card attestation, the OPUS §4/§6/§5 pages (out of brief ground) — carried as questions, not asserted.

**DISCOVERY-LOG BA.** (1) Origin: operator's armament-gap check → this lane opened BA cold. (2) Ground read: cells ledger + artifact + audit via `read_file`. (3) First check: both cells copies hashed equal → dual anchor real. (4) Arithmetic: delta 6,453,994 → D1 confirmed. (5) Form check: §2 = G1–G8, G9–G15 only in F4 grid → D2 confirmed. (6) Trace check: R1–R10 from artifact §3, prior version named at :160 → AoA's mis-trace finding inverted. (7) Seam: phantom reported sha absent in git, real sha exists → SW-1 is a report-layer class. (8) Outcome: CONFIRMED-by-spine.

**OUTCOME — BA: `CONFIRMED-by-spine`.** The verdict stands and is now skill-grounded. The AoA's BA-D1 sub-finding is adjusted at the AoA layer (§2.2), not here.

### 1.2 LANE-CA — `ADAPT` / `NOT-READY with named seams` (G2/G3/G4 open), 2026-11-23 landing `f4feeb4fc0`

- **classify.** *Complicated*: a sound specification whose guarantees are stated but not runnable. The layer's own §6 gate vocabulary (OPEN, not PASS) is the right frame; no chaotic re-ordering.
- **choose.** Probes by VOI: (a) the promised checklist-table form, (b) the gate's measurable variable, (c) the registry's existence, (d) the ancestry receipt's pin.
- **probe (executed, read-only).**
  - `grep -nE '^\| *(Action|Done-when)' lane-c-verification-readiness-20261121.md | wc -l` → **0**. `wc -lc` → **318 lines / 18,978 B**, exactly the audit's header. §4:153 promises a `(Action | Artifact | Done-when)` table per condition; **none of C1–C9 has one** → G3 FAIL-ON-FORM confirmed.
  - The audit's variable-mismatch claim re-read: artifact §2:104–105 measures "distinct runner/heap identities"; the ground's variable is the **pinned model-base ID** (`upstage/solar-mini4:free` at artifact :74/:83; `runner/heap` occurs only at :104). Two runs of one model on two hosts pass the literal gate while failing the intent → the seam is real and the close-condition (count distinct model-base IDs, explicit two-host exclusion) is the right standard.
  - G4 registry: the audit's whole-study 0-hit find (`*pin_registry*`, `pins.json`, `verify_pin*`) is its own receipt. This pass **did not re-run that find**; carry the audit's 0-hit receipt as reported, mark re-derivation **partial** (wall clause: the empty registry is the QUESTION "where is the first pin row + re-derivation?", not a claim that one-run-per-pin is false).
  - Ancestry pin: `git cat-file -e ab471fc80c^{commit}` → EXISTS (`ab471fc80cf22ea91cc3a0094ea9fa6c9522a13f`); `git merge-base --is-ancestor ab471fc80c f4feeb4fc0` → exit **0 (TRUE)**; the same check at `6de5aba311` → exit **1 (FALSE)**. The CA audit's R5 claim (`→ yes`) is **true at its current landing**, false at the earlier one.
- **evaluate.** ADAPT stands: the four guarantee scores (G2a PARTIALLY EXECUTABLE, G2b MOSTLY COMPLETE/NOT LANDED, G3 FAIL-ON-FORM, G4 RULE ONLY) are accurate against the artifact; no OPEN gate was smuggled into PASS. The AoA's *separate* CA-D1 "false ancestry at CA's own commit" does **not** survive at the current pin (§2.2).
- **adopt-or-park.** Adopt `ADAPT`. Park the seven wall-clause questions (Q-THE-NORTH … Q-registry) as questions with receipts. Park the AoA's CA-D1 as an **AoA-layer adjustment**; park G2/G3/G4 OPEN exactly where the layer put them.
- **standardize.** Named standards: the **external-readiness-review deliverable contract** (one section per condition, checklist table `Action | Artifact | Done-when`), the **blind-panel brief-neutrality/target-pin** controls, the **wall clause**, and the **base-diversity definition** (distinct pinned model-base IDs, at dispatch-pin level, not child-ID / runner identity).
- **verify.** Receipts: table-row grep → 0 · `wc -lc` → 318/18,978 · artifact :74/:83/:104/:153 · `cat-file` + two `merge-base` exit codes · `git cat-file -e f4feeb4fc0^{commit}` → EXISTS.

**FORENSIC PASS CA.** Evidence trail: G3 → artifact §4:153 vs byte-level table count; G2 → artifact §2:104 vs ground model-base names; G4 → study-wide find (audit's receipt, partial re-derivation here); ancestry → git object store. **Parent classes: P3 (promised form not materialized)** and **P1 (unpinned reference)** — the same "defined, not closed / named, not pinned" mechanism that produced the AoA's pin-dependent sub-findings. Dating: original landing 2026-11-21 19:14 (`6de5aba311`) → re-landing 23:51 (`ef08fe6069`) → fold/re-materialization → cold audit 2026-11-23 09:38 (`f4feeb4fc0`). The ancestry verdict flips across exactly those two pins — the amplifier is version churn, the root is the unpinned receipt.

**AGENT-WORK-REVIEW CA.** Consistency: header size/lines match the artifact byte-for-byte; the four guarantee verdicts match the receipts in §A–§D; the receipt table R1–R16 does not contradict the guarantee scoring. Accuracy: variable-mismatch claim verified by term locations. Unverifiable-from-here: the live-HF model sha `415501bd…`, the fold §7-u–§7-x, and any panel row — all carried as OPEN questions by the landing itself.

**DISCOVERY-LOG CA.** (1) Origin: operator's armament-gap check → open CA cold. (2) Full read of audit + artifact. (3) Form check: 0 checklist rows, size matches header. (4) Variable check: runner/heap vs pinned-base located. (5) Registry: 0-hit find received as reported; partial re-derivation declared. (6) Ancestry: exit 0 at current pin, exit 1 at earlier pin — pin-dependence found. (7) Seam: AoA's "false ancestry" claim is pin-specific → adjustment, not fabrication. (8) Outcome: CONFIRMED-by-spine.

**OUTCOME — CA: `CONFIRMED-by-spine`.** The verdict stands and is now skill-grounded; the AoA's CA-D1 sub-finding is adjusted at the AoA layer (§2.2), not here.

### 1.3 THE AoA — `DEFECTS-NAMED` / `ADAPT` with 8 settle-conditions, 2026-11-23

- **classify.** *Complex*: cross-lane adjudication of three audits on a shared route, with a receipt-integrity seam and an independence claim. Bounded probe, no predictive certainty; the nine axes are the record's own frame, not a force-fit.
- **choose.** Probes: (a) git object store for reported vs real shas, (b) commit dates/order, (c) cross-lane consistency matrix on the false-equality claim, (d) citation hit-check for the AoA's own cross-references, (e) act-0 read gate vs on-disk inputs, (f) armament trace in briefs/landings.
- **probe (executed, read-only).**
  - Phantom shas `16130475d2` (BA), `ab660b943b` (AA), `f4b845f05b` (CA) → `git cat-file -e` **ABSENT** (all three). Real shas `34424e81ac`, `2cc6f1832f`, `2ce77ce5ad`, `6de5aba311`, `f4feeb4fc0`, `7190c0efda` → **EXIST**. SW-1 (phantom report shas) **CONFIRMED**.
  - Commit dates: `6de5aba311` 2026-11-21 19:14 · `2cc6f1832f` 19:14 · `7190c0efda` 23:51 · CA re-landing 23:51 · `1c387c9cfe` 2026-11-22 09:56 (SW-2 re-materialization) · `f4feeb4fc0` 2026-11-23 09:38 · `34424e81ac` 2026-11-23 09:41. The AoA's §0 pins are the **2026-11-23 cold re-audits**; its §I "real landings" are the **2026-11-21 originals**. Both sets are real; the AoA never says they are different passes → identifier seam (§2.1).
  - Citation hit-check: `grep '\bG1\b\|\bI2\b'` over `lane-ca-audit-20261121.md` → **0 hits**. The AoA's §1.D "D1 confirmed by all three lanes independently (CA's G1/I2, BA's G1, AA's G1)" mis-cites CA. BA's D1 is **byte** equality (`647716330` vs `641262336`); AA's D1 is **SHA** equality (`pinned_repo_sha fc8b9934…` vs `model_safetensors_sha256 5747a90e…`). Two distinct variables, two lanes; CA tested neither → the "all three" claim is a cross-lane conflation (§2.3).
  - BA-D1 re-check: the AoA calls the revert mis-trace a live gap. The landed BA audit at **:160** explicitly names the superseded `7190c0efda` as the mis-traced version and re-derives R1–R10 from the artifact's own §3 → the finding is **true of the prior pass, false of the landed one** (§2.2).
  - CA-D1 re-check: false ancestry is **TRUE at `f4feeb4fc0`** (exit 0), **FALSE at `6de5aba311`** (exit 1) → pin-dependent (§2.2).
  - Act-0 read gate: `STAGE-PLAN-SEQUENCE-20261123.md` (114 lines) requires at act 0 "Read the cross-audit brief, all three plans, the record-mine, and the lane deliverables/contracts in full" before dispatch. The AoA records FLEETMATRIX/BATTERIES/RECORD-MINE as UNREAD — honestly, as UNKNOWN, never converted to PASS. This pass confirms the files **exist** at `plan/tank/` (`STAGE-PLAN-FLEETMATRIX` 201 lines · `STAGE-PLAN-BATTERIES` 153 lines · `plan/RECORD-MINE` 261 lines) but **did not read them** → the UNKNOWN stands; this is a QUESTION with a receipt, not a defect.
- **evaluate.** The **top-line verdict holds**: byte-level core confirmed (42/42, 8/8, R1 LANDED, all cell numbers), phantom shas real as phantom, no fabricated artifact, wall clause operating, seams named and settle-conditions teeth intact. Three **sub-findings** do not survive re-derivation and are amended below. The skill-grounding gap (§0) is **closed by this pass** — the AoA now has the armament on the record.
- **adopt-or-park.** Adopt `DEFECTS-NAMED` as the fan's skill-grounded state **after** the three amendments. Park all 8 settle-conditions as OPEN gates; park SW-1 (mechanism of phantom shas), SW-2 (index/disk divergence), the shared-route constraint, and the act-0 unreads as QUESTIONS with receipts. Park every named seam — none reconciled away.
- **standardize.** Named standards: think-tank **spine** (this document is its execution: classify/choose/probe/evaluate/adopt-or-park/standardize/verify at every step) · agent-work-review **consistency matrix + arithmetic re-derivation + identifier cross-check + explicit unverifiable list** · investigation-documentation **faithful discovery log with Limitations + Reproducibility** · defect-forensics **parent-class + root/amplifier + verdict-frame**. All other skills named-and-refused.
- **verify.** Receipts: `git cat-file -e` ×9 · `git log --format='%h | %ci | %s'` · `grep` citation hit-checks · `wc -l` input existence · `git show --name-only` per landing · the three landing outcomes in §1.1–§1.2.

**FORENSIC PASS AoA.** Evidence trails traced to their sources: phantom shas → git object store; D1 family → cells ledger keys; act-0 seam → sequence plan :18; armament gap → briefs/landings grep. Byte verification: all above. **Parent classes: P1 (unpinned reference — the root), P4 (armament assertion without application), P5 (cross-lane conflation), P2/P3 inherited from the audited artifacts.** Root vs amplifier: the **root** is the dispatch-time omission of the armament line (before 2026-11-21, now closed by this pass); the **amplifier** is the 2026-11-21 23:51 fold + 2026-11-22 09:56 re-materialization, which multiplied version identity and produced the pin-dependent findings. Date-stamped correlation; causation labeled, not folded as proven.

**AGENT-WORK-REVIEW AoA (consistency matrix).**

| # | Claim across verdicts | Status | Basis |
|---|---|---|---|
| C1 | 42/42 read-restore · 8/8 compose-check · R1 LANDED · cell numbers | **CONSISTENT** | cells ledger + BA/AA/CA audits; re-derived byte-exact above |
| C2 | Phantom report shas vs real landings (SW-1) | **CONSISTENT** | `cat-file` absent ×3 / exists ×6 |
| C3 | D1 "confirmed by all three lanes" | **ADJUSTED** | CA audit 0 G1/I2 hits; BA = byte equality, AA = SHA equality — two lanes, two variables |
| C4 | BA revert mis-trace (BA-D1) | **ADJUSTED** | BA audit :160 names superseded version; landed R1–R10 re-derived from artifact §3 |
| C5 | CA-D1 "false ancestry at CA's own commit" | **ADJUSTED** | exit 0 at §0 pin `f4feeb4fc0`; exit 1 at §I pin `6de5aba311` |
| C6 | §0 landing pins vs §I "real landings" | **DISCREPANCY (named)** | both exist; different passes; undated in the AoA |
| C7 | G2/G3/G4 OPEN / CA ADAPT | **CONSISTENT** | artifact table grep 0; registry owned as OPEN; no gate smoothed |
| C8 | act-0 inputs UNKNOWN | **UNVERIFIABLE-FROM-GROUND (honest)** | files exist (201/153/261 lines); not read here; not converted to PASS |
| C9 | live-HF / OPUS out-of-ground claims | **UNVERIFIABLE** | carried as questions by the landings; no online claim made here |

Arithmetic re-derivation: `647716330-641262336=6453994` ✓; cells sha both copies equal ✓; G1–G8 only / G9–G15 at :156–:157 ✓; 0 checklist rows ✓. Identifier cross-check: C4/C5/C6 above. Epistemic scoping: no adoption/permanence claim beyond evidence; drift reported, not patched.

**DISCOVERY-LOG AoA.** (1) Origin: operator's armament-gap check; three landings named. (2) All three read in full via `read_file`, plus AA landing, sequence plan, briefs, cells ledger. (3) Loaded the four armament skills. (4) Grepped armament trace → BA/CA/briefs 0, AoA claim-only. (5) Hashed cells → dual anchor real; re-derived D1 delta. (6) Checked artifact forms → CA 0 tables, BA G1–G8 only. (7) Git object store → phantom vs real shas; dated the passes. (8) Cross-checked citations → CA G1/I2 absent; BA :160 supersession found. (9) Re-checked ancestry → pin-dependent. (10) Confirmed act-0 inputs exist but stayed unread → UNKNOWN kept. (11) Verdict: top-line stands, three sub-findings adjusted. (12) Limitations + Reproducibility in §4–§5.

**OUTCOME — AoA: `ADJUSTED`.** Top-line `DEFECTS-NAMED` / `ADAPT` stands and is now skill-grounded; three sub-findings are amended with receipts: **C3** ("all three lanes confirm D1" → two lanes, two variables; CA citation absent), **C4** (BA-D1 revert mis-trace → true of superseded `7190c0efda`, not of landed `34424e81ac`), **C5** (CA-D1 false ancestry → pin-dependent, true at `f4feeb4fc0`, false at `6de5aba311`). The identifier seam C6 is named, not reconciled.

---

## 2 · THE ADJUSTMENTS, STATED AS AMENDMENTS (wall clause: questions with receipts)

### 2.1 Identifier seam — §0 pins vs §I "real landings"
The AoA §0 uses **CA `f4feeb4fc0` / BA `34424e81ac` / AA `2ce77ce5ad`** (2026-11-23 cold re-audits); §I uses **CA `6de5aba311` / BA `2cc6f1832f` / AA `2ce77ce5ad`** (2026-11-21 originals). All six exist; both sets are real. The AoA never says they are different passes. **Amendment:** the receipt ledger must carry both commits with their dates and the pass each belongs to. Receipt: `git log --format='%h | %ci | %s' --no-walk …` above.

### 2.2 Two pin-dependent findings
- **BA-D1 (revert mis-trace):** amend to "mis-trace existed in the **superseded** `7190c0efda` and was **self-corrected** in the landed `34424e81ac` at audit :160." Receipt: BA audit :160 + `git show --name-only 7190c0efda`.
- **CA-D1 (false ancestry):** amend to "pin-dependent — `is-ancestor(ab471fc80c, f4feeb4fc0)` exit 0 (the claim is TRUE at the AoA's own §0 pin); exit 1 only at the earlier `6de5aba311`." Receipt: the two `merge-base` exit codes above. The honest disposition is a QUESTION about which pin the AoA intended — never a fabricated claim and never a silent pass.

### 2.3 "All three lanes" conflation
Amend §1.D: D1 false-equality is **two distinct defects on two distinct variables**, confirmed by **two** lanes — BA (bytes: `647716330` vs `641262336`) and AA (SHA keys: `fc8b9934…` vs `5747a90e…`). CA audited the verification-readiness layer and has **0** `G1`/`I2` hits. Receipt: the citation grep + BA audit :69 + AA audit §1 G1/§3 D1.

---

## 3 · FORENSIC PARENT-CLASSES — the one mechanism under the seams

| Class | Name | Instances observed | Parent / amplifier |
|---|---|---|---|
| **P1** | **Unpinned reference** | phantom report shas (SW-1); §0-vs-§I landing pins; BA-D1 supersession; CA-D1 pin flip | **Root class of this pass.** The artifact's report layer does not bind a finding to one exact commit; version churn (fold + re-materialization) amplifies it into contradictory verdicts |
| **P2** | **Nominal equality without byte provenance** | BA D1 (egress vs model bytes); AA D1 (pin vs safetensors); artifact G1/I2 bar | Root in the **artifact template**, not in the lanes; named and revertible in all three lands |
| **P3** | **Promised form not materialized** | CA G3 checklist tables (0 rows); G4 registry empty; G2 gate never fired | Root in the layer's spec-vs-execution gap; ADAPT, not REJECT |
| **P4** | **Armament assertion without application** | AoA `:6`/`:201` claim; briefs and transcripts carry no spine; BA/CA name it nowhere | **Dispatch-time root** — closed by this pass; the "DATA but not skill-grounded" gap the operator found |
| **P5** | **Cross-lane conflation** | "D1 confirmed by all three lanes" — one label over two variables and a third lane that tested neither | Root in the consolidation step; the matrix (§2) separates the instances |

**Date-stamped root vs amplifier:** root = armament omission at dispatch (before 2026-11-21, now repaired); amplifier = HARNESS-FOLD `4912c0ad8f` 2026-11-21 23:51:43 + SW-2 re-materialization `1c387c9cfe` 2026-11-22 09:56, which multiplied version identity. Clean temporal correlation; causation labeled, not proven (defect-forensics §4 / investigation-documentation pitfall on correlation→causation).

---

## 4 · THE VERDICT — skill-grounded state and the integrity line

**The fan's state:** BA `DEFECTS-NAMED` and CA `ADAPT` are **CONFIRMED-by-spine** — every load-bearing number, form failure, and gate state re-derived against artifact + ground; both now carry the armament on the record. AA (not a target of this pass) remains the AoA-adjudicated `DEFECTS-NAMED`, whose D1/D2 were re-read and found consistent.

**The AoA's state:** `DEFECTS-NAMED` / `ADAPT` is **ADJUSTED** — the top-line stands skill-grounded (byte core, wall clause, settle-conditions, seam inventory all hold); three sub-findings (C3, C4, C5) are amended with receipts, and one identifier seam (C6) is named. No finding is reconciled away; no new machinery is invented to "fix" them.

**The stage's integrity line:** *the verdicts stood as DATA before this pass and stand as skill-grounded now — because the armament was actually loaded and the spine actually run against the artifacts, not merely named in a header. Every byte claim was re-derived, every receipt traced to its source, every parent class named; the three adjustments are corrections of the AoA's consolidation layer, not damage to the fan's landings. Nothing public · RFC quiet · no installs · study paths only · no push · no destructive git; the settle-conditions remain the verdict's teeth, never a smoothed PASS. A non-reproduction is a QUESTION with receipts.*

---

## 5 · SEAMS NAMED — NONE RECONCILED AWAY

1. BA/CA/AoA landings dispatched without the armament line — **closed by this pass** (armament loaded, spine executed); the brief-level omission stays on the record as the parent cause.
2. SW-1 phantom report shas — **KEPT** as a mechanism question; artifact receipts are clean.
3. C6 §0-vs-§I landing pins — **KEPT**; both real, different passes, now dated.
4. C4 BA-D1 / C5 CA-D1 — **ADJUSTED** as pin-dependent; the pins named, not guessed.
5. C3 "all three lanes" — **ADJUSTED** to two lanes / two variables.
6. CA G2/G3/G4 OPEN, G2 gate never fired, G4 registry empty — **KEPT OPEN** per the layer's own §6.
7. Shared-route constraint (three audits rode one base) — **KEPT**; same-base convergence is never claimed as independence.
8. Act-0 unreads (FLEETMATRIX/BATTERIES/RECORD-MINE) — **KEPT UNKNOWN**; files exist, not read this pass.
9. Out-of-ground claims (live-HF sha, OPUS pages, fold §7-u–§7-x) — **KEPT** as questions with receipts.
10. Record-correction rows (BA-D1/S1/S3/S5/S6, AA-S1/S2, CA-D1/S1/S2, SW-1, SW-2, AOA-OQ) — **PRESERVED**, history never rewritten.

---

## 6 · LIMITATIONS + REPRODUCIBILITY (investigation-documentation form)

**Limitations.** This is a re-derivation of three *landed* verdicts, not a new audit of the canary itself: no battery was re-run, no model re-loaded, no external page fetched. The G4 registry 0-hit find and the live-HF / OPUS claims are received as the landings' receipts, not independently re-executed (declared at §1.2/§1.3). The act-0 inputs are confirmed present but unread. No root-cause *causation* is claimed for the version churn — the timeline is verified, the mechanism is a hypothesis.

**Reproducibility (commands, read-only).**
```
cd /root/workspace/repos/hermes-agent
git rev-parse --abbrev-ref HEAD && git rev-parse HEAD
for s in 16130475d2 ab660b943b f4b845f05b f4feeb4fc0 34424e81ac 2cc6f1832f 2ce77ce5ad 6de5aba311 ab471fc80c; do
  git cat-file -e "$s^{commit}" 2>/dev/null && echo "$s EXISTS" || echo "$s ABSENT"; done
git merge-base --is-ancestor ab471fc80c f4feeb4fc0; echo "CA-current exit=$?"
git merge-base --is-ancestor ab471fc80c 6de5aba311; echo "CA-original exit=$?"
git log --format='%h | %ci | %s' --no-walk 34424e81ac 2cc6f1832f 2ce77ce5ad 6de5aba311 f4feeb4fc0 7190c0efda
cd studies/rfc-143379-rig
sha256sum probes/CANARY-CELLS-20261120.json /root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json
grep -oE '"(model_bytes|egress_bytes|egress_secondary_downloads|load_seconds|param_count|argmax_next_token|deterministic_max_abs_diff|determinism_tolerance)"[^,}]*' probes/CANARY-CELLS-20261120.json
python3 -c 'print(647716330-641262336)'
grep -nE '^\| *(Action|Done-when)' plan/tank/lane-c-verification-readiness-20261121.md | wc -l
wc -lc plan/tank/lane-c-verification-readiness-20261121.md
grep -nE '^\| *G[0-9]+' plan/tank/lane-b-phase1-design-20261121.md
grep -nE 'G9|G1[0-5]' plan/tank/lane-b-phase1-design-20261121.md
grep -nE '\bG1\b|\bI2\b' plan/tank/lane-ca-audit-20261121.md | wc -l
```
Citation ledger: every numeric/identifier claim in this document carries its command or file:line inline (§1–§2); no memory-authored citations.

---

*Facimus semper. The verdict renders on the evidence; the evidence is on the record; the record corrects itself out loud — and this pass is that correction, made under the armament rather than beside it.*

*— kanban-pilot <pilot@rig.local>, 2026-11-23 · armament: think-tank + agent-work-review + investigation-documentation + defect-forensics · all others named-and-refused.*
