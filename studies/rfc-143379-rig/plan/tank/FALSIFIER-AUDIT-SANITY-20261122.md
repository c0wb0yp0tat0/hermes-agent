# FALSIFIER-AUDIT-SANITY-20261122 — SANITY rung: the audit's own claims re-derived

Contract: BRIEF-SPECIAL-MISSION-3-SANITY-20261122.md · audit deliverable
studies/rfc-143379-rig/plan/tank/FALSIFIER-AUDIT-20261122.md (7eb2ac5421).
Current tree: study branch `study/rfc-143379-rig-20261105`, HEAD
`7eb2ac54217232431816c788caec80f3a288838a` (origin/study/rfc-143379-rig-20261105 =
`bb3b33c7b7cc3c681240286926e16878cdfe740e`). Reference trees: battery
`30f08c2a0f7c666e3675d51fe940c5daeedd9b35` (fixes/falsifier-battery-20261104);
pr-139606 `d1bdb4582cd5d16be6a6b486f696f8240c222b96`; feat/140005-spa-dream
`ffb85c2c58`. All checks LOCAL read-only; the battery run is a pytest pass/fail count
only (study paths untouched).

## 0. The re-run evidence

- Battery count re-run at the battery HEAD (30f08c2a0f):
  `python3 -m pytest tests/falsifier-battery/ -p no:cacheprovider -q` →
  **28 passed, 1 xpassed in 0.91s** — 0 failed, 0 skipped. Matches the audit's G0 claim
  "28 passed, 1 xpassed, 0 failed, 0 skipped" **at the battery HEAD**.
- Battery history counts (`def test_`): e366d9f8e5 = 20; 5077bb3e = 23; 30f08c2a0f = 29.
  "21 matches no commit" holds (auditor's G0 count drift).
- Orphan-edge ancestry (`git merge-base --is-ancestor`): a996d4ad30 **IS an ancestor** of
  the battery HEAD 30f08c2a0f; **NOT an ancestor** of the current study HEAD 7eb2ac5421.
- Zero-call sites at the current study HEAD: `grep -rn verify_post_write --include='*.py' .`
  → 0 matches (the function is absent at the study HEAD, not merely un-called).
- dream_cycle bank-line: `tools/dream_cycle.py` absent at the study HEAD; no
  `MemoryStore.bank` anywhere in the fork (the only `def bank` is a `FakeStore` in
  tests/tools/test_dream_cycle.py:21).
- preserve_session returns' drop: at the current study HEAD, tools/spa_integration.py is
  absent; at the only ref that carries it (ffb85c2c58), lines 100-107 drop both
  `store.add` return dicts and return `doc_name` unconditionally.

## 1. G2 misread-catch — CONFIRMED (the audit's misread-class is TRUE)

- Prior verification row 2 (XNGG-GAPS-VERIFICATION-20261105.md, row 2) recorded the gap as
  "NOT REPRODUCED at this pin" — the guard IS present: `if name is None: return …`,
  citing memory_tool.py:280-283.
- At pr-139606 (d1bdb4582c), `name = doc_name(doc)` (:282) is followed by
  `if name is None: return …` (:283). The guard checks the **result** of
  `doc_name(doc)`, not whether `doc_name` is callable. pr-139606's
  `except ImportError` block (:46-53) sets `doc_name = None` because the #116673
  doc-chain primitives are absent. Hence `doc_name(doc)` at :282 raises
  `TypeError: 'NoneType' object is not callable` **before** the guard at :283 can fire.
  The prior row's "NOT REPRODUCED" misclassified the guard's shape → the audit's
  misread-class is TRUE (the prior row is a false refutation).
- Current study HEAD (7eb2ac5421): `memory_tool()` has no `doc` parameter and grep for
  `DOC_TARGET_PREFIX|doc_name|_resolve_target` is empty → the TypeError class is
  unreachable by removal (the doc chain is absent, not guarded). Fix-brief FB-4
  (`doc_name`-None guard) still applies to the battery/pr-139606 lineage.

## 2. Battery run numbers — CONFIRMED at the battery HEAD; the study's local copy diverges

- At the battery HEAD 30f08c2a0f: 28 passed, 1 xpassed, 0 failed, 0 skipped (re-run =
  audit's claim receiptable about the battery lineage).
- At the current study HEAD (7eb2ac5421), the study branch's local copy of the battery
  tests (tests/falsifier-battery/ at root and nested) reports **16 passed, 13 skipped**
  — the study's copy dropped the `_read_substrate_guard` fixture in
  test_nugget6_strengthened.py, so 13 substrate tests self-skip. The audit's matrix does
  not account for the study branch carrying its own battery copy; the two trees diverge.
  This is the only battery-path divergence found; the counts' truth is at the battery HEAD.

## 3. GREEN-not-RED orphan edge — receiptable at the battery HEAD only

- a996d4ad30 IS an ancestor of the battery HEAD 30f08c2a0f: the whole-anchor resolution
  landed before the battery was cut; at the battery HEAD the strengthened arms are GREEN.
- a996d4ad30 is NOT an ancestor of the current study HEAD (7eb2ac5421): the flip is not
  receiptable at the study HEAD (the study branch does not carry the battery lineage).
- The audit's G0 verdict "a996d4ad30 is an ancestor of the HEAD" is therefore TRUE only
  about the battery lineage. The brief's (c) check at the current tree returns NOT
  ancestor → the orphan edge's GREEN state is not appliable to the current study head.

## 4. Zero-call-sites / dream_cycle / preserve_session at the current lines

- verify_post_write: 0 occurrences at the current study HEAD (function absent). Its sole
  production call site on the fork is pr-139606:memory_tool.py:366-367 — verified by
  `git show d1bdb4582c:tools/memory_tool.py` (the `from tools.write_gate import
  verify_post_write` + readback call). The audit's G1 verdict "read-back unwired on both
  paths" holds at the study HEAD; the zero-call-site claim holds too.
- dream_cycle bank-line: tools/dream_cycle.py absent at the study HEAD; no
  MemoryStore.bank on any ref (only the FakeStore in tests/tools/test_dream_cycle.py:21).
  The audit's G4 verdict holds.
- preserve_session returns' drop: at the current study HEAD the file is absent; at
  ffb85c2c58, tools/spa_integration.py:104-107 drops both `store.add` return dicts and
  returns `doc_name` unconditionally. The audit's G3 verdict holds (the claim is about
  the spa/dream tree, not the study tree).

## 5. Receipts' hygiene — the matrix's tree-labels

- "study HEAD = bef53e1ebd" is **WRONG** at the current tree: the current study HEAD is
  7eb2ac54217232431816c788caec80f3a288838a. The matrix's other labels hold (battery =
  30f08c2a0f; pr-139606 = d1bdb4582c; feat/140005-spa-dream = ffb85c2c58).
- Line-count ledger at the current study HEAD matches the audit's matrix
  (tools/memory_tool.py 485 ln; agent/context_compressor.py 5825 ln; tools/memory_tool_store.py
  700 ln). The audit's G2 claim "grep DOC_TARGET_PREFIX|doc_name|_resolve_target → empty" at
  the study HEAD also holds.
- The audit's G0 claim "a996d4ad30 is an ancestor of the HEAD" is receiptable only about
  the battery lineage, not about the study HEAD (the study branch does not carry the
  battery lineage). The matrix's "battery = fixes/falsifier-battery-20261104 = 30f08c2a0f"
  label is accurate.

## 6. The verdict — truth-state of the audit's claims

Per claim:
- **G2 misread-class: CONFIRMED** — the audit's misread is TRUE; the prior verification's
  "NOT REPRODUCED" is a false refutation (the guard checks the result of `doc_name(doc)`,
  not whether `doc_name` is callable; the `TypeError` fires before the guard).
- **Battery run counts: CONFIRMED at the battery HEAD** (`28 passed / 1 xpassed / 0 failed /
  0 skipped`); the study's local battery copy diverges (16 passed / 13 skipped) and is the
  only battery-path divergence.
- **Orphan edge: the GREEN-flip is receiptable at the battery HEAD only** (a996d4ad30 is
  an ancestor there; not at the current study HEAD).
- **Zero-call-sites (verify_post_write): CONFIRMED** at the current tree (the function is
  absent at the study HEAD; 0 grep matches).
- **dream_cycle bank-line: CONFIRMED** (no MemoryStore.bank anywhere in the fork).
- **preserve_session returns' drop: CONFIRMED** on the tree that carries it
  (ffb85c2c58 lines 104-107); the file is absent at the study HEAD.
- **Receipts' hygiene: the matrix's study-HEAD label is WRONG** (`bef53e1ebd` vs current
  `7eb2ac5421`); the battery/pr-139606/feat-140005 labels hold.

Aggregate per the dry-run ruler's spirit: the audit's central diagnosis (G2) is
CONFIRMED; its battery-run, zero-call-site, and no-bank verdicts are CONFIRMED at the
current tree; its orphan-edge verdict is receiptable only about the battery lineage;
and its own tree-label ledger contains one error (the study HEAD SHA). The audit's own
reproducibility claims hold at the current tree where they name a reference tree; they
do not transport to the current study head.

## 7. Fold-inputs

The fold must carry:
1. **Proven verdicts** — G2 misread-class CONFIRMED (audit's misread TRUE); battery-run
   counts CONFIRMED at the battery HEAD (28 passed / 1 xpassed / 0 failed / 0 skipped);
   zero-call-sites CONFIRMED (verify_post_write absent at study HEAD); no MemoryStore.bank
   CONFIRMED; preserve_session returns' drop CONFIRMED on the spa/dream tree; orphan-edge
   receiptable at the battery HEAD only.
2. **Open questions** — the study branch's local battery copy diverges (16 passed / 13
   skipped vs 28 passed / 1 xpassed at the battery HEAD): is the study copy the intended
   battery surface, or is the divergence drift? The flip is not appliable to the current
   study head (a996d4ad30 not an ancestor) — the fold must not claim the orphan edge's
   GREEN state at the study HEAD.
3. **Fix-briefs priority order (from the audit, FB-1 … FB-8)**:
   - FB-1/batch read-back (closes G1) — highest; proven false-success reproduces at the
     current tree; the named guard is orthogonal and the read-back is unwired on both
     paths.
   - FB-4/doc_name-None guard (closes G2) — the audit's central misread is CONFIRMED; the
     TypeError class is real at pr-139606.
   - FB-2/add read-back (G1b-1) and FB-3/remove-patch attestation (G1b-2/3) — the
     read-back attestation is not called on either path.
   - FB-5/preserve_session atomicity (G3) — both return dicts dropped at ffb85c2c58:104-107.
   - FB-6/.bank adapter and FB-7/compressor hook (G4) — no landing site on any branch.
   - FB-8/battery count/branch pin (G0) — pin the battery HEAD and quote the counting
     rule; the study's local copy must use the same pin.

Sealed artifacts and the plan are untouched. No public write, no push, no checkout/stash/rm.
