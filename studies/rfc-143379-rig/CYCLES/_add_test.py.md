import io
p = "/root/workspace/.worktrees/compose-20261108/tests/agent/test_lean_single_aux_call.py"
src = io.open(p, encoding="utf-8").read()
test = '''

class TestAnchorMultiGenerationCarry:
    """The deterministic anchor index must survive MORE than one summary-augmentation generation.

    Regression for RFC opp 1 / IMPROVEMENTS-W1 #2: `_augment_summary_lean` used to rebuild the
    anchor from the current generation's `turns_to_summarize` only, so generation N's exact
    identifiers dropped out of the anchor after one generation.
    """

    @staticmethod
    def _turns_with_marker(marker):
        turns = _big_region(n_rounds=5)
        turns[0] = {"role": "user", "content": marker}
        return turns

    def test_anchor_identifiers_survive_subsequent_generations(self):
        c = _mk_compressor()
        gen_a = "Fix PR #99999 in agent/alpha.py"
        gen_b = "Fix PR #88888 in agent/beta.py"
        gen_c = "Fix PR #77777 in agent/gamma.py"
        with patch("agent.context_compressor.call_llm", return_value=_llm_response(SUMMARY_BODY)):
            summary1 = c._generate_summary(self._turns_with_marker(gen_a))
        assert "#99999" in summary1 and "agent/alpha.py" in summary1

        with patch("agent.context_compressor.call_llm", return_value=_llm_response(SUMMARY_BODY)):
            summary2 = c._generate_summary(self._turns_with_marker(gen_b))
        assert "#88888" in summary2 and "agent/beta.py" in summary2
        # THE contract: generation A's anchor identifiers survive into generation B.
        assert "#99999" in summary2 and "agent/alpha.py" in summary2

        with patch("agent.context_compressor.call_llm", return_value=_llm_response(SUMMARY_BODY)):
            summary3 = c._generate_summary(self._turns_with_marker(gen_c))
        assert "#77777" in summary3
        # ...and into generation C (N generations, not one).
        assert "#99999" in summary3 and "#88888" in summary3
        assert "agent/alpha.py" in summary3 and "agent/beta.py" in summary3

    def test_anchor_carry_is_noop_without_prior_summary(self):
        """Fresh compaction (no `_previous_summary`) is unchanged: no phantom carry."""
        c = _mk_compressor()
        with patch("agent.context_compressor.call_llm", return_value=_llm_response(SUMMARY_BODY)):
            summary = c._generate_summary(self._turns_with_marker("Fix PR #99999 in agent/alpha.py"))
        assert "#99999" in summary and "agent/alpha.py" in summary


if __name__ == "__main__":
    pytest.main([__file__, "-q"])
'''
old_main = '''

if __name__ == "__main__":
    pytest.main([__file__, "-q"])
'''
assert src.count(old_main) == 1, src.count(old_main)
src = src.replace(old_main, test)
io.open(p, "w", encoding="utf-8").write(src)
print("test-added")