# HY-GATE-MISSION3-20261122 — MISSION-3's FINAL RUNG: the approve-or-reloop gate on the falsifier/gap-audit

*Seat: tencent/hy4-flash:free — PIN-READ-BACK VERIFIED at the fire. Brief: `plan/tank/briefs/BRIEF-HY-GATE-MISSION3-20261122.md` (read in full — the contract). Chain: AUDIT (longcat, 7eb2ac5421 — the gaps × claims matrix) → SANITY (solar, 02803d14b2 — the audit's own claims re-derived, one label corrected) → FOLD (§7-ak, 1f79c62907) → **THIS GATE**. This rung alters NEITHER the plan NOR any artifact; the verdict seals or returns the mission.*

*Armament: think-tank (spine) + agent-work-review + investigation-documentation — loaded and used; the rest named-and-refused (an unarmed lane would be a finding). Anchor: `/root/.hermes/memories/MEMORY.md` + `USER.md` read; GATE LAW's final form — the word gates ONLY public writes outside PR #1 plus deep deletions/money; internal doors act, never wait.*

---

## 1. VERDICT

**APPROVE.** The fold-in is complete: **13/13 carriers present in §7-ak, 0 dropped, 0 blurred.** MISSION-3 seals. The fix-briefs' priority order rides the main pilot-readiness improver loop's next pass, with the lost-write false-success's falsifier FIRST (FB-1, the read-back's real wiring). No reloop scope.

---

## 2. THE REASONING (the spine)

A final gate is a second pair of eyes, not a full redo. I re-read the arc in order — the audit, the sanity, the fold §7-ak, and the two raw rows byte-for-byte — then checked the one thing only a gate can check: that the arc's honesty survives the fold intact.

It does, and the load-bearing reason is this: **the fold carries the study's own most uncomfortable refutation as faithfully as its receipts.** The headline round-two claim — *"the bypass class does not reproduce here"* — was refuted at the tree (the 1-item `operations=[patch]` lost-write false-success reproduces at the battery branch **and** the study HEAD; `verify_post_write` is defined but called from zero production sites). The audit says so in its strongest catch; the sanity re-derives it; §7-ak carries it verbatim: *"the strongest catch: the headline 'the bypass class does not reproduce here' does not reproduce."* A fold that had smoothed this into the operator's closure claim would have been the failure. It did not.

The same fidelity holds on the audit's own error. The sanity found one wrong label in the audit's tree register — `study HEAD = bef53e1ebd` (the real head at that rung was the audit's own commit `7eb2ac5421`) — and §7-ak does not bury it: *"the audit's receipts' hygiene: ONE error — the matrix's 'study HEAD = bef53e1ebd' mislabel (current: 7eb2ac5421), corrected."* The falsifier was applied to the falsifier, and the correction survived the seam. That is the tree-is-the-truth discipline turned on the study itself.

The three genuinely open items are carried as questions with receipts, never laundered: the study branch's local battery copy diverges (`16 passed / 13 skipped` vs the battery HEAD's `28 passed / 1 xpassed`, the `_read_substrate_guard` fixture dropped); the orphan edge's GREEN state is receiptable at the battery HEAD only (`a996d4ad30` an ancestor of `30f08c2a0f`, **not** of the study head); the prior `XNGG-GAPS-VERIFICATION` row 2 is a false refutation (the guard checks the *result* of `doc_name(doc)`, not its callability). §7-ak carries all three by name — the divergence as "the batched open question (the divergent local battery copy's provenance)," the orphan edge as "receiptable at the battery HEAD only," the misread as "row 2 = a MISREAD." Under the wall clause a non-reproduction is a QUESTION with receipts, and under the GATE LAW an internal question does not wait on the word. These ride the readiness loop's next pass; they are not reloop triggers.

At the tree, read-only, the corrections check out: `7eb2ac5421`, `02803d14b2`, `1f79c62907` are sequential commits on the study branch (audit → sanity → fold), `bef53e1ebd` is a distinct earlier commit, and `git grep verify_post_write HEAD -- tools/` returns nothing (the function is absent at the study head's tools, confirming the zero-call-site receipt). The gate-time head (`597d4d198a`) is a later, unrelated ARM-0 weights-rung fire that landed *after* the fold; it does not falsify the sanity's time-bound label claim. No public write, no push.

---

## 3. THE FOLD-IN COMPLETENESS CROSSWALK (§2(a) — the double-check)

Each element the arc produced is re-located in §7-ak. PRESENT = carried with meaning intact (not dropped, not flattened, not blurred).

| # | Element (as the arc produced it) | In §7-ak? | Carried content (verbatim or faithful) |
|---|---|---|---|
| 1 | G1 — batch bypass REFUTED-as-claimed (empty-ops guard real but orthogonal; 1-item `operations=[patch]` lost-write false-success reproduces at battery + study HEAD; `verify_post_write` defined, ZERO call sites) | PRESENT | "G1 the batch-path bypass REFUTED-as-claimed (the empty-ops guard real but orthogonal; a 1-item operations=[patch]'s lost-write false-success reproduces at the battery branch AND the study HEAD; verify_post_write defined but called from ZERO production sites)" |
| 2 | G1b — CONFIRMED-as-stated, NOT CLOSED (store semantics as claimed; read-back attestation a different rule, unwired) | PRESENT | "G1b CONFIRMED-as-stated, NOT CLOSED" |
| 3 | G2 — CONFIRMED at the pin, operator's fix ABSENT at the study HEAD (TypeError/AttributeError reproduce) | PRESENT | "G2 CONFIRMED at the pin, the operator's fix ABSENT at the study HEAD (the TypeError/AttributeError reproduce)" |
| 4 | Misread-catch — prior `XNGG-GAPS-VERIFICATION` row 2 is a false refutation (checked the result, not the callability) | PRESENT | "the prior XNGG-GAPS-VERIFICATION row 2 = a MISREAD (checked the result, not the callability)" |
| 5 | G3 — REFUTED (both `store.add` return dicts dropped; dangling-pointer classes open) | PRESENT | "G3 REFUTED (the returns dropped; the dangling-pointer classes open)" |
| 6 | G4 — REFUTED (no `MemoryStore.bank` on any ref; compressor hook 0 landings) | PRESENT | "G4 REFUTED (no MemoryStore.bank on any ref; the compressor 0 landings)" |
| 7 | G0 battery stale-claim inversion — "21 tests" STALE (unsourced; real run `28 passed / 1 xpassed / 0 failed`) | PRESENT | "the battery's 21-tests claim STALE (the real run: 28 passed / 1 xpassed / 0 failed; ...)" |
| 8 | Local-copy divergence (sanity's new find): study copy `16 passed / 13 skipped`, `_read_substrate_guard` fixture dropped | PRESENT | "PLUS the new divergence: the study's local battery copy DIVERGES (16 passed / 13 skipped — the _read_substrate_guard fixture dropped)" |
| 9 | GREEN-at-battery-head — orphan edge GREEN not RED; `a996d4ad30` ancestor of `30f08c2a0f`, NOT the study head; true @06:26Z, false by 06:58Z | PRESENT | "the orphan edge GREEN, not RED — the whole-anchor resolution landed, an ancestor of the battery HEAD — true at 06:26Z, false by 06:58Z" + "the orphan-edge receiptable at the battery HEAD only (a996d4ad30 an ancestor of 30f08c2a0f, NOT of the study HEAD)" |
| 10 | Corrected label — matrix's `study HEAD = bef53e1ebd` mislabel → current `7eb2ac5421` | PRESENT | "the audit's receipts' hygiene: ONE error — the matrix's 'study HEAD = bef53e1ebd' mislabel (current: 7eb2ac5421), corrected" |
| 11 | Fix-briefs' priority order — FB-1 (lost-write false-success's falsifier) FIRST, the read-back's real wiring | PRESENT | "the fix-briefs' priority order (the lost-write false-success's falsifier FIRST — the read-back's real wiring)" |
| 12 | Frame's 0-public line | PRESENT | "The frame: 0 public writes" |
| 13 | RFC-quiet carrier — the round-two claims' partial refutation rides the PR + the study record until the operator's word; the RFC is the gated class | PRESENT | "the RFC's upstream surface QUIET (the round-two claims' partial refutation rides the PR + the study record until the operator's word — the RFC's the gated class)" |

**Crosswalk count: 13/13 PRESENT · 0 dropped · 0 blurred.** Precision note (nothing smoothed): §7-ak is a fold index line — it names the fix-briefs' priority order and its FIRST item, and names the stale-claim inversion with the real run; the full FB-1…FB-8 enumeration (audit §3), the `def test_` count-rule pin (audit G0 / sanity §0), and the divergence's exact provenance question (sanity §7-2) live in the artifacts it references. Carrying the pointers with their load-bearing content is the settled fold form, not a drop.

---

## 4. THE AUDIT/SANITY PAIR'S COHERENCE (§2(b))

| Check | Result |
|---|---|
| Label-error fix checks out at the tree | **YES.** `7eb2ac5421` is a real commit on the study branch and the audit's own landing; the chain audit → sanity → fold is sequential. `bef53e1ebd` is a distinct earlier commit. The sanity's correction is legitimate and is carried in §7-ak (crosswalk #10). |
| Zero-call-site receipt | **COHERENT.** Audit: `verify_post_write` defined but called from zero production sites (sole production site `pr-139606:366-367`). Sanity: function absent at the study head, `grep` → 0; read-only gate re-check `git grep verify_post_write HEAD -- tools/` → empty. No contradiction. |
| Battery counts | **COHERENT.** Audit `28 passed / 1 xpassed / 0 failed / 0 skipped` at the battery HEAD; sanity re-run confirms; "21 matches no commit" holds in both. (Gate is second eyes, not a third battery run.) |
| Orphan-edge ancestry | **COHERENT refinement, not contradiction.** Audit's "ancestor of the HEAD" is scoped by the sanity to the battery lineage (`a996d4ad30` ancestor of `30f08c2a0f`), not the study head — carried that way in §7-ak. |
| No-bank / returns-drop / G2 misread | **COHERENT.** All three confirmed at their named trees by the sanity; no sanity claim contradicts an audit proven receipt. |
| Handshake's integrity | **The audit's single error is its own study-HEAD label; the sanity corrects it, and §7-ak carries the correction.** No blurred or dropped receipt, no contradictory claim. |

---

## 5. THE FRAME'S ADHERENCE LINE (§2(c))

- **0 public writes** — verified at the wire: `7eb2ac5421`, `02803d14b2`, `1f79c62907` each touched one `studies/rfc-143379-rig/` path only (`git show --name-only`); no push. This rung writes one study path only, no push.
- **RFC #143379 upstream QUIET** — the round-two claims' partial refutation rides PR #1's thread + the study record until the operator's word; the RFC is the gated class, flagged internally only.
- **No pilot contact** — the field pilot's channel is the operator's, held.
- **GATE LAW (final form, MEMORY.md:19):** the word gates ONLY public writes outside PR #1 plus deep deletions/money; internal doors act, never wait. This verdict is an internal door — it acts.

---

## 6. RELOOP SCOPE

**None.** APPROVE. The fix-briefs' priority order rides the readiness loop's next pass, FB-1 (the lost-write false-success's falsifier — the read-back's real wiring) FIRST. The divergent local battery copy's provenance (study copy `16 / 13` vs battery HEAD `28 / 1x`) rides as a named open question to that same next pass — carried with receipts in §7-ak and in the sanity's fold-inputs, hence a next-pass ask and not a fold-gap (the MISSION-2 gate precedent: a question carried with receipts = APPROVE, not RELOOP). The fold-in itself returns nothing.

---

## 7. THE STRONGEST REASONING LINE

The fold carries the study's own most uncomfortable refutation as faithfully as its receipts — the headline "the bypass class does not reproduce here" is recorded as *not reproducing*, and the audit's single error (the study-HEAD SHA) is corrected rather than smoothed, all the way into §7-ak. That is tree-is-the-truth applied to the study's own claims, intact end-to-end from the raw rows to the master. MISSION-3 seals.

---

*Facimus semper — the gate reads the record, the record answers to the bytes, the bytes hold. — kanban-pilot*
