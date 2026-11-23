# LANE-BA AUDIT — CROSS-AUDIT LANE B (BRIEF 1)

**Artifact under test:** `plan/tank/lane-b-phase1-design-20261121.md` (canary phase-1 skeleton, rung 1)
**Ground (read cold, in order):** `CANARY-CELLS-20261120.json` · `OPUS-NM3-CANARY-20261120.md` · `PILOT-VERDICT-20261121.md` · `night-20261121/FINAL-LEG-PLAN-20261121.md`
**Audit date:** 2026-11-21 · **Lane:** BA (audit lane B) · **Method:** re-derive every gate/number against the cell ledger (number-seam discipline); wall clause — a non-reproduction is a **QUESTION**, never a defect.

---

## VERDICT LINE

**SOUND** — all 15 items and all 8 gates in the artifact are derivable from, or named-and-tagged for later measurement at, the cell ledger; every numeric claim re-derived from `CANARY-CELLS-20261120.json` matches exactly; revert points R1–R10 are named with triggers and mechanisms; the sole-egress discipline is held (cell `egress_route` = sole route, `egress_bytes` byte-counted, `egress_secondary_downloads` = 0); the judgment layer F1–F5 is consistent with `PILOT-VERDICT-20261121.md` and `FINAL-LEG-PLAN-20261121.md`.

Two **seams named** (defects that do not move the verdict; each revertible):

| Seam | Where | What | Fix (revert) |
|---|---|---|---|
| S1 citation | G6 receipt anchor | "PILOT-VERDICT-20261121.md §2" — that file has **no numbered §2** (headings are unnumbered). The record-first principle is grounded in the cell's own record-first wall clause + `OPUS-NM3-CANARY-20261120.md` §2(1). | Re-anchor G6 to the cell record-first fields and OPUS §2(1); re-run this pass. Gate G6 stays PASS. |
| S2 measurement | G5 / item 6 (sandbox envelope) | G5 PASS-by-assertion from cell `sandbox_env_id` annotation (added `2026-11-20T04:45:00Z`) — the boundary is **named, not measured**; the pilot re-measures at run (carry EXT-2). | Pilot ring-1 measurement of the isolation envelope; verdict row rewritten to PARTIAL iff the measurement fails. |

---

## SEAMS & RECEIPTS — every claimed gate/number traced to source

### G1 — model sha == pinned track-1 sha
- Claim: pin `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` (pinned_repo_sha); safetensors `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c` (model_safetensors_sha256); bytes 641,262,336 (model_bytes).
- Ground: `CANARY-CELLS-20261120.json` lines 3–4, 7–8. **Exact match** ✓
- Verdict: PASS (CONFIRMED).

### G2 — load + minimal forward + determinism
- Claim: load 0.95s (load_seconds); params 319,028,736 (param_count); logits [1,4,129280] (logits_shape); argmax 49969 (argmax_next_token); max abs diff 0.0 (deterministic_max_abs_diff), tolerance 1e-6 → `deterministic_within_tolerance=true`.
- Ground: cell lines 12, 13, 17–21, 9–10. **Exact match** ✓ (transformers 5.23.0 / torch 2.15.0+cpu; native `deepseek_v4` config rejected `compress_ratios=48`, repo-own `code/deepseek_v4` used).
- Verdict: PASS (CONFIRMED).

### G3 — licensing attestation
- Claim: MIT verified live from HF model card; `license_compatible_private_repo=true`.
- Ground: cell line 24 (`license` verbatim) + line 25. **Traceable** ✓.
- Verdict: PASS (CONFIRMED).

### G4 — LFS egress clearance
- Claim: sole route `nm3-canary-r1-20261120`; bytes 647,716,330; secondary 0.
- Ground: cell lines 5, 27–28 (`egress_route` "…sole route"; `egress_bytes`; `egress_secondary_downloads`). **Exact match** ✓.
- Verdict: PASS (CONFIRMED).

### G5 — sandbox env contract
- Claim: `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)`; isolation boundary named; no rig disk state; no prod seat; no HF download in sandbox.
- Ground: cell line 32 (`sandbox_env_id` verbatim) + line 33 (`sandbox_env_id_added_utc` = 2026-11-20T04:45:00Z).
- Verdict: PASS — **by assertion**, i.e. the cell stages the envelope annotation but does not measure it; the pilot re-measures the envelope at run (see EXT-2). Seam S2 named here; the run-time measurement is the fix.

### G6 — record-first five gate fields
- Claim: field mapping unchanged on a second cold re-read; no invention introduced.
- Ground: cell record-first wall clause + `OPUS-NM3-CANARY-20261120.md` §2(1) ("record-first: unreadable = 'not confirmed'") + §7 (field-1 closed head-side only after the cell carried the key, at 04:45Z).
- **Seam S1:** the artifact cites `PILOT-VERDICT-20261121.md §2` — no such section exists (the file's headings are unnumbered: THE VERDICT / THE EVIDENCE TOWER / THE START LINE — LIVE STATE / THE TWO-WAY DOOR). The gate itself stays **PASS**; the anchor is re-mapped to the cell's record-first fields + OPUS §2(1). Reverted: artifact §2 G6 receipt re-written with the re-mapped anchor.

### G7 — verdict row at the named commit
- Claim: R1 LANDED (receipt complete); rung-2 conditions ARMED (defined + ready, never promised).
- Ground: `OPUS-NM3-CANARY-20261120.md` §4 (Verdict) + §6 (Review-loop: no-change re-read ×2, termination satisfied). **Traceable** ✓.
- Verdict: PASS (CONFIRMED).

### G8 — compose-check table
- Claim: all 8 marks FIRED (mark 2 via proxy).
- Ground: `OPUS-NM3-CANARY-20261120.md` §5 (M1–M8, all FIRED, M2 via proxy). **Exact match** ✓.
- Verdict: PASS (CONFIRMED).

### Items 1–15 — traceability to cell ledger
| Item | Claim | Cell field (ground) | Re-derived | Verdict |
|---|---|---|---|---|
| 1 | Rung-1 cell identity + pin | `pinned_repo_sha`, `candidate` | match ✓ | FIRED |
| 2 | Model sha + bytes | `model_safetensors_sha256`, `model_bytes` | match ✓ | FIRED |
| 3 | Load + forward + determinism | `load_seconds`, `param_count`, `logits_shape`, `argmax_next_token`, `deterministic_max_abs_diff`, `deterministic_within_tolerance` | match ✓ | FIRED |
| 4 | Licensing | `license`, `license_compatible_private_repo` | match ✓ | FIRED |
| 5 | Egress single route | `egress_route`, `egress_bytes`, `egress_secondary_downloads` | match ✓ | FIRED |
| 6 | Sandbox env contract | `sandbox_env_id`, `sandbox_env_id_added_utc` | verbatim ✓ | FIRED (by assertion; pilot re-measures at run — SEAM S2) |
| 7 | Record-first wall clause | cell wall clause + OPUS §2(1)/§7 | match ✓ | FIRED |
| 8 | Two-way door / rollback | OPUS §4 | match ✓ | FIRED |
| 9 | Method cards (running) | kit tree: `KIT-METHOD-CARDS-20261121.md` + kit contents | named, stands | NAMED |
| 10 | Improvement-loop honest termination | OPUS §6 + `FINAL-LEG-PLAN-20261121.md` THE ACES-TRIGGER (6h) | consistent ✓ | NAMED |
| 11 | Capture home for the canary | `KIT-METHOD-CARDS-20261121.md` + kit folder (`RELEASE-CONDITION-20261121.md`, `READ-UX-SHAPE-20261121.md`) | named ✓ | NAMED |
| 12 | Fail-safe grid + fold-and-anchor | `FINAL-LEG-PLAN-20261121.md` ARM 6 (judgment layer mechanics in kit) | consistent ✓ | NAMED |
| 13 | Gate-state file (OPEN) | no cell ground — new continuation point | named, not measurable yet | OPEN |
| 14 | Judge-gate (OPEN) | no cell ground — new continuation point | named, not measurable yet | OPEN |
| 15 | Candidate sequence, rung 2 armed | none in ledger — forward item | "V3-3.4B-small, sha 415501bd… — defined + ready, never promised" | OPEN |

### Revert points R1–R10 — triggers and mechanisms, re-verified
R1 no gate-state file → verdict row PARTIAL, re-arm at next ring — matches artifact §3 line 2 ✓.
R2 run fails the first two gates → PARTIAL verdict row, do not advance to ring 2 — matches artifact §3 line 3 ✓.
R3 PR status diverges → branch rebased; the gate-state file points at the PR head — matches FINAL-LEG-PLAN ARM 7-style fold rule ✓.
R4 post lands before run → hold; no execution; release-criteria row in `RELEASE-CONDITION-20261121.md` is the pre-condition, not the signal — consistent ✓.
R5 reply posted but no measurement → no verdict row; wall clause (field recorded "not confirmed" first) — matches cell record-first clause ✓.
R6 held run interrupted → sandbox torn down (already done at 04:41:43Z end per cell); verdict row frozen at PARTIAL; re-arm at next ring — matches artifact §3 line 6 ✓.
R7 gate-state file additive → last PASS revision frozen (committee + operator, per OPUS §4); rewrite rewrites the verdict row — matches artifact §3 line 7 ✓.
R8 transcript asks a question → question answered by who owns the question (operator → the pilot kit is a gate state, not a commitment) — matches PILOT-VERDICT THE TWO-WAY DOOR ✓.
R9 born-out gate schema → the schema is additive and revisioned; the last PASS revision is the rollback point — matches artifact §3 line 7 ✓.
R10 measured plateau (no-change twice) → the improver loop stops and the change is receipted twice over — matches `FINAL-LEG-PLAN-20261121.md` THE ACES-TRIGGER ✓.
Single egress path rule 1–3: sole route `nm3-canary-r1-20261120` (cell `egress_route`), byte-counted `egress_bytes` with `egress_secondary_downloads` = 0 (cell lines 27–28) ✓; rules 4–6 (no prod seat, no HF download in sandbox, no rig disk state) are the cell `sandbox_env_id` text verbatim ✓.

### Judgment layer F1–F5 — consistent with the pilot verdict artifact
- F1 pre-committed verdict vocabulary → PILOT-VERDICT THE TWO-WAY DOOR (gate state, not identity). Consistent ✓.
- F2 out-of-band evaluator's schedule (rings 40–60 min; all landings; before any claim; ACES at 6 h) → `FINAL-LEG-PLAN-20261121.md` ARM 3 + THE ACES-TRIGGER ✓.
- F3 no-gate doctrine (operator word gates the posting surfaces only) → PILOT-VERDICT THE TWO-WAY DOOR ✓.
- F4 fail-safe grid (per-gate revert, freeze) → artifact §3 R1–R10 ✓.
- F5 receipt stamp on every gate row → cell record-first wall clause ✓.

### Egress disposition §4 — sole-route held
Rules 1–3 trace to cell `egress_route`/`egress_bytes`/`egress_secondary_downloads` ✓; rules 4–6 are the `sandbox_env_id` text ✓.

---

## EXTENSIONS — new continuation points (named, measured, revertible)

**EXT-1 — Gate-state file schema (item 13, OPEN).** Draft the schema so the first landing is nameable: `{kit, version, ring, started_at, ended_at, cells_sha256, cells_env: {env_id, added_utc}, items: [{id, state, measured:{}, receipt:{artifact, sha, cmd}}], verdict_rows:[{ring, state, measured:{}, revision}], drifts:[{gate, field, cell_value, brief_value, delta, ts}], closed:[']}`, with `cells_sha256` = `f1ed5b0db75d8d91fe15780a23ea6529d370bdf9e3ad98b26e57787f0d49b536` (cell line 35) as the version anchor. **Measured:** schema derives verbatim from the gate table §1/§2 row format of the artifact + the cell ledger. **Reverted:** additive; the last PASS revision is frozen per R7 — the draft is written to `plan/tank/gate-state-20261121-schema.md`, never to the verdict row.

**EXT-2 — Isolation-envelope measurement (item 6 / G5, SEAM S2).** The pilot's first ring gate measures the named boundary mechanically: `[ -f /tmp/venv/bin/python ] && mountpoint -q /tmp && [ "$(stat -f -c %T /tmp)" = "tmpfs" ]` and a probe for any HF/SAFETENSORS pull from the sandbox (`ss -tn` + `ps` audit during load). **Measured:** cell `sandbox_env_id` names the envelope; the pilot re-derives the measurement at ring 1 and writes it into the verdict row (PARTIAL iff the measurement fails). **Reverted:** additive verdict row; no statement is ever closed by a measurement that wasn't run.

**EXT-3 — Judge-gate re-read cadence (item 15 / thread 5).** First re-read 15 min after the pilot ring closes; then every 2 h (re-grounding cron), each re-read appended as a drift row with the measured cell vs the brief value. **Measured:** drift rows never claims; a drift row is written only when a cell field is absent or a gate number moved. **Reverted:** no drift row is ever a silent correction — every re-read is a named row in the revisioned gate-state file.

**EXT-4 — Egress re-receipt at run (thread 6).** The pilot writes its own one-way receipt (command + sha256 of the pulled safetensors + bytes + secondary=0) into the gate-state file at ring end, citing the cell's `egress_route`/`egress_bytes`/`egress_secondary_downloads` as the reference; any mismatch rewrites the verdict row for G4 to PARTIAL and stops the ring. **Measured:** pilot re-derives sha256 and byte count from the pulled file. **Reverted:** additive receipt row; the cell's numbers are the immutable reference.

---

## OPEN ITEMS — non-reproductions are QUESTIONS, never defects

- **O1 (rung-2 fire):** timing of rung 2 + the gate that fires it are named ("V3-3.4B-small, sha 415501bd… — defined + ready, never promised", artifact §7/§9.1) but have no cell-ledger ground. **QUESTION** for the rung-2 window plan; answered by the next cell, not by this pass.
- **O2 (capture-home exact names):** item 13 says "the kit folder: the four cards + the audit + the sceptic, by exact names". The brief's four-file ground doesn't include the kit tree; from the kit tree, `KIT-METHOD-CARDS-20261121.md`, `KIT-AUDIT-20261107.md`, `KIT-SKEPTIC-20261107.md` sit at the branch root, while `kit/` holds `RELEASE-CONDITION-20261121.md` + `READ-UX-SHAPE-20261121.md`. **QUESTION:** the "kit folder" naming in item 13 maps to the root cards/ and the `kit/` files, not a single folder — corrected by renaming the item (additive rewrite, no verdict change).
- **O3 (EXT-2 result):** the isolation-envelope measurement is not yet run; it is the pilot's first ring gate and is revertible. **OPEN** until the run.

---

## NUMBER-SEAM SUMMARY (verify discipline)

- All 8 gate numbers re-derived from `CANARY-CELLS-20261120.json` match exactly (G1 G2 G3 G4 G5 cells) — no claim failed re-derivation.
- The only non-matching citation in the artifact is **G6's anchor** (S1): `PILOT-VERDICT-20261121.md §2` does not exist as a numbered section; the gate itself passes on the cell record-first clause + OPUS §2(1) + §7. Re-anchored, no verdict change.
- S2 (measurement) and EXT-2–EXT-4 are the pilot-side continuations: named, measured at run, always additive + revisioned.

**END OF DELIVERABLE — `plan/tank/lane-ba-audit-20261121.md`**
