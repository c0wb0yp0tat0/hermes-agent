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

## II.8 Review round / termination (one, then stop)

Adversarial re-read: equality-fix (§I.2) re-derived from CELLS:4/7/8/34 — no cross-key `==`, two shas distinct ✓; voice grep 0 hits ✓; three-value test 0 divergence ✓; rollback pre==post ✓; determinism diff = timings-only (disconfirm of a false "outputs differ" reading) ✓. The two-sha disconfirm and the floor's non-reproduction are named, not smoothed. After this round no further measurable change is available (a second read of the same bytes yields no change ×2) → **PARK the improvement loop with the record**, report, stop.

---

*Facimus semper — the receipt renders on the bytes; the bytes are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a defect, never a silent pass. The canary's first real run is the customer. — kanban-pilot*
