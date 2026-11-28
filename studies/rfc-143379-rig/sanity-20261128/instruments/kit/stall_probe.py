#!/usr/bin/env python3
"""RW STALL-ON-READ PROBE — the reader-writer arm, our own execution.

Kvnloo's arm (row 7143199711): a reader's read() takes a disk snapshot and
stalls before returning; a writer commits meanwhile; the reader resumes. Under
the ORIGINAL #116673 read(), the read loads its (now stale) snapshot back into
the live cache when it resumes, rolling the writer's commit back (RB). Under
the FIXED read at a9c65dc4, read never mutates the live store (GREEN).

Variants (his 11-23 receipts):
  as-at-pin               GREEN   (snapshot under _file_lock, no cache write)
  lock-removed            GREEN   (no cache write either arm — stale never loads)
  cache-write-restored    GREEN   (the lock serializes reader before writer)
  both-removed            RED     (stale snapshot loads back into the live list)

The measurement is the LIVE list after the sequence: if the writer's "latest"
survives there, the reader didn't roll it back (GREEN); if the live list shows
["initial"] after the writer committed "latest", the rollback happened (RED).
The disk file always keeps both — the live cache is the rollback surface.
"""
import contextlib, importlib.util, json, os, subprocess, sys, tempfile, threading
from pathlib import Path

REPO = os.environ.get("PROBE_REPO", "/root/workspace/repos/hermes-agent")
PIN = "a9c65dc43db9000e8b6e238b50916aa6fa32ff08"
FIRST_SEED = "initial"
WRITER = "latest"

def store_source(pin):
    # the runner may lack the repo: fall back to the shipped pin's source file
    src = subprocess.run(["git","-C",REPO,"show",f"{pin}:tools/memory_tool_store.py"],
                         capture_output=True, text=True)
    if src.returncode == 0:
        return src.stdout
    for name in ("rw-store-a9c65dc4.py", "memory_tool_store.py"):
        local = Path(__file__).parent / name
        if local.exists():
            return local.read_text(encoding="utf-8")
    raise RuntimeError("no repo and no shipped store source")

def make_sandbox(mem_dir, read_variant):
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
    mt.get_memory_dir = lambda: mem_dir; mt.fcntl = None; mt.msvcrt = None
    hc = importlib.util.module_from_spec(importlib.util.spec_from_loader("hermes_constants", None))
    hc.mkdir_under_hermes_home = lambda p: Path(p).mkdir(parents=True, exist_ok=True)
    hp = importlib.util.module_from_spec(importlib.util.spec_from_loader("tools.hosted_tool_policy", None))
    hp.host_feature_enabled = lambda n: True
    sys.modules.update({"utils": utils, "tools": tools, "tools.threat_patterns": tp,
                        "tools.memory_tool": mt, "hermes_constants": hc,
                        "tools.hosted_tool_policy": hp})
    ns = {"__name__": "rw_probe", "os": os, "re": __import__("re"), "time": __import__("time"),
          "Path": Path, "Any": dict, "Dict": dict, "List": list, "Optional": lambda x=None: x,
          "Tuple": tuple, "ContextVar": __import__("contextvars").ContextVar,
          "contextmanager": __import__("contextlib").contextmanager,
          "suppress": __import__("contextlib").suppress}
    exec(compile(store_source(PIN), "<store>", "exec"), ns)
    S = ns["MemoryStore"]
    if read_variant in ("lock-removed", "both-removed"):
        S._file_lock = staticmethod(lambda path: contextlib.nullcontext())
    if read_variant in ("cache-write-restored", "both-removed"):
        # the ORIGINAL #116673 reader: read() takes its disk snapshot; if the
        # LOCK IS PRESENT the writer cannot interleave (it waits behind the
        # lock), so the snapshot is never stale and the cache write is benign.
        # If the lock is REMOVED the writer commits mid-read and the resumed
        # read loads its STALE snapshot into the live list — the rollback.
        lock_present = read_variant == "cache-write-restored"
        stall = threading.Event()
        inside = threading.Event()
        done = threading.Event()
        def read_with_cache(self, target):
            raw, ok = self._read_raw_checked(self._path_for(target))
            entries = list(dict.fromkeys(self._parse_entries(raw))) if ok else []
            inside.set()                  # the read holds its snapshot
            if not lock_present:
                stall.wait(5)             # writer may commit mid-read (no lock)
            self._set_entries(target, entries)   # the cache write
            done.set()
            return {"success": True, "target": target, "entries": entries}
        S.read = read_with_cache
        S._RW_STALL = stall
        S._RW_INSIDE = inside
        S._RW_DONE = done
        S._RW_LOCK_PRESENT = lock_present
    return S

def run(variant):
    mem = Path(tempfile.mkdtemp(prefix="rw-"))
    (mem/"MEMORY.md").write_text("Dated memory chain: @doc:alpha\n", encoding="utf-8")
    store = make_sandbox(mem, variant)()
    store.add("doc:alpha", FIRST_SEED)

    reader_stalled = threading.Event()
    resume_reader = threading.Event()
    writer_done = threading.Event()
    state = {}

    def reader():
        # call read() — it snapshots, signals inside, and blocks; the writer
        # commits during the block; then the read resumes with its stale view.
        store.read("doc:alpha")
        state["reader_done"] = True

    def writer():
        # with the LOCK PRESENT, the writer cannot interleave: it must wait
        # for the reader's read to COMPLETE (the lock serializes). With the
        # lock removed, the writer commits mid-stall (the race's window).
        done = getattr(store, "_RW_DONE", None)
        inside = getattr(store, "_RW_INSIDE", None)
        stall = getattr(store, "_RW_STALL", None)
        lock_present = getattr(store, "_RW_LOCK_PRESENT", True)
        if lock_present:
            if done is not None:
                done.wait(5)              # serialized: the read finishes first
        else:
            if inside is not None:
                inside.wait(5)            # the reader holds its snapshot
        store.add("doc:alpha", WRITER)
        if stall is not None:
            stall.set()                   # release the stale read (no-lock arm)

    t1 = threading.Thread(target=reader); t2 = threading.Thread(target=writer)
    t1.start(); t2.start(); t1.join(); t2.join()

    # THE MEASUREMENT: the live list (the rollback surface), not the disk file
    live = store._entries_for("doc:alpha") if hasattr(store, "_entries_for") else store.memory_entries
    doc = mem/"docs"/"alpha.md"
    disk = doc.read_text(encoding="utf-8") if doc.exists() else ""
    return {"variant": variant,
            "live_entries": list(live),
            "disk_bytes": len(disk.encode()), "disk_chars": len(disk),
            "LATEST_SURVIVED_IN_LIVE": WRITER in live,
            "rollback_observed": WRITER not in live and FIRST_SEED in live,
            "disk_has_latest": WRITER in disk}

if __name__ == "__main__":
    out = {v: run(v) for v in ("as-at-pin", "lock-removed", "cache-write-restored", "both-removed")}
    print(json.dumps(out, indent=2))
