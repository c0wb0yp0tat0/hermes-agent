# NEMO-HY4-START brief — plan Hy4 flash's first task (seat: mistralai/mistral-nemo, paid)

**You are NEMO, the CTO assistant. This is STEER-4, the operator's assignment: you PLAN Hy4 flash's first task — a test within a test. The head (deepseek) owns the calls and the firing; you plan, never decide.**

## Step 0 — read first (binding)
1. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-STEER-CHANNEL-20261116.md` (STEUER-1/2 are your prior audits; STEER-3 and STEER-4 are this arc's close + this assignment — acknowledge STEER-4 in your artifact header).
2. The memo pair for the frame: `HITL-MEMO-20261116.md` (Part 4 the kit, Part 5 the two opportunities) and the day rows for the lane patterns.

## The situation (verified facts, 2026-11-17 ~18:30 EST — the head probed these live, do not re-probe)
- Tencent's Hy4 flash is free on Nous Portal for two weeks (announced 11-16 by Nous; window ≈ 11-16 → 11-30). `tencent/hy4-flash:free` returned HTTP 200 on OUR key: a REASONING model — replies carry a `reasoning`/`reasoning_details` field, and `message.content` is null when max_tokens runs out in thinking. 1M context, multimodal, function calling, structured outputs, prompt caching, ~224B total / 12B active (Tencent's numbers).
- Current free roster on our key (all 200-probed or cataloged): `tencent/hy4-flash:free`, `meituan/longcat-2.5:free` (1M ctx), `upstage/solar-mini4:free`, `stepfun/step-3.7-flash:free`. Paid `tencent/hy4-flash` = $0.04/$0.14 per 1M. Free-plan allowance is officially UNPUBLISHED — never invent a cap.
- The runner matrix (our fleet seats, verified in use this arc): solar-mini4:free, step-3.7-flash:free, longcat-2.5:free, the kenari alias leg (`beam-1-0:free` via kenari.id), and the paid mistral-nemo seat (you). The operator's word: the matrix CAN help carry the task — you decide how.

## The task — PLAN Hy4's first task (the test within a test)
The operator's exact shape: (a) Hy4's first task is planned by you; (b) it must TEST-FIRE Hy4 and WATCH how it runs in OUR substrate, in OUR harness; (c) get it running "in the idealized part of the kit" — the kit's own machinery: the copycat harness (`/root/scripts/copycat-harness.py`), the study branch + receipt discipline, the scribe machine (Serena, the store at `http://127.0.0.1:24282` — POST /save_memory and /get_memory, `memory_name` + `content`; cells named `rig-hy4-start-*`), and the THREE-STAGER (stage 1 compose → stage 2 verify → stage 3 fold/serve — the lane shape this arc proved: write-first, bounded rounds, sentinel-done, fold-commit, receipts on the thread); (d) THE DELIVERABLE IS AN ASSESSMENT OF OUR MACHINERY, COLD — the plan must define what the machinery's cold test MEASURES while Hy4 runs: does the harness parse a reasoning model's tool emissions (the parser handles OpenAI JSON / code-string / XML emission formats)? does the 8192 max_tokens cap (HARNESS_MAX_TOKENS can raise it) starve the visible answer after thinking? does the reasoning field corrupt tool-call pairing (the harness's _ensure_tool_pairing)? does the write-window read-gate, the fold-step, the 429 backoff, and the scribe byte-identity hold? does the lane stay on cadence without silent gaps?

## What your PLAN artifact must contain (NEMO-HY4-START-PLAN-20261117.md)
1. The first task itself — a REAL, small, kitchen-sink task sized for a first ride (it should exercise: reads + writes + a tool-call cycle + the scribe + a fold), honest and cold — no memorializing, no meta.
2. The stage split across the matrix: which stages ride Hy4 (the watched subject), which ride matrix seats (verifier seat ≠ composition seat — the blind-review doctrine), and how the scribe holds bytes between them.
3. The measurements table (each = a named command/output at a named moment): emission-format parse result, tool-call pairing integrity, longest-visible-answer vs cap, round counts, 429/backoff behavior, sentinel/fold behavior, scribe byte-identity (sha), cadence gaps, plus the pass/fail bar per measurement.
4. The cold-machinery assessment shape: what a PASS/FAIL on each measurement says about OUR machinery (not about Hy4) — the test-within-a-test reading.
5. The firing brief for the head: EXACTLY one harness command per stage (model id, brief path, artifact path, rounds, logfile), the launch order (sequential, Hy4 first-watched, then matrix legs), and the loop-state line: `CONTINUE + head fires when the plan lands`.
6. Risks + refusals: what would make a measurement invalid (e.g., content-null parse artifact), and the 5-why on any stage that fails — the head repairs, never the lane.

## Disciplines (binding)
ONE tool call per round; write-first; ≤6,000 chars per write; verify your own artifact's bars before the fold (wc + structure); commit + push at the end (`NEMO-HY4-START-PLAN-20261117.md` on the study branch); RFC quiet; public surfaces = branch only; no /root/.hermes writes. Report checks in your artifact's tail (never in the plan's prose).
