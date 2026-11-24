# FLEET-BRIEF RESERVE-LONGCAT LOOP 2, FIRE 3 — ASSEMBLY ONLY (the convergence audit's final form)

*Seat (pin): `meituan/longcat-2.5:free` — the RESERVE. The operator's word: "Reloop a few times to be sure." This is the third and final fire of the loop-2 audit. The first two fires did the verification; their conclusions are in the ground below. THIS fire is assembly only: write the complete audit, receipted, in one `write_file` call within your first five rounds.*

## THE TASK (this is not a re-verification)

The verification evidence is already gathered. Your job: assemble the audit document at the artifact path, replacing the skeleton, using ONLY the receipts below (BORROWED, quoted from the committed skeleton + the two failed fires' logs + the head's settlements). **The verdict is YOURS to write** — you may conclude READY, READY-WITH-CORRECTIONS, or NOT-READY — but every row you write must rest on the receipts below, not on new commands.

**Permitted tool use (ALL of it):** one `read_file` of `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FLEET-AUDIT-LOOP2-20261124.md` (the skeleton — quote its Row 2 receipts verbatim) and one `read_file` of `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-SPEC-LOOP2-VERIFY-20261124.md` (the loop-2 verification record). Then ONE `write_file` with the complete audit. Then `git add` + `git commit`. That is the whole mission. **No other terminal calls. No git grep. No rev-parse. No history.** If a check would require a command you aren't allowed to run, write it into the corrections block as a requirement — do not run it.

## The verified ground (BORROWED — each with its receipt; quote, don't re-derive)

1. **The fold chain (verified by fire 2's log):** `d53efee975` (flagship spec) → `edda06a214` (loop-1 audit fold) → `8453c59adc` (head's corrections fold, spec-only +10/−7) → `2b76a4c06b` (loop-2 verification record) → `2b9d756df2` (this audit's skeleton fold).
2. **Row 2 — pin-truth (from the committed skeleton, re-run in THIS tree by fire 1):** `268bb091…`, `a9c65dc4…`, `0f602c5f…`, `9ce4e0078c…`, `60a2e156…`, `ec649ad9…`, `af16e3ab16…` all RESOLVE; `b6ff7dae` → `fatal: Needed a single revision`. The head's cat-file settlements stand with them: `cat-file -t` on each resolved pin → commit; on `b6ff7dae6f18…` → absent (the 40-hex was a graft — see the loop-2 record).
3. **C1's quote never existed (verified by fire 2):** "OBSERVED, not invented" (with comma) is absent from BOTH `d53efee975` and `8453c59adc`. The loop-1 audit's C1 quoted a phrase that was never in the committed bytes. The head's fold-logged disposition (C1's SUBSTANCE applied — the b6ff7dae record-cited marker — while the phantom quote was not applied, there being nothing to apply) stands as the fold's own decision; audit that decision.
4. **The loop-1 audit read a DRAFT state (fire 2's finding):** the loop-1 audit cited spec sections `§9.1`, `§9.2`, `§9.3`, `§11` which DO NOT EXIST in any committed revision (the committed spec has 9 sections; HOLD-BACK is §5 not §11). The loop-1 audit's citations were valid only against the flagship's mid-write draft. This affects the loop-1 audit's Row-1 table's "Spec location" column — the five promised elements are located differently in the committed bytes (failing case §1, MAIN signature §2, fix signature §3, removal control §4, hold-back §5, pins §6, conditions §7, wall record §8, run envelope §9).
5. **The loop-2 wall-item fates (from the verification record at `2b76a4c06b`):** b6ff7dae REFUSED-with-receipt + graft withdrawn · `_add_doc` verbatim :580 def / :615 whole-file write CONFIRMED · fix arms present + joining write corrected to `a9c65dc4:911` · C4 verbatim endpoint refused (404), marker stands. §6 of the corrected spec now carries the record-cited marker for b6ff7dae and the reserve's resolved receipts.
6. **The wake verdict (from `WAKE-READ-LOOP2-VERIFY-20261124.md` at `c01f0133bf`):** PARTIAL stands — zero memory-store anchor hits, no residues, convergence line written.

## The five checks' rows (assembly template — fill each with the receipts above)

1. **Promise-completeness:** five elements located in the COMMITTED spec (see ground 4's mapping) — present, run-cold form, with the loop-2 record closing the wall items. PASS/PASS-with-caveat/NOT-PASS — yours to judge, cited to the sections.
2. **Pin-truth:** quote ground 2 verbatim (the eight rev-parses + the cat-file settlements + the one fatal). The graft withdrawal is part of this row: the record no longer asserts a false full form.
3. **Mechanism:** the `_add_doc` whole-file write at `268bb091:615`, the fix arms at `a9c65dc4` with the corrected `:911` joining write — cited from the verification record's quotes.
4. **Hold-back:** §5 of the committed spec, ONE class, sealed; the loop-2 records contain no hold-back tokens (the records name only the class's existence).
5. **Residues:** the fold's C1/C2/C3 dispositions audited (C1 phantom — ground 3; C2 applied and byte-visible in §6 — the record-cited marker; C3 logged-absent — the "§9.3 byte-verified" phrase does not exist in the committed bytes, so the head's "logged, not applied" was the honest disposition — and the loop-1 audit's draft-state citations are themselves the residue, named in this row).

## The verdict and pair briefing

Write the verdict line and the three-line pair briefing from the assembled rows. READY-WITH-CORRECTIONS is a normal landing (the fold's dispositions ride); NOT-READY requires a missing element or a real catch in the corrections.

## Write-window

`write-window: 4` — you are told to write by round 5; the window line is a backstop only. Write early; there is nothing left to verify.

## The hard lines (binding)

- Nothing public, EVER, without the operator's word — the RFC #143379 issue surface stays QUIET; PR #1's thread is the only row surface, and only the head rows. The HOLD-BACK is NEVER quoted.
- No installs. All reads LOCAL.
- `git add` + `git commit` locally — **NEVER `git push`, NEVER `git pull`**.
- Never `git checkout --`, never `git stash`, never `git rm -rf`. The audit VERIFIES and assembles; it never mutates the spec or the records. `ls-remote` first, per fold — the branch is shared.

## The emission contract

Exit 0 = the complete audit EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words — the artifact is the landing.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the LP envelope; the wall clause) · agent-work-review (this IS the review: rows → receipts → verdict) · investigation-documentation (the discovery log's form — the receipts ARE the deliverable).

**Refused — and THIS TIME ENFORCED, not listed:** any terminal call beyond `git add`/`git commit`; any new verification command (rev-parse, cat-file, grep, show, diff, log); any install; any web read; any row posting; any mutation of the spec or records. The two previous fires prove the pattern: deep re-derivation, no assembly. This fire assembles. If a check needs a command, the corrections block names it for the head — the head runs it.

## The LP envelope

- **Customer Obsession:** the pair's gate needs the verdict, not another history.
- **Ownership:** the seam is yours until the audit is on disk, byte-verified, committed.
- **Invent and Simplify:** one write, five rows, one verdict.
- **Are Right A Lot:** the receipts are settled; your judgment on their assembly is the value.
- **Bias for Action:** write now, re-read after.
- **Dive Deep:** quote the receipts you cite; never graft a number.
- **Deliver Results:** the convergence verdict, complete, committed.

**THE WALL CLAUSE:** a missing receipt is a QUESTION resolved by naming it in the corrections block with its minimal move — never by running a fresh command this fire.
