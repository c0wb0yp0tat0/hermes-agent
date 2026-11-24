# Hermes Setup — Local LLM Notes

Last updated: 2026-08-30

## Local LLM status: WORKING — via Ollama (documented path), tuned for speed

**Verified end-to-end (2026-08-30):** `hermes -p lmstudio chat` uses the terminal
tool through the local model with real tool calls. Final model: **gemma4:e2b** —
**4m 45s first response** (session `20260830_141401_35d40a`, 2 tool calls, exit 0).

### Model comparison (all tested on this box, tool calls verified)
| Model | First response | tok/s | RAM | Notes |
|---|---|---|---|---|
| llama3.1:8b | 20+ min ❌ | 9 | 14 GB | reliable but too slow |
| qwen3.5:4b | 8m 8s (trimmed) | 18 | 5.6 GB | worked; 17m38s untrimmed |
| **gemma4:e2b** | **4m 45s** ✅ | **34** | 7.4 GB | **winner — fastest, tools OK** |
| gemma4:e4b | 8m 20s ❌ | 17 | 10 GB | slower AND failed tool call (printed text) — removed |
| gemma4:e2b-it-qat (mobile) | 6m 18s | 27 | 4.5 GB | mobile-optimized QAT variant; slower here but smallest footprint |

The "mobile" variant (gemma4:e2b-it-qat, QAT/LiteRT lineage) is available and works,
but the generic e2b Q4_K_M is faster on this CPU. Both under the 5-min goal.

### THE WORKING RECIPE (final)
1. **Ollama** (not llama.cpp, not LM Studio) — `curl -fsSL https://ollama.com/install.sh | sh`
2. **Model: `qwen3.5:4b`** — 256K native context (no 64K clamp issue), ~18-19 tok/s
   on this CPU, real tool calling verified. 8B models (llama3.1:8b) = reliable but
   20-min first response (disqualified). Community floor for *reliable* agentic
   tool use is 8B, but on this CPU the 4B is the practical choice.
3. **Ollama systemd override** (`/etc/systemd/system/ollama.service.d/override.conf`):
   ```
   [Service]
   Environment="OLLAMA_CONTEXT_LENGTH=64000"
   Environment="OLLAMA_KEEP_ALIVE=24h"
   Environment="OLLAMA_NUM_THREADS=12"
   ```
4. **Profile .env**: `HERMES_API_TIMEOUT=1800`
5. **Profile config** (via `hermes config set`):
   - `model.default: qwen3.5:4b`, `model.provider: custom`
   - `model.base_url: http://localhost:11434/v1`
   - `model.context_length: 262144`
   - `agent.reasoning_effort: none`  (llama3.1 rejected thinking params; qwen3.5
     with reasoning off avoids thinking-token waste)
   - **`hermes tools disable bfl --platform cli`** — drops 10.2 KB of FLUX video
     tool schemas (useless on GPU-less box) → prompt 35.6→25.2 KB schemas.
     **This cut the first response from 17m38s → 8m8s.**
6. Profile cli toolsets (minimal, keep capability): web, file, terminal, memory,
   skills, todo, clarify. Skills index + memory injection already off.

### Speed math (Xeon E5-1650, 2012, AVX-only, DDR3 bandwidth wall)
- ~18 tok/s is the ceiling for 4B Q4 (memory-bound, not core-bound; more threads
  don't help — verified OLLAMA_NUM_THREADS=12 changed nothing).
- Fixed prompt ≈ 8.2K tokens (9.5 KB system + 25 KB schemas) → ~7.5 min prefill.
- First turn: ~8 min. Follow-ups: fast (Ollama caches; `cached n_tokens` in logs).
- To go faster: smaller model (3B) breaks tool-call reliability (user reports);
  trimming more toolsets (skills/clarify/todo) only saves ~2-3 min and costs
  capability. 8 min is the honest floor for reliable local agent work here.

### What did NOT work (history)
- LM Studio `lms` Linux binary: AVX2-only → SIGILL on this CPU. Dead end.
- llama.cpp hand-build: worked (tool calls OK) but not documented path; slower
  than Ollama for same model.
- qwen2.5-coder:7b: 32K native context — Hermes hard-rejects (<64K). Can't be
  raised (Ollama clamps to GGUF max).
- llama3.1:8b: works (128K, tools) but 20+ min first response — too slow.
- qwen3.5:4b with full toolset: 17m38s. With bfl off: 8m8s. ✅

### Ollama version note
- v0.33.2. `OLLAMA_CONTEXT_LENGTH` env var works (model loads at 64000).
- `ollama ps` CONTEXT column is the source of truth.
- Keep-alive is critical — without it the model unloads after 5 min and breaks
  mid-conversation requests.

## Still working (unchanged)
- Telegram gateway: systemd `hermes-gateway`; hermes-webui 0.0.0.0:8787; Tailscale
  pve-1 = 100.112.72.20; Hermex shows default (Nous) + lmstudio (local) profiles.

## Open items
1. Reboot test of ollama.service auto-start (enabled; verify after next reboot).
2. Hermex: profile picker → lmstudio for local chats (first message ~8 min, then fast).
3. Old llama.cpp artifacts: /root/llama.cpp + /root/models GGUFs (~8 GB) —
   superseded, safe to delete. Ollama has qwen2.5-coder:7b + qwen2.5-coder-64k
   + llama3.1:8b + qwen3.5:4b; the first three can be removed (~10 GB) if disk needed.

## Environment facts
- Proxmox host: root, LAN 192.168.1.179/24, Tailscale 100.112.72.20.
- CPU: Xeon E5-1650 (Sandy Bridge, AVX only — NO AVX2). RAM: 31 GB. Disk ~33 GB free.
- Hermex URL: http://100.112.72.20:8787 (password in ~/hermes-webui/.env).
