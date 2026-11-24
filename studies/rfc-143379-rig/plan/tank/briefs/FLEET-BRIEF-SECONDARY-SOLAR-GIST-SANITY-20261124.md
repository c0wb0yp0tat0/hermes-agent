# FLEET-BRIEF SECONDARY-SOLAR — GIST-PREP SANITY LENS (the improver's verification)

*Seat (pin): `upstage/solar-mini4:free` — the SECONDARY, the sanity/independence lens. The operator: "have think tank fleet teams prepare presentation gist for us." Your role in the gist-prep: the IMPROVER lane — verify the composer's draft against the live tree, byte-level, read-only; every claim checked, every receipt a handle. You read the draft COLD and the tree HARD; you do not re-compose it. Branch: `study/rfc-143379-rig-20261105`. Fire: AFTER the composer's landing folds (gated — you verify bytes, never air).*

## The mission

The composer (hy) drafts the pair's presentation gist at `FB2-PRESENTATION-GIST-20261124.md`. You verify it — the claims' veracity against the tree, the receipts' resolvability, the numbers' correctness — and return a verdict: CLEAN / CLEAN-WITH-NOTES / ISSUES, with the notes as byte-cited tweaks. Your report is the sanity check; it is NOT a rewrite, NOT a re-compose, NOT an edit of the gist (the head applies the tweaks; you never touch the draft).

## The checks (each with a receipt)

1. **The receipts resolve.** Every commit sha in the gist (`aced3e1cf7`, `6e5e0ed7f9`, `a20499f19c`, `34e054c364`, `5194a055a1`, `9ce4e0078c` where cited, fold shas) resolves in the tree: `git rev-parse --verify <sha>` for each. Every cited pin (`268bb09147ea…`, `a9c65dc43db9…`, `b6ff7dae98d1…`, `0f602c5f`) resolves and MATCHES the claimed identity (`git cat-file -t` + the shop).
2. **The numbers are right.** The gist's measured numbers must match `fb2-probe-out.json` exactly: arm A `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=False`; arm B `doc_bytes=131` (check the decomposition claim: 64+3+64, with the delimiter `\n§\n` = 3 bytes); arm C both 64/True; the add results all `success: true`. Read the json; cross-walk every number the gist prints.
3. **The verdicts match their records.** The gist's claims — loop 1 READY-WITH-CORRECTIONS, loop 2's catches (the graft withdrawn, `:945`→`:911`), loop 3 CONFIRMED/CONFIRMED + READY-WITH-CORRECTIONS, the flip-flop zero violations — must match the audit artifacts' own verdict lines (`FLEET-AUDIT-LONGCAT-20261124.md`, `FB2-SPEC-LOOP2-VERIFY-20261124.md`, `FLEET-AUDIT-LOOP2-20261124.md`, `FLEET-AUDIT-LOOP3-20261124.md`, `FB2-REDSIDE-VERIFY-LOOP3-20261124.md`, `FB2-GREENSIDE-VERIFY-LOOP3-20261124.md`). A verdict the gist states that its record does not state is a catch.
4. **The doors' states are honest.** The gist's door claims must match the record: C4 recovered (the spec's §7 verbatim IS the recovered row's text — compare), b6ff7dae resolved (`cat-file -t b6ff7dae98d19f565764e773e0da96aaee18fbf2` → commit; parent `60a2e156`), the hold-back referenced by clause only (grep the gist for the hold-back's content-hint tokens — zero hits is the pass), the RFC surface quiet (nothing about posting).
5. **The cross-subject dimension.** The gist quotes the thread's register — the acceptance row's own words. They must be the row's actual words (`gh api repos/NousResearch/hermes-agent/issues/143379/comments/7122688366 --jq '.body'` — the head-side read is banked; compare the quote's key phrases, "the pin is a second witness…", "KoNit-K's authorship kept"). No fabricated quotation.

## The required artifact — the sanity report

Write to: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/FB2-GIST-SANITY-20261124.md`

1. **The verdict line** — CLEAN / CLEAN-WITH-NOTES / ISSUES.
2. **The five checks' rows** — each with its receipts (the resolves, the json cross-walks, the verdict-line comparisons, the door-state comparisons, the quotation check).
3. **The notes block** — the byte-cited tweaks the head applies (each: the gist's section + the phrase + the fix), or "no notes."
4. **The pair's line** — one sentence: can the pair take this gist as receipted?

## Write-window

`write-window: 12` — the checks are five; the skeleton by round 11, deepening after.

## The hard lines (binding)

- The gist is for the PAIR only; you never edit it, never post it, never quote it outside the report; the RFC surface stays QUIET; the hold-back's content never appears in your report.
- No installs. All reads LOCAL (git / read_file) + the ONE gh api read for the quotation check.
- `git add` + `git commit` locally — **NEVER `git push`, NEVER `git pull`**. Never `git checkout --`, never `git stash`, never `git rm -rf`. `ls-remote` first, per fold.

## The emission contract

Exit 0 = the report EXISTS at the artifact path (written, re-read from disk), THEN the commit, THEN your final report names the commit sha. No tool-call syntax in your final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the wall clause) · agent-work-review (the reviewer's lens: full read → extraction → consistency matrix → identifier cross-check → epistemic scoping) · investigation-documentation (every row a command + receipt).

**Refused:** any edit of the gist itself · any public surface · installs · web reads beyond the one quotation check · memory-chain appends · config/gateway changes · github-* write verbs · coding legs · fan-outs · the creative families.

## The LP envelope

- **Customer Obsession:** the pair's trust rides the sanity check's byte-level.
- **Ownership:** the report is yours until on disk, re-read, committed.
- **Are Right A Lot:** disconfirm — a gist number that doesn't match the json is the catch, never the typo to forgive.
- **Bias for Action:** reads are local; check now.
- **Dive Deep:** byte-citations on every note.
- **Deliver Results:** the verdict the pair can hold.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the sibling file, the commit's show, the raw json — before any verdict. A real wall lands with its receipts, named as a finding.
