# RELIABILITY-PASS — Hosted-Custom-Code Architecture (second seat)
**Date:** 2026-11-09 · **Lens:** reliability / failure-modes · **Register:** plain, evidence-carrying · **Limit:** ~10 min

Doctrine: failures are findings. The design must name its failure-modes + guards BEFORE the build. Each row: failure · trigger · guard · residual gap.

---

## 1. FAILURE-MODES REGISTER (per slice)

### Transport slice
| # | Failure | Trigger | Guard | Residual gap |
|---|---|---|---|---|
| T1 | Release-asset drift / 404 on pull | tag exists but asset missing/misnamed | curl `-fsSL` + sha256sum -c; fail fast | no retry/backoff; one missing part kills whole pull; no resume |
| T2 | Partial download (network drop mid-curl) | unstable runner link | none stated (curl writes partial file, sha fails) | no atomic temp+rename; partial file can be mistaken for complete on re-run; no resume (`-C`) |
| T3 | Checksum manifest itself tampered/missing | manifest path wrong | sha256sum -c against manifest.json | manifest not signed; attacker with release write can swap manifest+assets consistently |
| T4 | GHCR pull auth failure | expired GHCR_PAT | docker login; fail | no token-refresh / rotation policy; no fallback to release assets on image pull fail |
| T5 | Concurrent pulls clobber `/opt/avrea` | two jobs same runner | none stated | no flock; race on shared path; mixed-version state |

### Execution slice
| # | Failure | Trigger | Guard | Residual gap |
|---|---|---|---|---|
| E1 | Runner pull-failure (clone/pull) | webhook missed, runner offline | cron fallback (5-min poll) | no liveness/heartbeat on runner; stale runner silently misses pushes; no dead-letter |
| E2 | Build-only-if false-skip (stale marker) | marker present, artifact corrupted | invariant: re-verify artifact_sha256 before run | marker write not atomic; crash mid-write leaves half-marker; no fsync |
| E3 | Build failure mid-way | compile error | exit_code in marker; only written on success (implied) | partial build dir left; next run may reuse stale artifact if marker absent-but-dir-present check missing |
| E4 | Artifact upload failure | network/size | verify each upload with GET+SHA | no retry; "partial upload = run marked upload-incomplete, no receipt" — but no auto-retry/requeue; job just dies |
| E5 | Queue stall | runner busy, jobs pile | none stated | no concurrency limit, queue depth, or timeout-on-queue; a hung build blocks all |
| E6 | Report comment never posted | GitHub API rate limit | receipt hash recomputed on reader | no idempotent retry; receipt may be lost; ledger row stuck pending |

### Models slice
| # | Failure | Trigger | Guard | Residual gap |
|---|---|---|---|---|
| M1 | Cache corruption (ready.flag + sha mismatch) | disk error, partial write | on verify failure: delete partial key dir, re-download once; second failure → fail | only ONE retry; no quarantine of bad dir for forensics; eviction can race with running job |
| M2 | Split-part reassembly error | part missing/reordered | sha256 on final | `cat` concatenation has no per-part checksum; a swapped part passes only if total sha differs (it will, but error is late) |
| M3 | flock contention deadlock | parallel jobs same key | flock per key dir | lock file lifetime not specified; crashed job leaves stale lock → permanent stall unless flock is advisory+auto-release (it is, on process exit — OK if process dies; not if hung) |
| M4 | LRU eviction kills in-use model | cache pressure | "never evict currently-running key (pin via lock file)" | pin mechanism not implemented in stated flow; relies on lock file existing; eviction runner may not check it |
| M5 | Cold-run timeout | first download slow | budget 20 min cold / 8 warm | runner "picks based on cache hit logged at step 2" — but selection happens before step 2 completes; chicken-and-egg; job may time out on cold with warm budget |
| M6 | Model >2GB split at 2GB but GitHub 2GB soft limit | upload of part >2GB | split -b 2000m | 2000m = 2.0GB > 2GB soft limit; off-by-factor risk; no margin (use 1900m) |

### Return slice
| # | Failure | Trigger | Guard | Residual gap |
|---|---|---|---|---|
| R1 | Push 403 (token scope) | fork runner → study branch | AVREA_PUSH_PAT required; fallback patch+head-am | PAT rotation/expiry not handled; fallback requires human-in-loop, breaks perpetual loop |
| R2 | Receipt push race / conflict | two runs same branch | none | no rebase/retry on push conflict; receipt file collision on run_id (UUID, low risk) but branch lock absent |
| R3 | Ledger row never closes | missing receipt file | pending-receipt state; fold-gate requires both receipts | no timeout/escalation for stuck pending rows; ledger grows unbounded |
| R4 | Idempotent comment edit race | two runners same PR | find by marker, edit if exists | GitHub API eventual consistency; duplicate comments possible; no unique-constraint |
| R5 | Zero-delta terminal misread | measurement noise | "honest-negative accepted" | no definition of noise floor; a real tiny delta may be falsely terminal |

---

## 2. THE CROWN-RISK
**R1 — the token-scope wall (Return slice).** The whole architecture's loop depends on results landing back on the spine. The default GITHUB_TOKEN cannot push to the study branch from a fork-runner; the AVREA_PUSH_PAT fallback requires a human. If the PAT lapses or is absent, the loop silently degrades into manual patch-am, and "perpetual" becomes "manual." Guard present (PAT + fallback) but the fallback breaks autonomy. **This is the single failure that kills the architecture's claim.**

Guard strength: medium. The receipt still emits to the release (so evidence isn't lost), but ledger closure stalls. Mitigation: ship PAT-provisioning + rotation as part of v1, or move receipt landing to a path the auto-token CAN write (release asset + PR comment only, no branch push) and treat branch-landing as optional enrichment.

---

## 3. RELIABILITY-ADDITIONS (sharpest 2-3 still needed)

1. **Atomic, resumable transport (Transport T2/T1).** Every pull becomes: download to `<name>.part`, verify sha per-part where possible, atomic rename, resume with `curl -C -`. Add per-asset retry (3×, exponential) and a manifest signature (at minimum, pin manifest sha in the release notes / commit). Without this, a flaky link produces silent partial state.
2. **Runner liveness + queue discipline (Execution E1/E5).** Heartbeat endpoint or GitHub Actions runner status check; job queue with max-concurrency and queue-timeout; dead-letter on missed webhooks with cron-reconciliation that compares `git ls-remote` SHA vs last-processed SHA. Prevents silent stalls.
3. **PAT lifecycle + autonomous fallback (Crown R1).** Either provision AVREA_PUSH_PAT with documented rotation + expiry alert, or redefine "receipt lands on branch" as best-effort and make release-asset + PR-comment the authoritative receipt (which the auto-token CAN produce). Pick one before v1; do not ship both ambiguously.

Plus (honorable mention): define noise floor for zero-delta terminal (Return R5) and pin lock-file lifetime for model cache (Models M3/M4) — small, but each is a latent stall.
