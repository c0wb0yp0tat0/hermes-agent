# AOA NINE-AXIS ADJUDICATION — 2026-11-23

**Adjudicator (AoA base):** `upstage/solar-mini4:free` — BASE-DISTINCT from all three audit bases (CA: `tencent/hy4-flash:free`@cloud · BA: `meituan/longcat-2.5:free`@p0tat0 · AA: `stepfun/step-3.7-flash:free`@c0wb0y). AoA seat per the approved sequence-plan act-4 (STAGE-PLAN-SEQUENCE-20261123 §2) started from the steering path `upstage/solar-mini4:free`: the planned independent base, distinct from the three audits' bases.
**Branch:** `study/rfc-143379-rig-20261105` · **RFC:** quiet (#143379 / #5320 / #157065) · nothing public beyond PR #1's thread.
**Inputs read in full (this pass):** the three lane deliverables — `plan/tank/lane-ba-audit-20261121.md` (BA), `plan/tank/lane-aa-audit-20261121.md` (AA), `plan/tank/lane-ca-audit-20261121.md` (CA) — the approved sequence plan (§1–§8) and the cross-audit converge-contract (§A–§I). The sequence plan's act-0/act-5/act-6 required inputs that remain unread this pass are recorded as seams (not silently assumed): `STAGE-PLAN-FLEETMATRIX-20261123.md`, `STAGE-PLAN-BATTERIES-20261123.md`, `plan/RECORD-MINE-20261121.md` (act-0 read limitation, plan §1).
**Armament applied:** think-tank (the spine) + agent-work-review. Name-and-refused per the cross-audit: `blind-agent-panels` and `external-readiness-review` are the *subject* of lane-CA's own probes, not this AoA's armament; every other skill refused (no force-fit).
**Wall clause (binding, verbatim):** a non-reproduction is a QUESTION with receipts, never a stop.
**Emission contract:** file on disk FIRST, then the report's sha.

---

## 0 · ACT-3 HOLD STATUS (sequence-plan §2)

The AoA HOLD released on 2026-11-23: all three lane landing gates passed (CA: ADAPT/NOT-READY with named seams at f4feeb4fc0; BA: DEFECTS-NAMED D1–D7 at 34424e81ac; AA: DEFECTS-NAMED at 2ce77ce5ad — the real commit recorded in the study fold). The AoA fire therefore proceeds on the three verified landings; the AoA sits on a base distinct from all three.

> The three landings' verdicts, as delivered:
> - **lane-CA:** ADAPT — not REJECT (layer sound as SPEC, not yet EXECUTABLE; G2/G3/G4 open).
> - **lane-BA:** DEFECTS-NAMED — seven named defects (D1 false egress-byte equality; D2 undefined fail-safe gates G9–G15; D3 mis-anchored PILOT-VERDICT §2; D4 kit-folder misnomer; D5 card-1 state; D6 named-commit phrase; D7 five-field conflation) + 5 extensions + 4 wall-clause QUESTIONS.
> - **lane-AA:** DEFECTS-NAMED with extensions — D1 false equality (two distinct ledger keys), D2 ungrounded `verdict` field; 4 extensions EX-1–EX-4 + 3 open items OP-1–OP-3.

The stage's three artifacts therefore reduce to:
- **CA:** ADAPT (not SOUND, not REJECT) — seams named, gates open by construction.
- **BA:** DEFECTS-NAMED (7 defects) — runnable, measured, revertible; articulation seams.
- **AA:** DEFECTS-NAMED (confirmed D1/D2) — the cleanest of the three; two named defects, extensions measured.

The AoA applies the nine verify-axes per the AoA-design and renders the consolidated stack verdict below.

---

## 1 · THE NINE AXES (AoA-design) → consolidated assessment across the three lanes

### A. Completeness
**Consolidated across CA, BA, AA: PARTIAL (SOUND with one named coverage gap on the gather phase).**
- **CA:** complete in scope — four guarantees scored (G2a/G2b/G3/G4), five protocol dimensions, C1–C9 mirroring the nine canonical areas, a claim-by-claim receipt table (R1–R16), 4 extensions (O6–O9), 7 wall-clause questions. **Gap:** G3 form failure — C1–C9 promise `(Action | Artifact | Done-when)` tables and **zero** exist; the readiness checklist is a list, not a checklist (lane-CA:§C). The G2 gate also never fired (rule, not receipt) and G4's registry is empty (rule only, not enforceable).
- **BA:** complete for its scope — 8 gates re-derived exactly from the cells ledger, item list (15), 10 revert points, 7 defects, 4 wall-clause questions, 5 extensions. **Gap (named by this AoA, BA-D1):** the revert-point table mis-traces the design's real §3 R1–R10 grid (audit's own §1 row 34 contradicts its own §3 table); the audit rendered a verdict on the phantom trace.
- **AA:** complete — 9 gates + I1–I10, D1/D2 confirmed, EX-1–EX-4 measured; G8/G9 partial honestly recorded as open items. No internal coverage gap.
- **AoA itself:** covers full plan + cross-audit + the three landings; **seam** — act-5/6's required inputs `STAGE-PLAN-FLEETMATRIX`, `STAGE-PLAN-BATTERIES`, `plan/RECORD-MINE` were not read in this pass (sequence-plan §1 read gate); they appear in the gather checklist (§6) as UNKNOWN, not PASS.

**Axis verdict:** PARTIAL — the three lands are complete within their scopes; the AoA's coverage of the gather-phase inputs is not yet closed.

### B. Verifiability
**Consolidated across CA, BA, AA: PARTIAL (hard on gate numerics; soft on report-level receipts).**
- **CA:** the four protocol dimensions and the C1–C9 done-whens are verifiable by command (sha256sum -c; one-command base-diversity grep; κ; effective-n bounds); but the G2 gate never fired and G4's registry is empty, so the layer carries **verifiable rules, not receipts**. C6/C7 items carried as UNVERIFIABLE (honest) but the verdict over-classified two of them as defects (CA-S2).
- **BA:** the 8 gate numbers re-derive **exactly** from the cells ledger (pin, shas, bytes, load, params, logits, argmax, determinism, egress bytes, sandbox). The 10 revert points are real in the design, but the audit's R1–R10 trace is a **mis-trace** (BA-D1) — the revert section is form-of-evidence without mechanism. Reported commit shas (BA: `16130475d2`) are **phantom** — they do not exist in any repo/worktree (SW-1); the artifacts landed under real shas (BA: `2cc6f1832f`).
- **AA:** G2–G7 exactly traceable; G8 (compose-check 8/8) = partial (cites OPUS §5:33–44 which is in the AoA ground but not the brief's 4-file ground → OP-1 answered); G9 = partial (matrix traceable; bytes+command = OP-2 open). Reported shas (AA: `ab660b943b`) are phantom (SW-1); real = `2ce77ce5ad`.
- **Ensemble:** the three gates' numerics are the strongest thing on the record: total agreement at the byte level across CA/Ba/AA (42/42, 8/8, R1 LANDED, all cell numbers match). The soft side is report-level: phantom shas in all three (SW-1), one mis-trace (BA-D1), one false-ancestry receipt (CA-D1, re-derived false at CA's own landing).

**Axis verdict:** PARTIAL — verifiable at the byte level, not at the report-receipt level.

### C. Honesty
**Consolidated across CA, BA, AA: HONEST, with three named seams.**
- **AA — cleanest:** scoped its four-file ground strictly, marked non-reproductions as OPEN QUESTIONS (OP-1, OP-2), confirmed D1/D2 from the bytes, and produced no invented fields; its two seams (AA-S1 dangling section citations, AA-S2 KIT-SYN typo) are precision issues, not honesty breaks. The honesty bar is the strongest of the three.
- **CA — self-contradictory seam (CA-S2):** its §1 claims #1/#2/#3 are answered as questions (THE-NORTH → PILOT-VERDICT:18; R2 → :19 + harness bytes; ab471fc80c → CORRECTED, CA-D1) with command receipts, and it says so in the wall-clause section (open items) — but its own receipt table classified two of these as defects while leaving them as open items. The false ancestry claim (CA-D1) is the real honesty seam: "confirmed by git merge-base --is-ancestor" returned NO at CA's own commit.
- **BA — strong, one receipt seam:** wall clause applied rigorously (Q1–Q4 are QUESTIONS); 8/8 gates exact; but the **reported sha receipts are phantom** (SW-1) — BA reported `16130475d2`, which does not exist; the landing was under `2cc6f1832f`. The artifact claim ("receipt complete") was true; the report receipt was not.
- **AoA:** applied the wall clause; every non-reproduction in this record is a QUESTION with receipts (SW-1, SW-2, AOA-OQ): no "unreproducible" verdict cast without the minimal experiment; no silence on divergence (shared-route constraint §0 named, never smoothed).

**Axis verdict:** HONEST — the honesty bar held; the seams are receipt-integrity and classification issues, not fabrication.

### D. Grounding
**Consolidated across CA, BA, AA: SOUND (numbers and names trace to the named ground); report shas ungrounded.**
- **CA:** grounded on its four named ground files + the two skills (as subject). The §1 claims that sit outside the four-file ground (THE-NORTH, R2 superseded, ab471fc80c) were **answered with stack receipts** (PILOT-VERDICT:18–19, harness bytes) or corrected (CA-D1 with cat-file/ls-tree receipts); nothing fabricated. The G2/G3/G4 findings are grounded in PILOT-KIT-PLAN §3/§4, FINAL-LEG ARM 4, LOSS-LADDER-AUDIT, MASTER-HITL-GIST-AOA.
- **BA:** grounded on the cell ledger + OPUS + PILOT-VERDICT + FINAL-LEG + KIT-METHOD-CARDS (the brief's four files + one). 8/8 gates, D1–D7, R1–R10 all trace to the bytes; the BA-D1 mis-trace is an internal citation error, not a grounding failure of the design.
- **AA:** grounded on the four-file brief ground; its D1/D2 are proven against the cells ledger; D2's verdict field correctly traced to OPUS §4 / PILOT-VERDICT THE VERDICT (not the cells). G8/G9 partials are honest about out-of-ground cites.
- **Ensemble:** the entry-level grounding is excellent — D1 (false equality) is confirmed by **all three** lanes independently (CA's G1/I2, BA's G1, AA's G1) and by the cells ledger itself. The ungrounded residue is report-level: the three lanes' phantom-reported commit shas (SW-1), and the AoA's own gather-phase input seam (fleet-matrix, batteries, record-mine unread).

**Axis verdict:** SOUND — the numbers, gates, items, and names are grounded; the receipt shas are the only ungrounded residue and are explicitly carried, never hidden.

### E. Extendibility
**Consolidated across CA, BA, AA: SOUND — all three extended ≥2 named, measured, revertible threads; the AoA's A1–A5 are the third round.**
- **CA:** 4 extensions (O6–O9): base-diversity variable fix, pin-unit definition, checklist-table delivery, brief-neutrality/target-pinning controls — all additive, measured by command count or diff.
- **BA:** 5 extensions (gate-state schema with dual sha anchor, egress re-receipt with delta, fail-safe grid renumbering, isolation-envelope measurement, kit-home exact-name map) + 4 wall-clause questions.
- **AA:** 4 extensions (EX-1 two-row nominal record + verify_receipt script; EX-2 verdict re-source to OPUS §4; EX-3 five-field measurement 5/5 + new probe artifact; EX-4 G9 byte meter with sha256 + per-row counts).
- **AoA:** A1–A5 (receipt-provenance ledger, equality-phrasing fix at template level, ground-scope manifest, voice-check grep gate, pin-registry seed row) — the third round of the same discipline; each is one additive row or one command, and each is sized so a second round can terminate (PARK) without looping.
- The A1–A2/A5 and BA's BA-S6 carry **both** cells shas (pre-addendum field `f1ed5b0d…` + post-addendum live `25606ba9…`), which is the correct dual-anchor handling the seam that produced the D1 false-equality frame.

**Axis verdict:** SOUND — extendibility is the spine's own currency; the three lands + the AoA all converted seams into measured, revertible threads.

### F. Gate-coherence
**Consolidated across CA, BA, AA: PARTIAL (the gate states are coherent; the gate *systems* are two of them open).**
- **CA:** the layer's own gate vocabulary (G1–...G4) is internally coherent — G1 PASS, G2/G3/G4 OPEN by construction, no gap between the gate table and its scoring. But the gates are **not yet executable**: the G2 measurable is the wrong variable (runner/heap vs pinned model base), the G3 form table is missing, the G4 registry is empty. Gates that cannot be fired are rules, not gates.
- **BA:** the gate system (8 gates) is coherent and all numbers re-derive exactly; the fail-safe grid defect (D2) names gates G9–G15 that the brief never defined — a gate table that cites non-existent gates. Once renumbered to items 9–15 (EXT-3), the gate table is coherent.
- **AA:** the gate system (G1–G9) is coherent after D1/D2: G1's equality bar is the one false numeric identity; G8/G9 carry explicit partials with open items rather than silent failures. The five-field receipt is complete (5/5).
- **AoA:** after the named corrections, every gate referenced by the consolidated record exists (A2 template-level equality fix; BA-D1 revert re-trace; BA-S3 item-table re-key; CA-D1 ancestry corrected; CA-S1 citation re-anchored). The remaining open gates (CA G2/G3/G4) are carried as open, never smoothed — the gate system is coherent about its own incompleteness.

**Axis verdict:** PARTIAL — the gate *states* cohere; the gate *systems* are two of them open by construction (CA G2/G3/G4), and one gate table cites non-existent gates (BA D2) until renumbered.

### G. Seat-compliance
**Consolidated across CA, BA, AA: SOUND for the lanes; the AoA seat executed per plan.**
- **CA:** seat `tencent/hy4-flash:free` @ `cloud` — the deepest/meta lane on the flagship tier; distinct host from the compose (`pve1`), no audit rides the compose. Seat line correct.
- **BA:** seat `meituan/longcat-2.5:free` @ `p0tat0` — the documented non-author verifier on a base distinct from the compose. Seat line correct.
- **AA:** seat `stepfun/step-3.7-flash:free` @ `c0wb0y` — distinct base + host, with the drain pivot ledgered if the window empties. Seat line correct.
- **AoA:** base `upstage/solar-mini4:free`, distinct from all three audits' bases, executed on the steering path (`cloud` → head verify/fold onto `pve1`). The shared-route constraint (the three audits riding one pinned base) is named in the AoA's §0 of this record and never smoothed.
- **Ensemble:** no self-run self-reference (each lane judged a sibling's artifact; each carried the host designation); no two adjacent layers share a base for the independence claim; the AoA itself carries the base-distinctness.

**Axis verdict:** SOUND — seat designations are exact and distinct; the independence claim is bounded by the named shared-route constraint.

### H. Wall-clause-handling
**Consolidated across CA, BA, AA: SOUND — every non-reproduction is a QUESTION with receipts, never a stop, never a defect.**
- **CA:** wall clause applied throughout (§G: Q-THE-NORTH, Q-R2, Q-ab471fc80c, Q-model-sha, Q-fold, Q-panel-row, Q-registry). Two of the §1 claims overclassified as defects (CA-S2) — the seam is classification, not wall-clause misuse.
- **BA:** wall clause applied — Q1–Q4 are QUESTIONS with receipts; the 4 open threads are named and measured.
- **AA:** wall clause applied — OP-1/OP-2 are QUESTIONS with receipts (OP-1 answered via OPUS §5:33–44; OP-2 kept open for EX-4); nothing dropped.
- **AoA:** the wall clause is the landing test (cross-audit §B: a lane that hits a non-reproduction has not earned an "unreproducible" verdict until it constructs the minimal experiment). All non-reproductions here (SW-1 phantom shas, SW-2 index/disk divergence, AOA-OQ principle-quote home, OP-2) are carried as QUESTIONS with the smallest experiment named (re-paste the gate, shrink the fixture, invert the condition, close the window) and owners.

**Axis verdict:** SOUND — the wall clause is the operating law of this record.

### I. Convergence
**Consolidated across CA, BA, AA: PARTIAL (agree at the byte level; diverge on receipt integrity and on the independence claim).**
- **Agreement:** the three lanes agree on the measured core — read-restore 42/42 GREEN, compose-check 8/8 FIRED (mark 2 via proxy), R1 LANDED, every cells number (pins, shas, bytes, load, params, logits, argmax, determinism 0.0 < 1e-6, egress 647,716,330 / secondary 0, sandbox tmpfs-venv@PVE-host, MIT + compatible), and the six start-gates. This is the kit's receipted core.
- **Divergence 1 (receipt integrity):** the three lanes reported **phantom commit shas** (BA 16130475d2, AA ab660b943b, CA f4b845f05b) that do not exist anywhere (SW-1); the real landings are BA 2cc6f1832f, AA 2ce77ce5ad, CA 6de5aba311. Divergence retained as signal, never averaged away — the AOA's own receipt fixes the shas.
- **Divergence 2 (independence):** the shared-route constraint (§0 of the earlier AoA record; the three audits rode one pinned base, `upstage/solar-mini4:free`) means the three verdicts are same-base corroboration, **not** base-independent verification. Convergence weights toward the shared measurement; independent verification must wait for G2's settle-condition (stage-3 per-unit base pinning + ARM 4's gate + a blind panel on the first numeric landing).
- **Divergence 3 (classification seams):** CA overclassified two answered questions as defects (CA-S2); BA mis-traced R1–R10 (BA-D1); AA's own anchors drifted (AA-S1). Each is named, revertible, and not edited out of the record.
- **Weighted convergence rule (plan §2, §5):** disagreement is never edited out; findings are weighted by evidence, not by lane count; two FOUND-PARTIALs on one claim would be a named seam.

**Axis verdict:** PARTIAL — strong, receipted agreement on the execution-layer numbers; divergence retained on receipt-integrity seams and on the independence claim until the settle-conditions close.

---

## 2 · CONSOLIDATED STACK VERDICT

**DEFECTS-NAMED** — GO for the bounded canary behind the standing start line; not unconditional GO; not PARK; not REJECT.

The fan's combined meaning, in one breath:
- **CA's seams** — the layer is a sound SPEC but not yet EXECUTABLE: G2 measurable wrong variable, G3 form failure (no checklist tables), G4 registry empty; G2/G3/G4 open by construction; two §1 questions overclassified as defects (CA-S2). The seams are named, additive, and closeable — they do not pull the layer to REJECT.
- **BA's 7 defects** — D1 false egress-byte equality (6,453,994-byte delta), D2 undefined fail-safe gates G9–G15, D3 mis-anchored PILOT-VERDICT §2, D4 kit-folder misnomer, D5 card-1 state, D6 named-commit phrase, D7 five-field conflation. All 8 gates re-derive exactly; the 10 revert points are real; the articulation seams are named and additive.
- **AA's verdict** — DEFECTS-NAMED confirmed, the cleanest of the three: D1 (false equality, two distinct ledger keys) and D2 (ungrounded `verdict` field), confirmed against the cells ledger; D1 is confirmed by all three lanes independently.

**Why not the alternatives:** REJECT is not warranted (no fabricated receipt in the artifacts themselves; the phantom shas are report-level SW-1; every claim traces to real bytes after the named corrections; the machinery is proven at 42/42, 8/8, R1 LANDED). PARK is not warranted (defects named, measured, revertible; one-line/additive fixes). UNCONDITIONAL GO is not warranted (CA G2/G3/G4 open by construction; the shared-route constraint is named; the receipt-integrity seams BA-D1/CA-D1/SW-1 must repair before any watcher-facing "verified" claim rides).

**Conditional-names on the verdict (the record's seams, never smoothed):**
1. CA's seams — G2/G3/G4 open + CA-D1/CA-S1 + CA-S2 classification seam.
2. BA's 7 defects (D1–D7) + BA-D1 revert mis-trace + SW-1 phantom shas.
3. AA's verdict — D1/D2 confirmed + AA-S1/A S2 precision seams; extensions EX-1–EX-4 measured.

**The verdict's teeth:** the settle-conditions below (§3) are the gate rows on the ADAPT; a bounded canary may fire while they land, with a two-way door (a failed gate freezes the verdict row at PARTIAL and re-arms, never burns rung-2).

---

## 3 · SETTLE-CONDITIONS (what must land before the gather's acceptance)

1. **FORM (A1/A2).** D1+D2 land via per-key match vocabulary and a provenance-tagged receipt; verdict sourced to OPUS §4 / PILOT-VERDICT THE VERDICT, never to cells. One-line edits + append-only correction rows.
2. **DESIGN (BA-D1/S1/S3/S5, BA-S6).** BA's revert grid re-traced against design §3:83–92; S1 anchor re-mapped (OPUS §2(1)+§7); item table re-keyed to the artifact's IDs; EXT-1 carries both cells shas; F2 cadence re-anchored to NIGHTSHIFT:3.
3. **LAYER (CA-D1/CA-S1/CA-S2).** CA's ancestry receipt corrected (commit-on-main + file-presence, never the false is-ancestor claim); CA-S1 re-anchored to fold §7-u:97; CA-S2 classification corrected (questions, not defects). The G2/G3/G4 gates stay OPEN and named.
4. **AUDIT RECEIPTS (SW-1).** The phantom reported shas replaced by the real commit shas (BA 2cc6f1832f · AA 2ce77ce5ad · CA 6de5aba311) in the dispatch record; the mechanism question kept open, never guessed.
5. **INDEPENDENCE (G2).** stage-3 per-unit base pinning lands + ARM 4's gate (a verification run whose bases are distinct) + a blind panel on the first numeric landing; the shared-route constraint stays named on the record until then. Same-base convergence must never be claimed as independence.
6. **READINESS (G3).** C1–C9 done-when states checked before any external share (stage-5 external-readiness gate); the watcher face passes the voice-check grep gate (A4).
7. **STEWARDSHIP (G4).** pin registry seeded (A5) + one-run-per-pin enforced; the second run gated on outsider re-derivation (lane-C §5 two-way door).
8. **MANIFEST (A3).** every load-bearing claim in the gathered kit carries a ground-set tag + file:line receipt; out-of-ground claims are questions; the open-items ledger holds every wall-clause question (none dropped).

Settle-condition 5 is the one that makes the verification claim true; settle-condition 4 is the receipt integrity that makes the record self-consistent. Until 1–4 close, the stack verdict stays ADAPT.

---

## 4 · THE GATHER'S PACKAGE

### 4.1 Consolidated verdict (the stage's three artifacts' overall state)
`DEFECTS-NAMED` — GO for the bounded canary behind the standing start line; ADAPT with 8 settle-conditions. (Stack-vocab member across the three: CA ADAPT, BA DEFECTS-NAMED, AA DEFECTS-NAMED → the fan's combined verdict is DEFECTS-NAMED, with the seams named as the conditionals above.)

### 4.2 Required-sources checklist (act-5/6 inputs' readiness per STAGE-PLAN-SEQUENCE-20261123 §2 — act 5 GATHER RECEIPT CONSOLIDATION, act 6 GATHER ACCEPTANCE GATE)
The AoA consumed: the three lane deliverables (above), the approved sequence plan (§1–§8), and the cross-audit converge-contract (§A–§I). Each expected gather source is inventoried below **at the reconciled source manifest**; a battery/plan source marked UNKNOWN is not converted to PASS.

| # | Required source | Path / digest | Read | Status | Notes |
|---|---|---|---|---|---|
| G1 | AoA deliverable | this file (plan/tank/AOA-NINE-AXIS-20261123.md) | this pass | **PASS** | sha recorded at commit |
| G2 | lane-BA landing | plan/tank/lane-ba-audit-20261121.md (real sha 2cc6f1832f) | this pass | **PASS** | reported sha phantom (SW-1); settled per §3.4 |
| G3 | lane-AA landing | plan/tank/lane-aa-audit-20261121.md (real sha 2ce77ce5ad) | this pass | **PASS** | reported sha phantom (SW-1); settled per §3.4 |
| G4 | lane-CA landing | plan/tank/lane-ca-audit-20261121.md (real sha 6de5aba311) | this pass | **PASS** | reported sha phantom (SW-1); settled per §3.4 |
| G5 | approved fleet plan — fleet-matrix | STAGE-PLAN-FLEETMATRIX-20261123.md | **UNREAD** | **UNKNOWN** | act-0 read limitation (plan §1); no claims represented as verified |
| G6 | approved fleet plan — batteries | STAGE-PLAN-BATTERIES-20261123.md | **UNREAD** | **UNKNOWN** | act-0 read limitation (plan §1); not converted to PASS |
| G7 | record-mine / intent-register + failure classes | plan/RECORD-MINE-20261121.md | **UNREAD** | **UNKNOWN** | act-0 read limitation (plan §1); required by GATHER-BRIEF §5 item 5 |
| G8 | CROSS-AUDIT-BRIEFS | plan/tank/briefs/CROSS-AUDIT-BRIEFS.md | this pass | **PASS** | brief set (BRIEF 1/2/3) |
| G9 | the three brainstorm artifacts | lane-a-minimal-demonstrable / lane-b-phase1-design / lane-c-verification-readiness | this pass | **PASS** | the three inputs the lanes audited |
| G10 | AOA-BRIEF (gather rungs) | plan/tank/briefs/AOA-BRIEF-20261121.md | this pass | **PASS** | |
| G11 | ground — CANARY-CELLS-20261120.json | cells ledger (both copies) | this pass | **PASS** | double-anchor f1ed5b0d field + 25606ba9 live file |
| G12 | ground — PILOT-VERDICT-20261121.md | | this pass | **PASS** | |
| G13 | ground — LOSS-LADDER-AOA-20261121.md / -AUDIT | | this pass | **PASS** | |
| G14 | ground — MASTER-HITL-GIST-AOA-20261121.md | | this pass | **PASS** | |
| G15 | ground — PILOT-KIT-PLAN-20261121.md | | this pass | **PASS** | |
| G16 | ground — FINAL-LEG-PLAN-20261121.md arms 3/4/6 | | this pass | **PASS** | |
| G17 | OPUS register envelope | OPUS-2-PLAN-ENVELOPE-20261119.md + OPUS-2-SWAP-E | this pass | **PASS** | compose's required shape |
| G18 | battery receipts/raw (approved matrix) | per STAGE-PLAN-BATTERIES | **UNDEFINED** | **UNKNOWN** | block on G6 + the batteries plan's approved matrix |

Missing/duplicate/stale/conflicting inputs appear in the discrepancy register (this table) and **hold gather acceptance** unless explicitly excluded by an authorized decision (plan §2 act 6). G5–G7 and G18 are the named seams; they are named, not assumed.

### 4.3 Next-act inputs (what the gather / the master / the operator's eyes need)
- The resolved source manifest (paths + digests/commits) once G5–G7 are read and reconciled.
- The real commit shas as landing receipts (BA 2cc6f1832f · AA 2ce77ce5ad · CA 6de5aba311) with the phantom-sha mechanism question kept open (SW-1).
- The 8 settle-conditions as the ADAPT's gate rows.
- The spine/face/armor composition inputs (abbreviated):
  - **Spine** — the phase-1 brief (lane-B design), corrected per settle-condition 2 (real R1–R10 revert grid, per-key gate table, judgment-layer fixtures, sole-egress, reversion points).
  - **Face** — the minimal receipt (lane-A), corrected per settle-condition 1 (per-key match, provenance tags, verdict from record, voice-check gate passing).
  - **Armor** — the verification layer (lane-C), corrected per settle-conditions 3/5/6/7 (base-diversity gate real, blind-panel protocol skill-verified, C1–C9 done-whens, pin registry seeded, G2/G3/G4 carried OPEN, shared-route constraint named).
- The open-items ledger: every wall-clause question from the three landings + this AoA — kept/answered/escalated (OP-1 ANSWERED, OP-2 kept, CA#1/2 ANSWERED, CA#3 CORRECTED + mechanism kept, CA#4/5 ESCALATED, CA#6 KEPT, SW-1 KEPT, AOA-OQ KEPT, SW-2 KEPT).
- The record-correction rows (append-only, history never rewritten): BA-D1, BA-S1/S3/S5, BA-S6, AA-S1/S2, CA-D1, CA-S1, CA-S2, SW-1, AOA-OQ.

### 4.4 Emit the package
The gather index and immutable package are assembled **from this table** + the AoA artifact; each item is linked (not paraphrased in place of its evidence). The gather acceptance gate (plan §2 act 6) signs the row above with the enumerated inventory, omissions (G5–G7, G18 = UNKNOWN), repair owners, and gate decision; OPUS composition waits for acceptance or an explicitly bounded, conspicuously-excluded scope.

---

## 5 · SEAL-VOICE / HARD-LINES CHECK (this AoA)
- nothing public · RFC #143379 / #5320 / #157065 QUIET · no installs · writes only under studies/rfc-143379-rig/ · all local paths via read_file, never web_extract · never push · never git checkout -- / rm -rf / stash · commits as kanban-pilot <pilot@rig.local> · armaments applied: think-tank (spine) + agent-work-review; the rest name-and-refused.

*Facimus semper — the verdict renders on the evidence; the evidence is on the record; the record corrects itself out loud. A non-reproduction is a QUESTION, never a defect; a receipt that points at nothing is the failure class, never a silent pass.*

---

## A · AXIS INDEX (for the AoA record, plan §2 act-4 axis names)
| AoA-design axis | Plan/cross-audit axis | Status |
|---|---|---|
| 1 Completeness | COVERAGE | PARTIAL |
| 2 Verifiability | EVIDENCE-REALITY | PARTIAL |
| 3 Honesty | VOICE-CHECK (honesty bar) | HONEST |
| 4 Grounding | BASE-INDEPENDENCE is separate; grounding = EVIDENCE-REALITY/OPEN-ITEMS | SOUND |
| 5 Extendibility | OPEN-ITEMS | SOUND |
| 6 Gate-coherence | HARD-LINES (gate vocabulary) | PARTIAL |
| 7 Seat-compliance | BASE-INDEPENDENCE (seat) | SOUND |
| 8 Wall-clause-handling | VOICE-CHECK (wall clause) | SOUND |
| 9 Convergence | REGURGITATION-DIAL | PARTIAL |
