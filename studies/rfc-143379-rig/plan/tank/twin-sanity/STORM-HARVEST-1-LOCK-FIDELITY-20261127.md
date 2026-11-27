# STORM-HARVEST-1-LOCK-FIDELITY-20261127 — the probe-shape defect, cross-referenced

*Reframe (Kettering): probe harnesses are assembled from variant-carrying stubs with no per-arm semantic audit; measurement follows the harness, not the product. Storm classes: flock semantics, release windows, atomic-rename readers, test-double fidelity. Distilled per class — source URL + the literal line + the seam it names. All results served by the exa keyless tier (searxng down this window; noted per the down-protocol).*

## 1 · flock(2): independent fds contend, release has no sequencing
- **Source:** man7.org/linux/man-pages/man2/flock.2.html (flock(2) manual, current).
- **Lines:** "If a process uses open(2) (or similar) to obtain more than one file descriptor for the same file, these file descriptors are treated independently by flock(). An attempt to lock the file using one of these file descriptors may be denied by a lock that the calling process has already placed via another file descriptor." · "Release of a lock when a file descriptor is closed is not sequenced after all observable effects of close(2)."
- **Seam:** legitimizes the structural check's held-open arm (same-process tester fd contends — 100/100 EWOULDBLOCK, observed) AND names the natural arm's artifact: the release is not sequenced with the harness flag's clear — the 3,042 "inside successes" are the observed unsequenced-release window, exactly as the man page predicts. Also: flock↔fcntl locks do not interact (Linux) — the store's consistent flock usage is the safe side; any future fcntl-record-lock in the same tree would bypass it (seam for the parked substrate).
- **Confirmation:** stackoverflow.com/questions/68845147 (same-process second-fd contention blocked — the exact mechanism, with a demo program); notryan.com/pdf/flock.pdf ("independent file descriptors, e.g. created using two open calls, don't share the lock acquisition").

## 2 · The release-window class is real and measurable
- **Source:** stackoverflow.com/questions/45823707 ("delay between close(fd) and releasing of flock").
- **Line:** contention "usually recovers within max 5 retries of interval 1ms" in a complex threaded program — close-time release is not atomic-with-close in practice.
- **Seam:** the child's regression test must treat EACCES as contention too (the field's own set): github.com/tox-dev/filelock src/filelock/_unix.py — "_CONTENTION_ERRNOS: {EACCES, EAGAIN, EWOULDBLOCK}" — a filesystem can report EACCES where EWOULDBLOCK is expected; a test that only catches EWOULDBLOCK will flake/false-pass on such filesystems. Spec change: the structural check treats all three as "blocked."

## 3 · The inode-split trap (what the store already avoids)
- **Source:** github.com/tox-dev/filelock (src/filelock/_unix.py) — "Unlinking a locked file on Unix splits waiters across inodes and breaks mutual exclusion for processes that coordinate via the same path."
- **Seam:** the store never unlinks MEMORY.md.lock (only fchmod-tightens the open inode) — its design already dodges the trap; the child's future writer-side changes must keep the rule (lock-file lifecycle: create/keep/reuse, never unlink while locks are in use).

## 4 · Atomic rename: whole-file reads, qualified
- **Sources:** cs.utexas.edu/~witchel/378AC/lectures/040_wal_internals-slides.pdf (the rename recipe: write → fsync → rename → fsync-dir); learn.padho.ai/wiki/flushing-a-memtable-to-an-sstable ("rename() is only atomic with respect to the filesystem metadata — fsync the data, then rename"); docs.rs/vaultdb-core writer::atomic_write_with ("Concurrent readers either see the full old content or the full new content; they never see a partial write").
- **Seam:** kvnloo's shape-(2) claim is field-validated but only for *file* reads: rename grants whole-file visibility, it does not order an in-memory live list — which is precisely WHY the child keeps the read stateless AND keeps the lock (shape-(1) remains the honest choice). Durability caveat: the recipe includes fsync(tmp)+fsync(dir); the store's `_write_file` (atomic replace per a9c65dc4 L906-913) should verify its fsync posture against the recipe (seam for the write-gate review, parked).

## 5 · The parent class: test-double drift (the rig's own envelope was the first instance)
- **Source:** martinfowler.com/articles/mocksArentStubs.html (Fowler, 2007, Meszaros vocabulary) — stubs "provide canned answers," a double "can drift"; senior-stack.uz Over-Mocking ("Mocks don't fail when reality changes — they keep returning what you scripted... the most expensive place to find a bug"); specstory.com mocks-vs-stubs ("A double can drift from the real component. When the real component changes its interface or its rules, tests against the old double keep passing") and its rule: "a mock at a boundary is only acceptable when a slower, higher-fidelity test covers the same seam."
- **Seam:** the nulled-fcntl stub was a drift of the exact class (the kit's stub *is* the lock-removed arm; reusing it as boilerplate measured a lockless store). kvnloo's finding-1 (comment 7210367328) is the SAME parent: the envelope's lock row tested a cache-writing reader the child doesn't ship. The cure the field names is the cure we adopted: keep the cheap probe, add the deterministic control/high-fidelity arm that checks the seam against reality.

## Meta-finding
The storm validates the rig's shape rather than inventing: the structural check (deterministic arm + control) IS the field's "high-fidelity backstop at the boundary" — formalized, not new. The one spec change the child should take: contention errnos = {EACCES, EAGAIN, EWOULDBLOCK}.
