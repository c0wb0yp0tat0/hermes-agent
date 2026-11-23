# ACT2-SEAT-PROBE-20261123 — the per-fire seat liveness + content-bearing probe (Act-2)

*Seat: `meituan/longcat-2.5:free` — the mechanical-class seat, host-matched per the fleet-doctrine. **Dispatch contract VERIFIED at probe #1: the config's `delegation.model` == `meituan/longcat-2.5:free` == the brief's seat, and probe #1's responding `model` field IS `meituan/longcat-2.5:free` (PIN-READ-BACK VERIFIED).** Branch `study/rfc-143379-rig-20261105`. Contract: `plan/tank/REVISED-STAGE-PLAN-20261123.md` §2.1 (AM-C1 + AM-C2) + §3 act-2 + `plan/SEAT-REGISTRY-20261123.md` (the CURRENT register governs; `SEAT-REGISTRY-20261122.md` read for continuity — byte-identical, 1712 B each, no drift). Nothing public; RFC #143379 / #5320 / #157065 QUIET; no installs; never push; no `checkout --` / `stash` / `rm -rf`; writes only under `studies/rfc-143379-rig/`; local config left AS FOUND.*

## Armament / name-and-refuse (the skill-dump doctrine — the FULL stack dumped)

- **ARMED — used, each named with WHY:**
  - **think-tank** — the spine, and this is the verdict's form: classify (each seat's evidence class) → choose (the probe's form) → probe (the live fire) → evaluate (the verdict's class) → adopt-or-park (the pivot ledger) → standardize (the receipt's rows) → verify (the runner/registry read-back).
  - **agent-work-review** — the verdict's consistency: every seat row re-derived from the raw HTTP status + JSON bytes, never from the registry's prose; the decoy-guard class hunted (a 200 is not a content pass; a 404 is not a freeze; an echo is not an answer).
  - **investigation-documentation** — the receipts' form: raw question-sha / responding-model / PIN-echo / `content_head` / `reasoning_tokens` / `max_tokens`, seams named, the wall clause as a QUESTION with receipts.
  - **defect-forensics** — the evidence classes named with receipts: **VOID-CLASS** (hy4's 200-with-null-content) · **transport-void** (stepfun's 429) · **DEAD** (qwen's 404 free-period-ended) · **WORKABLE** · **PAID-OK**.
- **REFUSED — considered, not loaded, each named with WHY:** the creative / media / design / ascii / video families (no artifact-making load in a mechanical probe) · serving-llms-vllm / llama-cpp / local-llm-serving / local-llm-studio-headless (the local floor is PROBED, never served or changed — no install, no config) · evaluating-llms-harness / aces-harness-probes (no benchmark run; this is one content-gate fire per seat, not a harness battery) · codex / claude-code / opencode (no coding leg) · github / github-* (no PR/issue write; the commit is local) · web-storm / grounded-citations / arxiv / ddg-cli-search / web-search-plus (LOCAL receipts only — no field search) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops / hermes-update-preflight (no config/gateway/update change) · blind-agent-panels / supervisor-delegation / think-tank-feedback (no consensus fan-out — a single-seat mechanical probe) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · safe-file-editing (no source edits) · computer-use / browser-harness-sop (no UI) · the note-taking / email / maps / polymarket / x-surface families (no load).

## §1 The probe's method (the act-2 clause's form)

- **Channels (the fleet's EXISTING channels only, never invented access):** the flagship/keyless route `https://inference-api.nousresearch.com/v1/chat/completions` (Bearer = `auth.json`'s `providers.nous.agent_key`); the local floor `http://127.0.0.1:44831/v1/chat/completions` (llama-server; the GGUF path as the model id).
- **One shot per seat; a 429/404 is the seat's OWN transport receipt, recorded, never a retry loop.** A drained pin is never re-fired in the same window (AM-C1).
- **The real question** (content-bearing budget `max_tokens = 512`), per-seat PIN: *"You are a probe target. Reply with exactly this token on the first line: {PIN} Then, in one sentence, state what the number 143379 is best known as (an RFC number, a study id, or something else). Keep it under 40 words."*
- **The content-gate's caveat, quoted verbatim (AM-C2):** *"the probe's positive-token echo establishes liveness only. Where a probe's response enters a landing's evidence as content (any seat-generated answer, number, or evaluator row), the probe must ALSO carry the content-gate: a real question at a content-bearing budget with `content_head` + `reasoning_tokens` + `max_tokens` receipted. **A 200-with-emptiness or an echo-only response is liveness, NOT content; it is labeled VOID for any content claim.**"*
- **PIN read-back:** the response's `model` field == the requested pin (the dispatch contract's check) PLUS the in-content PIN echo.

## §2 The seats' rows

| # | seat (pin) | probe-http | content-bearing | verdict | receipts |
|---|---|---|---|---|---|
| 1 | `meituan/longcat-2.5:free` | **200** | **yes** | **WORKABLE** | responding `meituan/longcat-2.5:free`; PIN-70FABE99E3 echoed; `content_len` 112; completion 39; finish `stop`; qsha `b1a243622a1804b8`; 3.1s |
| 2 | `tencent/hy4-flash:free` | **200** | **no** | **VOID-CLASS** | responding `tencent/hy4-flash:free`; `content = null`; finish `length`; completion 512; reasoning 512; qsha `03f9997bb9a6282d`; 6.4s |
| 3 | `upstage/solar-mini4:free` | **200** | **yes** | **WORKABLE** | responding `upstage/solar-mini4:free`; PIN-8D294DF352 echoed; `content_len` 182; completion 46; reasoning 0; finish `stop`; qsha `f60ae7515d1cc369`; 0.9s |
| 4 | `stepfun/step-3.7-flash:free` | **429** | no | **VOID-CLASS (transport-void)** | fair-share rate limit; `retry_after` 1177s; qsha `d571d79e9dc4267e`; 0.3s |
| 5 | `qwen/qwen4-max:free` | **404** | no | **DEAD** | "This model's free period has ended. To continue using Qwen4 Max, switch to 'qwen/qwen4-max'."; qsha `e26d30b94262d1cf`; 0.2s |
| 6 | `openai/gpt-6-luna` (paid) | **200** | **yes** | **PAID-OK** | responding `openai/gpt-6-luna`; PIN-FBDDD151ED echoed; `content_len` 122; completion 361; reasoning 325; finish `stop`; qsha `e8da3f0f3c34cc80`; 4.4s |
| 7 | local darkhorse (GGUF @44831) | **200** | **yes (partial)** | **WORKABLE** | responding == requested GGUF path; `content_len` 1694; finish `length`; completion 512; PIN echoed inside the `<think>` block; 103.5s; host-matched tasking only |

**The per-fire re-probe (the law's own check):** longcat fired a SECOND time in the full sweep — **200**, PIN-9B2A385332 echoed, `content_len` 170, completion 49, finish `stop`, qsha `55568b77d097f6e9` — the seat is live and content-bearing at both fires, not a one-shot.

**The classes, named with receipts:**
- **VOID-CLASS (content)** — hy4: HTTP 200, `content = null`, `finish = length`, `reasoning = completion = max_tokens = 512`. Liveness only; **VOID for any content claim** (AM-C2's exact class).
- **VOID-CLASS (transport)** — stepfun: HTTP 429, the model's own fair-share limit, `retry_after` 1177s. Distinct from a content void; never re-fired in this window.
- **DEAD** — qwen4-max: HTTP 404, the free period ended (the 404's re-check CONFIRMED, not a transient). The paid form `qwen/qwen4-max` is named by the endpoint itself.
- **WORKABLE** — longcat, solar, local darkhorse. **PAID-OK** — luna.

## §3 The runners' liveness (the walk-fleet's probe-form)

| alias | channel | os | machine | walk | API |
|---|---|---|---|---|---|
| p0tat0 | c0wb0y@100.98.69.7 | Linux | c0wb0yp0tat0 (241) | **OK** | online · busy=false |
| c0wb0y | c0wb0y@100.70.143.25 | Windows | DESKTOP-8R44VEP (241) | **OK** | online · busy=false |
| pve1 | (local) | Linux | pve-1 (THIS host) | — | online · busy=false |

**Walked actual: installed 2 / failed 0.** Registry presence: `plan/SEAT-REGISTRY-20261123.md` + `plan/SEAT-REGISTRY-20261122.md` both present, byte-identical (continuity clean; the current register governs). The heartbeat re-verified the registry's rows rather than assuming them.

## §4 The ledgered-pivot ledger (AM-C1)

*Lane roles per AM-C1: lane-BA `meituan/longcat-2.5:free` @ `p0tat0` · lane-AA `stepfun/step-3.7-flash:free` @ `c0wb0y` · lane-CA `tencent/hy4-flash:free` @ `cloud` · the AoA's fourth base.*

| seat | state this fire | lane role | ledgered pivot candidate | base-diversity after pivot |
|---|---|---|---|---|
| `stepfun/step-3.7-flash:free` | 429 drained (transport-void) | lane-AA @ c0wb0y | `upstage/solar-mini4:free` (distinct base; keeps the support role) | {solar, hy4, longcat} — ≥2 distinct ✓ |
| `tencent/hy4-flash:free` | 200 liveness / content-void | lane-CA @ cloud | `upstage/solar-mini4:free` or `openai/gpt-6-luna` for a CONTENT-bearing fire | ≥2 distinct ✓ (luna is a distinct base) |
| `qwen/qwen4-max:free` | 404 DEAD (free period ended) | the flagship's free window | the paid `qwen/qwen4-max` (if authorized) else hy4 (liveness) / solar / longcat | ≥2 distinct ✓ |
| local darkhorse | 200 / content present (reasoning-exhaustion caveat) | host-matched tasking only | n/a — never a remote lane's pivot | n/a |

**Diversity re-verified after EVERY pivot (AM-C1):** the current content-bearing set {longcat, solar, luna} = 3 distinct bases; any single-seat pivot leaves ≥2. A pivot that collapses diversity is a named constraint, never a silent pass. The one-lane-per-seat law is honored: no doubled-ticketed seat (a pivot onto longcat would double lane-BA's pin — refused as the stepfun pivot for that reason).

## §5 The verdict

- **The live-matrix:** **WORKABLE** = `meituan/longcat-2.5:free` · `upstage/solar-mini4:free` · the local darkhorse (GGUF @44831, host-matched). **PAID-OK** = `openai/gpt-6-luna`. **VOID-CLASS** = `tencent/hy4-flash:free` (content; liveness-only) · `stepfun/step-3.7-flash:free` (transport; 429). **DEAD** = `qwen/qwen4-max:free` (404, free period ended).
- **Act-3's readiness (runner/registry):** **READY** — walked actual 2/0 + registry presence verified + heartbeat rows re-verified (all three runners online, busy=false).
- **Act-4's battery-window candidates (the content-bearing seats for the B2 fire):** **`meituan/longcat-2.5:free` · `upstage/solar-mini4:free` · `openai/gpt-6-luna`** — three distinct, PIN-read-back-verified, content-bearing bases (the fan's ≥2-diversity gate satisfied with margin). The local darkhorse is a host-matched candidate carrying the reasoning-exhaustion caveat (`finish = length` at 512, content = the `<think>` block). **hy4 / stepfun / qwen are NOT content-bearing candidates** (VOID-CLASS / DEAD).
- **Act-5's fan:** the three distinct bases {longcat, solar, luna} are all content-bearing and PIN-read-back verified — the parallel fan's base-diversity gate is satisfiable now; the fan still fires only after acts 2–3 pass (this receipt IS act-2's).

## §6 Emission contract + hard lines

This file was written on disk FIRST with the probes' raw receipts inside (§2 + the appendix), then committed as `kanban-pilot` with **only this path staged**, on the current HEAD re-checked at commit, never pushed; the master's append-only; the plan, sealed artifacts, crons, anchors, and sibling plates left AS FOUND; local config left AS FOUND. A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.

## Appendix — the raw probe receipts (verbatim JSON rows)

```json
{"requested_model":"meituan/longcat-2.5:free","pin":"PIN-70FABE99E3","max_tokens":512,"question_sha":"b1a243622a1804b8","http":200,"dt":3.1,"responding_model":"meituan/longcat-2.5:free","content_head":"PIN-70FABE99E3\n143379 is best known as the study ID for a clinical trial or rese","content_len":112,"finish_reason":"stop","prompt_tokens":79,"completion_tokens":39,"reasoning_tokens":null,"pin_echo_in_content":true}
{"requested_model":"meituan/longcat-2.5:free","pin":"PIN-9B2A385332","max_tokens":512,"question_sha":"55568b77d097f6e9","http":200,"dt":3.7,"responding_model":"meituan/longcat-2.5:free","content_head":"PIN-9B2A385332\n143379 is best known as the RFC number for \"An Extension to HTTP/","content_len":170,"finish_reason":"stop","prompt_tokens":80,"completion_tokens":49,"reasoning_tokens":null,"pin_echo_in_content":true}
{"requested_model":"tencent/hy4-flash:free","pin":"PIN-7D81C26B02","max_tokens":512,"question_sha":"03f9997bb9a6282d","http":200,"dt":6.4,"responding_model":"tencent/hy4-flash:free","content":null,"content_head":"","content_len":0,"finish_reason":"length","prompt_tokens":83,"completion_tokens":512,"reasoning_tokens":512,"pin_echo_in_content":false,"reasoning_content_head":"We need answer user. Need answer final only. User asks: \"You"}
{"requested_model":"upstage/solar-mini4:free","pin":"PIN-8D294DF352","max_tokens":512,"question_sha":"f60ae7515d1cc369","http":200,"dt":0.9,"responding_model":"upstage/solar-mini4:free","content_head":"PIN-8D294DF352 The number 143379 does not correspond to a widely recognized RFC ","content_len":182,"finish_reason":"stop","prompt_tokens":121,"completion_tokens":46,"reasoning_tokens":0,"pin_echo_in_content":true}
{"requested_model":"stepfun/step-3.7-flash:free","pin":"PIN-3C77D1B19E","max_tokens":512,"question_sha":"d571d79e9dc4267e","http":429,"http_body":"{\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand — retry after the indicated delay, or try an alternate model.\",\"reason\":\"rate_limited\",\"retry_after\":1177,\"alternates\":[\"~google/gemini-flash-latest\",\"meta/muse-spark-1.2\",\"moonshotai/kimi-k2.7-co","dt":0.3,"responding_model":null,"content_len":0}
{"requested_model":"qwen/qwen4-max:free","pin":"PIN-686AB3AD0A","max_tokens":512,"question_sha":"e26d30b94262d1cf","http":404,"http_body":"{\"status\":404,\"message\":\"This model's free period has ended. To continue using Qwen4 Max, switch to 'qwen/qwen4-max'.\"}","dt":0.2,"responding_model":null,"content_len":0}
{"requested_model":"openai/gpt-6-luna","pin":"PIN-FBDDD151ED","max_tokens":512,"question_sha":"e8da3f0f3c34cc80","http":200,"dt":4.4,"responding_model":"openai/gpt-6-luna","content_head":"PIN-FBDDD151ED\n143379 is best known as something else; it is not widely recogniz","content_len":122,"finish_reason":"stop","prompt_tokens":65,"completion_tokens":361,"reasoning_tokens":325,"pin_echo_in_content":true}
{"requested_model":"/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf","pin":"PIN-0949C8F47E","max_tokens":512,"question_sha":"2fdfc770a80d9924","http":200,"dt":103.5,"responding_model":"/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf","content_head":"<think>\nThinking Process:\n\n1.  **Analyze the Request:**\n    *   **Role:** Probe ","content_len":1694,"finish_reason":"length","completion_tokens":512,"reasoning_tokens":null,"pin_echo_in_content":true}
```

*The local floor's first fire (a model-id prefix mismatch) returned a 90s timeout — recorded as a probe-harness seam, not a seat verdict; the exact-id re-fire above is the seat's receipt. Facimus semper — the failures are findings.*
