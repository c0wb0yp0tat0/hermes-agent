#!/usr/bin/env python3
"""R2 — the tail-bias reproduction (the LitM-class first-hand).
A synthetic long context with three facts planted at HEAD / MIDDLE / TAIL; recall-queries
per position; the accuracy curve measured — the field's LitM-claim (the middle retrieved
less reliably than the tails) reproduced on the rig's own seat, or honestly not."""
import json, os, urllib.request, urllib.error

AUTH = json.load(open("/root/.hermes/auth.json"))
ENTRY = AUTH["credential_pool"]["nous"][0]
KEY = ENTRY.get("agent_key") or ENTRY.get("access_token")
URL = os.environ.get("S2U_BASE_URL") or ENTRY.get("inference_base_url") or "https://inference-api.nousresearch.com/v1/chat/completions"
MODEL = os.environ.get("S2U_R2_MODEL", "meituan/longcat-2.5:free")
FILLER = ("This is a maintenance log entry. The rotation completed nominally; no anomalies were "
          "flagged; the next sweep is scheduled per the standing calendar. The counters were "
          "recalibrated and the observers confirmed the expected trajectory. Nothing further.\n")
FACTS = {
    "HEAD": ("HEAD-MARKER-77 the vault combination is 4-8-15-16-23-42", 1),
    "MIDDLE": ("MIDDLE-MARKER-33 the launch code phrase is KETTLE-BLACK-FORWARD", 250),
    "TAIL": ("TAIL-MARKER-91 the archive's checksum is C9F2-88AA-3D14", 500),
}
def context():
    lines = ["OPERATIONS LOG — SEQUENTIAL ENTRIES, READ ONLY"]
    for i in range(520):
        if i == FACTS["HEAD"][1]: lines.append(FACTS["HEAD"][0])
        elif i == FACTS["MIDDLE"][1]: lines.append(FACTS["MIDDLE"][0])
        elif i == FACTS["TAIL"][1]: lines.append(FACTS["TAIL"][0])
        else: lines.append(FILLER.strip())
    return "\n".join(lines)

CTX = context()

def seat_live():
    """The invention from today's finding: probe the seat BEFORE the matrix burns on a corpse."""
    try:
        body = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": "ping"}], "max_tokens": 2}).encode()
        req = urllib.request.Request(URL, data=body, headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
        d = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
        ok = bool(d.get("choices"))
        print(f"SEAT-PROBE: {'live' if ok else 'dead'} at {MODEL}")
        return ok
    except Exception as e:
        print(f"SEAT-PROBE: dead ({str(e)[:80]})")
        return False

if not seat_live():
    raise SystemExit(3)  # the seat's gone — exit before the matrix, receipt the reason

print(f"R2-LITM-REPRO at {MODEL} — context {len(CTX)/4:.0f} tokens-ish, 3 positions, 2 queries each")

def ask(q, mut=None):
    msgs = [{"role": "user", "content": CTX}, {"role": "user", "content": q}]
    body = json.dumps({"model": MODEL, "messages": msgs, "max_tokens": 60}).encode()
    hdr = ({} if os.environ.get("S2U_KEYLESS") == "1" else {"Authorization": f"Bearer {KEY}"})
    hdr["Content-Type"] = "application/json"
    try:
        req = urllib.request.Request(URL, data=body, headers=hdr)
        d = json.loads(urllib.request.urlopen(req, timeout=120).read().decode())
        return (d.get("choices") or [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        return f"[[ERR {str(e)[:50]}]]"

QUERIES = {
    "HEAD": ["What is the HEAD-MARKER-77's value?", "Quote the HEAD-MARKER-77 entry."],
    "MIDDLE": ["What is the MIDDLE-MARKER-33's value?", "Quote the MIDDLE-MARKER-33 entry."],
    "TAIL": ["What is the TAIL-MARKER-91's value?", "Quote the TAIL-MARKER-91 entry."],
}
TRUTH = {"HEAD": "4-8-15-16-23-42", "MIDDLE": "KETTLE-BLACK-FORWARD", "TAIL": "C9F2-88AA-3D14"}
acc = {}
for pos, qs in QUERIES.items():
    hits = 0
    for q in qs:
        out = ask(q)
        ok = any(tok in out.upper() for tok in TRUTH[pos].replace("-", " ").split() + [TRUTH[pos].split(" ")[0]])
        hits += 1 if ok else 0
        print(f"  {pos}: {ok} :: {out[:70]!r}")
    acc[pos] = hits / len(qs)
print(f"R2-SUMMARY acc={json.dumps(acc)}")
errs = sum(1 for _v in [out for qs in QUERIES.values() for out in [ask(q) for q in qs]] if "[[ERR" in _v)
verdict = "INCONCLUSIVE-ERRORS" if errs else ("LITM-CLASS-REPRODUCED (middle below tails)" if acc["MIDDLE"] < max(acc["HEAD"], acc["TAIL"]) else "PARTIAL/FLAT")
print(f"R2-VERDICT: {verdict} (errors={errs})")
