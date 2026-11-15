# XNGG-GAPS-VERIFICATION-20261105 — the four seam-gaps cross-checked at the exact pins

**Status:** the rig's verification of xngg1021's four seam/contract gaps (RFC #143379, comment 6630249660) — probed at the exact pinned heads, byte-level, on the fork's battery-clone. Every row cites the pin's code. A claim that does not reproduce is recorded as such — the falsifier applies to every contributor, including our own reviewers' guidance.

## The table

| # | xngg's claim | Pin | Verdict at the pin | Evidence |
|---|---|---|---|---|
| 1 | Stage-7 `verify_post_write` bypassed on the `operations=[...]` batch path | d1bdb4582c | **CONFIRMED** | `tools/memory_tool.py:343`: `return _applied(store.apply_batch(target, operations))` — the batch-branch returns directly after the gate; `verify_post_write` is wired only on the single-op path (`:366-367`). |
| 2 | `_resolve_target` calls `doc_name(doc)` unguarded against `doc_name is None` (standalone `#139606`) | d1bdb4582c | **NOT REPRODUCED at this pin** | `tools/memory_tool.py:280-283`: the guard IS present — `if name is None: return target, ("Invalid chain doc name…")`. Either the citation refers to a different tree-version or the guard landed in the merge-head's reconcile. |
| 3 | `preserve_session` ignores `store.add` return dicts → silent preservation failures | ffb85c2c58 | **CONFIRMED** | `tools/spa_integration.py:100-107`: both `store.add(...)` calls' return values dropped, `return doc_name` directly — the headroom-limit and threat-scanned-payload failures are unobservable from the caller. |
| 4 | `DreamCycle.deep_sleep`'s `.bank()` adapter + `ContextCompressor` hook gap | ffb85c2c58 | **NOT REPRODUCED (adapter part); compressor-hook NOT YET PROBED** | `tools/dream_cycle.py:118-122`: `self.store.bank(c)` IS called with the comment "the banking (the caller verifies)". The ContextCompressor-side hook was outside this probe's window. |

## The register
- The probes: static line-reads at the cited lines + the pattern checks, on the battery-clone at the exact pins (d1bdb4582c, ffb85c2c58). The dynamic probe of gap-2's read-path was blocked by the pin's missing deps (recorded, the static read carried the verdict).
- The value: the review's four gaps now carry pin-level verdicts — two confirmed with byte-citations, one refuted at the pin, one partially-open (the compressor-hook). The falsifier's ethics: a claim's non-reproduction is a finding, never an insult to its author — the pins move, the code reconciles, the verification re-runs at the next heads.
- The follow-ups: the gap-4's compressor-hook probe at ffb85c2c58; the gap-2's re-check at the latest #139606-head (the guard's landing commit); the gaps' battery-tests (the confirmed ones as RED-on-gap probes in the falsifier-lineage).
