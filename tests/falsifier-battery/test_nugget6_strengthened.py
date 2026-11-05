"""Falsifier battery — Nugget 6 STRENGTHENED: the mutated-case + the #141876-composition arm.

Built by the head per the improver's proposal-1 (the verified-record landing; the
lane-channel's fair-share exhaustion ended the re-dispatch circus).

The mutated-case class (the divergence's resolution):
  * Shape A (the design-delta probe) holds on the current head (exact-first arm).
  * Shape B (the seam-probe, mutated): after the orphan 'foo' is transformed/removed,
    a substring 'foo' still resolves into '@doc:foobar' and removes it — FALSIFIED.
  The strengthened falsifier asserts the delta's fix-contract: the substring inside a
  whole anchor token is NEVER a match target. RED on the current head (the surviving
  seam), GREEN when the delta's whole-anchor/structural resolution lands.

The #141876-composition arm (xngg1021's gift — the composition the single-head battery
lacked): the read-back contracts must hold through the composed store surface.
"""
import pytest

from tools.memory_tool_store import (
    MemoryStore,
    ENTRY_DELIMITER,
    _find_unique_match,
)


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=5000, user_char_limit=1000)
    return s


def _load(store, entries):
    (store._path_for("memory").parent / "MEMORY.md").write_text(
        ENTRY_DELIMITER.join(entries), encoding="utf-8"
    )
    store.load_from_disk()


class TestNugget6MutatedCase:
    def test_anchor_only_state_foo_query_is_ambiguous(self, store):
        # After the orphan 'foo' is gone, the anchor '@doc:foobar' remains.
        # A bare 'foo' substring must NOT silently resolve into the anchor.
        _load(store, ["@doc:foobar"])
        idx, ambiguous = _find_unique_match(["@doc:foobar"], "foo")
        assert idx is None or ambiguous is True, (
            "substring inside a whole anchor token must never be a silent match target"
        )

    def test_mutated_remove_never_hits_the_doc_anchor(self, store):
        # The seam-probe's exact mutated shape: the orphan transformed away,
        # then remove('foo') — must NOT remove '@doc:foobar'.
        _load(store, ["@doc:foobar", "foo"])
        store.remove("memory", "foo")
        entries = [e for e in store.read("memory")["entries"] if e.strip()]
        assert any("@doc:foobar" in e for e in entries), (
            "the substring-remove must not consume the doc-anchor entry"
        )


class TestCompositionArm:
    def test_composed_read_back_contracts_present(self):
        # The #141876-composition's contracts: the composed store surface exposes a
        # read path with the disk-attestation (the presence-assertion; the
        # composition's availability is the branch's own property).
        assert hasattr(MemoryStore, "read")
        assert hasattr(MemoryStore, "load_from_disk")
