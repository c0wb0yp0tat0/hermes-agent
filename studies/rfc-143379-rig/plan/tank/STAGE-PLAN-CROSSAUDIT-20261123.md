# STAGE-PLAN-CROSSAUDIT-20261123 — the cross-audit's implementation-plan (the stage's head)

*Planner: PLANNER-1, seat `tencent/hy4-flash:free` (the flagship's slice). This document is the PLAN only — no lane is fired, no probe run, no verdict rendered here. The proxy approves or reloops.*
*Study branch: `study/rfc-143379-rig-20261105` · Date: 2026-11-23 · Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/STAGE-PLAN-CROSSAUDIT-20261123.md`.*
*Hard lines (binding, carried in every lane brief): nothing public · **RFC #143379 quiet · #5320 quiet · #157065 quiet** · NO installs · ALL LOCAL reads via `read_file` (never `web_extract`) · never push · never `git checkout --` / `rm -rf` / stash · master append-only · commit as `kanban-pilot <pilot@rig.local>`, study paths only.*
*Wall clause (binding, verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*

---

## A. The three report lines (the spine / the seats / the converge)

- **SPINE:** The cross-audit's head = three blind lanes (lane-BA audits B's design · lane-AA audits A's form · lane-CA audits C's layer) fired in PARALLEL on three distinct bases/hosts, each landing `SOUND / DEFECTS-NAMED / REJECT` with re-derivable receipts + ≥2 extensions + wall-clause `QUESTION`s at its named path; the AoA — BLOCKED on all three verified landings — applies the nine verify-axes and renders the consolidated stack verdict into the gather; the whole rides the think-tank spine under the agent-work-review discipline.
- **SEATS:** `lane-BA → meituan/longcat-2.5:free @ p0tat0` · `lane-AA → stepfun/step-3.7-flash:free @ c0wb0y` · `lane-CA → tencent/hy4-flash:free (flagship) @ cloud` · `AoA → base-distinct-from-all-three (solar fallback, re-probed) @ cloud→pve1 head verify/fold`; `pve1` = compose host, NO audit rides it.
- **CONVERGE:** Each lane lands at its named path (verdict ∈ {SOUND, DEFECTS-NAMED, REJECT} + command/sha/count/answer/evaluator-row receipts + ≥2 extensions + wall-clause `QUESTION`s, kanban-pilot commit, sha reported); the AoA fires only on 3 verified landings (session-id + result + artifact + branch/tree), on a base distinct from the audits, and renders per-audit nine-axis verdicts + the CONSOLIDATED STACK VERDICT + settle-conditions + the gather's held launch package — no verdict floats, no seam "reconciled away."

---

## B. Armament — employed / named-and-refused

**Employed (the whole armament):**
1. **think-tank — the spine.** Mechanism spine `classify → choose → probe → evaluate → adopt-or-park → standardize → verify`; minimum runnable spine `deconstruct → sense → choose → calibrate → probe → review → record → compose-check`. Its dispatch-envelope, sequenced-fire, base-diversity, emission-contract, landing-gate and failure-class doctrine are the plan's operating law (§F–§H).
2. **agent-work-review — the audit discipline.** Full reads first → extraction → cross-doc consistency matrix → arithmetic re-derivation → identifier cross-check → epistemic scoping → explicit unverifiable list → asserted → status → basis, flat neutral tone. This is the shape every lane's receipts and every AoA axis take (§E).

**Named-and-refused (NOT in armament; do not load, do not run for this plan):** `blind-agent-panels` and `external-readiness-review` are the *subject* of lane-CA's probes (it verifies against their reality), not this planner's armament; `two-model-reasoning`, `supervisor-delegation`, `systematic-debugging`, `plan` (this doc is the study's plan, not a `.hermes/plans/` artifact), `matrix-proposal-skill`, `defect-forensics`, `competitor-news-monitor`, and every other skill are refused. Calibration clause: the skills inform the judgment; the judgment decides — no force-fit.

**The wall clause is the landing test:** a lane that hits a non-reproduction has NOT earned an "unreproducible" verdict until it constructs the minimal experiment that moves the wall (advance the date, shrink the fixture, invert the condition, close the window). A bare "green here / can't reproduce" is a hypothesis and re-arms the lane — it is never a landed finding.

---

## C. The ground read (full reads, per agent-work-review step 1)

**The brief set (read in full):** `plan/tank/briefs/CROSS-AUDIT-BRIEFS.md` — three self-contained briefs, blind-panel pattern: briefs never summarize the sibling's content; the artifact is read cold; the ground is named.

**The three artifacts under test (read in full, cold):**
- lane-B artifact: `plan/tank/lane-b-phase1-design-20261121.md` — the canary phase-1 skeleton (15 items, G1–G8 gates, R1–R10 reverts, sole-egress, three judgment fixtures, six open threads).
- lane-A artifact: `plan/tank/lane-a-minimal-demonstrable-20261121.md` — the minimal demonstrable form (one watcher-visible receipt, I1–I10, G1–G9, six revert points, judgment layer, six open threads).
- lane-C artifact: `plan/tank/lane-c-verification-readiness-20261121.md` — the field-receipt layer (receipt skeleton, base-diversity + blind-panel protocols, C1–C9 readiness conditions with done-whens, one-run-per-pin stewardship, G1–G4 verdict gate, five open threads).

**The grounds each lane re-derives against** are exactly those named in BRIEF 1/2/3 (`CANARY-CELLS-20261120.json` · `OPUS-NM3-CANARY-20261120.md` · `PILOT-VERDICT-20261121.md` · `FINAL-LEG-PLAN-20261121.md` arms 3/6/4 · `LOSS-LADDER-AOA-20261121.md` · `LOSS-LADDER-AUDIT-20261121.md` · `MASTER-HITL-GIST-AOA-20261121.md` · `PILOT-KIT-PLAN-20261121.md` §1+§2 / §9+stage-3). The pins are the brief's scope contract — enumerate them at dispatch, never after a miss. A ground doc over the lane's read-cap is SPLIT at staging time (not post-wall); the lane's honest depth is capped by staging, never by the material.

**Truth surfaces:** the branch's docs + artifacts + receipts (the thread is a record's surface, not the lanes' ground — thread-ban; exception only if a mission's object is the thread).

---

## D. The fleet register — seats, runners, exact designations

The exact designation is the ONLY reference (the sloppy-alias class: a bland "the flagship" lets a misspoken family name pick the wrong model). Every dispatch, brief, row and report carries the full model-id. The three audits ride three distinct bases and three distinct runner hosts, all distinct from the compose's base (`upstage/solar-mini4:free`) and host (`pve1`) — no self-run self-reference for the independence claim.

| Role | Exact designation (pin at dispatch) | Runner host | Anchor / rationale |
|---|---|---|---|
| lane-BA auditor | `meituan/longcat-2.5:free` (NO `-preview` suffix) | `p0tat0` | longcat was B's documented non-author verifier pair (with solar-mini4); continuity of the independent eye, now on a base distinct from the compose's. |
| lane-AA auditor | `stepfun/step-3.7-flash:free` | `c0wb0y` | Distinct base + host. **Fair-share drain class:** re-probe the live token before pinning; if its window is drained, pivot to a re-probed live base keeping the lane's role (designation is the lens, channel truth is told), and ledger the pivot in the receipt. |
| lane-CA auditor | `tencent/hy4-flash:free` (the flagship) | `cloud` | The deepest/meta layer (verification-readiness protocol audit against skill reality) rides the flagship tier. `cloud` gives a host distinct from `pve1`. |
| AoA (downstream slice, not fired here) | base DISTINCT from all three audit bases; `upstage/solar-mini4:free` fallback if re-probed live | `cloud` → head verify/fold on `pve1` | Adjacent layers never share a base; heaviest adjudication rides the flagship tier on its own slice. The AoA is BLOCKED until all three landings verify. |
| head (this planner / gate / verify / fold) | session's own driver | `pve1` (homebase) | Head-side owns the two uses only: its own moves (look, research, steer's shaping) and the stalled-channel stop-loss landing. The head does NOT self-edit a produced artifact (producer's base never judges its own product). |

**Base-diversity gate (runnable):** the family is BASE-DIVERSE iff it holds ≥2 distinct pinned bases and the family's claim is not "same-base." Here: three audits on three distinct bases × three distinct hosts; the AoA on a fourth distinct base. "Same-base" verdicts are reports about one machine, not claims about the kit — they do not converge.

**One-run-per-pin:** each pin is exercised exactly once per study lifecycle; the single run IS the receipt. The dispatcher is the pin registry's sole writer; a second run of a pin needs an OUTSIDER's re-derivation of the first receipt as its gate, not the runner's say-so. The pin registry rows owner + budget + receipt sha at each landing.

---

## E. Per-lane execution-shape (the three lanes, one sub-shape each)

Every lane is a self-contained act: it reads its artifact cold, reads its ground in full, re-derives every claim, extends ≥2 open threads, writes its deliverable at the named path, commits it as kanban-pilot, and reports the sha + verdict. Each lane's shape below fixes: scope · probes · receipt form · seat · sequencing · time-box · failure handling · converge form.

### E1 — lane-BA · audit B's design

- **Brief-defined scope:** the artifact = `lane-b-phase1-design-20261121.md` (the canary's phase-1 skeleton). Ground = cells JSON + `OPUS-NM3-CANARY` + `PILOT-VERDICT` + `FINAL-LEG-PLAN` arms 3+6. Mission: the skeleton must be **runnable, measured, revertible, egress-disciplined, judgment-layer-equipped**; gates derivable from the cells' ledger; items named; revert points real. Deliverable = `plan/tank/lane-ba-audit-20261121.md`.
- **The audit's probes (agent-work-review discipline):** (1) full reads of artifact + all four grounds; (2) consistency matrix — trace every gate/number (pin `fc8b9934…`, sha `5747a90e…`, bytes `641,262,336`, load `0.95s`, params `319,028,736`, logits `[1,4,129280]`, argmax `49969`, egress `647,716,330`/secondary `0`) across artifact and cells; (3) arithmetic re-derivation — re-sum the gate table and check each verdict against B's OWN stated rules (F1 vocabulary LANDED/PARTIAL/GAP/QUESTION/REVERTED/CLOSED; fail→freeze at PARTIAL/GAP, never a silent skip); (4) identifier cross-check — sha/pin bytes must agree across artifact, cells, verdict; (5) epistemic scoping — "FIRED vs RUNNING vs OPEN" states must not overclaim (a cell assertion is a receipt, not a run measurement — the isolation-boundary seam, B's open thread 2); (6) egress sole-route + revert-point reality (R1–R10); (7) wall clause — any non-reproduction of a gate number becomes a `QUESTION` with the minimal experiment, not a stop; (8) EXTEND ≥2 of B's six open threads with new continuation points.
- **Receipt form:** verdict ∈ {SOUND, DEFECTS-NAMED, REJECT} + receipts (command + measured count + source sha + quoted answer + independent evaluator row) + the asserted→status→basis table + ≥2 extensions + explicit unverifiable list (what only `pve1`'s on-disk cells can confirm).
- **Seat:** `meituan/longcat-2.5:free` @ `p0tat0` (§D).
- **Sequencing:** PARALLEL member of the fan — independent artifact, no dependency on AA/CA. Its landing does not gate AA/CA, but all three landings gate the AoA.
- **Time-box:** one ring, 40–60 min. If it cannot land in the ring, it re-arms at the next ring with the partial frozen at PARTIAL/GAP — never a silent skip, never a re-run with different values.
- **Failure handling:** channel-dark → pivot per §F4; emission parse-fragment → not landed (§F3); ground over read-cap → staged split; a failed check is filed AS the finding (named mechanism + fix + re-verification), never a bare "failed"; number seam → hunt the raw cell/receipt before calling unverifiable.
- **Converge form:** named-path file + kanban-pilot commit sha + verdict line + receipts + extensions + wall-clause `QUESTION`s → the AoA's nine axes (coverage, verdict-consistency, evidence-reality, base-independence, voice-check, hard-lines, open-items, emission, regurgitation-dial).

### E2 — lane-AA · audit A's form

- **Brief-defined scope:** artifact = `lane-a-minimal-demonstrable-20261121.md` (the minimal demonstrable form). Ground = cells JSON + `PILOT-VERDICT` + `LOSS-LADDER-AOA` + `PILOT-KIT-PLAN` §1+§2. Mission: the one outside-watcher-visible receipt must be **complete, honest (no invented fields), re-derivable by an outsider, and revertible**; gate artifacts must exist or be nameable; the item list must cover the pilot's promise. Deliverable = `plan/tank/lane-aa-audit-20261121.md`.
- **The audit's probes:** (1) full reads; (2) consistency matrix over §2's five-field receipt (sandbox env id, model sha vs pin, load/determinism, license attestation, LFS egress), I1–I10 and G1–G9; (3) arithmetic re-derivation of G1–G9 bars (`max_abs_diff 0.0 < 1e-6`, byte counts, 8/8 compose marks — mark 2 "via proxy" must be named as proxy, not silently treated as direct); (4) **honesty/invented-field sweep** (agent-work-review epistemic scoping + intent check) — every receipt field maps to a cell or a named artifact; a field that cannot be re-derived is a receipt failure, not a story; (5) identifier cross-check — receipt sha vs pin; (6) reversibility of the six revert points; (7) voice-check — no reserve-name whisper, no private detail on any watcher-facing path; (8) wall clause on the loss-ladder meter (G9 byte-verified, not prose) — non-reproduction becomes a `QUESTION` with the minimal depth-cut experiment (0.65 / 0.5 cuts); (9) EXTEND ≥2 of A's six open threads.
- **Receipt form:** as E1 — verdict + receipts + asserted→status→basis table + ≥2 extensions + unverifiable list (on-disk run log / cells only verifiable on `pve1`).
- **Seat:** `stepfun/step-3.7-flash:free` @ `c0wb0y` (re-probe; pivot ledgered if drained — §D).
- **Sequencing / time-box / failure handling:** PARALLEL fan member; one ring 40–60 min; §F failure classes as E1.
- **Converge form:** named-path file + sha + verdict + receipts + extensions + `QUESTION`s into the AoA's nine axes.

### E3 — lane-CA · audit C's layer

- **Brief-defined scope:** artifact = `lane-c-verification-readiness-20261121.md`. Ground = `PILOT-KIT-PLAN` §9+stage-3 · `FINAL-LEG-PLAN` arm 4 · `LOSS-LADDER-AUDIT` · `MASTER-HITL-GIST-AOA`. Mission: the layer's guarantees must be **executable** — the base-diversity gate real (≥2 distinct bases), the blind-panel protocol complete (blindness in the briefs, real-work missions, mediator reconciliation), each of the nine external-readiness conditions with a checkable done-when, one-run-per-pin enforceable. Verify against ground + the skills' reality (`blind-agent-panels`, `external-readiness-review` — as SUBJECT, not armament), then EXTEND ≥2 open threads. Deliverable = `plan/tank/lane-ca-audit-20261121.md`.
- **The audit's probes:** (1) full reads; (2) consistency matrix over the receipt skeleton (command/count/sha/answer/evaluator-row), the two protocols (§2 base diversity, §3 blind panel), C1–C9 done-whens, §5 stewardship, G1–G4 verdict gate; (3) arithmetic re-derivation of the done-whens (e.g. `sha256sum -c SHA256SUMS` exit 0; κ raw ≥80% AND κ ≥0.70; the family ≥2 distinct bases; no pin twice-run without re-derivation); (4) identifier cross-check — the M4 shared-pin constraint must be named, never a silent pass; (5) **protocol reality check against the two skills** — is blindness actually in the brief (artifact path + questions, never content)? are missions real-work? is reconciliation weighted-convergence / divergence-as-signal (never majority-"reconciled away")? are C1–C9 done-whens checkable states, never "reviewed"/"done"? (6) epistemic scoping — the layer must not pre-judge GO/ADAPT/PARK, only arm it; (7) wall clause on any unexercised protocol seam → `QUESTION` with the minimal experiment; (8) EXTEND ≥2 of C's five open threads (O1–O5).
- **Receipt form:** as E1/E2 — verdict + receipts + asserted→status→basis + ≥2 extensions + unverifiable list.
- **Seat:** `tencent/hy4-flash:free` (flagship) @ `cloud` — the deepest protocol/meta audit rides the flagship tier on a host distinct from the compose's (§D).
- **Sequencing / time-box / failure handling:** PARALLEL fan member; one ring 40–60 min; §F failure classes as E1.
- **Converge form:** named-path file + sha + verdict + receipts + extensions + `QUESTION`s into the AoA's nine axes.

---

## F. Sequencing — the named acts, each with its receipt

The three audits are a PARALLEL fan (independent artifacts, no cross-dependency). The successor lenses are STAGED and SIT BLOCKED: the AoA reads the landings, not air. Sequence is "end to end to end"; the excitement of a firing is the cue to RE-CHECK sequencing, never to skip it.

| # | Named act | Gate / hold condition | Receipt |
|---|---|---|---|
| 1 | **GROUND-STAGE** | All briefs + artifacts + grounds read in full; any ground over read-cap split at staging; pins enumerated at dispatch. | The staged file list + the split manifest. |
| 2 | **BASE-PROBE** (standing gate before every dispatch) | Positive-token probe of each exact pin (grep the expected reply token, never the absence of failure strings); config default's liveness checked; per-lane base pinned explicitly. | Probe output + the pin registry row. |
| 3 | **LAUNCH-CHECK** (four-step challenge-do-verify, each answer carries its VALUE) | (a) backgrounded? → "background=true, notify, persist" (b) full 40-char pin quoted? → the hash spoken (c) artifact path absolute + unique? → the path spoken (d) brief carries armament + landing-verb? → first block's name. | The four answered values; a launch whose four carry their values is the only launch. |
| 4 | **FAN-FIRE** (parallel) | lane-BA, lane-AA, lane-CA dispatched on three distinct bases × three distinct hosts; no two children share an id; each brief blind (path + questions, never content). | Three dispatch records with exact designations. |
| 5 | **EACH LANDING-GATE** (five checks, value-carrying) | (1) sentinel exists (2) the run itself wrote the artifact (mtime moved) (3) verdict + receipts + extensions inside (4) commit on branch (`git ls-tree HEAD` shows the file) (5) sha reported. Board status is a MIRROR, never evidence — verify by session-id + result + artifact. | Per-lane landing row: path + sha + verdict + evaluator row. |
| 6 | **AoA-HOLD** | AoA card created BLOCKED until all three landing-gates pass; if a jump still happens, sharpen the hold-condition onto the running card immediately. | The blocked card + the three landing rows. |
| 7 | **AoA-FIRE** | On all three verified landings: AoA audits the AUDITS cold on a base distinct from all three, applies the nine verify-axes, renders the CONSOLIDATED STACK VERDICT + settle-conditions + the gather's held launch package. | The AoA deliverable + the shared-route constraint named (never a silent pass). |
| 8 | **FOLD / ROW** | Single-writer fold (only the designated parent updates a shared index); worker artifacts are distinct, never shared; compose-check via the disk artifact, not self-report. | The fold row + the state vocabulary per mechanism: FIRED / DORMANT / MIS-FIRED / CORRECTLY-ABSENT with observable evidence. |
| 9 | **ACES-TRIGGER** | At the 6-hour mark with no check-in: improve/audit/review loop fires over the landings themselves (the loop improving the loop); stops on a measured plateau (no-change twice), termination receipted twice over. | The trigger row + the termination receipt. |

**Runners' legs:** `p0tat0` (BA), `c0wb0y` (AA), `cloud` (CA and the AoA's first leg), `pve1` (head verify/fold; no audit rides it). Every fork and the verification-batteries' matrices are available as independent legs, but a fork's leg carries its own pin and its own landing row — a matrix run is a battery, not a demo (every gate measured, named, recorded raw).

---

## G. Time-boxes and cadence

- **Per audit lane:** one ring, **40–60 min**. A lane that cannot land in its ring re-arms at the next ring with its partial frozen at PARTIAL/GAP — never a silent skip, never a re-run with different values.
- **The fan:** one ring window (≤60 min) for all three parallel landings.
- **Re-grounding crons:** every 2h; **cadence cron:** hourly; **ACES trigger:** 6-hour mark.
- **AoA:** next ring after all three landings verify (dependent-leg law — a confirmation leg never precedes the artifact it confirms).
- **No mid-run config changes.** An agreed suggestion or an "enrich the other lane" ask does NOT steer a running leg — it lands in the next pass / next leg's brief, never as a comment on a live card.

---

## H. Failure-class handling (named → refused/handled)

| Failure class | Handling |
|---|---|
| **Channel dark** (designated base fails across separate windows) | Bounded probe-watch over a window → pivot the same brief to a base that runs, keeping the designation's ROLE and telling the channel truth; check the pool's free-status rotation; never keep waiting on a dark base. |
| **Emission contract** (exit 0 with parse-fragment only, no artifact) | Not a landing. Judge by artifact existence + verdict words, never exit code. Re-dispatch carries "respond in PROSE ONLY — your final response IS the verdict — write the file first, then report the sha" as the corrective. |
| **Board phantom** (done/running with empty session-id/result/artifact) | Phantom advancement; re-truth the card from session-id + result + artifact at the fold; never claim "landed" on a column. |
| **Staged read-cap** (ground over lane read-cap returns only its head) | Split the ground at STAGING, never post-wall; the lane's honest wall is a staging defect's symptom. |
| **Base collision / shared route** | ≥2 distinct bases; AoA distinct from audits; a shared base is NAMED as a constraint on the record, never a silent pass. |
| **Wall hit without construction** | Not a verdict — a `QUESTION` with the minimal experiment (advance date, shrink fixture, invert condition, close window); re-arm the lane. |
| **Number seam** (disagreeing records for the same run) | Hunt the RAW receipt (cells, fold, judge command) and reconcile from it; "unverifiable" stands only after the raw receipt was actually hunted. xfailed ≠ xpassed; duration matches to the digit. |
| **Retry-loop mask** (`[CALL ERROR …]` returned as a string; blank/near-empty output) | Retry on `v.startswith("[CALL ERROR")`, reject `len(v.strip()) < 50`; gate the artifact write on both. Iterate LANES, never index by base count. |
| **Re-dispatch collision** (two writers on one live worktree) | Check processes before any re-dispatch; if the original lives, the steer lands in the brief for the NEXT dispatch. A shape-change supersession kills the old writer (verify zero matching processes) before the replacement spawns. |
| **Two-location steer** (direct-execution runner reads the brief, not the card) | Steer lands in BOTH the card comment (record) and the brief append (runner's contract), then re-dispatch with the updated brief. |
| **Rushed brief** | A thin brief under hurry/mood is a DEFECT; its landings are voided and redone at full standard. The full ground — verbatim receipts, exact paths, receipt shapes, LP envelope, wall clause — is the ONLY brief. |
| **Over-flag / wrong surface** (naive pattern on the wrong bytes; credit by search-hit rather than authorship) | Read the ACTUAL bytes and re-derive; trace authorship before crediting; adjudicate mechanism claims by the real control flow, not the audit's arithmetic. |
| **Failed check** | Report the failure AS the finding — named mechanism, fix, re-verification — never a bare "failed" or a re-dispatch cascade. |
| **Public-gate breach** (internal steer vocabulary on a public surface) | Hard-line violation; the substance is held for regroup, the ungated surface corrected; `#143379` / `#5320` / `#157065` stay QUIET. |

---

## I. Converge-contract — each verdict's form into the AoA

Each audit lands its verdict at its named path with: (a) headline verdict ∈ {SOUND, DEFECTS-NAMED, REJECT}; (b) receipts in the uniform shape — envelope-head `id/kind/from/to/status` with handles (SHAs, paths, commit sha), then the five sections Executive Summary / Analysis Brief / Recommendation-Action Plan / Next Steps / Artifact — with every number asserted→status→basis; (c) the receipt skeleton (command + measured count + source sha + quoted answer + evaluator's independent verdict row FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND / GUESSED-WRONG + evidence paths); (d) ≥2 extensions; (e) wall-clause `QUESTION`s, each with its minimal experiment; (f) explicit unverifiable list (what only the owning host can verify — the file wins); (g) kanban-pilot commit + sha reported.

The AoA consumes these by the nine verify-axes (COVERAGE · VERDICT-CONSISTENCY · EVIDENCE-REALITY · BASE-INDEPENDENCE · VOICE-CHECK · HARD-LINES · OPEN-ITEMS · EMISSION · REGURGITATION-DIAL), re-deriving never trusting, then renders: per-audit verdicts with receipts · the extension list · the shared-route constraint named · the **CONSOLIDATED STACK VERDICT** (the fan's combined meaning for the pending decision, with settle-conditions) · and what the GATHER must hold (the launch package: the spine brief, the minimal face, the verification armor). Convergence weighted; divergence is signal, never averaged; two FOUND-PARTIALs on one claim are a named seam, and the landing stays un-composed until the seam is closed or explicitly carried as a named seam. No verdict floats; no seam is "reconciled away."

**Seams that re-enter the plan loop:** any NEW finding surfaced at any stage does NOT ride along as an inline patch — it re-enters plan → head decision → leg audit rotation → cold-read adjudication → amend, then re-execute. Executors never self-amend on new findings.

---

## J. Emission contract for THIS deliverable

The plan is on disk FIRST (this file at the named path), committed as `kanban-pilot <pilot@rig.local>` on study paths only, never pushed, master append-only, local config left as found. Only AFTER the commit lands does the report give the sha plus the three one-line report lines (§A). Exit 0 = deliverable on disk then sha. No execution — the PLAN only; the proxy approves or reloops.

---

*Facimus semper — the plan renders on the evidence; the evidence is on the record; the record corrects itself out loud. Nothing public; RFC #143379 / #5320 / #157065 quiet; reads only; the operator's word gates the public surfaces.*
