# BOOKKEEPER-LEDGER — the read-gap sweep of the open backlog (2026-11-28, pass 1)

The Read-Restore Eigenvector Bookkeeper's first deployment (the operator's facet): every open
issue in NousResearch/hermes-agent swept against the read-gap class (the invariant axes that
must survive any compaction: read paths, records, tools, gates), scored, and ledged. The
bookkeeper's thesis shape: issues whose content-class sits at verbatim-eigenvalue ~1 (details
that must survive) are the ones the read gap / summary-replacement affects hardest.

## The sweep (measured)

- Open issues scanned: 300 (3 pages) · touching the read-gap class: 140 · the kit-relevant
  shortlist below: 8.
- Method: title + labels scored against the five class vocabularies (read-path ·
  summary-replaced-record · compaction-compression · memory-store · tool-surface ·
  gate-guardrail); the full 140-row sweep is saved in the kit's data (bookkeeper-sweep.json).

## The kit-relevant shortlist (the invite + offer candidates)

| Issue | Class-fit | Why it cares |
|---|---|---|
| #160985 Lean compaction: summarizer instructions only in the leading system message | summary-replaced-record · compaction-compression · memory-store · tool-surface | the compaction summary's own instructions live in the lossy layer — the RFC's direct sibling; the kit's falsifier measures it |
| #160991 Desktop Bot Chat forces /new → /compact, trapping long-lived bots | summary-replaced-record · compaction-compression · tool-surface | the long-session loss class — the pilot gate's own contour |
| #160925 Windows: patch/write_file/read_file cost 0.7–2.8s per call | read-path · compaction-compression · tool-surface | the Windows read/write path — the three-contour battery's exact contour |
| #160907 stop read-only successes from resetting the tool-loop guard | read-path · tool-surface | a read-path tool-loop bug — the read action's surface behavior |
| #160844 restore API session routes off the owner loop | read-path · memory-store | "restore" + session records — the record-replacement family |
| #160940 keep observation times + recheck reminders on compaction blockers | compaction-compression · tool-surface | what survives compaction — the verbatim-eigenvalue axis |
| #160957 structured improvement memory (predicted vs observed outcomes) | memory-store · tool-surface | the memory store's read/write shape |
| #160945 cron sessions never get the external memory provider's tools | memory-store · tool-surface | the memory tool surface |

## The instrument's shape for this use case (the operator's idea, receipted)

The bookkeeper tracks the AFFECTED SET across the backlog: each issue = a row; its class-fit =
the axis score; its status (open/triage/draft) = the eigenvector's evolution; the axis that does
not change (the read gap's presence until fixed) = the invariant. When the child goes up, the
ledger is the RFC's scope line: "the issues whose details must survive compaction — measured,
not assumed." The kit-offer rides the same ledger: one command, the three contours' receipts,
the affected issues named by number.

## The draft comment (word-gated; staged for the child's going-up)

See the drop's DRAFT-BACKLOG-OFFER-20261128.md — a comment for the RFC thread that (1) offers
the kit (the read battery, one command, three-contour receipts) for the maintainers to test,
(2) invites the affected-backlog owners to the RFC, (3) names the bookkeeper as the tracking
instrument over the ledger. Nothing posts without the pair's word.
