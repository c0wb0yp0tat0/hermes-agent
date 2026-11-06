"""sweep_crossings.py - E3 crossings arm sweep."""
import os
import probe_crossings as pc

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    rows = pc.run()
    for r in rows:
        print(r)
    print("wrote", len(rows), "rows")

if __name__ == "__main__":
    main()