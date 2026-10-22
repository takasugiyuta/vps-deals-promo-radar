---
title: "VPS Deals: What One Extra GB of Storage Really Costs — and Why Your Backup Ignores the Disk You Attached"
slug: vps-deals-block-storage-price-per-gb
date: 2026-10-22
description: "Read off four hosts' own pages on 2026-10-22. An extra gigabyte is not one number: DigitalOcean charges $0.10 per GiB per month for a network volume, Namecheap sells extra disk at $3.00/mo per 10 GB ($0.30/GB) and extra offsite backup at $10.00/mo per 10 GB ($1.00/GB), Hetzner publishes no per-GB rate at all, and Liquid Web sells no add-on storage at any price. The bigger finding is the one nobody prints: Hetzner states in writing that \"we do not provide Backups or Snapshots for Volumes. Backups and Snapshots for servers do not include any Volumes which are attached to your server,\" and DigitalOcean's limits page says \"Volumes are not included in Droplet backups.\" So the price of one extra copy of your data is 1.60x the storage bill on DigitalOcean, 2.00x on Hetzner (the only copy available is a second volume plus dd/rsync) and 4.33x on Namecheap. Plus arithmetic you cannot get from a deal page: matching a $0.03/GiB daily backup plan with manual volume snapshots costs $1.80/GiB/month — 60x more for the same 30 restore points."
question: When a VPS deal says "add storage," what does the extra gigabyte actually cost per month — and does the backup I'm paying for cover the disk I attached?
sources:
  - https://docs.digitalocean.com/products/volumes/details/pricing/
  - https://docs.digitalocean.com/products/volumes/details/limits/
  - https://docs.digitalocean.com/products/snapshots/details/pricing/
  - https://docs.digitalocean.com/products/snapshots/how-to/snapshot-volumes/
  - https://docs.digitalocean.com/products/volumes/how-to/delete-detach/
  - https://docs.digitalocean.com/products/backups/details/pricing/
  - https://docs.hetzner.com/cloud/volumes/overview/
  - https://docs.hetzner.com/cloud/volumes/faq/
  - https://www.hetzner.com/cloud/block-storage
  - https://www.namecheap.com/hosting/vps/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off four hosts' own pages on 2026-10-22: an extra gigabyte of VPS storage costs $0.093/GB on DigitalOcean, $0.30/GB on Namecheap, nothing at any price on Liquid Web, and an unpublished number on Hetzner. And on two of the three hosts that sell you a separate disk, the backup you are already paying for does not cover it.** Hetzner writes it in one sentence on its Volumes page: *"we do not provide Backups or Snapshots for Volumes. Backups and Snapshots for servers do not include any Volumes which are attached to your server."* DigitalOcean writes the same thing more quietly, as a bullet on its volume limits page: *"Volumes are not included in Droplet backups. To protect volume data, create volume snapshots."*

Here is the whole answer in one screen. "Price per GB" is what one more gigabyte of storage costs per month. "Cost of one copy" is the total bill for storing a gigabyte *and* keeping one restorable copy of it — expressed as a multiple of the storage bill alone.

| Host | Extra storage sold as | Price per GB / month | Automated backup covers it? | Cost of one copy (multiple of storage bill) | Can you shrink it? |
|---|---|---|---|---|---|
| **DigitalOcean** | Network-attached volume, 1 GiB–16,384 GiB | **$0.10 per GiB** ($0.093/GB) | **No.** Manual volume snapshots only, **$0.06 per GiB/mo** | **1.60x** | Not verified today |
| **Hetzner** | Cloud Volume, 10 GB–10 TB | **Not published** (see below) | **No — none exists.** No backups, no snapshots, for volumes | **2.00x** (second volume + `dd`/`rsync`) | **No** — "only be enlarged, not reduced" |
| **Namecheap** | Extra disk space add-on, 10 GB blocks | **$0.30/GB** ($3.00/mo per 10 GB) | Extra offsite backup sold separately, **$1.00/GB** | **4.33x** | Not stated |
| **Liquid Web** | Nothing — storage is fixed per tier | **Not sold** | Acronis Cyber Backup, fixed **100 / 250 / 500 GB** per tier | Included, but capped | Not sold |

## What a gigabyte actually costs

DigitalOcean's volume pricing page is the only one of the four that prints a clean unit price: *"DigitalOcean Volumes Block Storage cost $0.10 per GiB per month and range from 1 GiB to 16384 GiB (16 TiB). Charges accrue hourly for as long as the volume exists."* Note the unit. DigitalOcean bills **GiB** (1,073,741,824 bytes), Namecheap sells **GB** (1,000,000,000 bytes), so the honest cross-host comparison is $0.093/GB versus $0.30/GB — **Namecheap's add-on disk is 3.2x DigitalOcean's volume rate** for the same physical bytes.

Namecheap's own spec table lists the add-on as *"Extra disk space … $3.00/mo for 10 GB"* on every one of its five VPS plans, and the sister line *"Extra backup storage (Complete managed VPS) … $10.00/mo for 10 GB."* Those two lines are the most useful numbers on the page, because they let you price protection directly: on Namecheap, **one gigabyte of backup costs 3.33x one gigabyte of disk** ($1.00 vs $0.30).

Liquid Web's packages page sells no add-on storage at all. Storage is welded to the tier — 240 GB on the 8 GB plan, 440 GB on 16 GB, 640 GB on 32 GB — and the page contains no per-GB rate and no mention of snapshots. Fill the disk and the only lever is moving up a tier.

Hetzner is the awkward one. Its Volumes documentation has a heading literally called **"Pricing,"** and the section under it contains no price: *"Volumes have a monthly price cap and are billed hourly. They can have a storage capacity of 10 GB to 10 TB and you can select the desired size in 1 GB increments. For more information about the prices, see hetzner.com/cloud/block-storage."* We read that product page on 2026-10-22 and it also prints no per-GB figure — only server plan prices from €5.99/month. Hetzner's Cloud API pricing endpoint requires an authenticated token, which we did not use. **Hetzner's per-GB volume rate is therefore not verifiable here, and we are not going to guess it.** What we can verify is that Hetzner does publish a monthly price *cap* and hourly billing, which is a different promise from per-GB.

## The part nobody prints: your backup stops at the system disk

This is the finding worth more than the price table.

- **Hetzner** (`docs.hetzner.com/cloud/volumes/overview/`, ID CL-ADF96): *"Please note that we do not provide Backups or Snapshots for Volumes. Backups and Snapshots for servers do not include any Volumes which are attached to your server."* You can enable the Backups feature on the server, watch it run weekly, and every byte on the attached volume is invisible to it.
- **DigitalOcean** (`products/volumes/details/limits/`, last verified 5 Aug 2026): *"Volumes are not included in Droplet backups. To protect volume data, create volume snapshots."* DigitalOcean at least sells you the fix.

So the real question when you read a VPS deal is not "how much is the disk" — it is **"what does one restorable copy of this disk cost me?"** That number is derivable, and it differs by a factor of nearly three between hosts:

| Host | Store 1 GB | One restorable copy of 1 GB | Total | As a multiple of storage |
|---|---|---|---|---|
| DigitalOcean | $0.093 | $0.06/GiB snapshot = $0.056 | $0.149 | **1.60x** |
| Hetzner | not published | no product exists — second volume + `dd`/`rsync` = 1.00x storage | — | **2.00x** |
| Namecheap | $0.30 | $1.00 | $1.30 | **4.33x** |

Hetzner's 2.00x is not a guess at a price — it falls out of its own FAQ. Asked *"Can I clone / duplicate Volumes?"* Hetzner answers: *"This is not currently possible using Hetzner Console. As a workaround, you could create a second Volume of the same size and mount it on the server where the source Volume is mounted. Depending on your requirements, you could use tools such as `dd` or `rsync` to copy your data to the destination Volume."* A second volume of the same size is a second full storage bill. **On Hetzner, your only backup of a 1 TB volume is a second 1 TB volume: you pay for 2 TB to hold 1 TB.**

## DigitalOcean's own arithmetic: the snapshot tax

DigitalOcean prices the two halfs of the same problem in different currencies, and the mismatch is large.

- Volume: **$0.10 per GiB per month.**
- Volume snapshot: **$0.06 per GiB per month**, with *"a minimum charge of $0.01."*
- Droplet backups on usage-based plans: **$0.03/GiB/mo daily**, $0.02 every 12 hours, $0.015 every 6 hours, **$0.01 every 4 hours.** On Basic plans it is a flat **20% (weekly) or 30% (daily) of the Droplet's cost.**

Put those side by side and a volume is the worst-backed-up thing you can own on the platform. A Droplet's own disk gets a **daily** restorable copy for $0.03/GiB/month. A volume gets **no** automated schedule, so the equivalent is one manual snapshot per day — each of which persists and bills at $0.06/GiB/month until you delete it:

- Keeping **7** daily snapshots: 7 x $0.06 = **$0.42/GiB/month = 14x** the $0.03 daily backup rate.
- Keeping **30** daily snapshots: 30 x $0.06 = **$1.80/GiB/month = 60x** the daily backup rate.
- Trying to match a **4-hourly** plan (180 snapshots/month): 180 x $0.06 = **$10.80/GiB/month = 1,080x** the $0.01/GiB rate.

**The formula: `snapshot cost per GiB/month = number of snapshots you keep × $0.06`.** There is no schedule, no rotation and no expiry. A snapshot you take once and forget is a subscription you bought by accident.

Two more operator-grade details from the same page. Volume snapshots are *"crash-consistent"* but explicitly **not** filesystem-consistent — *"the snapshot process does not coordinate with the operating system or running applications to flush in-memory caches."* DigitalOcean's advice is to power off the Droplet, or run `sync`, or stop the database first. And because snapshots work at block level, *"the snapshot size may not match what the filesystem reports"* — deleted files still occupy billable blocks until you trim them, which is why DigitalOcean recommends `fstrim` or the `discard` mount option **to make your snapshots smaller and therefore less expensive.**

## Detaching is not deleting

DigitalOcean's detach/delete page closes the last loophole: *"After detaching a volume, you can access it from the Volumes page. You continue to be billed for the volume until you delete it."* Detaching keeps the data and stops nothing. Only *"Delete a volume, which permanently removes the volume and all of its data"* stops the meter. Combined with the pricing page's *"You are charged for volumes whether or not they are attached to a Droplet,"* an orphaned volume is the cleanest way to pay 100% of a storage bill for 0% of its use — and unlike a snapshot, nothing about it looks forgotten in the console.

## The cheapest extra gigabyte is usually a plan upgrade, not an add-on

Namecheap's numbers make this concrete. Its add-on disk is $0.30/GB/month regardless of billing cycle. But moving one tier up — from Spark (1 CPU / 1 GB RAM / 20 GB) to Pulsar (2 CPU / 2 GB RAM / 40 GB) — costs:

- **Monthly column:** $11.88 − $5.88 = $6.00/month for +20 GB = **$0.30/GB** — identical to the add-on, *plus* a CPU and a gigabyte of RAM.
- **Yearly column:** $106.56 − $58.56 = $48.00/year = $4.00/month for +20 GB = **$0.20/GB** — 33% cheaper than the add-on, again with CPU and RAM included.

**The rule this produces: on Namecheap, buying extra disk as an add-on is never cheaper than upgrading, and if you can commit to a year it is strictly worse.** The same test is worth running on any deal page that shows an add-on rate next to a tier ladder.

Liquid Web has no ladder to run it on, but its tiers reveal a different cap. Backup is a fixed allowance, not a rate: 100 GB on the 8 GB plan, 250 GB on 16 GB, 500 GB on 32 GB. Set against each tier's own disk, **the cheapest plan can only back up 41.7% of the disk it ships with** (100 of 240 GB), the middle one 56.8% (250 of 440 GB), the top one 78.1% (500 of 640 GB). Namecheap's included offsite allowance — 100/200/400 GB on Quasar/Magnetar/Hypernova with Complete management — is a much healthier 83.3% / 83.3% / 80.0%, but it is gated behind the $25.00/month Complete management add-on, and the same page notes management add-ons are *"available only with the Quasar, Magnetar and Hypernova"* plans.

## Ceilings, if you are pushing the product

| | DigitalOcean (limits page, verified 5 Aug 2026) | Hetzner (Volumes docs) |
|---|---|---|
| Size range | 1 GiB – 16,384 GiB | 10 GB – 10 TB, 1 GB steps |
| Volumes per machine | **15** per Droplet, 15 per DOKS node | **16** per cloud server |
| Simultaneous attachment | one Droplet at a time | *"Up to 1 server at a time"* |
| Account ceiling | **5,000** volumes per account | docs say *"In total up to 10 TB"* under Limits |
| Throughput / IOPS | Shared 7,500 IOPS / 300 MB/s; dedicated burst 15,000 IOPS / 525 MB/s | sustained 5,000 / burst 7,500 IOPS, 200 / 300 MB/s |

Two things fall out. First, DigitalOcean's ceilings are generous: 15 volumes x 16,384 GiB = **245,760 GiB (240 TiB) on a single Droplet**, which at $0.10/GiB is **$24,576/month** of block storage hanging off one machine. Second, the performance comparison lands on an exact coincidence worth knowing: **Hetzner's burst ceiling (7,500 IOPS and 300 MB/s) is identical to DigitalOcean's shared-CPU sustained floor (7,500 IOPS and 300 MB/s).** DigitalOcean's dedicated-CPU burst tier is exactly 2x those IOPS and 1.75x that throughput.

We have to flag one inconsistency rather than paper over it: Hetzner's Limits section lists *"Up to 16 Volumes per server"* **and** *"In total up to 10 TB"* on the same page, while its FAQ says a single volume may be *"between 10 GB and 10 TB."* Read literally, 16 volumes cannot each be 10 TB within a 10 TB total. The docs point to the Console Limits page for *"the additional current limits,"* so treat the project total as console-defined and do not plan capacity from the docs sentence alone. Hetzner also notes a practical gotcha: *"Servers which have run for quite some time may need a power off and power on cycle"* before a volume will attach — *"A soft reboot is not enough."*

## What we could not verify

Stated plainly, because these gaps are part of the answer:

- **Hetzner's per-GB price.** Not published on the docs page, not on the product page it links to, and the pricing API needs a token. Not verifiable; not estimated.
- **Whether a DigitalOcean volume can be shrunk.** The resize how-to path returned 404 today. Hetzner is explicit that volumes *"can only be enlarged, not reduced in size"*; we are not going to assume DigitalOcean matches.
- **Namecheap and Liquid Web direct access.** Both product pages returned **403** to a direct scripted request on 2026-10-22, as they have throughout this series; the figures quoted here were read from the pages themselves and are attributed to the product pages, not to a terms document. Neither host publishes a per-GB block-storage rate comparable to DigitalOcean's — Namecheap sells 10 GB blocks, Liquid Web sells nothing.
- **Whether volumes survive server deletion.** Neither host's page we could read states it. Treat "delete the server" as unrelated to "delete the volume" until you see it in writing — on DigitalOcean, at least, deletion and billing are separate buttons and only the second one stops the money.

## What to do with this

1. **Price the copy, not the disk.** Before you attach anything, ask what one restorable copy costs. On DigitalOcean multiply the volume price by **1.60**; on Hetzner by **2.00**; on Namecheap by **4.33**.
2. **If you are on DigitalOcean and need daily protection on a volume, budget `snapshots kept × $0.06 × GiB`.** Seven snapshots costs 14x a Droplet daily backup; thirty costs 60x. If you need more than a handful of restore points, the volume is the wrong place for that data.
3. **Run `fstrim` before snapshotting.** Snapshots bill on block-level size, not on what `df` reports.
4. **Detach is not delete.** Audit for volumes with no Droplet attached — they bill at full price.
5. **Check backup headroom against disk, not against the marketing line.** Liquid Web's entry tier covers 41.7% of its own disk; Namecheap's covers ~80–83% but only with a $25/month management add-on on the top three plans.
6. **Compare the add-on rate to the tier ladder before you buy an add-on.** On Namecheap the add-on is never cheaper and, on a yearly term, 33% worse.

Every number above is quoted from the host's own page on 2026-10-22 or is arithmetic you can redo from those numbers. Where a host does not publish a figure, it says so — that silence is data too, and on a VPS deal page it usually means the add-on is priced to be bought without being compared.
