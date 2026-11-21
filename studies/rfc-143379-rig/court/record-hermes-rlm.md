##### ISSUE #59 #####
TITLE: R1: Load the four RLM paper benchmark families
STATE: open | created 2026-11-20T05:45:48Z | updated 2026-11-20T05:45:48Z
BODY:
DOT-EVALS-01 · [claim R1](https://github.com/kvnloo/oss-factory/issues/448#issuecomment-7031451323)

Adds one offline materializer for OOLONG trec_coarse, author-gold or reconstructed Appendix D.1 Pairs, fixed 1,000-unique-document BrowseComp-Plus with evidence inclusion, and LongBench-v2 CodeQA. Outputs are real TaskBuilder manifests; local dataset inputs are clearly marked unverified against reference revisions. No datasets or labeled contexts are shipped. Existing materialization mode remains unchanged.

Uses the verbatim [RLM-author OOLONG scoring slice](https://github.com/alexzhang13/rlm/blob/d86154e6b03b9ff880b31a1b0eadd273ff92b9e8/training/environments/oolong/oolong/env.py) under its MIT notice and checks eight fixed examples. This is author reference code, not proven to be the paper-table runner. Pairs F1 and CodeQA accuracy are local metric adapters; original parser parity is not established. BrowseComp defaults to an unscored sentinel: a live matrix run refuses it unless a trusted custom scorer is provided, or an operator explicitly chooses diagnostic exact match when generating the manifest. No semantic judge or original 150-query assignment was verified.

```sh
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench -p test_paper_datasets.py -v
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench
```
Exact base with new tests could not import `paper_datasets` (nonzero). Candidate: 6 passed in 0.110s; full exact bench snapshot 95 run in 7.486s, OK (one requirements check skipped without its explicit flag). Four synthetic TaskBuilder manifest types accepted by `paper_matrix.load_tasks`: 28 full, 4 smoke, 20 Pairs, 5 CodeQA. Real source download probes from this computer returned curl 28 / HTTP 000 / 0 bytes; no full corpora, Parquet path, live inference, or end-to-end reproduction claimed.

##### ISSUE #61 #####
TITLE: R2: Add an exact-token scaling sweep and task-bootstrap plots
STATE: open | created 2026-11-20T05:57:15Z | updated 2026-11-20T05:57:15Z
BODY:
DOT-EVALS-01 · [claim R2](https://github.com/kvnloo/oss-factory/issues/448#issuecomment-7031627775)

Adds a 2^13–2^20 exact-token synthetic sweep using a local tokenizer JSON, an opt-in full-context baseline that reserves chat and output tokens before dispatch, and a plotter with task-clustered 95% intervals on task-level rows. The base arm never slices an admitted context. It records declared window/reserve and tokenizer code/data identity; it does not verify a serving route's actual capacity. Aggregate-only input yields point estimates without manufactured intervals.

```sh
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench -p test_scaling_sweep.py -v
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench -p test_plot_scaling.py -v
BENCH_REQUIRE_DEPS=1 python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench
python -B -m bench.generate_scaling --tokenizer-json "$TOKENIZER_JSON" --out "$SWEEP_DIR"
python -B bench/plot_scaling.py "$STUDY_SUMMARY" --cohort primary --output "$PLOT_PNG"
```
Focused exact base plus regression fails importing the absent generator. Candidate: sweep 3 passed (0.160s); plot 6 passed (2.443s); full 98 passed (9.159s). The real GPT-2 vocabulary sweep generated 48 tasks across eight exact lengths; independent native tiktoken encoding matched all 48, and `load_tasks` accepted full/smoke manifests. The [exact requested study summary](https://github.com/kvnloo/z0evals/blob/19f53a3742c5ae7c0e9fc2b610fe613bfe425376/studies/rlm-paper-replication-v1/data/summary.json) rendered 32 primary score points across five panels (1300×2405 PNG). It has no task rows, so no intervals were recomputed from it. No provider calls or performance comparison.

##### ISSUE #62 #####
TITLE: R3: Report protocol failures and show citation-valid FINAL calls
STATE: open | created 2026-11-20T06:05:51Z | updated 2026-11-20T06:05:51Z
BODY:
DOT-EVALS-01 · [claim R3](https://github.com/kvnloo/oss-factory/issues/448#issuecomment-7031795117)

Adds an offline adherence report over the published aggregate and optional caller-provided audited evidence. It classifies missing validated FINAL, uncited answer, observed direct context reads through another tool, and child error. It reports overlapping observations and unknowns, without letting any evidence-only field change audit validity or disclosing raw answers or traces.

The actual frozen public summary reports 177/300 strict-invalid and 28/180 Hermes protocol-adherent, but has no cause-level replay evidence. The historical top cause is unknown. This candidate fixes a concrete prompt/validator contradiction: the registered REPL tool advertised an uncited FINAL example that the host rejects for loaded context. It now teaches citation-valid submission, retry on rejection, and end-of-turn after accepting. This is not evidence of improved historical or live adherence.

```sh
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench -p test_protocol_adherence.py
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s tests -p test_final_prompt_contract.py
BENCH_REQUIRE_DEPS=1 python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s bench
python -B -X pycache_prefix="$(mktemp -d)" -m unittest discover -s tests
python -B bench/protocol_adherence.py --summary "$STUDY_SUMMARY"
```
Exact main plus prompt regression: 1 fail (uncited registered example). Candidate: offline classification 5 pass (0.005s); actual registration/validator regression 1 pass (0.001s); full 94 bench pass (7.547s), 42 runtime-side tests pass (0.222s). Exact [frozen study summary](https://github.com/kvnloo/z0evals/blob/19f53a3742c5ae7c0e9fc2b610fe613bfe425376/studies/rlm-paper-replication-v1/data/summary.json) yields 300/177/28 and null (not zero) for all four historical cause counts. No private archives or provider/live-host runs.

##### ISSUE #64 #####
TITLE: Re-port v0.1-era fixes onto the paper-faithful main (if they still reproduce)
STATE: open | created 2026-11-20T06:37:28Z | updated 2026-11-20T06:37:28Z
BODY:
These draft PRs were written against the v0.1 code that #1 (paper-faithful) replaced. Each one conflicts with main or targets a function #1 rewrote, so none can merge as written. Some of the bugs may still exist on main (8ec5d15). This issue keeps them findable after the PRs close.

To re-port one: reproduce the bug on main first, with a test that fails on main. If it doesn't fail, the bug is gone; tick it and move on. If it does fail, open one PR from main with the fix and that test.

Real bug claims (check whether each reproduces on main):
- [ ] #38 Session releases kernel pipes on kill/respawn (ResourceWarning leak)
- [ ] #42 bench rlm_usage skips an unparseable (torn) log line
- [ ] #43 bench rlm_usage skips valid-JSON non-row lines
- [ ] #44 bench rlm_usage counts null token fields as zero
- [ ] #45 / #46 null or None host usage counted as zero in sub-call accounting
- [ ] #47 Session._read buffers lines itself (a second line in one pipe read was stranded)
- [ ] #48 load_corpus counts each file once (#1's notes say it already deduplicates; confirm)
- [ ] #55 sub-call BaseException handling

Features to redo on main if still wanted:
- [ ] #2 installable plugin + 3.11/3.12 CI. main already has bench.yml; add only what's missing.
- [ ] #3 root plugin manifest, runtime disclosure, parity test (needed for a Hermes catalog entry)
- [ ] #6 task_id change starts an empty REPL (stacked on #3)

Closed as pin-only, no replacement planned: #36, #41, #60, #63.

Landed so far in the cleanup: #1, #4, #5, #49, #54, #56, #57, #58.


