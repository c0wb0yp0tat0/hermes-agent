# RD-RUNNER-IDLE-FILL-20261111 — the idle-fill problem statement, R&D

**Date:** 2026-11-11 (ET) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Gate:** nothing public without the operator's word.

## 1. THE ONE-LINE STATEMENT (the separation test)

**ONE statement:** the runner's idle windows produce verified, rowed work — never derailing the wave.

**ONE mechanism.** VERIFY (the deterministic receipted legs at green pins) and MEASURE (the battery legs) share the runner's job loop — that is the job loop, not two. STAGE (the patrol's support previews — drafts only) is the existing idle-fill, and its receipt gate must go green FIRST. The derail-guards are the gates, not a split.

## 2. THE GROUND, VERIFIED THIS SESSION (byte-level)

- The runner (`pve1-avrea-parallel`, self-hosted, UNMETERED) is **online** (API: status `online`).
- Its standing idle-fill (the kindness-patrol workflow) is **RED 5/5** at the receipt step: runs 43000924909 / 43003797597 / 43005983573 / 43016468942 / 43017141142 — the class-chain: the pre-fix SyntaxError → after the de-f-string + UA carry, the NEXT seam = `<stdin>` line 23's `urlopen` raising an **unhandled HTTPError** (the fetch's auth/limit class — the traceback ends at `http_response → self.parent.error(...)`, exit 2). The patrol's rows never land; the runner-side voice in the machine-log is silent, and the sweep rows had to hand-carry the patrol's story.
- The dispatched verify leg at the interim head failed: run 43016521299, the Avrea full-suite jobs exit **4** (the pytest usage/collection seam at pin 485119a8 — not a green receipted pin).
- The wave's live lanes (B05-A-R2 landed bceba54157, B05-B-R3 + KTRIO-AUDIT in flight) run on the free seats against the study branch's working tree — single-writer.

## 3. THE FILL-QUEUE DESIGN (first cut)

1. **THE RECEIPT GATE FIRST** — the patrol's receipt step is repaired before any fill-work rides it: the fetch at line 23 carries the Authorization (the GH_TOKEN) + the UA + the retry/backoff, and a failed receipt becomes a LOUD row, never a silent exit. The recorded intent already names it (the ACES improve-pass: "the patrol's own receipt cannot fail silently again").
2. **THE PARALLEL TRACK (the user's standing, sharpened 11-11)** — the fill-work is a PARALLEL task with its own triage slot, never a subordinate that starves: it dispatches in the runner's idle slots (the runner idle = the fill's schedule — the watcher's sweep detects the idle window and fires the queue's next leg). The collision rule, not the ordering rule: the wave's verify legs and the approvals PREEMPT the fills when they need the runner; everything else, the fills run alongside, in the gaps, on the cadence.
3. **GREEN-PINS-ONLY** — the fill legs are the RECEIPTS.md rows whose pins are battery-green at the CURRENT head — the interim-patrol-head verify (the exit-4 class) is the derail-shape, refused by the pin-gate. The run-a-leg guide's volunteer path already defines the leg shape (the pinned workflow + the RUNNER-ROW report); the fill-queue runs the same legs on the rig's own runner in the gaps.
4. **THE FILL-SCHEDULER** — the idle-floor fires the next spec-complete leg from the queue (the run_eval battery legs at the green pins, the receipt re-verifications) with the row-on-arrival contract; the queue's size is bounded (the gap-window, never the backlog).
5. **THE DERRAIL-GUARDS (hard)** — the fill-work builds its own checkout (never the study branch's working tree — the harness lanes' single-writer); nothing public, ever, without the operator's word; the pins it verifies come from the RECEIPTS ledger, not the interim heads; the fill rows ride the envelope form, handles only.

## 4. THE SEQUENCE (the R&D's loop)

1. The patrol's receipt repair (auth + retry + loud-row) — the study-ref script, verified by a dispatched patrol run (GREEN).
2. The Avrea exit-4 seam's fix (the invocation's collection check at the dispatch head).
3. The fill-queue spec from the RECEIPTS green pins (the run_eval legs + the re-verification rows) — dispatched into the rider's next idle window.
4. The wave's landings keep priority: B05-B-R3 + KTRIO-AUDIT landings → the ACES audit → the AoA — the fill never preempts the wave (the gates hold the order).

## 5. NEXT-LAUNCH

(1) the patrol receipt-step repair + a dispatched GREEN patrol run · (2) the exit-4 diagnosis · (3) the fill-queue's first GREEN leg across the idle window.

## 6. THE REFERENCE RECEIPTS (the branch's own verified record)

- `6bb5c3480c` — "runner: receipt-step retry+loud-row (patrol 403 class) + the battery path-tolerance guard (the write-gate path's exit-4 class — the 11-05 earned pattern extended)". The workflow's receipt step now retries the fetch with the auth + UA + backoff and a failed receipt exits loudly. **This is the gate repair the fill-queue depends on.** The .yml carries the receipt row as a `gh api POST` with retry and a LOUD failure.
- `97ffe7655d` — "kindness-patrol: the receipt row rides the runner's own authed gh CLI (the GITHUB_TOKEN's comment-write 403 class proven after the retry+loud-row pass — the self-hosted runner's PAT is the thread's writer)".
- `62e993d1be` — "kindness-patrol: the runner's idle-floor script (stages support previews; never posts — the operator's word is the only gate)".
- `FINISH-LINE-REPLICATION-20261105.py` / `FINISH-LINE-REAPEX-20261105.py` — the failable acceptance written before the runs (the finish-line-first shape); the dispatch rules' pattern.

## 7. THE DERAIL-GUARD REGISTER

| Guard | How it holds | Status |
|---|---|---|
| Receipt gate first | the patrol's receipt step is repaired before any fill-work rides it | repair at 6bb5c3480c, awaiting a dispatched GREEN run |
| Pins from the RECEIPTS ledger | the fill legs verify only green pins, never the interim head | the interim-patrol-head verify (exit-4 class) refused by the pin-gate |
| Fill builds its own checkout | never the study branch's working tree | hard guard, to be enforced on the first fill leg |
| Nothing public without the operator's word | the runner sends drafts only; the operator's "go" is the only publication gate | the kindness-patrol's existing rule, the fill adopts it |
| The wave's verify legs and approvals preempt the fills | the collision rule holds order | the gate's rule, the fill runs in the gaps |

## 8. THE 5-LINE SUMMARY

1. The runner's idle windows are a schedule, not a void: the watcher's sweep detects the idle, the fill-queue fires the next green-pin leg, and the wave's verify legs and approvals pre-empt the fills when they need the runner.
2. The receipt gate first: the patrol's receipt step is repaired (retry + UA + loud row), and a failed receipt becomes a LOUD row, never a silent exit.
3. The fill-legs verify only pins that are battery-green at the current head; the interim-patrol head's exit-4 class is refused by the pin-gate.
4. The fill-work is a parallel task with its own triage slot, running in the runner's idle gaps on the cadence, never a subordinate that starves.
5. The wave's landings keep priority: B05-B-R3 + KTRIO-AUDIT landings → the ACES audit → the AoA — the fill never preempts the wave (the gates hold the order).

*Finding (one line):* the runner's idle-fill is the parallel track in the job loop — the receipt gate is repaired first, the refill legs verify only green pins, the wave's legs and approvals pre-empt the fills, and the idle gaps produce verified, rowed work without derailing the wave.

*Next mechanism (one line):* a dispatched GREEN patrol receipt run (the receipt gate green) followed by the fill-queue's first GREEN leg across the idle window, with the pin-gate refusing the interim-patrol head's exit-4 class.
