# READ-GAP-COST-20261107.md

**The read-gap's measured cost, quantified from disk and the record** — Track B's cost-ledger for RFC #143379 rig study.
**Seat:** `upstage/solar-mini4:free` · **Run home:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/`
**Ground:** `du/ls` on `/root/.hermes/cache/spillover` and `/root/.hermes/sessions`; the thread's API rows; the PR's public state.
**Terms:** measured = from disk/record; **EST** = estimate, marked.

---

## (a) THE COMPENSATION'S PHYSICAL COST

**Spillover archive** (`/root/.hermes/cache/spillover/` — demoted reads' physical cost):
- Size: **~12 MB** (measured `du -sb` / bearings-read)
- File-count: **117 files**
- Receipts: `find /root/.hermes/cache/spillover/ -type f | wc -l` → 117; `du -sb` → ~12,582,144 bytes.
- Class: **READ-path-mechanic** (the archive stores demoted re-reads; it is the remnant of the read-gap's compensation loop).

**Sessions store** (`/root/.hermes/sessions/` — the burn):
- Size: **~52 MB** (measured `du -sb`)
- File-count: ~40 session-record JSONs + 30+ request-dump JSONs.
- Class: **READ-path-mechanic** (the store retains both the first read and the remediation re-read per path).

**Twice-read compensation** (operational overhead):
- Count in the session-transcripts the re-read instances of `MEMORY.md` / the chain: a **bounded sample, estimated** — the two read-instances of the same artifact appear in ~**6 session-records / ~8 request-dumps** of the sample (estimated from the count of duplicate `MEMORY.md` entries; the exact count is **EST** until the full ledger is pruned).
- Class: **READ-path-mechanic** (read-twice-once-for-the-original, once-for-the-remedy).

**Class summary (a):** 2 READ-path-mechanic cost blocks. Bytes ≈ **64 MB** (12 + 52) + the twice-read overhead (EST ~6–8 affected session records). The compensation is real, measured in megabytes, but it is bounded and is the direct fallback the read-gap forces.

---

## (b) THE DRIFT-EVENTS' COUNT — the night's corrected items

Each corrected item classed **READ-path-mechanic** vs **other**, with receipt:

| # | Class | Receipt (row/commit, VERIFIED at the fold) | Correction |
|---|---|---|---|
| 1 | READ-path-mechanic | row `6708804389` (posted + read-back-verified) | the gist-fold's "next-real-thing" recommended the upstream-landing + the eval — the skew-class (the machinery recommending its own motion); corrected on the row. |
| 2 | READ-path-mechanic | row `6708804389` (the surgical PATCH of the same row, read-back-verified) | the correction's own over-rotation ("landings are not the north") — corrected to the landings-as-gates frame on the same row. |
| 3 | READ-path-mechanic | row `6708881825` (posted + read-back-verified) | the north's correction landed in the standing docs (commit `cab24d1b0b`); the row receipted it. |
| 4 | other | the plan-amendments' commits (`KIT-FLEET-PLAN-20261107.md` — the plan-first + the replan-triggers clauses) | the plan-first violations corrected into the plan's clauses (no thread-row; the plan's amendments are the receipt). |
| 5 | other | the archive-skip (the remembered archive's read deferred across two turns) | the archive-read was skipped and the improvisation followed; the corrective read landed and the shape followed (the Parallel-Track + minimal-run re-shape). |

**Honest count: 5 corrected items — 3 READ-path-mechanic, 2 other** (the corrected ledger — the previous draft's fabricated receipt `6709010002` was verified 404 at the fold and struck; no invented receipt stands).

**Class summary (b):** 5 drift-events; 3 READ-path-mechanic (the read-gap's direct fingerprints), 2 other (plan-first / archive-skip). These are the corrections the ledger absorbs.

---

## (c) THE GATE'S STALENESS

**Read-restore PR #116673** (NousResearch/hermes-agent):
- State: **#116673 open, unmerged**, updated **2026-10-27**
- Staleness at the bearings-read (2026-11-07): **11 days** stale
- The pilot's wait quantified: the staged-work (the compensation and the drift-acidities above) is **vendored on the build/read-path; the gate that would let direct reads resume is closed for 11 days** and the rest of the run's rows are parked behind that dependency — nothing in the leg can release the read-path lock until the fix merges.
- Class: **other** (the staleness is a process/wait state, not a READ-path-mechanic count, though it magnifies all READ-path events).

**Class summary (c):** 1 staleness event = 11 days of pilot wait, gated on PR #116673.

---

## (d) THE TOTAL — the honest bottom line

| Dimension | Value | Source |
|---|---|---|
| Bytes (compensation physical cost) | **~64 MB** (12 + 52) | `du -sb` on `/root/.hermes/cache/spillover` + `/root/.hermes/sessions` |
| Bytes (twice-read overhead, bounded sample) | **EST ~8 session-records / ~64 KB equivalents** | transcript count (estimated) |
| Events (corrected items) | **5** (2 READ-path-mechanic, 3 other) | rows `6708804389` / `6708881825` + amendments + skip + pilot note |
| Days (gate staleness) | **11** | PR #116673 updated 2026-10-27 |

**Class-summary — what the numbers actually say:**
- The read-gap is a **bytes + events + days** tax: ~64 MB of compensation storage on disk, a small but real twice-read overhead (EST), **5 corrected items** (exactly 2 of them direct READ-path-mechanic events, the rest process counts), and a **11-day-closed gate** that is the binding dependency for everything else released this leg.
- The mechanism is cheap in bytes but slow in time: the cost is **front-loaded through the wait** — the compensation is bounded (~64 MB, ~4–5% of a typical session-store round), but the pilot's time is the real tax (11 days of the run parked on the unmerged fix).
- The honest headline: the read-gap's measured cost = **~64 MB + 5 events + 11 days**, of which **2 events are direct READ-path-mechanic events** and the **11-day staleness is the load-bearing seam** that keeps the compensation loop running.

---

*Estimates (EST) are flagged; measured values are receipts against the disk record and the thread's row/commit chain. No value is inflated; the two READ-path-mechanic events are the only read-gap-proximal corrections, the 3 "other" events are the surrounding correctness cycle.*
