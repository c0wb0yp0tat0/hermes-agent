# Extract targeted text from research pages (batch 2)
# Usage: BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use < script.py
import time

PAGES = [
    ("wolfe-stats-evals", "https://cameronrwolfe.substack.com/p/stats-llm-evals"),
    ("stat-reality-llm-eval", "https://medium.com/@juanc.olamendy/the-statistical-reality-of-llm-evaluation-what-works-what-doesnt-and-when-it-matters-7d9ba6ecdfca"),
    ("galileo-calibrate", "https://galileo.ai/blog/calibrate-llm-judge-human-annotations"),
    ("forrt-replication", "https://forrt.org/replication-handbook/execution_replications.html"),
]

def grab(url, maxlen=8000):
    goto_url(url)
    wait_for_load()
    time.sleep(1.2)
    title = js("document.title")
    text = js("(()=>{const a=document.querySelector('article')||document.querySelector('main')||document.body;return (a.innerText||'').replace(/\\n{3,}/g,'\\n\\n')})()")
    return title, (text or "")[:maxlen]

for name, url in PAGES:
    try:
        title, text = grab(url)
        print("=" * 70)
        print("PAGE:", name, "|", url)
        print("TITLE:", title)
        print(text)
    except Exception as e:
        print("=" * 70)
        print("PAGE:", name, "|", url, "| ERROR:", repr(e))
