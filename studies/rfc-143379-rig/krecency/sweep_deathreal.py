"""sweep_deathreal.py - death-cell-real sweep."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probe_deathreal as p

if __name__ == "__main__":
    rows = p.run()
    for r in rows:
        print(r)