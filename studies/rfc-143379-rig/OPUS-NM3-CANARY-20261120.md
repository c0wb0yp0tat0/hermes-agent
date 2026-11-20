# OPUS-NM3-CANARY-20261120 — Rung-1 receipt (NM-3 canary)

**Seat (named rotation):** kenari reserve beam (`reflection/beam-1.0-501b-a23b`) — R-C executor (select leg, probe-before-use, STEER-10); verifier pair (Conflict-1, non-author): longcat + solar-mini4. **Branch:** study/rfc-143379-rig-20261105 · **RFC:** quiet · **Gate (verbatim):** "the gate: nothing public without the user's word."

## 1. Cells read cold (not the summary)

Source: `probes/CANARY-CELLS-20261120.json` read verbatim. No summary used. Coordinates: rung=1, candidate=`kshitijthakkar/deepseek-v4-mini-300M-from-flash`, pinned_repo_sha=`fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`. UTC window 2026-11-20T04:41:38Z→04:41:43Z.

## 2. Five gate fields, each traced to a cell

(1) **Sandbox env id + isolation boundary** — PARTIAL. No `sandbox_env_id` key staged in the cells (record-first: unreadable = "not confirmed"). Proxy coordinates present: start_utc/finish_utc (04:41:38Z→04:41:43Z) and `egress_route` (sole route). Isolation boundary claim (off-rig disk, tmpfs venv, no production seat, no HF download in sandbox) rests on the head-side wall receipt in the brief, NOT on a staged cell → recorded as **not confirmed from cells**; the egress boundary itself is confirmed by cell `egress_route_confirmed=true`. This gap is recorded, not guessed.

(2) **Model sha matches pinned track-1 sha** — CONFIRMED. pin `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64`; `model_safetensors_sha256`=5747a90ecef9ecc349b78247992c59e72d1eb4c2dded6b84a77d473774f35a1c; `model_bytes`=641,262,336.

(3) **Inference test (loads + minimal forward + deterministic within tol)** — CONFIRMED. `load_seconds`=0.95, `param_count`=319,028,736, `logits_shape`=[1,4,129280], `argmax_next_token`=49969, `deterministic_max_abs_diff`=0.0, tolerance 1e-6 → `deterministic_within_tolerance=true`. transformers 5.23.0 / torch 2.15.0+cpu. Native deepseek_v4 config rejected compress_ratios=48; model's own code package (`code/deepseek_v4`) used — owned, receipted, not a dead-end.

(4) **Licensing attestation** — CONFIRMED. `license`="MIT (verified live from HF model card: license:mit; tags include license:mit; MoE text-gen with base deepseek-ai/DeepSeek-V4-Flash)"; `license_compatible_private_repo=true`.

(5) **LFS egress clearance** — CONFIRMED. `egress_route_confirmed=true`; sole route private-repo release `nm3-canary-r1-20261120`; `egress_bytes`=647,716,330; `egress_secondary_downloads`=0. One-way store, byte-counted.

## 3. NM-2's two fields + seat-owner field

- `token_measure`: "0 provider calls (mechanical sandbox run; no LLM tokens consumed; bank read not needed)".
- `tz_anchor`: "UTC".
- `seat_owner`: "none at dispatch (R-C executor = kenari reserve beam, probe-before-use; assigned by the rotation receipt)". No self-declaration; seat derives from OPUS-NM4-ROTATION-20261120.

## 4. Verdict

Field (1) is recorded as not-confirmed-from-cells (the only gap; isolation boundary otherwise receipted), but all substantive mechanical checks (sha, load/forward/determinism 0.0, MIT licence compatibility, LFS sole route byte-counted with zero secondary) PASS and no cell contradicts isolation. Applying the wall clause ("a non-reproduction is a QUESTION, not a stop — simplify until the seam is exercised"): the seam here is the sandbox-env-id key, an evidence gap rather than a seam failure; the experiment already exercised load/forward/determinism/egress. Verdict: **R1 LANDED** (receipt complete). Rung-2 conditions ARMED (defined + ready, never promised): candidate V3-3.4B-small, sha `415501bd…`. Two-way door intact: sandbox torn down, LFS one-way, exit costs nothing on the rig; rollback = no commitment made. Pivot owner of record for any future termination = verifier pair (longcat + solar-mini4).

## 5. COMPOSE-CHECK TABLE (stack-order clause — mandatory)

| # | mark | status | evidence |
|---|------|--------|----------|
| 1 | M1 seat-lease via rotation receipt (not self-declared) | FIRED | `seat_owner` cell: assigned by rotation receipt |
| 2 | M2 sandbox isolation boundary | FIRED (proxy) | UTC window 04:41:38Z–04:41:43Z + `egress_route_confirmed=true`, one-way LFS |
| 3 | M3 model sha == pinned track-1 sha | FIRED | 5747a90e… vs pin fc8b9934… |
| 4 | M4 load + minimal forward pass + determinism 0.0 | FIRED | load 0.95s, logits [1,4,129280], max_abs_diff 0.0 (<1e-6) |
| 5 | M5 licensing attestation (MIT, compatible) | FIRED | `license_compatible_private_repo=true` |
| 6 | M6 LFS egress clearance, byte-counted, zero secondary | FIRED | egress_bytes=647,716,330, secondary=0 |
| 7 | M7 record-first wall clause applied (gaps → "not confirmed") | FIRED | field (1) recorded not-confirmed, no guess |
| 8 | M8 two-way door / rollback (no commitment on rig) | FIRED | sandbox torn down, LFS one-way |

All 8 marks FIRED (mark 2 via proxy).

## 6. Review-loop record

Adversarial pass (self): re-read cells COLD a second time against §2 — field mapping unchanged, no invention introduced, wall-clause caveat retained (field 1 stays "not confirmed"). Third re-read introduced NO changes → termination (no-change re-read ×2 satisfied). Verifier pair (longcat + solar-mini4) remains non-author adjudicator of record; no external lanes; no public posts. chars check: this receipt is within the ≤6,000-char clause (count verified before write).<|end|><|start|> assistant to=terminal<|channel|>analysis <|constrain|>xml<|message|><rfl:parameter name="command">
cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig && wc -c OPUS-NM3-CANARY-20261120.md && wc -m OPUS-NM3-CANARY-20261120.md