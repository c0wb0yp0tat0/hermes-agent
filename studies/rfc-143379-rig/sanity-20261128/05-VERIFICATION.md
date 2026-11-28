# VERIFICATION — the hardened read, three contours (2026-11-27, closed)

The fixed read (#141876 artifact `tools/memory_tool_store.py`, sha256 `a43818a6…1586a`,
PR head `6609dac`) — the SAME files — run as one hybrid battery on three real contours.
Method follows the data-forensics trio (defect-forensics / investigation-documentation /
agent-work-review) and the think-tank spine (classify → probe → evaluate → adopt →
standardize → verify). Every claim below carries its receipt; nothing posted.

## The receipts (same battery, same artifact, three interpreters)

| contour | backend | python | host | entries | blocked idx | threat leaked | twice-read | hash unchanged | inside/outside (50) | live-held (80 probes) |
|---|---|---|---|---|---|---|---|---|---|---|
| pve1 | fcntl | 3.13.5 | linux | 3 (1 BLOCKED) | [1] | false | true | true | 50 / 50 | 25·26·23 |
| WSL2 (the PC) | fcntl | 3.11.9 | DESKTOP-8R44VEP | 3 (1 BLOCKED) | [1] | false | true | true | 50 / 50 | 52·25 |
| Windows native | **msvcrt** | 3.14.7 | windows | 3 (1 BLOCKED) | [1] | false | true | true | 50 / 50 | **5**·10 |

The BLOCKED view (all three, byte-identical shape):
`[BLOCKED: MEMORY.md entry contained threat pattern(s): prompt_injection, leak_system_prompt.
Withheld from the model-facing view. memory(action=remove, target='memory') removes it when you
have the entry text; otherwise the user can delete it in the file.]`

## What each row proves (the three field points, answered with receipts)

1. **Sanitize (3oltan point 1)** — the read's own outputs are threat-scanned: the view carries the
   `[BLOCKED: …]` marker, `blocked` names the index (entry stays addressable for removal), and the
   threat text is ABSENT from the view on every contour (`threat_text_leaked: false`).
2. **Windows lock (3oltan point 2)** — the REAL `msvcrt.locking` path, on REAL Windows py 3.14.7:
   structural both directions 50/50, and the live read-held probe blocked 5/80 while `read()`
   looped — the read holds a real lock on Windows, not a no-op. WSL2 on the same PC (real fcntl,
   WSL2 kernel) 50/50 + 52/80. 3oltan's contour-verification demand is met with real numbers.
3. **Stateless (kvnloo spec (1))** — twice-read byte-identical on every contour; the memory file's
   sha256 unchanged across reads (a read that races a writer leaves the live list alone).
4. **The structural check is the only lock test that can go red (kvnloo's row 3)** — our battery
   uses his exact hook shape: NBLCK on `MEMORY.md.lock` from a second fd; refused 50/50 inside,
   acquired 50/50 outside — both backends, three contours.

## Discovery log (the forensics arc — what actually happened)

1. Local read test of the INSTALLED store (spec-2 shape, no lock held): read answers both anchors
   (11 + 13 entries), twice-read stable, hash unchanged — but this session's tool surface exposes
   no read action (documented contract: the official docs state "There is no `read` action"; PR
   #12831 shows the maintainer-side refusal the child's evidence answers).
2. Kit artifact located: the fixed store = `_AOA-RERUN-20261123/tools/memory_tool_store.py`
   (sha `a43818a6…1586a` — kvnloo's own cited file id, the PR head `6609dac`).
3. Hybrid bundle built (all real): store, threat_patterns, hermes_constants, hermes_dir_acl,
   utils (verbatim: TRUTHY_STRINGS, is_truthy_value, _atomic_write, atomic_write_text),
   memory_tool (real head; the final `registry.register` block declared as a named seam — the
   tool-surface registration, not the read path), registry (seam mirroring the real
   `no_cache_check_fn` decorator, tools/registry.py:272-275). Import surface measured per defect
   (each ModuleNotFoundError traced to its real file or declared seam).
4. **My-test artifact caught by measurement:** the wrapper probe initially counted 0/50 blocked —
   the wrapper derives the lock file from the MEMORY path (`MEMORY.md` → `MEMORY.md.lock`), so
   probing with the lock path itself locks `MEMORY.md.lock.lock`. Passed the MEMORY file → 50/50.
5. **Windows-native empty-read defect caught by measurement:** the battery wrote the temp store
   WITHOUT an explicit encoding; on Windows py 3.14.7 the default is the ANSI codepage (cp1252) —
   `§` became a lone `0xA7` byte, invalid UTF-8. The store's STRICT `utf-8-sig` read refused it
   (`read_ok=False`, the wipe-class guard working as designed). Harness fixed (encoding="utf-8");
   all three contours then green, byte-identical.
6. kvnloo check (per the operator's steer): his two comments are macOS/fcntl-only (Python
   3.15.2); he never mentions Windows or the msvcrt path; his structural hook pattern (the
   NBLCK-inside-read probe) is exactly the shape our battery runs. The Windows contour is
   3oltan's concern (point 2) — now closed with real numbers.

## Telegram (gateway) session — the requested confirmation line

The read kit was exercised LIVE from this Telegram gateway session: the installed store's read
answered both anchors from right here (11 memory + 13 user entries, twice-read identical, file
hashes unchanged) and the FIXED artifact ran the full battery from this same session (pve1 row
above). Confirmed: **a Telegram (gateway) session works with the read kit** at the store layer.
The session's documented tool surface carries no read action (official docs: "There is no `read`
action — memory content is automatically injected into the system prompt at session start"), which
is the child's ask: restore the read AND wire the surface it reaches through.

## Live-held counts — dual-run provenance (C1 reconciliation, hy4 20261127)

Two real runs produced two count sets: run 1 (the 12-cell battery, first shoot) 25/52/5; run 2
(the extended battery, final shoot, the receipts cited in the wave) 26/25/10; the fold's dry
re-run read a third (23 on pve1). All are true receipts; the counts are scheduling-dependent
(probe cadence vs the read's hold window) and the binary signal — probes REFUSED while read()
ran — held on every contour in every run. The structural 50/50 rows are the deterministic
receipts; the live-held row is a presence signal. Cite by run; never mix the sets. The C1 flag
from hy4's lane-landing (2026-11-27) is resolved by this provenance note, not silently.

## Limitations (stated, not hidden)

- Windows-native coverage runs the real artifact's lock + read + sanitize on the real interpreter;
  the full 35-cell battery was not ported byte-for-byte (the bundle is the read-relevant import
  surface, not the whole repo). The cells this battery covers are the ones the three field points
  name.
- The live-held probe counts are scheduling-dependent (run 1: 25/52/5 — run 2: 26/25/10 — fold dry re-run: 23 — the read's hold window
  vs probe cadence); the SIGNAL is binary: probes were refused while the read ran on every
  contour. The structural 50/50 rows are the deterministic receipts.
- WSL2 python is the fleet's real python for the WSL contour; native py 3.14.7 is the PC's real
  Windows Python. Both official install contours (docs: install.sh for Linux/macOS/WSL2,
  install.ps1 for Windows native).

## Reproducibility

- Bundle: `readkit-bundle/` (hermes_constants, hermes_dir_acl, utils, tools/{__init__,
  memory_tool_store, memory_tool, threat_patterns, registry}) — store sha `a43818a6…1586a`.
- Battery: `hybrid_battery.py` — one file, three commands:
  - pve1: `python3 hybrid_battery.py <bundle>`
  - WSL2: `bash -lc "cd /mnt/c/Users/c0wb0y; python3 hybrid_battery.py /mnt/c/Users/c0wb0y/readkit-bundle"`
  - native: `cmd.exe /c "py -3 C:\Users\c0wb0y\hybrid_battery.py C:\Users\c0wb0y\readkit-bundle"`
- Store sha check: `sha256sum <bundle>/tools/memory_tool_store.py` → `a43818a6…1586a`.

## Think-tank spine classification

Classify: "can we gain the pilot kit's benefits on our layer" → the read fix exists in the kit and
is portable. Probe: the three-contour battery above. Evaluate: all green on fcntl AND msvcrt,
sanitized, stateless. Adopt: the battery becomes a standard leg of the kit's verification
(the Windows leg 3oltan asked for — real, runnable, one command). Standardize: the bundle +
battery ship with the kit; the contour table is the receipt shape. Verify: hashes + the table.

## Next actions (all wait the pair's word — nothing posted)

1. Commit the prediction (PREDICTION-KVNLOO-6609DAC-ROWS.md, hash 337e87d1…e0e7) — the only
   pending PUBLIC write; kvnloo runs the 6609dac re-run cold, posts the hash = the landed step.
2. Post the two replies: kvnloo (the decision + the adoption on his 6609dac rows) and 3oltan
   (three points answered with the receipts above).
3. Apply the child edits E1-E5 (gist 577535cda874a7fc483ff9c69d5d6c86) + E6 (answer PR #12831's
   maintainer rationale: "entries are already in the prompt" — the frozen snapshot is exactly what
   a cold topic cannot answer from; the pre-registered falsifier measures that).
