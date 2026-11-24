# BeautifulBeast Handoff — SSH access + Antenna (RTL8822bu) investigation

## Access
- Host: BeautifulBeast, Debian 13 (trixie), 192.168.1.200 (eth) / 192.168.1.199 (wifi), user `c0wb0y`
- Reachable from pve-1 (192.168.1.179) on LAN; port 22 OPEN on both IPs
- Auth: password (provided by user in session; NOT stored here). Key auth NOT yet set up (offered, awaiting go-ahead)
- PASSWORDLESS SUDO ON BEAST: c0wb0y has `NOPASSWD: ALL` (user granted trust via /etc/sudoers.d/c0wb0y-trust during troubleshooting)
- CAREFUL: user was burned by earlier probing (fear of block lists). Always get explicit approval + credentials before connecting/probing.

## Recall files (this dir)
- `last-session.json` — raw request dump of the last Hermes session on Beast (901 messages, ended on HTTP 503 max_retries)
- `transcript.txt` — readable ordered transcript of that session (read twice; full picture below)

## Machine state at handoff (end of Beast session 20260811_115749_5f7394)
- Booting kernel **6.1.0-50-amd64 by default** (GRUB_DEFAULT set to wifi-kernel entry at user request; 6.12.101 still installed + in Advanced options)
- 88x2bu driver (RinCat fork) built+installed for BOTH 6.1 and 6.12; stock rtw88 blacklisted; lwfinger rtw88 removed
- Internet works via: ethernet enp42s0 (100Mbps, PHY downshift = cable, user's only long cable) + MT7601U wifi wlx3c3300006a6a (the "cheap" dongle — currently the ONLY working wifi)
- RTL8822bu "good" dongle (0bda:b812 Techkey AC1200): interface wlx00e04c35fc8a created by 88x2bu but radio dead (txpower -100, scan EPERM, firmware download fails at chip level)
- Coral TPU: unplugged (was in the USB3 port), gasket DKMS removed to unblock 6.1 install, libedgetpu1-std installed, udev rule present. Reinstall needed later.
- Hermes on Beast: memory ON, skills hub init, streaming ON

## The antenna root-cause saga (verified in session)
- rtw88 (stock + lwfinger): "invalid fw checksum" — chip's DMA rejects firmware bytes
- 88x2bu (morrownr + RinCat): interface created, radio dead
- 6.1 kernel boot: STILL fails — `RTW: _debug_dlfw_fail: 0x80 = 0x0020`, `ERROR rtl8822b_hal_init Download Firmware from array failed`
- KEY FINDING at very end of session: 88x2bu build lacks `CONFIG_FILE_FWIMG`, so it ALWAYS uses embedded firmware array (ignores /lib/firmware/rtl8822b/FW_NIC.bin which was placed)
- **cilynx/rtl88x2bu driver cloned to /tmp/rtl88x2bu (and /tmp/cilynx-rtl88x2bu) but NEVER BUILT/TESTED** — its embedded firmware array is DIFFERENT: 160504 bytes md5 88a7bc29... (RinCat: 161240 bytes md5 e155ac20...). Untested variable.
- Pi users reportedly run this exact antenna successfully (yduf page); cilynx is the Pi-community driver. CONFIG_FILE_FWIMG / firmware handling differs.

## User's research direction (from handoff message)
1. Emulate penetration-tester approach: **two wifi dongles active simultaneously** on Beast so we can transition without killing connectivity (both "network managers" on the wifi dongle — verify what this means technically)
2. Raspberry Pi community knowledge for this device
3. This host (pve-1) = research machine; do the deep-dive HERE, not on Beast
4. No touching Beast without explicit approval

## Open items
- [ ] Test cilynx driver build on 6.12 (or 6.1) — the different firmware array may fix the radio
- [ ] Decide GRUB default (6.1 vs restore 6.12) — assistant recommended restoring 6.12; user said stop/keep looking
- [ ] Coral TPU reinstall (gasket DKMS re-add + replug)
- [ ] Key auth setup on Beast (offered, awaiting approval)
- [ ] MT7601U eventually returns to uConsole; ethernet cable is the permanent 100Mbps limit
