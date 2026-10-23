---
title: "VPS Deals: Can You Restore a Snapshot in Another Region? Two Hosts Answer Opposite in Writing"
slug: vps-deals-snapshot-cross-region
date: 2026-10-23
description: "Read off the hosts' own pages on 2026-10-23. Hetzner writes \"Are Backups/Snapshots location bound? No, they are not location bound. You can use a Backup/Snapshot to create a new server in any location.\" DigitalOcean writes the opposite: \"By default, a Droplet snapshot is only available in the region where it was created,\" and for volumes, \"You cannot transfer volume snapshots to other regions.\" That is a 36-of-36 restore matrix against a 1-region default. The part nobody prints is the price: DigitalOcean charges $0.06 per GB per month and states \"There is no additional charge for making a snapshot available in multiple regions\" — so the cost per region-copy falls to $0.020 at three regions and $0.010 at six. Also derived here and not published anywhere: because DigitalOcean volume snapshots are \"not incremental\" and capped at 25 per volume, the snapshot bill for any volume, of any size, tops out at exactly 15.0x that volume's own storage bill. Plus the fire-zone exception buried in Hetzner's own table — 3 of its 6 locations store your snapshot in the same location as the server, and 2 of 6 keep automatic backups in the same data center."
question: When a VPS deal includes snapshots or automatic backups, can I restore that copy into a different datacenter region — or is it welded to the region where it was made?
sources:
  - https://docs.digitalocean.com/products/snapshots/how-to/change-regions/
  - https://docs.digitalocean.com/products/snapshots/details/pricing/
  - https://docs.digitalocean.com/products/snapshots/details/limits/
  - https://docs.digitalocean.com/products/backups/details/pricing/
  - https://docs.digitalocean.com/products/backups/how-to/convert-to-snapshot/
  - https://docs.digitalocean.com/support/how-long-will-my-backup-or-snapshot-take-to-complete/
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/faq/
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/
  - https://docs.hetzner.com/cloud/general/locations/
  - https://www.hostinger.com/vps-hosting
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the hosts' own pages on 2026-10-23: whether your snapshot can leave its region depends entirely on which host made it, and the two hosts that publish an answer say opposite things.** Hetzner's FAQ answers the question in one word — *"Are Backups/Snapshots location bound? **No, they are not location bound.** You can use a Backup/Snapshot to create a new server in any location."* DigitalOcean's documentation answers the same question the other way: *"By default, a Droplet snapshot is only available in the region where it was created."* And on the one kind of copy that matters most for data you keep outside the system disk, DigitalOcean is absolute: *"You cannot transfer volume snapshots to other regions."*

This is a different question from "can I move the server" — every host answers *that* one with no, and the answer is published. This page is about the **image**: once you hold a copy of your disk, how far does it travel? That is the path you actually use for a rebuild in a new region, for a second site, and for getting back up after a region-level failure.

Here is the whole answer in one table. Every cell is either a verbatim policy or arithmetic from it.

| Question | DigitalOcean — Droplet snapshot | DigitalOcean — volume snapshot | Hetzner — Backup (automatic) | Hetzner — Snapshot (manual) |
|---|---|---|---|---|
| Restorable in another region out of the box? | **No** — you must add it | **No — never** | **Yes** | **Yes** |
| Can you make it portable? | Yes: **Add to region** (panel, API, `doctl`) | **No.** SnapShooter / rsync / SFTP only | Already portable | Already portable |
| Extra charge per extra region | **$0** ("no additional charge") | n/a | **Not stated** | **Not stated** |
| Who picks where the copy physically sits | **You** (you name each region) | Fixed to source region | **Hetzner** — random, cannot be changed | **Hetzner** — random, cannot be changed |
| Survives deleting the server? | Yes | Yes (while the volume exists) | **No** — "automatically be deleted if you delete the server" | **Yes** |
| Restore-point cap | No account cap published; **25 per volume** | **25 per volume** | **7 slots per server** | **30 across all projects** |
| Blocked by CPU architecture? | Not stated | Not stated | **Yes** — x86 cannot restore onto Arm64 | **Yes** — same rule |
| Published rate | **$0.06/GB/mo** (Droplet), **$0.06/GiB/mo** (volume) | $0.06/GiB/mo | Not published on the docs page | Not published on the docs page |

## The collision, in the hosts' own words

**DigitalOcean** (`products/snapshots/how-to/change-regions/`, last verified 13 Jul 2026):

> *"By default, a Droplet snapshot is only available in the region where it was created. If you want to use a snapshot to create Droplets in other regions, you need to add the snapshot to those regions first. **It doesn't cost more to add a snapshot to more regions.**"*

> *"**You cannot transfer volume snapshots to other regions.** As an alternative, you can use tools like SnapShooter, rsync or SFTP to transfer the data to a new volume created in the target region."*

**Hetzner** (`cloud/servers/backups-snapshots/faq/`, ID CL-B2495):

> *"Are Backups/Snapshots location bound? **No, they are not location bound.** You can use a Backup/Snapshot to create a new server in any location. Therefore, the new server does not have to match the original location of the server the Backup/Snapshot was created from."*

Hetzner then prints the whole matrix, and it is the most useful artefact on either site — six source locations, and every one of them can create a server in all six locations. That is **36 of 36 combinations enabled**, with no button, no transfer step, and no per-region fee mentioned. DigitalOcean's equivalent is **one region by default**, plus one manual "Add to region" action per extra region, and **zero** for volumes.

The distinction that decides real outcomes is this: **on Hetzner the portable thing is the copy you already have.** Automatic daily Backups — the ones you did not have to remember to take — are cross-location restorable as-is. On DigitalOcean the automatic thing is the locked one; the portable thing is a Snapshot you made on purpose.

## The number nobody prints: multi-region costs nothing extra

DigitalOcean's snapshot pricing page (last verified 8 May 2024) states three things in three short lines:

> *"Snapshots are charged at $0.06 per GB per month for Droplets and $0.06 per GiB per month for volumes."*
> *"There is a minimum charge of $0.01..."*
> *"There is no additional charge for making a snapshot available in multiple regions."*

Read together with *"Snapshots are not incremental. Each snapshot is a full disk image"* (snapshots limits page), that last line is remarkable: DigitalOcean will hold a **complete, independent copy of your disk in every region you name**, and bill you for **one** copy.

So the honest price of a region-copy is a falling curve, not a rate. The formula is `0.06 ÷ regions`:

| Regions the snapshot is available in | Monthly bill for a 100 GB snapshot | Effective cost per region-copy, per GB | Per region-copy for the whole 100 GB |
|---|---|---|---|
| 1 (the default) | $6.00 | $0.0600 | $6.00 |
| 2 | $6.00 | $0.0300 | $3.00 |
| 3 | $6.00 | $0.0200 | $2.00 |
| 6 | $6.00 | $0.0100 | $1.00 |
| 10 | $6.00 | $0.0060 | $0.60 |

At six regions, a full restorable copy of your 100 GB server in six datacenters costs **$6.00 a month** — *$1.00 per region*. There is no per-region image fee, no egress line, and no transfer charge anywhere in that document. If your disaster plan is "be able to rebuild in another region," this is the cheapest artefact on the page, and no deal listing mentions it.

The catch is time, not money. Adding a region is not instant — DigitalOcean's own walkthrough says *"A spinner displays as the snapshot image is added, **which may take several minutes**."*

## The 15x ceiling on volume snapshots

Here is a derived number that is not printed on any page and follows from three published facts:

1. *"You can store up to **25** snapshots of a given volume."*
2. *"Snapshots are not incremental. Each snapshot is a full disk image."*
3. Volume storage costs **$0.10 per GiB per month**; volume snapshots cost **$0.06 per GiB per month**.

Twenty-five full copies at $0.06 is **$1.50 per GiB** of snapshotting, against **$0.10 per GiB** of storage. The ratio is `25 × 0.06 ÷ 0.10 = 15.0`, and **the volume's own size cancels out** — so the ceiling is 15.0x for a 10 GiB volume and 15.0x for a 16 TiB one:

| Volume size | Storage bill | 25 snapshots (the cap) | Total | Snapshots as a multiple of storage |
|---|---|---|---|---|
| 10 GiB | $1.00 | $15.00 | $16.00 | **15.0x** |
| 100 GiB | $10.00 | $150.00 | $160.00 | **15.0x** |
| 500 GiB | $50.00 | $750.00 | $800.00 | **15.0x** |
| 1,000 GiB | $100.00 | $1,500.00 | $1,600.00 | **15.0x** |

Two more constraints bite before you ever reach that ceiling. The limits page caps creation at *"up to one snapshot every **10 minutes**"* per volume, so twenty-five slots take at least **24 intervals × 10 minutes = 4 hours** to fill. And a volume snapshot can *"not be moved between regions or transferred to different DigitalOcean accounts"* — so those 25 copies are 25 copies in one region, in one account, with no export path except the rsync/SFTP workaround DigitalOcean itself points you to.

For comparison on the Droplet side, DigitalOcean's automatic backups are priced as a **percentage of the Droplet**, not per GiB: *"Weekly 20.0% of the Droplet's cost per month"* and *"Daily 30.0% of the Droplet's cost per month"* on Basic plans, or on usage-based plans *"Weekly $0.04 per GiB per month"* down to *"Every 4 Hours $0.01 per GiB per month."* On a $4/mo Droplet, weekly backups are **$0.80/mo** — against **$15.00/mo** for 25 snapshots of a 10 GiB volume. **The unit price of protection differs by roughly 19x depending on which of the two knobs you turn.**

## The unit glitch: GB for Droplets, GiB for volumes

DigitalOcean's own pricing sentence switches units mid-sentence: *"$0.06 per **GB** per month for Droplets and $0.06 per **GiB** per month for volumes."* One GiB is 1,073,741,824 bytes; one GB is 1,000,000,000. So the volume rate, expressed in the same bytes, is `$0.06 ÷ 1.073741824 = $0.05588/GB` — **6.87% cheaper per byte** than the Droplet rate printed next to it.

On 1,000 GiB of real data (1,073.74 GB), the volume rate bills **$60.00/mo**; the Droplet rate applied to those same bytes would bill **$64.42/mo**. A **$4.42/mo** difference, or **$53.08 a year**, purely from which unit the line item uses.

## Where the copy physically sits — and the fire-zone exception

This is the part that only shows up if you scroll past the headline answer. Hetzner says snapshots are not location bound, but it does **not** say you get to choose where they are stored:

> *"Backups are in the same location as the cloud server they were created from, but usually in a different data center. This way, it is guaranteed that the Backups are in a different fire zone than the server. **In Hillsboro and in Singapore only one data center is in use**, which is why those locations are a little bit different. There, Backups are always saved in the same data center as the server."*

> *"Snapshots are automatically in a different location than the cloud server they were created from. **The location itself is allocated randomly and cannot be changed.** The location has to be in the same network zone, which is why Ashburn, Hillsboro and Singapore are a little bit different."*

Hetzner's own mapping table makes the consequences explicit:

| Server is in | Snapshot is stored in | Same location as the server? |
|---|---|---|
| Falkenstein (`fsn1`) | Helsinki **or** Nuremberg | No |
| Nuremberg (`nbg1`) | Helsinki **or** Falkenstein | No |
| Helsinki (`hel1`) | Nuremberg **or** Falkenstein | No |
| Ashburn (`ash`) | Ashburn | **Yes** |
| Hillsboro (`hil`) | Hillsboro | **Yes** |
| Singapore (`sin`) | Singapore | **Yes** |

Count it: **3 of Hetzner's 6 locations store your snapshot in the same location as the source server.** Those three are exactly the sites where Hetzner does not own the data center park — its locations page states *"We do not have our own data center parks in the USA or in Singapore. There, we use colocation space at other data centers."* For automatic Backups the exposure is narrower but different: **2 of 6** (Hillsboro and Singapore) keep backups in the *same data center*, not merely the same location.

So "not location bound" does not mean "geographically redundant." It means *the restore is portable*. On a Falkenstein server your snapshot is in Helsinki or Nuremberg — a genuine second site. On an Ashburn, Hillsboro or Singapore server, it is in the building you are already in.

There is a second asymmetry hiding here. Hetzner's locations page defines **four network zones for six locations**: `eu-central` (Falkenstein, Nuremberg, Helsinki), `us-east` (Ashburn), `us-west` (Hillsboro), `ap-southeast` (Singapore). Snapshot *storage* must stay inside the source network zone. But the FAQ says you may restore into *any* location — including across zones. A Falkenstein snapshot restored to Ashburn therefore crosses a zone boundary. Hetzner's locations page says plainly that *"Traffic between two different network zones (such as Hetzner Cloud servers in Europe and USA) will be billed just as any other normal internet traffic"* — but that sentence is about **server** traffic, and neither the FAQ nor the locations page says what a cross-zone snapshot restore costs. **Not stated; not estimated here.**

DigitalOcean's model is the mirror image: you pick the region, so you control the geography, but the default is *one* region and every extra region is a click you have to remember to make.

## How many restore points you actually have

The retention numbers differ in a way that matters when you go looking for last Tuesday:

| Host | Automatic | Manual | What happens when you delete the server |
|---|---|---|---|
| DigitalOcean | *"We retain **weekly backups for four weeks** and **daily backups for seven days**"* | Snapshots kept *"until you choose to delete them"* | Convert to a snapshot first — the convert-to-snapshot page is the sanctioned route |
| Hetzner | *"For every server, there are **seven slots** for Backups. If all slots are full and you create an additional one, then the oldest Backup will be deleted"* | *"Up to **30** Snapshots across all projects"*; *"never deleted or updated automatically"* | *"Backups … will automatically be deleted if you delete the server"*; snapshots *"remain available even if you delete the server"* |

Two practical notes out of that table. First, **Hetzner's cap is account-wide (30) and DigitalOcean's is per-volume (25)** — so a single 25-snapshot volume on DigitalOcean already holds more copies than Hetzner allows across your entire account. Second, **on both hosts the automatic backup dies with the machine**; the thing that outlives a server is always the snapshot you made deliberately. DigitalOcean's convert-to-snapshot page closes the loop explicitly: *"If you want to keep a backup indefinitely, you can convert it to a snapshot,"* and then points you straight at *"copy snapshots to additional datacenter regions."*

One more restore blocker that is easy to miss: Hetzner requires the architecture to match. *"The architecture type of a new server always has to match the architecture type of the Backup/Snapshot used to create the server"* — an x86 snapshot cannot become an Arm64 server, in either direction.

## Time: what a snapshot actually costs you in hours

DigitalOcean's support answer gives a rate, not a promise: *"Creating a snapshot or backup takes about **1 to 3 minutes per GB** of used disk space on the Droplet, so a Droplet with 10 GB of used disk space would take 10 to 30 minutes."* Applied to the plan sizes people actually buy:

| Used disk on the Droplet | Snapshot time |
|---|---|
| 10 GB (DigitalOcean's own example) | 10–30 min |
| 25 GB | 25–75 min |
| 50 GB | 50 min – 2 h 30 m |
| 80 GB | 1 h 20 m – 4 h |
| 200 GB | 3 h 20 m – 10 h |

Then add *"several minutes"* per region for each Add to region. A four-region DR posture on an 80 GB server is realistically a **half-day job**, not an afternoon click. Note also that the clock runs on *used* space, and DigitalOcean warns that size is an estimate: *"Snapshots of Droplets are a best estimate based on the disk usage. Snapshots of volumes operate at the block storage level, so the snapshot size may not match what the filesystem reports."* Hetzner publishes no comparable timing figure — not verifiable.

## Hosts that publish nothing

- **Hostinger** (product page read 2026-10-23) sells the move and not the copy. Its page promises *"**Change location anytime** — Move your VPS to any of our **10 locations**"* across *"10 data centers across 4 continents"* (USA, Brazil, France, Germany, the UK, Lithuania, India, Indonesia and Malaysia are named in the footer), while the only data-protection line on the page is *"**Free weekly backups** — Keep your data protected with automatic weekly backups. Restore your VPS from your dashboard whenever needed."* **The word "snapshot" does not appear on the page**, and there is no statement about how many restore points, how long they are kept, where they are stored, or whether a backup made in one location can be restored in another. Not verifiable.
- **Liquid Web** (packages page read 2026-10-23) bundles *"Acronis Backup"* at **100 / 250 / 500 GB** on its three Linux tiers and *"Automated backups — daily backups that scale with the package."* No region, location, or cross-site restore policy is stated anywhere on the page. Not verifiable.
- **Namecheap**: as throughout this series, its product page has returned **403** to direct scripted requests; nothing is quoted from it here.
- **Hetzner pricing**: the Backups/Snapshots overview page (ID CL-5DCF1, last change 2026-09-03) has a heading called **"Pricing"** whose entire content is *"For information about the prices, see the respective info box at hetzner.com/cloud/regular-performance/"* — and that product page, read today, carries no backup or snapshot price either. **Hetzner's snapshot and backup rates are not verifiable, and are not estimated here.** What is verifiable is that Hetzner's overview repeats the exclusion from the top of this article: *"Backups and Snapshots do not include any Volumes which are attached to your server."*

## What to do with this

1. **Decide your host by which kind of copy you rely on.** If your safety net is *automatic* backups, Hetzner's are cross-location restorable out of the box and DigitalOcean's are not documented as such — DigitalOcean's backup docs never state a region rule at all, in either direction. If your safety net is *manual* snapshots, both are portable, and DigitalOcean's are portable in more places.
2. **On DigitalOcean, convert before you destroy.** Automatic backups are retained *"four weeks"* (weekly) or *"seven days"* (daily). Convert to a snapshot, then use **Add to region**. Do it before the Droplet is gone.
3. **Use the free multi-region copy.** DigitalOcean charges $0.06/GB/mo whether your snapshot lives in one region or ten. Cost per region-copy is `0.06 ÷ regions`. There is no reason to leave a snapshot in only one region.
4. **Never plan capacity on volume snapshots.** They are *"not incremental"*, capped at **25**, and immobile. Budget `snapshots × $0.06 × GiB`; the ceiling is **15.0x** the volume's own bill at any size. If you need more than a handful of restore points on attached storage, the volume is the wrong place for that data.
5. **Check the fire-zone case, not the headline.** On Hetzner, *"not location bound"* still leaves Ashburn, Hillsboro and Singapore snapshots in the same location as the server, and Hillsboro and Singapore backups in the same data center. If second-site separation is the requirement, those three locations do not give it to you for snapshots.
6. **Match the architecture.** Hetzner will not restore an x86 image onto an Arm64 server. Check before you plan a migration around a snapshot.
7. **Budget hours, not minutes.** Snapshotting runs at **1–3 min per GB of used space** on DigitalOcean, plus *"several minutes"* per added region.

Every number above is quoted from a host's own page read on 2026-10-23, or is arithmetic you can redo from those numbers. Where a host does not publish a figure — Hetzner's rates, Hostinger's snapshot policy, Liquid Web's restore geography — it says so rather than filling the gap. On a VPS deal page, that silence is usually the most expensive line in the offer.

### Where each number came from

- DigitalOcean region default, free multi-region, and the volume-snapshot transfer ban: `docs.digitalocean.com/products/snapshots/how-to/change-regions/` (page states "Last verified 13 Jul 2026").
- $0.06/GB and $0.06/GiB, the $0.01 minimum, and "no additional charge for making a snapshot available in multiple regions": `docs.digitalocean.com/products/snapshots/details/pricing/`.
- 25 snapshots per volume, non-incremental, one per 10 minutes, no cross-region or cross-account transfer for volume snapshots: `docs.digitalocean.com/products/snapshots/details/limits/`.
- 20% / 30% of Droplet cost and the $0.04–$0.01 per GiB usage-based ladder: `docs.digitalocean.com/products/backups/details/pricing/`.
- Four weeks / seven days retention and the convert-to-snapshot route: `docs.digitalocean.com/products/backups/how-to/convert-to-snapshot/`.
- 1–3 minutes per GB: `docs.digitalocean.com/support/how-long-will-my-backup-or-snapshot-take-to-complete/`.
- "Not location bound", the 6×6 restore matrix, the snapshot storage mapping, seven Backup slots, 30 Snapshots across all projects, architecture matching, and volumes excluded: `docs.hetzner.com/cloud/servers/backups-snapshots/faq/` (ID CL-B2495).
- Seven Backup slots, snapshots never auto-deleted, volumes excluded, and the empty "Pricing" section: `docs.hetzner.com/cloud/servers/backups-snapshots/overview/` (ID CL-5DCF1, last change 2026-09-03).
- Four network zones / six locations, colocation in the USA and Singapore, and cross-zone traffic billing: `docs.hetzner.com/cloud/general/locations/` (ID CL-113CC).
- Ten data centers, "Change location anytime", "Free weekly backups", no snapshot policy: `hostinger.com/vps-hosting`, read 2026-10-23.
- Acronis Backup 100 / 250 / 500 GB per tier: `liquidweb.com/vps-hosting/packages/`, read 2026-10-23.
