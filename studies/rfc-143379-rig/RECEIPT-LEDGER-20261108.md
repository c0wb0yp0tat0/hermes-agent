# RECEIPT LEDGER — 2026-11-08 (Track 1, the merge-composition falsification)

Append-only rows: need-id -> task -> evidence (exit codes + artifact paths).
Lane: copycat. Tool constraint: git-only terminal (no pytest/py_compile execution); runtime claims byte-verified against `git show`/`git grep`/`git merge-tree`/`git ls-tree`.

| seam-gap | task | evidence |
|---|---|---|
| seam-gap-1 | reconciliation legitimacy (0 conflict markers) | `git grep -n -e '^<<<<<<<' -e '^=======$' -e '^>>>>>>>' -- tools/memory_tool.py tools/memory_tool_store.py` → exit 1 (no matches); store blob `3a45ead6436143c4a36b3292578cd38bf3f22576`; `_anchor_gate` at store:479/516; chain_docs/orphan_docs at store:275/567/569 |
| seam-gap-1 | #139606 apply onto the composed head (conflict = DATA) | `git merge-tree --write-tree 180b13b4fc pr-139606` → exit 1; CONFLICT in `tools/memory_tool.py`, `tests/tools/test_memory_tool_schema.py`, `.github/actionlint.yaml`, `hermes_cli/observability/shared_metrics_contract.py` |
| seam-gap-2 | composed battery presence | `git ls-tree HEAD tests/tools/test_write_gate.py` → empty (absent); `git ls-tree pr-139606 tests/tools/test_write_gate.py` → `37cf1c6c1e3ff043dc3b4b750d250e7d5ef3622b` (unapplied) |
| seam-gap-2 | skip-reason veracity (regression-lie check) | `tests/tools/test_memory_tool.py` only skip = `@pytest.mark.skipif(not hasattr(os, "O_NOFOLLOW"), reason="O_NOFOLLOW unavailable")` (line 138); no "doc-chain primitives absent" skip; composed store exports `DOC_TARGET_PREFIX`/`doc_name`/`doc_target` (store:37/47/53) |
| seam-gap-3 | #141876 read-action claim | `tools/memory_tool.py:282-283` `if action == "read": return _applied(store.read(target))` resolves before the Unknown-action guard at :309; store:544 `def read`; usage line at store:565 |
| seam-gap-3 | #116673 chain-doc claim | store:273 `doc_name(target) if target.startswith(DOC_TARGET_PREFIX)`; :275 `def chain_docs`; :281 `_read_file(self._path_for(doc_target(name)))`; :567 `response["chain_docs"]`; :569 `response["orphan_docs"]` |
| seam-gap-3 | #139606 write-gate claim (unfalsifiable) | `git ls-tree HEAD tools/write_gate.py tests/tools/test_write_gate.py` → both empty; `git ls-tree pr-139606 tools/write_gate.py` → `356a54c2981d31860d70ce640964aa88c786e0d1` |
| seam-gap-4 | Pyright diagnostic at store:779 | store:695 `def _apply_batch_op(working: list[str], act: str, ...)` vs store:777-778 caller `act = op.get("action")` → `self._apply_batch_op(working, act, ...)`; REAL as type-annotation mismatch, runtime-handled |
| seam-gap-1 | #139606 merge attempt onto the composed head (conflict = DATA, drift-class) | `git merge-tree --write-tree 180b13b4fc pr-139606` → exit 1, tree `3c725b82…`; CONFLICT in `tools/memory_tool.py`, `tests/tools/test_memory_tool_schema.py`, `.github/actionlint.yaml`, `hermes_cli/observability/shared_metrics_contract.py`; full register in `TRACK1-139606-COMPOSITION-20261108.md` §2 |
| seam-gap-1 | drift quantification (REGISTER, not union) | `git diff --stat 180b13b4fc pr-139606` → 2755 files, 146200+/55306−; merge-base `681346296c` not an ancestor of `670a261c75` nor vice versa; 2174 commits in `681346296c..pr-139606`; `tools/memory_tool_store.py` zero-diff in that range |
| seam-gap-2 | pinned-battery presence | `git ls-tree HEAD tools/write_gate.py tests/tools/test_write_gate.py` → empty (absent); `pr-139606` blobs `356a54c…` / `37cf1c6…` (unapplied) |
| seam-gap-2 | battery execution | OPEN SEAM (git-only lane) — unblock: shell lane runs `python3 -m pytest tests/tools/test_write_gate.py tests/tools/test_memory_tool.py -rs -q` on the rebased tree (see TRACK1-139606 §4) |
| seam-gap-2 | skip-reason veracity (139606 leg) | no "141876-family absent" skip in the composed tree; `test_write_gate.py` probe `_DOC_CHAIN_PRESENT` is falsifiable and evaluates True on the composed store (store:37) |
| seam-gap-3 | #139606 doc-target / anchor-gate compatibility | gate delegates via `getattr(store, "_doc"/"_char_count"/"_char_limit"/"_entries_for")`; composed store has all four (store:271/393/414/417); gate advisory-only, `_mutate` locked match stays commit authority |
| seam-gap-3 | #139606 tension registered | `test_memory_tool_schema.py` 3 assertion rewrites (schema shape, `over_budget` failure_class, duplicate-add `success is False`) — gate's intended behaviour changes, adjudication deferred to the battery |
| seam-gap-4 | unblock path named | rebase-class: re-cut the write-gate commits (`tools/write_gate.py` +713, `tests/tools/test_write_gate.py` +899, `tools/memory_tool.py` hooks + schema, `test_memory_tool_schema.py` rewrites) onto `180b13b4fc`, drop the 2,724-file drift, union-resolve the 4 conflicts, run the battery (TRACK1-139606 §3d) |

## Open seams (registered, not fixed)

| seam | state | unblock path |
|---|---|---|
| S1 | #139606 apply is drift-class (4 conflicts + 2,755-file drift) | rebase-class unblock (TRACK1-139606 §3d): re-cut the write-gate commits onto `180b13b4fc`, union-resolve, run the battery |
| S2 | `tests/tools/test_write_gate.py` + `tools/write_gate.py` absent from composed tree | lands only with the rebase of #139606 |
| S3 | Pyright `act`-parameter diagnostic (store:779) | annotate caller or widen callee; no behavioral fix |
| S4 | live pytest tail not run (git-only lane) | any lane with a shell runs `python3 -m pytest tests/tools/test_memory_tool.py tests/falsifier-battery/ -rs -q` |
| S5 | `py_compile` not run (git-only lane) | any lane with a shell runs `python3 -m py_compile tools/memory_tool.py tools/memory_tool_store.py` |
| T1-S3 | `test_memory_tool_schema.py` 3 assertion rewrites unadjudicated (gate behaviour change vs regression) | battery run on the rebased tree decides |
