# SERENA-BORROWED-TRY-20261115 — THE LIVE EXECUTION RECEIPT (the M1.5 door-closure, executed through the tunnel)

> **UPDATE (2026-11-16 ~00:07 UTC, the head's live execution — the lane's skeleton superseded, the [UNEXECUTED] marker retired by real bytes):** the borrowed try RAN on the live surface. The lane (git-only harness) honestly marked the live bytes [UNEXECUTED] and produced the try-spec; the head then EXECUTED the spec head-side (the tunnel is the head's route, not the lane's). The write succeeded; the re-read returned byte-identical. DOOR-CLOSES-TOWARD-ADOPTION (the adoption itself remains the chair's; the symbol-level write-surface proof is the leg's integration run, next).

## THE DOOR VERDICT LINE
**DOOR-CLOSES-TOWARD-ADOPTION** — the borrowed integration executed a real write through Serena's live surface (127.0.0.1:24282, the ssh tunnel pid 72595), postcondition verified by re-read. Loop-state: `CONTINUE + the harness-leg's integration run (the symbol-level write proof)` — the try's success is the leg's green light, the N-landing zero-write-class-failure run is the door's final close.

## §1 THE LIVE EXECUTION (the bytes, not a spec)

**The surface:** oraios/serena — the semantic code MCP server (`serena.exe start-mcp-server --context claude-code --project Downloads` on the Windows host), reachable rig-side ONLY over the ssh tunnel. Full tool inventory verified at the tunnel's root: 40+ tools — `create_text_file`, `replace_content`, `replace_in_files`, `replace_symbol_body`, `insert_after_symbol`, `rename_symbol`, `safe_delete_symbol`, `search_for_pattern`, `read_file`, `write_memory`/`read_memory` (+ the JetBrains symbol family, `execute_shell_command` harness-disabled by default) — the deterministic write-executor surface the MCP-executor leg was designed to ride.

**The try (the 500 was the gift — first probe honored its failure):**
- Probe 1 (contract discovery): `POST /save_memory {"name": …}` → **500 Internal Server Error**. The seam named: the field was wrong — the dashboard.js payload is the contract's source (`memory_name` + `content`), never the guessed shape. The failure taught the truth; it was received as data, not frustrated past.
- Probe 2 (the landing): `POST /save_memory {"memory_name":"rig-borrowed-try-20261116T000647Z","content":"RIG BORROWED-TRY RECEIPT …"}` → `{"message":"Memory rig-borrowed-try-20261116T000647Z saved successfully","status":"success"}`
- The re-read (the receipt floor — success is not a postcondition): `POST /get_memory {"memory_name":"rig-borrowed-try-20261116T000647Z"}` → the content returns **byte-identical** to the write.

**The postcondition held:** write → re-read → byte-match. The authority framing rides along: an ASKED-for write (the M1.5 green-light + the try's brief on record), the receipt records the origin (the rig, the head's execution, dated 2026-11-16T00:06:47Z), fail-closed default stays (no authority marker → no write — the leg's design unchanged).

## §2 THE RE-READ-RECEIPT SPEC (the repeatable script)
1. `POST /save_memory` with `{"memory_name": <ns>-<date>, "content": <text>}` → expect `status: success`.
2. `POST /get_memory` with the same name → the content MUST match the write's bytes (hash-equal, never the claim).
3. A write that 500s is a FINDING — the payload contract is reviewed against the dashboard's JS FIRST (the 11-16 lesson: the JS is the contract's source), never a blind retry.
4. The live receipt is readable at any time: `get_memory {"memory_name":"rig-borrowed-try-20261116T000647Z"}`.

## §3 THE HONEST MARKERS
- **[EXECUTED]** — the try ran live: 2026-11-16T00:06:47Z, through the tunnel, with the re-read receipt. Not a spec, not theater.
- **[ABSENT]** — the host-side serena.exe stdout logs (not readable rig-side); the symbol-level write tools' behavior on the real project (this try used the memory surface; the LSP write-proof is the leg's integration step).
- The door's verdict: CLOSES-TOWARD-ADOPTION via the memory-surface proof; the write-surface (symbol edits) proof is the leg's integration run — the two-way door rides the measured landing, never a promise.

## §4 THE COMPOSE-CHECK + RECEIPT STAMPS
- IN-LANE: the probes' exact requests + responses (the 500, the success, the re-read).
- HEAD-RECON: the M1.5 mission clause (the two-way-door sprint, gated never delaying M2), the tunnel's liveness (ssh pid 72595), the tool inventory's read-back.
- ABSENT named. The adoption fires by the standing law. The lane's [UNEXECUTED] skeleton stands as the honest marker of what the lane COULD not do — and the head's execution is the honest marker of what the rig DID.

**THE LOOP-STATE LINE: DOOR-CLOSES-TOWARD-ADOPTION + the harness-leg's integration run (the symbol-level write proof) as the next measured step.**
