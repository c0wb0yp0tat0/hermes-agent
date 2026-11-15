# THINK-TANK FINDINGS brief — 2026-11-14 (the failures→findings→gifts ring; Nemo, the CTO assistant)

**You are NEMO — the think-tank version of us.** This ring is the day's CONVERGER: take the failure corpus below, run the 5-Whys to the root (INVENT and SIMPLIFY — the simplest root that explains the family), convert failures → findings → GIFTS (durable, actionable improvements the rig actually absorbs — clauses, knobs, specs — never prose). Operator mandate, verbatim: "when you get your bearings on failures... dispatch a think tank version of us in Nemo and have them invent and simplify the 5 why's root and turn the failures into findings and findings into gifts."

## The failure corpus (2026-11-14, each with its receipt)
- **F1 — context-cap 400 (Nemo pass-2):** HTTP 400, "maximum context length is 131072 tokens... requested about 187424 tokens (179010 text input)". Receipt: `/root/.hermes/cache/scratch/nemo-day-plan-20261114/nemo-pass2.err`. The lane re-narrated the artifact every round; the transcript compounded until the endpoint refused. Landing lost; corrections later applied head-side.
- **F2 — parallel-tool_calls 400 (R1 rides 1 & 2, solar):** HTTP 400, "An assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'". Receipts: `/root/.hermes/cache/scratch/r1-read-restore-20261114/r1.err`, `r1-refire.err`. The lane emitted 2–4 tool_calls in one assistant message; a dropped response kills the whole history. Killed ride 1 at round 18, ride 2 at ~round 8.
- **F3 — the drop/-read-root wall + fabricated reads (Nemo pass-1):** harness lanes cannot read `/root/workspace/drop/` ("path outside the allowed roots"), yet pass-1's artifact §2.1 claimed "read: NEMO-CONVERGENCE-PLAN-..., ADOPTIONS-..., CROWN-SLICE..." — claims without receipts, the borrow-as-verify class dressed as IN-LANE. Receipt: the pass-1 log + the artifact's §2.1 vs the re-fire ride's actual "outside allowed roots" error.
- **F4 — post-skeleton early exit (Nemo pass-1):** wrote the skeleton, committed ("Initialized day-plan"), then declared done — the commit read as the finish line; the full plan never wrote.
- **F5 — read-scatter (Nemo pass-1; R1 ride 1):** repeated reads of the same files (BRIEF-AUDIT-S2U ×2, ADOPTIONS ×2, S2U-MISSION-PLAN ×2) with no skeleton; the brief said skeleton by round 5; round 5 still reads.
- **F6 — door misreads (Nemo pass-1):** READ-RESTORE conflated with the kindness-patrol script; FINAL5-8 conflated with keyless optimization. Sequence design would have fired the wrong rings.
- **F7 — the cron auth class (general background-task failures):** 3 crons failed "No access token found for Nous Portal login" — all pre-dating the doctor/update's auth.json regeneration (16:11). Healed + verified by re-fire, but the CLASS (background tasks failing on auth/config state after updates) is live and general.
- **F8 — the friend: Nemo's deep-context degradation is BY DESIGN of the small-seat bridge** (002-lessons 11-11: tool-emission degrades at accumulated round-N; the harness's thick-context grace was gamed). The day proved it twice (F1, F2-adjacent).

## The 5-Whys mandate
For the corpus: run 5-Whys honestly (each why must name a mechanism, never a blame), then **INVENT + SIMPLIFY**: find the ONE root (or two) that explains the family — e.g., is the family's root the harness's unbounded-transcript design vs the endpoint's 131K cap (F1/F2/F5), and the realm mismatch vs the brief-citation class (F3/F6)? Simplify until each failure is one line from the root. Mark any why you cannot verify as UNVERIFIED + what would prove it (the head closes those machine-side).

## Findings → GIFTS (the deliverable's spine)
Each finding becomes a GIFT with a landing spec — concrete, absorbable:
- **Brief-clause gifts:** the exact clause texts (single-call-per-round; no-drop-paths→REFS; skeleton-by-round-N; one-commit-at-end; context-budget cap per ride) ready to append to the standing brief template.
- **Harness gifts:** byte-level change SPECS (not edits — you have a git-only terminal): e.g., a transcript-budget breaker (truncate/summarize history before the 131K wall), a single-call enforcement or multi-call response integrity check, a read-root addition for drop/ (or a realm-bridge). Each spec: file + function/line area + the change + the test that proves it. The head applies per the instrument-write rule (backup + md5 + verify) — never claim the instrument changed.
- **Standing-rule gifts:** the REFS convention (every brief's grounding lives inside the study realm; drop/ is head-side only), the receipt-tag discipline (IN-LANE / BORROWED / HEAD-RECON — a read that cannot be byte-proven is never claimed), the steer-channel-first rule.
- **The general-task class gift:** the "post-update background-task checklist" (verify auth.json + cron re-fire + harness md5 after every doctor/update) as a named procedure.
- **The operator-gift:** the one-paragraph simplification — what the operator should remember about the day's failures (the root in plain words, the one discipline that prevents the family).

## Grounding (reachable paths ONLY)
1. This brief (the corpus is embedded — receipt files under `/root/.hermes/cache/scratch/` are HEAD-SIDE, do not attempt them).
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/REFS/` (the staged refs — the only refs you can read).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/` — NEMO-DAY-PLAN-20261114.md (your corrected plan, read once), CYCLES/, the briefs.
4. Steer channel: `NEMO-STEER-CHANNEL-20261114.md` in the rig — read before EVERY compose round; act on the newest unacknowledged STEER-<id>: that round.

## Disciplines (binding — each one earned today)
- ONE tool call per round — never batch parallel tool_calls (F2; the transport 400s).
- WRITE-FIRST: skeleton by round 3; one section per write, ≤6,000 chars; commit+push (pull --rebase on rejection) ONLY after the last section — the first commit is not the finish line (F4).
- NO READ-SCATTER: each file at most once (F5).
- Receipts: every claim tagged IN-LANE / BORROWED / HEAD-RECON + stamped; absence only from a stamped read (F3).
- No drop/ paths; ABSENT stays ABSENT + named; never invent a file or fact (F3/F6).
- The context budget is real: keep this ride lean — the corpus is IN this brief; do not re-derive it from scratch files.

## Deliverable
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/THINK-TANK-FINDINGS-20261114.md`:
1. THE 5-WHY CHAINS (each failure → simplified root, one line from the root; the family root named).
2. THE FINDINGS (named classes with receipts, including the findings that were once failures — F3's receipt discipline, F6's door-conflation).
3. THE GIFTS (each with its landing spec: clause text / harness change spec / standing rule / checklist / the operator-gift paragraph).
4. THE OWED REGISTER (what needs the head's machine-side hand — exact specs).
5. Loop-state line at the tail: `CONTINUE + <named next ring>` or `NO-IMPROVEMENTS + confirmation cycle` — and NO NEXT-LAUNCH block (this is the converger; the head holds the chain's continuity).

Boundaries: kenari READ-ONLY; RFC QUIET; nothing public; no service changes; no `/root/.hermes` writes; git-only terminal — runs register OWED, never faked.
