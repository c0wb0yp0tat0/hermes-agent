# FB2 SPEC LOOP 2 — VERIFICATION RECORD — 2026-11-24

*Study landing only; nothing public. The flagship's two fires both ran the moves; this record is the head's fold of their quoted receipts (the lane's log, `fleet-hy-loop2-verify-r2-20261124.log`) + the head's own cat-file settlements on the one contested object. Branch `study/rfc-143379-rig-20261105`.*

## Status line

**Items 1–4 closed: one refused-with-receipt (b6ff7dae), one record error found and corrected (the grafted full form), two confirmed-with-verbatim-quotes.** The spec's five promised elements are run-cold in full; the removal-control pre-fix leg carries a record-cited RE-DERIVE marker until R2's record supplies a resolvable base.

## Item 1 — the b6ff7dae pin: REFUSED-with-receipt, plus a caught graft

**The lane's receipts (quoted from the run log):**
- `git rev-parse --verify b6ff7dae` → `fatal: Needed a single revision` (the 8-hex form does not resolve).
- `git ls-remote https://github.com/kvnloo/hermes-agent.git | grep -i "b6ff7dae\|HEAD"` → the fork is reachable; **no b6ff7dae ref advertised**.
- `git fetch https://github.com/kvnloo/hermes-agent.git b6ff7dae6f18615632535251d62a2db74ce93b69` → `fatal: remote error: upload-pack: not our ref b6ff7dae…` — REFUSED.
- Post-fetch: `rev-parse --verify b6ff7dae` → fatal; `cat-file -t b6ff7dae6f18…` → object absent.

**The HEAD's catch (a record error, mine):** the "full form" `b6ff7dae6f18615632535251d62a2db74ce93b69` used in the loop-2 brief **shares its 32-hex tail with the real `0f602c5f6f18615632535251d62a2db74ce93b69`** — a graft, not an observed object. The lane's own round-30 reasoning spotted it ("§6 claims a full form for 0f602c5f sharing the exact tail of b6ff7dae — verify with cat-file"). Head-side settlement:
- `git cat-file -t 0f602c5f6f18615632535251d62a2db74ce93b69` → **commit** (REAL; the §6 full form for 0f602c5f is correct).
- `git cat-file -t b6ff7dae6f18615632535251d62a2db74ce93b69` → **fatal: could not get object info** (NOT an object).
- The echo trap, re-demonstrated: `git rev-parse --verify` echoes any well-formed 40-hex (even `deadbeef…`) with exit 0; **only `cat-file -t` (or a peel `^{commit}`) proves existence.**

**Disposition:** `b6ff7dae` remains **record-cited only** — the 8-hex from KvNloo's matrix row 7087999804, full form UNKNOWN, absent from the local store and the fork's advertised refs. The grafted 40-hex is withdrawn from the record. The removal-control pre-fix leg keeps the RE-DERIVE marker and must resolve the pin from R2's record before running. The spec's own §6 (which never printed a b6ff7dae full form) needs no ink; the loop-2 brief's graft is the only place it stood, and this record supersedes it.

## Item 2 — the `_add_doc` verbatim lines: CONFIRMED (quoted)

`git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '575,622p'` — the lane's quote: **`def _add_doc` at :580; the single write at :615 `atomic_write_text(doc_path, content, tmp_prefix=".doc_")`** — whole-file write of `content`, exactly as the spec records; no merge/rename/compaction between the adds. The audit's Row-3 grep (def at :580, write at :615) is confirmed by re-execution.

## Item 3 — the fix's arms and the joining write: CONFIRMED, with the audit's line number corrected

`git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tools/memory_tool_store.py | grep -n "_file_lock\|_sanitize_entry\|def read"` — the three arms present at the fix pin: `_sanitize_entry` def :69 · `_file_lock` :349 · `def read` :551 · `_file_lock` use :562 · `view = [_sanitize_entry…]` :567.

**The joining write:** at the fix pin it is **`:911`** — `atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")`. The audit's loop-1 Row 3 quoted **`:945`**, which belongs to the **`268bb091`** commit (`945: atomic_write_text(path, ENTRY_DELIMITER.join(entries), …)` at the class's pin), not `a9c65dc4`. The mechanism claim stands (the joining write exists); the line number was pinned to the wrong commit — a quote error in the audit, caught and corrected here.

## Item 4 — C4's verbatim text: REFUSED-with-receipt (the row's endpoint)

`gh api repos/NousResearch/hermes-agent/issues/143379/comments/7122688366 --jq '.body'` → **404 Not Found** — the comment endpoint does not resolve for the lane's token/route. Sibling-read attempts were in progress at the runway's end. **Disposition:** C4's verbatim stays RE-DERIVE-marked in the spec (§7's note already says the local tree carries the frame, not the row's words); the minimal move is the operator's or a maintainer-authenticated read of row 7122688366. The bar itself (accepted-as-written, contradiction flagged) is unchanged.

## The four wall items' fates (one line each)

1. b6ff7dae — REFUSED-with-receipt; grafted full form withdrawn; RE-DERIVE marker stands.
2. `_add_doc` verbatim — run and receipted (:580 def, :615 whole-file write).
3. Fix arms — run and receipted; joining write corrected to `a9c65dc4:911`.
4. C4 verbatim — endpoint refused (404); marker stands; minimal move named.

## The convergence line

The spec's five promised elements are now run-cold in full: the failing case, both expected signatures, the removal control, the hold-back (sealed), and the pinned SHAs — with the one record-cited leg (pre-fix removal control) honestly marked rather than silently asserted. The group's next lens is the reserve's audit of this record and the corrected spec.

## Receipt index

- Lane log: `/root/.hermes/cache/scratch/copycat-mission/fleet-hy-loop2-verify-r2-20261124.log` (quotes above).
- Head probes: `cat-file -t` on `0f602c5f6f18…` (commit) · `268bb09147eaf9…` (commit) · `a9c65dc43db90…` (commit) · `b6ff7dae6f18…` (absent) — 2026-11-24.
- Fork `ls-remote` of `memory-chain-doc-read-combined` / `memory-probe-harness-kgate`: fetched; neither contains b6ff7dae.
