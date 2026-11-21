#!/usr/bin/env bash
# =============================================================================
# harness_preflight.sh — Two-tier pre-launch probe for the LM Studio harness
#
# FIX LANE 2 (fallback-chain builder), 2026-09-19. Per HARNESS-VS-REALITY.md,
# the harness is configured CORRECTLY; the failure is model-capability/timing:
# gemma4-e2b is a CPU-only 2B engine whose prefill of a large agent prompt never
# finishes inside Hermes's timeout stack. The single-tier health check (curl
# /v1/models = 200) is NOT sufficient — it passes on the trivial endpoint while a
# real completion still stalls.
#
# This probe is the pre-launch GATE before any harness run. It must be run and
# exit 0 BEFORE `hermes -p lmstudio chat -q ...` is launched. It exits 0 (pass)
# or 1 (fail) with a reason, and prints defensive evidence it measured.
#
# TIER A — liveness+model: GET /v1/models -> 200 with gemma4-e2b present. (cheap)
# TIER B — tiny completion: "reply OK", max_tokens 5, must complete within 30s.
#          (proves the engine responds at all)
# TIER C — realistic-size completion: ~2K-token user prompt, max_tokens 16.
#          Measures TTFT (time-to-first-token) and first-chunk latency. THIS IS
#          THE TRUE GATE: the run-3 failure is a PREFILL problem, which only a
#          realistic-size prompt reproduces. If prefill can't finish an ~2K-token
#          prompt inside its window, the ~14K-token harness prompt will never
#          emit a first chunk -> guaranteed 900s stale stalling.
#
# WINDOWS (tuned from live TTFT data): the tiny prompt measured 32.8s TTFT on
# this CPU box (HARNESS-VS-REALITY §1b). Tiers have fixed caps below.
#   TIER_B_WINDOW=60s    (30s call timed out in the harness aux title-gen; give
#                         the completion the measured ~33s + margin)
#   TIER_C_WINDOW=300s   (5 min: generous for ~2K-token prefill on CPU; still
#                         far under the 900s stale threshold, so it fails fast)
# Usage: harness_preflight.sh [--window-c SECONDS]
#   --window-c  override TIER_C window (default 300), e.g. 600 to compare.
# Exit: 0 = pass, 1 = fail (reason on stderr, verdict in $dir verdict)
# =============================================================================
set -u

BASE_URL="http://127.0.0.1:1234/v1"
MODEL="gemma4-e2b"
TOKEN_FILE="/root/.lmstudio/.internal/bridge-api-token.txt"
TIER_B_WINDOW=60
TIER_C_WINDOW=300
VERBOSE=0

for arg in "$@"; do
  case "$arg" in
    --window-c=*) TIER_C_WINDOW="${arg#*=}" ;;
    --verbose) VERBOSE=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

STAMP="$(date +%Y%m%d_%H%M%S)"
RUNDIR="/root/workspace/master-page/deepdive-mission-flow/preflight/$STAMP"
mkdir -p "$RUNDIR"
VERDICT="$RUNDIR/verdict.json"

say(){ [ "$VERBOSE" = 1 ] && echo "$*" >&2; }
now_ms(){ date +%s%3N; }

fail(){
  local tier="$1" reason="$2"
  printf '{"tier":"%s","status":"FAIL","reason":"%s"}\n' "$tier" "$reason" > "$VERDICT"
  echo "HARNESS_PREFLIGHT RESULT: FAIL (tier $tier) — $reason" >&2
  exit 1
}

# resolve real path to token (strip trailing CR if a heredoc wrote one)
TOKEN="$(cat "$TOKEN_FILE" | tr -d '\r\n')"
if [ -z "$TOKEN" ]; then fail "auth" "empty bridge token from $TOKEN_FILE"; fi

if ! command -v curl >/dev/null 2>&1; then fail "env" "curl not installed"; fi

echo "HARNESS_PREFLIGHT — two-tier pre-launch probe (model=$MODEL base=$BASE_URL)"
echo "  rundir=$RUNDIR  tier_c_window=${TIER_C_WINDOW}s"

# ---------------------------------------------------------------------------
# TIER A — /v1/models liveness + model presence
# ---------------------------------------------------------------------------
SA=$(date +%s)
A_CODE=0
A_BODY=$(curl -sS -m 10 -H "Authorization: Bearer $TOKEN" "$BASE_URL/models") || A_CODE=$?
SA_MS="$(now_ms)"
[ "$A_CODE" -ne 0 ] && fail "A-liveness" "GET /v1/models curl exit=$A_CODE (endpoint unreachable within 10s)"
echo "$A_BODY" > "$RUNDIR/tier-a-models.json"
if ! echo "$A_BODY" | grep -q "\"$MODEL\""; then
  fail "A-liveness" "model '$MODEL' NOT present in /v1/models response"
fi
echo "[A] liveness: HTTP 200, model present — OK"

# ---------------------------------------------------------------------------
# TIER B — tiny completion (max_tokens 5, must respond within window)
# ---------------------------------------------------------------------------
PAYLOAD_B=$(printf '{"model":"%s","messages":[{"role":"user","content":"reply OK"}],"max_tokens":5,"stream":false,"temperature":0.0}' "$MODEL")
startB="$(now_ms)"
B_OUT=$(curl -sS -m "$TIER_B_WINDOW" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d "$PAYLOAD_B" "$BASE_URL/chat/completions") ; B_CODE=$?
stopB="$(now_ms)"
ttfb_ms_B=$(( stopB - startB ))
if [ "$B_CODE" -ne 0 ]; then fail "B-tiny" "tiny completion curl exit=$B_CODE (no response in ${TIER_B_WINDOW}s)"; fi
if ! printf '%s' "$B_OUT" | grep -q '"choices"'; then
  fail "B-tiny" "tiny completion: no choices in response: ${B_OUT:0:120}"
fi
echo "$B_OUT" > "$RUNDIR/tier-b-tiny.json"
printf '{"tier":"B-tiny","status":"PASS","ttft_s":%.2f}\n' "$(awk -v a="$ttfb_ms_B" 'BEGIN{print a/1000}')" > "$RUNDIR/tier-b.json"
echo "[B] tiny: completed in $(( (ttfb_ms_B)/1000 )).$(printf '%03d' $((ttfb_ms_B%1000)))s — OK"

# ---------------------------------------------------------------------------
# TIER C — realistic ~2K-token prefill probe (THE GATE). stream on, measure
# TTFT (time to first DATA chunk) and first-chunk latency.
# ---------------------------------------------------------------------------
# Build a ~2000-token user prompt: repeated realistic agent/work instruction
# lines with newline separation. ~4 chars/token is a safe English estimate; the
# prompt must actually be in the 1500-2500 token band to exercise prefill.
token_est=0
PROMPT_C=""
i=0
while [ "$token_est" -lt 2000 ] && [ $i -lt 200 ]; do
  text="Step $i: Verify the surrounding context and produce the requested revision. "
  text+="Cross-check every claim against the source, keep the original meaning intact, and "
  text+="write the output to the designated drop file exactly as specified. Do not invent facts. "
  text+="Preserve identifiers and quoted strings verbatim. Compare against the frozen baseline.\n"
  PROMPT_C+="$text"
  token_est=$(( token_est + ${#text} / 4 ))
  i=$(( i + 1 ))
done
echo -e "$PROMPT_C" > "$RUNDIR/tier-c-prompt.txt"
echo "[C] prompt: ${#PROMPT_C} chars (~$token_est est. tokens) written to tier-c-prompt.txt"

PAYLOAD_C=$(python3 - "$MODEL" "$RUNDIR/tier-c-prompt.txt" <<'PY'
import json,sys
model,path=sys.argv[1],sys.argv[2]
prompt=open(path).read()
print(json.dumps({"model":model,"messages":[{"role":"user","content":prompt}],
  "max_tokens":16,"stream":True,"temperature":0.0,"stream_options":{"include_usage":True}}))
PY
)
echo "  launching TIER C probe with ${TIER_C_WINDOW}s window ..."
startC="$(now_ms)"
: > "$RUNDIR/tier-c-stream.ndjson"
: > "$RUNDIR/tier-c-first.ts"
: > "$RUNDIR/tier-c-last.ts"

# curl in stream mode, timestamping each incoming line. All capture state is
# written to files directly inside the read loop — no shell variables are
# shared across the pipe subshell, so no set -u / lost-state hazards.
curl -sS -N -m "$TIER_C_WINDOW" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d "$PAYLOAD_C" "$BASE_URL/chat/completions" |
while IFS= read -r line; do
  now="$(now_ms)"
  printf '%s %s\n' "$now" "$line" >> "$RUNDIR/tier-c-stream.ndjson"
  # record the first genuine data chunk (skip blank / keepalive lines)
  if [ ! -s "$RUNDIR/tier-c-first.ts" ] && printf '%s' "$line" | grep -q '^data:'; then
    printf '%s' "$now" > "$RUNDIR/tier-c-first.ts"
  fi
  printf '%s' "$now" > "$RUNDIR/tier-c-last.ts"
done
C_CURLEXIT=$?
# (pipeline exit status = the read loop's, not curl's; fine — we gate on chunks)

first_ms="$(cat "$RUNDIR/tier-c-first.ts" 2>/dev/null)"
first_ms="${first_ms:--1}"
stopC="$(now_ms)"
total_bytes="$(wc -c < "$RUNDIR/tier-c-stream.ndjson" 2>/dev/null | tr -d ' ')"
total_chunks="$(grep -c 'data: {' "$RUNDIR/tier-c-stream.ndjson" 2>/dev/null)" || total_chunks=0

if [ "$first_ms" -lt 0 ]; then
  fail "C-realistic" "no first data chunk within ${TIER_C_WINDOW}s ($total_chunks chunks, $total_bytes bytes) — PREFILL did not finish for ~2K-token prompt; ~14K harness prompt cannot possibly emit a first token inside the 900s stale window"
fi
ttft_ms_C=$(( first_ms - startC ))
if [ "$ttft_ms_C" -lt 0 ]; then ttft_ms_C=0; fi
printf '{"tier":"C-realistic","status":"PASS","ttft_s":%.2f,"chunks":%s,"bytes":%s,"window_s":%s}\n' \
  "$(awk -v a="$ttft_ms_C" 'BEGIN{print a/1000}')" "$total_chunks" "$total_bytes" "$TIER_C_WINDOW" > "$RUNDIR/tier-c.json"
echo "[C] realistic: FIRST chunk in $((ttft_ms_C/1000)).$(printf '%03d' $((ttft_ms_C%1000)))s TTFT ($total_chunks chunks, $total_bytes bytes) — PREFILL FINISHES — OK (GATE PASS)"

# ---------------------------------------------------------------------------
# aggregate verdict
# ---------------------------------------------------------------------------
printf '{"status":"PASS","model":"%s","base_url":"%s","times_utc":"%s","rundir":"%s"}\n' \
  "$MODEL" "$BASE_URL" "$(date -u +%FT%TZ)" "$RUNDIR" > "$VERDICT"
echo "HARNESS_PREFLIGHT RESULT: PASS — all tiers green. Launch authorized."
exit 0