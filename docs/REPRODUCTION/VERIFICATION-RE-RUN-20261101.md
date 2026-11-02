# VERIFICATION RE-RUN — 2026-11-01 (NS-VERIFICATION-RE-RUN)

Read-only verification pass. Nothing public. Surface verified: LIVE GitHub API (issue/PR comments + PR body) + on-disk rig record.

## Bottom line

- 11 enrichment edits (the contract's named checks) verified against the LIVE comment/PR-body surface: **9 CLOSED**, **2 COHERENCE-GAP**.
- The 2 COHERENCE-GAPs are the two stale-claim corrections (#135039, #11548): the edit is live and a pointer sits at the top, but the body still asserts the stale claim inline ("closed/merged=false", "sole open vehicle"), so a top-to-bottom read hits the stale framing before the correction.
- The remaining 18 pulse-scan findings (7 code-surface verified on `main` in the first pass + 11 comment-surface findings not enumerated in available evidence) are **UNVERIFIABLE from this host** — the original pulse-scan finding list (32 → 29) is not on disk here. Listed in §4.

## §1 — Method

Per agent-work-review: full reads of each target comment (not snippets), live `gh api` fetches, then claim-vs-live comparison, then coherence read top-to-bottom. No self-grading: verdicts are bounded by what the live bytes show.

Targets: the 8 threads c0wb0yp0tat0 is directly involved in (#135039, #116673, #140980, #110126, #11548, #69264, #140848, #116788) and the 11 enrichment edits documented in side-by-side gist 4986caf0d6451606e0e6b3a39132fcb0.

## §2 — Verdict table (11 enrichment edits)

| # | Thread | Surface | Class | Live receipt | Verdict |
|---|---|---|---|---|---|
| 1 | #135039 (comment 6102192135) | issue comment | stale-claim correction | UPDATE pointer at top (line 1) + full correction at bottom (line 79): "PR #116673 was reopened by its author on 2026-10-12 and is **open** (head `2c1941aac`, not merged)" — present | COHERENCE-GAP — body still asserts "PR #116673, now closed/merged=false" inline (line ~5); reader hits stale claim before correction |
| 2 | #11548 (comment 6103397556) | issue comment | stale-claim correction | UPDATE pointer at top + correction at bottom: "PR #116673 … is **open** (head `2c1941aac`, not merged) … no longer the only door" — present | COHERENCE-GAP — body still asserts "was closed by its author on 2026-10-10" and "sole open vehicle" inline |
| 3 | #110126 (comment 6101413435) | issue comment | fingerprint strip | "The installed build (SHA `24b9f0f8c5`)" present; canary build string `24b9f0f8c5, v0.21.4+canary…` → 0 occurrences; `/usr/local/lib/hermes-agent` → 0 occurrences | CLOSED |
| 4 | #116673 (comment 6137384793) | PR comment | fingerprint strip | "the project root on `PYTHONPATH`" present (line 9); absolute cache path `OXR0iE4_eIrFE7js` → 0; `/usr/local/lib/hermes-agent` → 0 | CLOSED |
| 5 | #135039 (comment 6159746520) | issue comment | orphaned-diff link | "https://gist.github.com/c0wb0yp0tat0/b54cb1fcbaf57e347cf4cab8e456e42d (`pr139606.diff`)" present; URL resolves HTTP 200 | CLOSED |
| 6 | #69264 (comment 6244692039) | PR comment | fingerprint strip | "the skills directory (`hermes-agent/skills/<category>/`)" (line 227) and "the repo's skill-resolution test" (line 262) present; `test_related_skills_resolve` → 0; `~/.hermes/skills/` → 0 | CLOSED |
| 7 | #11548 (comment 6283695624) | issue comment | date-anchor | "At the time of that check (2026-10-20), the session's context was at 321K tokens and the anchor was over its char limit (2540/2200)" present (line 11) | CLOSED |
| 8 | #116788 (comment 5748269437) | issue comment | config-contents replacement | "the local config has no background-review settings block" present (line 5); no `my config.yaml has no …` / no config key path | CLOSED |
| 9 | #140848 (comment 6247480404) | PR comment | orphaned-diff link | "https://github.com/NousResearch/hermes-agent/pull/139606/files (commit `5b31ccb7d5`)" present (line 7); URL resolves HTTP 200 | CLOSED |
| 10 | #140980 (comment 6258090981) | PR comment | orphaned-diff link | "The diff is in the PR: https://github.com/NousResearch/hermes-agent/pull/140980/files" present (line 7); URL resolves HTTP 200 | CLOSED |
| 11 | #140980 (PR body) | PR body | credit tags | `@xngg1021`, `@ardaaltinors`, `@OctaveAdb`, `@jg3fw2t35`, `@cloverthe-ai` all present (line 49 of body) | CLOSED |

## §3 — Coherence check (top-to-bottom read)

- Rows 3–11: the edited text is the body text itself (fingerprint removed inline, link added inline, date added inline, config key replaced inline, tags added inline). No stale framing remains at the top. Read coherently.
- Rows 1–2: COHERENCE-GAP. The append-only correction lives at the bottom; the body still carries the stale claim ("closed/merged=false" on #135039; "closed by its author on 2026-10-10" / "sole open vehicle" on #11548). A pointer line was added at the very top ("the framing below was accurate on 10-10 but is stale now — see the correction at the bottom"), which mitigates but does not remove the inline stale assertion. A reader scanning top-to-bottom still encounters the stale claim before the correction. Per the verification craft (agent-work-review "Verify the edited artifact READS coherently from the top"): a correction appended to a surface whose top still shows the old framing is a coherence gap, not a nit.

Corrective-only notes (no public writes; nothing applied here):
- For #135039 (6102192135) and #11548 (6103397556): the inline stale spans ("now closed/merged=false" and "was closed by its author on 2026-10-10 … sole open vehicle") should be either (a) struck through / annotated in place, or (b) the pointer line strengthened to a clearly-visible "STALE — see correction below" banner, so the top no longer asserts the stale fact. The append-only convention is preserved; this is a readability fix, not a rewrite. Any such edit is a two-way door (GitHub keeps edit history) and waits on the owner's word before posting.

## §4 — The 18 unverifiable findings (explicit unverifiable list)

The original pulse-scan finding list (32 raw → 29 confirmed, cross-audited both ways) is not present on this host (not in drop, not in the memory chain, not in a gist). Per agent-work-review §7, the following are stated as unverifiable from here rather than asserted:

- 7 code-surface findings that the first pass verified on `main` (per the rig's own record, 002-lessons 2026-10-21 dated bullet: "7/29 verified"). I did not re-derive these; the original scan's enumeration is not on disk. If the owner wants them re-verified, the owning host must supply the pulse-scan artifact.
- 11 comment-surface findings beyond the 11 enrichment edits above (per the same record: "22 gaps" in the code-surface pass, of which 11 were the enrichment edits). These are not enumerated in any available artifact; I cannot map them to threads or comments without the scan output.

Nothing in §4 is claimed closed. They remain open items pending the pulse-scan artifact.

## §5 — Live receipt index

- Comment 6102192135 (#135039) — fetched 2026-11-01, 5153 bytes, contains both UPDATE markers.
- Comment 6103397556 (#11548) — fetched 2026-11-01, 3604 bytes, contains both UPDATE markers.
- Comment 6101413435 (#110126) — fetched 2026-11-01, 9084 bytes, fingerprint absent (0 hits).
- Comment 6137384793 (#116673) — fetched 2026-11-01, 9892 bytes, fingerprint absent (0 hits).
- Comment 6159746520 (#135039) — fetched 2026-11-01, 5409 bytes, link present, resolves 200.
- Comment 6244692039 (#69264) — fetched 2026-11-01, 18343 bytes, fingerprint absent (0 hits).
- Comment 6283695624 (#11548) — fetched 2026-11-01, 3059 bytes, date-anchored phrase present.
- Comment 5748269437 (#116788) — fetched 2026-11-01, 1036 bytes, generic replacement present.
- Comment 6247480404 (#140848) — fetched 2026-11-01, 1431 bytes, link present, resolves 200.
- Comment 6258090981 (#140980) — fetched 2026-11-01, 1148 bytes, link present, resolves 200.
- PR 140980 body — fetched 2026-11-01, @-tags present (5 unique handles).

## §6 — Verdict summary

- CLOSED: 9 (rows 3–11).
- COHERENCE-GAP: 2 (rows 1–2) — edits live, but top still shows old framing.
- STILL-OPEN: 0 among the 11 named checks.
- UNVERIFIABLE: 18 (§4) — not claimed either way.

No public writes performed. No public-surface changes. Read-only pass complete.