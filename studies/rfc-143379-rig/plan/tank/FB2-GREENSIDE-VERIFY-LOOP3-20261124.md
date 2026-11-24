# FB-2 GREENSIDE VERIFICATION — LOOP 3 (2026-11-24)

Pin base: `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` (GREEN side)
Pre-fix pin (RED side, flagship's ground): not read. Rejected by the flip-flop.

## 1. THE VERDICT

**CONFIRMED.** The fix tree at its own bytes makes Section 3's GREEN signature
(append-only add + delimiter join, first entry never dropped) and arm C's removal
control (single-add file holds exactly one entry) the only behaviors the seam
permits. The `add` closure appends to `entries` and never rewrites the previous
content store; `_write_file` joins with `ENTRY_DELIMITER` at line :911
(`atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")`),
so a second add preserves the first entry's bytes; a single add leaves exactly one
entry.

## 2. THE SEAM QUOTES (from `a9c65dc4`, `tools/memory_tool_store.py`)

### 2.1 The `_add` closure — `add`, lines :583–614 (verbatim)

```
    def _add(entries, limit):
        if content in entries:
            return self._success_response(target, "Entry already exists (no duplicate added).")
        if limit is not None and len(ENTRY_DELIMITER.join(entries + [content])) > limit:
            return self._add_overflow(target, content, limit)
        return entries + [content], "Entry added."
```

Append-only: the new entry is `entries + [content]`; NO whole-file content write
occurs in the closure. Drift guard skipped (`skip_drift=True`), but the mutation
`_mutate` still atomically rewrites the file from the joined entry list.

### 2.2 The join — `_write_file`, lines :904–911 (verbatim)

```
    @staticmethod
    def _write_file(path: Path, entries: list[str]):
        """Atomic temp-file + rename: readers never see a truncated file. Callers
        hold ``_file_lock`` (via ``_mutate``): a bare write from an earlier snapshot
        drops concurrent entries (#119668)."""
        try:
            atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")
        except OSError as e:
            raise RuntimeError(f"Failed to write memory file {path}: {e}")
```

`ENTRY_DELIMITER.join(entries)` at the :911 position. A second add rebuilds the
file from `entries + [content]`; the delimiter inserts exactly one separator
between the first and second entry, so FIRST's bytes are byte-preservingly
re-emitted.

## 3. THE RECEIPT RE-DERIVATION (cross-walked against the seam)

Probe receipt at the fix pin: `studies/rfc-143379-rig/plan/tank/fb2-probe-out.json`
(arm B executed against `a9c65dc4`; arm C executed against the same pin).

### 3.1 Arm B — `A-fix-two-add` (two adds, fix pin)

Expected GREEN signature per spec §3: first entry survives the second add.

- FIRST body = 64 bytes (the probe's `doc_head` is exactly the FIRST marker body,
  `FIRST marker note: the fleet's two-add probe, byte unique al…`).
- Second add appends `SECOND` (66 bytes): the join emits
  `FIRST + ENTRY_DELIMITER + SECOND` = 64 + 3 + 64 = **131 bytes** ✅ (both bodies are 64 ASCII bytes; the delimiter is the 3-byte `\n§\n` — corrected by the loop-3 neutral audit, whose byte-check showed the FIRST/SECOND name-length swap cancels the alpha./beta. suffix swap).
- `FIRST_SURVIVED_SECOND_ADD=True`: `_add` always does `entries + [content]` — the
  closure never drops, slices, or rewrites an existing entry; `_write_file` is the
  single emission point, and it re-emits the whole joined list. First byte-preserves
  its 64 bytes; the measured `doc_bytes` 131 = 64 + 3 + 64 is exactly what append +
  delimiter join yields. ✅

### 3.2 Arm C — `C-fix-single-add` (single add, fix pin)

- Single add appends one entry, join re-emits exactly one entry: **doc_bytes = 64**
  (= len(FIRST)) ✅.
- `FIRST_SURVIVED_SECOND_ADD=True`: there is no second add, so survival is
  vacuous; single-add leaves exactly one entry. Its measure is True by construction. ✅

### 3.3 Why the seam permits ONLY these two outcomes

1. `_add` returns `entries + [content]` — append; no replacement /
   splice / content rewrite.
2. `_write_file` is the single writer and uses a delimiter join; join is
   length- and order-preserving (delimiters are the only separators).
3. Hence second-add ⇒ FIRST survives (131 bytes); single-add ⇒ exactly one entry
   (64 bytes). Both match the probe's measured values at the SAME pin.

## 4. THE SPEC-vs-PROBE CHECK (§3 + §4 vs executed arms)

### 4.1 §3 — the fix arm's procedure + expected GREEN signature

§3 specifies: (a) the fix arm appends a second entry via `add` (no whole-file
content write in the add closure); (b) writes go through the delimiter join;
(c) expected signature: FIRST_SURVIVED_SECOND_ADD=True and doc_bytes = 131 for two
adds. Executed probe arm B at the same pin yields `FIRST_SURVIVED_SECOND_ADD=True`
and `doc_bytes=131`. **Agreement** — the procedure (append entry, join with
`ENTRY_DELIMITER`) and the measured signature are exactly what the seam delivers.

### 4.2 §4 — the removal control

§4 requires arm C (single add, fix pin) to show `FIRST_SURVIVED_SECOND_ADD=True`
and doc_bytes=64. Executed probe arm C at the same pin yields 64 bytes / True.
**Agreement** — a single add cannot drop the only entry; the file holds exactly
one entry.

### 4.3 Flip-flop integrity — the join line position

Loop-2's audit had mis-placed `_write_file`'s join at `:945`; the corrected
position is `:911`. Re-confirmed at this pin: the verbatim `_write_file`
quoted above emits `ENTRY_DELIMITER.join(entries)` at `:911` (after
`atomic_write_text(`), with no second emission site in the file. The join line is
closed: `a9c65dc4:_write_file` owns the join at `911`, and nothing at `:945`
touches the write path.

## 5. THE CONVERGENCE LINE

The GREEN side (Section 3's append/join signature) and the removal control (arm C)
run cold at `a9c65dc4` — the receipts are derived from, not quoted from, the seam
at this pin, and all receipts agree byte-for-byte; only the RED-side
`268bb091` verification remains (that is the flagship's own ground, not this
lap's) plus the spec's §5/§6 sections, which this lap does not read.

## The form envelope (added at the fold 2026-11-24, loop-3 audit's residue (a))

- **Hard lines, binding:** nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows. The hold-back is never quoted.
- **No installs; all reads LOCAL:** every seam quote above is `git show a9c65dc4…:tools/memory_tool_store.py`, read from the pin's own tree.
- **Commit locally only:** `git add` + `git commit`; NEVER push, NEVER pull (fold-side pushes only).
- **No shared-tree mutation:** no checkout/stash/rm; append-only. The branch is shared — ls-remote first, per fold.
- **Emission contract:** exit 0 = the deliverable exists at the artifact path (written, re-read), then the commit, then the report names the commit sha.
- **The wall clause:** a non-reproduction is a QUESTION with a constructed minimal move — the sibling read at this pin, the narrowed sed, the raw json — before any verdict.
- **Name-and-refuse:** armed = think-tank, investigation-documentation, agent-work-review; refused = the pre-fix pin's tree (the flip-flop — the flagship's ground), installs, web reads, memory-chain appends, config/gateway changes, source edits, github write verbs, coding legs, fan-outs, creative/design/media families.
