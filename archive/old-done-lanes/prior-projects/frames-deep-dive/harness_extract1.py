import re

def dump(url, keywords, win=2600, label=""):
    goto_url(url)
    wait_for_load()
    text = js("(()=>{const a=document.querySelector('#mw-content-text')||document.querySelector('article')||document.body;return (a.innerText||'').slice(0,180000)})()")
    if not text:
        print(f"--- {label or url}: NO TEXT ---")
        return
    print(f"===== {label or url} (len={len(text)}) =====")
    for kw in keywords:
        idx = text.lower().find(kw.lower())
        if idx >= 0:
            print(f"--- [{kw}] @{idx} ---")
            print(text[max(0,idx-400):idx+win].replace("\n\n\n","\n\n"))
        else:
            print(f"--- [{kw}] NOT FOUND ---")

dump("https://en.wikipedia.org/wiki/New_World_Order_conspiracy_theory",
     ["History of the term", "Freemasonry", "Illuminati", "Robertson", "evangelical", "Bush"],
     label="NWO_CONSPIRACY_WIKI")

dump("https://www.conspiracyarchive.com/NWO/All_Seeing_Eye.htm",
     ["eye", "pyramid", "Masonic", "Illuminati", "Great Seal", "dollar"],
     label="CONSPIRACYARCHIVE_ALLSEEINGEYE")
