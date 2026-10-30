# KVNLOO654 — THE EXACT 297-CASE BATTERY MANIFEST (2026-10-30)

*NIGHT-654 LEG 2 (P2) deliverable — reconstructed from the local runs, never from prose.*
*Kevin's ask:* "The author's exact 297-case list is still not published, so the runner correctly reports `claimed_297_battery_green=false` and NOT_CERTIFIED." This manifest IS that list: the test-file enumeration, the selection rule, the per-file counts — summing exactly **297** — and the verification by local re-run.

---

## 1. Test-file enumeration (15 files)

All paths relative to the repository root of the round-two combined substrate
(branch `round2-combined-substrate`, commit `995de91d28` = `af16e3ab16` + the 5 develop fixes + the chain-doc closures, on `/root/hermes-agent-pr`; worktree copy `/tmp/kvnloo654-combined`):

| # | File |
|---|------|
| 1 | `tests/tools/test_rfc_homework.py` |
| 2 | `tests/tools/test_kvnloo654_fix01_cache_coherence.py` |
| 3 | `tests/tools/test_kvnloo654_fix02_bounded_pager.py` |
| 4 | `tests/tools/test_kvnloo654_fix03_schema_contract.py` |
| 5 | `tests/tools/test_kvnloo654_fix04_consent_deny.py` |
| 6 | `tests/tools/test_kvnloo654_fix05_fail_closed_gate.py` |
| 7 | `tests/tools/test_write_gate.py` |
| 8 | `tests/tools/test_memory_tool.py` |
| 9 | `tests/tools/test_memory_patch_action.py` |
| 10 | `tests/tools/test_memory_target_contract.py` |
| 11 | `tests/tools/test_write_approval.py` |
| 12 | `tests/tools/test_write_deny.py` |
| 13 | `tests/tools/test_threat_patterns.py` |
| 14 | `tests/tools/test_memory_tool_schema.py` |
| 15 | `tests/tools/test_memory_tool_import_fallback.py` |

## 2. Selection rule

The battery is the **union of the two local runs' regression scopes** on the round-two
fixed substrate (`/root/mtw-dev-t967aac65`, HEAD `af16e3ab16` + 5 fixes):

1. **The round-two full regression (13 files → 274 passed)** — the exact pytest command
   is preserved in the round-two develop session's raw transcript (`state.db`
   message 253017, session `local-a121da3cd2…`): the five fix-probe files
   (34 fail-to-pass items) plus the eight pre-existing memory/write regression files
   (240 pass-to-pass items). Its own accounting: *"Full 274 suite (240 pass-to-pass +
   34 fail-to-pass)" → 274 passed in 11.90s.*
2. **The skips-closure additions (2 files + 1 split → +23)** — the closure ran the full
   `test_rfc_homework.py` (16 items; 14 passed + 2 skipped → 16 passed after the two
   documented skips were closed) and `test_write_gate.py` (6 items), and split
   `test_is_doc_returns_false_when_primitive` into two tests (fix05: 8 → 9 items).
   The closure's completion report (the raw run's own accounting): *"Full regression:
   297 tests pass, 0 failures, 0 skips (16 rfc_homework + 34 fix01-05 + 6 write_gate +
   240 pass-to-pass + 1 schema)"* — where the "34 fix01-05 + 1 schema" groups the
   post-split 35 fix01-05 items (the split's extra test is the "1 schema").

Files 8–15 (the 240) are the pre-existing **memory/write regression suite** — exactly
the files the round-two develop collected and counted raw: `test_memory_tool.py` 64,
`test_memory_patch_action.py` 19, `test_memory_target_contract.py` 64,
`test_write_approval.py` 24, `test_write_deny.py` 10, `test_threat_patterns.py` 57,
`test_memory_tool_schema.py` 1, `test_memory_tool_import_fallback.py` 1
(= 240; the AoA's independent 240/240 regression check, t_aac6a3f6, corroborates).

Selection exclusions, as in the raw runs: no file outside this 15-file set is part of
the battery (the repo's other `tests/tools/` files, labs, and benchmarks are separate
legs of the round-two scope). No `-k` selectors; each file's full collection is in the
battery.

## 3. Per-file case counts — summing exactly 297

| File | Cases |
|------|------:|
| `tests/tools/test_rfc_homework.py` (4 tests, 1 × 12-scenario parametrization) | 16 |
| `tests/tools/test_kvnloo654_fix01_cache_coherence.py` | 5 |
| `tests/tools/test_kvnloo654_fix02_bounded_pager.py` | 7 |
| `tests/tools/test_kvnloo654_fix03_schema_contract.py` | 6 |
| `tests/tools/test_kvnloo654_fix04_consent_deny.py` | 8 |
| `tests/tools/test_kvnloo654_fix05_fail_closed_gate.py` (post-split) | 9 |
| `tests/tools/test_write_gate.py` | 6 |
| `tests/tools/test_memory_tool.py` | 64 |
| `tests/tools/test_memory_patch_action.py` | 19 |
| `tests/tools/test_memory_target_contract.py` | 64 |
| `tests/tools/test_write_approval.py` | 24 |
| `tests/tools/test_write_deny.py` | 10 |
| `tests/tools/test_threat_patterns.py` | 57 |
| `tests/tools/test_memory_tool_schema.py` | 1 |
| `tests/tools/test_memory_tool_import_fallback.py` | 1 |
| **TOTAL** | **297** |

16 + 5 + 7 + 6 + 8 + 9 + 6 + 64 + 19 + 64 + 24 + 10 + 57 + 1 + 1 = **297** ✓

Grouped as the raw run reported it: **16 rfc_homework + 35 fix01-05 (34 + the split's
"1 schema") + 6 write_gate + 240 pass-to-pass = 297**.

## 4. Hash

The manifest is hashed as a published artifact; the hash of the exact published bytes is
carried by the sidecar receipt `KVNLOO654-297-BATTERY-MANIFEST-20261030.sha256`
(sha256 over this file's exact bytes — one line, `filename  hash` form), and the value
is repeated in the landing records. Verification: `sha256sum -c <receipt>`.

## 5. Verification — local re-run

Command (the closure's runner: the substrate venv python, `PYTHONPATH` = the tree):

```
cd /tmp/kvnloo654-combined && PYTHONPATH=/tmp/kvnloo654-combined \
  /usr/local/lib/hermes-agent/venv/bin/python3 -m pytest \
  tests/tools/test_rfc_homework.py tests/tools/test_kvnloo654_fix01_cache_coherence.py \
  tests/tools/test_kvnloo654_fix02_bounded_pager.py tests/tools/test_kvnloo654_fix03_schema_contract.py \
  tests/tools/test_kvnloo654_fix04_consent_deny.py tests/tools/test_kvnloo654_fix05_fail_closed_gate.py \
  tests/tools/test_write_gate.py tests/tools/test_memory_tool.py tests/tools/test_memory_patch_action.py \
  tests/tools/test_memory_target_contract.py tests/tools/test_write_approval.py tests/tools/test_write_deny.py \
  tests/tools/test_threat_patterns.py tests/tools/test_memory_tool_schema.py \
  tests/tools/test_memory_tool_import_fallback.py \
  -q --tb=short -p no:cacheprovider
```

Result (2026-10-30, local re-run, exit code 0):

```
........................................................................ [ 24%]
........................................................................ [ 48%]
........................................................................ [ 72%]
........................................................................ [ 96%]
.........                                                                [100%]
297 passed in 14.90s
```

**297 passed, 0 failed, 0 skipped.** Re-run log sha256:
`b9438c93674e5ea742db4fc1ebd33150b07805968316f5778e6c7e8c698b6590`.
Per-file collected counts on the verified tree equal the manifest counts exactly
(§3), so every row of the manifest is individually exercised by the re-run.
