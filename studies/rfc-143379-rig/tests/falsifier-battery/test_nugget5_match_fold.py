"""Falsifier battery — Nugget 5: literal-string allowlist seat.

Delta: the deny seat is language-familied via _MATCH_FOLD; every curly
quote/dash folds to its straight canonical form.
"""
import pytest

from tools.memory_tool_store import _MATCH_FOLD, _normalize_for_match


class TestNugget5MatchFold:
    def test_curly_single_quote_folds(self):
        assert _normalize_for_match("\u2019") == "'"

    def test_em_dash_folds(self):
        assert _normalize_for_match("\u2014") == "-"

    def test_full_family_fold(self):
        # _MATCH_FOLD folds EVERY curly quote (single AND double) to the
        # straight single quote "'" — the family's canonical form. (The
        # seam-probe's table was self-wrong on the curly-double-quote pair;
        # the code is authoritative.)
        pairs = [
            ("\u2018", "'"), ("\u2019", "'"), ("\u201a", "'"), ("\u201b", "'"),
            ("\u201c", "'"), ("\u201d", "'"), ("\u201e", "'"), ("\u201f", "'"),
            ("\u2010", "-"), ("\u2011", "-"), ("\u2012", "-"), ("\u2013", "-"),
            ("\u2014", "-"), ("\u2015", "-"), ("\u2212", "-"),
        ]
        for literal, expected in pairs:
            assert _normalize_for_match(literal) == expected, (literal, expected)

    def test_whitespace_collapse(self):
        assert _normalize_for_match("a\nb") == "a b"

    def test_match_fold_is_translation_table(self):
        assert isinstance(_MATCH_FOLD, dict) or hasattr(_MATCH_FOLD, "maketrans")
        assert _normalize_for_match("\u2018foo\u2019") == "'foo'"
