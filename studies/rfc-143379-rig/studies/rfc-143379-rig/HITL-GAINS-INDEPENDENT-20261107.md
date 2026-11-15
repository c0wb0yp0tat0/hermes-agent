# HITL-GAINS-INDEPENDENT-20261107 — the independent eye (lane 5)

**Seat:** `stealth/crouton-alpha` (the second alpha-lane, the copycat role — the independent eye) **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public) **Register:** receipts, never claims. **Round-budget:** 40. **Method (binding):** cold reads only — study-folder listing + branch log + key artifacts' bytes; the team's summaries never taken as fact. Thread tail via `gh api` is UNMEASURED in this git-only lane (flagged wherever it matters, never filled in).

> **One-line finding:** The study's actual HITL gain is a *waiting discipline*: fork-only staging + a single user-word gate + a two-way-door record that survives re-walking — the amplifier's launch and the ACES loop's double convergence are gains precisely because they were *not* posted upstream without that word.

---

## 1. My own read — what the study ACTUALLY gained (receipts from my own reads)

### 1.1 The gate that held (the user's word as the only gate)
- `HITL-READY-20261105.md` (landed `6a990867ec`) stages 7 candidates (RFC-GUIDANCE, XNGG-VERIFICATION, runner-pipeline, fleet landings, webstorm-guidance, watcher-contract, recitation-arm), each with receipt + status + *decision awaited*. Its false-claims register reads: "Empty. The thread's claims all trace to their receipts."
- `FLEET-CYCLE-BODY-20261107-1403.md`'s CURRENT STATE (HEAD `015e365227`): "the upstream's surface quiet until the user's word (the authoritative gate — no self-gate, no re-ask beyond it)."
- My verdict: the gain is not speed, it is *non-action with receipts*. No upstream post, no public surface — every landing rowed on arrival, "the stalls as plainly as the greens."

### 1.2 The run-machine gain (amplifier + fabric, receipted at HEAD bytes)
- Universal-pin launch `9dc35ee053` (FABRIC-RECEIPTS, 31 forks, run-ids e.g. `agent-governance-toolkit …42349103810` → `projectsend …42349177806`); inputs-encoding finding banked in the same commit (422→204 on `-f inputs=` double-escape; `--input -` object form).
- Fabric 2.0 re-dispatch `2becb714af`: I read the HEAD bytes myself — 31 rows, per-fork pins, status column `queued` across the board (e.g. line 41 `agent-governance-toolkit | main | refire-v2 | 2bc3ef1887b0 | 42349942414 | queued`). **No conclusion column at HEAD.** The honest gain: 31 discriminating run-ids (the weak-receipt arm CLOSED in C3, `c9a0325719`), *not* 31 verdicts. Anyone claiming "31 GREEN" from branch bytes alone is ahead of the bytes.
- `ACES-IMPROVE-C3` (my read): 0 new commits since `653f535bfd`, 30 queued + 1 in_progress, thread UNMEASURED. The loop correctly named 0 improvements rather than inventing them.

### 1.3 The verification-loop gain (ACES converged, proved twice)
- Cycle counts from the log (my read): C1 14 named → 9 CONFIRMED / 2 NUANCED / 3 REFUTED (`5e0774420b` corrections C-1..C-5: IMP-1/6/7 struck on the 5-vs-6 miscount — a real self-correction, receipted); C2 4/4/0 (`93ced6090b`); C3 11/0/0 (`ca15b98e1f`); C4 11/11 (`c1965e6871`, `ccd33a1ebf` NO-IMPROVEMENTS CONFIRMED TWICE).
- The constant copycat `e1d9b0c51b` confirmed convergence across C1–C3 with C4 honestly UNMEASURED at read time. My independent read agrees on the *shape* (declining findings 14→0, two consecutive zero-cycles) even where I cannot re-derive every per-row count from the files sampled this session.
- Gain: the stop-line is a *measured* stop, not fatigue — 0 new commits since `653f535bfd` re-derived in both C3 and C4.

### 1.4 The human-register gain (the enrichment arc — the newest byte)
- `PR-ENRICHMENT-20261107.md` (`204bf6c672`, human register: amplifier + ACES-converged + scheduled rhythm + forward targets, two-way-door close) → independent audit `ENRICHMENT-AUDIT-20261107.md` (`537d2c3bda`, verdict **PASS**, per-axis ledger A1–A10 on my read) → record correction `f084af11cf` (the artifact's own drift named: mangled refs + scope-exceed + body's restore receipted).
- This is the HITL gain in its purest form: a human-readable story the producer wrote, an independent seat re-derived claim-by-claim cold, and the drift *named + corrected on the record* rather than smoothed. Three zero-write deaths, each evidenced on the thread with its class named (per FLEET-CYCLE-BODY-1403).

### 1.5 What I see that is NOT a gain (plain register)
- Fabric conclusions at HEAD: still `queued` in branch bytes. The GREEN claims in FLEET-CYCLE-BODY-1403 (Avrea union `42250764897`, fabric-battery `42349137165`) rest on run-ids cited in those files, not on conclusion rows in FABRIC-RECEIPTS at HEAD.
- W2-isolation: SEPARATION-UNMEASURED (the eval-runtime cannot execute the isolate re-run yet) — carried honestly as a wall, never spun.
- Thread tail: UNMEASURED in every git-only lane including this one. Any HITL synthesis claiming thread-verified facts from this lane is over-claiming.

---

## 2. The CROSS-READ — agreements and divergences vs `HITL-GAINS-SYNTH-20261107.md`

**Receipt for the synthesis's absence:** `ls studies/rfc-143379-rig/ | grep -iE 'HITL|GAINS|SYNTH'` (my read) returns only `HITL-READY-20261105.md` + `ONESHOT-THREAD-SYNTHESIS-20261106.md`; `git log --all -- studies/rfc-143379-rig/HITL-GAINS-SYNTH-20261107.md` returns empty. The synthesis **has not landed on this branch as of my read** (local HEAD `015e365227`).

| # | Item | Status | Receipt |
|---|---|---|---|
| X-1 | The user's-word gate as the binding HITL mechanism (fork-only, upstream quiet) | **AGREEMENT (expected)** — both this read (§1.1) and the prior fleet-cycle body (`015e365227`) converge on it; the synthesis, when it lands, must show the same receipts or diverge | `HITL-READY-20261105.md` (`6a990867ec`); FLEET-CYCLE-BODY-1403 bytes |
| X-2 | ACES convergence proved twice (NO-IMPROVEMENTS C3+C4) as the loop's gain | **AGREEMENT (expected)** — convergent with `ccd33a1ebf` / `c1965e6871` log subjects and with my §1.3 | branch log (my read, -25) |
| X-3 | Amplifier 31 run-ids discriminating; conclusions still queued at HEAD bytes | **DIVERGENCE RISK (flagged)** — FLEET-CYCLE-BODY-1403's "30/30 GREEN at per-fork pins" is *not* in FABRIC-RECEIPTS rows at HEAD (my read: all `queued`); if the synthesis repeats GREEN from the body file without the run-ids, it claims what branch bytes don't show — each such claim needs its run-id receipt | HEAD bytes of FABRIC-RECEIPTS (my read) vs FLEET-CYCLE-BODY-1403 CURRENT STATE |
| X-4 | Synthesis file present to cross-read | **ABSENT — UNMEASURED** — the cross-read's agreement/divergence table cannot be completed until `HITL-GAINS-SYNTH-20261107.md` lands; this row is the divergence's first data point: the synthesis is *behind* the independent leg, not ahead of it | ls + git log (my read, above) |
| X-5 | Thread-verified claims | **ABSENT — UNMEASURED** — no lane here can verify thread rows; any synthesis claim resting on thread bytes must be marked UNMEASURED, not CONFIRMED | IMPROVE-C3 / AUDIT-C4 method lines (my read) |

**The divergence is the data:** the team's parallel synthesis has not landed; my independent read therefore stands as the first HITL-gains receipt on this branch, and X-3/X-4 are the divergences the head must fold when the synthesis arrives — the GREEN-vs-queued gap and the missing-file gap are both receipted, not smoothed.

---

## 3. Landing note
Fork-only. Nothing public until the user's word. This file is the independent leg's landing; the synthesis's arrival will complete §2's table — until then, X-4 stands as written.
