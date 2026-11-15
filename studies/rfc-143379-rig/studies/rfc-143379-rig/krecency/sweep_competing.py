"""Sweep driver for the competing-admission arm."""
import probe_competing as pc
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
res = pc.run_sweep()
print("rows", len(res))
