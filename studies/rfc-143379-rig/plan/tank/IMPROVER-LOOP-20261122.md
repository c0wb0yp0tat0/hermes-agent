# IMPROVER-LOOP-20261122 — the Amazon-style improver loop over the PILOT KIT stack's landed corpus

**Seat:** tencent/hy4-flash:free · **Branch:** study/rfc-143379-rig-20261105 · **HEAD at entry:** `6c49affd58747d6572ad270fa22554cb4007e19d`
**Contract:** IMPROVER-BRIEF-20261122.md (read in full, binding) · **RFC #143379:** QUIET · **nothing public** · **no installs** · **no push** · **no checkout / stash / rm** · writes only under `studies/rfc-143379-rig/`.
**Wall clause:** a non-reproduction is a QUESTION with receipts — never a guess, never a silent pass.
**Termination:** two consecutive rounds with zero measurable total delta → PARK with the record and stop.

---

## 0 · ARMMENT & REFUSAL (operator directive, applied before the loop)

**Loaded and applied:** `think-tank` (spine: classify→choose→probe→evaluate→adopt/park→standardize→verify; this loop's `adopt or park` node), `agent-work-review` (full reads → consistency matrix → arithmetic re-derivation → explicit unverifiable list), `investigation-documentation` (faithful discovery log + Limitations/Reproducibility), `external-readiness-review` (the nine canonical condition areas used as the armor ruler), and `night-20261121/BRIEF-KIT-METHOD-CARDS.md` (receipts-not-claims; append corrections; no smoothing).

**Named-and-refused (rest of the inventory):** every other loaded skill — the remaining `autonomous-ai-agents/*`, `creative/*`, `devops/*`, `email/*`, `github/*`, `hermes/*`, `inference/*`, `media/*`, `mlops/*`, `note-taking/*`, `productivity/*`, `research/*`, `software-development/*`, and the deferred MCP/rea/wolfram tools — is **out of arm** for this leg. Ground: the brief's envelope (no new arms, no gate changes, no canary re-scoping, no public surfaces, no installs) and the plan guard. Refusal is recorded, not debated.

---

## 1 · CORPUS READ MANIFEST (in the brief's order, all LOCAL via read_file)

| # | Artifact | Path | Read status |
|---|---|---|---|
| 1 | The OPUS (launch package) | `plan/tank/OPUS-PILOT-KIT-20261121.md` (184 ln) | READ IN FULL ✓ |
| 2 | The AoA (audit-of-audits) | `plan/tank/aoa-audits-20261121.md` (189 ln) | READ IN FULL ✓ |
| 3 | Three cross-audits | `plan/tank/lane-{ba,aa,ca}-audit-20261121.md` | **NOT LANDED at cited path** — wall-clause Q |
| 4 | Three brainstorm artifacts | `plan/tank/lane-{a-minimal-demonstrable,b-phase1-design,c-verification-readiness}-20261121.md` | **NOT LANDED at cited path** — wall-clause Q |
| 5 | Three contracts | `plan/tank/briefs/{CROSS-AUDIT-BRIEFS,AOA-BRIEF-20261121,GATHER-BRIEF-20261121}.md` | **NOT LANDED at cited path** — wall-clause Q |
| 6 | WEIGHTS-RUNG pre-reg | `studies/rfc-143379-rig/WEIGHTS-RUNG-PRE-REG-20261121.md` (78 ln) | READ IN FULL ✓ |
| 7 | WEIGHTS-RUNG battery | `WEIGHTS-RUNG-BATTERY-20261122.md` | **NOT LANDED** ("if landed" — did not land) — Q |
| 8 | Wedge landing | `WEDGE-ROOT-FIX-20261122.md` | **NOT LANDED** ("if landed" — did not land) — Q |
| 9 | GAP-3 battery deliverable | `.../GAP-3-300-gate-battery/` — verdict.json, ledger.json, run-record.md, battery.py, verdict-row.md | ALL 5 READ IN FULL ✓ |
| 10 | Grounds: cells / NM-3 / pilot verdict | `CANARY-CELLS-20261120.json` (35 ln), `OPUS-NM3-CANARY-20261120.md` (53 ln), `PILOT-VERDICT-20261121.md` (33 ln) | READ IN FULL ✓ |
| 11 | Grounds: audits / plan / arms | `LOSS-LADDER-AOA` (151), `LOSS-LADDER-AUDIT` (216), `MASTER-HITL-GIST-AOA` (170), `PILOT-KIT-PLAN` (86), `FINAL-LEG-PLAN` (32), `RECORD-MINE` (261) | READ IN FULL ✓ |
| 12 | Kit method cards | `night-20261121/BRIEF-KIT-METHOD-CARDS.md` (16 ln) | READ IN FULL ✓ |

Search receipts for the non-landed members: `search_files(target=files)` across `/root/workspace` on each exact filename returned no `.md` at the cited study path. Eight are absent from every local archive scanned (`master-page`, `drop`, both `mechanism-of-mechanisms*` repos); `CROSS-AUDIT-BRIEFS.md` exists only at the off-study `/root/workspace/drop/CROSS-AUDIT-BRIEFS.md`. All eight+one are recoverable from **git objects** in this repo (e.g. lane-B design `1f0309974b`/`3a7afc066a`, lane-BA `2cc6f1832f`/`7190c0efda`, A+C fold `141649ac15`/`d92eac73a3`) but **not via the mandated read_file path**. Per the AoA's SW-2 this is the harness fold's tree-state, not a lane defect and not this lane's to repair: never checkout/rm/stash; no materialization. They enter the record as open QUESTIONS.

---

## 2 · BASELINE GATE RE-DERIVATIONS (round 0 — every number re-derived, raw)

| Artifact | Its own gate | Baseline (raw) | Re-derivation receipt |
|---|---|---|---|
| OPUS | compose-check table (8 marks) | **8/8 FIRED** (mark 2 via proxy) | rows 1–8 each carry a FIRED state + evidence line; OPUS §compose-check + §Re-verify ledger |
| AoA | verdict re-derivations (3 audits + stack verdict + falsifier) | **ADAPT stands**; 6 real shas exist, 3 reported shas phantom | `git cat-file -t`: `2cc6f1832f`/`2ce77ce5ad`/`6de5aba311`/`20d11790c8`/`1f0309974b`/`141649ac15` = commit ✓; `16130475d2`/`ab660b943b`/`f4b845f05b` = Not a valid object ✓ (SW-1 confirmed) |
| WEIGHTS-RUNG pre-reg | 8-mark compose-check + bars B0/B1/C | **0/8 marks resolved** (every cell literally `FIRED/ABSENT`); bars ≥20pp & B1≥0.85C pre-committed | regex over §6 table: 8 rows, 0 single-state; §4 bars |
| GAP-3 battery | ledger rows (instrument re-run) | **7/7 rows MATCH** on-disk verdict.json; 3 PASS / 4 BLOCKED; vacuous 47/69 = 0.6812 | imported `battery.py`, ran `run_all(build_fixture())` in memory (no file writes): all 7 statuses MATCH; `round(47/69,4)=0.6812` ✓; `model_execution_rows` = junctions/read_decide/variance/gate300 ✓; certification = NOT-YET-CERTIFIED |
| Pilot verdict / grounds | cells numbers | **all match** cells: sha `fc8b9934…`, safetensors `5747a90e…`, bytes 641,262,336, load 0.95, params 319,028,736, logits `[1,4,129280]`, argmax 49969, diff 0.0, MIT+compatible, egress 647,716,330 / 0 secondary | read_file of cells + NM-3; 42/42 & 31/35 are *cited* on the verdict, not re-run here (no test execution, no installs) → ON-GROUND, not RE-DERIVED |
| Armor (nine conditions) | external-readiness-review reality | **C8 COVERED; C5/C7/C9 PARTIAL; C1/C2/C3/C4/C6 UNKNOWN/OPEN** | §C.3 done-whens defined but G3 OPEN; no SHA256SUMS / anchor session log / stats appendix / OSF link in the landed corpus |

---

## 3 · IMPROVEMENT SPECS (named, measured, revertible — expected deltas, NOT receipts)

- **I1 — WEIGHTS-RUNG pre-reg compose-check resolution.** What: append a resolution row to §6 turning the 8 literal `FIRED/ABSENT` cells into determinate states — marks 1–7 → FIRED (grounded in §§0–5 + this file's own bytes), mark 8 → HELD-OPEN (run not fired; `WEIGHTS-RUNG-BATTERY-20261122.md` not landed; §7 review-loop OPEN). Measured property: count of FIRED marks (0 → 7) and determinate states (0 → 8). Expected delta: **+7 FIRED, +8 determinate, +1 correctly held-open**. Revert: delete the appended row.
- **I2 — OPUS receipt-availability ledger.** What: append a ledger tagging the 12 seal-cited paths (3 PRESENT, 8 ABSENT-everywhere, 1 off-study present) and converting the 9 unresolvable-at-cited-path citations into wall-clause QUESTIONS with their git-object homes named as the seam — no file materialization, no history rewrite. Measured property: seal citations silently unresolvable via the mandated read path (9 → 0 untagged). Expected delta: **−9 silent unresolvable, +9 tagged questions**. Revert: delete the appended ledger.
- **Non-improvements (disconfirmed before landing):** AoA verdict re-derivations re-derive cleanly (no number to move — its §9 already parked its own loop); GAP-3 battery rows re-derive 7/7 exactly (0 headroom; the 4 BLOCKED rows need a model run — no installs, no public, RFC quiet); pilot verdict numbers are cited on-ground, not re-runnable here. Each is recorded as a zero-delta artifact, not padded.

*(Gate receipts and raw deltas land below as the rounds execute.)*

---

## 4 · ROUND EXECUTION (receipts, raw)

### Round 1 — two improvements applied, every gate re-run

**I1 applied** — `WEIGHTS-RUNG-PRE-REG-20261121.md` §11 appended (commit `4d8f8a5e3e`).
Gate re-run (parsed from disk, not from narration): original §6 table **still** 8×`FIRED/ABSENT` (unchanged — history intact); appended resolution row = **7 FIRED + 1 HELD-OPEN**, 8 determinate.

| Measured property | Baseline | Re-run | Raw delta |
|---|---|---|---|
| FIRED compose-check marks | 0 | 7 | **+7** |
| Determinate states | 0 | 8 | **+8** |
| Correctly held-open (mark 8, run un-fired) | 0 | 1 | **+1** |

**I2 applied** — `OPUS-PILOT-KIT-20261121.md` receipt-availability ledger appended (commit `f0e78cf3ca`).
Gate re-run: 12 ledger rows (3 PRESENT / 9 ABSENT), 9 tagged QUESTION Q1–Q9, 0 untagged-unresolvable; the artifact's own 8-mark compose-check is **unchanged at 8/8**.

| Measured property | Baseline | Re-run | Raw delta |
|---|---|---|---|
| Untagged-unresolvable seal citations | 9 | 0 | **−9** |
| Tagged wall-clause questions | 0 | 9 | **+9** |
| OPUS compose-check FIRED | 8 | 8 | 0 |

**Zero-delta artifacts in Round 1 (disconfirmed before landing anything):**
- **AoA** — verdict re-derivations re-derived: 6/6 named real shas exist (`git cat-file -t` = commit), 3/3 reported shas invalid (SW-1 confirmed) → ADAPT stands. Delta **0**. Its own §9 had already parked its loop.
- **GAP-3 battery** — `battery.py` re-imported and `run_all(build_fixture())` re-executed in memory: statuses `PASS,PASS,BLOCKED,BLOCKED,PASS,BLOCKED,BLOCKED` = **7/7 MATCH** vs on-disk verdict.json; `round(47/69,4)=0.6812`; certification NOT-YET-CERTIFIED. Delta **0** (the 4 BLOCKED rows need a live model run — no installs, no public, RFC quiet; wall clause → open item, not a fabricated pass).
- **Pilot verdict / grounds** — cells numbers match (sha `5747a90e…`, params 319,028,736, diff 0.0, egress 647,716,330 / 0 secondary). 42/42 and 31/35 are *cited* on the verdict, not re-run here. Delta **0**.
- **Plan/arm documents** (PILOT-KIT-PLAN, FINAL-LEG-PLAN, RECORD-MINE, method cards) — records, no numeric gate owned. Delta **0**.

**Round 1 total delta:** +7 / +8 / +1 / −9 / +9 — **non-zero → continue**.

### Round 2 — re-derive all gates, seek a further improvement

| Property | Re-derived value |
|---|---|
| pre-reg FIRED / determinate / held-open | 7 / 8 / 1 |
| OPUS tagged questions / untagged-unresolvable / compose FIRED | 9 / 0 / 8 |
| GAP-3 battery MATCH | 7 / 7 |
| AoA real commits / phantom shas invalid | 6 / 6 · 3 / 3 |
| cells coherence | 1 / 1 |

Further-improvement scan: unresolved placeholders in the pre-reg resolution row = **0**; OPUS untagged-unresolvable rows = **0**; battery rows all MATCH; AoA shas all confirmed. No named, measured, revertible change remains that can move a gate number without an install, a model run, a public surface, or a plan alteration (all hard-lined). **Round 2 total delta = 0.**

### Round 3 — repeat the full re-derivation

Same nine properties re-derived from disk: `7/8/1`, `9/0/8`, `7/7`, `6/6 · 3/3`, `1/1`. Per-property delta R2→R3 = **0 on all nine**; total absolute delta = **0**. No new actionable improvement (same disconfirmation).

### Convergence / PARK

Rounds **2 and 3 are consecutive zero-delta rounds**. Termination condition is met → **PARK with this record and stop.** No expansion, no orbit, no arm re-ordering, no new arms, no gate changes, no canary re-scoping, no public surfaces.

---

## 5 · FINAL VERDICT — dry-run ruler (COVERED / PARTIALLY-COVERED / GAP / UNKNOWN)

**Corpus as a whole: PARTIALLY-COVERED.** The landed core is grounded and re-derivable (execution layer covered; 8/8 OPUS compose-check; 7/7 battery structure; pre-reg bars pre-committed and its compose-check resolved), with named seams: verification independence and certification remain open, and a material fraction of the named corpus is not landed — recorded as UNKNOWN, never smoothed into a pass.

| Corpus member | Verdict | Basis |
|---|---|---|
| OPUS launch package | PARTIALLY-COVERED | 8/8 compose-check; 9 seal citations now tagged questions (not silently carried) |
| AoA (stack verdict) | COVERED | verdict re-derivations re-derive; 6 real / 3 phantom shas; ADAPT stands |
| Three cross-audits · three brainstorm artifacts · three contracts | **UNKNOWN** | not landed at cited paths; git-object recoverable only — open QUESTIONS Q1–Q9 |
| WEIGHTS-RUNG pre-reg | PARTIALLY-COVERED | bars pre-committed; 7 FIRED + 1 HELD-OPEN; mark 8 open (run un-fired) |
| WEIGHTS-RUNG battery (`WEIGHTS-RUNG-BATTERY-20261122.md`) | **UNKNOWN** | did not land at this read |
| Wedge landing (`WEDGE-ROOT-FIX-20261122.md`) | **UNKNOWN** | did not land at this read |
| GAP-3 battery deliverable | PARTIALLY-COVERED | structure 7/7 re-derives; certification NOT-YET-CERTIFIED (4 BLOCKED rows) |
| Pilot verdict + canary cells / NM-3 grounds | COVERED | all cited cell numbers re-derive; 42/42 & 31/35 on-ground, not re-run here |
| Plan / arm / mine documents | COVERED (as records) | no numeric gate owned; read in full |

**Armor reality (external-readiness-review, nine conditions):** **C8 COVERED** (scoped claims — "scope-bounded to the stub / tested depths" throughout); **C5 / C7 / C9 PARTIAL** (cited study numbers present but no related-work section; cost ledger cited 3.66× / $0.00 / 5.8¢ shadow premium; cells MIT+compatible but no fair-use analysis in the landed corpus); **C1 / C2 / C3 / C4 / C6 UNKNOWN-OPEN** (no SHA256SUMS kit, no enforced grader pin, no anchor session log, no statistics appendix, no OSF/Zenodo registration — G3 remains OPEN). Re-checked on disk this loop: C1/C3/C4 artifacts ABSENT, C6 no OSF/Zenodo string in the pre-reg.

---

## 6 · OPEN ITEMS — non-reproductions as QUESTIONS with receipts

1. **Q1–Q9** — OPUS seal citations unresolvable at their cited paths via the mandated read method; git-object homes named (e.g. lane-B design `1f0309974b`, lane-BA `2cc6f1832f`, A+C fold `141649ac15`). Receipt: OPUS appended ledger + AoA SW-2 (harness fold removed `plan/tank/` from tracking). **Not repaired here** — others' files; never checkout / rm / stash.
2. **Mark 8 of the pre-reg** — HELD-OPEN: no run fired; battery artifact not landed. Receipt: pre-reg §7 + §11 resolution row.
3. **GAP-3's 4 BLOCKED rows** (junctions, read_decide, variance, gate300) — free-tier quota exhausted (exit 75), prior attempts 12–21; plus the literal `@<commit>` identifier placeholders in verdict.json/ledger.json/verdict-row.md (a sha cannot be invented). Receipt: GAP-3 run-record.md + battery.py re-run.
4. **Armor C1/C2/C3/C4/C6** — open; receipt: on-disk absence checks above + OPUS §C.3 done-whens.

**Concurrent-tree note (not mine, untouched, not committed):** `studies/rfc-143379-rig/SCRIBE-WITNESS-REGISTRY.log` is modified; `night-20261121/BRIEF-WEDGE-ROOT-20261122.md` and `plan/tank/briefs/IMPROVER-BRIEF-20261122.md` are untracked — other lanes' files. The `briefs/` directory contains **only the contract brief**; the three contracted artifacts did **not** land. No checkout / stash / rm / push was performed on any of them.

---

## 7 · LIMITATIONS + REPRODUCIBILITY (investigation-documentation discipline)

- **Read in full via `read_file`:** all LANDED corpus members (§1), the four arming skills, the method cards. **Never** `web_extract`, never a guessed path.
- **Re-derived by execution:** battery rows (instrument imported, run in memory, no file writes), vacuous ratio, pre-reg compose-check states, OPUS ledger counts, AoA sha liveness, cells coherence, armor file-presence.
- **Cited, not re-run:** 42/42 read-restore, 31/35 W2 presence, M1 stamp, channel-lift study numbers — these are on-ground measurements; re-running them would need test execution / model calls (no installs, no public surfaces). Labeled ON-GROUND, not presented as this loop's receipts.
- **Repro commands (from `/root/workspace/repos/hermes-agent`):** `git cat-file -t <sha>` for AoA shas; import `.../GAP-3-300-gate-battery/battery.py` and call `run_all(build_fixture())`, compare to `verdict.json`; regex-count `FIRED/HELD-OPEN` in pre-reg §11 and `QUESTION Q\d+` + numbered FIRED rows in the OPUS; `search_files(target=files, path=/root/workspace)` on the nine cited filenames.
- Raw numbers are reported unsmoothed; expected deltas in §3 were stated before the re-runs and are not commingled with receipts.

---

## 8 · HARD-LINES COMPLIANCE

nothing public ✓ · RFC #143379 QUIET ✓ · no installs ✓ · writes under `studies/rfc-143379-rig/` only ✓ · all corpus reads local via `read_file` ✓ · no push ✓ · no `git checkout --` / `git rm -rf` / `git stash` ✓ · index unlocked (no lock retry needed) ✓ · plan unaltered — no arm re-ordering, no new arms, no gate changes, no canary re-scoping, no public surfaces ✓ · history never rewritten — all edits are appends ✓.

---

## 9 · COMMITS + STRONGEST IMPROVEMENT

- `4d8f8a5e3e` — I1, pre-reg compose-check resolution (append-only).
- `f0e78cf3ca` — I2, OPUS receipt-availability ledger (append-only).
- This record lands as its own commit on the study branch (sha reported in the lane report).

**Strongest applied improvement:** **I1 — pre-reg compose-check resolution.** It moved the artifact's own gate count from **0 FIRED marks to 7** (**+7**, with 0→8 determinate states), re-derived from the on-disk resolution row after the append; mark 8 was correctly held open rather than promoted. I2 (OPUS) is the runner-up at **−9 untagged-unresolvable → 0** (**+9** tagged wall-clause questions) with the compose-check unchanged at 8/8.

*Facimus semper — the loop parks on the convergence; the record corrects itself out loud. PARK.*
