# LOCAL-LM-ASSET-REQUEST — 20261109 (design phase)

**Seat:** beam (flagship) · **Class:** WRITE-design · **Artifact:** `studies/rfc-143379-rig/LOCAL-LM-ASSET-REQUEST-20261109.md`  
**Status:** DESIGN ONLY — no fire without the operator's word. The workflow draft is a design; it is not wired into CI.

**Operator's frame (verbatim-shaped):** the platform meters its HOSTED VMs, NOT the self-hosted runner — the only install we own is the Avrea runner's environment, so a CUSTOM GitHub-Action that runs there turns the unmetered silicon into the LOCAL-LM testbed: run the dark-horse family's fast machinery (or a fast small-LM equivalent) on what we have, as a test of a local-LM aspect to this project — the custom-Action becomes the amplifier.

---

## 0. Ground read (the hardware + the runner + the precedent)

### 0.1 Host hardware (Avrea self-hosted runner)

Read via `nproc` / `free -g` / `lscpu | head` on the runner's shell. Recorded reality (the brief's anchor): **12 cores**, ~`free -g` reporting the box's RAM (operator's own silicon, unmetered). The design assumes a 12-core / multi-GB box with no GPU (CPU-only inference). Concretely the workflow must be sized to **CPU-only, fast small-LM** — no CUDA, no ROCm, no Metal; AVX2/AVX-512 friendly engines only.

| Probe | Expected (operator to re-confirm on the runner) | Design use |
|---|---|---|
| `nproc` | 12 | thread count for build (`-j12`) and inference (`-t 8`/`-t 12`) |
| `free -g` | ≥ 16 GB (typical Avrea box) | model + KV cache headroom; pick quant + ctx to fit |
| `lscpu` flags | `avx2` (and ideally `avx512f`) | engine choice (llama.cpp / ik_llama.cpp build flags) |
| `/opt/actions-runner` | exists, label `self-hosted,avrea` | runner cwd + workspace + label pin |

Build-time estimate from 12 cores: a clean `cmake --build . --config Release -j12` of llama.cpp ≈ **3–6 min** on a 12-core box (CPU-only, no CUDA). A from-scratch `git clone` + cmake configure adds ~1–2 min. Total engine step ≈ **5–8 min**. Model download (a ~1–2 GB quant) ≈ **1–3 min** on the runner's link. Battery (see §2) ≈ **per-cell 200–250 s × N cells** — that is the long pole; size the matrix accordingly (see §2.4).

### 0.2 Runner install (`/opt/actions-runner`)

- Path: `/opt/actions-runner` — the self-hosted runner's root.
- Label (pin in the workflow): `self-hosted, avrea` (the Avrea runner's label; matches the precedent `rig-hosted-verify-avrea.yml`).
- Workspace: `/opt/actions-runner/_work/<repo>/<repo>` (GitHub runner default). The workflow's `working-directory` and artifact paths must be expressed relative to `${{ github.workspace }}`, never hard-coded `/opt/...`, so the design survives runner relocation.
- The runner's env is the only install we own → the custom Action lives in the repo's `.github/actions/` (a composite or docker action) OR is inlined as workflow steps. **Decision: inlined steps + one composite action `local-lm-engine`** (see §1.2) so the engine build is reusable and cacheable.

### 0.3 Existing precedent

- `.github/workflows/creative-copycat.yml` — the self-hosted pattern + study-ref dispatch. The new workflow mirrors its `workflow_dispatch` inputs (`study_ref`, `run_id`) and its `runs-on: [self-hosted, avrea]` pin, so the local-LM test is dispatchable against a study branch exactly like the copycat lane.
- `.github/workflows/rig-hosted-verify-avrea.yml` — the Avrea verify matrix; the local-LM test is a sibling, not a replacement.
- The aces-harness-probes battery architecture (SKILL.md): script-once, per-cell timeouts, incremental JSON written after every cell, verdict file before summary echo, resume-safe skip of present `cell_id`s, pre-warm embedding cache at every window size.
- Dark-horse lineage (`references/harness-lineage.md`): `darkhorse-*.sh` on `/root/scripts/` — v1 motor (TOOL_OK smoke), v2 form (schema envelope), v3 function (9B as bounded ACES audit lane), v4 control (no LP), v4.1 LP-framed A/B. The smoke payload: load `deepseek-v4-pro-qwen3.5-9b-mtp` @131072 ctx, MTP on, LM-Studio-served. The eldest bridge's mechanism = query-embedder → cosine-match against real doc-chain segments → route dark horse (:44831) or gemma (:1234) → cite winning segment or NOT IN CHAIN.

---

## 1. The workflow skeleton

### 1.1 Complete draft — `.github/workflows/local-lm-test.yml`

```yaml
# DESIGN ONLY — do not merge/enable without operator's word.
# Runs on the UNMETERED Avrea self-hosted runner. No hosted-VM minutes consumed.
name: local-lm-test

on:
  workflow_dispatch:
    inputs:
      study_ref:
        description: "study branch or commit to test against"
        required: true
        default: "study/rfc-143379-rig-20261105"
      run_id:
        description: "unique run id (for artifact naming)"
        required: false
        default: "local-lm-001"
      model_profile:
        description: "fast small-LM profile"
        required: false
        default: "qwen2.5-0.5b-q4km"
        type: choice
        options:
          - qwen2.5-0.5b-q4km
          - qwen2.5-1.5b-q4km
          - phi3.5-mini-q4km
      engine_profile:
        description: "engine build profile"
        required: false
        default: "llama-cpp-cpu"
        type: choice
        options:
          - llama-cpp-cpu
          - ik-llama-cpu

concurrency:
  # one battery at a time on the runner (harness lock is per-harness)
  group: local-lm-test-${{ github.ref }}
  cancel-in-progress: false

jobs:
  local-lm:
    name: local-lm battery on avrea runner
    runs-on: [self-hosted, avrea]
    timeout-minutes: 360   # 6h ceiling; battery is the long pole
    env:
      STUDY_REF: ${{ github.event.inputs.study_ref }}
      RUN_ID: ${{ github.event.inputs.run_id }}
      MODEL_PROFILE: ${{ github.event.inputs.model_profile }}
      ENGINE_PROFILE: ${{ github.event.inputs.engine_profile }}
      # engine threading (12-core box, leave 2 for OS/runner)
      LLAMA_THREADS: "10"
      LLAMA_CTX: "4096"
    steps:
      - name: checkout study ref
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.inputs.study_ref }}
          fetch-depth: 1

      - name: runner header (hardware receipt)
        shell: bash
        run: |
          set -euo pipefail
          mkdir -p results/local-lm
          {
            echo "=== RUNNER HARDWARE HEADER ==="
            echo "run_id=${RUN_ID}"
            echo "study_ref=${STUDY_REF}"
            echo "hostname=$(hostname)"
            echo "nproc=$(nproc)"
            echo "mem_total_gb=$(free -g | awk '/^Mem:/{print $2}')"
            echo "cpu_model=$(lscpu | awk -F: '/Model name/{gsub(/^ +/,"",$2);print $2;exit}')"
            echo "cpu_flags=$(lscpu | awk -F: '/Flags/{print $2}' | tr ' ' '\n' | grep -E 'avx2|avx512f|avx512bw' | sort -u | tr '\n' ' ')"
            echo "runner_root=/opt/actions-runner"
            echo "github_workspace=${GITHUB_WORKSPACE}"
            echo "timestamp_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
          } | tee results/local-lm/hardware-header.txt

      - name: build engine (minimal, CPU)
        uses: ./.github/actions/local-lm-engine
        with:
          engine_profile: ${{ env.ENGINE_PROFILE }}
          threads: ${{ env.LLAMA_THREADS }}

      - name: fetch model (smallest viable quantized)
        shell: bash
        run: |
          set -euo pipefail
          mkdir -p models
          case "${MODEL_PROFILE}" in
            qwen2.5-0.5b-q4km)
              URL="https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf"
              FILE="qwen2.5-0.5b-instruct-q4_k_m.gguf"
              ;;
            qwen2.5-1.5b-q4km)
              URL="https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf"
              FILE="qwen2.5-1.5b-instruct-q4_k_m.gguf"
              ;;
            phi3.5-mini-q4km)
              URL="https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF/resolve/main/Phi-3.5-mini-instruct-Q4_K_M.gguf"
              FILE="Phi-3.5-mini-instruct-Q4_K_M.gguf"
              ;;
          esac
          if [ ! -f "models/${FILE}" ]; then
            echo "downloading ${FILE}"
            curl -L --fail --retry 3 -o "models/${FILE}.part" "${URL}"
            mv "models/${FILE}.part" "models/${FILE}"
          else
            echo "cached: models/${FILE}"
          fi
          sha256sum "models/${FILE}" | tee "models/${FILE}.sha256"
          echo "MODEL_FILE=models/${FILE}" >> "$GITHUB_ENV"

      - name: pre-warm (embedding cache) — no-op for raw engine; placeholder for harness mode
        shell: bash
        run: |
          set -euo pipefail
          # The harness's embedder cache warm-up (per ACES SKILL cache rules) only applies
          # when harness-bridge.sh is in play. In raw-engine mode this step is a no-op marker.
          echo "pre-warm step: raw-engine mode — skipping embedder cache warm (n/a)"

      - name: run probe battery
        shell: bash
        env:
          ENGINE_BIN: ${{ github.workspace }}/engine/llama-cli
          MODEL_PATH: ${{ github.workspace }}/${{ env.MODEL_FILE }}
          RESULTS_JSON: ${{ github.workspace }}/results/local-lm/battery-results.json
          VERDICT_FILE: ${{ github.workspace }}/results/local-lm/verdict.txt
          CELL_TIMEOUT_SEC: "240"
          HARNESS: "raw-engine"   # or "harness-bridge" when the bridge is present
        run: |
          set -euo pipefail
          python3 scripts/local_lm_battery.py \
            --engine-bin "${ENGINE_BIN}" \
            --model "${MODEL_PATH}" \
            --threads "${LLAMA_THREADS}" \
            --ctx "${LLAMA_CTX}" \
            --results-json "${RESULTS_JSON}" \
            --verdict-file "${VERDICT_FILE}" \
            --cell-timeout "${CELL_TIMEOUT_SEC}"

      - name: write receipt (cold-stranger re-run manifest)
        shell: bash
        run: |
          set -euo pipefail
          cat > results/local-lm/receipt.md <<EOF
          # local-lm-test receipt
          run_id: ${RUN_ID}
          study_ref: ${STUDY_REF}
          engine: \${ENGINE_PROFILE}
          model: \${MODEL_PROFILE} -> \${MODEL_FILE}
          threads: \${LLAMA_THREADS}  ctx: \${LLAMA_CTX}
          cell_timeout_sec: 240
          hardware: see hardware-header.txt
          results: battery-results.json
          verdict: verdict.txt
          re-run: gh workflow run local-lm-test -f study_ref=${STUDY_REF} -f run_id=${RUN_ID}
          EOF
          echo "receipt written"

      - name: upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: local-lm-${{ github.event.inputs.run_id }}
          path: |
            results/local-lm/
            models/*.sha256
          retention-days: 30
```

### 1.2 Composite action — `.github/actions/local-lm-engine/action.yml`

```yaml
name: local-lm-engine
description: Build the smallest viable CPU engine on the Avrea runner.
inputs:
  engine_profile:
    required: true
  threads:
    required: false
    default: "10"
outputs:
  engine_bin:
    description: path to llama-cli
    value: ${{ steps.build.outputs.engine_bin }}
runs:
  using: composite
  steps:
    - name: cache engine build
      uses: actions/cache@v4
      with:
        path: |
          engine/build
          engine/src
        key: local-lm-engine-${{ inputs.engine_profile }}-${{ hashFiles('engine/CMakeLists.txt') }}
        restore-keys: local-lm-engine-${{ inputs.engine_profile }}-
    - name: clone + configure (cache miss only)
      if: steps.cache.outputs.cache-hit != 'true'
      shell: bash
      run: |
        set -euo pipefail
        mkdir -p engine
        if [ ! -d engine/src/.git ]; then
          git clone --depth 1 https://github.com/ggerganov/llama.cpp engine/src
        fi
        cmake -S engine/src -B engine/build \
          -DCMAKE_BUILD_TYPE=Release \
          -DLLAMA_BUILD_TESTS=OFF \
          -DLLAMA_BUILD_EXAMPLES=OFF \
          -DLLAMA_CURL=OFF
    - name: build
      shell: bash
      run: |
        set -euo pipefail
        cmake --build engine/build --config Release -j${{ inputs.threads }}
        test -x engine/build/bin/llama-cli
    - name: record engine version
      id: build
      shell: bash
      run: |
        set -euo pipefail
        ./engine/build/bin/llama-cli --version | tee engine/version.txt
        echo "engine_bin=${GITHUB_WORKSPACE}/engine/build/bin/llama-cli" >> "$GITHUB_OUTPUT"
```

Engine choice rationale: **llama.cpp** (CPU-only, AVX2/AVX-512, no GPU dep, smallest build surface, fastest cold start). `ik_llama.cpp` is the alternate profile (better CPU throughput on some quants) but heavier build; offered as a choice, not the default. The "smallest viable engine" is llama.cpp with tests/examples/curl disabled → ~3–6 min build on 12 cores. The "smallest viable quantized model" is **Qwen2.5-0.5B-Instruct Q4_K_M** (~0.4 GB) — fast enough to run the dark-horse chain probes in seconds per cell; 1.5B and Phi-3.5-mini are the upgrade rungs.

### 1.3 Timeouts

| Layer | Value | Rationale |
|---|---|---|
| Job `timeout-minutes` | 360 | 6h ceiling; battery is the long pole |
| Per-cell `CELL_TIMEOUT_SEC` | 240 | sits UNDER the engine's own 300s curl/subprocess timeout so the probe owns the verdict (ACES pitfall) |
| Build step | inherits job | 5–8 min expected |
| Model download | inherits job | 1–3 min expected |
| Viability gate (separate score) | 180 s | a cell finishing under 180s counts as "fast"; over = slow but not fail |

### 1.4 Runner cwd patterns

- All paths via `${{ github.workspace }}` (the runner's `_work/...` dir). Never hard-code `/opt/actions-runner`.
- Engine build cache under `engine/` in the workspace, restored by `actions/cache` keyed on engine profile + CMakeLists hash.
- Model cache under `models/` — NOT cached across runs by default (disk pressure); the `if [ ! -f ]` guard skips re-download within a single run if a step re-runs.
- Results always under `results/local-lm/` → uploaded by `upload-artifact`.

---

## 2. The probe-battery design

### 2.1 Mapping the dark-horse family onto the local engine's lexicon

The dark-horse family (`darkhorse-*.sh`) is the rig's own prior implementation of the read-gap compensation: embedder → cosine-match against real doc-chain segments → route to dark horse (:44831) or gemma (:1234) → cite winning segment or NOT IN CHAIN. The local engine (llama.cpp running a 0.5B quant) replaces the routed engine; the **probe shapes** are the ACES battery's, mapped onto the local engine's lexicon:

| ACES probe shape (dark-horse / harness lineage) | Local-engine lexicon | What it tests on the 0.5B |
|---|---|---|
| **Chain-segment probe** (retrieve + cite segment N) | `retrieve-and-cite`: feed a 500-char segment context + a query; ask the model to cite the segment id or say NOT IN CHAIN | Does the 0.5B honor the cite-or-refuse contract on CPU? |
| **Cosine-threshold tuning** (absent-factoid score vs lowest grounded score) | `threshold-knee`: run grounded + absent queries at threshold 0.60; record DEBUG_SCORE | Where is the honest-rejection knee on this engine? |
| **Window/block-size sweep** (HARNESS_WIN_SIZE 2048/4096) | `window-sweep`: same chain at win_size 2048 vs 4096 | Does context window change retrieval correctness on a tiny model? |
| **Preamble-style shift** (BS=a "Thinking Process" vs no-thinking SYSTEM_MSG) | `preamble-style`: two system-message variants, score refusal vs answer | Does the 0.5B's refusal gate on preamble style (C32 finding) or on content? |
| **Boundedness / tool-loop** (valid-tool drive, wall-clock alarm only) | `boundedness`: drive a valid tool (trivial `execute_code`) in a loop; measure termination | Does the local engine terminate on budget or only on retry cap? (confound check) |
| **Invalid-tool confound control** | `invalid-tool-control`: deliberately invalid tool name; confirm 3-retry cap, NOT budget | Names the mechanism (retry cap vs budget) |

### 2.2 The battery script (`scripts/local_lm_battery.py`) — design spec

- **Script-once, never per-cell calls:** ONE script, ONE invocation, per-cell timeout, incremental JSON written after EVERY cell (timeout-safe). Resume-safe: skip `cell_id`s already present in the JSON.
- **Calls the engine via subprocess** (`llama-cli` with `-p` prompt, `--json` where supported, `-n` max tokens). No raw HTTP; the engine is a local binary.
- **Pre-warm:** n/a for raw engine (no embedder cache); the step is a documented no-op. If run in `harness-bridge` mode, pre-warm the embedder cache at every window size first (per ACES cache rules).
- **Segment file naming (harness glob):** if harness mode is used, segment copies must start with `0` (convention `002-<cycle>-seg<NN>.md`), backup original first.
- **WRITE-FIRST:** verdict file written BEFORE the final summary echo.

Cell shape (incremental JSON, one object per cell):

```json
{
  "cell_id": "retrieve-and-cite::seg006::threshold0.60::win2048",
  "shape": "retrieve-and-cite",
  "segment": "seg006",
  "threshold": 0.60,
  "win_size": 2048,
  "bs": "a",
  "preamble_style": "default",
  "prompt": "...",
  "raw_output": "...",
  "cited_segment": "seg006 | null",
  "verdict": "CORRECT | HONEST_REFUSAL | CONFABULATION | TIMEOUT | ERROR",
  "latency_sec": 12.4,
  "exit_code": 0,
  "timestamp_utc": "..."
}
```

### 2.3 Per-cell timeouts

- `CELL_TIMEOUT_SEC=240` (probe owns the verdict; sits under engine's 300s).
- Viability gate scored separately at 180s (a "fast" cell).
- A cell exiting -9 (SIGKILL) with the engine alive and no OOM → battery-lifecycle kill (process-group), NOT an engine defect (ACES diagnostic signature). Fix the run mode (foreground script-once + notify), not the engine.

### 2.4 Matrix sizing (don't blow the 6h ceiling)

Recommended default matrix: 6 cells × ~120s avg ≈ 12 min. Full matrix (all shapes × 2 window sizes × 2 preamble styles) ≈ 24 cells × ~120s ≈ 48 min — well inside 6h. Do NOT run two batteries concurrently on the same runner (harness lock is per-harness; phantom CONFABULATION cells).

### 2.5 Verdict file

`results/local-lm/verdict.txt` — written BEFORE the final summary echo. Contains: per-cell evidence table, per-bucket recommendation, verdict vs invariant, engine lock state, skills loaded, hardware header pointer, engine version, model quant, re-run command. Chat carries only the one-line verdict + artifact path.

---

## 3. The receipt shape

A cold stranger re-runs with: `gh workflow run local-lm-test -f study_ref=<ref> -f run_id=<id>` and gets the same evidence. The run "lands" only if ALL of these are present in the uploaded artifact:

1. **Hardware header** (`hardware-header.txt`): nproc, mem_total_gb, cpu_model, cpu_flags, runner_root, github_workspace, timestamp_utc, run_id, study_ref.
2. **Engine version** (`engine/version.txt`): `llama-cli --version` output + build profile + thread count + cache key.
3. **Model quant** (`models/*.sha256` + the model filename in receipt.md): profile name, filename, sha256, size bytes.
4. **Per-cell rows** (`battery-results.json`): every cell with cell_id, shape, verdict, latency_sec, exit_code, raw_output, timestamp.
5. **Verdict** (`verdict.txt`): one-line verdict + per-cell evidence table + per-bucket recommendation + verdict-vs-invariant + re-run command.
6. **Receipt** (`receipt.md`): the cold-stranger manifest (run_id, study_ref, engine, model, threads, ctx, cell_timeout, hardware pointer, results pointer, verdict pointer, re-run command).

Gate: if any of 1–5 is missing, the run does NOT count as a landing; the verdict file must say so explicitly.

---

## 4. The cross-use's creative note

The union of (a) an unmetered self-hosted runner we fully own, (b) a custom in-repo Action that builds the smallest viable CPU engine and runs a fast 0.5B quant, and (c) the ACES probe battery's script-once/incremental/verdict discipline turns the Avrea box into a **CI-shaped local-LM lab**: every study branch becomes re-runnable evidence, the dark-horse family's read-gap machinery (embedder → cosine → cite-or-refuse) gets a cheap, repeatable, version-controlled test surface on real silicon, and the local-LM aspect of this project — "can a tiny model honor the cite-or-refuse contract on our own hardware?" — becomes answerable with a single `gh workflow run`, at zero hosted-VM cost, with the receipt as the artifact. The amplifier is not the model; it is the **repeatability**: unmetered compute + a workflow + a verdict file means the local-LM question stops being a one-off experiment and becomes a regression we can re-run on every branch. (Design phase only — no fire without the operator's word.)

---

## 5. Compose-check (self-audit before commit)

- [x] Workflow skeleton complete (`.github/workflows/local-lm-test.yml` draft) with self-hosted label, study-ref dispatch, engine build, model download, battery step, receipt, artifact upload.
- [x] Engine chosen to run fast on what we have (llama.cpp CPU, AVX2/AVX-512, 12 cores, 3–6 min build); smallest viable quantized model named with download URL (Qwen2.5-0.5B Q4_K_M).
- [x] Build-time estimate from hardware read (5–8 min engine, 1–3 min model).
- [x] Runner cwd patterns (all via `${{ github.workspace }}`, caches keyed).
- [x] Timeouts (job 360 min, cell 240 s, viability gate 180 s).
- [x] Probe battery design: dark-horse shapes mapped onto local-engine lexicon (retrieve-and-cite, threshold-knee, window-sweep, preamble-style, boundedness, invalid-tool control); script-once, per-cell timeouts, incremental JSON, verdict file, resume-safe.
- [x] Receipt shape: hardware header, engine version, model quant, per-cell rows, verdict — cold-stranger re-runnable.
- [x] Cross-use creative note (one paragraph, operator's frame honored).
- [x] Nothing public: artifact on the study branch only; workflow is a design (not enabled).
- [x] No fire: `workflow_dispatch` only, no `push`/`schedule` triggers.

---

## 6. Open items (operator decision before any fire)

1. Confirm hardware numbers (`nproc`, `free -g`, `lscpu` flags) on the actual Avrea runner; adjust thread count / quant choice if RAM < 8 GB.
2. Confirm the runner's label is `avrea` (or update the `runs-on` pin).
3. Confirm network egress from the runner to huggingface.co for the model download (or pre-stage the model on the runner).
4. Decide whether to run in `raw-engine` mode (default, this design) or `harness-bridge` mode (requires copying `harness-bridge.sh` onto the runner).
5. Operator's word to fire (`gh workflow run local-lm-test`).
