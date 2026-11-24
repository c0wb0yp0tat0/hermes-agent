# FLEET-BRIEF FLAGSHIP-HY LOOP 2 — the verification lap (the wall items resolved)

*Seat (pin): `tencent/hy4-flash:free` — the FLAGSHIP (operator-designated 2026-11-24). The operator's word: "Reloop a few times to be sure." This is the second circuit: the spec stands at the corrected fold `8453c59adc`; the wall items the first pass left RE-DERIVE-marked are THIS lap's mission. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24, after loop 1's fold.*

## The mission (traced to the operator's words)

The pair (the operator + the head) judges readiness on convergence, not on the first pass's word. Loop 1's reserve audit (`FLEET-AUDIT-LONGCAT-20261124.md`) found the spec's load-bearing ground sound but left four wall items RE-DERIVE-marked. THIS lap resolves them; the next lap re-reads what you resolve. The four items, each with its move:

**Ground already established (the first fire's log + the head's re-checks — BORROWED, re-verify before citing):** (a) item 1's fetch was REFUSED by the fork (`fatal: remote error: upload-pack: not our ref b6ff7dae6f18…`) and the head's own `ls-remote` of `memory-chain-doc-read-combined` / `memory-probe-harness-kgate` did not surface `b6ff7dae` — the pin is REFUSED-with-receipt, confirm once and write the receipt; (b) the fix's joining write is at **`a9c65dc4:911`** (not `:945` — that line number belongs to the `268bb091` commit; the first fire caught this divergence and the audit's §3 table quoted `:945` from the loop-1 spec) — re-quote the :911 line and flip the audit's mechanism row: the catch IS the record; (c) the `_add_doc` verbatim lines at `268bb091` :580-619 were established by the loop-1 reserve (grep receipts in `FLEET-AUDIT-LONGCAT-20261124.md` Row 3) — re-run the sed to confirm, quote into the record.

## The four wall items and their minimal moves (the wall clause: construct, don't stop)

1. **`b6ff7dae` (the removal control's pre-fix leg pin).** Record-cited from KvNloo's matrix row 7087999804 (`+b6ff7dae` → green 17/17). Does not resolve locally (`git rev-parse --verify b6ff7dae` → `fatal: Needed a single revision`; the full form `b6ff7dae6f18615632535251d62a2db74ce93b69` is NOT in the object store — the short-SHA echo test is not proof; only `--verify` is). **Minimal move:** `git fetch https://github.com/kvnloo/hermes-agent.git b6ff7dae6f18615632535251d62a2db74ce93b69` — if the fork serves it, `git rev-parse --verify b6ff7dae6f18615632535251d62a2db74ce93b69` MUST then resolve; record the fetch's output and the resolved check. If the fork refuses (unreachable / dumb server), the pin stays a record-cited RE-DERIVE marker and you RECEIPT that state — a refusal is a finding, never a hole.
2. **The `_add_doc` verbatim lines (§2's embedded command).** `git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '575,622p'` — read the actual bytes; confirm the whole-file `atomic_write_text(doc_path, content, …)` at :615 and the absence of merge/rename/compaction between the two adds. Quote the load-bearing lines into your verification record.
3. **The fix's three arms (§3's embedded command).** `git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tools/memory_tool_store.py | grep -n "_file_lock\|_sanitize_entry\|def read"` — the three arms (`_file_lock` at :349, `read` at :551-567, `_sanitize_entry` at :567-573, and the joining write at :945) must all be present. Quote them.
4. **C4's verbatim text (the contradiction-flagged fourth row).** The local tree carries the frame, not the row's words. **Minimal move:** `gh api repos/NousResearch/hermes-agent/issues/143379/comments/7122688366 --jq '.body'` — the thread row that accepted his fourth condition as written. Extract the row's own sentence(s) about the contradiction flag VERBATIM into your record; if the API is refused, state the refusal with its receipt and keep the RE-DERIVE marker.

## The required artifact — the verification record

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-SPEC-LOOP2-VERIFY-20261124.md`

1. **The four resolves** — one row per item: the command run, its verbatim output head, the resolution state (RESOLVED / REFUSED-with-receipt / UNCHANGED-marker).
2. **The resolved pin table** — b6ff7dae's final state, plus the three target pins re-confirmed (`268bb091`, `a9c65dc4`, `0f602c5f` full forms) with `--verify` receipts.
3. **The delta list** — what the spec needs at the next fold (each named with the spec's section): the §6 marker's upgrade if b6ff7dae resolved, §2/§3's wall-record lines flipped from "NOT run" to "run and receipted", C4's entry if the verbatim was recovered. The head applies these mechanically at the fold; the spec's standing bars do not change.
4. **The convergence line** — one sentence: are the spec's five promised elements now run-cold in full? What, if anything, still waits?

## Write-window

`write-window: 16` — run the moves FIRST, write the skeleton no later than round 15, deepen after (the gate opens at 16; a written skeleton reopens reads). The loop's lesson: the gated-read trap — never let the clock close on unrun moves.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows. The hold-back never enters this record.
- No installs. The gh api call is a READ (it retrieves the row); the harness's own gate allows `gh api` — never `gh` write verbs, never the browser.
- `git add` + `git commit` locally with the study identity — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only). `git fetch` of the pin is a read-side move: it writes only to the local object store/refs and is allowed; it never touches the shared branch's head.
- Never `git checkout --`, never `git stash`, never `git rm -rf`. The master's append-only. The branch is shared with a sibling's archiver — `ls-remote` first, per fold.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words — the artifact is the landing.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause — every wall item has a constructed move here, and a refusal lands as a finding with its receipt) · investigation-documentation (the discovery log's form: command → output → resolution; the receipts are the deliverable) · agent-work-review (the adversarial self-lens: your record's claims must be reproducible from its own quoted commands).

**Refused:** any install/serving/benchmark family (no installs is a hard line) · web-storm / grounded-citations / arxiv / browser-harness-sop (no web surface beyond the one gh api read) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no asset edits) · github-* write verbs (no PR/issue write, no row posting) · codex / claude-code / opencode (no coding leg) · blind-agent-panels / supervisor-delegation (no fan-out) · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the verification record is the pair's convergence evidence — every command re-runnable by hand.
- **Ownership:** the seam is yours until the record is on disk, byte-verified, committed.
- **Invent and Simplify:** four moves, one record, the deltas named.
- **Are Right A Lot:** disconfirm — a fetch that "succeeds" but leaves `--verify` failing is NOT a resolve; a gh api row that does not contain C4's flag is NOT the verbatim.
- **Bias for Action:** the objects are local or one fetch away — move now.
- **Dive Deep:** verbatim quotes, never paraphrase, for both the source lines and the row's words.
- **Deliver Results:** the wall items closed or receipted; the convergence line honest.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — try the sibling ref, the fork's fetch, the row's API — before any verdict. A real wall lands with its receipts, named as a finding. Never soften a REFUSED into a RESOLVED.
