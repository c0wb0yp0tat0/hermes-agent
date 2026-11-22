# INDEPENDENCE-LAYER-20261122 — ARM 4: the independence layer (base-pin fix + blind-panel protocol + distinct-bases gate)

*Lane: independence layer (FINAL-LEG-PLAN arm 4). Seat: tencent/hy4-flash:free. Branch: study/rfc-143379-rig-20261105. RFC #143379 upstream QUIET · nothing public beyond PR #1's thread · no installs · write ONLY under `studies/rfc-143379-rig/` (the config edit is this arm's own one-line execution, restored) · the PLAN is not altered · never push · no checkout -- / rm -rf / stash.*

*Ground read IN FULL, in the brief's order: BRIEF-INDEPENDENCE-LAYER-20261122.md (contract) → FINAL-LEG-PLAN-20261121.md arm 4 → aoa-audits-20261121.md §0 shared-route constraint + §7 settle-5 → /root/.hermes/config.yaml delegation block (READ-ONLY) → skills think-tank (spine, per-lane-base SOP) + blind-agent-panels (panel pattern) + agent-work-review + investigation-documentation → MEMORY.md + USER.md (anchor). Rest named-and-refused; no other armament loaded. A non-reproduction is a QUESTION with receipts, never a guess (wall clause).*

---

## 1 · THE BASE-PIN FIX — one configuration line

### The constraint being closed (AoA §0, on the record)
The three cross-audit lanes rode **one** pinned base — `upstage/solar-mini4:free` — because Hermes's `delegation.model` is a **single global pin** and `delegate_task` children inherit the parent's current pin. The fan-out left the same pin standing across all spawns → **same-base corroboration, not independent verification**. AoA §0 named it; settle-5 requires a distinct-bases run + a blind panel before any "verification independent" claim.

### The exact patch (one line)
The fix closes the constraint **by construction**: re-write the single pin line before every verification spawn, to a base id distinct from the immediately preceding spawn's base. Children inherit the parent's current pin, so two consecutive spawns pinned to different ids cannot share a base.

```diff
  delegation:
-   model: tencent/hy4-flash:free          # pre-fire value (single standing pin)
+   model: meituan/longcat-2.5:free        # spawn-1 pin   (adjacent base #1)
+   model: tencent/hy4-flash:free          # spawn-2 pin   (adjacent base #2 — differs from #1)
```
- **The line:** `delegation.model:` — the value line `  model: <base-id>` inside the `delegation:` block.
- **Placement:** `/root/.hermes/config.yaml`, `delegation:` block, the `model:` key. Line **73** in the current serialization (line **78** in the pre-fire serialization first read this task — see OPEN-1 for the serialization seam).
- **Mechanism:** the pin is global and inherited at spawn time. The dispatcher's rule — *re-pin this one line, then dispatch, before each spawn* — makes adjacent bases distinct deterministically, never by coincidence. This is the think-tank SOP's per-lane-base rule ("a fan-out that does not pin per-lane bases is a single-model echo"; "the repair is `hermes config set delegation.model <live-base>`") applied as a one-line re-pin.
- **Rollback:** restore the line to `  model: tencent/hy4-flash:free` (the pre-fire value). Verified byte-identical: `config_start_sha256 4d9a4f8a8410b3cc8fe1b4288fb9fd78f7d875828af8cffc8baa7d14a3f8c72e == config_end_sha256 4d9a4f8a8410b3cc8fe1b4288fb9fd78f7d875828af8cffc8baa7d14a3f8c72e`; `line_deltas_vs_launcher_start = []`; `hermes config get delegation.model = tencent/hy4-flash:free`.

### Disconfirmation before landing (Are Right A Lot)
A positive-token base-health probe ran **before every dispatch** (think-tank SOP: never skip):

| Base | Probe `Reply with exactly: OK` | Verdict |
|---|---|---|
| `tencent/hy4-flash:free` | rc=0, OK token present, 6s | LIVE — selected (spawn 2) |
| `meituan/longcat-2.5:free` | rc=0, OK token present, 6s | LIVE — selected (spawn 1) |
| `upstage/solar-mini4:free` | rc=0, OK token present, 3s | LIVE — **excluded**: it is the compose/audit base (lane-C §2) |
| `stepfun/step-3.7-flash:free` | probe OK (6s) but the real spawn timed out rc=124 ×2 | DARK under load — named, not used (OPEN-3) |
| `reflection/beam-1.0-501b-a23b:free` | rc=1, no OK token, 10s | DARK — named, not used |

Two probe-live bases, both different from each other and from the compose base, were chosen — the pin was disconfirmed before it landed.

### The applied receipt (config edit at the fire)
Each edit changed **exactly one line** (line 73), verified by sha and `hermes config get`:

| Step | Action | changed line | config sha before → after | `config get` | ok |
|---|---|---|---|---|---|
| edit 1 | `delegation.model -> meituan/longcat-2.5:free` | 73 only | `4d9a4f8a…` → `1a06e517…` | `meituan/longcat-2.5:free` | true |
| edit 2 | `delegation.model -> tencent/hy4-flash:free` | 73 only | `1a06e517…` → `4d9a4f8a…` | `tencent/hy4-flash:free` | true |
| rollback | `delegation.model -> tencent/hy4-flash:free` | none (already original) | `4d9a4f8a…` → `4d9a4f8a…` | `tencent/hy4-flash:free` | true |

At 13:04:05Z / 13:04:21Z / 13:04:30Z, 2026-11-22. The config is back at its pre-fire value; the fix's mechanism (per-spawn re-pin) is the durable design, the edit was transient and reversed on demand.

---

## 2 · THE BLIND-PANEL PROTOCOL — mechanized, ready to arm

Applied to the pilot's landing-verification — the rung-1 receipt's verification panel (`canary-rung1-receipt-20261122.md`, `receipt_sha256 47013dc29a431bcb02a2c8b111fd2d0ae600e19c8861c810fcc58faacf9e673c`). From `blind-agent-panels` + lane-C §3/C1–C9 + the receipt skeleton:

1. **When.** Every pilot-kit landing carrying a numeric claim — the canary receipt, the weights-rung fire, GAP-3's 300+ battery, GAP-4's release-condition battery — gets a blind panel **before** its landing is composed into a verdict.
2. **Who.** 2–3 blind subagents, dispatched in parallel from the **fixed** free pool; each child a distinct ID, no two children of one dispatch share an ID; pool re-inventoried **once per shift**, not per dispatch. Armable pool today (probe-live): `meituan/longcat-2.5:free`, `tencent/hy4-flash:free` (the gate proved these two distinct); `upstage/solar-mini4:free` is excluded as the compose base; `stepfun` / `beam` are named-dark.
3. **Blindness (non-negotiable).** The brief carries the **artifact path + the questions only** — never the artifact's content; a brief that leaks the answer's shape is void. Each worker reads the rig's chain files with `read_file` first (pve-1 local disk, not cloud-reachable), then runs its own research (discovery → reading → retry-once-then-fallback → stop at CAPTCHA/2FA). No separate supervisor-side research lane.
4. **Deliverable.** Each worker writes a distinct per-worker file **and** returns markdown: verdicts `FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND / GUESSED-WRONG` per claim, with tool-call counts + evidence paths. The parent re-reads every written deliverable and re-derives the load-bearing numbers from disk before composing the landing. A worker returning `{}` while its artifact exists is a **landing failure** (self-report miss), not a missing artifact.
5. **Reconciliation — the mediator's job (named).** Convergences weighted; divergences treated as **signal, never averaged**. A `FOUND-PARTIAL` on one claim from two panels is a named seam — the landing stays un-composed until the seam is closed or explicitly carried. Nothing is reconciled away by majority.

**Application to rung-1.** The panel's independent verdict row (lane-C §1's fifth receipt field) reads the rung-1 receipt's load-bearing claims blind: the per-key two-sha rule (§I.2), the LIVE floor determinism content-sha `03f113ca…` (§II.2 L8–L10), the byte-verified rollback `1b63e694…` (§II.4), and the PARTIALLY-COVERED overall verdict (§I.6). No "verified"/"independent" claim rides until the panel lands — G2/G3/G4 stay carried as open until then. The mediator composes the per-worker rows into the evaluator's independent verdict row; the operator's read remains C3's human anchor.

**One-line shape:** *2–3 blind workers, path+questions-only briefs on distinct pinned bases → per-worker `FOUND-EXACT/PARTIAL/NOT-FOUND/GUESSED-WRONG` verdicts with evidence → a named mediator weights convergences and carries divergences as seams, nothing averaged.*

---

## 3 · THE GATE — a verification run whose bases are DISTINCT

**Verdict: PASS.** Two consecutive verification spawns, re-pinned between them, on two different bases; their manifests' models differ.

| # | `pinned_base` (manifest model) | session id | `delegation_model_at_spawn` | attestation | rc | time (UTC) |
|---|---|---|---|---|---|---|
| spawn-1 | `meituan/longcat-2.5:free` | `local-d6ec0b42d2e300b93368cd845723fcfdefd3df4081d077a7faa28f2475ef78c7` | `meituan/longcat-2.5:free` | `VERIFIED` | 0 | 13:04:20Z |
| spawn-2 | `tencent/hy4-flash:free` | `local-09c4165615b7fdcf8cd7227a58aa59f118c191439504070b7ecd6993f8e42d85` | `tencent/hy4-flash:free` | `VERIFIED` | 0 | 13:04:29Z |

- **Distinct bases:** `['meituan/longcat-2.5:free', 'tencent/hy4-flash:free']` → `distinct = true`; `both_differ_from_compose_base_solar_mini4 = true`.
- Each spawn used a blind brief (artifact path + mission, no content) and a one-token seat-attestation dispatch (`hermes chat -q 'Reply with exactly: VERIFIED' -m '<base>' --oneshot`); the manifest is authoritative for the pinned base (it records the exact `--model` flag and the re-pinned `delegation.model` at spawn). Manifest files: `/root/.hermes/cache/scratch/ind-manifest-spawn-{1,2}.json`; raw dispatch stdout + sha in the manifests; full run receipt `/root/.hermes/cache/scratch/ind-fire-receipt.json`.
- **Consecutive:** spawn-2 was pinned and dispatched only after spawn-1 returned; the re-pin between them is the fix executing (config edits 1→2 above).
- **Rollback after the run:** config restored to `tencent/hy4-flash:free`, sha start == end, zero line deltas.
- **Scope of this gate (named):** it proves the **distinct-bases run** (settle-5's first clause). It does **not** itself claim "verification independent" — the substantive blind panel on rung-1 and stage-3 per-unit pins are still to land (OPEN-2/OPEN-5). Same-base convergence is never claimed as independence.

---

## 4 · OPEN ITEMS (wall clause — every non-reproduction / seam kept with receipts, none smoothed)

| # | Item | Disposition | Receipt |
|---|---|---|---|
| OPEN-1 | Config YAML **reserialization** seam | KEPT — named, not smoothed | An aborted first launcher used `hermes config set`, which reserialized the YAML (folded personality scalars unfolded; 6410 B / 306 lines → 6499 B / 301 lines; all 38 top-level keys and every value preserved). Every subsequent ARM-4 edit was byte-precise one-line with sha-preserving rollback. The config is semantically identical to the pre-task original with `delegation.model` restored; **byte-identity to the pre-task file is not claimed.** |
| OPEN-2 | Gate spawns are **one-token seat attestations**, not full `FOUND-*` verdict panels | KEPT — named seam | The gate's purpose is base distinctness (proved). The full blind-panel protocol with substantive verdicts on rung-1 is documented §2, ready to arm; first substantive panel still to land (CA#4 / settle-5). |
| OPEN-3 | Seat availability volatility | KEPT | `stepfun/step-3.7-flash:free`: OK-probe passed (6s) but the real spawn timed out rc=124 twice; `reflection/beam-1.0-501b-a23b:free` rc=1 (dark). Pool re-inventory once per shift per the skill; both named, never retried into a false pass. |
| OPEN-4 | Board-spawn path vs delegation route | KEPT | lane-C O5: the board-spawn repair is one config line; the delegation route's **per-unit** pinning needs a second line. This arm closed the delegation route's standing single pin (the audits' shared base); the per-unit second line remains named. |
| OPEN-5 | Independence claim | KEPT — constraint stays named | AoA §0 / settle-5: no "verification independent" claim until stage-3 per-unit pins + this gate + a substantive blind panel on a first numeric landing all close. This gate closes the distinct-bases run only. |
| OPEN-6 | Doors | named, waiting, OUTSIDE scope | Court posting / RFC #143379 upstream / autopilot pilot gate — GATE LAW (MEMORY:19). RFC QUIET; nothing public beyond PR #1's thread. |

---

## 5 · HARD LINES · EMISSION · TERMINATION

- **Hard lines ✓:** nothing public · RFC #143379 upstream QUIET · no installs · local paths via `read_file` only, never `web_extract` · writes only under `studies/rfc-143379-rig/` (plus this arm's own one-line config edit, restored) · no push · no `git checkout --` / `git rm -rf` / `git stash` · commit as kanban-pilot.
- **Emission ✓:** this file at `studies/rfc-143379-rig/INDEPENDENCE-LAYER-20261122.md` carries the exact patch + applied receipt (§1), the blind-panel protocol (§2), the gate's distinct-bases receipts (§3), and the open items (§4); committed, sha reported.
- **Termination ✓:** one review round (falsifier pass: seat disconfirmation before pinning, byte-level rollback check, distinct-manifest check, scope limit named). No further measurable change available on the same bytes → **PARK the improvement loop with the record**, report, stop.
- **LP compact:** Customer Obsession (independence serves the pilot verification's credibility) · Ownership (the seam is this lane's until the receipt lands) · Invent and Simplify (one line, one panel) · Are Right A Lot (the pin was disconfirmed — stepfun/beam named dark — before landing) · Bias for Action · Dive Deep (the config's current shape was read, not assumed; the one-line diff was sha-verified) · Deliver Results (this file + the commit + the sha).

*Facimus semper — the gate renders on the bytes; the bytes are on the record; the record corrects itself out loud. A non-reproduction is a QUESTION with receipts, never a defect, never a silent pass. — kanban-pilot*
