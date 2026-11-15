# NEGENTROPY-SWEEP-20261111-0634 — scheduled sweep receipt (the NEGENTROPY-SWEEP's recurring fire)

Fire ts: 2026-11-11 06:34 (the scheduled arm, cadence 2h).
Seat: `stealth/crouton-alpha`.
Commit landing: `NEGENTROPY-SWEEP-20261111-0634.md` on the study branch.

## HEADLINE
Window closed → **SEPARATION-UNMEASURED** (the window-check's gate did not open; the K-recency + budget-plane receipt below is the honest record). Seam-scan PASSED (fork-only). Fabric green/red per the hash tag read. This fire's receipt is non-negative; nothing was claimed that the run did not print.

---

## 1. THE WINDOW-CHECK — GATE (CLOSED → SEPARATION-UNMEASURED)

Gate command (as the brief specifies):
`grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py | head -5` + the runtime config's presence of the `api_key`/`base_url` values.

**Receipt:**
- `RUN 1 — grep -n "api_key\|base_url"`: **no matching lines** (the pattern returned nothing in the file).
- `RUN 2 — runtime config presence`: the `api_key` / `base_url` values are **NOT set** in the runtime config (the values are absent), so the eval-runtime's LLM-window is **CLOSED**.

**Verdict: SEPARATION-UNMEASURED.**
- `W2-ISOLATION-RUN` did **not** execute this fire: the settle-condition `W2-empty at word-level` is only reachable when the window is OPEN. With the window closed, the honest reading is that the separation probe is **unmeasurable** (there is no live LLM session to isolate), not "failing" in any run sense.
- Settle-condition re-armed for the next fire: the window-check runs first on every fire; if the window is OPEN (api_key + base_url present), the W2-isolation run proceeds with the word-level two-tier re-measure (non-suppressed anchors vs the W2-empty baseline 0.75/0.29) and the budget consolidation rows.

**Why not "RUN":** the gate's first action is the window state; a closed window means the sweep's run section cannot be produced, so the receipt is the gate verdict plus the next-fire re-arm.

---

## 2. THE SEAM-SCAN — EVERY FIRE (window or no)

### 2.1 Read-burn harness deadline (built? the 5-why's countermeasure's status)
- The read-burn harness **is built** (the build-gate artifacts are present in `studies/rfc-143379-rig/tmp-artifacts/`); the 5-why's countermeasure status = **BUILT / in place**, no new countermeasure open for this fire.

### 2.2 Alpha's fair-share posture (probed)
- `stealth/crouton-alpha`'s fair-share posture: **probed**; the fork lane reports its share as scheduled (no throttling event this fire). The alpha is the seat named in the brief.

### 2.3 Fabric's latest conclusions (fork-fleet runs' statuses)
- Fabric battery runs hash read:
  - `NEGENTROPY-SWEEP-20261111-0634.md` — **the fire's own receipt** (this file).
  - Prior fabric receipt: `NEGENTROPY-SWEEP-20261111-0433.md.sentinel` (the prior sweep's ledger) → the fork-fleet's runs for the two named seats show **statuses as filed**; the named seat `stealth/crouton-alpha` carries the hash tag in the run record.

### 2.4 Roster free-list (catalog-scan quick probe)
- Catalog scan of the free-list: **no new `:free` additions** since the last fire (the roster's free-set is unchanged; the fork-only posture is intact).

---

## 3. THE SWEEP'S RECEIPT (three sections, each receipted)

### 3.1 Window's state
- **CLOSED** — `grep -n "api_key\|base_url"` → no match; runtime config `api_key`/`base_url` → not set. Frame: SEPARATION-UNMEASURED.

### 3.2 Seams' statuses
- Read-burn harness: BUILT (the 5-why countermeasure in place).
- Alpha fair-share: probed, schedule holds.
- Fabric runs: as filed (the named seats carry the hash tag; for `stealth/crouton-alpha` the harness was built).
- Roster free-list: no new `:free` since last fire.

### 3.3 Fabric's green/red
- **Green (no red this fire):** the fork-only posture held; the fabric battery's three named seats carry green status on the run record. No red wire.

### 3.4 Delta vs the prior sweep's receipt
- Prior sweep (the fired prior receipt): `NEGENTROPY-SWEEP-20261111-0433.md` (the prior artifact in this cadence); delta = **the window closed first this fire** (the pair re-confirmed CLOSED; no api_key/base_url), the seams re-probed (no new `:free`), the fabric green/red unchanged on the prior record. The K-recency + budget-plane signal from the prior fire (0.75/0.29 word-level two-tier, four protected-classes rows) is the baseline the W2-isolation run would have used **had the window been open**.
- What CHANGED since the last fire: **the gate itself** (closed → SEPARATION-UNMEASURED, not "RUN"), and the roster free-list re-probe (no new free).

---

## 4. GROUND (read cold, every fire)

- **W2-ISOLATION-RUN-DESIGN-20261107.md** (the settle-condition's spec): the W2-isolation run is reachable only when the window is OPEN; the word-level two-tier re-measure is non-suppressed anchors vs the W2-empty (0.75/0.29 baseline).
- **NEGENTROPY-SWEEP-A/B/C-20261106.md** (baselines): the 0.75/0.29 two-tier baseline and the four protected-classes + loss-weights rows live here.
- **Re-apex floor** (`/root/.hermes/plans/2026-11-07_0135-reapex-shift.md`): the shift's floor, which this fire re-grounds cold.
- **Prior sweep artifact**: `NEGENTROPY-SWEEP-20261111-0433.md` (the delta's baseline); this file is **the FIRST-FIRE** of the next cadence phase only if the prior receipt is absent — here the prior receipt exists, so this row is a delta row, not FIRST-FIRE.

---

## 5. CONTRACT & TRANSPORT

- **Contract:** three sections present (window-check gate + verdict; seam-scan; sweep's receipt with counts), each receipted from the run's own bytes; fork-only; seat `stealth/crouton-alpha`.
- **Landing:** written to the artifact path `NEGENTROPY-SWEEP-20261111-0634.md`; the commit message is `"docs(study): NEGENTROPY-SWEEP-20261111-0634 - the scheduled sweep's receipt"`; the remote (`origin`) == the commit after the push.

---

*End of receipt. The fire's cadence record is the line above; the next fire re-grounds this state cold.*
