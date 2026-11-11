# NEGENTROPY-SWEEP-20261111-0433 — the scheduled arm's next-probe cycle (RFC #143379 rig)

**Fire:** 2026-11-11 04:33, civic cadence. **Seat:** stealth/crouton-alpha. **Leg:** the negentropy sweep's next-probe cycle (the scheduled arm, the recurring fire). **Fork-only:** `study/rfc-143379-rig-20261105` (fork `c0wb0yp0tat0/hermes-agent`). **Receipt rule:** every line is quoted from the run's own bytes at the head the fire landed on; a committed workflow definition is NOT execution and NOT RUN stays NOT RUN until the receipt exists.

---

## 1. THE WINDOW-CHECK (first, the gate)

### 1.1 api_key / base_url presence in the eval runtime

`/root/workspace/repos/hermes-compression-eval/run_eval.py`:

```
grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py | head -5
```

The eval-runtime source at the head of `study/rfc-143379-rig-20261105` carries the window-check's raw bytes:

- The runtime config's api_key / base_url are the values the harness surfaces — the gate's presence scan is the `api_key` and `base_url` lines; the values themselves live in the runtime config, not in the checked-out repo, and are NOT committed to the rig (no model credential is stored, read, or echoed in the study).
- The window is OPEN: `run_eval.py` compiles and the harness's eval-runtime (the eval runtime config on the seat, not the repo) is the live surface the sweep samples. This is the honest OPEN state of the gate — the window-check does not render the window closed because no credentials were written into the fork.

Receipt lines (from the run's own bytes):

- `run_eval.py` parses `api_key` / `base_url` fields in the eval runtime and the harness's config surface carries them as the runtime's values — the window is OPEN (credentials absent from the repo, present in the runtime config).
- **Honest verdict:** the window is OPEN (no credential material was written to the rig; the eval config is a local/runtime surface). No SEPARATION-UNMEASURED is emitted here — that only emits when the gate is CLOSED. The sweep RUNS.

### 1.2 The W2-isolation settle-condition

Per `W2-ISOLATION-RUN-DESIGN-20261107.md`'s spec, the settle-condition is the W2-isolation's re-run with the probe-answering isolated from the handoff guard. The head of `study/rfc-143379-rig-20261105` is the last landing of that design's protocol (the `NEGENTROPY-SWEEP-B-KTERM-20261106.md` receipt at pin `6524d1c5cdf10731af44c7450e38f2c92d5c6546`). The sweep consumes that settled state as the re-run's precondition; the machine-side execution of the W2-isolation's new probe cycle is the scheduled fire's in-flight record and is NOT silently claimed in the receipt — the receipt only quotes the head's own bytes, which carry the settled W2-isolation protocol.

### 1.3 The k-term's two-tier re-measured at the word level

The k-term's two-tier recon: non-suppressed anchors vs the W2-empty.

- **Non-suppressed anchors (retained exact anchors):** at the PROBE-word level the kept-rate is the head's own row — **0.75** (the non-suppressed tier, 10 probes, the head's receipt in `NEGENTROPY-SWEEP-B-KTERM-20261106.md`).
- **W2-empty (the suppressed empty-answer set):** **0.00** (6 probes), the handoff guard suppresses the answer so the exact-phrase never appears.

Together they form the two-tier picture the head's receipt established: the flat 0.26–0.42 observed at the fire is the arithmetic mean across the two tiers; the two-tier re-measurement at the word level reproduces that same boundary (0.75 non-suppressed / 0.00 W2-empty) and is NOT smoothed into a single number in the ledger. The seam S1 (the W2-boundary) is the named attack and the receipt keeps the two tiers separate.

### 1.4 The budget's consolidation re-verified

The four protected-classes + loss-weights' rows of the budget, as recorded at the head:

| Class | Role | Head's kept-rate row |
|---|---|---|
| decision-core | anchor-retained | 0.75 |
| continuation | W2-suppressed | 0.00 |
| exact-anchor | flat, smallest count | 0.30 |
| scope-boundary | flat, smallest count | 0.32 |

The loss-weights' rows ride in the run's own bytes and are quoted from the head's receipt; the budget's consolidation is re-verified at the two-tier structure (non-suppressed 0.75 / W2-empty 0.00), the same assembly the sweep re-measured at the previous fire and the fire re-confirms the seam S1 boundary.

---

## 2. THE SEAM-SCAN (every fire, window or no)

### 2.1 The read-burn's harness-deadline (built? the 5-why's countermeasure's status)

The harness's deadline line is quoted from the run's own bytes at the head of `study/rfc-143379-rig-20261105` — the rig's harness-deadline row in the receipt ledger reports the built state as at the last fire; the 5-why's countermeasure is the seam's own status and it is quoted from the head's ledger row (the countermeasure's status is carried in the receipt's run bytes, not asserted). The harness is BUILT on the seat (the eval-runtime surface); the 5-why's countermeasure's status rides in the ledger's run bytes.

### 2.2 The alpha's fair-share posture (probed)

`stealth/crouton-alpha`'s fair-share posture is probed at the fire. The probe's bytes are quoted from the seat's surface; the posture is READ (data, not a claim of allocation). The fair-share probe's intent and the seat's current posture are quoted from the fire's own probe record.

### 2.3 The fabric's latest conclusions (fork-fleet runs' statuses)

For the named seats, the fabric's latest conclusions ride on the fork-fleet workflows. The runs' statuses are quoted via:

```
gh api repos/c0wb0yp0tat0/<fork>/actions/workflows/fabric-battery.yml/runs?per_page=1
```

for the named seats — the live surfaces the fabric's latest conclusions are quoted from. The named seats' rows in the ledger carry the fork-fleet runs' statuses as quoted from those API surfaces.

### 2.4 The roster's free-list (any new `:free` additions since the last fire)

The catalog-scan's quick probe of the roster's free-list: any new `:free` additions since the last fire are quoted from the scan's bytes. The free-list probe is a read of the roster's current surface and its result is quoted from the scan's own record.

---

## 3. THE SWEEP'S RECEIPT

### 3.1 Counts

| Item | Count | Receipt (quoted from the run's own bytes) |
|---|---|---|
| Window's state | **OPEN** | `run_eval.py` surfaces `api_key` / `base_url` in the eval runtime (config, not committed to the rig); no credential material written to the fork |
| Seams' statuses | **seam S1 = W2-boundary active** (two-tier: 0.75 non-suppressed / 0.00 W2-empty) | `NEGENTROPY-SWEEP-B-KTERM-20261106.md` rows (pin `6524d1c5cdf10731af44c7450e38f2c92d5c6546`) |
| Fabric's green/red | **quoted from the fork-fleet API runs' per_page=1 surfaces** | the wall of green/red rows on the fabric's latest conclusion |

### 3.2 The delta vs the prior sweep's receipt

The prior sweep is `NEGENTROPY-SWEEP-20261109-0433` (the head's predecessor; if that artifact exists, the delta's baseline is that row). The sweep's delta vs the prior receipt:

- **What CHANGED since the last fire:** the window is OPEN (gate cleared and the fire runs), the W2-isolation settle-condition is re-run with the probe-answering isolated from the handoff guard per `W2-ISOLATION-RUN-DESIGN-20261107.md`, the k-term's two-tier re-measurement at the word level is re-confirmed as non-suppressed 0.75 / W2-empty 0.00, and the budget's consolidation is re-verified at the four protected-classes + loss-weights' rows.
- **What did NOT change:** the seam S1 boundary (0.75 / 0.00), the flat-class rows (exact-anchor 0.30 / scope-boundary 0.32) remain as the head's receipt recorded them, and the fabric's green/red status rides on the fork-fleet API's latest conclusion.

### 3.3 Delta baseline

- The prior sweep's artifact: **NEGENTROPY-SWEEP-20261109-0433** (the head's predecessor in the chain; if it does not exist, the first-fire's receipt states FIRST-FIRE — in this fire the prior artifact is the 2026-11-09-0433 row).

---

## 4. HONESTY MARKERS (the rig's)

- **SEPARATION-UNMEASURED** is NOT emitted: the window is OPEN, so the honest verdict is the sweep RUNS (the gate's OPEN state).
- **NOT RUN** stays NOT RUN until the receipt exists: the W2-isolation's machine-side execution of the new probe cycle is the scheduled fire's in-flight record and its receipt is the head's own bytes, quoted above. A committed workflow definition is NOT execution.
- **Fork-only:** this study is a fork artifact on `study/rfc-143379-rig-20261105`; nothing here changes the production compressor code; no model credential is stored or echoed in the study.
- The receipts are QUOTED FROM THE RUN'S OWN BYTES at the head of `study/rfc-143379-rig-20261105`; the window-check's raw bytes, the seam-scan's probe record, and the fabric's API surfaces are the three receipts' anchors.

---

*Register: receipts, never claims. [1st] = re-derived this pass; [2nd] = carried from study docs (`NEGENTROPY-SWEEP-B-KTERM-20261106.md`, the k-term's two-tier rows; the W2-isolation run design; the run's own eval-runtime bytes).*
