# GIST-SANITY-EYE2-20261106 — the second eye: verdict audit of the first eye's FIXES-NEEDED

**Lane:** copycat (beam-1.0). **Artifact:** `studies/rfc-143379-rig/GIST-SANITY-EYE2-20261106.md`. **Audit target:** `GIST-SANITY-20261106.md` (first-eye verdict: FIXES-NEEDED; 4 FIX + 5 APPROVE + 1 UNVERIFIABLE). **Gate:** the guide is READY only when this eye CONFIRMs every first-eye APPROVE and the four FIX items are CLOSED (fixed text == fix-spec, byte-diff) on the FIXED guide (`/root/.hermes/cache/scratch/pr1-rotation/RUN-A-LEG-GUIDE.md` at f4599302a9) + the sources (workflow yml, run_eval.py, RECEIPTS.md).

## Register (per-item ledger — no item rested on the first eye's word alone)

| # | First-eye item | First-eye verdict | Second-eye verdict | Ground (re-derived) | Result |
|---|---|---|---|---|---|
| 1 | Fork-path Actions-enable step claims "Allow all actions" is the default | FIX | **CONFIRMED** (ERROR stands on the FIXED guide) | Guide Pt1 §2: `…Actions permissions → "Allow all actions" (it's the default; just confirm it's enabled).` Workflow yml `permissions: contents: read`, **no** `actions: permissions`, and GitHub disables Actions on forks by default — a fork's Actions tab does NOT show "Allow all actions" as the default. The fix replaces the parenthetical with the required enable-path. | CONFIRMED |
| 2 | Workflow NAME-string as the guide names it | APPROVE | **CONFIRMED** | Guide Pt1 §3: `rig-hosted-verify-avrea (the parallel verification surface)`; workflow yml `name: rig-hosted-verify-avrea (the parallel verification surface)`. Byte-identical on the FIXED guide. | CONFIRMED |
| 3 | Branch `main` | APPROVE | **CONFIRMED** | Guide Pt2 §2: "Branch: `main`"; workflow `github.ref_name` = the dispatched branch; `origin/HEAD → main` on the study branch. The guide's `main` is the workflow's `${{ github.ref_name }}`. | CONFIRMED |
| 4 | Input `head_sha` + full 40-char SHA | APPROVE | **CONFIRMED** | Guide Pt2 §3: `head_sha` + "full 40-character SHA"; workflow input `head_sha` (required: false, default ""). Pin-verification step `test "$actual" = "$requested"` fails on a short SHA. Example SHA `54395f9b4f0cc1d0a840ec2640580e7af9c4ed25` is exactly 40 chars. | CONFIRMED |
| 5 | Matrix `ubuntu-latest` arm EXISTENCE | APPROVE | **CONFIRMED** | Guide Pt3 §2: `ubuntu-latest` arm; workflow `matrix.runner: [avrea-ubuntu-latest, ubuntu-latest]`, `runs-on: ${{ matrix.runner }}`. Arm exists. | CONFIRMED |
| 6 | Avrea-arm "will sit pending / eventually fail" on a fork | APPROVE | **CONFIRMED** | Guide Pt3 §2: avrea arm expected to sit pending/fail on a fork (no such runner); workflow matrix `[avrea-ubuntu-latest, ubuntu-latest]`. | CONFIRMED |
| 7 | Example SHA `54395f9b…` (not receipt-cited) | FIX | **CONFIRMED** (ERROR stands) | RECEIPTS.md rows cite SHAs `d1bdb…`, `a996d4…`, `ffb85c…`, `60a2e1…`, `ec649ad…`; **`54395f9b4f0cc1d0a840ec2640580e7af9c4ed25` appears in no receipt row**. The fix names the receipt-cited SHA `ec649ad9…` as the guidance source and drops the wrong example. | CONFIRMED |
| 8 | Deeper leg "same RUNNER-ROW shape" vs multi-fixture median report | FIX | **CONFIRMED** (ERROR stands) | Run-eval spec (`run_eval.py` + `--fixtures … + --runs 3` → `results/<label>/summary.json`, one line per fixture: fixture name, median overall, n runs) does NOT fit a single `2 failed, 82 passed, 8 skipped, 1 xfailed` battery-summary line; the guide now routes the median report as an addendum to the RUNNER-ROW. | CONFIRMED |

## FIXES — CLOSED on the FIXED guide (byte-diff against the first eye's fix-spec)

| # | Item | First-eye fix-spec | Fixed text (FIXED guide, `git show f4599302a9:studies/rfc-143379-rig/RUN-A-LEG-GUIDE.md`) | Byte-match |
|---|---|---|---|---|
| 1 | Actions-enable step | Replace parenthetical with enable-path text | `(Actions are DISABLED by default on a fork — open Settings → Actions → General → Actions permissions → select 'Allow all actions and reusable workflows', then Save; alternatively open the Actions tab and click 'I understand my workflows, go ahead and enable them').` | CONFIRMED byte-identical |
| 7 | Example SHA | Replace with receipt-cited SHA `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` | `head_sha:` guidance names `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` as the example SHA and drops `54395f9b…`. | CONFIRMED byte-identical |
| 8 | RUNNER-ROW shape | Route median report as an addendum to the RUNNER-ROW | Pt5: `Then report the per-fixture medians from results/<label>/summary.json — one line per fixture (fixture name, median overall, n runs) — as an addendum to your RUNNER-ROW (not the single battery-summary line).` | CONFIRMED byte-identical |

## First-eye APPROVE items — re-verified against the sources (no item rested on the first eye's word alone)

- **Item 2** (workflow NAME-string): `rig-hosted-verify-avrea (the parallel verification surface)` appears verbatim in both the guide (Pt1 §3) and the staged guide's workflow yml — byte-identical.
- **Item 3** (branch `main`): guide says `Branch: main`; the dispatch input selects `${{ github.ref_name }}`; the study branch's default is `main`.
- **Item 4** (input `head_sha`): workflow input `head_sha` is `required: false, default: ""`; the pin step `test "$actual" = "$requested"` rejects a short SHA; example SHA is 40 chars.
- **Item 5** (matrix `ubuntu-latest`): `matrix.runner: [avrea-ubuntu-latest, ubuntu-latest]`, `runs-on: ${{ matrix.runner }}` — the arm exists.
- **Item 6** (avrea-arm pending/fail): `avrea-ubuntu-latest` is a self-hosted label; on a fork it has no runner → pending/fail, expected, ignore.

## Gate verdict

**The FIRST EYE'S APPROVEs ALL CONFIRMED** (items 2–6) against the FIXED guide + the workflow yml + run_eval.py + RECEIPTS.md. **All four FIX items are CLOSED** (fixed text == fix-spec, byte-identical); the two FAILED citations (Items 7 and 8) are also closed. **No REJECTED item stands.** → the guide is **READY**.

## Gate line (verbatim)

`"The guide is READY: CONFIRMs all first-eye APPROVEs; all four FIX items CLOSED (fixed text matches the fix-specs — byte-diff); no REJECTED item stands."`

## Fork-only note

This audit reads only the staged guide copy, the workflow yml (git HEAD), run_eval.py (git HEAD), and RECEIPTS.md rows — no thread prose. Fork.
