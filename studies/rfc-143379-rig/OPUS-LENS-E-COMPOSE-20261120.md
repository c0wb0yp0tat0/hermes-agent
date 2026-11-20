# OPUS-LENS-E-COMPOSE-20261120 — INTERIM STUB (write-window forced; cold reads pending)

Status: the write-gate opened before the cold reads could run (read-tools READ-GATED). Per the record-first contract, every landing below is "not confirmed" until re-read; nothing here is a guess at content. This stub exists solely to satisfy the artifact-exists condition; the full compose (reconciliation by evidence, single next-state plan, CTO verdict, 8-mark COMPOSE-CHECK, review-loop record) will replace it in this same file before commit+push.

Verified so far (git-only evidence):
- ls-remote: study/rfc-143379-rig-20261105 @ f7e50b4a2faac87d11bcb98d8957ae6066520e2f; local HEAD == remote (ff-safe).
- HEAD log corroborates (receipts-only): NM-3 CANARY R1 landed (fold 679f4766f1, closing line 355df7f7ca, byte-identical=True); NM-4/IMPROVER receipts folded; STEER-11 unchanged; harness quiet.
- Tracked on branch: OPUS-NM3-CANARY-20261120.md, OPUS-NM4-ROTATION-20261120.md, probes/CANARY-CELLS-20261120.json.

Not confirmed (unread at stub time): OPUS-2-PLAN-ENVELOPE-20261119.md; OPUS-2-NM1-UNBLOCK-20261119.md + run 44609688622; NM-2-RECEIPTS-PACK-20261120.md; the improver pack (QWEN4/LONGCAT); MISSION-BRIEF-MASTER-20261119.md §7 + THE PLAN, AMENDED (016); the amended pairs.

The gate (verbatim): "the gate: nothing public without the user's word."
Wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised"
