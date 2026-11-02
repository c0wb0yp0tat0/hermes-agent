# NIGHT-654-R2-LEG1 — the #659 runner probe against the published head (2026-10-30)

Card: t_ada1c4fac1d04 (NIGHT-654-R2, SECOND PASS — loop clause fired). The first
pass landed end-to-end (LEG1-5 verified); the fold's loop-state named this leg's
brief from the remaining seams. This is R2-leg1: **the seam probe + validation of
kvnloo/hermes-agent#659's fixed-substrate runner against the published head
`b84150e9be`** — the real substrate, not a stand-in.

> Verdict line: **PROBED — THE SEAM IS REAL AND NAMED.** The as-published #659
> runner (head `5184f7a1`) **refuses to run against the published head**: exit 1,
> `RuntimeError: Candidate already contains injected test path; refusing
> overwrite`, raised before a single test executes. Root cause byte-verified:
> the round-two substrate already ships its own copy of the shared falsifier
> probe at the runner's injection path — consent fixture byte-identical, probe
> file a strict prefix (missing the four encoding-freshness tests). No runner
> receipt was produced and none is claimed; **NOT_CERTIFIED stands**, now with a
> named why. Nothing in P1/P2/P3 changes; the 297 battery's own re-run stands
> (297/0/0 on the published tree, LEG2).

---

## 1. What was run (exact, re-runnable)

Runner source: `kvnloo/hermes-agent` PR #659 head `5184f7a1` (branch
`study/rfc143379-shared-falsifiers-20261026`), files extracted from the git
object store — `run_fixed_substrate.py`, `test_real_checkout.py`,
`consent_scenarios.json`, `test_fixed_substrate_runner.py`,
`RUNNER-SELFTEST-20261026.json`.

```bash
cd /tmp/rfc659-runner
python3 run_fixed_substrate.py \
  /root/hermes-agent-pr \
  b84150e9be88911280f981467de9628fcfb0f60f \
  /tmp/rfc659-runner/out-r2leg1 \
  --suite-manifest /tmp/rfc659-runner/suite-297.txt
```

- Candidate repo: `/root/hermes-agent-pr` (contains the published commit object:
  `git cat-file -e b84150e9be^{commit}` OK).
- Suite manifest `suite-297.txt`: the 15 test paths exactly as enumerated in the
  published `KVNLOO654-297-BATTERY-MANIFEST-20261030.md` §1, one per line —
  sha256 `c83d072f92b00b692157bd9af9d9a045d4a9d93b81b76b69d7fc347d097c4fcc`.
- Fresh output dir `/tmp/rfc659-runner/out-r2leg1` (the runner refuses an
  existing dir; none was created by the run — the guard fires before run_one).

## 2. The result — a hard refusal, exit 1

```
Traceback (most recent call last):
  File "/tmp/rfc659-runner/run_fixed_substrate.py", line 225, in <module>
    raise SystemExit(main())
  File "/tmp/rfc659-runner/run_fixed_substrate.py", line 177, in main
    raise RuntimeError("Candidate already contains injected test path; refusing overwrite")
RuntimeError: Candidate already contains injected test path; refusing overwrite
EXIT: 1
```

- No `receipt.json` — the guard is in `main()` before any `run_one` invocation.
- The failed run left no stray worktrees (`git worktree list` clean after;
  the runner's `finally` removed the temp worktree).
- The runner itself is healthy and is the exact repaired artifact Kevin's
  selftest receipt records: its 14 offline selftests pass here
  (`python3 -m unittest discover -s . -p test_fixed_substrate_runner.py` →
  `Ran 14 tests ... OK`, 0.408s), and the runnable files' git blobs match the
  receipt's source readback (`2494ecb4` runner, `c17b66b7` tests).

## 3. Why — the byte-verified root cause

The runner's design (its README + the guard at L175-177): the candidate is
expected to be a *pristine* fixed substrate; the runner **injects** its own
unchanged #654 probe as `tests/tools/test_rfc_homework.py` and its consent
fixture as `tests/tools/rfc_consent_scenarios.json`, and **refuses to overwrite
either path if the candidate already contains it**.

The published head `b84150e9be` **already contains both paths** — the round-two
combined substrate ships the shared falsifier probe in-tree:

| Path at `b84150e9be` | State vs the runner's injection | Evidence |
|---|---|---|
| `tests/tools/rfc_consent_scenarios.json` | **byte-identical** to the runner's fixture | sha256 `f9076148…` on both sides |
| `tests/tools/test_rfc_homework.py` | strict prefix of the runner's probe: first 130 lines byte-identical (same 5 test defs incl. the 12-scenario consent param); **missing the four encoding-freshness tests** | `diff <(git show … | head -130) <(…probe… | head -130)` → identical; defs diff shows only the 4 additions |

The candidate's own probe covers the runner's required set partly:
`test_read_dispatch_contract` ✓ · `test_read_concurrency_snapshot` ✓ ·
`test_chain_doc_reference_race` ✓ · budget-candidate advisory ✓ · consent ×12 ✓
— but **none** of the four `encoding_freshness` alternatives exist anywhere in
the candidate's `tests/tools` (grep: 0 matches, tree-wide scan of the def names
in the whole tree: 0). So even a hypothetical guard-bypass that ran the
candidate's own file would collect 0 tests for the encoding selector →
`tests > 0` unmet → `required_green` False → NOT_CERTIFIED.

## 4. Consequence — precise, honest

1. **The as-published #659 runner cannot validate the published head.** Its own
   integrity guard (no-clobber of a candidate's in-tree probe) fires on the real
   round-two substrate. The runner needs an "already-pinned probe" mode (verify
   byte-identity, skip injection, run the candidate's own copy) or a candidate
   that does not carry those paths — that is a runner-side change on #659, not
   something a validation run can conjure, and **no receipt was fabricated** by
   bypassing it.
2. **The substrate's probe file lacks the encoding-freshness family.** If Kevin's
   certification frame includes those four falsifiers, the round-2 probe file
   needs them added — a develop-side seam, now visible and named.
3. **Nothing in P1/P2/P3 changes.** The published SHA is still
   `995de91d28…` (parent of the head, unchanged), the head still
   `b84150e9be` (re-probed by ls-remote this run, 00:59 EDT), the 297 manifest
   still exact (sidecar `44ae6e30…` matches disk byte-for-byte), the 297 battery
   re-run still stands (297 passed / 0 failed / 0 skipped, 14.90s, LEG2).
4. **Kevin's frame is answered with the runner's own terms:** his runner reports
   NOT_CERTIFIED until the exact 297 list is published — the list IS now
   published on the branch (commit `b84150e9`) — and the next blocker his
   runner hits is its own injection guard on the substrate's in-tree probe.

## 5. Seam B — the P3 gate's Nov-1 window (checked live this run)

- `kvnloo/hermes-agent` Actions: 3,699 runs total, **latest 2026-10-09** —
  nothing since Oct 9 (the draft's line holds).
- Our fork `c0wb0yp0tat0/hermes-agent`: 13 runs, latest **2026-10-20**.
- Gate remains closed (needs 2,402 reference min vs 1,722 allowance; allowance
  resets at the **Nov 1 00:00 month roll** — the earliest possible open; the
  fresh snapshot is Kevin's side to take). Unchanged, re-verified, no overclaim.

## 6. Seam C — fresh motion (checked live this run)

- #654 thread: last comment `6514625145` (the user's own check-in,
  2026-10-30T04:00:08Z) — nothing after it.
- #659: 0 comments; state OPEN; `updatedAt` 2026-10-26 (unchanged).
- #653 (tracking): last event 2026-10-23 `subscribed`. No motion.
- Both forks' Actions silent (above). **No fresh motion to fold.**

## 7. The honesty line

- Every claim above is backed by a re-runnable command or a byte compare; no
  SHA was invented; no receipt.json was written (the runner never ran a test).
- Nothing public was written: no comment, no push, no issue. The morning
  comment draft stays staged and **posts on the user's word only** (this run
  added a P4 note naming the runner seam — see the amended draft).
- Loop-state line: **SECOND PASS LEG-1 PROBED → RUNNER SEAM NAMED
  (GAPS REMAIN → HOLD on the runner's certification; the publish side is
  complete)**. Re-arm options for the next iteration: (a) the runner gains the
  already-pinned-probe mode (Kevin-side, on #659), (b) the substrate probe gains
  the encoding-freshness family (develop-side), (c) the Nov-1 roll re-check.

*Written 2026-10-30 ~01:00 EDT by the R2-leg1 probe run (t_ada1c4fac1d04). Cold-readable:
every claim is a command or a diff in the run.*
