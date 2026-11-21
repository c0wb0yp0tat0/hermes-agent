#!/bin/bash
ROW="/tmp/hour8-pointer-row.md"
printf "%s\n" \
"envelope: {\"id\":\"20261107-hour8-pointer\",\"kind\":\"handoff+state\",\"from\":\"head\",\"to\":[\"thread\"],\"status\":\"row-posted\"}" \
"" \
"**Hour 8 - the mission's end, and the operator's chair is the receiver.** The proposals staged through the night (the die-fallback's experiments, the reserve's opportunities, the standby's fallback-wave) wait at studies/rfc-143379-rig/STANDBY-MATERIAL-20261107.md plus the OPPORTUNITIES/MISSED files (committed at the fold-pins). The operator's word gates every staged item; nothing fires, everything is named, the receiver is the chair." > "$ROW"
jq -n --rawfile b "$ROW" '{body:$b}' | gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments --input - --jq '{id: .id}' >> /root/.hermes/cache/scratch/hour8-pointer-log.txt 2>&1
echo "hour8-pointer complete $(date)" >> /root/.hermes/cache/scratch/hour8-pointer-log.txt
