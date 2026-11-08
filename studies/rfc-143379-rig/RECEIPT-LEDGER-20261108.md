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

## Open seams (registered, not fixed)

| seam | state | unblock path |
|---|---|---|
| S1 | #139606 apply conflicts on the memory-tool surface | resolve the conflict; register both orders' conflicts (`/tmp/compose-conflicts.log`) |
| S2 | `tests/tools/test_write_gate.py` + `tools/write_gate.py` absent from composed tree | lands only with #139606 |
| S3 | Pyright `act`-parameter diagnostic (store:779) | annotate caller or widen callee; no behavioral fix |
| S4 | live pytest tail not run (git-only lane) | any lane with a shell runs `python3 -m pytest tests/tools/test_memory_tool.py tests/falsifier-battery/ -rs -q` |
| S5 | `py_compile` not run (git-only lane) | any lane with a shell runs `python3 -m py_compile tools/memory_tool.py tools/memory_tool_store.py` |