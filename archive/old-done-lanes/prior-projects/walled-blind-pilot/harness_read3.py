import re, time

def grab(url, head=2000, keys=(), win=1000, maxhits=1):
    for attempt in (1, 2):
        try:
            goto_url(url)
            wait_for_load()
            break
        except Exception as e:
            print("NAV_ERROR", url, "attempt", attempt, repr(e)[:150])
            time.sleep(2)
    else:
        print("NAV_FAILED", url)
        return
    try:
        txt = js("document.body.innerText")
    except Exception as e:
        print("JS_ERROR", url, repr(e)[:150])
        return
    if not txt or len(txt) < 200:
        print("EMPTY_OR_SHORT", url, "len=", len(txt) if txt else 0)
        return
    print("="*90)
    print("URL:", url)
    print("TITLE:", js("document.title"))
    print("LEN:", len(txt))
    print("---HEAD---")
    print(txt[:head].replace("\n", " "))
    low = txt.lower()
    for k in keys:
        hits = [m.start() for m in re.finditer(re.escape(k.lower()), low)]
        print(f"---KEY '{k}' hits={len(hits)}---")
        for i in hits[:maxhits]:
            s = max(0, i - 400); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+400])

grab("https://tianpan.co/blog/2026-04-28-llm-judge-ceiling-auto-eval-human-correlation",
     head=3500, keys=["ceiling", "correlation", "lenien", "agreement"])

grab("https://old.reddit.com/r/mlops/comments/1rfb7kl/observations_on_llmasjudge_calibration_in/",
     head=2500, keys=["ceiling", "inter-rater", "calibration"])

grab("https://arxiv.org/html/2408.02442v1",
     keys=["format", "JSON", "performance", "constraint"])

grab("https://arxiv.org/html/2601.03444v1",
     keys=["0-5", "scale", "agreement", "ceiling"])

grab("https://arxiv.org/html/2605.19196v1",
     keys=["blind spot", "omission", "miss", "failure"])
