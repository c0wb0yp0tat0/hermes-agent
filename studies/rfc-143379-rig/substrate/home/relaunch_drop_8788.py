#!/usr/bin/env python3
"""Launch md_server for the drop (:8788) as a fully detached daemon.

Double-fork + setsid so the process re-parents to init and is NOT a child of
the launching shell/subagent session. Survives the orchestrator's exit.
Usage: python3 /root/scripts/relaunch_drop_8788.py
"""
import os, sys, time

CMD = ["/usr/bin/python3", "/root/md_server.py", "/root/workspace/drop", "8788", "0.0.0.0"]
LOG = "/root/.hermes/logs/drop-8788.out.log"
ERR = "/root/.hermes/logs/drop-8788.err.log"

def daemonize():
    os.umask(0)
    # first fork
    try:
        pid = os.fork()
    except OSError:
        sys.exit("first fork failed")
    if pid > 0:
        os._exit(0)
    os.setsid()
    os.chdir("/")
    # second fork
    try:
        pid = os.fork()
    except OSError:
        sys.exit("second fork failed")
    if pid > 0:
        os._exit(0)
    devnull = os.open(os.devnull, os.O_RDWR)
    if LOG:
        err_fd = os.open(ERR, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
        os.dup2(err_fd, 2)
        os.close(err_fd)
    os.dup2(devnull, 0)
    os.dup2(devnull, 1)
    os.close(devnull)

if __name__ == "__main__":
    daemonize()
    os.execvp(CMD[0], CMD)