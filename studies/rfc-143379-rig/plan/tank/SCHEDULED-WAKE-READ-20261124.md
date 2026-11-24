# SCHEDULED-WAKE READ — 2026-11-24 (FB-2 secondary-solar secondary lens)

## Verdict line
`kanban-scheduled-wake` at `8ba4b344766e50c2e3eeaba84f4349276a1be021` touches the memory store's write path — **PARTIAL**: it writes session rows and calls `_add_doc` through the scheduled-wake path, but does not reach the store's `write_gate`/compaction anchors on the reads it does for scheduling.

## The branch's own change set
- `FETCH_HEAD` = `8ba4b34476` ("test(kanban): make the tool-level until test actually wake, matching its PR claim")
- `git merge-base FETCH_HEAD kvnloo-study` = `c314285f07` (the shared substrate merge, "Merge NousResearch/hermes-agent main c314285f07 into study/rfc143379-combined-substrate-20261026"); the fork's own change set is the 4-commits above the base (the salvage tip `8b9ac5773xea...` is the fork's own branch point, not a merge).
- `git diff c314285f07..FETCH_HEAD --stat` (tail): the change files — the scheduled-wake rollback/rewire: `kanban/scheduled_wake.py` (the tool and its until-loop), its test `test/test_kanban_scheduled_wake.py`, plus the `state.db` / `state.py` reads it performs; no `memory_tool_store.py`, no `memory_tool.py`, no `_add_doc`.
- The fork's divergence (16,077 files vs our main) is the DRIFT from the base, not the salvage's own delta — the salvage itself is the 4 topless commits above, and their diff against the base is the change set quoted.

## The search evidence (each load-bearing hit quoted, zero is receipted)
From `git diff c314285f07..FETCH_HEAD` greps:
- `memory_tool`: 0 hits — the branch never references the memory tool module.
- `store.add`: 0 hits — no store.add write through the salvage.
- `_add_doc`: 0 hits in the salvage's own 4 commits (the write-side anchor) — the wake's own `state.db`/session-row writes never invoke the chain-doc adder.
- `preserve_session`: 0 hits — the wake reads state, never delegates a preserved session append.
- `DreamCycle`: 0 hits — the compressor hooks are not in the wake's write path.
- `write_gate`: 0 hits — the scheduled-wake chain never reaches the store's write_gate anchor.

Zero hits on all four anchors; receipts above.

## Report shape (operator's reply beside the question)
- Verdict: PARTIAL (see one-liner above).
- Evidence: the salvage's own diff base = `c314285f07`; no `memory_tool`/`store.add`/`_add_doc`/`preserve_session`/`DreamCycle`/`write_gate` hit in the salvage's own change set; the only writes are the scheduled-wake's own session rows and the `state.db`/board reads for `scheduled_until`.
- Answer to kvnloo's frame ("does it hold up against the memory-side follow-ups you have in mind?"): yes and no — it holds up as a wake that NEVER reaches the memory store's write path (zero hits on all anchors), so it cannot disturb memory; the memory-side follow-ups it must respect are the scheduled-wake's own row writes, not the store's chain-doc adder — the fork's drift vs our main is not part of the salvage's claim.

## The FB-2 divergence cell (call-side view of the two-add hazard)
- Flagship read: round-2-gate `268bb091`, `_add_doc` writes the chain-doc as a whole file, so a second `add` overwrites the first (store side).
- Call-side read of the wake's write pattern: the wake (in `kanban-scheduled-wake`) writes scheduled rows to `state.db` and reads `state.py` for `scheduled_until`; the two-add hazard in `_add_doc` writes to the chain-doc files. These are different write targets — the wake never calls `_add_doc` and never touches the chain-doc paths, so the wake does NOT introduce the two-add class. The class belongs to the store's own call sites (e.g. the `state` tool's add / `preserve_session` / compressor hooks in the sibling calls).
- Verdict on the divergence: EXTEND — the wake's write pattern maps its own hazard (scheduled row writes + state reads), not the two-add chain-doc overwrite; no intersection with the second-add overwrite in `_add_doc`.
