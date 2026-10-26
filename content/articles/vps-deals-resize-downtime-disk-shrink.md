---
title: "VPS Deals: You Can Downgrade the CPU and the RAM. You Can Never Shrink the Disk — and the Lock Costs $72 to $768 a Year"
slug: vps-deals-resize-downtime-disk-shrink
date: 2026-10-26
description: "Read off the vendors' own pages on 2026-10-26. Both DigitalOcean and Hetzner let you downgrade vCPU and RAM after you have upgraded, and neither will ever shrink a disk: DigitalOcean — \"You cannot decrease the size of a Droplet's disk\"; Hetzner — \"we do not offer disk downgrades.\" The real cost is not the disk, it is the price floor you can never get back under. DigitalOcean's own published plan table (38 plans) shows the cheapest plan you are allowed to occupy doubles at every disk rung: 25 GB locks you to $6/mo, 50 GB to $12, 80 GB to $24, 160 GB to $48, 320 GB to $96, 640 GB to $192 — 48x its $4 entry price. Hetzner's CPX ladder reaches only 20.11x its own entry price at the same 640 GB floor, making the ratchet 2.39x more punishing at DigitalOcean. Also published nowhere else: DigitalOcean is the only one of the two that prints a downtime formula (\"about one minute of downtime per GB of used disk space\") and it runs even when you only change RAM; Hetzner's Cloud servers FAQ contains no occurrence of the word \"downtime\" at all. Both vendors hide the same escape hatch — \"keep the storage size fixed (for the ability to downscale later)\" at DigitalOcean, \"When scaling up, you can choose to keep your current disk size\" at Hetzner — and it only works if you choose it before you scale."
question: When a VPS deal says you can upgrade or downgrade anytime, does that include the disk — does a resize need downtime, can I go back down, and what does the irreversible part actually cost me?
sources:
  - https://docs.digitalocean.com/products/droplets/how-to/resize/
  - https://docs.digitalocean.com/products/droplets/concepts/choosing-a-plan/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.digitalocean.com/products/volumes/details/pricing/
  - https://docs.hetzner.com/cloud/servers/faq/
  - https://docs.hetzner.com/cloud/servers/deprecated-plans/
  - https://www.hetzner.com/cloud/regular-performance/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the vendors' own pages on 2026-10-26: the upgrade is reversible on compute and irreversible on disk, at both hosts.** DigitalOcean states it flatly — *"You cannot decrease the size of a Droplet's disk."* Hetzner states it just as flatly — *"Rescaling to a plan with a smaller disk is not possible, regardless of how much storage you are actually using… For this reason, we do not offer disk downgrades."*

The consequence is not the disk. It is the **price floor**. Because DigitalOcean also writes *"You can resize to any Droplet plan that has an equal or greater amount of disk space as the original Droplet,"* every gigabyte you let the boot disk grow permanently removes every cheaper plan from your reachable set. Working from DigitalOcean's own pricing page on 2026-10-26 (38 plans, machine-readable in the page source), the cheapest plan you are allowed to occupy rises from $4.00/mo at a 10 GB floor to **$192.00/mo at a 640 GB floor — 48 times the entry price.** Hetzner's CPX ladder reaches only **20.11x** its own entry price at that same 640 GB floor. **The disk ratchet is 2.39x more punishing at DigitalOcean than at Hetzner.**

The good news, and it is the single most valuable thing in this article: **both hosts give you a switch that stops the ratchet, and neither puts it anywhere near the pricing page.** DigitalOcean's control panel offers *"Choose whether to keep the storage size fixed (for the ability to downscale later)"*; Hetzner's FAQ says *"When scaling up, you can choose to keep your current disk size. This allows you to later downgrade to a server plan with the same disk size."* It only works if you set it **before** you scale.

## The answer, in six questions

Every cell is verbatim policy from the pages linked at the bottom, or arithmetic on numbers printed on those same pages. Read 2026-10-26.

| Question | DigitalOcean | Hetzner |
|---|---|---|
| Can I downgrade vCPU / RAM after upgrading? | **Yes** — *"**CPU and RAM only**. This option increases or decreases the amount of CPU and RAM available to a Droplet"* | **Yes** — *"you can also rescale to and from a plan with shared resources or up- and downgrade to another plan"* |
| Can I ever shrink the disk? | **No** — *"You cannot decrease the size of a Droplet's disk"* | **No** — *"we do not offer disk downgrades"* |
| Does a resize need downtime? | **Yes, and there is a published formula** — *"Allow for about one minute of downtime per GB of used disk space"* | **Not stated.** The Hetzner Cloud servers FAQ (ID CL-BD8DE, last changed 2024-09-12) contains **zero** occurrences of the word "downtime" and publishes no estimate |
| Does the partition grow automatically? | **No** — the resize page documents a disk at *"50.0 GiB"* still holding a *"24.9 GiB"* partition | **No** — *"If you rescale your cloud server, you will have to manually resize the partition via Rescue System"* |
| Can I change plan family while resizing? | **No** — *"You cannot resize between v5 configurations and bundled plans"*; *"You cannot resize GPU Droplets"* | **No** — *"when you rescale your server, you can only change to a server plan with the same architecture type"* |
| Is there a way to stop the disk ratchet? | **Yes** — *"Choose whether to keep the storage size fixed (for the ability to downscale later)"* | **Yes** — *"When scaling up, you can choose to keep your current disk size"* |

Two things jump out of that table. First, the *"upgrade or downgrade anytime"* promise is true for compute and false for storage, and nobody says so on the pricing page. Second, **the two hosts are asymmetric about the one number buyers actually want**: DigitalOcean publishes a downtime formula and Hetzner publishes nothing.

## What the lock actually costs: the price-floor ladder

This is the arithmetic nobody publishes, so here it is with the inputs. On 2026-10-26 we pulled every CPU Droplet plan with its boot-disk size and monthly price straight out of DigitalOcean's pricing page (38 plans across Regular, Premium Intel and Premium AMD). For each disk size we then asked a single question: *once my disk has grown to at least this big, what is the cheapest plan I am still allowed to occupy?*

| Disk floor (you can never go below) | Cheapest plan you may occupy | Multiple of the $4 entry price | Added cost of crossing this rung | Per year |
|---|---|---|---|---|
| 10 GB | $4.00/mo (`s-1vcpu-512mb-10gb`) | 1.0x | — | — |
| 25 GB | $6.00/mo (`s-1vcpu-1gb`) | 1.5x | +$2.00/mo | $24 |
| 50 GB | $12.00/mo (`s-1vcpu-2gb`) | 3.0x | +$6.00/mo | $72 |
| 80 GB | $24.00/mo (`s-2vcpu-4gb`) | 6.0x | +$12.00/mo | $144 |
| 160 GB | $48.00/mo (`s-4vcpu-8gb`) | 12.0x | +$24.00/mo | $288 |
| 320 GB | $96.00/mo (`s-8vcpu-16gb`) | 24.0x | +$48.00/mo | $576 |
| 640 GB | $192.00/mo (`s-8vcpu-32gb-640gb-intel`) | 48.0x | +$96.00/mo | $1,152 |

Read the third column again: from 25 GB upward the floor **doubles at every single rung**. Let your boot disk cross 50 GB once — for a one-off import, a database dump, a bad `docker pull` spree — and the cheapest server you can ever own again costs $12/mo instead of $6/mo. That is **$72 a year, every year, for disk you may no longer be using.** Cross 160 GB and it is $24/mo, or **$288 a year**, permanently.

Here is the same calculation for Hetzner's CPX line, taken from the plan table printed on its Regular Performance page on 2026-10-26 (EU-Central, excl. VAT):

| Disk floor | Cheapest CPX plan | EUR/mo | Multiple of the EUR6.49 entry |
|---|---|---|---|
| 20 GB | CPX02 | EUR6.49 | 1.00x |
| 40 GB | CPX12 | EUR11.99 | 1.85x |
| 80 GB | CPX22 | EUR19.99 | 3.08x |
| 160 GB | CPX32 | EUR35.99 | 5.55x |
| 320 GB | CPX42 | EUR69.99 | 10.78x |
| 480 GB | CPX52 | EUR100.99 | 15.56x |
| 640 GB | CPX62 | EUR130.49 | 20.11x |

Comparing the two directly is meaningless at face value — one is dollars, one is euros — so compare each host against **its own entry price**, which cancels the currency. At a 640 GB disk floor DigitalOcean charges **48.0x** its entry price; Hetzner charges **20.11x** its own. **The ratchet is 2.39x more punishing at DigitalOcean.**

The reason is visible in the marginal price of one more gigabyte of boot disk:

| Step | DigitalOcean marginal | Hetzner marginal |
|---|---|---|
| First step up | $0.2400/GB (25→50 GB: +$6.00 for +25 GB) | EUR0.2750/GB (20→40 GB: +EUR5.50 for +20 GB) |
| Mid ladder | **$0.3000/GB** (60→80, 80→160, 160→320 GB all identical) | EUR0.2000/GB (40→80 and 80→160 GB) |
| Top of ladder | $0.3000/GB | EUR0.1844/GB (480→640 GB) |

Two useful readings. DigitalOcean's boot disk settles at a flat **$0.30/GB** marginal; its separately billed block-storage volume costs **$0.10 per GiB per month** = $0.0931/GB (*"DigitalOcean Volumes Block Storage cost $0.10 per GiB per month"*). **Buying disk by resizing the boot disk costs 3.22x what the same gigabyte costs as a volume — and the volume is the one you can detach, snapshot and resize.** Hetzner, meanwhile, gets *cheaper* per gigabyte as you climb (EUR0.2750 down to EUR0.1844/GB), which is exactly why its floor multiple rises more slowly.

### A trap inside the ladder

Because the floor is defined by *disk* and not by vCPU or RAM, the cheapest survivable plan at a given floor is sometimes a different CPU family than the one you started on. At a 60 GB floor, the cheapest DigitalOcean plan is **not** the Regular `s-2vcpu-2gb` at $18.00/mo — it is `s-1vcpu-2gb-70gb-intel`, a **Premium Intel** plan with 1 vCPU and 2 GB RAM at **$16.00/mo**. And the steps are not smooth: moving from a 90 GB floor to a 100 GB floor — 10 GB — jumps the minimum from $24.00/mo to $32.00/mo, **$96 a year for ten gigabytes.**

## The downtime clock: one host prints a formula, the other prints nothing

DigitalOcean's resize page is unusually candid: *"Allow for about one minute of downtime per GB of used disk space, though the actual time necessary is typically shorter."*

That is a formula, so here is what it produces at common disk sizes. It measures **used** space, not disk size — check it yourself with `df / -h`, which is the command DigitalOcean tells you to run.

| Used disk space | Estimated downtime | In hours |
|---|---|---|
| 12 GB (25 GB disk, 50% full) | ~12 min | 0.2 h |
| 40 GB (80 GB disk, 50% full) | ~40 min | 0.7 h |
| 160 GB (320 GB disk, 50% full) | ~160 min | 2.7 h |
| 256 GB (320 GB disk, 80% full) | ~256 min | 4.3 h |
| 512 GB (640 GB disk, 80% full) | ~512 min | 8.5 h |

Now the part that catches people out, quoted verbatim: *"Estimated downtime depends on disk usage even for resizes that don't change the amount of disk space. This is because the Droplet may move to a new hypervisor, which transfers disk data over the network."*

**Doubling the RAM on a 320 GB Droplet that is 80% full is estimated at roughly 4.3 hours of downtime, even though the disk never changes.** The clock is not set by what you asked to change. It is set by how much data happens to be on the disk.

Hetzner publishes no equivalent. We searched the full text of its Cloud servers FAQ — the page that answers *"Is it possible to downgrade the disk?"* and *"Why has the disk partition remained the same after rescaling?"* — and the string "downtime" does not appear once. That is not a criticism of the platform; it is a gap in what you can plan against. **If you need a maintenance window in writing, only one of these two hosts gives you the inputs to compute one.** (That FAQ carries ID CL-BD8DE and its own header says *"Last change on 2024-09-12"* — 774 days before this article was written.)

## The escape hatch, and why you have to set it first

Both vendors ship the same protection, and both describe it in a single sentence buried away from the pricing page.

- **DigitalOcean**, in the control-panel walkthrough: *"Choose whether to keep the storage size fixed (for the ability to downscale later), select a compute plan, and choose the new Droplet size."* The screenshot caption on that page literally names a *"downscale option."*
- **Hetzner**, in the disk-downgrade FAQ: *"When scaling up, you can choose to keep your current disk size. This allows you to later downgrade to a server plan with the same disk size."*

This is the whole game. If you scale from 25 GB to a bigger plan **and keep the disk at 25 GB**, you stay eligible for every plan at or above 25 GB, and your $6.00/mo floor survives. If you scale and let the disk ride along to 50 GB, your floor becomes $12.00/mo forever.

Note the wording difference, because it is easy to miss: Hetzner frames it as a **disk-size** choice (*"keep your current disk size"*), while DigitalOcean frames it as a **downscale capability** (*"for the ability to downscale later"*). Same mechanism, but only DigitalOcean's phrasing tells you what the switch is *for*.

One more wrinkle on DigitalOcean's side: its resize page also says the *"Disk, CPU, and RAM"* option *"permanently increases the size of a Droplet's disk."* Both sentences are on the same page. The reconciliation is that growing the disk is permanent once you do it — the toggle is what stops you from doing it.

## After the resize, the partition does not grow

Neither host hands you the new space. You paid for it; you have to go get it.

DigitalOcean documents the failure mode with its own console output. After a 25 GB → 50 GB resize, `gdisk -l /dev/vda` reports *"Disk /dev/vda: 104857600 sectors, 50.0 GiB"* while the partition table still shows *"1 227328 52428766 24.9 GiB 8300"* — **a 50 GiB disk holding a 24.9 GiB partition.** The fix is `growpart /dev/vda 1` followed by `resize2fs /dev/vda1` for ext3/ext4 or `xfs_growfs /dev/vda1` for XFS. DigitalOcean's own caution: *"In certain cases, a disk resize fails to resize the Droplet's partition or filesystem. If you rerun `df -h` after a disk resize and the output is unchanged, this usually indicates a problem."*

Hetzner has a dedicated FAQ entry for exactly this — *"Why has the disk partition remained the same after rescaling?"* — and the answer is *"You have to manually resize the partition via Rescue System after the Rescale has been completed."*

So there are three separate things to verify after any resize, at both hosts: the plan changed, the disk grew, and **the filesystem actually grew with it.** The third one is on you, and at Hetzner it needs a boot into Rescue.

## Side effects that are not on the pricing page

- **Your CPU vendor can change.** Hetzner: *"The hardware is automatically allocated based on availability — both during the creation of new servers, and during a rescale to a different plan. As a result, the CPU type (Intel® or AMD) may change during a rescale."* On DigitalOcean the vendor is part of the slug you pick (`s-2vcpu-4gb` vs `s-2vcpu-4gb-intel` vs `s-2vcpu-4gb-amd`), so it changes only if you choose it.
- **The availability data is up to 15 minutes stale, and does not refresh.** Hetzner: *"The availability of a server plan is checked and updated about every 15 minutes,"* and *"the availability status of server plans is loaded only once when you initially access the page."* It also describes a two-step order path where the second step *"can happen that due to limited availability no free resources can be found — despite a positive best-effort availability check in the first step."* In plain terms: a rescale can fail after you click it.
- **Architecture is frozen.** Hetzner: *"when you rescale your server, you can only change to a server plan with the same architecture type as your current server plan."* DigitalOcean has the equivalent wall one level up — *"You cannot resize between v5 configurations and bundled plans"* — plus *"You cannot resize GPU Droplets."*
- **The machine stays off.** DigitalOcean requires a power-off first (*"Before you can resize a Droplet in the control panel, you need to power it off"*), the API *"automatically powers down the Droplet first,"* and afterwards *"Once the resize is complete, power the Droplet back on"* — it does not come back by itself.
- **Take a snapshot first, and delete it after.** DigitalOcean: *"We strongly recommend taking a snapshot of the Droplet before resizing… If you use snapshots, you can delete the snapshot after confirming that the resize was successful."* Snapshots bill until you delete them.

## What the three big sites actually show you

We read the first screen of all three benchmark sites on 2026-10-26. None of them answers this question, and the shape of the gap is instructive.

LowEndBox's front page is a **geo-and-feature directory plus a deal feed**: location menus, then dated promo cards where the specs live inside the teaser prose (*"25GB of disk"*) rather than in fields. Resizing, upgrading and downgrading do not appear; more CPU is framed as *choosing a different provider*, not changing the one you have. Namecheap's home page is built around a single decision — register or transfer a domain — with VPS present only as a navigation link; there is no spec table above the fold and no mention of scaling, resizing or downtime.

Liquid Web is the interesting one, because it sells the opposite impression. Its VPS packages page carries a panel headed *"Easy VPS upgrades"*: *"Upgrade your VPS package with one click. Server resources, backups, and security scale together—no rebuilding or reconfig required."* Note what is absent — **no mention of downgrading, no downtime figure, and no disk-size caveat.** It also starts you far higher up the ladder than either of the others: the three packages printed on 2026-10-26 are 240 GB, 440 GB and 640 GB of storage. **Liquid Web's smallest VPS disk is 24x DigitalOcean's smallest and 12x Hetzner's** — so if you are comparing a VPS deal there against a $4 droplet, you are comparing a 240 GB floor against a 10 GB one.

Its renewal arithmetic is worth reading before you take the one-click upgrade, because the cliff gets steeper the further you climb:

| Liquid Web package | vCPU / RAM / disk | Intro price | Renews at | Jump at renewal |
|---|---|---|---|---|
| 8 GB | 4 / 8 GB / 240 GB | $150.30/mo | $2,004/yr = $167.00/mo | **+11.1%** |
| 16 GB | 6 / 16 GB / 440 GB | $175.50/mo | $2,676/yr = $223.00/mo | **+27.1%** |
| 32 GB | 8 / 32 GB / 640 GB | $256.50/mo | $5,280/yr = $440.00/mo | **+71.5%** |

Upgrading is one click. The upgrade also moves you onto a steeper renewal step, and nothing on the page describes how to come back down.

## Verdict: what to do before you click resize

1. **Decide the disk question before you touch compute.** If you are scaling for CPU or RAM, find the *keep the current disk size* switch first — *"Choose whether to keep the storage size fixed (for the ability to downscale later)"* on DigitalOcean, *"you can choose to keep your current disk size"* on Hetzner. This single choice is worth $72 to $1,152 a year at DigitalOcean.
2. **If you need space temporarily, do not resize — attach a volume.** At DigitalOcean it is $0.10 per GiB per month versus $0.30/GB to grow the boot disk (3.22x cheaper), and the volume detaches. Growing the boot disk is permanent at both hosts.
3. **Schedule the window from used bytes, not from the plan.** DigitalOcean: about one minute per GB **used**. A 320 GB disk that is 80% full is ~4.3 hours even for a RAM-only change. At Hetzner no figure is published, so plan from your own `df` output and assume the worst.
4. **Budget two manual steps after the resize:** power the machine back on (DigitalOcean does not do it for you), then grow the partition — `growpart` + `resize2fs`/`xfs_growfs` on DigitalOcean, Rescue System on Hetzner. Run `df -h` and confirm it actually changed.
5. **Snapshot before, delete after.** Both are manual, and snapshots bill until deleted.
6. **Check the family wall before you plan the move.** v5↔bundled and GPU are dead ends at DigitalOcean; architecture type is frozen at Hetzner. If a resize is refused, that is usually why.

If you remember one sentence: **compute is elastic in both directions, storage is elastic in one, and the bill follows the disk forever.**

## What we could not verify

- **Hetzner's current shared (CX) plan ladder.** Its documentation itemises disk sizes only for the *deprecated* list (*"Deprecated shared (CX) and dedicated (CCX) server plans"*, last changed 2023-08-29): CX22 40 GB, CX32 80 GB, CX42 160 GB, CX52 320 GB — an exact doubling per step. The current CPX figures in this article come from the plan table on Hetzner's Regular Performance product page, which is a product page, not a docs page. We did not use the deprecated ladder in any calculation.
- **Hetzner's downtime during a rescale.** Not published anywhere we could reach. The statement above is that the number is *absent*, not that the downtime is zero.
- **Whether DigitalOcean's "keep the storage size fixed" toggle is exposed in the API or CLI.** The resize page documents it only in the control-panel walkthrough; the API and CLI sections describe powering down and specifying a size slug, with no storage-fixed flag mentioned.
- **Liquid Web's downgrade policy and downtime.** The packages page describes upgrading only. Its legal and policy paths returned access errors to our automated checks on 2026-10-26, so we did not attempt to work around them and we publish no figure we could not read.
- **Namecheap's resize policy.** Its VPS page returned an access error to our automated checks on 2026-10-26; no figure from it is used here.

## Method and sources

All figures were read from the pages below on **2026-10-26**. The DigitalOcean plan table (38 plans with boot-disk size, vCPU, RAM, transfer quota, hourly and monthly price) was parsed out of the pricing page source; the floor ladder, marginal $/GB and multiples in this article are arithmetic on those published numbers and nothing else. Every quotation is verbatim from the linked page.

- DigitalOcean, *How to Resize Droplets for Vertical Scaling* (page states `last_updated: "2026-08-25"`) — https://docs.digitalocean.com/products/droplets/how-to/resize/
- DigitalOcean, *Choosing the Right CPU Droplet Plan* — https://docs.digitalocean.com/products/droplets/concepts/choosing-a-plan/
- DigitalOcean, Droplet pricing (source of the 38-plan table) — https://www.digitalocean.com/pricing/droplets
- DigitalOcean, *Volumes Block Storage Pricing* — https://docs.digitalocean.com/products/volumes/details/pricing/
- Hetzner, *Cloud Servers FAQ* (ID CL-BD8DE, *"Last change on 2024-09-12 • Created on 2020-07-02"*) — https://docs.hetzner.com/cloud/servers/faq/
- Hetzner, *Deprecated server plans* (ID CL-740FD) — https://docs.hetzner.com/cloud/servers/deprecated-plans/
- Hetzner, Regular Performance cloud server plans — https://www.hetzner.com/cloud/regular-performance/
- Liquid Web, VPS Packages & Bundles — https://www.liquidweb.com/vps-hosting/packages/
