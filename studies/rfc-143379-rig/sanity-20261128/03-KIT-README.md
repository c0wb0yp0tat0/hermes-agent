# PHASE-1 PILOT KIT — the read fix's testable run (3oltan-seo's contour, cold)

## What this is
The hardened read (the locked, stateless, sanitized `read()` at a9c65dc4) as a testable run — **not a paragraph, a package**. Run it anywhere with python3; it produces the receipt in seconds. No secrets, no network, your contour, your call.

## How to run
`sh RUN.sh` — one command. It executes the four-variant envelope (the store with the fix at as-at-pin · the lock removed · the cache-write restored · both removed) and prints the receipt + the envelope verdict + the receipt's sha256.

## What to expect (the verified prediction, byte-deterministic)
GREEN · GREEN · GREEN · RED — the red at `both-removed` is the ROLLBACK (the native read's stale-snapshot clobber): `rollback_observed: true` with `LATEST_SURVIVED_IN_LIVE: false`, while the disk always holds both entries. Every earlier row green = the fix's arms each hold alone. Verified on our machine (2026-11-25): the receipt is byte-deterministic — the same store + seed produce the same sha256 wherever it runs.

## The pilot's part (your call entirely)
- Run it at your pace; adopt, refuse, or take half — each answer is complete.
- The rollback-visibility log line (if you want it): after any read-then-add in your contour, if the chain holds only the first entry, log it and re-add — the miss becomes a datapoint, never a silent loss.
- Nothing leaves your contour: aggregates, deltas and trends are yours to share or not; raw material stays where it lives.

## The receipt
The run's output IS the receipt: the four rows + the envelope verdict + the sha256. The reference receipt (2026-11-25, our machine) — and the hash to expect from your own run: `sha256 3ff6aee45b16d45b6d8db1084381c6447f549fd01ab72da11c4aedcb5071fba9`. Same store, same seed, same bytes — the hash matching IS the verification.
