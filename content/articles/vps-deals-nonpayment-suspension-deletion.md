---
title: "Cheap VPS Deals: How Many Days You Get After a Payment Fails — Before the VPS Is Switched Off and Deleted"
slug: vps-deals-nonpayment-suspension-deletion
date: 2026-10-17
description: "Read off the hosts' own pages on 2026-10-17: only one of five publishes a real deadline. Namecheap cancels a VPS exactly 7 days after the billing date — suspension and cancellation on the same day, with retries on day 2 and day 5. Hetzner gives you 10 days to pay, then up to 4 reminders, and its last remaining payment rail (bank transfer, 'up to two weeks' to arrive) is slower than the deadline it cures. Hostinger's grace period is not a number: it is whatever is left of your subscription period, 0 to 30 days. Liquid Web's is 10 days plus a 1.5%/month late charge, and stopping payment on day 1 of an annual VPS can turn a $150.30 invoice into a $1,653.30 early-termination claim — 11.0x. DigitalOcean publishes no timeline at all, and 'past due' does not stop your server."
question: If my card fails on a cheap VPS deal, how many days do I have before the host suspends the server, and how many before it deletes it?
sources:
  - https://docs.digitalocean.com/platform/billing/late-payments/
  - https://docs.digitalocean.com/support/what-if-im-unable-to-pay-my-invoice/
  - https://docs.digitalocean.com/support/ive-paid-my-bill-so-why-arent-my-services-online/
  - https://docs.digitalocean.com/platform/teams/how-to/view-resource-limits/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/payment-overview/
  - https://docs.hetzner.com/general/company-and-policy/data-protection-at-hetzner/
  - https://docs.hetzner.com/robot/dedicated-server/troubleshooting/guideline-in-case-of-server-locking/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9165/21/invoicing-policies/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/10567/21/hosting-packages-life-cycle/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9197/21/how-can-i-reactivate-my-canceled-hosting-package/
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.liquidweb.com/policies/terms-of-service/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off five hosts' own pages on 2026-10-17: exactly one of them publishes a date you can put in a calendar. Namecheap says a VPS is "suspended and cancelled 7 days later" than the billing date — and it does both on the same day, so there is no window in which your server is merely switched off. Hetzner says invoices are payable "within ten days." Hostinger publishes no grace period at all: it retries your card "until the current subscription period ends," which is a number between 30 and 0 depending on where in the month it tried. Liquid Web gives a 10-day cure period after written notice and charges 1.5% per month on the unpaid balance. DigitalOcean states plainly that it "does not publish fixed timelines for these stages."**

The second thing nobody tells you is that **"past due" is not "switched off."** DigitalOcean's own late-payment page says that when an account is past due, "The account's existing resources continue to run" — what stops is your ability to create new ones. The power-off happens one stage later, at *suspended*. If you are watching for your VPS to go dark as the warning sign, you are watching for the wrong event, and by then you have already lost one stage.

This matters more on cheap VPS deals than anywhere else, because the cheap end of the market is where annual prepay, expiring cards and $4/month auto-charges collide. Below is every number these five hosts actually publish, plus the arithmetic that turns them into deadlines.

## The runway table — copy this, it is the whole article

Runway is measured from the moment money is first demanded to the moment the server is unrecoverable. `L` = days between invoice issuance and the due date; `C` = days you get after the due date.

| Host | Invoice sent (`L`) | Due / grace after due (`C`) | Total published runway | Switched off and deleted on the same day? | Recoverable after? |
|---|---|---|---|---|---|
| **Namecheap** (VPS) | 7 days before billing date | **7 days** | **14 days** | **Yes** — "suspended and cancelled 7 days later" | Often yes (see below) |
| **Hetzner** | 0 (due immediately) | **10 days** | 10 days + up to 4 reminders | No, staged: lock → cancel → delete | Only if paid before the termination notice |
| **Hostinger** | 0–30 days before period end | Remainder of the subscription period | **0–30 days** | Yes — "terminate upon expiration" | Not stated |
| **Liquid Web** | Not stated | **10 days** after written notice (nonpayment) | ≥10 days | No — 15 days from notice before a suspension becomes termination | Not stated |
| **DigitalOcean** | 0 (billed on the 1st for prior month) | **Not published** | **Unknown** | No — 3 distinct stages | **No** — "Deleted resources cannot be recovered" |

Only Namecheap gives you a number and a second number. Everyone else gives you a stage list and a discretion clause.

## Namecheap: the only host that tells you the exact day

Namecheap's *Invoicing policies* article (last updated 6/9/2026) is the single most specific document any of these five hosts publishes about non-payment. The timeline, in the order the page gives it:

1. **Billing date − 7 days** — "Hosting accounts are invoiced 7 days prior to billing date. An invoice notification email is sent out at the time of invoice generation indicating the outstanding amount and the due date."
2. **Billing date** — "Invoices are due on the billing date." With auto-renewal on, the card is charged "on the 7th day after invoice generation (i.e., on the billing date)."
3. **Billing date + 2 and + 5 days** — "In case the first auto-renewal attempt failed, the system will try to renew the hosting plan on the 2 and 5 days after the billing date."
4. **Billing date + 7 days** — "If the outstanding invoice remains unpaid after the billing date, your hosting account will be suspended and cancelled 7 days later (for Shared packages, VPS and Dedicated server) and 23 days later (for Reseller packages)."

Two things fall out of that which no deal roundup ever mentions.

**The last retry and the cancellation are two days apart, not seven.** The retry schedule compresses: attempts land on D+0, D+2 and D+5, and the axe falls at D+7. So after the *final* automatic charge attempt you have **2 days**, not 7.

**An expired card is treated worse than a declined one.** The page continues: "If the system receives an error related to invalidity of a card (i.e. the attached card expired) it sets a pause in 7 days till the next charge. Thus, there will be only one more automatic attempt to renew the service before it is suspended." A 7-day pause starting from the billing date lands the final attempt on the same day the 7-day suspension clock expires — and the page says that attempt is the last one before suspension. **A hard card failure and a soft card failure do not get the same runway.**

Namecheap also publishes how cancellation is priced differently per product. Subscription-based dedicated servers are "cancelled in 3 days after the billing date" if auto-renewal is on, and **on the billing date itself** if it is off. A VPS gets 7 days: **2.33x the runway of a subscription dedicated server with auto-renewal enabled, and infinitely more than one without it.**

On recovery, Namecheap is the most forgiving of the five, and it publishes the price. Its reactivation article (updated 5/9/2025) says VPS "backups are generated once a week, during the weekend, for all VPS Packages, regardless of the management type," and "backups are over-written by newly created ones." That gives a hard bound on the damage: **your worst-case data loss is the writes since the previous weekend — up to 7 days.** Three further costs are stated in the same article:

- After restoration, "your VPS will have a new IP address." Your DNS and any IP allowlists break, and that is not optional.
- If you only want the data and not a restored server: "You'll need to add $15 to your Namecheap funds."
- VPS Complete Management gets 100 GB of backup storage and backups "3 times a week"; extra space is "$10 per 10 GB of additional backup disk space" — **$1.00/GB**.

The dedicated-server line in the same article is the one to read before you buy anything bigger: "After your dedicated server is canceled, all data is deleted from the server. It is impossible to obtain a backup for User-Responsible servers or servers with the Basic Management option."

## Hetzner: 10 days, four reminders, and a payment rail slower than the deadline

Hetzner's payment overview (last changed 2026-07-28) is blunt: "Invoices are due immediately. You must pay within ten days for all your invoices. After that, we will send you an email reminder." Its data-protection FAQ (last changed 2026-07-20) adds the count: "we will send a total of four payment reminders. In the third payment reminder, we will inform you that your account will be deactivated if payment is still not received."

So the warning arrives in reminder 3 of 4 — **you get exactly one more notice after being told the account will be deactivated.**

What happens next is a menu, not a schedule. The payment overview lists three possible steps — "Lock one or more of your Hetzner servers or services," "Cancel your Hetzner products," "Lock or delete your entire Hetzner account" — and then: "We make decisions about this on a case-by-case basis." New accounts are explicitly faster: "For new accounts, we usually react more quickly to late payments... If you do not pay your first invoice within a short period of time, we may lock your Hetzner servers and other products at an early stage." **A first invoice is treated differently from a twentieth invoice.**

Then comes the trap. As an invoice gets later, Hetzner removes payment methods: "If your late payment is later or very late, we may deactivate these options to help prevent abuse and fraud. If your invoice is very late, we will only accept payment via a bank/wire transfer." And bank transfers, per the same page, take **"up to two weeks"** to arrive.

That is a 14-day settlement time on a 10-day deadline — **the only rail left is 1.4x slower than the clock it is supposed to stop.** If you intend to cure a Hetzner late payment by wire, you are already late by construction.

There is also a hard, non-appealable cliff that no other host here states as plainly: "We will reactivate your account automatically once we process your payment. We will only do so if we receive the payment before we issue a notice of termination. **You cannot revoke a notice of termination that we issue.**"

And on data: "Your data may or may not still be available after we have locked or cancelled your Hetzner product or account. It depends on how late your invoice is and on your specific situation. We do not guarantee that you will be able to restore your data." Access returns only "after you have paid all late invoices, and after we have reactivated your Hetzner products and account." Failed charges on the automatic route may be retried "up to five times" before you have to ask billing to charge the card manually; unresolved debts go to "a debt collection agency," which "will result in additional fees that will increase the original invoice amount."

## Hostinger: the grace period is not a number

Hostinger's Universal Terms of Service §16 does not give a grace period, because structurally it cannot. Auto-renewal is charged at a Charge Date that is "from 30 (thirty) to 0 (zero) calendar days before the end of the current subscription period." Then: "If we cannot charge the renewal payment at the scheduled Charge Date, we may make additional attempts to charge your Payment Method(s) linked to your Account **until the current subscription period ends**."

**Your Hostinger grace period equals whatever is left of your subscription period — anywhere from 30 days down to 0**, decided by where in that 30-to-0 window Hostinger happened to schedule the charge. Two customers on identical plans can get wildly different runways, and neither is published.

Turn auto-renewal off and the number goes to zero explicitly: "should you disable the auto-renewal and fail to manually renew your Services before the end of the then-current subscription period, your Services will terminate upon expiration of the then-current subscription period." Note that this is the *only* one of the five where switching off auto-renewal — the thing everyone is told to do to avoid renewal shock — is also the thing that removes your grace period entirely.

Three more clauses decide what a non-payment actually costs you at Hostinger:

- **No money back once it stops.** "All fees for Services are non-refundable (even if your Services are suspended, terminated or restricted in any other manner, or transferred prior to the end of the Services' subscription period)."
- **A chargeback skips the whole ladder.** On receiving "notification of a chargeback, reversal, payment dispute, or is charged a penalty," Hostinger may pursue "immediate cancellation, termination or suspension, **without notice to you**." No Charge Date, no retries, no remainder of the period.
- **Destruction is discretionary and includes backups.** Where restrictions are applied, Hostinger "may, in its sole and absolute discretion, remove and destroy any data and files (**including back-up copies**) stored by you on its servers, and has no obligation to provide you with such data and files."

Hostinger also disclaims the outcome outright: "Hostinger is not responsible for the loss of Services resulting from an inability to collect fees for Services from your Payment Method(s)." And any balance you were holding is not a rescue fund — credits "will expire after 2 (two) years from their issuance," may be applied by Hostinger to "any outstanding fees (including for the purpose of charging auto-renewal payment)," and "In the event that your Account is terminated... any remaining available credits in Hostinger Balance will be forfeited."

## Liquid Web: 10 days to cure, then 11.0x the invoice

Liquid Web's Terms of Service (effective May 8, 2024) is the only document here with a **price** attached to being late: "we may impose a late charge in an amount equal to one and one-half percent (1½%)... of the unpaid balance per month." On its entry VPS package — 8 GB, 4 vCPU, 240 GB, 5 TB at **$150.30/mo**, renewing at $2,004/year — that is **$2.25 per month** on the unpaid balance.

The timing is in §8. Either party may terminate on written notice if the other defaults and the default "continues for a period of thirty (30) days after receipt of written notice specifying the nature of the breach, or a period of **ten (10) days** in the case of nonpayment of Fees." Nonpayment gets a third of the cure period of any other breach. Separately, breach-based suspensions convert: "In the event you are unable to cure the breach within fifteen (15) days of our notice, the suspension may be treated as a termination for cause."

Two clocks, two different triggers, and the page never says they cannot both run — **≥10 days for nonpayment, plus up to 15 more before a suspension hardens into a termination.**

The number that should stop you is the early-termination charge. Nonpayment "resulting in the termination of the Agreement... shall entitle us to collect from you... one hundred percent (100%) of the monthly recurring charges for the Services multiplied by the number of months remaining in the Service Term," payable "within sixty (60) days of termination."

Run that on the published prices. Stop paying on the entry package one month into a 12-month term and 11 months remain:

| Package | Monthly | Months remaining | Early-termination charge | Multiple of the one unpaid invoice |
|---|---|---|---|---|
| 8 GB | $150.30 | 11 | **$1,653.30** | **11.0x** |
| 16 GB | $175.50 | 11 | **$1,930.50** | **11.0x** |
| 32 GB | $256.50 | 11 | **$2,821.50** | **11.0x** |

**A single failed $150.30 payment on day one becomes a $1,653.30 claim — exactly 11.0x the invoice you missed**, on a service you no longer have. (Assumes the "monthly recurring charges" are the introductory monthly rates printed on the packages page; the ToS does not specify which rate applies.)

Two more from the same document: "During the suspension period, we shall have the right to deny access to, and/or, destroy data stored on the compromised server or account," and on data generally, "You shall be responsible for maintaining all backups of all Customer Data on our servers." You also have "thirty (30) days" to dispute a charge — **three times the cure period for not paying it.**

## DigitalOcean: three stages, zero days

DigitalOcean's late-payments page (last updated 2026-07-15) is the clearest description of the *shape* of the process and the only one that refuses to quantify it. The three stages, verbatim:

- **Past due:** "We email the account owner. We place the account on hold, which prevents creating new resources. **The account's existing resources continue to run.** In certain cases, any Spaces on the account cannot be accessed."
- **Suspended:** "We power down the account's resources. We redirect logins to the payment page."
- **Permanently deleted:** "If an unresolved balance continues after suspension, we may permanently delete the account's resources. **Deleted resources cannot be recovered.** The account owner can still pay the balance to access the account, but they must recreate any resources that were removed."

And then, in the page's own words: "How fast an account moves between past due, suspension, and permanent deletion depends on the account. **DigitalOcean does not publish fixed timelines for these stages.**"

So the honest answer for DigitalOcean is: **nobody outside DigitalOcean knows, and DigitalOcean says so.** That is a better answer than the fake "30 days" that gets repeated on forums, and it is the reason this article exists.

Two operational details cost people real downtime. First, **paying does not bring the server back**: "After your account is current, you must manually power on Droplets that were powered off. **We do not automatically power on any resources for you.**" There are two clocks at DigitalOcean — the money clock and the downtime clock — and only one of them stops when you pay. Second, there is no escape valve: "We do not offer refunds" and "We do not offer extensions."

Here is the arithmetic that explains why cheap DigitalOcean setups almost never see the mid-month enforcement event at all. DigitalOcean may "charge your primary payment method earlier in the month when your outstanding balance reaches your tier's auto-charge amount," and the tier table (last updated 2026-09-30) starts at **$25** for Tier 1. The cheapest Basic Droplet on the pricing page today (2026-10-17) is 512 MiB / 1 vCPU / 10 GiB SSD at **$0.00595/hr, $4.00/mo**. $25 ÷ $4.00 = **6.25**, so:

| Tier | Auto-charge amount | Cheapest Droplets needed to reach it in a month |
|---|---|---|
| Tier 1 | $25 | **7** (6 × $4.00 = $24.00 is under; 7 × $4.00 = $28.00 is over) |
| Tier 2 | $50 | **13** |
| Tier 3 | $250 | **63** |
| Tier 4 | $1,000 | **250** |
| Tier 5 | $4,000 | **1,000** |

**You need seven entry Droplets running before DigitalOcean's mid-month charge can even fire.** For the one-Droplet buyer — the entire audience of a cheap VPS deal — the only enforcement event that exists is the invoice on the first of the month, which means the whole past-due → suspended → deleted ladder can only start on the 1st.

## What the three big comparison sites show instead

Read on 2026-10-17, all three of the sites that rank for `vps deals` are silent on this.

- **LowEndBox** — the homepage is a directory and post feed. Every card carries exactly six fields: title, author, date, comment count, excerpt, and a "Read More" link. Price, RAM and location exist only inside free-text headlines. The words *non-payment*, *overdue*, *invoice*, *grace period*, *suspend* and *deleted* appear **nowhere** on the page.
- **Namecheap** — the homepage has **no VPS card at all**; VPS is a navigation link only. The product cards that are present all print renewal figures (`.com` "renews at $18.48/year", Private Email "Renews at $41.88/year"), so the mechanism exists — it is simply never applied to VPS, and there is no non-payment language anywhere on the page.
- **Liquid Web** — the VPS packages page gives three tiers ($150.30 / $175.50 / $256.50 per month, renewing at $2,004 / $2,676 / $5,280 per year, 10% / 21% / 42% off) plus a four-question FAQ covering what a VPS package is and what to do if you outgrow one. **Zero non-payment, suspension or deletion content**, and no billing FAQ.

The pattern is consistent with the earlier gaps in this series: these pages are built to rank for *what a deal costs*, never for *what happens when the deal stops being paid for*. That is precisely why the numbers above had to be dug out of billing docs, KB articles and terms of service.

## Not verifiable today (2026-10-17)

Stated plainly rather than filled in from memory or proxies:

- **Vultr** — `vultr.com/pricing` returned **403** to direct access; no timeline obtained.
- **Namecheap VPS product page** — `namecheap.com/hosting/vps/` returned **403** to direct script access. Everything Namecheap above comes from its **publicly readable Knowledgebase**, which is a different path and was reachable.
- **Liquid Web** — `liquidweb.com/vps-hosting/packages/` returned **403** to direct script access; the package prices and the Terms of Service clauses were read from the public pages and are labelled as such.
- **Hetzner Cloud pricing** — server prices are client-side rendered and could not be read, so **no Hetzner price arithmetic is asserted anywhere in this article**, only its published day counts.
- **DigitalOcean** — the number of days between stages is not published. That is a fact about the host, not a gap in this research.
- **Hostinger** — no published number of retry attempts, and no published notice period before termination.

## What to do with this

1. **Put the Namecheap date in your calendar if you use Namecheap.** Billing date + 7 is the day the VPS is both suspended and cancelled. Do not wait for the D+5 retry to fail.
2. **Assume DigitalOcean's clock is shorter than you think, because it is unpublished.** Treat the "past due" email as your only warning — by the "suspended" email your Droplets are already powered down.
3. **After paying DigitalOcean, power the Droplets back on yourself.** "We do not automatically power on any resources for you" is the entire difference between a one-hour outage and a multi-day one.
4. **Do not plan to cure a Hetzner default by wire transfer.** "Up to two weeks" to arrive against a 10-day due date means the rail outlives the deadline. Keep a card or SEPA mandate valid on the account.
5. **If you use Hostinger and turn off auto-renewal, you have also turned off your grace period.** Services "terminate upon expiration" — re-add a valid card rather than relying on the remainder of the term.
6. **Never let a Liquid Web annual VPS go unpaid in month one.** 11 months × $150.30 = $1,653.30, due within 60 days, for a service you no longer have.
7. **Backups are the only thing that survives every one of these five policies.** Namecheap's own VPS backups are weekly and overwritten, so worst case you lose a week; Hetzner and DigitalOcean both explicitly do not guarantee your data survives. Namecheap charges **$15** for data-only retrieval — cheap relative to every alternative on this page.
