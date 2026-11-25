import re

def extract(url, selector, label, maxlen=4500):
    print(f"\n===== {label} :: {url} =====")
    try:
        goto_url(url)
        wait_for_load()
        txt = js(f"(()=>{{const el=document.querySelector({selector!r});return el?el.innerText:null}})()")
        if not txt:
            txt = js("document.body.innerText")
        if txt:
            txt = re.sub(r'\n{3,}', '\n\n', txt)
            print(txt[:maxlen])
        else:
            print("NO TEXT")
    except Exception as e:
        print("ERROR:", e)

# 1. Vatican motu proprio Ad charisma tuendum (English)
extract("https://www.vatican.va/content/francesco/en/motu_proprio/documents/20220714-motu-proprio-ad-charisma-tuendum.html",
        "div.content", "VATICAN AD CHARISMA TUENDUM")

# 2. Opus Dei Fact and Fiction (Da Vinci Code response)
extract("https://opusdei.org/en-us/article/opus-dei-fact-and-fiction/",
        "div.article-body", "OPUS DEI FACT AND FICTION")

# 3. Great Seal motto history page
extract("https://www.greatseal.com/mottoes/seclorum.html",
        "body", "GREATSEAL.COM SECLORUM")
