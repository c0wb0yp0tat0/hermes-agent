# STAGE-PLAN-SEQUENCE-20261123 — sequencing and close-out plan

*Planner: PLANNER-4 · slice 4/4 · 2026-11-23. PLAN ONLY: no lanes dispatched, no probes/batteries run, no verdicts rendered, no compose/seal/lens performed. The proxy approves or reloops.*
*Scope: end-to-end sequencing from the three cross-audit landings through AoA, gather, OPUS composition, seal, and operator lens. Study paths only; local reads only; nothing public; RFC #143379, #5320, and #157065 remain quiet; no installs; never push.*

## 1. Planning basis and limits

This sequence uses the stage's named cross-audit contract: three independent audit lanes (BA, AA, CA), each with a named artifact and landing receipt; an AoA blocked on verified landings; nine verification axes; weighted convergence with divergence retained as signal; and a held launch package for the gather. The lane artifacts are inputs, not findings of this plan. This plan issues no audit verdict.

**Input-read limitation:** the required local inputs include `plan/tank/briefs/CROSS-AUDIT-BRIEFS.md`, `STAGE-PLAN-CROSSAUDIT-20261123.md`, `STAGE-PLAN-FLEETMATRIX-20261123.md`, `STAGE-PLAN-BATTERIES-20261123.md`, and `plan/RECORD-MINE-20261121.md`. The tool's read gate opened before the fleet-matrix, batteries, and record-mine contents could be read in this pass. Accordingly, no claims about their detailed contracts, receipts, or mine-derived findings are represented here as verified. The proxy must reconcile this sequence with those source artifacts before execution; unresolved differences become named seams, not silent assumptions. No execution is authorized by this document.

## 2. End-to-end sequence: named acts and receipts

All gates are fail-closed. A receipt records the actual artifact/path, content digest or commit where applicable, timestamp/window, responsible role, status, evidence pointers, and explicit unknowns. A dashboard/card is a mirror, not evidence. Do not fabricate missing fields; mark them UNKNOWN and retain their gate.

| Order | Named act | Inputs and gate | Output / required receipt |
|---|---|---|---|
| 0 | **GROUND-AND-CONTRACT RECONCILIATION** | Read the cross-audit brief, all three plans, the record-mine, and the lane deliverables/contracts in full. Compare this sequence against each. Enumerate exact pins, paths, owners, limits, and any split-read manifest before dispatch. | Reconciliation ledger: source path + digest/commit + read status; contract deltas; source-to-step map; staged-read splits; unresolved questions and owner. No downstream act starts with an unclosed material contract conflict. |
| 1 | **THREE-LANE FAN** | BA, AA, CA each receive their own blind brief and full ground set, exact pinned designation/host per the fleet plan, and the applicable time-box. Parallel only after independent base/host and dispatch gates pass. Each lane audits its assigned artifact cold; no lane sees another's draft finding. | Three distinct landing packages at their specified paths: verdict, re-derivable receipts, asserted→status→basis table, extensions, wall-clause QUESTIONS with minimal experiments, unverifiable list, commit SHA, and evaluator row. A missing or malformed package is not a landing. |
| 2 | **LANDING VERIFICATION / FREEZE** | Verify each lane's session/run identity, actual artifact existence and content, commit/tree inclusion, reported SHA, verdict, required receipt fields, and applicable one-run-per-pin rule. Preserve each finding as landed; do not permit self-amendment. | Three independently checked landing rows, or explicit held rows (PARTIAL/GAP/UNKNOWN) with evidence and next action. Freeze hashes and versions used by downstream adjudication. |
| 3 | **AoA HOLD** | AoA remains BLOCKED until all three lane landing gates pass. A verdict, status-board update, or dispatch completion alone does not pass this gate. | Hold record naming each input artifact/hash and its gate state. If any is absent, no AoA firing. |
| 4 | **AoA NINE-AXIS ADJUDICATION** | Once all three verified landings exist, an adjudicator on the required independent base applies COVERAGE, VERDICT-CONSISTENCY, EVIDENCE-REALITY, BASE-INDEPENDENCE, VOICE-CHECK, HARD-LINES, OPEN-ITEMS, EMISSION, and REGURGITATION-DIAL. Re-derive from receipts; do not trust assertions or average disagreement. | AoA artifact with per-lane/per-axis asserted→status→basis and evidence links; consolidated stack verdict; every divergence/seam; settle-conditions; shared-route/base constraints; explicit UNKNOWNs; versioned input manifest. This is the decision record, not the gather or court document. |
| 5 | **GATHER RECEIPT CONSOLIDATION** | Requires the AoA artifact plus the approved fleet plans, all verified lane findings, and battery receipts/requirements. Inventory each expected source against the reconciled source manifest. A battery marked UNKNOWN is not converted to PASS; missing receipts remain visible. | Gather index and immutable package: source manifest with paths/hashes/commits; fleet-plan records; lane receipts; battery matrices/raw receipts and statuses; AoA; discrepancy/UNKNOWN register; completeness check. Each item is linked, not paraphrased in place of its evidence. |
| 6 | **GATHER ACCEPTANCE GATE** | Independent check that every required source is present, identity-consistent, readable, in-scope, and status-labeled; no unsupported claims or vanished disagreements. | Signed/attributed acceptance row with enumerated inventory, omissions, repair owners, and gate decision. OPUS composition waits for acceptance or an explicitly approved, bounded composition scope that visibly marks exclusions. |
| 7 | **OPUS-COMPOSE** | Compose only from the accepted gather package and its manifest. Keep evidence, analysis, recommendation, and decision distinct. Do not invent details, merge away dissent, upgrade UNKNOWN, or treat the plan as an execution report. | Court-document draft with source citations to gathered artifacts, decision and conditions, dissent/seams, exclusions, and traceability map back to the gather. Draft digest and composition receipt identify the exact gather version. |
| 8 | **COMPOSE-CHECK / RECONCILE** | A reviewer other than the composer checks every material claim against the gather, verifies citations/identifiers, tests that minority findings and unresolved questions remain represented, and checks hard lines/public-surface restrictions. | Claim-to-source matrix, corrections, reviewer identity, draft digest, and PASS/RETURN decision. Returned drafts go to the composer; new evidence goes through the seam loop below, not an inline unsupported patch. |
| 9 | **SEAL-CERTIFICATION** | Only a compose-check PASS on a fixed document and accepted gather version permits sealing. Certify identity, integrity, provenance, scope, required approvals, and quiet/publication boundary. The seal is a certification step, not publication authorization. | Sealed artifact plus certification receipt: artifact path and digest, gather/AoA/lane input digests, signer/role and time, checks performed/results, exceptions, seal/version identifier. Any missing approval or failed integrity check blocks sealing. |
| 10 | **OPERATOR LENS / READ DIGEST** | Operator-facing digest is generated from the sealed artifact only, at the approved audience boundary. Its cadence and door schedule are confirmed with the operator during gate 0; absent that source instruction, no cadence or audience is presumed. | Lens digest with sealed-source digest, generation time, intended audience, concise decision/conditions, material uncertainty/divergence, next review/door time, and omitted-detail pointer. Verify it does not introduce claims absent from the seal. |
| 11 | **CLOSE-OUT / ROW** | All preceding receipts exist and reconcile; no open blocker is mislabeled resolved. | Append-only close-out row: final state, artifact inventory/digests, gate-by-gate result, outstanding questions and owners, next decision/door, provenance, and explicit statement that no public release or execution occurred unless separately authorized. |

## 3. Gate map and dependency graph

```text
GROUND-AND-CONTRACT RECONCILIATION
        └──> dispatch readiness ──> BA ─┐
                                  ├──> AA ├──> landing verification / freeze
                                  └──> CA ┘            │
                                                       ├── all three pass ──> AoA
                                                       │                       │
                                                       │                       v
                                                       └── any hold ──> remain blocked
                                                                               │
 AoA + fleet plans + batteries + all lane receipts + source manifest ──> GATHER
                                                                            │
                                                                  gather acceptance
                                                                            │
                                                                    OPUS-COMPOSE
                                                                            │
                                                                    COMPOSE-CHECK
                                                            fail/return ─────┴── pass
                                                                                │
                                                                        SEAL-CERTIFICATION
                                                                                │
                                                                         OPERATOR LENS
                                                                                │
                                                                         CLOSE-OUT ROW
```

**Strict dependencies:** ground reconciliation before dispatch; each landing before AoA consumption; all three verified landings before AoA; accepted AoA and complete/explicitly scoped source inventory before gather acceptance; gather acceptance before composition; independent compose-check before seal; seal before operator digest; all receipts before close-out. No downstream step may infer an absent upstream receipt.

**Parallel work:** the three audits may run concurrently after their individual dispatch gates. Independent battery work may run concurrently only if its approved battery plan specifies distinct inputs/owners and does not consume mutable lane findings; its receipt joins the gather only after verification. Gathering is assembly after inputs are fixed, not a parallel reinterpretation. Compose, seal, and lens are sequential.

## 4. Time-boxes and cadence

- **Preflight:** one bounded planning ring to read/reconcile all inputs, settle paths/pins/roles, and schedule doors. If any contract is unavailable, record the blocker and stop at preflight.
- **Audit fan:** one concurrent window, maximum 60 minutes per lane as specified by the cross-audit contract; each lane has its own receipt. An unfinished lane is held and re-armed in a new approved window with its partial frozen, never silently skipped or changed mid-run.
- **Landing verification:** one bounded review window immediately after the fan; any failed identity/content check blocks AoA.
- **AoA:** next available ring only after all three verified landing rows. Reserve a separate adjudication window; do not overlap with mutable lane work.
- **Batteries and gather:** follow the batteries plan's approved matrix and time-box, once reconciled. Parallel battery windows are permitted only as specified there. Gather begins after battery receipts and all source versions are fixed; use one consolidation ring plus one independent acceptance check.
- **Compose and close-out:** separate bounded windows for OPUS composition, independent check/revision, seal certification, and lens generation. Do not compress away any gate to meet a clock. An overdue item becomes an explicit held state with next owner/window.
- **Cadence / door schedule:** no hourly, six-hour, or other operator cadence is adopted by this plan without confirmation against the fleet/battery contracts and record-mine. At preflight, the operator records the digest cadence and the door schedule (who may receive/read it, and when); changes require a versioned receipt. A cadence trigger is not permission to publish.

## 5. Failure classes and sequence response

| Failure class | Required response / gate effect |
|---|---|
| **Lane divergence** | Preserve each lane's verdict and evidence. AoA names the claim, competing bases, and resolution/settle-condition. Weighted convergence is not majority voting; disagreement is never edited out. If evidence cannot settle it, carry it as an explicit seam and constrain the consolidated decision. |
| **Battery UNKNOWN / missing / partial** | Retain UNKNOWN (or the battery plan's precise partial state), include raw available evidence and reason, name owner and smallest next test. Do not coerce to PASS/FAIL. Hold any gather/composition decision whose required condition depends on that battery, unless a formally bounded exclusion is approved and made conspicuous. |
| **Missing lane, malformed artifact, or unverified commit** | Landing gate fails; AoA remains BLOCKED. Correct/complete in an approved new leg. A board status or self-report is not evidence. |
| **Read-cap / missing source** | Split the source during staging, record ranges/manifest, and finish reading before dependent work. If unavailable, mark preflight blocked; do not infer its terms. |
| **Base/pin collision or channel dark** | Follow the reconciled fleet contract; record exact designation, pivot, host, and independence limitation. A shared route is named, never silently passed. No repeated pin run without its defined independent re-derivation gate. |
| **Non-reproduction / wall hit** | File as a QUESTION with observed condition, raw receipt, smallest experiment to move the wall, and owner. It is neither a negative verdict nor permission to stop without the question; re-arm only through the approved sequence. |
| **Receipt-number / identity seam** | Hunt the raw source, compare identifiers and digests, retain both conflicting values until reconciled. If unresolved, mark UNKNOWN and keep the dependent gate closed. |
| **Emission fragment / absent artifact / phantom board state** | Not landed. Require the on-disk artifact, content checks, and commit/tree verification. Do not use exit code, notification, or board column alone as proof. |
| **Compose claim without source / lost dissent** | Return for correction. The source-to-claim matrix must identify evidence or label the assertion as inference/unknown; divergence is restored, not smoothed. |
| **Seal integrity, approval, or audience-boundary failure** | No seal and no lens. Preserve draft and failure receipt; remediate under a new versioned gate. Never disclose internal material to an unauthorized surface. |
| **New finding at any stage** | Stop affected downstream progression. Re-enter plan → owner/head decision → appropriate audit/battery leg → cold verification → amended version; do not inline-patch an executor's result or mutate a frozen input. |

## 6. Converge-contract and close-out forms

### Lane-to-AoA contract
Each lane supplies one frozen, addressable package: exact artifact path and digest; commit SHA; pin/host identity as permitted by its contract; verdict; command/receipt evidence and evaluator row; asserted→status→basis; required extensions; explicit unverifiable items; wall-clause QUESTIONS and minimal experiments. AoA records which package/version it consumed. Any absent field is UNKNOWN, not filled from memory.

### AoA-to-gather contract
AoA delivers nine-axis adjudication, per-lane findings, consolidated stack verdict, named dissent/seams, settle-conditions, and the held launch package. Gather inventories all required fleet plans, audit findings, and battery receipts by stable path/digest/status. It does not rewrite source evidence. Missing, duplicate, stale, or conflicting inputs appear in a discrepancy register and hold acceptance unless explicitly excluded by an authorized decision.

### Gather-to-OPUS contract
OPUS receives the accepted gather version and a claim-source map. Each material conclusion is traceable to one or more receipts; inference is labeled; UNKNOWN and divergence remain legible. The composition states decision scope and conditions, not unperformed work. A new source after acceptance invalidates the affected composition inputs and triggers re-gather/re-check.

### Seal and lens contract
Seal certifies the exact checked document against exact gathered inputs and named approvals; it does not publish or broaden audience. The lens digest references that seal's digest, states the operator decision, conditions, unknowns, and next door, and carries no unsupported detail. Operator-directed cadence and audience are explicit receipt fields, not planner assumptions.

### Close-out receipt
One append-only row includes: stage identifier/version; each act's status and evidence pointer; input/output paths and digests; commits; owners and timestamps; gate decisions; all UNKNOWNs, divergences, exclusions, and open QUESTIONS with owners/next dates; seal identifier; lens source digest/cadence/audience; and a no-publication/no-execution attestation where true. Close-out is complete only when every required step is either passed or explicitly held with an accountable next action; a held stage is not represented as complete.

## 7. Planning principles considered

Relevant standing-harvest ideas are considered only as corroboration, not adopted as implementation: write-gated sequencing and read-path discipline; evidence-gated admission/commit gates; read-side evidence verification; fidelity appropriate to the decision; and stage-decoupled evaluation. They do not override the source contracts, local evidence, operator authorization, or this plan's fail-closed gates. No mechanism is claimed to have run or been installed.

## 8. Approval boundary

This is a sequencing plan only. It authorizes no dispatch, audit, battery run, compose, seal, public disclosure, or RFC activity. The next mechanism is proxy review against the un-read fleet-matrix, batteries, and record-mine sources, followed by explicit approval or reloop. Any discrepancy is recorded and resolved before the affected gate opens.

*Facimus semper — receipts first; divergence visible; no gate passed by implication.*
