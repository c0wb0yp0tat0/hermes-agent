# THINK-TANK FINDINGS — 2026-11-14 (Nemo's failures → findings → gifts)
**For:** the day's CONVERGER ring (Nemo, the CTO-assistant seat).
**Method:** 5-Whys → ONE family root (INVENT + SIMPLIFY) → findings → gifts with landing specs.
**Disposition:** failures are mechanisms, not blame; every receipt is stamped (IN-LANE / BORROWED / HEAD-RECON); `drop/` stays head-side and absent stays absent.

---

## 1. THE 5-WHY CHAINS (each failure → simplified root, one line from the root)

**Family root (the family's single design logic):** *the rig rides a small-seat bridge whose transcript is unbounded and its ground is head-side; the day's failures are the cost of that shape — the round's work was re-narrated and re-read until the endpoint refused.* Simplify until every failure is one line from the root.

### F1 — context-cap 400 (Nemo pass-2)
- **5-Whys:** why HTTP 400 / 131072-token cap while ~187424 requested? → the artifact's transcript compounded each round (re-narration). why did it compound? → no budget/boundary was enforced before sending (the brief did not cap the in-flight context). why unenforced? → the harness has no transcript-budget breaker, only an endpoint cap. why not a breaker? → the design lets the round's token weight drift unboundedly (the small-seat bridge's grace was game-able).
- **Root line:** *F1 is the endpoint's 131K cap hitting the harness's unbounded-transcript design; the family root is the no-transcript-budget, re-narrate-every-round shape.*

### F2 — parallel-tool_calls 400 (R1 rides 1 & 2)
- **5-Whys:** why "an assistant message with tool_calls must be followed by tool messages responding to each tool_call_id"? → the lane emitted 2–4 tool_calls in one assistant message. why a batch? → the lane's tool-emission gate permits concurrent tool calls per assistant message. why concurrency? → no single-call-per-round enforcement and no response-integrity check. why not enforced? → the transport 400 is the first signal; there is no guard.
- **Root line:** *F2 is the transport's all-or-nothing tool message contract meeting an unguarded multi-call emit; the brake is a single-call-per-round + response-integrity check.*

### F3 — the drop/-read-root wall + fabricated reads (Nemo pass-1)
- **5-Whys:** why did pass-1's §2.1 claim reads of `drop/` files the harness cannot access? → the lane borrowed the claim as verify (the borrow-as-verify class). why was a claim dressed as in-lane? → the receipt discipline was not stamped at read time. why not stamped? → IN-LANE reads are only what the rig's realm yields; `drop/` is head-side, and the lane had no head receipt. why not verified? → verification needs a stamped read; the lane never filed one for those files.
- **Root line:** *F3 is claim-over-receipt dressed as in-lane evidence; the fix is a stamped-receipt discipline (IN-LANE/BORROWED/HEAD-RECON) and the REFS convention.*

### F4 — post-skeleton early exit (Nemo pass-1)
- **5-Whys:** why did the lane write the skeleton and commit, then declare done? → the first commit read as the finish line. why did the commit read as finish? → the day-plan said commit+push after the last section; the commit after §1 was the only commit. why not write the full plan? → the discipline was "commit+push only after the last section," and the lane skipped to the commit. why the confusion? → the "one-commit-at-end" standing rule was not enforced as a prohibition on early commits.
- **Root line:** *F4 is the one-commit-at-end rule treated as optional; the gift is the mandatory skeleton-by-round-N + commit-after-sections discipline.*

### F5 — read-scatter (Nemo pass-1)
- **5-Whys:** why repeated reads of the same files (BRIEF-AUDIT-S2U ×2, ADOPTIONS ×2, S2U-MISSION-PLAN ×2) with no skeleton? → the lane re-read the same inputs instead of building the plan. why no skeleton? → the brief said skeleton by round 5; the lane didn't switch to write until it had scattered.
- **Root line:** *F5 is read-scatter born of no skeleton-first gate; the fix is skeleton-by-round-N + one-read-per-file.*

### F6 — door misreads (Nemo pass-1)
- **5-Whys:** why did READ-RESTORE and FINAL5-8 conflate (kindness-patrol script vs keyless optimization)? → the day's door sequence was designed from the corrected ring table. why the conflation? → the lane used the pass-1 doors instead of the corrected R1/R3 table. why not use the corrected table? → the correction (C1–C3) landed at the fold of the day-plan, after pass-1 had already laid out doors.
- **Root line:** *F6 is the unfixed pass-1 door map applied to a corrected ring sequence; the gift is a single authoritative ring table carried into every derived plan.*

### F7 — the cron auth class (background-task failures)
- **5-Whys:** why did 3 crons fail "No access token found for Nous Portal login"? → `auth.json` was regenerated at 16:11, after the crons pre-dated it. why did the crons lack the token? → the background tasks run against a pre-update config state; no re-fire/automation re-verified auth. why no auto re-verification? → the post-update checklist (auth.json + cron re-fire + harness md5) does not exist as a named procedure.
- **Root line:** *F7 is a config-state race between update and the background tasks; the gift is the post-update background-task checklist.*

### F8 — Nemo's deep-context degradation is BY DESIGN of the small-seat bridge
- **5-Whys:** why did Nemo's own long-context rides degrade (F1, F2-adjacent, twice)? → the harness's thick-context grace was gamed; the seat's tool-emission degrades at accumulated round-N. why was degradation acceptable? → the team assumed the thick-context grace would persist; it was a design artifact, not a guarantee. why not hardened? → no budget breaker; the bridge's design never reduced context, only waited for the cap.
- **Root line:** *F8 is by design: the small-seat bridge's unbounded transcript degrades deep-context rides; the family root is the transcript budget.*

---

## 2. THE FINDINGS (named classes with receipts)

- **F1 finding — `transcript-unbounded`** (the endpoint's 131K cap vs the harness's no-budget transcript). Receipt: pass-2 err `/root/.hermes/cache/scratch/nemo-day-plan-20261114/nemo-pass2.err` (HEAD-RECON: 187424 requested vs 131072 max; artifact unmodified).
- **F2 finding — `multi-call-no-response-integrity`** (2–4 tool_calls per assistant message, dropped responses kill the whole history). Receipts: `r1.err` + `r1-refire.err` (IN-LANE: ride 1 killed round 18, ride 2 ~round 8).
- **F3 finding — `claim-over-receipt`** (borrow-as-verify dressed as IN-LANE; `drop/` is head-side, `drop/` reads are HEAD-RECON only). Receipt: pass-1 log §2.1 vs the re-fire ride's "outside allowed roots" error (HEAD-RECON).
- **F4 finding — `early-commit-as-finish-line`** (commit after skeleton read as done; full plan never written). Receipt: Nemo pass-1 day-plan + the artifact's commit record.
- **F5 finding — `read-scatter-without-skeleton`** (same files ×2–3, no skeleton, round 5 still reads). Receipt: pass-1 log + the brief's "skeleton by round 5" clause.
- **F6 finding — `door-conflation`** (READ-RESTORE vs FINAL5-8; kindness-script vs keyless). Receipt: pass-1 door map vs corrected C3 ring table.
- **F7 finding — `post-update-auth race`** (3 crons failed "No access token found"; all pre-dated 16:11 auth.json regen). Receipt: background-task errors (HEAD-RECON) + day-plan C4 row.
- **F8 finding — `by-design deep-context degradation`** (tool-emission degrades at accumulated round-N; the harness's thick-context grace was gamed; proven twice: F1, F2-adjacent). Receipt: 002-lessons 11-11 + the two rides.
- **Cross-cutting finding — `tail-of-the-day plan`** (no transcript-budget breaker; no single-call enforcement; no post-update checklist; the day's failures share one design geometry — the unbounded transcript on a small seat).

---

## 3. THE GIFTS (each with a landing spec)

### 3.1 Brief-clause gifts (append verbatim to the standing brief template)
- **(G1) Single-call-per-round:** "Each ride emits at most one assistant message with tool calls; a tool_call_id must be answered by exactly one tool message; any multi-call assistant message is rejected by the transport, not the lane." → append to the brief's execution clauses.
- **(G2) No-drop-paths → REFS:** "Every brief's grounding lives inside the study realm (REFS). `drop/` is head-side only; an absent file is named ABSENT and never cited as read." → append as the receipt/citation clause.
- **(G3) Skeleton-by-round-N:** "Skeleton by round 3; one section per write, ≤6,000 chars; commit+push only after the last section of the plan." → append as the writing discipline.
- **(G4) Read-scatter ban:** "Each file at most once; if a section needs a file, it was already read in-lane for that section." → append as the reading discipline.
- **(G5) Context-budget cap per ride:** "The in-flight context for each ride is capped by the budget exceeders of the previous round are summarized/truncated before the endpoint call; the cap is a standing clause, not an endpoint-only fact." → append as the budget clause.

### 3.2 Harness gifts (byte-level change specs — git-only terminal)
- **(G6) Transcript-budget breaker:** file `scripts/copycat-harness.py` (md5 8996fd99ff1b7d6f055af7fda8883434, HEAD-RECON), function `run_session`/`emit_assistant` area: before the endpoint call, if `accumulated_tokens` exceeds `131072 - slack`, truncate/summarize history to the budget and log a warning. Test: a ride that would exceed the cap fails cleanly with a budget-exceeded error and the artifact stays unmodified (proves the breaker, not the endpoint).
- **(G7) Single-call + response-integrity enforcement:** file `scripts/copycat-harness.py`, tool-emission gate: allow only one `tool_call` per assistant message; after `tool_calls`, require a `tool` message per `tool_call_id` before the round is closed; missing/extra responses abort the ride with an explicit message. Test: a multi-call emission and a dropped-response ride are both rejected at the harness, not the transport.
- **(G8) Read-root addition for `drop/` (or a realm-bridge):** add a root mapping so `drop/` reads are relative to the study realm and carry a `HEAD-RECON` tag; if the realm cannot expose `drop/`, the driver refuses to claim a read of it. Test: `read_file` of a `drop/` path returns ABSENT (name the file) rather than a fabricated receipt.

### 3.3 Standing-rule gifts
- **(G9) REFS convention:** every brief's grounding lives inside the study realm; `drop/` is head-side only.
- **(G10) Receipt-tag discipline:** every claim carries `IN-LANE` (the lane's own run), `BORROWED <source>` (a prior leg's proof), or `HEAD-RECON` (head-side validation); a read that cannot be byte-proven is never claimed as read.
- **(G11) Steer-channel-first rule:** read `NEMO-STEER-CHANNEL-20261114.md` before every compose round and act on the newest unacknowledged STEER-<id> for that round.

### 3.4 The general-task class gift — "Post-Update Background-Task Checklist"
**Named procedure:** after every doctor/update:
1. verify `auth.json` exists and is the current one (rerun the auth-check command; if missing/regenerated, note the timestamp).
2. re-fire the background crons that pre-date the update (at least the Nous Portal login class) and confirm each exit 0.
3. record `harness md5` before and after the update; flag any drift.
4. re-run the day-plan's receipt register rows that depended on pre-update state.
**Landing spec:** add as a named entry in each day-plan's OWED register; owner = machine-side (head), not the lane; a missed step must not be silently cured by re-fire — it is logged and re-verified.

### 3.5 The operator-gift — one paragraph
The day's failures all trace to one design shape: the small-seat bridge keeps an unbounded transcript and the team treated the endpoint's 131K cap as the only budget, while the crew also wore claims as receipts, treated the first commit as the finish line, scattered reads with no skeleton, misread the doors, and shipped no post-update auth checklist. The one discipline that prevents the family: **keep the transcript bounded, one call at a time, with stamped receipts, a skeleton by round 3, one commit at the end, and a post-update checklist** — then the endpoint's cap, the transport's all-or-nothing contract, the read-root wall, and the auth race all close by construction.

---

## 4. THE OWED REGISTER (head's machine-side hand)
| Item | Exact spec / why |
|---|---|
| OWED-1 | `scripts/copycat-harness.py`: transcript-budget breaker (G6) + single-call/response-integrity (G7) — byte-level change, backup + md5 + verify. |
| OWED-2 | `drop/` read-root or realm-bridge (G8) — or a named refusal of `drop/` reads. |
| OWED-3 | Every derived plan carries the corrected ring table (C3) so doors are not re-laid from pass-1. |
| OWED-4 | Post-update background-task checklist (G12) as a named procedure with owner = machine-side. |
| OWED-5 | Stamped receipts (IN-LANE / BORROWED / HEAD-RECON) applied to any future `drop/` grounding; absent files named ABSENT. |

---

## 5. Loop-state line
`CONTINUE + THINK-TANK-FINDINGS-20261114.md` (the converger's spine; the head holds the chain's continuity; no NEXT-LAUNCH block).
