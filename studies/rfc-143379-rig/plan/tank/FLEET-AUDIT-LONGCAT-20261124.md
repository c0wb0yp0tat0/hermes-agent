# FLEET AUDIT — LONGCAT (the reserve's lens) — 2026-11-24

*Seat: `meituan/longcat-2.5:free` — the RESERVE (operator-designated 2026-11-24). Subject: `FB2-FAILING-CASE-SPEC-20261124.md` (flagship). Ground: `VET-KVNLOO-20261122.md` @ `9ce4e0078c`. Companion read: `SCHEDULED-WAKE-READ-20261124.md`. Branch: `study/rfc-143379-rig-20261105`. This audit VERIFIES; it does not mutate the spec, and it publishes nothing.*

## 1. The verdict line

**READY-WITH-CORRECTIONS.** All five promised elements are present in run-cold form and every load-bearing pin and `_add_doc` mechanism reproduces against THIS tree; the only wall is one supporting pin (`b6ff7dae`) that does not resolve here, carried by one overstated phrase — both are fold-line corrections, not a missing element, so no landing is struck.

## 2. The five checks' rows

### Row 1 — Promise-completeness: PASS (presence + run-cold form; one leg caveat feeds Correction 1)

The thread's promise names five elements. Each located in the spec, each quotable:

| # | Promised element | Spec location | Run-cold form |
|---|---|---|---|
| A | expected failure signature, ungated add on MAIN | §2 "Expected signature (what the failing run emits): both a `link:` entry and a `remove anchor:` refusal."; test `test_memory_round2_ungated_double_add_overwrites_first_note` (§9.1) | §9.2: `tree: 268bb091…`, patch context for `_anchor_gate`, `entries=[NOTE_A, NOTE_B]` |
| B | the same case on THE FIX | §9.1 `test_combined_best_ungated_double_add_preserves_both_entries` @ `a9c65dc4…` | §9.2: same patch context, same entries, asserted preserved union |
| C | the removal control | §9.1 `test_r2_chain_doc_interleaved_add_refuses_after_remove`; §2/§9.2 `_anchor_gate` receipts | pre-fix leg cites `b6ff7dae/tools/memory_tool_store.py`; post-fix `a9c65dc4` |
| D | the hold-back class | §11 HOLD-BACK block — ONE class `BATCH-PATH DOUBLE-ADD`, withheld from published surface (`holdback-test-hints.txt`) | §8 trace constraints + §9.1 test name; release = pair's word |
| E | the pinned SHAs | §6 table (`0f602c5f16`, `268bb091…`, `a9c65dc4…`) + §9.2 per-test pins | rev-parse receipts below |

Caveat (feeds Correction 1): element C's pre-fix leg is written against the record pin `b6ff7dae`, which does not resolve in this tree; a stranger cannot execute that leg from the spec's pin alone. Element present; cold-run receipt absent for that one leg.

### Row 2 — Pin-truth: PASS with one RE-DERIVE marker

Receipts (all local, git-only):

```
$ git rev-parse --verify 268bb09147eaf948ece6a1beecd92a2268a5fc95
268bb09147eaf948ece6a1beecd92a2268a5fc95     # RESOLVES
$ git rev-parse --verify a9c65dc43db9000e8b6e238b50916aa6fa32ff08
a9c65dc43db9000e8b6e238b50916aa6fa32ff08     # RESOLVES
$ git rev-parse --verify 0f602c5f
0f602c5f6f18615632535251d62a2db74ce93b69     # RESOLVES
$ git rev-parse --verify 9ce4e0078c
9ce4e0078cd14f9758e0b962d4744f3cbc0bb3eb     # RESOLVES (vet pin)
$ git rev-parse --verify 60a2e156
60a2e1563802368b46018bba2a70f11de31a6b0a     # RESOLVES (supporting)
$ git rev-parse --verify ec649ad9
ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a     # RESOLVES (supporting)
$ git rev-parse --verify af16e3ab16
af16e3ab16eed2492552c325ad1777533a8b7004     # RESOLVES (supporting)
$ git rev-parse --verify b6ff7dae
fatal: Needed a single revision            # DOES NOT RESOLVE — RE-DERIVE MARKER
```

Scope notes. The spec quotes its pins from the tree (it prints the lines it relies on), and every pin the spec's claims ride on resolves. The vet's R4 recorded `0f602c5f`/`a9c65dc4` as "ABSENT from our object store"; in THIS tree both resolve, so that absence receipt is stale and does not bind the spec. `b6ff7dae` (§6 "R2 base") is the one non-resolution; the spec labels it observed, which overstates it — see Row 5 / Correction 1.

### Row 3 — Mechanism: PASS

Spec claim (§2): "`_add_doc` writes **whole file at once** — the new note's `content` is assigned to the whole target file… Load-bearing path: `tools/memory_tool_store.py:580-618`. Nothing merges/renames/compacts."

Tree at the class's pin:

```
$ git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | grep -n "def _add_doc\|atomic_write_text\|def chain_docs"
580:    def _add_doc(self, doc_name: str, content: str) -> dict[str, Any]:
615:            atomic_write_text(doc_path, content, tmp_prefix=".doc_")
620:    def chain_docs(self) -> list[str]:
```

Lines 580–619 hold the `def`, Phase-1 gate, Phase-2 lock/re-check, and the single `atomic_write_text(doc_path, content, …)` — no merge, rename, or compaction. Range and quoted line match literally.

Fix side (§2) quoted `atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")   # :945`; tree at `a9c65dc4`:

```
69:def _sanitize_entry(entry: str, filename: str) -> str:
349:    def _file_lock(path: Path):
488:        with self._file_lock(path):
551:    def read(self, target: str) -> dict[str, Any]:
562:        with self._file_lock(path):
567:        view = [_sanitize_entry(e, path.name) for e in entries]
945:            atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")
```

All three guard arms present at the class's pin. Catch: none.

### Row 4 — Hold-back: PASS — exists and is sealed

§11 marks exactly ONE class, `BATCH-PATH DOUBLE-ADD`, clearly withheld: "Withhold from published surface: `holdback-test-hints.txt`" and "Release gate: the pair's word." §8 seals it further — "no content-string claims are made" and "neither entry set contains any `link:`/`anchor:`/`remove:` token"; §9.1 discloses only the test name (`test_batch_double_add_two_docs_second_overwrites_first`). No expected-signature string for the hold-back appears elsewhere in the spec. Sharpness holds: leading hints remove an anchor by patching `_anchor_gate`, while §11 states batch adds by construction produce no anchor event — a leading hint cannot satisfy the class. The audit never publishes the hold-back contents.

### Row 5 — Residue: ONE named, ONE qualified, ONE stale-promise coupling

(a) **Overstated claim (headline residue).** §2: "The first-patch tip parent: `268bb09147eaf948ece6a1beecd92a2268a5fc95`; the first-patch deltas (`60a2e156` / `b6ff7dae`) are OBSERVED, not invented." Receipt: `60a2e156` resolves; `b6ff7dae` returns `fatal: Needed a single revision`. The phrase asserts tree-observation for a delta the tree does not contain. Fold-line correction in §3 below.

(b) **Stale-promise coupling.** §6 describes `b6ff7dae` as "R2 base" while §7's pre-fix variant test is written as `test_r2_chain_doc_interleaved_add_refuses_after_remove` at `b6ff7dae/tools/memory_tool_store.py`. Because the pin does not resolve, the element-C pre-fix leg cannot be run cold; the spec presents it as runnable. This is the same byte-level fact as (a), seen from the run-cold angle.

(c) **Vocabulary / softer-claim scan.** No refused vocabulary found in the audited sections: the spec uses "NOT-RUN", "trace-only", "withheld" honestly, and labels all live claims as pending. One softer-than-receipt spot: §9.3 calls the two harnesses "byte-verified" for their pin/mechanism quotes — true for the quoted lines, but the phrase could be read as covering the not-yet-run tests; scope it in the fold if the head wants the seam tighter.

## 3. The corrections block (fold-line, mechanical)

- **C1 — §2 phrase "are OBSERVED, not invented".** Replace with: "the first-patch delta `60a2e156` is observed in-tree; `b6ff7dae` is cited from the record and does not resolve in this tree (`git rev-parse --verify b6ff7dae` → `fatal: Needed a single revision`)."
- **C2 — §6/§7 pin `b6ff7dae`.** Annotate: "record pin, non-resolving in this tree — re-derive from R2's record row before running the pre-fix leg", or substitute a resolvable base if R2's record supplies one. The head applies mechanically; the landing itself stands.
- **C3 — §9.3 "byte-verified" scoping.** Qualify to the quoted mechanism/pin lines, not the not-yet-run tests.

No strike of the landing. The corrections ride the fold line.

## 4. The pair's briefing

- Rely on: five-element completeness; §6 load-bearing pins resolve; `_add_doc` mechanism reproduced at `268bb091` (:580 def, :615 whole-file atomic write); hold-back class exists, is sharp, and is sealed.
- Watch: `b6ff7dae` does not resolve here — the removal-control pre-fix leg is record-derived, and the phrase "OBSERVED, not invented" overstates it; apply C1/C2 mechanically.
- Waits the operator's word: publication and any hold-back release; this lane posted no row and struck no landing.

---
*Audit receipts: spec head+tail read in full; §3–§8 middle windowed by reader size — deepened where load-bearing (mechanism and pins verified by direct git reads). Pins: `268bb09147eaf948ece6a1beecd92a2268a5fc95`, `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`, `0f602c5f6f18615632535251d62a2db74ce93b69`, `60a2e1563802368b46018bba2a70f11de31a6b0a`, `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a`, `af16e3ab16eed2492552c325ad1777533a8b7004` resolve; `b6ff7dae` does not.*