---
title: "Cheap VPS Deals: You Picked the Wrong Datacenter — What Moving Actually Costs"
slug: vps-deals-wrong-datacenter-move
date: 2026-10-19
description: "Read off five hosts' own pages on 2026-10-19: not one of them will move your VPS to another region. Hostinger is the only host with a button for it — and its own KB warns that reinstalling in a new location 'will permanently delete all existing data, including backups and snapshots,' with an SFTP download as the only sanctioned safeguard. Hetzner writes it flat: 'It is not possible to change the location of an existing server.' DigitalOcean's path is snapshot → add the image to a new region (free, 'no additional charge for making a snapshot available in multiple regions') → new Droplet, and along the way your IPv4 dies ('you cannot retain a Droplet's IPv4 when you transfer the Droplet to a new region') and your disk can only get bigger ('You cannot downsize a Droplet from a snapshot'). Plus the arithmetic nobody publishes: keeping the snapshot costs $0.06/GB/month, which is 15%–25% of each DigitalOcean Basic tier's own monthly price, and the forgotten 320 GiB one bills $230.40 a year — 57.6 months of the $4.00/mo Droplet — with no way to download it and stop the clock."
question: I bought a cheap VPS in the wrong datacenter — can I move it to another region, or do I have to rebuild from scratch?
sources:
  - https://docs.digitalocean.com/support/how-do-i-migrate-my-droplet-to-another-datacenter-region/
  - https://docs.digitalocean.com/products/snapshots/how-to/change-regions/
  - https://docs.digitalocean.com/products/snapshots/how-to/migrate-droplets/
  - https://docs.digitalocean.com/products/snapshots/details/pricing/
  - https://docs.digitalocean.com/support/can-i-preserve-my-droplets-ipv4-address-when-i-transfer-the-droplet/
  - https://docs.digitalocean.com/support/can-i-downsize-a-droplet-using-a-snapshot/
  - https://docs.digitalocean.com/support/can-i-download-a-backup-or-snapshot/
  - https://docs.digitalocean.com/support/how-long-will-my-backup-or-snapshot-take-to-complete/
  - https://docs.digitalocean.com/products/droplets/details/availability/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/cloud/servers/faq/
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/
  - https://docs.hetzner.com/cloud/servers/primary-ips/overview/
  - https://www.hostinger.com/support/10289743-how-to-transfer-your-vps-to-a-different-location-in-hostinger/
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/support/knowledgebase/subcategory/48/vps/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off five hosts' own pages on 2026-10-19: not one of them will move your VPS to another datacenter. Not one.** Three of the five publish an actual answer, and the three answers are shaped differently enough that the differences — not the price, not the RAM — decide what a wrong-region mistake costs you.

Hetzner states it in one line: *"It is not possible to change the location of an existing server."* DigitalOcean never says "no"; it says *"take a snapshot of your Droplet and then create new Droplet from the snapshot in the new datacenter"* — a rebuild, not a move. Hostinger is the only one of the three that gives you a real button: its KB explains that *"although the location of your Virtual Private Server (VPS) cannot be changed directly, you can reinstall it in a new location as an alternative"* — and then warns, in bold, that doing so *"will permanently delete all existing data, including backups and snapshots."*

So the answer to "can I move it" is **no, everywhere** — and the answer that actually matters is **what the substitute destroys on the way.** That is what this page measures.

## The one-line answer, per host (read 2026-10-19)

| Host | Can an existing VPS be moved to another region? | What the official path is | What survives | What dies |
|---|---|---|---|---|
| **DigitalOcean** | No — rebuild | Snapshot → add image to the new region → create a new Droplet from it | Disk contents, user accounts, SSH keys | IPv4 address, backups, volume snapshots |
| **Hetzner** | No — *"not possible"* | Create a **new** server in the desired location from a Snapshot or Backup of the old one | Disk contents up to the moment of the snapshot | Anything written after the snapshot; the old server stays |
| **Hostinger** | No — reinstall in place | VPS → Plan details → **Change** → pick location → Next | Nothing | *"all existing data, including backups and snapshots"* |
| **Namecheap** | No published answer | None found | — | — |
| **Liquid Web** | No published answer | "Expert-led migrations" (marketing copy, no relocation policy) | — | — |

## DigitalOcean: the move is free, the snapshot is not

DigitalOcean's migration doc is unusually explicit about the sequence, and its pricing page is unusually explicit about the price. Put the two together and the cost of a region change on DigitalOcean is **$0.00 for the transfer and a per-GB monthly rent on the copy.**

From the snapshots pricing page: *"Snapshots are charged at $0.06 per GB per month for Droplets... There is a minimum charge of $0.01... There is no additional charge for making a snapshot available in multiple regions."* And from the how-to: *"By default, a Droplet snapshot is only available in the region where it was created. If you want to use a snapshot to create Droplets in other regions, you need to add the snapshot to those regions first."*

That means the geographic part of the move is free and the *storage* part keeps billing. Here is that rent worked out against every Basic (shared-CPU) tier on the pricing page, read 2026-10-19, using the full boot-disk size as the upper bound:

| Plan (slug) | vCPU / RAM | Boot disk | Price/mo | Snapshot rent/mo (disk × $0.06) | Rent as % of the plan | 24 h running both |
|---|---|---|---|---|---|---|
| `s-1vcpu-512mb-10gb` | 1 / 0.5 GB | 10 GiB | $4.00 | $0.60 | **15.0%** | $0.14 |
| `s-1vcpu-1gb` | 1 / 1 GB | 25 GiB | $6.00 | $1.50 | **25.0%** | $0.21 |
| `s-1vcpu-2gb` | 1 / 2 GB | 50 GiB | $12.00 | $3.00 | **25.0%** | $0.43 |
| `s-2vcpu-2gb` | 2 / 2 GB | 60 GiB | $18.00 | $3.60 | **20.0%** | $0.64 |
| `s-2vcpu-4gb` | 2 / 4 GB | 80 GiB | $24.00 | $4.80 | **20.0%** | $0.86 |
| `s-4vcpu-8gb` | 4 / 8 GB | 160 GiB | $48.00 | $9.60 | **20.0%** | $1.71 |
| `s-8vcpu-16gb` | 8 / 16 GB | 320 GiB | $96.00 | $19.20 | **20.0%** | $3.43 |

Three things fall out of that table.

**The overlap is cheap; the snapshot is not.** Running old and new side by side for a day costs $0.14–$3.43 depending on tier. Leaving the snapshot behind costs 15%–25% of the machine's own price *every month*, indefinitely. On the 320 GiB tier, one year of a forgotten snapshot is **$230.40 — which is 57.6 months of the $4.00/mo Droplet**, i.e. 4.8 years of the cheapest machine on the platform, spent on a disk image.

**You cannot make the billing stop by moving the data off.** DigitalOcean's own support page: *"You cannot currently download DigitalOcean backups or snapshots, but you can use third-party tools to save your data locally."* The only lever that zeroes the $0.06/GB is deleting the snapshot — which deletes the copy. Hostinger's official instruction is the exact opposite: download first, *then* press the button.

**Time scales on used space, cost scales on disk.** *"Creating a backup or snapshot takes about 1 to 3 minutes per GB of used disk space"* — while the downsize doc notes that *"the entire disk is imaged, not only the data present on the disk."* A 320 GiB machine with 40 GB used snapshots in 40–120 minutes but is billed on the image. Budget the wall clock on used data; budget the invoice on the disk.

## The datacenter trap nobody warns you about

DigitalOcean's Droplet availability page (last updated 2026-08-25) lists **16 datacenters**: NYC1, NYC2, NYC3, AMS3, SFO2, SFO3, SGP1, LON1, FRA1, TOR1, BLR1, SYD1, ATL1, RIC1, MKC1, MEM1. They are not interchangeable.

- The classic plan families (Basic, General Purpose, CPU-Optimized, Memory-Optimized, Storage-Optimized) are **fully available in 11** of them, partially available in 4 (SFO2 *"Premium AMD CPUs are not available"*; ATL1, RIC1, MKC1 *"Only Premium … CPUs are available"*), and **not available at all in MEM1**.
- **v5 configurations are available in exactly 4** — ATL1, RIC1, MKC1, MEM1.

The overlap between those two sets is **zero**. There is not one datacenter where a v5 Droplet and a fully-provisioned classic Basic Droplet both exist. If you are on a v5 plan and you want to be in New York, Amsterdam or Singapore, the migration is not geographic — you are changing plan family at the same time, and the snapshot route will not carry the plan with it.

## The ratchet: a move is one-way on disk size

*"You cannot downsize a Droplet from a snapshot. Data is not always stored sequentially in memory, so reducing the size of a disk can result in data loss or corruption."* And the reason is structural: *"When creating a snapshot, the entire disk is imaged, not only the data present on the disk. This means that you can only create Droplets with as much disk space as the Droplet the snapshot was taken from, or more."*

So every snapshot-based region change has a floor: **the new machine's disk is ≥ the old machine's disk.** If part of why you wanted to move was to land somewhere cheaper and smaller, the official path cannot do it. DigitalOcean's own workaround is to *"create a smaller Droplet and then transfer your data over the new Droplet using `rsync`"* — a second migration method, on top of the snapshot one.

Two more casualties on the same page, both official:

- **Your IPv4 dies.** *"Unfortunately, you cannot preserve a Droplet's IP address when transferring the Droplet between regions, nor can you reassign a non-reserved IP address to another Droplet."* And you cannot pre-empt it: *"You cannot convert a Droplet IP address into a Reserved IP."* A Reserved IP is region-bound too, so it is a way to keep an address across *rebuilds in one region*, not across regions.
- **Volume snapshots do not move.** *"You cannot transfer volume snapshots to other regions."* Only Droplet snapshots can be added to another region.

## Hostinger: the only one-click move — and it deletes the safety net

Hostinger's KB article *"How to transfer your VPS to a different location in Hostinger"* (updated ~2 months before 2026-10-19) is the single most useful relocation document in this comparison, because it is the only one describing a button you press inside your existing plan:

> *"Although the location of your Virtual Private Server (VPS) cannot be changed directly, you can reinstall it in a new location as an alternative."*
> *"Important: Reinstalling your VPS in a new location will permanently delete all existing data, including backups and snapshots. To avoid losing important information, ensure you create and download a full backup via SFTP before proceeding."*

The steps are: VPS section → select the server → **VPS Plan details → Change** → choose the location from the dropdown → Next.

The collision with Hostinger's own product page is worth stating plainly. The VPS page (read the same day) lists **"Free weekly backups"** as an included feature on every plan — and the relocation procedure destroys backups and snapshots by design. So on Hostinger the host's own safety net is *inside the blast radius of the move*, and the only sanctioned way out is to pull 50–400 GB down over SFTP yourself first — the plan sizes on that page being KVM 1 (50 GB NVMe), KVM 2 (100 GB), KVM 4 (200 GB), KVM 8 (400 GB).

That gives you the cleanest rule in this whole comparison: **the easier the move, the more it deletes.** Hostinger's one-button move costs you every copy the host was holding for you. DigitalOcean's manual rebuild is slower, but the old Droplet keeps running while you test the new one, and the docs even recommend it — *"it can be worth the cost to retain the original Droplet and snapshots, run automated and manual tests."*

## Hetzner: flat no, plus a copy you must keep current

Hetzner's Cloud FAQ answers the question directly under the heading *"How can I change the location of my server?"*:

> *"It is not possible to change the location of an existing server. When you create a new server in the desired location, you can, however, choose to use a Snapshot or Backup of the existing server. The new server will then be a direct copy of the existing server."*

Two limits govern what you can copy, both from the backups/snapshots overview: **up to 7 Backup slots per server**, and **by default up to 30 Snapshots across all projects**. Snapshots also *"are never deleted or updated automatically"* — so unlike a rolling backup window, a Hetzner snapshot is a manual commitment.

And the caveat that decides whether a Hetzner move loses data: *"Make sure that your Snapshot is up to date. Changes that have been made on the server after the Snapshot was created, are not included in the Snapshot."* If your latest Backup is stale, the doc tells you to *"create a new Backup manually"* first. There is no automatic "sync the delta at cutover" step on any of the three hosts — the copy is as old as the copy.

Hetzner's IP economics are at least published, unlike the relocation itself: a Primary IPv4 is **€0.50 / $0.60 per month (€0.0008 / h)**, Primary IPv6 is free, each server holds one of each, and the account total is *"server limit multiplied by 2."* Hetzner's docs do not state whether a Primary IP can follow a server across locations, so treat your address as lost on a Hetzner move too.

## What the three comparison sites actually answer

Checked all three on 2026-10-19, first screen down:

- **LowEndBox** — the homepage's whole location system is a **filter taxonomy** (North America → West Coast / Inland / East Coast; Europe; Asia/Pacific — down to city), and the intro says *"Browse budget-friendly VPS and dedicated server offers by location, virtualization type, and special features like NVMe or DDoS protection."* Location is a shopping filter, not a lifecycle question. Nothing on the page says what happens after you buy.
- **Namecheap** — the VPS card on the homepage carries a price and a term and no location field at all. The nearest thing to a location control anywhere on that first screen is a URL parameter on the *shared hosting* buy link (`addons=server-location;server-location-us`).
- **Liquid Web** — the packages page never states when or how a datacenter is chosen. The only location text is *"With data centers in the U.S., Europe, and Australia"*, and the only migration text is the value-prop *"Our team has migrated thousands of sites. You choose the timing, we handle the technical details."* No relocation policy, no downtime figure, no cost.

None of the three gives an answer. That is the gap this page fills.

## Not verifiable (2026-10-19, no proxies, no UA spoofing)

- **Namecheap** — no relocation path is published. Its VPS knowledge-base section (`/support/knowledgebase/subcategory/48/vps/`) listed **46 articles** when read today and **none** concerns changing a server's location or datacenter; the VPS product page `/hosting/vps/` returned **403** to a direct fetch.
- **Liquid Web** — `/vps-hosting/packages/` returned **403** to a direct fetch; the quotes above come from reading the public page text, and the relocation policy itself is not published there.
- **Vultr** — `/pricing/` and the instance-move doc both returned **403**.
- **Linode / Akamai** — `techdocs.akamai.com` returned a navigation shell only (3.7 MB of SPA chrome, no article body); no cross-region migration text could be read.
- **Hetzner snapshot pricing** — the docs defer to *"the respective info box at hetzner.com/cloud"*, which is client-rendered and returned no figures. No Hetzner price is asserted on this page.

## What to do, in order

1. **Decide whether you are moving regions or moving plan families.** On DigitalOcean, if you are on v5, any target outside ATL1 / RIC1 / MKC1 / MEM1 forces a plan change at the same time — check `docs.digitalocean.com/products/droplets/details/availability/` before you snapshot anything.
2. **Take the copy, then take it again.** Hetzner's rule is the general rule: only what existed at snapshot time travels. On a busy server, quiesce the writers, snapshot, and verify.
3. **Budget the wall clock on used data and the invoice on disk.** 1–3 minutes per GB *used*; $0.06 per GB of *disk* per month, thereafter, forever.
4. **On DigitalOcean, put a calendar reminder on the snapshot.** At 15%–25% of the tier's monthly price, a snapshot nobody deleted is the most expensive thing most people leave behind after a move — and you cannot download it to make the billing stop.
5. **On Hostinger, download before you press Change.** Everything goes, including the "free weekly backups" the product page sells you on. 50–400 GB over SFTP is the official price of that button.
6. **Assume the IP is gone.** DigitalOcean says it outright; neither Hetzner nor Hostinger documents an address that follows a server to a new location. Lower your DNS TTL *before* you start, not after.
7. **If you also wanted to shrink, do not use the snapshot.** It can only grow. Use `rsync` onto a freshly-created smaller machine, and keep both running until you have tested.
