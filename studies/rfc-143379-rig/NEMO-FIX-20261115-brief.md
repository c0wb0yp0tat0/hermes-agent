# NEMO FIX RIDE — the PR #1 roster-skew correction (2026-11-15) — Nemo's strategic position: the fix's composer

## Your role (fleet asset, CTO assistant)
Compose THE CORRECTION for a skewing comment on PR #1 (homebase). The head applies it; your deliverable is the correction text + its receipts. WRITE-ONLY contract: everything is inline; reading anything is a contract violation (the read-scatter class). Round 1 = the skeleton; then write only. ONE tool call per round. NEVER run git. Receipts per claim (INLINE-crate / DESIGN-NOTE / ABSENT).

## The target (inline)
Comment **`6686370615`** (2026-11-06 13:50Z, "LADDER-BATTERY STALL-ROW 2026-11-06") carries this skewing probe table (verbatim from its body):
> "The live-probe, made truthful: a direct dispatch-endpoint probe ... reports: longcat 404, laguna-s 404, laguna-xs 404, step-5 404, missingno 404 — solar-mini4 LIVE (pin-verified) and deepseek-v4-flash LIVE (pin-verified)."

That table is the mispin-era reading (probed pins `longcat`/`step-5`/`missingno` — NOT the plan's pins). The corrected truth, receipted:
- **The Nous free trio is LIVE on the plan's pins** (direct endpoint, responder-verified — model field == requested pin): `upstage/solar-mini4:free` LIVE · `stepfun/step-3.7-flash:free` LIVE (bare + :free) · `meituan/longcat-2.5:free` LIVE. Probed 2026-11-15 ~02:05 ET and re-verified ~14:00 ET (+ the portal's live /v1/models read: 398 total, 3 :free ids).
- The 404s in the old table probed NON-pins (`step-5`, `missingno`, bare `longcat`) — a pin-mismatch class, never a zone end.
- **kenari: NEVER held** — the operator's word (11-15); a live fleet surface (laguna-xs-2-1:free probed OK on kenari.id today, its own key/pool).
- **beam: NOT involved** (not free — the operator's word). **moonbeam: NOT an asset** (memory-corrected 11-15).
- **The fleet is bigger than the trio:** the runners — **pve1 (the Avrea self-hosted, unmetered), the cloud leg, c0wb0y, p0tat0** — plus Nemo, the head, the batteries, the keyless surfaces. The trio is the Nous core; the fleet is the whole.

## The deliverable
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEMO-ROSTER-FIX-20261115.md`:
1. **THE CORRECTION TEXT** — one comment-ready correction in the thread's register: names the stale framing (the 11-06 probe table), corrects it with the receipts above, states the current roster truth in speakable lines — the shape of the thread's UPDATE convention (an appended correction with citations, never a rewrite of history).
2. **THE RECEIPTS** — the probe rows (pin, result, datetime), the portal head-count read, the operator's words (kenari never held; beam out; moonbeam out; the 4 runners named).
3. **THE APPLY PLAN** — the patch target (comment 6686370615, in-place PATCH via `gh api ... -X PATCH -F body=@<file>`) or the UPDATE-comment route (appended with the citations) — your recommendation, one line.
4. **THE HONEST MARKERS** — anything unverified stays ABSENT + named.

## Binding
- The RFC + upstream stay QUIET — this is PR #1's own thread, the correction's home.
- End condition: the file > 4,000 chars, section 1's correction text standing alone as a clean comment body; then stop. No git.
