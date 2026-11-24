`@kvnloo` and lab —

You asked for the expected failure signatures on the thread before any run on MAIN. They are below, fixed in advance and runnable cold from this comment alone. Every bar is pre-registered; a divergence is a receipt entry, never a renegotiated bar.

**the pre-registration**

Five elements are fixed before your run.
- The failing case, named: FB-2 — a second chain-doc `add` overwrites the first, because `_add_doc` writes the note's `content` as the whole file rather than appending a record.
- The ungated signature: `FIRST_SURVIVED_SECOND_ADD = False`.
- The fix signature: `FIRST_SURVIVED_SECOND_ADD = True`.
- The removal control: one add round-trips green on all three pins; a RED there invalidates the probe, never the finding.
- One hold-back class, withheld by clause — its signature is deliberately not written where a runner can read it, so a hint from the sequential case cannot satisfy it on its own. It stays withheld.

**the pins**

Three pins, each verified by `git rev-parse --verify`:

| Role | Pin | Status |
|---|---|---|
| MAIN read-less baseline | `0f602c5f6f18615632535251d62a2db74ce93b69` | `read` answers `Unknown action 'read'`; battery 409 pass |
| Class's home (`round2-gate`) | `268bb09147eaf948ece6a1beecd92a2268a5fc95` | 297/297 green, race red; the two-add lives here |
| Combined fix (GREEN reference) | `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` | locked, stateless, sanitized read; equivalently composed `ec649ad9` (443 pass, dispatch contract 64/64) |

**the signatures**

RED arm — ungated at `268bb091` and at `0f602c5f`, reported separately. In a fresh temp store: add FIRST with a unique marker-bearing body; add SECOND with a different unique body; re-read FIRST's key; compare bytes. Expected: `FIRST_SURVIVED_SECOND_ADD = False` — FIRST's bytes are absent, and the file holds SECOND's content where FIRST's had been, a whole-file overwrite rather than an append. On `0f602c5f` a `read` action returns `Unknown action 'read'`; recover at the file level and note the read-less baseline separately.

GREEN arm — the fix at `a9c65dc4`. Same two adds, same markers, same byte comparison. Expected: `FIRST_SURVIVED_SECOND_ADD = True` — FIRST's bytes survive, both documents present, FIRST byte-matching what was written. The three arms are `_file_lock`, `_sanitize_entry`, and a hardened `def read`; removing the lock or the no-cache-write alone stays green, removing both turns red. A RED here is the probe's own catch — record it as a divergence and check the control before calling the fix broken.

Control — on each of the three pins, one chain-doc add with a unique marker-bearing body, then re-read and byte-compare. Expected: green on all three. A RED on any control arm invalidates the probe, never the finding — re-run the control before drawing anything from the failure arms.

Receipts, already executed: `268bb091` gave RED, SECOND's 64 bytes only, `False`. `a9c65dc4` gave GREEN, 131 bytes, both present, `True`. The control was green on both. Your run is a confirm.

**the acceptance rows**

| # | Condition | Pre-registered bar |
|---|---|---|
| C1 | Survival across four compactions, verbatim | 100% of pinned constants survive four compactions byte-verbatim, with RED on MAIN / GREEN on the branch and the removal control RED — meaning the fix's removal arm (removing the fix turns the run red again), distinct from the single-add probe control above, which stays GREEN; one pinned constant lost, or any arm flipped, fails the row. |
| C2 | Stated cap with plain refusal, no eviction | Declaring a max entry count and adding beyond it yields a plainly reported refusal with no eviction and no silent eviction-by-summary — a dropped entry or a silent overwrite fails the row. |
| C3 | No second store (decision-ledger entry, byte-compared) | Exactly one pin entry in decision ledger #113309, byte-compared against the ledger's own schema with nothing invented — a parallel store or a schema mismatch fails the row. |
| C4 | The contradiction-flagged row, accepted as written at row 7122688366 | Carry the proposed fourth condition as written, flag and all: do not silently resolve or drop the flagged contradiction; reproduce it as stated and record the flag in the receipt. |

C4's verbatim, from your own row: "the pin is a second witness the summary does not author, and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it. The ledgers move with your rebase, KoNit-K's authorship kept, /pin stacked as its own commit."

**the wake read**

PARTIAL at `8ba4b344766e50c2e3eeaba84f4349276a1be021`. The scheduled wake reads `state.db`/`state.py` and writes its own session rows, but hits zero on every memory-store anchor — `memory_tool`, `store.add`, `_add_doc`, `preserve_session`, `DreamCycle`, `write_gate`. The memory-store write path is untouched, so the wake cannot disturb it.

**the ask back**

Your run confirms base-red at `268bb091`, combined-green at `a9c65dc4`, and the single-add removal control green on all three pins. Divergences are data — log them in the receipt and leave the bars as written.
