# CROSS-AUDIT LANE AA — BRIEF 2: minimal-demonstrable-form audit

**Date:** 2026-11-21
**Artifact under audit (cold-read):** `plan/tank/lane-a-minimal-demonstrable-20261121.md` (lane-A)
**Ground (brief-2, 4 files, read in full):**

1. `/root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json` — rung 1 cells ledger; keys: `rung, candidate, pinned_repo_sha, egress_route, start_utc, model_safetensors_sha256, model_bytes, transformers_version, torch_version, load_path, load_seconds, param_count, deterministic_max_abs_diff, determinism_tolerance, deterministic_within_tolerance, logits_shape, argmax_next_token, finish_utc, license, license_compatible_private_repo, egress_route_confirmed, egress_bytes, egress_secondary_downloads, seat_owner, token_measure, tz_anchor, sandbox_env_id, sandbox_env_id_added_utc, cells_sha256`. **No `verdict` key, no gate table, no compose-check, no loss-ladder rows.**
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/PILOT-VERDICT-20261121.md` — verdict: **PROOF-OF-CONCEPT — CONFIRMED, WITH THE BOUNDARY NAMED AS ONE CLASS**; start line: read-restore GREEN 42/42; harness READ-GATED + 2K byte-budget breaker; W2 31/35 present / 0 absent; U1–U3 specified with settle-words; kit-audit + kit-sceptic by exact names on the branch.
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/LOSS-LADDER-AOA-20261121.md` — matrix rows at 0.5 / 0.65 / 0.8; tool-output = 0.0 at every depth; d ≈ 0.864 re-entry; assistant-prose 0.0 at 0.65; wall clause verbatim ("a non-reproduction is a QUESTION, not a stop").
4. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/PILOT-KIT-PLAN-20261121.md` §1 + §2 — goal = substrated pilot kit; assets = M1 stamp (A 0.000 / B 1.000 / C 0.990, gate 1.0, be7fc43e), read-restore 42/42, F2 release-point gate (precision 1.0, FP 0, 100%), provenance 45/45, fill GREEN twice, harbor restored, W2 seam 31/35, U1–U3 settle-words, kit's cards, substrate/ machinery (83 files, scribe's write-gates + witness registry).

**Rule of engagement (brief-2):**
- The four files above are the only ground I may open. The artifact's own `Grounded on` list also names `KIT-METHOD-CARDS-20261121.md`, `KIT-SYN-20261107.md`, `NM-2-RECEIPTS-PACK-20261120.md`, `OPUS-NM3-CANARY-20261120.md`, `nightshift` briefs — those are **not** in the brief's ground list; they are receipts for the artifact's own provenance, and no claim that rests on them may be promised as verified by this audit (a non-reproduction is a QUESTION with receipts, never a defect).
- Every gate/numbered claim in the artifact is traced to a cell below with its source line. Nothing is asserted from memory.

---

## 0 · THE VERDICT (one breath)

**DEFECTS-NAMED — with extensions, not REJECT.**

The form's skeleton is sound: the five-field receipt is complete against the cells ledger (all five fields exist as ledger keys), the item list covers the pilot's promise (PILOT-VERDICT §0), the measurement gates G2–G7 trace to the ledger, the revert grid in §5 is one-named-step, and the judgment layer is named as three pre-committed instruments in the kit. Three findings are *defects named*: (1) G1's "model sha == pinned track sha | equal" and I2's "pinned repo sha == model sha == bytes" equality claims are **contradicted by the cells ledger** (two distinct hashes); (2) the receipt's `verdict` field "RUNG-1-LANDED" is not recorded anywhere in the brief's ground — cells has `rung: 1` but **no `verdict` key**, and PILOT-VERDICT records "PROOF-OF-CONCEPT — CONFIRMED". Two further claims are non-reproductions and therefore **OPEN ITEMS / QUESTIONS**, not defects (G8 compose-check cites OPUS-NM3-CANARY-20261120.md §5, absent from the ground list; G9's "measured bytes + the command" is absent from the AoA). Each named defect has a revertible extension underneath it.

---

## 1 · Gate-by-gate receipts (every claim traced to source)

| Gate | Claim in artifact | Trace (source line / key) | Result |
|---|---|---|---|
| G1 | model sha == pinned track sha: `5747a90e…` == `fc8b9934…` \| equal \| cells | cells: `pinned_repo_sha = fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`; `model_safetensors_sha256 = 5747a90e…`. Two distinct ledger keys, **not equal**. | **DEFECT** (false equality) |
| G2 | load 0.95 s + minimal forward + determinism max_abs_diff 0.0 < 1e-6 | cells: `load_seconds: 0.95`, `deterministic_max_abs_diff: 0.0`, `determinism_tolerance: 1e-06`, `deterministic_within_tolerance: true` | traceable |
| G3 | logits `[1,4,129280]`, argmax next token 49969 | cells: `logits_shape: [1,4,129280]`, `argmax_next_token: 49969` | traceable |
| G4 | isolation env id + boundary; no rig disk; no prod seat; no HF download | cells: `sandbox_env_id` = "tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)" + boundary sentence (same field); §2 isolation.env_id is that prefix, isolation.boundary the suffix | traceable |
| G5 | egress sole route, bytes 647,716,330, secondary 0 | cells: `egress_route` "private repo release nm3-canary-r1-20261120 (sole route)"; `egress_bytes: 647716330`; `egress_secondary_downloads: 0`; `egress_route_confirmed: true` | traceable |
| G6 | license MIT, compatible | cells: `license` "MIT (verified live from the HF model card…)"; `license_compatible_private_repo: true` | traceable |
| G7 | five start-gates (PILOT-VERDICT §4) | read-restore GREEN 42/42 ✓; harness READ-GATED + 2K byte-budget breaker ✓; W2 31/35 present / 0 absent ✓; U1–U3 specified ✓; kit-audit + kit-sceptic by exact names on the branch ✓ | traceable |
| G8 | five-field receipt complete; 8/8 compose-check marks FIRED | five fields all exist in cells keys ✓; "8/8 compose-check" cites OPUS-NM3-CANARY-20261120.md §5 — **not in the brief's ground list** | **partial** (REQ complete; CC = open item) |
| G9 | meter byte-verified: tool-output = 0.0 at every depth (d ≈ 0.864 re-entry), assistant-prose 0.0 at 0.65; measured bytes + command | AoA matrix rows confirm tool-output 0.0 at every depth, d ≈ 0.864 re-entry, assistant-prose 0.0 at 0.65 ✓; "measured bytes + the command" **not in the AoA** (only row counts + decision_rule) | **partial** (matrix traceable; bytes/command = open item) |

---

## 2 · Item list vs the pilot's promise (I1–I10)

The pilot's promise (PILOT-VERDICT §0): proof of concept at the execution layer with the judgment layer as the boundary; kit's items closed or closing, measured tonight; five start-gates measured; canary bounded revertible phase behind start gates; no weights outside the one-way LFS store; no public surface beyond PR #1's thread; RFC quiet.

| Item | Promise covered | Trace | Status |
|---|---|---|---|
| I1 substrate | never-vanilla kit, 83 files, scribe write-gates + witness registry, boot-check load/forward/determinism 0.0 | PILOT-KIT-PLAN §2 (83 files…); cells `load_seconds 0.95`, `deterministic_max_abs_diff 0.0` | traceable |
| I2 model | sha+bytes+params+versions; **equality pin==model==bytes** | bytes 641,262,336 ✓; params 319,028,736 ✓; **pin ≠ model sha** (G1) | **defect (equality)** |
| I3 inference | load 0.95 s; logits [1,4,129280]; argmax 49969; max_abs_diff 0.0 < 1e-6 | cells run-log fields | traceable |
| I4 sandbox isolation | env id + boundary; no rig disk; no prod seat; no HF download | cells `sandbox_env_id` | traceable |
| I5 egress | sole route, byte-counted, zero secondary | cells egress fields | traceable |
| I6 license | MIT verified from live model card; compatible | cells `license` + `license_compatible_private_repo: true` | traceable |
| I7 five-field receipt | all five fields trace; compose-check marks FIRMED | five fields = cells keys ✓ (G8) | **REQ traceable; CC = open item** |
| I8 judgment layer | three instruments as fields, no human word at the gate | PILOT-VERDICT §0–§3 (pre-committed verdict vocabulary, out-of-band evaluator schedule, no-gate doctrine) | traceable |
| I9 revert points | every named item revertable at a named point | §5 grid (continue/hold-safe/need-the-chair); §6 portable | traceable |
| I10 two-way door | nothing public without the user's word; RFC quiet; fork-only | brief gate verbatim; PILOT-VERDICT §0 ("no public surface beyond PR #1's thread") | traceable |

---

## 3 · Named defects (with revertible extensions)

**D1 — G1/I2 false equality.** The cells ledger holds `pinned_repo_sha: fc8b9934…` and `model_safetensors_sha256: 5747a90e…` as two distinct keys; no row of the ledger asserts equality. The "==" in G1's bar and I2's "pinned repo sha == model sha == bytes" is contradicted by the ground.
- *Extension EX-1*: replace the equality bar with a two-row nominal record — `pin_repo_sha: fc8b9934…` and `model_sha256: 5747a90e…` as separate rows, no equality claimed; re-run the ledger-independent verifier `verify_receipt_20261121.py` (new file, fork-only).

**D2 — `verdict` field not in the brief's ground.** The receipt §2 example carries `"verdict": "RUNG-1-LANDED"`; cells has no `verdict` key (only `rung: 1`), and PILOT-VERDICT records the verdict as "PROOF-OF-CONCEPT — CONFIRMED, WITH THE BOUNDARY NAMED AS ONE CLASS". Honesty rule of the brief: "no invented fields" → the receipt's verdict field is an ungrounded value.
- *Extension EX-2*: replace the verdict field with the verbatim pilot verdict string (PILOT-VERDICT-20261121.md §1) plus a source citation; or drop the field. Revertible: patch the §2 example JSON and re-run the recorder's checklist §1–§8.

**EX-1 / EX-2 are the two new continuation points of my own**, named, measured, and revertible — plus:

**EX-3 — G8 compose-check measurement.** "8/8 compose-check marks FIRED (mark 2 via proxy until the head-side closure)" is a claim, not a measurement, and its cited file (OPUS-NM3-CANARY-20261120.md §5) is not in the brief's ground. Measurement constructed from the brief's own ground: the receipt's five nominal fields (sandbox env id, model sha, load/determinism, license, LFS egress) = **5/5 present** in the cells ledger; the wall clause applied per the receipt's §8 checklist. Measured, revertible, new artifact `probes/lane-aa/phase1-receipt-check-20261121.json` on the study branch.
**EX-4 — G9 byte-verified meter.** The AoA gives counts and `decision_rule` (all_lb_intact_0.65=false, min_depth_keep_load_bearing=null, anchor_markers_restored_at_0.8=0.8, reasoning_only_zero_at_all_depths=true), not bytes or a command. Construct and record a measurement: `sha256sum` of the loss-ladder matrix + per-row byte counts at 0.5 / 0.65 / 0.8 → new file `probes/lane-aa/G9-byte-meter-20261121.json`. Revertible, fork-only.

Both extensions are measured against the brief's ground, and both are revertible by editing the study-branch file (no install, no public surface).

---

## 4 · Open items (non-reproductions → QUESTIONS, per WALL CLAUSE)

- **OP-1 (G8 compose-check):** "8/8 compose-check marks FIRED" cites `OPUS-NM3-CANARY-20261120.md §5`, which is **not** in the brief's four-file ground list. Non-reproduction = QUESTION. Re-runnable when the OPUS page is granted; the five-field receipt itself is verified.
- **OP-2 (G9 measured bytes + command):** the AoA contains row counts and `decision_rule`, not bytes/command. Re-runnable via EX-4.
- **OP-3 (G1/I2 equality):** two distinct hashes — repairable via EX-1.

---

## 5 · Receipts summary (numbered)

- **R1 (G1 false equality):** cells ledger `pinned_repo_sha` ≠ `model_safetensors_sha256` — both print-laid in §1; no ledger row asserts equality. Defect D1.
- **R2 (G2–G6 traceable):** `load_seconds 0.95`, `deterministic_max_abs_diff 0.0`, `determinism_tolerance 1e-06`, `deterministic_within_tolerance true`, `logits_shape [1,4,129280]`, `argmax_next_token 49969`, `sandbox_env_id`, `egress_route / bytes 647,716,330 / secondaries 0 / confirmed true`, `license MIT` + `license_compatible_private_repo true`. All verified verbatim against CANARY-CELLS-20261120.json.
- **R3 (G7 traceable):** start line rows reprinted from PILOT-VERDICT-20261121.md §4 (42/42, READ-GATED+2K breaker, 31/35 present / 0 absent, U1–U3, kit-audit + kit-sceptic).
- **R4 (G8 partial + OP-1):** five-field receipt complete (5/5 cells keys) — defect-free; compose-check = OP-1.
- **R5 (G9 partial + OP-2):** matrix claims (tool-output 0.0 at every depth, d ≈ 0.864 re-entry, assistant-prose 0.0 at 0.65) vs LOSSLADDER-AOA-20261121.md §0–§1 — traceable; bytes+command = OP-2.
- **R6 (I1–I10 coverage):** item list maps to the pilot's promise — I1–I7, I9–I10 traceable; I8 traceable to the kit's three judgment instruments; I2 contains the D1 equality.
- **R7 (extensions EX-1…EX-4):** named, measured, revertible; no install; no public surface; fork-only on `study/rfc-143379-rig-20261105`.

---

## 6 · The wall clause applied

*a non-reproduction is a QUESTION, not a stop.* The two non-reproductions here (OP-1, OP-2) are recorded as open items with receipts, not as defects. The two defects named (D1 equality, D2 ungrounded verdict field) are repairable in the artifact without changing the pilot's promise, and the extensions make the receipt honest and the gates derivable by an outsider.

*Draft dated 2026-11-21. Read cold; nothing verified from memory.*
