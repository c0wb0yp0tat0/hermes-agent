import probe_alias, os
os.chdir("/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/krecency")
rows=probe_alias.run_sweep()
print("rows",len(rows))