# FIVEWHY-STORM-20261101 — The Field's Answers to the Rig's Root

**Mission:** Five-Why Web Storm. The storm lands on the root; it does not wander.
**Date:** 2026-11-01
**Deliverable:** `/root/workspace/drop/deepdive-mission-flow/FIVEWHY-STORM-20261101.md`
**Contract:** nothing public; the storm informs; the design stays ours.

## The Root (the five-why's output, from the rig's own record)

One stale gateway process — the "manual restart still pending" marker (pid 1480227, pre-update code serving, fallback chain unloaded) — sits under five layers of repeating failure:

1. The fallback not engaging.
2. The kanban owner-refusals.
3. The model 404 class.
4. The repeated 503s.
5. The stalled sequences.

A single restart from outside the gateway's tree collapses all five. The rig's designs must NOT depend on that act being remembered. The storm's job: find the field's canonical shapes so the rig can be armed against each layer without depending on a manual restart.

The marker is real and recurring across the rig's own run logs (e.g. `RFC-143379-APPROACHES-20261024/*.log`: `⚠ dashboard [default] pid 1480227: manual restart still pending; this process may still serve pre-update code.`).

## Q1 — Config-loading without manual restarts

**Question:** how do real systems load provider/fallback/rotation config changes without a process restart — hot-reload patterns, config-watch mechanisms, graceful-reload designs? Canonical shape.

### Pattern A — Atomic file-watch + validate-before-apply + pointer swap (the in-process canonical)

Mechanism: the process does not read config once and freeze it. It watches the config file (OS-level `inotify`/fsevents via a `watchdog`-class library, or polling fallback ~5s). On change: debounce (writes settle), re-parse, build a *new complete* config value, swap the pointer atomically (no in-place mutation — readers see old-or-new, never torn), then notify observers (subsystems subscribe once and react). Validate before apply; on invalid config, keep the last good config and alert (fail-safe, not fail-stop). Atomic-replace on write: write to temp file in same dir, `rename()` over target (reader sees entire old or entire new). Source: MCP Hangar hot-reload docs; Big Iron "Runtime config hot-reload"; phpboyscout "Reloading config without a restart" (arc-swap / Viper-style atomic swap + `watch::Receiver` observers).

Key canonical details:
- Triggers: file watcher (inotify, ~1s with watchdog; polling up to 5s default), SIGHUP (immediate, queued to a worker thread so the gateway keeps answering), MCP/REST tool (`POST /api/config/reload`), manual.
- Concurrency: reloads run one at a time; a second queues and applies after (`config_reload_waiting`); graceful drain up to 30s.
- Restart-only matrix: ports/sockets, worker counts decided at init, plugins/modules, memory layout, privilege drops, TLS/core directives, and "changes to the watch behavior itself" cannot hot-reload. Everything else (log levels, timeouts, rate limits, routing rules, upstream/backend lists, feature flags) is hot-reloadable.
- Honest partial-reload trap: a daemon may report "reload succeeded" while a setting it cannot move live (port) silently stays on the old value. Defense: know and document the reloadable-vs-restart matrix per service; verify the change took effect (new port listening, new limit enforced), never trust "reload succeeded."

### Pattern B — Graceful handoff / new-instance-alongside-old (the zero-dropped-connections model)

Mechanism: on reload, spin up a NEW engine instance alongside the old one with the new config; route new traffic to the new instance; in-flight work completes on the old one; old instance retires after a grace period (default ~30-60s). Memory roughly doubles during grace; planner cache cold on new instance (brief latency bump). WebSocket/SSE connections on old instance close at retire; clients reconnect. Source: Cosmo by WunderGraph GraphQL Router config hot-reload; nginx graceful reload (SIGHUP → new workers with new config, old workers stop accepting new connections but finish in-flight, exit when drained).

### Pattern C — Mutable-config option marking (the declared-mutability model)

Mechanism: config options are explicitly marked 'mutable'; only mutable options can be reloaded at runtime (via SIGHUP or `mutate_config_files`); non-mutable require restart. Three cases on mutation: option checked every time (takes effect immediately), cached on the stack (needs invalidation), wired at init (restart-only). Source: OpenStack oslo.config mutable config.

### Field canonical shape (the synthesis)

The canonical shape is a **three-part contract**: (1) a **trigger layer** (file watcher + SIGHUP + API endpoint, all funneling to one queued reload worker), (2) a **validate-then-atomically-swap layer** (validate new config fully before apply; build new complete value; atomic pointer swap; observers notified; invalid → keep last good), and (3) a **declared reloadable-vs-restart matrix** so partial reloads are never silent. Plus the **graceful handoff** (new instance alongside old, drain, retire) when the running thing cannot be mutated in place. And the **honest verification step**: "reload succeeded" ≠ "change took effect."

### Application to the rig's root (Q1 → stale gateway layer)

The rig's stale-gateway layer (pid 1480227 serving pre-update code; fallback chain unloaded) is exactly the failure mode Pattern A prevents: config changes (provider/fallback/rotation) that require a process restart because the gateway has no hot-reload path. The "manual restart still pending" marker is the tell. The field's answer: arm the gateway with a **config-watch + atomic swap + declared reloadable matrix**, OR (if hot-reload is too costly) make restart **cheap and graceful** (rolling restart behind a load balancer / SO_REUSEPORT handoff) so the restart is no longer a remembered act. The Cosmo/nginx graceful-handoff model is the zero-dropped version.

## Q2 — Channel-resilient dispatch

**Question:** how do production dispatch layers absorb provider windows (503/429/404) without stalling dependent sequences — retry budgets, circuit breakers, rotation policies, health-aware routing? Field default.

### Pattern A — Retry classification + retry budget + wait cap (the Kaana shape)

Mechanism: a failed attempt is retried on the same route only when (a) nothing has been delivered yet, (b) the failure is transient-and-deployment's (`rate_limited`, `provider_overloaded`, `provider_timeout`, `provider_error`/`server_error`), (c) retried fewer than `MaxRetriesPerRoute` (2) times, (d) the wait fits the request's remaining budget (15s). Wait = per-route backoff (1s base, doubling, equal jitter) or provider's `Retry-After`, whichever is longer; a `Retry-After` the budget cannot absorb is not waited for — the request moves on, or fails with the provider's hint. Non-transient (invalid request, model not found, permission denied, content filter, billing/quota, cancellation, unclassified) are never retried on the same route. Same-route retry is a full attempt: passes `Admit` again (never bypassing an open/half-open breaker), reports its own outcome, own cost row; not a route switch. Source: Kaana routing docs (`kaana.RetryPolicy`, `transientFailure`).

### Pattern B — Circuit breaker with failure classification + half-open probe + fail-open (the Switchyard/build-your-own-gateway shape)

Mechanism: per-deployment (or per-provider-id) breaker, state in shared store (Redis) so one OPEN decision protects every replica. States Closed/Open/HalfOpen. HalfOpen admits exactly one probe; success closes + resets failure count; transient failure reopens for another cooldown. Failure counted only after retry budget exhausted, not per HTTP attempt. Failure classification: transport, timeout, 408, 429, 5xx are transient (count); request-specific/local failures (context-window overflow, invalid request, auth, deterministic 4xx, config errors) do not open. 429/Retry-After specifically: NOT tripped (it's a working rate limiter — tripping converts throttle into outage); instead route into a token bucket sized from Retry-After. Cooldown expiry → bounded recovery; half-open recovery works even with background health checks disabled. Fail-open: if the store errors, proceed as if CLOSED (breaker is an optimization, not a dependency). Source: NVIDIA-NeMo/Switchyard#594; build-your-own-ai-gateway reliability docs; webhook-architecture circuit breaker patterns.

### Pattern C — Health-aware routing with penalty-not-ban + floor guarantee (the AWRR shape)

Mechanism: health-weighted smooth weighted round-robin. Penalty, not ban: unhealthy key stays selectable but less frequently; selection probability never drops below 50% of initial share within the same pool/tier (floor guarantee). Time-based recovery: exponential decay of consecutive-error penalty (half-life ~10min) so a key recovers without new errors. Retry path: "recover-to-best" — on retry, bypass SWRR, pick healthiest (highest multiplier) first. Alias isolation: health/penalty per `providerKey`, never shared across aliases. Two state machines that must not drift: deployment breaker (takes a deployment out) vs credential health (retires one key, moves to next key of the pool). Source: Kaana AWRR health-weighted routing doc; routecodex.

### Pattern D — Health scoring + deployment availability (the AxonHub/DeltaLLM shape)

Mechanism: error-aware strategy scores channels (base 200, -30 per consecutive failure decaying over cooldown, -40 for recent failure within 5min time-decaying); rate-limit-aware strategy tracks RPM/TPM/concurrency in 1-min sliding window, -10000 points (ranked last fallback) when exhausted or on 429 Retry-After cooldown. Routing: priority grouping → session consistency (same conversation prefers previously successful channel) → health awareness (avoid high-error channels) → weighted round-robin → latency awareness → rate-limit awareness. Deployments removed when unhealthy/cooled-down; cooldown expiry → bounded recovery (half-open). Source: AxonHub load-balance guide; DeltaLLM routing.

### Field default (the synthesis)

The field default is a **layered stack**, not a single mechanism:
1. **Retry layer** (same-route, bounded): retry budget 2, wait cap 15s, transient-classification only, never retry after delivery.
2. **Failover layer** (authorized route list, ordered): move to next authorized route only while nothing delivered; announce route_switch at replacement attempt.
3. **Circuit breaker layer** (per-deployment, shared state, fail-open): open on exhausted retries; half-open probe on real traffic (never synthetic); 429 → cooldown/token bucket, NOT trip.
4. **Health-aware routing layer** (penalty-not-ban with floor guarantee + time decay + recover-to-best on retry): so degraded keys stay selectable but deprioritized, and recover automatically.
5. **Health monitor layer** (observability, not routing authority): providers without health_check_url → UNKNOWN; routing never consults provider_health (it's observability, not a gate).

The key discipline: **one function decides attributability** (`provider.AttributableCategory`); breakers and retry read the same one, so they can never drift apart. Customer faults, content filters, cancellations, unclassified failures trip nothing and are retried nowhere.

### Application to the rig's root (Q2 → fallback-not-engaging / 503 / 404 layers)

The rig's "fallback not engaging" + "repeated 503s" + "model 404 class" layers map directly: the fallback chain is unloaded (stale gateway), so none of the retry/failover/breaker/health layers are armed. The field's answer: arm the dispatch layer with **retry budget + circuit breaker + health-weighted routing + a single attributability function**, so a 503/429/404 on one channel routes around it automatically instead of stalling. The 404 class (model not found) is explicitly non-retryable/transient in the field's classification — it must be caught at assignment time (Q4), not retried at dispatch time.

## Q3 — Sequence fragility

**Question:** how do orchestrated pipelines hand off when a leg fails — failover patterns, gap-honest handoffs, sequence-resilience designs (so one leg's channel failure never freezes an armed end-to-end flow)?

### Pattern A — Checkpoint-based cross-pipeline handoff with idempotency (the Pipeline Framework shape)

Mechanism: reliable handoff is orchestrator-owned and checkpoint-based. Source pipeline publishes a named checkpoint; target admits it through a mapper-backed subscription. Transport/broker binding/retry ownership stay in the runtime shell. Idempotency: preserve incoming dispatch identifiers when present, else derive a repeat-safe handoff key from configured checkpoint fields. Downstream retry/DLQ remains orchestrator-owned after background admission. Build-time validation checks checkpoint boundary declarations + mapper compatibility. Reliable handoff supported only for QUEUE_ASYNC orchestrators (rejected for FUNCTION pipelines). Live Subscribe is a weaker observer/tap, not the reliable path. Source: pipelineframework.org checkpoint handoff.

### Pattern B — Journal + lease-based failover recovery with at-least-once semantics (the Stepflow shape)

Mechanism: orchestrator killed and stays dead → surviving orchestrator detects orphaned run via etcd lease expiry, claims it, replays the journal, resumes execution. Steps whose completion was durably journaled before the crash must NOT be re-executed; in-flight steps MAY be re-executed (at-least-once). Idempotency keys (`executionId:stepIndex:attempt`) enforce dedup at boundaries. Crash matrix: before state commit → redeliver/re-execute (high dup risk); after state commit before next enqueue → transition stored, next dispatch stalls until due sweeper re-dispatches (low dup); during retry scheduling → persist retry intent before enqueue (medium); after external side effect before commit → side effect may repeat (high) — downstream dedupe keyed by transition identity; coordinator dies while lease held → lease expires, another claims (low); remote caller deadline expires → parked as `REMOTE_OUTCOME_UNKNOWN`, confirm disposition before re-drive. Source: stepflow recovery tests; pipelineframework error handling.

### Pattern C — Stage-gate loop with concentrated hardening at fragile handoffs (the conf-pipeline-orchestration shape)

Mechanism: orchestrator is an aggregator with internal recurrence, not a pass-through — holds and integrates, reconciles conflicts, checks the gate, decides whether artifact is good enough before issuing next command. Stage-gate loop: GROUND → for each stage: SPAWN worker (with explicit output path + return contract) → VERIFY (read returned artifact's status/confidence fields, not prose; retry fragile node or escalate on missing/low/failed; do not advance) → INTEGRATE (reconcile against prior stages; hold, don't pass through; check gate incl. diversity floor) → CHECK INVARIANTS → ADVANCE or ESCALATE. Concentrated hardening: protect the fragile medium-load nodes (the handoffs where failure cascades), not the resilient hubs — retries/verification/extra confidence checks at the fragile nodes (e.g. elicit→schedule handoff, enrichment fan-out), leave robust hubs alone. Source: claude skill `conf-pipeline-orchestration`.

### Pattern D — Gap-honest handoff (the rig's own earned doctrine + field's "honest state")

Mechanism: when a leg fails, the handoff names the gap honestly rather than spinning "in motion." The artifact beats the process name — the head lands the deliverable itself from the verified record when the designated lane's channel fails repeatedly. "Where is it?" is answered with the FILE (path, URL, hash), never lane statuses/retry counts/provider excuses. Failures are findings, not dead ends — report the named mechanism, the fix, the re-verification. Non-reproduction is a question, not a stop (the wall clause). Source: rig's own earned doctrine (think-tank/head-supervisor skills) + the field's "honest state report" discipline.

### Field default (the synthesis)

The field default is **checkpoint + journal + stage-gate + gap-honesty**:
1. **Checkpoint publication** as the handoff primitive (named, typed, idempotent key, orchestrator-owned retry/DLQ).
2. **Journal + lease** for crash recovery (replay from last durable journal; at-least-once in-flight; idempotency keys at boundaries).
3. **Stage-gate loop** with VERIFY-before-ADVANCE (read artifact fields, not prose; escalate on failure; never auto-advance on a phantom).
4. **Concentrated hardening** at the fragile handoffs (retries where cascades happen, not uniformly).
5. **Gap-honest handoff** when a leg fails: name the gap, land the artifact from verified record, never spin "in motion."

The invariant: **one leg's channel failure must never freeze an armed end-to-end flow** — the flow advances on the verified artifact or escalates with the gap named, never stalls silently.

### Application to the rig's root (Q3 → stalled-sequences layer)

The rig's "stalled sequences" layer is the failure mode Q3 addresses: a leg's channel failure (503/404 on the stale gateway) freezes the armed end-to-end flow. The field's answer: arm the sequence with **checkpoint publication + journal/lease recovery + stage-gate VERIFY-before-ADVANCE + concentrated hardening at the fragile handoffs (the channel-dependent legs) + gap-honest handoff**. The rig's own earned doctrine (artifact beats process name; failures are findings) is itself the gap-honest variant — the field corroborates it.

## Q4 — Assignment-vs-channel health

**Question:** when a designated model's channel is persistently unstable, what's the field's policy — health-aware assignment, fallback-with-standards, wait-or-rotate decision shapes?

### Pattern A — Tiered assignment with health-filtered pool + per-role offset (the voly shape)

Mechanism: models grouped into tiers (strong/standard/weak) → ordered real-provider preference, filtered by `ProviderHealthChecker`. `resolve_tier_model(tier, checker)` returns (model, provider) from the healthy pool; if none healthy in tier, fall to any healthy non-excluded provider; last resort = anthropic (surfaces clear auth error). `resolve_role_model(role, tier, checker)` adds per-role offset inside the tier pool for distribution. `chat_fallback_providers(tier, role, checker)` returns the ordered provider list to try after primary fails (rotated by role offset). Excluded providers (billing/credit outages) filtered out; mark_unhealthy still applies. Source: voly/a2a/assignment.py.

### Pattern B — Health-weighted assignment with penalty-not-ban + floor + recover-to-best (the AWRR shape, reprised)

Mechanism: assignment probability reduced (never to zero) for recently failing providers; floor guarantee (≥50% of initial share within pool/tier); time-decay recovery (half-life); on retry, snap to healthiest first. Alias isolation (per providerKey). Source: routecodex AWRR; Kaana.

### Pattern C — Fallback chains + context-window/content-policy fallbacks (the DeltaLLM shape)

Mechanism: declared fallback chains: `fallbacks` (general failures: timeouts, rate limits, provider errors), `context_window_fallbacks` (input too large for first model), `content_policy_fallbacks` (provider rejects content for policy). Workload-mode rejection prevents a different-workload group from being reached after a primary failure. Health records per deployment; cooldown expiry → bounded recovery; shared Redis permits one owner-scoped half-open request at a time. Source: DeltaLLM routing & failover.

### Pattern D — Wait-or-rotate decision matrix (the field's policy synthesis)

Mechanism: the field's decision shape is a **triage on attributability + persistence**:
- **Transient + deployment-attributable** (5xx, 429, timeout, transport) → **rotate** (retry same route bounded, then failover to next authorized route; open breaker after exhausted budget).
- **Non-transient + deployment-attributable** (404 model not found, invalid request, permission denied, content filter, billing/quota, cancellation) → **do NOT retry/rotate at dispatch**; the assignment itself is wrong → **re-assign** (move to a different model/channel at the assignment layer, Q4's job) or **surface as GAP**.
- **Persistently unstable channel** (repeated failures across the cooldown window, breaker open and re-opened) → **health-aware assignment** rotates the designation to the next healthy provider in tier; the unstable channel gets a cooldown and decays back (penalty-not-ban, not permanent ban) — so it can recover and re-enter rotation.
- **Wait vs rotate**: wait only when the failure is a working rate limiter (429 with Retry-After) and the wait fits the request budget; otherwise rotate. "Wait for the reset" is the anti-pattern when the channel is persistently unstable — the field rotates and lets the cooldown decay recover it.

The "fallback-with-standards" discipline: fallbacks are declared (not improvised) — general / context-window / content-policy chains, workload-mode-gated, health-recorded, cooldown-bounded. A fallback that fires must be announced (route_switch) and recorded (cost row), never silent.

### Field default (the synthesis)

When a designated model's channel is persistently unstable:
1. **Health-aware assignment rotates the designation** to the next healthy provider in the tier (voly shape), not a manual re-pin.
2. **Fallback chains are declared** (DeltaLLM shape) — general/context-window/content-policy — and fire only on the classified transient classes.
3. **Circuit breaker + cooldown + time-decay** (Kaana/AWRR shape) handles the recovery: the unstable channel is deprioritized (penalty, not ban), cools down, and decays back into rotation automatically.
4. **Wait only for a working rate limiter that fits the budget**; otherwise rotate. "Wait for the reset" is not the policy for persistent instability.
5. **404 (model not found) is an assignment defect, not a dispatch retry** — fix at assignment time (re-pin / re-assign), never retry at dispatch.

### Application to the rig's root (Q4 → wait-or-rotate / assignment-vs-channel-health layer)

The rig's "wait-or-rotate" tension (the designated model's channel persistently unstable; do we wait for the reset or rotate?) is resolved by the field's policy: **rotate at assignment time via health-aware assignment, let the cooldown+decay recover the unstable channel, and never wait for a reset as the default.** The rig's own "stalled lane's head landing" doctrine (head lands the deliverable itself when the channel fails repeatedly) is the gap-honest complement: rotate the assignment, land the artifact from the verified record, don't keep re-dispatching the dead channel.

## ROOT-MAP — which answers collapse which layers

| Rig's five-why layer | Collapsing answer | Mechanism |
|---|---|---|
| Layer 0: stale gateway process (manual restart pending; pre-update code; fallback chain unloaded) | **Q1** (config hot-reload OR cheap graceful restart) | Config-watch + atomic swap + declared reloadable matrix; OR rolling restart/SO_REUSEPORT handoff so restart is no longer a remembered act. |
| Layer 1: fallback not engaging | **Q2** (channel-resilient dispatch) + **Q1** | Fallback chain unloaded because gateway stale; once hot-reloaded/armed, retry+failover+breaker+health-routing engage automatically. |
| Layer 2: kanban owner-refusals | **Q3** (sequence fragility) + **Q4** | Owner-refusals are a sequence-stall class; gap-honest handoff + health-aware assignment let the sequence advance or escalate with the gap named instead of stalling. |
| Layer 3: model 404 class | **Q4** (assignment-vs-channel health) | 404 is an assignment defect, not a dispatch retry — fix at assignment time via health-aware assignment; never retry at dispatch. |
| Layer 4: repeated 503s | **Q2** (channel-resilient dispatch) | 503 is transient+deployment-attributable → retry bounded (2, 15s cap) → failover to next authorized route → open breaker → cooldown+decay recovery. |
| Layer 5: stalled sequences | **Q3** (sequence fragility) | Checkpoint + journal/lease + stage-gate VERIFY-before-ADVANCE + concentrated hardening at fragile handoffs + gap-honest handoff. |

The single restart collapses all five today because all five layers are downstream of Layer 0 (the stale gateway). The storm's contribution: **arm each layer independently** so the rig's designs never depend on the restart being remembered — config hot-reload removes the "remembered restart" dependency (Q1), and the dispatch/sequence/assignment layers (Q2/Q3/Q4) keep functioning even when a channel is unhealthy.

## READY/NOT-READY split

### READY (adoptable into the rig's next armament NOW)

- **Config-watch + atomic swap + declared reloadable-vs-restart matrix (Q1 Pattern A)** — the canonical shape is well-specified and directly applicable to the gateway's provider/fallback/rotation config. Adopt the trigger layer (file watcher + SIGHUP + API endpoint funneling to one queued reload worker), the validate-then-swap layer, and the honest verification step. Ready.
- **Retry budget + transient classification + wait cap (Q2 Pattern A)** — retry 2, 15s cap, transient-only, never after delivery. Ready to encode as the dispatch layer's retry policy.
- **Circuit breaker with failure classification + half-open on real traffic + fail-open (Q2 Pattern B)** — per-deployment, shared state, 429 → cooldown not trip. Ready.
- **Health-weighted routing penalty-not-ban with floor guarantee + time decay + recover-to-best (Q2 Pattern C)** — ready; floor guarantee (≥50%) prevents dead keys.
- **Health-aware assignment tiers with health-filtered pool + per-role offset + ordered fallback providers (Q4 Pattern A)** — ready to replace the rig's designated-model pinning with a health-filtered tier assignment.
- **Gap-honest handoff (Q3 Pattern D / rig's own doctrine)** — already the rig's earned practice; the field corroborates. Ready (already in use; codify).
- **Stage-gate VERIFY-before-ADVANCE with concentrated hardening at fragile handoffs (Q3 Pattern C)** — ready to apply to the rig's leg sequencing (the channel-dependent legs are the fragile nodes).

### NOT-READY (needs a decision)

- **Graceful handoff / new-instance-alongside-old (Q1 Pattern B)** — needs a decision: is the rig willing to double memory during grace and accept a cold planner cache? Also needs a decision on whether to build hot-reload at all vs. make restart cheap (rolling restart / SO_REUSEPORT) — the field says "when restarts are cheap, don't over-engineer." This is a design decision for the rig, not a field default.
- **Journal + lease-based crash recovery with etcd (Q3 Pattern B)** — needs a decision: the rig's orchestrator may not run under etcd/lease infrastructure; adopting this requires choosing the durability substrate (Kafka/checkpoint vs. simpler journal). Checkpoint-based (Pattern A) is lighter and may suffice.
- **Fallback chains declared (Q4 Pattern C) with workload-mode gating** — needs a decision on the chain topology (which models fall back to which) and whether the rig wants context-window/content-policy-specific chains or a single general chain. Also needs the "fallback-with-standards" declaration format decision.
- **Health monitor as observability-only (Q2 Pattern D)** — needs a decision: the rig currently may route on health; the field's discipline is that routing NEVER consults provider_health (it's observability, not a gate). Adopting means changing the rig's routing authority. Decision needed.
- **Checkpoint publication as cross-pipeline handoff primitive (Q3 Pattern A)** — needs a decision: QUEUE_ASYNC-only restriction; the rig's leg handoffs may be FUNCTION-class. Needs classification first.

## The design stays ours

The storm informs; the design stays ours. The field's canonical shapes above are the *veil* the storm sees through — the hidden layer. The rig's designs (the config-watch wiring, the circuit-breaker thresholds, the stage-gate's fragile-node list, the tier assignment's health checker) are ours to shape from this ground. Nothing here is a prescription to adopt wholesale; the READY/NOT-READY split marks what can be armed now vs. what needs a decision. Public surface: none. The storm's findings land on the root; they do not wander.

---

*Storm run 2026-11-01. Sources: MCP Hangar hot-reload docs; Big Iron runtime config hot-reload; phpboyscout reloading config; OpenStack oslo.config mutable; Cosmo/WunderGraph GraphQL router; nginx graceful reload model; NVIDIA-NeMo/Switchyard#594 circuit breaker; build-your-own-ai-gateway reliability; webhook-architecture circuit breaker patterns; Kaana routing (authorized failover, same-route retry, AWRR, health scoring); AxonHub load-balance; DeltaLLM routing & failover; routecodex AWRR; voly/a2a/assignment; conf-pipeline-orchestration skill; pipelineframework checkpoint handoff & error handling; stepflow recovery tests; rig's own earned doctrine (think-tank, head-supervisor-think-tank, mission-shaping).*
