# Execution Slice — Runner Pull-Build-Run-Report Loop

## 1. THE DETECTION — how the runner knows hosted code changed

Trigger options, pick per repo class:

- **Push-trigger (webhook → runner)**: GitHub `push` event fires on default branch; runner pulls on webhook. Lowest latency (~seconds). Cost: requires a persistent webhook receiver on the runner (or a relay). Best for active repos.
- **Release-creation-trigger (webhook on `release: published`)**: runner polls nothing; acts only on tagged releases. Strongest reproducibility (pinned artifact). Latency = time to tag. Best for shipped products.
- **Scheduled-check (cron, e.g. every 5 min)**: runner runs `git ls-remote` / checks latest release tag; pulls if SHA differs. Zero infra beyond runner. Latency = cron interval. Best for air-gapped / low-traffic runners.

Tradeoffs summary: push = latency 1, infra high, reproducibility low (floats on tip); release = latency 3, infra low, reproducibility high; cron = latency 2, infra none, reproducibility medium (floats on tip but bounded).

Decision rule: use release-trigger when results must be reproducible; push-trigger for dev loops; cron as fallback only.

## 2. THE BUILD-ONLY-IF — cached vs rebuild

Inputs to the decision: (a) presence of release assets, (b) source SHA, (c) marker file.

Algorithm per incoming (repo, ref):

1. Compute `source_sha = git rev-parse HEAD` of pulled tree.
2. Check release assets for that ref: if a prebuilt asset exists for `source_sha` → **pull-and-skip-build** (download asset, verify checksum, run).
3. Else check local marker `/var/runner/cache/<repo>/<source_sha>.built`:
   - present and checksum matches artifact → skip build.
   - absent or stale → **build**.
4. Build writes artifact to `/var/runner/cache/<repo>/<source_sha>/` and writes marker.

Marker shape (JSON, one file per source SHA):

```json
{
  "repo": "owner/name",
  "ref": "v1.2.3",
  "source_sha": "abc123…",
  "built_at": "2026-11-09T12:00:00Z",
  "builder": "runner-id",
  "artifact": "dist/app",
  "artifact_sha256": "…",
  "build_cmd": "make build",
  "exit_code": 0
}
```

Invariant: marker existence is necessary but not sufficient — always re-verify `artifact_sha256` before run. Never trust a marker whose SHA mismatches.

## 3. THE RUN-AND-REPORT — execution contract

Output schema (JSON, emitted to `results/<run_id>.json` and uploaded as release asset on the same spine):

```json
{
  "run_id": "uuid",
  "repo": "owner/name",
  "ref": "v1.2.3",
  "source_sha": "abc123…",
  "runner_id": "…",
  "started_at": "…",
  "finished_at": "…",
  "exit_code": 0,
  "stdout_path": "artifacts/stdout.log",
  "stderr_path": "artifacts/stderr.log",
  "artifacts": [
    {"name": "report.pdf", "path": "artifacts/report.pdf", "sha256": "…", "size": 12345}
  ],
  "status": "success|failure|timeout",
  "receipt": "sha256 of this file"
}
```

Artifacts upload-back: runner creates a GitHub release (or attaches to the triggering release) with all `artifacts/*` plus `results/<run_id>.json`. Use `gh release upload` or REST; verify each upload with a GET + SHA check.

Receipt emit: after upload, runner posts a comment on the triggering commit/PR (or release) containing `run_id`, `status`, `exit_code`, and a link to the release. The receipt's hash is the SHA-256 of the canonical JSON (sorted keys) — recompute on the reader side to verify integrity.

Return path: results flow back through the same spine (GitHub) — never a side channel. The runner is the arm; GitHub is the spine; the receipt is the proof.