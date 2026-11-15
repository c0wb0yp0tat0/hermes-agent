# VALUE-ADD INVENTORY — 2026-11-07
## Retrospective extraction: aspects of the runs already run that carried the most value

**Source archive:** `/root/.hermes/plans/`, `/root/workspace/master-page/deepdive-mission-flow/` (ACES series, adjudication/adversarial-gate pair, SBI work, run readouts), `/root/workspace/master-page/memory-chain/002-lessons.md`.

**Honesty rule:** aspects that LOOKED valuable but produced little are named in §Value-Add vs Theater.

---

## Top-8 value-add aspects

1. **Self-fire checkpoint + handle verification (002:195 FIX-NOW #1-3)**
   - Evidence: C26-C32 e2e investigation; watchdog-aces-e2e-verdict; C33 audit leg.
   - Receipted outcome: missed self-fires caught; JOB_NAME bug fixed; chmod +x enforced.
   - Why value-add: converted "dispatch claimed" into "dispatch verified — handle: JobID=<id>"; eliminated the single largest failure class (85% flight-side).

2. **Price gate (price_gate.py) as machine-checked allowlist (§5 Rule 18)**
   - Evidence: FIX-PRICE-GATE; WALLET-AFTERMATH ($4.72/86 calls).
   - Receipted outcome: paid slip blocked at every dispatch surface; `gpt-5.6-sol→BLOCK` verified.
   - Why value-add: real money risk → machine gate; doctrine text pinned to mechanism (Rule 21).

3. **Termination budget as dispatch precondition (Rule 23)**
   - Evidence: FC-2 (3h22m hang, no max_tokens), FC-8 (max_tokens:null cohort).
   - Receipted outcome: 2-leg consensus (LagunaXS #4 + LagunaS blocking); highest-leverage failure class closed.
   - Why value-add: dispatch-time defect caught pre-send instead of 3h later.

4. **Adversarial pre-commit gate (Red Team in its slot)**
   - Evidence: 002-lessons 09-19 (extra paren in visibility.html caught before ship).
   - Receipted outcome: shipping-blocking bug caught; logged as win, gate retained.
   - Why value-add: a gate that fires is the mechanism working, not a failure.

5. **Blind 3-lane rotation + audit-of-audit restart (full ACES)**
   - Evidence: ACES-RE-ORCHESTRATION §2; 002:73 termination condition.
   - Receipted outcome: C26→C32 ran end-to-end; audit-of-audit returns PASS/PARK only when no measurable change.
   - Why value-add: turns single-pass review into repeat-until-no-change with restart on pull.

6. **Single-writer fold + scripted/idempotent mirror (drop_sync.py)**
   - Evidence: 002-lessons 09-19; bridge_sync self-consuming PR (#46).
   - Receipted outcome: 152-item mirror verified hashes+200s; sync consumes own PR; pile cannot regrow.
   - Why value-add: generated blocks never hand-edited; coherence by construction.

7. **Evidence-grounded claims re-verified against disk (bench-grade lesson)**
   - Evidence: run2 ledger 55,032 vs disk 55,189; run3-short "identical" claim vs KeyboardInterrupt on disk.
   - Receipted outcome: ledger claims corrected; adversarial gate retained.
   - Why value-add: a ledger is a claim, disk is reality; re-verify size/hash/content before shipping.

8. **Visible-path dispatch (delegate_task, config-pinned models)**
   - Evidence: 002:43/46; non-steerable detached hermes chat flagged as defect.
   - Receipted outcome: lanes appear in /pulse-agents.json; tracker truthful; mid-run steers possible.
   - Why value-add: converts invisible, unsteerable lanes into tracked, steerable ones at $0.

## Value-add vs theater (aspects that looked valuable but produced little)

- **Dark-horse local synthesis (LM Studio 9B) in tool-executing roles** — across v3/v4/v4.1/T3: 0 tool calls every run, fabricated commands/outputs. Value-add only via harness-side retrieval (T1c embedder path, UC-B); tool-executing roles stay with Gemma/head. LOOKED valuable (research-grade synthesis claim) but mechanism never fired.
- **Humanizer as a default layer in development briefs** — scope-bleed; grading corrupted (value-add ladder carried "humanizer-clean voice" dimension). Fix: development briefs carry NO humanizer mandate; voice is a deferred separate pass.
- **Repeated human correction as defect signal (002:37)** — gut-supported, untested; controlled test (002:103) showed directional but weak support (+9.7–15pp, keep-with-caution). Looked like a proven mechanism; evidence was thin.
- **Launch-tests checking only exit code** — three models "passed" with exit 0 while 404'ing; exit 0 with all-error output is not completion. Looked like verification; was a dead-looks-alive false win.
- **Fork doctrine activation on C29 PARK** — never activated (CLASS 6 defect); C29 PARKED with named alternatives but fork never ran. Looked like a doctrine; was a propose-only item needing user word.
- **ACES record + landing ledger fold (C27-C32)** — absent from both record and ledger; only watchdog-log.md carried the sequence. Looked like a completed fold; was a fold gap.
- **Task-file contention (shared watchdog-task.md)** — flight executes a subset and dies before time-sensitive tasks; looked like a queue; starved urgent work.
- **Skill descriptions over 60 chars** — rejected by skill_manage; index truncates to 57 + '...' destroying routing signal. Looked like a skill; never registered.

## Top-8 (final summary)

1. Self-fire checkpoint + handle verification
2. Price gate as machine-checked allowlist
3. Termination budget at dispatch
4. Adversarial pre-commit gate (Red Team)
5. Blind 3-lane rotation + audit-of-audit restart
6. Single-writer fold + idempotent mirror
7. Evidence re-verified against disk
8. Visible-path dispatch (delegate_task)
