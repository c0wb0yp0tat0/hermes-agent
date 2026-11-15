"""sweep_seamint.py - seam-integration sweep (real ground)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probe_seamint as p

if __name__ == "__main__":
    rows = p.run()
    for r in rows:
        print(r)
