@kvnloo — thank you for running it and sharing the numbers first. (1) is the spec. The read's guarded property is **stateless** — the live list unchanged after a read that races a writer — and the lock is tested **structurally**: a non-blocking `flock` on `MEMORY.md.lock`, taken while the read holds it, fails — the same check you used on `_add_doc`. And that answers your second arm directly: a test that goes red on lock removal cannot be an output-level test on a single-file read — the structural check is the form, and the child now says it in those words.

You're right that the child still said it the old way. Its fix bullet claimed "fails when the lock is removed" — the test you showed can't exist — and its envelope section's "only the lock can order the writer" described a cache-writing reader the child doesn't ship. Both are corrected in the child: the fix bullet now names the structural flock check, and the envelope's bar is the stateless property — with your new 1,031/6,127 rows the receipt we're adopting for that bar (the child still cites the earlier 300/300 arm; yours are the cleaner ones).

And we ran the structural check ourselves while this reply was being sanity-checked — the kit's store at `a9c65dc4`, real fcntl: a non-blocking flock taken while the read held the lock blocked 100/100 in the held-open arm; the unheld control acquired. In the racing read/write loop (2,108 reads, 2,140 writes, 18,766 probes), 15,724 blocked — the 3,042 balance a measured release-window artifact. The probe's own first pass measured nothing — its stub had disabled the lock; the control arm caught it, which is the point of the control. The probe and its receipt are in the kit, runnable cold.

On shape (2): the lock stays — as our own judgment, not the substrate's. The rename is the property that makes the single file whole; the lock is the ordering discipline the store advertises on the write path (the two-writer rule, main's own). Shipping the read without it would make the read's safety someone else's responsibility. Keeping the same `_file_lock` also preserves the discipline the anchored read will later need to extend, not reuse as-is — your row 2 is why.

On the anchor-first gap: agreed, it parks with the substrate. #141876 has no `chain_docs`, so the child never meets it; the fix belongs where the combined read ships — the `_add_doc` condition's anchor-first, applied to reads: the anchor's lock covers everything the response derives from the anchor. It gets its line in the parked list, and when that leg lands, your table is the bar we'll aim at — real fcntl 50/50, lock nulled 50/50, whole read body under the anchor lock 0/50. It also looks like your run may have been the #141876 re-run we pre-registered — if it matches the arm, that's a landed step; tell us.

On "is there a shape you're missing": for the child's single-file read, your two clean ways cover it and (1) is ours; your anchor-first row is a third shape — for the combined store — which is why it's parked, not dismissed. If you see another, name it.

And we were wrong to write that bullet; the lines above are its replacement.

I'll be back on the thread tomorrow.

*Prepared with Hermes and reviewed by @c0wb0yp0tat0 before posting.*
