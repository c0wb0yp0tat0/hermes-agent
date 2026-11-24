# FLEET-BRIEF RESERVE-LONGCAT LOOP 2 — the corrected spec re-audited (the convergence audit)

*Seat (pin): `meituan/longcat-2.5:free` — the RESERVE (operator-designated 2026-11-24). The operator's word: "Reloop a few times to be sure." This is the second circuit: the spec now stands at the corrected fold `8453c59adc` (fold applied the loop-1 audit's C1/C2; C3 was logged as quoting a phrase absent from the committed bytes — VERIFY that logging decision too). Fire: AFTER the flagships' loop-2 landings fold (gated — the reserve reads ground, never air).*

## The mission (traced to the operator's words)

The pair judges on convergence. Loop 1's audit verdict was READY-WITH-CORRECTIONS; the head folded the corrections. THIS lap re-audits the CORRECTED spec cold — five checks again, against the tree, with zero carryover trust — and additionally audits the two loop-2 verification records the flagships will produce (their resolves feed your pin-truth and mechanism checks).

## The audit frame — the five checks, re-run cold

Read first, in this order (all under `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/`):

1. `FB2-FAILING-CASE-SPEC-20261124.md` — the CORRECTED spec (the fold commit `8453c59adc`; your loop-1 audit is superseded by the fold, so CHECK the corrections are actually in the bytes, don't trust the commit message).
2. `FLEET-AUDIT-LONGCAT-20261124.md` — your own loop-1 audit (your verdict's words; the C1/C2/C3 dispositions were logged — check each disposition against the corrected bytes: C1's marker present? C2's annotation present? C3's "phrase absent" claim true — grep the spec for it?).
3. `FB2-SPEC-LOOP2-VERIFY-20261124.md` — the flagship's loop-2 resolves (the wall items' fates).
4. `WAKE-READ-LOOP2-VERIFY-20261124.md` — the secondary's loop-2 re-derivation.
5. (Supporting ground, if needed) `VET-KVNLOO-20261122.md` @ `9ce4e0078c`; `SCHEDULED-WAKE-READ-20261124.md`.

Then the five checks:

1. **Promise-completeness, re-checked** — the five elements, each still present in run-cold form, now WITH the wall items' fates folded (b6ff7dae resolved or receipted-refused, §2/§3 lines verbatim-run, C4 verbatim recovered or marked). The fold may have changed §6/§8's wording — re-verify the bars themselves did not move.
2. **Pin-truth, re-checked** — re-run the rev-parses on the three target pins + `9ce4e0078c` + `60a2e156` + `ec649ad9` + `af16e3ab16` + (new) `b6ff7dae`: whatever the fold says about b6ff7dae, `git rev-parse --verify` in THIS tree decides. A flag's flip from "RE-DERIVE" to "resolved" without a resolving receipt is THIS lap's headline catch.
3. **Mechanism, re-checked** — re-quote the `_add_doc` lines at `268bb091` (:580-619) and the fix arms at `a9c65dc4`, against the loop-2 record's quotes. Mismatch = this lap's catch.
4. **Hold-back, re-checked** — the sealed class still exists in §11, still ONE class, still withheld; no expected-signature string leaked into the loop-2 records (grep the two loop-2 records for the hold-back's test-name and content-hint tokens — the hint file name must not appear in them). You never publish the hold-back contents.
5. **Residues, re-checked** — the corrected spec's new wording (the fold's sentences) scanned for harder-than-receipt claims; the two loop-2 records scanned for softer-than-move claims ("refused" reported as "resolved", "not run" reported as "run"). Each named with byte-citations.

## The required artifact — the loop-2 audit

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FLEET-AUDIT-LOOP2-20261124.md`

1. **The verdict line** — READY / READY-WITH-CORRECTIONS / NOT-READY, one-sentence why.
2. **The five checks' rows** — each re-run, each with its receipts.
3. **The corrections block** — the fold-line corrections the head applies mechanically (each with the artifact + section + byte-cited phrase), or "no corrections — the fold holds".
4. **The pair's briefing** — three lines max: what the pair can rely on, what they must watch, what waits the operator's word.

## Write-window

`write-window: 16` — the five checks' rows must ALL exist on disk by round 15 (the gate opens at 16); deepening after. The first fire's skeleton already holds Row 2's receipts — BUILD on it (read `FLEET-AUDIT-LOOP2-20261124.md` first), never re-run what it receipted. The first fire's missed rounds were history-rewinding; the ground below settles it.

## Ground established by the first fire (BORROWED — cite, don't re-derive)

- **C1's quote never existed:** "OBSERVED, not invented" (with comma) is absent from BOTH `d53efee975` and `8453c59adc` — the loop-1 audit's C1 quoted a phrase that was never in the committed bytes (the head logged this at the fold; the first fire independently confirmed it).
- **The fold chain:** `d53efee975` (flagship spec) → `edda06a214` (loop-1 audit fold) → `8453c59adc` (the head's corrections fold, spec-only +10/−7) → `2b76a4c06b` (loop-2 verification record) → HEAD `2b9d756df2` (this audit's first fold).
- **Row 2 is done:** the skeleton's own receipts (eight rev-parses: `268bb091`/`a9c65dc4`/`0f602c5f`/`9ce4e0078c`/`60a2e156`/`ec649ad9`/`af16e3ab16` resolve; `b6ff7dae` fatal) stand — quote them from the skeleton.
- **The loop-2 records exist and are committed:** `FB2-SPEC-LOOP2-VERIFY-20261124.md` (at `2b76a4c06b`) closes the four wall items with receipts; `WAKE-READ-LOOP2-VERIFY-20261124.md` (at `c01f0133bf`) re-derived the wake verdict cold. The graft correction (b6ff7dae's withdrawn 40-hex) is IN the verification record — audit the withdrawal itself, plus the spec's §6 now matching it.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows. The HOLD-BACK is NEVER quoted into any record.
- No installs. All reads LOCAL (git / read_file).
- `git add` + `git commit` locally with the study identity — **NEVER `git push`, NEVER `git pull`** (fold-side pushes only).
- Never `git checkout --`, never `git stash`, never `git rm -rf` — the audit VERIFIES; it never mutates the spec or the loop-2 records. The master's append-only. `ls-remote` first, per fold.

## The emission contract

Exit 0 = the deliverable EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words — the artifact is the landing.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause) · agent-work-review (the audit IS this skill: full reads → consistency matrix → identifier cross-check → epistemic scoping) · investigation-documentation (the discovery log's form: every check row carries its command + receipt).

**Refused:** any install/serving/benchmark family (no installs) · web-storm / grounded-citations / arxiv (no field reads) · memory-chain (no chain append) · hermes-agent / hermes-gateway-ops (no config/gateway change) · safe-file-editing (no asset edits) · github-* (no PR/issue write; no row posting) · codex / claude-code / opencode (no coding leg) · blind-agent-panels / supervisor-delegation (no fan-out) · the creative/design/media families.

## The LP envelope

- **Customer Obsession:** the convergence audit serves the pair's gate — cold, complete, quotable.
- **Ownership:** the seam is yours until the artifact is on disk, byte-verified, committed.
- **Invent and Simplify:** five checks re-run, one verdict.
- **Are Right A Lot:** disconfirm the fold itself — a correction folded without landing in the bytes is a residue this lap catches.
- **Bias for Action:** read first, write the skeleton early, deepen after.
- **Dive Deep:** quote the corrected spec beside the tree; quote the loop-2 records beside their receipts.
- **Deliver Results:** the convergence verdict, every check re-run and receipted.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the sibling ref, the record's row, the narrowed grep — before any verdict. A real wall lands with its receipts, named as a finding.
