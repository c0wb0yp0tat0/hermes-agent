"""utils — the atomic write primitive the pinned store imports (extracted from the repo, stdlib-only)."""

import os
import tempfile
from pathlib import Path

def atomic_write_text(path: str | Path, content: str, *, encoding: str = "utf-8", tmp_prefix: str = ".tmp_",
                      preserve_mode: bool = False, create_mode: int | None = None, mode: int | None = None,
                      fsync_dir: bool = False) -> None:
    """Write *content* to *path* via temp file + fsync + atomic rename.

    The target is never left partially written on crash/interrupt. Shared by every destructive
    file rewrite (memory store, skill manager, agent importer, ...). *mode* forces the final
    permission bits (secret files: ``0o600``) regardless of what exists; *create_mode* applies only
    when the target is new and *preserve_mode* carries an existing file's bits and owner across.
    """
    path = Path(path)
    _atomic_write(path, lambda f: f.write(content), prefix=tmp_prefix, encoding=encoding,
                  mode=mode if mode is not None else _mode_for_write(path, create_mode, preserve=preserve_mode),
                  preserve_owner=preserve_mode, fsync_dir=fsync_dir)
