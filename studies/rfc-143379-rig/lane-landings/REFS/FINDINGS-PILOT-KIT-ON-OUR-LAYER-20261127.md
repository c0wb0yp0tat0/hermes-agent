# FINDINGS — the pilot kit on our layer (live test, 2026-11-27)

Origin: the operator's ask to test, in this session, whether we can gain the benefits of
3oltan-seo's pilot kit on our own layer, per https://github.com/NousResearch/hermes-agent/issues/143379.
Then: address the new comments (kvnloo 7210367328 + 7211318206, 3oltan 7213322521). Nothing posted;
findings staged for the pair's review. Discovery-log shape; MAP rows (asserted → status → basis) after the xngg1021
kernel's evidence-receipts discipline; receipts byte-verified, twice-read where the discipline applies.

## Verdict, one line

The hardened read WORKS on our layer — the installed runtime's store answers both anchors, stateless,
twice-read stable, file hashes unchanged; the agent's tool surface here does not expose the read action,
so read-invoked = 0 by construction (3oltan's point 3, state measured on our own rig); the installed read
is kvnloo's spec-2 shape (no lock — atomic rename is safety), while the child ships spec-1 per #141876.

## MAP matrix

| # | Asserted | Status | Basis (byte-verified) |
|---|---|---|---|
| F1 | The hardened read answers on our layer | PASS | Installed store `MemoryStore.read` (v0.23.1, 3b4215785882, `/usr/local/lib/hermes-agent/tools/memory_tool_store.py` L441-455): `read("memory")` → 11 entries, `read("user")` → 13 entries, message "Read MEMORY.md (11 entries)." |
| F2 | The read is stateless (guarded property) | PASS | Live: sha256 of `MEMORY.md` before == after the reads; twice-read JSON byte-identical. |
| F3 | Installed read holds no lock (spec-2 shape) | CONFIRMED | `grep -n "_file_lock"` → only L257 (def) + L350 (inside `_mutate`); read body L441-455 calls `_read_raw_checked` bare. Safety = atomic temp+rename (`_write_file` comment, L699-703) + strict decode. |
| F4 | #141876 read is spec-1 shape (lock-holding) | CONFIRMED | kvnloo's 6609dac run: structural row refused 50/50 vs acquired 50/50 (7211318206); `git show 6609dac` has `def read` at store L435. |
| F5 | Tool-surface gap: this session's memory tool = operations only (add/patch/remove) | CONFIRMED | This session's tool schema; read absent → read-invoked = 0 here. Installed `memory_tool.py` L119 + L412 DO register the read action — the wiring exists in the runtime, not on this surface. |
| F6 | Windows lock variant exists in production code | CONFIRMED | Installed `_file_lock` L285-296: `if fcntl: flock else: msvcrt.locking` — the msvcrt path ships; the child's regression test (real fcntl only) does not cover it. 3oltan's point 2 = test-coverage gap, not code gap. |
| F7 | Recurrence ground (K-recency instrument on our data) | MEASURED | 24h request-dump corpus: 30 dumps, 60 turns, 7 distinct literals, 173 re-mentions, median gap 30 turns, K=10 window carry 17.9% (31/173), cross-request carry 173/173 (100%). Corpus is retry-dominated (all `max_retries_exhausted`). |
| F8 | The dump corpus's failure family | CONFIRMED | All sampled dumps: `NotFoundError` 404 "This model is no longer available" on `meituan/longcat-2.5:free` — the longcat rotation on the fleet transport (021's register). |

## Discovery log (turns)

1. Anchor: MEMORY.md + chain INDEX (`?raw=1`) + 021 read fully + krecency-instrument, kvnloo-z0-ecosystem,
   aces-harness-probes, pin-framework, cto-session-brief, think-tank, forensics trio
   (defect-forensics, investigation-documentation, agent-work-review) loaded. The thread's live truth pulled:
   wave fired 04:33Z (7209894733), kvnloo rows 05:07 + 06:12, 3oltan 08:15, "Seen" 15:13.
2. Read restore test: direct store call (signature `read(target, doc, verb)` — first attempt failed on
   missing positional args; corrected). Two passes, identical JSON; hashes before/after equal. PASS.
3. Lock-shape forensics: read body printed twice; grep for `_file_lock` contexts twice. Spec-2 confirmed.
4. Tool-surface check: this session's schema (operations only) vs installed `memory_tool.py` L119/L412
   (read registered). Surface gap confirmed.
5. Recurrence leg: first parser found 1 turn per dump (parser defect — dumps wrap one request each);
   inspected shape (`request.body.messages` = the context stream); corpus scan with two independent
   passes (identical results — pass 1 == pass 2, 173/173).
6. WHOLE-ARC-INVENTORY + CHILD-RFC-LEAN + both posted comments read in full (twice where the display
   compacted on first read).

## Limitations

- The recurrence leg's ground is retry-dominated (failure captures); a successful long session's stream
  wasn't in the 24h window. The 17.9% K=10 carry is a lower-bound contour on the transport shape, not a
  full-session measurement. Limitation named, not extrapolated.
- The tool-surface gap (F5) is measured on THIS gateway session; other seats may differ.
- The live read test called `MemoryStore.read` directly (Python), not through the agent tool path —
  the store layer is verified; the surface routing is the named gap.

## Reproducibility

- Read test: `python3` + `sys.path.insert(0, '/usr/local/lib/hermes-agent')`;
  `MemoryStore().read('memory', None, 'read')` and `read('user', None, 'read')`; hash-compare
  `/root/.hermes/memories/MEMORY.md` before/after.
- Lock-shape: `grep -n "_file_lock(" /usr/local/lib/hermes-agent/tools/memory_tool_store.py`.
- Recurrence: execute_code pass in this session (script in transcript), two independent passes.
- Chain reads: `curl "http://100.112.72.20:8789/memory-chain/INDEX.md?raw=1"` (payload route, not shell).

## Fold notes

- The child's fix bullet: add the read-invoked counter (3oltan's point 3) — staged, not applied.
- The child's regression test: Windows/msvcrt branch must be covered (3oltan's point 2) — staged.
- The child's parked list: anchor-first line (kvnloo 7210367328 row 2) — staged.
- The child's Open Questions: "narrower first slice" — resolved by 3oltan 7213322521; merged-first: no — staged.
- The 6609dac re-run: the held-open arm does NOT cover #141876's bytes; prediction artifact staged
  (PREDICTION-KVNLOO-6609DAC-ROWS.md); commit is the one pending public write, waits the pair's word.
