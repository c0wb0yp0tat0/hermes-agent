"""Minimal threat-pattern stub for the standalone probe (no threat scan — the labs' documented approach)."""

def first_threat_message(*args, **kwargs):
    """No threat scan in the probe harness; returns None (the store's threat gate passes)."""
    return None
