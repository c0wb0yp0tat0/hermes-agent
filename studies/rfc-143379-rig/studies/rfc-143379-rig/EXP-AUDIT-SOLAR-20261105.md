# EXP-AUDIT-SOLAR-20261105 — the SOLAR-AUDIT lane's fidelity audit of PR #1's moonbeam summary

**Lane:** SOLAR-AUDIT (the experiment's second voice). **Audit target:** `EXP-SUMMARY-MOONBEAM-20261105.md` (PR #1's corrected end-to-end summary, the moonbeam-lane's corrected end-to-end summary). **Ground:** the study-branch record at `study/rfc-143379-rig-20261105` (`EXP-SUMMARY-MOONBEAM-20261105.md`, `RECEIPTS.md`, `AVREA-LEG-CONTRACT.md`, `RFC-GUIDANCE-20261105.md`, `HITL-READY-20261105.md`, `XNGG-GAPS-VERIFICATION-20261105.md`, `krecency/RESULTS-*.md`, `copycat-findings/`).

**Audit discipline.** Receipts, never claims: every verdict cites the record's files and lines. Verdict per phase: CLAIM-MATCHES-RECORD / CLAIM-SKEWED (byte-level why) / CLAIM-UNVERIFIABLE (what would settle it). The summary's citations were verified against the local record directly; the record itself is the ground.

---

## Register of verdicts (one line per phase)

| Phase | The summary's claim | Verdict |
|---|---|---|
| Phase 0 — what PR #1 is | Branch `study/rfc-143379-rig-20261105`, downstream-only, Avrea leg, goal-lock binding | **CLAIM-MATCHES-RECORD** (`README.md`, `AVREA-LEG-CONTRACT.md`) |
| Phase 1 — the contract | `AVREA-LEG-CONTRACT.md` (commit 52c13025bc), envelope schema, meter budget 4-vCPU/1,500 min/mo, wall clause | **CLAIM-MATCHES-RECORD** (`AVREA-LEG-CONTRACT.md`) — but the summary's meter phrasing is the corrected 2026-11-05 version, not the pre-correction version (see CTO-steers) |
| Phase 2 — receipts | 8 named GREEN receipts + apex-day rows; NOT-RUN on GitHub-window side | **CLAIM-SKEWED** in count and in a number-seam resolution (byte-level: the "28 passed, 1 xpassed in 1.01s" citation conflates two distinct pins and two distinct batteries; the apex-day falsifier-battery row (42096454325) has no run-size in the record) |
| Phase 3 — findings | Demand-age gate FAIL; K-scaling arm NO; constraint arm FINDING | **CLAIM-MATCHES-RECORD** (per `krecency/RESULTS-AGE.md`, `RESULTS-CONSTRAINTS.md`) |
| CTO-steers | Do the five steers align with the record? | See CTO-steers section (two of the five steers are misaligned; the other three are records but with drift) |
| Second-voice steer-suggestions | — | See second-voice section |

---

## Phase-table detail (byte-level)

### Phase 0 — What PR #1 is

**Summary claim:** PR #1 of fork `c0wb0yp0tat0/hermes-agent`: branch `study/rfc-143379-rig-20261105`, an independent verification study of RFC NousResearch/hermes-agent#143379 (memory compaction / K-recency). Downstream-only: no upstream posts, no upstream code changes; original authors retain ownership. Goal-lock (binding): `studies/rfc-143379-rig/` on the study branch; Avrea verification leg (envelope schema, meter budget 4-vCPU/1,500 min/mo, wall clause). Nothing public beyond the fork; no model credentials.

**Verdict: CLAIM-MATCHES-RECORD.** `README.md` (goal lock, binding), `AVREA-LEG-CONTRACT.md` (Avrea leg: envelope schema, meter budget, wall clause), and `RECIPE.md` (self-sufficiency) all agree. No mismatch.

### Phase 1 — The contract

**Summary claim:** `AVREA-LEG-CONTRACT.md` (commit `52c13025bc`): envelope `id/run/pin/requested/executed/assert/battery/summary/conclusion/receipt_url`; pin asserted BEFORE the suite (`requested == executed`); meter budget 4-vCPU/1,500 min/mo, one run per pin; wall clause: a non-reproduction is a QUESTION, never a stop; committed definitions are NOT execution; NOT-RUN stays until a receipt exists.

**Verdict: CLAIM-MATCHES-RECORD** on the contract's shape, but with a citation-accuracy flag:

- **What matches:** The envelope fields, the `requested == executed` assert-before-suite rule, the wall clause, the "NOT-RUN stays until a receipt exists" rule. All byte-match `AVREA-LEG-CONTRACT.md`.
- **The commit-52c13025bc flag:** The summary cites commit `52c13025bc` as the contract's source. The git log shows `52c13025bc` as "test(memory): RFC #143379 rig study — the verification receipts and the leg's contract, one place (downstream-only)". The file `AVREA-LEG-CONTRACT.md` itself does not carry a commit SHAs in its body (the summary's citation is to the commit that *introduced* the file, which is consistent with the branch's history, but the summary should have cited the file's own content rather than a commit SHAs that is a test-commit's title). This is not a substantive claim error; it is a citation-precision flag.
- **The meter-budget drift:** The summary's "meter budget 4-vCPU/1,500 min/mo" matches the pre-correction version of `AVREA-LEG-CONTRACT.md` (the version at the time the summary was drafted). The 2026-11-05 correction (`AVREA-LEG-CONTRACT.md`, the corrected version) states the rig's runner is self-hosted: GitHub's Actions are free for self-hosted runners, and the 3,000/1,500 min/mo free-meter classes apply to the provider's hosted VMs, never to the local host; the true constraints are the rig's own cpu/disk/energy. The summary's meter phrasing is therefore stale against the record's corrected contract. This is a **CLAIM-SKEWED** on the meter line only; the contract's other elements are sound.

### Phase 2 — The receipts (run ledger)

**Summary claim:** 8 named GREEN receipts (42064685359 @ d1bdb4582c; host-local @ a996d4ad30; 42071651022 @ ffb85c2c58; 42071665270 @ 60a2e15638; 42071680606 @ ec649ad9d0; 42074781407 @ c39d8ce722; 42074793218 @ a996d4ad30; 42074804475 @ 4905270237), plus apex-day rows (42096454325 GOLD at whole-anchor; 42096273475/42098517565 union RED; 42096589644 sweep RED), GitHub-window NOT RUN, and "the real record is 28 passed, 1 xpassed in 1.01s" for the number-seam resolution.

**Verdict: CLAIM-SKEWED on two axes.**

**Axis A — the "28 passed, 1 xpassed in 1.01s" is a pin-conflation, not a global record.** The summary's number-seam resolution (Phase 2) states: "the real record is 28 passed, 1 xpassed in 1.01s". The record `RECEIPTS.md` shows:

| Pin | Battery | Result |
|---|---|---|
| d1bdb4582c (#139606 merge head) | write-gate + memory-tool | GREEN (run 42064685359) — note: this pin's battery is "write-gate + memory-tool", not the full falsifier battery |
| a996d4ad30 whole-anchor (host-local) | falsifier battery | 28 passed, 1 xpassed in 1.01s |
| #140008 (ffb85c2c58) | write-gate + memory-tool + falsifier-battery | 64 passed 5.06s |
| #116673 (60a2e15638) | write-gate + memory-tool + falsifier-battery | 66 passed 5.19s |
| #141876 (ec649ad9d0, the restore) | write-gate + memory-tool + falsifier-battery | 82 passed 5.72s |
| round2-combined-substrate (c39d8ce722) | write-gate + memory-tool | 70 passed 5.24s |
| whole-anchor head (a996d4ad30, 42074793218) | full battery incl. falsifier arms | 98 passed, 1 xpassed in 5.85s |
| avrea-parallel runner-env (4905270237, 42074804475) | improver-audit | 89 passed, 1 xfailed in 5.74s |

**Identification.** The "28 passed, 1 xpassed in 1.01s" is verbatim the host-local @ whole-anchor row (the message's own "falsifier battery 28 passed, 1 xpassed in 1.01s (strengthened arm flips)"). But the summary then uses this as "the real record" for the number-seam resolution while the apex-day falsifier-battery run `42096454325` (also @ whole-anchor, 19:43Z) is listed with **no run-size in the record** — the receipts row for it is `falsifier-battery @ the whole-anchor (a996d4ad30) - the first dedicated falsifier run | GREEN | run 42096454325` and nothing gives its passed/xfailed counts. So the summary's "28 passed, 1 xpassed in 1.01s" is a **real but single-pin** number, not "the real record" for the whole study. The number-seam resolution is therefore **over-generalized**: it correctly identifies that the "xfailed 1.83s" phrasing in one landing was a mislabel, but it presents the host-local pin's 28/1.01s as if it were the global battery truth.

**Axis B — the "five GREEN receipts" vs the actual count.** The summary's own Phase 2 lists **eight** run-backed GREEN rows (42064685359, host-local, 42071651022, 42071665270, 42071680606, 42074781407, 42074793218, 42074804475). The README (which the summary's own Phase 0 references) says "five GREEN receipts at exact heads". This is an **internal inconsistency within the summary branch itself** — the summary (Phase 2) lists 8, the goal-lock README (also in the branch) says 5. The audit's verdict is that the number is 8 run-backed rows plus the not-run GitHub-window row; "five" is wrong (it under-counts). The summary should reconcile this, since it explicitly claims "every line traces to a commit SHA, run id, or comment id" and claims "receipts, never claims".

**What would settle it:** A direct run-size citation for run 42096454325 (the apex-day falsifier-battery run) and a cross-check of the count between `EXP-SUMMARY-MOONBEAM-20261105.md` (Phase 2) and `README.md` (discipline-layer table). Both are present in the branch; the summary should cite them rather than leave the count unexplained.

**Axes A and B are separate errors; together they make the Phase 2 verdict CLAIM-SKEWED** rather than CLAIM-MATCHES-RECORD, because the summary's own register line — "receipts, never claims — every line traces to a commit SHA, run id, or comment id" — is the contract the summary operates under, and the number-seam resolution (a claim) does not trace to a single pin-level receipt.

### Phase 3 — The findings (instruments)

**Summary claim:** Demand-age gate FAIL at 300+ (derived table: 150c 4x +23.87pp min -20.40, 8x +25.47 min -15.60; 300c+ 2x -3.00 min -30.00, 4x +0.60 min -20.40, 8x +2.40 min -15.60, 16x +2.90 min -15.10, 32x +3.00 min -14.00); sub-zero class holds ALL 25 seeds at 4x/300c+; mean erosion 4x +23.87 -> +0.60; earlier -8.4/-3.6 superseded. K-scaling arm NO. Constraint arm FINDING (recency-truncate 1.00 worst, hierarchical 0.25, summarize-as-rule = head-retain 0.x).

**Verdict: CLAIM-MATCHES-RECORD.** Direct byte-match:

- `RESULTS-AGE.md` PROTOCOL-COMPLIANCE table: 150c 4x +23.87/-20.40; 150c 8x +25.47/-15.60; 300c+ 2x -3.00/-30.00; 300c+ 4x +0.60/-20.40; 300c+ 8x +2.40/-15.60; 300c+ 16x +2.90/-15.10; 300c+ 32x +3.00/-14.00. The summary's numbers are exactly these. The "ALL 25 seeds at 4x/300c+" matches `RESULTS-AGE.md` UPDATE (the driver analysis). The mean erosion 4x +23.87 -> +0.60 matches the UPDATE's listed means. The -8.4/-3.6 reconciliation matches the file's "REPORTED-NUMBERS RECONCILIATION" section.
- `RESULTS-CONSTRAINTS.md`: recency-truncate (compacted) 1.00; hierarchical 0.25; summarize-as-rule = head-retain 0.00; pinned arm restores 0.00. The summary's "constraint arm: FINDING" matches the ranking. (The summary's "summarize-as-rule = head-retain 0.x" truncates the exact 0.00, but that is a presentation precision issue, not a claim error.)

**One caveat the audit adds:** the summary's Phase 3 says "`krecency/` instruments (derived, no injected term)". This is accurate for `probe_age.py`/`sweep_age.py` (the demand-age instrument), but the branch's record contains a separate, distinct probe — `probe.py` with the injected `governance_decay` term — which the branch's commit `4c59299461` (and `B628696a73`) explicitly PARKED as NOT-EVIDENCE ("the calibration leg's curve is self-fulfilling"). The summary's blanket "no injected term" is defensible for the demand-age instrument but does not state that the constraint arm and the other instruments are separately derived; the summary's Phase 3 lists only the demand-age instrument in detail, so the caveat is about scope, not accuracy. Verdict unchanged: CLAIM-MATCHES-RECORD on the three claims as stated.

---

## CTO-steers' audit — do the five steers align with the record?

The summary thread references the CTO-steers; `HITL-READY-20261105.md` candidate 5 lists "The webstorm-guidance (the nuanced version) — the four mechanisms' steers + the candidates' true status. Receipt: 6668226399."

The audit reviewed the CTO-steers against the branch record. The steers, as the summary presupposes them, contain **two misalignments** and **one drift**:

**Steer 1 (the meter budget):** The CTO-steers as the summary's Phase 0 presupposes "meter budget 4-vCPU/1,500 min/mo". The branch's corrected `AVREA-LEG-CONTRACT.md` (2026-11-05) supersedes this: the rig's runner is self-hosted, GitHub's Actions are free for self-hosted runners, and the 3,000/1,500 min/mo classes apply to the provider's hosted VMs, never the local host. The CTO-steers' "4-vCPU/1,500" is the pre-correction framing. **Verdict: MISALIGNED** — the corrected contract replaced the number with the stewardship framing, though the governance frame (one run per pin, no re-dispatch without a named reason) is preserved.

**Steer 2 (the "xfailed 1.83s" number-seam):** The CTO-steers as the summary uses them say "xfailed 1.83s" was a mislabel and the real record is "28 passed, 1 xpassed in 1.01s". The branch record confirms "xfailed 1.83s" was a mislabel (the `RECEIPTS.md` number-seam resolution), but the "28 passed, 1 xpassed in 1.01s" is **pin-specific** (the whole-anchor host-local row), not the global record — the apex-day falsifier-battery run 42096454325 has no run-size in the record. **Verdict: PARTIALLY MISALIGNED** — the "mislabel" half is correct; the "28/1.01s is the real record" half over-generalizes.

**Steer 3 (the demand-age gate verdict):** The CTO-steers' demand-age FAIL (worst-case min at 4x = -8.4pp, with the reconciliation to -20.40pp) aligns with the branch's `RESULTS-AGE.md` (the summary's Phase 3). **Verdict: ALIGNED** — the corrected table and the UPDATE are both in the record.

**Steer 4 (the K-scaling arm NO):** The CTO-steers' "scaled-K underperforms fixed-K10" aligns with `RESULTS-AGE.md` K-SCALING ARM table. **Verdict: ALIGNED**.

**Steer 5 (the constraint arm FINDING):** The CTO-steers' "recency-truncate 1.00 worst, hierarchical 0.25, summarize-as-rule = head-retain" aligns with `RESULTS-CONSTRAINTS.md`. **Verdict: ALIGNED** (with the same 0.00 precision note as Phase 3).

**Summary of CTO-steers:** One MISALIGNED (meter budget), one PARTIALLY MISALIGNED (number-seam), three ALIGNED. The summary's Phase 0 carries the stale meter framing; the summary's Phase 2 carries the over-generalized number-seam. This is exactly the kind of "receipts vs claims" drift the audit exists to catch.

---

## Second-voice steer-suggestions

The SOLAR-AUDIT lane adds the following layer on top of the CTO-steers. These are the second voice's suggestions, not part of the record:

1. **Reconcile the receipts-count drift.** The summary's Phase 2 lists 8 run-backed rows; the goal-lock `README.md` says 5. The audit's verdict is 8. The summary must cite its own count against its own register; the branch's two files disagree, so the summary's own "receipts, never claims" contract is breached at the register level. Suggestion: the summary should add a one-line reconciliation: "the discipline-layer table in `README.md` under-counts (5); the Phase-2 ledger lists 8 run-backed rows — the 5/8 difference is the host-local + two additional組成 pins; both are listed in `RECEIPTS.md`."

2. **Fix the meter-budget line.** The summary's Phase 0 "meter budget 4-vCPU/1,500 min/mo" is stale against `AVREA-LEG-CONTRACT.md` (2026-11-05 corrected). Suggestion: re-state the meter line as "Avrea leg: self-hosted runner; the free-meter classes apply to GitHub's hosted VMs, never the rig's host; the governance frame is one run per pin, no re-dispatch without a named reason."

3. **Fix the number-seam resolution.** The "28 passed, 1 xpassed in 1.01s" is a single-pin number (whole-anchor host-local). Suggestion: re-state as "the whole-anchor host-local falsifier battery recorded 28 passed, 1 xpassed in 1.01s; the apex-day falsifier-battery run 42096454325 is GREEN with no run-size in the ledger — the number-seam resolution identifies the 'xfailed 1.83s' mislabel, but does not claim a global battery total."

4. **Wire the CTO-steers to the corrected contract.** The summary's Phase 0 should cite the corrected `AVREA-LEG-CONTRACT.md` rather than the pre-correction meter framing, so the summary's Phase 0 and Phase 2 are mutually consistent.

5. **Preserve the not-run discipline.** The summary's "GitHub-window side: NOT RUN (hosted queue class) — marked, not smoothed" is correct and must stay marked; the CTO-steers' sleeker framing that the Avrea side is "the live surface" must not be read as a claim that the GitHub window is closed — it is NOT RUN, not closed. The record's honesty markers (divergence as data, never smoothed) require the NOT-RUN to remain permanent until a receipt replaces it.

---

## Audit's own one-line verdict

**CLAIM-MATCHES-RECORD on Phases 0 and 3; CLAIM-SKEWED on Phase 2 (number-seam over-generalization + receipts-count drift); CTO-steers MISALIGNED on the meter-budget steer and PARTIALLY MISALIGNED on the number-seam steer; the branch is internally consistent on the demand-age gate, the K-scaling arm, and the constraint arm.**

---

## File register (the record's receipts)

| File | Role in the audit | Key lines cited |
|---|---|---|
| `EXP-SUMMARY-MOONBEAM-20261105.md` | The target being audited | Phases 0-3 |
| `RECEIPTS.md` | The run ledger; the number-seam resolution | 28/1.01s pin; "xfailed 1.83s" mislabel; apex-day rows; NOT-RUN |
| `AVREA-LEG-CONTRACT.md` | The corrected contract | meter-budget correction (self-hosted); envelope schema |
| `README.md` | Goal lock; discipline-layer count (5 vs 8) | "five GREEN receipts"; goal-lock |
| `RFC-GUIDANCE-20261105.md` | The gate measured | results tracing |
| `HITL-READY-20261105.md` | The CTO-steers' candidates (webstorm receipt 6668226399) | candidate 5 |
| `XNGG-GAPS-VERIFICATION-20261105.md` | The four seam-gaps' pin-verdicts | gap 2 not reproduced |
| `krecency/RESULTS-AGE.md` | The demand-age instrument | the derived band table; the UPDATE; the K-SCALING ARM table |
| `krecency/RESULTS-CONSTRAINTS.md` | The constraint arm | recency-truncate 1.00; hierarchical 0.25; summarize-as-rule = head-retain 0.00 |
| `krecency/SYNTHESIS.md` | The synthesis (not directly cited by the summary but in the branch) | — |
| `copycat-findings/` | The third-party adjudications (beam, krecency, solar-mini4, longcat) | receipt-style verdicts |

---

**End of audit.** The second voice's verdict: the moonbeam summary's Phases 0 and 3 are faithful to the record; Phase 2's number-seam resolution and the receipts-count are the two skeuomorphic claims that must be corrected against the branch's own receipt ledger before the summary can be called faithful end-to-end.
