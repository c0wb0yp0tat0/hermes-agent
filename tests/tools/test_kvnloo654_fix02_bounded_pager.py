"""Fix 2 — bounded read pager (#116673): no uncapped response.

``read_paged`` paginates at UTF-8 character boundaries and never exceeds
``limit`` bytes per page. A single chain-doc read must fit within the
4 KiB response budget.

Red (before fix): there was no read_paged; callers used read() which
returns the entire content unbounded (131 KiB on #116673).
Green (after fix): read_paged enforces the byte ceiling and reconstructs
losslessly across pages.
"""

import json

import pytest

from tools.memory_tool import MemoryStore
from tools.memory_tool_store import ENTRY_DELIMITER


@pytest.fixture()
def paged_store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=100_000, user_char_limit=100_000)
    s.load_from_disk()
    return s


class TestFix2BoundedPager:

    def test_doc_response_budget_within_4096(self, paged_store):
        """The 131 KiB defect: read_paged text must stay under the 4 KiB budget."""
        # Create enough entries that the full content exceeds 4096 bytes.
        for i in range(30):
            paged_store.add("memory", f"entry-{i:03d} " * 20)  # ~260 chars each, ~7800 total

        result = paged_store.read_paged("memory", limit=4096)
        assert result["success"] is True

        # The bounded `text` field (the response payload) must fit the budget.
        text_bytes = result["text"].encode("utf-8")
        assert len(text_bytes) <= 4096, (
            f"text is {len(text_bytes)} bytes — exceeds 4096 budget (#116673)"
        )
        assert result["has_more"] is True
        assert result["cursor"] is not None

    def test_read_paged_is_lossless_across_pages(self, paged_store):
        """Following cursors must reconstruct the full content exactly."""
        entries = [f"entry-{i:03d}" * 30 for i in range(10)]  # ~10 × ~120 chars
        for e in entries:
            paged_store.add("memory", e)

        collected = []
        cursor = None
        while True:
            result = paged_store.read_paged("memory", cursor=cursor, limit=4096)
            assert result["success"] is True
            collected.append(result["text"])
            cursor = result.get("cursor")
            if not result["has_more"]:
                break
            assert cursor is not None

        full_text = "".join(collected)
        expected = ENTRY_DELIMITER.join(entries)
        assert full_text == expected, "paginated read is not lossless"

    def test_utf8_boundary_safe_no_partial_multibyte(self, paged_store):
        """Pages must never split a multibyte codepoint mid-sequence (#116673).

        The 4-byte rocket emoji 🚀 would be corrupted if the pager cut at an
        arbitrary byte boundary. We force splits at a small limit and verify
        each page decodes cleanly.
        """
        multibyte = "SYNTHETIC-CONSENT-CODE-PX7412: " + "🚀" * 1000
        paged_store.add("memory", multibyte)

        cursor = None
        while True:
            result = paged_store.read_paged("memory", cursor=cursor, limit=97)
            text = result["text"]
            # If this raised, we'd have split a multibyte sequence.
            text.encode("utf-8").decode("utf-8")
            assert "�" not in text  # no replacement char from partial decode
            cursor = result.get("cursor")
            if not result["has_more"]:
                break

    def test_cursor_is_none_when_one_page_suffices(self, paged_store):
        """A small store needs no pagination."""
        paged_store.add("memory", "small entry")
        result = paged_store.read_paged("memory", limit=4096)
        assert result["success"] is True
        assert result["has_more"] is False
        assert result["cursor"] is None
        assert "small entry" in result["entries"]

    def test_invalid_cursor_falls_back_to_start(self, paged_store):
        """A non-numeric cursor must not crash — fail gracefully to start (#116673)."""
        paged_store.add("memory", "hello world")
        result = paged_store.read_paged("memory", cursor="not-a-number", limit=4096)
        assert result["success"] is True
        assert "hello world" in result["text"]

    def test_paged_vs_unbounded_consistency(self, paged_store):
        """Paged reconstruction matches read() exactly."""
        for i in range(5):
            paged_store.add("memory", f"consistency entry {i} " * 20)

        paged_text = []
        cursor = None
        while True:
            r = paged_store.read_paged("memory", cursor=cursor, limit=512)
            paged_text.append(r["text"])
            cursor = r.get("cursor")
            if not r["has_more"]:
                break

        read_result = paged_store.read("memory")
        expected_text = ENTRY_DELIMITER.join(read_result["entries"])
        assert "".join(paged_text) == expected_text

    def test_default_limit_is_4096(self, paged_store):
        """The default page size is 4096 bytes — no uncapped default."""
        large_entry = "A" * 5000
        paged_store.add("memory", large_entry)
        result = paged_store.read_paged("memory")
        text_bytes = result["text"].encode("utf-8")
        assert len(text_bytes) <= 4096
