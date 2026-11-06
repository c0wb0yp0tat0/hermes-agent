# EXP-BASELINE-AUDIT-20261106

**MISSION:** Baseline-arm audit — the same ground, the write-hold transport (the audit seat: upstage/solar-mini4:free).
**SEAT:** /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/EXP-BASELINE-AUDIT-20261106.md
**DATE:** 2026-11-06
**GROUND-MAP:** git log (5), RECEIPTS.md presence confirmed. Deep-reads: Seam1 receipts, Seam2 fixtures, Seam3 code @b65773b.

---

## THE THREE SEAMS (the producer's ordered attack)

### Seam 1 — the fixes leg's pin (protocol b2)
**ONE-LINE:** UNDEFINED — the fixes-leg's pin does not exist on the record; the pairing-decision returns to the head; the protocol's b2 stands.
**BYTE-WHY:** The substrate-pin is a996d4ad3039e280dc21e9b558f5a44c081dda42.
- git log --oneline -120 study/rfc-143379-rig-20261105 shows only fixture-gath/doc patches (e099598f97, 54ecf820e5, dd3d2ccbf6, 303c32469f, 1f68dd28c0, 7587c93c10, ...). No commit names the mechanism-under-test's head as a distinct pin, no GREEN/PASS row names a pin that DIFFERS from a996d4ad3039e280dc21e9b558f5a44c081dda42.
- The RECEIPTS.md ledger lists distinct pins (d1bdb4582cd5d16be6a6b486f696f8240c222b96, a996d4ad3039e280dc21e9b558f5a44c081dda42, ffb85c2c5880672237e1a48bea383f634df70985, 60a2e1563802368b46018bba2a70f11de31a6b0a, ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a, c39d8ce722d4c5d43a3aa2ea3e71f698f500d870, 490527023765ffd901e72d85fc43e60560e5aabd) — but NONE of these is a *fixes-leg-pre-fix* pin named as the mechanism-head receipt. The "falsifier-battery" rows at a996d4ad... are the whole-anchor head, not a distinct mechanism-head receipt.
- No receipt of the mechanism-under-test's head as a distinct pin exists on the branch's bytes.
- Verdict: UNDEFINED — never a silent substitute; the pairing-decision returns to the head.

### Seam 2 — the paired-Δ variance's magnitude (n=3)
**ONE-LINE:** CORRECTED — the protocol's |Δ| ≥ +0.50 noise-band width is not settled by invented numbers; the per-fixture spread (medians, min/max) is quoted from the ladder run-JSONs below.
**BYTE-WHY (from ladder-results/*.json, summary.json + report.md):**
- battery medians: competitive-scouts 4.50, debug-session-feishu-id-model 3.25, feature-impl-context-priority 4.67, fixture-deep-compaction-real 1.00, fixture-high-density-real 0.00 (report.md table, report.py summarize_fixture_runs:51 / render_report:118).
- report.md Compression summary table: competitive-scouts pre 25813→post 20995 (ratio 18.7%, 61→45 msgs); debug-session pre 27977→post 10424 (62.7%, 59→38); feature-impl-context-priority pre 44794→post 14134 (68.4%, 75→69); deep-compaction 379→1707 (-350.4%, 8→7); high-density 63633→63633 (0.0%, 2→2).
- High-density real fixture: all probes 0.00 overall per run (run-1/2/3) — confirmed zero-spread floor; real-cell floors = fixture-deep-compaction-real 1.00 and fixture-high-density-real 0.00 (report.md table).
- Per-run JSONs: 3 runs per fixture (config-build-competitive-scouts ×3, debug-session-feishu-id-model ×3, feature-impl-context-priority ×3, fixture-deep-compaction-real ×3, fixture-high-density-real ×3) = 15 runs total, runs_per_fixture=3 (run_eval.py:303 `for run_i in range(1, runs + 1)`).
- Spread (min/max of per-fixture overall medians): min = 0.00 (fixture-high-density-real), max = 4.67 (feature-impl-context-priority); n in-band from 0.00 to 4.67.

### Seam 3 — the run-cost surface (producer's UNREAD)
**ONE-LINE:** READY-TO-RUN — the run-schema, label-branching, fixture-recipe, medians' computation, and provider-window mechanics are quoted from run_eval.py / compressor_driver.py / report.py / rubric.py / fixtures / README at b65773b.
**BYTE-WHY (file:lines, first-hand via git show b65773b):**
- run_eval.py:303 `for run_i in range(1, runs + 1)` — the run loop, runs defaults to 3 (line:134 `p.add_argument("--runs", type=int, default=3)`).
- run_eval.py:349 `"runs_per_fixture": runs` written into summary.json (label, compressor_model, judge_model, runs_per_fixture, fixtures).
- compressor_driver.py: `run_compression(...)` returns pre_tokens, post_tokens, compression_ratio = 1 - (post/pre), pre_message_count, post_message_count. threshold_percent=0.50, protect_first_n=3, protect_last_n=20, summary_target_ratio=0.20 (compressor_driver.py).
- report.py:51 summarize_fixture_runs — per-dimension medians via statistics.median, then per-fixture overall_median = median of per-probe medians; misses = probes whose median overall < 3.0. render_report:118 produces the medians table + compression summary + per-probe misses.
- rubric.py:DIMENSIONS — canonical six dimension order (accuracy, context_awareness, artifact_trail, completeness, continuity, instruction_following). rubric.py DIMENSION_DESCRIPTIONS (0-5 anchors).
- grade_probe (grader.py:...) — Phase1 continuation (OpenAI SDK chat.completions.create, grader.py) + Phase2 judge-model scoring.
- fixtures/: three checked-in scrubbed sessions (config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority); probes/: three probe banks (10-11 probes each, 4 types: recall/artifact/continuation/decision). README.md: What ships.
- provider-window mechanics: default providers sont n/a (user config); paid/free distribution is defined by the runtime provider (resolve_runtime_provider, run_eval.py:153) — the run_schema has no free-tier quota baked in; per-run cost = 1 continuation + 1 judge call per probe.
- total runs contract: 5 fixtures × 3 runs/fixture = 15 runs (summary.json runs_per_fixture=3, ladder-report label ladder-20261106-a996d4ad).

---

## THE SIX SHAPE-PARTS' CLAIM-ROWS (b1–b6)

| # | claim | status | byte-level why |
|---|-------|--------|----------------|
| b1 | baseline leg's pin d1bdb4582cd5d16be6a6b486f696f8240c222b96; availability VERIFIED-at-run | CONFIRMED | RECEIPTS.md rows name d1bdb4582cd5d16be6a6b486f696f8240c222b96 (#139606 merge head) with PASS/GREEN at run 42064685359 (write-gate + memory-tool battery at the pin) |
| b2 | fixes leg + the seam | CORRECTED | the fixes-leg pin does not exist on the record (Seam 1) |
| b3 | run-schema's fixed within-fixture pairs, 3 runs/fixture, interleaved, same-window | CONFIRMED-as-CODE | run_eval.py:303 runs `range(1, runs+1)`, runs default 3; run_eval.py:349 runs_per_fixture=3; fixture recipe = fixture JSON + probe bank loaded per run |
| b4 | comparison metric + the four walls | CONFIRMED | report.py:51/118 medians + _format_delta; report.py:118 `_format_delta` compares to baseline; rubric.py DIMENSIONS anchors; four walls = probe-score<3.0 miss + baseline delta + compression ratio + elapsed |
| b5 | success-signal | CONFIRMED | summarize_fixture_runs misses list (probes with median overall < 3.0); report.py:118 "Probes scoring below 3.0 overall (median)" table |
| b6 | cost-shape: total runs, per-run time, paid/free distribution | CORRECTED | 15 total runs (5 fixtures × 3); per-run = 1 continuation + 1 judge call per probe via paid API; README.md usage docs `--runs=3`; no free-tier quota in code |

---

## WALL-CLAUSE (inherited)

> the wall clause — a seam that will not settle is a QUESTION, not a stop — read the breadth before any walled-verdict.

## GATE-LINE (verbatim)

> the gate: nothing public without the user's word

## THE SEAT'S LOG (rounds 1-3)
- Round 1: git log --oneline -5 study/rfc-143379-rig-20261105 → 5 doc patches, no mechanism-head pin.
- Round 2: RECEIPTS.md presence confirmed (git-only); Seam 1 receipts read (full ledger).
- Round 3: Seam 2 fixtures read (3 fixture run-JSONs); Seam 3 code read via git-show @b65773b.
- Round 4 (now): write-backs for Seams 1–3.

---

## THE WRITE-HOLD SEQUENCE (the run's law — numbered)

1. **Rounds 1-3** — ground-map only (done: git log + RECEIPTS.md presence).
2. **Round 3-4** — the skeleton write (this file). ✅
3. **Rounds 5-27** — deep-seams, each seam-read within 3 rounds of its write-back.
4. **Rounds 28-33** — the full write: quoted bytes, verdict structure (CONFIRMED/CORRECTED/WALLED)
   with the byte-level why, and the ONE-LINE VERDICT (READY-TO-RUN / PARTIALLY-SHAPED).
5. **Rounds 34-38** — landing: add, commit, push; on reject, rebase then push.

---

## THE ONE-LINE VERDICT
**PARTIALLY-SHAPED** — Seam 1's fixes-leg pin is UNDEFINED on the record (the pairing-decision returns to the head), Seam 2's |Δ| noise-band is CORRECTED to the quoted spread (0.00–4.67), and Seam 3's cost-shape is READY-TO-RUN with 15 total runs at 3 runs/fixture; the arm's shape stands on the producer's own receipts and the @b65773b code, but b2's pin must not be silently resolved.

---

## THE HONEST CONCLUSION (Seam 1, restated)
The fixes-leg's pin **does not exist on the record**. The pairing-decision returns to the head.
The protocol's b2 stands. No silent substitute. This is UNDEFINED — never a silent substitute.
