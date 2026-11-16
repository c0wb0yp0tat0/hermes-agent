# M1.5 BORROWED-TRY brief — the Serena PoC's actual try + re-read receipt (seat: probe-at-fire; the door-closure leg the map requires before M1.5 is DONE)

**You are M1.5's BORROWED-TRY lane — the two-way-door sprint's betrayed leg** (MISSION-MAP-20261115.md §1.5: "Its own loops: the borrowed try → the re-read receipt → the door closes or holds, reversibly"). Stages 1+2+3 landed the MAP (`SERENA-BEARINGS-20261115.md` @ `2890b0f3b0` — Serena MCP live at 127.0.0.1:24282, the /mcp route, the list/generate/similarity tools), the HARNESS-PLAN (`SERENA-HARNESS-PLAN-20261115.md` — the MCP-executor leg: model proposes, the executor executes with typed postconditions + hash-verified receipts), and the VERIFIER (`SERENA-STAGE3-VERIFIER-20261115.md` @ `bc88203c4f` — the acceptance battery). The TRY itself has NOT run — the door is held open at the design stage. THIS RIDE closes or holds it, honestly.

**The door's contract (from the verifier, inline):** the borrowed integration passes when (1) the postcondition checks verify (each write's typed postcondition, hash-verified receipt), (2) the authority gate holds (authority + source_attribution present; fail-closed on missing authority — the storm's authority-collapse steer: gold metadata cuts unauthorized action 16.9%→0.0%; false authority acted on 98.6%), (3) the re-read receipt lands (after the try, the surface re-read — the bytes verified, never the model's claim). VERDICT: DOOR-CLOSES (measured pass, receipts attached — the ADOPTION stays the chair's) or DOOR-HOLDS (a named FLAG + the alternative — never forced, never theater).

## Grounding (each ONCE; no hunting; ABSENT stays ABSENT + named; a clipped file is never re-read)
1. This brief, twice.
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SERENA-BEARINGS-20261115.md` — the surface map (read ONCE).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SERENA-STAGE3-VERIFIER-20261115.md` — the acceptance battery you execute (read ONCE).

## The honest reality (the head's fresh receipt — DO NOT fake the try)
- The Serena MCP (`127.0.0.1:24282`) is NOT reachable from this lane's harness terminal (the harness is git-only + the study realm). **The try on the LIVE surface is the head's move after your design lands** — DO NOT claim a live call you cannot make. Your deliverable is the TRY-SPEC + the RE-READ-RECEIPT-SPEC that makes the head's live execution deterministic, plus the honest marker that the live bytes are `[UNEXECUTED]` until the head's run.
- The alternative (if the live MCP is down at the head's execution): the HTTP fallback route + the stdio-launch route, both designed, both receipted in the harness-plan.

## What you produce (the deliverable)
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SERENA-BORROWED-TRY-20261115.md`:

1. **THE DOOR VERDICT LINE** — `DOOR-CLOSES` / `DOOR-HOLDS` + the loop-state (`CONTINUE + <the head's live execution>` / `DONE — the door's verdict on record`), receipted.
2. **§1 THE TRY-SPEC (the head's deterministic execution script)** — the exact sequence the head runs against the live MCP: the probes (list → the tool inventory read-back; generate → one bounded generation with a typed postcondition; similarity → one bounded pair), each with its expected receipt shape, the authority marker the executor must attach (`authority: <the surface's named scope>` + `source_attribution: <the call's origin>`), and the fail-closed condition (no authority marker → the write refused, the gate holds).
3. **§2 THE RE-READ-RECEIPT SPEC** — after the try: the surface re-read (the same tools called again, the bytes compared to the try's receipts — hash equality, never the model's claim), the re-read's verdict (MATCH / MISMATCH), and the receipt's landing (the re-read's own record, dated, verifiable).
4. **§3 THE HONEST MARKERS** — `[UNEXECUTED]`: the live MCP's bytes (not reachable from the lane — the head executes); `[ABSENT]`: anything not read; the door's verdict is the DESIGN's verdict until the head's live execution lands — the design is DONE, the door is HELD-OPEN-WITH-A-TRY-SPEC, never silently closed.
5. **§4 THE COMPOSE-CHECK + RECEIPT STAMPS** — every claim tagged `IN-LANE` / `BORROWED <source>` / `HEAD-RECON`; ABSENT named.
6. **THE LOOP-STATE LINE** — the verdict + the head's next move (the live execution at the MCP route, then the re-read), receipted.

## Disciplines (binding)
ONE tool call per round. Skeleton by round 3 (write-first, short). ≤6,000 chars/write, one section per write; the read-gate is the reason to KEEP WRITING. Commit + push ONCE at the END (pull --rebase on rejection; exit 0 only after the commit succeeded). **NEVER claim a live call; the `[UNEXECUTED]` marker is the honesty's receipt. The RFC QUIET; nothing posts. The adoption stays the chair's; the try-spec is the head's deterministic script. No service changes; no `/root/.hermes` writes; no drop/ paths.**
