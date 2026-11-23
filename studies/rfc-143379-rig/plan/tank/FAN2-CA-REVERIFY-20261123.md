# FAN2-CA-REVERIFY-20261123.md — blind Act-5 re-verification of REVERIFY-AMS3-20261123.md against the amended gates

*Seat: `tencent/hy4-flash:free` (hy, flagship) · Branch: `study/rfc-143379-rig-20261105` · Date: 2026-11-23 · Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/FAN2-CA-REVERIFY-20261123.md`.*

*Target, cold: `plan/tank/REVERIFY-AMS3-20261123.md`, landing commit `4c049ec82b8e606f84492aaa44f8084eb2e9cc9d` (verified in `git log --all`; worktree blob = commit blob `464c98f5451dcada0b8350af13b5354a0f362db7`). The brief's `4c049ec82b` is a COMMIT id, not the file blob — recorded, not silently normalized.*

*This is the blind re-verification lane. The target was read cold; the sibling lanes' drafts (FAN2-BA / FAN2-AA) were NOT opened (blind clause). All reads local via `read_file` / `git show` / `git rev-parse` / `grep`; no field search, no install, no harness or seat fired, no public write.*

*Hard lines (binding): nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · never push · never `git checkout --` / `git rm -rf` / `git stash` · master append-only · commit as `kanban-pilot <pilot@rig.local>` · write ONLY under `studies/rfc-143379-rig/` · plan, sealed artifacts, crons, anchors left AS FOUND · local config left AS FOUND (identity overridden per-commit).*

*Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised." Every non-re-derivable claim below is UNKNOWN with a minimal experiment; none is a silent pass.*

*Emission contract: this file lands on disk FIRST with the receipts inside, then the commit as `kanban-pilot` (this path only), then the report's sha. Exit 0 = deliverable on disk then sha.*

---

## 0. Armament — used with why, refused with why (skill-dump doctrine)

**USED (4):**

- **think-tank** — the spine: classify → choose → probe → evaluate → adopt-or-park → standardize → verify. Used to classify each target claim (landing verdict / identifier seam / gate coverage), choose the re-derivation route, probe the cited record, and adopt-or-park each claim on evidence. The loop's verify step is this file.
- **investigation-documentation** — the receipts form: a peer-reviewable discovery log, faithful (not distilled), with Limitations + Reproducibility. Used for §5 (limitations) and §6 (re-runnable commands); every check carries its row/path/digest, no claim floats.
- **defect-forensics** — the classes: verify the CLASS, not the flagged instance. Used to sweep SW-1 (report-sha vs landing-sha divergence) across all three lanes, to recognize the version seam, the false-equality class, the mis-trace class, the void class, and the unbacked-receipt class — so a defect found in one lane is checked in the others.
- **agent-work-review** — the verdict form: full reads → extraction → consistency matrix → arithmetic re-derivation → identifier cross-check → epistemic scoping → asserted → status → basis. Used for §2 (the asserted-to-status-to-basis table) and the explicit unverifiable list (§5). Flat neutral tone; the target's own vocabulary is preserved.

**REFUSED (named, with why):**

- blind-agent-panels / supervisor-delegation / github-think-tank-feedback — no consensus fan-out; this is a single blind lane (blind clause).
- codex / claude-code / opencode — no delegate coder for a study-path append.
- systematic-debugging — armed only on a non-reproduction; the wall clause governs here (questions, not fixes).
- browser-harness-sop / web-storm / grounded-citations / arxiv / ddg-cli-search — LOCAL receipts only, no field search.
- two-model-reasoning — no offline-reasoner leg.
- local-llm-serving / llama-cpp / serving-llms-vllm / evaluating-llms-harness / aces-harness-probes — no install, no harness or serving change; the B1 fire is RE-READ, not re-FIRED.
- hermes-agent / hermes-gateway-ops — no config or gateway change.
- memory-chain — no chain append.
- safe-file-editing — no secret-bearing file edited.
- the creative / design / media families — no artifact generation.

A lane that does not arm is a finding: this lane arms exactly the four above.

---

## 1. Scope — the gates read in full, and the record re-derived cold

### 1.1 The act-5 clause (REVISED-STAGE-PLAN-20261123.md, row 5, lines 144–150)

Verbatim load-bearing text at line 144: **"CROSS-AUDIT FAN + LANDING GATES (AM-C1–C3) — Three blind lanes on three distinct bases × hosts, fire in PARALLEL only after acts 2–3 pass; AoA stays BLOCKED on six-check landing gates (the new content-gate row included)."** Line 150 re-asserts the sequencing law: the fan is parallel, the AoA staged and BLOCKED on verified landings, the ROW single-writer, an agreed suggestion lands in the NEXT leg's brief, never on a live card. Acts 1–4 (lines 139–143) precede it. **This lane does not open act 5** — it audits the artifact that would gate it.

### 1.2 AM-C1 / AM-C2 / AM-B1 in full (REVISED :51–59, :97–100)

- **AM-C1 (:51–54):** every seat — BA `meituan/longcat-2.5:free`@`p0tat0` · AA `stepfun/step-3.7-flash:free`@`c0wb0y` · CA `tencent/hy4-flash:free`@`cloud` · the AoA's fourth base — is **re-probed at dispatch and at every fire** (positive-token read + PIN read-back, a REAL question); `stepfun-freeze` and `qwen's-end` are one liveness class; a drained/frozen pin is never re-fired in the same window; the pivot keeps the lane's role, is ledgered in the receipt, and **base-diversity (≥2 distinct bases; AoA distinct from all three) is re-verified after the pivot** — a diversity-collapsing pivot is a named constraint, never a silent pass.
- **AM-C2 (:56–59):** a positive-token echo establishes **liveness only**. Where a probe's response enters a landing's evidence as content (seat-generated answer, number, or evaluator row), the probe must ALSO carry the content-gate: a real question at a content-bearing budget with `content_head` + `reasoning_tokens` + `max_tokens` receipted. **A 200-with-emptiness or echo-only response is liveness, NOT content; VOID for any content claim.** The caveat is quoted verbatim in the act's receipt.
- **AM-B1 (:97–100):** a fire WITHOUT the real-question content-gate (item 1 real-question probe at content-bearing budget with PIN read-back AND item 2 per-call content-receipt) is **VOID-CLASS — verdict UNKNOWN, bars unevaluable, never a settlement**; a catalog class, not an anomaly. Three receipts cited: fire #4 (14×200, reasoning=completion=max_tokens=24, content=null) · fire #5 (200 + visible content + 16 reasoning tokens, PIN-READ-BACK VERIFIED) · B1's A3-arc fire (4 probes at 256/128 + 20 cells, all 200/null, reproduced at 10× budget). Degenerate ceiling `0 ≥ 0.85×0` at C=0 stays named and refused.

### 1.3 Records re-derived (all pins resolved; worktree = pinned blob)

| Record | Pin / commit | Blob re-verified | Role in this pass |
|---|---|---|---|
| target | `4c049ec82b` | `464c98f5451d…` | the artifact under audit |
| REVISED plan | `93d2def129` / fold `cfed8b30f9` | both `71cbe5cc5750…` | the amended gates + act order |
| fan CA | `f4feeb4fc0` | `5792e5cb7af3…` (148 lines) | target's §0.1-B / §2.1 |
| fan BA | `34424e81ac` | `bd8b98a2b2bf…` (172 lines) | target's §0.1-C / §2.2 |
| fan AA | `760092f1eb` / `2ce77ce5ad` | both `a2e44cd6de98…` (102 lines) | target's §0.1-D / §2.3 |
| AoA | `73b4cbead7` | `f1a579556708…` | target's §0.1-G / §4 |
| matrix-legs | `9d74420def` | `26462d6bfd13…` | target's §0.1-E / §2.4 |
| B1 fire | `f32f5ab716` | `c32aad4900bf…` | target's §0.1-F / §2.5 |

---

## 2. VERDICT: **DEFECTS-NAMED** (D-1 / D-2 / D-3)

All five landing verdicts and every load-bearing number in the target re-derive from the cited records. Three defects are named — two unseamed seams and one unbacked receipt claim — none of which overturns a landing verdict, so this is **DEFECTS-NAMED**, not SOUND and not REJECT.

- **D-1 — AoA internal version divergence not named (AM-S3 version-check seam).** Target §2.1/§2.2/§3.2 frame the earlier shas (`6de5aba311` CA / `2cc6f1832f` BA) purely as "AoA §4.2 vs task-named." Re-derivation shows the AoA is **internally** divergent: its §0 (line 14) already cites the task-named commits `f4feeb4fc0` / `34424e81ac`, while §4.2 (lines 164 / 166) cites the earlier ones. The specific §4.2 claim is accurate; the AoA's self-divergence is an unseamed seam, so the target's "divergence flagged, not smoothed" is incomplete.
- **D-2 — unbacked PIN receipt in the target's own header (AM-C1 / G1 / AM-C2).** Line 3 asserts "PIN-READ-BACK VERIFIED at the fire," while §6 (line 188) says "no seat was probed" and §2.1–§2.3 say "NO seat was fired in this landing"; §5's compose-check has no probe/content-receipt row. No question sha, responding model echo, `content_head`, `reasoning_tokens`, or `max_tokens` appears anywhere in the artifact. From the record this is **UNKNOWN**, not verified — under AM-C2 a 200-with-null is liveness only.
- **D-3 — AM-C2 absent from the four-gate ledger.** §0.2 title says "The four amended gates" and lists AM-C1 / AM-F3 / AM-B1 / AM-S3; AM-C2 enters only in §4's future-fan sentence. The content-gate is applied via AM-B1 alone; no per-landing content-ingress row exists. This is a coverage gap in the gate ledger, not a wrong verdict.

### 2.1 Asserted → status → basis table (34 rows: 31 CONFIRMED · 2 DISCREPANCY · 1 UNKNOWN)

A claim that cannot be re-derived is **UNKNOWN**, never inferred. "CONFIRMED" means re-derived from the cited bytes via the stated receipt. Statuses: C = CONFIRMED · D = DISCREPANCY · U = UNKNOWN.

| # | Asserted claim (from target) | Status | Basis — receipt row / path / digest / command |
|---|---|---|---|
| S01 | `4c049ec82b` is the target's landing commit; brief digest is a commit not a blob | C | `git log --all --oneline` hit; `git rev-parse 4c049ec82b:…REVERIFY…` = `464c98f5451d…` = worktree `git hash-object` |
| S02 | REVISED plan pinned `93d2def129` / fold `cfed8b30f9` | C | `git rev-parse <c>:…REVISED-STAGE-PLAN…` = `71cbe5cc5750…` at both |
| S03 | act-5 clause: 3 blind lanes × distinct bases/hosts, parallel only after acts 2–3, AoA BLOCKED on six-check gates incl. content-gate | C | REVISED-STAGE-PLAN-20261123.md:144, sequencing law :150 |
| S04 | AM-C1 in full (per-fire re-probe, PIN read-back, one liveness class, role kept, ledgered pivot, ≥2 bases, AoA distinct, re-verified after pivot) | C | REVISED-STAGE-PLAN-20261123.md:51–54 |
| S05 | AM-C2 in full (echo = liveness only; content-bearing 200 required; null-content 200 VOID at any budget) | C | REVISED-STAGE-PLAN-20261123.md:56–59 — see D-3 |
| S06 | AM-B1 in full (void-class catalog, 3 cited receipts, degenerate ceiling refused) | C | REVISED-STAGE-PLAN-20261123.md:97–100 |
| S07 | CA pin `f4feeb4fc0` blob `5792e5cb…`, 148 lines, supersedes `6de5aba311` (78 lines), not ancestor | C | `git rev-parse <c>:…lane-ca-audit…`; `git show <c>:… \| wc -l` = 148 / 78; `git merge-base --is-ancestor 6de5aba311 f4feeb4fc0` exit 1 |
| S08 | CA verdict ADAPT / NOT-READY with G2a variable mismatch, G2b 2 missing controls, G3 FAIL ON FORM, G4 rule only | C | lane-ca-audit-20261121.md:16,18,24–26,38,63,75,83; AoA:17,22,43,123 |
| S09 | CA 16 receipt rows R1–R16, 4 extensions O6–O9, 7 questions Q-THE-NORTH…Q-registry | C | CA:97–112 (R1…R16 all present), :120,122,124,126 (O6…O9), :132–138 (7 Qs) |
| S10 | CA R8 model sha `415501bd…` marked UNVERIFIABLE (online), a question not a claim | C | CA:104; target §2.1 / §3.4 agree |
| S11 | BA pin `34424e81ac` blob `bd8b98a2…`, 172 lines, supersedes `2cc6f1832f` (134 lines), not ancestor | C | `git rev-parse`/`git show … \| wc -l` = 172 / 134; `git merge-base --is-ancestor 2cc6f1832f 34424e81ac` exit 1 |
| S12 | BA verdict DEFECTS-NAMED D1–D7 | C | lane-ba-audit-20261121.md:10,69–75; AoA:35,131 |
| S13 | BA D1 false equality: egress `647,716,330` ≠ model `641,262,336`, delta `6,453,994` | C | BA:69, :103–105; independently AA:30,63 and AoA:64 |
| S14 | BA 5 extensions EXT-1…EXT-5, 4 questions Q1–Q4, cells sha `25606ba9…` byte-identical in both copies | C | BA:22–24 (sha ×2), :83,100,111,122,131 (EXT), :142–145 (Q1/Q4); AoA:54 (Q1–Q4 are QUESTIONS) |
| S15 | AA pin `760092f1eb` = `2ce77ce5ad`, blob `a2e44cd6…`, sibling sends not ancestor | C | `git rev-parse <c>:…lane-aa-audit…` = `a2e44cd6…` at both; `git merge-base --is-ancestor 2ce77ce5ad 760092f1eb` exit 1 |
| S16 | AA DEFECTS-NAMED D1/D2 (`fc8b9934…` ≠ `5747a90e…`; ungrounded `verdict` field), EX-1…EX-4, OP-1…OP-3 | C | lane-aa-audit-20261121.md:20,30,63–67,71–72,80–82; AoA:52,125 |
| S17 | AoA calls AA "the cleanest of the three" | C | AoA-NINE-AXIS-20261123.md:24,52,125 |
| S18 | AoA pin `73b4cbead7` blob `f1a57955…`; G1–G4 + G8–G17 PASS; G5/G6/G7/G18 UNKNOWN/UNDEFINED | C | `git rev-parse 73b4cbead7:…AoA…` = `f1a57955…`; AoA:163–180 and :182 |
| S19 | AoA's 8 settle-conditions; "until 1–4 close the stack verdict stays ADAPT"; shared-route constraint named | C | AoA:130–149, :92, :110, :149 |
| S20 | Phantom shas `ab660b943b` / `16130475d2` / `f4b845f05b` do not resolve; SW-1 class across all three lanes | C | `git rev-parse --verify <s>` = UNRESOLVED for all three; AoA:109 attributes BA/AA/CA respectively |
| S21 | Matrix pin `9d74420def` blob `26462d6b…`; R leg 4/4 PASS on N10 re-scope, as-is packet 4/4 FAIL | C | `git rev-parse 9d74420def:…MATRIX…` = `26462d6b…`; MATRIX-LEGRUNS-20261123.md:23,26,33 |
| S22 | Matrix P grep-counts `0/2/0/0` at `:367`/`:650`; C blob `7d447366…` + 14 `test_` methods; H NOT-RUN; F-16; handoff CLOSED/GATED | C | MATRIX:38,45,49–53,64,70 |
| S23 | Pin seam `6609dac951` unresolvable vs `6609dacba9…` tree-resolved; 3 study-ref values `f652b71b4e`/`f32f5ab716`/`9d56caa557` | C | `git rev-parse --verify 6609dac951` UNRESOLVED, `6609dacba9` resolves; MATRIX:14,16; REVISED:84 |
| S24 | Against AM-F3 the grid covers 4 of 8 arms; four equivalent/sync arms have no leg row | C | REVISED:82–91 (8 arms); MATRIX §2/§3 contains no `re-cut-write-gate-surgical`/`r2gate`/`r2cs`/`origin/fix/restore-read-action` leg rows (grep) |
| S25 | B1 pin `f32f5ab716` blob `c32aad49…`; battery verdict UNKNOWN/VOID-class, harness INCONCLUSIVE | C | `git rev-parse f32f5ab716:…B1…` = `c32aad49…`; B1-A3-ARC-FIRE-20261123.md:7,336 |
| S26 | B1 item 1 FAIL: 4 probes (256 then 128×3) all 200/null, reasoning=completion=max, finish=length; item 2 PRESENT: 20 cell-level content-receipts | C | B1:36–47 (4 probes), :51 (20 cells), :40–43 (budget/tokens) |
| S27 | B1 judge-control 20/20 `ok=true` fingerprint `ab9e6b5c868b6c30`; BIAS_V3 ids 0–6,8,9 with id 7 dead; verdict disconfirmed ×6 | C | B1:255,314 (fingerprint), :268 (delta log), :1522,1616 (×6) |
| S28 | B1 two-way door byte-identical: 3 harness shas, GGUF `afa0567d…`, `new_weight_files=[]`, `zero_gradient=true` | C | B1:1542,1544,1580–1582 |
| S29 | B1 `B_minus_A=0.0`, `C_minus_A=0.0`, `B_over_0.85C=true` only degenerately at C=0; §7 mechanically READY / verdict UNKNOWN / B2 NOT ADVANCED; OI-1…OI-5 | C | B1:304–306,336, :1589–1593 (§7), :1599–1603 (OI-1…5) |
| S30 | Target's next-act order Act-1→Act-5 and gather inputs not acceptance-ready | C | REVISED:139–145; AoA:149,:167–180; target §4:163–167 |
| S31 | Target header "PIN-READ-BACK VERIFIED at the fire" | **U** (D-2) | target:3 vs target:188 ("no seat was probed") and §2.1–2.3 ("NO seat was fired"); §5 compose-check rows 1–8 contain no probe/content-receipt. No `question sha`/`responding_model`/PIN echo/`content_head`/`reasoning_tokens`/`max_tokens` anywhere in the artifact — minimal experiment §4 Q-2 |
| S32 | Version seam framed as task-named sends vs "AoA §4.2" earlier sends only | **D** (D-1) | AoA:14 already cites `f4feeb4fc0`/`34424e81ac`; AoA:164,166 cite `6de5aba311`/`2cc6f1832f`; target:66,78,132,138 name only the latter — minimal experiment §4 Q-1 |
| S33 | §0.2 "four amended gates" = AM-C1 / AM-F3 / AM-B1 / AM-S3 | **D** (D-3) | target:33–38; AM-C2 is at REVISED:56–59 and appears in target only at :165 — minimal experiment §4 Q-3 |
| S34 | Superseding-send notation CA "114±44 lines" / BA "145±107 lines" | C (precision seam) | `git show f4feeb4fc0:…CA… | wc -l` = 148; `git show 34424e81ac:…BA… | wc -l` = 172; earlier sends 78 / 134. The ± ranges contain the measured values; exact counts recorded in §1.3 |

**Table count: 34 rows — 31 CONFIRMED, 2 DISCREPANCY, 1 UNKNOWN.** (S34's precision seam is CONFIRMED, not a defect.)

### 2.2 What re-derived *cleanly* (the load-bearing body)

Every fan verdict survives cold: CA ADAPT/NOT-READY (S08–S10), BA DEFECTS-NAMED D1–D7 with the exact byte delta (S12–S14), AA DEFECTS-NAMED D1/D2 with "cleanest" confirmation (S16–S17). The matrix's R/P/C/H rows and F-16 handoff stand (S21–S22), and the AM-F3 coverage shortfall is real (S24). The B1 fire is exactly what AM-B1 prescribes — UNKNOWN/VOID-class, not a settlement (S25–S29). The AoA's settle-conditions and input statuses are as the target reports (S18–S19); the phantom-sha class sweeps all three lanes (S20). No seam was silently reconciled in the body of the target.

---

## 3. Extensions I would open (5, at least 2 required)

- **E-1 (closes D-3):** add **AM-C2 as a fifth named gate row** in the target's §0.2 and re-answer Q-A/Q-B per landing with a content-ingress row: for each of the five landings, name any claim derived from a seat response and check it against `content_head`/`reasoning_tokens`/`max_tokens`; expected rows — CA R8 UNVERIFIABLE-online, BA/AA ledger hashes = document rows (not seat responses), B1 probes = void. A 200/content-null must be filed liveness-only.
- **E-2 (closes D-1):** re-seam the **AoA's internal version divergence** — AoA §0 line 14 vs §4.2 lines 164/166 — and record BOTH commit pairs (`f4feeb4fc0`/`34424e81ac` and `6de5aba311`/`2cc6f1832f`) in the version ledger with the non-ancestor receipts, keeping divergence as signal.
- **E-3 (closes D-2):** **strike or receipt the header PIN claim** — produce question sha + responding_model + PIN echo + `content_head`/`reasoning_tokens`/`max_tokens` for the act-1 fire, or delete "PIN-READ-BACK VERIFIED at the fire" from line 3. Under AM-C2 a 200-with-null cannot carry it.
- **E-4 (precision):** replace the ± line-count notation with measured counts (CA 148 / BA 172 at task-named sends; 78 / 134 at earlier sends) and re-pin the four blobs from §1.3.
- **E-5 (target's own close condition, adopted):** dispatch the four unrun AM-F3 arms — `re-cut-write-gate-surgical` `9811e52752` · `r2gate`/`round2-gate` `268bb09147` · `r2cs` `c39d8ce722` / `r2cs-sync` `42198f5e6d` · `origin/fix/restore-read-action` `ec649ad9d0` — as matrix legs with a raw receipt plus an AM-F2 content-gate row or NOT-RUN-with-reason; F-16 stays named. This is the ADJUSTED-NEEDS close condition, never a silent "4/8 = PASS."

---

## 4. Wall-clause QUESTIONS, each with its minimal experiment

- **Q-1 (D-1):** Is the AoA's commit divergence only AoA-vs-task, or internal? *Minimal experiment:* read AoA:14, :164, :166 side by side; run `git merge-base --is-ancestor` on both pairs; record both. Result above: internal divergence — DEFECT.
- **Q-2 (D-2):** Does the target's header PIN claim have any receipt? *Minimal experiment:* `grep -nE 'question.?sha|responding_model|PIN echo|content_head|reasoning_tokens|max_tokens' REVERIFY-AMS3-20261123.md`; only the B1-seat paraphrase at :110 appears, none for the target's own fire. Absence ⇒ UNKNOWN; produce receipt or strike the clause (E-3).
- **Q-3 (D-3):** Does any fan landing's verdict rest on a probe response used as content? *Minimal experiment:* the five-row content-ingress table of E-1; each row re-derived from the cited receipt, void filed UNKNOWN. No landing is promoted on a liveness-only 200.
- **Q-4 (inherited B1 OI-1):** Is fire #5's content-bearing window a rare stochastic state or question/budget-conditioned? *Minimal experiment:* stochastic re-probe at fire with a REAL question at a content-bearing budget, capturing PIN echo + `content_head` + `reasoning_tokens` + `max_tokens`; void ⇒ UNKNOWN, never a settlement. (Open in B1:1599; kept open here.)
- **Q-5 (AM-F3 close):** Do the four unrun arms carry legs? *Minimal experiment:* one leg row per arm per E-5; F-16 stays named.
- **Q-6 (SW-1 mechanism):** Why did three lanes report shas that point at nothing? *Minimal experiment:* `git rev-parse --verify` each of `ab660b943b`/`16130475d2`/`f4b845f05b`; all fatal (S20); mechanism stays UNKNOWN, never guessed.

---

## 5. Limitations and explicit unverifiable-from-this-pass list

- This is a **COLD re-read**, not a re-fire. **No seat was probed by this lane**; no battery re-run, no harness or GGUF touched, no install. Accordingly I do not manufacture a PIN/content-bearing probe receipt for myself — the target's own claim of one (D-2) is filed UNKNOWN on the record.
- Only the owning host can confirm: R8's live-HF model sha (CA:104), the run-time sandbox envelope / egress receipt (BA §5), live PR #1 status, the remote matrix columns' cross-runner determinism (p0tat0/c0wb0y/cloud), and the SW-1 mechanism. None is asserted verified here.
- Line references are from the pinned blobs (§1.3); where a landing's own line numbers age, claims were re-derived by symbol and number, not by position alone.
- The target's ± line-count notation (S34) is not falsified — the measured counts sit inside the stated ranges — but it is imprecise; E-4 records exact values.
- Blind clause honoured: FAN2-BA and FAN2-AA drafts were not opened.

---

## 6. Reproducibility (all local, no install)

```
cd /root/workspace/repos/hermes-agent
git log --all --oneline | grep 4c049ec82b
git rev-parse 4c049ec82b:studies/rfc-143379-rig/plan/tank/REVERIFY-AMS3-20261123.md
git hash-object studies/rfc-143379-rig/plan/tank/REVERIFY-AMS3-20261123.md
for s in 4c049ec82b 93d2def129 cfed8b30f9 f4feeb4fc0 34424e81ac 760092f1eb 2ce77ce5ad \
         73b4cbead7 9d74420def f32f5ab716 6609dac951 6609dacba9; do git rev-parse --verify "$s^{commit}" 2>/dev/null || git rev-parse --verify "$s"; done
for s in ab660b943b 16130475d2 f4b845f05b; do git rev-parse --verify "$s" 2>/dev/null || echo UNRESOLVED; done
git merge-base --is-ancestor 6de5aba311 f4feeb4fc0; echo $?   # 1 = not ancestor
git merge-base --is-ancestor 2cc6f1832f 34424e81ac; echo $?   # 1
git merge-base --is-ancestor 2ce77ce5ad 760092f1eb; echo $?   # 1
git show f4feeb4fc0:studies/rfc-143379-rig/plan/tank/lane-ca-audit-20261121.md | wc -l  # 148
git show 34424e81ac:studies/rfc-143379-rig/plan/tank/lane-ba-audit-20261121.md | wc -l  # 172
```
All study reads via `read_file` / local `git show`; no `web_extract`. Working-tree changes present at commit time are left AS FOUND; this commit stages only this deliverable's path.

---

## 7. Emission contract

This file was written on disk FIRST with the verdict, the 34-row table, and all receipts inside, then staged and committed as `kanban-pilot <pilot@rig.local>` with **only this path**, on the current HEAD re-checked at commit, never pushed; master append-only; plan, sealed artifacts, crons, anchors and sibling plates left AS FOUND; local config left AS FOUND. Index locked: wait 10s, retry once on contention. A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.

*Facimus semper — the re-verification renders on the receipts; the receipts are on the record; the record corrects itself out loud. Nothing public; RFC #143379 / #5320 / #157065 quiet.*
