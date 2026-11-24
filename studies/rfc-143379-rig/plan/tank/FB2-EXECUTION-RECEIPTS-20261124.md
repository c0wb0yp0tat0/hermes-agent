# FB-2 EXECUTION RECEIPTS — the promised test run on our side (2026-11-24)

*Study landing only; nothing public. The two-add probe executed against the verbatim store code at both named pins — real `add(doc:…)` path, stub-import sandbox (no installs, no branch touched), fresh temp store per arm, seeded `@doc:alpha` anchor. Probe runner: `/root/.hermes/cache/scratch/fb2-two-add-probe-20261124.py`; raw JSON: `fb2-probe-out.json`.*

## The pre-registered bars and the measured verdicts

| Arm | Pin | Two adds | `FIRST_SURVIVED_SECOND_ADD` | Bar | Verdict |
|---|---|---|---|---|---|
| A · ungated | `268bb09147ea…` | FIRST, then SECOND | **False** — the doc holds SECOND's 64 bytes only; FIRST's bytes gone | RED expected | **RED** — the clobber is REAL under execution |
| B · the fix (`A-fix-two-add` in the raw json) | `a9c65dc43db9…` | FIRST, then SECOND | **True** — the doc holds both (131 bytes; FIRST's bytes present) | GREEN expected | **GREEN** — the fix preserves the first |
| C · removal control | both pins | FIRST only | True on both (64 bytes, FIRST's bytes) | green on both | **GREEN** — the probe is not a false positive |

## The mechanism, at the executed seam

- **Pre-fix `268bb091`:** `add(doc:…)` routes to `_add_doc`; the write is `atomic_write_text(doc_path, content, tmp_prefix=".doc_")` (verbatim :615) — `content` is the WHOLE file, so add #2 replaces add #1's bytes entirely. No append, no join.
- **Fix `a9c65dc4`:** `add` routes through `_mutate` → entries are parsed, the new entry appended, `_write_file` joins with `ENTRY_DELIMITER` (`atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")`, verbatim :911) — add #2 appends; add #1's bytes survive.

Both seam-citations (`268bb091:615` and `a9c65dc4:911`) are now backed by executions, not greps.

## What this closes

The spec's Section 2 (RED signature) and Section 3 (GREEN signature) are no longer RE-DERIVE items — they are run receipts at the named pins. The removal control (Section 4) is executed. The only standing RE-DERIVE items remain C4's verbatim text (the row's endpoint refused the lane; 404 receipted) and the pre-fix leg's `b6ff7dae` base (record-cited only; the grafted 40-hex withdrawn at the loop-2 fold).

**The promised test is now run-cold in full at our side.** Nothing has been posted; the RFC surface is quiet; the hold-back stays sealed under the operator's word.
