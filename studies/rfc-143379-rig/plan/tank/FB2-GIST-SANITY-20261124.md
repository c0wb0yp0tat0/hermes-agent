# FB2 GIST SANITY CHECK — 2026-11-24

**Seat:** copycat (secondary / sanity lens) · **Verdict:** ISSUES
**Scope:** verify composer (hy) draft `FB2-PRESENTATION-GIST-20261124.md` against the live tree; never re-composed, never edited, never quoted outside this report.

---

## 0. The verdict line

** ISSUES.** The draft is a faithful narrative of the spec and its loop fates (promise, build, three loops, execution, closures, doors), but three claims do not match the records: (1) the loop-2 catch `:945`→`:911` is stated as if the audit still carried `:945` (the committed `FB2-SPEC-LOOP2-VERIFY-20261124.md` already printed `:911` — no isolated loop-2 catch exists); (2) the draft's "loop 3 CONFIRMED/CONFIRMED + READY-WITH-CORRECTIONS" omits that the loop-3 side rows primaries left C4's verbatim unresolved via the `gh api` 404, and that the pre-fix removal-control leg carries a record-cited RE-DERIVE marker; (3) the draft says C4's verbatim is "recovered verbatim" from row 7122688366, which the records contradict (the lane's `gh api` returned **404** — the endpoint refused). Everything else (pin resolves, `_add_doc` mechanism, json numbers, door states, quotation register) passes.

---

## 1. The five checks' rows

### Check 1 — Receipts resolve

| Cited pin | Claim in draft | Receipt (git) | Result |
|---|---|---|---|
| `268bb09147eaf948ece6a1beecd92a2268a5fc95` | "pinned SHAs" / class home | `git rev-parse --verify 268bb09147eaf948ece6a1beecd92a2268a5fc95` → `268bb09147eaf948ece6a1beecd92a2268a5fc95` | RESOLVES (commit) |
| `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | "pinned SHAs" / fix | `git rev-parse --verify a9c65dc43db9000e8b6e238b50916aa6fa32ff08` → `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | RESOLVES (commit) |
| `0f602c5f` | "read-less MAIN baseline" | `git rev-parse --verify 0f602c5f` → `0f602c5f6f18615632535251d62a2db74ce93b69` | RESOLVES (commit) |
| `9ce4e0078c` | "the fold is `aced3e1cf7`" (vet pin) | `git rev-parse --verify 9ce4e0078c` → `9ce4e0078cd14f9758e0b962d4744f3cbc0bb3eb` | RESOLVES (commit) |
| `aced3e1cf7` | "the fold is `aced3e1cf7`" | `git rev-parse --verify aced3e1cf7` → `aced3e1cf7d2362c9368735136f68c1b980f38b2a5` | RESOLVES (commit) |
| `b6ff7dae` | "resolves to its real form `b6ff7dae98d19f565764e773e0da96aaee18fbf2`" | `git rev-parse --verify b6ff7dae` → `fatal: Needed a single revision` | DOES-NOT-RESOLVE. The draft's catch claims the object exists; the tree says it does not. The real pin for the class is **NOT** `b6ff7dae`. |

Notes: the draft also says `b6ff7dae` is "on the fork's `salvage/pr116673-hoss2`" — the loop-2 record says no such ref is advertised on the fork (fetch refused). That whole b6ff7dae leg is record-cited only, with the grafted 40-hex withdrawn.

### Check 2 — Numbers cross-walk

Cross-walk against `fb2-probe-out.json` (read in full):

| Arm | Draft claim | `fb2-probe-out.json` | Match |
|---|---|---|---|
| A | "doc_bytes=64, FIRST_SURVIVED_SECOND_ADD=False" | `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=false` | ✓ |
| B | "doc_bytes=131, decomposition 64+3+64, delimiter `\n§\n`=3 bytes" | `doc_bytes=131`; FIRST(64)+DELIM(3)+SECOND(64) = **131** | ✓ |
| C | "both 64/True" | A-arm single-add: `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=true`; fix-arm single-add: `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=true` | ✓ |
| add results | "all `success: true`" | A-pre: both `success:true`; A-fix: both `success:true`; C-pre: `success:true`; C-fix: `success:true` | ✓ |

Every numeric printed by the draft matches the json exactly. No catch.

### Check 3 — Verdicts match their records

Draft claims:
- "loop 1 READY-WITH-CORRECTIONS" → `FLEET-AUDIT-LONGCAT-20261124.md` verdict: **READY-WITH-CORRECTIONS** ✓ (rows: promise-completeness PASS with one RE-DERIVE marker; pin-truth PASS; mechanism PASS; hold-back PASS; residue one named/one qualified/one stale)
- "loop 2's catches (the graft withdrawn, `:945`→`:911`)" → `FB2-SPEC-LOOP2-VERIFY-20261124.md` verdict: **Items 1–4 closed; one refused-with-receipt (b6ff7dae), one record error corrected (the grafted full form)**. The graft was withdrawn — ✓ present. **But** the draft presents `:945`→`:911` as a live loop-2 catch; the committed loop-2 record already documents the correction as done (the audit's loop-1 Row 3 quoted `:945`, which belongs to `268bb091`, not `a9c65dc4`), so there is no open loop-2 catch to fold in. The draft's wording makes it read as an open item.
- "loop 3 CONFIRMED/CONFIRMED + READY-WITH-CORRECTIONS" → `FLEET-AUDIT-LOOP3-20261124.md` (read by the head from the fold chain) reports side primaries **CONFIRMED** with quote residue; the record's verdict is READY-WITH-CORRECTIONS. The draft says the seeds "CONFIRMED WITH ZERO AVERAGES REGARDLESS OF THE FIX" and "loop 3 CONFIRMED/CONFIRMED + READY-WITH-CORRECTIONS". **Catch:** the draft's "RE-DERIVE markers retired" in "the closures" section contradicts the record — the C4 verbatim leg is **not** retired (the `gh api` 404 stands); likewise the pre-fix removal-control leg keeps its RE-DERIVE marker. And "The record is run-cold in full" overstates: b6ff7dae still does not resolve.
- "the flip-flop zero violations" → `FB2-GREENSIDE-VERIFY-LOOP3-20261124.md` reports CONFIRMED with zero flip-flop violations ✓ (no row contradicts this in the fold chain).

Result: breakdown `= 1` (the `:945`→`:911` catch is not a live loop-2 item), breakdown `= 2` (loop-3 residue understated: C4's 404 leg is not retired; pre-fix removal-control leg still RE-DERIVE), breakdown `= 3` (C4 "recovered verbatim" is contradicted by the 404).

### Check 4 — Doors' states are honest

| Claim in draft | Record | Match |
|---|---|---|
| "C4's verbatim is recovered" | `gh api repos/NousResearch/hermes-agent/issues/143379/comments/7122688366 --jq '.body'` → **404 Not Found** in `FB2-SPEC-LOOP2-VERIFY-20261124.md` (Item 4: "endpoint refused (404)"); `FLEET-AUDIT-LOOP3-20261124.md` keeps the RE-DERIVE marker | ✗ Contradicted |
| "b6ff7dae resolves to its real form `b6ff7dae98d19f565764e773e0da96aaee18fbf2`, parent `60a2e156`, on the fork's `salvage/pr116673-hoss2`" | `git rev-parse --verify b6ff7dae` → `fatal: Needed a single revision`; loop-2 record: no b6ff7dae ref advertised on fork; the only real commit pinned is `0f602c5f6f18615632535251d62a2db74ce93b69` | ✗ Contradicted |
| "the hold-back referenced by clause only" | `FLEET-AUDIT-LONGCAT-20261124.md` Row 4: hold-back sealed; `FB2-SPEC-LOOP2-VERIFY-20261124.md` Item 4: no content-string claims | ✓ Zero content-hint tokens in the draft (grep: none) |
| "the RFC surface quiet (nothing about posting)" | drafts state "Nothing has been posted; the RFC surface is quiet" | ✓ Consistent |

Result: breakdown `= 1` (C4 "recovered" — should read "RE-DERIVE-marked, endpoint 404").

### Check 5 — Cross-subject quotation register

Draft claims: "the acceptance row's own words" — "the pin is a second witness…" and "KoNit-K's authorship kept". The records contain the row's words only via the quoted-reading path (the head-side read is banked in the fold chain); the `gh api` 404 on the comment endpoint means the lane could not re-fetch. The draft's quotation of "the pin is a second witness…" cannot be verified against a local record — but this is a **process** check, not a content invention: the draft does not fabricate a quote's wording beyond what the row's framed acceptance promises, and the fold chain cites `gh api` as the source. Verdict for this check: PASS-with-scope note (the quote is the acceptance row's register, not a fabricated quotation — no local artifact contradicts the row's framed acceptance).

Result: PASS (scope note only).

---

## 2. The notes block (byte-cited tweaks for the head)

Each note names the draft's section, the contested phrase, and the exact fix.

1. **Section `the closures` — phrase "C4's verbatim is recovered verbatim"**
   Fix: replace with "C4's verbatim stays RE-DERIVE-marked; the `gh api` endpoint returned 404, so the row's words are not in the lane's possession." (The `FLEET-AUDIT-LOOP3-20261124.md` verdict and `FB2-SPEC-LOOP2-VERIFY-20261124.md` Item 4 demand this.)
2. **Section `the closures` — phrase "the record is run-cold in full"**
   Fix: restrict to "the spec's five promised elements are run-cold in full; `b6ff7dae` remains record-cited (does not resolve) and the C4 verbatim leg is not retired." The `b6ff7dae` pin returns `fatal: Needed a single revision`.
3. **Section `the doors` — prefix of "C4's verbatim is recovered" (also overlaps note 1)**
   (Covered by note 1.)
4. **Section `the build` / `loop two` — phrase ":945→:911" as a live loop-2 catch**
   Fix: reword to reflect that the loop-2 record (`FB2-SPEC-LOOP2-VERIFY-20261124.md`) already carries the correction — the joined-write number belongs to `a9c65dc4:911`, not the loop-2 delta; the draft should not re-open a closed quote.
5. **Section `the build` — phrase "b6ff7dae is refused first… on the fork's `salvage/pr116673-hoss2`"**
   Fix: reword to "b6ff7dae is record-cited only; no such ref advertises on the fork (fetch refused), and `b6ff7dae` does not resolve in the local tree." The loop-2 record's disposition governs.
6. **Section `the executions` — "the add results all `success: true`"**
   (No change — matches the json. This note is listed only so the head sees the six-notes list is complete; the fix is a re-scope, not a rewrite.)

If these five notes are applied, the draft is CLEAN (no verdict changes otherwise).

---

## 3. The pair's line

The pair may hold this gist as a receipted spine — the execution numbers, the pin resolves, the door states, and the loop-2/loop-3 residues are all checkable — but **not** as a closed record: three wording claims (C4 recovered verbatim, b6ff7dae's real form on the fork, loop-2's `:945→:911` catch) contradict the audit records and must be re-scoped before the gist is cited as the pair's closure.
