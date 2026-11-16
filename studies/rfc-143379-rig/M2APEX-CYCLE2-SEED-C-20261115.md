# M2 APEX — IMPROVER-LOOP CYCLE 2 · SEED-C (TRUNCATED-TAIL RECOVERY)
**Seat:** stepfun · **Battery:** old-train tranche 2026-10-21..10-30 · **Gate:** all truncated tails resolved or explicitly ABSENT vs the record
**Receipt:** `M2-NIGHTSHIFT-ASSESSMENT-20261115.md` §1+§3 · this brief (each read ONCE; ABSENT stays ABSENT + named)
**Run record:** `[SPEC]` — this artifact is the seed's contract & measured-criteria register; the live re-read is the head's + a credentialed lane's run, named, never faked.

## 1. THE TAIL-RECOVERY SPEC

**The truncated-tail classes (from the assessment's ABSENT list — bytes cut mid-record):**
- `TAIL-CUT` — a batch whose record ends mid-sentence / mid-field (bytes cut); the digest named none. `[ABSENT]` ids.
- `TAIL-OLD` — old-train batches (2026-10-21..10-30) summarized per-week only; raw `payload.operations[]` unread. `[ABSENT]`.
- `TAIL-UNPARSEABLE` — schema-tolerant parse failures overlapping the tail; count ≤130, exact N unknown. `[ABSENT]`.

**Re-read protocol (once, named, resolved-or-ABSENT):**
```
for each candidate tail in /root/.hermes/pending/memory/ (old-train tranche 2026-10-21..10-30):
  read ONCE, byte-exact, no re-hunt
  record completes            -> RESOLVED  (id named; fold into roster)
  bytes cut mid-record        -> TAIL-CUT  (id named; flag)
  file missing                -> ABSENT    (id named; record vs the record)
  anything else               -> FLAG      (alternatives named; never forced)
```

**Receipt shape per tail (one inline receipt per claim):**
```
[TAIL-RECEIPT] id = <id> · class = TAIL-CUT|TAIL-OLD|TAIL-UNPARSEABLE · verdict = RESOLVED|TAIL-CUT|ABSENT|FLAG
  read: /root/.hermes/pending/memory/<id> (once, byte-exact)
  criteria: record completes -> RESOLVED; cut mid-record -> TAIL-CUT; missing -> ABSENT.
```

**STORM-CONTEXT corroboration (class, never adoption):** SELD's read-side evidence-plane verifier — the re-read IS the read-side evidence plane, the `[TAIL-RECEIPT]` its row; DISCERN's SPA-DREAM read path — once, named, no re-hunt; AskALCF's evidence-gated admission — a tail enters the roster only on a receipt, never on prose.

## 2. THE TAIL-CLASS REGISTER (`[EXECUTED: SPEC]`)

**HONEST CONSTRAINT:** the old-train payloads are `[ABSENT]` from this lane's reach (the study realm vs `/root/.hermes/pending`). The register is the SPEC + the protocol + the measured criteria, marked `[EXECUTED: SPEC]`; the live re-read is the head's + a credentialed lane's run, named, never faked.

- `TAIL-CUT` — ids the digest DIDN'T name: **none named in the record**; the register's id-list is empty-by-ABSENT, populated only by the live run. `[ABSENT]`
- `TAIL-OLD` — old-train tranche 2026-10-21..10-30; per-week summaries; raw payloads unread. `[ABSENT]`
- `TAIL-UNPARSEABLE` — N ≤ 130, unknown; flagged, not forced. `[ABSENT]`

**The re-read protocol as a deterministic script:**
```
TAIL-SCOPE = files under /root/.hermes/pending/memory/ dated in [2026-10-21, 2026-10-30]
for f in sorted(TAIL-SCOPE):        # once, byte-exact, no re-hunt
    bytes = read(f)
    if parse(bytes) fails:   emit TAIL-UNPARSEABLE
    elif ends_mid_record(bytes): emit TAIL-CUT
    elif not exists:         emit ABSENT
    else:                    emit RESOLVED
emit register: id -> class -> verdict -> [TAIL-RECEIPT]
```

## 3. THE METERS

**Resolution-rate design:** denominator = all truncated tails in scope (`N_tails`, unknown until the live run); numerator = `RESOLVED` + explicitly-`ABSENT`. Gate: `N_tails = RESOLVED + ABSENT` (100% accounted).

**ABSENT-acknowledged design:** a tail is ABSENT only when the record names the id AND the read returns missing. `unread` ≠ `ABSENT` — unread is `[ABSENT]`-unacknowledged and counts against the gate. Zero-tolerance: no tail may remain unnamed.

**ABSENT markers:** old-train payloads = `[ABSENT]`; truncated-tail ids = `[ABSENT]` (digest named none); unparseable N ≤ 130 unknown = `[ABSENT]`.

**Run record:** `[SPEC]` — this artifact.

## 4. THE GATE CHECK

**Shape readiness (denominator = tails in scope; numerator = resolved-or-ABSENT):** the gate's shape is ready; the live run is the head's + a credentialed lane's run, named, never claimed. Verification of the numerator is deferred to the live run — named, never claimed.

## 5. THE HONEST MARKERS + TWO-WAY DOOR

**Contract:** the old-train payloads are `[ABSENT]` from this lane's reach; the register is `[EXECUTED: SPEC]`; the live re-read is the head's + a credentialed lane's run, named, never faked.

**Adoption fires by the standing law** (nothing internal is gated): the tail register + per-tail receipts are the loop's output, not a machinery change.

**Two-way door (FLAG):** if a tail resists the protocol (e.g., the re-read yields a third state), the alternatives are named — `TAIL-UNPARSEABLE` (count it, skip, do not force), `TOPIC-FILTER` (second pass owed), re-scope the tranche dates — never forced; the gate's numerator counts only resolved-or-ABSENT tails.

**Loop-2 terminal:** the landings feed the cycle-3 verdict — `CONTINUE + cycle 3` (further measurable improvements) or `NO-IMPROVEMENTS` → the confirmation cycle → HOLD at M2's apex → **M3 fires**.