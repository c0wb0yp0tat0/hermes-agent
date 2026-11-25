# Extract targeted text from research pages (batch 1)
# Usage: BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use < script.py
import time

PAGES = [
    ("compression-wild", "https://arxiv.org/html/2604.02985v1"),
    ("anthropic-evals", "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"),
    ("cohere-poll", "https://arxiv.org/abs/2404.18796"),
    ("thinking-smalls-judges", "https://arxiv.org/html/2509.13332v1"),
]

def grab(url, maxlen=9000):
    goto_url(url)
    wait_for_load()
    time.sleep(1.0)
    title = js("document.title")
    text = js("(()=>{const a=document.querySelector('article')||document.body;return (a.innerText||'').replace(/\\n{3,}/g,'\\n\\n')})()")
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
