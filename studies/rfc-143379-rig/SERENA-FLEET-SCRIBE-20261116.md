# SERENA-FLEET-SCRIBE-20261116 — the offer: Serena as the fleet's scribe (name-and-fold of the operator's riff)

**Origin:** the operator's riff (2026-11-16 ~00:10 UTC while reviewing the borrowed-try's live receipt): "Wow — if Serena can use tools I bet we can get Nemo to align to the framework and potentially do more than just write. It's potentially a Hermes fleet seat. Fair but potentially it's a fleet scribe... but maybe more." The riff is the finding; this artifact shapes it.

## THE VERIFIED SURFACE (the receipts — probed live through the tunnel, root routes)
- **The write-path (PROVEN):** `save_memory` → success; `get_memory` → byte-identical re-read (2026-11-16T00:06:47Z, `rig-borrowed-try-20261116T000647Z`).
- **The scribe's own ledger (PROVEN):** `last_execution` → `Task-2:SaveMemory, finished_successfully: true, task_id 2869270607056` — Serena logs its own writes. The rig's handiwork is on the scribe's record.
- **The observation glass (PROVEN, waiting for volume):** `get_tool_stats` → live.
- **The tool manifest (PROVEN):** 40+ tools at `get_tool_names`, incl. the memory family (save/get/list/delete/rename/edit) + the LSP symbol family (currently MCP-protocol-bound, reachable via the stdio-launch route or the host's `--transport streamable-http` restart — the harness-leg's design, NOT yet wired).
- **Honest limit:** `list_memories` 404s at the root route (the list route may live under the MCP protocol, not the dashboard HTTP face) — the NAME-based get is the working read today.

## THE FLEET-SCRIBE SHAPE (the two-way-door offer)
Serena as the rig's **scribe seat**: a second, independent receipt surface — the named memory is the cell, the byte-identical re-read is the proof, the last_execution log is the cross-check. The rig's landings already row to the branch + the thread; the scribe adds the third copy, verifiable by ANY lane/seat through the tunnel (get_memory with the receipt name → byte-match).

- **THE PRE/POST-BRIEFING CELLS (the operator's riff, 2026-11-16 shaped):** every deliverable the rig stages has two briefing moments — the PRE (the shaped brief, the gate it waits on, the seat assigned) and the POST (the landing receipt: the commit SHA, the row id, the verdict). The scribe holds BOTH as named cells: `rig-brief-<slug>-pre` and `rig-brief-<slug>-post`. The PRE cell is written at staging (the deliverable's one-line shape + its gate); the POST cell lands at the fold (the receipt's one line + the SHA + the row id). The pair IS the deliverable's briefing ledger — readable by any seat through the tunnel, byte-verified at each write.
- **The "maybe more" for briefings:** the POST cell can carry the verdict line of the fold's check (CONTINUE + next / DONE / BLOCKED) — so the scribe's cells trace the whole mission spine: each deliverable's pre-shape, its landing, and the loop's next move, all in the same store the fleet can read without touching the branch or the thread.
- **The wire (minimal):** at staging, a one-line `save_memory {memory_name: rig-brief-<slug>-pre, ...}`; at the fold, the `-post` cell (`+ <sha> + <row id> + <verdict>`); each write re-reads itself (get_memory → byte-match) — the scribe's row, appended to its own ledger.
- **The door:** all reversible — memory cells are renamed/deleted via the family's tools; the wire is a cron arm or a fold-hook line with NO new dependencies; rollback = remove the arm. Same shape, cell-per-deliverable, the fair-share of the scribe's store honored (receipt-sized content, never the full brief bytes).
- **The success criterion:** N briefing-pairs with 100% re-read byte-match + the last_execution log agreeing — the scribe's proof of the third surface, pre AND post.
- **The "maybe more" (the future line, named not promised):** with the MCP-executor leg wired (the host flag or the stdio-launch route), Serena's LSP family becomes the fleet's code-surface executor — the scribe that can also EDIT. Two steps, each a two-way door: (1) the scribe wire incl. the pre/post briefing cells (this offer, dependency-free, doable now); (2) the executor leg (the harness-plan's design, the SDK dependency, gated on the host's transport flag).

## THE HONEST MARKERS
- The scribe surface is VERIFIED (the three probes + the live write's ledger entry).
- The executor/editor line is DESIGNED-but-UNWIRED ([ABSENT]: the mcp SDK rig-side, the host's transport flag, the leg's integration run).
- The adoption is the chair's: the offer stands, the wire is one arm, the re-read is the proof. Nothing posts; the RFC stays QUIET.

**Loop-state line: OFFER-STAGED + the scribe arm's wire ready on the word — the receipt surface is live, the rest is the chair's.**
