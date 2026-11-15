import io

p = "/root/workspace/.worktrees/compose-20261108/agent/context_compressor.py"
src = io.open(p, encoding="utf-8").read()

helpers = '''def _extract_anchor_lines(text: str) -> list[str]:
    """Per-category lines of the anchor index section carried in *text* (generation-order preserved).

    The anchor index is deterministic and LLM-free, so its section can be lifted verbatim from a
    prior summary and merged into the next generation's index instead of decaying after one
    generation. Returns [] when *text* carries no anchor section.
    """
    if not text or _LEAN_ANCHOR_HEADING not in text:
        return []
    body = text.split(_LEAN_ANCHOR_HEADING, 1)[1]
    for cut in ("\\n(Exact identifiers", "\\n## "):
        idx = body.find(cut)
        if idx >= 0:
            body = body[:idx]
    labels = {label for label, _, _ in _ANCHOR_PATTERNS}
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        label, sep, _ = line.partition(": ")
        if sep and label in labels:
            lines.append(line)
    return lines


def _anchor_line_values(line: str) -> list[str]:
    """Identifier values of one anchor category line, dropping the ``(xN)`` frequency suffix."""
    _, _, rest = line.partition(": ")
    values: list[str] = []
    for part in rest.split(", "):
        val = part.strip()
        if not val:
            continue
        if val.endswith(")") and "(x" in val:
            val = val[: val.rfind("(x")]
        values.append(val)
    return values


def _build_anchor_index(turns: list[dict[str, Any]], prior_lines: list[str] | None = None) -> str:
    """Regex-harvest exact identifiers from the compacted region (LLM-free); per-category caps, most-frequent first.

    ``prior_lines`` carries the previous generation's anchor category lines forward: fresh
    identifiers rank first, then prior-generation identifiers not already present, so the
    mechanically extracted anchor survives more than one generation while the per-category and
    total budgets still prune the oldest/lowest-ranked entries.
    """
    contents = (_typed_user_text(m["content"]) if m.get("role") == "user" and isinstance(m.get("content"), str) else m.get("content") for m in turns)
    text = "\\n".join(c for c in contents if isinstance(c, str) and c)
    if not text and not prior_lines:
        return ""
    prior_by_label: dict[str, list[str]] = {}
    for line in prior_lines or []:
        label, _, _ = line.partition(": ")
        prior_by_label.setdefault(label, []).extend(_anchor_line_values(line))
    sections: list[str] = []
    used = 0
    for label, pattern, cap in _ANCHOR_PATTERNS:
        counts: dict[str, int] = {}
        last_seen: dict[str, int] = {}
        for n, m in enumerate(pattern.finditer(text)):
            val = m.group(0).strip().rstrip(".,;:")
            if val.lower() in _ANCHOR_NOISE:
                continue
            counts[val] = counts.get(val, 0) + 1
            last_seen[val] = n
        ranked = sorted(counts, key=lambda v: (-counts[v], -last_seen[v])) if counts else []
        carried: list[str] = []
        for val in prior_by_label.get(label, []):
            if val not in counts and val not in carried:
                carried.append(val)
        combined = (ranked + carried)[:cap]
        if not combined:
            continue
        line = f"{label}: " + ", ".join(f"{v}(x{counts[v]})" if counts.get(v, 0) > 1 else v for v in combined)
        if used + len(line) > _LEAN_ANCHOR_BUDGET_CHARS:
            break
        sections.append(line)
        used += len(line)
    if not sections:
        return ""
    return (
        "\\n\\n" + _LEAN_ANCHOR_HEADING + "\\n"
        + "\\n".join(sections)
        + "\\n(Exact identifiers from the compacted region \\u2014 use these verbatim, "
        "and as session_search query anchors to recover their full context.)"
    )'''

start = src.index("def _build_anchor_index(")
tail = src[start:]
end = tail.index("\n\n\n")
old_build = tail[:end]
assert old_build.startswith("def _build_anchor_index(turns: list[dict[str, Any]]) -> str:"), old_build[:80]
assert src.count(old_build) == 1, src.count(old_build)
src = src.replace(old_build, helpers)

old_aug = '''        if getattr(self, "tail_mode", "lean") != "lean":
            return summary
        for heading, build in (
            (_LEAN_ANCHOR_HEADING, lambda: _redact_compaction_text(_build_anchor_index(turns_to_summarize))),'''
new_aug = '''        if getattr(self, "tail_mode", "lean") != "lean":
            return summary
        prior_anchor_lines = _extract_anchor_lines(getattr(self, "_previous_summary", "") or "")
        for heading, build in (
            (_LEAN_ANCHOR_HEADING, lambda: _redact_compaction_text(_build_anchor_index(turns_to_summarize, prior_anchor_lines))),'''
assert src.count(old_aug) == 1, src.count(old_aug)
src = src.replace(old_aug, new_aug)

io.open(p, "w", encoding="utf-8").write(src)
print("patched-ok")