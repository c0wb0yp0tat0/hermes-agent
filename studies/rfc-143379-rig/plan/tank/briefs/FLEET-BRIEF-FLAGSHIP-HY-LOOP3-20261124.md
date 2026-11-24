# FLEET-BRIEF FLAGSHIP-HY LOOP 3 — the kaizen reloop, RED-side verification (pinned base: `268bb091`)

*Seat (pin): `tencent/hy4-flash:free` — the FLAGSHIP. The operator's steer: "Swap code bases and slightly reshape based on our frameworks historical successes especially the kit and reloop it kaizen style. I'm not saying it's wrong." The kit's L3 rule, honored: **the flip-flop — verification never shares the compose's base; per-unit base pinning.** YOUR base is the pre-fix tree `268bb091` (the RED side). Secondary verifies `a9c65dc4` (the GREEN side); the reserve's base is MAIN + study HEAD (neutral). No two lanes share a base. Branch: `study/rfc-143379-rig-20261105`. Fire: 2026-11-24.*

## The mission (traced to the operator's words)

The loop isn't wrong — it lacked per-unit base pinning. This lap verifies the FB-2 spec's RED-side claims (Section 2) and the execution receipts' arm A, **against the `268bb091` tree only**. You do not read the fixed tree; the fix is the secondary's ground. Your verdict: does the pre-fix tree, at its own bytes, support the spec's expected RED signature and the probe's measured `FIRST_SURVIVED_SECOND_ADD=False`?

## Your pinned ground (read from `268bb091` — never from HEAD or the fix pin)

1. **The seam, at your pin:** `git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '575,622p'` — quote `_add_doc`'s whole-file write at :615 (`atomic_write_text(doc_path, content, tmp_prefix=".doc_")`). Verify NO read-merge of existing entries precedes the write (the clobber's mechanism).
2. **The add route, at your pin:** `git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '560,575p'` — the `add` → `_add_doc` routing for `doc:` targets (the `_doc` resolver branch).
3. **The probe's receipt, cross-checked at your pin:** read `studies/rfc-143379-rig/plan/tank/fb2-probe-out.json` (committed) — arm A's json (`A-pre-fix-two-add`): two adds both succeed, doc_bytes 64, `FIRST_SURVIVED_SECOND_ADD=False`, doc_head = SECOND's bytes. Re-derive from the code at YOUR pin that this is the ONLY behavior the seam permits (a no-append whole-file write cannot leave FIRST's bytes; the second write replaces the file object).
4. **The spec's §2, checked:** read `FB2-FAILING-CASE-SPEC-20261124.md` §2 (the ungated arm's procedure + expected RED signature) and confirm the procedure matches the executed probe (fresh temp store, `@doc:alpha` anchor seeded, FIRST add, SECOND add, recovery read compares bytes). Any mismatch between the spec's procedure and the probe's execution is THIS lap's catch.

## The required artifact — the RED-side verification record

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-REDSIDE-VERIFY-LOOP3-20261124.md`

1. **The verdict line** — the pre-fix tree supports Section 2's RED signature: CONFIRMED / CONFIRMED-WITH-CORRECTIONS / NOT-CONFIRMED, with the one-sentence mechanism.
2. **The seam quotes** — the verbatim :615 write + the add routing, quoted from YOUR pin, with the line numbers.
3. **The receipt re-derivation** — the probe's arm-A json, cross-walked against the code: why `doc_bytes=64` and `FIRST_SURVIVED_SECOND_ADD=False` are the ONLY outcomes the seam permits.
4. **The spec-vs-probe check** — §2's procedure vs the executed probe: agreement, or the divergence with byte-citations.
5. **The convergence line** — one sentence: is the RED side run-cold, and what (if anything) still waits?

## Write-window

`write-window: 12` — reads first (M1–M5 by round 10), the record's skeleton by round 11, deepening after. The gated-read trap is known: never let the clock close on unrun moves; write early.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows. The hold-back is never quoted.
- No installs. All reads LOCAL (git / read_file on YOUR pin; `git show <pin>:…` only — the fix pin's tree is the secondary's ground, not yours; a peek that finds you reading `a9c65dc4` is a flip-flop violation).
- `git add` + `git commit` locally — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only).
- Never `git checkout --`, never `git stash`, never `git rm -rf`. The branch is shared — `ls-remote` first, per fold.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause) · investigation-documentation (command → output → resolution) · agent-work-review (the receipt-catch lens: only the seam at YOUR pin decides).

**Refused:** the fix pin's tree (the flip-flop — it's the secondary's base) · any install/serving/benchmark family · web-storm / grounded-citations / arxiv (no web reads) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config change) · safe-file-editing (no source edits) · github-* write verbs · codex / claude-code / opencode · blind-agent-panels / supervisor-delegation · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the pair's gate needs the RED side run-cold at its own pin.
- **Ownership:** the seam is yours until the record is on disk, byte-verified, committed.
- **Invent and Simplify:** one side, one pin, one record.
- **Are Right A Lot:** disconfirm — the mechanism must bite at YOUR pin's bytes, not at the receipt's words.
- **Bias for Action:** the objects are local; move now.
- **Dive Deep:** verbatim quotes; the receipt re-derived, never re-quoted.
- **Deliver Results:** the RED-side verdict, receipted.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the sibling read at your pin, the narrowed sed, the receipt's raw json — before any verdict. A real wall lands with its receipts, named as a finding. And if you find yourself reaching for the fix pin's tree — stop; that is the secondary's ground, and borrowing it is exactly the failure the kit named.
