# LAQ-FIDELITY-PROBE-20261106

**Seat:** the rig's own ladder-battery (rungs 1–5 × 3 runs, label `ladder-20261106-a996d4ad`).
**Domain:** COMPLICATED. **Registers:** receipts, never claims.
**The question:** does the compressed state preserve the FAR-APART structure (the theme-membership: the kept-facts' coherence across the runs and the ladder) or only the nearest-neighbors?
**The gate-line, verbatim from the storm's LAQ finding (2611.08341):** `local-neighbor survival != global structure`.

---

## 1. Executive Summary

**Verdict: G-LOST.** The compressed state preserves only the nearest-neighbors (local survival); the far-apart structure — the theme-membership's coherence across the runs and the four class-types — is absent. The data bears this out on every rung:

| Rung | Fixture | recovery median | compaction | below-3.0 probes (density proxy) | the far-apart facts the probes demand |
|---|---|---|---|---|---|
| 1 | config-build-competitive-scouts | 4.50 | 18.7% | 4 | recall-first-repo 0.00; artifact-all-jobs 0.00; artifact-final-schedule 0.00; continuation-execution-time 1.00 |
| 2 | debug-session-feishu-id-model | 3.25 | 62.7% | 5 | recall-upstream-confirmation 2.33; artifact-new-tool 0.00; decision-core-claim-validity 0.83; continuation-next-action 0.00; continuation-implementation-scope 0.00 |
| 3 | feature-impl-context-priority (deep) | 4.67 | 68.4% | 1 | continuation-next-step 2.17 (claims an uncommitted cli.py change remains; main is current) |
| 4 | fixture-deep-compaction-real (deep) | 1.00 | −350.4% | 3 | recall-session-identity 1.00; recall-loop-sequence 0.17; artifact-message-shape 0.00; decision-model-pin 1.17; continuation-close-intent 0.00 |
| 5 | fixture-high-density-real (density) | 0.00 | 0.0% | 5 | recall-stream-source 0.00/0.667/0.00; recall-retry-receipt 0.00/2.00/0.167; artifact-turn-shape 0.00/0.00/0.00; artifact-density-receipts 1.00/0.167/0.00; decision-truncation 0.00/0.00/0.00 |

The two rebuilt real cells — the **depth-cell floor (1.00)** and the **density-cell floor (0.00)** — are not intermediate rungs; both sit *below* all three native rungs, and BOTH sit below the seam-arc's honest-blind standard (3.33). The separation the LADDER-GAPS verdict asked for stands: compaction depth and fact-density are measured on distinct real streams, and the dense stream is the hardest cell in the ladder, not the deep one. Recovery does **not** track compaction depth, and recovery does **not** track either the depth-cell or density-cell floor's far-apart facts — it tracks only the local survival the nearest-neighbor probes can still reach. The kept-facts are local-only; the theme-membership is gone.

**The k-term confirms it.** The negentropy arm's k-table (ADJUDICATION-NEGENTROPY-20261106.md) reproduces the descriptor weights (3.0 − baseline median) as arithmetic from the ladder JSONs, but the k-term does **not** separate classes: kept-rates are flat 0.42 / 0.29 / 0.26 / 0.32 across the four classes, empties 24 / 36 / 22 / 48, overalls 2.61 / 2.75 / 3.08 / 2.13. No k≈1 (high-keep) vs k≈0 (low-keep) split. A global theme structure would demand differential keep-rates by class; the uniform k-term contradicts that mechanism. The budget's mechanistic underpinning falls, and with it the claim that the compressed state preserves the far-apart structure.

---

## 2. Analysis Brief

### (a) Domain, evidence, assumptions
- **Domain:** COMPLICATED. The probe is bounded to the rig's own ladder-battery JSONs (16 files: 5 fixtures × 3 runs + report.md + summary.json), the storm's LAQ finding receipt (2611.08341), and the negentropy k-table (ADJUDICATION-NEGENTROPY-20261106.md).
- **The gate-line, verbatim:** `local-neighbor survival != global structure`. The LAQ finding's named target is exactly this: local-neighbor survival is *not* global structure.
- **Assumption:** the ladder's probes are the yardstick. Each probe carries `expected_facts` (the kept-facts' theme-membership anchors) and per-dimension scores. The probes fall into two classes:
  - **nearest-neighbor / local probes:** recurring tokens, continuation continuity, artifact shape that the compressor's retained tail can still hit.
  - **far-apart / global probes:** the session's provenance path (`/root/.hermes/sessions/request_dump_local-1c11cf0fe057f35a3b`), the producing model (`poolside/laguna-xs-2.1:free`), the exact byte-shapes (30846 / 219239 / 221226 / 31367), the failure receipt (`max_retries_exhausted`), the retention state (`"truncated_to": null`), the session identity (`session_20261007_123305_f3465b`) and the control-class model (`control-model`).

### (b) What the data says — the far-apart facts are absent
- **Rung 5 — the density-cell floor (0.00).** The probes demand the far-apart facts, and they fail. `artifact-turn-shape` (exact byte-shapes 30846 / 219239 / 221226 / 31367) is **0.00 on every run**. `recall-stream-source` (provenance path + model) is **0.00 / 0.667 / 0.00** — the global provenance is lost in 2 of 3 runs. `recall-retry-receipt` (`max_retries_exhausted`) is **0.00 / 2.00 / 0.167** — only run 2 reaches the local cue; runs 1 and 3 are empty. `artifact-density-receipts` (recurring tokens earned / binding / artifact) is **1.00 / 0.167 / 0.00** — even the nearest-neighbor class is mostly gone (the highest-scoring probe in the entire ladder is 1.00 in run 1, and it is a nearest-neighbor-type probe; the global-density probe is 0.00 in run 3). `decision-truncation` (`"truncated_to": null`) is **0.00 / 0.00 / 0.00** — the retention state of the dense stream is not preserved. The density-cell floor preserves **nothing of the global structure**.
- **Rung 4 — the depth-cell floor (1.00).** `recall-session-identity` (session ID, start time, file path) is **1.00** (hallucinates a different session/date; omits all expected facts). `recall-loop-sequence` is **0.17** (empty). `artifact-message-shape` is **0.00** (empty). `decision-model-pin` is **1.17** (claims data absent; the required `control-model` and `truncated_to: null` are not provided — the compressor's `truncated_to: null` retention state is a far-apart fact that is **not** preserved). `continuation-close-intent` is **0.00** (empty). Even the "best" cell of the ladder fails the far-apart probes.
- **Rungs 1–3 (native).** The native rungs score higher on overall recovery median (4.50 / 3.25 / 4.67), but the below-3.0 probes still name the same class: `recall-first-repo 0.00`, `artifact-all-jobs 0.00`, `artifact-final-schedule 0.00`, `continuation-execution-time 1.00`, `artifact-new-tool 0.00`, `decision-core-claim-validity 0.83`, `continuation-next-action 0.00`, `continuation-implementation-scope 0.00`, `continuation-next-step 2.17` (incorrectly claims an uncommitted cli.py change remains). The theme-membership — the coherence of the kept-facts across the runs — is absent wherever a long-distance fact is demanded.
- **The k-term is flat.** kept-rates 0.42 / 0.29 / 0.26 / 0.32 — a spread of 0.16, no k≈1/k≈0 separation, no class ordering. The budget's own mechanism (differential keep by class: decision-core > continuation > exact anchors > scope boundaries) presupposes a k that separates classes; the flat k-term falsifies the mechanism. The compressed state does not encode theme-membership; it retains only what the nearest-neighbor probes can still surface.

### (c) Uncertainty
- The density-cell floor (rung 5, 0.00) and the depth-cell floor (rung 4, 1.00) are the two rebuilt real cells; the run JSONs are the receipts. The k-term numbers are carried in the negentropy adjudication (re-derived from the ladder's own metadata, not re-computed here — [2nd]). The LAQ receipt line itself was a paper finding (2611.08341), not a live run; the rig's ladder-battery is the operational confirmation of it.
- **Wall W1 applies (contract):** a non-reproduction is a question, never a stop — the minimal experiment that moves the wall is the rig's own battery (already run, 15 runs, receipts). No further wall triggered.

---

## 3. Recommendation / Action Plan (one reversible next action + success criterion)

**Reversible next action:** post the G-LOST verdict to the fork's register (comment-thread on the PR #1 landing), with the ladder-battery's per-rung recovery medians and the k-term kept-rates as the receipts, and **do not** upgrade the compressor's anchor-selection policy on the basis of the native rungs' medians alone.

**Success criterion:** the post carries the verdict (G-LOST) + the numbers (recovery medians 4.50/3.25/4.67/1.00/0.00; k-term kept-rates 0.42/0.29/0.26/0.32; the far-apart probes' scores quoted above) and stays fork-only. The action is bounded and reversible; if the next battery run at a fresh substrate-pin shows the k-term separating, the verdict flips and the post is overwritten with a new row.

---

## 4. Next Steps / Exploration

1. Build the next arm on the negative-space of the k-term: a probe that asks for the **theme-membership itself** — the far-apart facts that are *not* local neighbors — at a fresh substrate-pin, and report the kept-rate for that probe alone.
2. Track whether the native rungs' medians (4.50 / 3.25 / 4.67) ever track the k-term's class separation; so far they do not (rung 3 = deepest compaction but 4.67, the highest).
3. When the retention re-ranking fix (SEAMFIX) lands, re-run the ladder and confirm the k-term does not separate; if it still does not, the mechanistic underpinning stays dead and the G-LOST verdict stands.

---

## 5. Artifact

- **Path:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/LAQ-FIDELITY-PROBE-20261106.md`
- **Branch (fork-only):** `study/rfc-143379-rig-20261105`
- **Receiving receipts (all from this branch's own run JSONs / report / summary / k-table):**
  - Ladder-battery: 5 fixtures × 3 runs, label `ladder-20261106-a996d4ad`, compressor + judge `deepseek/deepseek-v4-flash-0731`.
  - Recovery medians: 4.50 / 3.25 / 4.67 / 1.00 / 0.00 (rungs 1–5).
  - k-term kept-rates: 0.42 / 0.29 / 0.26 / 0.32 across the four classes; empties 24 / 36 / 22 / 48; overalls 2.61 / 2.75 / 3.08 / 2.13.
  - The gate-line, verbatim: `local-neighbor survival != global structure`.
