# A-TEST — Independent Model-Facing Surface Probe (in-scratch)

Date: 2026-11-01
Mission slug: A-TEST-INDEPENDENT
Contract: in-scratch only; nothing public. Local artifact only.

## [Executive Summary]

The independent A-test probes the user-facing (model-facing) surface of
context_apply / context_recover — the surface Shape A would ship — on its own
merits, separate from the B-test's internal-harness probe. Result: the exposed
interface introduces NO loss of its own. Byte-exact retrieval holds 40/40
demanded recoveries at the model-facing boundary (5 noisy-debug + 3 app-dev +
12 long-horizon + 20 adequacy), with 0 serialization failures and 40/40
conversation-recovered payloads byte-exact. Atomic batch validation, protected-
message enforcement (by construction), and all failure modes (duplicate / unknown
id / already-archived / unavailable / unknown ref / malformed JSON) reject
correctly with no partial mutation. The misuse surface is bounded: the
controlled misuse scenario produced 3 rejected misfires and a blast of 2
recoveries / 200 completion tokens. BUT the reasoning-level gap is unchanged
at the surface: notes carry 0 of 40 demanded facts (0/40), so recovery remains
mandatory and the model still has no signal from the note that recovery is
needed. A real-model probe (deepseek/deepseek-v4-flash-0731) shows a capable
model CAN recover when explicitly asked (2/2 scenarios, byte-exact payload
confirmed) — but that is a prompted, cooperative setting, not uncontrolled
timing. Verdict: **A-STAYS-PARKED** — the surface itself is sound, but the
reasoning gap persists unchanged at every surface, and recovery timing remains
unproven in uncontrolled use. Nothing public.

## [Analysis Brief]

Domain: complex (runtime-emergent behavior dependent on execution) — run a
bounded probe, no predictive certainty. Evidence base (first-hand, verified by
run): in-scratch A-harness `/root/.hermes/cache/scratch/atest_harness.py`,
results `/root/.hermes/cache/scratch/atest_results.json`, real-model probe
`/tmp/scratchpad/realmodel_probe_results.json`. Compared against B-test
receipts (`/root/workspace/drop/deepdive-mission-flow/B-TEST-RECOVERY-20261101.md`,
`/root/.hermes/cache/scratch/btest_results.json`).

Assumptions: token count approximated at 4 chars/token (consistent with B);
cost uses a single flat rate ($3e-6/token); completion tokens proxied by
baseline + per-recovery reasoning cost (debug 100, app-dev 400, long-horizon
200) exactly as in B, so ratios are comparable. The A-harness is an independent
reimplementation of the tool boundary (JSON serialization, prompt transport,
conversation reconstruction) over an independent archive store; it does NOT
import btest_harness. The "model" in probes 1-3 is scripted (demand issued
deterministically); probe 3b adds a real-model (deepseek) check.

Uncertainty: no claim that the real-model probe represents uncontrolled use;
it is a prompted, cooperative setting. The 0/40 reasoning gap is a property of
the notes, not the interface, and holds by construction.

## [1] The in-scratch A-harness

Path: `/root/.hermes/cache/scratch/atest_harness.py` (Python 3.13, seed 20261101).

Implements the model-facing surface independently:
- `ASession`: conversation messages (protected + tool results) + independent
  `AStore` (byte-exact payload storage with SHA-256, stable refs `arc-NNNN`).
- `tool_context_apply(args_json)`: parses JSON tool-call args, validates the
  whole batch atomically (unknown / duplicate / already-archived / unavailable /
  malformed JSON reject with no partial mutation), stores originals, replaces
  bodies with stubs carrying note + archive ref. Returns a JSON tool result.
- `tool_context_recover(args_json)`: parses JSON, retrieves by ref, returns the
  original payload as a NEW result at the end of the conversation with a fresh
  id; does not rerun the tool. Payload passes through `json.dumps`/`json.loads`
  to probe serialization loss; `serialization_ok` is recorded.
- `active_context_text()` / `byte_exact_recovered_in_conversation()`: reconstruct
  the conversation as the model sees it (tool results carry JSON with a payload
  field) and verify the recovered payload is byte-exact inside that view.

Protected messages: user/system/assistant are added via `add_message` only; there
is no code path that archives them (by construction, and the tool accepts only
result ids, which never map to a protected message).

## [2] Probe 1 — Model-facing recovery (byte-exact at the exposed interface)

Same demanded-recovery scenarios as B, run through the tool boundary.

| workload | n_results | archived | demanded | recovery byte-exact | conv-recovered byte-exact | serialization failures |
|---|---:|---:|---:|---:|---:|---:|
| noisy_debug | 40 | 32 | 5 | 5/5 (100%) | 5/5 | 0 |
| app_dev | 8 | 5 | 3 | 3/3 (100%) | 3/3 | 0 |
| long_horizon | 60 | 48 | 12 | 12/12 (100%) | 12/12 | 0 |
| adequacy_probe | 20 | 20 | 20 | 20/20 (100%) | 20/20 | 0 |
| **total** | **128** | **105** | **40** | **40/40 (100%)** | **40/40** | **0** |

Atomicity: a batch containing one unknown id (`r9999`) was rejected in full
(ok=false) with no partial mutation — the already-archived result stayed
archived, no entry added. Verified. Double-apply on an archived anchor rejected.
Unknown ref rejected. Malformed JSON rejected. All failure modes reject with
no partial mutation.

Conclusion: the exposed interface does NOT introduce its own loss. The
storage-level byte-exact guarantee (B) survives the tool boundary, the JSON
serialization, and the prompt transport (conversation reconstruction). 0/40
serialization failures; 40/40 conv-recovered byte-exact.

## [3] Probe 2 — Misuse surface

Controlled misuse scenario (noisy-debug, aggressive archival of all 10 results
including 2 live anchors that are still needed, plus missed recovery and
malformed/mis-targeted calls):

| metric | value |
|---|---:|
| live anchors wrongly archived | 2 |
| recoveries demanded-but-not-issued (missed) | 1 |
| double-apply rejected (atomic) | yes |
| unknown-id apply rejected | yes |
| unknown-ref recover rejected | yes |
| misuse events recorded | 3 |
| blast: recoveries needed to repair | 2 |
| blast: completion tokens | 200 |

Adequacy-probe failure-mode checks: double_apply_rejected=true,
unknown_ref_rejected=true, malformed_rejected=true, atomicity_held=true,
atomicity_no_partial_mutation=true.

Misuse cost is bounded: every misfire is rejected at the boundary with no
partial mutation, and the only blast is the recovery work to pull back what
was over-archived (2 recoveries / 200 completion tokens in the controlled case).
The dangerous misuse — a live anchor archived and never recovered — is
possible (missed_recovery_count=1) and is the unbounded-in-principle case; it
is exactly the reasoning-gap seam (the note gives no signal that recovery is
needed).

## [4] Probe 3 — Adequacy through the model's eyes

Notes sufficient for the demanded fact: 0/20 in the adequacy probe (20 noisy-
debug results archived with short notes; each demanded `SECRET-DBG-...` token
deliberately absent from the note). Reasoning gap: 20/20 (100%). Across all
workloads: 5 + 3 + 12 + 20 = 40 demanded facts, 0 present in any note. The
interface's exposure does not change this: the notes are identical in content
to B's, and the tool boundary neither adds nor removes facts. The reasoning gap
holds at every surface.

Probe 3b — real-model check (deepseek/deepseek-v4-flash-0731, prompted,
cooperative, 2 scenarios requiring a demanded fact from an archived result):
- Scenario 1 ("exact DEBUG_MARKER in r0001"): model invoked context_recover and
  answered with the exact fact (SECRET-DBG-000-2491); recovered payload
  byte-exact. PASS.
- Scenario 2 ("which archived result contains a marker starting SECRET-DBG-000"):
  model invoked context_recover and answer contained the demanded fact. PASS.
Real-model probe receipt: `/tmp/scratchpad/realmodel_probe_results.json`.

Reading: a capable model CAN recover when explicitly asked, and gets the
byte-exact payload. But this is a prompted setting where the need is stated in
the question. In real use the model must infer the need from task context and
the lossy note gives no signal — that timing problem is unproven and is the
seam.

## [5] A-vs-B comparison table

| metric | B (internal harness) | A (model-facing surface) | delta |
|---|---|---|---|
| byte-exact demanded recoveries | 40/40 (100%) | 40/40 (100%) | 0 |
| serialization failures at interface | n/a (in-process) | 0/40 | new: none |
| conv-recovered byte-exact | n/a | 40/40 | new: all |
| noisy_debug prompt reduction | 75.1% | 75.1% | 0.0 |
| app_dev prompt reduction | 58.4% | 58.4% | 0.0 |
| long_horizon prompt reduction | 68.5% | 68.5% | 0.0 |
| noisy_debug total reduction | 70.2% | 70.2% | 0.0 |
| app_dev total reduction | 28.6% | 28.6% | 0.0 |
| long_horizon total reduction | 42.7% | 42.7% | 0.0 |
| noisy_debug completion ratio | 1.83x | 1.83x | 0.00 |
| app_dev completion ratio | 3.00x | 3.00x | 0.00 |
| long_horizon completion ratio | 5.00x | 5.00x | 0.00 |
| notes sufficient (adequacy) | 0/20 | 0/20 | 0 |
| reasoning gap | 20/20 | 20/20 | 0 |
| atomicity under bad batch | held (no partial) | held (no partial) | = |
| protected messages selectable | no (by construction) | no (by construction) | = |
| misuse cost bounded | n/a (no surface) | yes (3 rejected misfires, 2-recovery blast) | new |

The A-surface reproduces every B number to the digit. The interface does not
move any metric — neither the savings nor the gap.

## [6] Verdict

**A-STAYS-PARKED.**

The model-facing surface holds its own byte-exact guarantee under demand
(40/40) and the interface introduces no loss of its own (0 serialization
failures, 40/40 conv-recovered byte-exact, all failure modes reject cleanly
with no partial mutation). The misuse surface is bounded (misfires rejected
at the boundary; blast = recovery work, 2 recoveries / 200 tokens in the
controlled case). These two conditions for A-UNLOCKS are met.

However, the third named seam is present and unchanged: the reasoning gap
holds at every surface (0/40 notes sufficient). Exposing the tool does not
solve the core problem — the lossy note carries none of the demanded facts,
so recovery is mandatory, and the model has no signal from the note that
recovery is needed. The real-model probe shows recovery is feasible when
explicitly demanded, but uncontrolled timing (when, whether, and on which
archived result) remains unproven. Shipping now would push that untested
timing problem onto the model and, through it, onto the user — the same
reason B parked Shape A. The surface is sound; the reasoning is not ready.

Unlock condition (unchanged from B, now with surface evidence added): a
recovery-timing / note-adequacy mechanism that tells the model when a payload
is needed again, plus a recovery-demand task measured in uncontrolled use
(not only prompted). That is a reasoning-level addition, not a storage fix.
Shape B (internal harness mechanism) remains the home for archival.

## [7] Artifacts

- A-harness: `/root/.hermes/cache/scratch/atest_harness.py`
- A-results: `/root/.hermes/cache/scratch/atest_results.json`
- Real-model probe: `/tmp/scratchpad/realmodel_probe.py`,
  `/tmp/scratchpad/realmodel_probe_results.json`
- B-test (comparison ground): `/root/workspace/drop/deepdive-mission-flow/B-TEST-RECOVERY-20261101.md`,
  `/root/.hermes/cache/scratch/btest_harness.py`,
  `/root/.hermes/cache/scratch/btest_results.json`
- This artifact: `/root/workspace/drop/deepdive-mission-flow/A-TEST-INDEPENDENT-20261101.md`
- Status: landed (local only; nothing public). Contract honored: no public write.

## [8] Disk

```
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/pve-root   70G   61G  5.9G  92% /
```
EOF