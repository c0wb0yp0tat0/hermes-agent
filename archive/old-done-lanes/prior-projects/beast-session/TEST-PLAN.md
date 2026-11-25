# BeautifulBeast Antenna — FORENSICS + QUOTED TEST + DUAL WORKFLOW PLANS

**Date:** 2026-08-11 · **Prepared on:** pve-1 (research host) · **Target:** Beast 192.168.1.200
**Status:** NO SSH PERFORMED. Everything below is from saved session logs + public sources + driver-source forensics done locally.

---

## PART 1 — FORENSICS: what the session logs + source code actually prove

### 1.1 The "8822B" identity in every log is the USB ID talking, NOT the silicon

Verified in the actual driver source (`os_dep/linux/usb_intf.c`, both RinCat and morrownr trees):

```c
static void rtw_decide_chip_type_by_usb_info(struct dvobj_priv *pdvobjpriv, const struct usb_device_id *pdid)
{
    pdvobjpriv->chip_type = pdid->driver_info;   /* ← straight from the USB ID table */
    ...
    #ifdef CONFIG_RTL8822B
    if (pdvobjpriv->chip_type == RTL8822B)
        rtl8822bu_set_hw_type(pdvobjpriv);
    #endif
}
```

And the table entry:
```c
{USB_DEVICE_AND_INTERFACE_INFO(USB_VENDER_ID_REALTEK, 0xB812, ...), .driver_info = RTL8822B}, /* Default ID for USB Single-function, WiFi only */
```

- `0bda:b812` appears **exactly once** in the entire ID table, hard-coded `RTL8822B`.
- There is **no runtime silicon verification** at bind time in either driver tree.
- **Conclusion: the "8822B" in every dmesg line is the USB descriptor's generic default ID, not a chip-ID read.** Both morrownr and RinCat do this identically.

### 1.2 Both drivers are compiled 8822B-ONLY — no 8812B code path exists in the tree

- Makefiles (RinCat, morrownr, cilynx): `CONFIG_RTL8822B = y`; there is **no `CONFIG_RTL8812B` option at all**.
- `hal/` dirs contain only `rtl8822b/` (the `rtl8812a*` files present are the 8812A/8814A PCIe family, not 8812BU).
- `morrownr/8812bu` repo does not exist (404). The 8812BU-dedicated driver path in the community is the **same 88x2bu family**, which here compiles only the 8822B firmware/init path.
- **Implication:** if the die inside is actually RTL8812BU (as the teardown suggests), *no driver we can build from these trees will take the 8812B path* — they would all load 8822B firmware into 8812B silicon. That exactly matches "chip refuses all firmware."

### 1.3 Firmware identity — all images tested so far were effectively the SAME v30.20.0

Locally extracted and hashed (forensics done on pve-1 from the driver repos):

| Image | Size | md5 | Header | Version |
|---|---|---|---|---|
| linux-firmware `rtw8822b_fw.bin` (canonical, per session) | 161,240 | `e155ac20463300491d893ae2906915d8` | `228800001e001400` | v30.20.0 |
| RinCat embedded array (extracted locally) | 161,240 | `e155ac20463300491d893ae2906915d8` | `228800001e001400` | v30.20.0 |
| **cilynx embedded array (extracted locally)** | **160,504** | **`88a7bc29d35680924d50b5480d74bb5a`** | **`228800001e000b00`** | **v30.11.0** |

- RinCat's embedded array is **byte-identical** to canonical linux-firmware. Debian's stock file was an older v27.2.0. So the chip has been offered v27.2.0 and v30.20.0 — both rejected at the DLFW stage.
- **cilynx's v30.11.0 is the ONLY untested firmware image.** The clone on Beast (`/tmp/rtl88x2bu`, `/tmp/cilynx-rtl88x2bu`) was never built/tested before the session died on HTTP 503.

### 1.4 The chip's boot ROM is ALIVE but rejects the image (register-level evidence)

From the raw session logs (msg 871, untruncated):
```
_debug_dlfw_fail: 0x10F8 = 0x00000000
_debug_dlfw_fail: 0x10FC = 0x800056c7 (0/5) … constant across all 5 polls
_debug_dlfw_fail: 0xC0  = 0xbfc00182 / 0xbfc00180 (alternating)
_debug_dlfw_fail: 0x80  = 0x0020 (after 10 secs)
ERROR rtl8822b_hal_init Download Firmware from array failed
```
- `_debug_dlfw_fail()` is a diagnostics routine in `hal/hal_halmac.c` (source verified) that polls the DLFW (download firmware) handshake registers. A constant value across 5 polls = the boot ROM never progresses the handshake.
- Registers respond (chip is powered and enumerating); the firmware image is simply **never accepted**.
- HALMAC trace in the same log shows `pinmux_set_func_8822b` — the driver is executing the **8822B** init path (because of 1.1), not because the chip said so.

### 1.5 Firmware forensics (local strings/hexdump/byte-diff on pve-1) — NEW

Ran `strings`/`cmp` on the two extracted firmware images (saved at `forensics/fw_rincat.bin`, `forensics/fw_cilynx.bin`):

- **Both images contain embedded `8822b` PHY strings** (7 occurrences each): `config_phydm_parameter_init_8822b`, `config_phydm_trx_mode_8822b`, `config_phydm_switch_bandwidth_8822b`, `config_phydm_switch_agc_tab_8822b`, `config_phydm_switch_channel_8822b`, `config_phydm_switch_band_8822b`, `phydm_rfe_8822b_setting`.
- **Zero `8812b` strings in either image.**
- Header signature check: both begin `22 88` (0x8822 = RTL8822B family).
- Byte-diff: ~152,130 differing bytes out of ~161k — cilynx is a **substantially different build** of the same 8822B-family firmware (v30.11.0 vs v30.20.0), not a trivial version bump.

**Implication (revised):** the cilynx image is NOT a 8812B-family firmware — it is a different minor-version build of the same 8822B platform firmware. So:
- If the die is genuinely 8812BU, **no firmware in any of these driver trees can ever work** — the cilynx test would fail identically (same family, rejected at boot-ROM).
- If the die is 8822B but wants an older/other 8822B image version, cilynx v30.11.0 remains the one untested candidate.
- The driver source trees (RinCat/morrownr/cilynx) contain **zero RTL8812B code paths** — `usb_intf.c` has no RTL8812B reference at all; Makefiles have no `CONFIG_RTL8812B`. A 8812BU die would need a genuinely different driver that does not exist in these repos.

### 1.6 What this means for "fake vs authentic"

**Proven (from logs + source):**
1. The "8822B" label is the USB ID, never verified against silicon.
2. The chip rejects every 8822B-family image offered (v27.2.0, v30.20.0) at the boot-ROM handshake.
3. The rtw88 in-kernel driver (8822B-only) also failed to bring it up (efuse setup fail + fw errors).

**Strongly suggestive (from research):**
4. Teardown of the *identical* unbranded AC1200 form factor shows the PCB marked **USB3.0-8812BU** → the die is plausibly an RTL8812BU sold as 8822BU (this is the well-known "b812 fake" pattern; b812 is a generic Realtek default ID shared by both chip families).
5. Same b812 devices work in Windows/Ubuntu for other users → the hardware *family* works; this unit's die may simply be mislabeled.

**NOT determinable from the session logs alone:**
- The actual die identity. The one command that would have revealed it — reading the chip-version register during a clean probe — was never captured (session only captured the failure dump, not the probe-start chip version print).

---

## PART 2 — THE QUOTED TEST (run on Beast when we reconnect; read-only, no installs)

Goal: capture the ONE missing datum (die identity) + descriptor revision, without changing anything.

```bash
# 1. USB descriptor revision — known-good units show bcdDevice 2.10
lsusb -v -d 0bda:b812 2>&1 | grep -iE "bcdDevice|iProduct|iManufacturer|bNumConfigurations|bNumInterfaces|MaxPower"

# 2. Clean probe with max debug — capture from the START (the session only caught the failure tail)
sudo dmesg -C
sudo modprobe -r 88x2bu 2>/dev/null; sudo modprobe -r rtw88_8822bu 2>/dev/null
sudo modprobe 88x2bu rtw_drv_log_level=5
sleep 15
sudo dmesg | grep -iE "chip|version|efuse|8812|8822|dlfw|boot" | head -60

# 3. Driver procfs register dump (per DeepWiki troubleshooting page)
ls /proc/net/rtl88x2bu/ 2>/dev/null
cat /proc/net/rtl88x2bu/registers/mac_0 2>/dev/null | head -20

# 4. rtw88's own chip-version read (in-kernel driver reads REG_SYS_CFG1=0xF0 at probe)
sudo modprobe -r 88x2bu 2>/dev/null
sudo dmesg -C
sudo modprobe rtw88_8822bu
sleep 10
sudo dmesg | grep -iE "chip|version|sys_cfg|efuse|probe|fail" | head -40
```

**What we're looking for:**
- `Chip Version Info: CHIP_8822B_…` → die identifies as 8822B → **Workflow A**
- `CHIP_8812B…` / `0x8812`-ish / chip-version register mismatch → **Workflow B**
- `bcdDevice 2.10` → matches known-good units (openSUSE/RPi threads); anything else (e.g., 1.00/2.00) → another red flag for re-labeled silicon.

---

## PART 3 — WORKFLOW A: AUTHENTIC 8822B chip (firmware-version path)

Use when the chip-version read says genuine 8822B (or to try regardless — it is the cheapest test).

**A1. Build + test the cilynx driver (v30.11.0 firmware — the only untested image).**
```bash
cd /tmp/cilynx-rtl88x2bu 2>/dev/null || cd /tmp/rtl88x2bu 2>/dev/null || git clone https://github.com/cilynx/rtl88x2bu /tmp/cilynx-rtl88x2bu
VER=$(sed -n 's/.*PACKAGE_VERSION="\(.*\)"/\1/p' dkms.conf)
# RinCat/cilynx need the 6.12 set_monitor_channel guard patch (session already patched RinCat's copy the same way):
sudo sed -i 's/(LINUX_VERSION_CODE >= KERNEL_VERSION(6, 13, 0))/(LINUX_VERSION_CODE >= KERNEL_VERSION(6, 12, 0))/' os_dep/linux/ioctl_cfg80211.c
sudo rsync -a ./ /usr/src/rtl88x2bu-${VER}/
sudo dkms remove -m rtl88x2bu -v ${VER} --all 2>/dev/null
sudo dkms add -m rtl88x2bu -v ${VER}
sudo dkms build -m rtl88x2bu -v ${VER}
sudo dkms install -m rtl88x2bu -v ${VER}
sudo modprobe -r 88x2bu 2>/dev/null; sudo modprobe 88x2bu
ip link show | grep -i wlx
sudo dmesg | grep -iE "firmware|dlfw|checksum" | tail -10
```
- Pass = interface up, no DLFW error, txpower sane → connect (NetworkManager), verify throughput, then unplug MT7601U.
- Fail = same DLFW error → the image isn't the issue → proceed A2.

**A2. Enable file-based firmware and supply the image the chip wants.**
- Build with `CONFIG_FILE_FWIMG` (the driver has the code path; the Makefiles expose it as a config — set it `y` in the Makefile, rebuild via DKMS), place the matching `FW_NIC.bin` at `/lib/firmware/rtl8822b/FW_NIC.bin`, reload.
- Firmware version candidates to try in order: cilynx's v30.11.0 (extracted locally — see Part 1.3; bytes available), then older 8822B images from community `firmware-realtek` builds.
- Pass = radio up → connect → done.
- Fail = chip still rejects → the die is likely NOT 8822B → Workflow B.

---

## PART 4 — WORKFLOW B: KNOWN "FAKE" (8812BU die path)

Use when the chip-version read shows 8812B-family, or when A1+A2 both fail (silicon refuses every 8822B image).

**B1. Accept and confirm the die is RTL8812BU (evidence chain):**
- Teardown of the identical unit (PCB marked USB3.0-8812BU) — already documented.
- Our probe data: 8822B images rejected at boot-ROM; rtw88 (8822B-only) fails; b812 is the shared generic ID.
- (Optional, strongest) read the chip version register via the test in Part 2.

**B2. Get 8812B firmware loaded — the honest constraint:**
- The 88x2bu driver trees compile **only** the 8822B path (Part 1.2). There is no `CONFIG_RTL8812B` in morrownr/RinCat/cilynx Makefiles.
- The correct 8812BU driver in the community is the **realtek 8812BU SDK line** — e.g. `morrownr/8812bu` doesn't exist standalone; the viable routes are:
  1. The **aircrack-ng `rtl8812au`** driver covers 8812AU/8814AU — NOT the BU variant (session already ruled this out).
  2. Search for a maintained **rtl8812bu** DKMS package (Debian/Ubuntu have `rtl8812bu-dkms` in some PPAs/Ubuntu kernels; Kali ships 8812 variants). This is the *community-proven* driver for 8812BU silicon.
  3. If a genuine 8812BU DKMS driver exists, install it, blacklist `rtw88_8822bu` + `88x2bu`, reload, test scan. **Pass = die is 8812B → the dongle "works" but as a 8812BU, not 8822BU — which is fine for the user's goal (range + connectivity).**

**B3. If NO 8812B driver works either:**
- The die is neither cleanly 8822B nor 8812B (dead/marginal silicon, or an exotic clone) → the honest verdict: **replace the dongle**. The MT7601U stays until then; ethernet at 100 Mbps remains the backup. Recommend a known-good adapter (e.g., a chipset with in-kernel rtw88 support or a mainline ath9k/ath10k device).

---

## PART 5 — DECISION MATRIX

| Test result (Part 2) | Path | Expected outcome |
|---|---|---|
| Chip version says 8822B | Workflow A1 (cilynx v30.11.0) | likely works — firmware version was the issue |
| A1 fails, A2 (file fw) fails | Workflow B | die is 8812B or clone |
| Chip version says 8812B / no clean read | Workflow B2 | need 8812BU DKMS driver |
| B2 also fails | B3 | replace dongle |
| bcdDevice ≠ 2.10 | supports B; extra red flag | (see B1) |

**Recommended order of operations on reconnect (all reversible):**
1. Part 2 test (read-only) → captures die identity.
2. A1 cilynx build (30 min) → cheapest real fix.
3. A2 file-firmware build → second attempt.
4. B2 8812BU DKMS search+install → the "fake" path.
5. B3 verdict + recommendation.

**Safety notes:**
- Dual-dongle transition keeps MT7601U connected the whole time — no connectivity loss during any step.
- GRUB default is still 6.1 (wifi kernel). If the dongle works on 6.12 with the right driver, recommend restoring 6.12 as default before finishing.
- Coral TPU: gasket DKMS was removed to unblock the 6.1 install; TPU unplugged. Reinstall is a separate task.
