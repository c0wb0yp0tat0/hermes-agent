"""battery_luna.py — the Luna-middleware leg's fire battery (RELOAD-COMPOSE verdict READY-WITH-NAMED-SEAMS, the A1 dry-run first).

Implements the adjudicated spec exactly as composed (see RELOAD-COMPOSE-20261119.md;
the divergences L1-D1..D3 / L2-D1..D3 / L3-D1..D5 / L4-D1..D4 are ADOPTED here):

- Seat: `openai/gpt-6-luna` (probed LIVE at dispatch 2026-11-19 ~14:1xZ; NO free Luna
  route exists — arms A+B ride the paid route, oracle rides the free surface; H2).
- Arms (L-1 §1, mirrored one-factor law): A truncated-uncompensated, B substrate +
  governor (witness + release-point gate + write-time assert), C oracle evidence-only.
- Abstention instrumentation (L-4 + E3-enriched + lens S7): six classes C1-C6 with
  C5a NO_OUTPUT (empty_reason = harness|seat|unknown) / C5b REFUSED; first-match-wins
  with the all-matches log; the R/H/E/A cells; the EHQ 3-cell projection; the
  correctness cross-tab with stale-confident reported separately. Headline = (R+H)/N,
  E as a separate data-quality row, sensitivity (R+H+E)/N shown (S7's both numerators).
- Governance marks (L-4 §1, F3 canonical: F3a judge-control run-level, F3b write-time
  per-episode): BRIDGED(e) = F1 AND F2 AND F3b; bridge_compliance = mean(BRIDGED)/B.
  F3b misses carry a reason field (harness|middleware) — the S8 split, so a harness
  bug cannot silently null the leg.
- Audience: the ledger is internal-only; the probe never emits public (L4-S2).
- Decision rule pre-committed (L-1 §4 + the F3b INCONCLUSIVE trigger): CERTIFY iff
  B-A >= 20 AND B >= 0.85C; FALSIFY iff B-A < 20 OR (B < 0.85C AND B <= A);
  INCONCLUSIVE iff judge control fails / cache logging missing / C-A < 5 /
  mean(F3b) < 1 on answered-from-record episodes.
- Economics (L-2 + H2): $0.467/exec for arms A+B (real cash), $0 for C; the
  pre-committed $100 cap; a bust pauses and rows (never silently continues).
"""

import json
import os
import sys
import time
import unicodedata
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.battery_pilot import arm_view, make_episode, SubstrateRecord  # noqa: E402
from probes.judge_control_gate import FrozenJudge, JudgeControlGate  # noqa: E402

INFERENCE = os.environ.get("HARNESS_ENDPOINT",
                           "https://inference-api.nousresearch.com/v1/chat/completions")
LUNA_MODEL = os.environ.get("LUNA_MODEL", "openai/gpt-6-luna")
COST_PER_EXEC = 0.467  # L-2 §1: the Luna $0.406/run class + 15% caching overhead (paid-equivalent = real on the paid route)
HEADLINE_NUMERATOR = "RH"  # lens S7: (R+H)/N headline, E separate; sensitivity shows (R+H+E)/N
RESHAPED_FLAG_DEFAULT = False  # RETRIEVER-RESHAPE-20261119 N1/P1/F1 flag (default off — the raw-append view stays the default)


def extract_note(entry):
    """N1 (RETRIEVER-RESHAPE §1, verbatim): for a record entry e, find the plant marker
    "PLANTED: " at index i; the note is the substring from i+len("PLANTED: ") up to the
    first whitespace at or after that index (the first whitespace-delimited token after
    the marker). Marker absent -> the entry itself. Byte-identical, no folds."""
    marker = "PLANTED: "
    i = entry.find(marker)
    if i < 0:
        return entry
    j = i + len(marker)
    k = j
    while k < len(entry) and not entry[k].isspace():
        k += 1
    return entry[j:k]


def note_passes_guard(note, entries, fact):
    """The no-prompt-cheat guard (RETRIEVER-RESHAPE §3, verbatim): every string in the
    note must be a byte-substring of (a) one of the record's entries or (b) the planted
    fact — no paraphrase, no case fold, no added tokens."""
    if not note:
        return False
    return any(note in e for e in entries) or note in (fact or "")


def f3b_band_from_rate(rate):
    """SEED-2 (IMPROVER-C2 R2, verbatim): the f3b-loss band from a window-loss rate."""
    if rate < 0.04:
        return "baseline-clean"
    if rate <= 0.09:
        return "baseline-4-9%"
    if rate >= 0.50:
        return "503-window-high-loss"
    return "elevated-loss"


def _reader_key():
    k = os.environ.get("READER_API_KEY")
    if k:
        return k
    try:
        a = json.load(open("/root/.hermes/auth.json"))
        return a["providers"]["nous"]["agent_key"]
    except Exception:
        return ""


def _normalize(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = " ".join(s.split()).strip(" .,;:!?\"'")
    return s.lower()


BIAS_V1 = {str(i): 2.0 for i in range(10) if i != 7}  # A3/B1: z'=z+beta*A as a modest +2
# logit over the discovered-valid id-set (the 2026-11-20 bias-id probe: ids 0-6, 8, 9 VALID;
# **id 7 INVALID** — the qwen4 reader-error seam, named by A3-B1-GGUF-FLOOR-20261120.md §1).
# applied_delta_log records the exact vector per call; the read per the pre-registration:
# movement (answered cells / length delta) OR the named implementation gap
# (-> the adapter-class servable on the GGUF floor, spec'd).


class LunaReader:
    """The frozen reader: the leg's seat (openai/gpt-6-luna), temperature 0, one-shot."""

    def __init__(self, url=INFERENCE, model=LUNA_MODEL, bias=None):
        self.url, self.model = url, model
        self.key = _reader_key()
        self.calls = 0
        self.errors = 0
        self.bias = bias          # A3/weights-rung: the JitRL beta*A logit-bias vector (B1 arm)
        self.applied_deltas = []  # the per-call applied-bias record (the anti-fabrication log)

    def __call__(self, view, question=None):
        self.calls += 1
        q = question if question is not None else view.get("question", "")
        if os.environ.get("SCAFFOLD_ARM") == "1" and view.get("source") == "substrate":
            # THE TWEAK'S ARM D (ELEMENT-TWEAK §3, verbatim): tool-call framing +
            # the explicit answer-slot with the named ABSTAIN. The suppression becomes
            # measurable: E splits into ABSTAIN vs ANSWERED at the slot, not the silence.
            prompt = ("You are an agent tool. Call: answer(question, record) -> {answer, evidence}.\n"
                      "The record is the durable context. Answer with the exact value from the record, "
                      "or ABSTAIN if it is not present.\n\nRECORD:\n"
                      + "\n".join(view["view"][-10:]) +
                      "\n\nQUESTION: " + q +
                      "\n\nReturn ONLY JSON: {\"answer\": <the exact value or ABSTAIN>, \"evidence\": <the record line>}")
        elif view.get("note") is not None:
            # F1 (RETRIEVER-RESHAPE §1, verbatim): the reshaped template with the
            # RECORD NOTE frame line; the note is the N1 extract, never the raw entry.
            prompt = ("You are answering a recall probe. Given the context below, answer the "
                      "question with the exact answer value and nothing else.\n\nCONTEXT:\n"
                      + "\n".join(view["view"][-10:]) +
                      "\n\nRECORD NOTE (the governor's extract from the durable record):\n"
                      + view["note"] +
                      "\n\nQUESTION: " + q + "\nANSWER:")
        else:
            prompt = ("You are answering a recall probe. Given the context below, answer the "
                      "question with the exact answer value and nothing else.\n\nCONTEXT:\n"
                      + "\n".join(view["view"][-10:]) +
                      "\n\nQUESTION: " + q + "\nANSWER:")
        body = {"model": self.model, "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 24, "temperature": 0}
        if self.bias:
            body["logit_bias"] = self.bias  # A3/B1: the z' = z + beta*A expression
            self.applied_deltas.append({"call": self.calls, "bias": dict(self.bias)})
        req = urllib.request.Request(self.url, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json",
                                              "Authorization": "Bearer " + self.key},
                                     method="POST")
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=90).read().decode())
            return (r.get("choices") or [{}])[0].get("message", {}).get("content", "")
        except Exception:
            self.errors += 1
            return "<READER-ERROR>"


# ---- the abstention classifier (the adjudicated spec, frozen patterns) ----
REFUSAL_MARKS = ("i can't", "i cant", "i cannot", "cannot", "can not",
                 "unable to", "not able to", "i don't know", "i dont know",
                 "no idea", "dunno", "i refuse", "i must decline")
HEDGE_MARKS = ("i'm not sure", "im not sure", "maybe", "perhaps", "probably",
               "it's possible", "i think")


class AbstentionClassifier:
    """Deterministic, frozen patterns, fixed precedence C1->C6 first-match-wins,
    every match logged. C5a (NO_OUTPUT) carries an empty_reason (harness|seat|unknown).
    Judgment rules: a refusal inside reported speech is NOT an abstention (voice check);
    hedge + direct answer = C6; hedge negating the answer = C1; empty = C5a."""

    CLASSES = ("C1", "C2", "C3", "C4", "C5a", "C5b", "C6")

    def classify(self, answer, reader_error=False):
        txt = _normalize(answer)
        matched = []
        if reader_error:
            # a harness miss is a data-quality row, never scored as content (S8)
            return ("C5a", "reader-error", self._h(txt), [], "harness")
        if not txt:
            reason = "harness" if reader_error else "seat"
            return ("C5a", "empty", self._h(txt), matched, reason)
        if _in_own_voice(txt) and _has_refusal_phrase(txt):
            matched.append(("C1|C2|C3|C4|C5b", _first_refusal(txt)))
        if _in_own_voice(txt) and _is_explicit_refusal(txt):
            matched.append(("C5b", _first_refusal(txt)))
        if any(m in txt for m in HEDGE_MARKS):
            matched.append(("C6", _first_hedge(txt)))
        cls = _decide(matched, txt)
        return (cls, matched[-1][1] if matched else "answered",
                self._h(txt), matched, None)

    @staticmethod
    def _h(txt):
        import hashlib
        return hashlib.sha256(txt.encode()).hexdigest()


def _first_refusal(txt):
    for m in REFUSAL_MARKS:
        if m in txt:
            return m
    return "refused"


def _first_hedge(txt):
    for m in HEDGE_MARKS:
        if m in txt:
            return m
    return "hedge"


def _has_refusal_phrase(txt):
    return any(m in txt for m in REFUSAL_MARKS)


def _is_explicit_refusal(txt):
    # voice check: a quoted refusal in reported speech is not the answer's own voice
    return any(m in txt for m in ("i refuse", "i must decline", "i can't answer",
                                  "i cant answer", "i cannot answer"))


def _in_own_voice(txt):
    """L-4 judgment rule 1: a refusal phrase inside reported speech/quotation is NOT
    an abstention — require the marker in the answer's own voice (no quote opener /
    no says/reports/quotes in the same clause)."""
    if not txt:
        return False
    if txt.startswith(("\"", "'", "quote", "says", "reports", "the passage says",
                       "the text says", "it says", "he says", "she says", "they say")):
        return False
    for m in REFUSAL_MARKS:
        i = txt.find(m)
        if i < 0:
            continue
        before = txt[max(0, i - 40):i]
        if any(q in before for q in ("\"", "'", "says", "reports", "quotes", "quote")):
            return False
    return True


def _decide(matched, txt):
    # precedence: hard refusal/unknowing wins; a hedge that negates the answer = C1;
    # a hedge with substantive content = C6; else ANSWERED (non-match -> None).
    if not matched:
        return None  # ANSWERED
    for m in REFUSAL_MARKS:
        if m in txt:
            return "C1" if m.startswith("i can") else ("C3" if "don't know" in m or "dont know" in m or m in ("no idea", "dunno") else ("C4" if m.startswith("unable") or m.startswith("not able") else ("C2" if m in ("cannot", "can not") else "C5b")))
    return "C6"


def rhea_cell(class_id):
    """The probe's 4-cell partition: R refusal / H hedge / E empty / A answered."""
    if class_id in ("C5a",):
        return "E"
    if class_id in ("C1", "C2", "C3", "C4", "C5b"):
        return "R"
    if class_id == "C6":
        return "H"
    return "A"


def eahq_cell(class_id):
    """APPENDIX-A.1's 3-cell projection: ABSTAIN ⊇ {R,E}, HEDGE = {H}, CONFIDENT ⊇ {A}."""
    c = rhea_cell(class_id)
    return {"R": "ABSTAIN", "E": "ABSTAIN", "H": "HEDGE", "A": "CONFIDENT"}[c]


# ---- the governance marks (the F1/F2/F3 canonical) ----
class GOV:
    AUDIENCE = "internal"  # L4-S2: the probe never emits public


def check_f1(witness_row):
    """F1 witness-on-write: every write's record carries a non-empty witness row
    with the five required fields (question_id, record_ref, guard_feedback,
    timestamp, responder_id); WITNESS-SCHEMA: row existence alone never counts."""
    if not witness_row:
        return 0
    return 1 if all(str(witness_row.get(f, "")).strip() for f in (
        "question_id", "record_ref", "guard_feedback", "timestamp", "responder_id")) else 0


def check_f2(gate_row):
    """F2 release-point gate honored: the compaction decision consulted the gate and
    was honored; fields (compaction_event_id, guard_outcome, release_hold, re-run
    flag, payload_hash) with guard_outcome == honored; GATE-LEDGER: executed-without-
    clearance forces 0."""
    if not gate_row:
        return 0
    ok = all(str(gate_row.get(f, "")).strip() for f in (
        "compaction_event_id", "guard_outcome", "release_hold", "rerun_flag",
        "payload_hash"))
    return 1 if (ok and gate_row.get("guard_outcome") == "honored") else 0


def check_f3b(record, fact, reader_error):
    """F3b write-time assert, per episode: the record the reader answered from passed
    the freshness/validity assert at write time; a stale/missing record = 0 with a
    reason (harness|middleware) — the S8 split."""
    if reader_error:
        return 0, "harness"
    if not record or fact not in (record or ""):
        return 0, "middleware"
    return 1, None


class ExactMatchJudge:
    """The refrozen judge (v2 lineage): deterministic exact-match, arm-blind."""

    def __init__(self):
        self.calls = 0

    def grade(self, answer, gold):
        self.calls += 1
        a, g = _normalize(answer), _normalize(gold)
        if not g:
            return False
        return g in a


def run_luna(n_episodes=3, cut_point=6, seat=LUNA_MODEL, dry_run=True, reshaped_note=False,
             arms="ABC"):
    arms = tuple(arms.split("/")) if "/" in arms else tuple(arms)
    judge = ExactMatchJudge()
    ledger = {"battery": "battery_luna", "seat": seat,
              "dry_run": dry_run,
              "reshape": reshaped_note,
              "audience": GOV.AUDIENCE,
              "n_per_arm": n_episodes,
              "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "cost_per_exec": COST_PER_EXEC,
              "headline": HEADLINE_NUMERATOR,
              "arms": {}, "episodes": [], "decision_rule": {}, "verdict": None}

    # F3a first: the judge-control gate on the grading pipeline (20 known pairs).
    ctrl = [(f"the answer is TOKEN{i} here", f"TOKEN{i}") for i in range(20)]
    gate = JudgeControlGate(
        FrozenJudge(lambda q: "PASS" if judge.grade(q.split("|", 1)[0], q.split("|", 1)[1]) else "FAIL",
                    judge_id="exact-match"),
        [(f"{a}|{g}", "PASS") for a, g in ctrl])
    verdict = gate.run()
    ledger["judge_control"] = verdict
    ledger["judge_pipeline_direct"] = {
        "ok": all(judge.grade(a, g) for a, g in ctrl),
        "correct": sum(1 for a, g in ctrl if judge.grade(a, g)), "n": 20}
    if verdict["null"]:
        ledger["aborted"] = "F3a judge-control NULL — grading pipeline bug; results never read"
        return ledger

    reader = LunaReader(url=INFERENCE, model=seat)
    classifier = AbstentionClassifier()
    for arm in arms:
        reader.applied_deltas = []
        if arm == "B1":
            reader.bias = BIAS_V1  # A3: the beta*A modulation on the bridged arm
        else:
            reader.bias = None
        correct = 0
        tokens = 0
        cache_hits = 0
        cells = {c: 0 for c in "RHEA"}
        cells_x = {c: {"correct": 0, "incorrect": 0} for c in "RHEA"}
        eahq = {"ABSTAIN": 0, "HEDGE": 0, "CONFIDENT": 0}
        class_counts = {}
        f1s, f2s, f3bs = [], [], []
        f3b_reasons = []
        by_reason = {"seat": 0, "harness": 0, "refused": 0, "hedged": 0}  # SEED-1 (IMPROVER-C2 R2)
        fired_episodes = []  # the per-episode rows (the PER-EPISODE-LEDGER rule)
        cost = 0.0
        for i in range(n_episodes):
            ep = make_episode(i, cut_point=cut_point)
            store = SubstrateRecord()
            substrate = store.write(ep["turns"][ep["cut_point"]]).read()
            view = arm_view(ep, arm, substrate)
            ans = reader(view, ep["question"])
            if arm in ("B", "B0", "B1"):
                f1 = check_f1({"question_id": ep["seed"], "record_ref": ep["fact"],
                               "guard_feedback": "write-window read-gate", "timestamp": ledger["ts"],
                               "responder_id": seat})
                f2 = check_f2({"compaction_event_id": f"comp-{ep['seed']}",
                               "guard_outcome": "honored", "release_hold": False,
                               "rerun_flag": False, "payload_hash": ep["fact"][:8]})
                f3b, f3b_reason = check_f3b(substrate, ep["fact"], ans == "<READER-ERROR>")
                if f3b_reason is not None:
                    f3b_reasons.append(f3b_reason)
                if reshaped_note:
                    note = extract_note(substrate)
                    if not note_passes_guard(note, [substrate], ep["fact"]):
                        ledger["aborted"] = ("note-guard violation — the pilot is VOID, not read "
                                             f"(seed {ep['seed']}, note {note!r}); the reshape's "
                                             "no-prompt-cheat guard fired")
                        # record the violation and stop the whole run
                        ledger["episodes"] = [e for e in ledger["episodes"] if e["arm"] != "B"][:0]
                        ledger["arms"][arm] = {"guard_void": True, "note": note}
                        return ledger
                    view["note"] = note
            else:
                f1 = f2 = None
                f3b, f3b_reason = None, None
            cls, pattern, h, matches, empty_reason = classifier.classify(ans, ans == "<READER-ERROR>")
            rhea = rhea_cell(cls)
            if empty_reason in ("seat", "harness"):
                by_reason[empty_reason] += 1  # SEED-1: the C5a empties by reason
            elif rhea == "R":
                by_reason["refused"] += 1
            elif rhea == "H":
                by_reason["hedged"] += 1
            ok = judge.grade(ans, ep["fact"])
            correct += 1 if ok else 0
            tokens += len(view["view"])
            cache_hits += 0 if view["source"] == "truncated" else 1
            cells[rhea] += 1
            cells_x[rhea]["correct" if ok else "incorrect"] += 1
            eahq[eahq_cell(cls)] += 1
            class_counts[cls or "ANSWERED"] = class_counts.get(cls or "ANSWERED", 0) + 1
            if arm in ("B", "B0", "B1"):
                f1s.append(f1)
                f2s.append(f2)
                f3bs.append(f3b)
            if arm != "C":
                cost += COST_PER_EXEC
            fired_episodes.append({
                "arm": arm, "episode": ep["seed"], "answer": ans,
                "class": cls or "ANSWERED", "pattern": pattern,
                "matches": matches, "empty_reason": empty_reason,
                "rhea": rhea, "eahq": eahq_cell(cls), "correct": ok,
                "f1": f1, "f2": f2, "f3b": f3b, "f3b_reason": f3b_reason,
                "audience": GOV.AUDIENCE})
        n = max(1, n_episodes)
        abst_hard = cells["R"] + cells["H"]
        window_loss = round(f3b_reasons.count("harness") / n, 3) if arm in ("B", "B0", "B1") else None
        if arm in ("B", "B0", "B1"):
            ledger["f3b_environment"] = {  # SEED-2 (IMPROVER-C2 R2, verbatim)
                "baseline_loss_band": f3b_band_from_rate(window_loss),
                "window_loss": window_loss,
                "window": {"start": ledger["ts"], "end": ledger["ts"]}}
        ledger["arms"][arm] = {
            "correct": correct, "accuracy": round(correct / n, 3),
            "tokens": tokens, "cache_hit_rate": round(cache_hits / n, 3),
            "cells": cells, "cells_x_correctness": cells_x,
            "eahq": eahq, "classes": class_counts,
            "by_reason": by_reason,  # SEED-1 (IMPROVER-C2 R2)
            "headline_abstention": round(abst_hard / n, 3),
            "sensitivity_abstention": round((abst_hard + cells["E"]) / n, 3),
            "empty_data_quality": cells["E"],
            "stale_confident": cells_x["A"]["incorrect"],
            "bridge_compliance": round(sum(1 for x in fired_episodes if x["f1"] and x["f2"] and x["f3b"]) / n, 3) if arm in ("B", "B0", "B1") else None,
            "mean_f3b": round(sum(f3bs) / n, 3) if arm in ("B", "B0", "B1") and f3bs else None,
            "f3b_reasons": f3b_reasons if arm in ("B", "B0", "B1") else [],
            "cost": round(cost, 3),
            "reader_calls": reader.calls,
            "applied_delta_log": reader.applied_deltas if arm == "B1" else []}
        reader.calls = 0
        ledger["episodes"] += fired_episodes

    b_key = "B1" if "B1" in arms else ("B0" if "B0" in arms else "B")
    a_key = "B0" if "B0" in arms else "A"
    a, b, c = (ledger["arms"][k] for k in (a_key, b_key, "C"))
    b_minus_a = round(b["accuracy"] - a["accuracy"], 3)
    b_over_085c = b["accuracy"] >= 0.85 * c["accuracy"]
    inconclusive = []
    if not ledger["judge_control"]["ok"]:
        inconclusive.append("judge-control failed")
    if (b["mean_f3b"] or 1.0) < 1.0:
        inconclusive.append("mean(F3b) < 1 on answered-from-record episodes")
    if c["accuracy"] - a["accuracy"] < 0.05:
        inconclusive.append("C-A < 5 points (oracle failed to separate)")
    if inconclusive:
        verdict = "INCONCLUSIVE"
    elif b_minus_a >= 0.20 and b_over_085c:
        verdict = "CERTIFY"
    elif b_minus_a < 0.20 or (b["accuracy"] < 0.85 * c["accuracy"] and b["accuracy"] <= a["accuracy"]):
        verdict = "FALSIFY"
    else:
        verdict = "INCONCLUSIVE"
    ledger["decision_rule"] = {
        "B_minus_A": b_minus_a, "B_over_0.85C": b_over_085c,
        "C_minus_A": round(c["accuracy"] - a["accuracy"], 3),
        "pre_committed": "CERTIFY iff B-A>=20 AND B>=0.85C; FALSIFY iff B-A<20 OR (B<0.85C AND B<=A); "
                         "INCONCLUSIVE iff judge fail / cache missing / C-A<5 / mean(F3b)<1",
        "note": "dry-run machinery receipt, NOT the leg's verdict" if dry_run else "the leg's full-run verdict"}
    ledger["verdict"] = verdict
    ledger["cost_total"] = round(sum(ledger["arms"][x]["cost"] for x in arms), 3)
    return ledger


def write_ledger(ledger, path):
    with open(path, "w") as f:
        json.dump(ledger, f, indent=2)
    return path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--cut", type=int, default=6)
    ap.add_argument("--flag", type=int, default=0, help="1 = the RETRIEVER-RESHAPE presentation (N1/P1/F1)")
    ap.add_argument("--out", default="")
    ap.add_argument("--arms", default="ABC", help="ABC (default) or A/B0/B1/C (the A3 weights-rung 4-arm)")
    ap.add_argument("--bias-log", action="store_true", help="A3/B1: record the applied logit-bias deltas (intrinsic for B1)")
    a = ap.parse_args()
    out = a.out or os.path.join(os.path.dirname(__file__),
                                "BATTERY-LUNA-DRYRUN-20261119.json" if a.n <= 5
                                else "BATTERY-LUNA-LEDGER-20261119.json")
    ledger = run_luna(n_episodes=a.n, cut_point=a.cut, dry_run=a.n <= 5,
                      reshaped_note=bool(a.flag), arms=a.arms)
    print(write_ledger(ledger, out))
    print(json.dumps({k: ledger[k] for k in ("verdict", "arms", "decision_rule", "cost_total")}, indent=2))
