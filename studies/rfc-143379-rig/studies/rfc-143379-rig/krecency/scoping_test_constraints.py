import probe_constraints as pc

def test_present_zero():
    for s in pc.STRATEGIES:
        assert pc.violation_rate(s, "present") == 0.0

def test_absent_full():
    for s in pc.STRATEGIES:
        assert pc.violation_rate(s, "absent") == 1.0

def test_pinned_zero():
    for s in pc.STRATEGIES:
        assert pc.violation_rate(s, "pinned") == 0.0

def test_recency_worst():
    vals = {s: pc.violation_rate(s, "compacted") for s in pc.STRATEGIES}
    assert vals["recency-truncate"] >= max(v for k,v in vals.items() if k != "recency-truncate")
