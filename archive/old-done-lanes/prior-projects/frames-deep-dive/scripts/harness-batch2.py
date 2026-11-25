import re, time

def grab(url, head=4000, keys=(), win=1800, maxhits=2):
    for attempt in (1, 2):
        try:
            goto_url(url)
            wait_for_load()
            break
        except Exception as e:
            print("NAV_ERROR", url, "attempt", attempt, repr(e)[:200])
            time.sleep(2)
    else:
        print("NAV_FAILED", url)
        return
    try:
        txt = js("document.body.innerText")
    except Exception as e:
        print("JS_ERROR", url, repr(e)[:200])
        return
    if not txt or len(txt) < 100:
        print("EMPTY_OR_SHORT", url, "len=", len(txt) if txt else 0)
        return
    print("="*90)
    print("URL:", url)
    print("TITLE:", js("document.title"))
    print("LEN:", len(txt))
    print("---HEAD---")
    print(txt[:head].replace("\n", " ")[:head])
    low = txt.lower()
    for k in keys:
        hits = [m.start() for m in re.finditer(re.escape(k.lower()), low)]
        print(f"---KEY '{k}' hits={len(hits)}---")
        for i in hits[:maxhits]:
            s = max(0, i - 400); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+400])

grab("https://en.wikipedia.org/wiki/Novus_ordo_seclorum",
     head=3500,
     keys=["Virgil", "Eclogue", "seclorum", "translation", "Thomson", "annuit"])

grab("https://www.thelatinlibrary.com/vergil/ec4.shtml",
     head=1500,
     keys=["magnus ab integro"])

grab("https://opusdei.org/en/article/the-founding-of-opus-dei/",
     head=3500,
     keys=["1928", "Madrid", "Escriv", "vision", "name", "Work of God"])
