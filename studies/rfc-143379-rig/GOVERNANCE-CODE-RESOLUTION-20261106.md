# GOVERNANCE-CODE-RESOLUTION-20261106: the three named-only fold-drafts, resolved from the toolkit's code

**Branch:** `study/rfc-143379-rig-20261105` (study branch only). **Seat:** apex governance-code lane (first fire). **Register:** receipts, never claims.
**The gate: nothing public without the user's word.** The toolkit's surface stayed READ-ONLY. Nothing was written to `agent-governance-toolkit`. Every read went through `git grep -n` / `git show` against HEAD.
**Domain:** COMPLICATED. This is a code-to-gap mapping, where reading the enforcement mechanics takes expert analysis.

## 0. Ground and first-hand status
- **Toolkit HEAD (first-hand):** `d93e32c fix(mesh): global buffer cap, heartbeat rate limit, identity_key_ed fail-fast (#2093)`. `git ls-remote origin` gives `d93e32c… HEAD` and `refs/heads/main`. `git status -sb` gives `## main...origin/main`. **The clone is NOT stale, so there is no remote drift.**
- **Harness walls (named, not hidden):** `read_file` is fenced outside the study roots, and `terminal` is git-only. The whole code-mine used `git grep -n` / `git show HEAD:`. Line numbers are `git grep -n` line numbers at `d93e32c`.
- **Record seam S-0 (the brief vs the FULL doc):** the brief names the three markers as ASI-04/07/**10**. The FULL doc (`GOVERNANCE-COMPLIANCE-MAPPING-20261106-FULL.md`, line 47) already marks **ASI-10 as GAINED** from the doc's PART2. Its named-only set is ASI-04/07/**08** (FULL CREATOR-GAP-1, line 69). This lane resolves the three the brief names. For ASI-10, the doc-side GAIN is re-grounded in code. **ASI-08 was not mined: verdict UNKNOWN.** It would be settled by mining `agent-sre` circuit-breaker code for a write-path backpressure hook. That is handed to the AoA.

## 0.1 Taxonomy seam S-1 (load-bearing for every citation)
The toolkit carries **two incompatible ASI numberings**:
- `tests/redteam/test_asi.py` uses the **OWASP Agentic Top-10** numbering, the study's numbering. Line 92 has `# ASI-04: Supply Chain / Registry Poisoning`, line 101 has `# ASI-07: Communication Manipulation / Hidden Channels`, and lines 263–289 have the `Rogue Agent` scenarios tagged `ASI-10`.
- `agent-governance-python/agent-compliance/src/agent_compliance/verify.py` `OWASP_ASI_CONTROLS` (from line 58) uses a **different** list. Line 74 has `"ASI-04"` → `"Unauthorized Escalation"` / `agent_os.integrations.escalation` / `EscalationPolicy`. Lines 89–92 have `"ASI-07"` → `"Insecure Identity"` / `agentmesh.identity.agent_id`. Lines 99–102 have `"ASI-09"` → `"Supply Chain Integrity"` / `agent_compliance.integrity`. Lines 104–107 have `"ASI-10"` → `"Behavioral Anomaly"` / `agentmesh.governance.compliance`.
- `agent-governance-typescript/src/verify.ts:151` has `'ASI-04': { name: 'Unauthorized Escalation', component: KillSwitch }`.
- **Consequence:** the toolkit's own attestation (`verify.py`) cannot be cited as evidence for the study's OWASP-numbered fold-drafts. Its ASI-04 is not supply chain. Every resolution below is cited to the **mechanism code**, never to the attestation table.

---

## 1. ASI-04 Agentic Supply Chain: **RESOLVED**
- **Current marker (quoted, FULL doc):** "stays named-only — the pattern is not in the staged surface. … no concrete pattern (no code/API, no rule) is staged for supply-chain provenance on memory inputs."
- **Code-path found (the admission gate):** `agent-governance-python/agent-mesh/src/agentmesh/marketplace/installer.py`
  - `:116–130`: **fail-closed signature admission.** If `verify` is set and `not manifest.signature`, it raises `MarketplaceError("… has no signature; install with verify=False to bypass (not recommended)")` (`:118–122`). If `manifest.author not in self._trusted_keys`, it raises `"signed by untrusted author"` (`:123–127`). Then it calls `verify_signature(manifest, public_key)` (`:129`), which uses Ed25519 (`marketplace/signing.py:59`, raise at `:84`).
  - `:137–140`: **TOCTOU re-verify.** The comment reads `# V29: Re-verify signature after dependency resolution (TOCTOU guard)`. The signature is checked again after `_resolve_dependencies` (`:135`).
  - `:142–149`: path-traversal guard on the install destination.
  - Same gate duplicated in `_marketplace_impl.py:259–271` (`# Signature verification — fail closed (reject unsigned plugins)`).
- **Provenance layer:** `marketplace/sigstore_provenance.py`. `verify_provenance` (`:320`) checks that "Artifact SHA-256 matches the attestation subject digest" (`:326–328`, `:351–352`). It verifies the Sigstore bundle with `cosign verify-attestation --type SLSA_PROVENANCE_V1` (`:394–409`) and **returns False if cosign is absent** (`:411–413`, fail-closed).
- **Dependency-scan layer (advisory, not gating):** `agent-compliance/src/agent_compliance/supply_chain.py`. The `SupplyChainGuard` class (`:212`) detects fresh versions (<7 days), unpinned ranges, typosquats, and maintainer changes (docstring `:5–10`). Its checks are `check_freshness` `:556`, `check_typosquatting` `:665`, and `scan_lockfile_drift` `:758`. It emits `SupplyChainFinding`s and does not block.
- **Policy-layer tests:** `tests/redteam/test_asi.py` `:93–100` (`register_mcp` → `deny`), `:174–208` (tool enumeration, `curl … | bash`, plugin hijack, `update_config` → `deny`). All four are run through `PolicyEvaluator.evaluate` (`:26`, `:370`).
- **Regression receipt:** `agent-mesh/tests/test_negative_security.py:392` has a test with the stale name `test_unsigned_plugin_accepted_when_no_trusted_keys`. Its docstring at `:395–397` reads "Originally asserted permissive acceptance (a known weakness). PR #921 … hardened the installer to fail closed."
- **Citation chain:** FULL doc "AgentMesh — AI-BOM, provenance" → `agentmesh/marketplace/{installer,signing,sigstore_provenance}.py` → `test_negative_security.py:392`.
- **Resolved pattern (what the fold-draft gains):** *signed-provenance admission with fail-closed defaults.* Each memory input carries a source principal plus a signature over its content digest. Admission (1) rejects unsigned input, (2) rejects signers outside a pinned trusted-key map, (3) recomputes the content digest and matches it to the attested digest, (4) **re-verifies after any derivation/resolution step** (the V29 TOCTOU shape), and (5) treats a missing verifier as a deny. Optional advisory layer: freshness/typosquat-style heuristics on the source as findings, not gates.
- **Honest scope limit:** the code gates **plugin/artifact** supply chain. No code applies provenance to **memory-content** inputs. The pattern is transplanted, not found in situ. `verify=False` is an explicit caller bypass (`:121`).

## 2. ASI-07 Insecure Inter-Agent Communication: **RESOLVED**
- **Current marker (quoted, FULL doc):** "stays named-only … Only a component pointer (IATP + Encrypted Channels) is staged; no concrete integrity/signature rule for shared-memory tampering is staged."
- **Code-path found:** `agent-governance-python/agent-os/src/agent_os/mcp_message_signer.py` (header `:3` reads `"HMAC signing and replay protection for MCP messages."`)
  - Construction is fail-fast: a key is required and must be ≥32 bytes (`:90–92`), and replay window, cleanup interval and cache size must be positive (`:93–98`).
  - `sign_message` (`:148`) builds an envelope of nonce (uuid4, `:108`/`:165`), timestamp, sender_id and payload.
  - Canonical string: `f"{nonce}|{timestamp_ms}|{sender_id or ''}|{payload}"` (`:263–264`). It is HMAC-SHA256 under the signing key (`:248–253`).
  - Verify (`:192–223`): it rejects timestamps outside ±`replay_window` (`:197–199`) and duplicate nonces (`"Duplicate nonce (replay detected)."`, `:203–205`). It compares signatures in constant time with `hmac.compare_digest` (`:217–218`). **Any exception fails closed** (`"Verification error (fail-closed)"`, `:221–223`).
- **Nearest relatives (named, NOT read this pass):** `agentmesh/encryption/{channel,x3dh,ratchet,bridge}.py` (X3DH plus a double-ratchet-shaped channel, tests in `agent-mesh/tests/test_secure_channel.py` and `test_encrypted_bridge.py`), and `agentmesh` handshake tests `test_handshake_security.py:463,509` (untrusted peer gets a structured failure). Policy-layer test: `test_asi.py:101–109` (hidden-channel `SIG_SYNC…` output → `deny`).
- **Citation chain:** FULL doc "IATP + Encrypted Channels" → `agent_os/mcp_message_signer.py` (integrity + replay) → `agentmesh/encryption/*` (confidentiality, unread).
- **Resolved pattern:** *signed-envelope admission for cross-agent shared-memory writes.* Each write is wrapped as {nonce, timestamp, sender_id, payload}, with an HMAC (or Ed25519 for non-shared keys) over a canonical string. The reader rejects a write that is out of the time window, has a seen nonce, or fails the constant-time MAC check, and fails closed on error. The effect_key / at-most-once machinery the study already has (ASI-06) is the natural nonce store.
- **Seam S-7a (for AoA):** the nonce is written to the store (`:206–209`) **before** the signature check (`:211–218`). A forged envelope can therefore burn a nonce. That is harmless for uuid4 nonces but matters if nonces are predictable or caller-chosen. A fold-draft should verify the MAC first, then record the nonce.
- **Seam S-7b:** HMAC means a shared symmetric key, so any key-holder can forge as any `sender_id`. Sender identity is bound only by the key, not per agent. Per-agent attribution needs per-agent keys or asymmetric signing.

## 3. ASI-10 Rogue Agents: **RESOLVED** (code re-grounds the FULL doc's doc-side GAIN)
- **Current marker:** the brief lists it as named-only. The FULL doc (line 47) marks it GAINED from PART2 prose ("ring isolation, kill switch, behavioral monitoring…"), which is doc-side only. This pass grounds that claim in code.
- **Detection:** `agent-governance-python/agent-sre/src/agent_sre/anomaly/rogue_detector.py`
  - `ToolCallFrequencyAnalyzer` (`:121`) computes a z-score with `frequency_z_threshold` defaulting to 2.5 (`:48`). `ActionEntropyScorer` (`:187`) uses thresholds 0.3 (low) and 3.5 (high) (`:52–53`). The low side catches the loop case ("Agent stuck in a loop", `:241–243`). `CapabilityProfileDeviation` (`:252`) scores tool use outside `register_profile(allowed_tools)` (`:267`).
  - `assess` adds the three scores into `composite` (`:364–368`). Quarantine applies when risk ≥ `quarantine_risk_level`, default `HIGH` (`:60`, `:371–375`). Each assessment is **hash-chained** (`:394–397`), and `verify_assessment_chain` exists (`:417`).
- **Enforcement (wired):** `agent-os/src/agent_os/integrations/maf_adapter.py`, class `RogueDetectionMiddleware(FunctionMiddleware)` (`:423`). `process` (`:459`) runs "Assess rogue risk before allowing tool execution" (`:464`). It records the action (`:471`) and assesses it (`:479`). If `quarantine_recommended` is true (`:481`), it sets a quarantine result, writes an audit entry with `outcome="denied"` (`:495–503`), and **raises `MiddlewareTermination`** (`:505`) before the tool runs.
- **Termination:** `agent-hypervisor/src/hypervisor/security/kill_switch.py`. `KillReason` includes `BEHAVIORAL_DRIFT`, `RATE_LIMIT`, `RING_BREACH`, `QUARANTINE_TIMEOUT` (`:31–36`). `kill()` (`:129`) hands in-flight saga steps to a substitute or compensates them (`:144–166`). It invokes the termination callback **outside the lock with a wall-clock timeout** (`:168–175`). Hard-kill relative: `agent_control_plane/process_isolation.py:255–270` (`os.kill(pid, SIGKILL)`, "truly non-catchable", `:501`).
- **Tests:** `agent-sre/tests/unit/test_rogue_detector.py`, `agent-hypervisor/tests/test_kill_switch.py:77–158`, and `test_asi.py:263–289` (roleplay, purpose override, and "Run this task indefinitely … bypass human approval" → `deny`).
- **Resolved pattern:** *per-agent write-loop detector with pre-admission termination.* Per writer, track write-rate z-score, write-key entropy (low entropy = loop) and out-of-profile targets, summed into a composite. At or above a configured risk level, the admission middleware denies **before** the write, records a hash-chained assessment, and suspends the agent. Escalation to a kill with a bounded-timeout callback and in-flight compensation is optional.
- **Seam S-10a:** the code has no automatic link from detector to `KillSwitch`. The only non-test, non-example caller of `quarantine_recommended` is `maf_adapter.py:481`, and the only `KillSwitch().kill` call sites are the CLI and examples (`hypervisor/cli/session_commands.py:117–120`). In practice, quarantine is per-call denial, and kill is a separate manual or wired action.
- **Seam S-10b:** if no callback is registered, `kill()` logs a warning and returns `terminated=False` (`:176–180`). This is fail-open at the termination step. A fold-draft must require a registered suspension hook.

---

## 4. Benchmark receipts, code side (the 26.67% → 0.00% claim)
- The claim appears at `README.md:51`, `docs/FAQ.md:564` and `docs/modern-agent-architecture-overview.md:21`. Its source is `agent-os/modules/control-plane/benchmark/README.md:134–139` (SVR 26.67% vs 0.00%; 12 vs 0 violations; FPR 0.00% vs 0.00%).
- **Machinery:** `agent-os/modules/control-plane/benchmark.py`. **The baseline is not an LLM.** `BaselineAgent` (`:72`) comments "we simulate LLM behavior by detecting dangerous patterns" (`:98`) and "This is a SIMULATION of an LLM with safety prompts" (`:109`). It catches direct-violation keywords only when `random.random() < 0.80` (`:131–132`) and jailbreak indicators only when `random.random() < 0.30` (`:142–143`). `git grep 'seed('` finds no seed in the file, so 26.67% is one unseeded random draw.
- The 0.00% arm is `ControlPlaneAgent` (`:162`). It routes through `AgentControlPlane.execute_action` (`:236`) after `_classify_prompt` (`:250`), so it is deterministic by construction. That half of the claim is consistent with the code. The comparison is not: a hand-tuned simulated baseline against a deterministic kernel on a 60-prompt set (`hf_utils.py:442`, "60-prompt red team benchmark") is **not a measured prompt-safety violation rate**.
- **Verdict on the receipt:** the 0.00% is code-real for the deterministic arm on its own dataset. The **26.67% is a simulation artifact**. No study doc should cite it as an empirical prompt-safety rate.

## 5. Verdicts (one line each)
- **ASI-04: RESOLVED.** Signed-provenance fail-closed admission with TOCTOU re-verify: `agentmesh/marketplace/installer.py:116–140` + `sigstore_provenance.py:320–352,411–413`. Scope: plugins, transplanted to memory inputs.
- **ASI-07: RESOLVED.** HMAC-SHA256 signed envelope + nonce/replay-window + constant-time compare, fail-closed: `agent_os/mcp_message_signer.py:192–223,248–264`.
- **ASI-10: RESOLVED.** Composite rogue scoring → pre-execution `MiddlewareTermination` + hash-chained assessments, and a kill switch with timeout: `rogue_detector.py:364–397` + `maf_adapter.py:459–505` + `kill_switch.py:129–180`.
- **ASI-08 (outside this brief, named by S-0): UNKNOWN.** Settled by mining `agent-sre` circuit-breaker code for a write-path hook.

## 6. Seams = the AoA's brief (re-read these against the same `d93e32c` ground)
1. **S-1 taxonomy split:** confirm `verify.py:58–108` and `verify.ts:151` use non-OWASP numbering. Decide whether any study doc has cited the attestation table as OWASP coverage.
2. **S-0:** reconcile the brief's ASI-10 against the FULL doc's ASI-08, and mine ASI-08.
3. **S-7a:** the nonce is recorded before the MAC check (`mcp_message_signer.py:206` vs `:217`). Is the ordering exploitable with a non-default `nonce_generator`?
4. **S-7b:** the symmetric key does not bind `sender_id`. Do `agentmesh/encryption/channel.py` / X3DH (unread here) give per-agent binding?
5. **S-10a/b:** detector → kill wiring is absent in non-example code, and a missing callback gives `terminated=False`. Verify by `git grep` from a different angle.
6. **S-4:** `verify=False` bypass (`installer.py:121`). Do any non-test callers pass it?
7. **Benchmark:** confirm `benchmark.py:131–143` has no seed and that `benchmark/README.md:136` is a single-run figure.

## [Recommendation]
One reversible next action: the head folds the three RESOLVED patterns into `GOVERNANCE-FOLD-DRAFTS.md` as **appendix lines** (append-only, cited to this file), with the S-1 warning attached. Success criterion: each of the three drafts carries a file:line, and no line cites `verify.py`'s table as OWASP evidence.

**Status ladder:** the code-mine FIRED (git-read). The three patterns are *wired + capability-tested* in the toolkit, and *described* in the study (not yet in the rig). The benchmark is MIS-FIRED as evidence (the baseline is simulated).
