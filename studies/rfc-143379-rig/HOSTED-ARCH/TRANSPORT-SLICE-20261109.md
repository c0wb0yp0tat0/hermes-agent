# Transport-Slice — Hosting & Pull Mechanics

Target: self-hosted Avrea runner (labels: `avrea-ubuntu-latest`, Linux, self-hosted, X64; 12-core/16GB). GitHub is the distribution spine; runner is the execution arm.

## 1. Repo structure

```
avrea-custom-code/
├── .github/workflows/
│   ├── build-release.yml        # build-once → attach assets
│   └── build-image.yml          # GHCR option
├── engine/                      # compiled engine source
│   ├── src/
│   └── build.sh                 # produces engine binary
├── models/                      # quantized model manifests
│   ├── manifest.json            # {name, sha256, url}
│   └── *.gguf                   # gitignored, fetched at build
├── container/
│   ├── Dockerfile
│   └── entrypoint.sh
└── runner/
    └── pull-and-run.sh          # what the runner executes
```

Principle: source + manifests in git; heavy artifacts (engine binary, `.gguf`) never committed — attached to release.

## 2. Release-assets pipeline (build-once → release → runner pull)

**Workflow `.github/workflows/build-release.yml`:**

```yaml
on:
  push:
    tags: ['v*']
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build engine
        run: cd engine && bash build.sh   # -> dist/engine
      - name: Fetch models
        run: bash scripts/fetch-models.sh # verified by manifest sha256
      - name: Create release + attach assets
        uses: softprops/action-gh-release@v2
        with:
          files: |
            engine/dist/engine
            models/*.gguf
            models/manifest.json
```

**Runner pull (no rebuild):**

```bash
# runner/pull-and-run.sh  (runs on avrea-ubuntu-latest)
set -euo pipefail
TAG="${1:-latest}"
ASSETS="https://github.com/OWNER/avrea-custom-code/releases/download/${TAG}"
curl -fsSL "${ASSETS}/engine" -o /opt/avrea/engine && chmod +x /opt/avrea/engine
curl -fsSL "${ASSETS}/manifest.json" -o /tmp/manifest.json
jq -r '.[].name' /tmp/manifest.json | while read -r m; do
  curl -fsSL "${ASSETS}/${m}" -o "/opt/avrea/models/${m}"
done
sha256sum -c /opt/avrea/models/manifest.json   # verify
/opt/avrea/engine --serve
```

Transport: GitHub release asset URLs (CDN-backed), pulled once per runner, cached in `/opt/avrea`.

## 3. GHCR option (container image)

**When right:** when the engine + models + deps must move as one immutable unit, or runner lacks build toolchain. Overkill for a single binary + model files.

**Workflow `.github/workflows/build-image.yml`:**

```yaml
on:
  push:
    tags: ['v*']
jobs:
  image:
    runs-on: ubuntu-latest
    permissions: {packages: write}
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          file: container/Dockerfile
          push: true
          tags: ghcr.io/OWNER/avrea-custom-code:${{ github.ref_name }}
```

**Runner pull-and-run:**

```bash
echo "$GHCR_PAT" | docker login ghcr.io -u OWNER --password-stdin
docker pull ghcr.io/OWNER/avrea-custom-code:${TAG}
docker run --rm -d --name avrea \
  -v /opt/avrea/data:/data \
  ghcr.io/OWNER/avrea-custom-code:${TAG}
```

## Decision rule

- Release assets: default. Binary + models, runner pulls cheaply, no container runtime needed.
- GHCR: only when reproducibility of full env matters or deps are heavy/non-portable.
- Both can coexist: release assets for fast iteration, image for pinned production.