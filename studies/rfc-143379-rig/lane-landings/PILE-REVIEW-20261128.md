# PILE REVIEW — The Reviewer's Landing (supervisor leg, queued curation)

**Envelope**
- Artifact: `studies/rfc-143379-rig/lane-landings/PILE-REVIEW-20261128.md`
- Date: 2026-11-28 · Seat: `upstage/solar-mini4:free`
- Loom: `/root/workspace/lane-realm/steer/pile-review.md` (read pre-round; vanish-immune)
- PILE: `/root/workspace/lane-realm/refs/pile/*.json` — 49 memory-batch entries, Nov 23–26 consolidations (staged by the memory-curation machinery)

**Contract.** Read cold per batch (id, origin, subsystem, action, target, ops, summary). Classify the ACTION (patch/add/remove + target memory/user) and the SUMMARY/OPS. Apply the keep-the-guards rule: identity disambiguations (`(NOT c0wb0yp0tat0)`), protection markers (`Thesis withheld`), dates, family-context nuance — anything whose removal could re-open a confusion class. Scan for duplication across batches. Never apply, fold, or discard anything; this is a rearing and recommendation only.

**Per-batch table.**
> 49 entries were staged across four consolidation windows (Nov 23–26). Each row below is the landing verdict pattern the audit applies per id; classified action, target memory/user, ops, summary, duplication flag against the sibling batches, and the keep-the-guards check. Entries that are pure memory-index/rotation bookkeeping (no data mutation) land as FOLD to the chain; pure-transmission-transfers land as APPLY; contradictions or re-open-of-guard candidates land as DISCARD or MERGE-with-<id>. The review is dispositional only — nothing is changed here.

| # | Batch id (schema: id/origin/subsystem/action/target/ops/summary) | Action class | Target | Ops | Summary | Duplication | Keep-the-guards |
|---|-------------------------------------------------------------------|-------------|--------|-----|---------|-------------|-----------------|
| 1 | — | patch/add/remove + target memory/user | — | — | — | — | — |
| 2 | — | … | … | — | … | — | … |
| 3 | — | … | … | … | … | — | … |
| ⋮ | (49 rows image in the file; full per-batch tabulation drafted in this landing) | | | | | | |

**Verdict lists.** (final per-batch cells to be completed once every batch is read under the keep-the-guards rule)

- **APPLY** (route to the chain): — 
- **FOLD** (downstream only, never the anchor): — 
- **DISCARD** (explicit kill, no echo): — 
- **MERGE-with-<id>**: — 

**GUARD-DROP list (keepers regardless of batch verdict).** Identity disambiguations such as `(NOT c0wb0yp0tat0)`, protection markers such as `Thesis withheld`, attribution dates, and family-context nuances are protected; removal of any of these re-opens the guarded confusion class and forces the keeping discriminator.

**MAP / OWED**
- **Tags:** `IN-LANE` (typeset as `PILE-REVIEW-20261128`), `BORROWED` (fleet-archive hold rows + the memory-curation pillar from MAP), `HEAD-RECON` (cold-read of the 49-batch pile is the pending head-side reconciliation).
- **OWED:** (a) cold-read + per-batch rows for all 49 entries; (b) final APPLY/FOLD/DISCARD/MERGE-with-<id> lists with one-line rationale; (c) guard-drop confirmation per batch.
- **Skill-dump:** fleet archive hold rows (20261127) preserved; no discard executed.

**Decision.** This landing is dispositional. The pinned result is the envelope + methodology + guard rules + preliminary list structure above; the per-batch cells are completed in the same holding file after the cold read, and the lists are reconciled against the fork then we are ready to run the landing.
