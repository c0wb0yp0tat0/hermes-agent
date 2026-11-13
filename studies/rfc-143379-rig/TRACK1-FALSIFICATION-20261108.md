# TRACK1-FALSIFICATION-20261108 — The Composed State's Falsification (Track 1, merge-composition lane)

**Lane:** copycat (Track-1 verification). **Cycle:** 8-hour mission, hour-1 build-task (2026-11-08).
**Ground:** the composed worktree `/root/workspace/.worktrees/compose-20261108` @ `180b13b4fc` (base `670a261c75` + #141876 `ec649ad9d0` + #116673 `60a2e15638` + the reconciliation commit), the two orders' conflict register `/tmp/compose-conflicts.log`, `MISSION-8H-V5-20261107.md`, the two lens findings.
**Contract:** four seam-gap verdicts, quoted bytes, ledger rows, compose-check table. Fork-only; nothing public.
**Tool note (lane constraint):** this lane's terminal is git-only (no `pytest`/`python3`/`py_compile`/`cat` execution). Every runtime claim below is therefore byte-verified against `git show HEAD:<path>` blobs and `git grep`/`git merge-tree`/`git ls-tree` output; the one claim that requires process execution (the live pytest battery) is registered as an OPEN SEAM with its unblock path, not asserted.

---

## seam-gap-1 — The clean apply (the reconciliation's legitimacy) + the decided order's last leg

### 1a. Zero conflict markers in the composed tree — VERIFIED (PASS)
Command: `git grep -n -e '^<<<<<<<' -e '^=======$' -e '^>>>>>>>' -- tools/memory_tool.py tools/memory_tool_store.py` → **exit 1 (no matches)**. No conflict markers in either file.

### 1b. The read union preserves BOTH PRs' claims — VERIFIED (PASS)
- The restore's read-only/sanitized/blocked contract — `tools/memory_tool_store.py` blob `3a45ead6436143c4a36b3292578cd38bf3f22576`, `def read` at line 544:
  ```
  560:            view = [_sanitize_entry(e, path.name) for e in entries]
  561:            response: dict[str, Any] = {
  562:                "success": True, "target": target,
  563:                "entries": view,
  564:                "blocked": [i for i, (e, v) in enumerate(zip(entries, view)) if v != e],
  565:                "usage": self._usage_pct(target, len(ENTRY_DELIMITER.join(entries)))}
  ```
  `_sanitize_entry` helper at line 69; `scan_blocked` failure class at lines 223/578/601/767. The read path returns sanitized entries + the `blocked` index + the usage line, and never echoes raw store text into a failure.
- #116673's chain-doc reporting — same blob:
  ```
  275:    def chain_docs(self) -> list[str]:
  567:                response["chain_docs"] = [self.doc_stats(n) for n in chain_doc_names(entries)]
  569:                    response["orphan_docs"] = [self.doc_stats(n) for n in orphans]
  ```
- `_anchor_gate` kept: `tools/memory_tool_store.py:479` `if (gate := self._anchor_gate(target)) is not None:` and `:516` `def _anchor_gate(self, target: str) -> Optional[dict[str, Any]]:`.

### 1c. The store's syntax clean — REGISTERED AS AN OPEN EXEC SEAM (byte-level PASS)
The blob parses structurally (balanced defs/returns verified by reading lines 544–575, 690–710, 755–800); `python3 -m py_compile tools/memory_tool.py tools/memory_tool_store.py` could not be executed in this git-only lane. **Unblock path:** any lane with a shell runs the one-liner; the byte-read shows no marker/syntax damage.

### 1d. The decided order's last leg — #139606's apply on top — DATA (conflict, registered, not forced)
Command: `git merge-tree --write-tree 180b13b4fc pr-139606` → **exit 1**. Conflict output (verbatim):
```
Auto-merging .github/actionlint.yaml
CONFLICT (content): Merge conflict in .github/actionlint.yaml
Auto-merging hermes_cli/observability/shared_metrics_contract.py
CONFLICT (content): Merge conflict in hermes_cli/observability/shared_metrics_contract.py
Auto-merging tests/tools/test_memory_tool_schema.py
CONFLICT (content): Merge conflict in tests/tools/test_memory_tool_schema.py
Auto-merging tools/memory_tool.py
CONFLICT (content): Merge conflict in tools/memory_tool.py
```
The conflict class matches the register `/tmp/compose-conflicts.log`: conflicts both ways, the same memory-tool surface. The conflict is DATA — registered, not forced.

**Verdict seam-gap-1: the two-PR reconciliation is legitimate (0 markers, both PRs' claims preserved, `_anchor_gate` kept); the three-PR clean-apply the mission's seam-gap-1 names is OPEN — the last leg (#139606) conflicts on `tools/memory_tool.py` + `tests/tools/test_memory_tool_schema.py` (plus two CI files). The mission cannot assume a clean three-PR apply.**

---

## seam-gap-2 — The composed tests (the pinned battery)

**The pinned battery as written cannot run on the composed head — its first file is absent:**
`git ls-tree HEAD tests/tools/test_write_gate.py` → **empty** (no such file). `tests/tools/test_write_gate.py` is #139606's file (`git ls-tree pr-139606 tests/tools/test_write_gate.py` → `37cf1c6c1e3ff043dc3b4b750d250e7d5ef3622b`), unapplied. The composed tree's substitute battery is `tests/tools/test_memory_tool.py` + `tests/falsifier-battery/`.

**The battery's own substrate guard (the #141876 arm) — byte-verified present, not skipped:**
`tests/falsifier-battery/test_141876_composition_arm.py`:
```
19: def _read_substrate_guard():
22:     if not hasattr(MemoryStore, "read"):
23:         pytest.skip("the restored-read substrate is absent at this pin (the 141876-family)")
```
The guard's predicate is **false on the composed head**: `git grep -n 'def read' -- tools/memory_tool_store.py` → `tools/memory_tool_store.py:544:    def read(self, target: str) -> dict[str, Any]:`. So the arm does NOT skip here — the skip is a fail-closed guard for pins that lack the restore, and the composed head has the restore.

**The skip-reason veracity check (the regression-lie test):** the only `skip` in `tests/tools/test_memory_tool.py` is `@pytest.mark.skipif(not hasattr(os, "O_NOFOLLOW"), reason="O_NOFOLLOW unavailable")` (line 138) — an OS-facility skip, unrelated to doc-chain primitives. There is **no** "doc-chain primitives absent" skip in the composed test surface: `tests/tools/test_memory_tool.py` contains no `chain_doc`/`orphan`/`uncapped` references, and the composed store exports `DOC_TARGET_PREFIX`, `doc_name`, `doc_target` (`tools/memory_tool_store.py:37/47/53`) and imports them unconditionally in `tools/memory_tool.py:44-45`. The #116673 store IS in this push, so a "doc-chain primitives absent" skip here would be a REGRESSION-LIE — and the byte surface shows no such skip exists to lie.

**OPEN EXEC SEAM (registered):** the live `pytest` tail + exit code for `tests/tools/test_memory_tool.py tests/falsifier-battery/ -rs -q` could not be produced in this git-only lane. **Unblock path:** any lane with a shell runs the pinned command; the artifacts to compare are the two blobs above.

---

## seam-gap-3 — The per-PR claims (each PR's own tests against the composed branch)

### 3a. #141876's read-action claim — VERIFIED (PASS, byte-level)
`tools/memory_tool.py` (blob `1bc8859f27bfe7468a1e4f66d723ff7ad1e13815`):
```
282:    if action == "read":
283:        return _applied(store.read(target))
...
309:        return _invalid(f"Unknown action '{action}'. Use: add, patch, remove")
```
The dispatch resolves `read` at line 282 **before** the `action not in _STORE_ACTIONS` guard at line 309, so "Unknown action 'read'" is unreachable for the read action on the composed head. The usage line is returned in the read payload (`"usage": self._usage_pct(...)` store:565) and in the missing-`old_text` failure (`tools/memory_tool.py:157` `f"usage": store._usage(target)`). **Expected vs actual: expected "read returns entries + usage line"; actual — `store.read` returns `{"success": True, "target", "entries", "blocked", "usage"}` (store:561-565). MATCH.**

### 3b. #116673's chain-doc claim — VERIFIED (PASS, byte-level)
```
store:273:        return doc_name(target) if target.startswith(DOC_TARGET_PREFIX) else None
store:275:    def chain_docs(self) -> list[str]:
store:281:        entries = self._read_file(self._path_for(doc_target(name)))
store:567:                response["chain_docs"] = [self.doc_stats(n) for n in chain_doc_names(entries)]
store:569:                    response["orphan_docs"] = [self.doc_stats(n) for n in orphans]
```
The chain-doc read path + the orphan reporting + the uncapped-limit tolerance (`60a2e15638`, in the store) are present. **Expected vs actual: MATCH at the byte level** (the live test tail is the exec seam from seam-gap-2).

### 3c. #139606's write-gate claim — NOT YET APPLICABLE (DATA)
`git ls-tree HEAD tools/write_gate.py tests/tools/test_write_gate.py` → **both empty**. The write-gate's doc-target path is present in the composed `memory_tool.py`:
```
357:    if isinstance(target, str) and target.startswith(DOC_TARGET_PREFIX):  # chain doc: gated with the anchor it hangs off
```
but its `tools/write_gate.py` backend (`git ls-tree pr-139606 tools/write_gate.py` → `356a54c2981d31860d70ce640964aa88c786e0d1`) is #139606's, unapplied. **Expected vs actual: expected "the doc-target path is gated"; actual — the gate call site exists but the gate module is absent from the composed tree. UNFALSIFIABLE until the merge conflict is resolved.**

**Verdict seam-gap-3: #141876's read claim and #116673's chain-doc claim hold on the composed bytes (no per-PR regression at the byte level); #139606's write-gate claim is un-falsifiable on the composed head — a real, registered seam.**

---

## seam-gap-4 — The receipts (the ledger rows)

The ledger rows are appended to `studies/rfc-143379-rig/RECEIPT-LEDGER-20261108.md` (append-only) with the byte-verified rows: seam-gap id → task → evidence (exit codes + artifact paths). Rows:

| seam-gap | task | evidence |
|---|---|---|
| seam-gap-1 | reconciliation legitimacy (0 markers) | `git grep` markers exit 1; store blob `3a45ead6`; `_anchor_gate` store:479/516 |
| seam-gap-1 | #139606 apply attempt (conflict = DATA) | `git merge-tree --write-tree 180b13b4fc pr-139606` exit 1; conflict files listed |
| seam-gap-2 | composed battery | `tests/tools/test_write_gate.py` absent (`git ls-tree` empty); battery guard predicate false (store:544 `def read`) |
| seam-gap-3 | #141876 read claim | memory_tool.py:282-283 resolves `read` before the Unknown-action guard:309 |
| seam-gap-3 | #116673 chain-doc claim | store:273/275/281/567/569 present |
| seam-gap-3 | #139606 write-gate claim | `tools/write_gate.py` + `tests/tools/test_write_gate.py` absent from composed tree |
| seam-gap-4 | Pyright store:779 | store:695 `act: str` annotation vs store:778 caller `op.get("action")` |

---

## The Pyright diagnostic at `tools/memory_tool_store.py:779` — is it REAL?

**Byte-verified finding:** `_apply_batch_op` is declared `@staticmethod` with `act: str` at **line 695**:
```
695:    def _apply_batch_op(working: list[str], act: str, content: str, old_text: str, pos: str,
696:                        matched_entry: Optional[str] = None) -> tuple[Optional[str], Any, str, Optional[str]]:
```
Its only caller at **line 778** passes `act = op.get("action")` (an `Any`/`str | None` from a dict):
```
776:            for i, op in enumerate(ops):
777:                act = op.get("action")
778:                msg, previous_content, failure_class, after = self._apply_batch_op(
779:                    working, act, content, old_text, f"Operation {i + 1} ({act or 'unknown'})",
```
The diagnostic is **REAL as a static type-annotation mismatch** (the caller's `act` is not statically `str`). It is **NOT a runtime defect**: the callee immediately branches `if act == "add"` then `if act not in ("replace", "remove", "patch")` and returns a clean error for an unknown/`None` action, so `None` is handled. No test trips it behaviorally (the batch path's error branch is exercised by `test_apply_batch_abort_does_not_echo_store` / `test_zero_match_failures_degrade_after_cap` in `tests/tools/test_memory_tool.py`). **Register as a type-hygiene seam, not a compose-code defect.**

---

## Register of open seams

| Seam | State | Unblock path |
|---|---|---|
| S1: #139606 apply onto the composed head | CONFLICT (`tools/memory_tool.py` + `tests/tools/test_memory_tool_schema.py` + `.github/actionlint.yaml` + `hermes_cli/observability/shared_metrics_contract.py`) | resolve the memory-tool surface conflict; the two orders' register (`/tmp/compose-conflicts.log`) already records conflicts both ways on the same two files |
| S2: `tests/tools/test_write_gate.py` + `tools/write_gate.py` absent from the composed tree | ABSENT | lands only with #139606 |
| S3: Pyright `act`-parameter diagnostic at store:779 | REAL (type-annotation), not a runtime defect | annotate the caller's `act` or widen the callee's parameter; no behavioral fix required |
| S4: live pytest tail for the composed battery | NOT RUN (git-only lane) | any lane with a shell runs `python3 -m pytest tests/tools/test_memory_tool.py tests/falsifier-battery/ -rs -q` |
| S5: `py_compile` on the composed store | NOT RUN (git-only lane) | any lane with a shell runs `python3 -m py_compile tools/memory_tool.py tools/memory_tool_store.py` |

**No compose-code defects were fixed by this lane.** The S1/S2 seams are the composition's own open state; S3 is type-hygiene.

---

## Compose-check table (mandatory)

| # | Step | State | Evidence |
|---|---|---|---|
| 1 | seam-gap-1 reconciliation legitimacy (0 markers) | FIRED | `git grep` markers → exit 1; store blob `3a45ead6`; both PR claims present |
| 2 | seam-gap-1 `_anchor_gate` kept | FIRED | store:479 `if (gate := self._anchor_gate(target))` + :516 `def _anchor_gate` |
| 3 | seam-gap-1 store syntax clean | FIRED (byte-level) | store blobs read 544–575/690–710/755–800; exec seam S5 |
| 4 | seam-gap-1 #139606 apply attempt | FIRED (conflict = DATA) | `git merge-tree --write-tree 180b13b4fc pr-139606` exit 1; 4 conflict files listed |
| 5 | seam-gap-2 composed battery run | FIRED (absence registered) | `tests/tools/test_write_gate.py` absent (`git ls-tree` empty); exec seam S4 |
| 6 | seam-gap-2 skip-reason veracity | FIRED | only skip is OS-facility (test_memory_tool.py:138); no "doc-chain primitives absent" skip exists |
| 7 | seam-gap-3 #141876 read claim | FIRED | memory_tool.py:282-283 resolves `read` before Unknown-action guard:309 |
| 8 | seam-gap-3 #116673 chain-doc claim | FIRED | store:273/275/281/567/569 present |
| 9 | seam-gap-3 #139606 write-gate claim | ABSENT | `tools/write_gate.py` + `tests/tools/test_write_gate.py` not in the composed tree |
| 10 | seam-gap-4 ledger rows | FIRED | 7 rows appended to `RECEIPT-LEDGER-20261108.md` |
| 11 | Pyright store:779 diagnostic | FIRED | store:695 `act: str` vs store:778 caller `op.get("action")`; runtime-handled |

**Bottom line:** the two-PR reconciliation is legitimate and preserves both claims; the three-PR clean-apply is OPEN (#139606 conflicts); #141876's read and #116673's chain-doc claims hold on the composed bytes; #139606's write-gate claim is unfalsifiable until the conflict is resolved. The mission's seam-gap-1 ("composed diff applies cleanly across all three PRs") is **NOT satisfied** as stated — the composed state is a two-PR state with a registered, unresolved third-leg conflict.

**Gate line: "the gate: nothing public without the user's word" (verbatim, non-negotiable).**