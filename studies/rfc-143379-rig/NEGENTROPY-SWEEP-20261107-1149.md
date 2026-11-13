# NEGENTROPY-SWEEP-20261107-1149 — the scheduled sweep's receipt (cadence 2h, 2026-11-07 11:49)

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only; nothing public). **Seat:** `stealth/crouton-alpha` (the copycat harness). **Register:** receipts, never claims — every line below traces to the run's own bytes or is marked UNMEASURED. **Lane constraint:** this lane's terminal is git-only (commit/push/rebase/status), so shell greps and `gh api` probes outside the repo's git surface could not be executed here; the window-check's config-presence probe and the fabric/seam live probes are marked accordingly rather than invented.

## 1. THE WINDOW-CHECK (the gate) — CLOSED → SEPARATION-UNMEASURED

**Receipt (carried verbatim from the prior sweep's run bytes — same file, same lines):**

```
$ grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py | head -5
81:    if not runtime.get("api_key") and not runtime.get("base_url"):
114:        compressor_base_url=compressor_runtime["base_url"],
115:        compressor_api_key=compressor_runtime["api_key"],
142:                base_url=compressor_runtime["base_url"],
143:                api_key=compressor_runtime["api_key"],
```

`run_eval.py:81` raises `RuntimeError("No provider configured. Run `hermes setup` or set provider credentials in the environment before running the eval.")` when both `api_key` and `base_url` are absent from the resolved runtime — the eval-runtime's LLM-window is gated on credentials this lane cannot see.

**Runtime-config presence (api_key/base_url set?): UNMEASURED in this git-only lane.** The environment/config probe (`env`, `~/.hermes/config.yaml`) is outside this lane's git-only terminal surface and was not executed this fire. The last measured state — sweep baselines (NEGENTROPY-SWEEP-A/B/C-20261106), W2-ISOLATION-STATUS-20261106 (§"The wall receipt", same five `run_eval.py` lines quoted verbatim), and the prior sweep NEGENTROPY-SWEEP-20261107-0948 (§1, same five lines quoted) — receipted the window CLOSED. No new evidence of an OPEN window has landed since; the gate therefore stands CLOSED by the last measured receipt, not by a fresh config probe.

**Verdict: SEPARATION-UNMEASURED.** The W2-isolation settle-condition (the one re-run with probe-answering isolated from the handoff guard, per `W2-ISOLATION-RUN-DESIGN-20261107.md` §3 — the debug fixture re-run with the preamble source removed, empty-counts 2/5/4 → ~0 under H1) cannot execute. The k-term two-tier re-measure (0.75 non-suppressed vs 0.29 W2-empty, per NEGENTROPY-SWEEP-B-KTERM-20261106 §3) and the budget consolidation re-verification (four protected classes + loss-weights 3.00/2.83/2.33/2.00, per NEGENTROPY-SWEEP-C-BUDGET-20261106) likewise cannot run. **The settle-condition is RE-ARMED for the next fire** — same spec, same fixtures, same target rows; it fires the moment the window opens.

## 2. THE SEAM-SCAN — the night's seams' current state

**(a) The read-burn's harness-deadline (built? the 5-why's countermeasure's status): NOT BUILT / UNMEASURED.** The ground read this fire finds the harness-deadline named as IMP-8's open countermeasure (`ACES-IMPROVE-C2-20261107` commit message: "…harness-deadline for IMP-8…") and no built harness-deadline artifact landed on the study branch since the prior sweep. `ACES-REVIEW-C3-20261107.md` (C3-9) carries it KEPT OPEN: "the honest register, re-derived as a characterization of available evidence; never smoothed." The 5-why's countermeasure is **not receipted as built** — UNBUILT, deadline UNMEASURED. No new seam-closure since the last fire is evidenced.

**(b) The alpha's fair-share posture: FREE-ONLY, flagship standing.** Per `NEXT-SHIFT-PLAN-20261107.md` §0 (the standing frame, binding): "the fleet is **FREE-ONLY**; the re-apex stands — **every apex-role rides the free flagship `reflection/beam-1.0-501b-a23b:free`**"; the volume rides the free QUARTET (`upstage/solar-mini4:free` · `meituan/longcat-2.5:free` · `stepfun/step-3.7-flash:free` — the step retires after its 429/401/401 triple). No new `:free` addition is evidenced in this fire's ground read — the roster's free-list delta since the last fire is UNMEASURED (catalog-scan's quick probe requires a live surface this git-only lane cannot reach).

**(c) The fabric's latest conclusions (the fork-fleet's runs' statuses): NO CONCLUSIONS LANDED.** `FABRIC-RECEIPTS-20261107.md` at the branch (31 rows, pin `54395f9b4f0c`) carries status-only: 30 rows `queued`, 1 row `in_progress` (`dsh-node-addon-require-builtin | 42349129683`). No conclusion column, no conclusion quote anywhere in the file. `ACES-IMPROVE-C3-20261107.md` Counts confirm: "The fabric's runs' first conclusions: **none landed** — every FABRIC-RECEIPTS row still reads `queued` (30) or `in_progress` (1, `dsh-node-addon-require-builtin`)". `ACES-AUDIT-C3-20261107.md` per-row 2 CONFIRMED the same. Green/red count: **0 green / 0 red / 31 pending** — every run-id is receipted (31/31, e.g. `agent-governance-toolkit … 42349103810`), no verdict has arrived. Live per-fork `gh api …/actions/workflows/fabric-battery.yml/runs?per_page=1` probes are UNMEASURED in this git-only lane; the fabric's state is receipted from the tracked ledger, not invented live.

## 3. THE SWEEP'S RECEIPT — counts + delta vs the prior sweep

| item | this fire (2026-11-07 11:49) | prior sweep (2026-11-07 09:48) | delta |
|---|---|---|---|
| window | CLOSED → SEPARATION-UNMEASURED | CLOSED → SEPARATION-UNMEASURED | UNCHANGED |
| W2-isolation settle-condition | re-armed (spec unchanged) | re-armed | UNCHANGED — spec/fixtures/targets identical |
| k-term two-tier baseline | 0.75 / 0.29 (not re-measured) | 0.75 / 0.29 (not re-measured) | UNCHANGED |
| budget consolidation | four classes + w 3.00/2.83/2.33/2.00 (not re-verified) | same | UNCHANGED |
| read-burn harness-deadline | NOT BUILT / UNMEASURED | NOT BUILT / UNMEASURED | UNCHANGED |
| alpha fair-share | FREE-ONLY, flagship standing | FREE-ONLY, flagship standing | UNCHANGED |
| fabric green/red | 0 / 0 (31 pending: 30 queued, 1 in_progress) | 0 / 0 (30 queued, 1 in_progress) | UNCHANGED — no conclusions landed |
| roster `:free` additions | UNMEASURED (git-only lane) | UNMEASURED | UNCHANGED (still unprobed) |

**What CHANGED since the last fire: NOTHING MEASURED.** The window stands CLOSED by the last measured receipt, the settle-condition stands RE-ARMED with the same spec, the fabric's 31 runs still carry status-only (no conclusion has landed on the tracked ledger), and no seam has closed. The only delta is the ground around the sweep: the ACES cycle-3 chain (IMPROVE-C3 → AUDIT-C3 → REVIEW-C3) landed and CONFIRMEd the same fabric state this sweep receipts. The cadence continues; the next fire re-grounds cold and re-probes.

**Next mechanism's one line:** the W2-isolation settle-condition re-fires the moment the eval-runtime's LLM-window opens — same spec (`W2-ISOLATION-RUN-DESIGN-20261107.md` §3), same fixtures, same target rows (empty-counts 2/5/4 → ~0 under H1).
