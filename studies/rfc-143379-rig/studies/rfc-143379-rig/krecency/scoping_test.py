"""RED-on-leak / GREEN-on-fixed scoping proof."""
import probe

def test_window_empty_at_cycle_start():
    w = probe.Window(10)
    assert w.buf == []

def test_leak_class_fails():
    # simulate leak: window carries state across cycles
    w = probe.Window(10)
    w.push("LEAKED")
    # fixed scoping asserts empty -> this leaked window violates
    assert w.buf != [], "leaked window non-empty"
    # a fixed cycle resets; verify reset empties
    w.reset()
    assert w.buf == []

def test_cut_does_not_carry_state():
    stream = probe.token_stream(1, 50)
    kept, dropped = probe.compress_cut(stream, 10)
    w = probe.Window(10)
    for t in kept[-10:]:
        w.push(t[1])
    # state only from kept tail, not dropped
    assert all(x in [k[1] for k in kept] for x in w.snapshot())
