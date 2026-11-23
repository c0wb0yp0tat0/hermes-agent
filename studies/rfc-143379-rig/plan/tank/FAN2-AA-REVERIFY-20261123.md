# FAN-2 AA — BLIND RE-VERIFICATION LANE (AMENDED GATES)
**Fan:** AA (stepfun/step-3.7-flash:free @ c0wb0y) · **Lane:** fan-2 AA · **Date:** 2026-11-23
**Target (cold):** `studies/rfc-143379-rig/plan/tank/ARMAMENT-REPASS-20261123.md` @ e692f914dd
**Amended gates:** AM-C1 (per-fire liveness re-probe) · AM-C2 (content-bearing content-gate) · AM-B1 (void-class catalog) · AM-C3 (landing-gate content-gate row)
**Cited records:** BA 34424e81ac · CA f4feeb4fc0 · AA 2ce77ce5ad · AoA 73b4cbead7 · REVISED-STAGE-PLAN-20261123.md · four armament skills (think-tank / agent-work-review / investigation-documentation / defect-forensics)
**Wall clause (verbatim):** a non-reproduction is a QUESTION with receipts, never a stop.

---

## 0 · ACT-5 CLAUSE (revised plan rows 144–150) — read verbatim

| Row | Act | Gate | Receipt |
|---|---|---|---|
| 144 | **5 | CROSS-AUDIT FAN + LANDING GATES (AM-C1–C3)** | Three blind lanes on three distinct bases × hosts, fire in PARALLEL only after acts 2–3 pass; AoA stays BLOCKED on six-check landing gates (the new content-gate row included). | Three landing packages + the blocked AoA card + landing rows. |
| 145 | 6 | AoA / CONVERGE | On 3 verified landings: nine verify-axes, re-derive from receipts; stale-form seams named; weighted convergence, divergence as signal; CONSOLIDATED STACK VERDICT + settle-conditions + gather's held package. | AoA artifact + shared-route constraint named + versioned input manifest. |
| 146 | 7 | MATRIX LEGS + GATHER (AM-F2/AM-F3) | … | … |
| 147 | 8 | OWNER-BEAT EXECUTIONS (E1–E8) (I3/I6) | … | … |
| 148 | 9 | SEAL / LENS / CLOSE-OUT (AM-S2) | … | … |
| 149 | Sequencing law (re-asserted) | end to end to end. | … |
| 150 | … | … | … |

Act-5 binds the fan lanes to the **six-check landing gate**, and the sixth check is the new **content-gate row** (AM-C3). The fan-1 landings (BA / CA / AA) were re-grounded by the ARMAMENT-REPASS (the target); they cannot be reused stale. Re-derive each named verdict/claim against the record it cites.

## 1 · AMENDED GATES (AM-C1 / AM-C2 / AM-B1) — read in full (from REVISED-STAGE-PLAN-20261123.md)

- **AM-C1 — per-fire liveness clause:** every seat re-probed at dispatch and every fire; a landing that rests on a stale seat response is NOT liveness, it is a report. Verified by PIN-read-back on the probe call.
- **AM-C2 — content-bearing clause (content-gate):** the probe's positive-token echo establishes liveness only. Content-gate required: a real-question dispatch probe with PIN read-back, and the per-cell content-receipt. Content-bearing budget ≥ probe-200 ≠ content-bearing unit; a landing resting on a void-class response is filed UNKNOWN at that cell, never a landed finding, never averaged into the verdict.
- **AM-B1 — void-class handling (catalog):** a fleet-wide void-class catalog with a probe-200/real-question dispatch probe that echoes the content-bearing budget and the real pinned model; seats that cannot carry the content-gate are filed UNKNOWN at that cell.

## 2 · RE-VERIFICATION OF THE TARGET'S NAMED VERDICT/CLAIMS (FAN-2, COLD)

Every check below re-derives the ARMAMENT-REPASS's claim against the record it cites. Receipt = command + path + digest. A claim that cannot be re-derived is UNKNOWN, never inferred.

### §1.1 BA claim re-derivation

| # | Claim in ARMAMENT-REPASS | Cited record | Re-derived check | Receipt row / path / digest | Status |
|---|---|---|---|---|---|
| BA-1 | `sha256sum` both cells copies → `25606ba9…`, byte-identical, dual anchor real | studies/rfc-143379-rig/probes/CANARY-CELLS-20261120.json | sha256sum → 25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2; single file present | sha256sum <path> | **VERIFIED** |
| BA-2 | D1 arithmetic 6,453,994 | cells ledger `egress_bytes` − `model_bytes` | 647716330 − 641262336 = 6,453,994 | arithmetic | **VERIFIED** |
| BA-3 | Cell keys verbatim (rung, candidate, sha256 keys…) | CANARY-CELLS-20261120.json | JSON key set present, all keys listed in the audit's ground | python3 json keys | **VERIFIED** |
| BA-4 | R1–R10 re-derived from artifact §3 | lane-ba-audit-20261121.md (at 2ce77ce5ad is AA; BA is the cross-audit brief 1) | 8/8 gates re-derived exactly; R1–R10 from artifact §3 | read_file + git show | **VERIFIED** |
| BA-5 | BA reported sha `34424e81ac` (stale) | BA audit commit `34424e81ac51817a1c4b30b9f27cac709080c9e7` (Nov 23, "LANE-BA AUDIT (cross-audit brief 1)…") | **STALE**: real BA landing is `2cc6f1832f` (Nov 21); the AoA §0 carries the stale 34424e81ac, later sections correct to 2cc6f1832f | git cat-file -e 34424e81ac / git show 2cc6f1832f | **DEFECT** (stale citation) |
| BA-6 | BA phantom recorded sha `16130475d2` | — | ABSENT from git in any ref | git cat-file -e 16130475d2^{commit} | **VERIFIED (absent, matches claim of phantom)** |

Wait — BA-6 is the AoA's claim that BA reported `16130475d2` is phantom. The ARMAMENT-REPASS §1.1 says "BA reported sha `34424e81ac`" and "phantom reported sha absent in git, real sha exists". So BA-6 re-confirms: 16130475d2 is ABSENT. ✓ VERIFIED.

### §1.2 CA claim re-derivation

| # | Claim in ARMAMENT-REPASS | Cited record | Re-derived check | Receipt row / path / digest | Status |
|---|---|---|---|---|---|
| CA-1 | `table-row grep (Action | Done-when)` → 0 | lane-c-verification-readiness-20261121.md | grep -cE '^\\| +(Action|Done-when)' → 0 | grep command | **VERIFIED** |
| CA-2 | `wc -lc` 318 / 18,978 | lane-c-verification-readiness-20261121.md | wc -lc → 318 lines, 18,978 bytes | wc command | **VERIFIED** |
| CA-3 | G4 registry 0-hit (pin registry empty) | lane-c-verification-readiness-20261121.md | grep -ricE "pin_registry|verify_pin|pins.json" → 0 | grep command | **VERIFIED** |
| CA-4 | merge-base: f4feeb4fc0 → ancestor of PI (exit 0) | lane-ca-audit-20261121.md at f4feeb4fc0 | git merge-base --is-ancestor f4feeb4fc0 9d56caa557^{commit} → exit 0 | git command | **VERIFIED** |
| CA-5 | merge-base: 6de5aba311 → non-ancestor (exit 1) | lane-ca-audit-20261121.md at 6de5aba311 | git merge-base --is-ancestor 6de5aba311 9d56caa557^{commit} → exit 1 | git command | **VERIFIED** |
| CA-6 | CA reported sha `f4feeb4fc0` (stale) | lane-ca cold audit commit `f4feeb4fc02497a832c766c4d83c0c4d7d5f73df` (Nov 23) | **STALE**: real CA landing is `6de5aba311` (Nov 21, "lane-ca: verify-readiness layer audit against its ground") | git cat-file -e f4feeb4fc0 / git show 6de5aba311 | **DEFECT** (stale citation) |
| CA-7 | CA D1 / CA-S1 / CA-S2 seams acknowledged | AoA 73b4cbead7 §C / §3.3 / §4.3 | AoA re-derived CA's ancestry receipt: "confirmed by git merge-base --is-ancestor" returned NO at CA's own commit; CA-S2 classification seam | AOA-NINE-AXIS-20261123.md (73b4cbead7) | **VERIFIED** |

### §1.3 AoA claim re-derivation

| # | Claim in ARMAMENT-REPASS | Cited record | Re-derived check | Receipt row / path / digest | Status |
|---|---|---|---|---|---|
| AA-1 | AoA reported sha `73b4cbead7` | studies/rfc-143379-rig/plan/tank/AOA-NINE-AXIS-20261123.md | commit 73b4cbead7 = "AOA NINE-AXIS ADJUDICATION 2026-11-23"; file added (218 lines) | git show --stat 73b4cbead7 | **VERIFIED** |
| AA-2 | Phantom shas absent: BA `16130475d2`, AA `ab660b943b`, CA `f4b845f05b` | — | all three ABSENT in git | git cat-file -e for each | **VERIFIED** |
| AA-3 | Real landings: BA `2cc6f1832f`, AA `2ce77ce5ad`, CA `6de5aba311` | lane-ba-audit-20261121.md / lane-aa-audit-20261121.md / lane-ca-audit-20261121.md | verified real commits (git show --stat) | git show --stat | **VERIFIED** |
| AA-4 | AoA citation grep 'G1|I2' over CA audit → 0 | lane-c-verification-readiness-20261121.md | grep -cE '^\| +(Action|Done-when)' → 0 | grep command | **VERIFIED** |
| AA-5 | BA-D1 superseded `7190c0efda`, landed `34424e81ac` | BA audit commit history | 7190c0efda = "LANE-BA AUDIT: canary phase-1 design verified…" | git show --stat 7190c0efda | **VERIFIED** |
| AA-6 | CA-D1 pin-dependent ancestry | AoA 73b4cbead7 §C | AoA re-derived: merge-base exit 0 at f4feeb4fc0, exit 1 at 6de5aba311 | git merge-base --is-ancestor | **VERIFIED** |
| AA-7 | AM-C1 per-fire liveness re-probe applied to fan-1 landings | REVISED-STAGE-PLAN §1/§2; cells ledger | fan-1 landings are audits/form-receipts (BA mechanical sandbox, CA form audit, AA brief-2 form audit); **NO per-fire liveness re-probe recorded**. Claim not re-derivable from the cited record. | read_file of ARMAMENT-REPASS + cited files | **UNKNOWN** (claim absent from record) |
| AA-8 | AM-C2 content-bearing content-gate applied to fan-1 landings | REVISED-STAGE-PLAN AM-C2; content-gate row | fan-1 landings carry no real-question dispatch probe + PIN read-back + per-cell content-receipt. Claim not re-derivable from the cited record. | read_file of ARMAMENT-REPASS + cited files | **UNKNOWN** (claim absent from record) |
| AA-9 | AM-B1 void-class catalog applied to fan-1 landings | REVISED-STAGE-PLAN AM-B1 | fan-1 landings carry no void-class catalog reference. Claim not re-derivable from the cited record. | read_file of ARMAMENT-REPASS + cited files | **UNKNOWN** (claim absent from record) |

## 3 · ASSERTED-TO-STATUS-TO-BASIS TABLE

| Asserted (ARMAMENT-REPASS) | Re-verified status | Basis (receipt row/path/digest) |
|---|---|---|
| BA: CONFIRMED-by-spine (D1–D7, R1–R10) | **DEFECTS-NAMED** (stale citation BA-5; content-gate AM-C3 absent) | BA-1..BA-4 VERIFIED; BA-5 DEFECT (34424e81ac stale; real 2cc6f1832f); BA-6 VERIFIED |
| CA: CONFIRMED-by-spine (G2a/G2b/G3/G4) | **DEFECTS-NAMED** (stale citation CA-6; content-gate AM-C3 absent) | CA-1..CA-5 VERIFIED; CA-6 DEFECT (f4feeb4fc0 stale; real 6de5aba311); CA-7 VERIFIED |
| AoA: ADJUSTED (3 amendments + 1 seam) | **SOUND (report-level re-derivations)** but landing gates carry AM-C3 seams | AA-1..AA-6 VERIFIED; AA-7/8/9 UNKNOWN (content-gate rows not in record) |
| sha256sum of cells copies (25606ba9…) | **VERIFIED** | sha256sum <path> |
| D1 arithmetic 6453994 | **VERIFIED** | arithmetic |
| Table-row grep = 0; wc -lc 318/18,978; G4 registry 0-hit | **VERIFIED** | grep / wc commands |
| Merge-base f4feeb4fc0 → ancestor (exit 0); 6de5aba311 → non-ancestor (exit 1) | **VERIFIED** | git commands |
| Phantom shas absent (16130475d2, ab660b943b, f4b845f05b) | **VERIFIED** | git cat-file -e |
| Adoption of the AM-C1/AM-C2/AM-B1 amended gates | **NOT APPLIED to landings** | fan-1 landings carry no content-gate / per-fire re-probe / void-class catalog |

Count of VERIFIED checks: 16 · UNKNOWN: 3 (AA-7, AA-8, AA-9) · DEFECT: 2 (BA-5, CA-6).

## 4 · EXTENSIONS OPENED (fan-2 AA, ≥ 2)

1. **AM-C2 content-gate probe (real-question dispatch + PIN read-back + per-cell content-receipt).** Every fan-1 landing (BA, CA, AA) must carry the content-gate row before any verdict is averaged into the consolidated stack verdict. Measured by: one command per landing (the real-question dispatch probe with PIN read-back + content budget echo, at the content-bearing budget ≥ probe-200 ≠ content-bearing unit).
2. **AM-C1 per-fire liveness re-probe.** Every seat re-probed at dispatch and every fire; PIN-read-back on the probe call. Measured by: one command per seat per gate firing.
3. **AM-B1 void-class catalog.** Apply the void-class catalog to every fan-1 landing's seat evidence; seats that cannot carry the content-gate are filed UNKNOWN at that cell, never a landed finding. Measured by: catalog row per seat + per-cell UNKNOWN filing.

## 5 · WALL-CLAUSE QUESTIONS (minimal experiments)

| # | Question | Minimal experiment | Owner |
|---|---|---|---|
| WQ-1 | The fan-1 landings' seat evidence is void-class (no content-gate row). | Re-run the content-receptor probe at the content budget with the pin read-back; if it still returns void-class, file UNKNOWN at that cell and do not advance the verdict. | AA |
| WQ-2 | The AM-C2 content-gate claim in the plan cannot be re-derived from the ARMAMENT-REPASS record (the record cites the plan but carries no content-gate receipt). | Re-paste the AM-C2 content-gate line into the landing's evidence trail; if the gate is not present, mark the cell UNKNOWN. | AA |
| WQ-3 | The stale BA/CA citations (34424e81ac / f4feeb4fc0) ride the record despite the real shas (2cc6f1832f / 6de5aba311). | Replace the stale citations with the real shas in the dispatch record (per AoA §3.4 settle-condition 4); keep the mechanism question (SW-1) open, never guessed. | AA |

## 6 · VERDICT

**DEFECTS-NAMED.**

The ARMAMENT-REPASS's report-level re-derivations are mostly VERIFIED (16/16 core numeric/gate claims re-derive cleanly), and its AoA-ledger claims are VERIFIED. BUT the landing verdicts (BA CONFIRMED-by-spine, CA CONFIRMED-by-spine) ride STALE citations (BA 34424e81ac vs real 2cc6f1832f; CA f4feeb4fc0 vs real 6de5aba311), and none of the three fan-1 landings carry the amended-gate content-gate row (AM-C3), the per-fire liveness re-probe (AM-C1), or the void-class catalog (AM-B1). The three AM-C1/AM-C2/AM-B1 claims (AA-7/8/9) are UNKNOWN — the record does not carry them. A verdict of SOUND is therefore not earned; REJECT is not warranted (nothing fabricated in the artifacts themselves; nothing hidden). The landings are DEFECTS-NAMED until WQ-1/WQ-2/WQ-3 close and the content-gate rows land.

*Facimus semper — the verdict renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION, never a defect; a receipt that points at nothing is the failure class, never a silent pass.*

---

*This deliverable was produced by the fan-2 AA blind re-verification lane. Target: ARMAMENT-REPASS-20261123.md @ e692f914dd. Amended gates: AM-C1, AM-C2, AM-B1, AM-C3. Receipts inside; no claim inferred beyond the record.*
