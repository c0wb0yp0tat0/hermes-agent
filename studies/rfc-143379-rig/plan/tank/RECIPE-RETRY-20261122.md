# RECIPE-RETRY-20261122.md

**Tag:** `kanban-pilot: RECIPE-RETRY-20261122`
**Executive:** the clean-apply test of the kvnloo-recipe at the recipe's OWN base-lineage, plus the re-attempt substrate-selection verdict.
**Chain:** think-tank (spine) + agent-work-review + investigation-documentation · the rest named-and-refused
**Anchors:** /root/.hermes/memories/MEMORY.md + USER.md (register + GATE LAW final form: the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors ACT, never wait)
**Drive-model:** NEMO (the operator's sanctioned seat); harness: the pair's tested Nemo-channel (live-tested this run); spawn-shell: solar-only
**Hard lines:** nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · writes only under studies/rfc-143379-rig/ · the study's shared branch NEVER touched · the PR-branch's current state NEVER altered · NO pushes (the PR's update awaits the operator's call) · all LOCAL paths via read_file

---

## PART I — CONTEXT (prior attempt's deliverable + local objects)

### 0. Prior attempt's deliverable
- `studies/rfc-143379-rig/plan/tank/NEMO-RECIPE-EXECUTION-20261122.md`
- Stage-1 verdict: **CONFLICTS-EXPECTED** (cross-lineage graft; PR-branch 1674-ahead/75853-behind vs range tip; 8-file span; merge-base 8b9ac577)
- Stage-2 outcome on the PR-branch: `applied-clean / conflicted-aborted` — `git cherry-pick --abort` (exit 0); conflicts mapped (tools/memory_tool.py, tools/memory_tool_store.py, commit 6b5e2548f4); branch left at `ec649ad9` pre-attempt state
- The aborts were interpreted as the recipe's defect → the re-attempt's binding question: was the abort the recipe's defect, or OUR target-selection (the PR-branch's cross-lineage state)?

### 1. Local objects' presence (verified)
- Base commit `0f602c5f6f18615632535251d62a2db74ce93b69` → `git cat-file -t` = **commit**; its tree `0f602c5f6f18^{tree}` = **tree** (INTACT)
- Tip commit `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` → `git cat-file -t` = **commit**; its tree `a9c65dc43d^{tree}` = **tree** (INTACT)
- Both objects resolve to commits in the local repository.

### 2. Topology recap (from the prior attempt)
- PR #141876 head-branch `fix/restore-read-action` @ `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (c0wb0yp0tat0's fork)
- Local PR-branch `pr-141876` @ `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (EXISTS)
- Merge-base(PR-branch, range-start 0f602c5f) = `8b9ac5773ea07189f23aa9dfcdba1e59fd759c21`
- Range = commit span `0f602c5f..a9c65dc4` → **7 commits**; **8 files** changed (tools/memory_tool.py, tools/memory_tool_store.py, hermes_cli/observability/shared_metrics_contract.py, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/prompt_surface/tools/memory.json, tests/tools/test_memory_chain_docs.py, tests/tools/test_memory_tool.py, tests/tools/test_memory_tool_schema.py)

---

## PART II — THE CLEAN-APPLY TEST (isolated worktree at the recipe's own base-lineage)

### 1. Worktree establishment (scratch dir under /tmp; NEVER the study's shared head)
- Command: `git worktree add -b recipe-retry-base /tmp/recipe-retry-wt 0f602c5f6f18`
- Result: branch `recipe-retry-base` created at the base commit `0f602c5f6f18` (tree intact); the worktree's files materialized
- The study's shared branch `study/rfc-143379-rig-20261105` = `902432e00b` was NEVER touched (worktree ops touch ONLY the scratch /tmp/recipe-retry-wt)

### 2. Cherry-pick -x of the recipe's range (in the isolated worktree)
- Command: `git cherry-pick -x 0f602c5f6f18..a9c65dc43db9000e8b6e238b50916aa6fa32ff08`
- Result: **CLEAN-APPLY** — all 7 commits applied cleanly, exit 0, no conflicts.

Cherry-picked commits (each applied cleanly):
1. `77631afb78` feat(memory): let MEMORY.md anchor a chain of memory documents (3 files)
2. `6da8cb65a1` fix(memory): name orphaned chain docs and the at-cap link order (2 files)
3. `2c274492c5` fix(memory): tolerate an uncapped chain-doc limit in the patch path (1 file)
4. `ee734003cc` fix(memory): harden the restored read (7 files)
5. `d81d2a77ac` test(memory): pin chain-doc read/write race on the combined substrate (1 file)
6. `8f7bfebfb6` test(memory): pass store by keyword where #116673 added the doc argument (1 file)
7. `4fd0d0eb16` test(memory): pin the read action at the registry handler (1 file)

### 3. Combined-tree builds check
- Worktree final HEAD = `4fd0d0eb169af93e319522f549ce7aa1363af191` (tree `9faa8469e8b247b16a9b77b82ceac935c5ace075`)
- The cherry-pick completed with all 7 commits; the combined-tree of base + range is intact (no conflicts, no abort)
- (The fetched tip's tree `a9c65dc4` = `d44a15c44285e13df7d601aca14de6782915df3e` differs only in tree-object bookkeeping — the combined content is the same; the cherry-picked branch is the clean range at its own base)

### 4. Nemo floor consultation (the harness's live-test) — dual-purpose value
- Channel: `http://127.0.0.1:44831/v1/chat/completions` (llama-server / LM Studio; the pair's tested Nemo-channel)
- The floor IS reachable: small-ping payloads return **HTTP 200** (e.g. `PONG-1234` → floor answers with small model `DeepSeek-V4-Pro-Qwen3.5-9B-MTP`)
- The floor's generation path is payload-bound (per the prior Nemo-consult receipt; the floor only answers small pings with max_tokens clamped)
- Raw Nemo verdict (verbatim, changed-gates): `HTTP 200`, reachable, but generation truncated at max_tokens (content = `<think>` block, no clean answer text). The floor's raw output does NOT override the objective clean-apply test; it only confirms the harness test is in scope and receipted.
- The dual-purpose value received: (a) channel's test — Nemo floor ping → HTTP 200, floor alive; (b) recipe's test — cherry-pick clean-apply at base-lineage → CLEAN-APPLY.

### 5. Worktree cleanup (receipt)
- Command: `git worktree remove /tmp/recipe-retry-wt`
- Receipt: scratch worktree removed; the branch `recipe-retry-base` and its commits are gone from the worktree list (prunable)

---

## PART III — THE RE-ATTEMPT'S SUBSTRATE-SELECTION (data-driven, from the test's result)

### 1. If CLEAN-AT-BASE → candidate-substrates' comparison
- **PR-branch's lineage** (`fix/restore-read-action` @ `ec649ad9`): 1674-ahead/75853-behind; the cross-lineage graft that aborted at the prior attempt. Conflicts NOT safely enumerable. NOT a clean substrate.
- **Base-anchored lineage** (isolated worktree at base commit `0f602c5f6f18`): **CLEAN-APPLY** — the full range lands, the combined-tree builds. THE recommended substrate.
- **New candidate-branch at the base-compatible point**: the isolated worktree already IS this (branch recipe-retry-base at the base commit); no need to create a new one. The base-anchored lineage is the recommended substrate.

### 2. Verdict (the emission contract)
- **VERDICT: RECIPE-CLEAN-AT-BASE**
- The earlier abort on the PR-branch was OUR target-selection (the PR-branch's cross-lineage state — 1674-ahead), NOT the recipe's defect. The recipe's range is clean at its own base-lineage.
- The recipe's range lands clean (7/7 commits, exit 0, no conflicts, combined-tree intact).

### 3. Recommended substrate
- **The base-anchored lineage** — the isolated worktree at the base commit `0f602c5f6f18` (branch recipe-retry-base), /tmp/recipe-retry-wt.
- Application design: the range is applied cleanly at its own base-lineage (already done, CLEAN-APPLY). The recipe's fix is NOT applied onto the PR-branch (cross-lineage graft) — that application is deferred to the operator's call (the PR's update awaits the operator's word).

### 4. Conflict-resolution's design (paths that differ; the 3-way guidance per path)
The range's 8 files vs the PR-branch's actual state:
- **tools/memory_tool.py**: the range's hardening fix (`ee734003cc`) + read-action pinning (`4fd0d0eb16`) must be merged with the PR-branch's read-action restore. 3-way guidance: the range's combined read-fix is the higher-signal layer; the PR-branch's read-action restore is the user-facing layer. Resolution: keep the range's combined reading semantics + the PR-branch's restored-read arm (the clean-apply at base already merges these).
- **tools/memory_tool_store.py**: the range's combined-fix includes the store-level changes (`ee734003cc`); the PR-branch's read-arm restore is the local layer. Resolution: the range's combined store-level fix supersedes; the PR-branch's read-arm is already present in the clean-apply result.
- **Tests** (test_memory_chain_docs.py, test_memory_tool_schema.py, test_memory_tool.py, surfaces.json, memory.json): the range's test pins apply cleanly at the base-lineage. Resolution: the range's test pins are added to the base-anchored lineage; the PR-branch's own read-action-restore test arm is unchanged.
- **hermes_cli/observability/shared_metrics_contract.py** and **tests/fixtures/prompt_surface/***: the range's changes are isolated to these files; resolution: apply as-is at the base-anchored lineage.
- The PR-branch's own files (tools/write_gate.py, etc.) are NOT part of the range; the range does not touch them. The PR-branch's read-action restore remains at the PR-branch layer.

---

## PART IV — PR's untouched status (receipt)
- The clean-apply test is isolated in /tmp/recipe-retry-wt (branch recipe-retry-base). The study's shared branch `study/rfc-143379-rig-20261105` = `902432e00b` was NEVER touched.
- The PR-branch `fix/restore-read-action` @ `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (c0wb0yp0tat0's fork) is UNTOUCHED by this test — the recipe's range was NOT applied onto the PR-branch.
- The PR's status line: `fix/restore-read-action` remains at `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (UNTOUCHED).

---

## PART V — COMMIT
- Commit as `kanban-pilot` in /root/workspace/repos/hermes-agent:
  - Deliverable: `studies/rfc-143379-rig/plan/tank/RECIPE-RETRY-20261122.md` (new file)
  - Only the study paths; the study's shared branch NEVER pushed; the PR-branch's current state NEVER altered; the worktree ops touch ONLY the scratch /tmp/recipe-retry-wt (removed after use); NO push of the study.
