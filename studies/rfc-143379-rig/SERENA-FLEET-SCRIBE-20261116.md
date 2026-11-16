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

- **The wire (minimal):** at each significant fold, the head (or a scripted cron arm) writes `save_memory {memory_name: rig-fold-<sha>, content: <the receipt's one-line>}` and re-reads it (get_memory → byte-match) — the scribe's row, appended to its own ledger.
- **The door:** all reversible — the memory cells can be renamed/deleted (the family's tools); the wire is a cron arm with NO new dependencies; rollback = remove the arm.
- **The success criterion:** N scribe-rows with 100% re-read byte-match + the last_execution log agreeing — the scribe's proof of the third surface.
- **The "maybe more" (the future line, named not promised):** with the MCP-executor leg wired (the host flag or the stdio-launch route), Serena's LSP family becomes the fleet's code-surface executor — the scribe that can also EDIT. Two steps, each a two-way door: (1) the scribe wire (this offer, dependency-free, doable now); (2) the executor leg (the harness-plan's design, the SDK dependency, gated on the host's transport flag).

## THE HONEST MARKERS
- The scribe surface is VERIFIED (the three probes + the live write's ledger entry).
- The executor/editor line is DESIGNED-but-UNWIRED ([ABSENT]: the mcp SDK rig-side, the host's transport flag, the leg's integration run).
- The adoption is the chair's: the offer stands, the wire is one arm, the re-read is the proof. Nothing posts; the RFC stays QUIET.

**Loop-state line: OFFER-STAGED + the scribe arm's wire ready on the word — the receipt surface is live, the rest is the chair's.**
