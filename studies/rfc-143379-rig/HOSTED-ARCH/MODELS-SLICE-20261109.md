# Models-Slice — Local-LM Artifacts Hosting & Cache (2026-11-09)

## (1) Model-artifacts hosting (GGUFs + engine binaries as release assets)

- Host: GitHub Releases on the self-hosted runner's repo (same repo as custom code).
- Assets per release tag `model-<name>-<quant>-<enginecommit>`:
  - `<name>-<quant>.gguf` (single file if <= 2 GB; split into `.gguf.part-aa`, `.gguf.part-ab`, ... if > 2 GB using `split -b 2000m`, reassembled with `cat`).
  - `llama-server` / engine binary per runner arch (`linux-x64`, `linux-arm64`) built from the engine commit.
  - `sha256sums.txt` manifest: `<sha256>  <filename>` for every asset, signed via GitHub's release digest (no extra sig needed; sha256 is the integrity check).
- GitHub release asset hard limit: 2 GB per file (soft) / 5 GB practical; split at 2 GB to be safe. Total release size uncapped but keep per-model release <= 10 GB.
- Upload via `gh release upload` in CI after build; never commit binaries to git.

## (2) Runner cache (persisted model dir)

- Path: `/var/lib/avrea/models/` (persistent volume on runner, survives job runs).
- Cache key: `<model>-<quant>-<engine-commit-sha>` (model + quant + engine commit = key). Directory name = sanitized key.
- Layout: `/var/lib/avrea/models/<key>/{model.gguf, engine/, ready.flag}`.
- Download-once: on job start, check `ready.flag`; if present and sha256 matches manifest, skip download. Else fetch assets into a temp dir, verify sha256 against manifest, atomically rename to final key dir, write `ready.flag`.
- Concurrency: flock per key dir to avoid parallel downloads.
- Eviction: LRU by `ready.flag` mtime; keep total under 80% of disk (configurable `CACHE_MAX_GB`); evict oldest keys when exceeded. Never evict the currently-running key (pin via lock file).

## (3) First-execution flow & time budget

- First run (cold cache): full download of GGUF + engine binary. Expected: ~3–8 min for a 7B Q4 (≈4 GB) on runner bandwidth; split parts reassembled. Budget job timeout >= 15 min for first run.
- Cached run (warm): sha256 verify only (local, <10 s) + load model into memory (~30–90 s for 7B). Budget job timeout >= 5 min.
- Flow:
  1. Resolve cache key from model/quant/engine-commit.
  2. If `ready.flag` + sha256 ok → load (warm path).
  3. Else download assets → verify → atomic install → load (cold path).
  4. On any verify failure: delete partial key dir, re-download once; second failure → fail job with manifest mismatch error.
- Time-budget expectation documented in job's `timeout-minutes`: 20 (cold) / 8 (warm) — runner picks based on cache hit logged at step 2.