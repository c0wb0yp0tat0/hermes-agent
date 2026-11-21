#!/usr/bin/env python3
"""home-update.py — regenerate every derivable block of the living home page.

Owns the blocks between AUTO marker comments in index.html, each generated from
a canonical source (single source of truth; do NOT hand-edit the generated
blocks):

  Block            Canonical source            Renders
    ---------------  -------------------------   -------------------------------------
    Recent activity  ACTIVITY.md                 visible <ul> + changelog link
    Status table     STATUS.md                   <table class="kv"> rows (Key | value)
    Open items       OPEN-ITEMS.md              <ul class="plain"> of <li> items
    Docs grid        DOC-INDEX.md                two <details class="card"> groups
    Projects         PROJECTS.md                 <ul class="plain"> tracker rows

Idempotent: if every rendered block is byte-identical to what's already in the
file, the file is NOT rewritten (no mtime churn). Never touches any other part
of index.html. Stdlib only, no dependencies.

Run via root cron every 5 minutes (quiet on success, errors to stderr).

Link-integrity self-check (added by whole-mission supervisor, 2026-09-19):
after the fold, verify_links() reports any LOCAL href in the generated blocks
that points to a file missing on disk — the 1-year test (no silent rot) applied
to the home's own links. External https:// links and anchors are skipped.
"""
import os
import re
import sys
import datetime

INDEX = "/root/workspace/master-page/index.html"
ACTIVITY = "/root/workspace/master-page/ACTIVITY.md"
STATUS = "/root/workspace/master-page/STATUS.md"
OPEN_ITEMS = "/root/workspace/master-page/OPEN-ITEMS.md"
DOC_INDEX = "/root/workspace/master-page/DOC-INDEX.md"
MECHANISM_STATUS = "/root/workspace/master-page/MECHANISM-STATUS.md"
PROJECTS = "/root/workspace/master-page/PROJECTS.md"
N_VISIBLE = 4  # minimum recent entries shown; the block also shows ALL of today's entries

# (start_marker, end_marker) per block
BLOCKS = {
    "recent-activity": ("<!-- AUTO: recent-activity-start -->", "<!-- AUTO: recent-activity-end -->"),
    "status":          ("<!-- AUTO: status-start -->",          "<!-- AUTO: status-end -->"),
    "open-items":      ("<!-- AUTO: open-items-start -->",      "<!-- AUTO: open-items-end -->"),
    "docs":            ("<!-- AUTO: docs-start -->",            "<!-- AUTO: docs-end -->"),
    "mechanisms":      ("<!-- AUTO: mechanisms-start -->",      "<!-- AUTO: mechanisms-end -->"),
    "projects":        ("<!-- AUTO: projects-start -->",        "<!-- AUTO: projects-end -->"),
}

# Local link roots for the two md_servers (host -> on-disk root). Used by the
# link-integrity check so a rotted href (a link to a file that was planned but
# never created) is caught at fold time instead of silently 404ing for a year.
LINK_ROOTS = {
    "localhost:8789": "/root/workspace/master-page/",
    "localhost:8788": "/root/workspace/drop/",
}


def load_lines(path, predicate):
    """Return the ordered list of non-empty lines matching predicate, stripped of newline."""
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            if predicate(line):
                out.append(line)
    return out


def load_activity():
    """Recent-activity <li> inner-HTML strings, newest first."""
    return load_lines(ACTIVITY, lambda l: re.match(r"^\d{4}-\d{2}-\d{2}", l) or "<b>" in l)


def load_status():
    """Status rows as (key, value) pairs from 'Key | value' lines.

    Only lines whose key is a plain word/phrase (letters, digits, spaces) followed
    by ' | ' are data rows — this skips the file's header/convention prose.
    """
    rows = []
    for line in load_lines(STATUS, lambda l: re.match(r"^[A-Za-z][A-Za-z0-9 ]* \| ", l)):
        key, _, value = line.partition("|")
        rows.append((key.strip(), value.strip()))
    return rows


def load_open_items():
    """Open-items <li> inner-HTML strings."""
    return load_lines(OPEN_ITEMS, lambda l: "<span" in l or "<b>" in l)


def load_doc_index():
    """Docs groups as [(summary_text, open_bool, [<li> inner-HTML strings])]."""
    groups = []
    current = None
    for line in load_lines(DOC_INDEX, lambda l: l.startswith("## ") or "<a " in l):
        if line.startswith("## "):
            header = line[3:].strip()
            open_flag = header.endswith(" (open)")
            summary = header[: -len(" (open)")] if open_flag else header
            current = [summary, open_flag, []]
            groups.append(current)
        elif current is not None:
            current[2].append(line)
    return groups


def load_mechanisms():
    """Mechanism-status rows as (name, status, evidence_link) from 'Name | status | link' lines.

    Only lines matching 'Name | status | link' are data rows — this skips the
    file's header/convention prose. The status is one of the status-vocabulary
    values (FIRED / DORMANT / MIS-FIRED / CORRECTLY-ABSENT).
    """
    rows = []
    for line in load_lines(MECHANISM_STATUS, lambda l: re.match(r"^[A-Za-z][A-Za-z0-9 &]* \| (FIRED|DORMANT|MIS-FIRED|CORRECTLY-ABSENT) \| ", l)):
        name, _, rest = line.partition("|")
        status, _, link = rest.partition("|")
        rows.append((name.strip(), status.strip(), link.strip()))
    return rows


def load_projects():
    """Project tracker rows as (name, status, one_line, next_step, hitl, last_moved).

    From 'Name | status | one-line | NEXT STEP | hitl-link | last-moved' lines.
    Only lines with 6 pipe-separated fields are data rows (skips header prose).
    """
    rows = []
    for line in load_lines(PROJECTS, lambda l: l.count("|") >= 5):
        parts = [p.strip() for p in line.split("|")]
        rows.append((parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))
    return rows


def render_projects(rows):
    """Compact mobile-safe tracker: status tag + bold name + one-line + next: + HITL link + date."""
    tag_class = {"done": "tag ok", "active": "tag", "parked": "tag", "blocked": "tag bad"}
    out = []
    for name, status, one_line, next_step, hitl, last_moved in rows:
        cls = tag_class.get(status, "tag")
        hitl_link = hitl
        out.append("          <li><span class=\"%s\">%s</span> <b>%s</b> — %s <span class=\"li-sub\">next: %s · <a href=\"%s\">%s</a> · %s</span></li>"
                   % (cls, status.upper(), name, one_line, next_step, hitl_link,
                      hitl.split("/")[-1].replace(".md", ""), last_moved))
    return "\n".join(out) + "\n"


def render_mechanisms(rows):
    out = []
    for name, status, link in rows:
        tag = "tag ok" if status == "FIRED" else "tag"
        out.append("          <tr><th>%s</th><td><span class=\"%s\">%s</span> <a href=\"%s\">%s</a></td></tr>"
                   % (name, tag, status, link, link.split("/")[-1].replace(".md", "")))
    return "\n".join(out) + "\n"


def render_recent(entries):
    today = datetime.date.today().strftime("%Y-%m-%d")
    today_count = sum(1 for e in entries if e.startswith(today) or ("<b>%s</b>" % today) in e)
    visible = entries[:max(N_VISIBLE, today_count)]
    out = []
    out.append("    <ul class=\"plain\">")
    for e in visible:
        out.append("      <li>%s</li>" % e)
    out.append("    </ul>")
    # Tracker altitude (S5): the changelog lives downstream, not on the home.
    # One link to CHANGELOG.md replaces the 25-entry 'Older activity' collapsible.
    out.append("    <div class=\"changelog-link\"><a href=\"CHANGELOG.md\">Older activity → CHANGELOG</a> · <a href=\"ACTIVITY.md\">view all → ACTIVITY</a></div>")
    return "\n".join(out) + "\n"


def render_status(rows):
    out = []
    for key, value in rows:
        out.append("      <tr><th>%s</th><td>%s</td></tr>" % (key, value))
    return "\n".join(out) + "\n"


def count_non_done_projects():
    """(non_done, total) project counts from PROJECTS.md (active/parked/blocked)."""
    rows = load_projects()
    non_done = sum(1 for r in rows if r[1] in ("active", "parked", "blocked"))
    return non_done, len(rows)

def count_mission_docs():
    """Number of top-level .md docs in deepdive-mission-flow/ (the in-flight material)."""
    root = "/root/workspace/master-page/deepdive-mission-flow/"
    return sum(1 for f in os.listdir(root) if f.endswith(".md"))

def render_open_items(items):
    non_done, total = count_non_done_projects()
    docs = count_mission_docs()
    out = []
    out.append("      <h2>Open items — %d of %d projects · %d mission docs</h2>" % (non_done, total, docs))
    out.append("      <ul class=\"plain\">")
    for item in items:
        out.append("      <li>%s</li>" % item)
    out.append("      </ul>")
    return "\n".join(out) + "\n"


def render_docs(groups):
    out = []
    for summary, open_flag, links in groups:
        out.append("    <details class=\"card\"%s>" % (" open" if open_flag else ""))
        out.append("      <summary>%s</summary>" % summary)
        out.append("      <div class=\"inner\">")
        out.append("        <ul class=\"plain\">")
        for link in links:
            out.append("          <li>%s</li>" % link)
        out.append("        </ul>")
        out.append("      </div>")
        out.append("    </details>")
    return "\n".join(out) + "\n"


def render_block(name):
    if name == "recent-activity":
        return render_recent(load_activity())
    if name == "status":
        return render_status(load_status())
    if name == "open-items":
        return render_open_items(load_open_items())
    if name == "docs":
        return render_docs(load_doc_index())
    if name == "mechanisms":
        return render_mechanisms(load_mechanisms())
    if name == "projects":
        return render_projects(load_projects())
    raise ValueError("unknown block: %s" % name)




# Full-page sweep: every section of the home must be present in the rendered
# output. A fix that touches one half and leaves the other stale is a failed
# landing (the half-page trap — the user fought this for 24h+). This is
# mechanical, not procedural: the generator itself fails if any section is
# missing, so every 5-min cron run and every manual run enforces the sweep.
FULL_PAGE_SECTIONS = [
    "pulse-main", "Agents", "Telegram", "Local bench", "Projects",
    "GitHub feedback loop", "Workshop", "Status", "Mechanisms",
    "Open items", "Recent activity", "Plans &amp; kits", "Docs",
]

def verify_full_page(html):
    """Report any missing section to stderr; return the count missing (0 = full page)."""
    missing = 0
    for sec in FULL_PAGE_SECTIONS:
        if sec not in html:
            sys.stderr.write("home-update: FULL-PAGE SWEEP FAIL — section missing: %s\n" % sec)
            missing += 1
    return missing

def verify_links(html):
    """Report broken LOCAL hrefs in the generated AUTO blocks to stderr.

    Returns the count of broken links (0 = clean). A link is checked only when
    it is a relative path or an absolute URL on one of the known md_server hosts;
    external https:// links, anchors, and protocol links are skipped. Route-style
    links (e.g. /visibility -> visibility.html, / -> index.html) are resolved the
    way md_server serves them. This is the fold's self-check: the 1-year test
    (no silent rot) applied to the home's own links.
    """
    broken = 0
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(("#", "mailto:", "tel:", "javascript:", "https://")):
            continue  # anchors, protocols, external https
        if href.startswith("http://"):
            host = href.split("/")[2]
            root = LINK_ROOTS.get(host)
            if root is None:
                continue  # external http on an unknown host, skip
            path = root + "/".join(href.split("/")[3:])
        else:
            # relative path -> resolve against the master-page root
            path = LINK_ROOTS["localhost:8789"] + href
        path = path.split("#")[0].split("?")[0]
        # Resolve route-style links the way md_server serves them: a bare path
        # maps to <path>.html, and the root maps to index.html.
        candidates = [path]
        if not path.endswith((".md", ".html", ".css", ".js", ".png", ".jpg",
                              ".jpeg", ".gif", ".svg", ".mp4", ".txt", ".pdf",
                              ".json", "/")):
            candidates.append(path + ".html")
        if path.rstrip("/") == LINK_ROOTS["localhost:8789"].rstrip("/"):
            candidates.append(LINK_ROOTS["localhost:8789"] + "index.html")
        if not any(os.path.exists(c) for c in candidates):
            sys.stderr.write("home-update: BROKEN LINK %s -> %s (missing on disk)\n" % (href, path))
            broken += 1
    return broken


def main():
    with open(INDEX, encoding="utf-8") as f:
        html = f.read()

    changed = False
    for name, (start, end) in BLOCKS.items():
        if start not in html or end not in html:
            sys.stderr.write("home-update: AUTO markers not found for %s in %s\n" % (name, INDEX))
            return 1
        start_idx = html.index(start) + len(start)
        end_idx = html.index(end)
        old_block = html[start_idx:end_idx]
        # Leading newline keeps the block on its own line after the start marker;
        # trailing 4 spaces keep the end marker indented like its sibling lines.
        new_block = "\n" + render_block(name) + "    "
        if old_block != new_block:
            html = html[:start_idx] + new_block + html[end_idx:]
            changed = True

    if not changed:
        # no-op, idempotent — but still self-check the links on every run
        verify_links(html)
        if verify_full_page(html):
            return 1
        return 0

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(html)
    verify_links(html)
    if verify_full_page(html):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
