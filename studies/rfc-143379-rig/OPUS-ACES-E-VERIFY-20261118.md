# OPUS-ACES-E-VERIFY-20261118 — the VERIFIER lens (blind re-derivation of the landings)

Seat: kenari beam-1-0:free via kenari.id (fresh pool at 00:00Z) · scribe-cell: rig-opus-aces-e · RFC #143379 · branch `study/rfc-143379-rig-20261105`

## THE LENS
Verifier: blind re-derivation of every landing count from the raw artifacts (never from another lane's claim); sentinels and scribe-cells checked; adversarial asked what would make the apex an illusion.

## THE VERDICT
ADJUST — F1, F3, F4, F5 re-derive cleanly from `GAUGES-CYCLE-1` + `PROVIDER-ABSENCE-BATTERY-RESULTS` (raw), but two named gaps block full trust: (1) F2's metric shifted from GAUGES's "5/5 lenses landed" to CONFIRMATION's "3/3 crown rides + 1 goal-status ghost" with no documented bridge; (2) F6 mark 8's apex-hold half is self-referential (the mark certifies the verdict it is part of). Plus `CYCLE-4-NN-20261118.md` and `KAISEN-F6-20261118.md` were unreadable in this lane's window — their counter/mark claims are cited, not re-derived.

## THE FINDINGS
- F1 (read-solution readiness): 4/4 GREEN battery ceiling — re-derived: BATTERY run-1 2/4 (LEG-1 RED, stale-cell class), fix re-saved plan bytes, run-2 4/4 (LEG-1..4 GREEN); provider-call counter 0 by construction; GAUGES agrees. VERIFIED. Caveat: ceiling rests on one post-fix run; the two-flat counter 2/2 cited in CONFIRMATION (CYCLE-4-NN unreadable) — not independently re-derived. not confirmed at counter level.
- F2 (harness reliability): GAUGES baseline = 5/5 lenses landed (one after wall receipt), Nemo ghost at `4f66010a0d`. CONFIRMATION = 3/3 crown rides + 1 goal-status ghost (2 ghosts total). The two metrics (lenses vs crown rides) are not reconciled in the read window; "goal-status ghost" first appears in CONFIRMATION. ADJUST: publish the bridge before trusting NONE-REGRESSED.
- F3 (fleet utilization): 28/31 forks alight; 3 platform-disabled (agent-governance-toolkit, craft-anything, hermes-official-plugins); 3 self-hosted online + cloud Avrea. Re-derived from BATTERY fabric note + GAUGES + CONFIRMATION (all agree). VERIFIED.
- F4 (record completeness): 0 unrowed tracked modifications; untracked 3 (GAUGES landing) → 2 (CONFIRMATION); cells byte-integrity GREEN (plan 14,025 bytes sha256; B3 brief sha256). VERIFIED on 0 unrowed + byte-integrity. Caveat: "0 unrowed" excludes the 2 still-untracked files; completeness hinges on the tracked/untracked boundary. not confirmed whether those 2 are now rowed.
- F5 (project-layer currency): token advanced `STAGE-3-IN-FLIGHT` (GAUGES) → `CONFIRMATION-ARMED` (CONFIRMATION), both quoting `NIGHTSHIFT-PLAN` LOOP-STATE LINE; branch `study/rfc-143379-rig-20261105` unchanged. Re-derived via two independent quotes. VERIFIED. (Direct plan read not done in this window.)
- F6 (planning depth): GAUGES = 7/8 (mark 8 ABSENT, expected). CONFIRMATION = 8/8 (mark 8 FIRED). Mark 8 fires on battery 4/4 (receipted) + apex-hold (L5's gate). The battery half is receipted; the apex-hold half is the verdict this cycle certifies — self-referential. ADJUST: mark 8 must not certify itself; split the apex-hold witness to a lane other than the confirmer.
- Scribe-cells: CONFIRMATION `rig-nightshift-confirmation`; ENVELOPE `rig-opus-aces-e`; GAUGES `rig-nightshift-reload`; BATTERY head-side. Byte-identity claims (plan 14,025 bytes, B3 brief) re-derived via sha256 in BATTERY/GAUGES; cell-level byte-identity not independently re-read (read-gate closed before CYCLE-4-NN). not confirmed at cell level.
- Sentinel `df320b70c2` (ENVELOPE citation) not verified via git in this window. not confirmed.
- Adversarial (what would make the apex an illusion): (a) F2 redefinition masks a regression in lenses landed; (b) F1 ceiling from a single post-fix run; (c) F4 "0 unrowed" while 2 files remain untracked; (d) F6 mark-8 circularity; (e) two-flat counters in CYCLE-4-NN not re-derived here.

## THE NEXT
1. Publish the F2 bridge (lenses 5/5 → crown rides 3/3 + ghost accounting) with evidence. Cost: one doc edit. Slot: before the next-mission gate. Why: closes the only metric redefinition in the apex.
2. Split F6 mark 8 into battery-half (receipted) and apex-hold-half (witnessed by a lane other than the confirmer). Cost: one compose-check row. Slot: L5. Why: removes self-certification.
3. Re-derive the two-flat counters from CYCLE-4-NN in a follow-up verifier pass. Cost: one read round. Slot: pre-trust. Why: the counters are cited, not re-derived here (unreadable in this window).

## THE COMPOSE-CHECK
- think-tank spine — FIRED — ENVELOPE mission + LENS E + schema sections present.
- Amazon LP envelope — FIRED — verdict on re-derived evidence, named gaps, not-confirmeds.
- record-first — FIRED — all claims trace to GAUGES/BATTERY/CONFIRMATION files; no web.
- name-and-refuse — FIRED — CYCLE-4-NN, KAISEN-F6, NIGHTSHIFT-PLAN, git sha refused as unverified rather than estimated.
- two-way door — FIRED — ADJUST verdict is reversible; gaps are closable edits, not structural.
