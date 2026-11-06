# AUDIT-LADDER-RUNGS-20261106 — the rungs 4-5 substance-check (the ladder's gate re-opens)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Subject:** RUNGS-BUILD (`697cd49de7`, "schema-verified at build"). **Register:** receipts, never claims — every line below is a byte-read.

## The byte-checks (2026-11-06 05:2x, read-side)

1. `rungs/fixture-deep-compaction.json` vs `rungs/fixture-high-density.json` vs the eval-suite's `fixtures/config-build-competitive-scouts.json`: the `messages` lists are **byte-identical in all three** (`deep == high == config: True`; 61 messages each).
2. The full-JSON field-diff: the ONLY differing fields are `name` and `description`. No treatment-field (compaction-ratio, density-marker, truncation-delta) exists in the fixtures or the schema; `truncated_to: None` in all three; `source` identical in all three: `~/.hermes/sessions/20260328_160817_77bd258b.jsonl`.
3. The run-side: `run_eval.py`'s CLI exposes `--fixtures / --runs / --label / --judge-{model,provider} / --compressor-{model,provider} / --focus-topic / --compare-to / --verbose` — **no depth/density/ratio knob**; the compressor's prompt-variant is a tree-state, not a per-rung parameter. The stress-cells cannot be applied at the run-arguments.

## The verdict: RUNGS-REOPEN (the substance-check)

The rungs 4-5 as committed carry no cell-delta from rung 1: the same session, the same messages, the same meta — the names "deep-compaction stress" / "high-density stress" are aspirational, not constructed. The build's "schema-verified" was a shape-check only. Consequences, honest:

- The ladder's depth-vs-density separation **cannot** come from these fixtures: a 5-rung battery over them measures one cell five times (the retention-reward scalar's separation would be an artifact of the run-noise, not of the axes).
- The LADDER-PARTIAL's gate was armed at the provider-window alone; the deeper gate is the fixture-substance. The window was probed open (05:15, HTTP 200) — the battery's dispatch is nonetheless **withheld** until the cells exist.
- The RUNGS-BUILD gate re-opens at the substance-check.

## The next-arm (evidence-to-evidence): the REBUILD-ARM

1. The two stress-cells from DISTINCT rig sessions: the deep-compaction cell = a session-dump whose compressor profile is the high-ratio shape (the truncation/compaction-path receipts); the high-density cell = the many-tiny-facts-per-turn stream (the rig's request-dumps; the recurrence-bearing real streams the membership-AoA named — the real-stream cell's weighting-separation question rides the same fixtures).
2. The probe-banks derived from THOSE bytes (the seam-arc's bank-protocol: recall/artifact/decision/continuation, expected-facts present in the fixture's messages).
3. The battery-run: the rungs 1-3 re-measured in the same battery (the comparability-table) + the new stress-cells + the retention-reward scalar — at the substrate-carrying pin (the RECEIPTS-ledger's `a996d4ad`, `fixes/falsifier-battery-20261104`), the record's seat-class.

**Sequencing:** the rebuild lands → the banks land → the battery lands → each rows. The gate holds until the build's substance lands.

## [Artifact]
SHA: this commit. The diff-receipts: see the byte-checks above (the JSONs' hashes on the branch: dc `4ea2a719bc21` / hd `a3ebe2eb2a4d` / rung-1 `97456ccc1cbc` — the message-content all three identical).
