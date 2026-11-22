# FALSIFIER-AUDIT-20261122 — the gaps × claims matrix (xngg1021's four gaps × the round-two claims)

**Mission:** MISSION-3, the falsifier/gap-audit of RFC #143379's pilot-kit stack.
**Seat:** `meituan/longcat-2.5:free` (PIN-READ-BACK verified at the fire).
**Contract:** `plan/tank/briefs/BRIEF-SPECIAL-MISSION-3-FALSIFIER-AUDIT-20261122.md` (read in full before any action).
**Discipline:** THE TREE IS THE TRUTH — every claim re-derived at the actual tree bytes, never from prose. A claim absent from the tree is a **FINDING**, never a correction. A non-reproduction is a **QUESTION with receipts**.
**Armament:** `think-tank` (spine) + `agent-work-review` + `investigation-documentation` — loaded and used. The rest of the catalog is **named-and-refused** (an unarmed lane is a finding).
**Anchor:** `/root/.hermes/memories/MEMORY.md` + `USER.md` read; GATE LAW's final form — *the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait.*

---

## 0. The tree register (the foundational finding)

The brief's premise is that the study HEAD carries `tools/write_gate.py`, `tools/spa_integration.py`, `tools/dream_cycle.py`. **It does not.** The five named files live on four different trees, and no single tree carries them all:

| File | study HEAD `bef53e1ebd` | battery `30f08c2a0f` | `pr-139606` `d1bdb4582c` | `feat/140005-spa-dream` `ffb85c2c58` |
|---|---|---|---|---|
| `tools/memory_tool.py` | 485 ln, **no `read`**, no `doc` | 569 ln, `read`+guard, no `doc` | 588 ln, `read` **no guard**, `doc` | absent |
| `tools/write_gate.py` | **ABSENT** | 600 ln (verify@557, `_store_entries`) | 713 ln (verify@650, `_disk_entries`) | absent |
| `tools/spa_integration.py` | **ABSENT** | **ABSENT** | absent | 107 ln (the only copy on any ref) |
| `tools/dream_cycle.py` | **ABSENT** | **ABSENT** | absent | 141 ln (the only copy on any ref) |
| `tools/memory_tool_store.py` | 700 ln, **no `read`**, no `bank` | 988 ln, `read`@430, no `bank` | no `read`, no `bank` | 700 ln, **no `bank`** |
| `agent/context_compressor.py` | 5825 ln, 0 dream/spa/preserve/bank | 0 | 0 | 0 |

Tree identities: study HEAD = `bef53e1ebd` (worktree, branch `study/rfc-143379-rig-20261105`; `origin` = `bb3b33c7b7`, local is **19 ahead** — the stale-push hazard is live). Battery = `fixes/falsifier-battery-20261104` = `30f08c2a0f` (== `origin`). `pr-139606` = `d1bdb4582c` (xngg's pin). `feat/140005-spa-dream` = `ffb85c2c58` (xngg's pin). `verify_post_write` is **called from exactly one production site on the whole fork**: `pr-139606:tools/memory_tool.py:366-367`. Every other lineage defines it and never calls it.

**Consequence for the audit:** the round-two claims are claims about the *round-two substrate* (the battery lineage), not about the study HEAD. Both are audited below, and the tree is named per receipt.

---

## 1. The gaps × claims matrix (per-claim receipts)

### G1 — the batch-path bypass

**xngg's gap (at `pr-139606`, `d1bdb4582c`) — CONFIRMED, empirically.**
- `tools/memory_tool.py:331-343`: the non-empty `if operations:` branch returns `_applied(store.apply_batch(target, operations))` directly at `:343`.
- `verify_post_write` is wired **only** on the single-op path at `:366-367`.
- Probe (silent `_write_file` suppression, tool layer): single-op `patch` → `{"success": false, "failure_class": "readback_failed"}` with disk still `Alpha beta gamma`; 1-item `operations=[patch]` → `{"success": true, "message": "Applied 1 operation(s)."}` with disk still `Alpha beta gamma`. **The bypass reproduces exactly as xngg described.**

**The operator's round-two claim — REFUTED.**
- Claim: *"UNREACHABLE on this head. Empty operations are rejected up-front in `MemoryStore._batch` … The guard holds; the bypass class does not reproduce here."*
- The empty-ops guard is **CONFIRMED**: battery `memory_tool_store.py:845-846` → `_error("operations list is empty.", "invalid_args")`; study HEAD `:558` the same; probe returns `{"success": false, "error": "operations list is empty."}`.
- But the guard is **orthogonal** to the bypass: xngg's bypass is a **non-empty** 1-item batch, not an empty one. Probe at the battery branch **and** the study HEAD: `operations=[{"action":"patch",...}]` under a silent lost write → `success: true`, disk unchanged. **The bypass class reproduces at the current tree.**
- Worse, the framing is inverted at those trees: the read-back is unwired on **both** paths (`git grep verify_post_write` → only the def + tests). So it is not a batch-vs-single asymmetry; it is a **tree-wide absence of the read-back attestation**.

### G1b — the three single-op read-back blind spots

**xngg's gaps (at `pr-139606`) — all three CONFIRMED.**
1. `verify_post_write:672-673` — `if action not in ("replace","patch","remove") or not old_text: return None`; `add` is never read back. Probe: `add` → `success: true`, `entry_count: 2`, disk unchanged.
2. `verify_post_write:680-685` — remove attests **whole-entry equality** (`landed = not any(e == old_text for e in entries)`), while `MemoryStore.remove` matches by unique substring; a lost write of `old_text="tea"` passes because no on-disk entry equals `"tea"`.
3. `verify_post_write:687-691` — patch attests **presence-of-new** (`landed = any(content in e for e in entries)`), which a sibling already containing `content` satisfies.

**The operator's round-two claims — CONFIRMED-AS-STATED, REFUTED-AS-CLOSURE.**

| Claim | Store layer (battery) | Read-back layer (battery) | Verdict |
|---|---|---|---|
| add returns a complete terminal dict, not None | CONFIRMED — `_success_response:911-924`; probe: `success/done/target/usage/entry_count/message/note` | `verify_post_write:577` still returns `None` for `add` | **CONFIRMED as stated; NON-OPERATIVE** — the lost add still returns `success` with `entry_count: 2` over a 1-entry disk |
| remove selects by whole-entry exact match first | CONFIRMED — `remove:729` → `_find_unique_match:488-505` (`:490-492` exact first) | `:583` is `any(old_text in e …)` — **substring**, the *inverse* of the claim | CONFIRMED at the store; the read-back seam is a different rule and is **unwired** |
| patch is confined to the matched entry's own span | CONFIRMED — `patch:694` → `_patch_entry:473-486` | `:583`/`:691` presence-of-new, not span-confined | CONFIRMED at the store; the read-back seam is **unwired** |

The operator's three claims are true of `MemoryStore`'s **selection semantics**; xngg's three blind spots were in **`verify_post_write`'s attestation**. The claims do not close the gaps, and at the battery/study trees the attestation is not called at all.

### G2 — the standalone fallback (`doc=` / `action="read"`)

**xngg's gap (at `pr-139606`) — CONFIRMED, empirically.**
- `pr-139606`'s store has **no** `DOC_TARGET_PREFIX`, `doc_name`, or `read`; the `except ImportError` at `memory_tool.py:46-53` therefore sets `doc_name = None`.
- Probe with `doc_name = None`: `memory_tool("read","memory",doc="conventions")` → **`TypeError: 'NoneType' object is not callable`**; `memory_tool("read","memory")` → **`AttributeError: 'MemoryStore' object has no attribute 'read'`**. Both of xngg's deterministic failures reproduce.

**The prior verification's row is a MISREAD — a finding.**
`XNGG-GAPS-VERIFICATION-20261105.md` row 2 records this gap as *"NOT REPRODUCED at this pin — the guard IS present: `if name is None: return …`"*. The guard at `:283` checks the **result** of `doc_name(doc)`; it does **not** check whether `doc_name` is callable. The `TypeError` fires *before* the guard is reachable. The prior row is a false refutation — exactly the class this audit exists to catch.

**The operator's round-two claim — SPLIT.**
- *"the read action restored"*: **CONFIRMED on the battery branch** — `memory_tool.py:313-320` has `action == "read"` with a `hasattr(store,"read")` fail-closed guard; `store.read` at `:430`. **REFUTED at the study HEAD** — `_STORE_ACTIONS` (`:107-118`) has no `read`; `_memory_tool` has no `read` branch; `memory_tool_store.py` has no `def read`.
- *"the `doc_name`-None guard"*: the doc chain is **absent**, not guarded, on both the battery and study trees (`memory_tool()` has no `doc` parameter; `grep DOC_TARGET_PREFIX|doc_name|_resolve_target` → empty). The `TypeError` class is unreachable by **removal**, not closed by a guard.

### G3 — `preserve_session` (the ignored return dicts + the dangling pointers)

**xngg's gap (at `feat/140005-spa-dream`) — CONFIRMED.**
- `tools/spa_integration.py:104-107`: `store.add(anchor_target, f"@doc:{doc_name}")` and `store.add(f"doc:{doc_name}", payload)` — **both return dicts dropped**; `return doc_name` unconditionally. Both deterministic failure classes (headroom-exceeded anchor; threat-scanned payload) leave a dangling `@doc:` pointer with no backing file.

**The operator's round-two claim — REFUTED / UNVERIFIABLE-AT-TREE.**
- Claim: *"folded into the fork's fixes on the round-two substrate — the read action restored, the consent deny bound to content origin, the deny-family matched by language class."*
- `preserve_session` exists on **exactly one ref** in the entire fork (`origin/feat/140005-spa-dream`). No branch carries a return-checked version; no branch carries the function at all on the round-two substrate.
- The three named fixes do not touch this seam. The dangling-pointer classes remain open: the anchor-first-then-payload ordering means a refused payload leaves the anchor, and the battery's `_anchor_gate`/`_add_doc` validate the **reverse** direction (a doc with no anchor), not an anchor with no doc.

### G4 — `DreamCycle.deep_sleep` `.bank()` + the compressor hook

**xngg's gap (at `feat/140005-spa-dream`) — CONFIRMED.**
- `tools/dream_cycle.py:122` — `self.store.bank(c)`, after `:119-120` has already set `c.state = "promoted"`.
- **No `MemoryStore.bank` exists on any ref.** The only `def bank` in the fork is a `FakeStore` in `tests/tools/test_dream_cycle.py:21`. `dream_cycle.py` itself exists on one ref only.

**The operator's round-two claim — REFUTED.**
- Claim: *"landed as the origin-bound provenance seam."*
- `agent/context_compressor.py` contains **0** occurrences of `dream`/`spa`/`preserve_session`/`should_preserve`/`bank` on **every** branch probed (study HEAD, battery, `feat/140005-spa-dream`). The compressor hook did not land. No `.bank()` adapter exists. The seam has **no landing site on any tree**.

### G0 — the falsifier battery's own state

- **"21 tests across the six nuggets" — NON-REPRODUCING.** `def test_` counts across the branch's history: **20** (`e366d9f8e5`), **23** (`5077bb3e`, the strengthened RED-proof the operator names), 24, 25, 27, **29** (`30f08c2a0f`, the HEAD). **21 matches no commit.** The figure appears once in the study, in the operator's own sentence (reproduced at `CYCLES/RFC-143379-RECORD-20261111.md:669`) — unsourced. (Count-rule drift: the counting rule must be quoted before the number is used.)
- **The orphan-edge RED-state — STALE.** At the HEAD the battery runs **28 passed, 1 xpassed, 0 failed, 0 skipped** (real `pytest` run, `fixes/falsifier-battery-20261104`). `test_nugget6_strengthened.py`'s two mutated-case tests **PASS**, and the pre-fix `xfail` in `test_nugget6_substring_orphan.py` **XPASSes**. RED was true at `5077bb3e`; the whole-anchor resolution landed at **`a996d4ad30`** (2026-11-05 01:58 EST), an **ancestor of the HEAD**.
- **"the GREEN-flip is armed but not landed" — was true at the comment's time, is false now.** The operator's comment `6651356150` was created **2026-11-05T06:26:00Z**; `a996d4ad30` is **06:58:20Z** — ~32 minutes later. The claim is a **timestamp-bound** statement that the tree has since overtaken.
- The battery's own `nugget1` falsifier is the empty-ops rejection — i.e. the battery's named falsifier for "the batch-path bypass" does **not exercise the bypass** (see the strongest catch).

---

## 2. The verdicts

**Per claim (round-two substrate):**

| # | Claim | Verdict | Receipt |
|---|---|---|---|
| G1 | batch-path bypass UNREACHABLE; empty-ops guard holds | **REFUTED** (guard CONFIRMED, orthogonality REFUTED) | probe: 1-item batch lost-write → `success`, disk unchanged, at battery *and* study HEAD |
| G1b-1 | add returns a complete terminal dict, not None | **CONFIRMED-AS-STATED / NON-OPERATIVE** | `_success_response:911-924`; lost add still `success` |
| G1b-2 | remove whole-entry exact first | **CONFIRMED** at store; read-back seam is substring + unwired | `remove:729`→`_find_unique_match:490`; `verify:583` |
| G1b-3 | patch span-confined | **CONFIRMED** at store; read-back seam unwired | `patch:694`→`_patch_entry:473`; `verify:583` |
| G2 | read action restored; `doc_name` guard | **SPLIT** — read CONFIRMED on battery, **ABSENT at study HEAD**; doc chain removed, not guarded | battery `:313-320`, `:430`; study HEAD no `read` |
| G3 | preserve_session folded into the fork's fixes | **REFUTED / UNVERIFIABLE-AT-TREE** | one ref only; no return-check anywhere |
| G4 | `.bank()` adapter + compressor wiring landed | **REFUTED** | no `MemoryStore.bank`; compressor wiring 0 on every branch |
| G0 | 21 tests; orphan RED; GREEN-flip armed-not-landed | **NON-REPRODUCING / STALE** | 29 tests; 28 passed + 1 xpassed; `a996d4ad30` is an ancestor |

**Aggregate (one line per gap):**
- **G1 — REFUTED:** the batch bypass reproduces at the current tree; the named guard is orthogonal and the read-back is unwired on both paths.
- **G1b — CONFIRMED-AS-STATED, NOT CLOSED:** the store-layer selection semantics are as claimed; the read-back attestation they were meant to close is a different rule and is not called.
- **G2 — CONFIRMED at the pin; the operator's fix reproduces only on the battery branch and is ABSENT at the study HEAD; the prior verification's refutation was a misread of the guard.**
- **G3 — REFUTED:** no fixed `preserve_session` exists on any tree; the dangling-pointer classes are open.
- **G4 — REFUTED:** no `.bank()` adapter and no compressor wiring on any tree.
- **G0 — STALE:** 29 tests (not 21), GREEN at the HEAD (not RED), the GREEN-flip landed at `a996d4ad30`.

**The strongest catch:** the headline round-two claim — *"the bypass class does not reproduce here"* — **does not reproduce**. The non-empty 1-item batch's lost-write false-success reproduces at the study HEAD and the battery branch, and the read-back that would catch it (`verify_post_write`) is **defined but never called** on either. The guard the operator names (empty operations) is real and orthogonal; the battery's own `nugget1` falsifier tests that same orthogonal guard, so the battery's named arm for this gap does not exercise the gap.

---

## 3. The fix-briefs (designs, never patches — the plan and sealed artifacts are unaltered)

Falsifier-first: each brief names **the test that would have caught it**, **the guard's shape**, and **the landing-site**. None of these is applied.

**FB-1 — the batch read-back (closes G1).**
- *Falsifier:* inject a silent `_write_file` loss; assert `operations=[{patch}]` returns a non-success (or a disk-attestation) — the exact probe run here, promoted to a test.
- *Guard shape:* after `apply_batch`, re-read the target from disk and assert each op's effect; or wire `verify_post_write` into the batch branch, mirroring `pr-139606:memory_tool.py:366-367`.
- *Landing-site:* `tools/memory_tool.py` batch branch (`:337` battery / `:270` study HEAD), or `MemoryStore._batch`.

**FB-2 — the add read-back (closes G1b-1).**
- *Falsifier:* under an injected loss, assert `add`'s `entry_count` equals the on-disk entry count.
- *Guard shape:* the read-back attestation, not the terminal dict's shape.
- *Landing-site:* the same seam as FB-1.

**FB-3 — the remove/patch attestation rules (closes G1b-2/3).**
- *Falsifier:* remove → whole-entry eradication of the located entry; patch → positive presence of the new span **within the matched entry**, never a sibling.
- *Guard shape:* the `pr-139606` form (`_disk_entries`, `:680-691`).
- *Landing-site:* `tools/write_gate.py:verify_post_write` + its wiring.

**FB-4 — the `doc_name`-None guard (closes G2).**
- *Falsifier:* set `doc_name = None`; assert a clean `invalid_args`-style error, not `TypeError`.
- *Guard shape:* `if doc_name is None: return target, ("doc-chain unavailable in this store configuration.", …)` **before** the call; keep the existing `hasattr(store,"read")` guard.
- *Landing-site:* `tools/memory_tool.py:_resolve_target` (`pr-139606:272-286`).

**FB-5 — `preserve_session` atomicity (closes G3).**
- *Falsifier:* assert anchor+payload are both-or-neither, and that the return is `None` when either `store.add` refuses.
- *Guard shape:* check both return dicts; on payload refusal, roll back the anchor (or write the payload first, then the anchor).
- *Landing-site:* `tools/spa_integration.py:preserve_session` (`:104-107`).

**FB-6 — the `.bank()` adapter (closes G4).**
- *Falsifier:* run `DreamCycle.deep_sleep` against a real `MemoryStore` with a candidate over `PROMOTE_FLOOR`; assert no `AttributeError` and that the promotion lands.
- *Guard shape:* a `MemoryStore.bank(candidate)` adapter (or route promotions through `store.add`).
- *Landing-site:* `tools/memory_tool_store.py` + `tools/dream_cycle.py:122`.

**FB-7 — the compressor hook (closes G4).**
- *Falsifier:* assert `compress` calls `should_preserve`/`preserve_session` **before** the lossy path.
- *Guard shape:* the SPA trigger ahead of summarisation.
- *Landing-site:* `agent/context_compressor.py::compress`.

**FB-8 — the battery's own count/branch pin (closes G0).**
* Falsifier: a test that pins the branch SHA and the test count, and quotes the counting rule.
* Guard shape: the RED-proof's substrate `skip` must be reported as a skip, never silently as a pass.
* Landing-site:* `tests/falsifier-battery/` + the run receipt.

---

## 4. Limitations + reproducibility

- **Read via:** `read_file` on the local worktrees; `git show`/`git grep` on local refs; `gh api` **read-only** for the two comment rows (the RFC upstream was not written to). No `web_extract`; no installs; no pushes; no `checkout`/`stash`/`rm`.
- **Probes (re-runnable):** `/root/.hermes/cache/scratch/m3_probe.py` (store layer), `m3_probe_tool.py` (tool layer), `m3_probe_oserror.py` (OSError-raising variant). Each takes the target tree as `argv[1]`. The `pr-139606` tree was materialised read-only into the scratch dir via `git archive`.
- **Battery run:** `python3 -m pytest tests/falsifier-battery/ -p no:cacheprovider -q` in `fixes/falsifier-battery-20261104` → `28 passed, 1 xpassed`.
- **Withheld / not probed:** the dynamic behaviour of the compressor hook (no tree carries it); the `feat/140005-spa-dream` runtime (its `MemoryStore` has no `read`); the four-PR composition as a single tree (it does not exist — xngg simulated it, and no branch is that composition).
- **Causation note:** the operator's "armed but not landed" was **true at 06:26Z and false by 06:58Z**. That is a verified timeline; the reason the comment went out before the fix is **UNKNOWN** and is not asserted.

## 5. The register

- The round-two substrate's claims are a **mixed bag**: the store-layer semantics claims reproduce; the closure claims for the read-back seams do not; the spa/dream seams have **no landing site on any branch**; the battery's "21 tests / armed-but-unlanded" state is **stale at the current HEAD**.
- The falsifier applies to every contributor, including our own prior verification: `XNGG-GAPS-VERIFICATION-20261105.md` row 2 is a **false refutation** (the `if name is None` guard does not guard `doc_name is None`).
- Nothing in the plan or the sealed artifacts was altered. The fix-briefs above are **designs**.
