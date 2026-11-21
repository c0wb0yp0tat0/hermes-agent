#!/usr/bin/env python3
# C37 PREAMBLE SUPPRESSION INVESTIGATION — template-level approaches
# C36 found: temp 0.0 does NOT suppress the "We need to" preamble (C32 claim debunked).
# aces-harness-probes directs: "attack preamble via template change, never sampling
# or system-message sweeps alone."
# This script tests 3 template-level approaches on the D5_a query (detached legs lesson).
# Run via: hermes cron create --deliver local --no-agent --script c37-dispatch.sh '2m' --repeat 1 --name c37-verification

import json, subprocess, time, sys
from pathlib import Path

# --- Anchored to MEMORY.md OPERATING DOCTRINE (001:43/44/45 + 002:149/156/161) ---
# MEMORY.md pointer: /root/.hermes/memories/MEMORY.md
# Chain: /root/workspace/master-page/memory-chain/ (INDEX.md → 001→010)
# Key doctrine: self-fire via session-surviving cron arm; NEVER background child.
# C24d termination: C37 measures delta vs C36; delta=0 → PARK.

API_URL = "http://127.0.0.1:44831/v1/chat/completions"
ENG_HEALTH_URL = "http://127.0.0.1:44831/health"
MODEL_ID = "deepseek-v4-pro-qwen3.5-9b-mtp"

# Read the segment for D5_a query
SEG_PATH = Path("/root/workspace/master-page/memory-chain/006-seg006.md")
seg_text = SEG_PATH.read_text()

QUERY = "Quote the detached legs lesson."

# Preamble detection — markers that indicate a visible reasoning preamble
PREAMBLE_MARKERS = ["We need to", "We are given", "Thinking Process", "Let me think", "Let me"]

def check_engine():
    """Launch-test: verify engine health before investigation runs (002:158)."""
    try:
        result = subprocess.run(["curl", "-s", "-m", "10", ENG_HEALTH_URL],
                                capture_output=True, text=True, timeout=10)
        data = json.loads(result.stdout)
        if data.get("status") == "ok":
            return True, "ok"
        return False, f"unexpected: {data}"
    except Exception as e:
        return False, str(e)

def classify_preamble(text, status):
    """Return the preamble style or 'NONE (suppressed)'. Only checks real model output."""
    if status != "ok" or not text or len(text) < 2:
        return f"N/A ({status})"
    for marker in PREAMBLE_MARKERS:
        if marker in text:
            return f"Present: '{marker}'"
    return "NONE (suppressed)"

def make_api_call(messages):
    """Call the llama-server API and return (response_text, latency, status)."""
    payload = {
        "model": MODEL_ID,
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.0,
    }
    start = time.time()
    try:
        result = subprocess.run([
            "curl", "-s", "-m", "300", API_URL,
            "-H", "Content-Type: application/json",
            "-d", json.dumps(payload)
        ], capture_output=True, text=True, timeout=300)
        latency = time.time() - start
        data = json.loads(result.stdout)
        answer = data["choices"][0]["message"]["content"].strip()
        return answer, round(latency, 1), "ok"
    except subprocess.TimeoutExpired:
        latency = time.time() - start
        return "", round(latency, 1), "timeout"
    except Exception as e:
        latency = time.time() - start
        return "", round(latency, 1), f"error: {type(e).__name__}"

# --- Verify engine health (launch-test per 002:158) ---
eng_ok, eng_status = check_engine()
print(f"Engine health at :44831: {eng_status}")
if not eng_ok:
    print("FATAL: engine not available. Aborting.")
    sys.exit(1)

# --- 3 template-level approaches ---

# Approach A: Baseline (current — SYSTEM_MSG + no-thinking template)
# Reproduces C36 to confirm preamble presence.
baseline_system = "You are a concise assistant. Answer directly without any reasoning preamble, thinking blocks, or analysis. Provide only the answer with citation."
baseline_prompt = f"""You have a memory chain. The harness retrieved the most relevant segment for your question. Retrieved segment (006-seg006.md):

---
{seg_text}
---

Question: {QUERY}
Answer from the retrieved segment only, with the filename: \"<fact> (from 006-seg006.md)\". If the fact is not in the segment, say \"NOT IN CHAIN\"."""

# Approach B: Strong inline anti-preamble instruction in the user prompt body.
# Intentionally avoids writing the literal marker phrase to prevent self-match
# in error string handling.
strong_prompt = f"""You have a memory chain. The harness retrieved the most relevant segment for your question. Retrieved segment (006-seg006.md):

---
{seg_text}
---

Question: {QUERY}

CRITICAL INSTRUCTIONS:
- Output ONLY the answer with citation. Format: \"<fact> (from 006-seg006.md)\"
- NO preamble of any kind. NO reasoning text before the answer. NO thinking blocks.
- If the fact is not in the segment, say \"NOT IN CHAIN\".

Answer:"""

# Approach C: Minimal generation prefix — segment + question + "Answer:" only
prefix_prompt = f"""{seg_text}

Question: {QUERY}
Answer:"""

# --- Run tests ---
results = []
print("=" * 70)
print("C37 PREAMBLE SUPPRESSION — TEMPLATE-LEVEL INVESTIGATION")
print(f"Params: model={MODEL_ID} @ :44831, temp=0.0, query=D5_a")
print("=" * 70)

# Test A: Baseline
print("\n[A] Baseline (SYSTEM_MSG + no-thinking template)")
answer_a, lat_a, status_a = make_api_call(
    [{"role": "system", "content": baseline_system}, {"role": "user", "content": baseline_prompt}]
)
preamble_a = classify_preamble(answer_a, status_a)
print(f"  Latency: {lat_a}s | Preamble: {preamble_a} | Status: {status_a}")
if answer_a:
    print(f"  Output: {answer_a[:200]}...")
results.append({"approach": "A_baseline", "preamble": preamble_a, "latency_s": lat_a,
                "status": status_a, "output_head": answer_a[:200] if answer_a else ""})

# Test B: Strong inline instruction
print("\n[B] Strong inline anti-preamble instruction in prompt body")
answer_b, lat_b, status_b = make_api_call(
    [{"role": "system", "content": baseline_system}, {"role": "user", "content": strong_prompt}]
)
preamble_b = classify_preamble(answer_b, status_b)
print(f"  Latency: {lat_b}s | Preamble: {preamble_b} | Status: {status_b}")
if answer_b:
    print(f"  Output: {answer_b[:200]}...")
results.append({"approach": "B_strong_inline", "preamble": preamble_b, "latency_s": lat_b,
                "status": status_b, "output_head": answer_b[:200] if answer_b else ""})

# Test C: Minimal prompt with Answer: prefix
print("\n[C] Minimal prompt (segment + question + 'Answer:' prefix)")
answer_c, lat_c, status_c = make_api_call(
    [{"role": "system", "content": baseline_system}, {"role": "user", "content": prefix_prompt}]
)
preamble_c = classify_preamble(answer_c, status_c)
print(f"  Latency: {lat_c}s | Preamble: {preamble_c} | Status: {status_c}")
if answer_c:
    print(f"  Output: {answer_c[:200]}...")
results.append({"approach": "C_minimal_prefix", "preamble": preamble_c, "latency_s": lat_c,
                "status": status_c, "output_head": answer_c[:200] if answer_c else ""})

# --- Analysis ---
suppressed = [r for r in results if r["preamble"] == "NONE (suppressed)"]
not_suppressed = [r for r in results if r["preamble"] != "NONE (suppressed)" and r["status"] == "ok"]
errored = [r for r in results if r["status"] != "ok"]

print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)
print(f"Preamble suppressed: {len(suppressed)}/3")
print(f"Preamble NOT suppressed: {len(not_suppressed)}/3")
print(f"Errors/timeouts: {len(errored)}/3")

if len(suppressed) >= 1:
    winning = ", ".join(r["approach"] for r in suppressed)
    verdict = f"Preamble suppressed by approach(es): {winning}"
    delta = "> 0 — template-level approach works"
elif len(not_suppressed) >= 1:
    verdict = ("No template-level approach suppressed the preamble; delta = 0 vs C36. "
               "The model ignores anti-preamble instructions at the generation boundary. "
               "Recommend: post-processing preamble stripping OR server template mod "
               "(inject anti-preamble instruction in generation prompt of horse-server.sh Jinja)")
    delta = "= 0"
else:
    verdict = f"All tests errored/timeouts ({[(r['approach'], r['status']) for r in errored]}); cannot determine"
    delta = "unknown"

# --- Write results ---
output = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "c36_finding": "Preamble NOT suppressed at temp 0.0 (C32 claim debunked); all 6 cells CORRECT, gate intact, latency improved, delta > 0",
    "investigation": "Template-level preamble suppression approaches on D5_a query",
    "params": {"model": MODEL_ID, "endpoint": API_URL, "temperature": 0.0},
    "engine_health": {"status": eng_status},
    "c26_chain": "C26(P4 FAIL) -> C32(FIX: preamble/system_msg) -> C35(VERIFY temp 0.1: PASS) -> C36(VERIFY temp 0.0: PREAMBLE NOT SUPPRESSED, delta>0) -> C37(THIS: template-level investigation)",
    "tests": results,
    "analysis": {
        "suppressed_count": len(suppressed),
        "not_suppressed_count": len(not_suppressed),
        "errored_count": len(errored),
        "verdict": verdict,
        "delta_vs_c36": delta
    }
}

outpath = "/root/.hermes/cache/scratch/c37-verification-results.json"
with open(outpath, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nResults written to {outpath}")
print(f"Verdict: {verdict}")
print(f"Delta vs C36: {delta}")
