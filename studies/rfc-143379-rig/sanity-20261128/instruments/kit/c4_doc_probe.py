#!/usr/bin/env python3
"""C4 DOC-SEMANTICS PROBE — the doc add's whole-file-replace vs the append arm.

The question (kvnloo's 268bb091 find): two add("doc:notes", …) calls — under the
pinned `_add_doc`, the SECOND replaces the whole doc (atomic_write_text), so the
first entry is silently lost. The C4 arm applies the append semantics (locked
re-read → append → write) and checks both entries survive.

Receipts:
  replace-arm:  TWO-ADDS -> first lost?  -> SILENT-OVERWRITE or BOTH-SURVIVE
  append-arm:   TWO-ADDS -> first lost?  -> SILENT-OVERWRITE or BOTH-SURVIVE
"""
import contextlib, importlib.util, json, os, sys, tempfile, subprocess
from pathlib import Path

REPO = "/root/workspace/repos/hermes-agent"
PINS = {"fix": "a9c65dc43db9000e8b6e238b50916aa6fa32ff08",
        "gate": "268bb09147eaf948ece6a1beecd92a2268a5fc95"}

def store_source(pin):
    src = subprocess.run(["git","-C",REPO,"show",f"{pin}:tools/memory_tool_store.py"],
                         capture_output=True, text=True)
    if src.returncode == 0:
        return src.stdout
    return Path(__file__).parent.joinpath("memory_tool_store.py").read_text(encoding="utf-8")

def sandbox(mem_dir, append_arm, pin="fix"):
    def atomic(path, content, tmp_prefix=".tmp_"):
        path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(f"{tmp_prefix}{path.name}.{os.getpid()}.tmp")
        tmp.write_text(content, encoding="utf-8")
        os.replace(tmp, path)
    utils = importlib.util.module_from_spec(importlib.util.spec_from_loader("utils", None)); utils.atomic_write_text = atomic
    tools = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools", None)); tools.__path__ = []
    tp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.threat_patterns", None))
    tp.first_threat_message = lambda c, scope=None: None; tp.scan_for_threats = lambda e, scope=None: []
    mt = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.memory_tool", None))
    mt.get_memory_dir = lambda: mem_dir if isinstance(mem_dir, Path) else Path(mem_dir); mt.fcntl = None; mt.msvcrt = None
    hc = importlib.util.module_from_spec(importlib.util.spec_from_loader("hermes_constants", None))
    hc.mkdir_under_hermes_home = lambda p: Path(p).mkdir(parents=True, exist_ok=True)
    hp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.hosted_tool_policy", None))
    hp.host_feature_enabled = lambda n: True
    sys.modules.update({"utils": utils, "tools": tools, "tools.threat_patterns": tp,
                        "tools.memory_tool": mt, "hermes_constants": hc,
                        "tools.hosted_tool_policy": hp})
    ns = {"__name__": "c4_probe", "os": os, "re": __import__("re"), "time": __import__("time"),
          "Path": Path, "Any": dict, "Dict": dict, "List": list, "Optional": lambda x=None: x,
          "Tuple": tuple, "ContextVar": __import__("contextvars").ContextVar,
          "contextmanager": __import__("contextlib").contextmanager,
          "suppress": __import__("contextlib").suppress}
    exec(compile(store_source(PINS[pin]), "<store>", "exec"), ns)
    S = ns["MemoryStore"]
    if append_arm:
        # the C4 patch: the CLASS's _add_doc becomes a LOCKED re-read -> append -> write
        def add_doc_append(name, content):
            from pathlib import Path as _P
            target = _P(mem_dir if isinstance(mem_dir, Path) else Path(mem_dir)) / "docs" / f"{name}.md"
            with S._file_lock(target):
                raw = target.read_text(encoding="utf-8") if target.exists() else ""
                if content not in raw:
                    raw = raw.rstrip("\n") + ("\n" if raw.strip() else "") + content + "\n"
                atomic(str(target), raw)
            return {"success": True, "content": content}
        S._add_doc = staticmethod(add_doc_append)
    return S

def run(append_arm, pin="fix"):
    mem = Path(tempfile.mkdtemp(prefix="c4-"))
    (mem/"MEMORY.md").write_text("Dated memory chain: @doc:notes\n", encoding="utf-8")
    S = sandbox(mem, append_arm, pin)
    store = S()
    r1 = store.add("doc:notes", "first doc fact")
    r2 = store.add("doc:notes", "second doc fact")
    docfile = Path(mem) / "docs" / "notes.md"
    disk = docfile.read_text(encoding="utf-8") if docfile.exists() else ""
    return {
        "arm": "append" if append_arm else "replace (as-pinned)",
        "r1_message": str(r1.get("message") or r1),
        "r2_message": str(r2.get("message") or r2),
        "disk_after_two_adds": repr(disk),
        "FIRST_SURVIVED": "first doc fact" in disk,
        "SECOND_SURVIVED": "second doc fact" in disk,
        "CLASS": "SILENT-OVERWRITE" if ("first doc fact" not in disk and "second doc fact" in disk) else "BOTH-SURVIVE/OTHER",
    }

if __name__ == "__main__":
    import itertools
    out={}
    for pin in ("fix","gate"):
        out[pin]={"replace": run(False, pin), "append": run(True, pin)}
    print(json.dumps(out, indent=1))
