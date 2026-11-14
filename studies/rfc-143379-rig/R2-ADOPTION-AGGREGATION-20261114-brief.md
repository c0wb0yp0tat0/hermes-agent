# R2 ADOPTION AGGREGATION brief — 2026-11-14 (chain leg, seat: longcat)

**You are a fully armed ACES ring lane** (copycat harness, git-only terminal, artifact-gated writes). Your ring: **R2 — ADOPTION AGGREGATION** (Door 3 of the NEMO-REGROUP gist: "ADOPTIONS records scattered across B05/B06/B07/B08, not aggregated in the master synopsis").

## What the ring is
The adoption records live scattered across the rig's arcs. The fold must aggregate them into ONE adoption register: every adoption decision, its row (A–H classes), its adopt-internal vs parked status, and its evidence. Nothing adopts itself here — you AGGREGATE + VERIFY what exists; the adoption shape (A–D/F adopt-internal, E–H parked) comes from ADOPTIONS-20261112.md.

## Grounding order
1. This brief, twice.
2. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/REFS/` — the head-staged refs: ADOPTIONS-20261112.md (the primary record — read first), NEMO-CONVERGENCE-PLAN-20261114.md (the plan's adoption rows + platform-drift table), CROWN-SLICE.md (drop/ is OUTSIDE your read roots — the REFS copies are the only reachable way in).
3. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/REFS/` — also there: NIGHT-OPS-APEX-REPLAN-20261113.md (M1–M8 rows), BRIEF-CROSSING-{DOWNSTREAM,UPSTREAM,COMPARE,SYNTHESIS}.md (drop/ is OUTSIDE your read roots — never attempt a drop/ path; the REFS copies are the only reachable way in).
4. `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/CYCLES/` + the rig root — B05/B06/B07/B08 arc artifacts, IMPROVEMENTS-W1-20261107.md, LENS-OUTCOME-20261108.md, ACES-* audit/review files, the ADOPTIONS mirror if present.
5. The NEMO-DAY-PLAN-20261114.md corrected plan's C4 (the platform-drift rows — they are UNGROUNDED until a docs citation lands; the page-pull list is OWED to the head, so those rows aggregate as UNGROUNDED-PENDING-CITATION, never as adopted).

## Deliverable (the artifact — write incrementally, skeleton by round 5, ≤6,000 chars/write)
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/ADOPTIONS-AGGREGATE-20261114.md` containing:
1. **THE REGISTER** — every adoption row found (source file + line per row), its class (A–H), status (adopt-internal / parked / ungrounded-pending-citation), and the one-line substance. Dedupe by handle: two records of the same decision = one row + both sources cited.
2. **THE RECONCILIATION** — where records disagree (status, class, scope), name the disagreement with both receipts, never silently pick.
3. **THE GAPS** — named adoption decisions the record implies but no file carries (absent-target rule: name, don't invent).
4. **THE OWED REGISTER** — what needs the head's machine-side hand.
5. **Loop-state line** at the tail: `CONTINUE + <next ring's name>` or `NO-IMPROVEMENTS + confirmation cycle` — plus a NEXT-LAUNCH block naming R3 (brief path + seat + logdir) per the corrected plan's ring table (R3 = FINAL5-8 fold; the plan's seat rotation applies — probe at fire).

## Boundaries (binding)
- Kenari READ-ONLY; RFC upstream QUIET; nothing public; no service changes; no `/root/.hermes` writes; git-only terminal — runs register OWED, never faked.
- The write-window: your artifact's existence opens the gate; after your first write, KEEP WRITING (append per section) and commit+push (pull --rebase on rejection) ONLY after the last section — the first commit is not the finish line.
- Steer channel (read before EVERY compose round): `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-STEER-CHANNEL-20261114.md` — a `STEER-<id>:` line is a mid-flight steer; act on it that round and acknowledge in your artifact.
- Receipts: every row carries a source tag (IN-LANE / BORROWED / HEAD-RECON) + the file it came from; absence only from a stamped read.
- The absent-target rule: never invent a file or fact.
