import subprocess, sys, os
os.chdir("/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/krecency")
subprocess.run([sys.executable,"probe_recite.py"],check=True)
print("sweep done")
