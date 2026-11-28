"""Bundle seam (NAMED, mirrors tools/registry.py:272-275 of the artifact):
no_cache_check_fn marks a local availability check as uncached and returns it
unchanged — a decorator on the tool surface, never on the read path."""
_NO_CACHE_CHECK_FNS = set()


def no_cache_check_fn(fn):
    _NO_CACHE_CHECK_FNS.add(fn)
    return fn
