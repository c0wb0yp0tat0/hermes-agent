#!/usr/bin/env python3
"""ARXIV-WATCH — the pre-print stream for the rig's domains (scholarly-first).

The user's method, mechanized: the pre-print RSS/API feeds surface the bleeding
edge BEFORE formal publication — the mechanisms live there. This watcher
queries the arXiv API for the rig's topics, tracks seen entries, and reports
new pre-prints. The scholarly-first path: Stanford-banked, mechanism-harvested.
"""
import json, os, re, sys, urllib.request, urllib.parse, datetime

STATE = "/root/.hermes/cache/scratch/arxiv-watch/state.json"
TOPICS = [
    "agent memory",
    "context compression",
    "self-improving agents",
    "durable execution",
    "memory consolidation",
    "context management",
]

# Per-topic page size. 5 was a blind spot: the feed holds ~20 fresh pre-prints
# per domain and only the top 5 were ever fetched, so the watcher missed the
# bulk of the stream (measured 51 unseen @20 vs 2 unseen @5).
MAX_RESULTS = 20

def fetch(topic, max_results=MAX_RESULTS):
    q = urllib.parse.quote('all:"{}"'.format(topic))
    url = ("https://export.arxiv.org/api/query?search_query={}"
           "&start=0&max_results={}&sortBy=submittedDate&sortOrder=descending").format(q, max_results)
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return resp.read().decode()
    except Exception as e:
        return ""

def parse(xml):
    entries = []
    for m in re.finditer(r"<entry>(.*?)</entry>", xml, re.S):
        e = m.group(1)
        eid = re.search(r"<id>http://arxiv.org/abs/([^<]+)</id>", e)
        title = re.search(r"<title>([^<]+)</title>", e)
        date = re.search(r"<published>([^<]+)</published>", e)
        if eid:
            entries.append({
                "id": eid.group(1),
                "title": re.sub(r"\s+", " ", title.group(1)).strip() if title else "?",
                "published": date.group(1)[:10] if date else "?",
            })
    return entries

def main():
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    seen = {}
    if os.path.exists(STATE):
        seen = json.load(open(STATE))

    new_found = []
    for topic in TOPICS:
        xml = fetch(topic)
        for e in parse(xml):
            if e["id"] not in seen:
                seen[e["id"]] = {"topic": topic, "title": e["title"], "published": e["published"]}
                new_found.append((topic, e))

    _tmp = STATE + ".tmp"
    json.dump(seen, open(_tmp, "w"), indent=1)
    os.replace(_tmp, STATE)

    if new_found:
        print("NEW PRE-PRINTS ({}):".format(len(new_found)))
        for topic, e in new_found:
            print("  [{}] {} — {} ({})".format(topic, e["title"][:70], e["id"], e["published"]))
    else:
        print("ARXIV-WATCH: no new pre-prints in the tracked topics ({} seen total)".format(len(seen)))

if __name__ == "__main__":
    main()
