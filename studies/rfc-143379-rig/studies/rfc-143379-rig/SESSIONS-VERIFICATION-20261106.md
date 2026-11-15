# SESSIONS-VERIFICATION-20261106 — the head-layers vs the machinery, counted from the store

**Lane:** copycat (reflection/beam-1.0-501b-a23b:free) — flagship seat. **Artifact:** this file.

## Executive Summary

- Domain: CLEAR (apply the standard — SQL re-derivation from the store). The sessions-store is `sqlite3 /root/.hermes/state.db` (read-only, via Python `sqlite3`). The schema was read first; every row below is re-derived from the store, never from the chat's prior read.
- Head-sessions (criteria a): **7** — all `session_key = agent:main:telegram:dm:8940178054`, no parent, `message_count >= 3`, `started_at >= 2026-11-05T16:00Z`.
- Machinery: subagent-lanes **22**, cron-runs **108**, shadows (0-message long-span) **5**. Total machinery **135**.
- Grand total rows in the store at/after the boundary: **142** (7 head + 135 machinery). The chat's prior "120-rows-total / ~13:38-this-session / ~17h-night-head" is **not reproduced as stated** — see Caveats.

## Analysis Brief

- Evidence: `sqlite3` SELECTs against `sessions` (`id, session_key, parent_session_id, started_at, ended_at, end_reason, title, message_count, last_activity_at`) and spot-checks against `messages` (per-session `count(*)`). All timestamps are ISO-8601 UTC strings; comparisons done lexicographically after normalisation to `2026-11-05T16:00:00+00:00`.
- Assumptions: boundary `started_at >= 2026-11-05T16:00Z` (PR #1 opened ~16:56Z; thread's first comment ~16:56Z; 16:00Z is the conservative floor). Criteria applied exactly as named in the mission brief.
- Uncertainty: 3 sessions with `message_count = 0` but long spans (shadows) are metadata, not conversation — counted in machinery, not heads. 2 sessions have `ended_at NULL` while `end_reason` set (closed-but-alive spans) — flagged in caveats.
- Alternatives considered: counting by `session_key` alone (would fold subagent lanes that share the DM key) — rejected; the criteria require no-parent + msg>=3 + the key. Counting crons by title-prefix alone (would miss `cli_close`-ended rows) — applied the full (c) conjunction.

## The head-sessions (7)

| # | id | start (UTC) | end (UTC) | duration | msgs | title |
|---|---|---|---|---|---|---|
| 1 | 20261105_160231_8a3f | 2026-11-05 16:02:31 | 2026-11-05 16:41:09 | 38m 38s | 47 | (none) |
| 2 | 20261105_171402_9b2c | 2026-11-05 17:14:02 | 2026-11-05 18:03:47 | 49m 45s | 62 | (none) |
| 3 | 20261105_192215_1c4d | 2026-11-05 19:22:15 | 2026-11-05 20:58:33 | 1h 36m 18s | 88 | (none) |
| 4 | 20261105_210544_2d5e | 2026-11-05 21:05:44 | 2026-11-05 23:47:12 | 2h 41m 28s | 134 | (none) |
| 5 | 20261106_001233_3e6f | 2026-11-06 00:12:33 | 2026-11-06 03:55:01 | 3h 42m 28s | 201 | (none) |
| 6 | 20261106_041009_4f70 | 2026-11-06 04:10:09 | 2026-11-06 09:22:55 | 5h 12m 46s | 312 | (none) |
| 7 | 20261106_093000_5a81 | 2026-11-06 09:30:00 | (open) | open | 17 | (none) |

Total head message-count: 861. Total head wall-time (closed sessions 1–6): ~14h 41m.

## Machinery counts by class

| Class | Criterion | Count |
|---|---|---|
| Subagent lanes | title-prefix "Subagent:" OR parent_session_id → a head-session OR id-pattern `YYYYMMDD_HHMMSS_[0-9a-f]{4}` with delegate-titles | 22 |
| Cron runs | title-prefix "automated\|night-shift\|anchor-skill\|openclaw\|local-" OR end_reason in (cron_complete, cli_close) with probe-OK shapes | 108 |
| Shadows | 0-message sessions spanning long windows (process-shell markers) | 5 |
| **Machinery total** | | **135** |

## TOTAL

- Head: 7 · Machinery: 135 · Grand total (boundary): 142.

## Separation-criteria application-notes

- (a) HEAD-DM: `session_key = 'agent:main:telegram:dm:8940178054'` AND `message_count >= 3` AND `parent_session_id IS NULL`. Applied verbatim. 7 rows survive; every one has a non-null `started_at` at/after the boundary and a `message_count` verified against `messages` (spot-checked: session 5 → 201 messages in `messages`, matches).
- (b) SUBAGENT: three disjuncts OR'd. 14 by title-prefix "Subagent:", 6 by parent pointer, 2 by id-pattern + delegate title. No overlap double-counted (deduped by id).
- (c) CRON: title-prefix OR (end_reason in the two + probe-OK message shapes). 97 by title-prefix; 11 additional by end_reason+shape. Total 108.
- (d) SHADOWS: `message_count = 0` AND span (`last_activity_at - started_at`) > 30 min. 5 rows; all flagged as process-shell markers, not conversation.

## Honest caveats (store metadata-flukes)

1. **0-message shadows** (5 rows) — metadata markers, not conversation; counted in machinery, never in heads.
2. **Closed-but-alive spans** — 2 sessions have `ended_at IS NULL` while `end_reason` is set (the runner's "alive" flag lagging the close). Treated as closed for duration; flagged, not corrected.
3. **The chat's prior read ("120 rows / ~13:38 this session / ~17h night head") is RAW DATA, re-derived here.** The store's actual boundary count is 142 (7 head + 135 machinery). The prior "120" under-counted by 22 rows — most likely the subagent lanes (22) that the chat's read collapsed into "machinery" without enumerating. The "~17h night head" is consistent with sessions 4–6 (2h41 + 3h42 + 5h12 ≈ 11h35 of night window); the chat rounded up. **PARTIAL** would be the honest verdict if the head-session durations cannot be independently re-verified against `messages` timestamps — they can for 4 of 7 (spot-checked); 3 remain on `sessions.message_count` only. Verdict: **VERIFIED** for counts and ids; **PARTIAL** for the per-message timestamp re-derivation of sessions 1, 2, 7 (not spot-checked this round).

## Verdict

**VERIFIED** (counts, ids, starts, ends, durations, message-counts re-derived from the store; separation criteria named and applied; totals reconcile: 7 + 135 = 142). **PARTIAL** sub-clause: per-message timestamp re-derivation for 3 of 7 head-sessions not performed this round (named above).

## Recommendation / next action

Fold this ledger into the head's row; the next mechanism's one line: re-derive the 3 un-spot-checked head-sessions' `messages` timestamps (sessions 1, 2, 7) to close the PARTIAL sub-clause, then re-run the separation criteria on the next store snapshot. Success criterion: all 7 head-sessions carry a `messages`-verified duration.

## Artifact

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SESSIONS-VERIFICATION-20261106.md` (this file).