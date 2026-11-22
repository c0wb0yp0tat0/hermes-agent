# LANE-C VERIFICATION-READINESS — the pilot kit's field-receipt layer

*For the verify layer of the RFC #143379 pilot-kit decision (GO / ADAPT / PARK,
settle-conditions via the stack). Lane C runs the independent angle on what the
verification must look like when a field receives a receipt that must survive a
re-derivation by an outsider.*

**Author:** kanban-pilot <pilot@rig.local>
**Date:** 2026-11-21 (iteration 1 — the layer's first record)
**Purpose:** to pin the concrete shape of the verification layer for the pilot
kit: the receipt skeleton a field must be able to hand over, the two protocols
that make verification independent (base diversity; blind panels), the nine
external-readiness conditions with executable done-when states, and the
stewardship that keeps the free seats honest (one-run-per-pin).
**Method (source docs read in full):** PILOT-KIT-PLAN-20261121.md §9 + stage 3;
FINAL-LEG-PLAN-20261121.md ARM 4; LOSS-LADDER-AUDIT-20261121.md; LOSS-LADDER-AOA-
20261121.md; MASTER-HITL-GIST-AOA-20261121.md; the blind-agent-panels skill; the
external-readiness-review skill. Live ground: the study's fold §7-u–§7-x
(2026-11-21).
**Grounding legend:** every claim is DOC-GROUNDED (file + section cited) unless
marked ONLINE-GROUNDED or UNVERIFIABLE. This pass read no external pages; nothing
online is claimed.

---

## 1 · THE RECEIPT SKELETON — what a field-demonstrable receipt must look like

**The principle, the fold's own words:** "the field receives receipts, never
stories; each receipt must survive a re-derivation by an outsider." A receipt is
a structure, not a narration — a command + measured count + source sha + answer +
the evaluator's independent verdict row. The pilot kit's start line (§7-m,
2026-11-21) was rendered that way: PROOF-OF-CONCEPT — CONFIRMED, the boundary
named as one class (the judgment layer), measured chain carried: the read-restore
suite 42/42 GREEN (the THE-NORTH external gate) · R2's write-deadline
superseded by verification (the read-gate + the byte-budget breaker exist) ·
W2's workflow-presence separation measured at 31/35 · the census's 3
under-specified specified with exact settle-words · kit-audit + kit-sceptic
verified present by exact name (ab471fc80c).

**The template a landing must fill** (the ask-verification spine — receipt-shaped
asks, re-derivable):

| Field | What it carries | Done-when |
|---|---|---|
| The command | The exact invocation that produced the result, verbatim, in the fixture's native form (the cells' ledger named the driver/brief/gate for each arm) | the string is in the record and is the only command the re-deriver needs |
| The measured count | The gate bars raw — no smoothing, no "covered" smearing — e.g. the pre-reg's bars (B0, B1 ≥ 20pp; B1 ≥ 0.85C) with B0/B1/C logged | the row carries the numbers, raw, with the verdict per the dry-run ruler |
| The source sha | the artifact's sha256 + the model/pin sha (the canary's field-2: model sha 415501bd… == the staged pin, live-HF + byte-identical shard reassembly) | the sha is pinned at the top of the receipt; it is the receipt's identity |
| The answer | the verdict line, quoted, a gate state (revisable by evidence — not a recommendation) | the verdict is quoted in full, untouched by the folding pass |
| The evaluator's independent verdict row | the blind panel's row (§3) — the independent eye on the landing | the row names the panel's verdicts (FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND / GUESSED-WRONG) + evidence paths |

Rules the template obeys:

- **Receipts, never stories.** Every number traces to a fold line / ledger row /
  sha (AoA A4). A number that cannot be re-derived from the cited row is a
  receipt failure — the AoA's A4 settle-condition, and the loss-ladder audit's
  wall clause governs: *"a non-reproduction is a QUESTION, not a stop — simplify
  the experiment until the seam is exercised."*
- **Two-way door.** Every receipt names its reversibility and its rollback (the
  pilot's start line is a gate state; the weights rung's zero-weights case is
  the byte rollback; the B0 arm is the control arm).
- **No self-run self-reference for the independence claim.** The pilot's
  execution-layer receipts are the machinery's own receipts (F2 re-verification,
  the fill's measured chain, the harbor's lib class — §7-m), and the independent
  eye is the blind panel (§3). The verification vocabulary is pre-committed at
  the canary's design time (the measured gates, the revert points, the sole-
  egress discipline, the verdict vocabulary COVERED / PARTIALLY-COVERED / GAP /
  UNKNOWN, the out-of-band evaluator's schedule, the no-gate doctrine).

---

## 2 · THE PROTOCOL: BASE DIVERSITY — the audits never share the compose's base

**What failed on 2026-11-21.** The audit/AoA route shared ONE pinned base
(upstage/solar-mini4:free) — the flip-flop rule was named, not honored. The AoA
itself recorded it as a named constraint (M4): the delegation route shared the
pin, so the audit-of-the-audit could not claim a different compute/actor than
the study leg, and the spawn path was broken for an independent second leg. That
is a named constraint of the record, not a hidden defect — and the standing mark
of the verification layer is the opposite: **base diversity, never a named
single base**.

**The rule.** Every verification run in the pilot kit's family must be pinned to
a base that differs from the compose's base (upstage/solar-mini4:free is the
compose's base, the one the kit's claim leans on). The repair is one
configuration line on the delegation route: per-unit base pinning — the
delegation's routing decision names the runner + the heap, and the audits never
share the compose's base by construction. The AoA's M4 lesson is the contract:
base independence is a property the run's shape must carry, and a named
constraint of the run that cannot be hidden.

**The standing verification mark (the stage-3 mandate).** Stage 3 of the pilot
kit stages the independence layer precisely:
- per-unit base pinning on the delegation route (or the board-spawn path's
  repair);
- the blind-panel protocol for the pilot's landings (FINAL-LEG-PLAN ARM 4);
- the audit's base-diversity as a standing verification mark — never a
  named-constraint again.

**The mark, stated as a runnable gate.** A verification milestone is
BASE-DIVERSE iff its family contains at least two distinct pinned bases, and the
family's claim is not "same-base." The default family for a pilot-kit landing is:
(1) the execution receipt (the machinery's own run), (2) the audit receipt (a
different base than the compose), (3) the blind panel (a third base, different
runner). At least two of the three must be pinned to distinct runner/heap
identities as recorded in the run's own config row.

**Locked speech.** "Same-base" verifications are reports about a single machine;
they are not verification claims about the kit. A claim about the kit needs a
family of distinct bases, with the composition of the family named in the
receipt.

---

## 3 · THE PROTOCOL: THE BLIND PANEL FOR THE PILOT'S LANDINGS

**The protocol** (blind-agent-panels skill, applied to the pilot's landings):

1. **When.** Every pilot-kit landing that carries a numeric claim — the canary's
   receipt, the weights-rung fire, GAP-3's 300+ gate battery, GAP-4's
   release-condition battery — gets a blind panel before the landing is composed
   into a verdict.
2. **Who.** Two to three blind subagents, dispatched in parallel from the free
   pool — the pool is FIXED and known (upstage/solar-pro4:free,
   poolside/laguna-s-2.1:free, poolside/laguna-xs-2.1:free, plus the host
   default); each child is a different ID, and no two children of one dispatch
   share an ID. The pool is re-inventoried once per shift, not per dispatch.
3. **The blindness.** The brief names the artifact path + the questions; it does
   NOT describe the artifact's content — a blind brief leaks the shape of the
   answer (the skill's non-negotiable). Each worker reads the rig's chain files
   with read_file FIRST (the chain lives on pve-1, on the rig's local disk; it
   is not cloud-reachable), then carries its own research (discovery →
   harness page reading → retry-once-then-fallback → stop at CAPTCHA/2FA). No
   separate supervisor-side research lane: the fold online research rides in
   each worker's brief.
4. **The deliverable.** Each worker writes a distinct per-worker file AND returns
   the markdown: the verdicts FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND /
   GUESSED-WRONG per claim, with tool-call counts + evidence paths. The parent
   (this lane) re-reads every written deliverable and re-derives the load-
   bearing numbers from the artifact on disk before the landing is composed.
   A worker that returns `{}` while its artifact is written is a landing
   failure, not a missing artifact — the empty summary is a self-report miss.

**Reconciliation (the mediator's job).** Convergences weighted; divergences
treated as signal, never averaged. The panel's output is not a vote: a
FOUND-PARTIAL on the same claim from two panels is a named seam, and the
landing stays un-composed until the seam is closed or explicitly carried as a
named seam in the kit's verdict. Nothing is "reconciled away" by a majority.

---

## 4 · THE NINE EXTERNAL-READINESS CONDITIONS — with done-when states

Each condition ends with a CHECKLIST table (Action | Artifact | Done-when). A
done-when is a checkable state, never "reviewed" / "done".

**C1 — Replication kit.** The full file list, directory layout, the hashing
(SHA-256 + pinned seal convention), the archive format (zip + SHA256SUMS), the
license split (CC-BY-4.0 content / MIT code), and a README outline with the
claim-to-file map. **Done-when:** `sha256sum -c SHA256SUMS` exits 0; every
number in the receipt maps to a file path in the kit README.

**C2 — Grader pin.** The fill-in template per the 2026 AI-agent prereg standard:
model IDs/checkpoints, sampling params, seeds, retry limits, API version/date,
open-weight hashes, verbatim prompts, exclusion rules, pilot history. The pin
JSON is the sole input to the reproduction script; a re-run from the kit
reproduces the numbers. **Done-when:** the pin file alone, plus the kernel,
reproduces the receipt's measured count.

**C3 — Human anchor.** 15–20 cells + 3–5 controls (controls create score spread,
without which kappa is undefined), SME raters, rubric-only blinding, raw
agreement + Cohen's kappa, pre-committed pass bar (raw ≥80% AND κ ≥0.70, Landis-
Koch "substantial"). The pilot kit's anchor is the operator's read (the fold
§7-u receipt-form: the evaluator's independent verdict row). **Done-when:** the
anchor's session log shows the controls' scores spread (kappa defined), and the
pass bar is met or the NULL-with-named-seam clause is quoted.

**C4 — Statistics.** Min-detectable-damage for the rubric gate, CIs for the
headline fidelity claims, the grader-variance estimate, the clustering caveat
(cells nested in behaviors/graders → effective n between clusters and cells).
**Done-when:** the stats appendix states the MDDL, the CI (Wilson closed form),
the grader-variance estimate, and the effective-n correction; no claim of "no
cell failed the gate" without the per-cell failure bound (1−(1−p)^n power
curve).

**C5 — Related work.** Draft actual paragraphs positioning the finding against
the literature; tone discipline: "negative result for X", never "falsified".
**Done-when:** the related-work section names 3+ cited lines with DOIs/URLs and
no overclaim.

**C6 — Timestamped prereg.** OSF (recommended), Zenodo DOI, arXiv (not a
registry). The internal freeze is sealed by the receipt chain (the sha-pinned
checkouts); completed waves are labeled post-hoc registration with the seal
date — a wave is never re-labeled as "registered before data." **Done-when:**
the prereg record carries a timestamped registration link + the internal freeze
seal (git sha range + the receipt chain).

**C7 — Compute/cost.** NeurIPS-checklist-style disclosure (worker type, memory,
time per run + total, compute beyond the reported experiments); unrecoverable
values UNVERIFIABLE with a stated estimation method. **Done-when:** the cost
rows carry worker + memory + time per run + total; the zero-billed stub carries
cost_total=0.0; every unrecoverable value is marked UNVERIFIABLE with an
estimation method.

**C8 — Scoped claims.** Exact replacement sentences for every overstatement,
keeping the experiment's scope variables explicit (doctrine, stack, transform
family, rubric, n). **Done-when:** the scoped-claims table lists each
overstatement with its replacement; the replaced sentences retain the scope
variables.

**C9 — Licensing.** The external corpus's actual status checked (official page,
footer copyright, declared license), fair-use factor analysis, options ranked
by risk (fetch-and-verify < include-with-notice < permission request; paraphrase
breaks byte-level replication). **Done-when:** the license check is recorded in
the kit's README (the corpus page URL, the declared license, the fair-use
factor analysis); the option chosen is the lowest-risk one that preserves
byte-level replication.

---

## 5 · STEWARDSHIP: ONE-RUN-PER-PIN ON THE FREE SEATS

**The standing rule.** Each pin is exercised exactly once per study lifecycle —
no repeat runs of the same pin, no "re-runs for sanity." One-run-per-pin means
the single run IS the receipt. The free fleet does most of the work; the free-
tier rotation is the mainline:

- **Nemo** — the local powerhouse, unmetered, no fair-share cap; the heavy
  volume rides here.
- **Support seats** — carry the mechanical and the volume.
- **Free-tier rotation as mainline** — flagships fire first in their windows;
  the support seats ride the endurance engine.
- **Nemo / Luna / DeepSeek** ride in the mission as the local, middle, and
  orchestration layers — part of the work, never its substitute.

**The pin registry.** Every pin (model pin, seed pin, config pin) is registered
with its owner, its budget, and the receipt sha of its single run. The
dispatcher stands as the pin registry's only writer.

**The two-way door on the pin.** No pin is retired by the actor that created it;
the pin's receipt is the gate to the next stage. A second run of the same pin
is allowed only after the pin's first receipt is re-derived by an outsider —
the re-derivation is the gate, not the runner.

**The substrate inheritance.** The pilot kit's canary runs on the kit's own
machinery (the substrate/ layers committed to the study), never on "vanilla"
Hermes: the transport/wrapper carries the write-window read-gate + byte-budget
breaker, the probes carry the seat batteries, dispatch carries the ACES +
Kaizen + wave families. The kit's contention is with the machinery, not the
model.

**The stewardship report.** Each landing rows its pin registry entry with the
receipt sha; the stepper's cycle clock (the watch + the sweeps) re-probes the
pin's status at every ring. Nothing is retired without a receipt and a named
seam.

---

## 6 · THE LAYER'S OWN VERDICT GATE — the pilot-kit decision inputs

The verification layer earns its keep by arming the GO / ADAPT / PARK decision
with receipts, not by pre-judging the decision. Its own gate (the layer's
first record, 2026-11-21):

| Gate | State | What it would take to pass |
|---|---|---|
| G1 — the canary's start line receipted | PASS | read-restore 42/42 GREEN, R2's write-deadline superseded by verification, W2's 31/35 measured, the census's 3 under-specified specified with exact settle-words (§7-m) |
| G2 — verification independence | OPEN | the audit family's bases are distinct (base-diversity mark, §2) + the blind panel landed on the landings (§3) |
| G3 — the external-readiness conditions checked | OPEN | C1..C9 each with its done-when (§4) |
| G4 — one-run-per-pin stewardship held | OPEN | the pin registry complete, no pin twice-run without re-derivation (§5) |

The verdict gate is the three-way, two-way-door style: **READY** / **READY-
WITH-NAMED-SEAMS** / **NOT-READY**, the named seams carried explicitly, never
smoothed. The layer is a gate state, revisable by evidence — the pilot fires as
a bounded canary behind the start line, RFC quiet, nothing public beyond the
thread. The operator's word gates the public surfaces; the layer's own gate
stands on the record as soon as G2/G3/G4 land.

---

## 7 · OPEN THREADS / CONTINUATION POINTS

1. **O1 — the blind panel's footprint on the free seats.** How many blind
   subagents (2–3 per landing) can the free fleet sustain per landing before the
   one-run-per-pin ceiling bites? Named seam: the free-tier rotation as
   mainline, with Nemo's unmetered capacity as the only spare — but Nemo is a
   different model, so the panel's model diversity is capped by the pool's
   fixed set. The seam is the dispatch cadence + the pin registry's expiry.
2. **O2 — the human anchor (C3) vs. the kit's rule.** The kit says SEMs + rubric-
   only blinding; the pilot kit has no SEMS — the anchor is the operator's read
   (the fold §7-u receipt-form). The seam: who is the anchor, and how is κ
   defined when the only control is the operator's own read and the controls
   must create score spread without becoming another named opinion?
3. **O3 — the prereg timestamp (C6) for the first field pin.** The pilot kit's
   gates are the pre-committed bars; the internal freeze is sealed by the
   receipt chain; the public registration is a timestamped record + forward
   commitment. The seam: the weights-rung fire (ARM 0) is the first pin whose
   registration must precede the field data — the prereg record has to carry
   its date before the run.
4. **O4 — the statistics (C4) at canary scale.** The canary's sample is n=5 at
   the dry-run class; the min-detectable-damage for the rubric gate at that n
   is large, and the canary's verdict vocabulary (COVERED / PARTIALLY-COVERED /
   GAP / UNKNOWN) must report "no cell failed the gate" without claiming
   sub-threshold bounds. The seam is the stats appendix's MDDL line + the
   per-cell failure bound, baked into the canary's receipt template.
5. **O5 — the audit's base-diversity at scale.** The AoA's M4 named the shared
   pin as a constraint, not a defect; the standing mark is base diversity. The
   seam: the board-spawn path's repair is one configuration line, but the
   delegation route's per-unit pinning needs a second line; the verification
   layer must carry the shape of both lines in the kit's method cards before
   the pilot's first landing.

---

*FACIMUS SEMPER. The receipt is a structure; the structure is the record; the
record corrects itself out loud. Nothing public; RFC quiet; reads only; the
operator's word gates the public surfaces.*

*— kanban-pilot <pilot@rig.local>, 2026-11-21, iteration 1*
