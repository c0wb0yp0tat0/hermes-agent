# KVNLOO's STALL-ON-READ ARM — reference (row 7143199711, fetched 2026-11-24T20:12:51Z)

*The reply to our seek-to-understand question. Ground for the fleet's recon pass — every claim to be verified against the pin's bytes before it rides.*

@c0wb0yp0tat0, you're right, and I should have caught it: "removing both turns it red" is our claim from 11-23, not something you predicted. Thanks for tracing it back, and for running the concurrent double-add arm.

To answer your question: it's the second shape, **a read straddling a write**. It isn't a double-add. The test is `test_doc_reader_and_writer_keep_latest_live_state` at `a9c65dc4` (tests/tools/test_memory_chain_docs.py#L198-L244), and it doesn't depend on timing:

1. Seed the chain doc with `initial`.
2. A reader thread calls `store.read("doc:…")`, takes its disk snapshot, then blocks on an `Event` before returning.
3. A writer thread runs `store.add("doc:…", "latest")` and commits.
4. Release the reader, then assert the read returned `["initial"]` while the live list and the tool-level `read` both still say `["initial", "latest"]`.

With #116673's original `read()`, step 2 loads that stale snapshot back into the live cache when it resumes, which rolls the writer's commit back. On 11-23, at that pin:

| `read()` variant | Result |
|---|---|
| as at `a9c65dc4` (snapshot under `_file_lock`, live lists untouched) | green, 17/17 |
| lock removed, still no cache write | green |
| cache write restored, under the lock | green |
| both removed (= #116673's read) | **red**, 16/1: `['initial'] == ['initial', 'latest']` |

Either arm alone is enough. With the lock, the writer waits behind the paused read. Without the cache write, the stale snapshot never reaches the live list. That's why your sequential two-add stays green with both removed: it never puts a read across a write. The `read()` in question is `memory_tool_store.py#L551-L566`.

*These are the 11-23 receipts at the same pin. I didn't re-run them today.*

I'd treat it as an arm separate from FB-2, with the predicted signatures from the table: green, green, green, red. Your double-add shows the lock matters for writer-writer races. This one shows that both arms together cover reader-writer races.

**Does that match the arm you'd pre-register, or would you rather pause the reader somewhere else, e.g. inside the writer's commit?**

*Prepared with an AI agent and reviewed before posting.*
