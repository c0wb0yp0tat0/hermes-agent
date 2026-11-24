# Cloudflare OS — Research Collation & Hermes Application

*Compiled from live source verification on 2026-08-05. Sources: Cloudflare press release (cloudflare.com, cloudflare.net/BusinessWire), the launch blog post (blog.cloudflare.com/cloudflare-os), companion posts (Agent Access Model, WriteGuard, how-we-use-ai-with-cloudflare-os), the GitHub repo `cloudflare/cloudflare-os`, the `cloudflare-os-starter` deploy repo, Cloudflare developer reference-architecture doc, and corroborating discussion (Hacker News w/ Kenton Varda, AI Gateway custom-provider docs, Cloudflare Access self-hosted-app docs).*

---

## 0. Verification verdict

**GENUINE, not a hoax or hallucination.** All primary sources are Cloudflare-owned. Dates: press release dated Aug 4, 2026 (Business Wire / investor); blog + GitHub public-release activity Aug 5, 2026. Repo is live: Apache 2.0, ~1,000 stars, 47 forks, 622 commits, latest commit hours before this research.

Every capability in the original news alert was confirmed against primary sources. No factual errors found in the alert (if anything it understated the security model).

---

## 1. What Cloudflare OS actually is

- **NOT a traditional OS.** Metaphorical: (a) an OS *for the company* to be productive with AI safely; (b) an OS *for AI workloads*. Explicitly stated in README.
- **Origin:** internal Cloudflare tool. v1 (May 2026) gave every employee an agent workspace. v2 (Aug 2026, this open-source release) is a **complete rewrite** rebuilding on a new security foundation.
- **Stack:** TypeScript (96.5%), built on Cloudflare Workers, Durable Objects, Agent SDK, AI Gateway, MCP Server Portals, Dynamic Workers, Sandbox SDK containers, Browser Run.
- **Three pillars:**
  1. Agent workspace (chat UI preloaded with curated company context/skills; isolated runtime for code).
  2. Sandboxed app dev — agents build **"gadgets"** (small personal apps) with isolated state, safely shareable.
  3. **Gatekeepers** — security/governance framework; non-technical users "can safely go nuts and nothing bad will happen."
- **OS-analogy table (from README):**
  | Normal OS | Cloudflare OS |
  |---|---|
  | kernel | `packages/workshop-backend` |
  | device drivers | `packages/gatekeeper-*` |
  | shell | `packages/workshop-frontend` |
  | processes | gadgets |
  | executables | blueprints |
  | users | users |
  | ACLs | shared permissions |
  | ??? | agents |

---

## 2. Area A — Self-hosting: what you actually get

Three deployment shapes:

| Path | Status | Notes |
|---|---|---|
| `pnpm run-local` | ✅ now | Whole stack on wrangler/workerd locally. Dev/demo only. State in `.wrangler/`. |
| `cloudflare-os-starter` → your CF account | ✅ now | Pinned upstream, your branding, Cloudflare Access sign-in, your KV/R2, opt-in AI. |
| `workerd` on your own bare metal | ⚠️ "COMING SOON" | README points to raw `workerd.capnp`; not documented/production-ready. |

### SANITY CHECK (verified against Kenton Varda, top repo committer, on HN):
> "workerd itself is a runtime for Workers and Durable Objects, but is not intended to provide implementations of other services like KV, D1, etc. Wrangler/miniflare provides implementations for local testing, but these aren't meant for production."

**"Runs on your own servers" is true only for the Workers + Durable Objects layer.** The OS also requires **KV** (workspace registry), **R2** (file/context storage), **Browser Rendering**, and **Dynamic Worker Loaders** — none implemented by `workerd`. A production bare-metal deploy requires you to supply those equivalents (miniflare's are dev-only; OpenWorkers offers OSS bindings). Undocumented today.

**"Open source" caveat:** Apache 2.0 = read/fork/modify/self-host freely. BUT README: *"At this time, we are not seeking outside contribution"* — only trivially-verifiable PRs accepted. You fork and own your branch; you don't push back easily.

---

## 3. Area B — Security architecture & Gatekeepers (the real substance)

### B1. Gatekeepers (shipped, in repo)
- Like "supercharged MCP servers." One spawned per external connection.
- Wraps service's native API in a clean typed surface; handles OAuth; enforces **narrow, resource-specific** access; **logs every action**; requires **human approval** for side effects.
- **Capability-based, not ACL:** agent gets typed binding (`env.PROJECT.listIssues({teamId})`); underlying credential **never enters agent or generated code**.
- Server code runs in Dynamic Worker with **global outbound networking disabled**; client code in sandboxed browser frame. Neither reaches internet except via explicit capability.

**Novel bit — deferred (asynchronous) human-in-the-loop:**
> "When the agent performs an action that requires approval, the Gatekeeper will *simulate* the outcome locally, allowing the agent to proceed and queue up more actions… gives it simulated results. Once the agent is done, the user may approve or reject the actions in bulk, or one-by-one, later."

Confirmed in `gatekeeper-homeassistant` README: after `entity.turnOn()`, immediate `entity.getState()` returns `state:"on"` *though HA wasn't touched* — simulated post-action world. Nothing writes until you approve the batch.

### B2. Agent Access Model (AAM) — PROPOSED reference architecture (not all wired in v2)
Insight: *shrink the capability so there's less to judge*, not "smarter per-request AI decisions."
1. Credentials short-lived + sender-constrained (OAuth Token Exchange RFC 8693 + DPoP RFC 9449); model never sees token.
2. Enforcement in harness + network, **not the prompt** — *"A boundary you can talk your way past is not a boundary."*
3. Human oversight is **exceptional** (approval fatigue → reflexive clicking is the failure).
4. Grants reviewed from evidence; system proposes change for *future* tasks; never widens *active* task.
5. Capability state moves one way (Trust Ratchet only *removes* authority).

### B3. WriteGuard (Cloudflare-INTERNAL, private beta — NOT in open repo)
- Built before expanding agent write-access across their MCP servers. Motivating story: agent closed thousands of tickets/hour; logs couldn't distinguish Joe's manual closes from his agent's.
- Risk tiers: Read Only → Minimal Impact → Contained Write → Critical (merge_mr, prod deploy, bulk-delete).
- "Keep the person, add the agent" — agents act with employee's permissions; WriteGuard stamps each write with agent session + client context (attribution). Audit events async (zero added latency).
- **Pattern to copy** when writing your own Gatekeepers, since the open repo's Gatekeepers already do per-action logging + human approval.

**Shipped-today vs. aspirational line (draw sharply):**
- Enforced in repo: zero-by-default agents, typed capability bindings, outbound-disabled server code, deferred human approval, per-action logging.
- Proposed in paper: short-lived sender-constrained task creds, Trust Ratchet, full five-principle system.
- Internal-only: WriteGuard risk-tiering/attribution.

**Note:** "Gatekeepers" (Cloudflare OS's own abstraction) ≠ hosted "MCP Server Portals" product that WriteGuard attaches to. Related but distinct; keep separate.

---

## 4. Area C — You have a CF account + domain + cloudflared tunnel. Two topologies.

### Topology 1 — kernel on Cloudflare (public, shareable, Zero-Trust)
- Deploy `cloudflare-os-starter` to your CF account; your domain behind **Cloudflare Access** (self-hosted app mode, Zero Trust).
- LAN services reached via **cloudflared tunnel** to CF egress (required — Gatekeepers call out from CF).
- Self-hosted model reached via **AI Gateway custom provider** → your tunneled OpenAI-compatible endpoint. (Verified: AI Gateway supports custom base URL + upstream API-key header.)
- State in your KV/R2; SSO via your domain; easy external sharing.

### Topology 2 — kernel on your LAN (home-lab, LAN-native)
- `pnpm run-local` (or future `workerd`) on a machine on your network.
- **Gatekeepers reach LAN services directly** — `gatekeeper-homeassistant` README: *"On a self-hosted (workerd) deployment, LAN addresses like `http://homeassistant.local:8123` work fine — intended setup for users running Gadgets on same network as their HA."* No tunnel needed for LAN resources.
- Tunnel only needed if you want **remote access to the OS itself**.

| | T1 (kernel on CF) | T2 (kernel on LAN) |
|---|---|---|
| OS location | your CF account | your machine (run-local/workerd) |
| LAN services | tunneled to CF egress | direct LAN |
| self-hosted model | tunneled HTTPS → AI Gateway | local HTTP if bypass gateway |
| identity/SSO | Cloudflare Access (real ZT) | built-in passwd or front w/ Access |
| persistence | your KV/R2 | `.wrangler/` local |
| external sharing | trivial | need to expose OS (tunnel) |
| maturity | ✅ starter | run-local ✅; workerd prod ⚠️ |

**Model-reachability nuance:** On T1, inference goes "over HTTPS with tokens" (public internet) → self-hosted model **must be publicly reachable** (tunnel supplies it). On T2 (local workerd), backend could call LAN model directly if you bypass AI Gateway (`CF_AI_GATEWAY_WAI_DIRECT=true` for Workers AI; fully custom local model path = verify at deploy, repo's model story centers on CF AI Gateway + Workers AI).

**"Self-hosted" honesty:** In both topologies the *OS kernel* runs on Cloudflare's platform (your account) or your LAN. You truly own: account, domain, data, config, backing services, models. You do NOT run the kernel on bare metal unless you take the ⚠️ "COMING SOON" workerd path with self-supplied KV/R2/etc.

---

## 5. REFRAME — Applying this to improve Hermes (a self-hosted agent)

**Key insight from the user:** Cloudflare OS is a published *reference design for safe self-hosted agents*. Hermes is itself a self-hosted agent. So the question is what design patterns to lift to harden Hermes — not how to deploy their product.

### Hermes already mirrors the OS analogy
| Cloudflare OS | Hermes analog |
|---|---|
| kernel `workshop-backend` | Hermes runtime connecting tools↔model |
| `gatekeeper-*` | tool adapters (terminal/file/browser/web/image) |
| `workshop-frontend` | webui/chat on `0.0.0.0:8787` |
| gadgets | **subagents + cron jobs** |
| blueprints | **skills** |
| users | profiles (default, sub-profiles) |
| agents | the agent (me) |
| curated context/skills library | `~/.hermes/skills/`, memory, session_search ✅ (already done) |

**The one missing layer = capability-based security (zero-by-default agents + human-in-the-loop Gatekeepers).** Everything else Hermes already does. Because the user operates Hermes headlessly (accessibility bridge), a "non-technical operator can safely go nuts" posture is exactly the wanted end state.

### Principle-by-principle gap audit
| AAM / Gatekeeper principle | Hermes today | Gap |
|---|---|---|
| Agents start with zero access | ❌ runs as **root, ambient broad tool access** | biggest gap |
| Credential isolation (key never reaches agent) | ⚠️ keys in config/env, not context; but no capability-binding abstraction | no typed capability layer |
| Prompt is not a perimeter | ✅ instructed not to trust tool-output instructions; enforcement still prompt-based | need harness/network enforcement |
| Inline enforcement in harness/network | ⚠️ terminal flagged `curl|python3` as security HIGH + smart-approval (real inline gate, but heuristic/spot-check) | no consistent policy framework |
| Human oversight exceptional (deferred) | ❌ synchronous per-call approvals (`clarify`, tool confirms) | matches Cloudflare's pre-v2 pain |
| Trust Ratchet (capabilities only shrink) | ❌ subagents can be scoped (`enabled_toolsets`) but no ceiling that only removes | missing |
| Auditability (queryable tool/consent log) | ⚠️ session transcripts (session_search) = narrative audit; no structured risk-tiered log | medium gap |
| Identity gate before access | ✅ Tailscale + password on webui (Cloudflare Access analog) | gap is *authorization after auth* |

### Two parts mapping onto the user's real environment
- **The planned LM Studio box `192.168.1.70:1234`** = literal Area-C "bring your own self-hosted model over LAN" (Topology 2). Once up, Hermes routes to it instead of a vendor → private, no lock-in, data stays local. On the user's forward plan ("add SSD / stand up other machines"). Currently unreachable.
- **Tailscale + password gate = the Access layer.** Cloudflare's lesson: identity alone insufficient for agents; you also need *authorization* (what the authenticated agent may touch, with whose consent). That Gatekeeper layer Hermes lacks.

### Proposed improvements (Tier / feasibility)
**Tier 1 — buildable now with Hermes's own tools (skills/config/subagent patterns/LAN model wiring):**
- **"Gatekeeper" skill:** pre-tool-call checklist forcing explicit scoped capability grant before touching sensitive resources (system files outside `/root/workspace`, secrets, destructive commands, external sends). Open-source analog of Cloudflare Gatekeepers, enforceable at harness boundary.
- **Audit/WriteGuard-analog skill:** every tool call logged locally with risk tier + consent decision, queryable later (serves TTS review).
- **Capability-scoped subagents by default:** `delegate_task`/`enabled_toolsets` to spawn zero-by-default children (e.g. research subagent with only web/file, no terminal).
- **Bring LM Studio LAN model online:** wire Hermes to `192.168.1.70:1234` as private inference endpoint (contingent on box existing).

**Tier 2 — need Hermes platform change (propose to project, can't unilaterally do):**
- True zero-by-default capability system (typed bindings; credential never in context).
- Deferred/batch human approval (simulate-and-proceed, approve later) — hard for synchronous chat agent, viable in cron/delegate loops.
- Native per-action audit + consent logging.

### Recommended priority order (for a headless operator)
1. Tier-1 Gatekeeper skill (safe-by-default without supervision).
2. Tier-1 audit skill (voice-reviewable "what did it do" trail).
3. Bring LM Studio box online (private local inference; dovetails with hardware roadmap).

---

## 6. Open items / follow-ups (NOT acted on)
- No skills built, no memory written, no LM Studio wiring performed per user instruction ("take no further action").
- Deferred user choices offered: (a) build Gatekeeper skill, (b) build audit skill, (c) draft LM Studio online steps, (d) write Tier-2 platform proposals for Hermes project, (e) none.
- Bare-metal production deploy remains blocked on workerd's missing KV/R2/Browser-Rendering/Dynamic-Loader implementations (undocumented; "COMING SOON").

## 7. Source list (for re-verification)
- https://github.com/cloudflare/cloudflare-os (README, wrangler.jsonc, gatekeeper-homeassistant README, public-server.md, oauth-signin.md, ai-gateway-billing.md)
- https://github.com/cloudflare/cloudflare-os-starter (README)
- https://blog.cloudflare.com/cloudflare-os/
- https://blog.cloudflare.com/the-agent-access-model/
- https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/
- https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-os-is-the-first-ai-workspace-built-around-how-companies-actually-work/
- https://developers.cloudflare.com/reference-architecture/diagrams/ai/enterprise-ai-agent-workspace/
- https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/
- https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/
- Hacker News discussion (kentonv): workerd = Workers+DO only, not KV/R2/etc.
