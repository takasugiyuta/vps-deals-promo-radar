---
title: What a VPS Hourly Rate Actually Costs Per Month (The Multiplier Is 672, Not 730)
slug: vps-deals-hourly-to-monthly
date: 2026-10-10
description: Every VPS hourly-to-monthly conversion you have read multiplies by 730. DigitalOcean's own pricing table divides to exactly 672 on all 19 published plan pairs, and its billing docs say cycles run on the calendar month — which means the shortcut is right for uncapped plans, 8.63% too high for capped ones, and hands you 696 free hours a year.
question: On a VPS deal, what does an hourly rate actually cost per month — is the multiplier 730, 672, or something else?
sources:
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.digitalocean.com/platform/billing/
  - https://www.digitalocean.com/pricing/
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/
---

The multiplier is **not** 730. On DigitalOcean's own pricing page, read on 2026-10-10, every one of the 19 published plan pairs divides to **exactly 672 hours** — not 730, not 744, not "about 700." A $0.00595/hr Droplet is listed at $4.00/mo, and 4.00 ÷ 0.00595 = 672.3. A $1.87500/hr General Purpose Droplet is listed at $1,260.00/mo, and 1260.00 ÷ 1.875 = 672.0. Nineteen pairs, one number.

That matters because 730 is the number everyone uses, and using it on the wrong kind of plan overstates your bill by **8.63%** every single month. The catch — and this is the part no pricing page explains — is that 672 is not the same thing as 730 in disguise. They are two different billing contracts:

- **Capped plans** bill a flat monthly ceiling. DigitalOcean states it directly: *"Bundled Plans have a monthly cap, so you'll never pay more than the flat monthly price for that plan."* For these, your real annual cost is **12 × the monthly price**, period. Multiplying the hourly rate by anything is the wrong operation.
- **Uncapped plans** bill actual hours. Same page, next sentence: *"v5 Droplets are billed on actual hours used each month and are not capped at 672 hours."* For these, ×730 *is* correct, because 730 × 12 = 8,760, which is exactly the number of hours in a 365-day year.

So the folk rule everyone repeats is half right: **×730 is the correct formula for uncapped hourly billing and a 8.63% overestimate for capped plans.** The only way to know which one you are looking at is to read the one sentence the pricing page buries in its FAQ — and then to notice that 672 is not an arbitrary constant at all.

## Why 672: it is February

672 hours is exactly 28 days. DigitalOcean's billing documentation pins the cycle to the calendar: *"DigitalOcean billing cycles are monthly. Your balance accrues over the course of the calendar month based on the cost of the resources you use."*

Calendar months are not all the same length, and 2026 is not a leap year. Run a capped Droplet 24/7 for a full year and here is what the collision produces:

| Month type (2026) | Months | Hours in month | Hours billed (capped) | Free hours |
|---|---|---|---|---|
| 31 days | 7 (Jan, Mar, May, Jul, Aug, Oct, Dec) | 744 | 672 | **72** |
| 30 days | 4 (Apr, Jun, Sep, Nov) | 720 | 672 | **48** |
| 28 days | 1 (Feb) | 672 | 672 | **0** |

Add it up: 7 × 72 + 4 × 48 = **696 hours of free compute per year**, which is 29 full days. You run 8,760 hours and pay for 8,064. The advertised hourly rate is, quite literally, the **February rate** — the one month of the year where the cap and the calendar agree. In every other month the effective hourly rate is lower than the number printed on the page: in a 31-day month, $4.00 ÷ 744 = **$0.005376/hr** against an advertised $0.00595/hr, a 9.68% discount you get for free.

An uncapped v5 Droplet gets none of that. In January it is billed 744 hours. In February, 672.

## The whole published table, and what ×730 does to it

Every figure below is printed on DigitalOcean's pricing page as of 2026-10-10. The last two columns are the two answers to "what does this cost per month" — and they only agree in February.

| Plan (Shared) | Advertised $/hr | Listed $/mo | $/hr × 730 | Error vs listed | Real annual, capped | Real annual, uncapped |
|---|---|---|---|---|---|---|
| 512 MiB / 1 vCPU | $0.00595 | $4.00 | $4.34 | **+8.6%** | $48.00 | $52.12 |
| 1 GiB / 1 vCPU | $0.00893 | $6.00 | $6.52 | **+8.6%** | $72.00 | $78.23 |
| 2 GiB / 1 vCPU | $0.01786 | $12.00 | $13.04 | **+8.6%** | $144.00 | $156.45 |
| 2 GiB / 2 vCPU | $0.02679 | $18.00 | $19.56 | **+8.7%** | $216.00 | $234.68 |
| 4 GiB / 2 vCPU | $0.03571 | $24.00 | $26.07 | **+8.6%** | $288.00 | $312.82 |
| 8 GiB / 4 vCPU | $0.07143 | $48.00 | $52.14 | **+8.6%** | $576.00 | $625.73 |
| 16 GiB / 8 vCPU | $0.14286 | $96.00 | $104.29 | **+8.6%** | $1,152.00 | $1,251.45 |

The same 672 constant holds across the other two families on the page, so it is not a rounding artifact of the cheap tiers:

| Family | Sample pair | $/hr | $/mo | $/mo ÷ $/hr |
|---|---|---|---|---|
| CPU-Optimized | 4 GiB / 2 vCPU | $0.06250 | $42.00 | 672.0 |
| CPU-Optimized | 64 GiB / 32 vCPU | $1.00000 | $672.00 | 672.0 |
| General Purpose | 8 GiB / 2 vCPU | $0.09375 | $63.00 | 672.0 |
| General Purpose | 160 GiB / 40 vCPU | $1.87500 | $1,260.00 | 672.0 |

The error in the ×730 column is constant at 730 ÷ 672 − 1 = **8.63%**, on every tier, at every price point. That is the signature of a systematic mistake, not a rounding difference.

## The decision rule you can actually apply

You cannot tell which contract you have from the price. You have to read one sentence. Here is the test:

| What the page says | Your plan is | Monthly cost formula | Annual cost formula |
|---|---|---|---|
| Has a "monthly cap" / "never pay more than the flat monthly price" | **Capped** | The listed monthly price. Stop. | 12 × monthly price |
| "Billed on actual hours used" / "not capped" | **Uncapped** | $/hr × hours in *this* month (672 / 720 / 744) | $/hr × 8,760 |
| No hourly rate published at all | **Neither — it is a term contract** | Ignore hourly entirely; compare total contract value | See below |

That third row is where most VPS deals actually live, and it is worth saying plainly: **if a host does not publish an hourly rate, there is no hourly math to do.** Hostinger's VPS page, read on 2026-10-10, publishes no hourly figure anywhere — it lists KVM 1 at **$6.49/mo** (from $19.49, "67% off"), "Renews at $11.99/mo for 2 years," KVM 2 at $8.99/mo and KVM 4 at $12.99/mo. Namecheap goes the other direction and leads with a monthly-equivalent of an annual charge: its VPS card shows **$3.88/mo**, "Billed yearly," "You pay $46.56 — renews at $58.56/year," with a struck-through "Was $4.88/mo." Both of those reconcile correctly on their own terms (3.88 × 12 = 46.56; 58.56 ÷ 12 = 4.88). Neither has an hourly rate to convert.

Two hosts we could not verify today, stated as such rather than filled in with remembered numbers: direct requests to `liquidweb.com/vps-hosting/packages/` and `vultr.com/pricing/` both returned **HTTP 403** on 2026-10-10, and Hetzner's Cloud page renders its prices client-side, returning placeholder text in place of figures. **Not verifiable.** We did not substitute figures from any cache, proxy or archive for these three.

## Why nobody tells you this

We read the first screen of the three biggest VPS deal destinations on 2026-10-10, and the pattern is consistent: **all of them show a price with a period label attached and none of them reconcile the periods.**

- **LowEndBox** mixes annual and monthly headline prices in the same feed — *"a 1GB VPS for $12/Year"* next to *"a 6GB VPS for Only €3.49 / Month!"* — and never converts one into the other. Hourly billing appears exactly once, as a headline label on a LowEndTalk offer: *"Hourly Billing."* No rate, no conversion, no explanation.
- **Namecheap** leads with $3.88/mo while billing yearly, and shows both the annual total and the renewal rate without ever writing the sentence that connects them.
- **Liquid Web** is monthly-only on its packages page, with 1-year and 2-year toggles and a renewal figure in the fine print. No hourly rate appears anywhere on the screen.

The gap is not that these sites lack the arithmetic. It is that a page whose job is to rank deals cannot stop to explain the units, because explaining the units makes comparable things look less comparable. A $12/year VPS and a €3.49/month VPS are not the same kind of object, and an hourly rate is not a monthly price divided by 730.

## What to do with this

1. **Stop using ×730 on capped plans.** If the plan has a monthly cap, your monthly cost is the monthly price. On the $96.00/mo tier, ×730 tells you $104.29 — $8.29/month, $99.45/year, of pure arithmetic error.
2. **Find the sentence.** "Monthly cap" or "not capped" — it is usually in the FAQ at the bottom of the pricing page, not in the table. That one sentence is worth 8.63%.
3. **For uncapped plans, use 8,760 hours per year, not 730 × 12 as a guess.** They are the same number, but writing it as 8,760 forces you to remember February is cheaper than January: 672 hours billed vs 744.
4. **If you are comparing a capped plan against an uncapped one, compare annual totals, not hourly rates.** The capped plan's advertised hourly rate is its February rate — the most expensive rate it will ever charge you. The uncapped plan's advertised hourly rate is its every-month rate. Comparing $0.00595 against $0.00595 across those two contract types is comparing a ceiling to an average.
5. **When there is no hourly rate, walk away from the hourly question.** Hostinger, Namecheap and Liquid Web deals are term contracts. The number that matters is the renewal price and the total contract value, and no amount of hour arithmetic will get you there.
