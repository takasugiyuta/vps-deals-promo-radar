---
title: What a VPS Deal Actually Costs Per GB of RAM
slug: vps-deals-cost-per-gb-ram
date: 2026-10-09
description: We divided the posted price by the RAM on every plan card three major hosts publish. The spread runs from $1.62 to $9.00 per GB — and one plan inside a single provider's own line costs 50% more per GB than the bigger plan directly above it.
question: How much am I really paying per GB of RAM on a VPS deal, and which plans are quietly the worst value in their own lineup?
sources:
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/hosting/vps/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/cloud/billing/faq/
---

Every VPS deal page prints a monthly price. None of them print the price of what you are actually buying. Divide the posted price by the RAM on the card and the same three hosts — read from their own pricing pages on 2026-10-09 — span **$1.62 to $9.00 per GB**, a 5.5x spread on a commodity. Worse: **DigitalOcean sells a 2 GB / 2 vCPU Droplet at $9.00 per GB, while the 4 GB / 2 vCPU directly above it costs $6.00 per GB.** Same CPU count, double the memory, better rate. The smaller plan is strictly worse value than the one above it.

## The table: price divided by RAM

| Provider | Plan | Posted /mo | RAM | vCPU | **$/GB RAM** | $/vCPU |
|---|---|---|---|---|---|---|
| Hostinger | KVM 1 | $6.49 | 4 GB | 1 | **$1.62** | $6.49 |
| Hostinger | KVM 2 | $8.99 | 8 GB | 2 | **$1.12** | $4.50 |
| Hostinger | KVM 4 | $12.99 | 16 GB | 4 | **$0.81** | $3.25 |
| Hostinger | KVM 8 | $25.99 | 32 GB | 8 | **$0.81** | $3.25 |
| Namecheap | Spark | $3.88 | 1 GB | 1 | **$3.88** | $3.88 |
| Namecheap | Pulsar | $6.88 | 2 GB | 2 | **$3.44** | $3.44 |
| Namecheap | Quasar | $12.88 | 6 GB | 4 | **$2.15** | $3.22 |
| Namecheap | Magnetar | $24.88 | 12 GB | 8 | **$2.07** | $3.11 |
| Namecheap | Hypernova | $46.88 | 24 GB | 12 | **$1.95** | $3.91 |
| DigitalOcean | Basic 512 MiB | $4.00 | 0.5 GB | 1 | **$8.00** | $4.00 |
| DigitalOcean | Basic 1 GiB | $6.00 | 1 GB | 1 | **$6.00** | $6.00 |
| DigitalOcean | Basic 2 GiB | $12.00 | 2 GB | 1 | **$6.00** | $12.00 |
| DigitalOcean | Basic 2 GiB / 2 vCPU | $18.00 | 2 GB | 2 | **$9.00** | $9.00 |
| DigitalOcean | Basic 4 GiB | $24.00 | 4 GB | 2 | **$6.00** | $12.00 |
| DigitalOcean | Basic 8 GiB | $48.00 | 8 GB | 4 | **$6.00** | $12.00 |
| DigitalOcean | Basic 16 GiB | $96.00 | 16 GB | 8 | **$6.00** | $12.00 |

Read the billing basis before you compare: Hostinger's posted rate is the **total for the initial term divided by the months in it**, and its cards print the renewal rate separately. Namecheap's posted rate is the **yearly-billed monthly equivalent**. DigitalOcean posts a straight monthly list rate. These are not the same kind of number, and that is the point — the deal pages put them side by side as if they were.

## The renewal rate is where the unit price breaks

Hostinger prints both numbers, so you can watch the per-GB rate move:

| Plan | Promotional $/GB | Renewal $/GB | Jump |
|---|---|---|---|
| KVM 1 | $1.62 | $3.00 | **1.85x** |
| KVM 2 | $1.12 | $1.87 | **1.67x** |
| KVM 4 | $0.81 | $1.81 | **2.23x** |
| KVM 8 | $0.81 | $1.56 | **1.92x** |

At renewal, Hostinger's entry plan costs **$3.00 per GB** — which lands right next to Namecheap's yearly-billed rate of $3.88 and is no longer the cheapest thing on this page by a wide margin. The discount does not shrink the unit price by a fixed amount. It moves you to a different tier entirely.

Two more things fall out of that column. **KVM 4 and KVM 8 have identical promotional unit prices** — $0.81 per GB and $3.25 per vCPU each. Buying the bigger plan gets you no per-unit discount at all during the promotional term; the difference only appears at renewal ($1.81 vs $1.56). And the worst renewal jump is on KVM 4, not on the entry plan.

## DigitalOcean's line is flat — except in one place

Across 1 GB, 2 GB, 4 GB, 8 GB and 16 GB, DigitalOcean's Basic Droplets hold an almost perfectly flat **$6.00 per GB**. Whatever you think of the absolute number, that is a legible pricing curve: double the memory, double the price, no games.

Then there are the two exceptions, and one of them is a trap:

- The **512 MiB** plan costs $8.00 per GB — the second-worst rate in this entire table.
- The **2 GiB / 2 vCPU** plan costs **$9.00 per GB**, which is worse than every other DigitalOcean plan on the page *and* worse than the 4 GiB / 2 vCPU plan sitting directly below it at $6.00 per GB.

Both have 2 vCPUs. One has twice the memory. The one with twice the memory is 33% cheaper per GB. There is no workload for which the $18 plan is the better buy.

## Why nobody publishes this number

We read 30 pages across the three biggest comparison sites ranking for VPS deals. Not one of them divides price by RAM. They rank by headline monthly price, by star rating, or by a feature checklist — all of which are things the provider controls and prints for you.

Price per GB is the one number the provider does not print, cannot spin, and does not want compared. Hostinger will tell you it is "67% off." It will not tell you that at renewal you are paying $3.00 per GB, or that KVM 8 gives you no per-unit advantage over KVM 4 for the entire promotional term.

## How to run this on any deal in ten seconds

```
$/GB RAM  = monthly price / RAM in GB
$/vCPU    = monthly price / vCPU count
```

Then do the thing the deal pages will not do for you: **compute it twice**, once at the promotional rate and once at the renewal rate printed on the same card. If the renewal column is not printed, treat the promotional unit price as temporary and reprice at the list rate before you commit.

And check the plan one size up. In every lineup above, per-GB price falls as you scale — except where it does not, and those are exactly the plans to skip.

## What we could not verify

Hetzner's Cloud pricing page renders its plan prices client-side and returned no figures to an automated reader on 2026-10-09, so it is absent from the table rather than estimated. Its published billing model is hourly with a monthly price cap, rounded up to whole hours — a different shape from the three above, and worth its own calculation once the plan figures are readable.

Vultr, Linode and Contabo pricing pages also refused automated reads today. We are not filling those rows with recalled numbers.
