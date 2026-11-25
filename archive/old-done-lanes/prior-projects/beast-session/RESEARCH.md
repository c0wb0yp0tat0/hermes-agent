# BeautifulBeast Antenna Research Brief — RTL88x2bu / 0bda:b812 (Techkey AC1200)

**Date:** 2026-08-11 · **Researched from:** pve-1 (research host) · **Target:** BeautifulBeast (192.168.1.200)
**Status:** DRAFT FOR REVIEW — no actions taken on Beast; nothing applied yet.

---

## 1. Problem statement

The "good" wifi dongle on Beast (Realtek 0bda:b812, sold as RTL8822BU / AC1200 Techkey) will not bring its radio up on any tested configuration. The dongle is *needed* permanently because:
- Ethernet is capped at 100 Mbps (PHY downshift, cabling — user's only long-enough cable).
- The working MT7601U "cheap" dongle must eventually return to the uConsole.
- Goal: RTL8822bu working for range, MT7601U as backup, then unplug cheap dongle.

Failure signature (identical across all attempts):
- `txpower -100.00 dBm`, interface stuck DORMANT/DOWN, scan → `Operation not permitted (-1)`
- `RTW: _debug_dlfw_fail: 0x80 = 0x0020`
- `ERROR rtl8822b_hal_init Download Firmware from array failed`
- (rtw88 drivers: `invalid fw checksum` — chip's own DMA rejects firmware bytes)

Tested and failed: kernels 6.12.101, 6.12.94, 6.1.0-50 · drivers: stock rtw88, lwfinger rtw88, morrownr 88x2bu, RinCat 88x2bu · multiple USB ports (direct + hub).

---

## 2. Key research findings (verified, with sources)

### 2.1 The error is a KNOWN, unresolved driver-level issue — not unique to this dongle
- Manjaro forum: Archer T3U Plus (genuine TP-Link RTL88x2bu) shows the identical `_debug_dlfw_fail: 0x80` + "Download Firmware from array failed" log. Thread closed with no fix — advice was to file a bug with RinCat (driver author).
- Implication: **the failure can occur on genuine 8822BU hardware too.** Not conclusive proof the dongle is fake, but the error is a real known failure mode of this driver family.
- Source: https://forum.manjaro.org/t/archer-t3u-plus-tp-link-802-11ac-rtl88x2bu-fail-on-association-took-too-long-to-associate/75859

### 2.2 `0bda:b812` is a GENERIC Realtek default ID shared by 8812BU and 8822BU
- morrownr supported-device-IDs: `0BDA:B812 - Default ID for USB Single-function, WiFi only` (also B81A, B82C for multi-function).
- The 88x2bu driver family covers **both** RTL8812BU and RTL8822BU chipsets — the driver cannot distinguish the die from the USB ID alone.
- Source: https://github.com/morrownr/88x2bu-20210702 (supported-device-IDs file)

### 2.3 The teardown of THIS EXACT unbranded AC1200 shows the silicon is RTL8812BU
- Gough Lui teardown (linked from yduf's page for this device): the unbranded "AC1200 Dual-Band USB 3.0" adapter's PCB is marked **USB3.0-8812BU**, chip = RTL8812BU.
- The yduf resource page (dedicated to 0bda:b812) lists this teardown as the reference for this device.
- Implication: **many unbranded "AC1200/8822BU" dongles actually contain a 8812BU die.** If the driver loads 8822B firmware into 8812B silicon (or vice versa), the chip's own DMA/checksum will reject it — exactly our symptom.
- Sources: https://goughlui.com/2018/03/15/review-teardown-unbranded-ac1200-dual-band-usb-3-0-wi-fi-adapter/ · https://yduf.github.io/wifi-RTL88x2bu/

### 2.4 Same 0bda:b812 device WORKS in Windows and Ubuntu (openSUSE user report)
- openSUSE forum (two threads): the adapter "Works fine in Win10, and Ubuntu 22.10"; on openSUSE it ran under the in-kernel rtw88 driver, degraded only by a driver update (and LED indicator issue). One user's device worked with in-kernel rtw88_8822bu on kernel 6.3.
- Implication: **hardware is almost certainly functional.** The problem is a driver/firmware interaction on Beast's kernel/driver stack, not a dead chip.
- Sources: https://forums.opensuse.org/t/update-for-id-0bda-b812-seems-to-have-partly-broken-the-adaptor/163054 · https://forums.opensuse.org/t/driver-for-0bda-b812/167410

### 2.5 cilynx driver = the untested variable (Pi-proven, different firmware array)
- cilynx/rtl88x2bu: actively maintained (last commit Jun 2026, kernel v7.1 build fixes), 1.8k stars, the driver Raspberry Pi users run for this device; the yduf guide's install steps use it; works on Linux Mint with 0bda:b812 ("Works perfectly").
- Session's final discovery (never tested): cilynx's embedded firmware array differs from RinCat's:
  - RinCat fw: 161,240 bytes, md5 `e155ac2046330049…`, header `228800001e001400`
  - cilynx fw: 160,504 bytes, md5 `88a7bc29d3568092…`, header `228800001e000b00`
- Also: the 88x2bu build lacks `CONFIG_FILE_FWIMG`, so it always uses the embedded array (a `/lib/firmware/rtl8822b/FW_NIC.bin` file was placed on Beast but is ignored by the current build).
- Implication: **building and testing the cilynx driver is the single highest-value next step** — different firmware image than every failed attempt so far.
- Sources: https://github.com/cilynx/rtl88x2bu · https://yduf.github.io/wifi-RTL88x2bu/ · cilynx issue #98 (Pi 64-bit usage)

### 2.6 Dual-dongle transition (pen-tester approach) is confirmed viable
- Two wireless adapters can coexist: one in managed mode (connectivity), one being worked/monitor mode. Manual mode switching (`ip link set down` → `iw dev set type monitor` → up) does NOT kill the other adapter's connection — the standard pen-test dual-card setup.
- NetworkManager + wpa_supplicant hold exclusive locks on wifi interfaces; for monitor-mode work you stop NM interference (`airmon-ng check kill` equivalent), but for a managed-managed transition (both connected) they coexist fine.
- Implication: we can keep the MT7601U connected the entire time while bringing up the RTL8822bu, then drop the cheap dongle only after the good one verifies — no connectivity loss.
- Sources: https://security.stackexchange.com/questions/121215/ · https://yupitek.com/en/blog/enable-monitor-mode-kali-linux/ · https://www.stationx.net/articles/best-wifi-adapters-for-kali-linux

---

## 3. Root-cause assessment (hypotheses, ranked)

| # | Hypothesis | Support | Test |
|---|-----------|---------|------|
| H1 | **Wrong firmware family for the actual die** — dongle is 8812BU silicon reporting generic b812 ID; drivers load 8822B firmware → chip DMA rejects it | Teardown (2.3); generic ID (2.2); error is chip-level (session logs) | Build cilynx driver (different fw array); check `dmesg` chip-version line under 88x2bu debug level 5 (`rtw_drv_log_level=5`) — it prints detected chip type |
| H2 | Firmware version mismatch within 8822B family (chip wants older/newer image) | Manjaro failure on genuine 8822BU (2.1) | Try cilynx array (v older), then file-based FW_NIC.bin with CONFIG_FILE_FWIMG enabled build |
| H3 | Dongle hardware marginal/faulty | All-else-failed (session) | **Contradicted by 2.4** (same ID works on Win/Ubuntu) unless this specific unit is bad — definitive test: plug dongle into a known-good machine |
| H4 | USB power/port issue | Community "try another port" lore | Largely ruled out in session (direct motherboard port tested; still 480 Mbps is normal for this chip) |

**Working conclusion:** H1/H2 (firmware-die mismatch) is the leading theory. The dongle is likely fine; the driver/firmware selection is wrong for the silicon inside.

---

## 4. Recommended next steps (on Beast, in order — NONE done yet)

1. **Inspect chip identity on Beast (read-only):** reload 88x2bu with `rtw_drv_log_level=5`, capture `dmesg` lines showing the detected chip version (looks for "Chip Version Info" / CHIP_8822B vs CHIP_8812B). One command, no changes. *This confirms or kills H1.*
2. **Build & test cilynx driver** (clone already at `/tmp/rtl88x2bu` and `/tmp/cilynx-rtl88x2bu` on Beast): DKMS build for 6.12, blacklist stock rtw88 (already done), load, check interface + scan. *The untested variable from the session.*
3. If cilynx firmware loads: connect to wifi (NetworkManager or wpa_supplicant), verify IP + throughput, then unplug MT7601U.
4. If still failing: enable `CONFIG_FILE_FWIMG` build (or use morrownr driver with `rtw_phy_file_path` option) and supply the correct `FW_NIC.bin` for the detected chip.
5. Only if all software paths fail: test the dongle on another machine to settle H3 definitively.
6. Cleanup (whenever): decide GRUB default (6.1 vs 6.12) — currently 6.1 is default; assistant recommended restoring 6.12 since 6.1 didn't fix the radio. Reinstall Coral TPU gasket DKMS + replug TPU.

---

## 5. Open questions for the user

- Was this dongle ever known to work on ANY machine (Windows/Mac/Linux), or bought secondhand/new-never-tested?
- Is the unit labeled "Techkey" with an external RP-SMA antenna (matching the teardown form factor)?
- OK to run step 1 (read-only chip-identity check) on Beast on our next connection?
- Prefer to try steps on 6.12 (current default is 6.1) — or keep 6.1 for now?

---

## 6. Source list

1. https://forum.manjaro.org/t/archer-t3u-plus-tp-link-802-11ac-rtl88x2bu-fail-on-association-took-too-long-to-associate/75859 — identical dlfw error, unresolved
2. https://github.com/morrownr/88x2bu-20210702 — supported-device-IDs (b812 = generic default ID)
3. https://goughlui.com/2018/03/15/review-teardown-unbranded-ac1200-dual-band-usb-3-0-wi-fi-adapter/ — teardown: PCB = USB3.0-8812BU
4. https://yduf.github.io/wifi-RTL88x2bu/ — device resource page; Pi/cilynx install guide; teardown reference
5. https://forums.opensuse.org/t/update-for-id-0bda-b812-seems-to-have-partly-broken-the-adaptor/163054 — works in Win10/Ubuntu; broken by driver update
6. https://forums.opensuse.org/t/driver-for-0bda-b812/167410 — works with in-kernel rtw88 on 6.3; LED quirk
7. https://github.com/cilynx/rtl88x2bu — actively maintained driver (Jun 2026 commits); Pi instructions
8. https://github.com/cilynx/rtl88x2bu/issues/98 — Pi 64-bit usage of 0bda:b812
9. https://deepwiki.com/RinCat/RTL88x2BU-Linux-Driver/7.3-troubleshooting — driver troubleshooting: debug level 5, USB mode params, HW reset, rtw_power_mgnt
10. https://security.stackexchange.com/questions/121215/ — dual-card (monitor+managed) coexistence
11. https://yupitek.com/en/blog/enable-monitor-mode-kali-linux/ — NM/wpa_supplicant interference notes
12. https://www.stationx.net/articles/best-wifi-adapters-for-kali-linux — airmon-ng workflow (dual-adapter context)
13. https://github.com/RinCat/RTL88x2BU-Linux-Driver — RinCat fork (the one installed on Beast)
