# NEMO-COPYCAT READ-20261114.md
**One-line summary:** *CONVERGENT on the read-restore spine, DOOR-STATE reversibility, and fail-safe dispositions; DIVERGENT on free-seat rotation math, crons' post-update race, and the `drop/` read-root bridge; GAPS: NIGHTSHAPE omits the `REFS` convention, SUBSTRATE-COMPARISON lacks harness hardened transport's smoke-cert details; COPYCAT INDEPENDENT: the operator's one-paragraph gift on unbounded-transcript design.*

---

## Agreement/Divergence Table
| **Topic**                          | **NIGHTSHAPE**                          | **SUBSTRATE-COMPARISON**               | **Verdict**                     | **Receipts**                                                                                     |
|------------------------------------|----------------------------------------|----------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------|
| **Read-restore spine**             | Core mechanism (R1 decision-prep).     | Core mechanism (act-as-if substrate). | **CONVERGENT**                   | NIGHTSHAPE §1, SUBSTRATE-COMPARISON §1.1.                                                                 |
| **Door-state reversibility**       | Fail-safe dispositions (AUTO-CONTINUE). | Two-way doors (undo named).           | **CONVERGENT**                   | NIGHTSHAPE §4, SUBSTRATE-COMPARISON §3.                                                                 |
| **Free-seat rotation math**        | Fair-share rest (3 long-haul seats).    | Fair-share rest (3 long-haul seats).   | **DIVERGENT-NAMED**             | NIGHTSHAPE §2 (solar/longcat/stepfun), SUBSTRATE-COMPARISON §2.1 (no explicit rotation math).       |
| **Crons' post-update race**        | No post-update checklist.              | Post-update checklist **OWED**.        | **DIVERGENT-NAMED**             | THINK-TANK §3.4 (G12), SUBSTRATE-COMPARISON §2.1 (no mention).                                    |
| **`drop/` read-root bridge**       | Kenari READ-ONLY (no `drop/` access).   | `drop/` **OWED** (head-side).          | **DIVERGENT-NAMED**             | THINK-TANK §3.2 (G8), SUBSTRATE-COMPARISON §1 (no bridge).                                       |
| **Harness hardened transport**     | Hardened transport (G6/G7/G13).        | Hardened transport **smoke-certified**.| **GAP**                         | R4-GROUND §3 (smoke-cert), NIGHTSHAPE §1 (no smoke-cert details).                              |
| **`REFS` convention**              | No `REFS` convention.                  | `REFS` convention **standing**.       | **GAP**                         | SUBSTRATE-COMPARISON §1, THINK-TANK §3.1 (G2/G9).                                                 |

---

## Cross-Gaps
1. **NIGHTSHAPE omits the `REFS` convention**:
   - SUBSTRATE-COMPARISON explicitly names `REFS` as the grounding realm (§1), but NIGHTSHAPE does not reference it.
   - **Evidence**: THINK-TANK §3.1 (G2/G9), SUBSTRATE-COMPARISON §1.

2. **SUBSTRATE-COMPARISON lacks harness smoke-cert details**:
   - R4-GROUND confirms the harness is smoke-certified (G6/G7/G13), but SUBSTRATE-COMPARISON does not mention the md5 or backups.
   - **Evidence**: R4-GROUND §3, NIGHTSHAPE §1 (no smoke-cert).

---

## Copycat’s Independent Apex Read
**The operator’s one-paragraph gift on unbounded-transcript design**:
The day’s failures trace to a single design shape: the small-seat bridge’s unbounded transcript. The team treated the endpoint’s 131K cap as the only budget, while claims were dressed as receipts, early commits were treated as finish lines, and reads were scattered without a skeleton. This design geometry must be hardened with:
- **G6**: Transcript-budget breaker (truncate/summarize history at 131K).
- **G7**: Single-call + response-integrity enforcement.
- **G12**: Post-update background-task checklist (auth.json + cron re-fire + harness md5).

**Evidence**: THINK-TANK §3.5 (operator-gift), R4-GROUND §3 (G6/G7/G13 installed).

---

## Compose-Check Table
| **Metric**                          | **Status**                     |
|-------------------------------------|---------------------------------|
| **Seats alive at each fold**        | CONFIRMED (solar/longcat/stepfun).|
| **Runner-idle-zero checks**         | CONFIRMED (pve1/c0wb0y/p0tat0). |
| **Free-quota headers at fire-time** | CONFIRMED (opencode/kilo).       |
| **Batch honesty**                   | **NO-IMPROVEMENTS**             | The night’s failures are design geometry, not batch issues. The operator’s gift (unbounded-transcript) is the next mechanism.

---

**Loop-state line**: `NO-IMPROVEMENTS + confirmation` → **NEXT MECHANISM**: *harden the unbounded-transcript design with G6/G7/G12.*