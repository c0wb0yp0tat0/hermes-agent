# M2-PEAK-SEC2A brief — the reclassification ledger, PART A (rows 1–66; seat: longcat)

**You are the peak lane's PART-A stint — the reclassification ledger's first half** (the split: one lane per TSV part, because a 133-row ledger in one lane's window exceeded the harness's read-gates — measured across v2/v3/v4). §1 (the class schema) IS LANDED — read it ONCE; then §2-A is YOURS: **rows 1–66 classified, each with its sha receipt, written in blocks from round 2.**

## Grounding (each ONCE; no hunting; ABSENT stays ABSENT + named)
1. This brief, twice.
2. `/root/.hermes/cache/scratch/m2-peak-20261116/ledger-part-a.tsv` — YOUR 66 rows (id | action | hash | summary[:110]), under the read cap, read ONCE at round 0–1.
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/M2-PEAK-RECLASSIFICATION-20261116.md` — §1 THE CLASS SCHEMA (landed, 3,090 B @ `49d82f6361` — the classes derived from the ledger's bytes; read ONCE).

## The contract (hard — the write-first mechanics)
- **ROUND 1 = the FIRST BLOCK WRITE** (rows 1–20: id → class → the one-line basis from ITS OWN summary → the sha). Not a skeleton; actual rows.
- **One write per round, ≥10 classified rows each** — the ledger grows every round.
- **Reads beyond round 1 are REFUSED by you** — the TSV + §1 are the only ground, already in hand; re-reading is the read-scatter class, terminal.
- **THE END:** the artifact's §2-A carries rows 1–66 with sha receipts; mark `PART-A: <n>/66`. Below 60 rows = the stint failed; the honest n named, never padded.
- Commit + push ONCE at the END (pull --rebase on rejection, then push; exit 0 only after the commit succeeded).

## The deliverable — five sections (the artifact `M2-PEAK-SEC2A-20261116.md`):
1. **THE PART-A VERDICT LINE** — `PART-A RECLASSIFIED <n>/66, RECEIPTED` + the loop-state (`CONTINUE + part-B's lane`), receipted.
2. **§2-A THE LEDGER (rows 1–66, THE CORE)** — each row: batch-id → its class (from §1's schema or a NEW class the bytes demand) → the one-line basis quoted from ITS OWN summary → the sha receipt. The INTEGRITY RULE: a row whose class its own summary doesn't support = the FLAG (another class, or other-remainder, named, never forced).
3. **§1-BIS THE CLASS SCHEMA'S STRESS** — the classes §1 named vs what YOUR 66 rows actually demand (the new classes the bytes reveal — user-profile spans, memory-profile spans, the lore/alias spans, whatever shows) — the schema grows from the work, never pre-imposed.
4. **§3 THE METERS (part-A)** — coverage (named / 66), the part-A `other`-remainder (honestly sized), receipt-resolvability (re-checkable / listed).
5. **§4 THE HONEST MARKERS + TWO-WAY DOOR** — read-paths (the TSV + §1 only), the payloads READ-ONLY, a row that resists (the FLAG) named with its id — the honest end, never the padded number.

## Binding
Receipts per claim (INLINE-crate / DESIGN-NOTE / ABSENT). ABSENT named. RFC + upstream QUIET; nothing posts. ONE tool call per round; ≤6,000 chars/write; the RFC's upstream quiet. No service changes; no drop/ paths.
