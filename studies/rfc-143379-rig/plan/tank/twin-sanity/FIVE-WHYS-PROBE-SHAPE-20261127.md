# 5Y — THE PROBE-SHAPE ANOMALY (STRUCTURAL CHECK, 2026-11-27)

*Defect observed: the structural lock check's FIRST run returned 9,658 inside-probes with ZERO blocked — a lockless measurement; the SECOND run (real fcntl) held the property (deterministic 100/100 blocked, control acquired) with a named release-window artifact on the natural arm.*

## Problem statement (Kettering)
**Mechanism:** a probe harness measures the shipped store's lock semantics.
**Design assumption:** the harness's stub block is neutral setup ("import scaffolding") — its assignments carry no semantic weight toward the code under test.
**Missing channel:** per-arm audit of stub semantics — nothing gates a probe on "the stub's semantics match the arm under test."
**Consequence:** measurement follows the harness, not the product; a lockless run can present as a structural finding.

## The five whys (one base question: why did the first run measure a lockless store?)
1. **Why did the NB flock never contend?** Because the store never took the lock — 0 of 9,658 probes blocked.
2. **Why did the store never take the lock?** Because `tools.memory_tool.fcntl` was `None` in the harness, and the store's `_file_lock` yields without locking when `fcntl/msvcrt` are both None (the store's own no-lock branch).
3. **Why was fcntl None?** Because the harness stub block set `mt.fcntl = None; mt.msvcrt = None` — copied verbatim from the kit's stall-probe stub, whose variants include the **lock-removed** arm (that assignment exists to disable the lock).
4. **Why was a variant-carrying stub copied as neutral boilerplate?** Because the stub block was reused as a unit ("module-setup boilerplate") without re-reading each assignment against the probe's intent — the semantic weight of `fcntl = None` is invisible inside the scaffolding.
5. **Why was that reuse unchecked?** Because the probe-construction path has no per-arm stub audit: nothing in the rig gates a probe on "the stub's semantics match the arm under test," and the first run's all-green-all-wrong output is indistinguishable from a true green until a control arm exists. **ROOT: probe harnesses are assembled from variant-carrying stubs with no per-arm semantic audit — the harness shape silently diverges from the shipped shape, and the divergence is invisible without a deterministic control arm.**

## The parent-class correlation (same mechanism, second instance)
kvnloo's finding 1 (comment 7210367328): "The envelope's lock row tests a reader that writes the cache, and the child doesn't ship one." — the fleet's ENVELOPE harness measured a cache-writing reader; the shipped read is stateless. Same parent: **probe shape ≠ shipped shape.** Two instances, one mechanism; the rig's own envelope was the first instance, my stub the second.

## The secondary finding (release-window artifact)
Natural-arm "inside successes" (3,042/18,766) = the store unlocks inside `with fd:` before the harness flag clears (the flag tracks context, not lock-state). Fix: instrumentation signals the LOCK (fd-level), not the context — or the natural arm stays an observation while the deterministic arm asserts (adopted).
