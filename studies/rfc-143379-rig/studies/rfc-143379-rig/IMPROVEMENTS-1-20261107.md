# IMPROVEMENTS-1-20261107 — Cycle-1 improver, max-value-add 8-hour shape

Improvements count: 5.

## (a) Track-level improvements (sharpen / merge / re-sequence / re-concentrate)

1. **Merge Track B (RFC-Material Staging) into Track D (Read-Gate Watch) as a single "Reads → Staging" fold.** Track B's staging is already the consumption of Track D's reads; running both as separate tracks doubles the reporting without doubling value. Concentrate the saved hours into Track A's verification depth.
2. **Re-sequence Track A (Kit Readiness) to be blocked on the read-restore #116673 merge trigger**, not started cold at 23:59:50. The plan's replan-trigger says pilot fires after merge; starting kit readiness before the trigger fires risks wasted rework if the merge lands mid-run. Re-concentrate Track A on the seam-close (R2) + W2 measurement only, deferring fabric-conclusions capture to a post-merge fold.
3. **Sharpen Track C (Machinery Standing): replace "audit 16 crons" breadth with a liveness-only check of the four operator-held gates' watches.** The 16-cron audit is low-marginal-value against the needs-set; gate-watch is the value-bearing half. Drop lane-discipline drift-check to a single fold-point row.
4. **Re-concentrate Track D into a reads-diff consumer, not a poller.** "Poll reads" is noise between fold-points; replace with a single diff-at-fold-point against the mission's layers. Silence-when-healthy already says so — make the mechanism match the doctrine.

## (b) Overlooked needs (what the inventory missed)

5. **Chunked/batched-write lane (MINES recurring signal).** The inventory's 5 needs never names the operator's recurring write-gate char-cap overruns (500/10000) — the single most recurring friction in host history. Add as need #6: a chunked-write helper lane, STAGED, low urgency but high frequency. This is a real need the inventory's "real immediate needs" framing dismissed as tooling.
6. **Gateway-restart pending (MINES anomaly).** Dashboard pid 1480227 serving pre-update code is an unhandled standing risk; the inventory does not list it. Add as need #7 or fold into Track C's gate-watch.
7. **ENOSPC/disk-full host-storage recovery.** Recurring lockdown history; the inventory omits host-storage entirely. Should be a Track C sub-item, not a dismissed theme.

## (c) Value-shape — the single highest-value concentration the current design misses

The current design spends 8 hours across four needs-of-equal-weight tracks. The highest-value concentration it misses: **the merge-composition gap** (RFC-READ honest gaps) — no PR tests the composed state of #116673 + #141876 + #139606, and xngg1021's four seam gaps are unverified in composition. The 8 hours buy the most value by concentrating ONE track on composing + falsifying that single composed state (the study's falsifier battery already covers some; the whole-anchor resolution is still RED). All other tracks should be subordinated to feeding that composition. This is the substrate-surface-amplifier order applied: substrate (composed read) first, surfaces (RFC material) second, amplifier (machinery) last.

## (d) Cycle-2 SWAP recommendation — next lens

Swap the improver seat to a lens that takes the **composition-gap concentration** as the new primary axis and re-derives the track set from "which track feeds the composed-state falsifier" rather than "which track serves which need." Specifically: a lens that (1) enumerates the four seam gaps (batch-path bypass, standalone fallback guards, preserve_session ignored return dicts, doc=/read fallback) as acceptance criteria, (2) maps each current track's hours to one of those four, (3) names the one track that must die to fund the composition track. Recommended next lens: an RFC-update-delta lens (the four lines' honest deltas) reframed as "what does the composed state require the RFC to say."
