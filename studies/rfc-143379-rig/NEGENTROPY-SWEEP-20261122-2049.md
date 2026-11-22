# NEGENTROPY-SWEEP-20261122-2049 — the recurring sweep

**seat:** the copycat lane (recurring negentropy-sweep ride, no_agent arm) · **branch:** `study/rfc-143379-rig-20261105` · **fire time:** 2026-11-22T20:49Z · **the gate, verbatim:** "the gate: nothing public without the user's word." · **register:** receipts, never claims. **[1st]** = re-read by this lane this pass (git-tree/log/show + read_file); **[2nd]** = carried from a study doc, not re-derived; **HEAD-RECON** = the head's reconstruction. ABSENT + named, never invented.

*Delta baseline [2nd]: `NEGENTROPY-SWEEP-20261122-1848.md` @ `aa5e4234fe` (fire 18:48Z). Arming record [2nd]: `NEGENTROPY-ARM-EXECUTE-20261119.md`.*

## 1. THE WINDOW-CHECK (the gate)

| standing item | state | receipt |
|---|---|---|
| **W2-isolation settle-condition** (200/200 non-429 + judge 20/20) | **NOT MET** | judge-control clean 20/20 in BOTH fires [1st]; non-429 count = **0/20** at 13:23Z and **14/20** at the later fire [1st]. 1848's "done at L0 08:1x / L2 20:5x" is **stale** [2nd]. |
| **k-term two-tier re-measure** | **NOT RUN** | no k-term artifact in the last-20 commit log [1st, partial — log-depth 20]; baseline carried [2nd]: kept-rates 0.42/0.29/0.26/0.26 flat — contradicts the budget's differential-keep-rate presupposition. |
| **budget consolidation re-verify** | **NOT RUN** | carried [2nd]: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. |

**Countermove (W2):** the seat's fair-share window is the gate; the API names a fixed reset epoch ≈13:29:35Z (retry-after 384→371s across the window) [1st]. Re-firing without the head's window probe is burn — next move is the head's.

## 2. THE SEAM-SCAN (every fire)

| seam | current state | receipt | disposition |
|---|---|---|---|
| read-burn harness-deadline | arm patch landed 1814 [2nd]; arc 63/65/66/67 FAILURE → 68 SUCCESS [2nd]; kanban-pilot MISSION-5 SELD write-gate L0 **11/12 suites green** [1st] | `a65720275c` | AUTO-CONTINUE |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | no new fold artifact this pass | [1st] log-depth 20 | AUTO-CONTINUE |
| token watcher single-source line | `receipts/loop-state-negentropy.jsonl` **ABSENT from HEAD tree** (ls-tree grep empty) — still untracked | [1st] | HOLD-SAFE |
| machine-layer wire-checks | wire tip `bb3b33c7b7` (10:1x CADENCE): REF-3 0.0 (20/20 HTTP 200, judge 20/20, zero-gradient 5/5, GGUF `afa0567d` unchanged); REF-4 FIRED INCONCLUSIVE [2nd] | [1st] local **38 commits ahead** → wire stale 5h16m local | AUTO-CONTINUE (push) / HOLD-SAFE (freshness) |
| dispositions | AUTO-CONTINUE ×2 (push; MISSION-5) · HOLD-SAFE ×2 (watcher untracked; wire stale) · NEEDS-THE-CHAIR ×1 (W2 unmet — nightshift phase-2 already dispatched 12:25 local, `d49657d0d5`) | | |

## 3. THE ENTROPY CLASSES (CTO freedom applies)

- **Dead surface [1st]:** the branch's own wire vs local — 38 unpushed commits; the wire's REF rows are 5h16m stale and the sweep's delta baseline (1848) is 2h old. *Countermove:* push + re-baseline the next sweep on the new tip.
- **Loose thread (same-commit contradiction) [1st]:** `WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md`'s headline + §3.1 read **20/20 HTTP 429** at 13:23Z (ledger `…SETTLEMENT-QWEN4-20261122-3.json`, verdict INCONCLUSIVE, $0 billed), while the **same commit's** message (`597d4d198a`) reports **14/20 HTTP 200 + 6/20 429** and a NEW seam. The later fire's section is UNREAD by this lane (read-gated) → **ABSENT + named**. *Countermove:* the refire lane amends the headline or lands a §15 pointer; a headline that contradicts its own commit message is unrowed.
- **Loose thread (carried staleness) [1st]:** 1848's "W2 done" is stale against the wire's 10:1x REF-4 INCONCLUSIVE and the 13:23Z ledger. *Countermove:* re-mark done → NOT MET (done in §1).
- **Friction point [1st]:** the ARM-0 settlement is gated by a seat fair-share wall that opens/closed between the head's probe and the lane's fire; the API's retry-after is a fixed epoch, so blind re-fire is pure burn. *Countermove:* gate the next fire on the head's HTTP 200 + model-echo probe.
- **UNSPOKEN [2nd 1848, confirmed 1st]:** the sweep's own loop is the loudest entropy source — the loop-state token is untracked, so the loop's only lane-facing receipt is the sweep artifact itself. *Countermove:* track `receipts/loop-state-negentropy.jsonl` or name it out-of-scope.
- **PRIZE (unexpected) [1st]:** **REASONING-EXHAUSTION-24** — every HTTP 200 returned `content=null` with `reasoning_tokens=24=completion_tokens=max_tokens`; `by_reason.seat=14 / harness=6`. The seat spends the whole 24-token budget on reasoning and emits no content → the "0.0" is a **seat-format artifact, not a competence measurement**. *Countermove:* raise `max_tokens` (or take a non-reasoning route) and name the class in the next fire's pre-reg.

## 4. THE ORDERED NEXT-MOVES

1. **Push the 38 local commits.** gate: `ls-remote` before/after. seat: this lane.
2. **Re-mark W2-isolation done → NOT MET** in the next baseline. gate: the 13:23Z ledger + `597d4d198a` message. seat: this lane.
3. **Run the k-term two-tier re-measure OR strike the budget's class ordering.** gate: the flat 0.42/0.29/0.26/0.26 receipt. seat: budget lane / head.
4. **Reconcile the refire headline vs its commit message.** gate: same-commit byte-compare. seat: the refire lane.
5. **Track the loop-state token** (or name it out-of-scope). gate: `receipts/` in HEAD. seat: the watcher lane.
6. **Next ARM-0 fire gated on the head's window probe** (HTTP 200 + model echo). seat: head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

1. **Gate verbatim** — carried in the header; nothing public, upstream QUIET [1st].
2. **Register hand-separation** — every row tagged [1st]/[2nd]; the unread refire section named ABSENT [1st].
3. **Window-check** — W2 NOT MET (judge 20/20 clean; 0/20 then 14/20 non-429) [1st].
4. **Seam-scan** — write-gate L0 11/12 green; watcher token ABSENT from HEAD [1st].
5. **Entropy classes** — same-commit headline/message contradiction named [1st].
6. **Ordered next-moves** — six, each with gate + seat [1st].
7. **Compose-check** — this section; the eight steps close the loop on the artifact's own structure.
8. **Receipt stamps** — HEAD `b2f5603fff`; wire `bb3b33c7b7`; 38 ahead; baseline `aa5e4234fe` [1st].

## 6. THE LOOP-STATE LINE

**CONTINUE + push the 38 local commits (`b2f5603fff` vs wire `bb3b33c7b7`), then re-mark W2-isolation NOT MET at the next fire.** Receipt: `git ls-remote` truth before/after; the delta baseline is `NEGENTROPY-SWEEP-20261122-1848.md`.