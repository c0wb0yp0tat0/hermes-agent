#!/usr/bin/env bash
# base-health-probe.sh — dispatch-time base health gate (the fix-and-prevent treatment, user 10-15)
# Launch-tests each proven free base BEFORE a fan-out dispatches onto it, so a saturated base
# is routed around, never dispatched onto. The 3h S5 stall was the cost of NOT having this.
#
# Usage:
#   base-health-probe.sh              # probe the whole proven pool, print healthy/saturated
#   base-health-probe.sh <model-id>   # probe one base
# Exit 0 if ALL probed bases are healthy; 1 if any is saturated/dead (caller routes around it).
#
# The proven pool (provider-prefixed — bare names crash workers):
POOL=(
  "stealth/missingno"
  "poolside/laguna-s-2.1:free"
  "poolside/laguna-xs-2.1:free"
  "meituan/longcat-2.5-preview:free"
  "stepfun/step-5-preview:free"
  "upstage/solar-mini4:free"
  "deepseek/deepseek-v4-flash-0731"
)

# CORRECTED 2026-11-06 08:5x: the old probe used `hermes chat -q "Reply with exactly: OK" -m "$model"`,
# which triggers hermes' fallback-provider chain on a 404 — the probe then saw an "OK" from
# ANOTHER model and reported the DEAD pin HEALTHY. The lanes (copycat-harness) call the inference
# endpoint DIRECTLY, so the probe must hit the same endpoint and verify the RESPONDING MODEL matches
# the requested pin. A 404 is now reported honestly as DEAD (the laguna/longcat/step-5 crash-class).
probe() {
  local model="$1"
  local out
  out=$(timeout 90 python3 - "$model" <<'PYEOF'
import json, sys, urllib.request
model = sys.argv[1]
try:
    a = json.load(open("/root/.hermes/auth.json"))
    n = (a.get("providers") or {}).get("nous", {})
    k = ""
    for c in ("agent_key", "access_token"):
        if n.get(c):
            k = n[c]
            break
except Exception:
    k = ""
if not k:
    print("NO-KEY"); sys.exit(2)
body = json.dumps({"model": model, "messages": [{"role": "user", "content": "Reply with exactly: OK"}], "max_tokens": 4}).encode()
req = urllib.request.Request("https://inference-api.nousresearch.com/v1/chat/completions", data=body,
                             headers={"Content-Type": "application/json", "Authorization": "Bearer %s" % k})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode())
    ans = ((d.get("choices") or [{}])[0].get("message") or {}).get("content", "")
    got = (d.get("model") or "")
    print("OK %s %s" % (got.split("/")[-1].split(":")[0], ans.strip()[:20]))
except urllib.error.HTTPError as e:
    print("HTTP %s" % e.code); sys.exit(1)
except Exception as e:
    print("ERR %s" % type(e).__name__); sys.exit(1)
PYEOF
  )
  local rc=$?
  if [ $rc -eq 0 ] && echo "$out" | grep -q "^OK"; then
    echo "HEALTHY    $model   (answered: $(echo "$out" | cut -c4-60))"
    return 0
  else
    echo "DEAD       $model   ($(echo "$out" | tail -1 | cut -c1-60))"
    return 1
  fi
}

if [ $# -ge 1 ]; then
  probe "$1"
  exit $?
fi

all_healthy=0
for m in "${POOL[@]}"; do
  probe "$m" || all_healthy=1
done
exit $all_healthy
