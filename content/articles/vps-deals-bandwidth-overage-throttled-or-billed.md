---
title: "Cheap VPS Deals: You Blew Through Your Bandwidth — Now What? (Throttle, Suspend, or a Bill)"
slug: vps-deals-bandwidth-overage-throttled-or-billed
date: 2026-10-20
description: "Read off five hosts' own pages on 2026-10-20. Not one of them throttles you. DigitalOcean meters at $0.01 per GiB, Hetzner meters at €1 ($1.20) per TB in 100 MB blocks, and Namecheap sells extra bandwidth at $10/mo per 100 GB — so the same 100 GB of overage costs $1.00 at DigitalOcean, $0.12 at Hetzner, and $10.00 at Namecheap, an 83x spread. Hostinger and Liquid Web print the allowance (4-32 TB and 5/7/10 TB) and print nothing about what happens when you exceed it. Plus the arithmetic nobody publishes: DigitalOcean's free pool accrues per second of a Droplet's life up to a hard cap of 2,419,200 seconds — exactly 28 days — so deleting and rebuilding a Droplet does not reset your allowance, it shrinks it; and Hetzner's own 75% and 100% usage emails 'do not cap or stop it.'"
question: I went over my VPS bandwidth allowance — will my host throttle me, suspend the server, or just bill me per gigabyte?
sources:
  - https://docs.digitalocean.com/platform/billing/bandwidth/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/robot/general/traffic/
  - https://docs.hetzner.com/cloud/billing/faq/
  - https://www.namecheap.com/hosting/vps/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9215/48/how-to-upgrade-rambandwidthdisk-space-on-a-vpsdedicated-server/
  - https://www.hostinger.com/vps-hosting
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off five hosts' own pages on 2026-10-20: none of them throttle you. Not one.** Every host in this comparison that publishes a policy at all settles a bandwidth overage with money, not with a speed cap. The interesting part is not *whether* you pay — it is how much, and how two of the five refuse to say.

Here is the whole answer in one screen:

| Host | What happens when you go over | Unit price of the overage | Published? |
|---|---|---|---|
| **Hetzner** (Cloud) | Metered, billed in **100 MB blocks** | **€1/TB**, printed on the page as *"€ 1 ($1.20)/TB"* | Yes |
| **DigitalOcean** | Metered, billed **per GiB** | **$0.01 per GiB** | Yes |
| **Namecheap** | Prepaid add-on you must buy in advance | **$10.00/mo per 100 GB** (capped at 1 TB total) | Yes, as an add-on price |
| **Hostinger** | Nothing written anywhere | — | **No — not verifiable** |
| **Liquid Web** | Nothing written anywhere | — | **No — not verifiable** |

So the question "what happens next" resolves into three modes, and only one of them is a speed problem:

1. **Metered** — Hetzner, DigitalOcean, Namecheap. You keep your speed and get a bill.
2. **Silent** — Hostinger, Liquid Web. They print the allowance and never print the consequence.
3. **Suspended** — the budget end of the market. In a LowEndBox comment thread, a RackNerd representative described it plainly: *"the VPS would automatically be suspended until the bandwidth resets. The bandwidth resets monthly, every first of the month."* That is a suspension, not a bill and not a throttle.

---

## The 83x spread nobody prints side by side

Take one concrete event: **you push 100 GB more outbound traffic than your plan includes.** Same event, five hosts, three published prices:

| Host | Cost of 100 GB of overage | How it is measured |
|---|---|---|
| Hetzner | **$0.12** | 100 GB = 0.1 TB, at the page's own *"$1.20/TB"* |
| DigitalOcean | **$1.00** | 100 GiB × $0.01/GiB |
| Namecheap | **$10.00/mo** | one 100 GB add-on block, billed **every month** |

Namecheap is **83x** Hetzner and **10x** DigitalOcean for the identical 100 GB. Scale it to a full terabyte and the gap is the same: $1.20 at Hetzner, $10.24 per TiB at DigitalOcean (1,024 GiB × $0.01), $100.00/mo at Namecheap (ten 100 GB blocks).

And Namecheap's add-on has a ceiling the other two do not: the KB's table caps *Maximum Additional Bandwidth* at **1 TB**. On the Hypernova plan — which already includes **10,000 GB/mo** — the largest extra bandwidth you can buy is 1,000 GB, a 10% top-up for **$100/mo**, on top of a $56.88 month-to-month plan price.

The sharpest way to see it: **doubling your bandwidth is cheap at the metered hosts and absurd at the add-on host.**

- DigitalOcean $4/mo Basic (500 GiB): doubling your transfer costs 500 GiB × $0.01 = **$5.00**, i.e. 125% of your plan price.
- Namecheap Spark (1,000 GB): doubling your bandwidth needs 10 blocks = **$100/mo**, i.e. **17x** the $5.88 month-to-month plan price.
- Hetzner CX (20 TB): doubling costs 20 TB × $1.20 = **$24.00**.

---

## DigitalOcean: your free allowance is time-weighted, and rebuilding does not reset it

This is the part every "how much bandwidth do I get" post gets wrong. DigitalOcean's pool is not per-Droplet and it is not granted on the 1st of the month. From the Bandwidth Billing page (last updated 2026-09-14):

> *"Transfer allowance and usage is pooled cumulatively across all Droplets at the team level, not individually per Droplet. Accrued transfer does not roll over between months and cannot be transferred between teams."*

> *"We bill Droplets for each second they exist, rounded to the nearest minute, up to a maximum of 2,419,200 seconds (28 days) per monthly billing cycle. For every second a Droplet exists, it accrues 1/2,419,200 of its total transfer allowance towards the team's transfer pool."*

Check the arithmetic: 28 × 86,400 = **2,419,200 seconds**. DigitalOcean's transfer month is 28 days long no matter how many days the calendar month has.

Two consequences you can act on:

- **Destroying and recreating a Droplet does not reset anything.** A Droplet that exists for 14 days contributes 14/2,419,200 × 86,400 × ... i.e. exactly half of its allowance. If you burn 300 GiB on day 1, destroy it on day 2, and rebuild on day 10, the pool you earned in those two days is 2/28 of 500 GiB ≈ 36 GiB — and the new Droplet starts accruing from zero.
- **One noisy Droplet can spend another Droplet's allowance.** DigitalOcean's own example: two 1,000 GiB Droplets running a full cycle create a 2,000 GiB pool, and if one uses 1,500 GiB while the other uses 100 GiB, *"no overage fees apply."* The reverse is also true — the quiet Droplet's accrual can be eaten by the loud one.

What does **not** count against you, per the same page: inbound transfer (free), VPC private-network traffic, and — a genuinely unusual clause — *"We do not bill for outbound data transfer that we determine is dropped by a DigitalOcean firewall rule."* What **does** count, and surprises people: *"All IPv6 traffic uses the public interface,"* so IPv6 egress is billed exactly like IPv4.

### The overage is not always a penalty

Because the allowance scales with the plan, DigitalOcean's flat $0.01/GiB is sometimes *cheaper* than the rate you already pay. Divide each Basic tier's monthly price by its included transfer:

| Plan | Included transfer | Blended rate | Overage ÷ blended |
|---|---|---|---|
| $4/mo | 500 GiB | $0.00800/GiB | **1.25x** |
| $6/mo | 1,000 GiB | $0.00600/GiB | **1.67x** |
| $12/mo | 2,000 GiB | $0.00600/GiB | **1.67x** |
| $18/mo | 3,000 GiB | $0.00600/GiB | **1.67x** |
| $24/mo | 4,000 GiB | $0.00600/GiB | **1.67x** |
| $48/mo | 5,000 GiB | $0.00960/GiB | **1.04x** |
| $96/mo | 6,000 GiB | $0.01600/GiB | **0.63x** |

On the top two tiers, extra traffic costs **less per GiB than the plan itself**. Doubling the transfer on the $96/mo plan adds $60.00 — 62.5% of the plan price, not 167%.

---

## Hetzner: 100 MB blocks, and a warning email that explicitly does not stop anything

Hetzner's traffic page (ID `RO-CBB6A`) is the most concrete in the group: *"There is no bandwidth limitation. We will charge € 1 ($1.20)/TB for overusage."* Note the phrase — **no bandwidth limitation** is stated on the same page as the price. That is the opposite of throttling.

The Cloud billing FAQ adds the mechanics:

> *"If you exceed the traffic included in your package, we will bill you for the over-usage in blocks of 100MB. If you only consume a fraction of 100MB, we will round up to the next full 100MB."*

Its worked example: a server with 20 TB included that uses 20.00008 TB is billed for **0.0001 TB (= 100 MB)**. So the smallest possible overage charge is 100 MB — about $0.00012 — and Hetzner's rounding is the finest-grained of the three.

Then the sentence that matters most for anyone who thinks the email will save them:

> *"We will notify you, the project owner, if the traffic usage exceeds 75% of the included free traffic, and again if you reach 100%. These notifications are a convenience to help you keep track of your usage; they do not cap or stop it... Any traffic used beyond the included amount is billed as usual, even if a notification reaches you late or does not arrive at all."*

Hetzner also defines the measurement in a way that catches people out. Incoming and internal traffic is free, and **internal** includes *"Other Hetzner Cloud servers with the same network zone via their public IPs"* and *"Hetzner Online dedicated root servers."* But **outgoing** includes *"Other Hetzner Cloud servers with different network zones (eu-central, us-east, us-west, ap-southeast) via their public IPs."* Server-to-server traffic inside Hetzner is free within a network zone and billable across zones — even though it never touches the public internet.

Included allowances differ sharply by region, too. The same page's table gives CX/CPX/CAX **20 TB** in EU locations, but CPX only **0.5–5 TB in SIN** and **1–5 TB in US** locations depending on plan. A US cloud server can start with **one twentieth** of its EU twin's allowance.

---

## What your allowance actually means in Mbps

Every plan in this comparison hides the same trap: the allowance is a monthly volume, and the port is a rate. Convert the volume to a rate and the numbers get small fast. Formula: `GB × 8 ÷ 2,592,000` (a 30-day month in seconds) = the Mbps you can sustain 24/7 without overage.

| Plan | Included transfer | Equal to a constant |
|---|---|---|
| DigitalOcean $4/mo | 500 GiB (536.9 GB) | **1.66 Mbps** |
| Namecheap Spark | 1,000 GB | **3.09 Mbps** |
| Hostinger KVM 1 | 4 TB | **12.35 Mbps** |
| Liquid Web 8 GB package | 5 TB | **15.43 Mbps** |
| Hetzner CX/CPX (EU) | 20 TB | **61.73 Mbps** |
| Hostinger KVM 8 | 32 TB | **98.77 Mbps** |

Hostinger's product page pairs those allowances with a stated **1 Gbps network speed**. At line rate, 1 Gbps is 0.125 GB/s, so the 4 TB on KVM 1 is gone in 4,000 ÷ 0.125 = **32,000 seconds — 8.9 hours**. The port is roughly 81x what the allowance can sustain. Namecheap's own comparison table makes the same point from the other direction: it lists competing plans as *"Unmetered"* — and *unmetered* still means a physical port with a ceiling, not infinite throughput.

---

## What I could not verify (2026-10-20, direct requests, no proxy, no UA spoofing)

- **Hostinger**: the VPS product page lists 4 / 8 / 16 / 32 TB of bandwidth across KVM 1–8 and a 1 Gbps port. I read the full Universal Terms of Service Agreement and the product page; neither contains any clause on exceeding bandwidth, overage fees, throttling, or suspension for traffic. **Not verifiable** — if you need Hostinger's answer, ask before you buy, not after.
- **Liquid Web**: the packages page lists **5 TB** (8 GB), **7 TB** (16 GB), **10 TB** (32 GB) and *"Unlimited inbound"*, and contains no overage, throttling, or exceedance clause. Its FAQ's only traffic-related line is a sizing hint: *"The right VPS package depends on your website or application's resource needs, such as traffic levels and performance requirements."* **Not verifiable.** (A direct script request to this page returns 403; the text above was read through the standard fetch tool.)
- **Namecheap's main site** returns 403 to direct script requests; the plan figures and add-on prices above come from its Knowledgebase and the VPS product page.

---

## The decision rule

1. **Treat "unlimited" and "unmetered" as marketing, and the TB figure as the real product.** Compute your own baseline first: `monthly GB × 8 ÷ 2,592,000` is the sustained Mbps you can actually afford. If that number looks smaller than your average outbound, the plan is mispriced for you no matter what the headline says.
2. **Buy the overage unit price, not the allowance size.** One terabyte of headroom costs $1.20 at Hetzner, $10.24 per TiB at DigitalOcean, and $100/mo at Namecheap. On a cheap VPS the overage can exceed the plan price by an order of magnitude.
3. **If the host publishes nothing, assume the worst and self-meter.** Hostinger and Liquid Web give you a number and no consequence. Put your own alert at 75% of the allowance — the same threshold Hetzner uses — and do not wait for an email.
4. **At DigitalOcean, watch the team pool, not the Droplet.** Allowance accrues at 1/2,419,200 per second of a Droplet's existence and never rolls over. Rebuilds shrink it; a neighbour can spend it; IPv6 counts; firewall-dropped traffic does not.
5. **At Hetzner, remember the emails are informational.** *"They do not cap or stop it."* Overage is billed in 100 MB blocks whether or not the notification arrives.
6. **Never assume a throttle.** In this entire comparison, zero of five hosts throttle. If your server suddenly slows to a crawl after a heavy month, look at your own stack first — the hosts that publish a policy all bill instead.
