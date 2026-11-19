# NEGENTROPY-ARM-EXECUTE — the arming record (STAGE-2, head-executed), 2026-11-19

*The successor stage of the negentropy arming, executed by the head per the base-swap doctrine (Nemo's STAGE-1 plan landed at `24bd185313`; Nemo's STAGE-2 ride aborted on the seat's JSON-envelope quirk — the frame rides the seat that carries it, and the arming's mechanical steps ride the head). Every row below carries its receipt. The plan's rules are STANDARDIZED per Nemo's verdicts; the wiring is armed for the fire.*

## THE LOOP-STATE LINE (the single-source token, updated)
`NEGENTROPY-LOOP-20261119-v2 · STAGE-1 landed (Nemo) + STAGE-2 armed (head) · token source: this file · next: the fire's hold-audit (Nemo re-dispatch per STEER-3) · owner: head · UPDATED 2026-11-19 ~21:xx EST`

## 1 · THE TOKEN WATCHER — ARMED
- **The token's single source:** `NEGENTROPY-ARM-EXECUTE-20261119.md` (this file) — the loop-state line above is THE line; every watcher references THIS line, never a remembered stage.
- **The update rule:** `UPDATED <ts> · <stage> · <owner>` appended; two surfaces naming different stages = the watcher HOLDS (no dispatch on disagreement) and the head resolves.
- **The disarm:** the file is append-only; the token's stage line can be superseded by the next UPDATED line — never rewritten.
- **Receipt:** this file, committed and pushed (below).

## 2 · THE FOLD CHECKS — WIRED
- **The fold checklist (binding for every landing):** (a) the artifact on disk; (b) the scribe cell byte-verified (`save_memory` → `get_memory` byte-compare); (c) the served-verify where served (`?raw=1` grep); (d) the commit + push (ls-remote truth before and after); (e) the row to PR #1 in envelope-form (handles-only — that row IS the HITL update, never skipped).
- **The missed-fold trigger:** a landing without its cell (SCRIBE_MISMATCH/UNREACHABLE logged) is flagged and re-verified before the next dispatch — never silently carried.
- **Receipt:** the harness's write-time scribe assert (byte-identical=True observed on every landed lane); the fold rows in the lane logs.

## 3 · THE SUPPLY RE-SURVEY — RUN (the Nov-20 check, live)
- **Cloudflare Nov-20 deprecation — CONFIRMED LIVE (2026-11-19):** the official changelog still carries "November 20, 2026" (curl grep, 2026-11-19); the pricing page still lists the deprecating rows (kimi-k2.6/glm-5.2/deepseek-v4-flash-0731 present — the deprecated set, 4 hits). The lane-2 calendar's FLAGGED row stands: **do not dispatch new legs to the deprecated set after 2026-11-20; re-survey at dispatch time.**
- **Seat limits re-stamped:** the fleet's active rows (the four design seats, kenari, qwen4-max's window, SambaNova's 20-RPD tap) are dated facts — each dispatch re-reads its seat's live surface per lane-2's S1–S5 (never a cached row older than the window).
- **Receipt:** the curl greps above; lane-2's calendar as the base table.

## 4 · THE MACHINE-LAYER WIRE-CHECK — RUN (live, 2026-11-19)
| Surface | Check | Result | Receipt |
|---|---|---|---|
| Scribe tunnel :24282 | get_memory probe | REACHABLE (responded "Memory named 'rig-probe' not found") | curl, 2026-11-19 |
| Harbor :44831 | /v1/models | LIVE (DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q3_K_S.gguf serving) | curl, 2026-11-19 |
| SSH 192.168.1.241 | batch probe | REACHABLE — hostname c0wb0yp0tat0, disk 29% (77G free) | ssh -o BatchMode, 2026-11-19 |
| The wire-check rule (from Nemo's plan, now standardized) | pre-READY SSH probe per machine | **STANDARDIZED** — the head runs the probe before every READY; an unreachable machine is a named seam in the verdict, never a surprise | this row |

## 5 · THE DISPOSITIONS — SORTED (the sprint's items)
| Item | Disposition | Auto-path / packet |
|---|---|---|
| The probe (lane-1's plan, arms A/B/C + Luna leg) | AUTO-CONTINUE | fires on its seats; landings fold per §2; the decision rule is pre-committed |
| The bench door (lane-4's read) | AUTO-CONTINUE (once landed) | the three-state trigger rides the landings; ~$100 verify door stays two-way |
| The governance probes (lane-3's wires) | AUTO-CONTINUE (once landed) | each two-way-doored with rollback |
| The calendar's re-surveys | AUTO-CONTINUE | dispatch-time re-read per §3; Nov-20 gate is the hard line |
| The fold + scribe + rows | AUTO-CONTINUE | the §2 checklist is the standing fold |
| Anything needing a judgment the packets don't cover | NEEDS-THE-CHAIR | the chair = the head's calibrated judgment; packets pre-written (state + options + recommendation) |

## 6 · THE CHAIR-PACKETS — CUT
- **The only NEEDS-THE-CHAIR items tonight:** (a) the fire's READY verdict (the CTO-lens + no-lens pass — a packet will be cut from the landings); (b) any public move beyond PR #1's thread rows and the gists (the gate: nothing public without the user's word — that is the chair's, always); (c) the RFC upstream's quiet (the user's word is the only key).
- **Packet form:** state + options + recommendation, pre-written — the chair's judgment takes minutes when it arrives.

## 7 · THE HOLD-AUDIT (STEER-3, the fire-time certification — armed for the re-dispatch)
The operator's doctrine: once we fire, it succeeds on its own without us; we are here if needed. The audit that certifies this runs AT THE FIRE (Nemo re-dispatched per STEER-3, with this file as its ground): **HOLD** = the wiring survives the whole mission set without a human except the planned packets; **HOLD-WITH-NAMED-SEAMS** = each seam named with its auto-path or packet. Tonight's arming's pre-audit verdict: **HOLD-WITH-NAMED-SEAMS** — the names: the seat-envelope quirks (Nemo's JSON-blob class, a seat's 400s) are pre-armed by the base-swap doctrine (never retry the same lane; the frame rides the seat that carries it); the Nov-20 deprecation is dated and gated; the only true chair-items are the three in §6. Inertia drives; we are here if needed.

## THE COMPOSE-CHECK (this arming's own)
- deconstruct: FIRED (the six arming rows + the audit, each with its receipt)
- sense: FIRED (the plan's STANDARDIZE verdicts executed: token, mirror, folds, re-survey, wire-check)
- choose: FIRED (base-swap: STAGE-2 rides the head; the seat's ceiling named, never silent)
- calibrate: FIRED (live receipts — curl, ssh, the pricing-page grep; no estimate)
- probe: FIRED (the wire-checks actually ran; the Nov-20 date re-confirmed live)
- review: FIRED (the packet classes named; the audit's seams named, not hidden)
- record: FIRED (this file = the token's single source; committed + scribed below)
- compose-check: FIRED (the fire's hold-audit re-checks this arming at fire time)
