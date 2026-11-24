# FLEET AUDIT — LOOP 2 — the convergence audit — LONGCAT (reserve) — 2026-11-24

*Seat: `meituan/longcat-2.5:free` — the RESERVE (operator-designated 2026-11-24). Subject: `FB2-FAILING-CASE-SPEC-20261124.md` at the corrected fold `8453c59adc`, with the loop-2 verification record (`FB2-SPEC-LOOP2-VERIFY-20261124.md` at `2b76a4c06b`) and the wake record (`WAKE-READ-LOOP2-VERIFY-20261124.md` at `c01f0133bf`) in scope. This fire is ASSEMBLY ONLY: it replaces the skeleton using only the receipts below — the committed skeleton's Row-2 block, the two loop-2 records' quoted receipts, and the head's cat-file settlements. It ran no fresh verification command, mutated neither the spec nor the records, and published nothing. Loop 1's audit is superseded; the five checks are assembled here from settled evidence, not re-derived.*

## 0. Receipt spine — the fold chain (fire 2's log)

`d53efee975` (flagship spec) → `edda06a214` (loop-1 audit fold) → `8453c59adc` (head's corrections fold, spec-only +10/−7) → `2b76a4c06b` (loop-2 verification record) → `2b9d756df2` (this audit's skeleton fold).

Off-branch receipts: `c01f0133bf` (wake-read loop-2 record) · the lane log `fleet-hy-loop2-verify-r2-20261124.log` · the head's `cat-file -t` settlements on 2026-11-24.

## 1. The verdict line

**READY-WITH-CORRECTIONS.** All five promised elements are present and run-cold in the committed spec; the mechanism is confirmed (with one quote correction); the pin-truth is honest — seven resolve, `b6ff7dae` is record-cited with the grafted full form withdrawn; the hold-back is sealed; every residue is dispositioned. Two corrections ride with the landing, neither blocking: C4's verbatim awaits an operator/maintainer read of row 7122688366, and the pre-fix removal-control leg awaits a resolvable `b6ff7dae` base from R2's record. The fold's dispositions stand.

## 2. The five checks' rows

### Row 1 — Promise-completeness: PASS-with-caveat

The five promised elements live in the COMMITTED spec, located thus (the loop-1 audit's "Spec location" column cited the flagship's mid-write draft — see Row 5):

| Element | Committed location |
|---|---|
| failing case | §1 |
| MAIN signature | §2 |
| fix signature | §3 |
| removal control | §4 |
| hold-back | §5 |
| pins | §6 |
| conditions | §7 |
| wall record | §8 |
| run envelope | §9 |

The verification record's convergence line attests the run-cold form: *"The spec's five promised elements are now run-cold in full: the failing case, both expected signatures, the removal control, the hold-back (sealed), and the pinned SHAs — with the one record-cited leg (pre-fix removal control) honestly marked rather than silently asserted."*

The loop-2 record closes the four wall items:

1. b6ff7dae — REFUSED-with-receipt; grafted full form withdrawn; RE-DERIVE marker stands.
2. `_add_doc` verbatim — run and receipted (:580 def, :615 whole-file write).
3. Fix arms — run and receipted; joining write corrected to `a9c65dc4:911`.
4. C4 verbatim — endpoint refused (404); marker stands; minimal move named.

Caveat, honestly carried: the pre-fix removal-control leg remains record-cited (its pin does not resolve; R2's record must supply a base before it runs). Nothing promised is missing from the committed bytes; one leg is deferred with its marker intact — hence PASS-with-caveat, not an unqualified PASS.

### Row 2 — Pin-truth: PASS

Receipts quoted verbatim from the committed skeleton (re-run in this tree by fire 1):

```
$ git rev-parse --verify 268bb09147eaf948ece6a1beecd92a2268a5fc95
268bb09147eaf948ece6a1beecd92a2268a5fc95     # RESOLVES
$ git rev-parse --verify a9c65dc43db9000e8b6e238b50916aa6fa32ff08
a9c65dc43db9000e8b6e238b50916aa6fa32ff08     # RESOLVES
$ git rev-parse --verify 0f602c5f
0f602c5f6f18615632535251d62a2db74ce93b69     # RESOLVES
$ git rev-parse --verify 9ce4e0078c
9ce4e0078cd14f9758e0b962d4744f3cbc0bb3eb     # RESOLVES (vet pin)
$ git rev-parse --verify 60a2e156
60a2e1563802368b46018bba2a70f11de31a6b0a     # RESOLVES (supporting)
$ git rev-parse --verify ec649ad9
ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a     # RESOLVES (supporting)
$ git rev-parse --verify af16e3ab16
af16e3ab16eed2492552c325ad1777533a8b7004     # RESOLVES (supporting)
$ git rev-parse --verify b6ff7dae
fatal: Needed a single revision            # DOES NOT RESOLVE
```

The head's cat-file settlements stand with them: `cat-file -t` on each resolved pin → **commit**; on `b6ff7dae6f18…` → **absent**.

The graft withdrawal is part of this row. The 40-hex `b6ff7dae6f18615632535251d62a2db74ce93b69` was a graft — its 32-hex tail is shared with the real `0f602c5f6f18615632535251d62a2db74ce93b69` (the lane's own round-30 reasoning: *"§6 claims a full form for 0f602c5f sharing the exact tail of b6ff7dae — verify with cat-file"*). Settled: `cat-file -t 0f602c5f6f18…` → commit (REAL); `cat-file -t b6ff7dae6f18…` → fatal: could not get object info (NOT an object). The fetch was REFUSED — `fatal: remote error: upload-pack: not our ref b6ff7dae…` — and the fork advertises no such ref. Disposition: `b6ff7dae` remains **record-cited only** — the 8-hex from KvNloo's matrix row 7087999804, full form UNKNOWN, absent from the local store and the fork's advertised refs. The record no longer asserts a false full form. Echo trap on record: `rev-parse --verify` echoes any well-formed 40-hex with exit 0; only `cat-file -t` (or a peel `^{commit}`) proves existence.

### Row 3 — Mechanism: PASS (quote corrected)

`_add_doc`, CONFIRMED verbatim (`git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '575,622p'`): **`def _add_doc` at :580; the single write at :615 `atomic_write_text(doc_path, content, tmp_prefix=".doc_")`** — whole-file write of `content`, exactly as the spec records; no merge/rename/compaction between the adds.

Fix arms, CONFIRMED at the fix pin (`git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tools/memory_tool_store.py | grep -n "_file_lock\|_sanitize_entry\|def read"`): `_sanitize_entry` def :69 · `_file_lock` :349 · `def read` :551 · `_file_lock` use :562 · `view = [_sanitize_entry…]` :567.

Joining write: at the fix pin it is **`:911`** — `atomic_write_text(path, ENTRY_DELIMITER.join(entries), tmp_prefix=".mem_")`. Correction carried: loop-1's Row 3 quoted **`:945`**, which belongs to the `268bb091` commit, not `a9c65dc4`. The mechanism claim stands (the joining write exists); the line number was pinned to the wrong commit — a quote error in the audit, caught and corrected by the verification record.

### Row 4 — Hold-back: PASS

§5 of the committed spec — ONE class, sealed. It is never quoted here, in the skeleton, or in either loop-2 record. Leak check across the receipts: none — the records name only the class's existence; the skeleton's PENDING markers carried no content.

### Row 5 — Residues: PASS-with-note

- **C1 — phantom quote:** "OBSERVED, not invented" (with comma) is absent from BOTH `d53efee975` and `8453c59adc`; the loop-1 audit quoted a phrase that was never in the committed bytes. The fold's disposition, audited: C1's SUBSTANCE applied — the b6ff7dae record-cited marker — while the phantom quote was not applied, there being nothing to apply. That stands as the fold's own honest decision.
- **C2 — applied:** byte-visible in §6 of the corrected spec — the record-cited marker for b6ff7dae alongside the reserve's resolved receipts.
- **C3 — logged-absent:** the "§9.3 byte-verified" phrase does not exist in the committed bytes, so the head's "logged, not applied" was the honest disposition.
- **Loop-1 draft-state citations — named residue:** loop-1 cited §9.1, §9.2, §9.3, §11, which do not exist in any committed revision (the committed spec has 9 sections; the hold-back is §5, not §11). Its Row-1 "Spec location" column is valid only against the flagship's mid-write draft; the committed mapping in Row 1 above supersedes it.
- **Wake receipt:** the wake record's PARTIAL stands — zero memory-store anchor hits, no residues, convergence line written.

## 3. The corrections block

1. **C4 verbatim (row 7122688366):** the lane's endpoint returned `404 Not Found`. Minimal move: the operator's or a maintainer-authenticated read of the row. Until then the spec's RE-DERIVE marker stands; the bar (accepted-as-written, contradiction flagged) is unchanged.
2. **Pre-fix removal-control leg:** blocked on a resolvable `b6ff7dae` base. Minimal move: R2's record supplies the base; the RE-DERIVE marker stands until it does. The grafted 40-hex must not be reintroduced — any future full-form claim requires `cat-file -t` (or a peel `^{commit}`), never a rev-parse echo.
3. **Loop-1 audit citations:** superseded; the committed-spec mapping (Row 1) replaces its "Spec location" column. No further action beyond this naming.

No check required a command this fire did not run; the two open legs above are named here for the head, per the wall clause.

## 4. The pair's briefing (three lines)

1. **READY-WITH-CORRECTIONS** — all five promised elements run-cold in the committed spec (§§1–9); mechanism confirmed with the joining-write correction to `a9c65dc4:911`; pins honest — seven resolve, `b6ff7dae` record-cited with the graft withdrawn.
2. Two corrections ride, neither blocking: C4's verbatim awaits an operator/maintainer read of row 7122688366 (404 for the lane); the pre-fix removal-control leg awaits R2's resolvable base for `b6ff7dae`.
3. The fold's C1/C2/C3 dispositions stand audited (phantom quote never existed; substance applied; C3 honestly logged); loop-1's draft-state citations are the named residue; the convergence line is written — the pair may fold.

---
*Assembly fire: zero fresh commands; receipts quoted from the committed skeleton, `FB2-SPEC-LOOP2-VERIFY-20261124.md` (`2b76a4c06b`), `WAKE-READ-LOOP2-VERIFY-20261124.md` (`c01f0133bf`), and the head's settlements. The HOLD-BACK is never quoted. Nothing public.*