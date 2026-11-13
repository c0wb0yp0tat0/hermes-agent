# KIT-SKEPTIC-20261107 — the counter-pass: the as-is assembly's failures, the candidates' weakest grounds, the readiness gaps the draft missed

**Seat:** `meituan/longcat-2.5:free` (copycat lane — THE KIT'S SKEPTIC). **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Register:** receipts, never claims — every line below traces to a file on this branch or a commit in its log; the draftsman's framing is never reused; the counter's own reads are the ground. **Gate:** nothing public without the user's word. **Date:** 2026-11-07.

> **One-line finding:** A pilot kit assembled as-is from the study's current parts would fail at the harness write-deadline (named, unbuilt, split), the eval's pending state (W2 SEPARATION-UNMEASURED), the 40-marker NOT-RUN census (3 UNDER-SPECIFIED), the fabric's dispatched-not-concluded runs (30 `queued`, 1 `in_progress`, no conclusions column), and the machinery-vs-science ratio (one measured negative + one unmeasured separation vs a self-referential loop) — and the innovation-candidates' evidence is thinnest exactly where the kit's breadth measure (same-account forks), its termination proof (a self-audited zero), and its reservation theorem (one case, unbuilt retrieval check) are claimed.

---

## (a) THE AS-IS ASSEMBLY'S FAILURES — what a pilot kit built from the study's current parts WOULD fail at

Each failure is a non-negotiable: the kit cannot carry it into a pilot. Each has its receipt. Nothing is softened.

### (a1) The harness write-deadline — named, unbuilt, and split between branch bytes and thread row-ids

**The failure:** The kit's own design names a harness write-deadline as a pressure-point (B3), and the readiness list carries it as R2 — but the deadline is **unbuilt**, and its settle-condition is **split** between two surfaces that have never coincided in the receipts. A pilot kit that ships a deadline with no receipted ack is shipping a lore seam, not a designed pressure-point; a pilot cannot run against a deadline whose settle-condition is undefined.

**Receipts:**
- `ACES-AUDIT-C3-20261107.md` row 9 — **"Arm 6 — harness-deadline (IMP-8) STANDS, kept open"**; verbatim: *"No PR-UPDATE ack in branch bytes since `5e0774420b`; thread tail UNMEASURED in this git-only lane. C3's 'neither confirmed nor refuted from branch bytes — kept open, never smoothed' is the honest register, verified as a characterization of the available evidence."*
- `ACES-REVIEW-C3-20261107.md` C3-9 — the catch is **KEPT OPEN**, not applied.
- `KIT-INNOVATION-20261107.md` R2 — *"The harness write-deadline is named, unbuilt, and split between branch bytes and thread row-ids"*; settle-condition: *"One picking of the settle-condition (thread row-id *or* branch-byte artifact), receipted — the kit cannot carry an unsettled deadline into a pilot."*
- The draft's own verdict: *"most critically R5 … and R4/R2 (the two unbuilt instruments the kit's own design names as pressure-points)."*

**Why it fails a pilot:** the deadline is the one component the kit's design names as a *pressure-point* — a bounded, falsifiable construct — yet it has no bounded form in the bytes (no date, no ack, no wall-clause). The pilot would inherit an ambient convention and call it a mechanism.

### (a2) The eval's pending state — the W2-isolation's SEPARATION-UNMEASURED

**The failure:** The kit's eval instrument — the one experiment that would convert preparation into arrival — has not executed. The verdict-line is SEPARATION-UNMEASURED per the wall-clause; the guard-preamble and empty-answer receipts are banked, but the isolate re-run is not. A pilot kit whose eval is pending cannot report a measured effect; it can only report a wall.

**Receipts:**
- `W2-ISOLATION-STATUS-20261106.md` (commit `847c61ac4f`) — the verdict-line is **SEPARATION-UNMEASURED**; the isolate re-run has not executed.
- `W2-ISOLATION-RUN-DESIGN-20261107.md` (commit `d760fcae90`) — the spec exists; the run does not.
- `NEXT-SHIFT-PLAN-20261107.md` §1 goal 1 — the goal's receipt is *"The filled skeleton's result file on the branch + the W2-ISOLATION-STATUS's verdict-line flipped from SEPARATION-UNMEASURED."*
- `HITL-GAINS-SKEPTIC-20261107.md` §1.2 — *"the W2-isolation's SEPARATION-UNMEASURED"*; the spec exists, the re-run is unexecuted.
- `KIT-INNOVATION-20261107.md` R4 — *"The W2-isolation re-run is SEPARATION-UNMEASURED; the eval-runtime cannot execute it yet."*

**Why it fails a pilot:** the kit's compaction component (A4/A5) reports a lift (below-3.0 hold 5/5 → 1/5, median 0.67 → 3.00) whose cause is **unseparated** from the handoff guard — the W2-isolation is precisely the experiment that would separate them, and it is unmeasured. A pilot would be running on a lift with an unseparated cause.

### (a3) The NOT-RUN gaps — the 40-marker census, 3 UNDER-SPECIFIED

**The failure:** The kit's honesty-markers are its discipline, but the census that enumerates them is **40 markers deep**, and 3 of them are UNDER-SPECIFIED — their settle-conditions are class-level, not experiment-level. A pilot kit that treats NOT-RUN as a terminal honest state (B1) risks freezing 40 gaps as "complete-as-NOT-RUN" — a register that declares its own gaps closed by classification.

**Receipts:**
- `HONEST-WALLS-CENSUS-20261106.md` — *"40 markers — 8 NOT-RUN, 8 UNMEASURED, 16 WALL-CLAUSED, 8 MARKED-OPEN. The counts are exact; the inventory is complete against the ground read."* Verdict: **CENSUS-COMPLETE**.
- The same census — *"The census's own UNDER-SPECIFIED list is non-empty (3 entries) — the markers whose settle-condition is a named class but whose exact experiment/word is not fixed in the marker's own text; these are flagged, not smoothed."*
- Row 1 — *"the GitHub-window side … **NOT RUN** — the hosted queue class — the ubuntu-latest runs queued forever on this account; the Avrea side IS the live surface."*
- Row 3 — *"The recitation-length class (the wheel's third): named, not yet measured."*
- `KIT-INNOVATION-20261107.md` B1 — *"The census names 3 UNDER-SPECIFIED markers whose settle-conditions are class-level, not experiment-level — the kit needs to know whether class-level settle-conditions suffice."*

**Why it fails a pilot:** the kit's B1 proposal makes NOT-RUN a *terminal* state; with 40 markers and 3 under-specified, the pilot's register would be majority-marker. The kit's honesty is real; its terminal-state design is not yet safe for a pilot's component register.

### (a4) The fabric's runs — dispatched, not concluded

**The failure:** The kit's breadth measure (A1/B2) is the 31-fork fabric — but at the last full audit the fabric's runs were **30 `queued`, 1 `in_progress`, with no conclusion column**. The runs were dispatched; they were not concluded. A pilot kit whose verification layer is dispatched-not-concluded has breadth without receipts.

**Receipts:**
- `GITHUB-RUNNER-FABRIC-20261107.md` — *"**Workflow presence (`.github/workflows/`) per fork: UNMEASURED in this lane.** … **no fork's workflow presence is claimed here**"*; the lane is git-only, so the per-fork `gh api` reads could not be executed.
- `ACES-AUDIT-C3-20261107.md` row 2 — *"Fabric runs: none landed (30 `queued`, 1 `in_progress`, no conclusions)"*; **CONFIRMED**.
- `ACES-AUDIT-C3-20261107.md` row 3 — *"31 run-ids distinct across rows (`42349103810 … 42349191196` scan-verified in the worktree read) … Identical pin `54395f9b4f0c` is the universal-pin design, correctly not treated as a receipt failure."*
- `KIT-INNOVATION-20261107.md` R1 — *"The fabric's conclusions were absent at the last full audit (30 `queued`, 1 `in_progress`, no conclusion column) — closed later only at the per-fork-pin wave."*

**Why it fails a pilot:** the fabric's 30/30 GREEN at the per-fork pins is a **later** wave (`FLEET-CYCLE-BODY-20261107-1403.md`), and the draft's own R1 settle-condition is *"A conclusions column in `FABRIC-RECEIPTS-20261107.md` with per-fork conclusion quotes, audit-verified — the current 30/30 GREEN stands as the per-fork-pin receipts but has no C3-style independent audit yet."* A pilot kit cannot carry an unaudited breadth claim as its verification layer.

### (a5) The machinery-vs-science ratio — one measured negative, one pending experiment, one self-referential loop

**The failure:** The study's real output is a *measured* negative (the K-recency gate FAIL) plus a staged evidence-set for four lines that have not moved. The machinery (fabric dispatch, loop audits, sweeps, census) is voluminous; the science (one FAIL, one unmeasured isolation, one quantified-but-unseparated heuristic) is thin. A pilot kit assembled as-is would be a machinery kit with a science gap at its center.

**Receipts:**
- `krecency/SYNTHESIS.md` — the K-recency gate's **measured FAIL**; *"the one experiment that converts preparation into arrival, unmeasured"* — with the one-mechanism line: *"the recitation floor and the governance decay are one window wearing two hats."*
- `HITL-GAINS-SKEPTIC-20261107.md` §1.1 — *"in the ~2 days since the study's first landing, none of the four lines has crossed from *staged* to *landed*; none of their gates has been touched by an upstream event; the upstream's surface is quiet."*
- `HITL-GAINS-SKEPTIC-20261107.md` one-line finding — *"The study's real output is a *measured* negative (the K-recency gate FAIL) plus a staged evidence-set for four lines that have not moved."*
- `NEXT-SHIFT-PLAN-20261107.md` standing frame — *"the study's four lines stay **STAGED** (restore #141876 · network #116673 · governance #139606 · compaction #140008)."*
- `KIT-INNOVATION-20261107.md` A5 — the seam component ships the ~240-token (2.4%) heuristic *"as its current best composition"*, with the +0.33 grain-divergence recorded as *"a known instrument correction"* — and the K-recency FAIL as *"the kit's measured negative result, the counterweight that keeps the healing claim honest."*

**Why it fails a pilot:** the kit's healing claim (A5) is carried by a heuristic whose instrument diverged (+0.33) and whose cause is unseparated (W2); its counterweight is a FAIL. A pilot of this kit would be a pilot of a machinery stack whose one positive mechanism is a FAIL and whose one separating experiment is unmeasured.

---

## (b) THE CANDIDATES' WEAKEST GROUNDS — attacking the innovation-candidates' evidence

Each attack is receipted. The draft's candidates are proposals, never settled design; the attacks below name where the evidence is invented, thin, or missing.

### (b1) A1/B2 — "per-fork independence" is same-account forks, and the audit itself notes the shared pin

**The attack:** The kit's breadth measure counts 31 forks — but all 31 are forks of the **same account** (`c0wb0yp0tat0`), dispatched the **same pinned head + battery** through the **same `workflow_dispatch`** mechanism. The "independence" is a count of one account's forks, not a count of independent verifiers. The audit's own row 3 concedes the shared pin: *"Identical pin `54395f9b4f0c` is the universal-pin design, correctly not treated as a receipt failure."* The draft's B2 open question — *"Which surfaces must be fork-independent for a kit component to be pilot-eligible — all 31 forks, or a named quorum?"* — is unanswered, so the kit's confidence function is **undefined**.

**Receipts:**
- `GITHUB-RUNNER-FABRIC-20261107.md` — *"the account's 31 forked repos are public … every fork is its own hosted-runner window. The fabric = the same pinned head + battery dispatched fork-by-fork through each fork's `workflow_dispatch`."*
- `ACES-AUDIT-C3-20261107.md` row 3 — *"Identical pin `54395f9b4f0c` is the universal-pin design, correctly not treated as a receipt failure."*
- `KIT-INNOVATION-20261107.md` B2 open question — *"The study's receipts show the fabric exists; the eligibility threshold is not in the bytes."*

### (b2) A2/B5 — the "honest termination" is a self-referential zero, audited in the same lane family

**The attack:** The ACES loop's "0 improvements" is confirmed by an audit (`ACES-AUDIT-C3`) that is itself a product of the same lane family, in the same git-only lane, with the thread **UNMEASURED** — *"thread UNMEASURED (flagged, never filled in)"*. The "converged twice" is C3 and C4, both in the same lane family. The termination proves the loop **stops**; it does not prove the loop **found** anything. The kit ships a stop-condition it can prove it met — but a stop-condition is not a result.

**Receipts:**
- `ACES-AUDIT-C3-20261107.md` — *"thread UNMEASURED (flagged, never filled in) ⇒ no new improvement can attach."*
- `ACES-AUDIT-C3-20261107.md` stop-line row — *"Verified like any claim: 0 new commits pre-C3 + 0 landed conclusions + thread UNMEASURED."*
- `KIT-INNOVATION-20261107.md` B5 open question — *"At pilot time, does a converged loop with 4 standing arms count as ready, or must the standing arms' settle-conditions be re-fired first? The study's bytes record the convergence, not the eligibility verdict."*

### (b3) A4/A5 — the compaction lift's cause is unseparated, and the instrument diverged

**The attack:** The kit's compaction component reports a lift (below-3.0 hold 5/5 → 1/5, median 0.67 → 3.00) on ~60 tokens (0.6%) — but the W2-isolation that would separate the lift from the handoff guard is **SEPARATION-UNMEASURED**. The draft's own A5 records the audit's *"REPRODUCTION-DIVERGENT at +0.33 (the grain) was CONFIRMED at the substance"* — a calibration admission, not a result. The kit ships a lift with an unseparated cause and a divergent instrument as its "current best composition."

**Receipts:**
- `KIT-INNOVATION-20261107.md` A5 — *"the four-movement walk lifts the below-3.0 hold 5/5 → 1/5, the median 0.67 → 3.00, on ~60 tokens (0.6%) of time-anchor block (`847c61ac4f`; W2-isolation SEPARATION-UNMEASURED per the wall-clause — the eval-runtime cannot execute the isolate re-run yet)."*
- `KIT-INNOVATION-20261107.md` A5 — *"the +0.33 grain-divergence recorded as a known instrument correction."*
- `KIT-INNOVATION-20261107.md` A4 — *"pattern-blindness correction (Cell A literals match no pattern in `_ANCHOR_PATTERNS` — C2 has no class for these strings)."*

### (b4) B6 — the reservation theorem is one case, and its retrieval check is unbuilt

**The attack:** The "one-anchor necessary-not-sufficient" theorem is grounded in **one** case (the `open_id is app-scoped` anchor reserving verbatim into summary_text yet the answer `""` in all three runs — Wall W2). The draft's own open question names the gap: *"What retrieval check closes the sufficiency gap? … the W2-isolation re-run is SEPARATION-UNMEASURED — the kit's retrieval check is currently an unbuilt experiment."* A theorem with one case and an unbuilt check is a hypothesis, not a theorem.

**Receipts:**
- `KIT-INNOVATION-20261107.md` B6 — *"reserving `open_id is app-scoped` verbatim into summary_text is NECESSARY-NOT-SUFFICIENT (answer `""` in all three runs, Wall W2)."*
- `KIT-INNOVATION-20261107.md` B6 open question — *"the kit's retrieval check is currently an unbuilt experiment."*
- `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` (c) NECESSARY-NOT-SUFFICIENT — the source finding.

### (b5) B3 — the harness write-deadline's "designed pressure-point" has no bounded form

**The attack:** B3 proposes the deadline as *"a named, bounded, falsifiable pressure-point"* — but the bytes contain no date, no ack, no wall-clause. The draft's own evidence is that the deadline *STANDS, kept open*, with the settle-condition split between a thread row-id and a branch-byte artifact. A pressure-point with no bounded form is a process construct, not a mechanism; the kit cannot ship it as designed.

**Receipts:**
- `KIT-INNOVATION-20261107.md` B3 evidence — *"ACES C3 Arm 6 / IMP-8 (harness-deadline) STANDS, kept open — no PR-UPDATE ack in branch bytes since `5e0774420b`, thread UNMEASURED in the git-only lane."*
- `KIT-INNOVATION-20261107.md` B3 open question — *"the kit must pick one and price the other as a wall."*

### (b6) B4 — the eval's provider-window schedule is an external dependency, not a kit instrument

**The attack:** B4 proposes wiring the eval instruments to the provider-window as a standing schedule — but the window's return is **not a kit instrument**; it is an external dependency the kit does not control. The draft's own open question concedes: *"What does the kit do while the window is closed — hold (the study's current register) or run a degraded local proxy? … the bytes contain no degraded-proxy run."* A schedule keyed to an external window is a wait, not an instrument.

**Receipts:**
- `KIT-INNOVATION-20261107.md` B4 evidence — *"the composition's full-eval at the provider-window's return (the ladder's ready)"*; *"W2-isolation SEPARATION-UNMEASURED 'per the wall-clause — the eval-runtime cannot execute the isolate re-run yet'."*
- `KIT-INNOVATION-20261107.md` B4 open question — *"the bytes contain no degraded-proxy run."*

### (b7) A3/A6 — the receipt-discipline and enrichment loop are process machinery, and the loop's product is documentation

**The attack:** A3's envelope ledger / goal-lock / NOT-RUN markers and A6's producer→audit→correction loop are **process machinery**. The loop closes, but its product is documentation (the enrichment arc's zero-write deaths are evidenced, but the deaths are deaths). The kit's self-repair component repairs the record, not the science. A pilot kit whose self-repair is documentation-grade cannot repair a science gap.

**Receipts:**
- `KIT-INNOVATION-20261107.md` A6 — *"producer `204bf6c672` … after three zero-write deaths, each evidenced with its class named; independent audit `537d2c3bda` (verdict PASS); record correction `f084af11cf`."*
- `KIT-INNOVATION-20261107.md` A6 revision — *"A producer/audit/correction closed loop with zero-write deaths evidenced rather than hidden is the kit's self-repair component."*
- `HITL-GAINS-SKEPTIC-20261107.md` — the non-progress ledger's verdict that the study's output is a measured negative plus staged evidence, not landed lines.

---

## (c) THE READINESS GAPS THE DRAFT MISSED — the pilot's needs the draft didn't name

The draft's R1–R8 is honest but incomplete. The gaps below are the ones ANY pilot of this kit would hit — plainly grounded, each with its receipt. The operator's pilot-shape is unknown; these are the gaps that any shape would hit.

### (c1) The pilot's protocol is unnamed — the kit is a component inventory, not a pilot design

**The gap:** The draft names 3oltan-seo as the pilot's start and the read-restore PR fix as the gate, but never names **what the pilot does** — its task, its success/failure line, its measured outcome. A kit of components without a pilot protocol is a parts bin.

**Receipt:** `KIT-INNOVATION-20261107.md` §(c) — *"The pilot's start-line is gated by the read-restore PR fix passing … that gate is external to this kit list and is recorded here as the list's precondition, not its item."* The list's items are all kit-carried gaps; the pilot's own shape is absent.

### (c2) The read-restore PR fix's state has no receipt in the kit

**The gap:** The pilot's start-line is the read-restore PR fix passing — but the kit carries **no receipt of its state** (open/closed/passed/failed). The draft records it as a precondition, not an item; a pilot cannot start against a gate whose state is unread.

**Receipt:** `NEXT-SHIFT-PLAN-20261107.md` THE NORTH — *"the RFC's next phase starting 3oltan-seo on a pilot AFTER the read-restore PR fix passes"*; `KIT-INNOVATION-20261107.md` §(c) — *"recorded here as the list's precondition, not its item."*

### (c3) The thread surface — the operator's actual surface — is UNMEASURED in the git-only lane

**The gap:** The kit's receipts are branch-byte-bound. The thread (the operator's surface) is **UNMEASURED** in the git-only lane — *"thread UNMEASURED (flagged, never filled in)"*. A pilot whose operator surface is unread is a pilot whose operator's word is unread.

**Receipt:** `ACES-AUDIT-C3-20261107.md` — *"thread UNMEASURED (flagged, never filled in)"*; `GITHUB-RUNNER-FABRIC-20261107.md` — *"This lane's terminal accepts git commit/push/rebase only and rejects `gh api` calls, so **no fork's workflow presence is claimed here**."*

### (c4) The four lines' evidence-sets have no adoption path — the kit's components are unbuilt for the pilot's lines

**The gap:** The kit's components (fabric, ACES loop, seam, reservation, enrichment) are **verification and process components**, not the four lines' evidence-sets. The pilot is the RFC's next phase; the kit's components do not map to the four lines' gates (restore, network, governance, compaction). A pilot kit whose components do not map to the pilot's lines is a kit for a different pilot.

**Receipt:** `NEXT-SHIFT-PLAN-20261107.md` standing frame — *"the study's four lines stay **STAGED** (restore #141876 · network #116673 · governance #139606 · compaction #140008)"*; `HITL-GAINS-SKEPTIC-20261107.md` §1.1 — the four lines' gates are named and un-crossed; `KIT-INNOVATION-20261107.md` §(a) — the components are verification/process, not line-evidence.

### (c5) The K-recency FAIL's mechanism is unmeasured — the kit's one science result has no mechanism

**The gap:** The K-recency gate's FAIL is the study's one measured negative, but the draft's A5 notes *"the one experiment that converts preparation into arrival, unmeasured"* — the mechanism that would convert the FAIL into an arrival is itself unmeasured. A pilot kit whose one science result has no mechanism is a kit with a negative and no path.

**Receipt:** `krecency/SYNTHESIS.md` — *"the K-recency gate's measured FAIL (the one experiment that converts preparation into arrival, unmeasured)"*; `KIT-INNOVATION-20261107.md` A5 — *"the K-recency FAIL as the kit's measured negative result."*

### (c6) The pilot's seat and the kit's seat differ — the pilot's operator surface is the thread, not the branch

**The gap:** The kit is branch-bound (fork-only; nothing public). The pilot's operator (3oltan-seo) and the user's word live on the thread/upstream surface. A kit whose readiness is branch-bound cannot gate a pilot whose start-line is thread-bound — the two surfaces never coincide in the receipts.

**Receipt:** `KIT-INNOVATION-20261107.md` header — *"Branch: `study/rfc-143379-rig-20261105` (fork-only; nothing public)"*; `HITL-GAINS-SKEPTIC-20261107.md` §1.1 — *"none of their gates has been touched by an upstream event; the upstream's surface is quiet"*; `NEXT-SHIFT-PLAN-20261107.md` — *"Gate: nothing public without the user's word."*

---

## VERDICT

The kit's substrate is real and receipted; the draft's honesty is genuine. But the as-is assembly fails at five non-negotiables — the unbuilt split deadline, the unmeasured eval, the 40-marker census, the dispatched-not-concluded fabric, the machinery-vs-science ratio — and the candidates' evidence is thinnest at the kit's three load-bearing claims (breadth, termination, reservation). The draft's R1–R8 names eight gaps; the counter-pass names six more that any pilot would hit. The pilot cannot run on the kit alone until both lists carry their settle-conditions — and the two unbuilt instruments the kit's own design names as pressure-points (R2, R4) are the first to close.

**Artifact:** `studies/rfc-143379-rig/KIT-SKEPTIC-20261107.md` · **Branch:** `study/rfc-143379-rig-20261105` · **Seat:** `meituan/longcat-2.5:free`