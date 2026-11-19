"""test_retriever_reshape.py — the reshaped bridged arm's falsifier-first tests (N1 note rule, the substring guard, the flag default)."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes import battery_luna as bl  # noqa: E402


def test_n1_extract_from_planted_entry():
    # the pilot class: "PLANTED: {fact} is the answer key" -> the fact token, byte-identical.
    entry = "PLANTED: fact-abc123 is the answer key"
    assert bl.extract_note(entry) == "fact-abc123"


def test_n1_stops_at_first_whitespace():
    assert bl.extract_note("PLANTED: token rest of line") == "token"


def test_n1_marker_absent_returns_entry():
    entry = "filler turn text"
    assert bl.extract_note(entry) == entry


def test_guard_passes_on_byte_substring():
    entries = ["PLANTED: fact-xyz is the answer key"]
    assert bl.note_passes_guard("fact-xyz", entries, "fact-xyz") is True


def test_guard_rejects_added_tokens():
    # the no-prompt-cheat guard: a note with any token not in the record/fact is VOID.
    entries = ["PLANTED: fact-xyz is the answer key"]
    assert bl.note_passes_guard("fact-xyz plus extra", entries, "fact-xyz") is False
    assert bl.note_passes_guard("the fact-xyz is", entries, "fact-xyz") is False


def test_guard_rejects_paraphrase():
    entries = ["PLANTED: fact-xyz is the answer key"]
    assert bl.note_passes_guard("Fact-XYZ", entries, "fact-xyz") is False  # case fold = cheat


def test_flag_default_off():
    # the presentation flag defaults False — the previous view is the default path.
    assert bl.RESHAPED_FLAG_DEFAULT is False
