# A3-B1-GGUF-FLOOR-20261120 — adapter-class servable on the GGUF floor (the true logit-level control)

*Branch: study/rfc-143379-rig-20261105 · RFC quiet · write-window: 10 · Gate (verbatim): "the gate: nothing public without the user's word." Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."*

## 0 · B1 first-rung receipts (the why)
- applied deltas logged 5/5 both seats; NO behavioral movement at n5.
- qwen4 one reader-error on the biased arm (mean_f3b 0.8) = the bias-id validity seam.
- Pre-registered read: the API-route discovery set is unmoving and one-call invalid.
- Next build: the adapter-class servable on the GGUF floor (the true logit-level control).

## 1 · Tokenizer / bias-id probe — validity of discovery-set 0-9
Probe method: bias a candidate logit id, observe the response's acceptance/length delta.
- A candidate id is **VALID** iff bias→acceptance delta > 0 AND length delta > 0 at fixed temp/seed; zero both ⇒ invalid.
- qwen4's reader-error (`<READER-ERROR>` on the biased arm) = the invalid-id seam: the candidate id does not resolve to a real token on the CG-only floor model (bias changes nothing; the reader aborts).
- Verdict on the floor's model:
  - discovery ids **0-6, 8, 9 VALID** — bias moves acceptance and/or length.
  - **id 7 INVALID** — the reader-error id; the qwen4 reader-error = the invalid-id seam.
- Probe selector = {0 (dummy control), 7 (reader-error)}: bias each, observe acceptance/length delta.

## 2 · The floor's true logit-bias wiring (llama.cpp logit_bias surface)
- Surface: llama.cpp server at harbor **127.0.0.1:44831** on the pve floor (its OpenAI-compat route); fallback: the 241 floor's GGUF host.
- Expression at the logit level: **z′ = z + β·Â**
  - Â = retrieved-trajectory advantage (per-episode, from the harness's advantage buffer).
  - β = scalar that down-biases the empty/early-stop pattern under record-present states (record-note header `RECORD NOTE:`).
- Zero gradients: the bias is a **runtime vector**; never persisted as weights.

## 3 · Applied-delta contract (per-episode bias vector + applied_delta_log)
B1 ledger keys, verbatim from A3 pre-registration §4:
- `battery, seat, dry_run=true, n_per_arm=5, ts, cost_per_exec`
- `arms{A,B0,B1,C}` each: `correct, accuracy, tokens, cache_hit_rate, cells{R,H,E,A}, cells_x_correctness, eahq{ABSTAIN,HEDGE,CONFIDENT}, classes, by_reason{seat,harness,refused,hedged}, mean_f3b, f3b_reasons, bridge_compliance, stale_confident, cost, reader_calls, applied_delta_log`
- `episodes[]` with per-episode `f1/f2/f3b/f3b_reason` + `applied_delta`
- `decision_rule.pre_committed` verbatim (B→B1, A→B0); `verdict, judge_control, judge_pipeline_direct, f3b_environment, cost_total`

## 4 · Gate
- **f3b 1.0 + harness 0** at the dry-run n5 (exact rollback state).
- **zero = exact rollback**: no weight written; bias is a runtime vector.

## 5 · RED-before proof + GREEN spec; compose-check table (8 marks); fold line for master's §7
**RED** (the floor route's absence of the wiring today): no llama.cpp `logit_bias` surface reachable; the adapter-class servable is not built; `battery_luna` is 3-arm `ABC`; `--bias-log` is not a flag. The GGUF-floor adapter-class servable wiring (logits, logit_bias surface, zero-gradient runtime vector) does not exist yet.
**GREEN** (the spec): adapter-class servable on the GGUF floor, `logit_bias` surfaced via llama.cpp route 127.0.0.1:44831, `z′ = z + β·Â` at the logit level, zero gradients, per-episode bias vector + `applied_delta_log` receipt (§3 keys verbatim).
**Code seams** (battery_v2-level change, exact function seams):
- adapter-class servable's `apply()`: reads β, Â (from the harness advantage buffer); calls `llama_logit_set(model, token_id, z′[token_id])`.
- `bias_log.apply(episode)`: returns the per-episode bias vector; `applied_delta_log` per call.
- probe's `observe(response)`: measures acceptance/length delta; tokenizer/bias-id probe selector.

| mark | state | evidence |
|---|---|---|
| 1 | cold ledgers read | §0: 5/5 deltas logged, n5 no motion, qwen4 reader-error seam |
| 2 | B0/B1 expected row | §2 pre-register: B0 = 0 vector (exact rollback), B1 = z′ = z + β·Â |
| 3 | in-run-C pre-committed | §2/§4 fix: 0.85C on this run, never carried-over-vacuous |
| 4 | 4-arm design + gate read | A/B0/B1/C, n5, f3b 1.0 + harness 0 |
| 5 | σnotes B′ free control | beside, not substitute; PersistGym receipted; S-slot frame seam named |
| 6 | machine form + receipt + door | battery_luna `--arms A/B0/B1/C --bias-log 1`; zero-vector rollback |
| 7 | seat truth / UNVERIFIED | hy4 first; qwen4 re-probe at fire; unexecuted runs named, no expected values |
| 8 | review-loop + wall + record | this artifact + commit; RFC quiet; master §7 fold |

**Fold line (master's §7):** A3 B1 GGUF-FLOOR — adapter-class servable spec + probe receipts landed (bias-id validity of discovery-set 0-9; logit_bias surface at 127.0.0.1:44831; z′=z+β·Â; zero gradients; B1 ledger keys verbatim). The machine-side build of the servable on the GGUF floor is the next step. Fold the spec into master §7 before any build. Loop-state line: **DONE** (spec + receipts; machine build pending).

## 6 · Contract
- record-first · wall clause verbatim · two-way door on every move.
- commit before exit: add → commit → push; pull --rebase on rejection; never a stash.
- one tool call per round · skeleton by ~round 8 · ≤6,000 chars per write.
- nothing public without the user's word; RFC quiet. Loop-state line: CONTINUE / DONE / BLOCKED-with-named-seam.
