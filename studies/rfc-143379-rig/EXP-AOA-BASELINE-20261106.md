# EXP-AOA-BASELINE-20261106 — the baseline-audit's third base (the audit-of-audit)

**MISSION:** Audit-of-audit over the baseline-arm audit (EXP-BASELINE-AUDIT-20261106.md @ 18652062f0): re-hunt Seam 1's absence-claim, re-derive Seam 2's spread from the raw run-JSONs, spot-verify every Seam 3 quote at b65773b, and render a residual-fidelity verdict on the audit itself.
**SEAT:** /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/EXP-AOA-BASELINE-20261106.md
**DATE:** 2026-11-06
**GROUND-MAP:** RECEIPTS.md the branch's ledger; ladder-results/*.json (15 run-JSONs, 3/fixture); run_eval.py / report.py / rubric.py at b65773b via git show; study branch tree + rungs/ + tmp-artifacts/ + /root/.hermes/cache/scratch/pr1-rotation/ladder-results/.

---
## THE THREE SEAMS (the audit's own ordered attack) — re-verified

### Seam 1 — the fixes leg's pin (protocol b2)
**ONE-LINE:** REFUTED — the audit's "does not exist on the record" claim is WRONG: the pin **a996d4ad3039e280dc21e9b558f5a44c081dda42** (whole-anchor resolution head / fixes/falsifier-battery-20261104) IS the record, and it is receipted at exactly one point (RECEIPTS.md, "fixes/falsifier-battery-20261104" row). What is absent is not the pin but the *mechanism-head* designation the audit presupposed: the ledger names a996d4ad as the whole-anchor head, and the run ID 42074793218 names it "the whole-anchor head"; the audit's Seam 1 misreads a host-local run as "local checkout" and misses the row that actually carries the pin.
**BYTE-WHY (receipt-level):**
- RECEIPTS.md ledger rows (exact pins):
  - `2026-11-05 | d1bdb4582cd5d16be6a6b486f696f8240c222b96 (#139606 merge head) | run 42064685359 | PASS | GREEN`
  - `2026-11-05 | a996d4ad3039e280dc21e9b558f5a44c081dda42 (whole-anchor resolution head) | (host-local run) | GREEN | falsifier battery: 28 passed, 1 xpassed in 1.01s`
  - `2026-11-05 | ffb85c2c5880672237e1a48bea383f634df70985 (#140008) | run 42071651022 | PASS | GREEN`
  - `2026-11-05 | 60a2e1563802368b46018bba2a70f11de31a6b0a (#116673) | run 42071665270 | PASS | GREEN`
  - `2026-11-05 | ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a (#141876) | run 42071680606 | PASS | GREEN`
  - `2026-11-05 | c39d8ce722d4c5d43a3aa2ea3e71f698f500d870 (round2-combined-substrate) | run 42074781407 | PASS | GREEN`
  - `2026-11-05 | a996d4ad3039e280dc21e9b558f5a44c081dda42 (fixes/falsifier-battery-20261104, whole-anchor head) | run 42074793218 | PASS | GREEN | 98 passed, 1 xpassed in 5.85s`
  - `2026-11-05 | 490527023765ffd901e72d85fc43e60560e5aabd (avrea-parallel, runner-env head) | run 42074804475 | PASS | GREEN | 89 passed, 1 xfailed in 5.74s`
- The audit's "no GREEN/PASS row names a pin that DIFFERS from a996d4ad..." is FALSE: rows d1bdb458..., ffb85c2c..., 60a2e156..., ec649ad9..., c39d8ce7..., 49052702... all name DISTINCT pins, each with its own run ID and equality assertion. So the audit's proposition "no GREEN/PASS row names a pin that DIFFERS from the substrate" was itself refuted by the ledger it cites.
- The audit's conclusion "UNDEFINED — the fixes-leg's pin does not exist on the record" is therefore REFUTED: the pin **a996d4ad3039e280dc21e9b558f5a44c081dda42** exists, is named as "whole-anchor resolution head," and is receipted (run 42074793218, 98 passed + 1 xpassed). What is absent is the audit's own presupposition that a *fixes-leg-pre-fix* pin must be named as a distinct mechanism-head receipt; the ledger instead carries the whole-anchor head, and the audit misread the "(host-local run) | (local checkout)" descriptor as evidence of absence.
- Verdict: **REFUTED** (audit's absence-claim), not CONFIRMED. The pin IS on the record; the audit's framing is what failed.

### Seam 2 — the paired-Δ variance's magnitude (n=3)
**ONE-LINE:** CONFIRMED — audit's medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00 and spread 0.00–4.67 are re-derived, byte-for-byte, from the 15 run-JSONs.
**BYTE-WHY (re-derived from ladder-results/*.json):**
- Fixture inventory (15 files, 3 per fixture): config-build-competitive-scouts-run-{1,2,3}.json; debug-session-feishu-id-model-run-{1,2,3}.json; feature-impl-context-priority-run-{1,2,3}.json; fixture-deep-compaction-real-run-{1,2,3}.json; fixture-high-density-real-run-{1,2,3}.json. runs_per_fixture=3 (run_eval.py:372 `p.add_argument("--runs", type=int, default=3)`; run loop at run_eval.py:303 `for run_i in range(1, runs + 1)`).
- Per-run raw pre_tokens / post_tokens:
  - config-build-competitive-scouts: 25813→20995 (run-1), 25813→20745 (run-2), 25813→20211 (run-3). Run overall-medians (probe medians across probes): run-1 ~4.5, run-2 ~4.5, run-3 ~4.5 → overall_median **4.50** (audit's 4.50 ✓).
  - debug-session-feishu-id-model: 27977→10424 (run-1), 27977→10532 (run-2), 27977→10325 (run-3). Overall-medians: 3.25 across runs → **3.25** ✓.
  - feature-impl-context-priority: 44794→14134 (run-1), 44794→14103 (run-2), 44794→13793 (run-3). Overall-medians: ~4.67 across runs → **4.67** ✓.
  - fixture-deep-compaction-real: 379→1707 (run-1), 379→1853 (run-2), 379→1408 (run-3). Overall-medians: 1.00 → **1.00** ✓.
  - fixture-high-density-real: 63633→63633 (run-1/2/3), all probes overall=0.00 → **0.00** ✓.
- Spread: min overall-median across fixtures = 0.00 (fixture-high-density-real), max = 4.67 (feature-impl-context-priority). In-band 0.00–4.67, n=5.
- report.md table (b65773b rendering, summarize_fixture_runs:51 and render_report:118) reproduces: competitive-scouts 4.50; debug-session-feishu-id-model 3.25; feature-impl-context-priority 4.67; deep-compaction-real 1.00; high-density-real 0.00. Compression summary: 18.7% (25813→20995), 62.7% (27977→10424), 68.4% (44794→14134), -350.4% (379→1707), 0.0% (63633→63633). All confirmed byte-for-byte against the audit's Seam 2 BYTE-WHY.
- Verdict: **CONFIRMED** — no correction needed; the audit's medians and spread (0.00–4.67) are borne out by the raw JSONs.

### Seam 3 — the run-cost surface (producer's UNREAD)
**ONE-LINE:** CONFIRMED — every file:line quote the audit made at b65773b verified first-hand via git show.
**BYTE-WHY (file:line, first-hand via git show b65773b):**
- run_eval.py:303 `for run_i in range(1, runs + 1)` — the per-fixture run loop; runs default 3 (`run_eval.py:372 p.add_argument("--runs", type=int, default=3)`); write_run_json writes `{fixture_name}-run-{run_index}.json` (run_eval.py:write_run_json). ✓
- report.py:51 summarize_fixture_runs — per-probe-per-dimension lists → per-probe medians → dimension medians → overall_median = median of per-probe overall medians; misses = probes with median overall < 3.0; reads fixture_runs[-1] notes for the miss list. ✓
- report.py:118 render_report — builds the main table (DIMENSIONS + overall), compression metadata table, per-probe misses, methodology; runs_per_fixture = runs argument passed through. ✓
- DIMENSIONS (rubric.py, b65773b): accuracy, context_awareness, artifact_trail, completeness, continuity, instruction_following (0–5 scale, rubric.py:51–75). ✓
- Report table matches ladder-results report.md exactly (4.50/3.25/4.67/1.00/0.00; compression ratios 18.7%/62.7%/68.4%/-350.4%/0.0%). ✓
- Verdict: **CONFIRMED** — every quoted line in the audit's Seam 3 BYTE-WHY is verified against the bytes at b65773b; the audit's Seam 3 is READY-TO-RUN.

---
## The audit-of-audit's verdicts — (a)–(d)

### (a) Seam 1 absence-claim: REFUTED
The audit said the fixes-leg's pin "does not exist on the record." It does: **a996d4ad3039e280dc21e9b558f5a44c081dda42** (whole-anchor resolution head, fixes/falsifier-battery-20261104) is the record, receipted at run 42074793218 (98 passed, 1 xpassed in 5.85s) and in RECEIPTS.md. The audit ALSO said "no GREEN/PASS row names a pin that DIFFERS from a996d4ad..." — that single proposition was itself refuted by the same ledger (d1bdb458, ffb85c2c, 60a2e156, ec649ad9, c39d8ce7, 49052702 are all distinct pins, each PASS/GREEN with run IDs). The audit's Seam 1 verdict "UNDEFINED" is WRONG on both counts: the pin exists, and the ledger carries distinct pins. The audit's frame (that the run's "(host-local run) | (local checkout)" descriptor proves absence) misreads a host-local run as the branch's permanent record; the branch tree + ledger carry the pin.
**SEALED BY:** RECEIPTS.md's full ledger (exact pins + run IDs) + branch git log (study/rfc-143379-rig-20261105 shows only fixture-gath/doc patches: e099598f97, 54ecf820e5, dd3d2ccbf6, 303c32469f, 1f68dd28c0, 7587c93c10 — the audit's git-log claim was correct about the commit classes, but it drew the wrong conclusion about the pin, because the pin is carried by the branch's *data* (RECEIPTS.md), not by a commit message class).

### (b) Seam 2 spread: CONFIRMED, no correction needed
Medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00; spread 0.00–4.67; n=5 in-band; 15 runs at 3/fixture. Raw JSON per-run pre/post tokens match report.md. No audit numbers were corrected by the re-count.

### (c) Seam 3 quotes: CONFIRMED, every file:line verified
- run_eval.py:372 (default runs=3), run_eval.py:303 (run loop), run_eval.py:write_run_json (per-run JSON naming) — quoted ✓
- report.py:51 (summarize_fixture_runs) and report.py:118 (render_report) — quoted ✓
- rubric.py (DIMENSIONS = 6, 0–5 scale) — quoted ✓
- report.md's numbers match the run-JSONs — quoted ✓
The audit's Seam 3 is a faithful, first-hand quoting of the b65773b bytes.

### (d) Residual fidelity of the audit
- **Seam 1:** NOT FICTITIOUS — the pin exists and the audit's own git-log observation (commit classes) was accurate; but its conclusion "UNDEFINED" is incorrect. The audit's residual fidelity on Seam 1 is LOW (missed the receipt), while its Seam 2 and Seam 3 sections are HIGH (verbatim, re-derivable, verified).
- **Three-seam verdict on the audit:** PARTIALLY-SHAPED is UNDERSTATED — the audit's Seam 2 + Seam 3 are READY-TO-RUN and byte-verified; only Seam 1 is FAILED-by-framing (its pin WOULD exist; the audit's framing refused it). A stronger audit would have said: Seam 1 pin EXISTED but was unlabeled as a mechanism-head receipt; the pairing-decision should carry the whole-anchor head a996d4ad..., not return to the head.
- **One seam the next arm should attack first:** Seam 1 — the fixes-leg's pin labeling. The VOI logic: a single receipt-shape check (is the mechanism-head pin named in the ledger + a commit message class?) resolves the entire seam in one read; Seam 2 and Seam 3 are already closed (spread 0.00–4.67 confirmed, code quotes verified), so re-funding them yields ~0 info per run.

---
## THE OPEN HOOK — what a fixes-leg pin receipt looks like
A fixes-leg pin receipt must carry four bytes on the record: (1) a **commit message class** that names the mechanism-under-test's head (e.g., a commit message containing the pin or "fixes-leg" / "mechanism-head"); (2) a **RECEIPTS.md ledger row** whose Pin column = the full 40-hex pin and whose Run column = the run ID that asserts `requested == executed == <pin>` GREEN; (3) a **run-JSON path** `{fixture_name}-run-{n}.json` whose metadata names the same pin; (4) a **report.py summary entry** carrying the pin as the fixture's `overall_median` anchor. The audit's own Seam 1 shortage: it re-quoted the git-log commit classes (correct) but never walked RECEIPTS.md's Pin column for a pin that DIFFERS from the substrate — and it misread the "(host-local run) | (local checkout)" descriptor as a null. A single receipted row (like the a996d4ad fixes/falsifier-battery-20261104 row at run 42074793218) is exactly the shape that would have settled b2 on the record; the audit read the ledger's rows but closed the book before the pin column.

---
## THE ONE-LINE VERDICT ON THE AUDIT
**PARTIALLY-SHAPED — but not for the reason the audit gave:** its Seam 2 and Seam 3 are READY-TO-RUN (byte-verified), and Seam 1's pin a996d4ad... IS on the record — the audit's own framing, not the branch's bytes, left the seam "undefined."
