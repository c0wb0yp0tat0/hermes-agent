#!/usr/bin/env python3
"""NEMO-BRIDGE read-side scaffold (RFC #143379).

Memory-first tool wrapper: lifts a tool-shy seat into real tool-use by
curating the persistent memory store into the system turn and requiring a
read-back ping before every act. Read-side only; stdlib + tools.memory_tool.
"""
import json
import os
import urllib.request

PING = ("You CAN execute the tools: this lane's harness provides the terminal, read_file, "
        "write_file, and list_dir tools, and they are yours to use. Before every act, quote the "
        "memory entry that grounds it. The act is 'record/update this entry' - a memory operation, "
        "never a bare tool call. Where you can execute, you must - never claim an incapability the "
        "harness has not given you. Never report 'expected output' in place of real output.")

TOOLS = [
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read a text file from the workspace.",
        "parameters": {"type": "object",
                       "properties": {"path": {"type": "string"}},
                       "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "write_file",
        "description": "Write a text file into the workspace.",
        "parameters": {"type": "object",
                       "properties": {"path": {"type": "string"},
                                      "content": {"type": "string"}},
                       "required": ["path", "content"]}}},
]


def _text(block):
    """Coerce one memory block (str/dict/object) to display text."""
    if isinstance(block, str):
        return block
    if isinstance(block, dict):
        for k in ("text", "content", "body", "entry", "value", "summary"):
            v = block.get(k)
            if isinstance(v, str):
                return v
        return json.dumps(block, sort_keys=True)[:400]
    for k in ("text", "content", "body", "entry"):
        v = getattr(block, k, None)
        if isinstance(v, str):
            return v
    return str(block)[:400]


def _blocks(store):
    """Defensive extraction of the store's blocks across known shapes."""
    for attr in ("entries", "blocks", "memories", "items", "store"):
        cand = getattr(store, attr, None)
        if callable(cand):
            try:
                cand = cand()
            except Exception:
                continue
        if isinstance(cand, dict):
            cand = list(cand.values())
        if cand:
            return [_text(b) for b in cand]
    for meth in ("all", "list", "get_all", "dump"):
        fn = getattr(store, meth, None)
        if callable(fn):
            try:
                out = fn()
            except Exception:
                continue
            if isinstance(out, dict):
                out = list(out.values())
            if out:
                return [_text(b) for b in out]
    return []


def bridge(system, user_toolstep, max_blocks=5):
    """Load the memory store; curate the blocks relevant to user_toolstep;
    return the assembled system-turn string (memory-first, ping-terminated)."""
    head = (system or "").rstrip()
    try:
        from tools.memory_tool import load_on_disk_store
        blocks = _blocks(load_on_disk_store())
    except Exception as exc:  # store unavailable -> still emit the ping
        blocks = []
        head += "\n[memory_bridge: store unavailable: %s]" % type(exc).__name__
    want = [w for w in (user_toolstep or "").lower().split() if len(w) > 3]

    def score(t):
        tl = t.lower()
        return sum(1 for w in want if w in tl)

    picked = sorted(blocks, key=score, reverse=True)[:max_blocks]
    if not any(score(b) > 0 for b in picked):
        picked = blocks[:max_blocks]
    out = [head, "", "# MEMORY CONTEXT (curated read-side)"]
    if picked:
        for i, b in enumerate(picked, 1):
            out.append("MEMORY ENTRY %d: %s" % (i, b.replace("\n", " ")[:600]))
    else:
        out.append("(no memory entries matched)")
    out += ["", PING]
    return "\n".join(out)


def _auth():
    with open(os.path.expanduser("~/.hermes/auth.json")) as fh:
        return json.load(fh)


def _endpoint(auth):
    nous = (auth.get("providers") or {}).get("nous") or {}
    for k in ("base_url", "api_base", "endpoint", "url"):
        if nous.get(k):
            return nous[k].rstrip("/") + "/chat/completions"
    base = os.environ.get("NEMO_BASE_URL", "https://inference-api.nousresearch.com/v1")
    return base.rstrip("/") + "/chat/completions"


def _post(url, key, payload):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read().decode())


def _tool_calls(resp):
    try:
        return resp["choices"][0]["message"].get("tool_calls") or []
    except Exception:
        return []


def nemo_test(task="Read the file PROBE.txt and report its exact contents."):
    """A/B: same task, tools present, with vs without the bridge. Prints which
    returned tool_calls. The bridge WORKS iff the bridged request flips Nemo."""
    auth = _auth()
    key = auth["providers"]["nous"]["agent_key"]
    url = _endpoint(auth)
    mission = ("You are a careful assistant. When the user asks for a file, "
               "use the read_file tool to read it.")
    bridged = bridge(mission, task)
    print("== BRIDGED SYSTEM TURN ==")
    print(bridged)
    print("== A/B on mistralai/mistral-nemo (max_tokens 400) ==")
    verdict = {}
    for label, system in (("A_unbridged", mission), ("B_bridged", bridged)):
        payload = {"model": "mistralai/mistral-nemo",
                   "messages": [{"role": "system", "content": system},
                                {"role": "user", "content": task}],
                   "tools": TOOLS, "max_tokens": 400}
        try:
            calls = _tool_calls(_post(url, key, payload))
            verdict[label] = bool(calls)
            names = [c.get("function", {}).get("name") for c in calls]
            print("%s: tool_calls=%s %s" % (label, bool(calls), names))
        except Exception as exc:
            verdict[label] = False
            print("%s: ERROR %s: %s" % (label, type(exc).__name__, exc))
    ok = verdict.get("B_bridged") and not verdict.get("A_unbridged")
    print("VERDICT: bridge %s" % ("WORKS (Nemo flipped)" if ok else "did NOT flip Nemo"))
    return ok


if __name__ == "__main__":
    nemo_test()
