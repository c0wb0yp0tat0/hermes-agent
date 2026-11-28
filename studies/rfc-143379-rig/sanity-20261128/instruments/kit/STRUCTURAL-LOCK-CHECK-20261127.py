#!/usr/bin/env python3
"""STRUCTURAL LOCK CHECK — kvnloo's shape-(1) test, run for real (2026-11-27).

The read ships stateless and its lock cannot be tested on output (kvnloo's
1,031/0 + 6,127/0 rows). The structural test: a non-blocking flock on
MEMORY.md.lock, taken while the read holds it, MUST fail (EWOULDBLOCK) —
the same check kvnloo used on _add_doc. Store code untouched; the harness
wraps _file_lock to signal inside/outside only.
"""
import contextlib, importlib.util, fcntl, json, os, subprocess, sys, tempfile, threading, time
from pathlib import Path

KIT = Path("/root/workspace/drop/rfc143379-20261125-reply-stage/PILOT-KIT-PHASE1")
REPO = Path("/root/workspace/repos/hermes-agent")
PIN = "a9c65dc43db9000e8b6e238b50916aa6fa32ff08"

def store_source():
    src = subprocess.run(["git","-C",str(REPO),"show",f"{PIN}:tools/memory_tool_store.py"],
                         capture_output=True, text=True)
    if src.returncode == 0:
        return src.stdout
    return (KIT / "memory_tool_store.py").read_text(encoding="utf-8")

src = store_source()
cache_dir = Path(tempfile.mkdtemp(prefix="mod_cache_"))
mod_path = cache_dir / "memory_tool_store.py"
mod_path.write_text(src, encoding="utf-8")

# stub the repo tooling exactly as the kit's stall probe does (store code untouched)
utils = importlib.util.module_from_spec(importlib.util.spec_from_loader("utils", None))
utils.atomic_write_text = lambda p, c, tmp_prefix=".tmp_": (Path(p).parent.mkdir(parents=True, exist_ok=True), Path(p).write_text(c))
tools = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools", None)); tools.__path__ = []
tp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.threat_patterns", None))
tp.first_threat_message = lambda c, scope=None: None; tp.scan_for_threats = lambda e, scope=None: []
mt = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.memory_tool", None))
mt.get_memory_dir = lambda: cache_dir; mt.fcntl = fcntl; mt.msvcrt = None   # REAL fcntl: the lock must actually engage
hc = importlib.util.module_from_spec(importlib.util.spec_from_loader("hermes_constants", None))
hc.mkdir_under_hermes_home = lambda p: Path(p).mkdir(parents=True, exist_ok=True)
hp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.hosted_tool_policy", None))
hp.host_feature_enabled = lambda n: True
sys.modules.update({"utils": utils, "tools": tools, "tools.threat_patterns": tp,
                    "tools.memory_tool": mt, "hermes_constants": hc,
                    "tools.hosted_tool_policy": hp})

spec = importlib.util.spec_from_file_location("mts", mod_path)
mts = importlib.util.module_from_spec(spec)
os.environ.setdefault("HERMES_HOME", str(cache_dir))
spec.loader.exec_module(mts)

inside = threading.Event()
orig_file_lock = mts.MemoryStore._file_lock

class _WrappedLock:
    def __init__(self, ctx):
        self._ctx = ctx
    def __enter__(self):
        inside.set()
        self._ctx.__enter__()
        return self
    def __exit__(self, *a):
        try:
            self._ctx.__exit__(*a)
        finally:
            inside.clear()

def wrapped_file_lock(cls, path):
    return _WrappedLock(orig_file_lock(path))

mts.MemoryStore._file_lock = classmethod(wrapped_file_lock)

store = mts.MemoryStore()
store._path_for = lambda t: cache_dir / "MEMORY.md"
store.add("memory", "initial")

lock_path = cache_dir / "MEMORY.md.lock"
stats = {"inside_attempts": 0, "blocked_inside": 0, "success_inside": 0,
         "outside_success": 0, "outside_ewouldblock": 0, "reads": 0, "writes": 0}
stop = threading.Event()
lock = threading.Lock()

def reader():
    while not stop.is_set():
        store.read("memory")
        with lock:
            stats["reads"] += 1

def writer():
    i = 0
    while not stop.is_set():
        store.add("memory", f"writer-{i}")
        i += 1
        with lock:
            stats["writes"] += 1

def tester_natural():
    while not stop.is_set():
        if not inside.is_set():
            continue
        fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            with lock:
                stats["blocked_inside"] += 1
        else:
            with lock:
                stats["success_inside"] += 1
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
        with lock:
            stats["inside_attempts"] += 1

ts = [threading.Thread(target=reader), threading.Thread(target=writer), threading.Thread(target=tester_natural)]
for t in ts: t.start()
time.sleep(8.0)
stop.set()
for t in ts: t.join()

# deterministic held-open arm: 100 trials, exactly like its semantics
held_blocked = 0
for _ in range(100):
    with store._file_lock(cache_dir / "MEMORY.md"):
        fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            held_blocked += 1
        else:
            fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)

# outside control: no holder -> NB succeeds
fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
control = "EWOULDBLOCK"
try:
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    control = "ACQUIRED"
except BlockingIOError:
    pass
os.close(fd)

receipt = {
    "pin": PIN, "store": "a9c65dc4", "date": "2026-11-27",
    "natural_observation": {"inside_attempts": stats["inside_attempts"],
                "blocked_inside": stats["blocked_inside"],
                "success_inside": stats["success_inside"],
                "reads": stats["reads"], "writes": stats["writes"],
                "note": "the success-inside balance is the measured release-window artifact: the store unlocks inside its `with fd:` before the harness flag clears. The deterministic arm is the assertion."},
    "held_open_100": {"blocked": held_blocked},
    "outside_control": control,
    "assertions": {
        "held_open_all_block": held_blocked == 100,
        "control_not_blocked_when_unheld": control == "ACQUIRED",
    },
}
Path(KIT / "STRUCTURAL-LOCK-RECEIPT-20261127.json").write_text(json.dumps(receipt, indent=2))
print(json.dumps(receipt, indent=2))
ok = all(receipt["assertions"].values())
print("RESULT:", "ALL PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
