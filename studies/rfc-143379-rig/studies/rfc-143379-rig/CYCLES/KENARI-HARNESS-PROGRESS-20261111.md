# THE KENARI-HARNESS PROGRESS (2026-11-11 — the full arc, before the pivot)

The kenari-family integration's progress, documented for the successor. The operator's steer: pivot away after the FINAL7-LANE lands; this file is the knowledge that rides forward.

## THE SEAMS, IN ORDER SUCCESSIVE (each measured, named, cured)
1. **THE WRONG-PATH CLASS (the deepest root, the 404s' true cause):** HARNESS_ENDPOINT must be the FULL request-path — `https://kenari.id/v1/chat/completions` — never the bare base (`https://kenari.id/v1` POSTs to the root and the router returns `not_found`). The nous-default carries the full path, so only the kenari-rides hit it. THE DIVE's lesson: when every byte matches and the result differs, print the URL — the inline reproduction's REQ-URL revealed it.
2. **THE TOOLS-SEAM's false lean:** the early 404s suggested the tools-array was unwelcome → HARNESS_NO_TOOLS was added and the kenari-rides ran tool-less. The tools were innocent — the path was the root. The kenari route ACCEPTS the tools-array (compat-probe: "KENARI-compat: OK"). Tools-on is fine.
3. **THE MERGE-GUARD (the boundary-shape family's instance):** `_merge_adjacent_assistants` in the harness — the windowed history can split one assistant turn (content vs tool_calls) producing adjacent-assistant entries, a known compat-bug shape that providers reject as a wrongly-layer'd 404. Merge before the send; probe-passed.
4. **THE RECOVERY PARSER (the middleware's crown-piece, live):** the small-seat family (laguna observed, Nemo-class, ultra) emits tool-calls as `<tool_call>name<arg_key>k</arg_key><arg_value>v</arg_value></tool_call>` markup IN the content instead of the structured field. `_parse_prose_call` recovers it into a real tool-call, executed exactly as structured ones are. Probe-passed: the markup → a real write_file call. THE CLASS'S CLOSURE: the family's prose-calls become real executions.
5. **THE SEAT-CALIBRATION (the operator's metrics + their provider's own code):** their `hermes-kenari-provider` (cloned at /tmp/hermes-kenari-provider) names `glm-5-2` as the DEFAULT seat with a fallback roster (glm-5-2, claude-sonnet-5, gpt-5-5, deepseek-v4-pro, kimi-k2-7-code, minimax-m3) — the operator endorsed glm-5-2. The laguna-xs-2-1:free is B08-verified (HTTP-200) and now middleware-carried. The nemotron-3-ultra-550b's route is window-flaky (the provider "does not serve the model right now" — the docs' model_not_found's availability-line). Designated: glm-5-2; proven-fallback: laguna; window-flaky: ultra.

## THE KENARI-RIDES' CONTRACT (the env-set that works)
```
HARNESS_ENDPOINT="https://kenari.id/v1/chat/completions"   # the FULL path — never the bare base
HARNESS_MAX_TOKENS=512                                      # the family's tolerance
LM_API_KEY=<the KENARI_API_KEY from /root/.hermes/.env>     # kn-... format
# tools ON (HARNESS_NO_TOOLS unset) — the route accepts the array; the parser catches the prose-class
# the recovery-parser now executes the family's <tool_call>-markup as real calls
```

## THE RECEIPTS
- The compat-probes (the kenari's 200s at the full path), the spy-captures (the URL-reveal), the catalog-check (108 models; laguna/ultra present with exact IDs), their provider's own code (the glm-5-2 default, the verify_live canon: user-only messages, max_tokens 8, stream False).
- The chain's rows: 002-lessons (the tool-drop seam's root, the wrong-path class, the boundary-shape guard).

## THE PIVOT'S NOTE
The kenari-family's integration is proven-capable and documented; per the operator's steer, the fleet pivots away after FINAL7-LANE lands. The harness holds the knowledge; the seats stand ready for the future's deliberate return.
