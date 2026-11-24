# RW-P1 — THE HISTORY-DELTA: the "removing both turns red" claim, row by row

*Lane: copycat (reserve seat `meituan/longcat-2.5:free`). Branch `study/rfc-143379-rig-20261105`. Fire 2026-11-24. Artifact for the reader-writer P1: the claim's full provenance through our own records, so the reply's gratitude and corrections land on the true map.*

**Scope of re-read this pass:** spec §3 re-read in full; thread row 7087999804 re-read verbatim from `rfc-comments-full.json`; KVNLOO-STALL-ON-READ-REFERENCE-20261124.md read (head+tail window; middle table rows reconstructed below). **Not re-read this pass (write-window gated the terminal/read tools before the artifact existed):** `FB2-EXECUTION-RECEIPTS-20261124.md`, `VET-KVNLOO-20261122.md`, and the body of row 7140129275 — each is carried with its row id/sha and a RE-DERIVE label rather than a remembered paraphrase. Per the Wall Clause, a non-reproduction is a QUESTION with a constructed minimal move, never a silent edit.

---

## 1. The claim's trail

### Step 0 — the origin: row 7087999804 (2026-11-23T00:01:13Z, kvnloo) · the 11-23 matrix

Verbatim, item 1 of his three findings (`rfc-comments-full.json:227`, `"id": 7087999804`):

> "**#141876's `read()` with @jfugalde's hardening already contains our fix.** Removing either the lock or the no-cache-write alone stays green. Removing both turns it red."

The claim entered our record here, inside the same matrix that also rowed the pins: MAIN `0f602c5f` (`read` → `Unknown action 'read'`, battery 409 pass) · `60a2e156` (#116673, race 🔴, own 16/16) · `+b6ff7dae` (🟢 17/17) · `ec649ad9` (MAIN + #116673 + #141876, 🟢 443 pass, dispatch contract 64/64) · `round2-gate` `268bb091` (🔴, **297/297**). Item 2 of the same row is the FB-2 add-clobber (`_add_doc` writes `content` as the whole file, `tools/memory_tool_store.py#L580-L618`); item 3 is the `a9c65dc4` branch with the 89/89 deletion experiment. **So the removing-both claim and the FB-2 clobber were delivered in one row, as two separate findings.**

### Step 1 — our record: `FB2-FAILING-CASE-SPEC-20261124.md` §3 (GREEN signature on the fix)

Verbatim, re-read this pass:

> "The store is locked and stateless across the two adds and the read is sanitized: the three arms of the fix are present in `tools/memory_tool_store.py` at this pin — `_file_lock` (serializes write/read), `_sanitize_entry` (sanitizes on read), and a hardened `def read` (the #141876 no-cache-write/sanitized-read path). **Removing either the lock or the no-cache-write alone stays green; removing both turns red** — that is the class's definition, re-derived in the probe matrix and in `VET-KVNLOO-20261122.md`."

Citation as written: **"the probe matrix" + `VET-KVNLOO-20261122.md`**. The spec's §6 pin table separately credits the matrix row by id: MAIN `0f602c5f` "per KvNloo's matrix row 7087999804" (and `b6ff7dae` "record-cited from KvNloo's matrix row 7087999804"). **Delta the reply must absorb:** the spec §3 presents the removing-both sentence as *re-derived* ("the class's definition"), while its own sibling §6 credits row 7087999804 for the same matrix facts — the provenance inside our own document is split, and the reply must close it.

### Step 2 — our confirm-run reply: row 7140129275 (2026-11-24, c0wb0yp0tat0)

Role per the mission ground: the confirm-run reply that carried the claim back to him. **RE-DERIVE (not re-read this pass — write-window gated the read tools):** recover the verbatim from `rfc-comments-full.json` row `"id": 7140129275` and quote the sentence that carries the removing-both line, then place it beside Step 0 and Step 1. Minimal move: `git grep -n '"id": 7140129275' -- rfc-comments-full.json` and read the record body. Until that quote is on the page, the reply must NOT assert what our confirm-run reply said beyond its existence and date.

### Step 3 — the vet reference the spec cites: `VET-KVNLOO-20261122.md`

Cited in §3 ("re-derived ... in `VET-KVNLOO-20261122.md`") and in §2/§6 (reproduction commit `9ce4e0078c`, `FIRST_SURVIVED_SECOND_ADD=False`). **RE-DERIVE (not re-read this pass):** locate the file under `studies/rfc-143379-rig/` and quote the line that first states the removing-both result and the clobber. If the removing-both line is NOT in the VET file, that is the finding: the citation points at a document that carries the clobber, not the removing-both claim — and the reply must say so.

---

## 2. His correction's shape — row 7143199711 (2026-11-24T01:27:31Z, kvnloo)

**Confirmed (his words):** "your row 1 is confirmed: the tool is registered, all four probe arms ran, three green, one unresolved."

**Owned — the provenance correction (his words, verbatim from the stall row):**

> "and here's the part I want on the record plainly: **'removing both turns it red' is our claim from 11-23, not something you predicted.**"

Receipted context in the same row: the class "lives in `_add_doc`'s write shape, and I'm grateful your side caught it" — the clobber's reality is acknowledged on both sides, independently of the reader-writer question.

**Added — the reader-writer arm (his words + receipts):**
- Mechanism: "the dispatch line is the read's only serialization boundary"; deleting it "exposes the read to a write that lands mid-read" — "reads skip the lock, the lock skips the reads, and a write committed between the read's load and its sanitize lands in the returned text." The handler docstring's promise ("returns latest on-disk state ... across add/patch/remove and reload") is false without the line.
- Test: `test_doc_reader_and_writer_keep_latest_live_state` at `a9c65dc4`, `tests/tools/test_memory_chain_docs.py#L198-L244` — **PASS with the dispatch line present, RED with it deleted (same RED after re-adding the write-side `_file_lock`).**
- The receipts table at the same pin (11-23 rows): `ec649ad9` composed — 443 pass, dispatch contract 64/64 (the green tree) · `a9c65dc4` branch — restored read suite 89/89 **with and without** the dispatch line (the deletion experiment) · `round2-gate` `268bb091` — 297/297, two-add red (the red arm).
- Scope limit, his words: "What does this change for FB-2: nothing about the add overwrite. That's real, receipted, and separate."

**Net shape:** he confirms the clobber, owns the removing-both claim as the 11-23 side's, and adds a *distinct* read-straddling-write seam with a named test and a pin-level receipts table — while explicitly refusing to let the new arm absorb FB-2.

---

## 3. The honesty surface — 5 bullets the reply must carry

1. **Provenance, not prediction:** "removing both turns red" is the 11-23 matrix's claim (row 7087999804, item 1), delivered by him; our spec §3 recorded it and cited the matrix + VET. We received it, we recorded it, we armed it — we did not originate it, and the reply says so in those words.
2. **Two classes, never merged:** FB-2 (the `_add_doc` whole-file clobber, `268bb091`, receipt `VET-KVNLOO-20261122.md`/`9ce4e0078c`) and the read-straddling-write seam (dispatch-line serialization) are separate findings; his new arm does not explain, absorb, or retire FB-2, and we do not let it.
3. **His test, his name, his sha:** `test_doc_reader_and_writer_keep_latest_live_state` at `a9c65dc4`, `tests/tools/test_memory_chain_docs.py#L198-L244`, PASS-with / RED-without the dispatch line — credited to his arm, not adopted as ours.
4. **The receipts table is his 11-23 record at the same pin:** `ec649ad9` (443/64-of-64), `a9c65dc4` (89/89 ± dispatch line), `268bb091` (297/297 two-add red) — carried as his rows, with our confirm-run reply (row 7140129275) quoted beside them once re-derived.
5. **No credit-taking on the derivation verbs:** the spec §3's "re-derived" and the reply's "we found/ran it" must give way to "received from row 7087999804, confirmed at the pins, receipted by VET/executions" — the gratitude lands on his trace-back, not on our memory of it.

---

## 4. The convergence line

The claim's trail closes on a single sentence the reply can carry: **"removing both turns red" came from his 11-23 matrix (row 7087999804), our spec §3 recorded it with a split citation, and his reader-writer arm now supplies the mechanism the matrix could only assert — so the reply credits the 11-23 claim, separates the clobber from the seam, and carries his test and receipts table as his, with row 7140129275 and `VET-KVNLOO-20261122.md` re-derived before a word of it is posted.**

---

### RE-DERIVE ledger (wall-clause questions, none answered by memory)

| # | Question | Minimal move | Status |
|---|---|---|---|
| Q1 | What did row 7140129275 (our confirm-run reply) actually say? | `git grep -n '"id": 7140129275' -- rfc-comments-full.json` → read body | OPEN — gated this pass |
| Q2 | Does `VET-KVNLOO-20261122.md` contain the removing-both line, or only the clobber? | Locate file under `studies/rfc-143379-rig/`, grep "removing both\|turns red" | OPEN — gated this pass |
| Q3 | Does `FB2-EXECUTION-RECEIPTS-20261124.md` restate the claim, and with what row/sha? | Read the receipts file | OPEN — gated this pass |