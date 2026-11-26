# THE-CONDITION-MATRIX — analysis notes (the lock-holding conditions)

**Scope.** This is the analysis-lane receipt for kvnloo's reply conditions (RFC comment
7181202866, 11-26 02:53Z). The RUNS live in kvnloo's lab; those runs (his table on the
RFC) are not re-examined here (read-only surface). This note stress-tests the *analysis*:
predictions, contradictions, the lock-order/deadlock theorem, and the lost-add (silent
overwrite) detection. Verdict scale per condition: **SOUND / QUESTION / FALSE**.

---

## A. PREDICTION CONTRACT (per condition)

Each cell is ONE falsifiable sentence: "if X then Y, else the claim's wrong."

- **C1 (anchor lock held through the write):**
  IF the write is the whole-file replace (`atomic_write_text`, the doc-level `_add_doc`
  replace), THEN holding the anchor lock through that write does NOT prevent the second
  add from silently overwriting the first — the race is inside the replace, not at the gate.
  ELSE (C1 is claimed to fix the overwrite) the claim is wrong — a held anchor lock does
  not make a whole-file replace append.
- **C2 (lock released after re-read, before write):**
  IF the re-read is done under the anchor lock and the write happens after release, THEN
  the window is the same race as the shipped gate, only smaller — the interleaving that
  produced "the add lands after a returned removal" survives, just in a slimmer slice.
  ELSE the claim is wrong.
- **C3 (target's lock alone):**
  IF the removing writer only takes `MEMORY.md.lock`, THEN a target lock alone cannot
  serialize against it — the adds are not protected and the race stands as shipped.
  ELSE the claim is wrong.
- **C4 (doc-append under the anchor lock, locked re-read → APPEND):**
  IF the appending path is a true append under the anchor lock and no whole-file replace
  survives, THEN the overwrite class is fixed — but only if the replace has been removed
  from the path; a held anchor lock by itself does not turn a replace into an append.
  ELSE the claim is wrong (append recovers the overwrite only when replace is gone).
- **C5 (current whole-file replace / `atomic_write_text`):**
  IF two adds run at the doc level against a replace writer, THEN the second add silently
  overwrites the first with no refusal and no lost-entry exception — the loss is silent,
  the Windows end state only shows the single entry; NO gate (lock, re-read, or double-gate)
  fixes it because the overwrite happens inside the replace, after any gate has passed.
  ELSE the claim is wrong.

---

## B. PER-CONDITION VERDICT + ATTACK LINES

### C1 — SOUND (as a lock-owning claim; FALSE as an overwrite-fixer)
- **Predicted end state:** adds still land; ordering fixed by the gate (anchor is first
  reader). NO entry lost by the replace-vs-replace class, because the re-read catches the
  removal, and the append under the anchor lock publishes the new entry.
- **Predicted race-window:** if the replace path is NOT removed, the window inside the
  replace (read-then-write of the whole file) remains. The anchor lock held through the
  write prevents *two* writers from interleaving at the OS flock, but a single replace
  writer can still read a snapshot, drop entries, and write back a snapshot — silently.
- **Attack line:** the brief says "the anchor's lock HELD THROUGH THE WRITE" is an agreed
  condition for a reason — the *re-read* is what must see the removal. But the brief's
  own critical-distinction sentence is the attack: anchor-level `add` appends via
  `_mutate`; doc-level `_add_doc` REPLACES the whole doc. A held anchor lock makes the
  append safe from *concurrent* writers; it does not make a replace an append. The claim
  "held through the write" fixes *ordering*, not *content*. C1 alone leaves open the
  replace-within-one-write class: an add+add under one replace still loses one entry
  silently. Verdict: SOUND only if C4's append is the actual publish path and the replace
  is retired; false if C1 is claimed to fix the overwrite by itself.
- **Silent-loss check:** yes, C1-alone leaves the silent-loss class live (the second
  add's values are overwritten inside the replace; no refusal, no exception, no visible
  signal).

### C2 — FALSE (as stated)
- **Predicted end state:** same as C1's ordering benefit (gate semantics), because the
  re-read→release→write ordering produces exactly the shipped interleaving ("the add
  lands after a returned removal"), just slimmer.
- **Predicted race-window:** released *after* the re-read but *before* the write = the
  window that the shipped gate already has (re-read sees removal, release, then write
  publishes). The "smaller window" is a window of the *same shape*, not of a different
  shape.
- **Attack line:** calling it "the same race with a smaller window" is internally
  consistent, but as a *fix* it is FALSE: the read-and-then-write-two-step is the race
  itself. A smaller window does not remove the race; the double-gate (C4) is what tries
  to remove it, and it only works if the publish is a true append.
- **Verdict:** FALSE — the race-window is not eliminated, only narrowed.

### C3 — SOUND
- **Predicted end state:** no help. The removing writer takes `MEMORY.md.lock` only, so a
  target lock (e.g., the anchor) held elsewhere does not serialize the removal.
- **Predicted race-window:** the gate lives in whichever code takes the *anchor* lock at
  the *anchor level*; the removal at the target level races independently. A target-only
  lock cannot see an operation that never takes it.
- **Attack line:** the spec names the exact lock the writer takes; if the writer never
  takes the target lock, a target lock is unreachable for that writer. "Doesn't help
  either" is accurate by construction — the lock is the wrong one, and "the same race"
  is true again.
- **Verdict:** SOUND — a target lock alone is the wrong lock for a writer that takes
  `MEMORY.md.lock` only.

### C4 — QUESTION (strongest candidate, needs the replace to be gone)
- **Predicted end state:** if the path is: locked re-read → confirm no removal → APPEND
  under the anchor lock → publish, THEN end states never lose entries (add lands even if
  the removal raced earlier), and the overwrite class is dead *provided nothing on the
  path does a whole-file replace*.
- **Predicted race-window:** still present in the *re-read* if the append is not itself
  atomic against a concurrent replace: an append under the lock can be overwritten by a
  concurrent whole-file replace that reads a snapshot, and the append's bytes can be
  clobbered by that replace. The lock serializes, but only if *every* path that writes
  the doc (anchor, target, and the replace) takes the *same* lock and none does a
  non-lock'd replace.
- **Attack line:** C4's "append recovers it?" — YES, but only when C5's replace is
  removed from the write path. A lock does not transmute a replace into an append. If
  the replace is still reachable (e.g., a code path stays at `atomic_write_text`), C4's
  append is a no-op against it: the replace's snapshot read happens, the snapshot drops
  the new entry, and the write-back publishes only the old content. The deadlock-possi
  (double-lock) and the non-blocking-flock fallback remain the open engineering costs in
  this class.
- **Verdict:** QUESTION — C4 *is* the fix for the overwrite class in principle, but the
  claim as stated ("append under the anchor lock fixes the silent overwrite") is true
  only if the whole-file replace is removed from the write path; otherwise it is false.

### C5 — SOUND (as the diagnosis)
- **Predicted end state:** the two-add class at the doc level produces a *silent*
  overwrite — the second add's content replaces the first, the file ends with a *single*
  entry, no refusal, no exception, no lost-add signal. The end state kills the claim
  "end states never lose entries" *unless* the "entries" that never get lost are defined
  only at the anchor level and C5's overwrite is excluded by definition from that set.
- **Predicted race-window:** inside the replace — read snapshot, drop entries, write-back.
  The window is *after any gate has passed*, because the gate (re-read) is about order,
  and the replace is a single atomic-ish write that a gate cannot interpose between its
  read and write without holding the lock through both.
- **Attack line:** "NO gate fixes it" is the crux. A gate (lock, re-read, double-gate)
  can fix *ordering* races (removal vs add) but cannot fix a *content* race (replace vs
  replace), because the replace is a read-modify-write of the whole file that discards
  entries by construction. C4's append is the only operation that preserves entries.
  Verdict: SOUND as the diagnosis of the silent overwrite; the "no gate fixes it" claim
  is true for ordering-only gates, and C4 remains the proposed cure, contingent on the
  replace being retired.
- **Silent-loss check:** yes — the loss here is silent because the overwrite happens at
  the doc level and the end state shows the last writer's entry only; no refusal, no
  exception, no error that a harness could flag.

---

## C. THE LOCK-ORDER THEOREM — attack

The claim: "anchor first, then doc; anchor-only + USER.md writes take a single lock —
'no cycle'." Attack points:

1. **Two-lock path (USER.md vs MEMORY.md):** if an operation takes the anchor lock on
   TIME then the doc lock on MEMORY.md, and another operation (e.g., USER.md maintenance)
   takes the doc lock on MEMORY.md then the anchor lock on TIME, THEN the two-lock path
   is a genuine cycle under the *lock-order* rule — a deadlock is possible *if both
   orderings ever occur*. The theorem only holds if every operation in the system agrees
   on the same global order of *all* locks involved. A "USER.md single lock" is not shown
   to be disjoint from the MEMORY.md locks; if USER.md writes can be taken before or
   after MEMORY.md locks, the cycle can close.
2. **Re-entrancy:** an anchor-held re-entrant re-read that then tries to take the doc
   lock while the anchor lock is already held is fine only if the same thread re-enters
   the same lock; if the re-read is a *different* lock domain (e.g., target vs anchor),
   the re-entrancy is not re-entrant and the double-lock ordering is not proven.
3. **Non-blocking `flock`:** a non-blocking acquire (`LOCK_NB`) that falls back to a
   retry or abort breaks the "no cycle" claim: with `flock`'s park-if-busy semantics the
   ordering is guaranteed (a thread waits, not deadlocks), but with `LOCK_NB` and a
   manual retry, a thread can hold lock A, fail to get lock B, release A, retry, and
   *restart the hold of A* — giving the other thread a window to hold B and retry A,
   recreating the two-lock cycle. The non-blocking call is the *weakest* link in the
   deadlock-freedom proof, because the proof assumes a blocking acquire.
4. **Scope of "the doc":** "doc" is ambiguous — if it means `MEMORY.md` and the anchor
   also lives in memory, the theorem's single-lock claim for USER.md vs MEMORY.md mixes
   two different resources. The proof is sound only if the resource graph has a single
   global order and every operation follows it; the two-lock path is where that order is
   stress-tested.

Bottom line on the theorem: the "no cycle" claim is conditional, not unconditional. It is
SOUND only on the strict assumption that every path takes locks in one global order and
that no path mixes blocking/non-blocking semantics inconsistently. The two-lock (USER vs
MEMORY) and `LOCK_NB` paths are where the theorem breaks.

---

## D. THE CRITICAL DISTINCTION — restated for the pair

- **Anchor-level `add`** appends through `_mutate` (or equivalent) — it preserves prior
  entries.
- **Doc-level `_add_doc`** replaces the whole doc — it discards prior entries.
- **The two-add class at DOC level** (two adds, each doing a replace) → silent overwrite,
  NO gate fixes it, because the overwrite happens *inside* the replace, after any gate
  has passed. C1 (held anchor lock) fixes the *concurrent-write* race but not the
  *replace-within-one-write* class. C4's append recovers the overwrite *only if* the
  replace is removed from the write path; C1 alone leaves that class open.

---

## E. THE TABLE AGAINST THE ANALYSIS (form-check)

- serial add→remove → doc exists, unreferenced: SOUND (order is preserved; content is
  the question).
- serial remove→add → refused: SOUND as a gate claim; the "refused" is the gate, not the
  lock.
- interleaved gate-as-shipped → 10/10 the add lands after a returned removal: SOUND as a
  race analysis; the 10/10 is the race, the fix is the double-gate (C4), which changes
  the interleaving, not the end-state rule.
- interleaved anchor-held → 10/10 B waits: SOUND as an ordering claim (B waits for the
  anchor lock). "End states never lose entries" holds *only* when the publish path is a
  true append (C4) AND no replace remains on the path; the table's "never lose" is
  contingent.

---

## F. VERDICT SUMMARY

| Condition | Verdict | One-line |
|---|---|---|
| C1 | **SOUND** (lock claim); **FALSE** as overwrite-fixer | Held anchor lock fixes ordering, not content; the replace remains |
| C2 | **FALSE** | Released after re-read = same race, narrower window |
| C3 | **SOUND** | Target lock alone is the wrong lock (writer takes MEMORY.md.lock) |
| C4 | **QUESTION** | Append under anchor lock fixes the overwrite only if the replace is retired |
| C5 | **SOUND** (diagnosis) | The silent overwrite is real; no ordering gate fixes a replace-vs-replace |

**Lock-order theorem:** CONDITIONAL — sound only under a single global lock order across
all paths; the two-lock (USER.md vs MEMORY.md) and non-blocking `flock` paths are the
open attack lines.

**Prediction contract one-liner:** "if X then Y, else the claim's wrong" is the receipt;
the labs run the pins (a9c65dc4 / 268bb091 / 268bb091-append) as they choose, and this
lane's verdicts are the analysis's receipts, not the runs.
