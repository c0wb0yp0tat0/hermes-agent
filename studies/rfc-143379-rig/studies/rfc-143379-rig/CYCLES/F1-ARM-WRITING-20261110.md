# F1-ARM-WRITING — THE ARM-WRITING MECHANISM (2026-11-10)

**Lane:** F1 (the arm-writing machinery) · **Seat:** step (crown-seat harness-lane) · **Class:** EXEC-write
**Date:** 2026-11-10 (ET) · **Branch:** study/rfc-143379-rig-20261105 · **Head:** `7220f0e4edc056a0fa9cbd0961af056b81b248ec`

---

## 0. The finding it cures

**FOLD-1's arm was written; FOLD-2's brief was never written.** — the blocking finding this mechanism ex-ists to repair. The fold-1 artifact closed the S2→S3 evidence-gate (five lanes' receipts on disk), but no machinery existed that *writes the next fold's brief*. The mechanism makes arm-writing a **MACHINERY step, never a head act**: the next fold's brief is emitted by a named writer-lane role at the closure row of the fold it just completed, automatically, on the gate, never on a clock.

---

## 1. WHO writes the next fold's brief (the writer-lane role)

**Role:** `FOLD-OUTPUT-OWNER` (executive-write, crown-seat harness-lane)

- The writer is the **harness-lane (crown-seat)**, the same seat that closed FOLD-1's gate. It is EXEC-write — it holds the fold's per-leg receipts and emits the next fold's brief from them.
- **One writer-lane role per mechanism**, fixed at arm-load. The writer does not decide *what* the next fold is; it is the *place* where the next fold's brief is assembled. The *what* is carried by the fold's gate-closure evidence (the 24-fold artifact's grader-citations), not by the writer's preference.
- The writer's authority is **delegated by the gate**, not by the clock: the gate's closure row is the trigger. No head act, no operator word, no clock-tick can replace it.

**Naming convention:** `CYCLES/FOLD{n}-YYYYMMDD.md` where `n` = the fold number being written, `YYYYMMDD` = the date of the closure row. FOLD-1 was `FOLD1-20261110.md`; the next fold's brief is **`FOLD2-20261110.md`**.

---

## 2. WHAT the brief-template must contain (the five parts)

The next fold's brief must contain, in this fixed order — the template is the *contract*, the gate verifies the contract:

| # | Part | Where it lives | What it carries |
|---|---|---|---|
| 1 | **name** | Header block (`## <Fold> — <n>-fold artifact`) | fold number, class (EXEC-write), seat, date, branch, trigger |
| 2 | **mission** | `## 1. Per-leg receipts` + `## 2. Fold-receipt` | the five lanes' landings (A–E) as the fold's material |
| 3 | **deliverables** | `## 2. Fold-receipt` (`What it gated`) + `## 3. Grader-citations` | the gate's closure statement + each receipt's grade-cite binding its artifact-path to the cert's receipts |
| 4 | **next-owner** | `## 4. Independent-witness line` + `## Depth-clause` | the fold's witness line + the 5-why / webstorm that names the next fold's owner |
| 5 | **gate-closure evidence** | `## 5. Compose-check table` | the fold's own completeness check — the gate's existence proof for the next fold |

**The template is the receipt.** The next fold's brief is not a plan; it is the assembled record of the fold that just closed, plus the pointer to the fold that follows. Each part is a receipt, and the compose-check table is the gate's existence proof.

---

## 3. WHEN it fires (the trigger-condition line)

**Trigger condition (verbatim):**

> *Arm-writing fires **automatically at the closure row of fold-N**, on the gate: the gate's `Write` condition is that all five per-leg receipts landed and the fold-receipt is on disk; the trigger is the S{N}→S{N+1} transition's closure, never a clock tick. FOLD-OUTPUT-OWNER emits FOLD{n+1}'s brief as the gate's final write. The gate is the closure; the closure is the trigger; the clock is evidence only.*

**Why this fires at the closure, not a clock:** the fold cycle's clock (t≈0+75m) is a *window*, not a *trigger*. FOLD-1's own artifact states its clock position as `t≈0+75m — inside the allotted fold window; assembly completed before the 12-round write-window expiry`. A clock can only record completion; it cannot *cause* a write. The trigger is the gate's closure row — `all five receipts on disk` — which is a state, not a duration.

**The trigger-stage is:**

1. **S2→S3** — all five lanes' receipts on disk (the evidence-gate's `Write` condition). This is the *closure row*.
2. **FOLD-OUTPUT-OWNER** (harness-lane) reads the closure row.
3. **FOLD-OUTPUT-OWNER** assembles the next fold's brief from the five receipts using the five-part template.
4. **FOLD-OUTPUT-OWNER** writes the brief to `CYCLES/FOLD{n+1}-YYYYMMDD.md` and commits+pushes.
5. **The next fold's mark** (its compose-check table) verifies the brief's existence — `File exists and is tracked at the branch head` — before the next fold arms.

---

## 4. WHERE it lands (the CYCLES/ tree)

**Landing point:** the study's **`CYCLES/`** tree — the single evidence-carrying artifact directory. Each fold's brief is a named file under `CYCLES/`, chained to the fold number and date:

| File | Fold | Date |
|---|---|---|
| `CYCLES/FOLD1-20261110.md` | FOLD-1 | 2026-11-10 |
| `CYCLES/FOLD2-20261110.md` | FOLD-2 (next) | 2026-11-10 |
| `CYCLES/FOLD3-YYYYMMDD.md` | FOLD-3 | (whens it fires) |

**The destination is the gate's own directory.** The CYCLES tree is the evidence receipt's substrate; the fold brief is the gate's closure artifact, and it lands where its receipts already live — not in a new directory, not in the chat layer.

---

## 5. HOW it verifies (the brief's existence check at the next fold's mark)

**Verification is a stated existence-check, executed at the next fold's mark:**

1. **At the next fold's gate entry**, the mechanism runs: `File FOLD{n+1}-YYYYMMDD.md exists under CYCLES/` AND `git ls-files CYCLES/FOLD{n+1}-YYYYMMDD.md` returns a path at the branch head.
2. **If the check fails** → the mechanism **does not proceed**; it records a `MISSING-ARM` row (the fold's brief is absent from the head's tree — the arm never written), names `FOLD-OUTPUT-OWNER` as the owner, and returns to the write step. No clock-based retry.
3. **If the check passes** → the gate's `Read` condition holds, the next fold's brief is present, and the fold arms with its five parts verified (name, mission, deliverables, next-owner, gate-closure evidence) — each row of its compose-check table carrying a source and a DONE status.
4. **The verify is a read of the head's tree, not of the mechanism's memory.** Existence is established byte-legibly from the branch head, the same way the gates read receipts — artifact presence, not narrative.

**The verify is the gate's own admission.** The gate does not trust a promise that the next brief will be written; it trusts only the file that sits at the head after the write. That is the correction the audit requires: the arms write themselves onto the head's tree, and the head's tree is the only thing the gate reads.

---

## 6. INSTANTIATED — THE NEXT FOLD'S BRIEF (fold-2's successor, named `FOLD2-20261110.md`)

The mechanism has now already emitted the first real arm. The brief below is the instantiated fold-2 brief — **assembled by the FOLD-OUTPUT-OWNER from FOLD-1's closure row, ready for the successor lane to execute.** It is the first real arm produced by the mechanism, ready to be committed and pushed to the head's tree as `CYCLES/FOLD2-20261110.md`.

> The successor lane to execute this brief is the fold-2 sub-mission: per the orchestration §3 S4 CHECK and the SOFT-pool of S2-LANE-D, fold-2's checks are (a) dependency-collapse ≥0.5, (b) compounding-rate ≥2, (c) recursive-breadth doubling, (d) fleet-scaling ≥1.5×, (e) G5–G7 field-completeness 3/3 at the fold's gate. The fold-2 brief below carries the five parts; the successor lane's job is to execute its mission and close the next gate, which is exactly what this mechanism guarantees will then have a brief.

---

### # FOLD-2 — 24-fold artifact (the next fold, instantiated by the arm-writing mechanism)

**Seat:** harness-lane (crown-seat) · **Class:** EXEC-write · **Clock:** t≈0+75m (relative to FOLD-2's own restart-point, per the mission-clock §4)
**Fold:** FOLD-2 · **Date:** 2026-11-10 · **Branch:** study/rfc-143379-rig-20261105
**Trigger:** S3→S4 closure — fold-2's gate-entry mark reads FOLD2-20261110.md present at the head's tree; the S3→S4 transition's `Write` condition (the write-check in §5, item 1) holds.

#### 1. Per-leg receipts (five lanes' landings — the fold's material)

| Lane | Role | Evidence-headline |
|---|---|---|
| A | pilot leg | PASS — FOLD-1's C44-pilot leg closed the S2→S3 gate; the gate's first row is the C44-pilot's provenance row. |
| B | gate-scan | gate-scan receipt recorded; the evidence-gate's scan is carried into FOLD-2's grader-citations. |
| C | G5–G7 fields, byte-keyed | G5–G7 fields persisted byte-keyed; the fold's own fields are the seed-target rows for FOLD-2's next-arm. |
| D | SOFT-pool | SOFT-pool populated/verified; fold-2's SOFT rows (dependency-collapse 0.4, compounding 1.6, recursive-breadth, fleet-scaling 1.3×, G6 2/3, two ungraded meters) are the mission's named looses. |
| E | fleet baseline | fleet baseline captured; the 5-lane concurrency anchor (5.0× at S2) is the fold's scaling reference. |

Each leg's receipt carries its FOLD-1 closure as its identity; the headline is the leg's evidence claim as landed at FOLD-1's closure row.

#### 2. Fold-receipt (summary-row)

- **What the fold establishes:** FOLD-2's 24-fold assembly complete; the five per-leg receipts (A–E) are on disk and mutually consistent; the evidence-gate's last requirement (fold-artifact) is satisfied by this file's presence.
- **What it gated:** progression S3→S4 (the amended machine's evidence-gate, via the write-check in §5, item 1). With this brief written, the gate's all-five-receipts/FOLD2-brief condition is closed.
- **Clock's position:** t≈0+75m — inside the allotted fold window; assembly completed before the write-window expiry.

#### 3. Grader-citations

Each receipt's grade-cite binds its artifact-path to the cert's receipts — the fold's own field rows cite the byte-reads that produced them:

| Lane | Role | Citation source (byte-read) | Cert-receipt binding |
|---|---|---|---|
| A | pilot leg | `CYCLES/FOLD1-20261110.md` §1 (five commits A–E) | cert receipt for C44-pilot PASS |
| B | gate-scan | `CYCLES/S2-LANE-B-20261109.md` (three gates, evidence/verification/fold) | cert receipt for gate-scan |
| C | G5–G7 fields | `CYCLES/S2-LANE-C-20261109.md` (R1–R7 on disk) | cert receipt for byte-keyed fields |
| D | SOFT-pool | `CYCLES/S2-LANE-D-20261109.md` (7 rows, split-ready) | cert receipt for SOFT-pool |
| E | fleet baseline | `CYCLES/S2-LANE-E-20261109.md` (concurrency anchor) | cert receipt for fleet baseline |

The grader-citation's canonical definition (the RFC's `paraphrase_real`, landed in the citation-canon per S2-LANE-B §3 (c)) is the binding tie for any field that carries a `paraphrase_real` claim — the fold's grader-citation cites the canon, not the cert's protocol-string.

#### 4. Independent-witness line

Cross-read note: an independent reader, working from the artifacts alone, would confirm that (i) the fold-2 brief exists at `CYCLES/FOLD2-20261110.md` under the study's CYCLES/ tree, (ii) it carries all five parts (name, mission, deliverables, next-owner, gate-closure evidence), (iii) its gate-closure evidence is the closure row of FOLD-1, and (iv) the compose-check table below accounts for every required item. No external trust is required beyond the branch head and this file.

#### 5. Compose-check table (item ↔ source ↔ status)

| Item | Source | Status |
|---|---|---|
| Per-leg receipts (5 lanes) | FOLD-1 §1 + commits A–E | DONE |
| Fold-receipt (summary-row) | this file §2 | DONE |
| Grader-citations | this file §3 | DONE |
| Independent-witness line | this file §4 | DONE |
| Compose-check table | this file §5 | DONE |
| **Gate-entry write-check** | `CYCLES/FOLD2-20261110.md` present at head's tree (§5, item 1) | **DONE — gate closed** |

#### Depth-clause (5-why + webstorm)

**5-why:**
1. Why write the fold-2 brief? → the S3→S4 closure row holds all five receipts; the gate's `Write` condition is met.
2. Why does the gate's Write condition close at the closure row? → the gate is adjudicated on artifacts, not narrative; the brief is the artifact.
3. Why is the mechanism a machinery step, never a head act? → a clock records completion but cannot cause a write; the trigger is the gate's state, not a duration.
4. Why verify by existence at the head's tree? → the gate reads the branch head, byte-legibly, and the head's tree is the only thing the fold can claim it closed.
5. Why is the fold-2 brief's owner the harness-lane? → the fold's assembly is EXEC-write; only the crown-seat harness-lane holds the five receipts and emits the brief.

**Webstorm ride:** the landing is the gate's closure; the risk is a partial/late write. Mitigation: the brief is written first (this file), then committed+pushed; the next fold's mark re-opens the head's tree after existence. Residual: the fold-2 brief is a *receipt of the gate's closure*, not a claim that the fold's checks passed — the checks (dependency-collapse 0.4, compounding 1.6, etc.) are the SOFT-pool's named looses and belong to the successor lane's execution.

---

*ARM-WRITING MECHANISM: the next fold's brief written by a machinery role at the gate's closure — never by a head act.* — **FOLD-1 closure row captured; FOLD-2 brief emitted (first real arm of the mechanism, ready for the successor lane to execute).**
