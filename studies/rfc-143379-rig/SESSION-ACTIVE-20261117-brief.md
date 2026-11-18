# SESSION-ACTIVE brief — measure this session's arc (seat: stepfun/step-3.7-flash:free)

**You are the arc-measurement lane.** The operators are tracking long arcs and need the active session's true age, measured from the record — never guessed.

## The task
1. READ `/root/.hermes/state.db` (read_file auto-extracts SQLite: schema, row counts, first rows). The `sessions` table is keyed by `last_activity_at`, with `title` and `end_reason`; the `messages` table holds per-session rows with `role`/`content`/`timestamp`.
2. FIND the session that is currently active — the one with the most recent `last_activity_at` and no terminal end_reason (or the one whose title contains the current arc's marker, likely mid-2026-11-16/17).
3. MEASURE, from the record: session id; when it started (first message timestamp / created); when it most recently wrote (last message timestamp); the elapsed active time between those two (report in hours+minutes, and state UTC); total message rows; counts by role if the schema exposes it.
4. WRITE `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/SESSION-ACTIVE-20261117.md`:
   - `## The session` — id, title, start, latest activity, elapsed (with the clock quoted).
   - `## The volume` — message rows and role split, as the schema presented them.
   - `## The closing line` — one sentence on what the record shows about this arc's length.
5. If the current session cannot be distinguished from the record with certainty, say exactly what you could and could not determine, with "not confirmed" where the record was ambiguous — the honest measurement beats the neat one.

## Disciplines (binding)
One tool call per round. The SQLite extract comes through read_file; do not attempt terminal commands beyond needed local reads — this measurement is reads + one write. ≤6,000 chars per write. No commits, no pushes — the fold belongs to the head. When the artifact is complete, stop.
