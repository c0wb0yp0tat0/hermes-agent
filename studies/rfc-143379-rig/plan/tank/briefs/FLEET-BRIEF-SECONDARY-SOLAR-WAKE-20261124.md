# FLEET-BRIEF SECONDARY-SOLAR — the scheduled-wake salvage read + the FB-2 divergence lens

*Seat (pin): `upstage/solar-mini4:free` — the SECONDARY (operator-designated 2026-11-24). Probe at dispatch: HTTP 200, content_len 193, finish=stop, completion 36, responding model = the requested pin — WORKABLE. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission (traced to the operator's words + the thread promise)

The thread's promise (row 7122688366, 05:10Z) closed with: *"The scheduled-wake read lands with it."* The question, pre-registered in the reply (7122051629): **does the scheduled-wake salvage work on main touch the memory store's write path?** And the reserve's own ask, from kvnloo's field-data row (7106956922): `kanban-scheduled-wake` is his salvage of #137650 on MAIN for #158289 — "does it hold up against the memory-side follow-ups you have in mind?" — held with a short read of the branch, reported beside the question.

**Your artifact answers that read with receipts** — and adds the fleet's divergence on the FB-2 class (the second lens on the same question the flagship specs, from a different seat: the two-add mechanism viewed from the CALL side, not the store side).

## The known ground (BORROWED — verify each on the tree before quoting)

1. **The branch to read:** `kanban-scheduled-wake` (kvnloo's fork). Already fetched at `FETCH_HEAD` `8ba4b34476` (its tip: "test(kanban): make the tool-level until test actually wake, matching its PR claim"). The fork's diff vs OUR main is 16,077 files (fork divergence — the diff must be against its OWN base/merge-base, never against our main wholesale; `git merge-base` answers where it forked, then diff the SKELETON OF ITS OWN CHANGE, not the fork's whole drift).
2. **The question's frame:** the memory store's WRITE path = `tools/memory_tool_store.py`, `tools/memory_tool.py`, the `_add_doc` family, the `store.add` / `_anchor_gate` call sites (`:478-504` on the combined tree). A scheduled-wake that only READS the board (kanban state, `state.db`) does not touch it; a wake that writes session rows, compacts memory, or calls `store.add` (directly or via `preserve_session`, `DreamCycle`, the compressor hooks) does.
3. **The FB-2 class (the divergence lens):** from the store's write side, the second chain-doc add overwrites the first (`_add_doc` writes content as the whole file, `memory_tool_store.py:580-618` at round2-gate `268bb091`). Your lens: from the CALL side — what does the wake's own schedule-writing do to the chain-doc files? If the wake WRITES chain-docs on a schedule, the two-add class becomes the wake's own hazard; if it never goes near `_add_doc`/chain-doc paths, the class stays where the flagship specs it.

## The required artifact sections (real content per section — the write-time scan rejects skeletons)

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/SCHEDULED-WAKE-READ-20261124.md`

1. **The verdict line** — one line: does `kanban-scheduled-wake` (at `8ba4b34476`) touch the memory store's write path? YES / NO / PARTIAL, with the one-sentence mechanism.
2. **The branch's own change set** — `git merge-base` + `git diff <base>..8ba4b34476 --stat` (the branch's own delta, not the fork's drift); name the files the salvage itself touches.
3. **The search evidence** — the greps that decide: `git diff <base>..FETCH_HEAD | grep -n "memory_tool\|store.add\|_add_doc\|preserve_session\|DreamCycle\|write_gate"` — each hit quoted with its line; zero hits is a receipted ZERO (say "zero hits, receipts above"), never a claim.
4. **The report shape** — for the operator's reply beside the question: the verdict, the evidence lines, and the one-line answer to kvnloo's own frame ("does it hold up against the memory-side follow-ups").
5. **The divergence cell** — your independent read of the FB-2 class from the call side: does the wake's write-pattern (if any) intersect the two-add hazard? Agree / diverge / extend, with the mechanism named.

## The verification steps (execute, then write)

- `git log --oneline FETCH_HEAD -3` — confirm the tip you read.
- `git merge-base FETCH_HEAD <the fork's main or the study's main>` — if the merge-base computation is ambiguous, state the pins compared and pick the conservative base (the older), name the choice.
- `git diff <base>..FETCH_HEAD --stat | tail -15` and the greps in section 3 above — quote the load-bearing lines verbatim.
- Re-read the promise rows' wording from this brief (the two quoted rows are the contract; no other source needed).

## Write-window

`write-window: 10` — the branch reads are three commands; the skeleton by round 10, deepened after.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows.
- No installs. All reads LOCAL (git / read_file; `git fetch` only if a needed ref is absent — the target branch is already local at FETCH_HEAD; prefer the local ref).
- `git add` + `git commit` locally with the study identity — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only).
- Never `git checkout --`, never `git stash`, never `git rm -rf`. The master's append-only.
- The branch is shared with a sibling's archiver: `ls-remote` first, per fold; the tracking ref can lie.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path first (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words — the artifact is the landing.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause — a non-reproduction is a QUESTION with a constructed minimal move, never a stop) · agent-work-review (the adversarial lens: the branch's own delta vs the fork's drift — never let the 16k-file diff smuggle the verdict) · investigation-documentation (the discovery log's form: commands, receipts, limitations).

**Refused:** any install/serving/benchmark family (aces-harness-probes, evaluating-llms-harness, llama-cpp, local-llm-*, serving-llms-vllm — no installs is a hard line) · web-storm / grounded-citations / arxiv / browser-harness-sop (no field/web reads — local receipts only) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no source edits) · github-* (no PR/issue write; the read is local git) · codex / claude-code / opencode (no coding leg) · two-model-reasoning (no offline-reasoner leg) · blind-agent-panels / supervisor-delegation (no fan-out — this is the fan's own leaf) · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the read goes beside the question, in the operator's reply frame — a stranger can re-run every command.
- **Ownership:** the seam is yours until the artifact is on disk, byte-verified, committed.
- **Invent and Simplify:** one question, one artifact, the greps short enough to re-run by hand.
- **Are Right A Lot:** disconfirm — the merge-base choice, the hit count, the verdict line each get a second look against the raw diff before they land.
- **Bias for Action:** the refs are local — read first, write the skeleton early, deepen after.
- **Dive Deep:** every load-bearing hit quoted verbatim; a zero is a receipted zero.
- **Deliver Results:** the promised read, complete, with the divergence cell.

**THE WALL CLAUSE:** a non-reproduction (a ref that won't resolve, a diff that disagrees with the record's claim) is a QUESTION with a constructed minimal move — try the sibling ref, the conservative base, the narrowed grep — before any verdict. A real wall lands with its receipts, named as a finding.
