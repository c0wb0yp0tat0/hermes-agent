"""Scoping proof: recitation knob is a parameter; no decay-shaped function
multiplies trial outcomes. Grep check."""
import re, pathlib
src=pathlib.Path(__file__).with_name("probe_recite.py").read_text()
# no multiplication of results by a decay-shaped function
bad=["* math.exp(-","* (1-","decay(","1/(1+","**(-"]
hits=[p for p in bad if p in src]
print("decay-shaped multiplications found:", hits)
assert not hits, "scoping violation"
print("SCOPING OK")
