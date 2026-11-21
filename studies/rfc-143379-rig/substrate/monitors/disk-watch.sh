#!/usr/bin/env bash
# Disk-watch wrapper: quiet unless root free space < 5GB (watchdog pattern).
# Calls the canonical disk-alert.sh; stdout carries ONLY the WARN line.
# The 5G floor = the house's action line (DISK-BUDGET tier). Crashes begin under
# sustained 4-lane contention below ~8G, but the box's equilibrium is ~6.1G free
# (91%); the old 7G floor alarmed on every tick while nothing actionable existed.
# The trend stays visible in disk-alert.log on every run; the alert fires only
# when free drops under the 5G action line.
bash /root/scripts/disk-alert.sh 5