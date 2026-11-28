# CHILD-STATE — the child RFC's current asks + the staged edits (2026-11-28)

The child (the read-gap ticket, gist 577535cda874a7fc483ff9c69d5d6c86 = the audited child) proposes:
MemoryStore.read restored (the 12-line method per #141876, sha a43818a6...), the spec's guarded
property = STATELESS (live list unchanged by a read racing a writer); the lock tested
STRUCTURALLY (NBLCK flock on MEMORY.md.lock while the read holds it must fail — kvnloo spec (1));
the sanitized view (BLOCKED marker + blocked index, threat text withheld on the read's two paths);
a failed read logs a miss (3oltan's discriminator).

STAGED CHILD EDITS (word-gated, E1-E6 — see the enactments in the drop's CHILD-EDITS-STAGED-20261127.md):
E1 (3oltan point 3) add the read-INVOKED counter beside read-FAILED (three states: restored / broken / not called);
E2 (3oltan point 2) the structural regression test must cover the msvcrt Windows backend too;
E3 (kvnloo 7210367328 row 2) the anchor-first read rule gains its line in the parked list;
E4 (3oltan 7213322521) the open question resolves: narrower first slice, no merged-first;
E5 (kvnloo 7211318206) the stateless bar's receipt moves to kvnloo's 6609dac rows (pending the cold run);
E6 answer PR #12831 (the maintainer's prior refusal: "entries are already in the prompt") — the
frozen snapshot is exactly what a cold topic cannot answer from; the pre-registered falsifier measures it.
OPEN ASKS STANDING on the child: the prediction commit (337e87d1...) for kvnloo's 6609dac cold
re-run (the held-open arm does NOT cover #141876's bytes); nothing posts without the pair's word.
