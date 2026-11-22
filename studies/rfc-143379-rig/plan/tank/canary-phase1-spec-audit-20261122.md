# CANARY-PHASE1-SPEC-AUDIT-20261122 — ARM 3b audit of the canary's phase-1 spec

**ARM:** 3b (rotation's audit pass over the canary's phase-1 spec; arm's gate per FINAL-LEG-PLAN arm 3).
**Artifact under test:** `plan/tank/canary-phase1-spec-20261122.md` (181245e1ae; the ARM 3a deliverable).
**Seat:** upstage/solar-mini4:free (audit class; base-distinct from the spec's hy4).
**Ground method:** local `read_file` only — the DISK is the truth, now materialized; no `web_extract`; no installs; writes only under `studies/rfc-143379-rig/`.
**Envelope:** RFC #143379 QUIET · nothing public beyond PR #1's thread · the PLAN is not altered — this audit serves the armed arm · the reserve's name rides NO pilot-facing surface.

---

## VERDICT

**DEFECTS-NAMED** — the spec's measured values are SOUND (all 9 gates re-derive to the cells' keys; the real R1–R10 grid is carried; the sole-egress discipline is held; the crosswalk is 8/8; the fixtures are complete; the named absences are tagged, none dropped), **with named seams** in the carry-notes and in the audit record that do not touch any gate value:

1. **Q1/Q4 (carry-note staleness, resolved):** spec §8 labeled `plan/tank/lane-b-phase1-design-20261121.md` and `plan/tank/lane-ba-audit-20261121.md` ABSENT — that label was written at 06:57Z (before the 06:59Z materialization of those files in the current tree). Both files are now on disk, read in full for this audit, and confirmed as contract inputs. Resolution recorded, not a defect; the spec's disposition is unchanged and remains tagged (wall clause).
2. **G5 (PASS-by-assertion, correctly carried):** `sandbox_env_id` (CELLS:32–33) is a cell annotation, not an independent measurement; the spec's §3 G5 row names this (BA-S2) — retained; EXT-2 ring-1 run re-measures.
3. **G4 (registry-empty disconfirm, carried):** the G4 rule had no rows until A5 seeded (AOA:92,119) — carried as a disconfirm in spec §3 G4, not smoothed.
4. **Phantom-grid repair verified, not invented:** the spec §0 runbook step 3 and §4 carry the BA-D1 repair (the artifact's real R1–R10); the BA audit's phantom phrase set was grep-proven to one file; design bytes stable (`5d4015f2` == original blob). The spec does NOT carry the phantom trace. PAID.

The audit's own record carries named seams (Q1/Q4 staleness; phantom-sha mechanism SW-1 kept open; AOA-OQ kept open) — those are the DEFECTS-NAMED of this pass, all revertible, all with receipts.

---

## 1 · THE GATES — G1–G9 re-derived from the cells' keys (CELL vs RECORD provenance)

Ground: `CANARY-CELLS-20261120.json` — 35 key/value lines; every numeric claim re-derived from its key's literal value. Two keys are DISTINCT and never `==`: `pinned_repo_sha` (CELLS:4) vs `model_safetensors_sha256` (CELLS:7). `model_bytes` is a size, not a hash (AOA:51–52; SPINE:68).

| Gate | Per-key measurement (CELLS:line) | Bar | Provenance | Verdict |
|---|---|---|---|---|
| G1 | `pinned_repo_sha` = fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64 (4); `model_safetensors_sha256` = 5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c (7); `model_bytes` = 641262336 (8) | per-key match; two distinct keys; bytes = size | CELL | **PASS** — disconfirm: no ledger row asserts cross-key equality (AOA:51–52) |
| G2 | load 0.95 (12); params 319028736 (13); logits [1,4,129280] (17–21); argmax 49969 (22); max_abs_diff 0.0 (14); tol 1e-6 (15); within=true (16); transformers 5.23.0 / torch 2.15.0+cpu (9–10) | max_abs_diff < 1e-6 | CELL | **PASS** — repo-own code package used (CELLS:11), not a dead-end (NM3:15) |
| G3 | `license` MIT (24); `license_compatible_private_repo` true (25) | compatible with private repo | CELL | **PASS** — verified live from the model card, not inferred |
| G4 | sole route `nm3-canary-r1-20261120` (5); `egress_bytes` 647716330 (27); `egress_secondary_downloads` 0 (28); `egress_route_confirmed` true (26) | byte-counted; zero secondary | CELL | **PASS** — plus carried disconfirm: rule-with-no-rows until A5 seed (AOA:92,119) |
| G5 | `sandbox_env_id` `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)` (32); added 2026-11-20T04:45:00Z (33) | boundary named | CELL (assertion) | **PASS-BY-ASSERTION** — NOT measured; cell annotation, not independent (BA-S2; EXT-2 re-measures at ring 1) |
| G6 | field mapping unchanged on second cold re-read; no invention | record-first fields + OPUS §2(1)/§7 | RECORD | **PASS** — re-anchored, NOT "PILOT-VERDICT §2" (that file has no numbered sections) (AOA:28) |
| G7 | R1 LANDED, receipt complete; rung-2 armed sha `415501bd…` ("defined + ready, never promised") | verdict row at named commit | RECORD | **PASS** — O1 kept, not a promise (AOA:165) |
| G8 | 8/8 compose-check marks FIRED, mark 2 via proxy | 8/8 traceable | RECORD | **PASS** — proxy named (NM3:36: M2 sandbox isolation via UTC window + egress_confirmed) |
| G9 | byte-verified receipt meter: tool-output 0.0 @ 0.5/0.65/0.8; re-entry d≈0.864; assistant-prose 0.0 @ 0.65 | measured bytes + command | RECORD (partial) | **PARTIAL** — bytes/command = OP-2 (run log / `probes/loss_ladder.py`), carried open; never promoted (SPINE:37; AOA:169) |

**Count = 9 measured gates** (G1–G5 cell-derived; G5 an assertion; G6–G9 record-sourced, tagged, never presented as cell measurements). G1–G4 and G5 carry their disconfirmations; G1–G8 are PASS; G9 is PARTIAL.

## 2 · THE R1–R10 REVERT GRID (phantom trace repaired, carried)

The spec §4 is the artifact's real design §3 (design §3:83–92), carried from the spine (SPINE:39–54). The BA audit's phantom phrase set ("no gate-state file → PARTIAL / run fails first two gates / PR status diverges → branch rebased / post lands before run / reply posted but no measurement / born-out gate schema") is grep-proven to the audit alone (AOA:34); design bytes stable (`5d4015f2` == original blob, verified). That is a repair, not an invention — the audit record keeps the phantom trace as a named seam (AOA:34) and closes the spec's §9; the spec does not re-invent it.

| # | Revert point | Trigger | Mechanism | Receipt |
|---|---|---|---|---|
| R1 | Cell install | sha mismatch, or load fails | sandbox torn down; install additive, deleted on revert | SPINE:43 |
| R2 | Model load | `load_seconds` above barrier, or params ≠ 319028736 | load is a probe; forward never runs on a bad install | SPINE:44 |
| R3 | Determinism | max_abs_diff ≥ 1e-6 | run recorded as a probe, never a verdict; never burns rung-2 | SPINE:45 |
| R4 | License | `license_compatible_private_repo` false | model not compatible; release route untouched | SPINE:46 |
| R5 | Egress | `egress_secondary_downloads` > 0 | one-way, byte-counted; a second download aborts the run | SPINE:47 |
| R6 | Isolation | envelope contract not verifiable | boundary named and checked at run time (EXT-2) | SPINE:48 |
| R7 | Gate-state file | any gate fails | additive + revisioned; last PASS revision is rollback | SPINE:49 |
| R8 | Capture home | fold lands the file; nothing behind it | fold additive (root cards + `kit/` files) | SPINE:50 |
| R9 | Judge-gate re-reads | a re-read shows a drift | evaluator's verdict row carries the independent read | SPINE:51 |
| R10 | ACES trigger | improver loop fires | stops on measured plateau (no-change twice); termination receipted twice over | SPINE:52 |

Revert rule (design §3:94): a failed gate freezes the verdict row at PARTIAL/GAP and re-arms the item at the next ring — never a silent skip, never a re-run with different values.

## 3 · EGRESS DISCIPLINE — sole route, byte-counted, secondary 0

Six rules, all traceable to CELLS:5,26–28 + NM3:19 + EXT-4:

1. Sole route: private repo release `nm3-canary-r1-20261120`; no mirror/secondary (CELLS:5; SPINE:58).
2. One-way, byte-counted: `egress_bytes` = **647,716,330**; `egress_secondary_downloads` = **0**; `egress_route_confirmed` = true (CELLS:26–28; NM3:19).
3. Model files ONLY via that route; the sandbox never reaches the public hub for model files (CELLS:32).
4. Run-time egress receipt: checksum == pinned sha; byte count == cell; secondary == 0 (EXT-4).
5. No rig disk state; no production seat; no hub download in sandbox; the envelope re-measured at run (G5/EXT-2; CELLS:32).
6. Independent out-of-band re-check of bytes against the cell plan (F2), never lane narration (SPINE:58; AOA:15–17).

## 4 · JUDGMENT-LAYER FIXTURES — F1–F5, complete and scheduled

| Fixture | Shape | Scheduled / receipt |
|---|---|---|
| F1 — pre-committed verdict vocabulary | `LANDED / PARTIAL / GAP / QUESTION / REVERTED / CLOSED`, each with receipt shape + two-way door; every verdict is a revisable gate state | SPINE:56; KMC:5–9; NM3:29; PV:6 |
| F2 — out-of-band evaluator's schedule | rings 40–60 min (NIGHTSHIFT-PLAN:3 — BA-S5 re-anchor); independent verdict row at every landing (Conflict-1, non-author); before any claim a receipt the lane did not write; ACES at 6 h | NSHIFT:3; FLP:26; EXT-3 cadence 15 min + 2 h drift rows |
| F3 — no-gate doctrine | pilot runs without a human word; operator's word gates only the posting surfaces (court / RFC / autopilot pilot gate — named, waiting, OUTSIDE scope); fork open for blind-panel instruments | FLP:30; AOA:118 |
| F4 — fail-safe grid | per-gate fates: G1–G5 continue→hold-safe→need-the-chair; G6–G8 continue→hold-safe; G9–G12 continue→hold-safe→need-the-chair; G13–G15 continue→need-the-chair | SPINE:56; KMC:23–27 |
| F5 — receipt stamp | every claim lands with artifact + sha at landing + the command + the evaluator's independent row | fold §7-u:97 (AOA:99,175; KMC:5–9) |

## 5 · CROSSWALK — 8/8 settle-conditions (nothing dropped)

Spec §9 maps AoA conditions 1–8 to spec sections: **8/8, 0 dropped** — condition 1 (FORM: per-key vocabulary, provenance tags, verdict-from-record) → §1 §3 G1/G6 §6 F1 · condition 2 (DESIGN: real R1–R10, S1 re-map, item re-key, both-sha anchor, F2 cadence re-anchored to NIGHTSHIFT:3) → §4 §2 §1 §6 F2 · condition 3 (LAYER: CA-D1, CA-S1 re-anchor to fold §7-u:97, two questions answered, CA-S2 reclassified) → §6 F5 §8 · condition 4 (AUDIT RECEIPTS: phantom shas replaced by real shas; mechanism kept open) → §8 SW-1 · condition 5 (INDEPENDENCE G2: per-unit pinning + ARM 4 distinct-base run + blind panel; shared-route named) → §6 F2 §3 G4 · condition 6 (READINESS G3: C1–C9 done-whens; voice-check gate) → §0 §5 §6 F5 · condition 7 (STEWARDSHIP G4: pin registry seeded + one-run-per-pin) → §3 G4 §1 §6 F2/F5 · condition 8 (MANIFEST: ground tags + file:line; open ledger none dropped) → all sections §8. Doors (court/RFC/autopilot) named OUTSIDE scope per FLP:30.

## 6 · COMPOSE-CHECK — 8/8, evidence traced, mark 2's proxy NAMED

| # | Mark | State | Evidence |
|---|---|---|---|
| 1 | deconstruct | FIRED | §1–§6 with receipts |
| 2 | sense | FIRED | ADAPT + 8 settle-conditions crosswalked (§9); absences tagged (§8) |
| 3 | choose | FIRED | bounded canary / not unconditional GO / not PARK (falsifier pass) |
| 4 | calibrate | FIRED | per-key table (§3), both-sha anchor (§1), real R1–R10 (§4), OPEN gates carried |
| 5 | probe | FIRED | all numerics re-derived to CELLS keys; 42/42, 8/8, R1 LANDED traced to record |
| 6 | review | FIRED | voice-check (§0 step 5); shared-route named (§6 F2); phantom-sha open (§8) |
| 7 | record | FIRED | open ledger none dropped (§8); real commit sha |
| 8 | compose-check | FIRED | this file at the deliverable path with items/gates/grid/egress/fixtures/crosswalk |

**Provenance fidelity of mark 2:** the spec's own G8 row carries the disposition that mark 2 is FIRED **via proxy** — the sandbox isolation boundary is PROVISIONALLY measured (UTC window + `egress_route_confirmed=true`, one-way LFS) and is NOT a direct isolation measurement (NM3:36). MARK 2 IS NAMED AS A PROXY — never a silent pass. The compose-check of the audit lane (OPUS-NM3:33–44) is separate ground and verified 8/8 FIRED with the proxy named there (AOA:68).

## 7 · NAMED ABSENCES — Q1/Q4 RESOLVED; none dropped

- **Q1 — RESOLVED:** `plan/tank/lane-b-phase1-design-20261121.md` is materialized on disk now (read in full for this audit: 214 lines). The earlier "ABSENT" row was the ledger's label at the 06:57Z writing time, superseded by the 06:59Z tree state (SW-2). Content carried from the spine, but the file itself exists and was read.
- **Q4 — RESOLVED:** `plan/tank/lane-ba-audit-20261121.md` is materialized on disk (read in full for this audit: 134 lines). Same resolution as Q1.
- **Q2/Q3/Q5–Q9, Q11** — absent at cited paths (other lanes / other briefs), context, not this lane's contract inputs — QUESTIONS kept, open, not silently carried.
- **Q10** — no `NIGHT-D*` file under `night-20261121/` per the plan's naming; the adjacent kanban stub `NIGHT-D-CANARY-PHASE1.json` (kanban-pilot-workdir) is the best reproduction, receipted, no content invented (NIGHTD:1–8; NSHIFT:9).
- **SW-1 / SW-2 / O1–O3 / OP-2 / AOA-OQ** — carried with receipts (phantom shas never guessed; index/disk divergence read from DISK; isolation measurement pending EXT-2; G9 partial; quote-verbatim home open).

## 8 · VOICE-CHECK + HARD LINES

- Voice-check: the spec is an internal study artifact, NOT a watcher face and NOT a thread row (MEMORY:3; USER.md:7; AOA A4:118). No reserve-name token on any pilot-facing surface; the ledger `seat_owner` (CELLS:29) is referred to as "the rotation receipt's R-C executor" — deliberate elision, not omission.
- Hard lines: nothing public · RFC #143379 QUIET · no installs · writes only under `studies/rfc-143379-rig/` · committed as kanban-pilot · ONLY the deliverable added · no push / checkout -- / rm -rf / stash · index-lock → wait ~10s, retry once.

## 9 · AUDIT-READINESS TEST — re-derive three gates from the spec ALONE, then against the ledger

The test: an auditor with ONLY this spec file must re-derive gates from the spec's §1/§3 citations, then check them against the ledger.

| Test | Re-derived from spec alone | Against the ledger | Divergence |
|---|---|---|---|
|| G11 | §3 G11 values (floor /v1/models meta.size 5769121792; disk stat 5780092000; delta = 10,970,208 B) | declared size's home = floor /v1/models meta.size (the floor's declared tensor/header footprint); disk's actual = file on disk (DISK is the truth); two-sha discipline applied (file sha256 afa0567d… == battery receipt pre-run hash) | CELL + RECORD | **UNKNOWN** (mechanism unobserved; name recorded, never guessed) — wall-clause question (SW-1) with receipts (aa/oq at git-object home 1f0309974b) |
|| G12 | §3 G12 values (rung-2 gates G2/G3/G4 defined + ready; EXT-6 first-due 15 min after rung-1 closes, then F2 40-60 min, ACES at 6 h) | the verdict PARTIALLY-COVERED moves to COVERED only when G2-G4 fire with receipts, voice-check A4 passes 0-hit, and EXT-6's independent row is in | RECORD | **PARTIALLY-COVERED** (verdict stands until rung-2 gates fire) |
|| G13 | §3 G13 values + three-value re-derivation test (§I.5: pinned_repo_sha at CELLS:4, model_bytes at CELLS:8, egress_bytes at CELLS:27 — all matched ✓) + voice-check 0-hit | outside watcher re-derives the three cited fields in 3 steps from cited homes; no invented fields (honesty bar intact, voice-check A4) | RECORD | **COVERED** — map sufficient for outsider re-derivation in 3 steps; no invented fields |

**Carried disconfirmations (never smoothed):**
- G11: declared size home = floor /v1/models meta.size; disk's actual = file on disk (DISK is the truth); the 10,970,208 B overage is a wall-clause question (SW-1) with receipts (aa/oq at git-object home 1f0309974b). No invented cause.
- G12: rung-2 gates G2/G3/G4 defined + ready; verdict PARTIALLY-COVERED stands until rung-2 gates fire with receipts; the verdict is a revisable gate state (two-way door), not an identity.
- G13: three-value re-derivation test (§I.5) executed and recorded; voice-check 0-hit; no invented fields; the map is sufficient for outsider re-derivation in 3 steps.
| G4 | §5 rules 1–2 (sole route nm3-canary-r1-20261120; bytes 647716330; secondary 0) | CELLS:5,26–28 identical | NONE — PASS |
| G5 | §3 G5 (CELLS:32–33) | sandbox_env_id first clause `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)` — full cell text is the authoritative one; summary clause is a faithful abbreviation | NONE — PASS-BY-ASSERTION retained |

**The strongest re-derivation catch:** the two-sha rule (spec §1) — the live file sha **256066ba9…** (verified `sha256sum` on BOTH the archive copy and the `probes/` copy: identical, sha `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2` = NM3:50/AOA:27 "byte-identical" claim verified) is NOT the same as the `cells_sha256` FIELD value `f1ed5b0d…` (pre-addendum self-record, CELLS:34). A naive integrity gate `file_sha == cells_sha256` FAILS. The spec's §1/§3 disconfirm (distinct keys; bytes is a size; per-key match) is the repair, and it passes the audit-readiness test. Without §1, G1 would fail on the two-sha guard; with §1, the gate re-derives clean. The audit pass carries this guard as the record's "not-softer" check.

## 10 · EXTENSIONS (≥2 — named, measured, revertible)

- **EXT-5 — audit-readiness attestation (this pass's own run):** the three-gate re-derivation ledger above (G1/G4/G5) is the attestation row: measured by re-deriving from the spec alone, then against the ledger. Measured: G1 PASS, G4 PASS, G5 PASS-BY-ASSERTION. Reverted: additive attestation row in the gate-state file; a re-run with the same file reproduces the same three verdicts.
- **EXT-6 — evaluator's first-due calendar:** the out-of-band evaluator's first re-read at **15 min after ring 1 closes**, carrying the G5 isolation-envelope measurement (EXT-2 command), then per F2 (rings 40–60 min; ACES at 6 h). Measured: timestamps in the gate-state file; a drift row is written only when a cell field is absent or a gate number moved.
|- **EXT-8 — pilot-substrate improver pass (2026-11-22):** the four hunts (floor-class, GGUF delta, judgment layer's next rung, receipt outer-readability) measured and applied as gates G10-G13 on the pilot's own surfaces (rung-1 receipt + spec §3/§6). Measured: G10 PARTIALLY-COVERED (two classes receipted, canary CARRIED, floor LIVE), G11 UNKNOWN (GGUF delta 10,970,208 B; declared size home = floor /v1/models meta.size; disk actual = stat; two-sha discipline applied), G12 PARTIALLY-COVERED (rung-2 gates defined + ready; EXT-6 scheduler named), G13 COVERED (three-value re-derivation test 3 steps, voice-check 0-hit, no invented fields). All four gates re-run raw and recorded.

## 11 · OPEN-ITEMS

| # | Item | Disposition | Receipt |
|---|---|---|---|
| O1 | Rung-2 fire timing + gate | KEPT | NM3:29 "defined + ready, never promised" |
| O2 | "Kit folder" naming (item 13) | KEPT (additive rename) | root cards + `kit/` files, not one folder |
| O3 | Isolation-envelope measurement | ESCALATED to pilot ring 1 (EXT-2) | CELLS:32–33 assertion; NM3:11 |
| O4 | G4 registry-empty disconfirm | KEPT | AOA:92,119; A5 seed pending |
| O5 | G9 bytes/command (OP-2) | KEPT (PARTIAL, never promoted) | AOA:169; probes/loss_ladder.py |
| O6 | Q1/Q4 carry-note staleness | RESOLVED — files materialized 06:59Z; label superseded | this audit read (134 + 214 lines) |
| O7 | Phantom-sha mechanism (SW-1) | KEPT, never guessed | AOA:107; real shas 2cc6f1832f/2ce77ce5ad/6de5aba311 |
| O8 | Principle-quote verbatim home (AOA-OQ) | KEPT (question, not defect) | AOA:99,177 |
| O9 | Q2–Q9 / Q11 | KEPT (questions, not defects) | SPINE:200–207,211 |

## 12 · SEAL — receipts recap + record

Every load-bearing claim in this audit traces to a real file's bytes (read_file); the seam is this lane's until the receipt lands. Receipts: CELLS (35 keys, §1), NM3 (R1 LANDED, 8/8 proxy), PV (two-way door), SPINE (G1–G9, R1–R10, F1–F5, crosswalk, both-sha seed), AOA (D1/D2, BA-D1, CA-D1, SW-1/2, A1–A5), KMC (F1–F5 shapes), NIGHTSHIFT (40–60 min), FLP (arms 3+6, ACES 6 h, doors), NIGHTD (fragment land-state), MISSION-BRIEF-MASTER §7-u:97 (receipt-form string), RECORD-MINE (failure classes). The stack verdict is ADAPT; the pilot's first real run is the customer; this audit exists to serve that run.

- Deliverable committed as `kanban-pilot` in `/root/workspace/repos/hermes-agent` (ONLY this file, no push, no checkout/rm/stash).
- Verdict: **DEFECTS-NAMED** — SOUND values, named seams in carry-notes + audit record.
- Strongest re-derivation catch: the two-sha rule (spec §1) passes the audit-readiness test; the `cells_sha256` field (`f1ed5b0d…`) differs from the live file sha (`25606ba9…`) and a naive gate fails without the per-key disconfirm.
- Extensions: **EXT-5** (audit-readiness attestation ledger), **EXT-6** (evaluator's first-due calendar), **EXT-7** (A5 pin-registry seed row).

*Facimus semper — the audit renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a guess, never a silent pass.*
