# ENRICH-1 — MERGE-READINESS PACKAGE (chair-gated: stage only, nothing public)
**Prepared:** 2026-11-14 · **Lane:** apex-enrichment (merge-readiness for the read-restore fix) · **Gate:** chair decides; this package never crosses public on its own
**Head-receipt source:** R1 decision-prep (`READ-RESTORE-DECISION-PREP-20261114.md`, read once) + RFC-143379-RECORD §82 hold comment (comment 6787192097, 11-11) + the door's live state verified OPEN/unmerged via gh.
**Labels/stamps:** all receipts tagged HEAD-RECON / IN-LANE / BORROWED as noted.

---

## 1. THE ACCEPTANCE BATTERY

The testable definition of "**the read-restore landed right**" = the substrate's read-action battery is RED-turned-GREEN on #141876's head (the fix), with the schema-safe doc-chain bounded read and the memory path's existing ops untouched. Four checks:

**A. The 6/6 fabrication repro (red→green) against a SCRATCH store.** Per R1's record reproduction: on current main, the read path is absent and the agent fabricates `6/6` (reproduced ×2); against #141876's head, the same prompts yield clean grounded refusals. Runnable spec (machine-side, run by the chair):

```
# scratch store
mkdir -p /tmp/r1-scratch && cd /tmp/r1-scratch
git clone <#141876 remote @ af16e3ab16> repro-read-restore && cd repro-read-restore
# rebuild substrate with the restore head
# run the R1 repro battery (6/6 prompts) -> expect: clean grounded refusals, 0 fabrications
```

**B. The 12/12 clean-refusal repro** — a second, larger prompt set under the same scratch-store harness, identical class (embedded vs. permission-free access to a persistent store; without the read path the agent fabricates, with it the refusal is clean). Same command form as A; green = zero fabrications across all 12.

**C. The restore's head-returns-entries check** — `MemoryStore.read` (the 12-line method, #141876 :369) against the same scratch store returns the entries plus the usage line, first try (verified by a reviewer's execution, jfugalde, 10-24; in-lane receipt). Spec: run `MemoryStore.read` on a populated scratch store and assert the entry list + usage line appear, no collection error.

**D. The schema-safe edge (the doc-chain bounded read)** — #116673's bounded read: an anchored MEMORY.md doc chain is read with bounded scope; the head claim must be the verified current head `60a2e15638` (FINAL5 note #3). Spec: run the bounded-read harness on a populated doc chain and assert the chain anchor is returned with schema-safe bounds — no unbounded read, no body rewrite (out of scope per RFC §scope).

**E. The non-regression line (memory path's existing ops unchanged)** — the four hand-back sites (~30 lines in `tools/memory_tool_store.py` + the `_validate_single_op` echo in `tools/memory_tool.py`) are explicitly NOT claimed to be deleted by #141876 as scoped ("whether each then deletes or stays as defensive UX is the dive the owning work must do, not a claim to land in the body"). Spec: run the existing memory-path tests (write-then-read 200/200, concurrency 800/800, idempotence 100/100, over-budget 20/20, over-budget reroute-to-chain-doc seam) on #141876's head vs current main; the pass rates must be identical — a regression is any change in those baseline rates.

**Battery totals:** 12 steps (6 red→green + 6 green), all against a scratch store, all machine-side. Estimated cost: ~10 min setup + ~40 min run (R1's two log-files are cited as the receipts of the repro, not re-run).

---

## 2. THE VEHICLE RECOMMENDATION

**One anchor + one tie.** Anchor = **#141876** (the memory `read` restore, head `af16e3ab16`), the read-restore PR named in hold comment 6787192097 and the fix whose substrate is RED today. The bounded read (**#116673**, head `60a2e15638`) is tied to #141876's acceptance battery (check C above): it is the active read-path proposal whose acceptance the restore's landing must carry, exactly as R1's own recommendation shape holds status rather than the brake. Both verified OPEN/unmerged via gh at HEAD-RECON.

**#11548's role** (minimal dispatcher, branch `fix/116564-descr` @ `d3a6e577`): dispatch bootstrap, not read. It is the minimal routing that the doc-chain + restore claims sit on top of; it is NOT the read fix and it does not carry the acceptance battery. Recommendation to the chair: keep #11548 as a dispatch-bootstrap merge, independent of the read battery — its merge does not gate the read decision, and the read decision does not gate its bootstrap.

**Shipping shape (one PR, one battery, one label change P4→P2):**
- Single PR = #141876 only (the restore is the centerpiece the body names; the RFC itself sits P4 and is two bands below the queue).
- One acceptance battery = the five checks above.
- One label change = RFC's P4→P2, per the record's own triage (P2 at birth, 10-23 03:36Z; P4 the residue of the P2→P3→P4 trail).

**Split-shape (per-vehicle ships):** #141876 ships on its own battery; #116673 ships on #141876's battery as the tied bounded-read acceptance; #11548 ships untied. The recommended shape is the single-anchor — the artifact is order-of-magnitude simpler to chair, the label change lands once, the hold's condition (read-restore landing) is met in one shot.

---

## 3. THE CHAIR PACKAGE (one page)

**The wound (3 lines):** the read action was removed in `56ee8a5cc6` (2026-02-19, 14-line deletion); on current main the tool answers `Unknown action 'read'`; the memory path compensates with 6,275 lines (106 commits) because the store cannot be read. The user repeats; the record's provenance depends on workarounds. The restore is the single ~12-line method that collapses the compensation.

**The evidence (cited to R1):** the record (THE FULL-RFC GROUND: BODY + 37-comment thread): the label trail — P2 at birth → P3 → P4 (P2 removed → P3 added → P4 added → P3 removed), six category moves without a substance change, verified screenshot-verified; the queue shape (11-11 exact counts: P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173) — the RFC sits two bands below the queue's working range; the fabrication class 6/6 and 12/12 reproduced on our substrate (R1); the four-sites/~30-lines compensation subset; #141876 already P2 in repo triage. The hold (comment 6787192097): "holding for the read-restore PR (#141876)… if the fix does not land soon, we will discuss alternatives."

**The options (R1's A/B/C condensed):**
- **A — Restate the hold with the battery attached:** the chair keeps the hold, the read decision is deferred until the acceptance battery passes on #141876's head; the open question is the archive-before-stub ordering (one-way door).
- **B — Ship the split:** #141876 merges on its battery (P4→P2 label follows the body), #116673 rides it, #11548 stays bootstrap. 
- **C — Rescope:** the read question splits into the four sites' dependency question (per door §8: "if the read disagrees, I'd want to know which of the four sites is the actual dependency"), with evidence offers accepted.

**The acceptance battery's size:** 12 runs (6+6), ~40 min compute on a scratch store; no headless runs, no network changes, no public side effects. The hold's condition is met deterministically by the battery — the chair decides by the numbers, not by opinion.

**The word-gate note:** this package crosses to the public ONLY on the operator's word. The move is binary: restate the hold with the battery attached (A), or ship the split (B). Nothing posts today.

---

## 4. THE RISK REGISTER

**Stalled merge cost:** R1's extrapolation — the drift class at the full-history scale (~40,094 issues) is ~17,240 (2.36× the open-only estimate); ~190 issues arrive/day against ~43/day closing → net-growing backlog (16,878 open today, oldest open 234 days); 897 issues touched in the last two days. If #141876 does not land, the drift class (a fifth of the P4 bucket before memory/context/compression labels) keeps compounding behind the 6,275-line workaround — "the drift's the compounding, not the clearing." The door's own hold comment names the consequence: indefinite hold → community discussion, not delay.

**Rushed merge cost:** regression on the memory path — the four hand-back sites (~30 lines) and the `_validate_single_op` echo must be untouched (check E); a ship that claims "cleanup" across the 6,275-line compensation stack risks deleting the very echoes that make the restore safe, and the four-site question is explicitly NOT settled by #141876 as scoped.

**Two-vehicle churn risk:** #11548 (dispatch bootstrap) and #116673 (bounded read) are both OPEN/unmerged; the bounded read is the active read-path proposal and rides the restore's battery. Churn risk = merge-ordering confusion (bootstrap vs read), stale-branch divergence on #116673's head (mergeability computes pending), and a false "read landed" verdict if the battery is run against #116673 instead of #141876.

**Label-lottery risk on a rescope:** the RFC has already moved six categories (P2→P3→P4) without a substance change; any rescope that re-labels without the body's centerpiece intact repeats the signature — the label must follow the issue, not the reading.

---

## 5. THE OWED REGISTER (machine-side specs, run by head, never faked)

- **OWED-1:** Run the acceptance battery's red/green commands (B1–A–B: 6/6 + 12/12 scratch-store repro on #141876's head) and capture the two log-files R1 cites as its receipts. Spec string: `cd /tmp/r1-scratch && git clone <#141876@af16e3ab16> && python r1-repro.py 6 12` (exact command string per machine).
- **OWED-2:** Fetch #141876's mergeability + checks (gh) and #116673's verified current head (`60a2e15638`, re-verify), and #11548's dispatch bootstrap state (`d3a6e577`).
- **OWED-3:** The final merge dispatch for the chair's chosen option (A/B/C) — chair-gated; no merge fires without the operator's word.
- **OWED-4:** Register this package's own state as the chair's one-page input; no public crossing until the operator's word.

---

## 6. LOOP-STATE LINE

`CONTINUE + <what's next after the chair's word>`: after the chair's A/B/C word, the head runs OWED-1/2 (battery + mergeability), then OWED-3 only in the chosen shape — if A, the package restates the hold with the battery attached (no merge, no label change); if B, the single PR (#141876) lands on its battery with the P4→P2 change, #116673 rides the battery, #11548 stays bootstrap; if C, the four-site dependency question opens with evidence offers. Next in-realm leg: the chosen option's verification pass (battery results → chair re-read), then the label-change PR as decided. The package is staged for the chair and posts nowhere.

**NEXT-LAUNCH:** CHAIR-GATE — the operator's word on A/B/C (with this package attached), nothing more.
