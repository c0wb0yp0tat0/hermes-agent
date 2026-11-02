# CLOSECODE-RERUN-20261101 — three closures' code landing (in-scratch)

Mission: LEG-CLOSE-CODE RE-RUN. Land the three closure patches against the published head, run per-patch test receipts + combined state. In-scratch only; no pushes; nothing public. Landing on the published head's branch remains the user's word.

## 0. Published head verification

- Commit: `b84150e9be88911280f981467de9628fcfb0f60f`
- Subject: "publish the exact 297-case battery manifest + sha256 sidecar (verified: 15 files, per-file counts sum to 297 via pytest --collect-only at head 995de91d)"
- Source: fork branch `round2-combined-substrate` (c0wb0yp0tat0/hermes-agent), fetched via origin; `git cat-file -t` = commit.
- Clean checkout: `/root/.hermes/cache/scratch/closecode-rerun` (git worktree, detached HEAD, clean before patching).

## 1. Patch application (all three together)

Candidate patches: `/root/.hermes/cache/scratch/pilot-kit-20261029/night1030/followup/patches/`

| Patch | File(s) | sha256 |
|---|---|---|
| patch-a-consent-deny | tools/memory_tool.py | 0ca36ab585ef86a5842b30c9f8114ee49463a77b334144cec9b3948dd5dd5f02 |
| patch-b-orphan-doc-names | tools/memory_tool_store.py | 4357630f128207d7f8b22a1eacd74da8cb508074124bd3a5145fbe1cf1aefd64 |
| patch-c-exclude-newer | pyproject.toml, tests/test_packaging_metadata.py, uv.lock | 80e90e0b27fd63ae45ef5da608805e52c21e1b85c3f572fd8934bed0bbf3c166 |

Application: `git apply` all three in one invocation → clean. Changed 5 files, 72 insertions, 9 deletions. Post-patch tree: `9872d6ba2e6e3a165b01f4c2fbc7f554b1d6d956`.

## 2. Per-patch test receipts

### Patch A — semantic consent-deny (fix04 suite)
- Test file: `tests/tools/test_kvnloo654_fix04_consent_deny.py`
- Result: **8/8 pass** (TestFix4ConsentDeny).
- Scenarios: 8 single-op + 4 batch = 12 consent scenarios; all deny (reject) with marker absent on disk; mixed batches let clean ops proceed while marker ops are dropped.
- Controls: `test_consent_marker_is_detectable`, `test_op_consent_denied_detects_batch_members` hold.
- Deny-before-disk and deny-before-gate-stage verified (file never created; disk untouched).
- Renamed-identifier recognition: `_contains_consent_deny` matches structural marker shape + declaration metadata (`source_no_save`, `source_instruction`); `_op_consent_denied` keys on content/new_text plus metadata.

### Patch B — orphan_doc_names() + read entries
- Test file: `tests/tools/test_rfc_homework.py`
- Result: **16/16 pass** (5 test functions, parametrized to 16).
- Orphan probe: `MemoryStore.orphan_doc_names()` collects docs whose on-disk file exists but whose `@doc:` anchor is absent from MEMORY.md — verified returns `['orphan-note']` for a planted orphan; anchored docs excluded.
- Read response carries `entries` list on single-page reads (verified: `entries` key present, list type, populated) — `test_read_dispatch_contract` asserts `"Synthetic read anchor" in result["entries"]`.

### Patch C — absolute exclude-newer pin
- Test file: `tests/test_packaging_metadata.py`
- Result: **5/5 pass**.
- `uv lock --check`: exit 0, 327 packages resolved.
- `exclude-newer` now absolute timestamp `2026-10-09T00:00:00Z` in both pyproject.toml and uv.lock; `exclude-newer-span` removed from lock options.

## 3. Combined state

- All three patches co-applied on `b84150e9be` (detached HEAD worktree).
- Combined test run: `tests/tools/test_kvnloo654_fix04_consent_deny.py` + `tests/tools/test_rfc_homework.py` + `tests/test_packaging_metadata.py` → **29/29 pass** (8 + 16 + 5), 0 failures.
- `uv lock --check` exit 0, 327 packages.

## 4. Honest boundary

This run lands evidence in-scratch only. The code's landing on the published head's branch remains the user's word — no pushes, no public surfaces, no branch updates performed. The deliverable is this receipt document; the worktree holds the patched tree for the user's review/approval before any publish.

## Receipts summary

- Combined verdict: ALL GREEN — 29/29 tests pass; uv lock --check exit 0 (327 packages); 3 patches apply cleanly together.
- Patch A: 8/8 pass + 12 scenarios deny (staged false) + controls hold.
- Patch B: 16/16 pass + orphan collects with entries.
- Patch C: 5/5 pass + uv lock --check exit 0 (327 packages).
