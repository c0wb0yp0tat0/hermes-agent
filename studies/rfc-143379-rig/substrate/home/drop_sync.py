#!/usr/bin/env python3
"""drop_sync.py — REPEATABLE RUN-ABLE DEFINITION FOR STAGE A2/PRESERVATION.

Mirrors the docs-of-record (master-page/ + /docs top-level + memory-chain +
deepdive-mission-flow + render assets) into /root/workspace/drop, preserving the
relative subdir structure (root-to-root mapping), stamps a creation date
(prefer git birth commit date on git repos, else filesystem birthtime, else
mtime flagged) into DROP-MANIFEST.md. ADDITIVE ONLY — nothing is deleted; a
destination is only ever created or overwritten to match source. Source docs
are never touched.

Mapping:
  /root/workspace/master-page/<rel>  ->  /root/workspace/drop/<rel>
  /root/docs/<top-level file>        ->  /root/workspace/drop/<basename>

Usage: python3 drop_sync.py [--dry-run]
"""
import os, sys, hashlib, datetime, subprocess, re

MASTER = "/root/workspace/master-page"
DOCS   = "/root/docs"
DROP   = "/root/workspace/drop"
MANIFEST = os.path.join(DROP, "DROP-MANIFEST.md")

# text/document extensions — the docs-of-record set
DOC_EXTS = (".md", ".html", ".css", ".js", ".txt", ".json", ".yaml", ".yml", ".py")
# render assets always mirrored regardless of ext (banners, marked.min.js, webp/png)
ASSET_DIRS = {"assets"}
ALWAYS = {"theme.js", "design-tokens.css", "visibility.html",
          "index-v1-20260917.html", "index-v2-20260918.html"}
SKIP_DIRS = set()

# prior-projects sources -> drop/prior-projects/<name> (mirror like the rest of the drop)
PRIOR_PROJECTS = [
    ("/root/workspace/altman_firing_deepdive", "altman-firing-deepdive"),
    ("/root/workspace/beast-session", "beast-session"),
    ("/root/workspace/frames-deep-dive", "frames-deep-dive"),
    ("/root/workspace/malware-watch", "malware-watch"),
    ("/root/workspace/news-gambit-deep-review", "news-gambit-deep-review"),
    ("/root/workspace/notes", "notes"),
    ("/root/workspace/transcripts", "transcripts"),
    ("/root/workspace/walled-blind-pilot", "walled-blind-pilot"),
]
# loose root .md files -> drop/prior-projects/loose/
PRIOR_LOOSE = "/root/workspace"
PRIOR_EXCLUDE = {"PROXMOX-SAFE-OPS-REFERENCE.md", "VIDEO-EXTRACTION-RECONSTRUCTION.md"}
# promoted loose files -> drop/prior-projects/<folder>/ (kept out of PRIOR_LOOSE so
# promotion persists across re-runs instead of being re-copied back to loose/)
PRIOR_PROMOTED = {
    "ufos-moon-discovery-log.md": "ufos-moon-deepdive",
    "ufos-moon-full-discovery.md": "ufos-moon-deepdive",
    "ufos-moon-investigation-review.md": "ufos-moon-deepdive",
    "gj-ai-training-feedback.md": "gj-ai-training-feedback",
    "gj-ai-training-feedback-elaboration.md": "gj-ai-training-feedback",
}

def is_git_repo(d):
    return os.path.isdir(os.path.join(d, ".git")) or os.path.isdir(os.path.join(d, ".git")) and subprocess.run(
        ["git", "-C", d, "rev-parse", "--git-dir"], capture_output=True).returncode == 0

def git_created(d, relpath):
    """Return git author/add date of first-added version of relpath in repo at d, else None."""
    try:
        r = subprocess.run(["git", "-C", d, "log", "--diff-filter=A",
                            "--format=%aI", "--", relpath],
                           capture_output=True, text=True, timeout=20)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip().splitlines()[-1][:19].replace("T", " ")
    except Exception:
        pass
    return None

def birthtime(path):
    try:
        out = subprocess.run(["stat", "-c", "%W", path], capture_output=True, text=True).stdout.strip()
        return int(out) if out and out != "-1" else None
    except Exception:
        return None

def fmt(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def collect(a_root, rel="", out=None):
    """Collect (src_path, rel, git_root) for doc + render files under a_root."""
    if out is None:
        out = []
    d = os.path.join(a_root, rel)
    try:
        names = sorted(os.listdir(d))
    except OSError:
        return out
    is_git = os.path.isdir(os.path.join(d, ".git"))
    for name in names:
        p = os.path.join(d, name)
        if os.path.islink(p):
            continue
        if os.path.isdir(p):
            if name.startswith(".") or name in SKIP_DIRS:
                continue
            collect(a_root, os.path.join(rel, name), out)
            continue
        if name.startswith("."):
            continue
        if name == "index.html" and not rel:
            continue  # drop root serves a FILE LISTING, not the home copy
        top_rel = os.path.basename(a_root)
        if is_git and not rel and False:
            pass
        # decide whether this file is in scope
        in_assset = (rel.split(os.sep)[0] in ASSET_DIRS)
        in_scope = name.endswith(DOC_EXTS) or in_assset or name in ALWAYS or os.path.basename(name) in ALWAYS
        if not in_scope:
            continue
        out.append((p, os.path.join(rel, name)))
    return out

def cd_for(src, rel, a_root):
    """Determine creation date: git (if repo) > birthtime > mtime. Returns (date, source_flag)."""
    # find git root by walking up from a_root
    gr = a_root
    while True:
        if subprocess.run(["git", "-C", gr, "rev-parse", "--git-dir"], capture_output=True).returncode == 0:
            gitd = git_created(gr, rel)
            if gitd:
                return gitd, "git"
            break
        parent = os.path.dirname(gr)
        if parent == gr:
            break
        gr = parent
    bt = birthtime(src)
    if bt:
        return fmt(bt), "birthtime"
    st = os.stat(src)
    return fmt(st.st_mtime), "mtime*"

def main():
    dry = "--dry-run" in sys.argv
    planned = []
    # 1) master-page tree, root-to-root (incl memory-chain, deepdive-mission-flow, assets)
    for src, rel in collect(MASTER):
        dest = os.path.join(DROP, rel)
        planned.append((src, rel, dest, MASTER))
    # 2) /docs top-level text files -> drop root by basename
    for name in sorted(os.listdir(DOCS)):
        p = os.path.join(DOCS, name)
        if os.path.islink(p) or os.path.isdir(p) or name.startswith("."):
            continue
        if name.endswith((".md", ".txt", ".json", ".yaml", ".yml", ".py")):
            planned.append((p, "docs/"+name, os.path.join(DROP, name), DOCS))
    # 3) prior-projects sources -> drop/prior-projects/<name>
    for src_root, dest_name in PRIOR_PROJECTS:
        for src, rel in collect(src_root):
            dest = os.path.join(DROP, "prior-projects", dest_name, rel)
            planned.append((src, "prior-projects/"+dest_name+"/"+rel, dest, src_root))
# 4) loose root .md files -> drop/prior-projects/loose/
    for name in sorted(os.listdir(PRIOR_LOOSE)):
        p = os.path.join(PRIOR_LOOSE, name)
        if os.path.islink(p) or os.path.isdir(p) or name.startswith("."):
            continue
        if name in PRIOR_EXCLUDE or name in PRIOR_PROMOTED or not name.endswith(".md"):
            continue
        dest = os.path.join(DROP, "prior-projects", "loose", name)
        planned.append((p, "prior-projects/loose/"+name, dest, PRIOR_LOOSE))
    # 4b) promoted loose files -> drop/prior-projects/<folder>/ (kept out of loose/)
    for name, folder in sorted(PRIOR_PROMOTED.items()):
        p = os.path.join(PRIOR_LOOSE, name)
        if not os.path.isfile(p):
            continue
        dest = os.path.join(DROP, "prior-projects", folder, name)
        planned.append((p, "prior-projects/"+folder+"/"+name, dest, PRIOR_LOOSE))

    # dedupe by dest (a collide: master has docs/... and /docs top-level? guard)
    seen = {}
    for src, rel, dest, a_root in planned:
        if dest in seen and seen[dest][0] != src:
            # collision — prefer the master-page source (render surface is authoritative)
            print(f"  [collision] {dest}: master-page vs docs — keeping master", file=sys.stderr)
            continue
        seen[dest] = (src, rel, a_root)

    manifest_rows = []
    copied = 0; skipped = 0
    for dest, (src, rel, a_root) in sorted(seen.items()):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        need = (not os.path.isfile(dest)) or (sha256(src) != sha256(dest))
        date, src_flag = cd_for(src, rel, a_root)
        h = sha256(src)
        manifest_rows.append((rel, date, src_flag, src, h, "synced" if not need else "PENDING"))
        if dry:
            if need:
                copied += 1
            else:
                skipped += 1
            continue
        if need:
            import shutil
            shutil.copy2(src, dest)
            print(f"  + {rel}")
            copied += 1
        else:
            skipped += 1

    # --- write manifest ---
    lines = []
    lines.append("# DROP-MANIFEST — machine-readable mirror record (drop_sync.py)\n")
    lines.append(f"*Generated {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by /root/scripts/drop_sync.py "
                 f"({'DRY-RUN' if dry else 'run'}). Mirror root: `{DROP}` (served :8788). "
                 f"`creation_date` = git add-date on git repos, else filesystem birthtime, else mtime flagged `*`.*\n")
    lines.append("| relative_path | creation_date | date_source | source_path | sha256 |")
    lines.append("|---|---|---|---|---|")
    for rel, date, src_flag, src, h, state in manifest_rows:
        lines.append(f"| {rel} | {date} | {src_flag} | {src} | {h} |")
    lines.append(f"\n*Entries: {len(manifest_rows)} · newly copied: {copied} · already-current: {skipped}*")
    content = "\n".join(lines) + "\n"
    if not dry:
        with open(MANIFEST, "w") as f:
            f.write(content)
        print(f"\nWROTE {MANIFEST} ({len(content)} bytes) · entries={len(manifest_rows)} · copied={copied} · current={skipped}")
    else:
        print(f"\nDRY-RUN: would copy {copied}, skip {skipped}, manifest entries={len(manifest_rows)}")

if __name__ == "__main__":
    main()