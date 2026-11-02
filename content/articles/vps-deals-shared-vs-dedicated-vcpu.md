---
title: "VPS Deals: Is the vCPU You're Buying a Real Core? DigitalOcean and Hetzner Both Say It's a Thread — and Dedicated Costs Exactly 75% More"
slug: vps-deals-shared-vs-dedicated-vcpu
date: 2026-11-03
description: "Read off the vendors' own pages on 2026-11-03. Two hosts that publish a definition of \"vCPU\" agree on the same thing: it is not a core. DigitalOcean: \"A vCPU is a unit of processing power corresponding to a single hyper-thread on a processor core.\" Hetzner, on its dedicated line: \"Here one vCPU equals one thread of a physical CPU core.\" So the \"8 vCPU\" on a VPS deal page is eight threads, and neither host publishes how many threads sit on a physical core. The bigger finding is the price: at DigitalOcean, every size sold both ways costs exactly 1.75x as much when the vCPU is dedicated — 2 vCPU/4 GB is $24 shared vs $42 dedicated, 8 vCPU/16 GB is $96 vs $168 — and the dedicated plan ships 31.25% of the disk for that 75% premium. Hetzner prices the trade differently: at equal RAM the dedicated CCX line costs more and gives you half the threads (+20.8% at 8 GB, +23.6% at 16 GB, +6.5% at 32 GB), while its entry dedicated server is 6.70x the price of its entry shared one. Also published nowhere else: Hetzner charges US buyers about 75% more for the identical shared spec (8 vCPU/16 GB is EUR 69.99 in EU-central and EUR 120.99 in Hillsboro/Ashburn)."
question: In a VPS deal, is the vCPU you're buying a dedicated physical core or a shared thread, how do you tell which one you got, and what does the dedicated version actually cost?
sources:
  - https://docs.digitalocean.com/products/droplets/concepts/choosing-a-plan/
  - https://docs.digitalocean.com/products/droplets/details/pricing/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.digitalocean.com/reference/api/reference/sizes/
  - https://docs.hetzner.com/cloud/servers/faq/
  - https://www.hetzner.com/cloud/
  - https://www.hetzner.com/cloud/regular-performance/
  - https://www.hetzner.com/cloud/general-purpose/
  - https://www.hostinger.com/vps-hosting
  - https://www.vultr.com/products/cloud-compute/
  - https://www.linode.com/products/shared/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the vendors' own pages on 2026-11-03: a "vCPU" on a VPS deal page is a thread, not a core — DigitalOcean and Hetzner both say so in writing — and the word "dedicated" is the most expensive adjective in VPS pricing.** DigitalOcean: *"A vCPU is a unit of processing power corresponding to a single hyper-thread on a processor core."* Hetzner, describing its dedicated line: *"Here one vCPU equals one thread of a physical CPU core."* Neither host publishes how many threads sit on one physical core, so the honest reading of any deal page is that **8 vCPU means eight threads, and nobody selling you the box is telling you how many cores that is.**

The three things that decide what you are actually buying:

1. **Only the CPU is shared.** DigitalOcean states it outright: *"Resources like RAM, disk storage, and network bandwidth are always dedicated, but you can choose between shared CPU and dedicated CPU plans for dedicated vCPU."* The RAM figure on the deal page is real. The vCPU figure is the one with an asterisk.
2. **Dedicated threads carry a fixed premium.** At DigitalOcean, every size that is sold both ways costs **exactly 1.75x** dedicated — 2 vCPU/4 GB: $24.00 shared vs $42.00 dedicated; 4 vCPU/8 GB: $48.00 vs $84.00; 8 vCPU/16 GB: $96.00 vs $168.00. Same network allowance, and the dedicated plan ships **31.25% of the disk**.
3. **Hetzner prices the trade in threads, not dollars.** At equal RAM its dedicated CCX line costs more and hands you **half as many vCPUs**: +20.8% at 8 GB, +23.6% at 16 GB, +6.5% at 32 GB. Its cheapest dedicated server (EUR 43.49) is **6.70x** its cheapest shared one (EUR 6.49).

## The answer, in one table

Every cell is quoted or computed from the pages listed at the bottom, read on 2026-11-03.

| Question | DigitalOcean | Hetzner Cloud | Hostinger |
|---|---|---|---|
| **What is a vCPU?** | *"A vCPU is a unit of processing power corresponding to a single hyper-thread on a processor core."* | Dedicated line: *"Here one vCPU equals one thread of a physical CPU core."* | Not defined. The page says *"two virtual CPU cores"* — it calls them cores, not threads |
| **Which plans are shared?** | **Basic** (bundled) and **Shared** (v5). *"There are five bundled Droplet plans: one shared CPU plan and four dedicated CPU plans."* | **CX, CPX, CAX** — *"the compute resources are distributed among all instances on the same physical server"* | Not stated. The page makes one blanket claim: *"you will get dedicated resources, such as CPU power, RAM, or disk space."* |
| **Which plans are dedicated?** | General Purpose, CPU-Optimized, Memory-Optimized, Storage-Optimized (bundled); **General Purpose** (v5) | **CCX** — *"Plans (CCX) with dedicated resources have their CPU resources exclusively"* | Same blanket claim, no split published |
| **What does shared actually mean?** | *"the hyper-thread allocated to the Droplet may be shared between multiple other Droplets"*; the hypervisor hands out more under load — *"can"* give full threads *"but it's not guaranteed"* | *"a baseline CPU performance and have the option to temporarily burst CPU usage above the baseline level"* | Not stated |
| **Is the baseline/burst level published?** | No — not verifiable | No — not verifiable | No |
| **Can you switch later?** | Not between v5 and bundled plans (see below) | *"you can also rescale to and from a plan with shared resources"* | Not stated |
| **Cheapest shared / cheapest dedicated** | $4.00/mo (1 vCPU, 512 MB) / $42.00/mo (2 vCPU, 4 GB) | EUR 6.49/mo (CPX02) / EUR 43.49/mo (CCX13) | No dedicated tier published |

## What the vendors promise, in their own words

This is the part a spec table never shows you, and it is where "dedicated" stops being marketing and becomes a contract.

| Promise | DigitalOcean | Hetzner |
|---|---|---|
| **Dedicated vCPU** | *"Dedicated CPU Droplets have guaranteed access to the full hyper-thread at all times."* | *"Plans (CCX) with dedicated resources have their CPU resources exclusively… Instances with dedicated resources offer continuous and predictable high CPU performance."* |
| **Shared vCPU** | *"With shared CPU Droplets, the hyper-thread allocated to the Droplet may be shared between multiple other Droplets. When a shared CPU Droplet experiences heavier load, the hypervisor dynamically allocates more hyper-thread(s) to it."* | *"In plans (CX, CPX, CAX) with shared resources the compute resources are distributed among all instances on the same physical server. These instances provide a baseline CPU performance and have the option to temporarily burst CPU usage above the baseline level."* |
| **The catch** | *"the amount of CPU cycles available for the hypervisor to allocate depends on the workload of the other Droplets sharing that host. If these neighboring Droplets have high load, a Droplet could receive fractions of hyper-threads instead of dedicated access to the underlying physical processors. In practice, this means that shared CPU Droplets can have access to full hyper-threads, but it's not guaranteed."* | Hetzner never names the baseline, the burst ceiling, or how long a burst may last. The only number-free reassurance is *"This allows us to provide these shared plans to you at a much lower price."* |
| **Which CPU** | CPU-Optimized: *"Backed by Intel's Ice Lake and older processors with base clock speeds in excess of 2.6 GHz."* v5: *"run on 5th Generation AMD EPYC processors"* | *"CX plans can run on either Intel® or AMD. You can not choose the CPU type yourself. The hardware is automatically allocated based on availability… the CPU type (Intel® or AMD) may change during a rescale."* |

The DigitalOcean sentence about *"fractions of hyper-threads"* is the plainest admission of noisy-neighbour behaviour you will find on a hosting vendor's own site, and it is the reason a "2 vCPU" deal and another "2 vCPU" deal are not the same product. Hetzner's version is gentler but weaker: it promises a *baseline* and a *burst* and publishes neither number.

## The dedicated premium, priced out

DigitalOcean's pricing page publishes its whole size catalog, and the pattern is exact. Every bundled plan in a family costs the same amount per vCPU, because the families are linear:

| Family | CPU | $/vCPU per month | GB RAM per vCPU | $/GB RAM per month |
|---|---|---|---|---|
| **Basic** (shared) | Shared | **$12.00** (every 2 GB/vCPU size) | 2.0 | $6.00 |
| **CPU-Optimized** (`c-`) | Dedicated | **$21.00** flat | 2.0 | $10.50 |
| **General Purpose** (`g-`) | Dedicated | **$31.50** flat | 4.0 | $7.88 |
| **Memory-Optimized** (`m-`) | Dedicated | **$42.00** flat | 8.0 | $5.25 |
| **Storage-Optimized** (`so-`) | Dedicated | **$65.50** flat | 8.0 | $8.19 |

Check the linearity yourself: CPU-Optimized runs $42 (2 vCPU), $84 (4), $168 (8), $336 (16), $672 (32), $1,008 (48) — a clean $21.00 per vCPU all the way up. General Purpose runs $63, $126, $252, $504, $1,008, $1,260 — a clean $31.50. Shared Basic (at 2 GB per vCPU) runs $12, $24, $48, $96 — a clean $12.00.

**And that is where the 1.75x comes from: it is simply $21.00 ÷ $12.00.** The premium is not negotiated per size; it is baked into the two rates.

### Three sizes, sold both ways

These are the only shapes DigitalOcean sells in both flavours, and the ratios do not move:

| Shape | Shared (Basic) | Dedicated (CPU-Optimized) | Price | Disk | Transfer |
|---|---|---|---|---|---|
| **2 vCPU / 4 GB** | `s-2vcpu-4gb` — **$24.00/mo** ($0.03571/hr) | `c-2` — **$42.00/mo** ($0.0625/hr) | **+75.0%** (+$18.00/mo, +$216/yr) | 80 GB → 25 GB (**31.25%**) | 4 TB → 4 TB (same) |
| **4 vCPU / 8 GB** | `s-4vcpu-8gb` — **$48.00/mo** ($0.07143/hr) | `c-4` — **$84.00/mo** ($0.125/hr) | **+75.0%** (+$36.00/mo, +$432/yr) | 160 GB → 50 GB (**31.25%**) | 5 TB → 5 TB (same) |
| **8 vCPU / 16 GB** | `s-8vcpu-16gb` — **$96.00/mo** ($0.14286/hr) | `c-8` — **$168.00/mo** ($0.25/hr) | **+75.0%** (+$72.00/mo, +$864/yr) | 320 GB → 100 GB (**31.25%**) | 6 TB → 6 TB (same) |

Read that last row again, because it is the cleanest apples-to-apples number in this whole article: **the same 8 vCPU and 16 GB of RAM costs $96.00 a month shared and $168.00 a month dedicated, and the dedicated one arrives with 100 GB of disk instead of 320 GB.** You pay 75% more, keep the same 6 TB of transfer, and lose 68.75% of your disk. Nothing on the deal page tells you that.

There is also a ceiling worth knowing: **shared stops at 8 vCPU.** DigitalOcean's documentation gives Basic as *"1-8"* vCPU and v5 Shared as *"1-8"* with *"1-24 GB, at a 1x-3x RAM-to-vCPU ratio"*. There is no 16-vCPU shared Droplet in the catalog. If your workload outgrows 8 threads, dedicated is not a preference — it is the only way up. General Purpose starts at 2 vCPU and runs to 60.

## Hetzner: the price is close, the thread count is not

Hetzner splits its line by name, and the naming is the whole answer: **CX, CPX and CAX are shared; CCX is dedicated.** But when you put the two tables side by side, the trade-off is not the one most buyers expect.

**Shared (CPX, EU-central, excl. VAT):**

| Plan | vCPU | RAM | Disk | EUR/mo | EUR/vCPU |
|---|---|---|---|---|---|
| CPX02 | 1 | 1 GB | 20 GB | 6.49 | 6.49 |
| CPX12 | 1 | 2 GB | 40 GB | 11.99 | 11.99 |
| CPX22 | 2 | 4 GB | 80 GB | 19.99 | 10.00 |
| CPX32 | 4 | 8 GB | 160 GB | 35.99 | 9.00 |
| CPX42 | 8 | 16 GB | 320 GB | 69.99 | 8.75 |
| CPX52 | 12 | 24 GB | 480 GB | 100.99 | 8.42 |
| CPX62 | 16 | 32 GB | 640 GB | 130.49 | 8.16 |

**Dedicated (CCX, EU-central, excl. VAT):**

| Plan | vCPU | RAM | Disk | EUR/mo | EUR/vCPU |
|---|---|---|---|---|---|
| CCX13 | 2 | 8 GB | 80 GB | 43.49 | 21.75 |
| CCX23 | 4 | 16 GB | 160 GB | 86.49 | 21.62 |
| CCX33 | 8 | 32 GB | 240 GB | 138.99 | 17.37 |
| CCX43 | 16 | 64 GB | 360 GB | 276.49 | 17.28 |
| CCX53 | 32 | 128 GB | 600 GB | 533.99 | 16.69 |
| CCX63 | 48 | 192 GB | 960 GB | 853.99 | 17.79 |

Per vCPU, dedicated looks about **2x** shared — EUR 17.37 vs EUR 8.75 at 8 vCPU, for instance. But that comparison is misleading, because the two lines do not ship the same RAM per vCPU: **shared CPX is 2 GB per vCPU, dedicated CCX is 4 GB per vCPU.** Compare at equal RAM and the picture inverts:

| RAM you need | Shared option | Dedicated option | Price difference | vCPU you get |
|---|---|---|---|---|
| **8 GB** | CPX32 — 4 vCPU, **EUR 35.99** | CCX13 — 2 vCPU, **EUR 43.49** | **+20.8%** (+EUR 7.50) | 4 shared threads vs 2 dedicated threads |
| **16 GB** | CPX42 — 8 vCPU, **EUR 69.99** | CCX23 — 4 vCPU, **EUR 86.49** | **+23.6%** (+EUR 16.50) | 8 shared threads vs 4 dedicated threads |
| **32 GB** | CPX62 — 16 vCPU, **EUR 130.49** | CCX33 — 8 vCPU, **EUR 138.99** | **+6.5%** (+EUR 8.50) | 16 shared threads vs 8 dedicated threads |

**At every size, the dedicated plan costs more and gives you half as many threads — but at 32 GB the gap is only 6.5%.** That is the practical rule for Hetzner shoppers: if you are buying the machine for its RAM anyway, guaranteed threads are close to free. If you are buying it for parallel throughput, dedicated halves your thread count for a small premium, and the cheapest way to get threads is the shared line.

The entry-level gap is the other extreme: **EUR 6.49 (CPX02) to EUR 43.49 (CCX13) is a factor of 6.70**, and there is nothing in between.

### The location penalty nobody puts on the deal page

Hetzner runs a separate CPX series in its US locations, and it is not the same price for the same shape:

| Shape | EU-central | US (Hillsboro / Ashburn) | Difference |
|---|---|---|---|
| 4 vCPU / 8 GB | CPX32 — EUR 35.99 (160 GB) | CPX31 — EUR 62.99 (160 GB) | **+75.0%** |
| 8 vCPU / 16 GB | CPX42 — EUR 69.99 (320 GB) | CPX41 — EUR 120.99 (240 GB) | **+72.9%** (and 80 GB less disk) |
| 16 vCPU / 32 GB | CPX62 — EUR 130.49 (640 GB) | CPX51 — EUR 238.49 (360 GB) | **+82.8%** (and 280 GB less disk) |

The dedicated line has the same shape of penalty at a smaller magnitude: CCX63 is EUR 853.99 in EU-central and EUR 1,036.99 in Singapore (+21.4%), while the shared CPX62 is EUR 130.49 vs EUR 172.49 (+32.2%). **If you are comparison-shopping VPS deals on Hetzner, the region you pick moves the price more than the CPU class does.**

One more thing we observed while reading: every CCX plan's order button on the General Purpose page carried the notice *"This product is currently unavailable. Please check back later."* at the locations we read. Availability of the dedicated line is worth checking before you design around it.

## Why "8 vCPU" is not "8 cores"

Both hosts define a vCPU as a thread. DigitalOcean: *"a single hyper-thread on a processor core."* Hetzner, for its dedicated line: *"one vCPU equals one thread of a physical CPU core."*

That has one consequence most deal pages quietly hide. On a processor with two threads per physical core — the common configuration for server CPUs with simultaneous multithreading — **eight vCPUs is four physical cores.** Neither vendor publishes a threads-per-core figure in the pages we read, so we are not asserting a conversion for any specific plan; we are pointing out that the vendor's own definition makes the conversion *your* job, and leaves you without the number you need to do it.

The practical versions of this:

- **Licensing.** Software priced per core and software priced per thread disagree by a factor of two. If your database, control panel or hypervisor licence counts cores, a "16 vCPU" deal may cost you twice what you budgeted.
- **Benchmark comparisons.** Two reviews of "8 vCPU" plans from different hosts are comparing eight of *something*, and possibly not the same something.
- **`nproc` will not tell you.** It reports threads. Nothing in the guest reliably distinguishes a dedicated thread from a well-behaved shared one.

## How to tell what you actually bought

You do not have to trust the marketing name. Both hosts leak the answer in the plan identifier.

**DigitalOcean.** Its documentation says *"v5 size slugs begin with `g5-` for General Purpose configurations and `s5-` for Shared configurations"* — so on v5, `s5-` is shared and `g5-` is dedicated. The bundled families follow the same idea: `s-` Basic is the single shared plan (the docs say *"one shared CPU plan and four dedicated CPU plans"*), while `c-`, `g-`, `m-` and `so-` are the four dedicated ones. DigitalOcean's own recommended way to enumerate them is *"the `GET /v2/sizes` endpoint or the `doctl compute size list` command"*.

**Hetzner.** The FAQ gives the mapping directly: shared is *"(CX, CPX, CAX)"*, dedicated is *"(CCX)"*. Three letters tell you what the sales page will not.

And one asymmetry worth noting before you commit: Hetzner lets you move between the two — *"you can also rescale to and from a plan with shared resources"* — while DigitalOcean's documented constraint runs the other way (v5 configurations and bundled plans cannot be resized into each other, and disk can only grow). If you think you might change your mind, that difference matters more than the monthly price.

## Where shared actually hurts — and where it doesn't

DigitalOcean's own guidance is unusually honest about the boundary:

- Buy shared when *"your Droplet has low to moderate CPU or memory usage most of the time but sometimes bursts up and hits resource limits."*
- Buy dedicated when *"production workloads where time is of the essence or variable performance is intolerable."*
- Hetzner's equivalent: shared for *"personal websites and blogs, small databases, or web servers with low to moderate traffic"*; dedicated for *"business applications with high production workloads, such as high-traffic websites, large databases, gaming servers, machine learning, or processing large volumes of data."*

There is also a resource that moves with the CPU class and is easy to miss. On DigitalOcean v5, shared configurations get **2 Gbps** of network throughput, while General Purpose scales from **4 Gbps at 2 vCPU up to 50 Gbps at 64 vCPU**. If your deal is bandwidth-bound rather than CPU-bound, the shared tier caps your network at one figure regardless of size.

And the reverse case, which the numbers make plain: **if the RAM is what you are buying, dedicated can be the cheaper way to get it.** Memory-Optimized dedicated costs $42.00 per vCPU but carries 8 GB of RAM per vCPU — **$5.25 per GB of RAM**, cheaper per gigabyte than any other DigitalOcean family, shared or dedicated. You are paying for threads you may not use to get RAM you do.

## What we could not verify

We do not fill gaps with numbers from other sites. These are the ones that stayed open on 2026-11-03:

- **Hetzner's baseline and burst figures for shared plans.** The FAQ promises *"a baseline CPU performance"* and *"the option to temporarily burst CPU usage above the baseline level"* and publishes neither number. Not verifiable.
- **DigitalOcean's burst ceiling, and how many Droplets share a host.** The documentation describes the mechanism (*"the hypervisor dynamically allocates more hyper-thread(s)"*) but gives no ceiling, no baseline and no host density. Not verifiable.
- **Threads per physical core at either host.** Not published in any page we could read. Any "8 vCPU = 4 cores" arithmetic is yours to make, not the vendor's claim.
- **Vultr, Linode (Akamai) and Liquid Web.** Their product and pricing pages returned **403** to our direct requests on 2026-11-03. That is an access-control response, not a dead link; we do not use proxies or alternate user agents to get around it, so we publish nothing about their shared/dedicated split.
- **Hostinger's CPU claim.** Its page is readable and states *"you will get dedicated resources, such as CPU power, RAM, or disk space"* — a blanket claim covering every plan, with no shared tier, no thread definition and no vCPU-per-core statement. The same page's FAQ lists *"KVM 1 – $6.49/month KVM 2 – $8.79/month KVM 4 – $12.99/month KVM 8 – $25.99/month"* while the plan cards on the same page show $19.49 / $24.49 / $42.99 / $73.99; the page does not label which is promotional and which is renewal in the markup we could read, so we quote both and use neither in any calculation.
- **Whether Hetzner's dedicated CCX line is currently orderable.** Every plan's create button carried *"This product is currently unavailable. Please check back later."* at the locations we read. We report the notice as observed; we do not know its scope or duration.

## What to do with this when you're shopping a VPS deal

1. **Translate the vCPU count first.** Both hosts that define the term define it as a thread. Ask the vendor how many threads per core, or assume you are buying half the cores you think.
2. **Compare at equal RAM, not equal vCPU.** At Hetzner that is the difference between "dedicated costs 2x" and "dedicated costs 6.5% more and halves your threads". At DigitalOcean the RAM ratio is fixed per family (2 GB/vCPU on shared Basic and CPU-Optimized, 4 GB on General Purpose, 8 GB on Memory- and Storage-Optimized), so pick the family by the ratio you need before you look at the price.
3. **Budget the 75% if you need guaranteed threads at DigitalOcean.** It is a flat rate: $12.00 per shared vCPU per month becomes $21.00 dedicated. Check whether you also need the disk you are giving up — the dedicated shape ships 31.25% of it.
4. **Check the region before the CPU class at Hetzner.** The same 8 vCPU/16 GB shared server is EUR 69.99 in EU-central and EUR 120.99 in the US. That is a bigger swing than shared-vs-dedicated at that size.
5. **Remember the shared ceiling.** DigitalOcean's shared line stops at 8 vCPU; Hetzner's stops at 16. Past that, dedicated is not an upgrade, it is the only option.
6. **Look at the slug, not the label.** `s-`/`s5-` and `CX`/`CPX`/`CAX` mean shared. `c-`/`g-`/`m-`/`so-`/`g5-` and `CCX` mean dedicated.
7. **If RAM is the real requirement, price it per gigabyte.** DigitalOcean's Memory-Optimized dedicated line is the cheapest RAM per GB in the catalog at $5.25/GB, despite being the second most expensive per vCPU.

If you remember one sentence: **the word "vCPU" is not a unit anyone has standardised, the two hosts that define it define it as a thread, and "dedicated" is priced as a flat 75% premium at DigitalOcean and as half your thread count at Hetzner.**

## Method and sources

All quotations and figures were read from the pages below on **2026-11-03**, with no proxy, no user-agent spoofing and no attempt to bypass any access control. Per-vCPU and per-GB figures are arithmetic on the list prices those pages publish; percentages are ratios of those same list prices. Prices are list prices in the currency the vendor prints them in — **EUR and USD are never converted into one another in this article.** Where a page was unreachable or silent, this article says so instead of filling the gap.

- DigitalOcean, *Choosing the Right CPU Droplet Plan* (page states `last_updated: "2026-10-01"`) — vCPU definition, shared vs dedicated mechanics, plan families, v5 ranges, slug prefixes — https://docs.digitalocean.com/products/droplets/concepts/choosing-a-plan/
- DigitalOcean, *Droplet Pricing* (`last_updated: "2026-10-26"`) — points to the published size catalog and describes per-resource v5 billing — https://docs.digitalocean.com/products/droplets/details/pricing/
- DigitalOcean, CPU Droplet pricing page — the size catalog every dollar figure in this article is computed from (read 2026-11-03) — https://www.digitalocean.com/pricing/droplets
- DigitalOcean, API `GET /v2/sizes` reference — the documented way to enumerate size slugs — https://docs.digitalocean.com/reference/api/reference/sizes/
- Hetzner, *Cloud Servers FAQ* (ID CL-BD8DE, *"Last change on 2024-09-12"*) — shared vs dedicated definitions, CX/CPX/CAX vs CCX mapping, rescale behaviour, CPU type assignment — https://docs.hetzner.com/cloud/servers/faq/
- Hetzner, Cloud overview — shared vs dedicated product positioning — https://www.hetzner.com/cloud/
- Hetzner, *Regular Performance* (shared CPX line) — CPX plan table, EU/US/AP prices — https://www.hetzner.com/cloud/regular-performance/
- Hetzner, *General Purpose* (dedicated CCX line) — CCX plan table, EU/US/AP prices, availability notice — https://www.hetzner.com/cloud/general-purpose/
- Hostinger, VPS Hosting (readable 2026-11-03; blanket "dedicated resources" claim, no shared/dedicated split published) — https://www.hostinger.com/vps-hosting
- Vultr, Cloud Compute (returned 403 on 2026-11-03; nothing quoted) — https://www.vultr.com/products/cloud-compute/
- Linode / Akamai, Shared CPU plans (returned 403 on 2026-11-03; nothing quoted) — https://www.linode.com/products/shared/
- Liquid Web, VPS Packages & Bundles (returned 403 on 2026-11-03; nothing quoted) — https://www.liquidweb.com/vps-hosting/packages/
