# NIGHT-654-LEG1 — PRODUCE: the combined-substrate SHA + the parity receipt (2026-10-30)

> **LEG 1 deliverable per the night plan** (`NIGHT-654-PLAN-20261029.md`): locate the real
> combined-substrate head on /root/hermes-agent-pr, verify its tree against f90969ae's five
> hardening files (recomputed — a published hash is a claim), push to a public branch on the
> fork, publish the SHA + the receipt. **Never a fabricated SHA.**
>
> Kanban card: `t_394a38e17b3e4` (NIGHT-654-LEG1-PRODUCE, P1). Task created by the CTO.

## Verdict line

- **Head located:** `995de91d281f6613ae4a77ee43bebf6febef8993` — branch `round2-combined-substrate`
  (worktree `/tmp/kvnloo654-combined`, `git status` clean).
- **Push:** `https://github.com/c0wb0yp0tat0/hermes-agent/tree/round2-combined-substrate` —
  live and read-back verified (push output + `git ls-remote` + GitHub API).
- **Parity (recomputed, byte-for-byte): MISMATCH — NAMED.** None of f90969ae's five hardening
  files is byte-identical to the substrate head's tree. The substrate is the round-2
  develop's own implementation (write_gate overlay + its own read path); it does **not**
  carry jfugalde's f90969ae hardening content.

---

## 1. The combined-substrate head — located

| Field | Value |
|---|---|
| Full SHA | `995de91d281f6613ae4a77ee43bebf6febef8993` |
| Short | `995de91d28` |
| Branch | `round2-combined-substrate` |
| Subject | `round-two combined substrate: af16e3ab16 + 5 fixes + the 297 battery (tests + write_gate overlay)` |
| Author | `c0wb0yp0tat0 <c0wb0yp0tat0@users.noreply.github.com>` |
| Committed | `2026-10-30T00:06:02-04:00` |
| Parent | `af16e3ab16eed2492552c325ad1777533a8b7004` (the restore commit) |
| Workspace | `/tmp/kvnloo654-combined` — branch checked out, working tree clean |

Provenance: the branch is locally managed in the worktree at `/tmp/kvnloo654-combined`,
whose repo is `/root/hermes-agent-pr`. Its parent `af16e3ab16` matches the restore substrate
named in the KVNLOO654-ROUND2 handoff ("fixed substrate (af16e3ab16 + 5 fixes)").

## 2. The public push — verified, not asserted

```
$ git push origin round2-combined-substrate:round2-combined-substrate
 * [new branch]            round2-combined-substrate -> round2-combined-substrate

$ git ls-remote origin refs/heads/round2-combined-substrate
995de91d281f6613ae4a77ee43bebf6febef8993	refs/heads/round2-combined-substrate

$ gh api repos/c0wb0yp0tat0/hermes-agent/branches/round2-combined-substrate
{"name":"round2-combined-substrate","sha":"995de91d281f6613ae4a77ee43bebf6febef8993",
 "protected":false}
```

Branch URL: **https://github.com/c0wb0yp0tat0/hermes-agent/tree/round2-combined-substrate**
Fork: public (`gh repo view → {"isFork":true,"visibility":"PUBLIC"}`), owner `c0wb0yp0tat0`.

The published SHA is the commit's actual object id — read back from the remote after the
push. Nothing fabricated.

## 3. The parity — recomputed byte-for-byte (sha256 of each blob)

Method: `git show <rev>:<path> | sha256sum` — for each of f90969ae's five hardening files
(the set named in the READFIX verification receipt), at the reference commit `f90969aef6`
versus the substrate head `995de91d28`.

| # | Hardening file (path in repo) | f90969ae sha256 | bytes | substrate sha256 | bytes | Parity |
|---|---|---|---|---|---|---|
| 1 | `tools/memory_tool_store.py` | `5779d00cf3d7b683d8a175a8e721bc638ad1f2c92fbbbe980d50c4f15c2114ab` | 45,337 | `89b32c79b140dccb7b4caa8716ff09fcb57d87f93da087209adfd145a71f72e4` | 51,969 | **MISMATCH** |
| 2 | `tools/memory_tool.py` | `f5969419f2632e652bd4f271825a36e4bcb27cc49a1258f0b4ff842f797b1bbb` | 26,616 | `6a0e71fd887424f51432417b3aba313a26ad8cb18a381bf73ae82f3a835ccdf6` | 29,310 | **MISMATCH** |
| 3 | `tests/tools/test_memory_tool.py` | `776fbef289cb233620dc52c950b686214a292c4ad6e71b67a42ba7978e247f53` | 59,261 | `f197f30894964572b0e5993332ce68169b284939bc63b7e00d8eeda5f80cf28a` | 49,129 | **MISMATCH** |
| 4 | `tests/fixtures/prompt_surface/tools/memory.json` | `c255b8982173c51d8d1bb1c92a0d222e1333baee1e22d45d51cd5353f73b29b6` | 3,988 | `980d90b8b190a6c46fd4665f5540ac68f0188b591575513dd19a2c9e11be1f8c` | 3,930 | **MISMATCH** |
| 5 | `tests/fixtures/prompt_surface/surfaces.json` | `9adee57911888f22218d7a96f27b5db339bc08fa552c9f82d86f072f2bf72416` | 5,861 | `5a14ee1d5c2d8fecb76ab9c02ae8cd4c61141768807bf931250de14cd09285ec` | 8,048 | **MISMATCH** |

For completeness, the sixth file changed by f90969ae (`hermes_cli/observability/shared_metrics_contract.py`)
also differs: `a3a0e4fe3767bc8816ca4c633e9fdab6882b4193eea865158e71721cc88af8d2` (102,724 B)
vs `3cf47665da2c186682a414d39cc1acb3b068cc781509f40299ea319a3f46bf59` (102,179 B) — **MISMATCH**.

**Result: 0/5 of the hardening files are byte-identical. The parity does not hold.**

## 4. The mismatch — named

The substrate head `995de91d28` is not jfugalde's hardening applied on the restore. It is the
round-2 combined substrate: `af16e3ab16` + the round-2 develop's own five fixes + the 297-case
battery + the write_gate overlay. Concrete, re-verified differences against `f90969ae`:

1. **No `_sanitize_hints`, no `read_action_failed` metric class, no `_read_action_failed_error`.**
   The substrate's store defines its own `_read_failed_error` (line 63) reporting failure class
   `"read_failed"` (registered in `MEMORY_OP_FAILURE_CLASSES` at
   `shared_metrics_contract.py:271-275`). f90969ae's class is `read_action_failed` (contract L279,
   store `_read_action_failed_error` L93/L418). Different classes, different sentences.
2. **The batch `operations` item enum still contains `read`.**
   Substrate `tools/memory_tool.py` L477: `"action": {"type": "string", "enum": ["add", "patch", "remove", "read"]}`
   — the item-level enum keeps `read`. f90969ae's version (L439) is `["add", "patch", "remove"]`
   (read dropped from the batch enum, kept at the top-level `action` only).
3. **`read()` is a different implementation.** The substrate's `read()` (store L406-425) documents
   "no gate, no drift guard, no write, no shared-cache mutation" and returns raw parsed entries
   + `usage` only — no `blocked` list of masked positions, no sanitized view, and no
   `with self._file_lock(...)` on the read path (no `_file_lock` marker on read; grep shows the
   substrate store's read does not hold it, while f90969ae's read does — f90969ae store grep:
   `_file_lock(path)` x2, `_sanitize_hints` x3, `blocked` list present).
4. **The substrate carries its own test battery and overlay instead of the hardening tests.**
   f90969ae grows `tests/tools/test_memory_tool.py` by +195/-9 (the six hardening tests: blocked
   hint never leaks, batch hint, missing old_text points at read, read failure class, read failure
   not a write refusal, write refusal unchanged). The substrate's `test_memory_tool.py` is
   **smaller** than f90969ae's (49,129 B vs 59,261 B) and the substrate adds its own suites:
   `tools/write_gate.py` (+600 lines, new), `tests/tools/test_write_gate.py` (+103),
   `test_kvnloo654_fix01_cache_coherence.py`..`fix05_fail_closed_gate.py`, consent scenario
   fixtures and RFC homework tests.
5. **Read-failure sentence differs.** Substrate `_read_failed_error` still opens with
   "Refusing to write {path.name}: the file exists on disk but could not be read right now".
   f90969ae's own read-failure sentence starts "Could not read" (per the READFIX verification:
   "A failed read … no longer reports as a write refusal").

Nothing here is a value judgment on which implementation is correct — the receipt's job is
parity. The parity is: **not equal**. If Kevin (or anyone) tests `f90969aef6`'s five files
as a stand-in for the substrate, the result is a test of a **different tree** than
`995de91d28` — the mismatch is now named and reproducible from the table above.

## 5. Honest limits of this receipt

- This receipt verifies **tree parity only** — bytes of five/six files at two commit objects
  in `/root/hermes-agent-pr`. It does not re-run tests, does not judge semantics, and does not
  claim either implementation is defective.
- The SHA published here is real and remote-verified; no SHA in this document was invented.
- The prior READFIX verification (JFUGALDE-READFIX-VERIFICATION-20261025.md) covered the
  separate cherry-picked worktree `9e1bf9563c` (identical to f90969aef6 on the five files).
  That stand-in remains the closest verified stand-in for jfugalde's hardening; it is **not**
  the substrate head's content.

## Evidence commands (all re-runnable)

```
cd /root/hermes-agent-pr
git rev-parse round2-combined-substrate           # 995de91d281f6613ae4a77ee43bebf6febef8993
git show 995de91d28:tools/memory_tool_store.py | sha256sum
git show f90969ae:tools/memory_tool_store.py | sha256sum     # …and so on, per table
git ls-remote origin refs/heads/round2-combined-substrate
```

---

*Written 2026-10-30 by the LEG 1 develop (kanban t_394a38e17b3e4). Cold-readable: every claim
above is backed by a command in the evidence log or the table. PRODUCE EXIT: 0 — parity
mismatch named, SHA published and verified.*
