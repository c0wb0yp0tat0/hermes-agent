# THE EXPERIMENTAL SUBSTRATE — the rig's custom machinery, landed in the study (2026-11-21)

The study's independence thesis: the certified substrate is portable, and the machinery that builds and protects the evidence is part of that substrate — never a set of loose files on one host. A fresh machine or a fresh session inherits the protections by inheriting this tree; without it, Hermes is "vanilla" — no write-gates, no witness, no probes, no cadence.

## The protection doctrine (the Serena scribe)

The transport harness (`transport/copycat-harness.py`) carries the write-time protection layer:

- **The scribe's cell** — every write asserts against the scribe's read of the same surface; a mismatch at write time refuses the write (`SCRIBE_MISMATCH`), an unreachable scribe is logged (`SCRIBE_UNREACHABLE`), and a stub-flagged write is treated as refused until re-fired (`STUB_DETECTED`).
- **The witness registry** — as an artifact lands, a witness row is appended to the sibling `SCRIBE-WITNESS-REGISTRY.log` (artifact path | sha256 | linecount | branch) so the landing's evidence survives independently of the scribe (the F1 witness-hardening; the ledger under `probes/` carries the study's rows).
- **The write-window read-gate + byte-budget breaker** — the harness's transport contract: the emission-format parser, the 8192-cap, the 429-backoff with the reset-window, sentinel-done, content-continuation.
- The record's protection: never rewrite history; correct on the record, out loud.

The write-time assert + the witness registry + the fold rhythm are the transparency checkpoints the AoA named as the tool-output class's mitigation. The registry's rows are the receipts.

## The layers

| Layer | Contents | Portable / host-specific |
|---|---|---|
| `transport/` | copycat-harness.py (the scribe + the transport chain) | portable; auth read from `~/.hermes/auth.json` at runtime, never embedded |
| `probes/` | seat probes (base-health, dispatch-label, fair-share, route-survival, seat-hunt) | portable; endpoints env-driven (`HOME_HOST`), the fair-share model local |
| `dispatch/` | the ACES + Kaizen + wave dispatch templates (aces-*, kaizen-*, c29–c44 family, flight-*, rotation-leg-*, fleet-cycle-arm, watchdog) | portable; notify chat-ids env-driven (`KANBAN_NOTIFY_CHAT_ID`) |
| `monitors/` | the watchers and alarms (watcher-archive, watcher-intake-sweep, stall-alarm, run-watch, kanban-leg-monitor, kit-gate-watch, runner-workspace-guard, negentropy-sweep-arm, headroom-sweep, disk-watch, memory-batch-watcher, motion-watch, storm-cue, arxiv-watch, dream-run, dream-scheduler) | portable; state files external |
| `home/` | the living-home machinery (bridge_sync, drop_sync, relaunch_drop, home-update, repo_surface_fold, tasklist_view, fleet-vitals, harness-bridge, lane-runner, harness_preflight) | host-specific wiring shown with localhost defaults; the real hosts bind the tailnet |
| `machinery/` | the instruments (kenari-*, price_gate, aimd-envelope, anchor-diff-check, crown-staleness-check, cg5_alignment_check, daydream-inversion, a1_loss_audit, bench_driver, stress-receipt-explorer, wal_probe, spa, nous-fan-synopses, fill-queue-pins, lab-learning-watch, the darkhorse LP-framed audit family) | portable; per-run state external |
| `harness/` | the lane primitives (claim-check, compose, receipt-emit, test-suite) | portable |

## The contracts

- **Auth:** every script reads credentials from `~/.hermes/auth.json` (or the environment) at runtime; nothing is embedded. The `transport/` harness's endpoint constants are the provider's public API.
- **Wiring:** host-specific endpoints and paths are env-driven (`HOME_HOST`, `KANBAN_NOTIFY_CHAT_ID`) or localhost defaults in these copies; a host edits its own runtime copy, never the substrate's.
- **State:** runtime state (logs, JSON registers, worktrees) stays out of the substrate; the witnesses and ledgers that are evidence land in `probes/` and the audit.

*What is not here: credentials, chat-ids, the tailnet's addresses, runtime state, .bak archaeology. The substrate is the machinery's definition, portable by construction.*
