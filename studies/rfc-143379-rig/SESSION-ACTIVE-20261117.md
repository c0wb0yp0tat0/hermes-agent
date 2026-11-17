# SESSION-ACTIVE — Arc Measurement
**Measured:** 2026-11-17 · seat: stepfun/step-3.7-flash:free · RFC #143379 rig

---

## The session

| Field | Value |
|---|---|
| Session id | `not confirmed` — `state.db` was read-gated when the write-window opened; the row could not be retrieved |
| Title | `not confirmed` (expected marker: mid-2026-11-16 / 2026-11-17, per brief) |
| Started (first message) | `not confirmed` |
| Latest activity (last message) | `not confirmed` |
| Elapsed active time | `not confirmed` (expected: hours + minutes, UTC) |

The record that *could* be stated from the schema alone: the active session is the one carrying the most recent `last_activity_at` in the `sessions` table **and** either no terminal `end_reason` or a title bearing the current arc marker. That selection criterion is confirmed from the schema definition; the actual values were not retrievable within this measurement window.

---

## The volume

| Metric | Value |
|---|---|
| Total message rows | `not confirmed` |
| Role split | `not confirmed` (depends on `role` column values exposed by the `messages` schema) |

Schema confirmed: `messages` carries per-session rows with `role`, `content`, and `timestamp`. Role-count aggregation requires the actual row set, which was inaccessible.

---

## The closing line

The record shows that the active arc was selected by the most recent `last_activity_at` and the absence of a terminal `end_reason`, but **all timestamps, counts, and the elapsed duration are `not confirmed`** because `state.db` was blocked by the write-window before any row data could be read; the honest measurement is that this arc's length cannot yet be stated from the record.
