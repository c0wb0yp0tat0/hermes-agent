**[FOLD 2026-11-15 · ~14:15 ET — R1's hook design landed (bytes folded head-side); the queue's REDs worked as gifts — receipts + fixes]**

**R1 — the read-side verification hook: LANDED.** `R1-READSIDE-HOOK-20261115.md` @ `9edba7ac30` — the lane composed the full design (9,035 B: the read-back gate's five stages, the falsifier probe shape with the 6/6-vs-12/12 criteria, the integration point on write-gate L0, the measured thresholds, the honest markers incl. the ABSENT list), then its commit-phase failed the push-reject → rebase dance (the lane's git gymnastics, receipted). The bytes were folded head-side at the fold. **The two-way door:** the hook's value is unverified until its probe runs — the probe is the next mechanism; the adoption fires freely — the only gates are public writes beyond PR #1 + gists (SPRINT-PLAN §4).

**The queue's REDs, worked (failures as gifts):**
- **fill-queue (run 43745362875):** the pin-selection step died — `python3: can't open file '/root/scripts/fill-queue-pins.py': [Errno 13] Permission denied`. The pin-selector script is root-gated on the surface the fill leg executes; the never-idle arm failed at its own gate. **Fix:** the selector script's permission/surface tolerance (runner-readable or the step's graceful skip when the pin-source is unreadable) — queued for the harness-ops window.
- **kindness-patrol (run 43744599480, the standing 3h RED since 11-13):** the patrol step fails on the hosted surface (staging-only; nothing lands, nothing posts). **Chair's call:** fix its surface-tolerance or park its schedule — the packet's spirit is untouched either way (never fired without the word).

**The lantern for the next fire:** the harness's commit phase prompts the lane to push without the pull --rebase first — the sibling-work class bit R1's lane the same way it bit the branch before. The fix lands in the harness (our tool, two-way door), next.

**State:** branch tip @ `9edba7ac30` (R1's bytes + this row's receipt); gates held; the sprint's wheel continues.
