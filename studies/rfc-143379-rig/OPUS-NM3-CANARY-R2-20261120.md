# OPUS-NM3-CANARY-R2-20261120 — Rung-2 receipt (NM-3 canary, V3-3.4B-small)

**Seat (named rotation):** kenari reserve beam (`reflection/beam-1.0-501b-a23b`) — R-C executor (select leg, probe-before-use, STEER-10); verifier pair (Conflict-1, non-author): longcat + solar-mini4. **Branch:** study/rfc-143379-rig-20261105 · **RFC:** quiet · **Gate (verbatim):** "the gate: nothing public without the user's word."

## 1. Cells / evidence read (not the summary)
Rung=2 · candidate=`inference-optimization/DeepSeek-V3-3.4B-A3.0B-small` (V3-3.4B-small) · pinned sha `415501bd60fa678ca170c0179642545d5b7a5f32` (DARKHORSE-TRACK-1 / OPUS-2-PLAN-C & -F / LENS-E A4). Egress route = private repo release `nm3-canary-r2-20261120` (sole route; tag published 2026-11-20T13:34:55Z). License (live card): MIT. Sandbox run UTC 2026-11-20T08:40Z→08:42Z.

## 2. Five gate fields, each traced
(1) **Sandbox env id + isolation boundary** — CONFIRMED. `sandbox_env_id` = `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve); isolation: ephemeral venv /tmp/sandbox-r2/venv (RAM-backed tmpfs; /dev/shm work + base site-packages via hermes-agent venv; transformers 5.17.0 / torch 2.14.0+cu130 on CPU, bf16); model pulled ONLY from private release nm3-canary-r2-20261120; no rig disk state touched; no production seat; no HF download in sandbox.` egress_route_confirmed=true.

(2) **Model sha == staged pin** — CONFIRMED. staged pin (private-release course) = HF commit `415501bd60fa678ca170c0179642545d5b7a5f32`; live HF `model_info` sha = identical (verified 2026-11-20 via huggingface_hub, unauthenticated). model_safetensors_sha256 = `1b72ab1e4597e363907254806a4f0b9d52f7c01404744b234ba6ffabcd5067b3` (HF blob b5d4a49d…, 6,745,545,928 bytes); reassembled-from-5-shards sha byte-identical → release round-trip verified. param_count = 3,372,768,256 (3.4B).

(3) **Load + determinism** — CONFIRMED. load_seconds=1.152, param_count=3,372,768,256, logits_shape=[1,2,129280], argmax_next_token=1026, deterministic_max_abs_diff=0.0, tolerance 1e-6 → deterministic_within_tolerance=true. Native deepseek_v3 config supported by transformers (no wall; contrast R1's compress_ratios=48 rejection). transformers 5.17.0 / torch 2.14.0+cu130 (CPU, bf16), model.eval(), torch.no_grad.

(4) **Licensing** — CONFIRMED (live card read). license="mit" (HF model card: front-matter `license: mit`, tags include `license:mit`, base_model deepseek-ai/DeepSeek-V3-Base, transformers/safetensors text-gen MoE). license_compatible_private_repo=true. (Verified live via huggingface_hub.model_info + README.md front matter.)

(5) **LFS egress = sole route** — CONFIRMED. egress_route_confirmed=true; sole route private release `nm3-canary-r2-20261120` (11 assets: config, gen_config, tokenizer, tokenizer_config, chat_template, README + 5×1.5GB safetensors shards due to the 2GB/asset cap); egress_bytes=6,755,531,557 (model 6,745,545,928 + 9,985,629 small); egress_secondary_downloads=0. One-way store, byte-counted, RFC quiet.

## 3. NM-2's two fields + seat-owner
- token_measure: "0 provider calls (mechanical sandbox run; no LLM tokens consumed; bank read not needed)".
- tz_anchor: "UTC".
- seat_owner: "none at dispatch (R-C executor = kenari reserve beam, probe-before-use; assigned by rotation receipt)".

## 4. Verdict
All five fields CONFIRMED; byte receipts in this artifact cover the staged bytes and the load/determinism outputs. **R2 LANDED** (receipt complete) on V3-3.4B-small sha `415501bd…`. Rung-3 not armed here (no next rung pinned); the champion row's call is the next move. Two-way door intact: sandbox torn down (tmpfs /tmp + /dev/shm released), release stays as off-rig disk (one-way; costless to drop), exit commits only this landing — rollback = delete the release + this file, no rig state touched, no model on rig disk. Pivot owner of record for any future termination = verifier pair (longcat + solar-mini4).
Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised." (No wall encountered this rung; seam record = none.)

## 5. COMPOSE-CHECK TABLE
| # | mark | status | evidence |
|---|------|--------|----------|
| 1 | M1 seat-lease via rotation receipt (not self-declared) | FIRED | seat_owner by rotation receipt |
| 2 | M2 sandbox isolation boundary (env_id staged from start) | FIRED | env id + boundary §2(1) |
| 3 | M3 model sha == staged pin | FIRED | live HF sha == pin + byte-identical reassembly |
| 4 | M4 load + forward + determinism 0.0 | FIRED | load 1.152s, max_abs_diff 0.0 (<1e-6) |
| 5 | M5 licensing (MIT, compatible) | FIRED | live card read license:mit |
| 6 | M6 LFS egress, byte-counted, zero secondary | FIRED | egress_bytes=6,755,531,557, secondary=0 |
| 7 | M7 record-first wall clause applied | FIRED | no gaps; no "not confirmed" unresolved |
| 8 | M8 two-way door / rollback (no commitment on rig) | FIRED | sandbox torn down, LFS one-way |
All 8 marks FIRED.

## 6. Review-loop record
Adversarial pass (self): re-read live HF sha + card + sandbox receipt.json cold against §2 — mapping unchanged; SHA round-trip verified byte-identical (1b72ab1e…); no invention; the 5-shard split is a mechanical staging detail, not a claim change. Second re-read introduced NO changes → termination (no-change re-read ×2 satisfied). Verifier pair (longcat + solar-mini4) remains non-author adjudicator of record; no external lanes; no public posts. Chars checked ≤6,000 before write.
Fold line: R2 LANDED — five-field receipt complete on V3-3.4B-small sha 415501bd…; verifiers longcat+solar-mini4 read at the fold; RFC quiet; door open.
Loop-state: **CONTINUE** (next canary rung or the champion row's call).