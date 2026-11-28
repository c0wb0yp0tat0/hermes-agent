# IMPROVEMENT CYCLE — matrix + rulers (2026-11-27, closed)

Cycle run per the private-repo framework (mechanism-of-mechanisms: the ACES loop + the mini-spine
deconstruct → sense → choose → calibrate → probe → review → record → compose-check) with the
matrix shape from xngg1021's academic-research-kernel (asserted → status → basis) and the
fit-selected instruments: grounded-citations (every claim carries its receipt), the data-forensics
trio (defect-forensics / investigation-documentation / agent-work-review), the audit-of-audit
(L2 independent pass listed below), and the pin discipline (verbatim carry, contradiction flags).
Rulers were built where none fit the surface (the operator's "make a custom ruler" steer) — each
ruler below states its unit and its final reading.

## The rulers

| Ruler | Unit | Max | Final |
|---|---|---|---|
| R1 battery coverage | cells × contours | 12 × 3 | 36/36 |
| R2 ask coverage | thread asks answered in drafts | 13/13 | 13/13 (verified by probe below) |
| R3 commit-readiness | placeholders in the staged set | 0 | 0 (prediction sha 337e87d1…e0e7 embedded) |
| R4 hash parity | drop ↔ gist files matching | 7/7 | 7/7 |
| R5 standardization | battery legs in the kit | 1 | 1 (read-battery-20261127/, README + seams named) |

Plateau condition reached: every ruler at its max AND the probe of further candidates shows
no measurable delta (candidates below).

## MAP matrix (asserted → status → basis)

1. The fixed read (a43818a6…1586a) answers both stores on our layer — PASS — live store read on
   pve1: memory 11 entries, user 13; twice-read byte-identical; hashes unchanged (this session,
   2026-11-27).
2. The fixed read's view is sanitized on every contour — PASS — BLOCKED marker + blocked index,
   `threat_text_leaked: false` on pve1 / WSL2 / native Windows (battery JSON, 3 receipts).
3. The read holds a real lock, both backends — PASS — structural 50/50 inside / 50/50 outside on
   all three contours; live-held probes refused while read() ran (26/80, 25/80, 10/80).
4. The Windows/mSvcrt contour is verified, not assumed — PASS — native py 3.14.7, real
   `msvcrt.locking`, same battery, green rows (the `inside_blocked_50` 50/50 there included).
5. The miss path is clean and byte-safe — PASS — corrupt-file cell: `success: false`, the
   read-failed error, file hash unchanged (3 contours).
6. The dispatch arm reaches the read — PASS — `_memory_tool('read', …)` returns
   ("success", payload with 3 entries) on all three contours (contract measured first; the
   dispatch's label is "success", not a message — my first assertion was wrong, corrected).
7. The tool surface of THIS session exposes no read action — MEASURED, by design — the session's
   memory tool = operations (add/patch/remove); the official docs: "There is no `read` action —
   memory content is automatically injected into the system prompt at session start";
   PR #12831 (teknium1, 2026-04-20) = the maintainer-side refusal the child's evidence answers (E6).
8. The installed store is spec-2 shaped (no lock on read) — MEASURED — `_file_lock` appears only
   at L257/L350 of the installed store; the read body L441-455 holds none; atomic rename + strict
   decode are the safety. The child ships spec-1 per #141876; both shapes verified in the field.
9. The harness writes must be explicit UTF-8 — EARNED — the ANSI-codepage default (cp1252 on the
   PC's py 3.14.7) produced lone 0xA7 bytes; the store's strict `utf-8-sig` read refused them
   (read_ok=False) — the wipe-class guard demonstrated live, then harness fixed (battery now green
   everywhere). Folded as a skill pitfall (krecency-instrument).
10. kvnloo ran macOS/fcntl only — MEASURED — both comments (7210367328, 7211318206) name Python
    3.15.2, macOS, real fcntl; no Windows/msvcrt mention; his structural hook row 3 is the
    battery's structural leg (50/50 ×2 on three contours).
11. The prediction is commit-ready — PASS — the literal's sha256 (337e87d1…e0e7) embedded; the
    file's own metric: placeholders 0.
12. The staged reply set answers every named ask — PASS — see R2 probe below.
13. The bundle ships with named seams only — PASS — memory_tool seam = real head (1-476) + declared
    out-of-scope registry block (surface registration); registry seam mirrors the real decorator
    (tools/registry.py:272-275); utils seam = verbatim atoms only; store + threat_patterns +
    hermes_constants real (store sha a43818a6…1586a).

## R2 probe (ask coverage — mechanical)

- kvnloo draft contains: "prediction", "6609dac", "held-open arm does not cover", "structural",
  "parked" — present.
- 3oltan draft contains: "msvcrt", "WSL2", "native Windows Python 3.14.7", "50/50", "read-invoked",
  "BLOCKED", "smallest diff", "regular issue", "narrower first slice" — present.
Asks not named by either comment: none (both comments fully quoted in the thread log; the matrix
stands at 13/13 — the reply pairs: kvnloo spec decision + adoption + parked line + hook row +
"tell us" closure [5]; 3oltan sanitize scope + leak parked + Windows numbers + WSL2 caveat +
read-invoked + two agreements + pilot register [7] + the letter to the room's "Seen… dig in"
closure [1]).

## L2 audit (independent passes over the above)

- Twice-read stability re-run across the cycle (battery's own double-pass + the store-level
  repeats on three contours).
- Hash parity independently computed from the API's returned bytes (not from the manifest's own
  numbers) — 7/7.
- The structural row re-derived: first pass (lock.lock artifact), second pass (correct path),
  third pass post-encoding fix — three independent measurements converging on 50/50 ×2 ×3 contours.
- The dispatch contract measured (returned tuple) before the assertion was written; the assertion
  corrected once, then green on three contours.

## Parked (named, with the un-park condition)

- The long-session recurrence ground (K-recency instrument): the 24h corpus was retry-dominated
  (7 literals/173 re-mentions, K=10 carry 17.9%); the honest multi-turn stream needs a successful
  long session's transcript — un-park when one exists in the dumps.
- The 35-cell suite port to the bundle: the battery covers the three field points + the envelope's
  named properties (12 cells); the full suite rides the kit's own test file — un-park if the
  contour table must include the entire battery byte-for-byte.
- The gateway read wiring: the store answers from this Telegram session; the surface exposes no
  read action per the documented contract — the child's ask — un-park when the child lands.
- E6 (answer PR #12831's rationale in the child): staged, waits the word.

## Compose-check

- Nothing posted; every artifact staged on the drop + the secret gist (7/7 parity); the kit's
  battery leg added untracked (no commit/push); chain folded to 021; the skill pitfall folded.
- The operator's review surface: this file + the gist.
