# FLEET-BRIEF SECONDARY-SOLAR LOOP 2 — the wake verdict re-derived cold

*Seat (pin): `upstage/solar-mini4:free` — the SECONDARY (operator-designated 2026-11-24). The operator's word: "Reloop a few times to be sure." This is the second circuit: re-derive the loop-1 verdict (`SCHEDULED-WAKE-READ-20261124.md`, commit `19d1bd90b6`) from the tree COLD — no carryover trust, everything re-run. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission (traced to the operator's words)

The pair judges on convergence. Loop 1 said: **PARTIAL** — the wake reads `state.db`/`state.py` and writes its own session rows, but zero hits on every memory-store anchor. Convergence demands that verdict be re-derived by a fresh pass, not remembered. THIS lap re-runs every command the verdict rests on and checks the loop-1 artifact's own residues.

## The re-derivation moves (run each; the results ARE the artifact)

1. **The tip.** `git log --oneline FETCH_HEAD -3` — confirm the branch read is `8ba4b34476` ("test(kanban): make the tool-level until test actually wake…"), the same tip loop 1 read. If FETCH_HEAD moved, state the new tip and re-run everything against it.
2. **The merge-base choice.** Loop 1 chose `c314285f07` as the salvage's own base and treated the 4 topless commits as the change set. Re-derive: `git merge-base FETCH_HEAD origin/main` (or the fork's main if `origin/main` is unavailable locally) — if the merge-base resolves to a DIFFERENT commit, name the divergence and pick the conservative (older) base with a one-line why. `git rev-parse --verify c314285f07` first — if it does not resolve, the loop-1 base is itself a RE-DERIVE item; resolve it or state the old-base claim as record-cited only.
3. **The greps (the verdict's load-bearing receipts).** From the chosen base: `git diff <base>..FETCH_HEAD | grep -n "memory_tool\|store.add\|_add_doc\|preserve_session\|DreamCycle\|write_gate"` — each hit quoted with its line; ZERO hits is a receipted zero (quote the grep's emptiness with the command, never assert it). The verdict's anchors: does the wake's own diff touch `tools/memory_tool_store.py`, `tools/memory_tool.py`, or the `_add_doc` path? No = the verdict stands.
4. **The PARTIAL's own claims.** Loop 1 says the wake "writes its own session rows" — find that write IN THE DIFF (the `state.db` / session-row code it cites) and quote it. A claim without its quoted line is a residue this lap catches.
5. **The loop-1 artifact's residue scan.** Read `SCHEDULED-WAKE-READ-20261124.md` in full (31 lines). Any phrase softer or harder than its receipt? Verdict-line vs evidence mismatches? Name each with the byte-level receipt — or state "no residues found, full read" — never a blanket without the read.

## The required artifact — the loop-2 verification record

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/WAKE-READ-LOOP2-VERIFY-20261124.md`

1. **The verdict line** — PARTIAL stands / PARTIAL amended / NEW verdict, with the one-sentence why.
2. **The re-derived receipts** — tip, base choice, each grep's output head (or its named emptiness), the session-row write's quoted line.
3. **The residue rows** — loop-1 phrases found softer/harder than their receipts (or the clean statement, with the full-read receipt).
4. **The convergence line** — one sentence: is the answer to the thread's question ("does the scheduled-wake salvage touch the memory store's write path?") now converged? What, if anything, still waits?

## Write-window

`write-window: 8` — the commands are five; the record's skeleton by round 8, deepened after.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows.
- No installs. All reads LOCAL (git / read_file). `git fetch` only if a needed ref is absent (the target branch is already local at FETCH_HEAD; prefer the local ref).
- `git add` + `git commit` locally with the study identity — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only).
- Never `git checkout --`, never `git stash`, never `git rm -rf`. The master's append-only. `ls-remote` first, per fold — the branch is shared.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words — the artifact is the landing.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause) · investigation-documentation (the discovery log's form: command → output → resolution) · agent-work-review (the loop-1 artifact IS the subject — full read, consistency matrix, byte-level residues).

**Refused:** any install/serving/benchmark family (no installs) · web-storm / grounded-citations / arxiv / browser-harness-sop (no web reads) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no asset edits) · github-* write verbs (no PR/issue writes, no rows) · codex / claude-code / opencode (no coding leg) · blind-agent-panels / supervisor-delegation (no fan-out) · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the record is the pair's convergence evidence — re-runnable by hand.
- **Ownership:** the seam is yours until the record is on disk, byte-verified, committed.
- **Invent and Simplify:** five moves, one record.
- **Are Right A Lot:** disconfirm the loop-1 verdict — a re-derived verdict that agrees is only worth anything if every command actually ran.
- **Bias for Action:** the refs are local; move now.
- **Dive Deep:** quoted lines; a zero is a receipted zero.
- **Deliver Results:** the verdict converged or amended, with receipts.

**THE WALL CLAUSE:** a non-reproduction (a base that doesn't resolve, a diff that disagrees with loop 1) is a QUESTION with a constructed move — the older base, the narrowed grep, the ref's sibling — before any verdict. A real wall lands with its receipts, named as a finding.
