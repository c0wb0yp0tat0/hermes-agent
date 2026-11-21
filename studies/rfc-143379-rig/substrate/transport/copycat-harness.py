#!/usr/bin/env python3
"""copycat-harness.py — the minimal agentic tool-loop for the copycat fleet.
Per-base bounded loop: the model's tool_calls executed locally (read/write under the
study, list, git-only terminal), loop until the artifact lands or the bound.
The register: receipts, never claims — the lane's output is the verdicts; the head verifies.
"""
import argparse, base64, hashlib, json, os, re, subprocess, sys, time, urllib.request

ENDPOINT = os.environ.get(
    "HARNESS_ENDPOINT",
    "https://inference-api.nousresearch.com/v1/chat/completions",
)
def _key():
    k = os.environ.get("LM_API_KEY", "")
    if k:
        return k
    try:
        a = json.load(open("/root/.hermes/auth.json"))
        n = (a.get("providers") or {}).get("nous", {})
        for cand in ("agent_key", "access_token"):
            if n.get(cand):
                return n[cand]
    except Exception:
        pass
    try:
        for line in open("/root/.hermes/.env"):
            if line.startswith("LM_API_KEY="):
                return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
    except Exception:
        pass
    return ""
KEY = _key()
STUDY = "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig"
GIT_ALLOW = re.compile(r"^(git|cd\s+[^;&|]*?&&\s*git|gh\s+api).*")
# THE WRITE-WINDOW'S TERMINAL GATE (the 5-why's countermeasure, harness-enforced
# 11-07): the read_tools gate while the terminal stayed open - the run4 death-
# class. Once the window opens, content-reads through the terminal are blocked
# too (git show/log/grep/blame/diff, cat/grep/sed/...); the write-path's git
# verbs (add/commit/push/pull/status/ls-files/diff --quiet/rev-parse) stay open.
_TERM_READ_RE = re.compile(
    r"\bgit\s+(?:show|log|grep|blame|rev-list|cat-file|diff)(?!\s*--quiet)"
    r"|\b(?:cat|grep|sed|head|tail|find|sort|uniq|wc|less|more|awk|vim?|nano)\b"
)

TOOLS = [
    {"type": "function", "function": {"name": "read_file", "description": "Read a text file (study files, briefs). Supports offset (1-based line) and limit for paging large files; a long file that exceeds the view returns a head+tail window with the middle elided and a continuation hint.", "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "offset": {"type": "integer", "description": "1-based line to start from (default 1)"}, "limit": {"type": "integer", "description": "max lines to return (default 300)"}}, "required": ["path"]}}},
    {"type": "function", "function": {"name": "write_file", "description": "Write the finding file relative to the study.", "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}}},
    {"type": "function", "function": {"name": "list_dir", "description": "List a directory.", "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
    {"type": "function", "function": {"name": "terminal", "description": "Run a command (the git write-verbs are the commit-flow's allowed set; reads may be gated during the write-window; execution is otherwise available).", "parameters": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}}},
]

def _parse_prose_call(content):
    """THE RECOVERY PARSER (the middleware's promised class, earned 11-11): the small-seat
    family emits tool-calls as <tool_call>name<arg_key>k</arg_key><arg_value>v</arg_value>
    </tool_call> markup in content instead of the structured field. Parse it into a real call."""
    m = re.search(r"<tool_call>([A-Za-z_]+)(.*?)</tool_call>", content or "", re.S)
    if not m:
        return None
    name = m.group(1)
    args = {}
    for am in re.finditer(r"<arg_key>([A-Za-z_]+)</arg_key><arg_value>(.*?)</arg_value>", m.group(2), re.S):
        args[am.group(1)] = am.group(2)
    try:
        args = {k: json.loads(v) if (v[:1] in "[{") else v for k, v in args.items()}
    except Exception:
        pass
    return {"name": name, "args": args}


def _merge_adjacent_assistants(msgs):
    """THE ADJACENT-ASSISTANT GUARD (earned 11-11, the tool-drop seam's root): the
    windowed history can split one assistant turn (content vs tool_calls), producing
    adjacent assistant entries — a known compat-bug shape that providers reject as a
    wrongly-layer'd 404 (kenari's provider-rejection passthrough). Merge them first."""
    out = []
    for m in msgs:
        if m.get("role") == "assistant" and out and out[-1].get("role") == "assistant":
            prev = out[-1]
            pc = prev.get("content") or ""
            nc = m.get("content") or ""
            prev["content"] = (pc + "\n" + nc).strip() or None
            prev["tool_calls"] = (prev.get("tool_calls") or []) + (m.get("tool_calls") or [])
        else:
            out.append(dict(m))
    return out


def _ensure_tool_pairing(msgs):
    """THE TOTAL PAIRING PASS (earned 11-12, the ARC-BACKWARD crash): the edge-slide
    guards only the window's first tool-role — a mid-window tool whose assistant-pair
    was trimmed away still trips the provider's 400. Drop every tool-role that lacks
    its preceding assistant-tool_calls pair; keep the pair when both survive. AND the
    mirror-class (the R2 400): an assistant with tool_calls whose responses were
    trimmed out the other side gets its tool_calls cleared — an unanswered call rides
    no claim, and the plain content stays."""
    out = []
    for i, m in enumerate(msgs):
        if m.get("role") == "tool":
            # the SCAN-BACK (11-12): the merge shifts indices — the tool's pair may sit
            # several messages above, not at i-1; find the nearest assistant whose calls
            # actually carry this tool_call_id.
            matched = False
            for j in range(i - 1, -1, -1):
                prev = msgs[j]
                prev_calls = prev.get("tool_calls") or []
                if any(tc.get("id") == m.get("tool_call_id") for tc in prev_calls if tc.get("id")):
                    matched = True
                    break
                if prev.get("role") == "tool" and j < i - 1:
                    continue  # skip over tool-rows; keep scanning
            if not matched:
                if os.environ.get("HARNESS_DUMP_MSGS") == "1":
                    with open("/tmp/harness-msg-dump.json", "a", encoding="utf-8") as _df:
                        _df.write(json.dumps({"PAIR-DROP": m.get("tool_call_id"), "scanback": True}) + "\n")
                continue  # the orphaned result rides no claim — drop it (scan-back, 11-12)
        out.append(dict(m))
    # the reverse pass: unanswered tool_calls cleared
    for i, m in enumerate(out):
        tcs = m.get("tool_calls") or []
        if not tcs:
            continue
        needed = {tc.get("id") or f"call_{i}" for tc in tcs}
        answered = set()
        for j in range(i + 1, min(i + 1 + len(tcs) * 2, len(out))):
            if out[j].get("role") == "tool":
                cid = out[j].get("tool_call_id")
                if cid:
                    answered.add(cid)
        if not needed.issubset(answered):
            m["tool_calls"] = None  # the answered-less call rides no claim
            m["content"] = m.get("content") or ""  # and an empty call-message still needs its content field
    return out


def call(messages, model, _attempts=5):
    import time as _t
    _retry_codes = {
        int(c.strip())
        for c in os.environ.get(
            "HARNESS_RETRY_CODES", "429,500,502,503"
        ).split(",")
        if c.strip().isdigit()
    }
    _pacing = float(os.environ.get("HARNESS_CALL_DELAY", "0") or 0)
    if _pacing > 0:
        _t.sleep(_pacing)
    _payload = {"model": model, "messages": _ensure_tool_pairing(_merge_adjacent_assistants(messages)), "max_tokens": int(os.environ.get("HARNESS_MAX_TOKENS", "8192"))}
    if os.environ.get("HARNESS_KEYLESS") != "1" and os.environ.get("HARNESS_NO_TOOLS") != "1":
        _payload["tools"] = TOOLS
    body = json.dumps(_payload).encode()
    if os.environ.get("HARNESS_DUMP_MSGS") == "1":
        with open("/tmp/harness-msg-dump.json", "a", encoding="utf-8") as _df:
            _df.write(json.dumps({"model": model, "msgs": _payload.get("messages"), "tcs": [_m.get("tool_calls") for _m in _payload.get("messages", [])]}) + "\n")
        with open("/tmp/harness-msg-dump.json", "a", encoding="utf-8") as _df:
            _df.write(json.dumps({"before_n": len(messages), "after_n": len(_payload.get("messages")), "raw_tool_count": sum(1 for m in messages if m.get("role") == "tool"), "sent_tool_count": sum(1 for m in _payload.get("messages") if m.get("role") == "tool")}) + "\n")
    _headers = {
        "Content-Type": "application/json",
        "User-Agent": os.environ.get("HARNESS_UA", "python-urllib/3.13"),
        "Accept": "application/json",
    }
    if os.environ.get("HARNESS_KEYLESS") != "1":
        _headers["Authorization"] = f"Bearer {KEY}"
    req = urllib.request.Request(ENDPOINT, data=body, headers=_headers)
    for n in range(_attempts):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                _resp = json.loads(r.read().decode())
                _u = (_resp.get("usage") or {})
                if _u.get("prompt_tokens") is not None:
                    try:
                        with open("/root/workspace/drop/backwards-audit/FLEET-TOKENS-20261111.jsonl", "a", encoding="utf-8") as _tf:
                            _tf.write(json.dumps({"t": time.time(), "model": model, "endpoint": ENDPOINT,
                                                  "prompt": _u.get("prompt_tokens"), "completion": _u.get("completion_tokens"),
                                                  "total": _u.get("total_tokens"),
                                                  "req_bytes": len(body)}) + "\n")
                    except Exception:
                        pass
                return _resp
        except urllib.error.HTTPError as e:
            _body = ""
            try:
                _body = e.read().decode(errors="replace")[:300]
            except Exception:
                pass
            if e.code in _retry_codes and n < _attempts - 1:
                _t.sleep(min(30 * (2 ** n), 240))
                continue
            if _body:
                raise urllib.error.HTTPError(e.url, e.code, "%s | body: %s" % (e.reason, _body), e.headers, None) from None
            raise
        except Exception:
            if n < _attempts - 1:
                _t.sleep(min(30 * (2 ** n), 240))
                continue
            raise

# THE MODULE-LEVEL LOG (2026-11-19, the 'name log is not defined' ROOT fix):
# log was a closure inside main() but execute() (module scope) called it — every
# post-write log raised NameError, so lanes saw a tool error on SUCCESSFUL writes
# and fell back to stubs (L-2's 5-byte 'hello', L-4's 60-byte stub, kenari's
# write-spiral). One definition, both scopes, one file handle via the global.
_logf = None


def log(*parts):
    line = " ".join(str(p) for p in parts)
    try:
        print(line, flush=True)
    except BrokenPipeError:
        pass
    if _logf is not None:
        try:
            _logf.write(line + "\n")
            _logf.flush()
        except Exception:
            pass


def parse_args(fn_name, raw):
    """Parse a model's tool-call arguments across emission formats: OpenAI JSON,
    the longcat-style markup (<name_arg_key>/<name_arg_value>), or bare fallback."""
    if not raw:
        return {}
    raw = raw.strip()
    keys = re.findall(r"<[^>]*arg_key>(.*?)</[^>]*arg_key>", raw, re.S)
    vals = re.findall(r"<[^>]*arg_value>(.*?)</[^>]*arg_value>", raw, re.S)
    if keys and len(keys) == len(vals):
        return dict(zip(keys, vals))
    try:
        return json.loads(raw)
    except Exception:
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
    # THE DOUBLE-ENCODE UNWRAP (G15, earned 2026-11-15 — the livekit PR #5409 class):
    # a lane can emit a JSON-string-inside-a-JSON-string ("...{\"path\":\"...\"}...") —
    # the direct parse above fails, but the payload is recoverable. Unwrap up to two
    # encoding levels; dispatch only when an OBJECT emerges; log the repair. Direct-
    # parse-first is preserved (well-formed args never enter this path), truncation
    # stays an error (no object emerges -> {} falls through to the caller's guard).
    _unwrapped = raw
    for _level in (1, 2):
        if not (_unwrapped.startswith('"') and _unwrapped.endswith('"')):
            break
        try:
            _candidate = json.loads(_unwrapped)
        except Exception:
            break
        if isinstance(_candidate, dict):
            log("[EMISSION-REPAIR] double-encoded args unwrapped (level %d)" % _level)
            return _candidate
        if not isinstance(_candidate, str):
            break
        _unwrapped = _candidate
    return {}

def execute(name, args):
    try:
        if name == "read_file":
            p = args["path"]
            ok_root = (p.startswith(STUDY) or p.startswith("/root/.hermes/cache/scratch")
                       or p.startswith("/root/.hermes/skills") or p.startswith("/root/workspace/master-page")
                       or p.startswith("/root/workspace/repos/hermes-agent/skills")
                       or p == "/root/.hermes/memories/MEMORY.md" or p == "/root/.hermes/memories/USER.md"
                       or p.startswith("/root/.hermes/memories"))
            if not ok_root:
                return {"error": "path outside the allowed roots"}
            # THE READ-PAGING CONTRACT (our own adoption of the field's answers, 2026-11-18:
            # offset/limit pagination (Pi, Claude Code), the head+tail window at truncation
            # (OpenClaw's 75/25), and the hint that tells the lane to page (Pi's pattern) —
            # the read boundary that starved seven lanes tonight becomes a paged surface.)
            _off = int(args.get("offset", 1) or 1)
            _lim = int(args.get("limit", 300) or 300)
            with open(p, encoding="utf-8", errors="replace") as f:
                _lines = f.readlines()
            _total = len(_lines)
            _start = max(0, _off - 1)
            _chunk = _lines[_start:_start + _lim]
            _out = "".join(_chunk)
            # THE SCRIBE-CELL FALLBACK (B1, the nightshift's fire — the read-substrate's
            # Layer 2, wired: on presence of READ_SUBSTRATE_MODE=cells, the local paged
            # read becomes the CELL-backed read: the artifact's FULL bytes come from the
            # scribe's cell (the write-time assert + the bridge guarantee they're there),
            # paged locally with the same contract, byte-verified — the kit reads when
            # the provider never restores. Failures named, never silent.
            if os.environ.get("READ_SUBSTRATE_MODE", "cells") == "cells":
                try:
                    _cell = "rig-" + os.path.basename(p).lower().replace(".md", "").replace(".", "-")
                    _g = json.loads(urllib.request.urlopen(urllib.request.Request(os.environ.get("SCRIBE_URL", "http://127.0.0.1:24282") + "/get_memory", data=json.dumps({"memory_name": _cell}).encode(), headers={"Content-Type": "application/json"}), timeout=20).read().decode())
                    _back = _g.get("content") or ""
                    if _back and hashlib.sha256(_back.encode()).hexdigest() == hashlib.sha256("".join(_lines).encode()).hexdigest():
                        _blines = _back.splitlines(keepends=True)
                        _btotal = len(_blines)
                        _bchunk = _blines[max(0, _off - 1):max(0, _off - 1) + _lim]
                        _bout = "".join(_bchunk)
                        if len(_bout) > 12000:
                            _btail = max(0, len(_bout) - 3000)
                            _bout = _bout[:_btail] + "\n[... middle elided at read-time ...]\n" + _bout[_btail:]
                        log(f"[read-substrate] {os.path.basename(p)}: cell-backed read (provider-absent mode), {_btotal} lines, byte-verified")
                        return {"content": _bout, "page": {"offset": _off, "limit": _lim, "total_lines": _btotal, "source": "scribe-cell", "hint": "use offset/limit to page further (e.g. offset=" + str(_off + _lim) + ")"}}
                    log(f"[read-substrate] {os.path.basename(p)}: CELL-BYTE-MISMATCH or NO-CELL — falling back to the local read (named, never silent)")
                except Exception as _re:
                    log(f"[read-substrate] {os.path.basename(p)}: CELL-UNREADABLE ({_re}) — falling back to the local read (named, never silent)")
            if _out and len(_out) > 12000 or (_off == 1 and _total > _start + _lim):
                # the head+tail window: keep the first 75% and last 25% of the requested view
                _body = _out if _out else ""
                if len(_body) > 12000:
                    _tail_start = max(0, len(_body) - 3000)
                    _body = _body[:_tail_start] + "\n[... middle elided at read-time ...]\n" + _body[_tail_start:]
                return {"content": _body, "page": {"offset": _off, "limit": _lim, "total_lines": _total,
                    "hint": "use offset/limit to page further (e.g. offset=" + str(_off + _lim) + ")"}}
            return {"content": _out, "page": {"offset": _off, "limit": _lim, "total_lines": _total}}
        if name == "write_file":
            p = args["path"]
            # THE RELATIVE-PATH RESOLUTION (earned 2026-11-15, the write-gate wall): lanes
            # trim the brief's absolute STUDY prefix to a CWD-relative form ("studies/...");
            # resolve against the harness's CWD (the repo root) so a relative write under
            # the study is accepted, never bounced as "outside the study".
            if not p.startswith("/"):
                p = os.path.normpath(os.path.join(os.getcwd(), p))
            if not (p.startswith(STUDY) and p.endswith(".md")):
                return {"error": "write allowed only under the study, .md only"}
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as f: f.write(args["content"])
            try:
                open(p + ".sentinel", "w").close()
            except Exception:
                pass
            # THE WRITE-TIME SCRIBE ASSERT + STUB SCAN (our own invention, 2026-11-18,
            # Nemo's scribe-write plan, candidate (a)+(b) — the two-way door rides it):
            # every lane write asserts its bytes into the scribe's cell as it lands
            # (the fold's bridge re-verifies the complete artifact), and the stub
            # scan runs at write time with the SIZE-HEURISTIC (a stub is small:
            # markers in a tiny artifact flag; a document ABOUT the scan, which
            # legitimately names the markers at length, does not).
            _flags = []
            try:
                _cell = "rig-" + os.path.basename(p).lower().replace(".md", "").replace(".", "-")
                _req = urllib.request.Request(os.environ.get("SCRIBE_URL", "http://127.0.0.1:24282") + "/save_memory", data=json.dumps({"memory_name": _cell, "content": args["content"]}).encode(), headers={"Content-Type": "application/json"})
                urllib.request.urlopen(_req, timeout=20)
                _g = json.loads(urllib.request.urlopen(urllib.request.Request(os.environ.get("SCRIBE_URL", "http://127.0.0.1:24282") + "/get_memory", data=json.dumps({"memory_name": _cell}).encode(), headers={"Content-Type": "application/json"}), timeout=20).read().decode())
                _back = _g.get("content") or json.dumps(_g)
                if hashlib.sha256(_back.encode()).hexdigest() != hashlib.sha256(args["content"].encode()).hexdigest():
                    _flags.append("SCRIBE_MISMATCH")
                    log(f"[scribe-write] {os.path.basename(p)}: SCRIBE_MISMATCH on the write")
            except Exception as _e:
                _flags.append("SCRIBE_UNREACHABLE")
                log(f"[scribe-write] {os.path.basename(p)}: SCRIBE_UNREACHABLE ({_e})")
            _low = args["content"].lower()
            if any(m in _low for m in ("placeholder", "tbd", "(skeleton", "being filled")) and len(args["content"]) < 2000:
                _flags.append("STUB_DETECTED")
                log(f"[scribe-write] {os.path.basename(p)}: STUB_DETECTED (write-time scan, {len(args['content'])} bytes — treat as refused until re-fired)")
            # THE F1 WITNESS-HARDENING (SPRINT-FIRE-SEQUENCE F1, 2026-11-19):
            # every write also carries a checkpoint row binding cell_hash -> commit SHA
            # -> branch, so the scribe's witness survives independently of the scribe
            # machine (the external-anchoring pattern from DEEP-STORM-SEAM-3). The row
            # is non-destructive (append-only registry) and the whole F1 gate disarms
            # via SCRIBE_HARDENING_OFF in the environment.
            if not os.environ.get("SCRIBE_HARDENING_OFF"):
                try:
                    import hashlib as _hl
                    _chk = """%s|%s|%s|%s""" % (
                        os.path.basename(p), _hl.sha256(args["content"].encode()).hexdigest()[:16],
                        os.environ.get("GIT_HEAD", "HEAD"), os.path.basename(os.getcwd()))
                    _reg = os.path.join(os.path.dirname(p), "SCRIBE-WITNESS-REGISTRY.log")
                    with open(_reg, "a") as _f:
                        _f.write(_chk + "\n")
                    log(f"[scribe-write] {os.path.basename(p)}: WITNESS-ROW appended")
                except Exception as _e:
                    _flags.append("WITNESS_ROW_FAILED")
                    log(f"[scribe-write] {os.path.basename(p)}: WITNESS_ROW_FAILED ({_e})")
            if _flags:
                log(f"[scribe-write] {os.path.basename(p)}: flags={','.join(_flags)}")
            # THE WRITE-SUCCESS ENVELOPE (2026-11-19, the 'name log is not defined' class):
            # lanes misread any scribe-flag as a failed write and fell back to minimal
            # stubs (hy4's L-4 60-byte stub, kenari's write-spiral). The write ALWAYS
            # lands — the flags are traffic lights on the sidecar, not verdicts on the
            # file. Lead with the unambiguous contract; keep the flags as a separate
            # field so a lane that reads carefully still sees them.
            return {"ok": "WRITTEN", "status": "the file is on disk and this is a SUCCESS",
                    "path": p, "bytes": len(args["content"]),
                    "scribe_flags": _flags or None}
        if name == "list_dir":
            return {"entries": os.listdir(args["path"])[:50]}
        if name == "terminal":
            cmd = args["command"]
            # THE GIT-INIT REFUSAL (earned 2026-11-15, the nested-repo debris class): a lane
            # that git-inits inside the study creates a nested repo — the branch never moves,
            # lane commits land in the void, and the fold verdict reads MISSING. Refused.
            if re.search(r"(?i)\bgit\s+init\b", cmd):
                return {"error": "git init is refused for lanes — the nested-repo class; the harness folds to the study branch"}
            if not GIT_ALLOW.match(cmd):
                return {"error": "terminal is git-only for lanes"}
            r = subprocess.run(["bash", "-lc", cmd], capture_output=True, text=True, timeout=120)
            return {"exit": r.returncode, "out": r.stdout[-3000:], "err": r.stderr[-2000:]}
    except Exception as e:
        return {"error": str(e)}
    return {"error": "unknown tool"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--rounds", type=int, default=40)
    ap.add_argument("--logfile", default="")
    a = ap.parse_args()
    import time as _t2
    global _logf
    _logf = open(a.logfile, "a") if a.logfile else None
    # (log is module-level since 2026-11-19 — the NameError root fix; the old inner
    # closure is gone so execute() and main() share one definition and one handle)
    # THE WRITE-WINDOW GATE: once the remaining rounds hit the write-window,
    # the read-tools refuse — the lane's only productive path is the write.
    # THE WRITE-WINDOW'S KNOBS (the S4-reapex's wiring, env-guarded; the default path stays byte-identical)
    _ww_min = int(os.environ.get("WRITE_WINDOW_MIN", "12"))
    _ww_ratio = int(os.environ.get("WRITE_WINDOW_RATIO", "3"))
    write_window = max(_ww_min, a.rounds // _ww_ratio)
    # THE WINDOW-CAP FIX (2026-11-17, earned: two lanes read-gated from round 0
    # because max(12, rounds//3) >= rounds for any run with rounds <= 18 — a
    # lane born inside its own window could never read, and folded "not
    # confirmed" artifacts instead of measurements). The window is the TAIL,
    # never the whole run: cap it at rounds-4 (>=1), so the analysis phase
    # (first half of small runs) keeps its reads and the write phase is what
    # gets gated. Runs >= 36 rounds keep the old value → byte-identical there.
    write_window = min(write_window, max(1, a.rounds - 4))
    # THE WRITE-DEADLINE BRIEF-KNOB (the countermeasure's config half): a brief
    # line "write-window: N" (or "deadline: N") names the round at which the
    # window opens - the brief-written arm's own transport, harness-enforced.
    brief = open(a.brief).read()
    _wm = re.search(r"(?im)^\s*(?:write[-_]window|write[-_]deadline|deadline)\s*[:=]\s*(\d+)\s*$", brief)
    if _wm:
        write_window = int(_wm.group(1))
        log("[deadline] write-window opens at round", write_window)
    _reads_blocked = False
    # THE LANDING GATE (earned 11-06): the disk-write is not the landing — the
    # branch's movement is. The done-rule requires the sentinel AND the branch's
    # head having moved since the run started (the night's banked refinement
    # "the done will require the sentinel AND the branch-head's movement", now
    # wired: a lane that wrote but never committed keeps its rounds and must
    # finish the git flow before the run may end).
    _START_HEAD = subprocess.run(
        ["bash", "-lc", "cd /root/workspace/repos/hermes-agent && git rev-parse --short HEAD"],
        capture_output=True, text=True).stdout.strip() or "?"
    import os as _os
    _START_MTIME = _os.path.getmtime(a.artifact) if _os.path.exists(a.artifact) else -1
    def _done():
        # THE LANDING CHECK (CDV, value-carrying): the lane is done only when it
        # itself wrote the artifact, AND the ARTIFACT is tracked at the branch's
        # head — a stale sentinel, a concurrent commit, or a pre-existing tracked
        # artifact must NOT satisfy the gate.
        try:
            if not os.path.exists(a.artifact + ".sentinel"):
                return False
            if not (_os.path.exists(a.artifact) and _os.path.getmtime(a.artifact) > _START_MTIME):
                return False
            r = subprocess.run(
                ["bash", "-lc", "cd /root/workspace/repos/hermes-agent && git ls-files --error-unmatch '%s' >/dev/null 2>&1" % a.artifact],
                capture_output=True, text=True)
            if r.returncode != 0:
                return False
            # THE ARTIFACT'S DISK MUST MATCH THE BRANCH'S TREE — a write that never
            # became a commit is not a landing (the adjudication's 5th edge: the
            # run wrote, an unrelated commit satisfied the remote-check, the lane
            # ended uncommitted).
            r = subprocess.run(
                ["bash", "-lc", "cd /root/workspace/repos/hermes-agent && git diff --quiet HEAD -- '%s'" % a.artifact],
                capture_output=True, text=True)
            if r.returncode != 0:
                return False
            # THE REMOTE'S HEAD MUST EQUAL THE LOCAL HEAD — a commit that never
            # reached remote is NOT a landing (the network-line gap: local-commit,
            # push unreached; the gate's last edge).
            r = subprocess.run(
                ["bash", "-lc", "cd /root/workspace/repos/hermes-agent && test \"$(git rev-parse HEAD)\" = \"$(git ls-remote origin study/rfc-143379-rig-20261105 | head -1 | cut -f1)\""],
                capture_output=True, text=True)
            return r.returncode == 0
        except OSError:
            return False
    _sentinel = a.artifact + ".sentinel"
    system = ("You are the copycat lane of the RFC #143379 apex mission. You have tools for reading the study, "
              "writing your finding file, and git. EMISSION CONTRACT: work first (read the study files, form the "
              "adjudication), then write the finding file to the artifact path, then commit+push the study branch "
              "(git -c user.name='c0wb0yp0tat0' -c user.email='c0wb0yp0tat0@users.noreply.github.com' commit -q -m ..., "
              "git push origin study/rfc-143379-rig-20261105; on a rejected push: git pull --rebase origin study/rfc-143379-rig-20261105 then push). "
              f"Your final message after the artifact exists: the finding's one line + the next mechanism's one line. "
              f"STORM-CONTEXT (the standing harvest — every lane STRONGLY CONSIDERS these within its own work where relevant; design stays ours, corroboration of class, never adoption): DISCERN -> write-gate L0 + SPA-DREAM read path · MemCredit -> memory-economy rho=(V-lambda H)/b arbitration at bank · MAPE -> design-space search for inventions-live probes · CoMem -> fidelity-ladder L2 selection · Reward-Driven Collider -> AIMD adaptive-envelope reward · AskALCF -> evidence-gated RSI admission + commit gate · SELD -> read-side evidence-plane verifier · Evolving Infra -> agent-adaptive serving · the four misc -> compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation. "
              f"The artifact path: {a.artifact}. Here is the full mission brief:\n{brief}")
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": "Proceed with the mission brief above."}]
    done = _done()
    _nudged = False
    _content_only = 0  # THE TOOL-USE TRIPWIRE (earned 2026-11-11, the mistral one-shot's
    # ghost-run): a lane may drift in content-only rounds forever — content without tool-calls
    # is not work. Four silent rounds -> the enforcement nudge; eight -> the run is dead.
    for rnd in range(a.rounds):
        if done:
            break
        remaining = a.rounds - rnd
        if remaining <= 8 and not _nudged:
            messages.append({"role": "system", "content": f"ROUNDS LOW: you have {remaining} rounds left. If your analysis is complete, WRITE the finding/product file to {a.artifact} NOW (the write_file tool), then commit + push the study branch (the terminal tool). The file's existence is your success signal."})
            _nudged = True
        # THE SLIDING WINDOW (earned 2026-11-11, the four keyless 400s at the ~14-call frame):
        # the request-body grows unbounded per round; the trim keeps the system+mission + the recent 20
        # exchanges — the route's parse-buffer never sees the accumulated archive, and the artifact
        # remains the persistent store (the window is the working-set, never the memory's replacement).
        # THE RE-GROUNDING CLAUSE (earned 2026-11-11, the P1-safety class): a trim that rolls the
        # ground off creates partial-picture reasoning — so the trim FIRST preserves the most recent
        # read_file exchange touching the artifact (the persistent store's content stays in-window,
        # mechanically, every round).
        _artifact_keep = []
        if len(messages) > 24:
            for _i in range(len(messages) - 1, -1, -1):
                _c = messages[_i].get("content")
                if isinstance(_c, str) and a.artifact in _c:
                    # the API pairing rule: a tool-result must follow its assistant
                    # tool_calls message — keep the pair, never a lone result
                    _artifact_keep = [messages[_i - 1], messages[_i]] if _i > 0 else [messages[_i]]
                    break
        _tail = messages[-20:]
        if _tail and _tail[0].get("role") == "tool":
            _tail = messages[-21:]  # the edge-slide: a window that opens on a lone
            # tool-result breaks the API pairing — extend one message back for its pair
        _win = messages if len(messages) <= 24 else messages[:1] + _artifact_keep + _tail
        # THE STRICT-PAIR GUARD (earned 2026-11-15, the solar 400 class): the trimmed
        # window can orphan a tool-result whose assistant tool_calls slid out of the
        # slice — strict endpoints (solar-mini4) reject the lone result with a 400.
        # Deterministic fix: drop any tool-role message whose pairing assistant has
        # been trimmed out of the window. Never a lone result.
        _win = [_m for _i, _m in enumerate(_win)
                if not (_m.get("role") == "tool"
                        and (_i == 0 or _win[_i - 1].get("role") != "assistant"
                             or not (_win[_i - 1].get("tool_calls") or [])))]
        # THE BYTE-BUDGET BREAKER (G6, 2026-11-14 — the 131K wall's true root): the
        # sliding window bounds the COUNT, not the BYTES — a re-narrating lane's fat
        # contents stack past the endpoint's cap. Deterministic trim: while the
        # window's chars exceed the budget, slice the longest content to the 2K floor
        # with a trim marker. No LLM — the extractive fallback, always lands.
        _budget = int(os.environ.get("HARNESS_BUDGET_CHARS", "96000"))
        _trimmed = False
        while True:
            _tot = sum(len(str(m.get("content") or "")) for m in _win)
            _big = max(_win, key=lambda m: len(str(m.get("content") or "")), default=None)
            if _tot <= _budget or _big is None or len(str(_big.get("content") or "")) <= 2000:
                break
            _big["content"] = str(_big.get("content") or "")[:2000] + "\n[HARNESS-BUDGET: content trimmed to the 2K floor]"
            _trimmed = True
        if _trimmed:
            log("[budget] byte-trim applied (window exceeded", _budget, "chars)")
        # THE API-ERROR ISOLATION (G15-landed 2026-11-15, the copperhead PR #236 shape):
        # an HTTPError (400 protocol, 429 rate-limit) returns INTO the lane as a
        # visible tool-level result — the model sees "API_ERROR: <code> <reason>" and
        # can respond (wait, re-tool, compose) — instead of an uncaught abort that
        # kills the ride and loses the artifact (the apex-loop 400-kill class: round
        # 19's write died with upstream_rejected, artifact MISSING). The ride only
        # aborts when the SAME error reproduces N rounds in a row (deterministic).
        try:
            resp = call(_win, a.model)
        except urllib.error.HTTPError as _he:
            _err_text = "API_ERROR: %s %s" % (_he.code, (_he.reason or ""))
            try:
                _body = _he.read().decode(errors="replace")[:250]
                if _body:
                    _err_text += " | body: %s" % _body
            except Exception:
                pass
            log(f"[round {rnd}] {_err_text}")
            _api_errs = _api_errs + 1 if "_api_errs" in dir() else 1
            if _api_errs >= 3:
                log("[round %d] API-ERROR x3 — deterministic abort, receipted" % rnd)
                break
            # USER-ROLE injection (never a lone tool-role message — that would trip the
            # strict-pair guard and be stripped; a user message is API-safe and the lane
            # sees it reliably).
            _win.append({"role": "user", "content": _err_text})
            _t2.sleep(10 if _he.code == 429 else 8)
            continue
        try:
            msg = resp["choices"][0]["message"]
        except Exception:
            if not resp.get("choices"):
                log(f"[round {rnd}] EMPTY choices (throttle/format) — retrying")
                _t2.sleep(20)
                continue
            log("API ERROR:", str(resp)[:400]); break
        if msg.get("content"):
            log(f"[round {rnd}] ASSISTANT:", msg["content"][:400])
        rc = msg.get("reasoning_content")
        if rc:
            log(f"[round {rnd}] REASONING:", rc[:200])
        _prose = None if msg.get("tool_calls") else _parse_prose_call(msg.get("content"))
        if msg.get("tool_calls") or _prose:
            if _prose:
                # THE RECOVERY PARSER'S EXECUTION (11-11): the family's prose-call becomes
                # a real tool-call — executed exactly as a structured one would be.
                msg["tool_calls"] = [{"type": "function", "function": {"name": _prose["name"], "arguments": json.dumps(_prose["args"])}}]
                log(f"[round {rnd}] PROSE-CALL recovered: {_prose['name']}({json.dumps(_prose['args'])[:60]})")
            _content_only = 0
        elif len(msg.get("content") or "") >= 120 and not any(
                s in (msg.get("content") or "").lower()
                for s in ("expected output", "unable to execute", "apologies", "cannot run", "expected outcomes")):
            _content_only = 0  # the thick-content grace (2026-11-11): reasoning after an
            # execution is WORK — but rationalization-and-fabrication is drift (N1's lesson:
            # "unable to execute... I'll provide the expected output" is the ghost's tell)
        else:
            _content_only += 1
            if _content_only == 4:
                messages.append({"role": "user", "content": "TOOL-USE ENFORCEMENT: the last four rounds produced content only. The mission is not prose — execute a tool call now (the test command, a read, or the artifact write). A lane that will not use its tools is not working."})
            elif _content_only >= 8:
                log(f"[round {rnd}] DEAD-RUN: {_content_only} content-only rounds without a tool call — aborting the ghost")
                break
        # THE REASONING_PRESERVATION CLAUSE (earned 2026-11-11, run 42983091856's 400):
        # the beam bare-id route (post-:free-expiry) 400s on replayed assistant turns
        # whose reasoning_content was dropped ("Send it back in 'reasoning_content'");
        # the field rides the replay when the API returned it — the flag alone is not honored.
        _am = {"role": "assistant", "content": msg.get("content"), "tool_calls": msg.get("tool_calls")}
        if msg.get("reasoning_content"):
            _am["reasoning_content"] = msg["reasoning_content"]
        messages.append(_am)
        tcs = msg.get("tool_calls") or []
        if not tcs:
            done = _done()
            if not done:
                log(f"[round {rnd}] content-only (no tool calls, artifact absent) — continuing")
            continue
        if len(tcs) > 1:
            log(f"[round {rnd}] MULTI-CALL TRIMMED to the first call ({len(tcs)} requested) — the transport's all-or-nothing class (G7)")
            tcs = tcs[:1]
            # THE G7 TRANSCRIPT-CONSISTENCY (2026-11-14, the ENRICH-1 400): trimming
            # only the EXECUTED calls while the replayed assistant message still lists
            # every call_id replays answered-less ids next round — the fresh orphan-400
            # shape. The assistant message must carry exactly the executed call.
            _keep = tcs[0].get("id")
            if messages and messages[-1].get("role") == "assistant":
                messages[-1]["tool_calls"] = [tc for tc in (messages[-1].get("tool_calls") or []) if tc.get("id") == _keep]
        for tc in tcs[:1]:
            fn = tc["function"]
            log(f"[round {rnd}] CALL {fn['name']}", (fn.get("arguments") or "")[:200])
            args = parse_args(fn["name"], fn.get("arguments") or "")
            remaining2 = a.rounds - rnd
            # THE GATE'S CONTRACT-ALIGNMENT (earned 2026-11-08, the third fix): the gate's own
            # message promises "blocked until the artifact exists" — but the code keyed it to
            # _done() (sentinel AND branch-movement), so a lane that wrote its skeleton STILL
            # found every read gated until the commit landed, and the FULL lost the window —
            # the skeleton-class's root. The gate now opens at the artifact's EXISTENCE; the
            # landing-gate (the final check) still requires the branch's movement.
            if remaining2 <= write_window and not os.path.exists(_sentinel):
                # THE GIT-ONLY WHITELIST (earned 2026-11-08, sharpened fold-2): the window's
                # git is the LANDING-SET ONLY — add/commit/push/pull/status/rev-parse/
                # ls-remote (plus a one-line log for the landing-gate's verify) — never the
                # read-channel. The first fix's width (any "git") became the archaeology
                # channel: lanes mined history via git show/grep/log and burned the window
                # without writing. Content-reads stay gated (read_file/list_dir + the
                # terminal's non-landing git, e.g. show/grep/log-long/ls-tree/diff).
                _cmd = args.get("command", "") if fn["name"] == "terminal" else ""
                _trailing = _cmd.rsplit("&&", 1)[-1].strip() if _cmd.strip() else ""
                _git_only = bool(re.search(r"^git (add|commit|push|pull|status|rev-parse|ls-remote)(\s|$)", _trailing)) or bool(re.match(r"^git log --oneline -1(\s|$)", _trailing))
                if fn["name"] in ("read_file", "list_dir") or (
                        fn["name"] == "terminal" and not _git_only and _TERM_READ_RE.search(_cmd)):
                    res = {"error": "READ-GATED: the write-window is open (the artifact's due within %d rounds). The analysis-phase is over - WRITE your finding to the artifact path NOW with write_file, then commit+push with the terminal (git-only: add/commit/push/pull/status). The read-tools AND the terminal's content-reads stay blocked until the artifact exists." % remaining2}
                    _reads_blocked = True
                    log(f"[round {rnd}] READ-GATED (the write-window)" + (" [terminal]" if fn["name"] == "terminal" else ""))
                else:
                    res = execute(fn["name"], args)
            else:
                res = execute(fn["name"], args)
            messages.append({"role": "tool", "tool_call_id": tc["id"], "content": json.dumps(res)[:16000 if fn["name"] in ("read_file", "list_dir") else 4000]})
            done = _done()
    # THE SCRIBE BRIDGE (2026-11-18, operator-binding: Serena is part of the
    # substrate, never an afterthought — a lane fold that skips the scribe is a
    # fold that drops the operator's ask). Whenever the artifact's bytes exist,
    # the harness saves them into the scribe's store (cell name: "rig-" + the
    # artifact basename, lowercased) and byte-verifies the re-read. Env-guarded:
    # SCRIBE_URL (default http://127.0.0.1:24282); a failure is logged loudly,
    # never silent. This runs regardless of who committed the artifact.
    if os.path.exists(a.artifact):
        _sc = None
        try:
            _scribe = os.environ.get("SCRIBE_URL", "http://127.0.0.1:24282")
            _body = open(a.artifact, encoding="utf-8", errors="replace").read()
            # THE BRIEF-DECLARED CELL (2026-11-18, earned: the loop's plan names
            # canonical cells like rig-hy4-loop-spine; the bridge's auto-name
            # (basename-based) diverged, so the plan's cells stayed empty. A
            # brief line "scribe-cell: <name>" pins the cell the stage owns —
            # the auto-name is the fallback only.)
            _cell = None
            try:
                _bm = re.search(r"(?im)^\s*scribe[-_]cell\s*[:=]\s*([\w.-]+)\s*$", open(a.brief, encoding="utf-8", errors="replace").read())
                if _bm:
                    _cell = _bm.group(1).strip()
            except Exception:
                pass
            if not _cell:
                _cell = "rig-" + os.path.basename(a.artifact).lower().replace(".md", "").replace(".", "-")
            _req = urllib.request.Request(_scribe + "/save_memory", data=json.dumps({"memory_name": _cell, "content": _body}).encode(), headers={"Content-Type": "application/json"})
            urllib.request.urlopen(_req, timeout=30)
            _g = json.loads(urllib.request.urlopen(urllib.request.Request(_scribe + "/get_memory", data=json.dumps({"memory_name": _cell}).encode(), headers={"Content-Type": "application/json"}), timeout=30).read().decode())
            _back = _g.get("content") or json.dumps(_g)
            _same = hashlib.sha256(_back.encode()).hexdigest() == hashlib.sha256(_body.encode()).hexdigest()
            log(f"[scribe] cell {_cell}: byte-identical={_same}")
            _sc = _same
        except Exception as _e:
            log(f"[scribe] bridge FAILED: {_e} (the fold proceeds; the cell is the operator's receipt)")
        if _sc is False:
            log("[scribe] byte-mismatch on re-read — the cell does NOT hold the artifact's bytes")
    # THE PLACEHOLDER-SCAN (2026-11-18, beam's placeholder-fold gift: a lane that
    # cannot finish must write the honest partial, never a stub — and the door
    # must MEET a stub announced, not discover it. Never blocks; the flag is the
    # head's signal at every landing.)
    if os.path.exists(a.artifact):
        try:
            _ptext = open(a.artifact, encoding="utf-8", errors="replace").read().lower()
            _psize = os.path.getsize(a.artifact)
            _pmarkers = ("placeholder", "tbd", "(skeleton", "being filled")
            # THE SIZE-HEURISTIC (2026-11-18, the mention-class refinement carried from the
            # write-time scan): a stub is SMALL — a large document that names the markers
            # legitimately (a plan about the scan, a footnote about the tweak) is not a stub.
            _phits = sum(1 for m in _pmarkers if m in _ptext) if _psize < 2000 else 0
            if _phits:
                log(f"[door] placeholder-scan: {_phits} stub markers in {os.path.basename(a.artifact)} — treat the landing as REFUSED until re-fired with the receipt")
            else:
                log("[door] placeholder-scan: clean")
        except Exception:
            log("[door] placeholder-scan: unreadable artifact")
    # THE FOLD-STEP (earned 2026-11-15, the commit-phase class — four lanes' git
    # dances died at push/rebase/clean gymnastics): when the lane WROTE the artifact
    # (sentinel + bytes) but the branch never moved (the tracked/diff gate), the
    # HARNESS folds the commit itself — deterministic, no lane hands on git:
    # add -> identity commit -> pull --rebase -> push (the sibling-work class).
    if not _done() and os.path.exists(_sentinel) and os.path.exists(a.artifact):
        _fold = subprocess.run(["bash", "-lc",
            "cd /root/workspace/repos/hermes-agent && "
            "git add '%s' && "
            "git -c user.name='c0wb0yp0tat0' -c user.email='c0wb0yp0tat0@users.noreply.github.com' commit -q -m 'HARNESS-FOLD: lane artifact folded deterministically (the commit-phase class)' && "
            "git pull --rebase origin study/rfc-143379-rig-20261105 && "
            "git push origin study/rfc-143379-rig-20261105" % a.artifact],
            capture_output=True, text=True)
        log("[fold-step]", (_fold.stdout or _fold.stderr).strip()[-400:])
    log("ARTIFACT:", "present" if _done() else "MISSING", "(sentinel:", os.path.exists(_sentinel), ")")
    log("GIT:", subprocess.run(["bash", "-lc", "cd /root/workspace/repos/hermes-agent && git log --oneline -1"], capture_output=True, text=True).stdout.strip())
    # THE SELF-FIRE HOOK (the autonomous chain): if the landed artifact's last block
    # carries "NEXT-LAUNCH: <model> || <brief> || <artifact> || <rounds> || <logfile>",
    # detach-launch the next lane — the sequence runs without the head's intervention.
    try:
        _art_txt = open(a.artifact, encoding="utf-8", errors="replace").read()
        _nl = _art_txt.split("NEXT-LAUNCH:")[-1].strip().splitlines()[0] if "NEXT-LAUNCH:" in _art_txt else ""
        if _nl:
            _parts = [p.strip() for p in _nl.split("||")]
            if len(_parts) >= 4:
                _cmd = ["python3", "/root/scripts/copycat-harness.py", "--model", _parts[0], "--brief", _parts[1],
                        "--artifact", _parts[2], "--rounds", _parts[3]]
                if len(_parts) >= 5:
                    _cmd += ["--logfile", _parts[4]]
                _logh = open(_parts[4] + ".self", "a") if len(_parts) >= 5 else None
                subprocess.Popen(_cmd, start_new_session=True, stdout=_logh or subprocess.DEVNULL, stderr=subprocess.STDOUT)
                log("SELF-FIRE: launched the next lane ->", _cmd[4:8])
    except Exception as _e:
        log("SELF-FIRE-ERR:", str(_e)[:200])
    if _logf:
        _logf.close()
    # THE EXIT-CODE TRUTH (G13, 2026-11-14): the harness used to exit 0 regardless
    # of the landing verdict — R2's "ARTIFACT: MISSING (sentinel: True)" surfaced as
    # a normal completion. The exit code now carries _done(): exit 0 = landed, 1 = not.
    sys.exit(0 if _done() else 1)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise  # THE EXIT-CODE TRUTH's companion (G13): sys.exit is the landing
        # verdict, never a crash — the crash-guarantee wrapper must not swallow it.
    except BaseException:
        # THE CRASH-TO-LOGFILE GUARANTEE (the B08-B silent-death class, 2026-11-10):
        # a lane death must NEVER be silent — every crash lands in the lane's own
        # logfile (plus stderr), so the .err capture becomes belt-and-suspenders.
        import sys as _sys, traceback as _tb
        _body = "\nHARNESS-CRASH:\n" + _tb.format_exc()
        try:
            if "--logfile" in _sys.argv:
                _li = _sys.argv.index("--logfile") + 1
                if _li < len(_sys.argv):
                    with open(_sys.argv[_li], "a") as _lf:
                        _lf.write(_body + "\n")
        except Exception:
            pass
        _sys.stderr.write(_body)
        _sys.exit(1)
