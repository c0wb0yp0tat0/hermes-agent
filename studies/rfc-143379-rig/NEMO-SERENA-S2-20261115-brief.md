# NEMO STAGE 2 — THE SERENA HARNESS-PLANNER (2026-11-15) — the MCP-executor leg's design

## Your role (fleet asset, budget-conscious — stage 2 of 3)
Stage 1 (the bearer) landed `SERENA-BEARINGS-20261115.md`. You are the PLANNER: the harness-integration design — the two-way-door MCP-executor leg for the write-problem class. Your crate (inline below, from stage 1 + the CTO-side storm) + ≤ 3 BOUNDED reads of the harness's integration points, then WRITE. NO git. One tool call per round. Appends ≤ 6,000 chars. Receipts per claim.

## The crate (inline)
**Serena's true surface (stage-1 bearings):** oraios/serena — a semantic code MCP server (LSP symbol-level: find_symbol / rename_symbol / replace_symbol_body / insert_after_symbol; basics: search_for_pattern / replace_content / read_file / list_dir / execute_shell_command, typically disabled inside harnesses). NO LLM endpoint — an LLM orchestrates its tools. The host's instance runs STDIO-bound (launched by its client; the 24282 HTTP face = the dashboard only; `/mcp` 404s without `--transport streamable-http`). The tunnel rig→host is live; the host-side restart with the flag is the HTTP option (or the stdio-launch route: the executor starts the server itself — no host change).
**The write-problem class (the why):** five ride-failures tonight (read-scatter ×3, write-overwrite ×1, commit-phase ×1); the harness hardened (the fold-step + the write-only briefs). The field's corroboration (veneta's 9,759-turn counts): the model-emitted call is the flaky axis; the EXECUTION side's determinism is the fix.
**The storm-steer's shape (binding):** the harness's `execute()` gains an OPTIONAL MCP-executor leg — a local MCP client (Python SDK `mcp>=1.27,<2`) to Serena (stdio-launch preferred; HTTP after the host flag) — routing the lanes' WRITE-type calls through Serena's tools (symbol-level where they fit; replace_content/write patterns where not). The DEFAULT writer stays the default; the flag OFF = zero change. The receipt floor: success is not a postcondition — the executor's receipt = the re-read byte-check. The two-way door: the flag + the executor process + the tunnel = the config delta; rollback = drop all three; success = N compose-lane landings with zero write-class failures; exit = two failures.

## Your bounded reads (≤ 3, then WRITE)
1. `/root/scripts/copycat-harness.py` lines ~440–485 — the tool dispatch (`execute(fn["name"], args)` + the write-window gate + the fold-step) — the leg's integration point.
2. `/root/scripts/copycat-harness.py` lines ~225–245 — the `write_file` handler (where the lane's write calls already land).
3. Optional: the harness's `parse_args` (lines ~60–135) — the tool schemas.
Then WRITE. No other reads.

## The deliverable — `SERENA-HARNESS-PLAN-20261115.md`
1. **THE LEG'S DESIGN** — the flag (`--executor mcp` / env `HARNESS_EXECUTOR=mcp-serena`), the executor process (the stdio-launch route: the harness spawns the MCP client + serena's start command; OR the HTTP route after the host flag), the write-call routing (which lane calls route to Serena's tools vs the default writer — the write_file handler's decision point), the call-result pairing (one call one result, the mcp-session protocol), the bounded-results (the tool outputs truncated to the harness's result budgets).
2. **THE RECEIPT FLOOR** — the postcondition check: after Serena's write tool returns, the executor re-reads the artifact (hash/cmp vs the intended bytes) before the result rides back to the lane; the fold-step's verification unchanged. "Success is not a postcondition" — implemented as the re-read, never the tool's word.
3. **THE TWO-WAY DOOR, EXACT** — the config delta (the flag, the executor, the tunnel), the rollback (drop the flag → the standard writer resumes; kill the executor; close the tunnel), the success criterion (N=3 compose-lane landings through the leg, zero write-class failures) and the exit criterion (two failures → the door closes; the design note preserved).
4. **THE TEST PLAN** — the minimal live probe: one write-only compose brief (a small artifact) through the leg on a live seat; the pass = the artifact lands with the re-read receipt; the meters recorded.
5. **THE HONEST MARKERS** — what's unverified (the host's serena version's tool list unread — the LSP backend's language coverage; the stdio-launch's process-lifetime on Windows; the SDK availability rig-side) — ABSENT stays ABSENT + named.

## Binding
- The RFC + upstream stay QUIET; nothing posts; the tunnel is local. The stage ends with the artifact > 6,000 chars, all five sections. No git.
