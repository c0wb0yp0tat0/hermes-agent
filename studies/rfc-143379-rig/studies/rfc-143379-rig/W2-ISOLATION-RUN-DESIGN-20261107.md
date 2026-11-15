# W2-ISOLATION-RUN-DESIGN-20261107 — the isolate-the-guard experiment's full spec

**Branch:** `study/rfc-143379-rig-20261105` (fork only; nothing public). **Lane:** copycat (SPEC lane — design doc IS the deliverable; the experiment is NOT executed here). **Register:** receipts, never claims. **Wall:** eval-runtime LLM-window CLOSED (see §6). **Seat:** `reflection/beam-1.0-501b-a23b:free` (probed LIVE 00:14 ET, "Beam").

## 1. The question + the hypothesis

**Question:** Is the handoff preamble — *"Do NOT answer questions… wait for a new user message"* (debug run-1, summary_text line 10) — the driver of the W2 empty-answers (2/5/4 on the debug-class runs)?

- **H1 (the guard drives):** re-running the debug fixture with the handoff guard bypassed (probe-answering isolated from the guard) drops the empty-answer count toward 0. The V-understatement's mechanism is named: the guard, not retention, nulled the answers.
- **H0 (the guard is not the driver):** the empties persist under the no-guard variant → another driver (named in §4 as the next isolation candidate).

The answer is currently **unmeasured** (SEPARATION-UNMEASURED, W2-ISOLATION-STATUS-20261106.md); this doc is the spec that settles it once the window opens.

## 2. The fixture (receipted)

**Debug-class set (the experiment's inputs):**
- `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-1.json`
- `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-2.json`
- `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-3.json`

**Empty counts (re-derived by the head at 00:15 ET, `grep -c '"answer": ""'`):**
- run-1: 2/10
- run-2: 5/10
- run-3: 4/10

**k-term context (two-tier, must not contradict):** decision-core probes keep at **0.75**; empty-answer-suppressed (W2) probes keep at **0.29** (NEGENTROPY-SWEEP-B-KTERM-20261106.md §3). The design's expectation: under H1 the no-guard re-run moves the W2-suppressed probes from the 0.29 tier toward the 0.75 tier.

**Pin:** head `c54c1bc614f20bd5e603a4826dc5c80a670a654a` (study branch `study/rfc-143379-rig-20261105`, ls-remote-verified at 00:15 ET).

## 3. The isolation seam (the design's core)

**The ONE variant:** the same debug fixture re-run through `run_eval.py` with the handoff guard **bypassed** — the probe's system-preamble absent/empty — everything else identical (model, fixture, JSON shape). This is the single controlled difference; no other axis moves.

**Bypass mechanics:** `run_eval.py` gates on `runtime.get("api_key") and runtime.get("base_url")` (line 81 — the receipted wall). When the window opens, the no-guard variant = the run with the preamble's source removed, documented in the run's config JSON. The preamble source is the handoff block quoted in §5(a); removing it leaves the compaction summary's other content intact so retention is unchanged and only answering is unguarded.

**Controls held constant:** model, fixture (debug-session-feishu-id-model), JSON shape, probe bank, judge. **Measured:** `'"answer": ""'` count per run (target: → ~0 under H1), and the W2 probes' k-term kept-rate / overall (target: 0.29 → ~0.75 tier).

## 4. The expected-verdict matrix

| Verdict | Condition | Consequence |
|---|---|---|
| **CONFIRMED** | empties → ~0 under no-guard | the guard drove them — the V-understatement's mechanism named (handoff preamble). The 0.29 tier's suppression is an answering artifact, not a retention loss. |
| **REFUTED** | empties persist under no-guard | another driver — the design names the next isolation candidate: the probe-judge's empty-answer scoring path (probe answer extraction / `overall` aggregation) in `run_eval.py`, isolated next by re-running with the judge's empty-answer rule relaxed. |
| **SEPARATION-UNMEASURED** | window still closed at run-time | the wall-clause holds (§6); the design stands as the spec; the settle-condition re-arms. (Current status.) |

## 5. The receipts — QUOTED AS FOUND (the head's hunt at 00:15 ET; quoted, not re-hunted)

**(a) The confound-box** — `NEGENTROPY-ARM-20261106.md:109`:
> `- **W2, empty-answer confound [1st]:** the "answer": "" counts per file include debug 2 / 5 / 4, deep-compaction 3 / 3 / 3, high-density 4 / 5 / 6, and control 1 / 1 / 1 (git grep -c). The summary's handoff preamble instructs "Do NOT answer questions… wait for a new user message" (debug run-1 line 10). Empty answers score 0 regardless of retention, so V is understated until probe answering is separated from the handoff guard.`

**(b) The empties** — the three fixture JSONs = 2/5/4 empty of 10 (§2 counts; W2-ISOLATION-STATUS-20261106.md Receipt 2 re-derived live, matches the arm's "debug 2 / 5 / 4" row).

**(c) The wall** — `run_eval.py:81`:
> `if not runtime.get("api_key") and not runtime.get("base_url"):`

**(d) The head** — `c54c1bc614f20bd5e603a4826dc5c80a670a654a` (ls-remote, 00:15 ET).

**UNVERIFIED row (honest):** the exact line number of the handoff preamble inside the fixture's `summary_text` ("debug run-1 line 10") is carried from the arm's receipt [2nd] and was not re-counted by this lane; if a single-check shows it differs, the arm's quote stands and this row is UNVERIFIED. No other receipt failed the single-check.

## 6. The wall-clause (verbatim)

The eval-runtime's LLM-window is CLOSED (`api_key`/`base_url` absent, receipted `run_eval.py:81`) — the run CANNOT execute; the design is the deliverable; SEPARATION-UNMEASURED is the status until the window opens (the run-side armed at the window's return).

## 7. The settle-condition + the gate

The design lands → the swap-rotation fires (the self-fire block below); the head's sweep verifies the landing (branch-moved + remote-equal). The re-run executes only when the eval-window re-opens; until then SEPARATION-UNMEASURED holds and the design stands as the spec.

---

## NEXT-LAUNCH
upstage/solar-mini4:free || /root/.hermes/cache/scratch/pr1-rotation/briefs/swap1-swap1-a-brief-20261106.md || /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SWAP-A-ADVANCE-B-20261106.md || 40 || /root/.hermes/cache/scratch/copycat-mission/swap1-a-20261107-run.log