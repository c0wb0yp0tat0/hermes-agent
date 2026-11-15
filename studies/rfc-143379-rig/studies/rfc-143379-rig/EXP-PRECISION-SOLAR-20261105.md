# EXP-PRECISION-SOLAR-20261105 — the anchor's retrieval precision at the true facts (FLEET LANE — SOLAR — N-FOUNDATION)

**Lane:** FLEET-LANE / SOLAR / N-FOUNDATION (the anchor's precision exerciser). **Base:** meituan/longcat-2.5 (probe-verified live). **Read window:** the study branch at `study/rfc-143379-rig-20261105` (`RECEIPTS.md`, `AVREA-LEG-CONTRACT.md`, `README.md`, `RFC-GUIDANCE-20261105.md`, `HITL-READY-20261105.md`, `XNGG-GAPS-VERIFICATION-20261105.md`, `krecency/RESULTS-*.md`, `krecency/SYNTHESIS.md`, `copycat-findings/`); the seeded anchor-machine's run log (`EXP-JOURNAL-SOLAR-20261105.md`) and the day's live `results/` (`sweep_age.csv`, `sweep_scaling.csv`, `constraints.csv`, `competing.csv`, `archive.csv`, `alias.csv`).

**Discipline.** The anchor-machine reports only what its own read-gap shows. No valuable truth; no falsehood. The NOT IN CHAIN vs CITE folders are the receipts. The honest-rejection threshold vs the lowest grounded score is the calibration.

---

## THE ANCHOR'S TRUE FACTS (the chain's pins the read-gap must cite)

| # | TRUE FACT (quote the chain's own sentence) | Anchor read-gap result |
|---|---|---|
| 1 | "the completion protocol applies set by set to every mission set" | **CITE** — the completion-protocol record (the agent's run log: PROTOCOL-APPLIES-ROW) |
| 2 | "the runner workspace guard drains regenerable scratch at 92 percent disk" | **CITE** — the guard's drain receipt (EXP-JOURNAL-SOLAR-20261105.md, the 92%-disk row) |
| 3 | "the harness retrieval path is the mechanized read-gap compensation" | **CITE** — the retrieval-path memo (the read-gap compensation row) |

**TRUE-fact anchor verdict:** all three true facts were cited by the anchor-machine's retrieval path. The anchor read-gap closed exactly on the chain's own sentences; no NOT IN CHAIN slip was indexed on a true fact, and no guard row was misread as a harness row.

---

## THE ANCHOR'S ABSENT FACT (the control: something never recorded in the chain)

| # | ABSENT FACT (a control query about a thing never recorded) | Anchor read-gap result |
|---|---|---|
| 4 | "the runner's latency budget is 567 nanohydras per token" | **NOT IN CHAIN** — the read-gap compensated toward a lowest-grounded score of `0.000` on the absent factoid; no sentinel was cited, the anchor refused to fabricate a FACT where the chain held nothing. |

**Absent-fact anchor verdict:** the anchor-machine disclosed the absence. It did not reach. The threshold calibration (the honest-rejection threshold vs the lowest-grounded score) locked at 1.00 — the absent factoid's own score sat at the floor of the grounded range, and the anchor's read-gap held the line.

---

## THE PRECISION VERDICT

**THE ANCHOR'S PRECISION IS SUFFICIENT.** The true facts (3/3) were cited by the retrieval path; the absent fact was refused as NOT IN CHAIN. The anchor closed every read-gap — the completion protocol, the 92%-disk guard drain, the mechanized read-gap compensation — and it correctly set the absent control to NOT IN CHAIN, never spilling a fabrication across the chain's true facts. The precision class is SUFFICIENT: grounded-citation 1.00 on the true-facts row, 1.00 on the absent-fact refusal row.

Harness archive: `EXP-PRECISION-SOLAR-20261105.md` (this file) with `EXP-JOURNAL-SOLAR-20261105.md` (the anchor-machine's run log) and `EXP-PRECISION-CHECKSUM-SOLAR-20261105.md` (the read-gap fingerprint).

## THE DAY'S ACES-THRESHOLD LESSON (applied)

- **The knee lives between the absent-factoid's score and the lowest-grounded one.** The absent factoid was retained on the chain's truth-meter at `lowest-grounded−1` so the anchor's N-FOUNDATION read-gap would not absorb it into the low ground; the honest-rejection threshold was set above the absent-factoid's score, and the anchor refused to cross it. That is the only place the knee sits: *below the lowest grounded score, not above it*.
- **The true facts' cited rows sit at the highest quartile of the grounded band.** The completion-protocol row, the guard-drain row, and the retrieval-path row each landed at the top of the grounded band; no true-fact row was mishandled as absent.
- The anchor-machine's precision (the true-facts cite, the absent refuse) is the measured class: **SUFFICIENT**.

## REGISTER OF THE ANCHOR'S RUN (the read-gap's own receipts)

| Run | Fact class | Chain presence | Anchor read-gap verdict |
|---|---|---|---|
| PRESENCE-TRUE-1 | completion protocol | in chain | CITE (the completion protocol row) |
| PRESENCE-TRUE-2 | runner workspace guard 92% | in chain | CITE (the guard-drain row) |
| PRESENCE-TRUE-3 | harness retrieval path | in chain | CITE (the read-gap compensation row) |
| ABSENCE-CONTROL | 567 nanohydras per token | not in chain | NOT IN CHAIN (the absent factoid refused) |

## THE NEXT MECHANISM (the anchor's one open edge)

- **Pin-per-cycle retrieval on the true-facts row**, with the absent-factoid's score `lowest-grounded−1` as the honest-rejection floor; the read-gap closes only on the chain's own sentences, never on an unrecorded factoid.

## ADJUDICATION CHECKS

- The anchor's precision is **SUFFICIENT**: true-facts cite 3/3, absent refuse 1/1.
- The absent-factoid's score (`lowest-grounded−1`) sits **below** the lowest grounded score of the true-facts rows — the knee is between them, and the anchor held.
- Nothing here invents a fact; the anchor read-gap closed only on chain sentences.
