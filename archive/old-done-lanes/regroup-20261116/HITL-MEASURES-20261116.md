# HITL-MEASURES-20261116 — regimented measures for the M3-repost/regroup arc

- **Memo root:** `rfc-143379-rig` fork of `c0wb0yp0tat0/hermes-agent`
- **Measured-at (UTC, wall clock):** `2026-11-16T21:41:42Z` / `2026-11-16T21:41:53Z` (batch runs)
- **Convention:** every count below is re-derived verbatim from a raw source with the exact
  command that produced it. The spine (`HITL-SPINE-20261105-1116.md`) is **not** copied; its
  cited figures are only quoted as a comparison target so the reconciliation is auditable.

---

## 1. Thread total + per-day (issue #1 comments)

**Command (exact):**
```
gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments --paginate | jq length
gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments --paginate | jq -r '.[].created_at[0:10]' | sort | uniq -c
```

**Value (measured):** **815** total comment entries, all with bodies. Per-day:

| date | count |
|---|---|
| 2026-11-05 | 32 |
| 2026-11-06 | 159 |
| 2026-11-07 | 77 |
| 2026-11-08 | 68 |
| 2026-11-09 | 49 |
| 2026-11-10 | 35 |
| 2026-11-11 | 69 |
| 2026-11-12 | 52 |
| 2026-11-13 | 73 |
| 2026-11-14 | 53 |
| 2026-11-15 | 85 |
| 2026-11-16 | 63 |

**Receipt:** `gh api .../issues/1/comments --paginate` returned 815 JSON entries; the per-day
`uniq -c` block summed to 815 (`32+159+77+68+49+35+69+52+73+53+85+63`).

**Reconciliation note:** the spine cites "thread 814 comment bodies". Raw re-derivation returns
**815** (the API emits 815 comment objects, each with a body; the first entry begins `# RUN-RFC143379-RIG-20261105`).
The spine's 814 is therefore stale by exactly one entry — marked OPEN below so the verifier can
re-run the same command and confirm.

---

## 2. Timeline total

**Command (exact):**
```
gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/timeline --paginate | jq length
```

**Value (measured):** **1,126** events.

**Per-event-type breakdown (context, not a recount):**
`commented` 815 · `committed` 250 · `referenced` 28 · `mentioned` 12 · `subscribed` 12 ·
`head_ref_force_pushed` 2 · `labeled` 2 · `assigned` 1 · `cross-referenced` 1 · `unlabeled` 1 ·
`merged` 1 · `closed` 1.

**Receipt:** `gh api .../issues/1/timeline --paginate` returned 1,126 rows. (The count moves
during the day, 1,122 → 1,124 → 1,126; this measurement sits at **1,126**.) The spine also
cites 1,126 events — consistent at the value level.

---

## 3. Branch commits total + per-day (remote == local gate)

**Commands (exact):**
```
git rev-list --count study/rfc-143379-rig-20261105
git log --format='%ad' --date=short study/rfc-143379-rig-20261105 | sort | uniq -c
git ls-remote origin study/rfc-143379-rig-20261105
git rev-parse study/rfc-143379-rig-20261105
```

**Value (measured):** **960** commits across the full branch history
(`2026-09-12` → `2026-11-16`). Per-day:

| date | commits | date | commits |
|---|---|---|---|
| 2026-09-12 | 1 | 2026-11-05 | 100 |
| 2026-09-13 | 1 | 2026-11-06 | 115 |
| 2026-09-25 | 1 | 2026-11-07 | 81 |
| 2026-10-14 | 4 | 2026-11-08 | 73 |
| 2026-10-15 | 92 | 2026-11-09 | 60 |
| 2026-10-16 | 2 | 2026-11-10 | 41 |
| 2026-11-03 | 5 | 2026-11-11 | 106 |
| 2026-11-04 | 5 | 2026-11-12 | 59 |
| 2026-11-13 | 7 | 2026-11-14 | 36 |
| 2026-11-15 | 134 | 2026-11-16 | 37 |

**Remote == local gate:** `ls-remote` → `a7f385edc1f11d737aaba7dc2e59417ca1bfd1a0`;
`rev-parse` → `a7f385edc1f11d737aaba7dc2e59417ca1bfd1a0`. **Gate = TRUE.**

**Reconciliation note:** the spine cites "branch 849 commits". Raw re-derivation returns
**960** (full branch). **849** is reproduced as the **Nov 5–16 window** exactly
(`2026-11-05`→`2026-11-16` sums to 849). The two numbers are both re-derivable; they differ
only by scope (window vs. full branch). The window figure is the spine's; the exact command
above reports the full-branch figure.

---

## 4. Study artifacts total + date-pattern per-day

**Commands (exact):**
```
find /root/workspace/repos/hermes-agent/studies/rfc-143379-rig -type f | wc -l
find /root/workspace/repos/hermes-agent/studies/rfc-143379-rig -type f -name '*2026-11-*' | wc -l
find /root/workspace/repos/hermes-agent/studies/rfc-143379-rig -type f -name '*202611*' | wc -l   # compact form
```

**Value (measured):**
- **21,723** files total (`find -type f`).

**Race note:** the first parallel read of this command returned **21,722** (the `find` snapshot
was taken while a concurrent write landed); the command was re-run sequentially and froze at
**21,723**. Both are re-derivable counts of a live tree — the verifier should re-run the exact
`find` to confirm the current total.

- Dash-form date-pattern (`*2026-11-*`) → **0** files (the rig's file-naming uses compact
  `YYYYMMDD` digits, e.g. `NEGENTROPY-SWEEP-20261116-0128.md`, with no dashes between date parts).
- Compact date-pattern `202611NN` → **1,586** files; per-day:

| day | files |
|---|---|
| 04 | 4 |
| 05 | 46 |
| 06 | 120 |
| 07 | 290 |
| 08 | 197 |
| 09 | 177 |
| 10 | 57 |
| 11 | 231 |
| 12 | 68 |
| 13 | 11 |
| 14 | 143 |
| 15 | 179 |
| 16 | 63 |

**Receipt:** `find` enumerated 21,723 files; the `[0-9]{4}11[0-9]{2}` name-match returned
1,586 (per-day block above). The total is consistent with the live `find` count.

**Reconciliation note:** the spine cites "1,197 date-pattern artifacts". Raw re-derivation does
**not** reproduce 1,197 under the exact command (dash-form = 0; compact = 1,586). The 1,197
figure is **OPEN** below — it likely referenced a different scope or a snapshot hash the
command cannot settle.

---

## 5. Ledger measures

### 5a. Landing ledger (`memory-chain/landing-ledger.md`)

**Commands (exact):**
```
grep -oE '\b(PASS|FOLDED|FINDING|OPEN|POSTED|MERGED|DONE|VERIFIED)\b' landing-ledger.md | sort | uniq -c
grep -oE '\b(PASS|FOLDED|FINDING|OPEN|POSTED|MERGED|DONE|VERIFIED|RED|GREEN|COMPLETE|IN-FLIGHT|RECEIVED|RECEIPTED)\b' landing-ledger.md | sort | uniq -c
```

**Value (measured):** the ledger is a markdown table of dated rows. Data rows: **70** total,
of which **55** carry a 2026-11 date.

**Reconciliation note:** the spine cites "ledger 32 rows". Raw re-derivation returns **70**
data rows (55 Nov). The 32-row figure is a stale snapshot of an earlier state of the same
ledger (the landing-ledger is append-only and has grown across the day); this memo reports the
live re-derived count of **70**.

Verbatim verdict-vocabulary census (full-file `grep -oE`), the tokens **as they actually appear**:

| token | count |
|---|---|
| PASS | 40 |
| DONE | 57 |
| FOLDED | 8 |
| FINDING | 8 |
| POSTED | 4 |
| VERIFIED | 4 |
| OPEN | 2 |
| MERGED | 1 |
| COMPLETE | 4 |
| IN-FLIGHT | 2 |
| RED | 1 |
| GREEN | 1 |
| RECEIVED | 1 |
| RECEIPTED | 1 |

(The richer `grep -oE` pass over the full file also surfaces verbs outside the instruction's
8-token set: RECEIVED 1, RECEIPTED 1, COMPLETE 4, IN-FLIGHT 2, RED 1, GREEN 1. The verdict
**column alone** (not grep) is richer still: DONE 28, LANDED 4, IN-FLIGHT 2, PENDING 2, RUNNING 2,
plus varied closed/armed/banked/obsolete text.)

### 5b. Study internal SEC2 ledger (the 133-row peak ledger)

**Files located:** `M2-PEAK-SEC2A-20261116.md` and `M2-PEAK-SEC2B-20261116.md` in the rig root.
SEC2-A = rows **1–66** (seat: longcat); SEC2-B = rows **67–133**. Together **133 rows**.

**Verdict vocabulary + counts (read from the ledger files and their measure file):**

| surface | verdict tokens / counts |
|---|---|
| SEC2-A (`M2-PEAK-SEC2A-20261116.md`) | `PART-A RECLASSIFIED 65/66, RECEIPTED`; **1 FLAG** (row #56 / `60f8397f`, "Stack = refinement CHAIN (Red Team mandatory)"); `other-remainder` named, never forced |
| SEC2-B (`M2-PEAK-SEC2B-20261116.md`) | `PART-B RECLASSIFIED 66/66, RECEIPTED`; no re-reads; honest end 66/66 receipted |
| SEC2 measure (`M2-PEAK-MEASURE-20261116.md`) | **133/133 parsed**; coverage **132/133 = 99.2%**; **1** `other-remainder` (the FLAG); class distribution: user-profile 36, memory-profile 27, lore/alias 24, gates 10, register-voice 9, policy 6, governance 6, fleet 5, trust-circle 4, lessons 4, network 1, other-remainder 1 |

**SEC2 ledger settlement — which surface holds the 40/7/5/1/1 class split?**

**Neither surface holds the claimed composite.** Re-deriving both:

- **Landing ledger:** 40 **PASS** matches the claim's "40" term, but the rest do **not**.
  Actual: RED **1** (claim 7), COMPLETE **4** (claim 5), GREEN 1 (claims 1), IN-FLIGHT **2**
  (claim 1). So the landing-ledger is the *closest* match but is not the composite holder.
- **SEC2 ledger:** a classification ledger, not a verdict ledger. Its "verdicts" are
  `RECLASSIFIED` / `RECEIPTED` / `COMPLETE` / `HONEST` / `other-remainder`; it carries no
  40/7/5/1/1 split of any kind (its class distribution is 36/27/24/10/9/6/6/5/4/4/1/1).

**Conclusion for the memo:** the "40/7/5/1/1" class split as cited is **not supported by
either raw surface**; the landing-ledger reproduces only the "40 PASS" term, and the SEC2
ledger is a separate 133-row classification table. The claim stays **OPEN** (denied on
re-derivation, not guessed) until the source memo that asserted it is located.

---

## 6. Session measures (verbatim, from the session page)

**Source:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SESSION-ARC-STUDY-20261116.md`

| field | value |
|---|---|
| session id | `20261115_161220_edda6d67` |
| started | 2026-11-15 21:12 UTC |
| messages | 1,404 |
| API calls | 688 |
| tokens | ~7.43M |
| cost | ~$4.86 (paid head seat) |

**Receipt:** verbatim read of the session page (its own "THE SESSION'S MEASURES" block).
This is the raw source the memo references; no independent recompute was available in the
study dir, so these are reported as recorded on the page.

---

## OPEN list (measures not cleanly re-derived)

1. **Thread 814 vs 815** — spine cites 814 "comment bodies"; raw command returns 815. Settle by
   re-running `gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments --paginate | jq length`.
2. **Branch 849 vs 960** — spine's 849 is the Nov-5→16 window; the exact `git rev-list --count`
   command reports 960 (full branch). Both are legitimately re-derivable; scope must be named
   explicitly.
3. **Artifacts "1,197 date-pattern"** — not reproducible from the exact `find` command
   (dash-form = 0, compact = 1,586). The scope/hash the spine used is not recoverable from the
   command set; OPEN until the spine's source snapshot is located.
4. **The 40/7/5/1/1 class split** — not held by either surface on re-derivation. Landing-ledger
   reproduces only "40 PASS"; SEC2 is a classification ledger (36/27/24/10/9/6/6/5/4/4/1/1).
   Claim denied on re-derivation; needs the source memo that asserted it.

---

## Compose-check table (8 marks)

| # | mark | status | evidence line |
|---|---|---|---|
| 1 | deconstruct | FIRED | `gh api issues/1/comments --paginate | jq length` → 815; per-day block sums to 815 |
| 2 | sense | FIRED | node-first claims (thread 814, branch 849, artifacts 1,197) each reconciled to a re-derived command value instead of accepted on faith |
| 3 | choose | FIRED | branch window (849) vs full branch (960) both named with the exact command that yields each |
| 4 | calibrate | FIRED | SEC2 settlement: landing-ledger 40 PASS vs SEC2 133-row classification table; claim denied on re-derivation, not asserted |
| 5 | probe | FIRED | open items carry the exact command that would settle them instead of a plausible citation |
| 6 | review | FIRED | per-measure receipts cite command + measured-at timestamp; ledger census is verbatim `grep -oE | sort | uniq -c` output |
| 7 | record | FIRED | this file is the recorded measures block; no numbers copied from the spine |
| 8 | compose-check | FIRED | 8-mark table above; open list + SEC2 settlement at the end |

---

*End of MEASURES BLOCK. No commit; no push. All counts re-derived from raw sources; the only
values taken verbatim are the session-page fields (the study page is the raw session record).*
