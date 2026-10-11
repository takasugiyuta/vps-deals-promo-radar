---
title: What a Gigabyte of VPS Disk Actually Costs (NVMe vs SSD, Priced Per GB)
slug: vps-deals-cost-per-gb-disk
date: 2026-10-11
description: Every VPS deal page calls its storage "NVMe" or "SSD" but none of them price it. Read on 2026-10-11, DigitalOcean's own pricing page puts a gigabyte of included disk anywhere from $0.24 to $2.52 a month — a 10.5x spread, and the NVMe badge does not predict where a plan lands. Hostinger sells NVMe at $0.065/GB, which is cheaper than DigitalOcean's non-NVMe SSD.
question: On a VPS deal, how much more does NVMe storage actually cost than SSD, measured per gigabyte?
sources:
  - https://www.digitalocean.com/pricing/droplets
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/hosting/vps/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**The short answer: NVMe costs DigitalOcean about 46% more per gigabyte than its own regular SSD — and that is the only honest number in this article, because at one vendor the spread inside the NVMe-labelled plans alone is 5.77x.** Read on 2026-10-11, `digitalocean.com/pricing/droplets` publishes 31 plans across five families. Divide the monthly price by the included disk and a gigabyte costs anywhere from **$0.24** to **$2.52** per month. That is a **10.5x spread on one vendor's own page**, and the word "NVMe" tells you nothing about where in that range a plan sits.

Meanwhile the cross-vendor number runs the other way entirely. Hostinger sells **400 GB of NVMe for $25.99/mo — $0.065 per GB**. DigitalOcean's plain, non-NVMe SSD is **$0.30 per GiB**. Hostinger's NVMe is **4.6x cheaper per gigabyte than DigitalOcean's regular SSD**, and it is still cheaper if you price Hostinger at its *renewal* rate, which is the worst case.

So the two questions people actually ask — "is NVMe worth it?" and "how much more does NVMe cost?" — have completely different answers, and neither is the one the deal pages imply.

## The formula, so you can check this yourself

Every number below is one division. No estimation, no extrapolation, no scraping a field that does not exist:

```
$ per GB of disk = monthly plan price (USD) ÷ included disk (GB or GiB)
```

One worked example: DigitalOcean's Basic 16 GiB / 8 vCPU plan is listed at **$96.00/mo** with **320 GiB** of SSD. `96.00 ÷ 320 = 0.300`. That plan sells disk at **$0.30/GiB/month**.

Two caveats, stated up front so you can discount the numbers honestly:

1. **This is a bundling metric, not a marginal price.** You are not buying disk alone; you are buying RAM, vCPU, transfer and disk in one package. `$/GB` measures how generously a plan is provisioned with disk relative to its price. It is the right number for comparing two plans, and the wrong number for computing what one extra gigabyte would cost you.
2. **DigitalOcean quotes GiB, Hostinger quotes GB.** 1 GB = 0.931 GiB, so Hostinger's true per-GiB figure is about **7.4% worse** than its per-GB figure. I give both below, because at a 4.6x gap the unit difference does not change any conclusion, but it would be sloppy not to show it.

## The whole DigitalOcean table, priced per gigabyte

Read from `digitalocean.com/pricing/droplets` on 2026-10-11. Disk figures come from the column headed **SSD** (Basic) and **SSD** on the four premium families, which each carry a disk-variant selector defaulted to 1x.

| Family | Memory | vCPU | Disk | $/mo | **$/GiB** |
|---|---|---|---|---|---|
| Basic | 512 MiB | 1 | 10 GiB | $4.00 | **$0.4000** |
| Basic | 1 GiB | 1 | 25 GiB | $6.00 | **$0.2400** |
| Basic | 2 GiB | 1 | 50 GiB | $12.00 | **$0.2400** |
| Basic | 2 GiB | 2 | 60 GiB | $18.00 | **$0.3000** |
| Basic | 4 GiB | 2 | 80 GiB | $24.00 | **$0.3000** |
| Basic | 8 GiB | 4 | 160 GiB | $48.00 | **$0.3000** |
| Basic | 16 GiB | 8 | 320 GiB | $96.00 | **$0.3000** |
| CPU-Optimized | 4 GiB | 2 | 25 GiB | $42.00 | **$1.6800** |
| CPU-Optimized | 8 GiB | 4 | 50 GiB | $84.00 | **$1.6800** |
| CPU-Optimized | 16 GiB | 8 | 100 GiB | $168.00 | **$1.6800** |
| CPU-Optimized | 32 GiB | 16 | 200 GiB | $336.00 | **$1.6800** |
| CPU-Optimized | 64 GiB | 32 | 400 GiB | $672.00 | **$1.6800** |
| CPU-Optimized | 96 GiB | 48 | 600 GiB | $1,008.00 | **$1.6800** |
| General Purpose | 8 GiB | 2 | 25 GiB | $63.00 | **$2.5200** |
| General Purpose | 16 GiB | 4 | 50 GiB | $126.00 | **$2.5200** |
| General Purpose | 32 GiB | 8 | 100 GiB | $252.00 | **$2.5200** |
| General Purpose | 64 GiB | 16 | 200 GiB | $504.00 | **$2.5200** |
| General Purpose | 128 GiB | 32 | 400 GiB | $1,008.00 | **$2.5200** |
| General Purpose | 160 GiB | 40 | 500 GiB | $1,260.00 | **$2.5200** |
| Memory-Optimized | 16 GiB | 2 | 50 GiB | $84.00 | **$1.6800** |
| Memory-Optimized | 32 GiB | 4 | 100 GiB | $168.00 | **$1.6800** |
| Memory-Optimized | 64 GiB | 8 | 200 GiB | $336.00 | **$1.6800** |
| Memory-Optimized | 128 GiB | 16 | 400 GiB | $672.00 | **$1.6800** |
| Memory-Optimized | 192 GiB | 24 | 600 GiB | $1,008.00 | **$1.6800** |
| Memory-Optimized | 256 GiB | 32 | 800 GiB | $1,344.00 | **$1.6800** |
| Storage-Optimized | 16 GiB | 2 | 300 GiB | $131.00 | **$0.4367** |
| Storage-Optimized | 32 GiB | 4 | 600 GiB | $262.00 | **$0.4367** |
| Storage-Optimized | 64 GiB | 8 | 1,170 GiB | $524.00 | **$0.4479** |
| Storage-Optimized | 128 GiB | 16 | 2,340 GiB | $1,048.00 | **$0.4479** |
| Storage-Optimized | 192 GiB | 24 | 3,520 GiB | $1,572.00 | **$0.4466** |
| Storage-Optimized | 256 GiB | 32 | 4,690 GiB | $2,096.00 | **$0.4469** |

Three things fall out of that table that no deal page says.

**The NVMe badge does not price the disk.** DigitalOcean's own copy attaches NVMe to four of the five families — Memory-Optimized (*"Memory-Optimized Droplets use NVMe SSDs"*) and Storage-Optimized (*"Storage-Optimized Droplets use NVMe... can be order of magnitude faster than our regular SSDs"*) unconditionally, and CPU-Optimized and General Purpose only on their *"Premium variant"* (*"The Premium variant... also provides up to 10Gbps outbound network speeds and NVMe SSDs"*). Those four NVMe-tagged families charge **$0.4367, $1.6800, $1.6800 and $2.5200** per GiB. The cheapest NVMe and the most expensive NVMe on the page differ by **5.77x**. If you are choosing on the strength of the word "NVMe," you are choosing on a label that spans a 5.77x price range.

**The one clean NVMe-vs-SSD comparison is +45.6%.** Storage-Optimized is the family DigitalOcean commits to NVMe without conditions, and it is the only one that is also genuinely disk-heavy, so it is the only fair comparison against the regular-SSD Basic line. Storage-Optimized runs **$0.4367/GiB**; the Basic line settles at **$0.3000/GiB** from 60 GiB upward. That is a **45.6% premium**. Against Basic's cheapest rung ($0.2400/GiB) the premium is **81.9%**. So: *roughly 46–82%*, depending on which SSD rung you measure from. That is the answer to "how much more does NVMe cost" — and it is a lot less than the marketing implies, because the disk is not what you are paying for.

**The Basic line has no volume discount at all.** From 60 GiB to 320 GiB — a 5.3x increase in disk — the per-GiB price is flat at exactly **$0.3000**. And the smallest plan is the worst deal on the page: the 512 MiB / 10 GiB plan charges **$0.4000/GiB**, 67% more per gigabyte than the 1 GiB plan directly above it. If disk is what you need, the entry plan is the one plan never to buy it in.

## Hostinger: the premium is negative across vendors

Read from `hostinger.com/vps-hosting` on 2026-10-11. Every Hostinger KVM plan states its media explicitly as **"NVMe disk space"** in the plan feature list, and the page's own FAQ gives the prices: *"KVM 1 – $6.49/month, KVM 2 – $8.99/month, KVM 4 – $12.99/month, KVM 8 – $25.99/month."* The renewal rates are printed on the same cards as *"Renews at $11.99/mo for 2 years"* and so on.

| Plan | vCPU | RAM | NVMe disk | Promo $/mo | **$/GB promo** | Renews at | **$/GB renewal** |
|---|---|---|---|---|---|---|---|
| KVM 1 | 1 | 4 GB | 50 GB | $6.49 | **$0.1298** | $11.99 | **$0.2398** |
| KVM 2 | 2 | 8 GB | 100 GB | $8.99 | **$0.0899** | $14.99 | **$0.1499** |
| KVM 4 | 4 | 16 GB | 200 GB | $12.99 | **$0.0650** | $28.99 | **$0.1449** |
| KVM 8 | 8 | 32 GB | 400 GB | $25.99 | **$0.0650** | $49.99 | **$0.1250** |

Adjusted to GiB, the best tier is **$0.0697/GiB** on promo and **$0.1342/GiB** on renewal.

Now line that up against DigitalOcean:

- **Hostinger's NVMe on promo ($0.0650/GB) is 4.6x cheaper per gigabyte than DigitalOcean's regular SSD ($0.3000/GiB)** — the supposedly premium media, at the lower price.
- **Hostinger's NVMe on promo is 6.7x cheaper than DigitalOcean's NVMe** on Storage-Optimized ($0.4367/GiB).
- **Even at Hostinger's worst renewal rate — $0.2398/GB, the KVM 1 renewal, the least favourable number in that whole table — it still undercuts DigitalOcean's cheapest SSD rung of $0.2400/GiB.** The premium is not small. It is negative.

Two more structural differences worth knowing. Hostinger's per-GB price **falls** as you go up — $0.1298 → $0.0899 → $0.0650, a 2.0x volume discount — while DigitalOcean's Basic line is flat and its premium lines are perfectly flat. And Hostinger provisions **12.50 GB of disk per GB of RAM** on every single plan, against 20–30 on Basic, 6.25 on CPU-Optimized, 3.125 on General Purpose and Memory-Optimized, and 18.3–18.75 on Storage-Optimized. If you want to know how much disk you get for the RAM you are buying, that ratio is the faster test, and it is not printed anywhere.

## The benchmark that makes all of this concrete

The same DigitalOcean page carries an "Additional product pricing" table, and it is the only place on the page where a gigabyte is sold on its own:

- **Droplet Snapshots — $0.06/GB per month.**
- Backups, usage-based — *"start at $0.01/GiB per month."*

Put that next to the bundled figures and the bundling markup becomes visible:

| What you are buying | $/GiB | Multiple of DO's own snapshot rate ($0.06) |
|---|---|---|
| DigitalOcean snapshot storage | $0.06 | 1.0x |
| Hostinger NVMe, promo (KVM 4/8) | $0.0650 | 1.1x |
| DigitalOcean Basic SSD, cheapest | $0.2400 | **4.0x** |
| DigitalOcean Basic SSD, standard | $0.3000 | **5.0x** |
| DigitalOcean Basic SSD, 512 MiB plan | $0.4000 | **6.7x** |
| DigitalOcean Storage-Optimized NVMe | $0.4367 | **7.3x** |
| DigitalOcean CPU-Optimized / Memory-Optimized NVMe | $1.6800 | **28.0x** |
| DigitalOcean General Purpose NVMe | $2.5200 | **42.0x** |

**The most expensive gigabyte DigitalOcean sells is 42x the cheapest gigabyte DigitalOcean sells.** Both are on the same page. One is inside a General Purpose Droplet; the other is a snapshot. If your workload is read-heavy, archival, or anything that does not need block I/O at sub-millisecond latency, the plan upgrade is the expensive way to buy capacity.

There is a second, sharper use for that $0.01/GiB figure. DigitalOcean also offers percentage-based backups at **20% of Droplet cost (weekly)** or **30% (daily)**. Those two pricing models break even when:

```
disk GiB ÷ monthly price = 20   (weekly)   or   30   (daily)
```

No plan on the page gets close. The highest disk-to-price ratio DigitalOcean sells anywhere is **4.167 GiB per $1/month** (the Basic 1 GiB and 2 GiB / 1 vCPU plans); the General Purpose line manages **0.397**. So percentage-based backups are the expensive option on **every single plan published**, by 4.8x at best (Basic 1 GiB) and **50.4x** at worst (General Purpose, where weekly percentage backup of the $63/mo plan costs $12.60/mo against $0.25/mo usage-based). Pick usage-based.

## What I could not verify

Being straight about the holes, because a comparison table that quietly drops the unreadable vendors is worse than no table:

- **Namecheap** — `namecheap.com/hosting/vps/` returned **403** to this site's declared crawler on 2026-10-11. Its homepage advertises VPS *"From $3.88 Annual plan, Instead of $4.88/mo"* with no disk size and no media type at all. **Not verifiable.**
- **Liquid Web** — `liquidweb.com/vps-hosting/packages/` returned **403**. **Not verifiable.**
- **Vultr, Linode (Akamai), Contabo** — all **403**. **Not verifiable.**
- **Hetzner** — `hetzner.com/cloud` returns 200 but renders prices client-side, so no figures are extractable. **Not verifiable.**
- **DigitalOcean's disk-variant selector** (1x / 2x / 3x on the four premium families) is client-side; only the default 1x values are in the served HTML. I did not read the 2x and 3x prices, so this article makes no claim about the marginal price of adding disk within a premium plan.

No proxy, cache, or archive was used to fill any of those gaps, and no figure in this article came from anywhere but the two pages that returned 200.

## What to do with this

1. **Stop treating "NVMe" as a price signal.** Across the plans on one vendor's page it spans 5.77x. Across vendors it is inverted. The word tells you about the controller, not the invoice.
2. **If you can measure the real premium, it is about 46%.** Storage-Optimized NVMe at $0.4367/GiB versus Basic SSD at $0.3000/GiB. Pay that if you need the IOPS; do not pay it because a badge is green.
3. **Run the division before you upgrade.** `monthly price ÷ disk GB`. If you are comparing two plans and one is above $0.30/GB, you are buying RAM and vCPU and calling it storage.
4. **If you only need capacity, do not buy a bigger plan.** At $0.06/GB, snapshot storage is 4x to 42x cheaper than the same vendor's bundled disk, depending on the family.
5. **Buy disk where it is actually cheap.** Hostinger's NVMe at $0.065/GB undercuts DigitalOcean's regular SSD by 4.6x and its NVMe by 6.7x — and still wins at renewal. Check the renewal column before you sign; a promo per-GB number that triples on renewal is not a per-GB number you can plan with.

---

*Figures read 2026-10-11 from `digitalocean.com/pricing/droplets` and `hostinger.com/vps-hosting`, both returning HTTP 200. All per-gigabyte values are the monthly price divided by the included disk as printed on those pages. Vendors returning 403 or client-rendered pages are marked not verifiable and were not filled in from any other source.*
