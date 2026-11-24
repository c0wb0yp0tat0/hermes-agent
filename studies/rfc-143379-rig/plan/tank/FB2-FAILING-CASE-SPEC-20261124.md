# FB-2 FAILING-CASE SPEC — the pre-registration (promised in full)

*STUDY LANDING ONLY. Nothing in this document posts to RFC #143379 or any public surface without the operator's word. The reserve's audit gates the posting; this spec lands here first so a stranger can execute it cold. Fire date: 2026-11-24. Branch: `study/rfc-143379-rig-20261105`. The thread promise this discharges is row 7122688366 (2026-11-24 05:10Z); KvNloo's acceptance to run nothing on MAIN until the spec is on the thread is row 7122500729.*

**What this artifact is:** the pre-registered failing-case specification for FB-2. It fixes, in advance, the named failing case, the expected failure signatures on the ungated tree and on the fix, the removal control, one hold-back class, the three probe pins, and the four acceptance conditions. KvNloo replies base-red / combined-green / single-add removal control at these pins; divergences are data, not a renegotiation of the bars.

**How to read "red" and "green" here:** RED = the pre-registered failure signature was observed (the bug is present and the probe caught it). GREEN = the pre-registered failure signature was absent (the first doc survived). A GREEN on the ungated tree, or a RED on the fix, or any RED on the removal control, is a divergence — record it as data, do not retrofit the bar.

---

## 1. The failing case — name and statement

**Name: FB-2 — second chain-doc `add` overwrites the first.**

A chain-doc memory store holds named documents under a single chain file. In the ungated implementation the `add` action routes to `_add_doc`, and `_add_doc` writes the note's `content` as the **whole file** rather than appending it as a new record. Consequently, when a second chain-doc `add` is issued — whether a normal follow-up add or an add made while over the document/character budget — the second write replaces the file wholesale, so the first document's bytes are gone and the store now contains only the second document's bytes. A recovery re-read of the first document therefore returns nothing of the first note (or the second note's content under the first note's name), never the original first-note body. The 297-test battery at the class's home pin passes in full and does **not** cover this two-add sequence — that gap is the reason FB-2 is named as its own falsifier. Our own verbatim execution of the `_add_doc` body against a temp directory confirmed the clobber (`FIRST_SURVIVED_SECOND_ADD=False`, receipt `VET-KVNLOO-20261122.md`, commit `9ce4e0078c`), so the class is REAL before any MAIN run.

---

## 2. Expected failure signature — ungated add on MAIN

**Pins to probe (both are in scope for this arm; report each separately):**

- `268bb09147eaf948ece6a1beecd92a2268a5fc95` — `round2-gate`, the **home of the class** (297/297 green, race red; the two-add lives here).
- `0f602c5f` — **MAIN read-less baseline** per KvNloo's matrix row 7087999804 (his battery 409 pass while `read` answers `Unknown action 'read'` on MAIN). On this pin the `read` action is absent, so the recovery observation must be made at the store/file level (read the chain-doc file directly) rather than through a `read` tool call; if the runner attempts a `read` action here the expected auxiliary observation is `Unknown action 'read'`.

**Procedure (ungated arm):** at each pin, in a fresh temp store, (a) `add` a first chain-doc with a unique, marker-bearing content body — call it FIRST; (b) `add` a second chain-doc with a different unique body — call it SECOND; (c) perform a recovery re-read of FIRST's key (a `read` action where that action exists, otherwise a direct file read of the chain-doc file); (d) compare the recovered bytes to FIRST's original body.

**Exact expected observation (the RED signature):**

- `FIRST_SURVIVED_SECOND_ADD = False` — FIRST's bytes are absent from the recovered document.
- The chain-doc file after the second add contains SECOND's content where FIRST's content had been; the add behaved as a whole-file overwrite, not an append.
- On `0f602c5f` specifically, a `read` action issued for recovery returns `Unknown action 'read'`; use the file-level read to record the clobber and note the read-less baseline separately.

**Load-bearing path:** `tools/memory_tool_store.py:580-618` at `268bb091` — `_add_doc` assigns the new note's `content` to the whole file. The write is an overwrite of the file object, which is why the second add erases the first rather than chaining it.

> **RE-DERIVE marker (write-window gating, see §8):** the exact source bytes at `:580-618` were NOT re-read this pass — the write-window gated terminal content-reads before the verification commands could run. What is recorded here is the line range and the recorded shape of the write (whole-file `content` assignment). The runner must re-derive the verbatim lines with:
> `git show 268bb09147eaf948ece6a1beecd92a2268a5fc95:tools/memory_tool_store.py | sed -n '575,622p'`
> and confirm the assignment is a whole-file write before treating the line quote as settled. A line that reads differently than recorded is a QUESTION to be resolved by re-derivation, never a silent edit of the spec.

---

## 3. Expected failure signature — same case on THE FIX

**Pin to probe:** the combined tree `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` (equivalently the composed tree `ec649ad9` in KvNloo's matrix — MAIN + #116673 + #141876). This is the GREEN reference.

**Procedure (fix arm):** identical to §2 — same two chain-doc adds with the same marker-bearing FIRST and SECOND bodies, same recovery re-read, same byte comparison — executed on the combined tree.

**Exact expected observation (the GREEN signature):**

- `FIRST_SURVIVED_SECOND_ADD = True` — FIRST's bytes survive the second add; both documents are present and FIRST's body byte-matches what was written.
- The store is locked and stateless across the two adds and the read is sanitized: the three arms of the fix are present in `tools/memory_tool_store.py` at this pin — `_file_lock` (serializes write/read), `_sanitize_entry` (sanitizes on read), and a hardened `def read` (the #141876 no-cache-write/sanitized-read path). Removing either the lock or the no-cache-write alone stays green; removing both turns red — that is the class's definition, re-derived in the probe matrix and in `VET-KVNLOO-20261122.md`.
- GREEN is the expected state here. A RED on the fix is the **probe's own catch**: record it as a divergence (do not declare the fix broken on a single RED without checking the control arms in §4 and §7).

> **RE-DERIVE marker:** the three-arm grep at `a9c65dc4` was NOT re-run this pass (write-window gating). Re-derive with:
> `git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tools/memory_tool_store.py | grep -n "_file_lock\|_sanitize_entry\|def read" | head`

---

## 4. The removal control — single-add arm

**Procedure (control):** on **each** of the three pins (`0f602c5f`, `268bb09147eaf948ece6a1beecd92a2268a5fc95`, `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`), issue exactly **one** chain-doc add with a unique marker-bearing body, then re-read that document and byte-compare it to what was written.

**Expected observation:** GREEN on all three pins — the single add's content round-trips intact. There is no second add, so the overwrite path of §2 is never exercised.

**Ruling:** a RED on any control arm **invalidates the probe**, never the finding. If the single-add arm is RED, the two-add result is not interpretable (the harness may be mis-wired, the pin may be wrong, or the store may be failing for an unrelated reason) — re-run the control before drawing any conclusion from the failure arms. The control is the probe's own falsifier; pre-registration requires it to be reported alongside every base-red / combined-green pair.

*(Distinct from this control: the lock/no-cache-write single-removal arms in §3, which are expected to stay green and are part of the fix's definition, not the probe's validity check.)*

---

## 5. HOLD-BACK class — WITHHELD until the operator's word

> ### BEGIN HOLD-BACK — DO NOT PUBLISH THIS BLOCK OR ITS EXPECTED SIGNATURE
>
> **Withheld class: the BATCH-PATH double-add** — two chain-doc adds delivered through the store's batched/bulk add path (as opposed to the two sequential single adds in §2/§3). Whether the batch path reuses the same whole-file write, deduplicates by key, or serializes differently is a distinct mechanism from FB-2's sequential clobber.
>
> The expected failure signature for this class is **deliberately NOT specified in this document's spec fields** (§2–§4). It is named here only so the head can withhold it from the published surface until the operator's word. This is the class that keeps a leading hint from satisfying the probe on its own: a runner who guesses the answer from the sequential case must not be able to carry that hint into the batch case, because the batch case's bar is not written down where the runner can read it.
>
> Release condition: operator's explicit word, after which the head may extend the spec with this class's signature and its own pins. Until then this block is study-internal only.
>
> ### END HOLD-BACK

---

## 6. Pinned SHAs — the pins a runner will probe

| Role | Pin | Status in the record |
|---|---|---|
| MAIN read-less baseline | `0f602c5f` | MAIN head per KvNloo's matrix row 7087999804; `read` = `Unknown action 'read'`, his battery 409 pass |
| Class's home (`round2-gate`) | `268bb09147eaf948ece6a1beecd92a2268a5fc95` | 297/297 green, race red; the two-add class lives here |
| Combined fix (GREEN reference) | `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | locked, stateless, sanitized read; equivalently composed `ec649ad9` (443 pass, dispatch contract 64/64) |

**Supporting pins (context, not probe targets):** `60a2e156` (#116673, red on race, own 16/16); `b6ff7dae` (+single commit, green 17/17 — **record-cited from KvNloo's matrix row 7087999804; does NOT resolve in this tree, RE-DERIVE from the record before citing**); `ec649ad9` (composed tree); `9ce4e0078c` (our reproduction commit, `VET-KVNLOO-20261122.md`).

**Verification status — RESOLVED by the reserve's audit (2026-11-24, `FLEET-AUDIT-LONGCAT-20261124.md`):** the flagship's write-window left the three target pins RE-DERIVE-marked; the reserve ran the verification and all three (plus `9ce4e0078c`, `60a2e156`, `ec649ad9`, `af16e3ab16`) RESOLVE in this tree:

```
$ git rev-parse --verify 268bb09147eaf948ece6a1beecd92a2268a5fc95
268bb09147eaf948ece6a1beecd92a2268a5fc95     # RESOLVES
$ git rev-parse --verify a9c65dc43db9000e8b6e238b50916aa6fa32ff08
a9c65dc43db9000e8b6e238b50916aa6fa32ff08     # RESOLVES
$ git rev-parse --verify 0f602c5f
0f602c5f6f18615632535251d62a2db74ce93b69     # RESOLVES
```

`0f602c5f` resolved to its full form `0f602c5f6f18615632535251d62a2db74ce93b69`. `b6ff7dae` returns `fatal: Needed a single revision` — it is the one non-resolving pin; the removal-control pre-fix leg must re-derive from R2's record row before running (RE-DERIVE marker, do not substitute). A pin that fails to resolve is a QUESTION to be resolved by re-derivation, not a reason to drop the arm.

---

## 7. The condition section — the four pre-registered acceptance rows

These are KvNloo's acceptance rows, pre-registered as measurable properties rather than adjectives (recorded in the head's reply to him, `KVNLOO-REPLY-FINAL-20261123.md` / `REGROUP-COMPLETE-20261123.md` §Three). Each row carries its one-line pre-registered bar. The bars are fixed before the run; divergences are data.

| # | Condition | Pre-registered bar (one line) |
|---|---|---|
| C1 | Survival across four compactions, verbatim | 100% of pinned constants survive four compactions byte-verbatim, with **RED on MAIN / GREEN on the branch** and the **removal control RED** — one pinned constant lost, or any arm flipped, fails the row. |
| C2 | Stated cap with plain refusal, no eviction | Declaring a max entry count and adding beyond it yields a plainly reported refusal with **no eviction and no silent eviction-by-summary** — a dropped entry or a silent overwrite fails the row. |
| C3 | No second store (decision-ledger entry, byte-compared) | Exactly one pin entry in decision ledger **#113309**, byte-compared against the ledger's own schema with nothing invented — a parallel store or a schema mismatch fails the row. |
| C4 | The contradiction-flagged row — KvNloo's proposed 4th, **accepted as written** at row 7122688366 | Carry his proposed fourth condition **as written, flag and all**: do not silently resolve or drop the flagged contradiction; reproduce it as stated and record the flag in the receipt. **Verbatim recovered 2026-11-24 (head-side read of row 7122688366 — the lane's 404 was a token/route artifact):** "the pin is a second witness the summary does not author, and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it. The ledgers move with your rebase, KoNit-K's authorship kept, /pin stacked as its own commit." |

**Note on C4:** closed — the verbatim text is recovered and quoted above; the RE-DERIVE marker is retired. The bar (accepted-as-written, contradiction flagged, pin as second witness) is fixed.

---

## 8. Verification / wall record — what could not be re-derived this pass, and the minimal move

Per the Wall Clause, a non-reproduction is a question with a constructed resolution, never a stop and never a bare "couldn't reproduce."

- **Pin verification (§6):** `git rev-parse --verify` on the three target pins was NOT run by the flagship — the write-window gated terminal content-reads before the artifact existed. Minimal move: exact commands are written into §6 for the runner; pins are quoted from the brief's known ground with a RE-DERIVE label rather than asserted as locally verified. **RESOLVED 2026-11-24 by the reserve's audit** — the three pins (plus `9ce4e0078c`, `60a2e156`, `ec649ad9`, `af16e3ab16`) all resolve in this tree; receipts in §6 above. `b6ff7dae` remains the one non-resolving pin, record-cited only (RE-DERIVE before the pre-fix leg).
- **`_add_doc` verbatim lines (§2):** `git show 268bb091:... | sed -n '575,622p'` was NOT run this pass; the line range and whole-file-write shape are recorded from the brief, not from re-read bytes. Minimal move: exact command in §2; no source lines are fabricated.
- **Fix's three arms (§3):** the `a9c65dc4` grep was NOT re-run; the three arm names are recorded from the brief/matrix. Minimal move: exact command in §3.
- **C4 verbatim text (§7):** not present in the local tree at the fold. Minimal move: re-derive from thread row 7122688366; name it in the receipt, do not fabricate. **RESOLVED 2026-11-24 (head-side read of the row — the lane's 404 was a token/route artifact, not a wall):** the verbatim is quoted in §7 above; the RE-DERIVE marker is retired.
- **`b6ff7dae` (the removal-control pre-fix leg):** the grafted 40-hex withdrawn at the loop-2 fold; 8-hex record-cited. **RESOLVED 2026-11-24:** the real full form is `b6ff7dae98d19f565764e773e0da96aaee18fbf2` — "fix(memory): serialize chain-doc reads with writes", parent `60a2e156` (verified ancestor), live on the fork's `refs/heads/salvage/pr116673-hoss2`, fetched and `cat-file`-verified locally. The removal-control pre-fix leg now has its resolvable base; its RE-DERIVE marker is retired.

None of these gatings changes the pre-registration: the bars in §§2–4 and §7 are fixed and cold-runnable; the re-derive commands make every borrowed number checkable by the runner at the pin. When the write-window closes, the head should execute the three commands above and append the resolved outputs to this file before any posting — but no posting happens without the operator's word.

---

## 9. Run envelope and receipts

- **Nothing public:** this spec is a study landing. RFC #143379's issue surface stays QUIET. PR #1's thread is the only row surface, and only the head rows post — and only on the operator's word.
- **Local reads only:** `git show` / `read_file` / `git log` / `git rev-parse`; no web retrieval, no installs, no battery fire (this lane specs the probe; it does not run one).
- **No shared-tree mutation:** no `git checkout --`, `git stash`, or `git rm -rf` on shared files; the master is append-only. Probes run in fresh temp stores at the pinned trees.
- **Track the branch honestly:** the branch is shared with a sibling's archiver; the tracking ref can lie — `ls-remote` first, per fold.
- **No invented gates:** the only true gates are the fold-push at the wire's all-clear and the operator's word on public writes.
- **Receipt shape:** every claim above carries its pin + line/range or its thread row; divergences are recorded as data beside the bar they diverge from.

*Prepared as the STUDY pre-registration. Reviewed against the local record; unverified items carry RE-DERIVE markers rather than asserted certainty.*
