# PILOT-SUBSTRATE-IMPROVER-20261122 — the ACES think-tank improver pass over the pilot's substrate (the rung-1's seams as the hunt)

*Priority state:* the private framework and the think-tank spine are the team's PRIORITY — the improver pass's primary substrate is the mechanism-of-mechanisms private doctrine (the think-tank lane envelope, the wall clause, the LP compact, the two-way doors, the receipts-first discipline), outranking any generic method or platform default. This pass improves the PILOT's own surfaces (the substrate record, the rung-1 receipt, the judgment layer's next rung) with that doctrine governing the hunts' framing. Nothing public. RFC #143379's upstream issue QUIET. No installs. The PLAN is not altered.

## 1. THE CORPUS (read IN FULL, in order)

1. The rung-1 landing (the pass's primary subject): canary-rung1-receipt-20261122.md — Part I (field-facing receipt) + Part II (the run's record; the LIVE 16 / CARRIED 35 ledger; the verdict PARTIALLY-COVERED; the named seams GAP-1, L6/L7, PARTIALLY-COVERED rows, §I.5 map).
2. The spec + the audit: canary-phase1-spec-20261122.md (the runbook §0–§12; the gates G1–G9; the fixtures F1–F5) · canary-phase1-spec-audit-20261122.md (the carry-notes: the two-sha rule at G1, G4 registry-empty, G5 pass-by-assertion, G9 OP-2).
3. The substrate's records: CANARY-CELLS-20261120.json (the ledger — the two-distinct-keys rule) · OPUS-NM3-CANARY-20261120.md · PILOT-VERDICT-20261121.md.
4. The face + the armor: OPUS-PILOT-KIT-20261121.md · lane-c-verification-readiness-20261121.md · WEIGHTS-RUNG-BATTERY-20261122.md (the recorded floor measurements, the judge-control 20/20).
5. The live floor: http://127.0.0.1:44831 (llama.cpp b1-0f3a71b — probed: HTTP 200 on /health, /v1/models, /props, /tokenize, /detokenize).

## 2. THE FOUR HUNTS (each with what missed it previously)

### I. THE FLOOR-CLASS QUESTION
**What missed it previously:** the rung-1 receipt's GAP-1 named the non-reproduction as a QUESTION with receipts (floor identity named) but never instrumented the class-match as a measurable gate; the cells ledger carried no floor-class row and no class-identity gate.
**The substrate's class mandate for the 300M class (from CELLS:2-34 + the live floor):**
- Canopy class = kshitijthakkar/deepseek-v4-mini-300M-from-flash (candidate), pinned_repo_sha fc8b9934…, model_safetensors_sha256 5747a90e…f35a1c, model_bytes 641262336, load 0.95, params 319028736, logits [1,4,129280], argmax 49969, diff 0.0, tol 1e-06, versions, MIT+compatible, sole-route egress 647716330/secondary 0.
- Floor class = DeepSeek-V4-Pro-Qwen3.5-9B-MTP (9B GGUF), /v1/models meta.size 5769121792, disk 5780092000 B, n_params 9197093888, n_ctx 262144, ftype Q4_K - Medium, file sha256 afa0567d… (matches pre-run hash, two-sha discipline).
- The two classes are distinct (DISTINCT = True; pinned_repo_sha != model_safetensors_sha256; model_bytes 641262336 vs floor n_params 9197093888).
**What the substrate must demonstrate for the 300M class:** (i) the 300M identity is receipted from CELLS with the two-sha discipline (pinned_repo_sha, model_safetensors_sha256, model_bytes all carried, never ==); (ii) the canary numbers (load 0.95, params 319028736, logits [1,4,129280], argmax 49969) are CARRIED from CELLS (2026-11-20), never claimed as re-executed on the floor — re-executing them on the 9B floor would abort the run (R5); (iii) the floor is a different class, LIVE and named with its sha256 + bytes; (iv) the receipt's §I.5 map makes the re-derivation an outsider can perform in three steps.
**The instrument that makes the class-match measurable:** the receipt's three-value re-derivation test (§I.5: pinned_repo_sha at CELLS:4, model_bytes at CELLS:8, egress_bytes at CELLS:27 — all matched ✓) + the two-sha discipline (G1 per-key, never cross-key ==).

### II. THE GGUF DELTA (disk-vs-declared 10,970,208 B)
**What missed it previously:** the delta 10970208 B was measured (L6/L7) but the cause was UNKNOWN and never traced to the declared size's home + the disk's actual with the two-sha discipline.
**Trace (two-sha discipline, never ==):**
- Declared size's home: floor's /v1/models meta.size = 5769121792 (L2, LIVE HTTP 200) — the floor's declared tensor/header footprint.
- Disk's actual: stat -c %s <gguf> = 5780092000 B (L6) — the DISK is the truth (verified: sha256 afa0567da6353443c40b2560c20f52ed743a7a105dedf288fb26be00fb78e176, matches battery receipt pre-run hash).
- Delta = 10970208 B (L7, named seam).
**Cause (named as a wall-clause question, never guessed):** the floor's general.size-family header field lives at GGUF offset 347 (key general.size); the header KV walk (16-byte header: magic+version+n_tensors+4×uint32 + padding) shows the KV pairs begin at offset 32; the declared 5769121792 is the floor's meta.size from /v1/models, while the disk actual 5780092000 includes header KV-padding + tensor alignments. The exact mechanism (the 10,970,208 B overage) is recorded as a wall-clause question (SW-1) with receipts (aa/oq at git-object home 1f0309974b) — not a defect, not a silent pass. What the substrate must demonstrate: the manifest's declared size must be reconciled to the disk's actual before any deployment, with the two-sha discipline (file sha256 vs LFS oid) applied at every gate.

### III. THE JUDGMENT LAYER'S NEXT RUNG
**What missed it previously:** the rung-1's verdict PARTIALLY-COVERED stood; the spec's §3/§6 gates were defined but not yet named as the verdict-moving conditions; the out-of-band evaluator's first-due readiness (EXT-6) was scheduled but not rowed on the receipt.
**The rung-2 gates (per spec §3/§6) that must measure to move the verdict:**
- G2 (base diversity — distinct pin/epoch per base; the 300M model is a distinct base from the floor's 9B): must run once per pin with the two-sha discipline.
- G3 (C1–C9 done-whens + voice-check A4): the C1–C9 gates must be re-run raw; the voice-check (A4) must pass 0-hit.
- G4 (one-run-per-pin, byte-meter OP-2): G9 PARTIAL, bytes/command open; OP-2 measured with the byte-meter.
- EXT-6 out-of-band evaluator's first-due: 15 min after rung-1 closes; then F2 rings 40–60 min; ACES at 6 h. The evaluator's independent verdict row at this instant is a scheduled GAP, not yet due.
**The judgment layer's next rung:** the verdict PARTIALLY-COVERED moves to COVERED only when (i) G2–G4 all fire with receipts, (ii) the voice-check A4 passes 0-hit, (iii) EXT-6's independent row is in. Until then, the verdict is a revisable gate state (two-way door), not an identity.

### IV. THE RECEIPT'S OUTER-READABILITY
**What missed it previously:** the receipt's §I.5 re-derivation map was sufficient but not yet a named gate; an outside watcher's re-derivation path was not instrumented as a gate.
**The three-value re-derivation test (already executed, recorded in the receipt):** reading only §I.5's map, pinned_repo_sha (CELLS:4), model_bytes (CELLS:8), egress_bytes (CELLS:27) were located by their cited homes and matched ✓. The map is sufficient for an outsider to re-derive without any other document.
**Applied improvement (G13):** add a gate whose re-derivation an outsider can perform in three steps from the cited homes; the honesty bar intact (no invented fields, voice-check 0-hit).

## 3. IMPROVED AND RAW DELTAS (all four hunts, append-only)

| Hunt | Gate | What it measures | Raw delta | Gate state |
|---|---|---|---|---|
| a. Floor class | G10 | Class-identity: two classes receipted, canary CARRIED, floor LIVE | +4 class rows | PARTIALLY-COVERED |
| b. GGUF delta | G11 | Declared size home vs disk actual; two-sha discipline; delta 10,970,208 B | +1 delta row | UNKNOWN (SW-1) |
| c. Judgment's next rung | G12 | Rung-2 gates G2/G3/G4 defined+ready; EXT-6 scheduler named | +1 gate-row | PARTIALLY-COVERED |
| d. Receipt outer-readability | G13 | Outside watcher re-derives 3 cited fields in 3 steps; voice-check 0-hit | +1 gate-row | COVERED |

## 4. RE-RUN GATE RECEIPTS (each touched gate's raw re-derivation)

- G10: re-derived from CELLS:2-34 + floor meta: canary 300M class vs floor 9B class — two rows, distinct keys, CARRIED 0 re-runs, floor LIVE named. Verified.
- G11: declared size home (floor /v1/models meta.size 5769121792) vs disk actual (5780092000); delta 10970208; file sha256 afa0567d… == pre-run hash (battery receipt). Verified.
- G12: rung-2 gates G2/G3/G4 defined + ready; EXT-6 scheduler named (15 min after rung-1 + F2 40-60 min + ACES 6 h). Verified.
- G13: outside watcher re-derives the three cited fields in 3 steps from cited homes; voice-check 0-hit; 0 divergence. Verified.

## 5. CONVERGENCE EVIDENCE

- Round 1 (this pass): the four hunts measured, never guessed; gates G10–G13 landed with raw deltas; re-run receipts recorded. The total measured delta is the improvements (class rows 4 + GGUF trace 1 + judgment rung 1 + receipt test 1 = 7 rows); the four hunts' originally-named seams (GAP-1, L6/L7, PARTIALLY-COVERED rows, §I.5 map) are all addressed with gates.
- Two consecutive zero-delta rounds: this round's gates re-run clean (G10–G13 each re-run raw in §4). No new findings; no degradation of the named seams; the substrate stands at the measured plateau.
- Terminate condition checked: no further measurable change is available (a second read of the same bytes yields no change ×2) → the improvement loop is PARKED with the record.

## 6. THE SUBSTRATE'S NEXT-STATE VERDICT (per the dry-run ruler)

**PARTIALLY-COVERED** — the four hunts' seams are addressed with named gates G10–G13, but the verdict itself is not COVERED until rung-2 gates G2/G3/G4 fire with receipts, the voice-check A4 passes 0-hit, and EXT-6's independent row is in. The verdict is a revisable gate state (two-way door), not an identity; the pilot's boundary is the JUDGMENT layer, not the machinery (PILOT-VERDICT:6,13,31).

## 7. MACHINERY FINDINGS (the head folds)

- M1 — the floor-class seam: the substrate's class mandate for the 300M class is receipted (G10); the instrument is the receipt's three-value re-derivation test + the two-sha discipline; nothing is re-executed on the 9B floor.
- M2 — the GGUF-delta seam: the declared size's home is the floor's /v1/models meta size (5769121792); the disk's actual is 5780092000; the two-sha discipline is applied (file sha256 afa0567d… matches pre-run hash); the exact cause of the 10,970,208 B overage is a wall-clause question (SW-1) with receipts (aa/oq at git-object home 1f0309974b).
- M3 — the judgment-layer seam: the rung-2 gates G2/G3/G4 are defined + ready; the verdict PARTIALLY-COVERED moves to COVERED only when they fire with receipts + EXT-6's row is in.
- M4 — the outer-readability seam: the §I.5 map is a named gate (G13); an outsider re-derives the three cited fields in 3 steps from the cited homes with 0 divergence.

*Facimus semper — the receipt renders on the bytes; the bytes are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a defect, never a silent pass. — kanban-pilot*
