# FOLLOWUP-SEAM-OPTION-BRIEFS-20261101 — runner seam, both options shaped

Seam (named by the round-3 fold, reproduced byte-for-byte, R2-leg1 2026-10-30):
Kevin's kvnloo/hermes-agent#659 runner (head `5184f7a1`) refuses the published
head `b84150e9be` before a single test:

    RuntimeError: Candidate already contains injected test path; refusing overwrite
    (exit 1)

Cause: the round-2 combined substrate already ships the shared falsifier probe
in-tree — consent fixture byte-identical, probe file a strict prefix missing
the four encoding-freshness tests. Two-sided resolution: (a) runner gains an
already-pinned-probe mode; (b) the substrate probe gains the four
encoding-freshness tests. Both are shaped below so the pick lands with the work
already done. No pushes, nothing public — this file is the only artifact.

Receipts cited (all re-verified, see `NIGHT-654-R2-LEG1-RUNNER-PROBE-20261030.md`
and `NIGHT-654-R2-VERIFY-FOLD-20261030.md`):
- runner head `5184f7a19bbd6df8b50be32bb1cd501f163c19b9`, branch
  `study/rfc143379-shared-falsifiers-20261026`, file
  `studies/rfc-143379/checkout/run_fixed_substrate.py`
- candidate head `b84150e9be88911280f981467de9628fcfb0f60f` (round2-combined-substrate)
- consent fixture sha256 `f9076148…` identical on both sides
- in-tree probe `tests/tools/test_rfc_homework.py` (blob `4e5bfc5d…`): strict
  prefix of the runner's probe; first 130 lines byte-identical; missing the four
  encoding-freshness tests; `git grep encoding_freshness b84150e9be -- tests/`
  returns 0 matches.
- runner selftests: 14/14 OK (0.408s); selftest blobs match receipt
  (`2494ecb4` runner, `c17b66b7` tests).

---

## Option (a) — already-pinned-probe mode (runner-side, on #659)

### Mode name
`--already-pinned-probe` (CLI flag) / `ALREADY_PINNED` (internal mode tag).
Default behaviour unchanged: the runner still injects its own probe + fixture
into a pristine candidate and still refuses to clobber an existing path. The
flag opts into the new mode for candidates that already carry the shared
falsifier probe in-tree.

### Guard check (what the mode would accept)
Replace the hard refusal at L175-177:

    if target_probe.exists() or target_scenarios.exists():
        raise RuntimeError("Candidate already contains injected test path; refusing overwrite")

with a conditional that, when `--already-pinned-probe` is set, performs a
byte-identity verification instead of refusing:

1. Consent fixture: `sha256(candidate/tests/tools/rfc_consent_scenarios.json)`
   MUST equal the runner's own fixture sha256 (`f9076148…`). Mismatch → refuse
   with `RuntimeError("Candidate consent fixture differs from pinned probe")`.
2. Probe superset: the candidate's `tests/tools/test_rfc_homework.py` MUST
   define all four names in the runner's `REQUIRED["encoding_freshness"]`
   selector (the four encoding-freshness tests) — i.e. the candidate's probe is
   the runner's probe or a superset of it. Concretely: grep the candidate file
   for each of the four def names; all four must be present. (This is the
   link to option (b): without (b) the check fails and the mode refuses —
   (a) alone never certifies an incomplete probe.)
3. The five base defs (`test_read_dispatch_contract`,
   `test_read_concurrency_snapshot`, `test_chain_doc_reference_race`) and the
   consent parametrization (`test_no_save_never_lands_in_memory_or_pending`
   ×12) must also be present, so the candidate probe is byte-equivalent to
   the runner's required set, not a partial.

Only when all three hold does the mode skip injection and run the candidate's
own copy. On any mismatch the mode refuses with a named reason (no silent
fallback to injection, no overwrite).

### Skip-injection path
When accepted, the runner does NOT copy its probe/fixture into the worktree.
Instead it records in the receipt that the probe was already pinned in-tree
(`"probe_source": "candidate-in-tree"`, `"injection": "skipped"`) and runs the
candidate's own `tests/tools/test_rfc_homework.py` + `rfc_consent_scenarios.json`
through the normal `run_one` path. All downstream counting/verification
(`counts()`, required-green logic) is unchanged.

### Acceptance test
- Runner's existing 14 selftests still pass (`python3 -m unittest discover -s .
  -p test_fixed_substrate_runner.py` → `Ran 14 tests … OK`).
- New selftest `test_already_pinned_probe_mode` added to
  `test_fixed_substrate_runner.py` covering: (i) a candidate that carries the
  pinned probe → mode accepts, skips injection, receipt records
  `probe_source: candidate-in-tree`; (ii) a candidate missing the fixture →
  refusal with the named reason; (iii) a candidate with a drifted consent
  fixture sha → refusal; (iv) a candidate with the probe but missing the four
  encoding tests → refusal (the (a)↔(b) dependency).
- End-to-end: run the mode against the published head `b84150e9be` with the
  (b)-extended probe present → produces `receipt.json` with
  `encoding_freshness` 7/7 passed and `required_green: true`. That is the
  certification the runner was built to emit; it is currently blocked only by
  the seam named here.

### Revert
Remove the `--already-pinned-probe` flag and the conditional block; restore the
original two-line guard. No schema, receipt format, or test-path changes — the
revert is a single-file, single-hunk deletion. The receipt's `probe_source`
field becomes optional/absent again; old receipts remain valid (field simply
missing).

---

## Option (b) — four encoding-freshness tests in the substrate probe

The four test defs absent from the in-tree probe (strict prefix) but present in
the runner's selector. Reconstructed from the runner's selector
(`REQUIRED["encoding_freshness"]`) and the JUnit receipt of a green run, then
appended to `tests/tools/test_rfc_homework.py`'s existing shape. Verified
running green against the substrate's `MemoryStore` (23 passed = 16 original +
7 new cases).

### Test sketches (append after `test_no_save_never_lands_in_memory_or_pending`)

#### 1. `test_read_reflects_external_edit_without_mutating_frozen_prompt`
Parametrized `[memory-MEMORY.md]`, `[user-USER.md]`.

Assertion shape: capture `store._system_prompt_snapshot[target]` at load time;
externally append a new entry (with the `§` delimiter) directly to the file;
call `store.read(target)`; assert the read returns the new entry; assert the
frozen snapshot is byte-unchanged and does not contain the marker.

Why it holds: `read()` re-reads from disk and parses; the frozen snapshot is
captured once in `load_from_disk()` and never mutated by `read()` (read is
read-only: no gate, no drift guard, no write, no cache mutation). This is the
prefix-cache-stability invariant.

#### 2. `test_read_handles_utf8_bom_without_rewriting`
Parametrized `[memory-MEMORY.md]`, `[user-USER.md]`.

Assertion shape: write `b"\xef\xbb\xbfBOM entry content"` to the file; record
disk bytes; call `store.read(target)`; assert the entry does not start with
`\ufeff` and contains the content; assert disk bytes are unchanged.

Why it holds: `_read_raw_checked` decodes with `utf-8-sig`, which strips a
leading BOM; `read()` performs no write, so the file is untouched. (Plain
`utf-8` would glue U+FEFF to the first entry forever — the bug #10878/#10888
this test pins against.)

#### 3. `test_read_corrupt_utf8_keeps_disk_untouched`
Parametrized `[memory-MEMORY.md]`, `[user-USER.md]`.

Assertion shape: write invalid UTF-8 bytes (`b"\xff\xfe invalid utf8 \x80\x81"`);
assert `_read_raw_checked(path)` returns `read_ok is False` and empty raw; assert
`store.read(target)` returns `success is False`; assert disk bytes are unchanged.

Why it holds: decoding stays strict (no `errors="replace"`), so undecodable
bytes surface as `read_ok=False` and `_read_failed_error` — never a lossy view
that a later save would persist over the real bytes.

#### 4. `test_chain_doc_orphan_remains_readable_but_not_writable`
Single case (no parametrize).

Assertion shape: create `docs/orphan.md` directly (no `@doc:orphan` anchor in
MEMORY.md); assert `store.read("doc:orphan")` succeeds and returns the text;
assert `store.add("doc:orphan", ...)` is refused (`success is False`); assert
the doc file is unchanged.

Why it holds: `_read_doc_bounded` reads the file regardless of anchor state
(readable), while `_add_doc` runs `_anchor_gate` first and refuses when the
`@doc:<name>` reference is absent (not writable) — the orphan stays readable
but cannot be extended.

### Verification
Extended probe file (in-tree 16 + 4 defs/7 cases = 23) run against the
substrate's `MemoryStore`:

    python3 -m pytest tests/tools/test_rfc_homework.py -q
    → 23 passed in 0.41s (was 16 passed)

The four new defs are appended verbatim to the in-tree probe's shape (same
imports, same `memory_env` fixture, same ENTRY_DELIMITER semantics). No change
to the existing 16 cases.

### Revert
Delete the appended block (the four defs). The in-tree probe returns to its
original 16/16 green state. No other file touched.

---

## Receipts — the runner's selector, quoted

From `studies/rfc-143379/checkout/run_fixed_substrate.py` (runner head
`5184f7a1`), lines 18-28:

```python
REQUIRED = {
    "read_dispatch": "test_read_dispatch_contract",
    "read_concurrency": "test_read_concurrency_snapshot",
    "chain_reference_race": "test_chain_doc_reference_race",
    "encoding_freshness": (
        "test_read_reflects_external_edit_without_mutating_frozen_prompt or "
        "test_read_handles_utf8_bom_without_rewriting or "
        "test_read_corrupt_utf8_keeps_disk_untouched or "
        "test_chain_doc_orphan_remains_readable_but_not_writable"
    ),
}
```

From the green JUnit receipt (study-check, run on a substrate carrying the
four tests), `encoding_freshness.xml`:

```xml
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_reflects_external_edit_without_mutating_frozen_prompt[memory-MEMORY.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_reflects_external_edit_without_mutating_frozen_prompt[user-USER.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_handles_utf8_bom_without_rewriting[memory-MEMORY.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_handles_utf8_bom_without_rewriting[user-USER.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_corrupt_utf8_keeps_disk_untouched[memory-MEMORY.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_read_corrupt_utf8_keeps_disk_untouched[user-USER.md]" />
<testcase classname="tests.tools.test_rfc_homework"
  name="test_chain_doc_orphan_remains_readable_but_not_writable" />
```

7 cases total (3 defs × 2 targets + 1 standalone), matching the selector's
OR'd names. `tests=7, failures=0, errors=0, skipped=0` on that run.

Guard that fires today (runner L175-177, quoted):

```python
target_probe = checkout / "tests/tools/test_rfc_homework.py"
target_scenarios = checkout / "tests/tools/rfc_consent_scenarios.json"
if target_probe.exists() or target_scenarios.exists():
    raise RuntimeError("Candidate already contains injected test path; refusing overwrite")
```

---

## The pick

- Option (a) alone unblocks the runner on any candidate that already ships the
  pinned probe, but still refuses on the current substrate until (b) lands
  (the encoding selector would collect 0 cases).
- Option (b) alone completes the in-tree probe but the runner still refuses to
  run it (the guard fires first).
- Doing both is the full resolution: (b) makes the in-tree probe a superset of
  the runner's required set, (a) makes the runner accept and run that superset
  instead of refusing. Either order works; (b) first is the smaller change and
  is independently verifiable (23 passed).

No pushes, nothing public. Posting the morning comment / any public surface
stays gated on the user's word.
