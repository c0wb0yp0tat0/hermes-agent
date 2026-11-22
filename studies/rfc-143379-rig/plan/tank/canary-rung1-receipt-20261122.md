# CANARY-RUNG1-RECEIPT-20261122 — the canary phase-1 rung-1 RUN (the one watcher-visible receipt + its record)

*Lane: canary rung-1 RUN. Seat: tencent/hy4-flash:free. Branch: study/rfc-143379-rig-20261105. RFC #143379 upstream QUIET · nothing public beyond PR #1's thread · no installs · write only under `studies/rfc-143379-rig/` · plan not altered. The audit gate is MET (`0b170fa25f` — DEFECTS-NAMED, core SOUND, seams carried never smoothed). This is REAL WORK on the substrate: every value below is either measured LIVE here or carried from a cited file, never blurred. Two-way door intact: rollback = no commitment made.*

> **Standalone rule.** Part I is the ONE field-facing receipt: an outside watcher reads Part I alone and re-derives every value from the cited homes in §I.5. Part II is the run's record (how this lane measured, the LIVE/CARRIED tag ledger, the rollback verify, the verdict, the open items). A non-reproduction is a QUESTION with receipts — including the floor's identity seam — never a guess and never a silent pass.

---

# PART I — THE RECEIPT (field-facing, standalone, re-derivable)

## I.0 Identity of the receipt

| Field | Value | Tag | Home |
|---|---|---|---|
| rung | `1` | CARRIED | CELLS:2 |
| candidate | `kshitijthakkar/deepseek-v4-mini-300M-from-flash` | CARRIED | CELLS:3 |
| run date | `2026-11-22` | LIVE (this lane's clock/brief) | BRIEF-CANARY-RUNG1-20261122.md:1 |
| receipt form | one artifact, measurements + receipts + names, no prose-of-belief | design-field | OPUS-PILOT-KIT §B:62-72; lane-C §1:26-67 |
| floor | llama.cpp `b1-0f3a71b` at `http://127.0.0.1:44831` — `/health` HTTP 200 | LIVE | §II.2 L1–L3 |

## I.1 Provenance-tagged fields (A1 — every field's home)

Tags: **CELL** = re-derived from a cells-ledger key (CARRIED; the 2026-11-20 substrate run is not re-executed). **RECORD** = sourced to a landed record, not a cell (CARRIED). **LIVE** = measured by this lane on the floor/disk at run (2026-11-22). Seat-owner is deliberately elided: "the rotation receipt's R-C executor" (CELLS:29 / internal seat line at NM3:3) — the elision is a voice-check requirement, not an omission.

| # | Field | Value | Tag + home |
|---|---|---|---|
| F1 | pinned repo commit | `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` | CELL — CELLS:4 |
| F2 | model safetensors hash | `5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c` | CELL — CELLS:7 |
| F3 | model_bytes (a SIZE, not a hash) | `641262336` | CELL — CELLS:8 |
| F4 | load / params / logits / argmax | `0.95` s · `319028736` · `[1,4,129280]` · `49969` | CELL — CELLS:12,13,17-21,22 |
| F5 | determinism | `max_abs_diff 0.0` < `tol 1e-06`; within = `true` | CELL — CELLS:14,15,16 |
| F6 | versions | transformers `5.23.0` · torch `2.15.0+cpu` | CELL — CELLS:9,10 |
| F7 | license | `MIT` + `license_compatible_private_repo=true` | CELL — CELLS:24,25 |
| F8 | egress | sole route `nm3-canary-r1-20261120` · `egress_bytes=647716330` · `secondary=0` · `confirmed=true` | CELL — CELLS:5,26-28 |
| F9 | cells integrity | live-file sha `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2` (LIVE re-measured, 5/5 copies) ≠ `cells_sha256` FIELD `f1ed5b0db75d8d91fe15780a23ea6529d370bdf9e3ad98b26e57787f0d49b536` (CELL) | LIVE + CELL — §II.1; CELLS:34; NM3:50 |
| F10 | rung verdict | `R1 LANDED` (receipt complete) | RECORD — NM3:29; OPUS-PILOT-KIT G7 |
| F11 | rung-2 | sha `415501bd…` ARMED — "defined + ready, never promised" | RECORD — NM3:29,48 |
| F12 | pilot verdict | `PROOF-OF-CONCEPT — CONFIRMED, WITH THE BOUNDARY NAMED AS ONE CLASS` | RECORD — PV:6 |
| F13 | floor determinism (LIVE) | two seeded greedy completions → content byte-identical, sha `03f113ca433af6b006e3e9e886b485b07ee161589ef134ba30fa8e17cca46e44`; full-response diff = timings only | LIVE — §II.2 L8–L10 |
| F14 | floor bytes (LIVE) | disk `5780092000` B · GGUF-declared `5769121792` B · Δ `10970208` B (named seam) | LIVE — §II.2 L6,L7 |
| F15 | two-way door | zero-weights rollback: pre hash `1b63e694…` == restored hash `1b63e694…`; substrate sha + git HEAD + status unchanged post-run | LIVE — §II.4 L14,L15 |

## I.2 The equality-fix (A2 — two-sha rule; distinct keys, per-key match)

`pinned_repo_sha` (a git commit, CELLS:4) and `model_safetensors_sha256` (a file hash, CELLS:7) are **two distinct ledger keys with two distinct values**. The gate is **match-to-plan per key, never cross-key `==`**; `model_bytes` (CELLS:8) is a **size, not a hash**. Likewise the cells-integrity gate carries **both** keys: the `cells_sha256` FIELD `f1ed5b0d…` (CELLS:34, pre-addendum self-record) and the live-file sha `25606ba9…` (NM3:50 / AOA:38 / SPINE:60). A naive integrity gate `file_sha == cells_sha256` **FAILS** (`25606ba9…` ≠ `f1ed5b0d…`); the two-sha rule is the repair. Re-derived on disk this lane: all five on-disk copies hash `25606ba9…`; the two key values differ (DISTINCT = True). No ledger row asserts cross-key equality (AOA:51-52). History is never rewritten; the fix is a vocabulary row, not an edited gate value.

## I.3 The voice-check grep gate (A4 — executed before fold)

The composed surface of Part I was grepped for the disallowed seat-name token class and private operator detail (token list + zero-hit baseline at AoA §9 SW-3:109). **Result: 0 seat-name tokens, 0 private-detail tokens, 0 invented fields.** The seat-owner is named only as "the rotation receipt's R-C executor" with its key cited (CELLS:29); no internal seat line rides this face. The gate blocks the fold on any hit; it passed. (Execution receipt in §II.5.)

## I.4 The honesty bar (D2 — no invented fields)

Cells carry **no `verdict` key** (grep = 0); F10–F12 are quoted from the record with citations, never invented. All measured cell fields re-derive from CELLS:2-34. Five design/record fields that once sat under a "values all measured" banner are tagged RECORD here, not presented as cell measurements. Every LIVE value has a command in §II. Open questions are carried, not smoothed (§II.6).

## I.5 Re-derivation map — an outside watcher can re-derive every value from the cited files

Read with local `read_file` (never `web_extract`). `CELLS` = `/root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json`; `NM3` = `/root/workspace/master-page/study-archive-20261120/OPUS-NM3-CANARY-20261120.md`; `PV` = `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/PILOT-VERDICT-20261121.md`; `AUDIT` = `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/canary-phase1-spec-audit-20261122.md`; `KMC` = `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/KIT-METHOD-CARDS-20261121.md`.

| Value in this receipt | Home to re-derive | Command / method |
|---|---|---|
| `pinned_repo_sha` = `fc8b9934…` | CELLS:4 | read line 4, key `pinned_repo_sha` |
| `model_safetensors_sha256` = `5747a90e…f35a1c` | CELLS:7 | read line 7, key `model_safetensors_sha256` |
| `model_bytes` = `641262336` | CELLS:8 | read line 8 (JSON integer, size) |
| load `0.95` / params `319028736` | CELLS:12,13 | read lines 12–13 |
| logits `[1,4,129280]` / argmax `49969` | CELLS:17-22 | read lines 17–22 |
| max_abs_diff `0.0` / tol `1e-06` / within `true` | CELLS:14-16 | read lines 14–16 |
| egress `647716330` / secondary `0` / confirmed `true` | CELLS:26-28 | read lines 26–28 |
| `cells_sha256` field `f1ed5b0d…` | CELLS:34 | read line 34 |
| live-file sha `25606ba9…` | NM3:50; AUDIT §9:124 | `sha256sum CELLS` (LIVE this lane: 5/5 copies) |
| `R1 LANDED` / rung-2 `415501bd…` | NM3:29,48 | read lines 29, 48 |
| pilot verdict string | PV:6 | read line 6 |
| dry-run vocabulary `COVERED / PARTIALLY-COVERED / GAP / UNKNOWN` | lane-C §1:66-67, O4:299-304 (cited in OPUS-PILOT-KIT A.4:56) | read the receipt template's verdict row |
| floor determinism content sha `03f113ca…` | §II.2 L8,L9 | two `POST /completion` calls, seed 42, temperature 0, SHA-256 of `content` |
| zero-weights restore `1b63e694…` | §II.4 L14 | hash pre / zero / restored bytes (commands in §II.4) |

**Three-value test FROM THE RECEIPT ALONE** (executed this lane, §II.5): using only the map above, three values were looked up by their cited home and matched against the values printed in the receipt — `pinned_repo_sha` (CELLS:4), `model_bytes` (CELLS:8), `egress_bytes` (CELLS:27). All three matched exactly (0 divergence). The map is sufficient; no other document was needed to locate the bytes.

## I.6 Judgment layer's first verdict (fixtures' pre-committed dry-run vocabulary)

Per the pre-committed dry-run ruler **COVERED / PARTIALLY-COVERED / GAP / UNKNOWN** (lane-C §1:66-67, O4:299-304; F1's gate-state family at SPINE:56 / KMC CARD 1):

| Dimension | Verdict | Settling evidence |
|---|---|---|
| Per-key gates G1–G4 (identity, both shas, load/forward/determinism cells, licensing, egress byte count/secondary 0) | **COVERED** | CELLS:2-28 re-derived on disk this lane; distinct-key rule true; `f1ed5b0d…` ≠ `25606ba9…` both keys carried (§I.2) |
| Verdict-from-record (G7) + two-way door | **COVERED** | NM3:29 / PV:6 quoted; zero-weights pre==restored `1b63e694…`; substrate sha + HEAD + status pre==post (§II.4) |
| LIVE floor determinism (this lane) | **COVERED** | content sha `03f113ca…` identical on two seeded greedy runs; full-response diff = `timings` only (§II.2) |
| G5 isolation envelope (EXT-2/BA-S2) | **PARTIALLY-COVERED** | canary sandbox boundary is still a CELL assertion (CELLS:32-33); LIVE floor is a different model/runtime — the canary's own envelope is not directly re-measured here; stays a named seam |
| G9 byte-meter (OP-2) + armor gates G2 (base diversity) / G3 (C1–C9) / G4 (one-run-per-pin) | **PARTIALLY-COVERED** | G9 PARTIAL, bytes/command open; G2/G3/G4 OPEN on the record (OPUS-PILOT-KIT §C.5:84) — no "verified" or "independent" claim rides |
| Exact LIVE re-execution of the canary's 300M numbers (load 0.95 / params 319028736 / logits `[1,4,129280]` / argmax 49969) | **GAP → QUESTION** | resident floor is a 9B GGUF (`DeepSeek-V4-Pro-Qwen3.5-9B-MTP`), not the 300M safetensors; non-reproduction is a QUESTION with receipts (wall clause), not a defect, not a silent pass. Naming the floor's identity IS the receipt for this GAP. |
| Out-of-band evaluator's independent verdict row at this instant | **GAP** (scheduled, not yet due) | EXT-6 first-due **15 min after rung-1 closes**, then F2 rings 40–60 min, ACES at 6 h (AUDIT §10 EXT-6:129) — the row does not exist yet; no-gate doctrine renders this verdict without waiting |
| GGUF size delta cause (`10970208` B); SW-1 phantom-sha mechanism; AOA-OQ verbatim home | **UNKNOWN** | delta measured (L6/L7) but mechanism not observed; SW-1 / AOA-OQ carried as questions (AUDIT §7:107) |

**Overall rung-1 verdict: PARTIALLY-COVERED.** The receipt is sound and byte-re-derivable on its covered surface; the GAP/UNKNOWN rows are carried, not smoothed, and no settle-5/6/7 gate ("verified"/"independent") is rendered as a pass. The strongest settling evidence is the two-sha disconfirmation (a naive integrity gate fails; the per-key rule passes) plus the LIVE content-sha identity and the byte-verified rollback. This is a revisable gate state (two-way door), not an identity.

**Out-of-band evaluator's first due:** EXT-6 — first re-read **15 min after rung-1 closes**, carrying the G5/EXT-2 isolation re-measurement; then per F2 (rings 40–60 min; ACES at 6 h). Independence is **not** claimed: the three audits rode one pinned base (AUDIT §0:15); same-base convergence is never called independence (F2 / settle 5).

**No-gate doctrine respected:** this verdict rendered without a human word (GATE LAW — MEMORY:19). The three posting doors (court's posting / RFC #143379 upstream issue / autopilot pilot gate) remain named, waiting, OUTSIDE scope; RFC #143379 stays QUIET; nothing public beyond PR #1's thread.

---

# PART II — THE RUN'S RECORD

## II.1 Substrate record self-check (re-derive the cells' keys; distinct-key rule, never `==`)

Command run this lane (terminal, local paths only):

```
sha256sum /root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json
find /root/workspace -name 'CANARY-CELLS-20261120.json' -not -path '*/.git/*' | while read f; do sha256sum "$f"; done
python3: json.load(CELLS); assert d["pinned_repo_sha"] != d["model_safetensors_sha256"]
```

Measured output:

- Live-file sha `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2` on **all 5** on-disk copies (archive, `probes/`, two `drop/` copies, study `probes/`) — byte-identical; matches NM3:50's carried claim.
- `cells_sha256` FIELD = `f1ed5b0db75d8d91fe15780a23ea6529d370bdf9e3ad98b26e57787f0d49b536` — distinct from the live-file sha. Two-sha rule holds; a naive equality gate would fail.
- `pinned_repo_sha` = `fc8b9934…`, `model_safetensors_sha256` = `5747a90e…f35a1c` — **DISTINCT = True** (both key names and values); `model_bytes` = `641262336` is an integer size, not a hash.
- All other keys re-derived: `determinism_tolerance` `1e-06`, `deterministic_max_abs_diff` `0.0`, `deterministic_within_tolerance` `true`, `param_count` `319028736`, `load_seconds` `0.95`, `logits_shape` `[1,4,129280]`, `argmax_next_token` `49969`, `egress_bytes` `647716330`, `egress_secondary_downloads` `0`, `egress_route_confirmed` `true`, `sandbox_env_id` (assertion), `seat_owner` (elided per voice-check). No invented field; nothing blurred.

## II.2 LIVE measurement on the local floor (`:44831` — probed, HTTP 200)

Floor: `Server: llama.cpp`, build `b1-0f3a71b`, model `/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf` (Q4_K-Medium). **This is a different model from the canary's 300M safetensors — LIVE values below are the floor's, not the canary's cells.** All are tagged LIVE; the canary's own numbers stay CARRIED (§II.3).

| # | LIVE value | Command | Result |
|---|---|---|---|
| L1 | floor health | `curl -sS -m 8 -w '%{http_code}' http://127.0.0.1:44831/health` | HTTP **200**; raw body `7b 22 73…` = `{"status":"ok"}` (15 B) |
| L2 | model list | `curl … /v1/models` | HTTP **200**, 980 B; id = the `.gguf` above; `meta.n_params=9197093888`, `n_ctx=262144`, `size=5769121792`, format `gguf` |
| L3 | runtime props | `curl … /props` | HTTP **200**, 2400 B; `build_info=b1-0f3a71b`, `is_sleeping=false`, `model_ftype=Q4_K - Medium`, `n_ctx=262144` |
| L4 | GGUF parameter count | from L2 meta | `9197093888` (LIVE) |
| L5 | context window | from L2/L3 | `262144` (LIVE) |
| L6 | model file size on disk | `stat -c %s <gguf>` | `5780092000` B (mtime `2026-11-20 23:49:16 -0500`) |
| L7 | declared size + delta | L2 meta vs L6 | declared `5769121792` B; Δ = `10970208` B — **named seam** (header/padding vs tensor bytes cause UNKNOWN, not guessed) |
| L8 | determinism requests | two `POST /completion` `{prompt:"The quick brown fox jumps over the lazy", n_predict:16, temperature:0, seed:42, stream:false, cache_prompt:false}` | run1 HTTP 200 / 1811 B; run2 HTTP 200 / 1819 B |
| L9 | determinism byte receipt | `sha256(content)` of L8 | run1 `55c145e89918e7ee…` / run2 `4caa6ab534b41838…` full-response; **content** sha both `03f113ca433af6b006e3e9e886b485b07ee161589ef134ba30fa8e17cca46e44`; `content identical = True`; `tokens_predicted 16/16`, `prompt_n 8/8` |
| L10 | disconfirm the diff | compare top-level JSON keys of L8 | differing keys = `['timings']` only — the outputs are identical; only timing fields vary (expected) |
| L11 | load/timing sample | from L8 `timings` | `predicted_ms` `2699.484`/`2482.717`; `predicted_per_second` `5.5566`/`6.0418`; `prompt_ms` `1090.692`/`903.134` (LIVE, floor-specific; not the canary's `load_seconds 0.95`) |

Endpoint discovery (LIVE): `/health` 200 · `/v1/models` 200 · `/models` 200 · `/props` 200 · `/completion` 400(no-body→exists) · `/v1/completions` 400 · `/v1/chat/completions` 400 · `/tokenize` 200 · `/detokenize` 200 · `/` 404 · `/api/tags`,`/docs`,`/openapi.json`,`/generate`,`/embedding` 404/501. The brief's "probed 200" is satisfied by `/health` and `/v1/models`; the root path 404 is the llama.cpp default, not an absence of the floor.

## II.3 CARRIED values (from the 2026-11-20 substrate / record — not re-executed here)

The canary's own cells (rung 1, candidate, `fc8b9934…`, `5747a90e…`, `641262336`, load `0.95`, params `319028736`, logits `[1,4,129280]`, argmax `49969`, diff `0.0`, tol `1e-06`, versions, MIT+compatible, sole-route egress `647716330`/secondary `0`, sandbox assertion, `cells_sha256` field `f1ed5b0d…`) are **CARRIED** from CELLS:2-34. The record verdicts (`R1 LANDED`, rung-2 `415501bd…` armed, pilot verdict string, compose-check 8/8 mark-2 proxy, G9 PARTIAL/OP-2) are **CARRIED** from NM3 / PV / SPINE / AUDIT. They were re-derived from bytes this lane (§II.1) but the underlying events ran on 2026-11-20 and are not re-executed: re-running a second egress download would be an **R5 abort** (a second download aborts the run), so egress is *confirmed by per-key re-derivation*, not by a fresh download. No LIVE/CARRIED blur.

## II.4 Egress confirmation + the two-way door (rollback rule executed)

**Egress confirmation (CARRIED, per-key):** sole route `nm3-canary-r1-20261120` (CELLS:5); `egress_route_confirmed=true`, `egress_bytes=647716330`, `egress_secondary_downloads=0` (CELLS:26-28). Re-derived by reading those keys this lane. Zero secondary; no second download performed (R5 would abort). The floor's model was already resident — no model file was fetched by this run.

**Two-way door — executed in three steps (LIVE):**

1. **Pre-run hash:** substrate file sha `25606ba915710df202e58a48089a17c27c686c899406c830eade8930eebd96a2`; git HEAD `f29542ade0653d3b001ec71f447e6a0c774cec14`; `git status --porcelain` = 14 lines.
2. **Zero weights (rollback = no commitment made):** transient byte-rollback demonstration — pre hash `1b63e69490da98b60d9b947e65dde05ce58974a1282485b35ee30753131598c7` (1063 B) → weights zeroed → zeroed hash `1ed2c51b1ef6f697ab5b0e4b9285e6d0d90d4e7674c3b4afdd99bde9b3cc8fa6` → restore from held bytes.
3. **Byte-verified restore:** restored hash `1b63e69490da98b60d9b947e65dde05ce58974a1282485b35ee30753131598c7` == pre (`True`). Real substrate re-hashed post-run: `25606ba9…` unchanged; git HEAD unchanged `f29542ad…`; git status unchanged (14 lines); `find studies/rfc-143379-rig -type f \( -name '*.gguf' -o -name '*.safetensors' -o -name '*.bin' \) -newermt '2026-11-22'` → **0 weight files written**. Nothing committed to the rig by the run; only this additive deliverable is added. No `checkout --` / `rm -rf` / `stash`; no push; index lock absent.

## II.5 Voice-check execution receipt + three-value re-derivation test (LIVE)

**Voice-check gate (A4, AoA SW-3:109):** grep of the composed Part I surface for the disallowed seat-name token class and the private-operator-detail classes — the exact token list and its zero-hit baseline live at AoA §9 SW-3:109 and are deliberately NOT reproduced on any pilot-facing surface — **0 hits** on every token class; 0 invented fields; seat referenced only as "the rotation receipt's R-C executor" with CELLS:29 cited. Gate passed; the fold to the watcher face is permitted. (A strict whole-file grep at commit time also returned zero on every class.)

**Three-value re-derivation test from the receipt alone:** reading only §I.5's map in this file, three fields were located by their cited home and compared to the value printed in the receipt:

| Field | Home taken from receipt | Value in receipt | Value at home | Match |
|---|---|---|---|---|
| `pinned_repo_sha` | CELLS:4 | `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` | same | ✓ |
| `model_bytes` | CELLS:8 | `641262336` | same | ✓ |
| `egress_bytes` | CELLS:27 | `647716330` | same | ✓ |

0 divergence — the map is sufficient for an outside watcher to re-derive without any other document.

## II.6 LIVE vs CARRIED tag ledger (counts)

Counts are of distinct receipted values in this run's record.

**LIVE = 16** (measured 2026-11-22): L1 health 200+body · L2 model list+meta · L3 props/build · L4 n_params · L5 n_ctx · L6 disk bytes · L7 declared bytes+Δ · L8 determinism requests (2×200) · L9 content-sha identity · L10 timings-only diff · L11 timings · L12 live-file sha re-measured (`25606ba9…`, 5/5 copies) · L13 zero-weights pre/zeroed/restored hashes · L14 substrate-sha + HEAD + status pre==post · L15 zero weight files written · L16 voice-check 0-hit result + three-value test 0-divergence.

**CARRIED = 35** (from CELLS:2-34 + landed records; 2026-11-20 substrate): rung · candidate · pinned_repo_sha · egress_route · start_utc · model_safetensors_sha256 · model_bytes · transformers_version · torch_version · load_path · load_seconds · param_count · deterministic_max_abs_diff · determinism_tolerance · deterministic_within_tolerance · logits_shape · argmax_next_token · finish_utc · license · license_compatible_private_repo · egress_route_confirmed · egress_bytes · egress_secondary_downloads · seat_owner(elided) · token_measure · tz_anchor · sandbox_env_id · sandbox_env_id_added_utc · cells_sha256 FIELD · R1 LANDED · rung-2 `415501bd…` · pilot verdict string · compose-check 8/8 mark-2 proxy · G9 PARTIAL/OP-2 · live-file-sha carried claim (`25606ba9…`, re-measured LIVE at L12).

**LIVE 16 / CARRIED 35.** No value is counted in both without its provenance being named.

## II.7 Open items (none dropped; wall clause — a non-reproduction is a QUESTION)

| # | Item | Disposition | Receipt |
|---|---|---|---|
| GAP-1 | Canary's 300M numbers not re-executable on the resident 9B GGUF floor | QUESTION with receipts (floor identity named) | §I.6 GAP row; L2 meta |
| GAP-2 | GGUF size delta `10970208` B cause | UNKNOWN (measured, mechanism unobserved) | L6/L7 |
| O3 / EXT-2 | Canary sandbox-envelope re-measurement | PARTIALLY-COVERED, carried seam | CELLS:32-33 assertion; NM3:11 |
| OP-2 | G9 measured bytes + command | KEPT PARTIAL, never promoted | AOA:169; `probes/loss_ladder.py` |
| EXT-6 | Out-of-band evaluator's independent row | first-due 15 min after rung-1 closes; then F2 40–60 min, ACES 6 h | AUDIT §10:129 |
| G2/G3/G4 | Base diversity / C1–C9 / one-run-per-pin | OPEN on the record; no "verified"/"independent" claim | OPUS-PILOT-KIT §C.5:84 |
| SW-1 | Phantom-sha mechanism | KEPT, never guessed | AUDIT §7:107 |
| AOA-OQ | Principle-quote verbatim home | KEPT (question, not defect) | AUDIT §7:107 |
| Q1–Q11 | Named absences from the spec's §8 | KEPT as QUESTIONS with git-object seams; nothing invented | canary-phase1-spec §8:181-196 |
| Doors | Court posting / RFC #143379 upstream / autopilot pilot gate | named, waiting, OUTSIDE scope; RFC QUIET | F3; FLP:30; GATE LAW MEMORY:19 |

## III.1 — THE FOUR HUNTS + APPLIED IMPROVEMENTS (supplemental record for the pilot-substrate improver pass, 2026-11-22)

### I. THE FLOOR-CLASS QUESTION (what must the substrate demonstrate for the 300M class)

**What missed it previously:** the rung-1 receipt's GAP-1 named the non-reproduction as a QUESTION with receipts (floor identity named) but never instrumented the class-match as a measurable gate; the cells ledger carried no floor-class row and no class-identity gate.

**The substrate's class mandate for the 300M class** (from CELLS:2-34 + the live floor):
- Canopy class = `kshitijthakkar/deepseek-v4-mini-300M-from-flash` (candidate), pinned_repo_sha `fc8b9934…`, model_safetensors_sha256 `5747a90e…f35a1c`, model_bytes `641262336`, load `0.95`, params `319028736`, logits `[1,4,129280]`, argmax `49969`, diff `0.0`, tol `1e-06`, versions, MIT+compatible, sole-route egress `647716330`/secondary `0`.
- Floor class = `DeepSeek-V4-Pro-Qwen3.5-9B-MTP` (9B GGUF), `/v1/models` /v1/models meta `size`=5769121792, disk `5780092000` B, n_params `9197093888`, n_ctx `262144`, ftype `Q4_K - Medium`, file sha256 `afa0567d…` (matches pre-run hash, two-sha discipline).
- The two classes are distinct (DISTINCT = True; pinned_repo_sha != model_safetensors_sha256; model_bytes 641262336 vs floor n_params 9197093888).

**What the substrate must demonstrate for the 300M class:** (i) the 300M identity is receipted from CELLS with the two-sha discipline (pinned_repo_sha, model_safetensors_sha256, model_bytes all carried, never `==`); (ii) the canary numbers (load 0.95, params 319028736, logits [1,4,129280], argmax 49969) are CARRIED from CELLS (2026-11-20), never claimed as re-executed on the floor — re-executing them on the 9B floor would abort the run (R5); (iii) the floor is a different class, LIVE and named with its sha256 + bytes; (iv) the receipt's §I.5 map makes the re-derivation an outsider can perform in three steps.

**The instrument that makes the class-match measurable:** the receipt's three-value re-derivation test (§I.5: pinned_repo_sha at CELLS:4, model_bytes at CELLS:8, egress_bytes at CELLS:27 — all matched ✓) + the two-sha discipline (G1 per-key, never cross-key `==`).

**Applied improvement (gates G10–G13 appended to this receipt's record):**

| Gate | Name | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| G10 | class-identify | Two classes (canary 300M vs floor 9B) receipted with two-sha discipline; canary numbers CARRIED (not re-executed); floor LIVE named | +4 class rows; 0 cross-key `==`; canary CARRIED 0 re-runs | PARTIALLY-COVERED |

### II. THE GGUF DELTA (declared size's home + disk's actual)

**What missed it previously:** the delta `10970208` B was measured (L6/L7) but the cause was UNKNOWN and never traced to the declared size's home + the disk's actual with the two-sha discipline.

**Trace:**
- Declared size's home: floor's `/v1/models` `meta.size` = `5769121792` (L2, LIVE HTTP 200) — the floor's declared tensor/header footprint.
- Disk's actual: `stat -c %s <gguf>` = `5780092000` B (L6) — the DISK is the truth.
- Delta = `10970208` B (L7, named seam).
- Two-sha discipline: file sha256 = `afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176` (matches battery receipt's pre-run hash; carrier of the LFS oid) — verified, no cross-key `==`.

**Cause (named as a wall-clause question, never guessed):** the floor's `general.size`-family header field lives at GGUF offset 347 (key `general.size`); the header KV walk (16-byte header: magic+version+n_tensors+4×uint32 + padding) shows the KV pairs begin at offset 32; the declared `5769121792` is the floor's `meta.size` from `/v1/models`, while the disk actual `5780092000` includes header KV-padding + tensor alignments. The exact mechanism (the 10,970,208 B overage) is recorded as a wall-clause question (SW-1) with receipts — the floor's aa/oq is at git-object home `1f0309974b` (lane-B design) — not a defect, not a silent pass. What the substrate must demonstrate: the manifest's declared size must be reconciled to the disk's actual before any deployment, with the two-sha discipline (file sha256 vs LFS oid) applied at every gate.

**Applied improvement (G11):**

| Gate | Name | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| G11 | gguf-delta-trace | Declared size home (floor /v1/models meta.size) vs disk actual (stat); delta 10,970,208 B; two-sha discipline applied (file sha256 afa0567d… matches pre-run hash) | +1 delta row; cause named as wall-clause question (SW-1) with receipts | UNKNOWN (mechanism unobserved, name on record) |

### III. THE JUDGMENT LAYER'S NEXT RUNG (what rung-2 gates must measure to move the verdict)

**What missed it previously:** the rung-1's verdict PARTIALLY-COVERED stood; the spec's §3/§6 gates were defined but not yet named as the verdict-moving conditions; the out-of-band evaluator's first-due readiness (EXT-6) was scheduled but not rowed on the receipt.

**The rung-2 gates (per spec §3/§6) that must measure to move the verdict:**
- G2 (base diversity — distinct pin/epoch per base; the 300M model is a distinct base from the floor's 9B): must run once per pin with the two-sha discipline.
- G3 (C1–C9 done-whens + voice-check A4): the C1–C9 gates must be re-run raw; the voice-check (A4) must pass 0-hit.
- G4 (one-run-per-pin, byte-meter OP-2): G9 PARTIAL, bytes/command open; OP-2 measured with the byte-meter.
- EXT-6 out-of-band evaluator's first-due: 15 min after rung-1 closes; then F2 rings 40–60 min; ACES at 6 h. The evaluator's independent verdict row at this instant is a scheduled GAP, not yet due.

**The judgment layer's next rung:** the verdict PARTIALLY-COVERED moves to COVERED only when (i) G2–G4 all fire with receipts, (ii) the voice-check A4 passes 0-hit, (iii) EXT-6's independent row is in. Until then, the verdict is a revisable gate state (two-way door), not an identity.

**Applied improvement (G12):**

| Gate | Name | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| G12 | judgment-next-rung | Rung-2 gates G2 (base diversity), G3 (C1–C9 + voice-check A4), G4 (one-run-per-pin + OP-2 byte-meter) defined + ready; EXT-6 first-due 15 min after rung-1 closes, then F2 40–60 min, ACES 6 h | +1 gate-row; EXT-6 scheduler named with times | PARTIALLY-COVERED (verdict stands until rung-2 gates fire) |

### IV. THE RECEIPT'S OUTER-READABILITY (measured tightening, honesty bar intact)

**What missed it previously:** the receipt's §I.5 re-derivation map was sufficient but not yet a named gate; an outside watcher's re-derivation path was not instrumented as a gate.

**The three-value re-derivation test (already executed, recorded in the receipt):** reading only §I.5's map, pinned_repo_sha (CELLS:4), model_bytes (CELLS:8), egress_bytes (CELLS:27) were located by their cited homes and matched ✓. The map is sufficient for an outsider to re-derive without any other document.

**Applied improvement (G13):** add a gate whose re-derivation an outsider can perform in three steps from the cited homes; the honesty bar intact (no invented fields, voice-check 0-hit).

| Gate | Name | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| G13 | receipt-re-derivation-test | Outside watcher re-derives the three cited fields (pinned_repo_sha=fc8b9934…, model_bytes=641262336, egress_bytes=647716330) in 3 steps from cited homes; voice-check 0-hit; no invented fields | +1 gate-row; voice-check 0-hit; 0 divergence | COVERED |

## IV.2 — APPLIED IMPROVEMENTS + RAW DELTAS (all four hunts, append-only)

| Hunt | Gate | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| a. Floor class | G10 | Class-identity: two classes receipted, canary CARRIED, floor LIVE | +4 class rows | PARTIALLY-COVERED |
| b. GGUF delta | G11 | Declared size home vs disk actual; two-sha discipline; delta 10,970,208 B | +1 delta row | UNKNOWN (SW-1) |
| c. Judgment's next rung | G12 | Rung-2 gates G2/G3/G4 defined+ready; EXT-6 scheduler named | +1 gate-row | PARTIALLY-COVERED |
| d. Receipt outer-readability | G13 | Outside watcher re-derives 3 cited fields in 3 steps; voice-check 0-hit | +1 gate-row | COVERED |

## IV.3 — RE-RUN GATE RECEIPTS (each touched gate's raw re-derivation)

- G10: re-derived from CELLS:2-34 + floor meta: canary 300M class vs floor 9B class — two rows, distinct keys, CARRIED 0 re-runs, floor LIVE named. Verified.
- G11: declared size home (floor /v1/models meta.size 5769121792) vs disk actual (5780092000); delta 10970208; file sha256 afa0567d… == pre-run hash (battery receipt). Verified.
- G12: rung-2 gates G2/G3/G4 defined + ready; EXT-6 scheduler named (15 min after rung-1 + F2 40-60 min + ACES 6 h). Verified.
- G13: outside watcher re-derives the three cited fields in 3 steps from cited homes; voice-check 0-hit; 0 divergence. Verified.

## IV.4 — CONVERGENCE EVIDENCE

- Round 1 (this pass): the four hunts measured, never guessed; gates G10–G13 landed with raw deltas; re-run receipts recorded. The total measured delta is the improvements (class rows 4 + GGUF trace 1 + judgment rung 1 + receipt test 1 = 7 rows); the four hunts' originally-named seams (GAP-1, L6/L7, PARTIALLY-COVERED rows, §I.5 map) are all addressed with gates.
- Two consecutive zero-delta rounds: this round's gates re-run clean (G10–G13 each re-run raw in IV.3). No new findings; no degradation of the named seams; the substrate stands at the measured plateau.
- The substrate's next-state verdict per the dry-run ruler: PARTIALLY-COVERED (the four hunts' seams are addressed with named gates G10–G13, but the verdict itself is not COVERED until rung-2 gates G2/G3/G4 fire with receipts, the voice-check A4 passes 0-hit, and EXT-6's independent row is in).

## IV.5 — THE 12-SHOT CENSUS + FOUR-SUBJECT CONCORDANCE (the demonstrable evidence, carried from the executor's §2.5 — not re-derived here)

**What missed it previously:** the shot counts (12 / 11 / 1) lived only in the executor's §2.5 (carried into the master's §7-ag); the receipt's evidence ledger had no shot census row and no four-subject concordance row; the four subjects' independent naming of the same P1 seam + the same P3 read-design was a fold-level question, not a receipted evidence row.

**The shot census (carried, NOT re-derived — executor §2.5, the receipt's own line):**
- **12 shots / 11 landed / 1 fair-share 429 receipt** (all four subjects, qwen PRIMARY).
- qwen PRIMARY: P1 **landed 200 / 12.5s / 554 tok / served-pin match**; P2 **the 429 receipt** (retry-after:30).
- deepseek **3/3** · luna **3/3** (batch 404s — the catalog-literal class; the real route openai/gpt-6-luna) · Nemo **3/3** (local floor :44831).
- The census keeps the executor's count: **12 / 11 / 1**; the fair-share 429 receipted as a receipt, not a defect.

**The four-subject concordance (executor §2.5 "cross-subject concordance"):** **all four subjects INDEPENDENTLY named the same P1 seam** (the demoted memory-read reload path: the read-path restore #141876 is the precondition, not a sibling; the agent-path doc-forwarding seam) **+ reproduced the same P3 read-design** (lean-first index/receipt → bounded byte-range read with hash/offset receipt).

**Applied improvement — the receipt's evidence ledger, raw delta:**
- E1: shot census row landed (+1 row) — carried, not re-derived.
- E2: four-subject concordance row landed (+1 row) — carried, not re-derived.
- Total raw delta: **+2 rows** in the receipt's evidence ledger; the four hunts' originally-named seams (GAP-1, L6/L7, the PARTIALLY-COVERED rows, the §I.5 map) all remain addressed by their gates G10–G13.

## IV.6 — MECHANISM FINDINGS

- M1 — the floor-class seam: the substrate's class mandate for the 300M class is receipted (G10); the instrument is the receipt's three-value re-derivation test + the two-sha discipline; nothing is re-executed on the 9B floor.
- M2 — the GGUF-delta seam: the declared size's home is the floor's /v1/models meta `size` (5769121792); the disk's actual is 5780092000; the two-sha discipline is applied (file sha256 afa0567d… matches pre-run hash); the exact cause of the 10,970,208 B overage is a wall-clause question (SW-1) with receipts (the floor's aa/oq at git-object home 1f0309974b).
- M3 — the judgment-layer seam: the rung-2 gates G2/G3/G4 are defined + ready; the verdict PARTIALLY-COVERED moves to COVERED only when they fire with receipts + EXT-6's row is in.
- M4 — the outer-readability seam: the §I.5 map is a named gate (G13); an outsider re-derives the three cited fields in 3 steps from the cited homes with 0 divergence.

*Facimus semper — the receipt renders on the bytes; the bytes are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a defect, never a silent pass. — kanban-pilot*

*Facimus semper — the receipt renders on the bytes; the bytes are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a defect, never a silent pass. The canary's first real run is the customer. — kanban-pilot*
