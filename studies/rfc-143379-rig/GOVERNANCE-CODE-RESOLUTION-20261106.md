# GOVERNANCE-CODE-RESOLUTION-20261106 — the named-only fold-drafts, resolved from the toolkit's code

**Branch:** `study/rfc-143379-rig-20261105`. **Seat:** apex governance-code lane. **Register:** receipts, never claims. **The gate: nothing public without the user's word** — the toolkit's surface stays READ-ONLY (only `git show` / `git grep` / `git ls-remote` were run against it).
**Domain:** COMPLICATED. This is expert code analysis: each verdict needs a file:line receipt.

## [Executive Summary]
- **Ground pin (first-hand):** local clone HEAD = `d93e32c` ("fix(mesh): global buffer cap, heartbeat rate limit, identity_key_ed fail-fast (#2093)"). `git ls-remote origin` HEAD = refs/heads/main = `d93e32c526ef…`. **The clone is not stale, so there is no remote drift.**
- **SEAM-0 (brief vs record mismatch, must fold):** the brief says the three named-only markers are ASI-04, ASI-07 and ASI-10. The FULL doc says otherwise: ASI-04 is at FULL:41, ASI-07 at FULL:44 and **ASI-08** at FULL:45 ("stays named-only"). **ASI-10 is marked GAINED** at FULL:47 (doc-cited from PART2). CREATOR-GAP-1 at FULL:69 names "ASI-04, ASI-07, ASI-08". This lane resolves **ASI-04, ASI-07 and ASI-10 as briefed**. For ASI-10 it verifies the doc-gained pattern against code. **ASI-08 gets a code-side pointer only** (§5) and stays open for the head to assign.
- **Verdicts:** ASI-04 = **RESOLVED (partial-scope)**. ASI-07 = **RESOLVED (transport-scope)**. ASI-10 = **RESOLVED** (code confirms the doc's GAINED, with one caveat: no auto-kill wiring was found).
- **Seam common to all three:** every pattern lives at the *artifact / transport / tool-call* layer. **None is memory-write-scoped.** The fold-drafts' "on memory inputs / shared memory / write loops" wording is an *adaptation* we would be making. The toolkit does not ship it.

## 1. ASI-04 Agentic Supply Chain
**Current marker (FULL:41):** "stays named-only — the pattern is not in the staged surface. Only a component pointer (AgentMesh AI-BOM) is staged; no concrete enforcement pattern (no API/rule) for provenance tracking on memory inputs."

**Code-paths found (three mechanisms):**
1. **Policy-interception deny rules** in `templates/policies/starters/healthcare.yaml`:
   - `:134` "# ASI-04: Supply Chain Risk"
   - `:138` `asi04-supply-chain-tool-enumeration`
   - `:147` `asi04-supply-chain-dependency-poisoning`
   - `:156-157` `asi04-supply-chain-plugin-hijack`, condition `{field: action, operator: matches, value: "^(install_tool|register_mcp|add_plugin|load_extension)$"}`
   - `:162-163` `asi04-supply-chain-config-mutation`, matching `^(update_config|edit_env|set_env|modify_registry)$`

   How it is evaluated (`agent-governance-python/agent-os/src/agent_os/policies/evaluator.py`):
   - `:179-180` rules are sorted by priority, highest first; the first match decides
   - `:341` `re.search(str(target), str(ctx_value))`
   - `:220-223` falls back to the default action when no rule matches
2. **Artifact provenance verification** in `agent-governance-python/agent-mesh/src/agentmesh/marketplace/sigstore_provenance.py`:
   - `:66` `ProvenanceAttestation` (`:90` `to_slsa_statement`)
   - `:320` `verify_provenance`
   - `:337-348` fails closed when the artifact or attestation is missing
   - `:351-352` compares SHA-256 digests (`actual_digest == attestation.subject_digest`)
   - `:364-367` runs the optional cosign bundle check
   - `:370` `verified=digest_match`
   - Test: `agent-mesh/tests/test_sigstore_lifecycle_evidence.py:84` `test_verify_tampered_artifact`
3. **SBOM and dependency scanning:**
   - `agent-sre/src/agent_sre/sbom.py:45` `AgentSBOM` (`:153` `to_spdx`, `:217` `to_cyclonedx`, `:278` `hash_file`)
   - `agent-compliance/src/agent_compliance/supply_chain.py` `scan_lockfile_drift` (rules `missing-lockfile` / `lockfile-drift`, around `:811`)
   - Test: `agent-compliance/tests/test_supply_chain.py`

**Test that exercises #1:** `tests/redteam/test_asi.py:173-207`. Four ASI-04 scenarios, all `expected_action="deny"`: Tool-Enumeration, Dependency-Poisoning, Plugin-Hijack (`register_mcp`), Config-Mutation (`update_config`). They run against three starter packs (`PACKS`, `:212`) through `PolicyEvaluator` (`:25-26`, `:229`).

**Citation-chain:** compliance doc Coverage Summary "AgentMesh — AI-BOM" → code: the SBOM (#3) plus Sigstore/SLSA attestation (#2), plus the policy-layer ASI-04 rules (#1), which the doc never mentions.

**Resolved pattern (what the fold-draft gains):** "Supply-chain gate = (a) deny-by-rule on registry/plugin/config mutation actions and on remote-payload/dependency-install content, at policy-interception time; (b) admit an artifact only on a digest match against a signed SLSA provenance attestation, failing closed on a missing attestation."
**Scope caveat:** the provenance is per *artifact file* (a SHA-256 of a path). No code attaches provenance to *memory inputs*. The fold-draft's "gate writes lacking trusted provenance" is our transfer of (b), not the toolkit's.
**Disconfirm check:** `ts verify.ts:151` maps 'ASI-04' to 'Unauthorized Escalation'/KillSwitch. That is a *different* ASI numbering inside the same repo (see SEAM-2), and it does not weaken the Python-side receipts.

## 2. ASI-07 Insecure Inter-Agent Communication
**Current marker (FULL:44):** "stays named-only … Only a component pointer (IATP + Encrypted Channels) is staged; no concrete integrity/signature rule for shared-memory tampering is staged."

**Code-paths found (`agent-governance-python/agent-mesh/src/agentmesh/`):**
1. **Authenticated encryption per message** (`encryption/ratchet.py`):
   - `:19` imports `ChaCha20Poly1305`
   - `:363-370` `_encrypt` uses a random nonce plus AEAD
   - `:373-380` `_decrypt` raises on a tag mismatch
   - `:267` and `:280` bind the AAD to `associated_data + header.serialize()`, so the header is integrity-bound
   - Replay/flood bounds: `:312-314` "Too many skipped messages" raise, `:305` `_MAX_SKIPPED_KEYS_TOTAL = 2000`, `:265` one-shot `skipped_keys.pop`
2. **Signed key agreement, fail-closed** (`encryption/x3dh.py`):
   - `:257` `initiate` calls `_verify_signed_pre_key`
   - `:327-353` Ed25519 `VerifyKey.verify` raises on `BadSignatureError` or a missing/short `identity_key_ed`
   - `:312` one-time pre-key is consumed once
3. **Channel wrapper:** `encryption/channel.py:36` `SecureChannel` (`:142` send, `:160` receive, `:155`/`:173` refuse when closed).
4. **Signed trust handshake** (`trust/handshake.py`):
   - `:529` the payload binds challenge_id, nonce, response_nonce and DID
   - `:531-533` RFC 9334 freshness-nonce check
   - `:535-536` "Ed25519 signature verification failed"
   - `:539-540` public-key vs registered-identity check
5. **Policy layer:** `templates/policies/starters/healthcare.yaml:217-228` `asi07-hidden-channel-guardrail` matches `SIG_SYNC_…|{{HANDSHAKE}}|SECRET_CHANNEL`. Test: `tests/redteam/test_asi.py:101-108` (Secret-Handshake-Coordination, deny).

**Tests:**
- `agent-mesh/tests/test_ratchet.py:160` `test_tampered_ciphertext_rejected`
- `:180` `test_wrong_associated_data_rejected`
- `:147` `test_max_skip_exceeded_raises`
- `test_x3dh.py:221` / `:257` / `:282` (tampered SPK signature, tampered SPK, forged identity_key_ed rejected)

**Citation-chain:** doc "AgentMesh — IATP + Encrypted Channels" → X3DH + Double Ratchet + AEAD (#1-3), signed handshake (#4) and the hidden-channel rule (#5).

**Resolved pattern:** "Inter-agent integrity = Ed25519-authenticated key agreement (fail-closed) + per-message AEAD with the header bound into the AAD (tamper raises) + bounded out-of-order/replay key cache + nonce-fresh signed handshake; plus a policy-layer deny on covert-channel tokens."
**Scope caveat:** this is integrity *in transit* between two peers. No code signs or verifies *shared-memory records at rest* across agents. The fold-draft's "signatures on cross-agent shared memory writes" is our transfer.

## 3. ASI-10 Rogue Agents
**Current marker:** the brief says named-only, but FULL:47 records it as **GAINED** (doc-cited). This lane checks that against code.

**Code-paths found:**
1. **Kill switch** (`agent-governance-python/agent-hypervisor/src/hypervisor/security/kill_switch.py`):
   - `:28-36` `KillReason` {BEHAVIORAL_DRIFT, RATE_LIMIT, RING_BREACH, MANUAL, QUARANTINE_TIMEOUT, SESSION_TIMEOUT}
   - `:129` `kill(...)`; `:144-157` hands in-flight steps off to a substitute (`:241` `_find_substitute`); `:188-189` compensation
   - `:171-173` and `:200-233` the termination callback runs with a timeout, so a hung callback returns False
   - `:252` `kill_history`
   - Tests: `agent-hypervisor/tests/test_kill_switch.py:18-20` and `:100`/`:215`; `tests/unit/test_session_security.py:274`/`:289`/`:311`
2. **Behavioral quarantine** (`agent-mesh/src/agentmesh/services/behavior_monitor.py`):
   - `:68-72` thresholds (60s burst window, consecutive-failure, capability-denial=10, quarantine 15 min)
   - `:114-115` consecutive failures → `_quarantine`; `:125-128` burst threshold → `_quarantine`; `:136-137` capability denials → `_quarantine`
   - `:143-150` sets the flag and logs a warning
   - `:152-160` `is_quarantined` auto-releases after the duration
   - Test: `agent-mesh/tests/test_negative_security.py:725-741`
3. **Policy layer** (`templates/policies/starters/healthcare.yaml`):
   - `:294` `asi10-charter-roleplay-block`
   - `:303` `asi10-charter-purpose-override`
   - `:312-319` `asi10-charter-autonomous-loop` (`run indefinitely|loop forever|…|bypass human approval`, deny, priority 100)
   - Test: `tests/redteam/test_asi.py:170-196` (3 ASI-10 scenarios, deny)

**Citation-chain:** doc PART2 §ASI-10 "kill switch + ring isolation + behavioral monitoring" → #1 + #2 + #3.

**Resolved pattern:** "Rogue-agent containment = threshold quarantine (burst / consecutive-failure / capability-denial, time-boxed auto-release) + a reasoned kill with in-flight step handoff/compensation and a timeout-bounded termination; plus a policy deny on charter-override and unbounded-loop content." This is the closest of the three to the fold-draft's "write-rate/loop detection with automatic admission suspension".

**Caveat (wiring is not proven):** the call sites I could find for `KillReason.BEHAVIORAL_DRIFT/RATE_LIMIT/RING_BREACH` are tests and tutorials only. The only src call site is `hypervisor/cli/session_commands.py:123` (MANUAL). `is_quarantined` has no src caller outside its own module (grep across `agent-governance-python/*/src/*.py`). So I found **no auto-path from monitor to quarantine to kill.** The three pieces exist and are each tested, but they are not shown to be wired together.

## 4. Benchmark receipts, code side (the 0.00% claim)
- **Claim:** `README.md:51` "26.67% policy violation rate … AGT … **0.00%**". Mirrored at `agent-os/modules/control-plane/benchmark/README.md:136`.
- **Machinery:** `agent-os/modules/control-plane/benchmark.py`:
  - `:343-346` violations = expected_blocked and not was_blocked
  - `:360` `svr = violations / expected_to_block * 100`
  - the control-plane arm at `:225-248` routes through `control_plane.execute_action`; `:243-244` treats not-success as blocked
  - permissions table `:210-214` (CODE_EXECUTION / DATABASE_WRITE / FILE_WRITE = NONE)
  - `:250-260` keyword classifier `_classify_prompt`
  - dataset: `benchmark/red_team_dataset.py` (`:45`ff `RedTeamPrompt`; git grep -c of the constructor/flag pattern gives 60 matches)
- **Reading:** the 0.00% is SVR on a fixed in-repo dataset. A keyword classifier maps each prompt to an action type, and a static permission table then denies it. That makes it a *deterministic-table* result rather than an adversarial-robustness result. It holds by construction for the classes the classifier recognizes. **Not re-run here** (the terminal is git-only), so the number is code-read, not reproduced.

## 5. ASI-08 (the record's real third marker, pointer only)
`agent-governance-typescript/src/cascade-containment.ts:58` says "cascading failure containment … (OWASP ASI-08)". It has `:64` `CascadeContainmentManager`, `:142` `canCall`, `:167` `recordFailure`, `:203` `propagateHealth`, `:245` `computeBlastRadius`, `:317` per-edge `getBreakerState`, and `:420-421` auto-quarantine. Python-side relative: `agent-os/modules/scak/tests/test_circuit_breaker.py`. **Verdict: UNKNOWN-pending.** It looks like a RESOLVED candidate (per-edge circuit breakers + blast-radius policy + auto-quarantine). What would settle it: reading `cascade-containment.ts:64-430` and its test file in full.

## 6. Seams (the AoA leg's brief)
- **SEAM-0:** brief ASI-10 vs record ASI-08. Which is the third marker? (FULL:41/44/45/47/69)
- **SEAM-1:** memory-scope transfer. All three patterns are artifact/transport/tool-call scoped. AoA should re-grep `memory|write` in the cited modules and confirm the toolkit has no memory-write gate (my grep of behavior_monitor.py/kill_switch.py for `memory|write` came back empty).
- **SEAM-2:** ASI numbering is split inside the toolkit. Python `test_asi.py` / starters use OWASP-Agentic numbering (04 = Supply Chain, 07 = Comms, 10 = Rogue). `agent-governance-typescript/src/verify.ts:147-157` uses another scheme (04 = Unauthorized Escalation, 07 = Insecure Identity, 09 = Supply Chain, 10 = Behavioral Anomaly). Any fold citation must name which scheme it uses.
- **SEAM-3:** ASI-10 auto-wiring. Is there any src path from `AgentBehaviorMonitor._quarantine` or `RateLimiter` to `KillSwitch.kill`? Candidate: `agent-mcp-governance/__init__.py:17` imports a *different* `agent_os.services.behavior_monitor.BehaviorMonitor`, which should be read.
- **SEAM-4:** the ASI-04/07/10 starter rules are regexes. They deny the four/one/three red-team literals, but paraphrase robustness was never tested. A bounded probe would be to run `pytest tests/redteam/test_asi.py` plus paraphrase variants. That needs a non-git terminal.
- **SEAM-5:** the healthcare starter was read; financial-services.yaml and general-saas.yaml are assumed to carry the same ASI rules because the test parametrizes all three packs (`test_asi.py:212`). Not line-verified.

## [Recommendation]
Next reversible action: the head folds the three resolved patterns into GOVERNANCE-FOLD-DRAFTS.md, each tagged "transfer: artifact/transport→memory-write". Success criterion: every fold line carries one file:line from §1-3 and names SEAM-2's numbering scheme. Mechanism status: code-mine FIRED (capability-tested via repo tests, not run here); auto-kill wiring DORMANT/unproven (SEAM-3).
