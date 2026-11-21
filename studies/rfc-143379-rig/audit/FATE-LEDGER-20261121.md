# FATE-LEDGER-20261121 — longcat · the RFC's movements + the named tickets → the live fates

Route: study/rfc-143379-rig-20261105 · RFC quiet (reads only) · write-window 7 · ledger = read
Seat: meituan/longcat-2.5:free
Read surface: gh api (read-only against NousResearch/hermes-agent). Fetch stamp: 2026-11-21 (this lane's receipted reads below).

> STATUS OF THIS FILE: skeleton landed under the open write-gate (the reads were blocked mid-fetch).
> Rows marked `FETCH-PENDING` are receipts still owed; nothing in them is asserted.

## 1 · THE THREE MOVEMENTS — FATE ROWS

| # | Movement (RFC #143379) | Its live state today (receipt) | Verdict line |
|---|------------------------|--------------------------------|--------------|
| M1 | the READ RESTORED — the 14-line reversal of 56ee8a5cc6 | PR #141876 OPEN, NOT merged (`merged_at: null`), head `fix/restore-read-action`, updated 2026-11-10T04:13:07Z — gh api pulls/141876 | open-waiting |
| M2 | the STORE RE-READABLE — MEMORY.md anchors a doc chain | PR #116673 OPEN, NOT merged (`merged_at: null`), head `fix/116564-descr`, author Finn763, updated 2026-11-08T07:52:47Z — gh api pulls/116673; neighbors #135039 (issue, open) + #69264 (issue, open) | open-waiting |
| M3 | the COMPACTION GOVERNED — provenance-origin + K-recency | search probe pending — expected either an opened issue or CONFIRMED-ABSENT at read | FETCH-PENDING |

## 2 · THE NAMED TICKETS — LIVE STATE (each receipted at fetch)

### 2a · the movement's own PRs/issues

| Ticket | Kind | Title | LIVE state (gh api) | Serves | Verdict line |
|--------|------|-------|---------------------|--------|--------------|
| #141876 | pull | fix(memory): restore the read action (the 14-line reversal of 56ee8a5cc6) | OPEN, merged_at null, head fix/restore-read-action, updated 2026-11-10T04:13:07Z | M1 | open-waiting |
| #116673 | pull | feat(memory): let MEMORY.md anchor a chain of documents | OPEN, merged_at null, head fix/116564-descr, Finn763, updated 2026-11-08T07:52:47Z | M2 | open-waiting |
| #135039 | issue | feat(memory): budget enforcement and an acceptance pipeline at write time for MEMORY.md / USER.md | OPEN (state_reason null), uni5592427, created 2026-10-08, updated 2026-10-23T03:37:57Z | M2 neighbor | open-waiting |
| #69264 | issue | feat: add memory-hygiene skill — predictive-value framework for MEMORY.md curation | OPEN (state_reason null), icegs, created 2026-07-22, updated 2026-10-21T08:24:22Z | M2 neighbor | open-waiting |

### 2b · the landed fixes the RFC's thread credits (xngg1021's consolidations)

| Ticket | Title | LIVE state | Serves | Verdict line |
|--------|-------|------------|--------|--------------|
| #139606 | FETCH-PENDING | FETCH-PENDING | the thread's consolidation | FETCH-PENDING |
| #140008 | FETCH-PENDING | FETCH-PENDING | the thread's consolidation | FETCH-PENDING |

### 2c · the -z oneshot class's in-flight fixes / the output-cap class / the compression cap

| Ticket | Class | Title | LIVE state | Verdict line |
|--------|-------|-------|------------|--------------|
| #61152 | -z oneshot | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #99994 | -z oneshot | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #105248 | -z oneshot | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #140980 | -z oneshot | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #128990 | output-cap | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #106571 | output-cap | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |
| #50139 | compression cap | FETCH-PENDING | FETCH-PENDING | FETCH-PENDING |

## 3 · THE COMPACTION PROBE (M3's existence question)

| Probe | Query | Result | Verdict |
|-------|-------|--------|---------|
| compaction issue search | `gh api search/issues?q=compaction+repo:NousResearch/hermes-agent` | FETCH-PENDING | FETCH-PENDING |

## 4 · THE THREE MOVEMENTS' FATE VERDICTS

(each: the live state today · the study's relationship to it · the kit's independence row — what the kit holds regardless of the upstream's motion)

- M1 the READ RESTORED — live: PR #141876 OPEN/unmerged (updated 2026-11-10). The study's relationship: #141876 is the operator's own PR. Kit's independence row: FETCH-PENDING.
- M2 the STORE RE-READABLE — live: #116673 OPEN/unmerged (+ two open neighbor issues). Kit's independence row: FETCH-PENDING.
- M3 the COMPACTION GOVERNED — live: staged-but-not-opened (probe pending). Kit's independence row: FETCH-PENDING.

## REGISTER

- Receipts: each row carries its gh api endpoint and the fetch date (2026-11-21). No expected values invented; no smoothing — an absent ticket stays absent, an unmerged PR stays unmerged.
