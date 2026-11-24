def dump(url, keywords, win=2600, label=""):
    goto_url(url)
    wait_for_load()
    text = js("(()=>{const a=document.querySelector('#mw-content-text')||document.querySelector('article')||document.body;return (a.innerText||'').slice(0,200000)})()")
    if not text:
        print(f"--- {label or url}: NO TEXT ---")
        return
    print(f"===== {label or url} (len={len(text)}) =====")
    for kw in keywords:
        idx = text.lower().find(kw.lower())
        if idx >= 0:
            print(f"--- [{kw}] @{idx} ---")
            print(text[max(0,idx-500):idx+win].replace("\n\n\n","\n\n"))
        else:
            print(f"--- [{kw}] NOT FOUND ---")

dump("https://en.wikipedia.org/wiki/Opus_Dei",
     ["Da Vinci Code", "Criticism", "controvers", "secretive", "personal prelature"],
     label="OPUS_DEI_WIKI")

dump("https://millercenter.org/the-presidency/presidential-speeches/september-11-1990-address-joint-session-congress",
     ["new world order", "dream of a new world order"],
     label="BUSH_1990_SPEECH")
