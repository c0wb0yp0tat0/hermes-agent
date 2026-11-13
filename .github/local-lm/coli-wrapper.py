#!/usr/bin/env python3
"""colibri launcher wrapper for the local-lm battery (rig/local-lm-colibri branch).

The colibri launcher (colibri.cli:main) resolves its modules from the repo's
c/ dir and finds engine binaries NEXT TO the script (HERE). This wrapper is
copied into engine/ by the workflow, so:
  - HERE = engine/        -> engine/olmoe is discovered beside it
  - /tmp/colibri + c/     -> the source clone's modules resolve (family_registry...)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
for p in ("/tmp/colibri", "/tmp/colibri/c"):
    if p not in sys.path:
        sys.path.insert(0, p)

from colibri.cli import main

main()
