# NEMO STAGE 1 — THE SERENA BEARER (2026-11-15) — map the surface, design the two-way-door wiring

## Your role (fleet asset, budget-conscious)
You are Nemo — 2-3 STAGE assignment, sequenced so your budget is respected: STAGE 1 (you) = the SERENA SURFACE'S TRUE MAP + the wiring options + the two-way-door plan. Stage 2 = the planner (the harness-integration design, from your bearings). Stage 3 = the verifier. Your ride: bring the bearings home. Everything you need is below — bounded probes only (the surface's transport), then WRITE.

## The project (the operator's hypothesis, 2026-11-15)
Serena (the local MCP server on the Windows host) might be a FREE solution to some of the rig's WRITE problems (the compose-lane write contracts: read-scatter, write-overwrite, commit-phase failures — five receipts tonight). A two-way door: wire it into the harness IF it fits; back out cleanly if not. YOUR JOB: the map + the options + the reversibility plan.

## The bearings (probe receipts, inline)
- The host: `desktop-8r44vep` (Windows), tailnet `100.70.143.25`, SSH OK as c0wb0y.
- The process: `serena.exe start-mcp-server --context claude-code --project Downloads` — from the user's uv cache (`AppData\Local\uv\cache\archive-v0\...\Scripts\serena.exe`), PID 15564 (at look-time).
- The HTTP service: port `24282` (127.0.0.1, loopback-only) — **Werkzeug/3.1.7 Python/3.13.15** web app; GET / → 302 → `/dashboard/`; POST / → 405; `/mcp`, `/sse`, `/mcp/sse`, `/health`, `/v1/models` → 404. An SSH tunnel rig-side is LIVE (`127.0.0.1:24282` rides the rig now).
- The port 22212's listener (50075/57677) = GitHub Copilot's github.exe — NOT serena; ignore.
- The rig's write-problem context (the why): five compose-lane rides failed tonight (read-scatter ×3, write-overwrite ×1, commit-phase ×1); the harness was hardened (the fold-step + the write-only briefs). Serena's fit = a LOCAL, free, deterministic write surface (MCP tools) the harness could call as an executor leg.

## Your bounded probes (≤ 5 total, then WRITE — the budget rule)
1. `GET http://127.0.0.1:24282/dashboard/` — the app's face: what it serves, what it names (the MCP path? the tools? the docs?).
2. `GET/POST` the dashboard-adjacent API routes the face names (`/api/*`, `/openapi.json`, `/docs`) — the transport's documented surface.
3. If an MCP route emerges: initialize + tools/list (the protocol 2025-06-18; the session header's `mcp-session-id`).
4. One optional host-side read: the serena help (`serena.exe --help`) — via the SSH route — to name the server's canonical MCP transport.
5. Nothing else. Then WRITE.

## The deliverable — `SERENA-BEARINGS-20261115.md` (write-first; skeleton by round 3; appends ≤ 6,000; NO git; receipts per claim)
1. **THE TRUE SURFACE** — what Serena serves (the dashboard's content, the app's nature, the MCP transport + tools IF found; otherwise the named ABSENTs: the MCP route unconfirmed, the tool inventory unread).
2. **THE WIRING OPTIONS** (each with its shape + its reversibility): (a) the harness MCP-executor leg (the harness's tool executor calls Serena's tools over the tunnel as the write surface — the design sketch: where it plugs, what it replaces, the fallback to the current writer if it degrades); (b) the MCP-client connector route (the rig's gateway connects as an MCP client; serena's tools become callable rig-side); (c) the host-side script route (the harness's terminal executor calls serena via the ssh route). Options evaluated against the write-problem classes (which option kills which failure).
3. **THE TWO-WAY-DOOR PLAN** — the reversible entry: the exact config delta (the tunnel, the endpoint, the harness flag), the named rollback (remove the flag, drop the tunnel, the old writer returns), the success criterion (a compose-lane landing through Serena's tools with zero write-class failures in N landings) and the exit criterion (two failures → the door closes, the standard writer resumes).
4. **THE STAGE-2 SEED** — the exact input the planner needs (the confirmed surface facts, the chosen option's sketch, the harness's integration points to read).
5. **THE HONEST MARKERS** — every ABSENT named (the MCP route, the tools, the model/API nature of Serena — it may be an MCP server WITHOUT an LLM endpoint; that reality determines the wiring).

## Binding
- The RFC + upstream stay QUIET; nothing posts; the tunnel is local. The stage ends with the artifact > 5,000 chars, all five sections. No git.
