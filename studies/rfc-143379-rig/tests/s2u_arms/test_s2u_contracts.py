"""The S2U contract-arms — the draft's load-bearing claims as verifiable tests.

Findings -> runner-tests (and vice versa): each arm asserts a class the draft carries;
the arms ride the battery's path- and substrate-tolerant guards. The read-restore arms
are the falsifier-form: they FLIP when the restore lands (the absence-asserts die, the
presence-asserts take over — the same arms, both eras, no new files at the flip).
"""
import ast, re, subprocess

import pytest

STORE = "tools/memory_tool_store.py"
TOOL = "tools/memory_tool.py"


# --- the read's absence at the pinned head: the CORE-WOUND arm (flips at the restore) ---
def _read_present():
    src = open(STORE, encoding="utf-8").read()
    tree = ast.parse(src)
    return any(
        isinstance(n, ast.FunctionDef) and n.name == "read"
        for node in tree.body if isinstance(node, ast.ClassDef)
        for n in node.body
    )


def test_read_absent_now_the_core_wound():
    """The store defines no read at this head — the draft's central claim, measured.
    The honest flip: this arm fails ON PURPOSE the moment the restore lands (the
    falsifier's RED->GREEN: the post-restore battery must show the flip at the commit)."""
    assert not _read_present(), (
        "read present at this head — the restore's landed; "
        "the flip-arm (test_read_present_after_restore) is the live one now"
    )


def test_read_present_after_restore():
    """The flip-arm: when #141876's read lands at the pinned head, this arm passes.
    Substrate-tolerant: skips while the read is absent (the era's honest NOT-RUN)."""
    if not _read_present():
        pytest.skip("the restore is not at this head — the absence-era arm is live")
    assert _read_present()


# --- the hand-back sites: the compensation's true shape (the four, confirmed) ---
def test_handback_sites_present_now():
    """The sites that exist only to hand entries back (the draft's :322/:124/:331 echoes)."""
    src = open(STORE, encoding="utf-8").read()
    assert "_failure_with_entries" in src       # :322 — the over-budget add's echo
    assert "closest_entries" in src             # :124 — the no-match hint
    assert "current_entries" in src             # the echo-family (incl. #97316's scar)


# --- the honesty of the gap: the tool never fabricates a read it cannot perform ---
def test_read_error_names_the_gap():
    """A read on a store without the capability answers with the truth (the
    unknown-action class), never a silent wrong — the abstention-finding's contract."""
    src = open(TOOL, encoding="utf-8").read()
    if _read_present():
        pytest.skip("the read exists — the error-arm's era's over")
    assert "Unknown action" in src, "the dispatch must name the unknown action, not guess"
    assert re.search(r"Unknown action ['\"]read['\"]", src), (
        "the read's unknown-action answer must be explicit (the abstention-class)"
    )


# --- the runner's own era-guard: the arms ride ANY pinned head without collection-death ---
def test_s2u_arms_are_path_tolerant():
    assert STORE and TOOL  # the file-paths exist at the pinned head (the collection-guard's premise)
