# VALUE-ADD SYNTHESIS — 2026-11-07 (the fold lane)

## 1. Template elements ranked by evidence from the inventory

Ranked by how often/strongly the inventory shows the element actually produced value.

1. **Posture-diverse parallel legs** — produced: multi-voice catches single-pass misses. Backed by inventory #5 (blind 3-lane + audit-of-audit restart) and #8 (visible-path lanes). Strongest evidence of value.
2. **The fold contract** — produced: convergence verified, no drift. Backed by inventory #6 (single-writer fold) and #7 (re-verify against disk).
3. **Verification steps per task** — produced: byte-identity, md5 re-verify. Backed by inventory #4 (adversarial pre-commit gate) and #7.
4. **Landing-ledger discipline** — produced: no re-verification of verified files. Backed by inventory #7 (ledger vs disk).
5. **Replan-triggers clause** — produced: plan stays honest. Backed by inventory #5 (audit-of-audit restart on pull).
6. **Plan-on-entry** — produced: no plan-less fan-outs. Backed indirectly (#1-#8 all ran from plans).
7. **Bite-sized tracks with exact paths** — produced: scoped, auditable. Backed by #8 (visible-path dispatch).
8. **AC per phase** — produced: measurable done-state. Backed by #4 (gate fires).
9. **Risks / open questions named** — produced: named uncertainty. Backed weakly; theater-list shows named-but-unactivated items (fork doctrine).
10. **Dated amendment sections** — produced: audit trail. Backed by #7 (correction of ledger claims).
11. **Memory banking at fold time** — produced: durable knowledge. Backed by #7 (re-verification discipline).
12. **Hard-lines / quiet boundaries** — produced: scope discipline. Partially theater (fork doctrine never activated).

## 2. Generalizable core (keep/repeat)

- Self-fire checkpoint + handle verification — evidence C26-C32; why: converted claimed dispatch into verified handle.
- Price gate as machine-checked allowlist — evidence FIX-PRICE-GATE, WALLET-AFTERMATH; why: real money risk gated.
- Termination budget at dispatch — evidence FC-2/FC-8; why: catches hang pre-send.
- Adversarial pre-commit gate — evidence 002-lessons 09-19; why: gates that fire are working.
- Blind 3-lane + audit-of-audit restart — evidence ACES-RE-ORCHESTRATION; why: repeat-until-no-change.
- Single-writer fold + idempotent mirror — evidence bridge_sync #46; why: coherence by construction.
- Evidence re-verified against disk — evidence run2 55,032 vs 55,189; why: disk is reality.
- Visible-path dispatch (delegate_task) — evidence 002:43/46; why: tracked, steerable lanes at $0.

## 3. Kit-relevance (aspects the substrate pilot kit must carry)

- Machine-checked price gate (allowlist at every dispatch surface).
- Termination budget as dispatch precondition.
- Self-fire checkpoint + handle verification (JobID handle).
- Adversarial pre-commit gate in its slot.
- Blind 3-lane rotation + audit-of-audit restart.
- Single-writer fold + idempotent scripted mirror.
- Evidence re-verified against disk before ship.
- Visible-path dispatch (delegate_task, config-pinned models).

## 4. Honest counter (theater)

- Dark-horse local synthesis (LM Studio 9B) in tool-executing roles — 0 tool calls every run; value only via harness-side retrieval.
- Humanizer as default layer in dev briefs — scope bleed, corrupted grading.
- Repeated human correction as defect signal — gut-supported, weak evidence (+9.7–15pp).
- Launch-tests checking only exit code — exit 0 with all-error output false wins.
- Fork doctrine activation on C29 PARK — never activated.
- ACES record + landing ledger fold (C27-C32) — absent from both.
- Shared watchdog-task.md contention — starved urgent work.
- Skill descriptions over 60 chars — never registered.