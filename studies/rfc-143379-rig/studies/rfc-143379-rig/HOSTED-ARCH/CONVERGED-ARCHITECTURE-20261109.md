# THE CONVERGED-ARCHITECTURE — Hosted-Custom-Code (RFC-143379-rig)

**Date:** 2026-11-09 · **Register:** plain, evidence-carrying · **Limit:** ~10 min read · **Status:** design artifact, direct-applicable

## Doctrine (one line)
The architecture is the assistant's *residence* — a brain versioned in the repo, a body unmetered on the runner — not a CI system. GitHub is the spine; the runner is the arm. Every surface serves that, or it doesn't belong. The swap's convergence keeps the simplest components, the reliability-guards, the vision's first rung, and the sequence's risk-first order.

---

## 1. THE FINAL-ONE-PAGE — surfaces + steps (simplified)

```
  dev (local edit)  --push/PR-->  GitHub (spine)  --dispatch label-->  Avrea runner (arm)
        ^                                                          |
        |                                                          | pull-build-run-report
        |                                                          v
        +-- next-code iteration <-- report/PR-comment <-- artifacts (return)
```

**Surfaces (four, one responsibility each):**
- **Transport** — code + intent across the wire: git push, PR, dispatch label, artifact upload. Stateless; only surface touching network boundary.
- **Execution** — runner pull/build/run/report. Where the body lives; unmetered, self-hosted.
- **Models** — local-LM engine + model weights + probe battery, as *hosted-executed artifacts*, not infrastructure.
- **Return** — results/artifacts → report → next-code iteration. Closes the loop; only surface feeding back into dev.

**Perpetual loop:** dev → host → pull-build-run-report → return → iterate. Each pass leaves evidence (artifacts, logs, verdict).

**Canonical trigger:** dispatch label on a PR → probe run → runner executes → results attach to PR. Reuse for every probe battery; no new triggers.

**Transport mechanics (converged):** release assets (default) — build-once → tag → runner pulls binary + models, verifies sha256, caches in `/opt/avrea`. GHCR only when full-env reproducibility or heavy deps; both may coexist.

**Execution mechanics (converged):** trigger = release-trigger when reproducibility required; push-trigger for dev loops; cron fallback only. Build-only-if: release asset for SHA → skip; else marker + sha256 re-verify. Run-and-report: JSON result to `results/<run_id>.json`, upload as release asset, receipt comment on PR/commit (run_id, status, exit_code, link). Return through same spine — never side channel.

**Models mechanics (converged):** host as GitHub release assets per tag `model-<name>-<quant>-<enginecommit>`; split GGUF >2 GB; sha256 manifest. Cache at `/var/lib/avrea/models/<key>/{model.gguf,engine/,ready.flag}`; download-once with flock; LRU eviction under 80% disk, pin running key. Cold budget 20 min / warm 8 min.

**Return mechanics (converged):** upload-artifact v4, 7-day retention, one artifact per run; run-summary to `$GITHUB_STEP_SUMMARY` + issue-comment receipt-row (idempotent by `<!-- receipt:run_id -->`). Receipt file lands on `study/rfc-143379-rig-20261105` via `AVREA_PUSH_PAT`; fallback = runner commits patch, head applies + pushes, marked `landed-by: head`. Findings append to `G0-ledger.md` (append-only); no receipt-file → row stays `pending-receipt`; fold only when both fast+slow receipts present; zero-delta = terminal honest-negative.

---

## 2. THE V1's FINAL-CONTENTS — risk-first, with exit-criterion

**Week 1 — Transport + Execution.** Dispatch label → runner pull-build-run → artifact upload. Prove the arm moves. (Precedent: dispatch-label-probe.)

**Week 2 — Models slice.** Pin engine + model hashes in repo; runner loads by hash; probe battery runs against local-LM; results returned. Prove the LM is a hosted-executed artifact.

**Week 3 — Return loop closure.** Report → PR comment → next-code iteration evidenced by a second commit driven by the first run's output. Prove the loop is perpetual, not one-shot.

**Week 4+ — Partitioned-head mounting.** Only after 1–3 close. Tackle the five open questions one at a time, each gated on evidence from the prior step.

**First-release contents (minimal, no extras):**
- `probes/` — one battery, one model target
- `.github/workflows/` — one dispatch-label-triggered workflow
- `runner/` — pull/build/run/report script (self-hosted Avrea)
- `docs/crown-slice.md` — this document
- Pinned engine version + model hash manifest
- **Explicitly NOT in v1:** multi-head, persistent sessions, secrets management, state-sync policy. Each is a later slice gated on evidence.

**Exit criterion for "first release done":** a PR with the dispatch label produces a report comment that a human (or the next code commit) acts on. Loop closed once = architecture adopted.

**Reliability-guards kept (from slices):** marker existence necessary-but-not-sufficient (re-verify artifact_sha256); receipt hash = SHA-256 of canonical JSON (sorted keys), recompute on reader side; partial upload → run marked `upload-incomplete`, no receipt; verify each upload with GET + SHA check; honest token-scope limit (AVREA_PUSH_PAT required for runner direct push; fallback path for no-PAT).

---

## 3. THE VISION's-RUNG — partitioned-head's first-rung confirmation/adjustment

**Destination (confirmed, unchanged):** a dedicated head-layer assistant whose brain is versioned in the repo and whose body runs unmetered on the runner, connected by this spine. Brain (repo): prompts, memory, skills, tool definitions, decision logic — versioned, diffable, reviewable, PR'd. Body (runner): inference execution, tool execution, long-running work, probe batteries — unmetered, self-hosted. Spine (this architecture): the four slices, connecting brain ↔ body. Loop = nervous system. Mounting: assistant runtime is a repo-resident program the runner executes; state checkpoints land back in repo (or repo-referenced store) via Return. Head partitioned — reasoning/planning in brain, execution in body — so neither side carries the other's cost.

**Adjustment (convergence):** the partitioned-head is the *destination*, not the starting point. It mounts only after weeks 1–3 close, one open question at a time, each gated on evidence. The five open questions remain honestly unresolved and must not be faked:
1. State residency — repo (slow, auditable) vs runner-side store referenced by hash (fast, needs sync). Undecided.
2. Trigger granularity — one dispatch per task vs persistent runner session the brain drives. Undecided.
3. Failure semantics — on body failure mid-task: retry, replan, or escalate. No policy yet.
4. Multi-head — one assistant per repo vs many heads sharing one runner. Resource contention unknown.
5. Secrets — how body gets credentials without baking into brain/repo. Not addressed by current slices.

The vision's first rung is confirmed as-is: brain versioned, body unmetered, spine connects. What the swap adds is the discipline that the head does not mount until the loop closes with evidence.

---

## 4. THE CONVERGENCE's-LINE — what the swap changed vs the crown's original

The crown's original already named the smallest vertical slice, the four-slice spine, the local-LM as hosted-executed artifacts, and the five honest open questions; the swap's convergence did not overturn any of that but tightened the operational contract: it pulled the concrete mechanics out of the four slices (release-asset transport with sha256 verification, build-only-if caching with marker re-check, download-once model cache with flock and LRU eviction, PAT-gated receipt push with honest fallback and append-only ledger close) and made them the reliability-guards that the v1 must ship with, while holding the line that the partitioned-head mounts only after weeks 1–3 close with evidence and that the five open questions stay unresolved rather than being papered over. The diff is additive discipline, not redesign: same doctrine, same sequence, same exit criterion, now backed by verifiable contracts instead of described surfaces.
