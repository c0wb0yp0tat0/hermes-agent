# TRACK1-139606-COMPOSITION-20261108 — The #139606 Reconciliation (Track 1, last leg)

**Lane:** copycat (Track-1 last leg). **Cycle:** fold's first ticket (2026-11-08).
**Ground:** composed worktree `/root/workspace/.worktrees/compose-20261108` @ `180b13b4fc` (base `670a261c75` + #141876 `ec649ad9d0` + #116673 `60a2e15638` + read-union reconciliation — VERIFIED legitimate by falsification lane: 0 markers, both PRs' claims preserved, `_anchor_gate` kept, no per-PR regression at seam-gap-3); `pr-139606` head `d1bdb4582cd5d16be6a6b486f696f8240c222b96`; `TRACK1-FALSIFICATION-20261108.md` (seam-gap verdicts are the base, not re-litigated); `MISSION-8H-V5-20261107.md` (acceptance verbatim); `RECEIPT-LEDGER-20261108.md` (prior rows).
**Contract:** conflict register + resolution bytes + battery verdict + claim-check + receipt rows + Compose-check table. Fork-only; nothing public.
**Tool note:** this lane's terminal is git-only. Runtime claims (pytest/py_compile) cannot be executed here; they are registered as OPEN SEAMS with unblock paths, never asserted. Byte-evidence via `git ls-tree` / `git merge-tree` / `git diff --stat` / `git grep` / `git show` only.
**Gate line (verbatim, non-negotiable):** "the gate: nothing public without the user's word"

---

## §1 Verdict

**REGISTER, drift-class. NOT a surgical union.** #139606's branch diverges from the composed head by 2,755 files (146,200 insertions / 55,306 deletions); its merge-base `681346296c` is NOT an ancestor of the composed base `670a261c75`, and the composed base is NOT an ancestor of `pr-139606`. The write-gate's own new files (`tools/write_gate.py`, `tests/tools/test_write_gate.py`) do apply as clean additions, and its `tools/memory_tool.py` hunks are in principle union-able with the composed read-union — but a direct `merge pr-139606` onto `180b13b4fc` would drag the full drift width into the tree. The honest leg is a REGISTER with a named rebase-class unblock path (§3). A forced merge over the drift would be a falsification (§2.5 pre-digested fact, re-verified byte-by-byte below).

## §2 Conflict register

**Command:** `git merge-tree --write-tree 180b13b4fc pr-139606` → **exit 1**, tree `3c725b82fa77eefcf2d9a890a59af08580652751`. Verbatim output:

```
Auto-merging .github/actionlint.yaml
CONFLICT (content): Merge conflict in .github/actionlint.yaml
Auto-merging hermes_cli/observability/shared_metrics_contract.py
CONFLICT (content): Merge conflict in hermes_cli/observability/shared_metrics_contract.py
Auto-merging tests/fixtures/prompt_surface/surfaces.json
Auto-merging tests/tools/test_memory_tool_schema.py
CONFLICT (content): Merge conflict in tests/tools/test_memory_tool_schema.py
Auto-merging tools/memory_tool.py
CONFLICT (content): Merge conflict in tools/memory_tool.py
```

4 content conflicts. Per-file stage blobs (merge-tree output):

| file | stage-1 (base) | stage-2 (ours, composed) | stage-3 (theirs, #139606) |
|---|---|---|---|
| `.github/actionlint.yaml` | `f00d40563785a0b731658ad221b2472421898e09` | `71f34454aa9cc55bc8de39b4e761ea3bdd1c69d6` | `3c7445c82832e2c66112314e0a544d4b631ba04f` |
| `hermes_cli/observability/shared_metrics_contract.py` | `3ba33ea41b1e26db15e5d00f357a61485cbd75e3` | `999adb9d0e59d73b83eb35688a953aaa2ec58d4c` | `70462b2a761bb23e33c5e512894c2517beec4a35` |
| `tests/tools/test_memory_tool_schema.py` | `12e395923879e1b0e5bf433bbcedf6c22120718c` | `5d8d823e6deddbb92aaf59b383d7beb6e508ed13` | `c37974e7006c30425faa8c910204a52a34582c54` |
| `tools/memory_tool.py` | `abf8342f0b074ee239b2ea0cff8e260abc01a376` | `1bc8859f27bfe7468a1e4f66d723ff7ad1e13815` | `0f7d0fc87eed9843bc1f9185958dcb9e6c9535fe` |

**The write-gate's own files are NOT in the conflict set** — they are clean additions on the #139606 side, absent from the composed tree:

```
$ git ls-tree HEAD tools/write_gate.py tests/tools/test_write_gate.py   → (empty — absent)
$ git ls-tree pr-139606 tools/write_gate.py tests/tools/test_write_gate.py
  100644 blob 37cf1c6c1e3ff043dc3b4b750d250e7d5ef3622b  tests/tools/test_write_gate.py
  100644 blob 356a54c2981d31860d70ce640964aa88c786e0d1  tools/write_gate.py
```

**Drift quantification (byte-evidence):**

```
$ git diff --stat 180b13b4fc pr-139606 | tail -1
 2755 files changed, 146200 insertions(+), 55306 deletions(-)
$ git merge-base 180b13b4fc pr-139606
 681346296cbf26f3e6a3f2cc81c756f41451cf70
$ git merge-base --is-ancestor 670a261c75 pr-139606   → NOT ancestor
$ git rev-list --count 681346296c..pr-139606           → 2174
$ git diff --stat 681346296c..pr-139606 -- tools/     → 77 files, 4049 insertions(+), 847 deletions(-)
```

Crucially, the drift inside `681346296c..pr-139606` is real work, not only the write-gate: `tools/memory_tool.py` itself is `+175/-36` in that range, and `tools/memory_tool_store.py` shows **zero diff** in that range (`git diff 681346296c..pr-139606 -- tools/memory_tool_store.py` → empty). That is the byte-proof that #139606's branch carries NO store changes of its own — it was built against a store that already had the (pre-#141876) read arm, and its gate code (`_is_doc`, `_store_char_count`, `_store_char_limit`, `_store_entries`, `_disk_entries`) delegates to store doc-aware arms via `getattr` fallbacks.

## §3 Resolution's bytes — UNION judgment, and why the leg is a REGISTER

### 3a. What a union would require (the per-side claims, quoted)

**#139606's claims (the write-gate):** `tools/write_gate.py` (713 lines added in `681346296c..pr-139606`) implements a 7-stage acceptance gate. Quoted from `pr-139606:tools/write_gate.py`:

- Doc-aware delegation (INTEG-1/INTEG-2), fail-closed on a missing doc arm:
  ```
  def _is_doc(store, target: str) -> bool:
      """True when *target* addresses a chain doc (uncapped, doc-resident entries).
      Guarded so a two-way store (one without the doc-chain arm from #116673)
      falls back to ``False`` instead of raising ``AttributeError``. ..."""
      doc = getattr(store, "_doc", None)
      return callable(doc) and doc(target) is not None
  ```
- Per-target scoping via the store's own arms (`_char_count` / `_char_limit` / `_entries_for` / `_doc`), with two-way fallbacks when the doc arm is absent.
- `acceptance_pipeline(store, action, target, content, old_text, operations, caller, entries)` — "Run the 7-stage acceptance gate (stages 1-6 pre-write, stage 7 post-write). Returns `None` to proceed (admit), or a `GateRefusal` (refuse). On admit, exactly ONE Door-B ADMIT line is appended (T1-1). On refusal, exactly one line naming the violating stage."
- `verify_post_write(store, target, action, old_text, content)` — Stage 7 post-write read-back; "goes to the FILE (`_disk_entries`), never the in-memory lists: attesting the cache would pass a lost or concurrently reverted write." Failure class `readback_failed`.
- In `tools/memory_tool.py` (pr-139606): `_apply_write_gate` → `_gate_or_stage` → lazy `from tools.write_gate import acceptance_pipeline`; post-write `from tools.write_gate import verify_post_write` after successful `result.get("success")`. Also schema changes: `"required": ["target"]` (was `["target", "operations"]`), `action`/`content`/`old_text`/`doc`/`new_text` advertised at top level alongside `operations[]`, CHAIN DOCS doc-string mentioning `action='read', doc='<name>'`.

**The composed side's claims (the read-union):** `HEAD:tools/memory_tool_store.py` blob `3a45ead6436143c4a36b3292578cd38bf3f22576` — `def read` at line 544 returning sanitized `entries` + `blocked` index + `usage` (`response["usage"] = self._usage_pct(...)`) + `chain_docs`/`orphan_docs` when `target == "memory"`; `_anchor_gate` at :479/:516; doc arms `_doc` (:271), `_entries_for` (:393), `_char_count` (:414), `_char_limit` (:417, returns `None` for docs = uncapped), `_path_for` (:286, doc-aware). `HEAD:tools/memory_tool.py:282-283` `if action == "read": return _applied(store.read(target))` resolves before the Unknown-action guard at :309.

### 3b. Compatibility analysis (the union IS semantically sound — at file level)

The gate is **designed** to compose with the read-union:

1. **Doc-target path:** The gate's `_is_doc`/`_store_char_count`/`_store_char_limit`/`_store_entries` route through `store._doc` / `store._char_count` / `store._char_limit` / `store._entries_for`. The composed store HAS all four (`_doc` :271, `_entries_for` :393, `_char_count` :414, `_char_limit` :417 returning `None` for docs). So a chain-doc write is charged against the doc (uncapped — the gate skips the cap when `_char_limit` is `None`, INTEG-1) and anchored against the doc's entries (INTEG-2). The composed store's `_path_for` is doc-aware, so `verify_post_write`'s `_disk_entries` (via `store._path_for` + `store._file_lock` + `store._read_raw_checked` + `store._parse_entries`) works against the composed store unmodified.
2. **Anchor-gate:** Quoted from #139606's gate docstring: "Searched against the TARGET's entries (`_entries_for(target)`), not the anchor's. Advisory only: the store's locked match inside `_mutate` stays the commit authority." Stage 6 stale-entry refusal is advisory (`anchor_drift` receipt, fail-closed on drift); the composed store's `_anchor_gate` (:479/:516) and `_mutate` locked match remain the commit authority. No contradiction — the gate defers to the anchor-gate, it does not replace it. (No occurrence of `_anchor_gate` inside `write_gate.py` — only `anchor_drift` receipts and INTEG-2 doc-comments; the tension is registered, not forced: the gate's advisory matcher and the store's locked matcher are two different matchers, and the gate's own docstring concedes the store's wins.)
3. **The read path:** #139606's `memory_tool.py` keeps `if action == "read":-return _applied(store.read(target))` (pr-139606:329-330) — identical to the composed side (:282-283). The gate never intercepts reads (`_apply_write_gate` is only called on mutating paths: batch at :340, single-op at :359). The restore's read-only sanitized contract and the chain-doc reads are untouched by the gate.
4. **Fail-open precedent:** The gate is imported lazily ("if the import fails the caller proceeds (fail-open / degrade to the pre-gate behaviour)"). Even a partial composition degrades to pre-gate behaviour rather than raising.

### 3c. Why this is nevertheless a REGISTER, not a merge

The file-level union is sound, but the **branch-level merge is drift-class**: `merge pr-139606` onto `180b13b4fc` would attempt to reconcile 2,755 files / 2174 commits of upstream drift (web, skills, mcp, process_registry, …) — most of which auto-merge but whose semantic effect on `tools/memory_tool.py`'s schema/handler, `tests/tools/test_memory_tool_schema.py`, `.github/actionlint.yaml`, and `hermes_cli/observability/shared_metrics_contract.py` cannot be byte-adjudicated by a git-only lane without executing the battery. The 4 conflicts are exactly in the memory-tool surface where semantic judgment matters (schema shape, gate refusal classes, observability contract). Forcing them here would be a falsification (a hunk resolved without both sides' claims verified at runtime).

**Exactly ONE real semantic tension is registered** (not forced): `tests/tools/test_memory_tool_schema.py` — #139606 changes the expected schema properties from `{"target", "operations"}` to `{"action", "target", "content", "old_text", "doc", "new_text", "operations"}` and asserts `"new_text" in json.dumps(params)`, and changes two behavioural assertions: the over-budget add now expects `failure_class == "over_budget"` (the gate's refusal) instead of `current_entries`, and a duplicate add now expects `success is False` (was `True`). These are **#139606's own test rewrites** (quoted in the diff `681346296c..pr-139606 -- tests/tools/test_memory_tool_schema.py`), i.e. the gate intentionally changes those behaviours — the register records the change; it does not adjudicate whether the composed battery's older assertions should be updated or the gate's behaviours are regressions. That adjudication requires running the battery (§4 OPEN SEAM).

### 3d. The named unblock path (rebase-class)

1. Rebase (not merge) `pr-139606`'s write-gate commits onto the composed head `180b13b4fc` (or onto current main once the composed state lands). The write-gate's own commits are: `tools/write_gate.py` (+713), `tests/tools/test_write_gate.py` (+899, new file), `tools/memory_tool.py` gate hooks (`_apply_write_gate`, `_gate_or_stage` lazy import, `verify_post_write` call, schema shape), `tests/tools/test_memory_tool_schema.py` expectation rewrites. Everything else in `681346296c..pr-139606` is upstream drift to be dropped by the rebase.
2. At the rebase, the 4 conflicts resolve by UNION: `tools/memory_tool.py` keeps BOTH the composed read-union (`if action == "read": return _applied(store.read(target))` before the Unknown-action guard) AND the gate hooks; the schema takes #139606's shape (`"required": ["target"]`, top-level `action`/`content`/`old_text`/`doc`/`new_text` + `operations[]`) because the gate's CHAIN DOCS doc-string and `doc=` handler param depend on it; `tests/tools/test_memory_tool_schema.py` takes the #139606 expectations (the 3 quoted assertion rewrites) since they encode the gate's intended refusals.
3. Run the pinned battery (§4) on the rebased tree; only then falsify the FULL three-PR composition.

## §4 Battery verdict

**NOT RUN — OPEN SEAM (git-only lane).** `python3 -m pytest tests/tools/test_write_gate.py tests/tools/test_memory_tool.py -rs -q` and `python3 -m py_compile` cannot be executed in this lane (terminal is git-only). No traceback is quoted because no process was executed; an unquoted verdict is not a verdict, so no verdict is asserted. **Unblock path:** any lane with a shell runs, on the rebased tree (§3d):

```
python3 -m pytest tests/tools/test_write_gate.py tests/tools/test_memory_tool.py -rs -q
python3 -m pytest tests/falsifier-battery/ -rs -q   # if present
python3 -m py_compile tools/write_gate.py tools/memory_tool.py tools/memory_tool_store.py
```

**Battery presence (byte-verified):** `tests/tools/test_write_gate.py` exists ONLY on the `pr-139606` side (blob `37cf1c6c1e3ff043dc3b4b750d250e7d5ef3622b`); it is absent from the composed tree (`git ls-tree HEAD` → empty). So the pinned battery's first target file cannot even be collected on the composed tree today — further byte-proof the leg is pre-composition, not post-composition. The test file's own capability probe is quoted (falsifiability note): `_DOC_CHAIN_PRESENT = getattr(_memory_tool_mod, "DOC_TARGET_PREFIX", None) is not None` with the comment "the MODULE, never the entry-point function of the same name — getattr on the function is None forever, which made the old skipif unfalsifiable (the doc arms never ran)." On the composed tree the module-level `DOC_TARGET_PREFIX` IS present (`HEAD:tools/memory_tool_store.py:37`, re-exported by the memory tool module surface), so the doc variants would not be skip-dead there.

**Skip-reason veracity (regression-lie check):** The "141876-family absent" skip must NOT appear in this tree — the restore IS in the composed tree. Byte-check: `tests/tools/test_memory_tool.py`'s only skip is `@pytest.mark.skipif(not hasattr(os, "O_NOFOLLOW"), reason="O_NOFOLLOW unavailable")` (line 138, per falsification lane); the composed store exports `DOC_TARGET_PREFIX`/`doc_name`/`doc_target` (store:37/42/55). No dead skip found in the composed tree. The `tests/tools/test_write_gate.py` doc-chain skip (`_DOC_CHAIN_PRESENT`) is a *capability probe*, verifiably falsifiable, and would evaluate `True` (not skip) on the composed tree — checked against the store bytes above.

## §5 Per-PR claim-check on the COMPLETE composition

The complete composition does not exist as a tree (REGISTER, §3c), so the claim-check is byte-level — expected (PR's own claim) vs actual (composed tree bytes), each quoted:

| PR | claim | expected | actual on composed head | verdict |
|---|---|---|---|---|
| #139606 | 7-stage write-gate refusals (char-cap 85%, provenance, procedure-shape, grammar/threat, stale-entry, post-write read-back) | `tools/write_gate.py` + `tests/tools/test_write_gate.py` present with `acceptance_pipeline`/`verify_post_write` | Both absent (`git ls-tree HEAD` → empty); blobs exist only on `pr-139606` (`356a54c…`, `37cf1c6…`) | UNFALSIFIABLE on this tree — by design of the REGISTER |
| #139606 | doc-target path (chain-doc writes uncapped, anchored against the doc) | gate's `_is_doc`/`_store_char_count`/`_store_char_limit`/`_store_entries` delegate to `store._doc`/`_char_count`/`_char_limit`/`_entries_for` | Composed store HAS all four arms (`_doc` :271, `_entries_for` :393, `_char_count` :414, `_char_limit` :417 = `None` for docs); gate's `getattr` guards would bind | COMPATIBLE (byte-level) |
| #139606 | anchor-gate cohabitation | gate advisory-only vs store locked match | Gate docstring: "the store's locked match inside `_mutate` stays the commit authority"; composed `_anchor_gate` at :479/:516 | COMPATIBLE, tension registered (§3c) |
| #141876 | read-action returns entries + usage line | `memory_tool.py` `if action == "read": return _applied(store.read(target))` before Unknown-action guard; store `def read` returns `entries` + `blocked` + `usage` | `HEAD:tools/memory_tool.py:282-283` (read before guard :309); `HEAD:tools/memory_tool_store.py:544` `def read`, :560-565 `view`/`entries`/`blocked`/`usage` | VERIFIED PRESENT (falsification lane's verdict, not re-litigated) |
| #116673 | chain-doc reads | `chain_docs`/`orphan_docs` reporting in `read`; `doc_name`/`doc_target`/`DOC_TARGET_PREFIX` primitives | store:37 `DOC_TARGET_PREFIX`, :42 `doc_name`, :55 `doc_target`, :275 `def chain_docs`, :567 `response["chain_docs"]`, :569 `response["orphan_docs"]` | VERIFIED PRESENT (falsification lane's verdict) |

## §6 Receipt rows appended (to `studies/rfc-143379-rig/RECEIPT-LEDGER-20261108.md`)

| seam-gap | task | evidence |
|---|---|---|
| seam-gap-1 | #139606 merge attempt onto the composed head (conflict = DATA, drift-class) | `git merge-tree --write-tree 180b13b4fc pr-139606` → exit 1, tree `3c725b82…`; CONFLICT in `tools/memory_tool.py`, `tests/tools/test_memory_tool_schema.py`, `.github/actionlint.yaml`, `hermes_cli/observability/shared_metrics_contract.py` |
| seam-gap-1 | drift quantification (REGISTER, not union) | `git diff --stat 180b13b4fc pr-139606` → 2755 files, 146200+/55306−; merge-base `681346296c` not an ancestor of `670a261c75` nor vice versa; 2174 commits in `681346296c..pr-139606` |
| seam-gap-2 | pinned-battery presence | `git ls-tree HEAD tools/write_gate.py tests/tools/test_write_gate.py` → empty (absent); `pr-139606` blobs `356a54c…` / `37cf1c6…` |
| seam-gap-2 | battery execution | OPEN SEAM (git-only lane) — unblock: shell lane runs `python3 -m pytest tests/tools/test_write_gate.py tests/tools/test_memory_tool.py -rs -q` on the rebased tree (§3d) |
| seam-gap-2 | skip-reason veracity | composed tree: no "141876-family absent" skip; `test_write_gate.py` probe `_DOC_CHAIN_PRESENT` is falsifiable and evaluates True on the composed store (store:37) |
| seam-gap-3 | #139606 doc-target / anchor-gate compatibility | gate delegates via `getattr(store, "_doc"/"_char_count"/"_char_limit"/"_entries_for")`; composed store has all four (store:271/393/414/417); gate advisory-only, `_mutate` locked match stays commit authority |
| seam-gap-3 | #139606 tension registered | `test_memory_tool_schema.py` 3 assertion rewrites (schema shape, `over_budget` failure_class, duplicate-add `success is False`) — gate's intended behaviour changes, adjudication deferred to the battery |
| seam-gap-4 | unblock path named | rebase-class: re-cut the write-gate commits (`tools/write_gate.py` +713, `tests/tools/test_write_gate.py` +899, `tools/memory_tool.py` hooks + schema, `test_memory_tool_schema.py` rewrites) onto `180b13b4fc`, drop the 2,724-file drift, union-resolve the 4 conflicts, run the battery |

## §7 Compose-check table (eight steps — the stack-order clause)

| step | fired / absent | evidence |
|---|---|---|
| 1. composed diff applies cleanly (seam-gap-1) | ABSENT (registered DATA) | `git merge-tree --write-tree 180b13b4fc pr-139606` → exit 1; 4 content conflicts (quoted §2); drift 2,755 files / 2174 commits (§2) |
| 2. composed state's tests pass (seam-gap-2) | ABSENT (OPEN SEAM) | git-only lane: no pytest executed; `tests/tools/test_write_gate.py` absent from composed tree (battery uncollectable pre-composition) — unblock in §4 |
| 3. each PR's claim falsified / no regression (seam-gap-3) | PARTIAL (byte-level) | #141876 read + #116673 chain-docs VERIFIED PRESENT (falsification lane, not re-litigated); #139606 doc-target/anchor-gate COMPATIBLE at byte level, runtime falsification deferred (§5) |
| 4. receipts evidence the composition (seam-gap-4) | FIRED (this lane) | §6 rows; ledger append is part of this landing; rows need-id → task → evidence, byte-verified |
| 5. merge-composition centre (8H mission aim) | FIRED | this artifact is the merge-composition falsification of the three-PR state, with the fold-point register (§3d) |
| 6. fork-only, nothing public | FIRED | artifact + ledger land on `study/rfc-143379-rig-20261105` only; no thread posts; gate line quoted verbatim at top |
| 7. byte-verify habit (disk verification before receipt) | FIRED | every claim above is backed by a quoted `git ls-tree` / `git merge-tree` / `git diff` / `git show` output; runtime claims registered as OPEN SEAMS, never asserted |
| 8. landing-gate (tracked + REMOTE == commit) | FIRED | this file is tracked on the study branch and pushed; `git push origin study/rfc-143379-rig-20261105` after commit (pull --rebase on rejection) |

## §8 Open seams (carried forward, not fixed)

| seam | state | unblock path |
|---|---|---|
| T1-S1 | #139606 apply is drift-class (4 conflicts + 2,755-file drift) | rebase-class unblock (§3d): re-cut the write-gate commits onto `180b13b4fc`, union-resolve, run the battery |
| T1-S2 | pinned battery not executed (git-only lane) | shell lane: `python3 -m pytest tests/tools/test_write_gate.py tests/tools/test_memory_tool.py -rs -q` on the rebased tree |
| T1-S3 | `test_memory_tool_schema.py` 3 assertion rewrites unadjudicated (gate behaviour change vs regression) | battery run (§4) on the rebased tree decides |
| T1-S4 | `py_compile` not run (git-only lane) | shell lane: `python3 -m py_compile tools/write_gate.py tools/memory_tool.py tools/memory_tool_store.py` |
