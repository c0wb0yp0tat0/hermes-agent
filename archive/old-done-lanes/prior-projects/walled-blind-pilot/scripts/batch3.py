# Extract targeted text from research pages (batch 3)
# Usage: BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use < script.py
import time

def grab(url, maxlen=8000, start=0, sel='article||main||body'):
    goto_url(url)
    wait_for_load()
    time.sleep(1.2)
    title = js("document.title")
    text = js("(()=>{const a=document.querySelector('article')||document.querySelector('main')||document.body;return (a.innerText||'').replace(/\\n{3,}/g,'\\n\\n')})()")
    return title, (text or "")[start:start+maxlen]

# Wolfe article applied section: pull middle slice
try:
    title, text = grab("https://cameronrwolfe.substack.com/p/stats-llm-evals", maxlen=10000, start=15000)
    print("=" * 70)
    print("PAGE: wolfe-stats-evals (applied section) | TITLE:", title)
    print(text)
except Exception as e:
    print("wolfe applied ERROR:", repr(e))

PAGES = [
    ("know-thy-judge", "https://arxiv.org/html/2503.04474v1"),
    ("large-scale-llmaj", "https://arxiv.org/html/2606.19544v1"),
    ("deepchecks-calib", "https://deepchecks.com/llm-judge-calibration-automated-issues/"),
]

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
