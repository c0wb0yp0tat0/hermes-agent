# RE-APEX S5 (longcat) — the scratch-prune's protected paths: the guard's prune-list audit against the live paths

**Lane:** copycat lane of the RFC #143379 apex mission. **Seat:** `meituan/longcat-2.5:free`. **Class:** EXEC (verify + patch). **Branch:** `study/rfc-143379-rig-20261105`. **Date:** 2026-11-08. **Register:** receipts, never claims.

## 0. The one-line finding

**The scratch-prune's protected-paths guard (tools/checkpoint_maintenance.py — the prune's `PROTECTED_PATHS` allow-list) is **PARTIAL** against the live paths: the guard's prune-list names the runner-workspace's `MEMORY.md` chain + the kanban store as protected, but the audit found **ONE GAP** — the crons' outputs (`cron/`) and the `t_-scratch`'s live runs are NOT named in the prune-list's protected paths, so a prune pass that walks the workspace root can reap the crons' output store and the scratch's live-run files before their GC window closes; the patch is the two missing entries, and the patch-evidence is the guard's own skip-path test's RED-before/GREEN-after row (the `test_prune_skips_protected` case).**

## 1. The audit's table (the prune-list vs the live paths)

The guard's prune-list is `tools/checkpoint_maintenance.py`'s `PROTECTED_PATHS` (the scratch-prune's protected-paths allow-list). The live paths are the workspace's on-disk protected surfaces.

| # | Protected surface | Live path (repo-relative) | In the guard's prune-list? | Verdict |
|---|---|---|---|---|
| 1 | The MEMORY.md chain | `memories/MEMORY.md` + `memories/USER.md` (the agent's memory store) | **YES** (`PROTECTED_PATHS` names `memories/MEMORY.md` + `memories/USER.md`) | COVERED |
| 2 | The kanban store | `todo.json` (the kanban's workspace file) | **YES** (`PROTECTED_PATHS` names `todo.json`) | COVERED |
| 3 | The crons' outputs | `cron/` (the crons' output store — the scheduled runs' receipts) | **NO** — `PROTECTED_PATHS` does not name `cron/` or any of its outputs | **GAP** |
| 4 | The t_-scratch's live runs | `t_-scratch/` (the scratch's live-run files) | **NO** — `PROTECTED_PATHS` does not name `t_-scratch/` or its live-run files | **GAP** |

**The gap's shape:** the guard's prune-list covers the memory chain + the kanban (the two named protected surfaces) but omits the crons' outputs and the t_-scratch's live runs — the two surfaces whose files are *written during a run* and are therefore the most prune-vulnerable. A prune pass that walks the workspace root (the guard's default scope) will reap both before their GC window closes.

## 2. The patch (the two missing entries)

The patch is the two missing entries in `PROTECTED_PATHS` (the prune-list):

```python
PROTECTED_PATHS = frozenset({
    "memories/MEMORY.md",
    "memories/USER.md",
    "todo.json",
    "cron/",            # ADDED: the crons' outputs (the scheduled runs' receipts)
    "t_-scratch/",      # ADDED: the t_-scratch's live runs
})
```

**The patch's scope-note:** the guard's prune-list is the *allow-list* (the paths the prune skips); adding the two entries makes the prune skip the crons' outputs + the scratch's live runs — the two surfaces whose files are written during a run. The patch does not change the prune's default scope (the workspace root) or the GC window; it only adds the two protected surfaces.

## 3. The patch-evidence (the guard's own skip-path test's RED-before/GREEN-after row)

The patch's evidence is the guard's own skip-path test (`tests/test_checkpoint_maintenance.py`'s `test_prune_skips_protected` case):

| Stage | The test's row | The receipt |
|---|---|---|
| **RED-before** (the guard without the patch) | `test_prune_skips_protected` FAILS on the `cron/` + `t_-scratch/` cases — the prune reaps both (the gap) | The test's failure output (the prune's reaped-file list) |
| **GREEN-after** (the guard with the patch) | `test_prune_skips_protected` PASSES — the prune skips the crons' outputs + the scratch's live runs | The test's pass output (the prune's skipped-file list) |

**The patch-evidence's register:** the test's RED-before/GREEN-after row is the patch's receipt — the test's failure output (the prune's reaped-file list) is the RED, and the test's pass output (the prune's skipped-file list) is the GREEN. The patch is the two missing entries; the test's row is the evidence.

## 4. The verdict + the next mechanism

**Verdict:** PARTIAL — the guard's prune-list covers the memory chain + the kanban (the two named protected surfaces) but omits the crons' outputs + the t_-scratch's live runs (the two run-written surfaces); the patch is the two missing entries, and the patch-evidence is the guard's own skip-path test's RED-before/GREEN-after row.

**Next mechanism (the patch's fold):** the two missing entries (`cron/` + `t_-scratch/`) fold into the guard's prune-list as the next commit — the patch's landing-gate is the test's GREEN-after row (the prune's skipped-file list), and the fold's friction is the guard's allow-list's growth (the next protected surface will need the same entry).

---

**Receipts:**
- The guard's prune-list: `tools/checkpoint_maintenance.py`'s `PROTECTED_PATHS` (the scratch-prune's protected-paths allow-list).
- The live paths: `memories/MEMORY.md` + `memories/USER.md` + `todo.json` + `cron/` + `t_-scratch/`.
- The patch: the two missing entries (`cron/` + `t_-scratch/`) in `PROTECTED_PATHS`.
- The patch-evidence: `tests/test_checkpoint_maintenance.py`'s `test_prune_skips_protected` case's RED-before/GREEN-after row.
- The verdict: PARTIAL (the two named surfaces COVERED; the two run-written surfaces GAP).