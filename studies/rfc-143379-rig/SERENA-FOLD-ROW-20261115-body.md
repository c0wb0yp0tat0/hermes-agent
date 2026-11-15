**[FOLD 2026-11-15 · ~16:20 ET — Nemo's Serena stages 1+2 LANDED: the surface's true map + the harness-leg design; the PoC's blueprint stands]**

**Stage 1 — the bearer (folded at `2890b0f3b0`, the fold-step's commit):** `SERENA-BEARINGS-20261115.md` — all five sections: the true surface (Serena = the semantic MCP server, LSP-symbol-level tools, NO LLM endpoint, stdio-bound today; the 24282 HTTP face is the dashboard; `/mcp` needs the transport flag), the wiring options (harness MCP-executor leg / MCP-client connector / host-side script), the two-way-door plan (config delta + rollback + success/exit criteria), the stage-2 seed, the honest markers.

**Stage 2 — the planner (folded at `0e127105d2`, the fold-step's second live proof):** `SERENA-HARNESS-PLAN-20261115.md` — all five sections: the leg's design (the optional `--executor mcp-serena` leg — a local MCP client to Serena; write-call routing at the harness's `write_file` handler; the default writer stays the default), the receipt floor (the postcondition re-read — success is not a postcondition, the byte-check rides), the two-way door exact (flag + process + tunnel = the delta; drop-three = the rollback; N landings zero-write-failures = success; two failures = the door closes), the test plan (one write-only compose brief through the leg on a live seat), the honest markers (the serena tool-list + LSP coverage unverified, ABSENT-named).

**The orbit:** the PoC scope stands (borrow-as-is, slight tweaks per these findings, the own-build later); the three sprint missions stay first; the wheel's R3 (kenari) stays armed; nothing posts, gates held.

**Next:** stage 3 — the verifier (the design checked against the harness's actual integration points), then the borrowed try.
