# CANARY-PHASE1-SPEC-20261122 — the canary's FULL phase-1 specification

*ARM 3a · canary-spec lane · study/rfc-143379-rig-20261105 · RFC #143379 upstream QUIET · nothing public beyond PR #1's thread · no installs · write-window: this file only · gate: the rotation's audit pass (FINAL-LEG-PLAN:16).*

> **What this file is.** The ONE audited brief for the canary's first real run. It is a **user manual for the substrate**: an independent auditor must be able to run the canary from this file alone — no other document, no narration, no trust in prose. Every load-bearing claim is receipted to a real file's bytes (path + line). Every gate is re-derived from the cells ledger's **keys**. Nothing is invented; a non-reproduction is a **QUESTION** with receipts, never a guess and never a silent pass.
>
> **Plan guard.** The PLAN (night-20261121/FINAL-LEG-PLAN-20261121.md arms 3 + 6) is not altered. This spec serves the armed arm; it does not re-sequence, open, or close any door. The three doors — the court's posting, the RFC's surface (upstream issue QUIET), the autopilot's pilot gate — wait on the operator's word and are OUTSIDE this spec's scope (FLP:30; AOA:139-146; SPINE:122-124).
>
> **Wall clause (binding).** A citation that does not reproduce at its cited path under local `read_file` is a QUESTION with receipts — not a defect in the artifact, not a guess, and not silently carried. Two contract inputs do not reproduce: see §8. They are named there, with their git-object seam, and their content is carried here from the present OPUS spine (SPINE:19-60), which is itself contract input 2.

---

## 0 · AUDIT RUNBOOK (read this first — how to verify this spec from scratch)

1. **Receipt shorthand.** Every `TAG:N` below maps to an exact local path and line in §11 (the receipt index). Read with `read_file`, never `web_extract` (hard line; BRIEF:19).
2. **Re-derive, don't trust prose.** For each gate in §3, open `CELLS` at the cited line and compare the literal key/value. `pinned_repo_sha` (CELLS:4) and `model_safetensors_sha256` (CELLS:7) are **two distinct keys with two distinct values** — the gate is match-to-plan **per key**, never cross-key `==`; `model_bytes` is a size, not a hash (AOA:51-52; SPINE:68).
3. **Check the grid against the artifact, not the audit.** The real R1–R10 in §4 is the design's actual §3 (SPINE:39-54); the BA audit's phantom trace (AOA:34, BA-D1) is NOT the grid. This spec carries the repair.
4. **Count check.** Named items = 15 (§2). Measured gates = 9 (§3). Revert points = 10 (§4). Judgment fixtures = 5 (§6). Settle conditions = 8 (§9). Egress rules = 6 (§5). Crosswalk = 8/8, nothing dropped (§9).
5. **Voice-check.** This spec is an internal study artifact, NOT a watcher face and NOT a thread row. Per the register (MEMORY:3, USER.md:7; AOA A4:118; BRIEF-SPRINT-LEGS:13): thread rows are envelope-form, handles-only, and the reserve's name rides NO pilot-facing surface. This spec therefore does not spell that name; where the ledger's `seat_owner` (CELLS:29) and the internal seat line (NM3:3) carry it, this spec refers to "the rotation receipt's R-C executor" and cites the key — the elision is deliberate, not an omission. Nothing in this spec posts to PR #1.
6. **Emission/hard lines.** Committed as `kanban-pilot`, ONLY this deliverable; never pushed; no `checkout --` / `rm -rf` / `stash`; index-lock → wait ~10s, retry once (BRIEF:16). Writes only under `studies/rfc-143379-rig/`.
7. **Termination.** One review round after assembly (§12); no measurable change ×2 → PARK with the record, report, stop (BRIEF:19).

---

## 1 · THE SUBSTRATE RECORD (cells ledger, verbatim key-by-key)

The substrate is one file: `CANARY-CELLS-20261120.json`. Its keys are the **only** source for the measured gates. Re-derive from the bytes (CELLS:1-35; the study copy at `probes/CANARY-CELLS-20261120.json` is byte-identical per NM3:50 / AOA:27 — but read the archive copy below):

| Key | Value (literal) | Line |
|---|---|---|
| `rung` | 1 | CELLS:2 |
| `candidate` | `kshitijthakkar/deepseek-v4-mini-300M-from-flash` | CELLS:3 |
| `pinned_repo_sha` | `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` | CELLS:4 |
| `egress_route` | `private repo release nm3-canary-r1-20261120 (sole route)` | CELLS:5 |
| `start_utc` | `2026-11-20T04:41:38Z` | CELLS:6 |
| `model_safetensors_sha256` | `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c` | CELLS:7 |
| `model_bytes` | 641262336 | CELLS:8 |
| `transformers_version` | 5.23.0 | CELLS:9 |
| `torch_version` | 2.15.0+cpu | CELLS:10 |
| `load_path` | repo-own code package `code/deepseek_v4` — native config rejected `compress_ratios=48` (wall receipt) | CELLS:11 |
| `load_seconds` | 0.95 | CELLS:12 |
| `param_count` | 319028736 | CELLS:13 |
| `deterministic_max_abs_diff` | 0.0 | CELLS:14 |
| `determinism_tolerance` | 1e-06 | CELLS:15 |
| `deterministic_within_tolerance` | true | CELLS:16 |
| `logits_shape` | [1, 4, 129280] | CELLS:17-21 |
| `argmax_next_token` | 49969 | CELLS:22 |
| `finish_utc` | `2026-11-20T04:41:43Z` | CELLS:23 |
| `license` | MIT (verified live from HF model card: `license: mit`; tags include `license:mit`; text-gen MoE, base `deepseek-ai/DeepSeek-V4-Flash`) | CELLS:24 |
| `license_compatible_private_repo` | true | CELLS:25 |
| `egress_route_confirmed` | true | CELLS:26 |
| `egress_bytes` | 647716330 | CELLS:27 |
| `egress_secondary_downloads` | 0 | CELLS:28 |
| `seat_owner` | none at dispatch; R-C executor assigned by the rotation receipt (name elided per voice-check) | CELLS:29 |
| `token_measure` | 0 provider calls (mechanical sandbox run) | CELLS:30 |
| `tz_anchor` | UTC | CELLS:31 |
| `sandbox_env_id` | `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)`; isolation boundary named; model files pulled ONLY via the private-release route; no rig disk state; no production seat; no HF download in sandbox | CELLS:32 |
| `sandbox_env_id_added_utc` | `2026-11-20T04:45:00Z` | CELLS:33 |
| `cells_sha256` | `f1ed5b0db75d8d91fe15780a23ea6529d370bdf9e3ad98b26e57787f0d49b536` (pre-addendum self-record field) | CELLS:34 |

**Two-sha rule (load-bearing).** The `cells_sha256` **field** (CELLS:34, `f1ed5b0d…`) is the pre-addendum self-record; the **live file** hashes `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2` (NM3:50 / AOA:38 / SPINE:60). A naive integrity gate `file_sha == cells_sha256` would FAIL (`f1ed5b0d` ≠ `25606ba9`). The gate-state schema must carry **both** keys — field + live-file — so a re-read does not fail on the addendum (BA-S6; AOA:38; SPINE:60). Verdict **R1 LANDED**, rung-2 ARMED sha `415501bd…` ("defined + ready, never promised") is a **record** verdict (NM3:29,48), NOT a cell measurement — cells have no `verdict` key (AOA:53).

---

## 2 · NAMED ITEMS (15 — every item named, sourced, tagged)

Re-keyed to the **artifact's** IDs, not the BA audit's drifted table (BA-S3; AOA:36; settle 2). State tags: FIRED / RUNNING / OPEN (SPINE:23; design §1:40-54).

| # | Item | State | Tag | Receipt |
|---|---|---|---|---|
| 1 | Rung-1 identity (candidate + rung) | FIRED | measured-cell | CELLS:2-3; SPINE:23 |
| 2 | Model sha (per-key: repo pin + safetensors) | FIRED | measured-cell | CELLS:4,7; SPINE:23,68 |
| 3 | Load + minimal forward + determinism | FIRED | measured-cell | CELLS:12-22; NM3:15; SPINE:23 |
| 4 | Licensing (MIT + compatible) | FIRED | measured-cell | CELLS:24-25; SPINE:23 |
| 5 | Egress (sole route, byte-counted) | FIRED | measured-cell | CELLS:5,26-28; SPINE:23 |
| 6 | Sandbox envelope (boundary named) | FIRED | measured-cell (assertion) | CELLS:32-33; NM3:11,50; SPINE:23 |
| 7 | Record-first (unreadable = not confirmed) | FIRED | design-field | NM3:11; AOA:28; SPINE:23 |
| 8 | Two-way door (rollback = no commitment) | FIRED | design-field | NM3:29; FLP:30; SPINE:23 |
| 9 | Method card 1 — first-catches (two-way verdict + stamp) | RUNNING | design-field | KMC:5-9; SPINE:23 |
| 10 | Method card 2 — honest termination (no-change twice) | RUNNING | design-field | KMC:11-15; SPINE:23 |
| 11 | Method card 3 — byte-verified meter + out-of-band evaluator | RUNNING | design-field | KMC:17-21; SPINE:23 |
| 12 | Method card 4 — fail-safe grid + fold-and-re-anchor | RUNNING | design-field | KMC:23-27; SPINE:23 |
| 13 | Capture home (root cards + `kit/` files, NOT one folder) | FIRED | design-field | KMC:29-30; AOA:166; SPINE:23 |
| 14 | Gate-state file (operator's read surface) | OPEN | design-field | SPINE:23; AOA:125; SPINE:60 |
| 15 | Judge-gate re-reads (per-ring independent read) | OPEN | design-field | SPINE:23; AOA:125; SPINE:56 |

**Count = 15** (items 1-8 FIRED, 9-12 RUNNING, 13 FIRED, 14-15 OPEN). Every item carries its receipt anchor; no invented fields (SPINE:23). Item IDs follow the artifact; the BA audit's collapse of 9-12 into one row and displacement of card 3 (BA-S3) is NOT carried.

---

## 3 · THE MEASURED GATES (9 — per-key table, re-derived from the ledger)

Each row re-derived from CELLS keys (A2; AOA:116; SPINE:25-37). **Provenance tags:** `CELL` = re-derived from a ledger key; `RECORD` = sourced to a landed record (NOT a cell). Disconfirmation is explicit per gate (Are Right A Lot).

| Gate | Per-key measurement (CELLS:line) | Bar | Disconfirm / seam | Tag | Receipt |
|---|---|---|---|---|---|
| **G1** | `pinned_repo_sha`=`fc8b9934…` (4); `model_safetensors_sha256`=`5747a90e…f35a1c` (7); `model_bytes`=641262336 (8) | Each key MATCHES plan; **two distinct keys, never `==`**; bytes = size, not hash | Disconfirmed cross-key equality: distinct keys/values, no ledger row asserts equality (AOA:51-52) | CELL | SPINE:29; AOA:27 |
| **G2** | load 0.95 (12); params 319028736 (13); logits [1,4,129280] (17-21); argmax 49969 (22); max_abs_diff 0.0 (14); tol 1e-6 (15); within=true (16); transformers 5.23.0 / torch 2.15.0+cpu (9-10) | max_abs_diff < 1e-6 | Native config rejected `compress_ratios=48`; repo-own code package used (CELLS:11) — not a dead-end (NM3:15) | CELL | SPINE:30; NM3:15 |
| **G3** | `license` MIT (24); `license_compatible_private_repo` true (25) | Compatible with private repo | Verified live from model card, not inferred | CELL | SPINE:31; NM3:17 |
| **G4** | sole route `nm3-canary-r1-20261120` (5); `egress_bytes` 647716330 (27); `egress_secondary_downloads` 0 (28); `egress_route_confirmed` true (26) | Byte-counted; zero secondary | Registry was empty → G4 rule-with-no-rows; A5 seed row + one-run-per-pin pending (AOA:92,119) | CELL | SPINE:32; AOA:27 |
| **G5** | `sandbox_env_id` `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)` (32), added 2026-11-20T04:45:00Z (33) | Boundary named | **PASS-by-assertion — NOT measured**; cell annotation, not independent measurement (BA-S2); pilot re-measures at run (EXT-2) | CELL (assertion) | SPINE:33; AOA:29 |
| **G6** | Field mapping unchanged on second cold re-read; no invention | Record-first fields + OPUS §2(1)/§7 | Re-anchor: **NOT "PILOT-VERDICT §2"** (that file has no numbered sections) — S1 re-mapped (AOA:28) | RECORD | SPINE:34; NM3:11,50 |
| **G7** | R1 LANDED, receipt complete; rung-2 armed sha `415501bd…` | Verdict row at named commit | "defined + ready, never promised" — O1 kept, not a promise (AOA:165) | RECORD | SPINE:35; NM3:29,48 |
| **G8** | All 8 compose-check marks FIRED, mark 2 via proxy | 8/8, traceable | Mark 2 is proxy (UTC window + egress-confirmed), not a direct isolation measurement (NM3:36) | RECORD | SPINE:36; NM3:33-44 |
|| **G9** | Byte-verified receipt meter: tool-output 0.0 @ 0.5/0.65/0.8; re-entry d≈0.864; assistant-prose 0.0 @ 0.65 | Measured bytes + command | **PARTIAL**: bytes/command = OP-2 (run log / `probes/loss_ladder.py`), carried open; never promoted to pass | RECORD (partial) | SPINE:37; AOA:169 |

**NEW GATES (2026-11-22 pilot-substrate improver pass — the PLAN is not altered):**

|| **G10** | Two classes receipted with two-sha discipline: canary 300M class (CELLS:2-34; pinned_repo_sha fc8b9934…, model_safetensors_sha256 5747a90e…, model_bytes 641262336) vs the floor's 9B GGUF class (live floor, /v1/models meta.size 5769121792, disk 5780092000 B, sha256 afa0567d…, n_params 9197093888) | two classes, distinct keys, never `==`; canary numbers CARRIED from CELLS (2026-11-20), not re-executed on floor; floor LIVE named | CELL + RECORD | **PARTIALLY-COVERED** — class-match instrument applied (receipt's §I.5 three-value re-derivation test + two-sha discipline) |
|| **G11** | GGUF delta: declared size home (floor's /v1/models meta.size = 5769121792) vs disk actual (stat = 5780092000); delta = 10,970,208 B; two-sha discipline applied (file sha256 afa0567d… == battery receipt pre-run hash) | declared size's home = floor /v1/models meta.size; disk's actual = file on disk (DISK is the truth); the 10,970,208 B overage is a wall-clause question (SW-1) with receipts (aa/oq at git-object home 1f0309974b) | CELL + RECORD | **UNKNOWN** (mechanism unobserved; name recorded, never guessed) |
|| **G12** | Judgment layer's next rung: rung-2 gates G2 (base diversity), G3 (C1–C9 + voice-check A4), G4 (one-run-per-pin + OP-2 byte-meter) defined + ready; EXT-6 out-of-band evaluator's first-due 15 min after rung-1 closes, then F2 40-60 min, ACES at 6 h | the verdict PARTIALLY-COVERED moves to COVERED only when G2-G4 fire with receipts, voice-check A4 passes 0-hit, and EXT-6's independent row is in | RECORD | **PARTIALLY-COVERED** (verdict stands until rung-2 gates fire) |
|| **G13** | Receipt's outer-readability: three-value re-derivation test (§I.5: pinned_repo_sha at CELLS:4, model_bytes at CELLS:8, egress_bytes at CELLS:27 — all matched ✓) + voice-check 0-hit | outside watcher re-derives the three cited fields in 3 steps from cited homes; no invented fields (honesty bar intact, voice-check A4) | RECORD | **COVERED** — map sufficient for outsider re-derivation in 3 steps; no invented fields |

|| **Count = 13 measured gates** (G1-G9 from the audit pass plus G10-G13 from the 2026-11-22 pilot-substrate improver pass — the PLAN is not altered). G1-G5 are cell-derived (G5 an assertion); G6-G9 are record-sourced and tagged as such; G10-G13 are new pilot-substrate gates (class-identify, gguf-delta-trace, judgment-next-rung, receipt-re-derivation-test), each re-run raw and recorded (receipt: canary-rung1-receipt-20261122.md III). **Gate law (MEMORY:19):** internal doors ACT, never wait — a failed gate re-arms (§4), it does not pause the run for a human word.||

**Fail-safe fates for all gate rows** (F4 / design §5; SPINE:56): G1-G5 → continue → hold-safe → need-the-chair; G6-G8 → continue → hold-safe; G9-G12 → continue → hold-safe → need-the-chair; G13-G15 → continue → need-the-chair. The grid covers 15 gate identities; the 13 above are the ones with measured values at this reading.

---

## 4 · THE REAL R1–R10 REVERT GRID (10 — phantom trace repaired)

These are the **artifact's actual §3** (design §3:83-92), carried in the present OPUS spine (SPINE:39-54). The BA audit's "no gate-state file → PARTIAL / run fails first two gates / PR status diverges → branch rebased / post lands before run / reply posted but no measurement / transcript asks a question / born-out gate schema" (AOA:34) is a **phantom trace** — phrase-hunted to one file (the audit itself), design bytes stable (disk sha `5d4015f2` == original blob). It is NOT the grid. BA-D1 is repaired here (AOA:34; settle 2:140).

| # | Revert point | Trigger | Mechanism | Receipt |
|---|---|---|---|---|
| **R1** | Cell install | sha mismatch, or load fails | Sandbox torn down; install additive, deleted on revert | SPINE:43 |
| **R2** | Model load | `load_seconds` above barrier, or params ≠ 319028736 | Load is a probe; forward never runs on a bad install | SPINE:44 |
| **R3** | Determinism | `max_abs_diff` ≥ 1e-6 | Run recorded as a probe, never a verdict; never burns rung-2 | SPINE:45 |
| **R4** | License | `license_compatible_private_repo` false | Model not compatible; release route untouched | SPINE:46 |
| **R5** | Egress | `egress_secondary_downloads` > 0 | One-way, byte-counted; a second download aborts the run | SPINE:47 |
| **R6** | Isolation | Envelope contract not verifiable | Boundary named and checked at run time (EXT-2) | SPINE:48 |
| **R7** | Gate-state file | Any gate fails | Additive + revisioned; last PASS revision is the rollback point | SPINE:49 |
| **R8** | Capture home | Fold lands the file; nothing behind it | Fold additive (root cards + `kit/` files) | SPINE:50 |
| **R9** | Judge-gate re-reads | A re-read shows a drift | Evaluator's verdict row carries the independent read | SPINE:51 |
| **R10** | ACES trigger | Improver loop fires | Stops on measured plateau (no-change twice); termination receipted twice over | SPINE:52 |

**Revert rule (design §3:94; SPINE:54):** a failed gate freezes the run's verdict row at **PARTIAL/GAP** and re-arms the same item at the next ring — never a silent skip, never a re-run with different values. Rollback = no commitment made (NM3:29). Count = 10.

---

## 5 · THE SOLE-EGRESS DISCIPLINE (6 rules — from the cells' own rule)

Design §4:102-109 / SPINE:58; cells CELLS:5,26-28. The route is the **sole** route, byte-counted, secondary 0.

1. **One sole route:** private repo release `nm3-canary-r1-20261120`, no mirror/secondary (CELLS:5; SPINE:58).
2. **One-way, byte-counted:** `egress_bytes` = 647716330; `egress_secondary_downloads` = 0; `egress_route_confirmed` = true (CELLS:26-28; NM3:19).
3. **Model files ONLY via that route:** the sandbox never reaches the public model hub for model files (CELLS:32; SPINE:58).
4. **Run-time egress receipt:** the pilot produces its own receipt — checksum == pinned sha, byte count == cell, secondary == 0 (EXT-4 re-receipt; SPINE:58,60).
5. **No rig disk state, no production seat, no hub download in sandbox:** the pilot re-measures the envelope at run (G5 / EXT-2; CELLS:32; SPINE:58).
6. **Independent out-of-band re-check** of bytes against the cell plan (F2), never lane narration (SPINE:58; AOA:15-17).

**Voice/ethics:** nothing public, RFC #143379 upstream QUIET, no installs (BRIEF:19; FLP:30). The egress route is a private release; this spec opens no door.

---

## 6 · JUDGMENT-LAYER FIXTURES (F1–F5 — the mechanization of every boundary the human eye caught first)

The pilot's boundary is the JUDGMENT layer, not the machinery (PILOT-VERDICT:6,13,31). The three named instruments — pre-committed verdict vocabulary, out-of-band evaluator schedule, no-gate doctrine — each already exist in the kit and ride here as the canary's named fixtures (FLP:22; PV:31; SPINE:56). Fixture shapes from the kit's method cards (KMC:5-27; BMCD:9-11). Count = 5.

**F1 — Pre-committed verdict vocabulary (SPINE:56; KMC:5-9).** The vocabulary is fixed **before** the run: `LANDED / PARTIAL / GAP / QUESTION / REVERTED / CLOSED`, each with a receipt shape and a two-way door; every verdict is a revisable gate state, never an identity. A verdict names its revising evidence; the record's own correction machinery carries revisions (append-only; history never rewritten — AOA:105). Canonical instance: `R1 LANDED` (NM3:29) / `PROOF-OF-CONCEPT — CONFIRMED, WITH THE BOUNDARY NAMED AS ONE CLASS` (PV:6). No verdict is sourced to cells (AOA:53).

**F2 — Out-of-band evaluator's schedule (SPINE:56,60; AOA:37; NSHIFT:3; FLP:26).** Re-read G1–G5 at each ring (40–60 min cadence, sourced to NIGHTSHIFT-PLAN:3 — BA-S5 re-anchor, not FINAL-LEG). An independent verdict row at every landing (verifier pair, Conflict-1, non-author — NM3:3). Before any claim, a receipt the lane did not write (KMC:17-21). ACES trigger at 6 h: no check-in → improve/audit/review loop fires (FLP:26; NSHIFT:3). EXT-3 cadence: 15 min first re-read, then 2 h, drift rows (SPINE:60). **Independence is NOT claimed:** the three audits rode one pinned base (AOA:13-17); G2 stays OPEN until stage-3 per-unit pinning + ARM 4's distinct-base run + a blind panel on the first numeric landing (AOA:143). Same-base convergence is never called independence.

**F3 — No-gate doctrine (SPINE:56; FLP:30; AOA:118).** The pilot runs without a human word at the gate; the operator's word gates **only** the posting surfaces (court's posting / RFC's surface / autopilot's pilot gate — all named, waiting, OUTSIDE this spec). The fork is open for blind-panel instruments. The GATE LAW (MEMORY:19): the word gates only court / RFC / autopilot-pilot-gate / deletions / money; any other hold is a DEFECT; alarms ACT (reclaim + redispatch), never wait. The kit's readiness needs no human gate beyond the standing sets (FLP:30).

**F4 — Fail-safe grid (SPINE:56; KMC:23-27).** Gate fates pre-named in §3: G1-G5 continue→hold-safe→need-the-chair; G6-G8 continue→hold-safe; G9-G12 continue→hold-safe→need-the-chair; G13-G15 continue→need-the-chair. A mis-drawn fate is corrected at the next fold, never baked (KMC:26).

**F5 — Receipt stamp (SPINE:56; KMC:5-9).** Every claim lands with its artifact + sha at landing + the command + the evaluator's independent row (fold §7-u:97 receipt-form string — AOA:99,175). A landed claim is a claim until its bytes are checked; the stamp's correction rides the record's correction machinery.

**F6 — Judgment-layer next rung (verdict-moving conditions, PV:6; this pass's G12):** the verdict PARTIALLY-COVERED stands as a revisable gate state until (i) rung-2 gates G2 (base diversity — distinct pin/epoch per base), G3 (C1–C9 done-whens + voice-check A4), and G4 (one-run-per-pin, byte-meter OP-2) fire with receipts; (ii) the voice-check A4 passes 0-hit; (iii) the out-of-band evaluator's EXT-6 independent row is in (first-due 15 min after rung-1 closes, then F2 40-60 min, ACES at 6 h). Until then, the verdict is a revisable gate state (two-way door), not an identity. The pilot's boundary is the JUDGMENT layer, not the machinery (PILOT-VERDICT:6,13,31).

---

## 7 · NIGHT-D FRAGMENT INTEGRATION

The plan names night-D fragments "under night-20261121/ per the plan's naming — the fragments the OPUS-2 chain left" (BRIEF:10). Findings:

- **Found (adjacent path, not under night-20261121/):** `/root/workspace/kanban-pilot-workdir/arcs/NIGHT-D-CANARY-PHASE1.json` — 8 lines; `state: armed`, `assignee: head`, `workspace: studies/rfc-143379-rig/night-20261121`, `driver: head+lanes after A-C land`, `brief: the kit's method cards + capture home (memo Part 4)`, `gate: lands after A/B/C` (NIGHTD:1-8). It is the kanban arc stub of ARM D — the canary's first phase (NSHIFT:9; BMCD:1). **Integration:** it confirms this arm's scope and its gate ("lands after A/B/C"); it carries no measured gates, so no gate value is sourced from it. It is receipted here as the fragment's land-state, nothing more.
- **Companion fragments for context (not this arm):** NIGHT-A-BP-SIGMA, NIGHT-B-WEIGHTS-RUNG, NIGHT-C-COURT-VERIFY, NIGHT-E-RUNNER-MIRRORS in the same `arcs/` dir (INDEX.md:1-28; the INDEX itself lists only cycle 2026-10-01-C27, so the NIGHT-* stubs are a newer, unindexed set — a naming-seam, not a blocker).
- **Under night-20261121/ per the plan's naming:** no discrete file named `NIGHT-D*` exists (the dir holds NIGHTSHIFT-PLAN, BRIEF-KIT-METHOD-CARDS, BRIEF-SPRINT-LEGS, FINAL-LEG-PLAN, BRIEF-WEIGHTS-RUNG, BRIEF-COURT-VERIFY, BRIEF-WEDGE-ROOT-20261122, BRIEF-BP-SIGMA). **Wall clause → QUESTION Q10 (§8):** the fragment the brief expects at that path is not there; the adjacent kanban stub is the best reproduction and is receipted, not invented. No fragment content is guessed.

---

## 8 · NAMED ABSENCES & OPEN QUESTIONS (wall clause — open items with receipts; nothing dropped)

Per the improver's receipt-availability ledger (SPINE:188-211) and this lane's own scans. A non-reproduction is a QUESTION, never a defect in the artifact, never a guess.

| # | Named absence / question | Disposition | Receipt |
|---|---|---|---|
| **Q1** | `plan/tank/lane-b-phase1-design-20261121.md` — ABSENT (all local archives scanned) | QUESTION; **content carried here from SPINE:19-60** (design §1-§5/§9 re-rendered) | SPINE:199; git blobs `1f0309974b`/`3a7afc066a` named recoverable, but git-object recovery is outside `read_file` (SPINE:209) |
| **Q4** | `plan/tank/lane-ba-audit-20261121.md` — ABSENT | QUESTION; BA-D1 repair carried from AOA:34 + SPINE:39-54 | SPINE:202; git blobs `2cc6f1832f`/`7190c0efda` (SPINE:209) |
| **Q2/Q3/Q5-Q9** | lane-A / lane-C / lane-AA / lane-CA / AOA-BRIEF / GATHER-BRIEF / CROSS-AUDIT-BRIEFS — ABSENT at cited paths (context; not this lane's contract inputs) | QUESTIONS, open; not silently carried | SPINE:200,201,203-207 |
| **Q10** | night-D fragment under `night-20261121/` per plan naming — no `NIGHT-D*` file there | QUESTION; adjacent kanban stub found + receipted (§7), no content invented | NIGHTD:1-8; NSHIFT:9; SPINE:209's naming seam |
| **SW-1** | Phantom commit-sha mechanism (reported shas `16130475d2`/`ab660b943b`/`f4b845f05b` do not exist) | KEPT, never guessed; real landing shas used | AOA:107,176; SPINE:101 |
| **SW-2** | Index/disk divergence — read from DISK, never the index | KEPT (gather caution) | AOA:108,178; SPINE:103 |
| **O1** | Rung-2 fire timing + gate | KEPT (answered by next cell) | `415501bd…`, "defined + ready, never promised" — NM3:29; AOA:165 |
| **O2** | "Kit folder" naming (item 13) | KEPT (additive rename) | root cards + `kit/` files, not one folder — AOA:166; KMC:30 |
| **O3** | Isolation-envelope measurement not run | ESCALATED to pilot ring-1 (EXT-2) | CELLS:32-33 assertion; NM3:11; AOA:167 |
| **OP-2** | G9 measured bytes + command | KEPT (PARTIAL, never promoted) | AOA:169; SPINE:37 |
| **AOA-OQ** | Principle-quote verbatim home | KEPT (question, not defect) | AOA:99,177 |
| **Q11** | `WEIGHTS-RUNG-BATTERY-20261122.md` not landed at pre-reg's re-read → mark 8 HELD-OPEN | QUESTION, not a pass | PREPR:97-99 |

**Seam, not this lane's to repair:** Q1/Q4 (and Q2/Q3/Q5-Q8) are recoverable from this repo's git objects but git-object recovery is outside the mandated `read_file` method and the SW-2 fold removed `plan/tank/` from tracking (others' files; never checkout/rm/stash). No file is materialized; no history rewritten (SPINE:209; AOA:108). The spec does not claim those files exist; it carries their content from the present spine and tags the absence.

---

## 9 · SETTLE-CONDITIONS CROSSWALK (8 ↔ spec gates/sections — NOTHING DROPPED)

The stack verdict is **ADAPT** — GO for the bounded canary behind the standing start line, with eight settle-conditions; not unconditional GO, not PARK (AOA:134,136; SPINE:109). This spec serves all eight; each AoA condition is crosswalked to the exact spec section/gate that carries it. **8 of 8 mapped; 0 dropped.**

| AoA settle-condition (verbatim home AOA:139-146) | Carried by this spec | Gate/section | Receipt |
|---|---|---|---|
| **1 · FORM** — D1+D2 via A1/A2: per-key match vocabulary; provenance-tagged receipt; verdict sourced to record, never cells | §1 two-sha rule; §3 G1 disconfirm; §2 provenance tags; §6 F1 verdict-from-record | G1, G6, F1 | AOA:139; §1,§3,§6 of this spec |
| **2 · DESIGN** — BA-D1 revert re-trace (real R1–R10); S1 anchor re-map; item-table re-key; EXT-1 both cells shas; F2 cadence re-anchored to NIGHTSHIFT:3 | §4 real grid (repair); §2 re-keyed items; §1 two-sha rule; §6 F2 cadence | R1-R10, items 9-12, G1, F2 | AOA:140; §4,§2,§1,§6 of this spec |
| **3 · LAYER** — CA-D1 ancestry corrected; CA-S1 re-anchored to fold §7-u:97; two questions answered; CA-S2 reclassified | §6 F5 receipt-form (fold §7-u:97); §8 the two answered questions (PILOT-VERDICT:18-19) carried as answered, not defects | F5, §8 | AOA:141,99; §6,§8 of this spec |
| **4 · AUDIT RECEIPTS** — phantom shas replaced by real commit shas; mechanism question kept open | §8 SW-1 real shas + KEPT question; §11 receipt index uses real paths; this landing's own sha is real (report) | §8 SW-1 | AOA:142,107; §8 of this spec |
| **5 · INDEPENDENCE (G2)** — stage-3 per-unit pinning + ARM 4 distinct-base run + blind panel; shared-route constraint named; no same-base-as-independence | §6 F2 independence-not-claimed; §3 G4 registry-open; AOA:13-17 constraint named | F2, G4 | AOA:143; §6,§3 of this spec |
| **6 · READINESS (G3)** — C1–C9 done-whens before external share; watcher face passes voice-check grep gate | §0 runbook step 5 voice-check; §5 no-public/egress discipline; §6 F5 stamp | voice-gate, F5 | AOA:144,118; §0,§5,§6 of this spec |
| **7 · STEWARDSHIP (G4)** — pin registry seeded (A5) + one-run-per-pin; second run gated on outsider re-derivation | §3 G4 disconfirm (registry open); §1 two-sha seed (both keys); §6 F2/F5 outsider re-derivation | G4, §1 seed | AOA:145,119; §3,§1,§6 of this spec |
| **8 · MANIFEST (A3)** — every claim ground-tagged + file:line receipt; out-of-ground = questions; open-items ledger none dropped | §0 runbook (TAG:N → §11); §2/§3 provenance tags; §8 full open ledger (Q1-Q11, SW-1/2, O1-3, OP-2, AOA-OQ) | all sections, §8 | AOA:146; §0,§2,§3,§8 of this spec |

**Crosswalk completeness = 8/8 (100%); nothing dropped.** Doors (court / RFC upstream / autopilot pilot gate) are named OUTSIDE scope per FLP:30 and AOA:139-146 — they are not settle-conditions and are not gated by this spec.

---

## 10 · START LINE & TWO-WAY DOOR (the canary fires behind a measured line)

The start line is the kit's own, measured 2026-11-21, not asserted (PV:15-23): read-restore 42/42 GREEN (PV:18); harness READ-GATE + 2K byte-budget breaker (PV:19); W2 31/35 present (PV:20); U1-U3 settle-words (PV:26-28); kit-audit + kit-sceptic by exact name (PV:22). The pilot fires as a **bounded canary** behind this line: named items, measured gates, revertible at every named point — no weights, no public surface beyond PR #1's thread, RFC quiet (PV:31). Two-way door: a failed gate freezes the verdict row at PARTIAL/GAP and re-arms at the next ring (§4 rule); rollback is no commitment made (NM3:29).

---

## 11 · RECEIPT INDEX (full paths — every TAG:N above resolves here)

| Tag | Path |
|---|---|
| `CELLS` | `/root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json` |
| `NM3` | `/root/workspace/master-page/study-archive-20261120/OPUS-NM3-CANARY-20261120.md` |
| `PV` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/PILOT-VERDICT-20261121.md` |
| `SPINE` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/OPUS-PILOT-KIT-20261121.md` |
| `AOA` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/aoa-audits-20261121.md` |
| `FLP` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/night-20261121/FINAL-LEG-PLAN-20261121.md` |
| `KMC` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/KIT-METHOD-CARDS-20261121.md` |
| `BMCD` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/night-20261121/BRIEF-KIT-METHOD-CARDS.md` |
| `NSHIFT` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/night-20261121/NIGHTSHIFT-PLAN-20261121.md` |
| `MINE` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/RECORD-MINE-20261121.md` |
| `PREPR` | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/WEIGHTS-RUNG-PRE-REG-20261121.md` |
| `NIGHTD` | `/root/workspace/kanban-pilot-workdir/arcs/NIGHT-D-CANARY-PHASE1.json` |
| `BRIEF` (this contract) | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/briefs/BRIEF-CANARY-PHASE1-20261122.md` |
| MEMORY / USER | `/root/.hermes/memories/MEMORY.md` · `/root/.hermes/memories/USER.md` |
| fold §7-u:97 | `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md` (receipt-form string) |

Receipts are re-derived from bytes, not paraphrase. Where a cited path does not reproduce, §8 carries it as a QUESTION — never a silent pass.

---

## 12 · COMPOSE-CHECK (8 marks, register's stack-order clause) + REVIEW/TERMINATION

| # | Mark | State | Evidence |
|---|---|---|---|
| 1 | deconstruct | FIRED | Substrate / items / gates / revert / egress / fixtures separated with receipts: §1-§6. |
| 2 | sense | FIRED | ADAPT + 8 settle-conditions rendered + crosswalked (§9); named absences as questions (§8). |
| 3 | choose | FIRED | Bounded canary / not unconditional GO / not PARK — falsifier pass carried (§9, AOA:148-157). |
| 4 | calibrate | FIRED | Per-key gate table (§3), both-sha anchor (§1), real R1-R10 (§4), OPEN gates carried (§8). |
| 5 | probe | FIRED | Every numeric re-derived to CELLS keys (§1,§3); 42/42, 8/8, R1 LANDED traced to record (§10). |
| 6 | review | FIRED | Voice-check (§0 step 5); no invented field; shared-route constraint named (§6 F2); phantom-sha question open (§8). |
| 7 | record | FIRED | Open ledger none dropped (§8 Q1-Q11, SW-1/2, O1-3, OP-2, AOA-OQ); this spec + real commit sha. |
| 8 | compose-check | FIRED | This file exists at the deliverable path with items/gates/grid/egress/fixtures/crosswalk inside. |

**Review round (one, then terminate):** the disconfirmations in §3 (cross-key equality, G5 assertion, G7 promise, G8 proxy, G9 partial), the two-sha rule (§1), the phantom-grid repair (§4), and the 10 named absences (§8) were each checked against the cited bytes. No further measurable change is available after this round; a second read of the same bytes yields no change ×2 → **PARK the improvement loop with the record**, report, stop (BRIEF:19; AOA:186).

---

*Facimus semper — the spec renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION, never a defect; a receipt that points at nothing is the failure class, never a silent pass. The canary's first real run is the customer; this manual is written for that run, not for the lab's convenience.*
