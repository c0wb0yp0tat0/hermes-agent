# STORM-HARVEST-2 — The adversarial thesis: Continual-ARC and the weights question

Scribe-record of the CTO-side web storm (wave 2 of 2). The storm's second wave hunted the verifier's door and the adversarial thesis — and found both, named, with a contract.

## The adversary, named
**Daniel Lenton — founder, Unify (YC W23), creator of Ivy + unify-agent.** His post directly names our house:
> "OpenClaw, Hermes Agent and Prime Agent don't meaningfully learn from experience. On Continual-ARC… none of them were able to memorize anything of value and none were able to generalize to new tasks. Training a small 9B model's weights did both."

And the dagger line: *"Real learning on the job will need the weights to change, with the harness becoming the thing that trains the model, **not a growing pile of markdown files**."* The "pile of markdown files" is the doc-chain. He is arguing against the RFC's mechanism by name.

## The essay — "The harness is not enough" (unify.ai/blog/the-harness-is-not-enough)
- His definition of a harness is generous and accurate: "OpenClaw, Hermes-Agent, Prime Agent and the rest decide when the model gets called, what goes into its context, which tools it can reach, when to compact, when to spin up a sub-agent, and how to check the result."
- His concession is honest: "That is why the harness gets the credit, and to be fair, right now it deserves it."
- His thesis: vision's hand-designed filters gave way to learned CNNs; agent memory will do the same — experience goes into weights, the harness becomes the training pipeline (deciding what's worth training on, running the update, checking it worked).
- His open problems: what's worth training on; catastrophic forgetting; **"there's also no good way yet to measure how much an agent improves from experience, whether it keeps notes or updates its weights"** — that last one is the admission that makes Continual-ARC their answer.

## The benchmark (Continual-ARC, continual-arc.unify.ai + arXiv + github.com/unifyai/continual-arc)
- **The stream**: ARC puzzles recur with fresh inputs after long gaps (exponential spells, log-normal rests, Poisson arrivals), new ones keep arriving. The learner sees the task id + a fresh input grid; can pay 1 for a demonstration, 1 for a wrong answer, up to 8 each; a right answer ends the instance; an unsolved instance costs the whole budget of 16. "Failing is never cheaper than asking."
- **The two tests**: at stream's end the learner is frozen and plays BOTH — fresh inputs of the tasks it met (memorization) AND 100 tasks it never met (generalization). Every run is read against the same learner **reset before each instance** (the wiped harness) — so a stronger model earns nothing for being stronger. "The floors and the wiped harnesses carry nothing to a task they have not met, so their spread on the held-out test is its noise."
- **The headline result on Qwen3.5-9B (student) + GLM-5.3 Flash (teacher)**: notes kept in the harness saved at most **0.12** of the reset's spend on tasks met, **no more than chance** on new ones; training the weights saved **0.45** and **0.27**. The plane: notes→(0.12, ~0); weights→(0.45, 0.27).
- Leaderboard includes *programs kept*: L +0.60, U 11.5 — the top-right corner is the learned/tool-program class, not the notes class.

## The verification contract (the two-way door, standardized)
- Anything that is not wiring ARC data into the learner is allowed: "memory, programs, tools, a cache, **training the weights**. Compute is logged and shown beside the score, never in it."
- **The door**: run your learner on the public deterministic stream (git clone, `continual-arc data fetch`, `schedule make`), send the run directories **as a pull request** → joins the leaderboard marked **reported**. Then open the **Verify my learner** issue with the form: public repo + commit + import path (Python class implementing the learner protocol), the student model on OpenRouter + effort, teacher if any, and an OpenRouter key capped at your budget encrypted with their public key. **Unify reruns your code on a private held-out set of 50 new ARC-style rules nobody has seen, at a seed they don't disclose** → marked **verified**.
- Cost guidance: "The paper's harness runs on GPT-6 Luna cost 1 to 45 US dollars on the public streams… a cap of about 100 dollars suits a model of Luna's class." **Private Input & Output Logging must be OFF** on the OpenRouter account, or the run is void (their logs would hold the held-out tasks).
- Currently cannot verify a weight-training learner, or a system whose code can't be shared. "All verified submissions of genuine learning algorithms" are presented — they want the harnesses on the board too.

## The second essay — "Building a brain around a stateless model" (unify.ai/blog)
- unify-agent's own architecture: the model as "stateless cortical tissue"; the brain assembled around it in code — context window as the boundary between parts; conversation loop vs work loop with steerable handles; **skills stored as Python functions, not notes** ("one repair to a shared step reaches every task that uses it").
- **Their honest reversal on today's models**: the function-library beat notes on GPT-4.1 (under a third of the tokens), but "On today's models the rebuild was never more accurate than the simple alternatives… and it was never cheaper than retrieving past solutions. The stronger models solved every task even with no memory, and the library just made them about 60% more expensive."
- The one caveat that matters to us: **linking guidance to functions helped GPT-6 Luna pick up every rule that applied** — "Luna otherwise had to judge from the prose which rules applied, and it missed some." A memory-layer design beat plain context on the exact accused model.
- Ends where the essay began: the weights step is the next frontier; continual learning on own-work without forgetting is unsolved.

## What fires from this
- The RFC's thesis now has a named opponent, a public bench, and a verification door. Continual-ARC's "state that persists across the stream" IS the read-restore's question at lifetime scale.
- The honest scope of OUR claim must be named: the substrate's proven class is reliability-on-episodes (Jain/PersistGym), not lifetime skill acquisition (their 0.12 ceiling on notes, and their admission the benchmark is for "whether notes or weights"). The two windows are different claims, and the RFC's "you're not listening → re-read" is the episodic window.
- An actual submission is runnable and cheap for the rig: ~$100 Luna-class cap; code already shareable via PR #1's repo; the harness settings become class defaults. Public-stream run → reported → then the 50-rule held-out verify. A verified run with the doc-chain substrate would be the study's falsifier *on the adversarial's own bench*.
- The 0.12 ceiling is the field's best-measured number for notes-class learners; the doc-chain's write-time assert + read-restore exists to beat exactly that class — a target and a bar, not a verdict.
