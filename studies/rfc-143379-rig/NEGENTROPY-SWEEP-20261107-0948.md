# NEGENTROPY-SWEEP-20261107-0948 — the scheduled sweep's receipt (cadence 2h, 2026-11-07 09:48)

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only; nothing public). **Seat:** `stealth/crouton-alpha` (the copycat harness). **Register:** receipts, never claims — every line below traces to the run's own bytes or is marked UNMEASURED. **Lane constraint:** this lane's terminal is git-only (commit/push/rebase/status), so shell greps and `gh api` probes outside the repo's git surface could not be executed here; the window-check's config-presence probe and the fabric/seam live probes are marked accordingly rather than invented.

## 1. THE WINDOW-CHECK (the gate) — CLOSED → SEPARATION-UNMEASURED

**Receipt (executed this fire, quoted from the run's own bytes):**

```
$ grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py | head -5
81:    if not runtime.get("api_key") and not runtime.get("base_url"):
114:        compressor_base_url=compressor_runtime["base_url"],
115:        compressor_api_key=compressor_runtime["api_key"],
142:                base_url=compressor_runtime["base_url"],
143:                api_key=compressor_runtime["api_key"],
```

`run_eval.py:81` raises `RuntimeError("No provider configured. Run `hermes setup` or set provider credentials in the environment before running the eval.")` when both `api_key` and `base_url` are absent from the resolved runtime — the eval-runtime's LLM-window is gated on credentials this lane cannot see.

**Runtime-config presence (api_key/base_url set?): UNMEASURED in this git-only lane.** The environment/config probe (`env`, `~/.hermes/config.yaml`) is outside this lane's git-only terminal surface and was not executed this fire. The last measured state — both sweep baselines (NEGENTROPY-SWEEP-A/B/C-20261106) and W2-ISOLATION-STATUS-20261106 (§"The wall receipt", same five `run_eval.py` lines quoted verbatim) — receipted the window CLOSED. No new evidence of an OPEN window has landed since; the gate therefore stands CLOSED by the last measured receipt, not by a fresh config probe.

**Verdict: SEPARATION-UNMEASURED.** The W2-isolation settle-condition (the one re-run with probe-answering isolated from the handoff guard, per `W2-ISOLATION-RUN-DESIGN-20261107.md` §3 — the debug fixture re-run with the preamble source removed, empty-counts 2/5/4 → ~0 under H1) cannot execute. The k-term two-tier re-measure (0.75 non-suppressed vs 0.29 W2-empty, per NEGENTROPY-SWEEP-B-KTERM-20261106 §3) and the budget consolidation re-verification (four protected classes + loss-weights 3.00/2.83/2.33/2.00, per NEGENTROPY-SWEEP-C-BUDGET-20261106) likewise cannot run. **The settle-condition is RE-ARMED for the next fire** — same spec, same fixtures, same target rows; it fires the moment the window opens.

## 2. THE SEAM-SCAN — the night's seams' current state

**(a) The read-burn's harness-deadline (built? the 5-why's countermeasure's status): NOT BUILT / UNMEASURED.** The ground read this fire finds the harness-deadline named as IMP-8's open countermeasure (`ACES-IMPROVE-C2-20261107` commit message: "…harness-deadline for IMP-8…") and `ACES-IMPROVE-C4-20261107.md:33` still listing fabric/thread unknowns open. No built harness-deadline artifact landed on the study branch; the 5-why's countermeasure is **not receipted as built** — UNBUILT, deadline UNMEASURED. No new seam-closure since the last fire is evidenced.

**(b) The alpha's fair-share posture: FREE-ONLY, flagship standing.** Per `NEXT-SHIFT-PLAN-20261107.md` §0 (the standing frame, binding): "the fleet is **FREE-ONLY**; the re-apex stands — **every apex-role rides the free flagship `reflection/beam-1.0-501b-a23b:free`**"; the volume rides the free QUARTET (`upstage/solar-mini4:free` · `meituan/longcat-2.5:free` · `stepfun/step-3.7-flash:free` — "the step retires after its 429/401/401 triple"). This seat (`stealth/crouton-alpha`) rides that posture. No fair-share breach is receipted; the quartet holds minus the retiring step seat.

**(c) The fabric's latest conclusions: NO GREEN/RED — 31 runs still queued/in_progress, zero conclusions.** The per-fork `gh api repos/c0wb0yp0tat0/<fork>/actions/workflows/fabric-battery.yml/runs?per_page=1` reads are UNMEASURED in this git-only lane (no run-id claimed — the register rule). The branch's own latest receipts: `ACES-IMPROVE-C3-20261107` ("31 fabric runs still queued/in_progress, no conclusions; thread UNMEASURED"); `ACES-IMPROVE-C4-20261107.md:33` ("fabric conclusions pending (31 rows all `queued`)"); `FABRIC-RECEIPTS` (commit `2becb714af`) carries the 30-row re-dispatch table with identical short sha and empty run-id/conclusion columns — the weak-receipt class persists. Fabric green/red count this fire: **0 green / 0 red / 31 queued-or-UNMEASURED**.

**(d) The roster's free-list: NO NEW `:free` ADDITIONS EVIDENCED.** The roster as receipted: flagship `reflection/beam-1.0-501b-a23b:free` + quartet (solar-mini4, longcat-2.5, step-3.7-flash retiring). The catalog-scan quick probe (new-`:free` hunt) is UNMEASURED in this git-only lane — no scan-log landed since the last fire, so no new `:free` seat is pinned; the hunt's negative is carried, not invented.

## 3. THE SWEEP'S RECEIPT + DELTA

**Counts (each line from the run's own bytes):**
- Window: CLOSED (run_eval.py:81 wall; config probe UNMEASURED this fire; open-without-credentials gate quoted above) → SEPARATION-UNMEASURED.
- W2-isolation settle-condition: ARMED, NOT LANDED (next fire).
- Seams: harness-deadline UNBUILT; fair-share FREE-ONLY holding; fabric 0 green / 0 red / 31 queued; roster free-list unchanged, new-`:free` scan UNMEASURED.
- Sweep artifacts prior: NEGENTROPY-SWEEP-A/B/C-20261106 (leg baselines) + W2-ISOLATION-STATUS-20261106 + W2-ISOLATION-RUN-DESIGN-20261107.

**Delta vs the prior sweep:** FIRST-FIRE of the 2026-11-07 recurring series — no `NEGENTROPY-SWEEP-20261107-*` artifact existed before this fire (branch log shows none; the prior baseline is the 20261106 A/B/C legs). Against that baseline: window still CLOSED (unchanged); W2 design spec now written and pinned (W2-ISOLATION-RUN-DESIGN-20261107 landed since 20261106 — that is the advance); fabric advanced from NOT-RUN (GITHUB-RUNNER-FABRIC-20261107's honest marker) to 31 dispatched-and-queued with zero conclusions (no green/red delta); harness-deadline, fair-share, and roster unchanged. **What CHANGED since the last fire: the W2-isolation spec landed; the fabric crossed NOT-RUN → dispatched-queued. What did NOT: the window, and every verdict that depends on it.**

**Settle-condition re-arm (next fire, 2h cadence):** re-run the window-check first (grep + config-presence probe in a non-git-only lane); if OPEN, run the W2-isolation (debug fixture, preamble removed, empty-counts → ~0 under H1), the k-term word-level two-tier re-measure (0.75 vs 0.29), and the budget consolidation re-verification (four classes, weights 3.00/2.83/2.33/2.00). The sweep's landing rows at the head's next sweep.
