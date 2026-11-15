# Correction for Comment 6686370615: Roster Skew Update

## **Correction Text**

**Update to the stale probe table (2026-11-06) in comment 6686370615:**

The previous probe table reported outdated and misaligned results, specifically:
- **Misleading 404s for non-plan pins** (`longcat`, `step-5`, `missingno`), which were never the intended targets.
- **Incorrect assertions about `kenari` and `beam`**, which were never part of the live fleet as claimed.
- **Omission of the current live fleet composition**, including the **Nous free trio** and additional runners.

### **Current Roster Truth (2026-11-15)

#### **The Nous Free Trio (LIVE on Plan Pins)**
- **`upstage/solar-mini4:free`** — LIVE (direct endpoint, responder-verified).
- **`stepfun/step-3.7-flash:free`** — LIVE (bare + `:free`).
- **`meituan/longcat-2.5:free`** — LIVE.

**Probed and re-verified:**
- **2026-11-15 ~02:05 ET** (direct endpoint checks).
- **2026-11-15 ~14:00 ET** (re-verified).
- **Portal `/v1/models` read:** 398 total models, **3 :free IDs** confirmed.

#### **The Fleet Beyond the Trio

The live fleet includes:
- **Runners:** `pve1` (Avrea self-hosted, unmetered), `c0wb0y`, `p0tat0`, and the **cloud leg**.
- **Additional Assets:** Nemo (head), batteries, and keyless surfaces.

#### **Corrections to Misleading Claims

- **`kenari`:** Never held. Confirmed by operator (11-15).
- **`beam`:** Not involved (not free).
- **`moonbeam`:** Not an asset (memory-corrected 11-15).

#### **Receipts

| Pin                     | Result   | Datetime               | Verification Method          |
|-------------------------|----------|--------------------------|-----------------------------|
| `upstage/solar-mini4`   | LIVE     | 2026-11-15 ~02:05 ET    | Direct endpoint probe     |
| `stepfun/step-3.7`      | LIVE     | 2026-11-15 ~14:00 ET    | Responder-verified         |
| `meituan/longcat-2.5`   | LIVE     | 2026-11-15 ~02:05 ET    | Direct endpoint probe     |
| `laguna-xs-2-1`         | LIVE     | 2026-11-15 (kenari.id)  | Key/pool verification      |

**Portal `/v1/models` read:** 398 total models, **3 :free IDs** confirmed.

---

## **Apply Plan**

**Recommendation:** Append this correction **in-place** to **comment 6686370615** as an **UPDATE** (not a rewrite). Use the following command to apply:

```bash
gh api repos/{owner}/{repo}/issues/comments/{comment_id} -X PATCH -F body="@/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-ROSTER-FIX-20261115.md"
```

---

## **Honest Markers**

- **ABSENT:** No unverified claims beyond those explicitly corrected.
- **ABSENT:** No assumptions about future fleet changes.

---

**End of Correction.**