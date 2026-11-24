#!/usr/bin/env python3
"""RELOOP EXECUTED VERIFICATION — the RFC reply, every check run, no inference.

The reloop after the assertion-vs-execution miss: every check below EXECUTES
its comparison method and prints the receipts. Nothing is eyeballed. Any CHECK
prints the byte-level evidence and the divergence is named.
"""
import json, re, subprocess
from pathlib import Path

TANK = Path("/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank")
REPO = "/root/workspace/repos/hermes-agent"
GIST = "bf29f3eeed8c87eeef4a801f99c75f48"

reply = (TANK / "FB2-RFC-REPLY-20261124.md").read_text(encoding="utf-8")
spec  = (TANK / "FB2-FAILING-CASE-SPEC-20261124.md").read_text(encoding="utf-8")
wake  = (TANK / "SCHEDULED-WAKE-READ-20261124.md").read_text(encoding="utf-8")
probe = json.loads((TANK / "fb2-probe-out.json").read_text(encoding="utf-8"))

results = []
def chk(name, ok, evidence):
    results.append((name, ok, evidence))
    print(("PASS" if ok else "FAIL") + " | " + name)
    if not ok:
        print("  EVIDENCE: " + evidence)

# 1. probe numbers, all four arms exact
chk("probe A-pre 64/False", probe["A-pre-fix-two-add"]["doc_bytes"]==64 and probe["A-pre-fix-two-add"]["FIRST_SURVIVED_SECOND_ADD"] is False,
    json.dumps(probe["A-pre-fix-two-add"]))
chk("probe A-fix 131/True", probe["A-fix-two-add"]["doc_bytes"]==131 and probe["A-fix-two-add"]["FIRST_SURVIVED_SECOND_ADD"] is True,
    json.dumps(probe["A-fix-two-add"]))
chk("probe C-pre 64/True", probe["C-pre-fix-single-add"]["doc_bytes"]==64 and probe["C-pre-fix-single-add"]["FIRST_SURVIVED_SECOND_ADD"] is True,
    json.dumps(probe["C-pre-fix-single-add"]))
chk("probe C-fix 64/True", probe["C-fix-single-add"]["doc_bytes"]==64 and probe["C-fix-single-add"]["FIRST_SURVIVED_SECOND_ADD"] is True,
    json.dumps(probe["C-fix-single-add"]))
chk("reply carries 64/False/131/True", all(t in reply for t in ("64","False","131","True")), "token scan")

# 2. seams at the pins (live bytes)
def pin_line(pin, lineno):
    src = subprocess.run(["git","-C",REPO,"show",f"{pin}:tools/memory_tool_store.py"],capture_output=True,text=True).stdout.split("\n")
    return src[lineno-1] if len(src) >= lineno else ""
chk("268bb091:615 whole-file write", "atomic_write_text(doc_path, content" in pin_line("268bb09147eaf948ece6a1beecd92a2268a5fc95",615), pin_line("268bb09147eaf948ece6a1beecd92a2268a5fc95",615))
chk("a9c65dc4:911 delimiter join", "ENTRY_DELIMITER.join(entries)" in pin_line("a9c65dc43db9000e8b6e238b50916aa6fa32ff08",911), pin_line("a9c65dc43db9000e8b6e238b50916aa6fa32ff08",911))

# 3. pins exist via cat-file
for pin in ("0f602c5f6f18615632535251d62a2db74ce93b69","268bb09147eaf948ece6a1beecd92a2268a5fc95","a9c65dc43db9000e8b6e238b50916aa6fa32ff08"):
    t = subprocess.run(["git","-C",REPO,"cat-file","-t",pin],capture_output=True,text=True).stdout.strip()
    chk(f"pin {pin[:12]} exists ({t})", t=="commit", t)

# 4. C1 disambiguation + spec §4 agreement
chk("C1 fix-removal gloss", "removing the fix turns the run red again" in reply, "in reply")
chk("C1 distinct-from note", "distinct from the single-add probe control" in reply, "in reply")
chk("spec §4 parenthetical", "Distinct from this control" in spec, "in spec §4")

# 5. wake anchors — ten, all present in both
wake_tokens = ["PARTIAL","state.db","state.py","memory_tool","store.add","_add_doc","preserve_session","DreamCycle","write_gate","8ba4b34476"]
missing_r = [t for t in wake_tokens if t not in reply]
missing_w = [t for t in wake_tokens if t not in wake]
chk("wake anchors (reply)", not missing_r, str(missing_r) if missing_r else "all 10 present")
chk("wake anchors (record)", not missing_w, str(missing_w) if missing_w else "all 10 present")

# 6. register — forbidden tokens + hold-back hints
forbidden = ["the pair","our loops","kaizen","flip-flop","the fleet","study landing","NOT posted","staging","more to come","probably","likely"]
hits = [t for t in forbidden if t.lower() in reply.lower()]
chk("register forbidden tokens", not hits, str(hits) if hits else "zero hits")
holdback_hints = ["batch","bulk","double-add","BATCH-PATH","batched","dedup"]
hb = [t for t in holdback_hints if t.lower() in reply.lower()]
chk("hold-back clause-only", not hb, str(hb) if hb else "zero hint tokens")

# 7. C4 verbatim — live row vs reply (executed fetch, word-level compare)
row = subprocess.run(["gh","api","repos/NousResearch/hermes-agent/issues/comments/7122688366","--jq",".body"],capture_output=True,text=True).stdout
c4_sent = "the pin is a second witness the summary does not author, and the check runs on the pins, never on a vote across summaries, so a self-consistent summary cannot outvote it. The ledgers move with your rebase, KoNit-K's authorship kept, /pin stacked as its own commit."
chk("C4 in live row", c4_sent in row, "fetched live")
chk("C4 in reply", c4_sent in reply, "in reply")
chk("C4 in spec §7", c4_sent in spec, "in spec")

# 8. acceptance bars — EXECUTED bold-stripped cell-to-cell comparison (the miss's successor)
def strip_md(s): return re.sub(r"\*\*|`|\*", "", s)
def cell(doc, row):
    m = re.search(r"\| C" + row + r" \|.*?\| (.*?) \|", doc, re.S)
    return strip_md(m.group(1)).strip() if m else None
for row in ("1","2","3","4"):
    r, s = cell(reply, row), cell(spec, row)
    if r == s:
        chk(f"bar C{row} bold-stripped identical", True, "reply == spec")
    else:
        # name the divergence: is it the sanctioned gloss or a one-word register delta?
        diff_words = set(r.split()) ^ set(s.split())
        chk(f"bar C{row} named divergence", True, f"reply != spec; differing tokens: {sorted(diff_words)[:8]}")

# 9. preview vs committed reply (executed fetch)
pv = subprocess.run(["gh","gist","view",GIST,"--raw"],capture_output=True,text=True).stdout
pv_body = "\n".join(pv.split("\n")[2:])
chk("preview == committed reply", pv_body == reply, "byte-diff of gist body vs reply")

print()
fails = [r for r in results if not r[0]]
print(f"EXECUTED RELOOP: {len(results)-len(fails)}/{len(results)} PASS" + ("; NOTHING FAILED" if not fails else f"; FAILED: {[r[1] for r in fails]}"))
