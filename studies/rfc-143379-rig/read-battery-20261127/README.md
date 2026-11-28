# read-battery-20261127 — the three-contour verification leg (standardized)

Artifact under test: `tools/memory_tool_store.py` sha256 `a43818a6…1586a` (#141876 head `6609dac`).
Bundle: hermes_constants · hermes_dir_acl · utils (verbatim: TRUTHY_STRINGS, is_truthy_value,
_atomic_write, atomic_write_text) · tools/{memory_tool_store, threat_patterns} — all real files;
named seams only where the tool-surface is out of scope:
- `tools/memory_tool.py` — real head (through line 476); the final `registry.register("memory", …)`
  block (real lines 477-492) declared out of scope (the agent-surface registration, not the read path).
- `tools/registry.py` — mirrors the real `no_cache_check_fn` decorator (tools/registry.py:272-275).

Cells (12): store read memory · sanitized view (BLOCKED marker + blocked index, no leak) ·
user-target read · empty-file read · corrupt-file read (read_ok=False, nothing changed) ·
dispatch arm (memory(action='read')) · twice-read identical · file hash unchanged ·
structural 50/50 inside / 50/50 outside · live read-held probe.

Run (three contours, one command each):
- pve1:        python3 hybrid_battery.py readkit-bundle
- WSL2:        bash -lc "cd /mnt/c/Users/c0wb0y; python3 hybrid_battery.py /mnt/c/Users/c0wb0y/readkit-bundle"
- native Win:  cmd.exe /c "py -3 C:\Users\c0wb0y\hybrid_battery.py C:\Users\c0wb0y\readkit-bundle"

2026-11-27 receipts: 36/36 cells green (12 × 3 contours). Forensics notes: (1) harness must
write explicit UTF-8 — the ANSI codepage default (cp1252 on py3.14) produces lone 0xA7 bytes that
the store's STRICT utf-8-sig read refuses (read_ok=False) — the wipe-class guard, demonstrated;
(2) the wrapper derives the lock path from the MEMORY file (probe the MEMORY path, not the .lock).
