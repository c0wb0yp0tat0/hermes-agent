# NIGHTSHIFT-LENS-4 — the seam & fail-safe wiring
seat: tencent/hy4-flash:free · scribe-cell: rig-nightshift-lens4 · 2026-11-18

Steered by STEER-8 (the nightshift green light: whole fleet plans its night, reads never restore, seam carries the arc across any throw, no gates beyond public posts). Scope: seam wiring + fail-safe dispositions + the missing stage trigger. Claims trace to the three-source pack; own words throughout; RFC quiet.

## 1. SEAM-WIRING MAP (how the arc survives a throw)

**Cold start — the three-rung ladder.** A thrown session reconstitutes the mission in three ordered reads: the handoff segment 014 first (names the prior landing + current deck), then the mission map (scenario, sequence, contract, appendices), then the steer channel (live operator words, latest = STEER-8). The order is not preference: 014 says where the deck is, the map says what the mission is, the channel says what changed. All three are local branch artifacts — a throw costs three reads, not a re-brief. The seam contract and STEER-8 both assert this carry; the loop-state line is the resume byte.

**Mid-mission handoffs — pointer renewal.** Each stage does not merely finish; it repoints the deck. A landing writes its artifact, byte-verifies into its scribe cell (two-way door), then advances the map's loop-state line to the next stage token. That line is the deck's live pointer: the bearings artifact ends STAGE-1-LANDED / STAGE-2-ARMED; STEER-6's continuation contract shows the same landing-verifies-then-fires shape. Renewing on every landing means any throw resumes at the exact stage, not the start.

**Crons as seam-proof executors.** The rig has 18 live jobs (motion-watch, restored negentropy cadence, a 3h fleet cycle, storms, watchers, guards) with on-disk outputs — machine execution needing no seated session, itself a mineable record. These are the natural trigger carriers because they run with or without the head. **The gap:** none watches the mission's loop-state line, so no cron fires stage advancement — STAGE 2 onward still depends on a seated head reading the map. That seam hole is closed in §3.

**The pair's register.** "We" = the pair (head + its CTO-assistant seat, the operator's proxy/mirror). "The fleet" = everyone else: free reasoning lanes, kenari backbone, all runners incl. cloud Avrea, keyless surfaces, and every fork. The pair owns calls, folds, and the public surface; the fleet executes slices and fires on dispatch. AMENDMENT-3 folds the full runner set and all forks into the never-idle ensemble — forks are first-class fired assets, not spectators.

## 2. FAIL-SAFE DISPOSITIONS (silent-check-in protocol)

Principle: nothing stalls when the chair is absent; the only absolute hold is public writes. Dispose every item before the check-in goes silent.

**AUTO-CONTINUE (fire on the green light, no chair):**
- The five planning lenses + swap-and-enrich + reload compose: STAGE 2 is armed on STAGE-1-LANDED; green light stands (STEER-8, no gates).
- STAGE 3 fire + STAGE 4 loops: the build, the provider-absence battery, the ACES cycles, whose terminal is the six measured fronts each reading no-improvement twice (AMENDMENT-2). Loops stop on measurement, not on a check-in.
- Runner ensemble + fork-battery: never-idle across all seats incl. cloud Avrea and all forks, at the highest metered cadence (AMENDMENT-3).
- Gists and PRs: the sole public surface — landings, the final gist fold, branch PRs proceed.

**HOLD-SAFE (never stall — take the named auto-path):**
- Public posts beyond gists/PRs (comment posts, upstream opens): hold absolutely; auto-path = stage the intended text as a draft row/cell in the private repo, post nothing.
- RFC #143379: hold; auto-path = stay one-way on our side (quiet/404 from this repo), record locally, open nothing.
- Live-end config changes (background-review toggle): hold; auto-path = document-only + wire/sandbox-test in the fork, never touch live config (STEER-6B).
- Darkhorse pick/host: hold; auto-path = keep the board-ready family shapes parked as an option, fire nothing until plan + machine exist.
- Any self-imposed gate: hold; auto-path = fire when the plan is ready (STEER-4B revoked self-gates).

**NEEDS-THE-CHAIR (true one-way doors only — minimized; each pre-written now as a context/options/recommendation/reversibility/cost packet):**
- Re-shaping the plan's spine (sequence, scenario, contract): only the operator re-shapes; appendices ride on top (addendum note).
- Reversing the public-writes hold or opening upstream RFC #143379.
- Flipping the background-review toggle on the LIVE end after sandbox verification.
- Committing spend/hosting for the Darkhorse machine (a hard-to-unwind resource door).
Four doors, each packet drafted so an absent chair costs a read, not a stall.

## 3. THE MISSING TRIGGER'S DESIGN

Add one cron: the **stage-advance watcher**.

- **Gauge:** the mission map's loop-state line is the single source of truth. Each tick the watcher reads that token; a stage advances only when the prior stage's landing is byte-verified in its scribe cell and the line names it landed. Deep sequencing holds: STAGE-2-ARMED → dispatch planning; PLAN-LANDED → STAGE 3 fire; STAGE-4 with all six fronts no-improvement-twice → HOLD.
- **Cadence:** a 30-minute watch — faster than the 3h fleet cycle (covers a thrown head within half an hour) but not a spin. Idempotency: it stores the last-fired token in its own cell and will not re-dispatch the same token; advancing requires the line to change.
- **Two-way door:** the watcher never fires blind — it writes an advance-intent row, reads it back byte-verified, then dispatches. A present head overrides (pair owns calls); re-arming = resetting the loop-state token. Strictly seam-internal: posts nothing public, opens nothing upstream, touches no live config. If the map is missing/incoherent it holds-safe and logs the discrepancy rather than guessing a stage.

## 4. COMPOSE-CHECK TABLE (eight marks, one evidence line each)

| # | mark | state | evidence |
|---|------|-------|----------|
| 1 | cold-start ladder 014→map→channel | FIRED | seam contract + STEER-8 assert the carry |
| 2 | pointer renewal per landing | FIRED | loop-state lines + STEER-6 landing-verifies-then-fires |
| 3 | crons as executors | FIRED | 18 live jobs w/ on-disk outputs (bearings) |
| 4 | stage-firing cron | ABSENT | cron list has no loop-state watcher (bearings); designed in §3 |
| 5 | pair / fleet register | FIRED | head owns calls (steer channel); AMENDMENT-3 folds forks + all runners |
| 6 | fail-safe dispositions | FIRED | map fail-safe clause + STEER-8 no gates |
| 7 | public-writes hold | FIRED | map "only gate: posts outside gists and PRs"; STEER-8 |
| 8 | upstream quiet | FIRED | RFC quiet/404 (bearings); STEER-6 "RFC quiet" |

Seven marks FIRED, one ABSENT (mark 4) — the missing trigger, now designed. Every mark traces to the pack.
