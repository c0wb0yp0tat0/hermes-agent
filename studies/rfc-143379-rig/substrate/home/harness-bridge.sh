#!/usr/bin/env python3
# IMPLEMENT LANE - harness bridge script
# Query embedder -> cosine-match real chain -> route horse (:44831) or gemma (:1234) -> cite segment or NOT IN CHAIN

import json, subprocess, sys, os, time, hashlib
from pathlib import Path

QUERY = sys.argv[1] if len(sys.argv) > 1 else None
if not QUERY:
    print("Usage: $0 <query>")
    print("Exit codes: 0 = answer; 1 = no-match or usage/busy; 2 = generation unavailable")
    sys.exit(1)

CACHE_DIR = Path("/root/.hermes/cache/scratch/harness-cache")
LOCK_FILE = Path("/root/.hermes/cache/scratch/harness-bridge.lock")
LOG_FILE = Path("/root/.hermes/cache/scratch/memtest/uc-b-run.log")
MEMORY_CHAIN = Path("/root/workspace/master-page/memory-chain")
TOKEN = Path("/root/.lmstudio/.internal/bridge-api-token.txt").read_text().strip()
EMBED_URL = "http://127.0.0.1:1234/v1/embeddings"
EMBED_MODEL = "text-embedding-nomic-embed-text-v1.5"
# Cache threshold gate (single gate for grounded + absent queries, per harness
# single-threshold design):
# C25S5 fix: 0.35 -> 0.55 (was too permissive for absent-factoid queries)
# C27 Phase 5: 0.55 -> 0.60. Knee probe (24 cells, 19/24 pass) showed
# Q6-W4096 confabulated "6" at score 0.599 (above 0.58 gate). At 0.60,
# 0.599 < 0.60 catches it at the gate. Grounded minimum is Q1 at 0.608
# (no conflict). Q5 (0.548-0.557) and Q7 (0.569) also remain gate-rejected.
# Q8 reclassified as GROUNDED (fact IS in 002-lessons.md L104, not absent).
CACHE_THRESHOLD = float(os.environ.get("HARNESS_CACHE_THRESHOLD", "0.60"))

# Lock check
if LOCK_FILE.exists():
    # Stale-lock guard (2026-09-28): a crashed lane leaves the lock file
    # behind and the harness reports BUSY forever. Only treat the lock as
    # held if its PID is actually alive; otherwise clear it and proceed.
    try:
        _pid = int(LOCK_FILE.read_text().strip())
        _alive = False
        try:
            os.kill(_pid, 0)
            _alive = True
        except ProcessLookupError:
            _alive = False
        except PermissionError:
            _alive = True
    except Exception:
        _alive = False
    if _alive:
        print("BUSY")
        sys.exit(1)
    LOCK_FILE.unlink(missing_ok=True)

LOCK_FILE.write_text(str(os.getpid()))
import atexit
atexit.register(lambda: LOCK_FILE.unlink(missing_ok=True))

CACHE_DIR.mkdir(parents=True, exist_ok=True)

def embed(text):
    payload = json.dumps({"model": EMBED_MODEL, "input": text})
    result = subprocess.run([
        "curl", "-s", "-m", "30", EMBED_URL,
        "-H", f"Authorization: Bearer {TOKEN}",
        "-H", "Content-Type: application/json",
        "-d", payload
    ], capture_output=True, text=True)
    try:
        data = json.loads(result.stdout)
        return data["data"][0]["embedding"]
    except (json.JSONDecodeError, KeyError, IndexError):
        # Total outage (embedder down): fall through to the generation
        # unavailable path so the exit-2 contract holds for ALL failures,
        # not just generation failures. (Earned 2026-09-26: both endpoints
        # down crashed here with an unhandled JSONDecodeError, exit 1.)
        return None

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    norm_a = sum(x*x for x in a) ** 0.5
    norm_b = sum(x*x for x in b) ** 0.5
    return dot / (norm_a * norm_b) if norm_a * norm_b > 0 else 0

# Embed the query
query_emb = embed(QUERY)
if query_emb is None:
    print("GENERATION UNAVAILABLE")
    sys.exit(2)

# Get segment files
segments = sorted(MEMORY_CHAIN.glob("0*.md"))
if not segments:
    print("NOT IN CHAIN")
    sys.exit(1)

best_file = ""
best_score = 0.0
best_window_text = ""  # Best-matching window text for the prompt
best_window_idx = None  # Track which window index matched best

total_windows = 0  # Count total windows for position reporting

for seg in segments:
    mtime = seg.stat().st_mtime
    sha1 = hashlib.sha1(seg.read_bytes()).hexdigest()
    seg_full = seg.read_text()

    # Build sliding windows for THIS segment (covers full segment text,
    # not just [:500] head). Fixes the tail-window gap: content beyond
    # the first 500 chars (e.g. ENOSPC lessons in long segment 002) is
    # now matchable at the segment-level, not just the prompt-window.
    win_size = int(os.environ.get("HARNESS_WIN_SIZE", "4096"))
    step = win_size // 2
    if len(seg_full) <= win_size:
        windows = [seg_full]
    else:
        windows, i = [], 0
        while i < len(seg_full):
            windows.append(seg_full[i:i+win_size])
            if i + win_size >= len(seg_full):
                break
            i += step

    # Find best-matching window in this segment (unified segment + window match)
    for w_idx, w in enumerate(windows):
        total_windows += 1
        cache_key = f"{seg.name}:{mtime}:{sha1}:{win_size}:{w_idx}"
        cache_file = CACHE_DIR / f"{cache_key}.emb"

        if cache_file.exists():
            w_emb = [float(x) for x in cache_file.read_text().split(",")]
        else:
            w_emb = embed(w)
            if w_emb is not None:
                cache_file.write_text(",".join(str(x) for x in w_emb))
            else:
                continue  # embedder died mid-scan: skip this window

        s = cosine(query_emb, w_emb)
        if s > best_score:
            best_score = s
            best_file = seg.name
            best_window_text = w
            best_window_idx = total_windows - 1  # 0-indexed window position

# Check threshold
if os.environ.get("HARNESS_DEBUG"):
    # METRIC_WINDOW_POS: emit window position (env-guarded, default off for byte-identical default)
    if os.environ.get("METRIC_WINDOW_POS"):
        if best_window_idx is not None:
            print(f"DEBUG_SCORE={best_score:.6f} seg={best_file} window_{best_window_idx+1}/{total_windows}", file=sys.stderr)
        else:
            print(f"DEBUG_SCORE={best_score:.6f} seg={best_file} window=unknown", file=sys.stderr)
    else:
        print(f"DEBUG_SCORE={best_score:.6f} seg={best_file}", file=sys.stderr)
if best_score < CACHE_THRESHOLD:
    print("NOT IN CHAIN")
    sys.exit(1)

# C25 probe: block-size knob. Default 'a' = current behavior (single best window).
BLOCK_SIZE = os.environ.get("HARNESS_BLOCK_SIZE", "a")
SYSTEM_MSG = None  # C25S2: only set for 'f' (template-variant probe), empty for all production paths

if BLOCK_SIZE == "f":
    # ---- C25S2 PROBE ONLY (NOT production default): no-thinking template variant ----
    # Tests whether an explicit system instruction suppresses the reasoning preamble
    # emitted by the DeepSeek-V4-Pro model's default chat template.
    seg_text = best_window_text
    prompt = f"""You have a memory chain. The harness retrieved the most relevant segment for your question. Retrieved segment ({best_file}):

---
{seg_text}
---

Question: {QUERY}
Answer from the retrieved segment only, with the filename: "<fact> (from {best_file})". If the fact is not in the segment, say "NOT IN CHAIN"."""
    SYSTEM_MSG = "You are a concise assistant. Answer directly without any reasoning preamble, thinking blocks, or analysis. Provide only the answer with citation."

elif BLOCK_SIZE == "a":
    # ---- DEFAULT PATH (must match pre-C25 behavior exactly) ----
    # C32 FIX (2026-10-02, applied from c32-preamble-verdict.txt): the production
    # path emitted the "Thinking Process" preamble -> HONEST_REFUSAL on detached-legs
    # queries. C32 verified BS=a + system message = CORRECT (benign "We need to"
    # preamble, 33.1s). SYSTEM_MSG is the same no-thinking instruction BS=f uses.
    seg_text = best_window_text
    prompt = f"""You have a memory chain. The harness retrieved the most relevant segment for your question. Retrieved segment ({best_file}):

---
{seg_text}
---

Question: {QUERY}
Answer from the retrieved segment only, with the filename: "<fact> (from {best_file})". If the fact is not in the segment, say "NOT IN CHAIN"."""
    SYSTEM_MSG = "You are a concise assistant. Answer directly without any reasoning preamble, thinking blocks, or analysis. Provide only the answer with citation."

elif BLOCK_SIZE in ("b", "c"):
    # ---- (b)/(c) KNEE CELLS: best window + neighbor segments, (c) + INDEX ----
    # C24 confound: citation drift ("from 001" instead of "010-facts.md") was caused by
    # C24's probe_bypassing the harness and building its OWN prompt WITHOUT filenames.
    # The harness ALREADY embeds best_file in the prompt. Here we extend that to
    # every context block so the model always knows WHICH segment each fact comes from.
    best_num = int(best_file[:3])
    context_parts = []
    # Best window with explicit segment annotation
    context_parts.append(f"[Retrieved segment: {best_file}]\n{best_window_text}")
    # Neighbor segments (n-1, n+1) for cross-segment context
    for adj in [best_num - 1, best_num + 1]:
        if 1 <= adj <= 999:
            adj_prefix = f"{adj:03d}-"
            for seg in segments:
                if seg.name.startswith(adj_prefix):
                    neighbor_text = seg.read_text()[:3000]
                    context_parts.append(f"[Neighbor segment: {seg.name}]\n{neighbor_text}")
                    break
    if BLOCK_SIZE == "c":
        index_path = MEMORY_CHAIN / "INDEX.md"
        if index_path.exists():
            index_text = index_path.read_text()[:4000]
            context_parts.append(f"[INDEX]\n{index_text}")
    seg_text = "\n\n---\n".join(context_parts)
    prompt = f"""You have a memory chain. The harness retrieved the most relevant segment and additional context for your question. Each block is annotated with its source segment filename.

{seg_text}

Question: {QUERY}
Answer from the retrieved context only, citing the segment filename: "<fact> (from <segment>)". If the fact is not in the context, say "NOT IN CHAIN"."""

else:
    # Unknown value — fall back to default 'a' behavior
    seg_text = best_window_text
    prompt = f"""You have a memory chain. The harness retrieved the most relevant segment for your question. Retrieved segment ({best_file}):

---
{seg_text}
---

Question: {QUERY}
Answer from the retrieved segment only, with the filename: "<fact> (from {best_file})". If the fact is not in the segment, say "NOT IN CHAIN"."""

# Try horse first (24s avg, 5min max per guardrail)
answer = ""
model_used = "horse"

# L1: Temperature control via env var (default 0.7, no behavioral change)
# Byte-verified: temp was at hardcoded 0.7 in C25S1; now env-overrideable via HARNESS_TEMPERATURE
temperature = float(os.environ.get("HARNESS_TEMPERATURE", "0.7"))

try:
    resp = subprocess.run([
        "curl", "-s", "-m", "300", "http://127.0.0.1:44831/v1/chat/completions",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({
            "model": "deepseek-v4-pro-qwen3.5-9b-mtp",
            "messages": ([{"role": "system", "content": SYSTEM_MSG}, {"role": "user", "content": prompt}] if SYSTEM_MSG else [{"role": "user", "content": prompt}]),
            "max_tokens": 500,
            "temperature": temperature
        })
    ], capture_output=True, text=True, timeout=300)
    data = json.loads(resp.stdout)
    answer = data["choices"][0]["message"]["content"].strip()
except:
    pass

# Fallback to gemma (per guardrail)
if not answer:
    model_used = "gemma"
    try:
        resp = subprocess.run([
            "curl", "-s", "-m", "30", "http://127.0.0.1:1234/v1/chat/completions",
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {TOKEN}",
            "-d", json.dumps({
                "model": "gemma4-e2b",
                "messages": ([{"role": "system", "content": SYSTEM_MSG}, {"role": "user", "content": prompt}] if SYSTEM_MSG else [{"role": "user", "content": prompt}]),
                "max_tokens": 500,
                "temperature": temperature
            })
        ], capture_output=True, text=True, timeout=30)
        data = json.loads(resp.stdout)
        answer = data["choices"][0]["message"]["content"].strip()
    except:
        pass

if not answer:
    print("GENERATION UNAVAILABLE")
    sys.exit(2)

# Print result (model already includes citation)
print(answer)

# Log the run
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
answer_head = answer[:100].replace("\n", " ")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} | query={QUERY} | segment={best_file} | score={best_score} | model={model_used} | answer={answer_head}\n")

sys.exit(0)