# TESTBED-BUILD-20261109 — the local-LM testbed's next rung (arm-probe's successor)

**Seat:** harness-lane (engine) · **Class:** EXEC-write · **Date:** 2026-11-09 · **Status:** draft-for-next-dispatch (none executed; runner's actual build happens on the platform's next dispatch)

**Parent rung:** arm-probe (self-hosted runner executes hosted code end-to-end → `completed | success`).
**This rung:** THE TESTBED'S BUILD — runner-side action that compiles and runs a real local model.

---

## 0. Skill-mandate scan (family's lenses, named with why)

Inventory scanned: `skills/` (software-development, autonomous-ai-agents, devops, media, research, …). The three named family lenses — `local-LLM-serving`, `local-llm-studio-headless`, `llama-cpp` — are **not present as installed skills** in this tree (no `skills/**/local-llm*` or `*llama*` paths). They are treated as **external/latent lenses** to be loaded when the runner dispatches; this artifact records the *why* each would be loaded so the next operator can pull them:

| Lens | Why it would be loaded | What it governs in this artifact |
|---|---|---|
| `local-LLM-serving` | Governs how a self-hosted runner serves a model (process lifecycle, port, health-check, concurrency). | §3 fetch-model + run-command shape; §4 probe inputs (endpoint contract). |
| `local-llm-studio-headless` | Governs headless studio/CLI invocation of a local model (no GUI, deterministic flags). | §2 compile+run sketch (flags, threads, ctx size); §5 action steps. |
| `llama-cpp` | Governs llama.cpp build matrix (cmake flags, quant formats, binary names, GGUF). | §1 build-surface; §2 small-quantized model fetch-source; §6 receipt schema fields. |

**Load rule:** each lens is named at point of use (not bulk-loaded) so a missing lens degrades one section, not the whole artifact. Fallback = inline sketch below (this document is the source of truth until lenses arrive).

---

## 1. Build-surface — llama.cpp-style CPU build (sketch, draftable, not executed)

Target: a reproducible CPU-only build of llama.cpp on the self-hosted runner, producing `llama-cli` + `llama-embedding` (or `llama-server`) binaries.

### 1.1 Compile step (shape)
```bash
# runner: ubuntu-latest-class self-hosted, CPU only, no GPU
git clone --depth 1 https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
cmake -S . -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_NATIVE=ON \            # tune to runner CPU
  -DLLAMA_BUILD_TESTS=OFF \
  -DLLAMA_CURL=OFF
cmake --build build --config Release -j"$(nproc)" --target llama-cli llama-embedding
```
- **Verification (build step):** `build/bin/llama-cli --version` exits 0 and prints a version line; `build/bin/llama-embedding --help` exits 0. Binary sha256 recorded in receipt (§6).
- **Determinism note:** `GGML_NATIVE=ON` makes the binary host-specific; that's acceptable for a self-hosted runner probe but must be recorded (receipt `build.host_cpu`).

### 1.2 Small-quantized model fetch-source
- **Model:** a small quantized GGUF, e.g. `Qwen2.5-0.5B-Instruct-Q4_K_M.gguf` (or any ≤1B param, Q4_K_M, ~0.4 GB) from HuggingFace.
- **Fetch source (draft, not executed):**
```bash
MODEL_URL="https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf"
curl -L --fail --retry 3 -o models/model.gguf "$MODEL_URL"
sha256sum models/model.gguf   # recorded in receipt
```
- **Verification:** file size > 0 and < 1 GB; sha256 matches pinned value in receipt `model.sha256`; `llama-cli -m models/model.gguf --version`-style load probe (see §3) succeeds.

### 1.3 Run-command shape
```bash
./build/bin/llama-cli \
  -m models/model.gguf \
  -p "Say hello in one sentence." \
  -n 32 \
  --threads "$(nproc)" \
  --ctx-size 512 \
  --temp 0.0 \
  --no-display-prompt
```
- **Success meter:** process exits 0, stdout non-empty, latency < 60s on runner CPU.

---

## 2. Probe-battery design — dark-horse family's probe as first probe

First probe in the battery: **embedder-cosine read-gap machinery** (the dark-horse family's probe). It measures whether the runner's local model can produce embeddings whose cosine similarity tracks a known read-gap (semantic distance) between pairs.

### 2.1 Probe inputs
- **Pairs file** `probe/pairs.jsonl`, each line:
  ```json
  {"id":"p1","a":"the cat sat on the mat","b":"a feline rested on the rug","label":"close","expected_cosine_min":0.75}
  {"id":"p2","a":"the cat sat on the mat","b":"quantum chromodynamics and gluon flux","label":"far","expected_cosine_max":0.30}
  ```
- **Embedding command (shape):**
  ```bash
  ./build/bin/llama-embedding -m models/model.gguf -f probe/texts.txt --embd-normalize 2 -ngl 0
  ```
  (or `llama-server` `/embedding` endpoint; both acceptable; receipt records which.)

### 2.2 Expected outputs
- For each pair, cosine similarity `cos(e_a, e_b)` in `[-1,1]`.
- Report JSON `probe/report.json`:
  ```json
  {"probe":"embedder-cosine-read-gap","n":N,"pairs":[{"id":"p1","cos":0.81,"pass":true}], "read_gap": <mean close - mean far>, "pass": true}
  ```

### 2.3 Success meters
- **M1 (load):** embedding binary runs and emits vectors for all inputs; no crash/OOM.
- **M2 (ordering):** for every `close` pair cos > every `far` pair cos (strict separation) OR read_gap ≥ 0.4.
- **M3 (threshold):** ≥ 80% of pairs satisfy their `expected_cosine_min/max`.
- **M4 (receipt):** `probe/report.json` written and uploaded (§5 step 5–6).
- **Probe verdict:** `pass` iff M1 ∧ M2 ∧ M3 ∧ M4.

---

## 3. Action-matrix — custom GitHub Action steps (in order)

Action name (draft): `testbed-build` (composite action or workflow job). Steps:

| # | Step | Command / action | Verification |
|---|---|---|---|
| 1 | checkout | `actions/checkout@v4` (repo + this study) | workspace present; `git rev-parse HEAD` recorded |
| 2 | build | cmake configure+build (§1.1) | `llama-cli --version` exit 0; binary sha256 recorded |
| 3 | fetch-model | curl model + sha256 verify (§1.2) | file size in range; sha matches pinned |
| 4 | probe | run embedder-cosine (§2) | `report.json` exists; verdict computed |
| 5 | receipt-write | write `receipts/testbed-build-<run>.json` (§6) | JSON validates against schema; all fields populated |
| 6 | artifact-upload | `actions/upload-artifact@v4` (binaries? no—receipts+report+logs) | artifact downloadable; name recorded in receipt |

- **Ordering invariant:** step N+1 must not start if step N failed (job-level `if: success()`). Probe failure still writes a receipt with `verdict=fail` (step 5 runs `if: always()` for receipt, upload `if: always()`).

---

## 4. Receipts-arch integration — build receipt schema

File: `receipts/testbed-build-<run_id>.json` (or `.md` twin). Schema (draft):

```json
{
  "rung": "TESTBED-BUILD",
  "run_id": "<github run id>",
  "commit": "<sha>",
  "host": {"os": "...", "cpu": "...", "nproc": N},
  "build": {
    "llama_cpp_ref": "<git sha>",
    "cmake_flags": ["..."],
    "binary": "llama-cli",
    "binary_sha256": "...",
    "build_seconds": 0
  },
  "model": {"url": "...", "sha256": "...", "size_bytes": 0, "quant": "Q4_K_M"},
  "probe": {
    "name": "embedder-cosine-read-gap",
    "report_path": "probe/report.json",
    "verdict": "pass|fail",
    "read_gap": 0.0,
    "meters": {"M1": true, "M2": true, "M3": true, "M4": true}
  },
  "steps": [{"n":1,"name":"checkout","status":"success","seconds":0}, "..."],
  "verdict": "pass|fail",
  "timestamp": "ISO8601"
}
```

- **Integration point:** receipts land in the study's `receipts/` convention (mirroring `FINISH-LINE-REPLICATION-*.py` outputs and `NEGENTROPY-SWEEP-*` receipts). The harness-lane reads `verdict` + `probe.read_gap` as the rung's success signal.

---

## 5. Own 5-why (ride the landing)

1. **Why build a real local model on the runner?** Because the arm-probe only proved code *executes*; it did not prove the runner can compile+run a model — the actual asset capability.
2. **Why llama.cpp CPU?** It's the lowest-friction, no-GPU, reproducible build that still yields real inference + embeddings; matches self-hosted runner constraints.
3. **Why embedder-cosine as the first probe?** It's deterministic-ish, cheap, and tests a *semantic* capability (not just "did it print text"), giving a real signal vs. a smoke test.
4. **Why a receipt schema?** Without a structured receipt the rung's result is unverifiable across dispatches; the schema is the contract between runner and harness-lane.
5. **Why draft-only now?** The runner's actual build happens on the platform's next dispatch; this artifact is the spec the dispatch consumes. Executing here would violate "nothing public; rowing's the rotation's" and skip platform verification.

**Webstorm (landing check):** The rung is *complete as a spec* when (a) build sketch is unambiguous, (b) probe has measurable success meters, (c) action steps are ordered with per-step verification, (d) receipt schema is defined. All four present → spec complete; execution deferred to platform dispatch. Risk: model URL/sha may rot → mitigate by pinning and re-verifying at fetch time (step 3 verification).

---

## 6. Next mechanism (one line)

Next rung after TESTBED-BUILD passes: **TESTBED-PROBE-BATTERY-EXPANSION** — add a second probe (chat-completion coherence + latency SLO) to the battery and a cross-probe aggregate verdict, consuming the receipt schema above.

---

*Artifact written per mission brief. Nothing public; rowing's the rotation's.*
