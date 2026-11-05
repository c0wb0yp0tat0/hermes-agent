import probe_archive as pa
import csv, json
from collections import defaultdict

if __name__ == "__main__":
    res = pa.run_sweep()
    # aggregate worst-case min per (ratio, budget, rlimit, cycle-bucket)
    # print summary
    print("rows", len(res))