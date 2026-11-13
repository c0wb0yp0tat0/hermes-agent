import io
p = "/root/workspace/.worktrees/compose-20261108/agent/context_compressor.py"
src = io.open(p, encoding="utf-8").read()
bad = "compacted region \\u2014 use these verbatim"
good = "compacted region \u2014 use these verbatim"
assert src.count(bad) == 1, src.count(bad)
src = src.replace(bad, good)
io.open(p, "w", encoding="utf-8").write(src)
print("footer-fixed")