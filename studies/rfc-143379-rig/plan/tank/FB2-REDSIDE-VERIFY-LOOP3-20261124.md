# FB-2 RED-SIDE VERIFICATION — LOOP 3 (pre-fix pin `268bb091`)

*Study landing only — nothing public. RFC #143379 stays QUIET; the hold-back stays sealed under the operator's word. Base pin: `268bb09147eaf948ece6a1beecd92a2268a5fc95` (pre-fix, RED). The flip-flop is honored: this lane read **only** the pre-fix tree; the fix pin (`a9c65dc4`) is the secondary's ground and was never opened. Branch `study/rfc-143379-rig-20261105`; fire 2026-11-24.*

## 1. Verdict

**The pre-fix tree supports Section 2's RED signature: CONFIRMED.**

Mechanism (one sentence): at `268bb091` `add("doc:alpha", …)` short-circuits to `_add_doc`, whose `:615 atomic_write_text(doc_path, content, tmp_prefix=".doc_")` writes the new note as the *whole* doc file with no read-merge of the existing doc, so add #2 atomically replaces add #1's bytes and `FIRST_SURVIVED_SECOND_ADD=False`, `doc_bytes=64`, `doc_head`=SECOND — exactly the receipted arm A — is the only behavior the seam permits.

*(One non-substantive procedural note is caught in §4 — the probe used §2's direct-file-read recovery variant rather than the `read` action at a pin where `read` exists; both observe the identical clobbered bytes, so the verdict does not move.)*

## 2. The seam quotes — verbatim, from MY pin only

Source: `git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py`.

**The write (`:615`) and its whole `_add_doc` body (`:580`–`:618`):**

```
 580\t    def _add_doc(self, doc_name: str, content: str) -> dict[str, Any]:
 590\t        # Phase 1: gate check (may be patched by callers for interleaving)
 591\t        gate_result = self._anchor_gate(f"doc:{doc_name}")
 592\t        if not gate_result.get("success"):
 593\t            return gate_result
 594\t        if not gate_result.get("present"):
 595\t            return _error(
 596\t                f"Chain-doc write refused: anchor reference '@doc:{doc_name}' "
 597\t                f"not found in memory.", "anchor_missing",
 598\t                target=f"doc:{doc_name}", doc=doc_name)
 599\t        # Phase 2: transactional commit under the memory anchor lock
 600\t        memory_path = self._path_for("memory")
 601\t        with self._file_lock(memory_path):
 602\t            raw, read_ok = self._read_raw_checked(memory_path)
 603\t            if not read_ok:
 604\t                return _read_failed_error(memory_path)
 605\t            # Re-check the anchor under the lock — this closes the TOCTOU window.
 606\t            if f"@doc:{doc_name}" not in raw:
 607\t                return _error(
 608\t                    f"Chain-doc write refused: anchor '@doc:{doc_name}' was removed "
 609\t                    f"before commit (TOCTOU).",
 610\t                    "anchor_removed", target=f"doc:{doc_name}")
 611\t            # Anchor still present: commit the doc.
 612\t            doc_path = self._doc_path_for(doc_name)
 613\t            from hermes_constants import mkdir_under_hermes_home
 614\t            mkdir_under_hermes_home(doc_path.parent)
 615\t            atomic_write_text(doc_path, content, tmp_prefix=".doc_")
 616\t        return {"success": True, "target": f"doc:{doc_name}",
 617\t                "message": f"Chain doc '{doc_name}' written.",
 618\t                "text_bytes": len(content.encode("utf-8"))}
```

**NO read-merge precedes the write — verified at the pin's bytes:** the only reads in `_add_doc` are `:591 _anchor_gate(...)` and `:602 self._read_raw_checked(memory_path)`, and `memory_path` is `self._path_for("memory")` (`:600`) — i.e. **MEMORY.md, the anchor**, never the doc file. `_doc_path_for` (`:612`) is used only to compute the destination path; the existing `doc_path` bytes are never read, parsed, joined, or appended. `content` is handed to `atomic_write_text` verbatim as the entire file body. This is the clobber's mechanism: no append, no join, no read of prior doc bytes.

**The add route (`:529`–`:543`) and the `_doc` resolver (`:303`–`:314`):**

```
 303\t    def _doc(self, target: str) -> Optional[str]:
 304\t        """Chain-doc resolver. Returns the doc name for a ``doc:<name>`` target,
 305\t        else ``None``. This is the store's own doc-aware arm: ``_is_doc`` in
 306\t        write_gate.py checks ``callable(getattr(store, '_doc', None))`` and
 307\t        returns ``store._doc(target) is not None``.
 308\t        """
 309\t        if not isinstance(target, str) or not target.startswith("doc:"):
 310\t            return None
 311\t        name = target[len("doc:"):].strip()
 312\t        if not name:
 313\t            return None
 314\t        return name
```

```
 529\t    def add(self, target: str, content: str) -> dict[str, Any]:
 530\t        """Append a new entry. Returns error if it would exceed the char limit.
 531\        ...
 535\t        content = content.strip()
 536\t        if not content:
 537\t            return _error("Content cannot be empty.", "missing_content")
 538\t        if scan_error := _scan_memory_content(content):
 539\t            return _error(scan_error, "scan_blocked")
 540\t        # Chain-doc target: route through the transactional anchor protocol
 541\t        doc_name = self._doc(target)
 542\t        if doc_name is not None:
 543\t            return self._add_doc(doc_name, content)
 545\t        def _add(entries, limit):
```

Routing, at my pin: `add("doc:alpha", …)` → `:541 _doc("doc:alpha")` → `:309 startswith("doc:")` true → `:314` returns `"alpha"` → `:542–543` short-circuits to `_add_doc("alpha", content)`. The non-doc append path — `:545 def _add(entries, limit)`, which parses entries and joins with `ENTRY_DELIMITER` — is **never reached** for a `doc:` target. This rebuts the only "maybe it appends" alternative: doc writes bypass the append machinery entirely.

## 3. Receipt re-derivation — arm A (`A-pre-fix-two-add`), cross-walked to the pin's code

Receipt (`fb2-probe-out.json`, committed): `pin=268bb09147ea`, both `add_results` success/`failure_class:null`, `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=false`, `doc_head="SECOND marker note: the fleet's two-add probe, byte unique b"`.

Derived from the code, step by step — not re-quoted from the receipt:

1. **Both adds succeed.** `:591` gate and `:606` re-check both look for `@doc:alpha` in MEMORY.md; the probe seeds `Dated memory chain: @doc:alpha` (probe script `seed_anchor`, `:91–92`), so neither the `anchor_missing` (`:594`) nor `anchor_removed` (`:607`) branch fires. Doc writes never touch MEMORY.md, so the anchor persists across both adds. Both return the `:616 success:True`. ⇒ receipt's two `success:true, failure_class:null`.
2. **Each body is 64 bytes.** `FIRST = "FIRST marker note: the fleet's two-add probe, byte unique alpha."` and `SECOND = "SECOND marker note: the fleet's two-add probe, byte unique beta."` (probe script `:25–26`) are each 64 ASCII bytes (`FIRST` 5 + `alpha.` 6 vs `SECOND` 6 + `beta.` 5 — the differences cancel). `:535 content.strip()` removes nothing. ⇒ after add #1 the doc is FIRST's 64 bytes; after add #2 it is SECOND's 64 bytes.
3. **Why `doc_bytes=64` is forced.** `:615 atomic_write_text(doc_path, content, …)` writes `content` as the whole file (stub contract: `tmp.write_text(content)` then `os.replace(tmp, path)` — a temp file + atomic rename). After add #1 the file is 64 bytes; after add #2 the second `os.replace` swaps in a **new file object** holding SECOND's 64 bytes. With no read of `doc_path` anywhere in `_add_doc` (§2), there is nothing to append to and no delimiter join: the file never exceeds one note's body. Any append/join implementation would yield ≥128 bytes; the measured 64 is only consistent with whole-file replacement.
4. **Why `FIRST_SURVIVED_SECOND_ADD=False` is forced.** The doc file after add #2 contains only SECOND's bytes. A recovery read for FIRST (whether the probe's direct read or the `read` action — see §4) therefore cannot find FIRST's marker: `FIRST in raw` is `False` by construction. `doc_head` (first 60 chars) = `"SECOND marker note: the fleet's two-add probe, byte unique b"` — the head of SECOND, not FIRST.
5. **Determinism.** Because `content` is always the whole file and no prior bytes are ever consulted, after N adds the doc file equals the Nth note's body, *for any N*. The RED outcome is not timing-dependent — the lock in `:601` only protects the anchor check, not any merge — so `FIRST_SURVIVED_SECOND_ADD=False` at `doc_bytes=64` is the **only** behavior this seam permits.
6. **Control corroboration (same pin, from the receipt).** `C-pre-fix-single-add` — one add — gives `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=true`, `doc_head`=FIRST's prefix. That is the same `:615` write with no second replace, confirming the clobber is caused by add #2's replacement and not by a mis-parse. (The fix pin's `doc_bytes=131` in the receipt is the secondary's ground; noted only as the arithmetic contrast — 64+64+3, a join — and its seam was not read here.)

**Result:** the receipt's arm-A json is fully re-derived from `268bb091`'s bytes. The RED signature is real under execution, and the code at MY pin — not the receipt's prose — is what decides it.

## 4. Spec-vs-probe check — §2's ungated procedure vs the executed probe

Source: `FB2-FAILING-CASE-SPEC-20261124.md` §2 (ungated arm A procedure + expected RED signature) vs `fb2-two-add-probe-20261124.py` (committed runner) and `fb2-probe-out.json` (committed receipt).

| §2 step | Executed probe | Match |
|---|---|---|
| fresh temp store | `mem_dir = Path(tempfile.mkdtemp(prefix="fb2-…"))` — probe `:98` | ✓ |
| add FIRST, unique marker-bearing body | `add("doc:alpha", FIRST)` — `:106` i=0, `FIRST` at `:25` | ✓ |
| add SECOND, different unique body | `add("doc:alpha", SECOND)` — `:106` i=1, `SECOND` at `:26` | ✓ |
| recovery re-read of FIRST's key | `raw = (mem_dir/"docs"/"alpha.md").read_text()` — `:110–111` | ✓ (method note below) |
| compare recovered bytes to FIRST's body | `survived = FIRST in raw` — `:112` | ✓ |
| expected RED signature | doc holds SECOND's 64 bytes; FIRST's gone | ✓ (`doc_bytes=64`, `False`, SECOND `doc_head`) |

**Catch — one non-substantive procedural note.** §2's step (c) reads: "*perform a recovery re-read of FIRST's key (a `read` action where that action exists, otherwise a direct file read of the chain-doc file)*." At `268bb091` a `read` action **does** exist, so §2's primary branch there would be `read("doc:alpha")`; the probe instead used the parenthetical's fallback (a direct file read of `mem_dir/docs/alpha.md`, probe `:110–111`). This is a method-level divergence from §2's preferred branch, and THIS lap names it. It does **not** flip the verdict, and the reason is verified at MY pin, not assumed: `read("doc:alpha")` routes via `:413–415` to `_read_doc_bounded("alpha")`, which at `:432–433` reads `self._doc_path_for("alpha")` — the very same `mem_dir/docs/alpha.md` file — and (64 bytes < 3800-byte page, `:427`, `:444`) returns `text` = the file's full bytes at `:466`. So the `read` action and the direct file read observe byte-identical content (SECOND's 64 bytes; FIRST absent); both yield `FIRST_SURVIVED_SECOND_ADD=False`. The RED signature in §2 is itself defined at the file level ("the chain-doc file after the second add contains SECOND's content where FIRST's content had been"), which the direct file read measures most directly.

**Second note (implicit precondition, not a divergence).** §2's prose says "fresh temp store" but does not spell out seeding the anchor; the probe calls `seed_anchor` (`:89–92`, `:99`) to place `@doc:alpha` in MEMORY.md. This is required by `_add_doc`'s anchor protocol at my pin (`:594` `anchor_missing`; `:607` `anchor_removed`) — without it both adds would be refused and the clobber could not be reached. The probe makes §2's implicit precondition explicit; the test target is unchanged.

No substantive divergence: the procedure executed is §2's procedure, and every measured field is re-derived from `268bb091`'s seam in §3.

## 5. Convergence line

The RED side is **run-cold** at its own pin: `268bb091`'s `:615` whole-file write is verbatim-quoted, its no-merge mechanism is byte-verified, and arm A's `doc_bytes=64` / `FIRST_SURVIVED_SECOND_ADD=False` is re-derived as the seam's only outcome; what still waits is the secondary's GREEN-side verification at `a9c65dc4` (out of this lane's base by the flip-flop), plus the two standing RE-DERIVE items the receipts name (C4's verbatim text — row endpoint 404, and the pre-fix leg's `b6ff7dae` record-cited base) — and, as always, the operator's word before any public surface.

## Appendix — receipts (command → result → resolution)

| Command | Result | Resolution |
|---|---|---|
| `git show 268bb091…:tools/memory_tool_store.py \| nl -ba \| sed -n '575,622p'` | `:615 atomic_write_text(doc_path, content, tmp_prefix=".doc_")`; only reads are MEMORY.md anchor checks | Seam quote + no-merge proof (§2) |
| `git show 268bb091…:tools/memory_tool_store.py \| nl -ba \| sed -n '303,320p'` | `_doc` resolver `:309/314` | `doc:` target routing (§2) |
| `git show 268bb091…:tools/memory_tool_store.py \| nl -ba \| sed -n '529,548p'` | `add` → `:541–543 _add_doc`; append `_add` at `:545` unreachable for doc targets | Add route (§2) |
| `git show 268bb091…:tools/memory_tool_store.py \| nl -ba \| sed -n '400,470p'` | `read("doc:…")` → `_read_doc_bounded` → `_read_raw_checked(doc_path)` `:432–433`, `text` at `:466` | §4 method-divergence resolution |
| `read_file fb2-probe-out.json` | arm A: 64 bytes, `False`, SECOND head | Receipt re-derived (§3) |
| `read_file FB2-EXECUTION-RECEIPTS-20261124.md` | A RED / B GREEN / C green-on-both | Cross-check context (§3.6) |
| `git show HEAD:…/fb2-two-add-probe-20261124.py` | `:98` temp store, `:99` seed, `:106` adds, `:110–112` recovery/compare | Spec-vs-probe check (§4) |

*The fix pin's tree was never read. No push, no pull, no source edits, no public post. All findings derive from `268bb091` bytes and the committed receipts.*
