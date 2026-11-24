#!/usr/bin/env python3
"""FB-2 CONCURRENT-ADD PROBE — answers kvnloo's interleaving question empirically.

The claim "removing both the lock and the no-cache-write turns red" (spec §3,
traced to kvnloo's own matrix row 7087999804) needs the interleaving that makes
it true: TWO adds racing concurrently, both reading before either writes, with
the lock removed (yield-only) — last-writer-wins drops the first's entry.

Run: the verbatim `_add_doc` body at a9c65dc4 (the fix pin) with the lock
stubbed yield-only (the removal arm), two threads, barrier-synced so both pass
the read and hit the write. Expected: FIRST_SURVIVED_SECOND_ADD=False under
concurrency even at the fix pin — the red that sequential two-add cannot see.
"""
import json, threading, subprocess, tempfile
from pathlib import Path

REPO = "/root/workspace/repos/hermes-agent"
PIN = "a9c65dc43db9000e8b6e238b50916aa6fa32ff08"
FIRST = "FIRST marker note: the fleet's two-add probe, byte unique alpha."
SECOND = "SECOND marker note: the fleet's two-add probe, byte unique beta."

def store_source(pin):
    return subprocess.run(["git","-C",REPO,"show",f"{pin}:tools/memory_tool_store.py"],
                          capture_output=True, text=True, check=True).stdout

def make_sandbox(mem_dir):
    import importlib.util, os, sys
    def atomic(path, content, tmp_prefix=".tmp_"):
        path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(f"{tmp_prefix}{path.name}.{os.getpid()}.tmp")
        tmp.write_text(content, encoding="utf-8")
        os.replace(tmp, path)
    tips = {}
    utils = importlib.util.module_from_spec(importlib.util.spec_from_loader("utils", None)); utils.atomic_write_text = atomic
    tools = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools", None)); tools.__path__ = []
    tp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.threat_patterns", None))
    tp.first_threat_message = lambda c, scope=None: None; tp.scan_for_threats = lambda e, scope=None: []
    mt = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.memory_tool", None))
    mt.get_memory_dir = lambda: mem_dir; mt.fcntl = None; mt.msvcrt = None
    hc = importlib.util.module_from_spec(importlib.util.spec_from_loader("hermes_constants", None))
    hc.mkdir_under_hermes_home = lambda p: Path(p).mkdir(parents=True, exist_ok=True)
    hp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.hosted_tool_policy", None))
    hp.host_feature_enabled = lambda n: True
    sys.modules.update({"utils": utils, "tools": tools, "tools.threat_patterns": tp,
                        "tools.memory_tool": mt, "hermes_constants": hc,
                        "tools.hosted_tool_policy": hp})
    ns = {"__name__": "store_probe", "os": os, "re": __import__("re"), "time": __import__("time"),
          "Path": Path, "Any": dict, "Dict": dict, "List": list, "Optional": lambda x=None: x,
          "Tuple": tuple, "ContextVar": __import__("contextvars").ContextVar,
          "contextmanager": __import__("contextlib").contextmanager,
          "suppress": __import__("contextlib").suppress}
    exec(compile(store_source(PIN), "<store>", "exec"), ns)
    return ns["MemoryStore"]()

def run(twice_concurrent):
    mem = Path(tempfile.mkdtemp(prefix="fb2-race-"))
    (mem/"MEMORY.md").write_text("Dated memory chain: @doc:alpha\n", encoding="utf-8")
    store = make_sandbox(mem)
    if not twice_concurrent:
        store.add("doc:alpha", FIRST)
        store.add("doc:alpha", SECOND)
    else:
        barrier = threading.Barrier(2)
        results = {"r": []}
        def do(content):
            barrier.wait()
            r = store.add("doc:alpha", content)
            results["r"].append((content[:5], bool(r.get("success"))))
        t1 = threading.Thread(target=do, args=(FIRST,)); t2 = threading.Thread(target=do, args=(SECOND,))
        t1.start(); t2.start(); t1.join(); t2.join()
    doc = mem/"docs"/"alpha.md"
    raw = doc.read_text(encoding="utf-8") if doc.exists() else ""
    return {"concurrent": twice_concurrent, "doc_bytes": len(raw.encode("utf-8")),
            "doc_chars": len(raw), "FIRST_SURVIVED": FIRST in raw,
            "head": raw[:40].replace("\n","\\n")}

if __name__ == "__main__":
    out = {"sequential": run(False), "concurrent-race": run(True)}
    print(json.dumps(out, indent=2))
