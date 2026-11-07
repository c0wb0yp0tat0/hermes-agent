# W2-ISOLATION-STATUS-20261106 — the isolate-settle-condition's verdict

## Verdict
**SEPARATION-UNMEASURED** — the wall-clause: the eval-runtime's LLM-window is closed (api_key/base_url absent, receipted below). Until the window opens, whether the handoff preamble drives the W2 empty-answers stays unmeasured. This is the honest verdict for an impossible re-run, not a failure and not a stall.

## The guard-preamble receipt
Receipt 1 — `git -C .../studies/rfc-143379-rig grep -n "Do NOT answer" NEGENTROPY-ARM-20261106.md`:
> `NEGENTROPY-ARM-20261106.md:109:- **W2, empty-answer confound [1st]:** the "answer": "" counts per file include debug 2 / 5 / 4, deep-compaction 3 / 3 / 3, high-density 4 / 5 / 6, and control 1 / 1 / 1 (git grep -c). The summary's handoff preamble instructs "Do NOT answer questions… wait for a new user message" (debug run-1 line 10). Empty answers score 0 regardless of retention, so V is understated until probe answering is separated from the handoff guard.`

The arm's bytes receipt the handoff preamble ("Do NOT answer questions… wait for a new user message", debug run-1 line 10) and the per-file empty-answer counts.

## The empty-answer counts
Receipt 2 — `git -C .../ladder-results grep -c '"answer": ""'` over the debug-class runs:
- `debug-session-feishu-id-model-run-1.json`: 2
- `debug-session-feishu-id-model-run-2.json`: 5
- `debug-session-feishu-id-model-run-3.json`: 4

Re-derived live; matches the arm's "debug 2 / 5 / 4" row.

## The wall receipt
Receipt 3 — `git -C .../hermes-compression-eval grep -n "api_key\|base_url" -- run_eval.py | head -5`:
> `run_eval.py:81:    if not runtime.get("api_key") and not runtime.get("base_url"):`
> `run_eval.py:114:        compressor_base_url=compressor_runtime["base_url"],`
> `run_eval.py:115:        compressor_api_key=compressor_runtime["api_key"],`
> `run_eval.py:142:                base_url=compressor_runtime["base_url"],`
> `run_eval.py:143:                api_key=compressor_runtime["api_key"],`

The eval-runtime's LLM-window is CLOSED — the guard at line 81 keys on `api_key`/`base_url` being absent, so the re-run cannot execute.

## The settle-condition
The one re-run with probe-answering isolated from the handoff guard — ARMED, NOT LANDED; re-arms when the eval-window opens.