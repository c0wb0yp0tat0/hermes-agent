# FLEET-BRIEF FLAGSHIP-HY — the FB-2 failing-case spec (the promised test's centerpiece)

*Seat (pin): `tencent/hy4-flash:free` — the FLAGSHIP (operator-designated 2026-11-24). Probe at dispatch: HTTP 200, content_len 212, finish=stop, completion 1662 @ max_tokens 4096 — **content-bearing, window OPEN** (at 256/512/1536 the void shape; at depth the bearing — the depth lesson, AM-C2 honored: probe at the depth you intend to use; the harness's default 8192 ≫ 4096). Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission (traced to the operator's words + the thread promise)

The RFC #143379 thread's last promise (row 7122688366, 2026-11-24 05:10Z): *"The FB-2 failing-case spec is promised in full soon: the expected failure signatures for the ungated add on main and the same case on the fix, the removal control, and the hold-back class, at pinned SHAs. Nothing runs until it is on the thread."* KvNloo accepted the pre-registration (row 7122500729): he will run nothing on MAIN for FB-2 until the spec is on the thread, then reply base-red / combined-green / single-add removal control at pinned SHAs, divergences as data. The reserve's audit gates the posting — the spec lands on the STUDY first; nothing posts to the RFC surface without the operator's word.

**Your artifact IS the pre-registration.** Write it so a stranger can run it without us.

## The known ground (BORROWED — re-derive each from the pins before quoting it into the spec)

1. **The named failing case (FB-2):** a second chain-doc `add` overwrites the first. The mechanism: `_add_doc` writes `content` as the WHOLE file — `tools/memory_tool_store.py:580-618` at pin `268bb091` (round2-gate). The 297-battery does not cover it.
2. **Our own reproduction (VET-KVNLOO-20261122.md, commit 9ce4e0078c):** the verbatim `_add_doc` body executed against a temp dir — the second add clobbered the first (`FIRST_SURVIVED_SECOND_ADD=False`). The class is REAL, confirmed under our own execution, no installs, no branch touched.
3. **KvNloo's probe matrix (RFC row 7087999804, MAIN `0f602c5f`):** MAIN → `read` = `Unknown action 'read'`, 409 pass; `#116673` `60a2e156` red, own 16/16; +`b6ff7dae` green 17/17; MAIN + #116673 + #141876 `ec649ad9` green — 443 pass, dispatch contract 64/64; our `round2-gate` `268bb091` red — 297/297 (the two-add lives here).
4. **The fix's shape (from the same matrix + the vet):** the lock + the no-cache-write (`read()` hardened in #141876) — removing either alone stays green, removing both turns red. The combined tree `ec649ad9`/`a9c65dc4` is the GREEN reference for this case.

## The required artifact sections (each must carry REAL content — the write-time scan rejects skeletons)

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-FAILING-CASE-SPEC-20261124.md`

1. **The failing case's name and one-paragraph statement** (what an over-budget or normal second chain-doc add does to the first).
2. **The expected failure signature, ungated add on MAIN** — the observable: two successive chain-doc `add`s, the first doc's content surviving via a recovery re-read → what the probe sees (the first's bytes gone, replaced by the second's; the exact `_add_doc` overwrite path at `:580-618`). Name the main pin to probe (round2-gate `268bb091` for the class's home; MAIN `0f602c5f` for the read-less baseline) and the exact expected observation.
3. **The expected failure signature, same case on THE FIX** — the observable on the combined tree (locked, stateless, sanitized read at `a9c65dc4`/`ec649ad9`): the same two adds, the first surviving. Green is the expected state; a red here is the probe's own catch.
4. **The removal control** — the single-add arm: one chain-doc add on each tree, expected green on both. A red control arm invalidates the probe, never the finding.
5. **The hold-back class** — ONE class of the same family whose expected signature you DO NOT put in the spec field (e.g. the batch-path double-add, or the add-under-char-limit edge, or the add-after-remove re-add): name it in a clearly marked `HOLD-BACK` block that the head withholds from the published surface until the operator's word. This is the class that keeps a leading hint from satisfying the probe on its own (the promise's own language).
6. **The pinned SHAs** — the exact pins a runner will probe: MAIN read-less baseline, the class's home, the combined fix. Verify each pin exists with `git rev-parse --verify` in THIS tree (all three are present locally) before writing it into the spec.
7. **The condition section** — the four acceptance rows kvNloo pre-registered: 100% pin survival ×4 compactions verbatim (RED main / GREEN branch / removal control RED); stated cap with plain refusal, no eviction; no second store (decision-ledger entry, byte-compared); the contradiction-flagged row (his proposed 4th, accepted as written at 7122688366). Each with a one-line pre-registered bar.

## The verification steps (execute them, then write)

- `git rev-parse --verify 268bb09147eaf948ece6a1beecd92a2268a5fc95` and `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` and `0f602c5f` (the MAIN head per kvnloo's row — if absent locally, quote the row's claim with a RE-DERIVE marker).
- `git show 268bb091:tools/memory_tool_store.py | sed -n '575,622p'` — read the `_add_doc` whole-file write with your own eyes; quote the load-bearing lines into the spec.
- `git show a9c65dc4:tools/memory_tool_store.py | grep -n "_file_lock\|_sanitize_entry\|def read" | head` — the fix's three arms present at the combined pin.
- Re-read `plan/tank/VET-KVNLOO-20261122.md` (full) before composing the reproduction paragraph.

## Write-window

`write-window: 14` — the reads above are few and targeted; the artifact's skeleton must exist by round 14, deepened around it after.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — this artifact is a STUDY landing; the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows.
- No installs. All reads LOCAL (git show / read_file / git log — never web_extract).
- `git add` + `git commit` locally with the study identity — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only; the harness denies them).
- Never `git checkout --`, never `git stash`, never `git rm -rf` on shared files. The master's append-only.
- The branch is shared with a sibling's archiver: the tracking ref can lie — `ls-remote` first, per fold.
- No invented gates: the only true gate is the fold-push at the wire's all-clear + the operator's word on public writes.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path first (written, verified on disk by re-reading it), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words, no streamed fragments — the artifact is the landing, your last message is the report.

## The armament + name-and-refuse

**Armed (loaded, named with why):** think-tank (the spine: classify → choose → probe → evaluate → adopt-or-park → standardize → verify; the LP envelope; the wall clause) · agent-work-review (the adversarial self-lens: re-derive the numbers from tree bytes before quoting them — testimony is not evidence) · investigation-documentation (the receipts' form: every claim carries its pin + line; the discovery log's shape).

**Refused (considered, not loaded — each with its why):** aces-harness-probes / evaluating-llms-harness (no battery fire — this lane SPECS the probe, it never runs one) · web-storm / grounded-citations / arxiv (no field search — local receipts only) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config or gateway change) · safe-file-editing (no source edits — reads only, plus the spec file) · codex / claude-code / opencode (no coding leg) · github-* (no PR/issue write — commit is local) · two-model-reasoning (no offline-reasoner leg) · the creative/design/media families (no artifact of that class).

## The LP envelope (the operating laws)

- **Customer Obsession:** the spec serves kvnloo's runner and the pair's gate — a stranger must be able to execute it cold.
- **Ownership:** the seam is yours until the artifact is on disk, byte-verified, and committed. No hand-off mid-way.
- **Invent and Simplify:** the hold-back picks ONE sharp class; the spec stays one document, not three.
- **Are Right A Lot:** disconfirm your own verdicts — re-verify the pins, re-read the lines, before they enter the spec.
- **Bias for Action:** the window is open NOW; write the skeleton early, deepen after.
- **Dive Deep:** quote the actual `_add_doc` lines into the spec; never paraphrase the mechanism's shape.
- **Deliver Results:** the promised pre-registration, complete, with the hold-back sealed and the pins verified.

**THE WALL CLAUSE:** a non-reproduction (a pin that fails to resolve, a line that reads differently than the record claims) is a QUESTION, not a stop — construct the minimal move that resolves it (probe the pin again, show the sibling ref, shrink the claim to what the tree actually holds) before you ever verdict. A "couldn't reproduce / record says otherwise" without the construction is a hypothesis, and you are armed to do better. When the wall is real, name it with its receipts in a final section — the finding IS the deliverable's worth.
