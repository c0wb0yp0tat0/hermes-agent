# THE RUNNER-ARM'S INTEGRATION-PLAN — ALPHA (runner-loop)

**Date:** 2026-11-09 · **Register:** plain, evidence-carrying · **Limit:** ~12 min · **Status:** design artifact, direct-applicable

## Doctrine (one line)
The runner-arm is the perpetual loop's execution-surface: transport/execution/models/return are the loop's body. Every surface below serves that, or it doesn't belong. No gates but the public one.

---

## 1. THE SPINE'S FULL-LOOP — permanent architecture

### Surfaces (four, each a distinct responsibility)
- **Transport** — how code + intent cross the wire (git push, PR, dispatch label, artifact upload). Stateless; the only surface touching the network boundary.
- **Execution** — runner pulling, building, running, reporting. Where the body lives; unmetered, self-hosted.
- **Models** — local-LM engine + model weights + probe battery, treated as *hosted-executed artifacts*, not infrastructure.
- **Return** — results/artifacts → report → next-code iteration. Closes the loop; the only surface feeding back into code dev.

### Steps (the loop's body, in order)

```
dev → host → pull-build-run-report → return → iterate
```

1. **dev** — local edit; brain (prompts, memory, skills, tool defs, decision logic) versioned in repo, diffable, reviewable.
2. **host** — push/PR to GitHub (spine). Dispatch label on PR triggers probe run (canonical trigger shape; reuse, don't invent).
3. **pull** — runner (`avrea-ubuntu-latest`, 12-core/16GB) pulls source by ref; computes `source_sha = git rev-parse HEAD`.
4. **build-only-if** — decision per incoming (repo, ref):
   - if release asset exists for `source_sha` → pull-and-skip-build (download, verify checksum, run);
   - else if local marker `/var/runner/cache/<repo>/<source_sha>.built` present AND `artifact_sha256` matches → skip build;
   - else build → write artifact to `/var/runner/cache/<repo>/<source_sha>/` + marker.
   - Invariant: marker existence is necessary but not sufficient — always re-verify `artifact_sha256` before run. Never trust a marker whose SHA mismatches.
5. **run** — execute probe battery against local-LM (engine + pinned model hashes). Output: `results/<run_id>.json`.
6. **report** — upload artifacts + result JSON to release on same spine (`gh release upload` or REST); verify each upload with GET + SHA check.
7. **receipt** — post comment on triggering commit/PR/release with `run_id`, `status`, `exit_code`, link. Receipt hash = SHA-256 of canonical JSON (sorted keys); recompute on reader side to verify integrity.
8. **return** — results flow back through GitHub only; never a side channel. Runner is the arm; GitHub is the spine; receipt is the proof.
9. **iterate** — next-code commit driven by prior run's output. Loop is perpetual; each pass leaves evidence (artifacts, logs, verdict).

### Failure-guards baked in
- `set -euo pipefail` on runner script; non-zero exits captured in `exit_code`, never swallowed.
- SHA re-verification before every run (marker never trusted alone).
- Upload verification: GET + SHA check per artifact; mismatch → status=failure, no receipt posted.
- Receipt integrity: canonical-JSON SHA-256 recomputed by reader; mismatch → receipt invalid.
- No ambient state: probe result is a function of (engine commit, model hash, battery version, runner env). If not reproducible from repo alone → not a result, an anecdote.
- Transport is the only network-boundary surface; Execution/Models/Return never touch the wire directly.

### First executed rung (arm-probe proof)
The dispatch-label-probe is the canonical trigger shape and the first rung: a label on a PR dispatches a probe run; runner executes; results attach to the PR. Reuse this trigger for every probe battery.

---

## 2. THE INTEGRATION — runner-loop → mission-of-missions

- **Executed-proofs as record's receipts.** Each completed run emits a receipt (SHA-256 of canonical result JSON) that lands on the triggering PR/release as a comment. These receipts are the mission-of-missions' evidence layer: every mission tick that exercises the runner leaves a verifiable receipt, not a narrative.
- **Runs as the loop's executed-moments.** A run is one tick of the perpetual loop (dev→host→pull-build-run-report→return→iterate). The mission-of-missions is the sequence of these ticks; each tick's artifacts/logs/verdict are the record. No tick without evidence; no evidence without a receipt.
- **Feed direction:** Return surface is the only surface that feeds back into code dev, hence into the next mission tick. The mission-of-missions advances only when a receipt is acted on (human or next commit).
- **Reproducibility invariant:** a mission claim is valid only if its receipt recomputes from the repo alone (engine commit + model hash + battery version + runner env). Ambient results are anecdotes, not mission evidence.

---

## 3. THE FIRST-DEPLOYMENT — exact contents (v1)

### What's built first (single smallest vertical slice that proves the loop)
A repo with one probe battery + one dispatch-label trigger + one runner that pulls, builds, runs, and posts a report back to the PR. Nothing else. Loop closed end-to-end with evidence = architecture real.

### v1 release contents (minimal, no extras)
- `probes/` — one battery, one model target
- `.github/workflows/` — one dispatch-label-triggered workflow
- `runner/` — pull/build/run/report script (self-hosted Avrea)
- `docs/crown-slice.md` — the crown slice doc
- Pinned engine version + model hash manifest (`models/manifest.json`: {name, sha256, url})
- Repo layout (from transport slice):
```
avrea-custom-code/
├── .github/workflows/
│   └── build-release.yml        # build-once → attach assets
├── engine/                      # compiled engine source
│   ├── src/
│   └── build.sh
├── models/
│   ├── manifest.json
│   └── *.gguf                   # gitignored, fetched at build
├── container/                   # (optional, GHCR only)
│   ├── Dockerfile
│   └── entrypoint.sh
└── runner/
    └── pull-and-run.sh
```

### Explicitly NOT in v1
Multi-head, persistent sessions, secrets management, state-sync policy. Each is a later slice gated on evidence.

### Exit criterion for "first release done"
A PR with the dispatch label produces a report comment that a human (or the next code commit) acts on. Loop closed once = architecture adopted.

### Sequence
1. Week 1 — Transport + Execution. Dispatch label → runner pull-build-run → artifact upload. Prove the arm moves.
2. Week 2 — Models slice. Pin engine + model hashes; runner loads by hash; probe battery runs against local-LM; results returned. Prove the LM is a hosted-executed artifact.
3. Week 3 — Return loop closure. Report → PR comment → next-code iteration evidenced by a second commit driven by the first run's output. Prove the loop is perpetual, not one-shot.
4. Week 4+ — Partitioned-head mounting. Only after 1–3 close. Tackle the five open questions one at a time, each gated on evidence.

### Open questions (honest, unresolved — must not be faked)
1. State residency (repo-tracked vs runner-side store referenced by hash).
2. Trigger granularity (one dispatch per task vs persistent runner session).
3. Failure semantics (retry / replan / escalate on body failure).
4. Multi-head (one assistant per repo vs many heads sharing one runner).
5. Secrets (how body gets credentials without baking into brain/repo).

---

## One-paragraph synthesis
Build the smallest end-to-end loop first — dispatch label in, report out — treating the local-LM (engine + pinned models + probe battery) as hosted-executed artifacts in the repo, not ambient infrastructure. That loop is the assistant's residence in embryo: brain versioned, body unmetered, connected by the spine. Mount the partitioned head only after the loop closes, one open question at a time. One loop closed with evidence is worth more than five slices described.
