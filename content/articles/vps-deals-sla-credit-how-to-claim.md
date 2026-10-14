---
title: "Cheap VPS Deals and SLA Credits: What You Actually Get Paid When the Server Goes Down"
slug: vps-deals-sla-credit-how-to-claim
date: 2026-10-14
description: "Read off providers' own pages on 2026-10-14: DigitalOcean's CPU Droplet SLA has exactly one tier — below 99.99% it pays 100% of the affected Droplet's monthly charge, and the trigger is about four minutes of downtime. Hetzner publishes 99.9% annual network availability with no credit at all, Hostinger's VPS terms say the uptime guarantee applies 'if any', and Namecheap bills $10.00 to bring a failed server back online."
question: If my cheap VPS goes down, how much money do I actually get back, and how do I claim it?
sources:
  - https://www.digitalocean.com/sla/cpu-droplets
  - https://www.digitalocean.com/sla/gpu-droplets
  - https://www.digitalocean.com/sla/volumes
  - https://www.digitalocean.com/sla/doks
  - https://www.digitalocean.com/legal/terms-of-service-agreement
  - https://www.digitalocean.com/pricing/droplets
  - https://www.hetzner.com/legal/terms-and-conditions/
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.namecheap.com/hosting/vps/
  - https://www.liquidweb.com/wordpress-hosting/vps-wordpress/
---

**Read off the providers' own pages on 2026-10-14, the answer for the four VPS brands that dominate cheap deals is: DigitalOcean pays 100% of the affected Droplet's monthly charge the moment a single Droplet misses 99.99% in a month — a threshold of roughly four minutes — but you have to email `success@digitalocean.com` yourself within two billing cycles and the money arrives as non-refundable credit. Hetzner publishes 99.9% and pays nothing. Hostinger's VPS contract says the uptime guarantee applies "if any". Namecheap prints 99.9% on its plan table and charges $10.00 to restore a failed server.** The percentages you see in marketing are the easy part; the payout mechanism is where the four diverge completely.

## DigitalOcean's VPS SLA has one row, not a ladder

The [DigitalOcean CPU Droplet SLA](https://www.digitalocean.com/sla/cpu-droplets) (last updated June 3, 2025) commits to "a Monthly Uptime Percentage of 99.99% for each individual Droplet instance" and — this is the part nobody quotes — its service credit table contains exactly one line:

> less than 99.99% → 100%

That is the whole table. Not 10%, not 25%, not a sliding scale. Compare it with DigitalOcean's own other SLAs, read the same day: the [GPU Droplet SLA](https://www.digitalocean.com/sla/gpu-droplets) (last updated October 21, 2025) commits to only **99%** and pays 10% / 25% / 50% in three tiers, capping at 50%. The [DOKS SLA](https://www.digitalocean.com/sla/doks) commits to 99.95% and pays 10% / 25% / 100%. So the cheapest product has the tightest target *and* the most generous payout — and the one product where a breach is easiest to prove.

Two more structural points hide in the definitions. The credit applies **per Droplet**: "Service Credits apply only to charges incurred for the specific Droplet resources affected." And credits are "credited towards future invoices", are "non-refundable", and are issued "within one billing cycle" of verification.

## The trigger is about four minutes — and the payout is the same for five minutes as for thirty days

The SLA defines Monthly Uptime Percentage as `(Total minutes in the month - Minutes of Unavailability) / Total minutes in the month`. So the downtime you are allowed before the 99.99% line breaks is 0.01% of the month:

| Month length | Total minutes | Downtime allowed at 99.99% |
|---|---|---|
| 28 days (February, non-leap) | 40,320 | **4 min 1.9 s** |
| 29 days | 41,760 | **4 min 10.6 s** |
| 30 days | 43,200 | **4 min 19.2 s** |
| 31 days | 44,640 | **4 min 27.8 s** |

Your allowance moves with the calendar — you get 25.9 seconds more downtime in a 31-month than in a February — but in every case it rounds to **four whole minutes**. Counted in whole minutes, the fifth minute of unavailability in a month is what flips you from $0 to 100%.

Because the payout is binary rather than proportional, the arithmetic gets strange. Take DigitalOcean's cheapest Basic Droplet, **$0.00595/hr and $4.00/mo** (512 MiB / 1 vCPU / 10 GiB / 500 GiB transfer, read from [the pricing page](https://www.digitalocean.com/pricing/droplets) today). Its proportional value per minute of downtime is $4.00 ÷ 43,200 = $0.0000926. Now compare what the SLA actually pays:

| Outage length in a 30-day month | Proportional value | What the SLA pays | Multiple |
|---|---|---|---|
| 4 minutes (inside the allowance) | $0.00037 | **$0** | 0x |
| 5 minutes | $0.00046 | **$4.00** | 8,640x |
| 1 hour | $0.00556 | **$4.00** | 720x |
| 24 hours | $0.13333 | **$4.00** | 30x |
| Full month | $4.00 | **$4.00** | 1x |

The multiple is simply 43,200 ÷ minutes of downtime, capped at the month's charge. **A five-minute outage and a thirty-day outage pay the identical $4.00.** There is no incentive in the contract for DigitalOcean to restore you quickly once the line has been crossed, and no extra compensation for you if it doesn't.

## The "100%" is 100% of one Droplet, not of your bill

Because the SLA "applies separately to each Droplet you use", the percentage you recover depends on how much of your fleet broke. Take ten 1 GiB Basic Droplets at $6.00/mo each — a $60.00/mo fleet:

| Incident | Machine-minutes lost | Credit | Share of the $60 bill |
|---|---|---|---|
| 1 Droplet down the whole month | 43,200 | **$6.00** | 10.0% |
| 2 Droplets down the whole month | 86,400 | **$12.00** | 20.0% |
| All 10 Droplets down 3 minutes each | 30 | **$0.00** | 0% |
| 1 Droplet down 5 minutes | 5 | **$6.00** | 10.0% |
| All 10 Droplets down 5 minutes each | 50 | **$60.00** | 100% |

Read the third and fourth rows together. **Ten Droplets each losing three minutes costs you 30 machine-minutes and pays $0. One Droplet losing five minutes costs you 5 machine-minutes and pays $6.00.** The worse incident, by any operational measure, is the one that pays nothing. If your load balancer returns errors during those three-minute blips, your users saw an outage and your SLA saw a perfect month.

## How to file, and the deadline that differs per product

For CPU Droplets the SLA says: "To request a Service Credit, contact DigitalOcean at success @digitalocean .com within two (2) billing cycles of the month when the downtime occurred. Include the email address associated with your account, affected Droplet resource details, and outage dates/times."

That is an email address, not a form, not a ticket, and not an automatic adjustment. **Nothing happens unless you notice, document and write.** And the deadline is not the same across the products on the same account:

| DigitalOcean product | Uptime target | Credit shape | Deadline to claim | Extra conditions |
|---|---|---|---|---|
| CPU Droplets | 99.99% monthly | 100% of affected Droplet | **2 billing cycles**, by email | Non-refundable; toward future invoices |
| Volumes Block Storage | 99.99% monthly | "100% of lost time at the hourly rate incurred" | **3 months** | Unavailability = all requests fail for **more than 5 minutes** |
| DOKS (HA control plane) | 99.95% monthly | 10% / 25% / 100% | **3 months** | Worker nodes covered by the Droplet SLA instead |
| GPU Droplets | **99%** monthly | 10% / 25% / **50% max** | **Notify within 24 hours** or forfeit; claim within 3 months | Credits **expire after 90 days**; none issued if the amount is **≤ $1** |

The GPU row is worth staring at: 99% monthly means 1% of a 30-day month is allowed — 432 minutes, or **7 h 12 min**, which is 100x the CPU allowance — and yet you must give written notice within 24 hours of the downtime starting or you lose the claim entirely. On one account, a GPU Droplet claim can be time-barred in a day while a CPU Droplet claim has roughly two months.

Two clauses in the [DigitalOcean Terms of Service](https://www.digitalocean.com/legal/terms-of-service-agreement) sit above all four. §6.5: "all credits, whether previously offered or otherwise, are revocable or subject to early expiration at any time and for any reason or no reason by us." §8.3: "The Service Level Agreements do not apply to Beta Services." The credit you earned is discretionary, and it does not exist at all on anything labelled beta or preview.

Finally, what counts. "Unavailability" is defined as loss of connectivity over the Droplet's public, reserved or private IP **due to the failure of DigitalOcean infrastructure**, or loss of read/write access to the root disk. And the exclusion list removes scheduled maintenance, customer-initiated downtime, "issues arising from customer application code or configuration errors", account restrictions and force majeure. **A Droplet that is up but slow, or dropping half its packets, is not "unavailable" under this definition** — the word is *loss*, not degradation.

## What the other three actually publish

**Hetzner** — §3.3 of its [Terms and Conditions](https://www.hetzner.com/legal/terms-and-conditions/) reads: *"We undertake to make economically reasonable efforts to achieve an annual average network availability of 99.9% at our data centers."* Three things matter here. It is an **endeavour**, not a commitment. It is **annual**, so a single catastrophic month can be averaged away against eleven quiet ones. And it is **network availability at the data centres** — not your cloud server. Over a year, 0.1% of 525,600 minutes is **8 h 45 min 36 s** of permitted downtime against DigitalOcean's 0.01% monthly, which works out to 52 min 34 s per year — exactly 10x tighter. Hetzner's T&C contains no service credit table at all.

**Hostinger** — §5 of the [Universal Terms of Service Agreement](https://www.hostinger.com/legal/universal-terms-of-service-agreement) that governs its VPS plans says: *"The service uptime guarantee applicable to specific Services, if any, is defined in other documents (e.g., specific Service agreement)... You acknowledge and agree that we assume no liability to you or any other party with regard thereto."* The contract you click through contains **no uptime number**. The guarantee is contingent — "if any" — and any liability is disclaimed in the same sentence.

**Namecheap** — its [VPS page](https://www.namecheap.com/hosting/vps/) does print a number: the spec table lists **Uptime 99.9%** for all five plans, glossed as "the monthly measurement of your server's accessibility to the Internet". At 99.9% monthly, a 30-day month permits 43 min 12 s of downtime. The page publishes no credit mechanism, no claim process and no SLA link. What it does publish is a price pointing the other way: under Complete management, *"Restore server failure — If the server fails, our Tech Support will bring the server back online"* is listed at **$10.00 flat rate per restore**, with *"Fix server failure cause"* at **$10.00 per hour**. On a Spark plan billed at **$46.56/year**, one restore is **21.5%** of a year's hosting cost. The only published money remedy on the page is a 30-day money-back guarantee, which expires 30 days after purchase and never applies to month nine.

**Liquid Web** — its [WordPress VPS page](https://www.liquidweb.com/wordpress-hosting/vps-wordpress/) carries the boldest number of the four: *"Uptime SLA — We guarantee your network and power are available 100% of the time."* Read the scope: **network and power**, not your VPS, not your database, not your application. No credit, no claim process and no remedy appears anywhere on that page or on the VPS packages page (which today shows an 8 GB plan at $150.30/mo with "10% OFF", and up to 42%/45% off for 1- and 2-year terms, and mentions uptime nowhere).

## What we could not verify today, and why we did not fill it in

We do not bypass bot protection and we do not estimate unreadable numbers, so these are stated as unread rather than guessed:

- **Vultr** — `vultr.com/legal/sla/` returned 403 to a direct request. No SLA read.
- **Namecheap legal** — `namecheap.com/legal/hosting/service-level-agreement/` returned 403. The 99.9% above comes from its public VPS plan table only; we could not read a credit clause.
- **Liquid Web legal** — both `liquidweb.com/legal/service-level-agreement/` and `liquidweb.com/about/legal/service-level-agreement/` returned 403. The 100% statement above is marketing copy from a product page, not the SLA document.
- **Hetzner SLA** — `hetzner.com/legal/service-level-agreement/` returns a legal-notice shell with no SLA text. The 99.9% figure above is from the general T&C, §3.3.
- **Hostinger** — `hostinger.com/legal/service-level-agreement` returned 404. There is no public SLA page to read; §5 of the universal terms is the only uptime language we could reach.
- **DigitalOcean** — `docs.digitalocean.com/support/how-do-i-request-an-sla-credit/` returned 404. There is no support article for the claim process; the `/sla/cpu-droplets` page is the only source, and note that `digitalocean.com/sla` is an index of **14 separate SLAs** — there is no single "DigitalOcean SLA" to point at.

## What to do, in order

1. **Instrument before you need it.** Every credit mechanism above is claim-driven. If you cannot produce dates and times per affected resource, you have nothing to send. A 1-minute-interval external ping to each VPS costs nothing and is the entire difference between $0 and 100%.
2. **Know your trigger.** On DigitalOcean CPU Droplets it is the fifth minute of unavailability in a calendar month. On Volumes it is five minutes of *complete* request failure. On Hetzner and Hostinger there is no trigger, because there is no payout.
3. **File inside the shortest deadline you have.** Two billing cycles for CPU Droplets; three months for Volumes and DOKS; **24 hours** for GPU Droplets. Put the deadline in your calendar the day an incident ends, not the day you get around to it.
4. **Calculate the claim before you send it.** Credit = (monthly charge of the affected Droplets only) × (credit tier). On a ten-node fleet with one node down, expect 10% of the bill, not 100%.
5. **Treat credits as store credit, not compensation.** DigitalOcean's are non-refundable and future-only, revocable under §6.5, and GPU credits expire in 90 days. Budget as if the payout were zero and the SLA is a signal about reliability, not an insurance policy.
6. **When comparing VPS deals, compare the mechanism, not the number.** 99.99% monthly with a binary 100% payout (DigitalOcean) and 99.9% annual with no payout (Hetzner) are not two similar products with slightly different decimals. They are, respectively, a claim you can file for $4.00 and a claim you cannot file at all.
