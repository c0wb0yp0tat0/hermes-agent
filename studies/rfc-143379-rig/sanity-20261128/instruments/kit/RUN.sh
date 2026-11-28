#!/bin/sh
# THE PHASE-1 PILOT RUN — the read fix's testable envelope (one command, cold)
set -e
cd "$(dirname "$0")"
python3 stall_probe.py > receipt.json 2>&1
echo "--- receipt ---"
cat receipt.json
echo "--- envelope check ---"
python3 - <<'PY'
import json,sys
r=json.load(open('receipt.json'))
order=['as-at-pin','lock-removed','cache-write-restored','both-removed']
expect={'as-at-pin':False,'lock-removed':False,'cache-write-restored':False,'both-removed':True}
ok=True
for k in order:
    v=r[k]
    roll=v.get('rollback_observed')
    status='RED' if roll else 'GREEN'
    ok = ok and (roll==expect[k])
    print(f'{k}: {status} (expected {'RED' if expect[k] else 'GREEN'})')
print('ENVELOPE:', 'GREEN-GREEN-GREEN-RED CONFIRMED' if ok else 'UNEXPECTED — FINDING, not a failure')
import hashlib
h=hashlib.sha256(open('receipt.json','rb').read()).hexdigest()
print('RECEIPT_SHA256:', h)
PY
