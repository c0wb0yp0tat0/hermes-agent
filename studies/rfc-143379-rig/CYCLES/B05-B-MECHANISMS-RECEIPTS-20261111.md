# B05-B-MECHANISMS-RECEIPTS-20261111 — the backwards audit, night 11-05: MECHANISMS + RECEIPTS

**Lane:** B05-B · **Seat:** meituan/longcat-2.5:free · **Date:** 2026-11-11 (ET) · **Branch:** `study/rfc-143379-rig-20261105` · **Gate:** nothing public without the user's word.

**Write-window gate (registered).** This artifact was written at the harness's write-window gate (round ~9, due within 14). Byte-direct re-derivations are marked **[1st]** (re-derived this lane, from the branch's committed bytes at HEAD) or **[2nd]** (carried from a branch artifact's own receipt). The terminal's content-reads and the read-tools were gated mid-analysis; the absences the gate froze are named OWED, never inferred.

**Skills mandate (reported honestly).** `skill_view` is **ABSENT from this lane's tool inventory** (the seam the sibling lanes B06-B/B07-C/B08-B registered). The mandates — defect-forensics, investigation-documentation, agent-work-review, comment-driven-lab-ops — are applied as METHOD (byte-direct claim→PASS/FLAG with failure-mode, the absence-protocol, the machine-envelope decode) and the load is registered **OWED**, not papered. A landing that claims the skills loaded when the tool is absent would be the exact silent-skip class this audit exists to catch.

**Method.** Byte-direct where the lane's tools reach: `git show` / `git cat-file` / `git ls-tree` / `git log` / `git rev-parse` at HEAD, `read_file` on the study tree. No `gh` — the thread's live tail is UNMEASURED in-lane; the thread's 11-05 rows are read through the branch's own envelope-map (`ENVELOPE-TRANSLATION-MAP-20261106.md`) and the machine-log receipts. `/root/.hermes/cron/jobs.json` is outside the lane's read-root → the direct alive-now check is OWED. Every claim carries its read-stamp and byte; absence claims re-checked at a second stamp where the gate allowed.

---

## 1. THE WATCHER CENSUS — alive-then / alive-now

The 11-05 night's automatic mechanisms, from the thread's 11-05 rows' envelopes + the tree's sweep/arm artifacts. The 11-05 thread rows are the chronology the 11-06 synthesis registers (the launch row 6677338997 → the CTO-regroup 6684983987 → the wave-1 machine-log 6686579651 → the E-3 machine-log 6686903402); the machine-envelope schema (`id/kind/from/to/status`) is the watcher contract's own seed.

| # | Mechanism | Alive 11-05? | What it reported / caught | Alive-now |
|---|---|---|---|---|
| 1 | **The negentropy sweep** (the 2h cadence class) | **YES** | the apex-day sweep rows: **RED 42096589644** @ study-head (the nugget-6 substrate-absent class); **GREEN 42150952031** @ current head (the instruments executed at the pinned head, the CSVs re-produced) | **INDIRECT-PASS** — the `NEGENTROPY-SWEEP-*` series continues 11-07 → 11-11 (`NEGENTROPY-SWEEP-20261111-0634` is the scheduled sweep's receipt at this audit's own write-window) |
| 2 | **The fleet-cycle PR-body cycle** (the 3h class) | **YES** | the fleet's first fold landed + byte-verified (`77a441dc92` + wave-5 `6ded14715c`) — the longcat divergence | **INDIRECT-PASS** — `FLEET-CYCLE-BODY-20261107-*` … `FLEET-CYCLE-BODY-20261111-0008` |
| 3 | **The reapex-harvest** (the 1h class) | **YES** | `FINISH-LINE-REAPEX-20261105.py` — the re-apex run's **failable** acceptance check (written BEFORE the run; exits non-zero on any missing node) | **INDIRECT-PASS** — `REAPEX/` dir continues 11-09 (`STALL-ARMING-T0`, `THE-MISSION-OF-MISSIONS-ORCHESTRATION`) |
| 4 | **The pr1-watcher** (trigger-driven machinery) | **SEEDED** | the watcher contract: the machine-envelope (`id/kind/from/to/status`), the `[SELF-FIRE battery=… pin=…]` grammar, the poller's contract; decision "the build's go" | **CLAIM-UNVERIFIABLE from the branch** (the 11-06 summary says so; `HITL-READY-20261105.md` corroborates staging). The convention lives in `tmp-artifacts/pr1-watcher-contract.md` at HEAD |
| 5 | **The runner pipeline** (union → row → re-arm) | **YES** | 43 completions (27 failed / 14 succeeded / 2 canceled), green-rate **0.24 → 0.41** (+0.17); the guarded head's first zero-failed GREEN (16 passed / 77 skipped-with-reasons) | **INDIRECT-PASS** — the runner's arc continues (`42163546699` … `42250764897`) |
| 6 | **The copycat lane** | **YES** | five findings for 11-05: `copycat-beam/krecency/longcat/solar-mini4/step-20261105.md` (+ `.sentinel` each) | **INDIRECT-PASS** — the `CYCLES/` B-lane artifacts (B06-B, B07-C, B08-B, this B05-B) |
| 7 | **The finish-line acceptance checks** | **YES** | `FINISH-LINE-REPLICATION-20261105.py` + `FINISH-LINE-REAPEX-20261105.py` — failable checks over the ledger's promised artifacts | **INDIRECT-PASS** — the finish-line class continues (`FINISH-LINE-REAPEX-20261105.py` is the 11-05 form) |
| 8 | **The darkhorse / harness-bridge** (read-restore) | **YES** | the anchor-machine's retrieval-half; the read-restore arc's refusal-contract (NOT IN CHAIN) | **INDIRECT-PASS** — the read-restore arc continues (`EXP-REBUILD-CERT-20261106.md`, the darkhorse family) |

**What the census caught.** The 11-05 night's machinery was **alive and self-reporting**: the sweep fired RED then GREEN at two heads; the runner cycled 43 runs and climbed the green-rate; the fleet folded; the reapex check was written failable before its run; the watcher contract seeded the trigger grammar. The night's machinery also **caught itself**: the sweep's RED named the nugget-6 substrate-absent class, and the guard `76f95dd401` landed after the RED dispatches — the machinery's own correction loop.

**The dead-class names (the 11-05 forms).**
1. **Blind-but-honest (SEPARATION-UNMEASURED).** The sweep fires and reports its own blindness honestly (the GitHub-window side NOT RUN). Alive, subject unmeasured.
2. **Floor-blind (reapex-floor-unreadable).** The watcher cannot read its own floor plan (`/root/.hermes/plans/...`).
3. **Verifier-blind (fabric per-fork gh-unreadable).** The watcher reports the GREEN line from the cycle bodies but cannot independently verify per-fork statuses.
4. **Unmarked-fire (sentinel inconsistency).** The `.sentinel` convention is applied inconsistently across the watchers.
5. **Silent-skip (probe-fail → exit 0 → clock "ok").** NOT confirmable from branch bytes; requires the `jobs.json` last_status/error fields. Named, owed, not asserted.

**The cron roster cross-check — OWED.** `/root/.hermes/cron/jobs.json` is outside the lane's read-root (the terminal is git-only; the direct read is blocked). The record DOES say (`PR1-READ-20261107.md`, carried in the sibling B06-B's census): "145 entries → 16 live (129 consumed/expired removed, zero failures)"; "Scheduled: negentropy-sweep (2h) + reapex-harvest (1h) armed, read-back verified." The direct per-job last_status/error cross-check is **OWED** to a lane with `/root/.hermes` read access.