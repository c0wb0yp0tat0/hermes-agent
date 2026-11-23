# MATRIX-LEGRUNS-20261123 — the runner-fork-matrix's first leg-runs (pve1/avrea)

*Leg-run receipts for the approved `STAGE-PLAN-FLEETMATRIX-20261123.md` (the 12-leg matrix). Seat: `tencent/hy4-flash:free`, PIN-READ-BACK VERIFIED. Host: pve1 (avrea-parallel), the rig's own unmetered seat. Every row a raw receipt or a NOT-RUN-with-reason; the wall clause governs non-reproductions as QUESTIONS-with-receipts. Nothing public; RFC #143379 / #5320 / #157065 QUIET; no installs; never push; no `checkout --` / `stash` / `rm -rf`; the study paths only.*

## Armament / name-and-refuse

- **Armed:** **think-tank** (the spine — classify → choose → probe → evaluate → adopt-or-park → standardize → verify) + **investigation-documentation** (the peer-reviewable discovery log: receipts raw, seams named, limitations + reproducibility stated).
- **Name-and-refuse (considered, not loaded):** agent-work-review (the plan's second lens — this leg's adversarial re-derivation is done inline from tree bytes, no separate lens loaded) · aces-harness-probes / evaluating-llms-harness / local-llm-serving / llama-cpp / serving-llms-vllm (no install, no serving change) · two-model-reasoning (no offline-reasoner leg) · web-storm / grounded-citations / arxiv (LOCAL receipts only, no field search) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no source edits — the re-scope lives in a throwaway worktree) · systematic-debugging (armed only on a non-reproduction; the wall clause governs) · the creative/design/media families.

## §1 The pins (SHA resolution — tree-first)

| Ref in plan | Plan's label | Resolved object (executed) | Note |
|---|---|---|---|
| study HEAD | `f652b71b4e` | `f652b71b4e…` | the plan's pre-restore pin; current branch HEAD moved to `f32f5ab716…` under concurrent lanes — **not touched by this leg**. Negative-control measured at the plan pin (and re-checked at current HEAD — same surface). |
| pr-139606 | `d1bdb4582c` | `d1bdb4582cd5d16be6a6b486f696f8240c222b96` | local commit; write-gate. |
| pr-141876 | `6609dac951` | `6609dacba951d51cdd880ac1031e546dd7fac289` | **QUESTION-with-receipts, ANSWERED:** the plan's 10-char label `6609dac951` resolves to NO object (`git rev-parse --verify 6609dac951` → fatal). The unique prefix `6609dac` → `6609dacba9…` = branch `pr-141876` = `git ls-remote origin refs/heads/fix/restore-read-action` → `6609dacba9…` (the pushed-truth). Typo'd label, tree-resolved; **no fetch needed** (all three objects local). |
| a9c65dc4 | `a9c65dc43d` | `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | local commit; combined. |

**Pin assertion (AVREA §9.1):** the R-leg worktree's `git rev-parse HEAD` = `6609dacba951d51cdd880ac1031e546dd7fac289` == requested. `git worktree add --detach` (NOT a checkout of any study path); cleaned up after.

## §2 The legs — run, receipts, verdict

### leg:R-read-restore — pr-141876 (`6609dacba9`), pve1 primary — **MEASURED: 4/4 PASS**

- **Run:** isolated worktree `git worktree add --detach /root/.hermes/cache/scratch/matrix-leg-r-read-6609dac 6609dacba9…`; the study's 4-test packet `studies/rfc-143379-rig/tests/test_memory_read.py` lifted via `git show`; run with `PYTHONPATH=. python3 -m unittest -v`.
- **Baseline (packet verbatim @ the ref) — the QUESTION-with-receipts:** `Ran 4 tests in 0.003s` → `FAILED (failures=1, errors=3)` — 4/4 FAIL, the exact N10-predicted call-shape mismatches:
  - `test_read_action_dispatch` → `AttributeError: module 'tools.memory_tool' does not have the attribute 'MEMORY_PATH'`
  - `test_read_returns_entries_and_usage` → `TypeError: MemoryStore.add() missing 1 required positional argument: 'content'`
  - `test_read_is_read_only` → `FileNotFoundError: …/MEMORY.md`
  - `test_read_in_operations_enum` → `AssertionError: 'read' not found in '{}'`
- **Re-scoped per N10's four designed call-site edits** (dispatch → `memory_tool.memory_tool(action='read', target='memory', store=MemoryStore())` with `get_memory_dir` patched; `add("memory", content)` / `read("memory")`; read-only vocab with an existing file; `MEMORY_SCHEMA` for the enum): **`Ran 4 tests in 0.528s` → `OK`** — 4 tests, 4 pass, 0 fail, exit 0. Test names: `test_read_action_dispatch ok` · `test_read_in_operations_enum ok` · `test_read_is_read_only ok` · `test_read_returns_entries_and_usage ok`.
- **Raw-output seam (honest):** the re-scoped run emits two **non-fatal** stderr tracebacks on import (`nemo_relay` missing → "Hermes Relay runtime initialization failed"; "Hermes shared metrics initialization failed" → `RuntimeError: Hermes core Relay runtime is unavailable`). They are environment-initialization noise (no install performed — the hard line holds); the suite still reaches `OK` (exit 0). The chmod-000 failure path is not exercised under root (named N10 seam) — the read-only assertion passes either way.
- **Verdict:** **PASS (4/4)** at the pin, on the N10 re-scope. The restored-read store (:435), dispatch (:261), and schema (:377/:412) are tree-confirmed and executable.

### leg:P-write-gate — pr-139606 (`d1bdb4582c`), pve1 primary — **MEASURED: S7 present**

- **Run:** read-only `git grep -n "verify_post_write(" <ref> -- 'tools/*.py'` across the four refs (no worktree needed — the gate is presence/read-back rows).
- **Receipts (grep-counts):** HEAD **0** · pr-139606 **2** · pr-141876 **0** · a9c65dc4 **0**. pr-139606's two rows: `tools/memory_tool.py:367` (`readback = verify_post_write(store, target, action, old_text, content=content)` — the sole PROD caller) and `tools/write_gate.py:650` (`def verify_post_write(store, target, action, old_text, …)` — the definition). Matches the N2 §2 P53 map exactly.
- **Verdict:** **PASS (S7 present)** at pr-139606 only; absent at the other three (the fork feature-split stands).

### leg:C-chain-docs — a9c65dc4 (`a9c65dc43d`), pve1 parallel (cloud primary) — **MEASURED: present + read surface**

- **Run:** read-only `git cat-file -t` / `git show` / `grep` at the ref (presence + features; the 14-test execution is cloud-primary's receipt — a remainder, §5).
- **Receipts:**
  - chain-docs test file `tests/tools/test_memory_chain_docs.py` — **PRESENT**, blob `7d447366b803a7099c832fc331d453a478c826ec`, **14 `def test_` methods** (uncapped append, orphan reporting, anchor cap, linked-doc race, patch-against-uncapped, doc reader/writer live state, etc.).
  - read surface at the same ref: `MemoryStore.read` (:551), `def add` (:579); read dispatch `return _applied(store.read(target))` (:283); `MEMORY_SCHEMA` (:405) with action enum `["read"]` (:445); `get_memory_dir` (:38). `verify_post_write` count **0**.
- **Verdict:** **PASS (chain-docs + read present together)** at a9c65dc4; write-gate Stage-7 still absent — the fork carries read + chain-docs, not the full combination (F-16 holds).

### leg:H-read-only (negative controls) — study HEAD × every runner — **NOT-RUN WITH REASON (never a failed run)**

- **Fork's own surface, measured at the plan pin `f652b71b4e` (and re-checked at current HEAD `f32f5ab716` — identical):** `_STORE_ACTIONS = {add, replace, remove, patch}` at `tools/memory_tool.py:107` — **no `read` arm**; `def read` count **0**; `verify_post_write` count **0**; `tests/tools/test_memory_chain_docs.py` **ABSENT** (`fatal: path … does not exist`).
- **Receipt:** every runner cell (pve1 / p0tat0 / c0wb0y / cloud) = **NOT-RUN — reason: no read-arm surface at study HEAD** (the fork has nothing for the 4/4 suite to read). Retained as the matrix's honesty surface (§2/§3 of the plan); never promoted to "tests passed", never a failure.
- **Verdict:** **NOT-RUN (correctly held)** — the leg CANNOT carry the data; the record stands.

## §3 The measured rows (fork × runner, this host's column populated)

| Fork | pve1 (this host) | p0tat0 (Linux 241) | c0wb0y (Windows 241) | cloud (matrix) |
|---|---|---|---|---|
| study HEAD `f652b71b4e` | leg:H = **NOT-RUN** (no read arm) | NOT-RUN (same) | NOT-RUN (same) | NOT-RUN (same) |
| pr-139606 `d1bdb4582c` | leg:P = **S7 present** (2 rows, :367/:650) | await (support) | await (support) | await (precision) |
| pr-141876 `6609dacba9` | leg:R = **4/4 PASS** (re-scope, exit 0) | await (support) | await (support) | await (precision) |
| a9c65dc4 `a9c65dc43d` | leg:C = **chain-docs+read present** (blob 7d447366, 14 tests) | await (support) | await (support) | await (primary) |

- **Central gap (F-16) confirmed at the tree:** no single fork carries read-restore + write-gate S7 + chain-docs. pr-139606 = S7 only (and a *broken* read arm — dispatch without `MemoryStore.read`, F-15); pr-141876 = read only; a9c65dc4 = read + chain-docs; study HEAD = none. The full combination remains UNTESTED on any fork.

## §4 The verdict (convergence)

- **The legs are what they are:** on pve1/avrea the three positive legs are measured (R: 4/4 PASS at the pin; P: S7 present at pr-139606; C: chain-docs + read present at a9c65dc4) and the negative-control legs are NOT-RUN-with-reason (study HEAD has no read arm). No cell is a fabricated "all verified".
- **The F-16 gap is load-bearing:** the full combination (read + S7 + chain-docs) is untested on any single fork; continuation = the merged substrate (base-anchored lineage / Finn's #116673) OR the cross-fork matrix — never a claim of a single green fork.
- **Handoff gate:** **CLOSED / GATED, not released** — (i) source-level close PENDING (the legs boarded; merged substrate = the operator's/Finn's seat); (ii) the matrix's legs named, designed, and here first-run; (iii) the remote runners' receipts still outstanding (§5), so cross-runner determinism is UNMEASURED; (iv) chair's-word gates (W2 pre-reg amendment, k-term W2 settlement, budget re-verify, token single-source) NEEDS-THE-CHAIR — never self-gated.
- **Non-reproduction discipline:** the only non-reproductions are (a) the plan's typo'd `6609dac951` label (answered by tree resolution) and (b) the verbatim packet's 4/4 FAIL at the ref (answered by the N10 re-scope → 4/4 PASS). Both carry receipts. Nothing was papered over.

## §5 The remainders — ready-to-dispatch (named, this host holds; the remote runners carry them)

Each is a defined cell of the approved matrix, **ready-to-dispatch** — no new design needed, only a runner receipt. Named for **p0tat0 (Linux 241)** and **c0wb0y (Windows 241)**:

1. **p0tat0 — `leg:R-read-restore` (support):** lift the same 4-test N10-re-scoped packet to `6609dacba9…`; capture `Ran 4 … OK` + the executed-SHA assertion. (The pve1 receipt in §2 is the template.)
2. **c0wb0y — `leg:R-read-restore` (support):** same packet on Windows 241 — the OS-differential receipt (p0tat0/c0wb0y compared) feeds cross-runner determinism.
3. **p0tat0 — `leg:P-write-gate` (support):** the `verify_post_write` read-back at `d1bdb4582c…` (the :367 PROD caller); grep-count receipt + the A3 decision→representation read-side receipt.
4. **c0wb0y — `leg:P-write-gate` (support):** same S7 read-back on Windows 241.
5. **p0tat0 — `leg:C-chain-docs` (support):** execute the 14 chain-docs tests at `a9c65dc43d…` (presence already receipted here) + the read/write race receipt.
6. **c0wb0y — `leg:C-chain-docs` (support):** same on Windows 241.
7. **Cross-runner determinism:** compare the four runners' receipts per leg; the divergence (not a fabricated agreement) is the data (avrea-parallel-verification). **cloud (matrix)** carries leg:C primary + leg:P/R precision — named but self-hosted; the remote windows are p0tat0/c0wb0y above.
8. **The full-combination leg (F-16):** NOT a runner leg — awaits the merged substrate (the operator's/Finn's #116673 seat), not a dispatch. Held GATED.
9. **Negative-control legs at p0tat0/c0wb0y/cloud:** each retains its NOT-RUN-with-reason record (no read arm at study HEAD); no dispatch required, but the grid must keep the row.

## §6 Limitations + reproducibility

- **Limitations:** leg:R's 4/4 PASS is on the N10 re-scope designed in the N2 round, executed for the first time here; the as-is packet FAILS 4/4 (receipted). The chmod-000 failure branch is unexercised under root. Leg:P leg:C are *presence/feature* receipts (read-only tree greps), not battery executions; the 14 chain-docs tests and the write-gate read-back's runtime behavior are cloud/support receipts (§5). No install, no public write, no serving change, no chain append.
- **Reproduce (all local, no install):**
  - `git rev-parse --verify 6609dac` → `6609dacba9…`; `git ls-remote origin refs/heads/fix/restore-read-action` → same.
  - `git worktree add --detach <wt> 6609dacba9…`; `git show HEAD:studies/rfc-143379-rig/tests/test_memory_read.py > <wt>/test_memory_read_baseline.py`; `(cd <wt> && PYTHONPATH=. python3 -m unittest -v test_memory_read_baseline)` → `FAILED (failures=1, errors=3)`.
  - The re-scoped packet (§2) → `Ran 4 tests … OK`, exit 0; `git rev-parse HEAD` in `<wt>` == the pin; `git worktree remove <wt>` after.
  - `git grep -n "verify_post_write(" {HEAD,pr-139606,pr-141876,a9c65dc43d} -- 'tools/*.py'` → `0 / 2 / 0 / 0`.
  - `git cat-file -t a9c65dc43d:tests/tools/test_memory_chain_docs.py` → blob; `git show … | grep -c '^    def test_'` → 14; `git show a9c65dc43d:tools/memory_tool_store.py | grep -n 'def read'` → :551.
  - `git show f652b71b4e:tools/memory_tool.py | sed -n '107,118p'` → add/replace/remove/patch only (no `read`).

*Exit 0 = this file exists on disk with the receipts inside, committed as kanban-pilot on the study path only, then the sha reported. A parse-fragment-only response has NOT landed.* — the runner-fork-matrix's first leg-runs (pve1/avrea column boarded; the remote columns named, ready-to-dispatch).
