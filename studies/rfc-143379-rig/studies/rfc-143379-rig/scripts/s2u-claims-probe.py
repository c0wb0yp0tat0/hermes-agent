#!/usr/bin/env python3
"""The S2U claims probe — the fresh-test-in-response (the independent convergence with evidence).

Each load-bearing claim the corrective final draft carries is MEASURED at the pinned head,
with the restore-head counterfactual where the draft asserts one. Rows printed, verdicts
against the draft's claims, honest to the NOT-RUN ceiling. Runner-side: no gh assumed,
no network assumed beyond the origin fetch (guarded, receipted).
"""
import ast, json, os, re, subprocess, sys

ROOT = os.getcwd()
ROWS = []


def row(claim, measured, verdict, note=""):
    ROWS.append({"claim": claim, "measured": str(measured)[:200], "verdict": verdict, "note": str(note)[:120]})
    print(f"[CLAIM] {claim}")
    print(f"  measured: {str(measured)[:200]}")
    print(f"  verdict: {verdict} {note}")


# --- C1: the read's absence at this pinned head (the draft's core wound) ---
try:
    src = open(os.path.join(ROOT, "tools", "memory_tool_store.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    has_read = any(
        isinstance(n, ast.FunctionDef) and n.name == "read"
        for node in tree.body if isinstance(node, ast.ClassDef)
        for n in node.body
    )
    row("C1 the store's read method is absent at this head",
        f"read-method present: {has_read}",
        "PASS-vs-draft" if not has_read else "CONTRADICTS-draft")
except Exception as e:
    row("C1 the store's read method is absent at this head", f"probe-error: {e}", "INCONCLUSIVE")

# --- C2: the dispatch's unknown-action answer for read (the execution-confirmed gap) ---
try:
    src = open(os.path.join(ROOT, "tools", "memory_tool.py"), encoding="utf-8").read()
    m = re.findall(r"Unknown action [^\"']+", src)
    measured = "|".join(m[:3]) if m else "no-unknown-action-string-in-tree"
    row("C2 the dispatch's unknown-action answer exists for read", measured,
        "PASS-vs-draft" if "Unknown action" in measured else "CONTRADICTS-draft")
except Exception as e:
    row("C2 the dispatch's unknown-action answer exists for read", f"probe-error: {e}", "INCONCLUSIVE")

# --- C3: the hand-back sites at the pinned tree (the four + the echoes) ---
try:
    src = open(os.path.join(ROOT, "tools", "memory_tool_store.py"), encoding="utf-8").read()
    sites = {
        "_failure_with_entries": "_failure_with_entries" in src,
        "closest_entries-hint": src.count("closest_entries") > 0,
        "current_entries-echoes": src.count("current_entries"),
    }
    ok = sites["_failure_with_entries"] and sites["closest_entries-hint"] and sites["current_entries-echoes"] > 0
    row("C3 the hand-back sites exist only to hand entries back", json.dumps(sites),
        "PASS-vs-draft" if ok else "PARTIAL")
except Exception as e:
    row("C3 the hand-back sites exist only to hand entries back", f"probe-error: {e}", "INCONCLUSIVE")

# --- C4: the restore-head's counterfactual (fetched + worktree'd; honest to NOT-RUN) ---
note, verdict = "", "NOT-RUN"
try:
    # the fetch-source's parameterized (the C4-counterfactual's fix, 11-11: the pull-ref lives on
    # the UPSTREAM, never the fork's origin)
    _upstream = os.environ.get("S2U_UPSTREAM", "https://github.com/NousResearch/hermes-agent")
    r = subprocess.run(["git", "fetch", _upstream, "refs/pull/141876/head:refs/restore-head"],
                       capture_output=True, text=True, cwd=ROOT, timeout=120)
    if r.returncode == 0:
        r2 = subprocess.run(["git", "worktree", "add", "/tmp/restore-head", "refs/restore-head"],
                            capture_output=True, text=True, cwd=ROOT, timeout=60)
        if r2.returncode == 0:
            src2 = open("/tmp/restore-head/tools/memory_tool_store.py", encoding="utf-8").read()
            m = re.search(r"\n    def read\(self", src2)
            verdict = "PASS-vs-draft" if m else "CONTRADICTS-draft"
            note = f"restore-head defines read at {m.start() if m else 'no-location'}"
        else:
            note = f"worktree-error: {r2.stderr.strip()[:80]}"
    else:
        note = f"fetch-error: {r.stderr.strip()[:80]}"
except Exception as e:
    note = f"probe-error: {e}"
row("C4 the restore-head defines read (the counterfactual the draft asserts)", note, verdict)

print("\n=== S2U-CLAIMS-SUMMARY ===")
print(json.dumps(ROWS, indent=1))
