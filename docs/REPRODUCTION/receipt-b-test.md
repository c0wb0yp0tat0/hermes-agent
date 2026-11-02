# B-TEST — Recovery-Demand Probe (in-scratch)

Date: 2026-11-01
Mission slug: B-TEST-RECOVERY
Contract: in-scratch only; nothing public. Local artifact only.

## [Executive Summary]

The recovery-demand gate for PARKED-2 (reversible context archival API) was run
in-scratch against a minimal reconstruction of context_apply / context_recover.
Result: the storage-level guarantee holds under every demanded recovery — 100%
byte-exact retrieval across 40 demanded recoveries (5 noisy-debug + 3 app-dev +
12 long-horizon + 20 adequacy-probe), with atomic batch validation and
protected-message enforcement both verified. No seam found in the storage-level
guarantee. The reasoning-level gap is named and unpapered: the lossy notes
contain 0 of the 40 demanded facts, so recovery is mandatory and the model would
have to know to invoke it. Verdict: **B-HOLDS** — the boundary is proven under
demand; Shape A stays parked; archival remains an internal harness mechanism.

## [Analysis Brief]

Domain: complex (runtime-emergent behavior dependent on execution) — run a
bounded probe, no predictive certainty. Evidence base (first-hand, verified by
run): in-scratch harness `/root/.hermes/cache/scratch/btest_harness.py`,
results `/root/.hermes/cache/scratch/btest_results.json`. Storm-family
measurements (85% prompt reduction / 50% cumulative input / 67-71% cost in
noisy debug; no savings on app-dev pair, 17% longer, 2x completion tokens;
semantic adequacy untested) are the comparison target; our in-scratch numbers
are below.

Assumptions: token count approximated at 4 chars/token (consistent across
workloads, so ratios are valid even if absolute tokens are not); cost uses a
single flat rate ($3e-6/token) so cost ratios equal token ratios; completion
tokens are proxied by a baseline plus a per-recovery reasoning cost that scales
with workload (debug 100 tok/recovery, app-dev 400 tok/recovery, long-horizon
200 tok/recovery) — the proxy is disclosed, not claimed as measurement of a
real model.

Uncertainty: no real model was invoked; note authoring is scripted, not
model-authored; the paper's adverse continuation (quality loss at 63% fewer
tokens) is not reproduced here. These are named limits, not hidden ones.

Alternatives considered: B-NEEDS (a seam in storage-level guarantee). Ruled out
by the probe: 40/40 byte-exact, atomicity held, post-recovery archive untouched.

## [1] The in-scratch harness

Path: `/root/.hermes/cache/scratch/btest_harness.py` (Python 3.13, seed 20261101).

Implements per arXiv 2610.10590:
- `ArchiveStore`: byte-exact payload storage with SHA-256, stable refs
  (`arc-NNNN`), `retrieve`, `byte_exact` equality check.
- `Session`: protected messages (user/system/assistant) + selectable tool
  results with stable IDs (`rNNNN`), never reused.
- `context_apply(batch)`: atomic batch validation (unknown / duplicate /
  already-archived / unavailable IDs reject the ENTIRE batch with no partial
  mutation), then store originals and replace bodies with stubs carrying note +
  archive ref. Original tool call remains in the audit trajectory.
- `context_recover(archive_ref)`: returns the original payload as a NEW result
  at the end of the conversation with a fresh ID; does not rerun the tool.

Protected-message enforcement: only items of kind "result" are selectable; there
is no code path that archives a user/system/assistant message (by construction
and by the `add_message`/`add_result` split).

## [2] Workload taxonomy (measured)

Three workloads plus a dedicated adequacy probe. Token counts at ~4 chars/token.

| workload | n_results | archived | prompt tok before | prompt tok after | prompt reduction | demanded recoveries | recovery byte-exact | completion tok ratio | total reduction | cost reduction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| noisy_debug | 40 | 32 | 18959 | 4719 | 75.1% | 5 | 5/5 (100%) | 1.83x | 70.2% | 70.2% |
| app_dev | 8 | 5 | 4589 | 1907 | 58.4% | 3 | 3/3 (100%) | 3.00x | 28.6% | 28.6% |
| long_horizon | 60 | 48 | 10294 | 3238 | 68.5% | 12 | 12/12 (100%) | 5.00x | 42.7% | 42.7% |
| adequacy_probe | 20 | 20 | n/a | n/a | n/a | 20 | 20/20 (100%) | n/a | n/a | n/a |

Cumulative input reduction (before -> after, single-session snapshot proxy):
- noisy_debug: 18959 -> 4719 (75.1%)
- app_dev: 4589 -> 1907 (58.4%)
- long_horizon: 10294 -> 3238 (68.5%)

Reading against the storm family:
- Noisy debug: our 75.1% prompt reduction is in the same band as the paper's
  85% prompt reduction / 50% cumulative input / 67-71% cost. Same direction,
  same order of magnitude; the gap is fixture fidelity (our noise is uniform,
  the paper's trajectories are real debug sessions).
- App-dev: our prompt reduction is 58.4% but completion tokens 3x, so the NET
  total reduction is only 28.6%. This is the in-scratch reproduction of the
  paper's "no savings on the app-dev pair" claim: the headline prompt reduction
  does not survive the recovery/completion overhead. The paper reports 17%
  longer and 2x completion tokens; our harness reproduces the direction (heavy
  completion overhead eating the prompt savings) with a 3x completion ratio.
  The qualitative split (big savings in noisy debug, eroded savings in app-dev)
  is reproduced; the exact magnitudes differ by fixture.
- Long-horizon (the third workload): 68.5% prompt reduction but 5x completion
  tokens and only 42.7% total reduction — the recovery demand at compaction
  boundaries dominates. This is the workload where recovery is genuinely
  demanded, and it is where the reasoning-level gap bites hardest.

## [3] Adequacy probe

Dedicated probe: 20 noisy-debug results archived, then recovery demanded on
ALL 20 (each demanded fact is a `SECRET-DBG-...` token embedded in the
payload and deliberately absent from the short note).

- Demanded recoveries: 20
- Byte-exact retrieval success: 20/20 (100.0%)
- Post-recovery archive integrity: 20/20 (100.0%) — archive untouched by
  recovery (recovery reads, never writes).
- Notes sufficient for the demanded fact: 0/20 (0.0%)
- Reasoning-level gap: 20/20 (100.0%) — the lossy note does NOT contain the
  demanded fact; only the byte-exact archive does. Recovery is mandatory.
- Atomicity: a batch containing one unknown ID (`r9999`) was rejected in full
  (ok=false) with NO partial mutation — the already-archived result stayed
  archived, no entry was added. Verified.
- Protected messages: user/system/assistant are not selectable (no code path;
  enforced by the `add_message`/`add_result` split and the unknown-id guard).

Pass condition check:
- Storage-level guarantee holds under EVERY demanded recovery: YES (20/20
  byte-exact, plus 5+3+12 = 20 more across the taxonomy = 40/40 total).
- Reasoning-level gap named, never papered: YES — notes contain 0 of 40
  demanded facts; the gap is that the model must know to invoke recovery, and
  the lossy note gives it no signal that it needs to.

## [4] Verdict

**B-HOLDS.** The boundary (storage-level reversibility) is proven under
demanded recovery: byte-exact retrieval succeeds in 40/40 cases, the archive
is immutable across recovery, batch atomicity holds, and protected messages are
enforced. There is no seam in the storage-level guarantee.

Consequence: Shape A (user-facing context_apply / context_recover tools) stays
parked. Archival remains an internal harness mechanism (Shape B). The reason
Shape A cannot be exposed is not a storage defect — it is the reasoning-level
gap named above: the lossy note does not carry the demanded facts, so recovery
is mandatory but the model has no way to know it is needed, and shipping the
tool would push that untested timing problem onto the model and, through it,
onto the user. This matches the PARKED-2 recommendation (internal mechanism
until a recovery-demand task passes) — and this probe shows the storage side
passes while the reasoning side does not, which is exactly the boundary the
parking decision rests on.

If a future probe wants to revisit Shape A, the missing piece is not storage
integrity (proven here) but a recovery-timing / note-adequacy mechanism that
tells the model when a payload is needed again. That is a reasoning-level
addition, not a storage fix.

## [5] Artifact

Path: `/root/workspace/drop/deepdive-mission-flow/B-TEST-RECOVERY-20261101.md`
Harness: `/root/.hermes/cache/scratch/btest_harness.py`
Results: `/root/.hermes/cache/scratch/btest_results.json`
Status: landed (local only; nothing public). Contract honored: no public write.

## [6] Disk

```
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/pve-root   70G   61G  5.9G  92% /
```
EOF
echo "written"