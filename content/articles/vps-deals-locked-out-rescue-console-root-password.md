---
title: "VPS Deals: Locked Out of Your Own VPS — Hetzner's Rescue Dies in 60 Minutes, DigitalOcean's Never Expires, and Three OSes Can't Be Reset at All"
slug: vps-deals-locked-out-rescue-console-root-password
date: 2026-10-28
description: "Read off the vendors' own pages on 2026-10-28. Every host here can get you back into a locked-out VPS, but not on the same clock, through the same door, or with the same password. Hetzner's cloud rescue self-destructs: \"Rescue remains activated for 60 minutes\" and \"If you restart your server after those 60 minutes, the server will boot from its local disk again\" — a reboot you trigger too late silently puts you back on the broken disk. DigitalOcean's recovery ISO has no time limit at all and Namecheap's Rescue Mode has to be switched off by hand (\"Make sure to disable Rescue Mode in SolusVM afterwards\"). The password itself arrives three different ways: DigitalOcean emails it (\"You will receive an email containing the Droplet's temporary password\"), Hetzner prints it on screen (\"The new password will appear directly in the Hetzner Console\"), Namecheap prints it in the panel after \"a few minutes\". And DigitalOcean's own docs refuse the reset outright on some systems: \"Root password resets are not available for operating systems with internally-managed passwords, including AlmaLinux, Fedora, and Rocky Linux\" — the same page where Fedora is listed as a supported Droplet Console OS, and where the lost-SSH-key page draws the line at a minor version (\"Ubuntu, Debian, CentOS, or Fedora 27\" works, \"FreeBSD, Fedora 28, Fedora Atomic, and RancherOS\" cannot be reset externally at all). Also published nowhere else: DigitalOcean's browser console depends on an agent installed by default only on Droplets created after August 2021 — 1,884 days before this article — so the console cannot help on older machines precisely when you are locked out and cannot install it."
question: When a VPS deal leaves you locked out — lost password, lost SSH key, broken sshd, or a kernel that won't boot — what rescue path actually exists, how long does it stay open, and where does the new password arrive?
sources:
  - https://docs.digitalocean.com/support/how-do-i-reset-my-droplets-root-password/
  - https://docs.digitalocean.com/support/i-lost-the-ssh-key-for-my-droplet/
  - https://docs.digitalocean.com/support/i-did-not-get-an-email-of-my-droplets-root-password/
  - https://docs.digitalocean.com/products/droplets/how-to/connect-with-console/
  - https://docs.digitalocean.com/products/droplets/how-to/recovery/recovery-console/
  - https://docs.digitalocean.com/products/droplets/how-to/recovery/recovery-iso/
  - https://docs.digitalocean.com/products/snapshots/details/pricing/
  - https://docs.hetzner.com/cloud/servers/getting-started/rescue-system/
  - https://docs.hetzner.com/cloud/servers/getting-started/vnc-console/
  - https://docs.hetzner.com/cloud/servers/how-to-rescue/reset-password/
  - https://docs.hetzner.com/robot/dedicated-server/maintenance/kvm-console/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9974/48/how-to-manage-your-vps-with-solusvm-for-kvm/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9975/48/how-to-set-up-a-vnc-client-with-a-vps-hosting/
  - https://www.hostinger.com/vps-hosting
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the vendors' own pages on 2026-10-28: every host in this comparison can get you back into a machine you have locked yourself out of — but they do not hand you the same door, the same clock, or the same password, and DigitalOcean's own documentation refuses to reset three of them at all.** The differences are not marketing; they are written in the docs, and they decide whether a 2 a.m. lockout costs you ten minutes or a rebuild.

The three facts that matter most, all quoted below from the vendors:

1. **The rescue window is not universal.** Hetzner's cloud rescue expires on its own: *"Rescue remains activated for 60 minutes… If you restart your server after those 60 minutes, the server will boot from its local disk again."* DigitalOcean's recovery ISO has no published expiry and Namecheap's Rescue Mode has to be switched off by hand.
2. **The password arrives by three different channels.** DigitalOcean emails it, Hetzner prints it on screen, Namecheap prints it in the panel after a wait. If your mail is the thing that is broken, the email channel is the one path that stalls.
3. **Some operating systems cannot be reset from outside.** DigitalOcean: *"Root password resets are not available for operating systems with internally-managed passwords, including AlmaLinux, Fedora, and Rocky Linux."* Its own lost-SSH-key page is even sharper — *"On FreeBSD, Fedora 28, Fedora Atomic, and RancherOS… it's currently not possible to reset the root password externally."*

## The answer, in five situations

Every cell is verbatim policy from the pages listed at the bottom, read on 2026-10-28.

| What went wrong | DigitalOcean | Hetzner Cloud | Namecheap (SolusVM) |
|---|---|---|---|
| **Forgot the root password** | Control panel → **Reset root password** → *"You will receive an email containing the Droplet's temporary password."* Refused on AlmaLinux / Fedora / Rocky Linux | Server → **RESCUE** → **ROOT PASSWORD** → **RESET ROOT PASSWORD** → *"The new password will appear directly in the Hetzner Console"* | SolusVM → **Root/Admin Password** → **Change** → *"Wait for a few minutes… you will receive a 'Success' message with the new password"* |
| **sshd is dead, or your own firewall locked you out** | **Recovery Console** (VNC): *"provides out-of-band access and is available regardless of your network settings… even if a Droplet has lost network access or the `sshd` process has failed"* | **VNC console** in the browser: *"use your root user and the root password that you received via email"* | SolusVM **VNC** — HTML5 client in a browser tab, or an external client on `IP:port` with its own VNC password |
| **Kernel won't boot / filesystem corrupt / disk 100% full** | Boot the **recovery ISO** (Ubuntu 24.04 based), then the Recovery Console gives a 7-option menu including *"Check Filesystem"* and *"Reset Droplet Root Password"* | **Rescue** (network boot, runs in memory): SSH in as root, then `mount` / `chroot-prepare` / `chroot` / `passwd` / `reboot` | **Rescue Mode**: pick a kernel, *"you'll receive your temporary SSH connection details"* |
| **Lost the SSH private key** | Reset the password, then *"Enable password authentication by editing the SSH config and restarting the SSH service."* On Ubuntu 22.04+ and Debian 12+ the flag must be set in **two** files | Rescue + chroot, or follow the dedicated *"Changing the SSH key"* rescue article | VNC or Rescue Mode |
| **Nothing left to try** | DigitalOcean's own written fallback: *"we instead recommend creating a snapshot of that Droplet and redeploying to a new Droplet to which you have access"* — snapshots bill at **$0.06 per GB per month** (minimum charge $0.01) | Not stated in the rescue documentation we could read | **Reinstall** — *"will erase all the existing data on your VPS"*, *"allow the installation up to 10 minutes to complete"* |

## Nobody's rescue runs on the same clock

This is the part no comparison article prints, because it is only visible if you read the activation page instead of the feature list.

| Host | Rescue mechanism | Time limit | Auto-expires? | How it ends |
|---|---|---|---|---|
| **Hetzner Cloud** | Network boot (PXE) into a live system | **60 minutes** to trigger the reboot | **Yes** — after 60 min, a restart boots the local disk and *"Rescue will automatically be deactivated again"* | *"The only way to end Rescue is to restart the server once again."* Ending your SSH session with `CTRL`+`D` does **not** end it |
| **Hetzner dedicated** | KVM-over-IP (Lantronix Spider or Raritan Dominion) | **Free for 3 hours**, paid beyond that | Not stated | Ordered through a Robot support form; *"Since the number of KVM Consoles in each DC is limited, we recommend that you order the KVM Console in advance"* |
| **DigitalOcean** | Boot from recovery ISO | **None published** | No | You go back into **Settings → Recovery mode** and choose **Boot from Hard Drive** |
| **Namecheap** | SolusVM Rescue Mode | **None published** | No | *"Make sure to disable Rescue Mode in SolusVM afterwards."* |

The Hetzner 60 minutes is the sharpest trap in this whole article, because it is a deadline on the **reboot**, not on the session. The page gives two activation paths: *"Enable rescue"*, where *"The server does not automatically restart and you will have to do it manually"*, and *"Enable rescue & power cycle"*, where the restart happens for you. If you pick the first one and then spend an hour reading a Stack Overflow thread before hitting reboot, Hetzner's own sentence applies: *"If you restart your server **after** those 60 minutes, the server will boot from its local disk again."* You get no error, no warning — you get your broken machine back, and the rescue is gone.

The Namecheap failure is the exact mirror image. There is no auto-off, so the documented last step is a manual one you have to remember: *"Make sure to disable Rescue Mode in SolusVM afterwards."* Forget it and the machine keeps coming up in the temporary environment.

## Where the new password actually appears

Three vendors, three channels. This decides what you do when the mail server is the thing that is broken.

| Path | Channel | What the vendor says | Failure mode |
|---|---|---|---|
| DigitalOcean, panel reset | **Email** | *"You will receive an email containing the Droplet's temporary password"* | Mail delayed or unreachable → you are stuck. Note also *"After creation, we do not send this password to the registered email address"* — the only email DigitalOcean sends is the reset one |
| DigitalOcean, recovery ISO | **On screen** | The Recovery Console prints *"Root Password has randomly been set to: exam-ple0-1234-5678"* | Needs console access first |
| Hetzner, panel reset | **On screen** | *"The new password will appear directly in the Hetzner Console"* | Needs Console login (not server login) |
| Hetzner, rescue activation | **On screen** | *"you will be given a root password directly on your Hetzner Console"* | — |
| Hetzner, initial login | **Email** | *"use your root user and the root password that you received via email"* | — |
| Namecheap, panel reset | **On screen, after a wait** | *"Wait for a few minutes for the password to be reset. Once it is done, you will receive a 'Success' message with the new password"* | Unquantified wait |

Only DigitalOcean forces a change afterwards: *"When you log in to the Droplet with your new password via SSH, the operating system prompts you to change the password. It first asks for the current password (the new root password emailed to you), then asks you to enter the new password twice."*

## DigitalOcean's dead end: a four-step chain, and a one-version cliff

Put DigitalOcean's own pages side by side and a specific failure chain appears. It is worth walking, because each step is documented separately and none of them warns about the next.

1. **You are locked out and reach for the browser console.** The Droplet Console is *"available at no extra cost"*, but it needs an agent on the guest: *"The Droplet agent is installed by default on all new Droplets created after August 2021, and you can install the agent manually on older Droplets."* That was **1,884 days** before this article was written. On an older Droplet, the agent is not there — and installing it needs the root access you just lost. It also *"is not available for Private Droplets because they have no public IP address"*, and it needs *"outbound TCP access to `169.254.169.254`"* or *"the Droplet Console cannot authenticate your session"* — a host firewall that blocks the metadata service breaks the console too.
2. **So you fall back to the Recovery Console.** It works without any agent: *"available even if a Droplet has lost network access or the `sshd` process has failed"*. But it *"requires password authentication on the Droplet"* — and if you built the Droplet with an SSH key only, there is no password to use.
3. **So you ask the panel to reset the password.** Here the OS list bites: *"Root password resets are not available for operating systems with internally-managed passwords, including AlmaLinux, Fedora, and Rocky Linux."* The panel answers with *"This Droplet's root password is managed internally and cannot be changed from the control panel."*
4. **Which leaves the documented fallback:** *"we instead recommend creating a snapshot of that Droplet and redeploying to a new Droplet to which you have access."* At **$0.06 per GB per month**, an 80 GB disk costs **$4.80/month** to park while you rebuild — and the old Droplet bills until you destroy it.

Two details in that chain are published nowhere else:

- **Fedora appears in two DigitalOcean lists with opposite meanings.** The Droplet Console page lists supported systems as *"Ubuntu, Debian, CentOS, and Fedora"* — Fedora is supported. The reset page lists *"AlmaLinux, Fedora, and Rocky Linux"* as un-resettable — Fedora is refused. Same distribution, both statements current on the same day.
- **The cliff is one minor version wide.** The lost-SSH-key page says the recovery walkthrough works on *"any version of Ubuntu, Debian, CentOS, or **Fedora 27**"*, and that on *"FreeBSD, **Fedora 28**, Fedora Atomic, and RancherOS"* it *"is currently not possible to reset the root password externally."*

This is not an abstract edge case. Liquid Web's VPS package page, read the same day, lists **"AlmaLinux 9"** as the operating system on every card — the exact family DigitalOcean says it cannot reset from the panel.

## What you actually get once you are in

The two rescue environments are not the same shape, and the difference changes what you can fix.

**DigitalOcean's recovery ISO is a menu.** Boot it and the Recovery Console shows a numbered prompt with **seven** options: `1. Mount your Disk Image`, `2. Check Filesystem`, `3. Reset Droplet Root Password`, `4. Configure Keyboard`, `5. Attempt to 'chroot' into installed system`, `6. Interactive Shell [/bin/bash]`, `7. Clear out Cloud-Init cached data (will regenerate host ssh keys)`. It announces itself as *"This rescue environment is based on Ubuntu 24.04"*, warns *"SSH Host keys do NOT match while using this rescue system"*, and *"Network access and SSH have been enabled automatically"*. Its `fsck` option carries its own warning: *"`fsck` can occasionally cause data corruption on active disks, so only attempt this on an unmounted file system… We recommend taking a snapshot of your Droplet first."*

**Hetzner's rescue is a shell.** You pick *"linux64"* as the rescue OS, optionally attach an SSH key, get a root password on the Console, and SSH in. Everything else is manual: `mount /dev/sda1 /mnt`, `chroot-prepare /mnt`, `chroot /mnt`, `passwd`, `reboot`. Hetzner also documents the side effect DigitalOcean only hints at — the host key changes: *"With the rescue system, however, this fingerprint is **not valid**"*, with instructions to comment out or delete the old `known_hosts` line.

One asymmetry worth knowing before you need either: Hetzner's rescue page offers exactly one rescue OS, **`linux64`**, and Hetzner's whole documentation index contains zero occurrences of `arm64` or `ARM`. Whether its Arm64 cloud servers can boot the rescue system is **not stated** — we are not going to guess it for you.

## How stale is the advice you are following

Read the same day, the vendors' own change dates differ by more than four years. If a rescue step fails, check this before you assume you did it wrong.

| Page | Vendor's own last-change date | Days before 2026-10-28 |
|---|---|---|
| Hetzner, *Using the console* (VNC) | 2022-06-28 | **1,583** |
| Hetzner, *Using Rescue* (cloud) | 2022-08-26 | **1,524** |
| Hetzner, *KVM Console* (dedicated) | 2025-10-01 | 392 |
| Hetzner, *Resetting the password* | 2026-06-02 | 148 |
| DigitalOcean, *Connect with Droplet Console* | 2026-06-30 | 120 |
| DigitalOcean, *Recovery ISO* | 2026-07-13 | 107 |
| DigitalOcean, *Reset root password* | 2026-09-02 | 56 |
| DigitalOcean, *Recovery Console* | 2026-09-03 | 55 |
| DigitalOcean, *Snapshots pricing* | 2026-10-26 | 2 |

## What we could not verify

- **Liquid Web's rescue, console and root-password policy.** Its packages page was readable on 2026-10-28 and lists *"AlmaLinux 9"*, *"Managed"*, *"Dedicated IP address"* and Acronis Backup tiers of 100 / 250 / 500 GB, with *"Daily backups are configured for you and scale automatically with your package."* The page contains **no mention of console access, rescue mode, or root access** anywhere on it, and its legal and policy paths returned access errors to our automated checks. We did not work around that and we publish no figure we could not read.
- **Hostinger's rescue path.** Its VPS page was readable on 2026-10-28 and advertises a *"VPS Web Console"* and an *"AI web terminal"* plus *"Full root access"*, but after stripping scripts the page contains **zero occurrences of "rescue", "VNC" or "root password"**. Whether a lockout path exists, and what it costs in time, is not verifiable from the vendor today.
- **Whether Hetzner's Arm64 cloud servers can boot its rescue system.** Not stated in any Hetzner page we could reach; the docs index has no `arm64` entry at all.
- **Session timeouts.** Neither DigitalOcean's Recovery Console nor Namecheap's VNC publishes a session limit. The absence of a published number is not a promise that there isn't one.

## What to do before you need any of this

1. **Set a root password once, on purpose, even if you log in with a key.** DigitalOcean's Recovery Console *"requires password authentication on the Droplet"*; Hetzner's VNC console logs in with the root password. A key-only machine has one fewer door.
2. **Check whether your OS is on the un-resettable list before you standardise on it.** AlmaLinux, Fedora and Rocky Linux cannot be reset from DigitalOcean's panel; FreeBSD, Fedora 28, Fedora Atomic and RancherOS cannot be reset externally at all.
3. **Verify the console works today, not on the night you need it.** At DigitalOcean that means the Droplet agent (default only after August 2021), outbound TCP to `169.254.169.254`, and SSH allowed on the `sshd` port. At Hetzner and Namecheap it means knowing where the VNC button is.
4. **If you enable Hetzner's rescue, reboot inside the hour.** Past 60 minutes the restart silently boots your local disk and deactivates rescue.
5. **If you enable Namecheap's Rescue Mode, turn it off when you are done.** Nothing else will.
6. **Snapshot before `fsck`, and know what parking one costs.** DigitalOcean says so itself, and the parking fee is $0.06 per GB per month.
7. **Assume the host key will change.** Both vendors say so. Keep a note to clean your `known_hosts` afterwards.

If you remember one sentence: **the lockout tool is not the same as the lockout clock, and the operating system you picked decides whether the tool works at all.**

## Method and sources

All quotations and figures were read from the pages below on **2026-10-28**, with no proxy, no user-agent spoofing and no attempt to bypass any access control. Day counts are arithmetic on the dates those pages print about themselves. Where a page was unreachable or silent, this article says so instead of filling the gap.

- DigitalOcean, *How do I reset my Droplet's root password?* (page states `last_updated: "2026-09-02"`) — https://docs.digitalocean.com/support/how-do-i-reset-my-droplets-root-password/
- DigitalOcean, *I lost the SSH key for my Droplet* (`last_updated: "2026-07-13"`) — https://docs.digitalocean.com/support/i-lost-the-ssh-key-for-my-droplet/
- DigitalOcean, *I did not get an email of my Droplet's root password* (`last_updated: "2026-07-13"`) — https://docs.digitalocean.com/support/i-did-not-get-an-email-of-my-droplets-root-password/
- DigitalOcean, *How to Connect to Droplets with the Droplet Console* (`last_updated: "2026-06-30"`) — https://docs.digitalocean.com/products/droplets/how-to/connect-with-console/
- DigitalOcean, *How to Recover Access to Droplets using the Recovery Console* (`last_updated: "2026-09-03"`) — https://docs.digitalocean.com/products/droplets/how-to/recovery/recovery-console/
- DigitalOcean, *How to Recover Data from Droplets with the Recovery ISO* (`last_updated: "2026-07-13"`) — https://docs.digitalocean.com/products/droplets/how-to/recovery/recovery-iso/
- DigitalOcean, *Snapshots Pricing* (`last_updated: "2026-10-26"`) — https://docs.digitalocean.com/products/snapshots/details/pricing/
- Hetzner, *Using Rescue* (ID CL-B9851, *"Last change on 2022-08-26"*) — https://docs.hetzner.com/cloud/servers/getting-started/rescue-system/
- Hetzner, *Using the console* (ID CL-A10B1, *"Last change on 2022-06-28"*) — https://docs.hetzner.com/cloud/servers/getting-started/vnc-console/
- Hetzner, *Resetting the password* (ID CL-98866, *"Last change on 2026-06-02"*) — https://docs.hetzner.com/cloud/servers/how-to-rescue/reset-password/
- Hetzner, *KVM Console* (ID RO-50C7E, *"Last change on 2025-10-01"*) — https://docs.hetzner.com/robot/dedicated-server/maintenance/kvm-console/
- Namecheap, *How to manage your VPS with SolusVM (for KVM)* (KB 9974) — https://www.namecheap.com/support/knowledgebase/article.aspx/9974/48/how-to-manage-your-vps-with-solusvm-for-kvm/
- Namecheap, *How to set up a VNC client with a VPS Hosting* (KB 9975) — https://www.namecheap.com/support/knowledgebase/article.aspx/9975/48/how-to-set-up-a-vnc-client-with-a-vps-hosting/
- Hostinger, VPS Hosting (readable 2026-10-28; no rescue or root-password-reset detail published) — https://www.hostinger.com/vps-hosting
- Liquid Web, VPS Packages & Bundles (readable 2026-10-28; no console or rescue detail published) — https://www.liquidweb.com/vps-hosting/packages/
