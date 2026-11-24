# RW-P1 — THE ARM-CONTOUR: the read-straddles-write arm's shape
*(FLAGSHIP-HY · copycat lane · 2026-11-24 · study landing only, PREVIEW — nothing posts)*

*Digest for Pass 2 to compose into the reply. Every mechanism claim below is traced either to kvnloo's row `7143199711` (`KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`, verbatim) or to the pin's bytes at `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` (`git show a9c65dc4:…`, `git log -L 551,566:tools/memory_tool_store.py a9c65dc4`). Where a signature is his 11-23 receipt and not our re-run, it is labelled as such. The WALL CLAUSE is honored: no verdict is asserted without the constructed minimal move that would reproduce it.*

---

## 0. Pin identifiers (cold-runnable anchors)

- Fix pin: `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` — subject `test(memory): pin the read action at the registry handler` (resolved locally via `git rev-parse a9c65dc4`).
- Store source: `git show a9c65dc43db9…:tools/memory_tool_store.py`, `read()` at **`#L551-L566`** (his row: *"The `read()` in question is `memory_tool_store.py#L551-L566`"*). The hunk that produced those lines is commit `41dc81fa2710be52d0877529b8800834132478bb` (from `git log -L 551,566:tools/memory_tool_store.py a9c65dc4 -1`).
- Test source: `git show a9c65dc43db9…:tests/tools/test_memory_chain_docs.py`, test at **`#L198-L244`**.
- Named test: **`test_doc_reader_and_writer_keep_latest_live_state`** (his row naming the file:line; confirmed verbatim in the pin's test file).

---

## 1. The arm's mechanism — his words + the pin's bytes

### 1.1 His words (row 7143199711, verbatim, line cites into `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`)

- L7: *"it's the second shape, **a read straddling a write**. It isn't a double-add."* — the shape is named, and explicitly NOT the writer-writer clobber.
- L7: the test *"doesn't depend on timing"* — the interleaving is forced by an `Event`, not won by a scheduler. This is what makes it pre-registerable.
- L9–L12 (the forced interleaving, verbatim):
  1. *"Seed the chain doc with `initial`."*
  2. *"A reader thread calls `store.read("doc:…")`, takes its disk snapshot, then blocks on an `Event` before returning."*
  3. *"A writer thread runs `store.add("doc:…", "latest")` and commits."*
  4. *"Release the reader, then assert the read returned `["initial"]` while the live list and the tool-level `read` both still say `["initial", "latest"]`."*
- L14: *"With #116673's original `read()`, step 2 loads that stale snapshot back into the live cache when it resumes, which rolls the writer's commit back."* — the fault is a **stale-snapshot reload into the live cache**, i.e. a rollback of a commit that already landed on disk.
- L22–L23: *"Either arm alone is enough. With the lock, the writer waits behind the paused read. Without the cache write, the stale snapshot never reaches the live list."* — the two independent guards.
- L24: *"That's why your sequential two-add stays green with both removed: it never puts a read across a write."* — why the writer-writer probe cannot stand in for this arm.

### 1.2 The pin's bytes — `read()` at `tools/memory_tool_store.py#L551-L566`

Bound from `git log -L 551,566:tools/memory_tool_store.py a9c65dc4 -1` (hunk `@@ -512,9 +551,16 @@`, fix commit `41dc81fa…`). The `-` lines are **#116673's original read**; the `+` lines are the pinned read.

Pinned (`+`) docstring, verbatim: *"Entries of *target* for the model, read-only: no gate, no drift guard, no write. Read under ``_file_lock`` so the file read cannot race a concurrent write. This method does NOT mutate the live store: the returned view is the deduped (first occurrence wins), stripped, threat-scanned parse of the bytes on disk, and the live lists are left as a writer last left them. …"*

Pinned (`+`) body, verbatim:
```
    path = self._path_for(target)
    with self._file_lock(path):                      # <-- the LOCK arm
        raw, read_ok = self._read_raw_checked(path)  # <-- the disk SNAPSHOT (step 2)
        if not read_ok:
            return _read_action_failed_error(path)
        entries = list(dict.fromkeys(self._parse_entries(raw)))
```
No line after `entries = …` writes anything back — *"the live lists are left as a writer last left them"* is the byte fact behind green row 1 and green row 3.

Original (`-`, #116673) body, verbatim:
```
    raw, read_ok = self._read_raw_checked(path)       # NO lock
    if not read_ok:
        return _read_failed_error(path)
    entries = list(dict.fromkeys(self._parse_entries(raw)))
    self._set_entries(target, entries)                # <-- the CACHE-WRITE arm
```
`self._set_entries(target, entries)` is the exact statement his L14 names: it loads the stale `["initial"]` snapshot into the live cache on resume, rolling back the writer's committed `["initial", "latest"]`. **The two arms of the removal table are literally two lines: delete `with self._file_lock(path):` (lock arm) and restore `self._set_entries(target, entries)` (cache-write arm).**

Supporting helper bytes (`git show a9c65dc4:tools/memory_tool_store.py`):
- `_read_file` docstring: *"Entries of a memory file ([] on any error). Read-only callers only; mutation paths use ``_read_raw_checked`` so they can refuse to overwrite an unreadable file."*
- `_read_raw_checked` tail: `return path.read_text(encoding="utf-8-sig"), True`, with the warning that a lossy view handed to write callers is *"a subsequent save [that] persists over the real bytes — the wipe class documented above"*, and `except (OSError, UnicodeDecodeError): return "", False` — the snapshot taken in step 2 and the undecodable-byte guard.
- `_parse_entries`: `return [e for e in (x.strip() for x in raw.split(ENTRY_DELIMITER)) if e]` — how the snapshot becomes entries before any (mis)application.
- `_write_file` docstring: *"Atomic temp-file + rename: readers never see a truncated file. Callers hold ``_file_lock`` (via ``_mutate``): a bare write from an earlier snapshot drops concurrent entries (#119668)."* and body `atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")` — the writer's **commit** in step 3 and the atomic-rename fact used in §4.

### 1.3 The pin's bytes — the test at `tests/tools/test_memory_chain_docs.py#L198-L244`

Bound verbatim from `git show a9c65dc4:tests/tools/test_memory_chain_docs.py`. Docstring: *"A paused read must not roll the live chain doc back after a committed add."* The forced interleaving:

```
captured, release, written = Event(), Event(), Event()
read_raw = store._read_raw_checked
def paused(path):
    snapshot = read_raw(path)
    if current_thread().name == "doc-reader" and path.name == f"{DOC}.md":
        captured.set()
        assert release.wait(8)          # <-- the PAUSE
    return snapshot
monkeypatch.setattr(store, "_read_raw_checked", paused)
def read_doc():  results["read"]  = store.read(f"doc:{DOC}")
def write_doc(): results["write"] = store.add(f"doc:{DOC}", "latest"); written.set()
```

Seeding (`store.add("memory", ANCHOR_REF)`, `store.add(f"doc:{DOC}", "initial")`), then:
```
reader.start()
captured.wait(8); writer.start()
# On the unlocked carrier the writer finishes while the old read is
# paused; with the real reader lock it waits until we release the read.
written.wait(3)
release.set()
```
Final assertions, verbatim: `assert results["read"]["entries"] == ["initial"]` · `assert store._entries_for(f"doc:{DOC}") == ["initial", "latest"]` · `assert _call(store, action="read", target="memory", doc=DOC)["entries"] == ["initial", "latest"]`. These three bind his step 4 (returned snapshot / live list / tool-level read) exactly, and prove the test's determinism (no timing luck).

### 1.4 The mechanism in one line

A reader snapshots the doc from disk (`_read_raw_checked` → `path.read_text`) and blocks inside `_read_raw_checked` before returning; a writer commits `"latest"` under `_file_lock` via `_write_file`/`atomic_write_text`; the resumed **original** `read()` executes `self._set_entries(target, entries)` and writes its stale `["initial"]` back into the live cache — so the tool-level `read` reports the pre-commit state and the commit is rolled back in memory. The pinned `read()` holds the snapshot under `_file_lock` and omits `_set_entries`, so the writer's commit survives.

---

## 2. Difference from FB-2 — named sharply

| | FB-2 (our prior arm) | THIS arm (ARM-CONTOUR) |
|---|---|---|
| Race class | **writer–writer** | **reader–writer** |
| Shape | two `add(doc:…)` calls; add #2's whole-file write clobbers add #1 | one read's disk snapshot straddles one committed write; stale `_set_entries` reload rolls the commit back |
| Fault seam | pre-fix `268bb091:615` `atomic_write_text(doc_path, content)` (WHOLE file) → fix `a9c65dc4:911` `_mutate` → `_write_file` joins with `ENTRY_DELIMITER` | `read()` at `a9c65dc4:551-566`; `self._set_entries` removed, `with self._file_lock(path)` added |
| Decisive change | the fix's append-through-`_mutate` preserves the first writer | lock **and** no-cache-write; either alone suffices |
| Receipt status | **executed by us** (`FB2-EXECUTION-RECEIPTS-20261124.md`): A RED, B GREEN, C GREEN | **his 11-23 receipt at the pin**; not re-run by us (*"I didn't re-run them today"*, row L26) |

- His framing, verbatim (row L28): *"Your double-add shows the lock matters for writer-writer races. This one shows that both arms together cover reader-writer races."*
- Our FB-2 probe (`fb2-race-probe-out.json`) shows both `sequential` and `concurrent-race` GREEN at the fix pin (`FIRST_SURVIVED: true`, `doc_chars: 131`) — the fix holds under writer–writer concurrency; it says nothing about a read straddling that write. Different interleaving, different seam, different arm — **not a substitute**.
- Coverage statement: **FB-2 + ARM-CONTOUR together = the race coverage** (writer–writer and reader–writer). Neither subsumes the other; present them as the two halves of one race story.

---

## 3. Pre-registration skeleton (Pass 2 composes against this)

### 3.1 Procedure — four steps, in our pre-registration form

Adapted from his four-step interleaving (row L9–L12) to the pin's test (§1.3), cold-runnable:

1. **Seed.** Fresh temp store at `a9c65dc4`; `store.add("memory", ANCHOR_REF)` then `store.add("doc:…", "initial")` (his step 1; test seeding).
2. **Park the reader.** Start thread `doc-reader`; it calls `store.read("doc:…")`. Monkeypatch `_read_raw_checked` so, after `snapshot = read_raw(path)`, it sets `captured` and blocks on `release.wait(8)` for `doc-reader` — i.e. pause **after the disk snapshot, before the return** (his step 2; test `paused()`).
3. **Commit the writer.** After `captured.wait(8)`, start `doc-writer` running `store.add("doc:…", "latest")`, which commits via `_mutate`/`_write_file` under `_file_lock`; the test waits `written.wait(3)` (his step 3).
4. **Release + assert.** `release.set()`, join both threads; assert `results["read"]["entries"] == ["initial"]` while `store._entries_for("doc:…") == ["initial", "latest"]` and the tool-level `read(... doc=…)["entries"] == ["initial", "latest"]` (his step 4; test assertions). Failure = live/tool state shows `["initial"]`.

### 3.2 Pins

- **Green pin:** `a9c65dc43db9…`, `read()` as at the pin — `with self._file_lock(path)`, **no** `self._set_entries`.
- **Red variant:** #116673's original `read()` — `self._set_entries(target, entries)` restored AND `with self._file_lock(path):` removed (the "both removed" row).
- The four variants are toggled **on the same pin** by two line-level knobs: presence of `with self._file_lock(path):` and presence of `self._set_entries(target, entries)`; no second commit needed.

### 3.3 Predicted signatures — green / green / green / red

His table (row L16–L21, verbatim) — **his 11-23 receipts at the pin, not our re-run**:

| `read()` variant | Predicted / 11-23 receipt |
|---|---|
| as at `a9c65dc4` (snapshot under `_file_lock`, live lists untouched) | **green**, 17/17 |
| lock removed, still no cache write | **green** |
| cache write restored, under the lock | **green** |
| both removed (= #116673's read) | **red**, 16/1: `['initial'] == ['initial', 'latest']` |

Sequence of signatures: **green / green / green / red.** The test comment in §1.3 is the runtime tell for the lock knob: *"with the real reader lock it waits until we release the read"* vs *"On the unlocked carrier the writer finishes while the old read is paused."*

### 3.4 Named test

`test_doc_reader_and_writer_keep_latest_live_state` — `tests/tools/test_memory_chain_docs.py#L198-L244` @ `a9c65dc4`. Its `Event`-forced interleaving (three `Event`s, `release.wait(8)`) is why the arm *"doesn't depend on timing"* (row L7): deterministic, not a flaky race hunt.

### 3.5 Removal arms — his table, three controls + baseline

| Arm | `with _file_lock` | `self._set_entries` | Expected | Why |
|---|---|---|---|---|
| Baseline (pin's `read()`) | on | off | green 17/17 | snapshot under lock, live lists untouched |
| **lock-only removed** | off | off | green | *"Without the cache write, the stale snapshot never reaches the live list"* (row L22) — no-`_set_entries` alone suffices |
| **no-cache-write-only removed** (`_set_entries` restored) | on | on | green | *"With the lock, the writer waits behind the paused read"* (row L22) — lock alone suffices |
| **both removed** (#116673's read) | off | on | **red** 16/1 | neither guard remains → stale snapshot reloads and rolls back the commit |

Either single guard is sufficient; only the double removal is red. Distinct from FB-2, where the fix's append is the decisive change.

---

## 4. The pause-location question — framed for the head's honest answer

His close (row L30, verbatim): *"Does that match the arm you'd pre-register, or would you rather pause the reader somewhere else, e.g. inside the writer's commit?"*

**Yes — his placement matches the arm we'd pre-register.** Grounds, byte-first:

- His pause sits at the seam that matters: the test-blocked `release.wait(8)` is inside `paused()` **after `snapshot = read_raw(path)` and before `return snapshot`** (§1.3) — i.e. after the disk snapshot, at the exact point where #116673's original `read()` then executes `self._set_entries(target, entries)` (§1.2). That is the reload/rollback fault; the red arm targets it directly.
- Pausing "inside the writer's commit" is a **different bug class** and a weaker arm. The commit is `_write_file` → `atomic_write_text(..., tmp_prefix=".mem_")`, whose pin docstring says *"Atomic temp-file + rename: readers never see a truncated file"* (§1.2 bytes). A reader paused inside that rename cannot observe a torn file; it would test a torn read that atomic rename already prevents, not the stale-cache rollback. Moving the pause there changes the signature away from the #116673 regression the arm is meant to pin.
- Honest caveat the head must carry: this is a **design judgment**, not a measured result. We have not executed this arm (row L26: *"I didn't re-run them today"*). Per the WALL CLAUSE the verdict is held as a **question with a constructed minimal move** (§6), not asserted as ours.

Recommended reply shape: *keep the pause where you put it (after snapshot, before return); it's the minimal faithful seam for the #116673 rollback. An inside-commit pause tests torn reads, which the atomic rename already rules out, so it would dilute rather than sharpen the pre-registration. We'd pre-register your four-step arm as written.*

---

## 5. Convergence line

**FB-2 is the writer–writer half; the ARM-CONTOUR is the reader–writer half; together they are the race coverage.** The pre-registration is runnable cold: named test `test_doc_reader_and_writer_keep_latest_live_state` (`tests/tools/test_memory_chain_docs.py#L198-L244` @ `a9c65dc43db9…`), four-step `Event`-forced procedure, two-line removal knobs (`with self._file_lock(path):` / `self._set_entries(target, entries)`), signatures green/green/green/red. Pass 2 composes: the fix's lock + no-cache-write are each sufficient, only double-removal is red, and the pause stays at the snapshot/return seam. Nothing posted; the hold-back stays sealed under the operator's word.

---

## 6. WALL-CLAUSE minimal move (bindings complete; reproduction is a question, not a verdict)

Both canonical windows are now bound (§1.2 `read()` diff, §1.3 test body) — no phantom claims remain. Constructed minimal reproduction, stated as a QUESTION: apply #116673's original `read()` at `a9c65dc4:551-566` (delete `with self._file_lock(path):`, restore `self._set_entries(target, entries)`), run the 17 tests `test_doc_reader_and_writer_keep_latest_live_state` belongs to; expect 16/1 red with `['initial'] == ['initial', 'latest']`; restore either line and expect green. If the red does not appear, the question for kvnloo is whether his 11-23 receipt pin differs from `a9c65dc43db9…` — not a claim that the arm fails.
