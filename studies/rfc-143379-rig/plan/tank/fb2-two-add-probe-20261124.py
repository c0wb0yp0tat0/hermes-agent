#!/usr/bin/env python3
"""FB-2 TWO-ADD EXECUTION PROBE — the promised test, run on our side.

The vet's recipe taken whole: execute the REAL `tools/memory_tool_store.py`
at each pinned SHA (git blob, exec'd verbatim) inside a stub-import sandbox
with a real temp memory dir, real atomic_write_text, no installs, no branch
touched. Both arms run the actual `add(doc:...)` path at the pin.

  Arm A  pre-fix 268bb091   two adds -> FIRST_SURVIVED_SECOND_ADD=?
  Arm B  fix     a9c65dc4   two adds -> FIRST_SURVIVED_SECOND_ADD=?
  Arm C  both               single add (removal control) -> entry survives

Pre-registered bars (from FB2-FAILING-CASE-SPEC-20261124.md):
  A RED  (FIRST_SURVIVED_SECOND_ADD=False — the clobber is present)
  B GREEN(FIRST_SURVIVED_SECOND_ADD=True  — the fix preserves the first)
  C control green on both.
"""
import importlib.util, json, os, subprocess, sys, tempfile
from pathlib import Path

REPO = "/root/workspace/repos/hermes-agent"
PINS = {"pre-fix": "268bb09147eaf948ece6a1beecd92a2268a5fc95",
        "fix":     "a9c65dc43db9000e8b6e238b50916aa6fa32ff08"}
STORE_REL = "tools/memory_tool_store.py"
FIRST = "FIRST marker note: the fleet's two-add probe, byte unique alpha."
SECOND = "SECOND marker note: the fleet's two-add probe, byte unique beta."


def blob(pin: str) -> str:
    return subprocess.run(["git", "-C", REPO, "show", f"{pin}:{STORE_REL}"],
                          capture_output=True, text=True, check=True).stdout


def make_sandbox_modules(mem_dir: Path):
    """Stub the store's real import surface with behavior-preserving minimal stand-ins."""
    import contextlib
    # utils.atomic_write_text — the real contract: temp file + rename.
    utils_mod = importlib.util.module_from_spec(importlib.util.spec_from_loader("utils", None))
    def atomic_write_text(path, content, tmp_prefix=".tmp_"):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(f"{tmp_prefix}{path.name}.{os.getpid()}.tmp")
        tmp.write_text(content, encoding="utf-8")
        os.replace(tmp, path)
    utils_mod.atomic_write_text = atomic_write_text
    # tools package root (submodule imports need the parent namespace)
    tools_pkg = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools", None))
    tools_pkg.__path__ = []
    sys.modules["tools"] = tools_pkg
    # tools.threat_patterns — benign content must pass; no threat scan at the store seam.
    tp_mod = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.threat_patterns", None))
    tp_mod.first_threat_message = lambda content, scope=None: None
    tp_mod.scan_for_threats = lambda entry, scope=None: []
    tp_mod.dirname = ""
    # tools.memory_tool — the store's monkeypatch seam: get_memory_dir -> sandbox dir.
    mt_mod = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.memory_tool", None))
    mt_mod.get_memory_dir = lambda: mem_dir
    mt_mod.fcntl = None  # both pins' _file_lock tolerate fcntl=None (yield-only path)? see below
    mt_mod.msvcrt = None
    # hermes_constants
    hc_mod = importlib.util.module_from_spec(importlib.util.spec_from_loader("hermes_constants", None))
    hc_mod.mkdir_under_hermes_home = lambda p: Path(p).mkdir(parents=True, exist_ok=True)
    # tools.hosted_tool_policy (used by the fix's _mutate gate)
    htp_mod = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.hosted_tool_policy", None))
    htp_mod.host_feature_enabled = lambda name: True
    sys.modules.update({"utils": utils_mod, "tools.threat_patterns": tp_mod,
                        "tools.memory_tool": mt_mod, "hermes_constants": hc_mod,
                        "tools.hosted_tool_policy": htp_mod})


def load_store(pin: str, mem_dir: Path):
    import contextlib
    make_sandbox_modules(mem_dir)
    src = blob(pin)
    # The module-level imports are stubbed via sys.modules; exec the file verbatim.
    ns: dict = {"__name__": f"store_{pin[:12]}",
                "__file__": f"{STORE_REL}@{pin[:12]}",
                "os": os, "re": __import__("re"), "time": __import__("time"),
                "Path": Path, "Any": dict, "Dict": dict, "List": list,
                "Optional": lambda x=None: x, "Tuple": tuple,
                "ContextVar": __import__("contextvars").ContextVar,
                "contextmanager": contextlib.contextmanager,
                "suppress": contextlib.suppress}
    exec(compile(src, f"<store@{pin[:12]}>", "exec"), ns)
    store_cls = ns["MemoryStore"]
    return store_cls


def seed_anchor(mem_dir: Path):
    mem_dir.mkdir(parents=True, exist_ok=True)
    (mem_dir / "MEMORY.md").write_text(
        "Dated memory chain: @doc:alpha\n", encoding="utf-8")


def run_arm(which: str, twice: bool):
    """Run one arm: instantiate the pin's real store, seed the anchor, add once/twice, read the doc file."""
    pin = PINS[which]
    mem_dir = Path(tempfile.mkdtemp(prefix=f"fb2-{which}-"))
    seed_anchor(mem_dir)
    cls = load_store(pin, mem_dir)
    store = cls()
    results = []
    for i, content in enumerate((FIRST, SECOND)):
        if i == 1 and not twice:
            break
        r = store.add("doc:alpha", content)
        results.append({"add": i + 1, "success": bool(r.get("success")),
                        "failure_class": r.get("failure_class"),
                        "error": (r.get("error") or "")[:80]})
    doc_path = mem_dir / "docs" / "alpha.md"
    raw = doc_path.read_text(encoding="utf-8") if doc_path.exists() else ""
    survived = FIRST in raw
    return {"arm": which, "pin": pin[:12], "twice": twice,
            "add_results": results, "doc_bytes": len(raw),
            "FIRST_SURVIVED_SECOND_ADD": survived,
            "doc_head": raw[:60].replace("\n", "\\n")}


if __name__ == "__main__":
    out = {}
    for which in ("pre-fix", "fix"):
        out[f"A-{which}-two-add"] = run_arm(which, twice=True)
        out[f"C-{which}-single-add"] = run_arm(which, twice=False)
    print(json.dumps(out, indent=2))
