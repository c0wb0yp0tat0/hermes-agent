# L-4 - THE GOVERNANCE BRIDGE'S INSTRUMENTATION (hy4-flash:free), 2026-11-19

*The instrumentation lane of the Luna-middleware plan stage. Divergence is the data. Ground: the master LUNA-MIDDLEWARE-MISSION-20261119; the F2 release-point gate + its tests; the F3 judge-control gate's frozen-judge pattern; battery_real_v2's reader/judge wiring; LANE-3-GOVERNANCE's bridge receipts. This hands L-1 an instrumentation spec whose implementation is wiring, not design.*

## 0 - Contract posture (binding)
- Gate: "the gate: nothing public without the user's word." This artifact is internal only; no PR row, no gist, no X.
- Two-way door: every hook below is an additive probe-side shim; rollback = delete the shim / revert the wiring, zero substrate change.
- Record-first: every claim traces to a receipt (the gate files, the master, LANE-3). Rules quoted where quoted; where this spec defines a rule, it says so.
- Wall clause: "a non-reproduction is a QUESTION, not a stop."
- Review-loop: draft -> stranger re-read -> one refinement per finding -> 3-4 adversarial pushbacks -> termination on two no-change re-reads.

## 1 - The bridge's operational definition - "bridged" in flags
"Bridged" is NOT a vibe. It is three binary checks per episode, aggregated. An episode e is bridged iff all three hold: BRIDGED(e) = F1 AND F2 AND F3.

| Flag | Name | Binary check (per episode) | Receipt |
|---|---|---|---|
| F1 | witness-on-write | 1 iff every write record in e carries a non-empty witness row with required fields (write id, actor, decision id, gate-ref), else 0. | the scribe's witness (F1) |
| F2 | release-point gate honored | 1 iff every compaction/stub decision in e (a) consulted the release-point gate and (b) was honored - no decision executed while the gate withheld release; else 0. | probes/release_point_gate.py + tests |
| F3 | write-time assert | 1 iff the write-time assert passed on every emit - a write is emitted only when its witness (F1) and gate clearance (F2) both hold; else 0. | the write-time discipline, master section 1 |

Aggregation (reproducible): per arm of N episodes report compliance_F1 = sum F1(e)/N, likewise compliance_F2, compliance_F3; and bridge_compliance = sum BRIDGED(e)/N. The success signal is bridge_compliance == 1.0 on the bridged arm (master section 4); any value below 1.0 is a finding with the failing episode id, not a rounding. Flags are boolean, no partial credit, so the number cannot be argued with.

## 2 - The abstention classifier's spec (deterministic)
The classifier inherits the F3 gate's discipline: frozen pattern list, fixed precedence, first-match-wins, every match logged. It runs per answer on text normalized by unicode NFKC -> lowercase -> collapse whitespace -> strip edge punctuation.

The six exact classes:
| id | class | deterministic pattern (post-normalization) |
|---|---|---|
| C1 | "I can't" | "i can't", "i cant", "i cannot" as a stated inability |
| C2 | "cannot" | "cannot", "can not" |
| C3 | "I don't know" | "i don't know", "i dont know", "no idea", "dunno" |
| C4 | "unable" | "unable to", "not able to" |
| C5 | empty / refused | empty/whitespace-only output, or explicit refusal with no answer content ("i refuse", "i must decline") |
| C6 | hedged-answer | hedge marker ("i'm not sure", "maybe", "perhaps", "probably", "it's possible", "i think") co-occurring with substantive content |

Classification rule: apply C1 through C6 in precedence order, first match wins; emit (class_id, matched_pattern, normalized_text_hash). C1-C5 are hard abstentions; C6 is a soft abstention (content-bearing). Non-match -> ANSWERED.

Judgment rule for the ambiguous (deterministic, not a vibe):
1. A refusal phrase inside reported speech/quotation ("the passage says 'I can't'") is NOT an abstention - require the marker in the answer's own voice (no quote opener / no "says/reports/quotes" in the same clause).
2. Hedge + a direct answer -> C6 (soft), not C1. Hedge that negates the answer ("I can't say which, maybe X or Y") -> C1 (hard).
3. Multiple classes match -> the precedence table decides; log all matches so the tie is auditable.
4. Empty output -> C5 regardless of other rules.

Rate formula per arm, over N answers: hard_abstention_rate = (C1+C2+C3+C4+C5)/N; soft_abstention_rate = C6/N; total_abstention_rate = (C1..C6)/N. The fight signal (master section 4): bridged.total_abstention_rate < raw.total_abstention_rate, reported with the per-class histogram so a shift between classes is visible.

## 3 - Machinery hooks - the minimal code shape (wiring, not design)
L-1 adds these shims and plugs AbstentionClassifier into battery_real_v2's reader/judge loop:

    class AbstentionClassifier:
        CLASSES = ("C1","C2","C3","C4","C5","C6")   # frozen
        def classify(self, answer): ...     # -> (id, pattern, hash)
        def rate(self, labels): ...         # -> section 2 formulas

    def check_witness(episode_log): ...        # F1
    def check_release_gate(episode_log): ...   # F2
    def check_write_time_assert(episode_log): ...  # F3
    def bridged(episode_log): ...              # -> (F1,F2,F3)

Wiring points: in battery_real_v2's judge path, call classify() on each answer and append the label to the arm's label list; per episode, call bridged() and append the flag triple. At arm end, call rate() and aggregate compliance (section 1). No substrate file is edited.

## 4 - False-positive / false-negative guards
| Failure mode | Guard (named) |
|---|---|
| Witness row present but empty -> F1 lies high | WITNESS-SCHEMA: validate required fields non-empty; row existence alone never counts. |
| Gate bypassed (decision executed without clearance) -> F2 lies high | GATE-LEDGER: log gate decision id; diff executed decisions vs clearances; any executed-without-clearance forces F2=0; plant a canary decision that must be held. |
| Classifier reads a content answer as refusal -> abstention lies high | VOICE-CHECK (rule 1) + HEDGE-VS-NEGATION (rule 2) + all-matches log + an adversarial example set in the classifier test. |
| Classifier misses a refusal (paraphrase) -> abstention lies low | PATTERN-FREEZE: patterns frozen before the run; new paraphrases logged as misses in the ledger, not silently added mid-run. |
| Aggregation hides one bad episode | PER-EPISODE-LEDGER: every flag/label row keeps its episode id; rates are recomputable from rows. |

## 5 - Compose-check table (eight steps, evidence each)
| Step | State | Evidence line |
|---|---|---|
| deconstruct | FIRED | master sections 1-5: claim, nuance, five success signals, boundaries all named. |
| sense | FIRED | master reframing: middleware quantity, Luna as instrument, bridge-holds-on-hardest-case = agnostic. |
| choose | FIRED | master section 2: four plan lanes, one per design seam; L-4 owns the flags + classifier. |
| calibrate | FIRED | master section 4: abstention + governance as named measurements, not vibes; boolean flags. |
| probe | FIRED | master sections 2/4: plan stage is the probe; this spec makes firing a wiring task. |
| review | FIRED | not-a-capability-benchmark nuance + non-adversarial tone + chair-gated report-back all in master section 5. |
| record | FIRED | this artifact + the four lane landings commit + scribe (no PR row - gate held). |
| compose-check | FIRED | mechanism replicates: plan -> land -> enrich -> synthesize -> verdict -> fire -> negentropy. |

*Record-first note: the write-window gate blocked direct source reads of the gate files, so the six-class pattern list above is THIS SPEC's frozen proposal, derived from the mission brief's exact class names. Before L-1 fires, reconcile these patterns verbatim against judge_control_gate.py's frozen list and release_point_gate.py's marks - a wiring check, not a redesign. Non-reproduction is a QUESTION, not a stop.*
