# KVNLOO-COMMENT-7210367328 — verbatim (the substrate the sanity rides on)

Fetched 2026-11-27. Author: kvnloo. Created 2026-11-27T05:07:22Z.

> @c0wb0yp0tat0 Short answer: **for the read on its own, the spec stops before the rule does. The rule itself stops at the anchor read once chain docs exist.** I ran both before replying. Setup: the `a9c65dc4` store in the kit's sandbox with real `fcntl` loaded, Python 3.15.2, macOS, 50 trials per row. `main` at `7c57dbf` still has no `read`.
>
> ### 1. "Fails when the lock is removed" can't happen for the read #141876 ships
>
> `read` at `6609dac` (tools/memory_tool_store.py#L435-L455) takes one file's lock, reads that file and never writes the live list. Writers go through `_write_file`, which writes a temp file and renames it into place (L906-L913), so even a reader without the lock only ever sees a whole file. I looped `read("memory")` while a writer appended 20 entries, then checked every returned list against the committed prefixes:
>
> | `_file_lock` | reads | not a committed prefix |
> |---|---|---|
> | real `fcntl` | 1,031 | 0 |
> | nulled | 6,127 | 0 |
>
> So no test on this read's output can go red when the lock is removed. The envelope's lock row (the arm from my last comment) tests a reader that writes the cache, and the child doesn't ship one. I see two clean ways to write the spec:
>
> 1. Make "stateless" the guarded property: the live list is unchanged after a read that races a writer. Test the lock structurally: a non-blocking `flock` on `MEMORY.md.lock`, taken while the read is inside it, fails. That's the same check I used on `_add_doc`.
> 2. Or drop the lock from the read, and state that the atomic rename is what makes it safe.
>
> ### 2. Where the rule stops: the anchor read with chain docs
>
> On the combined store, `read` at `a9c65dc4` releases `MEMORY.md.lock` after the snapshot. It then builds `chain_docs` from that snapshot but `orphan_docs` from a fresh disk read (L284-L297). If a `remove` of the `@doc:alpha` entry commits in that gap, the response names `alpha` as both a chain doc and an orphan. The disk never held that state at any single moment. To widen the gap, the harness holds `doc_stats` until the remove commits; the store code is unchanged.
>
> | row | `alpha` in both lists / 50 |
> |---|---|
> | real `fcntl` | 50 |
> | lock nulled | 50 |
> | whole read body under the anchor lock | 0 |
>
> The lock can't help, because it's already released before the cross-file part runs. This is the anchor-first rule from the `_add_doc` condition, applied to reads: **the anchor's lock covers everything the response derives from the anchor**. It belongs with the parked substrate, not the child, since #141876 has no `chain_docs`. It's worth a line in the parked list so it doesn't get lost.
>
> **Which one does the child mean: (1), stateless plus a structural lock check, or a test that goes red on lock removal? If it's the second, I can't find an output-level test for a single-file read. Is there a shape I'm missing?**

## The substrate code kvnloo names (pinned)
- `read` (the shipped read): commit `6609dac`, tools/memory_tool_store.py#L435-L455 — takes one file's lock, reads, never writes the live list.
- `_write_file`: the a9c65dc4 store, L906-L913 — temp file + atomic rename.
- combined `read`: a9c65dc4, L561-L577 — releases MEMORY.md.lock after the snapshot; `chain_docs` from the snapshot, `orphan_docs` from a fresh disk read (L284-L297).
- his harness row-2 wrapper: holds `doc_stats` until a concurrent remove commits.

The draft reply rides THIS substrate: every claim in the draft must agree with these rows and this code, nothing else.
