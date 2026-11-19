# RETRIEVER-RESHAPE-20261119 — the bridged arm's presentation reshape (design lane)

Seat: copycat (design lane) · branch `study/rfc-143379-rig-20261105` · RFC #143379. Gate verbatim: "nothing public without the user's word." RFC QUIET. Artifacts only. Wall clause: "a non-reproduction is a QUESTION, not a stop." Pre-registered path: attribution failure → RETRIEVER RESHAPE, never store. ABSENT, named: the F6 cert door packet / the operator's word (chair-gated) — this pilot rides the pre-committed gate, not the F6 door.

## 0. SEED (receipted)
- `probes/battery_pilot.py::arm_view` arm B: `{"view": episode["turns"][:cut_point] + [substrate or ""], "fact_available": episode["fact"] in (substrate or ""), "source": "substrate"}` — the record appended RAW.
- `probes/battery_luna.py` current prompt (quoted): `"You are answering a recall probe. Given the context below, answer the question with the exact answer value and nothing else.\n\nCONTEXT:\n" + "\n".join(view["view"][-10:]) + "\n\nQUESTION: " + q + "\nANSWER:"`.
- Measured (`CONFIRMATION-CYCLE-LUNA-20261119.md` §1a): R1 B 19/40 = 0.475; R2 B 23/40 = 0.575; C 29/40 = 0.725; A 0/40. B−A = 47.5/57.5 pts; 0.85×C = 0.61625; both B below → INCONCLUSIVE twice. The gap = the missing extraction-to-notes step (L-1 §1 arm B: "compaction + extraction-to-notes + retry gating + release-point gate").

## 1. THE RESHAPED BRIDGED ARM (retriever spec)
**N1 — note construction (one deterministic rule, verbatim):** For each record entry `e`, the governor finds the plant marker `"PLANTED: "`. If found at index `i`, the note `n(e)` is the substring of `e` from `i+len("PLANTED: ")` up to the first whitespace at or after that index (the first whitespace-delimited token after the marker). If the marker is absent, `n(e) = e`. The note is emitted as the single line `n(e)`, byte-identical to that substring — no case fold, no whitespace normalization, no paraphrase, no added tokens. Pilot class (`e = "PLANTED: {fact} is the answer key"`): `n(e) = "{fact}"`.

**P1 — placement:** the note is the last line of the context, after the truncated turns, immediately before the QUESTION — the same slot the raw append held; the delta is that it is the extracted note, not the raw entry.

**F1 — framing (prompt template delta; current template quoted in §0):** the reshaped template splits the view into context and note and inserts one frame line:
```
You are answering a recall probe. Given the context below, answer the question with the exact answer value and nothing else.

CONTEXT:
{episode["turns"][:cut_point] joined by "\n"}

RECORD NOTE (the governor's extract from the durable record):
{note}

QUESTION: {q}
ANSWER:
```
Delta named: (i) view split into truncated context + note; (ii) the `RECORD NOTE (...)` frame line inserted; (iii) the note is the N1 extract, not the raw entry. The instruction line and the `ANSWER:` suffix are unchanged.

**Untouched:** the classifier (C5a/ANSWERED, R/H/E/A, EHQ projection, empty_reason split), the F1/F2/F3a/F3b checks, the audience field, the decision rule, the episode machinery, the gate/witness. The pre-committed rule is NOT re-opened.

**Reversibility (every add):** one presentation flag `RESHAPED_NOTE` (default `False`). Flag off → the old view (raw append) and the old template; rollback = the old view. Zero substrate change: the record, witness, gate, and F-checks are untouched; the flag lives in the battery's view construction only.

## 2. PILOT RUN PROTOCOL (costed inside $25.28)
- **Scale:** 20 episodes/arm × 3 arms (seeds 0–19 of the same 40-episode construction; `make_episode` unchanged). A 20 + B′ 20 paid at $0.467/exec = 40 × 0.467 = **$18.68**; C 20 free. Remaining room $25.28 − $18.68 = **$6.60** (two-way door: 10/arm = $9.34 is the fallback if the budget tightens).
- **Comparison:** B′ vs the banked R1/R2 B baseline — the same seeds' rows in `BATTERY-LUNA-LEDGER-20261119.json` / `-R2.json` (schema: `episodes[]` with `arm/episode/class/matches/empty_reason/rhea/eahq/correct/f1/f2/f3b/f3b_reason/audience`). Report B′−A, B′/C, and B′ vs banked B (paired by seed).
- **Rule re-computed on the pilot's arms** (A, B′, C at 20/arm): CERTIFY iff B′−A ≥ 20 AND B′ ≥ 0.85×C; FALSIFY iff B′−A < 20 OR (B′ < 0.85×C AND B′ ≤ A); INCONCLUSIVE iff judge control fails OR cache logging missing OR C−A < 5 OR mean(F3b) < 1 on answered-from-record episodes.
- **Verdict line + two-way door:** a B′ gain toward C opens the full-run extension (40/arm, the remaining budget); no gain = the reshape joins the dead-end registry's candidates — a finding, never a repeat.

## 3. FALSE-POSITIVE GUARD (the reshape must not be a prompt-cheat)
**GUARD (verbatim):** Every string in the note must be a byte-substring of (a) one of the record's entries or (b) the episode's planted fact. No paraphrase, no case fold, no whitespace normalization, no added tokens, no reordering. The frame line (`RECORD NOTE (...)`) is template text, not note content; it carries no fact tokens and is not scored. A note that fails the substring check is a hard abort of the pilot (the run is void, not read).
- **Theater-check:** if B′ ≥ C (not merely ≥ 0.85×C), flag a presentation-artifact suspect and require a second-eyes pass before the full-run extension — the confirmation's theater-check class (§1d).

## 4. PRE-COMMITTED RULE'S APPLICATION (pilot verdict shape)
Applied to the pilot's arms; the pilot's verdict is the reshape's gate. Numbers land with the run; the shape is fixed here.
- CERTIFY: B′−A ≥ 20 AND B′ ≥ 0.85×C → full-run extension opens.
- FALSIFY: B′−A < 20 OR (B′ < 0.85×C AND B′ ≤ A) → reshape dead-ended.
- INCONCLUSIVE: judge control fails / cache logging missing / C−A < 5 / mean(F3b) < 1 on answered-from-record episodes → QUESTION, not a stop (wall clause).

## 5. COMPOSE-CHECK TABLE (8 steps)
| # | Step | Evidence / receipt |
|---|---|---|
| 1 | Read the seed gap (arm B raw append + prompt) | `battery_pilot.py::arm_view`; `battery_luna.py` prompt (quoted §0) |
| 2 | Read the hold-contract | `CONFIRMATION-CYCLE-LUNA-20261119.md` §3 (machinery reusable as-is) |
| 3 | Read the banked baseline + schema | both ledgers' `episodes[]` rows; §1a numbers |
| 4 | Specify N1 (extraction-to-notes) | L-1 §1 arm B spec (via brief); byte-substring guard |
| 5 | Specify P1 + F1 (placement + framing) | current template quoted; delta named |
| 6 | State the false-positive guard | §3 verbatim; theater-check §1d |
| 7 | Cost the pilot inside $25.28 | ledger `cost` rows (0.467/exec); 40 × 0.467 = 18.68 |
| 8 | Apply the pre-committed rule + two-way door | `battery_luna.py::decide`; rollback = flag off |

**Storm-context corroboration (class, not adoption):** the reshape is a read-path presentation change (DISCERN's SPA-DREAM read path; write-gate L0 stays); the note is a read-side evidence card with a substring verifier (SELD's read-side evidence-plane verifier class); the extraction is a memory-economy distillation (MemCredit's arbitration class); the guard is evidence-gated admission + compile-time gating (AskALCF / the misc); the pilot is a design-space probe with an adaptive scale envelope (MAPE / Reward-Driven Collider); the note's verbatim-substring fidelity is an L2 selection (CoMem). Design stays ours.

**Loop-state:** `HOLD-AT-APEX → RETRIEVER-RESHAPE designed (copycat lane); the head wires N1/P1/F1 behind the flag and writes the run.`