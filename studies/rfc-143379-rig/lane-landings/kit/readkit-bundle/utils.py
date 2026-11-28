"""Bundle seam (NAMED): utils — the read battery's measured import surface,
verbatim from the real artifact: TRUTHY_STRINGS, is_truthy_value,
_atomic_write, atomic_write_text. The rest of utils (yaml wrappers, env
helpers, ...) is not hit by the read path and stays out of the bundle."""
import errno
import logging
import os
import shutil
import tempfile
import time
from contextlib import suppress
from pathlib import Path
from typing import Any, Optional

TRUTHY_STRINGS = frozenset({"1", "true", "yes", "on"})

def is_truthy_value(value: Any, default: bool = False) -> bool:
    """Coerce bool-ish values using the project's shared truthy string set."""
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip().lower() in TRUTHY_STRINGS
    return bool(value)

def _atomic_write(path: Path, write, *, prefix: str, encoding: str = "utf-8", mode: int | None = None,
                  preserve_owner: bool = True, binary: bool = False, fsync_dir: bool = False) -> None:
    """Temp file + fsync + :func:`atomic_replace`, then re-apply owner/mode.

    *write(f)* emits the payload into the open handle (text, or bytes when *binary*). The temp file
    is created by ``mkstemp`` — ``O_CREAT|O_EXCL`` at 0600 regardless of umask — so a secret is
    never readable at process umask, not even between create and chmod. *mode* is fchmod'd onto
    the temp fd BEFORE the replace so the target never transits through mkstemp's 0600 (fchmod is
    Unix-only; the post-replace chmod is the sole path on Windows). With no *mode* a NEW target
    gets what ``open(path, "w")`` would have given it (process umask) — the callers this replaced
    wrote at umask, and silently tightening every fresh cache/state file to 0600 breaks shared
    volume mounts; an existing target with no *mode* keeps mkstemp's bits, as before. *fsync_dir*
    also fsyncs the resolved target's parent so the rename itself is durable. The temp file is
    removed on any failure — ``BaseException`` on purpose, so KeyboardInterrupt / SystemExit still
    clean up.
    """
    # A profile delete leaves a tombstone beside its removed home.  Background
    # writers may retain that home in a context variable, so a plain mkdir here
    # would resurrect the profile before the write can fail.
    from hermes_constants import mkdir_under_hermes_home

    mkdir_under_hermes_home(path.parent)
    if mode is None and not path.exists():
        mode = default_new_file_mode()
    original_owner = _preserve_file_owner(path) if preserve_owner else None
    fd, tmp_path = mkstemp_beside(path, prefix=prefix, suffix=".tmp")
    try:
        with os.fdopen(fd, "wb" if binary else "w", encoding=None if binary else encoding) as f:
            if mode is not None and hasattr(os, "fchmod"):
                os.fchmod(f.fileno(), mode)
            write(f)
            f.flush()
            os.fsync(f.fileno())
        replaced = Path(atomic_replace(tmp_path, path))  # symlink-preserving actual destination
        _restore_file_metadata(replaced, original_owner, mode)
        if fsync_dir:
            fsync_directory(replaced.parent)
    except BaseException:
        with suppress(OSError):
            os.unlink(tmp_path)
        raise

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

def _mode_for_write(path: Path, create_mode: int | None, preserve: bool = True) -> int | None:
    """Existing permission bits of *path* (when *preserve*), else *create_mode* for a new file."""
    mode = _preserve_file_mode(path) if preserve else None
    return mode if mode is not None or path.exists() else create_mode

def _is_contended_windows_replace_error(exc: OSError) -> bool:
    """Candidate-only: winerror 5 also covers a genuine ACL denial."""
    return _IS_WINDOWS and getattr(exc, "winerror", None) in _WINDOWS_CONTENDED_REPLACE_ERRORS

def _preserve_file_mode(path: Path) -> int | None:
    """Permission bits of *path* if it exists, else ``None``."""
    try:
        return stat.S_IMODE(path.stat().st_mode) if path.exists() else None
    except OSError:
        return None

def _preserve_file_owner(path: Path) -> tuple[int, int] | None:
    """Owning ``(uid, gid)`` of *path* on POSIX, else ``None``."""
    try:
        st = path.stat() if os.name == "posix" else None
    except OSError:
        return None
    return (st.st_uid, st.st_gid) if st else None

def _publish_path(target_str: str) -> str:
    """The path :func:`atomic_replace` renames onto: a symlink's real file, else the target itself."""
    return os.path.realpath(target_str) if os.path.islink(target_str) else target_str

def _restore_file_metadata(path: Path, owner: tuple[int, int] | None, mode: int | None) -> None:
    """Best-effort re-apply of uid/gid and permission bits after an atomic replace.

    Docker/NAS installs often run some commands as root on a volume owned by the runtime user;
    ``os.replace`` swaps in the temp file's owner, so privileged callers chown it back. ``mkstemp``
    creates 0o600 files; without re-applying *mode* the target would inherit that and break
    volume mounts relying on broader permissions.
    """
    if owner is not None and hasattr(os, "chown"):
        with suppress(OSError):
            os.chown(path, owner[0], owner[1])
    if mode is not None:
        with suppress(OSError):
            os.chmod(path, mode)

def atomic_replace(tmp_path: str | Path, target: str | Path) -> str:
    """Atomically move *tmp_path* onto *target*, preserving symlinks.

    Resolves a symlink first so ``os.replace`` writes the real file in place and the symlink
    survives. Otherwise identical to ``os.replace`` unless the rename fails with EXDEV/EBUSY
    (cross-device, bind-mount, busy file: copy/fsync/unlink immediately — these never clear on
    retry) or a Windows rename contended by another open handle (winerror 5/32/33: bounded retry,
    then in-place rewrite).
    """
    target_str = str(target)
    real_path = _publish_path(target_str)
    tmp_str = str(tmp_path)
    try:
        os.replace(tmp_str, real_path)
        return real_path
    except OSError as exc:
        contended = _is_contended_windows_replace_error(exc)
        if exc.errno not in _CROSS_DEVICE_ERRNOS and not contended:
            raise
        if contended:
            # Lazy: keeps ``utils`` free of a package-level dependency on ``agent``.
            from agent.retry_utils import jittered_backoff
            for attempt in range(1, _REPLACE_RETRY_ATTEMPTS + 1):
                time.sleep(jittered_backoff(attempt, base_delay=_REPLACE_RETRY_BASE_DELAY_S, max_delay=_REPLACE_RETRY_MAX_DELAY_S))
                try:
                    os.replace(tmp_str, real_path)
                    return real_path
                except OSError as retry_exc:
                    exc = retry_exc
                    if retry_exc.errno in _CROSS_DEVICE_ERRNOS:
                        contended = False  # not contention after all — stop burning the budget
                        break
                    if not _is_contended_windows_replace_error(retry_exc):
                        raise
        logger.debug("atomic_replace: %s -> %s failed with %s; falling back to %s", tmp_str, real_path,
                     getattr(exc, "winerror", None) or errno.errorcode.get(exc.errno or 0, exc.errno),
                     "in-place rewrite" if contended else "copy")
        # The rewrite re-raises its own error, so an ACL denial is reported as such, not as contention.
        (_rewrite_in_place if contended else _copy_fallback)(tmp_str, real_path)
    return real_path

def default_new_file_mode() -> int | None:
    """The mode ``open(path, "w")`` gives a file it has to create (``0o666 & ~umask``); ``None``
    when the umask cannot be read or on non-POSIX hosts (Windows mode bits are synthesized).

    ``mkstemp`` always creates at 0600, so publishing a *new* non-secret file through a temp
    file would tighten it to owner-only — the Docker/NAS volume-mount hazard
    :func:`_restore_file_metadata` documents. The transient mask is 0o077: a thread that opens
    a file in the read window gets a tighter file, never a looser one.
    """
    if os.name != "posix":
        return None
    try:
        current = os.umask(0o077)
        os.umask(current)
    except OSError:
        return None
    return 0o666 & ~current

def fsync_directory(path: str | Path) -> None:
    """Best-effort fsync of a directory entry so a just-renamed file survives power loss.

    No-op on Windows (directories can't be opened with ``os.open``; the file fsync still applies)
    and on any OSError — durability of the directory entry is never worth failing a write that
    has already been replaced into place.
    """
    if os.name == "nt":
        return
    try:
        fd = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    except OSError:
        return
    try:
        with suppress(OSError):
            os.fsync(fd)
    finally:
        os.close(fd)

def mkstemp_beside(target: str | Path, **kw: Any) -> tuple[int, str]:
    """``tempfile.mkstemp`` in the directory :func:`atomic_replace` will rename into.

    A temp staged next to a symlink whose target lives on another filesystem turns the publish
    rename into EXDEV, and atomic_replace's copy fallback then rewrites the file in place (torn on
    a crash). Staging beside the resolved target keeps the rename atomic. If that directory is not
    writable to us (the file itself may still be), stage beside the link instead: the save keeps
    working through the non-atomic copy fallback, exactly as before.
    """
    target_str = str(target)
    link_dir = str(Path(target_str).parent)
    stage_dir = os.path.dirname(_publish_path(target_str)) or link_dir
    try:
        return tempfile.mkstemp(dir=stage_dir, **kw)
    except PermissionError:
        if stage_dir == link_dir:
            raise
        return tempfile.mkstemp(dir=link_dir, **kw)
