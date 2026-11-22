# OPUS-PILOT-KIT-20261121 — the pilot kit's launch package

> **NOTE (framing, not content).** The stack renders brainstorm → cross-audit → AoA → gather → master → the operator's eyes. This artifact is the gather rung's compose: it gathers the AoA-corrected brainstorm artifacts into one launch package — the phase-1 brief as spine, the single watcher-visible receipt as face, the verification-readiness layer as armor. It carries SHAPE, not backstory. Stack verdict **ADAPT**: GO for the bounded canary behind the standing start line, with eight settle-conditions. The three posting doors ride the operator's word and are OUTSIDE this compose's scope. RFC #143379 upstream stays QUIET; nothing public beyond PR #1's thread. All receipts below are re-derived from the cited files' bytes; a non-reproduction is a QUESTION with receipts, never a guess.

---

## [Executive Summary]

The pilot kit's launch package is three artifacts rendered as one: **spine** (the runnable phase-1 canary brief), **face** (the one receipt an outside watcher or the operator reads), **armor** (the verification-readiness layer that makes the reading trustworthy). The execution layer is independently receipted to the bytes — read-restore 42/42 GREEN (PILOT-VERDICT:18), compose-check 8/8 FIRED, mark 2 via proxy (OPUS-NM3:33–44), R1 LANDED with rung-2 armed (OPUS-NM3:29), and every canary cell number matching (CANARY-CELLS:2–34). PROOF-OF-CONCEPT is CONFIRMED with the boundary named as one class, the judgment layer (PILOT-VERDICT:6).

The three brainstorm artifacts are sound after named corrections, but the cross-audit rung itself carries evidence-reality defects (BA's phantom revert trace, AA's dangling anchors, CA's false ancestry receipt + R3-10 mis-citation, all three reported commit shas phantom) and the verification layer is not independent (shared-route constraint; G2/G3/G4 open by construction). Therefore **ADAPT**, not unconditional GO and not PARK: the bounded canary fires behind the standing start line while the eight settle-conditions land, and no "verification independent" or watcher-facing "verified" claim rides until they close (AoA §7:134–146).

The kit's readiness needs no human gate beyond the standing sets. The doors the compose names but does not carry — the court's posting, the RFC's surface, the autopilot's pilot gate — wait on the operator's word only, outside this compose's critical path.

---

## [Analysis Brief]

### A. THE SPINE — the phase-1 canary brief (runnable by an outsider from the cells ledger alone)

The spine is the canary's phase-1 brief (lane-B design) corrected per AoA settle-condition 2: the gate table uses per-key match language (A2), the revert grid is the artifact's real R1–R10 (BA-D1 repaired), and the four continuation points ride as measured, revertible rows.

**A.1 Named items (design §1:40–54; re-keyed to the artifact's IDs per BA-S3).** Items 1–8 FIRED (rung-1 identity; model sha; load/forward/determinism; licensing; egress; sandbox envelope; record-first; two-way door), items 9–12 RUNNING (method cards 1–4: canary first-catches, honest termination, byte-verified meter + out-of-band evaluator, fail-safe grid), item 13 FIRED (capture home — the root cards `KIT-METHOD-CARDS` / `KIT-AUDIT` / `KIT-SKEPTIC` plus the `kit/` files, not one folder: BK-O2), items 14–15 OPEN (gate-state file = the operator's read surface; judge-gate per-ring re-read). Every item carries its receipt anchor; no invented fields.

**A.2 The per-key gate table (design §2:64–71, corrected A2 — each gate derivable from CANARY-CELLS).**

| Gate | Per-key measurement (cells:line) | Bar | Receipt |
|---|---|---|---|
| G1 | `pinned_repo_sha` = `fc8b9934bfdc04adaa7ff7f3f10f48349c72bf64` (cells:4); `model_safetensors_sha256` = `5747a90e…f35a1c` (cells:7); `model_bytes` = 641,262,336 (cells:8) | Each key MATCHES the cell plan; **two distinct keys, never cross-key "=="**; bytes is a size, not a hash | AoA §5 A2:116; cells:4,7,8 |
| G2 | load 0.95 s (12); params 319,028,736 (13); logits `[1,4,129280]` (17–21); argmax 49969 (22); max_abs_diff 0.0 (14); tol 1e-6 (15); `deterministic_within_tolerance=true` (16); transformers 5.23.0 / torch 2.15.0+cpu (9–10) | max_abs_diff < 1e-6 | cells:9–10,12–22 |
| G3 | `license` MIT (24); `license_compatible_private_repo=true` (25) | Compatible with private repo | cells:24–25 |
| G4 | sole route `nm3-canary-r1-20261120` (5); `egress_bytes` 647,716,330 (27); `egress_secondary_downloads` 0 (28); `egress_route_confirmed=true` (26) | byte-counted; zero secondary | cells:5,26–28 |
| G5 | `sandbox_env_id` `tmpfs-venv@PVE-host (kernel 7.0.14-16-pve)` (32), added 2026-11-20T04:45:00Z (33) | Boundary named; **PASS-by-assertion — re-measured at run (EXT-2 / BA-S2)** | cells:32–33; OPUS-NM3:11 |
| G6 | Field mapping unchanged on second cold re-read; no invention | Record-first fields + OPUS §2(1)/§7 — **NOT "PILOT-VERDICT §2"** (that file has no numbered sections: S1 re-mapped) | OPUS-NM3:11,50; AoA §1:28 |
| G7 | R1 LANDED, receipt complete; rung-2 armed sha `415501bd…` ("defined + ready, never promised") | Verdict row at named commit | OPUS-NM3:29,48 |
| G8 | All 8 compose-check marks FIRED, mark 2 via proxy | 8/8, traceable | OPUS-NM3:33–44 |
| G9 | Byte-verified receipt meter: tool-output 0.0 at 0.5/0.65/0.8; re-entry d≈0.864; assistant-prose 0.0 @ 0.65 | measured bytes + command — **PARTIAL: bytes/command = OP-2 (run log / `probes/loss_ladder.py`), carried open** | LOSS-LADDER-AUDIT:144–147; AoA §8 OP-2:169 |

**A.3 The real R1–R10 revert grid (design §3:83–92; BA-D1 phantom trace repaired — these are the artifact's actual bytes).**

| # | Revert point | Trigger | Mechanism |
|---|---|---|---|
| R1 | Cell install | sha mismatch, or load fails | sandbox torn down; install additive, deleted on revert |
| R2 | Model load | load_seconds above barrier, or params ≠ 319,028,736 | load is a probe; forward never runs on a bad install |
| R3 | Determinism | max abs diff ≥ 1e-6 | run recorded as a probe, never a verdict; never burns rung-2 |
| R4 | License | `license_compatible_private_repo` false | model not compatible; release route untouched |
| R5 | Egress | `egress_secondary_downloads` > 0 | one-way, byte-counted; a second download aborts the run |
| R6 | Isolation | envelope contract not verifiable | boundary named and checked at run time |
| R7 | Gate-state file | any gate fails | additive + revisioned; last PASS revision is the rollback point |
| R8 | Capture home | fold lands the file; nothing behind it | fold additive (root cards + `kit/` files) |
| R9 | Judge-gate re-reads | a re-read shows a drift | evaluator's verdict row carries the independent read |
| R10 | ACES trigger | improver loop fires | stops on measured plateau (no-change twice); termination receipted twice over |

Revert rule (design §3:94): a failed gate freezes the run's verdict row at PARTIAL/GAP and re-arms the same item at the next ring — never a silent skip, never a re-run with different values.

**A.4 Judgment-layer fixtures (design §5:117–161).** F1 **pre-committed verdict vocabulary** — LANDED / PARTIAL / GAP / QUESTION / REVERTED / CLOSED, each with a receipt shape and a two-way door; every verdict is a revisable gate state. F2 **out-of-band evaluator's schedule** — re-read G1–G5 at each ring (40–60 min, cadence sourced to NIGHTSHIFT:3 per BA-S5); an independent verdict row at every landing (longcat + solar-mini4, Conflict-1, non-author); before any claim a receipt the lane did not write; ACES trigger at 6 h (no-change twice). F3 **no-gate doctrine** — the pilot runs without a human word; the operator's word gates only the posting surfaces (named below); the fork is open for blind-panel instruments. F4 **fail-safe grid** — G1–G5 continue→hold-safe→need-the-chair; G6–G8 continue→hold-safe; G9–G12 continue→hold-safe→need-the-chair; G13–G15 continue→need-the-chair. F5 **receipt stamp** — every claim lands with its artifact + sha at landing + the command + the evaluator's independent row.

**A.5 Sole-egress discipline (design §4:102–109; the cells' own rule).** (1) One sole route: private repo release `nm3-canary-r1-20261120`, no mirror/secondary. (2) One-way, byte-counted: `egress_bytes` 647,716,330, `egress_secondary_downloads` 0. (3) Model files pulled ONLY via that route; the sandbox never reaches HF for model files. (4) At run the pilot produces its own egress receipt (checksum == pinned sha, byte count == cell, secondary == 0) — EXT-4 re-receipt. (5) No rig disk state, no production seat, no HF download in sandbox; the pilot re-measures the envelope at run (G5). (6) Independent out-of-band re-check of bytes against the cell plan (F2), never lane narration.

**A.6 Continuation points carried into the spine (design §9; BA EXT-1…4).** EXT-1 gate-state-file schema with `cells_sha256` carrying **both** keys — pre-addendum field `f1ed5b0d…` (cells:34) and post-addendum live-file sha `25606ba9…` (OPUS-NM3:50), so a naive file-sha gate does not fail (BA-S6); EXT-2 isolation-envelope re-measurement at ring 1; EXT-3 judge-gate cadence (15 min first re-read, then 2 h, drift rows, sourced NIGHTSHIFT:3 + FINAL-LEG:26); EXT-4 egress re-receipt at run. Rung-2 candidate `V3-3.4B-small` sha `415501bd…` stays ARMED, never promised (O1 kept).

### B. THE FACE — the one watcher-visible receipt

One artifact only: `probes/canary/phase1-receipt-20261121.json`, on the study branch, fork-only (lane-A §2:29). It is the only thing the outside watcher or the operator reads; no prose, no "we believe" — measurements, receipts, names.

**B.1 Provenance-tagged fields (AoA §5 A1:115 — the "read verbatim / all measured" banner scoped to measured cells).** Every field carries `{measured-cell | design-field | verdict-from-record}` and a file:line home. Measured-cell fields (candidate, `pin_repo_sha`←`pinned_repo_sha` (cells:4), `model_sha256`←`model_safetensors_sha256` (cells:7), model_bytes 641,262,336 (cells:8), frames: load 0.95 / params 319,028,736 / logits `[1,4,129280]` / argmax 49969 / max_abs_diff 0.0 / tol 1e-6 / within=true (cells:12–22), isolation env id (cells:32), egress route/bytes/0-secondary (cells:5,27–28), license MIT + compatible (cells:24–25)) re-derive from the cells ledger. Design fields (`spec` tag, `wall_clause`, `revert_points`, `judgment_layer`) carry their own ground tags (design §3/§5; the brief's wall clause). Verdict field is sourced to the record, never to cells.

**B.2 The equality-fix (AoA §5 A2:116; lane-AA D1).** `pinned_repo_sha` (a git commit) and `model_safetensors_sha256` (a file hash) are two distinct ledger keys with distinct values; the gate is match-to-plan **per key**, never cross-key "=="; bytes is a size, not a hash. The loose "==" phrasing is inherited from the ground (OPUS-NM3:13/37 → lane-A I2/G1, lane-B G1 label, lane-BA G1 heading) — repaired at template level by an append-only record-correction row; gate values unchanged, history never rewritten.

**B.3 The honesty bar (lane-AA D2; AoA §2:53–54).** Cells have **no `verdict` key** (grep = 0). The face's verdict is quoted from the record — `PROOF-OF-CONCEPT — CONFIRMED, WITH THE BOUNDARY NAMED AS ONE CLASS` (PILOT-VERDICT:6) / `R1 LANDED` (OPUS-NM3:29) — with its citation, never invented. Five design/record fields under lane-A's "values all measured" banner are re-tagged, not presented as cell measurements. No invented field rides the face.

**B.4 The voice-check grep gate (AoA §5 A4:118; gate enforced before any fold to the face).** Before the face folds to the watcher surface, grep the composed surface for the reserve-name token class and private operator detail; a hit blocks the fold, never rewrites history (the token list and the zero-hit baseline are receipted at AoA §9 SW-3:109). The internal design's seat line (lane-B design:4) carries the reserve's name ground-consistently but must never ride a thread row — thread rows are envelope-form, handles-only. The face passes the gate: zero reserve-name hits, zero private operator detail, zero invented fields. AOA-OQ (the principle-quote's verbatim home) is carried as a question, not silently patched.

### C. THE ARMOR — the verification-readiness layer

**C.1 Base-diversity gate, real and decidable (lane-C §2:71–110; AoA §5 A2/A5; E1).** BASE-DIVERSE iff a verification family contains ≥2 distinct pinned bases and its claim is not "same-base." Default family: (1) execution receipt, (2) audit receipt on a different base than the compose, (3) blind panel on a third runner. ≥2 of the 3 must be pinned to distinct runner/heap identities in the run's own config row. One-command receipt: `grep -oE '(runner|heap)[=:][^ ,]+' config.yaml | sort -u | wc -l` ≥ 2. The shared-route constraint — the three audits rode one pinned base `upstage/solar-mini4:free` (AoA §0:15) — stays named on every verdict row until stage-3 per-unit pinning lands; same-base convergence is never claimed as independence.

**C.2 Blind-panel protocol (lane-C §3:114–147; skill-verified).** 2–3 blind subagents dispatched in parallel from a FIXED, re-inventoried-once-per-shift free pool (upstage/solar-pro4:free, poolside/laguna-s-2.1:free, poolside/laguna-xs-2.1:free, host default), each a distinct ID, no two sharing an ID. The brief names artifact path + questions, never the artifact's content (blindness is non-negotiable). Workers read the rig's chain files with read_file first, then carry real-work missions; no separate supervisor research lane. Each worker writes a distinct file and returns markdown verdicts FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND / GUESSED-WRONG per claim with tool-call counts + evidence paths; the parent re-reads each deliverable and re-derives load-bearing numbers from the artifact on disk; an empty `{}` summary is a landing failure, not a missing artifact. The mediator weights convergences and treats divergences as signal — nothing is "reconciled away" by a majority.

**C.3 C1–C9 external-readiness conditions, each a checkable done-when (lane-C §4:151–216; external-readiness-review skill).** C1 Replication kit → `sha256sum -c SHA256SUMS` exits 0; every receipt number maps to a kit-README file path. C2 Grader pin → the pin file alone, plus the kernel, reproduces the measured count. C3 Human anchor → the anchor's session log shows controls' score spread (kappa defined) and the pass bar (raw ≥80% AND κ ≥0.70) is met or the NULL-with-named-seam clause is quoted. C4 Statistics → appendix states MDDL, Wilson CI, grader-variance estimate, effective-n correction, per-cell failure bound. C5 Related work → 3+ cited lines with DOIs/URLs, "negative result for X" never "falsified." C6 Timestamped prereg → registration link + internal freeze seal (git sha range + receipt chain); no wave re-labeled "registered before data." C7 Compute/cost → worker + memory + time per run + total; zero-billed stub carries `cost_total=0.0`; unrecoverable values UNVERIFIABLE with estimation method. C8 Scoped claims → overstatement→replacement table retaining scope variables. C9 Licensing → corpus status + fair-use analysis in the kit README, lowest-risk option preserving byte-level replication.

**C.4 Seeded pin registry (AoA §5 A5:119; lane-C §5:235–242; E2).** Row schema `pin_id, owner, base/heap, budget, receipt_sha, expires_at`. Seed row: rung-1 canary pin `fc8b9934…` / `5747a90e…`, owner = rotation receipt's R-C executor, `receipt_sha` = live cells file `25606ba9…` **and** pre-addendum field `f1ed5b0d…` (both keys, BA-S6), expires_at = the rung-2 window. One-run-per-pin: a second run is allowed only after the first receipt is re-derived by an outsider (`verify_pin.py`), never by the creating actor. G4 thus moves from rule-with-no-rows to rule-with-one-measured-row and becomes enforceable.

**C.5 Gate states carried OPEN, never smoothed (lane-C §6:264–269; AoA §7 settle 5/6/7).** G1 canary start line PASS; **G2 verification independence OPEN** (bases distinct + blind panel landed); **G3 external-readiness checked OPEN** (C1–C9 done-whens + voice-check gate); **G4 one-run-per-pin OPEN** (registry seeded, enforcement pending). The layer's own verdict is READY / READY-WITH-NAMED-SEAMS / NOT-READY; G2/G3/G4 remain OPEN on the record until their settle-conditions close. No open gate is rendered as a pass.

### D. THE OPEN-ITEMS LEDGER — none dropped (AoA §8:163–178)

| # | Question | Disposition | Receipt |
|---|---|---|---|
| O1 | Rung-2 fire timing + gate | KEPT (answered by the next cell) | OPUS-NM3:29 — `415501bd…`, "defined + ready, never promised" |
| O2 | "Kit folder" naming (item 13) | KEPT (additive rename) | root cards + `kit/` files, not one folder (BA O2) |
| O3 | Isolation-envelope measurement not run | ESCALATED to pilot ring-1 (EXT-2) | cells:32–33 assertion; OPUS-NM3:11 |
| OP-1 | Compose-check 8/8 outside AA ground | ANSWERED | OPUS-NM3:33–44, 8/8 FIRED, mark 2 proxy |
| OP-2 | G9 measured bytes + command | KEPT (byte meter constructed; command needs run log) | LOSS-LADDER-AOA counts+decision_rule; `probes/loss_ladder.py` |
| CA#1 | R2 write-deadline superseded | ANSWERED | PILOT-VERDICT:19 + copycat-harness:663/:542/:549 |
| CA#2 | THE-NORTH external gate label | ANSWERED | PILOT-VERDICT:18 |
| CA#3 | `ab471fc80c` ancestry | CORRECTED (CA-D1) + mechanism KEPT | commit real on main; IS_ANCESTOR=NO at HEAD and at `6de5aba311`; kit files tracked via fold |
| CA#4 | Blind-panel land status | ESCALATED (stage-3 / ARM 4) | lane-C §6 G2 OPEN:267 |
| CA#5 | Pin registry empty | ESCALATED (A5 seed + stage-3) | lane-C §6 G4 OPEN:269 |
| CA#6 | Fold as ground needs own receipt | KEPT (A3 manifest); receipt-form string verified | fold §7-u:97 verbatim |
| SW-1 | Phantom commit-sha mechanism | KEPT (never guessed) | real commits `2cc6f1832f`/`2ce77ce5ad`/`6de5aba311`/`20d11790c8`; reported shas nonexistent across canonical + 10 siblings |
| AOA-OQ | Principle-quote verbatim home | KEPT (question, not defect) | lane-C:28–29 present; verbatim fold home unfound; concept verified fold §7-u:97 |
| SW-2 | Index/disk divergence (commit-phase) | KEPT (gather caution — **read from DISK, never the index**) | tank untracked at earlier fold; design disk sha==original `5d4015f2`; wire `5044a79ae4` diverged; never checkout/rm/stash |

Record-correction rows for every corrected receipt are append-only; history is never rewritten. The real commit shas (`2cc6f1832f` BA · `2ce77ce5ad` AA · `6de5aba311` CA · `20d11790c8` AoA) are the landing receipts, never the phantom reported ones (SW-1).

### E. THE STACK VERDICT — ADAPT (AoA §7:134–146)

**ADAPT** — GO for the bounded canary behind the standing start line, with settle-conditions; not unconditional GO; not PARK. The kit may fire as a bounded canary (two-way door, no human word at the gate, RFC quiet, nothing public beyond PR #1) while the adaptations land; no "verification independent" or watcher-facing "verified" claim rides until the settle-conditions close.

The eight settle-conditions (verbatim, AoA §7:139–146):

1. **FORM:** D1+D2 land via A1/A2 (per-key match vocabulary; provenance-tagged receipt; verdict sourced to OPUS §4 / PILOT-VERDICT THE VERDICT, never cells). One-line edits + additive correction rows.
2. **DESIGN:** BA-D1 revert re-trace against design §3:83–92 (the artifact's real R1–R10); S1 anchor re-map (OPUS §2(1)+§7); item-table re-key to artifact IDs (BA-S3); EXT-1 version anchor carries both cells shas (f1ed5b0d field + 25606ba9 live file, BA-S6); F2 cadence re-anchored to NIGHTSHIFT:3 (BA-S5).
3. **LAYER:** CA-D1 ancestry receipt corrected (commit-on-main + file-presence, never the false is-ancestor claim); CA-S1 re-anchored to fold §7-u:97; defect#1's two questions carried as answered (PILOT-VERDICT:18–19 + harness bytes); CA-S2 wall-clause classification corrected (questions, not defects).
4. **AUDIT RECEIPTS:** the phantom reported shas replaced by the real commit shas (BA 2cc6f1832f · AA 2ce77ce5ad · CA 6de5aba311) in the dispatch record; the mechanism question kept open (SW-1), never guessed.
5. **INDEPENDENCE (G2):** stage-3 per-unit base pinning lands + ARM 4's gate (a verification run whose bases are distinct) + a blind panel on the first numeric landing; the shared-route constraint stays named on the record until then; same-base convergence never claimed as independence.
6. **READINESS (G3):** C1–C9 done-when states checked before any external share (stage-5 external-readiness gate); the watcher face passes the voice-check grep gate (A4).
7. **STEWARDSHIP (G4):** pin registry seeded (A5) + one-run-per-pin enforced; the second run gated on outsider re-derivation (lane-C §5 two-way door).
8. **MANIFEST (A3):** every load-bearing claim in the gathered kit carries a ground-set tag + file:line receipt; out-of-ground claims are questions; the open-items ledger holds every wall-clause question (none dropped).

### F. THE DOORS — named, waiting, OUTSIDE this compose's scope

The court's posting, the RFC's surface (#143379 upstream issue QUIET), the autopilot's pilot gate, and the voice-check's shape ride the operator's word only (PILOT-KIT-PLAN §7:55; FINAL-LEG THE DOORS:30; AoA §7:136). All named; all waiting; none gated by this compose, none on its critical path. The kit's readiness needs no human gate beyond the standing sets. The compose names these doors; it does not open, close, or sequence them.

---

## [Recommendation/Action Plan]

Fire the bounded canary behind the measured standing start line (PILOT-VERDICT:15–23) with the spine, face, and armor as rendered above. It is a two-way door: a failed gate freezes the verdict row at PARTIAL/GAP and re-arms at the next ring; the rollback is no commitment made (design §3:79,94).

Close the eight settle-conditions as gate rows, in the AoA's numbering; each is named, measured, revertible. Until settle 5/6/7 close, no "verification independent" or watcher-facing "verified" claim rides — the shared-route constraint and G2/G3/G4 OPEN states stay on every verdict row. All repairs are one-line edits or additive, receipted rows (append-only record-correction rows; history never rewritten). Every claim in this package carries a ground-set tag + file:line receipt (settle 8); a non-reproduction is a QUESTION with receipts, never a guess.

---

## [Next Steps/Exploration]

- Close settle 1 (face) and 2 (spine) — the per-key vocabulary, provenance tags, real R1–R10 trace, both-cells-sha version anchor — as append-only correction rows; no runtime change.
- Close settle 3/4 (layer + receipts) — CA-D1 ancestry and R3-10 re-anchors, the real commit shas in the dispatch record; keep the phantom-sha mechanism question (SW-1) open.
- Close settle 5/6/7 (independence, readiness, stewardship) at stage 3/5 — per-unit base pinning + ARM 4's distinct-base run + a landed blind panel; C1–C9 done-whens + the voice-check gate; the seeded registry with outsider re-derivation.
- Resolve or re-label the kept questions, never silently: SW-1 phantom-sha mechanism, CA-D1 mechanism, SW-2 disk-vs-index (read from DISK), AOA-OQ verbatim home, OP-2 judge-command receipt, O1 rung-2 timing, O2 kit-folder naming.
- The three doors wait on the operator's word outside this scope; the master renders this package to the operator's eyes next.

---

## [Artifact]

`studies/rfc-143379-rig/plan/tank/OPUS-PILOT-KIT-20261121.md` — the pilot kit's launch package, in the OPUS register. Spine = the phase-1 brief; face = the one watcher-visible receipt; armor = the verification layer; all gathered under one `ADAPT` verdict with eight settle-conditions and a none-dropped open-items ledger. Receipt path shorthand used above: `cells:N` = CANARY-CELLS-20261120.json line N (archive + study copies); `OPUS-NM3:N` = OPUS-NM3-CANARY-20261120.md line N; `PILOT-VERDICT:N` = PILOT-VERDICT-20261121.md line N; `design:N` = lane-b-phase1-design-20261121.md line N; `lane-A/C:N` = the lane-a/lane-c brainstorm artifacts; `AoA §x:N` = aoa-audits-20261121.md section/line. Full paths in the seal.

### Compose-check table (register's 8 steps, FIRED/ABSENT, one evidence line each)

| # | Step | State | Evidence line |
|---|---|---|---|
| 1 | deconstruct | **FIRED** | Spine/face/armor separated with receipts: design §1–§5, lane-A §2, lane-C §2–§5. |
| 2 | sense | **FIRED** | ADAPT rendered from the AoA's consolidated verdict (AoA §7:134–146); eight settle-conditions quoted verbatim. |
| 3 | choose | **FIRED** | GO bounded canary / not unconditional GO / not PARK — the AoA's falsifier pass re-rendered (AoA §7:148–157). |
| 4 | calibrate | **FIRED** | Per-key gate table (A2), both-cells-sha version anchor (BA-S6), real R1–R10 grid (BA-D1), OPEN gates carried. |
| 5 | probe | **FIRED** | Every numeric claim re-derived to cells bytes (cells:2–34); 42/42, 8/8, R1 LANDED traced to OPUS/PILOT-VERDICT. |
| 6 | review | **FIRED** | Voice-check grep gate (A4), honesty bar (no invented field), shared-route constraint named, phantom-sha mechanism kept open. |
| 7 | record | **FIRED** | Open-items ledger 14/14 none dropped (AoA §8:163–178); record-correction rows append-only; real shas named. |
| 8 | compose-check | **FIRED** | This artifact exists at the deliverable path with schema envelope, compose-check, and seal; doors named OUTSIDE scope. |

### SEAL — receipts block (every load-bearing claim to a real file's bytes)

- **Verdict / stack meaning:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/aoa-audits-20261121.md` §6:123–128 (gather holds), §7:132–157 (ADAPT + 8 settle-conditions + falsifier pass), §8:161–178 (open-items ledger), §5:113–119 (A1–A5), §0:13–17 (shared-route constraint).
- **Cells ledger (all gate numbers):** `/root/workspace/master-page/study-archive-20261120/CANARY-CELLS-20261120.json` :2–34 — candidate/pin :3–4, egress route :5, model sha :7, bytes :8, versions :9–10, load/params/determinism :12–16, logits/argmax :17–22, license :24–25, egress bytes/secondary :27–28, sandbox env :32–33, cells_sha256 :34.
- **Rung-1 receipt / compose-check / record-first:** `/root/workspace/master-page/study-archive-20261120/OPUS-NM3-CANARY-20261120.md` §2:9–19, §4:27–29 (R1 LANDED, rung-2 armed), §5:31–44 (8/8, mark 2 proxy), §7:49–50 (post-addendum sha `25606ba9…`), §8:52–53 (S2 sanitize, inert injection flagged).
- **Pilot verdict / start line / doors:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/PILOT-VERDICT-20261121.md` :6 (verdict string), :15–23 (five start-gates 42/42, READ-GATED+2K breaker, 31/35, U1–U3, kit cards), :30–31 (two-way door, judgment-layer boundary).
- **Spine (items/gates/revert/egress/judgment):** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-b-phase1-design-20261121.md` §1:36–56, §2:60–73, §3:77–94 (real R1–R10), §4:98–109 (six egress rules), §5:113–161 (F1–F5), §9:203–210.
- **Face (receipt / provenance / equality / honesty):** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-a-minimal-demonstrable-20261121.md` §2:27–84 (one artifact + JSON example), §3:86–101 (I1–I10), §4:103–119 (G1–G9); equality defect re-derived at AoA §2:50–54; honesty bar D2 at lane-AA audit §3 D2:66.
- **Armor (base diversity / blind panel / C1–C9 / registry / gates):** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-c-verification-readiness-20261121.md` §2:71–110, §3:114–147, §4:151–216, §5:220–254, §6:258–276 (G1 PASS, G2/G3/G4 OPEN).
- **Gate corrections / equality provenance:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-aa-audit-20261121.md` §0:18–22 (D1/D2), §3:61–74 (EX-1…4); `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-ba-audit-20261121.md` §VERDICT:9–18 (S1/S2), EXT-1:110 (schema), OPEN O1–O3:120–124; `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/lane-ca-audit-20261121.md` §RECEIPT:35–49 (C1–C9/G2–G4), OPEN:65–72.
- **Settle-condition grounds:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/PILOT-KIT-PLAN-20261121.md` §2:9–15, §3 L3:21, §4 Stage 3:32, §7:53–55 (doors), §9:75–86; `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/night-20261121/FINAL-LEG-PLAN-20261121.md` ARM 3:16, ARM 4:18 (distinct-base gate), THE ACES-TRIGGER:26, THE DOORS:30; `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/LOSS-LADDER-AUDIT-20261121.md` §4:143–147 (d≈0.864 re-entry) and `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/LOSS-LADDER-AOA-20261121.md` §1:29–39 (matrix + decision_rule); `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/MASTER-HITL-GIST-AOA-20261121.md` M4:130–132 (base constraint), R3-10:68, fold §7-u:97 (receipt-form string).
- **The nutrient (intent register + failure classes):** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/RECORD-MINE-20261121.md` §1:33–114 (intent register), §2:118–177 (failure classes incl. leak class 2.4), §3:180–223 (cadence shapes).
- **OPUS register shape:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/OPUS-2-PLAN-ENVELOPE-20261119.md` §PLANNING ENVELOPE:6–13 (stack-order clause: deconstruct/sense/choose/calibrate/probe/review/record/compose-check, FIRED/ABSENT + one evidence line; wall clause; record-first; refusals); 8-mark table pattern confirmed at `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/MASTER-TEAM-M1-20261119.md` §5:54–65.

### Re-verify ledger (compose-check re-run)

- **Length/depth:** every required list rendered in full (R1–R10, G1–G9, C1–C9, 8 settle-conditions, 14 open items) — the arc is rendered, never referenced by pointer to the AoA.
- **Doors:** court's posting · RFC's surface · autopilot's pilot gate · voice-check's shape — named as waiting on the operator's word, OUTSIDE this compose's scope.
- **Receipts traced:** each load-bearing claim carries a file:line receipt above; re-derived from bytes, not paraphrase.
- **Hygiene:** the face passes the voice-check grep gate — no reserve-name token, no private operator detail, no invented field; SW-2 divergence handled by reading from DISK, never the index.

*Facimus semper — the kit renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION, never a defect.*
