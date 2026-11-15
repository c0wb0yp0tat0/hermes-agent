# HITL Gains — the study's real gains so far, receipted

**Seat:** `stealth/crouton-alpha` · **Lane:** copycat lane 1, the draftsman · **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public) · **Date:** 2026-11-07 · **Register:** the plain human register — a proper human-in-the-loop summary, receipted, no machinery-noise.

A note before the ledger: this is a summary for the human in the loop, not a trophy case. Every gain below carries its receipt — the run, the commit, the file — and, just as important, what it is actually worth for the RFC #143379 gate. The verification receipt is the point; the machinery is only the means, never the gain itself. Where something is not yet gained, that is stated plainly at the end, unsmoothed.

---

## The gains ledger

### 1. The 31-fork verification fabric went from a design to real, receipted runs

**What was gained.** All 31 of the account's public forks were each given their own GitHub-hosted runner window, and the same test battery was dispatched to all 31 at once, at the pinned head. That is no longer a claim about a single fork — it is 31 distinct runs, each with its own run-id.

**Receipts.**
- The inventory — hand-counted, live: 31 forks, zero difference from the brief's 31 (`GITHUB-RUNNER-FABRIC-20261107.md`, commit `6fef8e3379`; its 31-row table names each fork with its default branch and last-push time).
- The launch — battery deployed and dispatched 2026-11-07 01:52–01:57 ET at the universal pin `54395f9b4f0c…` (`FABRIC-RECEIPTS-20261107.md`, commit `9dc35ee053`), first run-id `gent-governance-toolkit … 42349103810`, last `projectsend … 42349177806`.
- The follow-through — the 31 runs were later recorded as green on all three surfaces: the Avrea union closed green (`42250764897`, the reconciliation arc closed), the hosted fabric went green after the fix below, and the rig's own self-hosted run `42349137165` landed green at 02:00 (per the fleet body at `f084af11cf`, `FLEET-CYCLE-BODY-20261107-1403.md`). The independent audit confirmed the launch numbers cold (`ENRICHMENT-AUDIT-20261107.md`, commit `537d2c3bda` — verdict PASS, rows A1–A8).

**What it is worth for the gate.** This is the platform-side breadth the RFC's verification always lacked: independent, hosted, per-fork receipts at a known pin. A green run you can point to, per fork, is evidence; a design doc is not. The honest catch — the first wave went 30 of 31 red, and that red is itself accounted for in the next gain — does not erase the breadth; it is what makes the receipt trustworthy.

### 2. The improver loop ran four full cycles and converged — provably, twice

**What was gained.** The loop that reads the study's own work, names what could be better, and then has those names audited and reviewed independently, ran four cycles (C1 through C4). Cycle 1 named 14 improvements; the steady state is now cycles that name *zero* — and that zero was confirmed twice in a row, by independent audit.

**Receipts.**
- Cycle 1: 14 named improvements → 9 confirmed / 2 nuanced / 3 refuted (`ACES-IMPROVE-20261107.md`, commit `e640efb7a3`; audit `ACES-AUDIT-20261107.md`).
- Cycle 3: 0 improvements named, a NO-IMPROVEMENTS stop-line carried (`ACES-IMPROVE-C3-20261107.md`, `c9a0325719`); its audit came back **11 CONFIRMED / 0 NUANCED / 0 REFUTED** (`ACES-AUDIT-C3-20261107.md`, `ca15b98e1f`); its review confirmed the same (`ACES-REVIEW-C3-20261107.md`, `98e8de2303`).
- Cycle 4: 0 new improvements again, one re-derivation pass named (IMP-C4-1) for the next live cycle (`ACES-IMPROVE-C4-20261107.md`, `c5e321e73b`); its audit **11/11 CONFIRMED** (`ACES-AUDIT-C4-20261107.md`); its review likewise (`ACES-REVIEW-C4-20261107.md`, `ccd33a1ebf`). The fleet body records it plainly: "NO-IMPROVEMENTS CONFIRMED TWICE" (`f084af11cf`).

**What it is worth for the gate.** A verification study lives or dies on whether its own quality claims survive independent checking. Being able to say "two successive cycles, independently audited, found nothing left to improve — and here are the audit ledgers" is the strongest thing this study can put in front of a reviewer. It converts "we think we're good" into a receipted non-finding.

### 3. The fork-fleet's hosted-window machinery is built and actually used

**What was gained.** The machinery to deploy a workflow to every fork's default branch and dispatch it fork-by-fork through the platform's own dispatch is built, and it has been used — not once, but for a second wave too.

**Receipts.** The battery's deployment and dispatch across all 31 forks (`FABRIC-RECEIPTS-20261107.md`); the second wave, the per-fork-pin re-dispatch, with its own run-ids, e.g. `agent-governance-toolkit … 42349942414`, `dsh-node-addon-require-builtin … 42350006029` (commit `2becb714af`); the study's own fork run `42349137165` green at 02:00 (`f084af11cf`).

**What it is worth for the gate.** Reproducibility you can repeat is what separates a one-off result from a verification. If the next pinned head needs checking, the fleet can be re-dispatched in minutes rather than rebuilt — that lowers the cost of every future verification the gate will ever ask for.

### 4. The scheduled sweeps and harvests are running on a rhythm, with receipts

**What was gained.** Recurring, scheduled passes over the study's own accumulated work — sweeping for drift, redundancy, and stall-rows — are happening on a timetable and landing their receipts like any other work.

**Receipts.** The scheduled negentropy sweep of 2026-11-07 at 13:50: leg A (reservation does not lift), leg B (the k-term's two-tier refinement), leg C (the budget's consolidation — four protected classes resolved), and leg D's stall-row with a re-fire rowed (`cc0993727c`, `NEGENTROPY-SWEEP-20261107-1350`; recorded in `f084af11cf`). Earlier legs of the same sweep family are on the branch (`3ddd351070`, `6524d1c5cd`).

**What it is worth for the gate.** Verification decays; a study that never re-checks its own claims quietly becomes a liability. A scheduled sweep that leaves receipts — including naming its own stalls — is how the evidence base stays current enough to stand behind at the gate.

### 5. The study caught its own fallible instruments — and banked the lessons

**What was gained.** Two classes of instrument error were found, named, and fixed in the open, rather than smoothed over.

**Receipts.**
- **The inputs-encoding class.** The dispatch's `-f inputs=` form double-escaped its payload; the object form (`--input -`) is the correct way. Found and banked at the launch itself (`FABRIC-RECEIPTS-20261107.md`, commit `9dc35ee053`; corroborated in `ENRICHMENT-AUDIT-20261107.md`, rows A1–A2).
- **The checkout-class.** At the universal pin, 30 of the 31 fabric runs went red on checkout — the pin as requested did not match what executed. The fix was a per-fork-pin re-dispatch (`2becb714af`), after which the fabric recorded green (fleet body `f084af11cf`: "30/31 RED at the universal pin on the checkout-class, then 30/30 GREEN at the per-fork pins").

**What it is worth for the gate.** This is the gain people most often underrate. An instrument that silently lies is worse than no instrument. A study that has *demonstrated* it catches its own bad instruments — with the class named and the fix receipted — is one whose green results a reviewer can actually believe.

---

## The honest ceiling — what is not yet gained

Stated plainly, never smoothed:

1. **The four lines still staged.** The restore, the network, the governance, and the compaction lines of RFC #143379 have *not* arrived upstream. The campaign stands at the provision, not the arrival — "FAIL today" is still the honest self-assessment (`FLEET-CYCLE-BODY-20261107-1403.md`, `f084af11cf`); the arrivals await the user's word.
2. **The eval-window's wall.** The isolation experiment that would settle the study's last open measurement confound (SEPARATION-MEASURED or SEPARATION-REFUTED) remains unmeasured — the eval runtime cannot yet execute the isolate re-run (`f084af11cf`; the W2-isolation wall-clause at `847c61ac4f`). The near-full recovery of the seam-arc (5/5 → 1/5 below 3.0, median 0.67 → 3.00) is real, but its isolation check is not.
3. **The harness write-deadline is unbuilt.** The harness-deadline item (IMP-8) stands open: no PR-UPDATE acknowledgement has landed on the branch, and the thread tail is unmeasured from this lane — it is kept open, neither confirmed nor refuted (`ACES-IMPROVE-C3-20261107.md`, arm 6; `ACES-AUDIT-C3-20261107.md`, per-row 9; carried through C4). Nothing is claimed there until a receipt exists.
4. **Two receipt gaps ride along.** The fabric's settle bytes — a seat line, a falsifier locator, a settle condition — are still missing from the receipts file, so the landing-gate arm remains only partially satisfied (C3/C4 arm 1); and the per-fork workflow-presence for every fork is still unmeasured from this lane (C3/C4 arm 2, `GITHUB-RUNNER-FABRIC-20261107.md` L7/49: "UNMEASURED in this lane"). Both are small, named, and open — listed here so nobody has to discover them.

---

## The one-line version

The study has gained a receipted 31-fork verification fabric that runs green, a self-improvement loop that converged and was independently audited to zero twice, recurring scheduled sweeps, and a demonstrated habit of catching its own bad instruments — and it has *not* yet gained the four lines' arrival, the eval-window's isolation measurement, or the harness write-deadline. That is the honest state, and it is a good one to be in.
