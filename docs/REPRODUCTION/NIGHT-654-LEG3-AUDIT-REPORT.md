# NIGHT-654 LEG 3 — BLIND AUDIT (recompute, don't trust)

**Board card:** NIGHT-654-LEG3-AUDIT · **Auditor:** ornith (blind) · **Date:** 2026-10-30
**Method:** every claim re-derived from local git blobs + a fresh pytest collect-only at the published head + the live public fork API. Nothing trusted from leg prose.

---

## VERDICT: CLEAN-WITH-NOTES

All five core landings independently recompute TRUE. Leg 1's one known error (manifest claimed "on branch," was local-only) was corrected by leg 2 and is now genuinely published and hash-verified. Notes are documentation-completeness only — no false claims remain that would survive the morning regroup **provided** the regroup cites `b84150e9be` and keeps the two substrates distinct (N1, N2).

---

## Per-claim receipts

### 1. THE PUBLISH IS REAL — CONFIRMED
- **Branch head == b84150e9be:** `gh api .../branches/round2-combined-substrate` → `b84150e9be88911280f981467de9628fcfb0f60f` ✓ (public fork `c0wb0yp0tat0/hermes-agent`).
- **Parent chain:** `b84150e9be^ == 995de91d281f6613ae4a77ee43bebf6febef8993` ✓ (local git; exactly leg 2's claimed old head).
- **Manifest + sidecar present in tree:** `KVNLOO654-297-BATTERY-MANIFEST-20261030.md` (blob `6dc5100b…`, 6909 B) + `KVNLOO654-297-BATTERY-MANIFEST-20261030.sha256` (both type=blob at head). My first `.md.sha256` probe 404'd — wrong path shape; the real sidecar drops the `.md` before `.sha256`. Not a defect.
- **Manifest commit touched ONLY the 2 files:** `git diff --stat 995de91d b84150e9be` → manifest (127 lines) + sidecar (1 line), `2 files changed, 128 insertions(+)`. "Tree otherwise clean" ✓.
- **Five hardening files UNCHANGED by the manifest commit:** `git diff 995de91d b84150e9be -- <5 files>` = empty. Parity 0/5 carries from 995de91d to b84150e9be, nothing new ✓.

### 2. THE 297 IS EXACT — INDEPENDENTLY RE-RUN (stronger than the published-bytes fallback)
- **Worktree detection caveat:** my first `[ -d .git ]` test reported the worktree GONE, but a worktree's `.git` is a *file*; `git worktree list` shows `/tmp/kvnloo654-combined` **exists at b84150e9be** (satisfies the brief's exact condition). Either way I did better: a **fresh detached worktree at the exact published head** `b84150e9be` (local commit == remote full hash, verified).
- **`pytest --collect-only` at b84150e9be:** `297 tests collected in 2.62s`, exit 0, zero collection errors.
- **Per-file all MATCH** (collected vs manifest §3): rfc_homework 16/16, fix01 5/5, fix02 7/7, fix03 6/6, fix04 8/8, fix05 9/9, write_gate 6/6, memory_tool 64/64, patch_action 19/19, target_contract 64/64, write_approval 24/24, write_deny 10/10, threat_patterns 57/57, schema 1/1, import_fallback 1/1. No extras, no missing, no zero-collected.
- **Sum:** 16+5+7+6+8+9+6+64+19+64+24+10+57+1+1 = **297** ✓ (re-derived, not trusted).
- **Published-bytes hash:** raw curl → `sha256sum` = `44ae6e303706ec7029b6d098f9ce72dc1cff68970b3a9f9290bad7c1f791e422`, 6909 B ✓ (matches leg 2 + the sidecar content exactly).

### 3. THE PARITY SLICE — CONFIRMED (both directions, from local blobs)
- **b84150e9be = 0/5 vs f90969ae** (all five MISMATCH): memory_tool `6a0e71fd`≠`f5969419`, memory_tool_store `89b32c79`≠`5779d00c`, surfaces.json `5a14ee1d`≠`9adee579`, memory.json `980d90b8`≠`c255b898`, test_memory_tool `f197f308`≠`776fbef2`. Parity 0/5 stands at the new head ✓.
- **e0bb8b504b = 5/5 identical to f90969ae** (all five MATCH) ✓. Parent `e0bb8b504b^ == af16e3ab16eed2492552c325ad1777533a8b7004` ✓ (the readfix-only sibling's base is af16e3ab16, as leg 1 claimed).
- **The five-file set is correct:** f90969ae touched 6 files; the sixth `tests/observability/shared_metrics_contract.py` is empty (`e3b0c442…` = empty-string sha256), correctly excluded from the five.

### 4. P3 — CONSOLE SNAPSHOT GROUND TRUTH — NEEDS-KVINLOO-SIDE
Grounded in #654 comment `RFC1-AVREA-RECEIPTS-20261025` (kvnloo/hermes-agent), corroborated by the plan + later comments.
- **(a) Whose side:** KEVIN's. The lane is canonical `fleet-avrea` → `kvnloo/fleet-runner` `verify.yml` (`docs/fleet/README.md`, `kvnloo/.files`). The `fleet-avrea-budget` gate and the Avrea meter live on his infra. The receipts state the meter "needs a fresh console reading **from Kevin**" — our side cannot read the live meter (last snapshot 2026-10-24T23:15Z was refused: `accounting unavailable: snapshot is future-dated, stale (>24h)`).
- **(b) November reset:** the 2×32 layout needs 2,402 reference minutes vs the 1,722-minute free allowance → `fleet-avrea-budget` refused. A monthly reset (month roll, Nov 1) is the mechanism that WOULD re-open the gate (fresh allowance), but it is a **future** event (today is Oct 30) and unconfirmed — the live meter is unreadable to us. The "monthly reset" cadence is the plan's framing; the receipts establish the allowance/need/refusal but not the exact reset timing.
- **(c) Honest status line:** **NEEDS-KVINLOO-SIDE.** No fresh console snapshot has been provided (the Oct-26 comment records it was bypassed "on Kevin's instruction; there was no fresh console snapshot"; nothing newer supplies one). The gate's open/closed state is UNKNOWN to us pending Kevin's snapshot.

### 5. WHOLE-PACKAGE PUBLISHABILITY
No leg-1/leg-2 claim is false. The one historical error (leg 1's manifest "on branch") is corrected and re-verified as published. The five hardening files, the manifest bytes, the 297 sum, and both parity slices all recompute. Embarrassment risk is confined to two framing traps a careless regroup could fall into (N1, N2 below) — both are notes, not errors.

---

## Corrective-only change list (no rewrites)
- **N1 — Cite the current tip, not the parent.** The morning comment must name `b84150e9be` (branch head, where the manifest lives), not `995de91d` (substrate-only parent). Test tree is byte-identical at both, so the 297 holds at either; only the pointer needs to be the tip.
- **N2 — Keep the two substrates distinct.** The 297 battery is on the **combined substrate** (0/5 vs f90969ae — it does NOT contain jfugalde's five hardening fixes). `f90969ae` is a SEPARATE readfix reference; the sibling `e0bb8b504b` is the 5/5-to-f90969ae one. Conflating "the 297 is on the readfix substrate" would mislead Kevin's runner. State both, plainly.
- **N3 — Manifest §1 commit reference is one behind.** §1 says the enumeration is at `995de91d28`; the manifest is published at `b84150e9be` (its parent). Add a clause: "test tree identical to tip `b84150e9be`." Corrective-only; counts are right at both.
- **N4 — Two re-run receipts, one not in the manifest.** Manifest §5 documents the re-run at 995de91d (`b9438c93…`, 14.90s); leg 2's landing also cites a re-run at b84150e9be (`df43c6c8…`, 14.24s). Both = 297 passed; the manifest doesn't mention the b84150e9be run. The auditor's own collect-only at b84150e9be (=297, all per-file match) closes the gap independently. Informational.
- **N5 — P3 reset wording.** Say "the Nov-1 monthly reset WOULD re-open the gate; confirmation needs Kevin's fresh console snapshot (meter unreadable to us, last reading stale)." Don't assert the gate is currently open — it is UNKNOWN pending his side.

---

## Summary (one paragraph)
The publish is real and the numbers survive a cold recompute: the public branch head is `b84150e9be` (parent `995de91d`, manifest + sidecar the only two files added, the five hardening files untouched), the manifest's published bytes hash to `44ae6e30…e422` (6909 B, sidecar matches), and a **fresh `pytest --collect-only` at the exact published head collected 297 with every per-file count matching the manifest** (not just the arithmetic). Parity recomputes both ways — `b84150e9be` is 0/5 vs `f90969ae` (same five mismatches, nothing new) and the readfix-only sibling `e0bb8b504b` is 5/5 identical. P3's honest status is **NEEDS-KVINLOO-SIDE**: the Avrea console/meter is on Kevin's `fleet-runner`, our side can't read the live allowance (last snapshot refused as stale), and the Nov-1 monthly reset is the mechanism that would re-open the 2,402-vs-1,722 gate but is future and unconfirmed. Verdict CLEAN-WITH-NOTES — five corrective-only notes, the operative two being "cite b84150e9be not 995de91d" and "keep the combined substrate (0/5) distinct from the readfix sibling (5/5)." Leg 1's one known error is corrected and re-verified. Disk 89% (7.4G free); read-only, no pushes, temp worktree removed, leg 2's `/tmp/kvnloo654-combined` untouched.
