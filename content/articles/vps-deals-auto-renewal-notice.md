---
title: "How Much Notice Do You Need to Cancel a VPS Deal? The Auto-Renewal Switch, Priced"
slug: vps-deals-auto-renewal-notice
date: 2026-10-12
description: "Three providers, three different answers, and only one of them is literally 'cancel anytime'. Read on 2026-10-12: DigitalOcean needs zero notice but makes committed spend non-cancelable, Hostinger's auto-renewal is on by default and can charge up to 30 days before your term ends, and Hetzner requires 30 days' notice to the end of a calendar month."
question: Does cancelling a VPS require advance notice, and is auto-renewal switched on by default?
sources:
  - https://www.digitalocean.com/legal/terms-of-service-agreement
  - https://docs.digitalocean.com/platform/accounts/deactivate/
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.hostinger.com/legal/refund-policy
  - https://www.hetzner.com/legal/terms-and-conditions/
---

**The short answer, read off the providers' own legal pages on 2026-10-12: there is no industry-wide notice period, and the phrase "cancel anytime" is doing work it does not deserve.** DigitalOcean genuinely needs zero notice. Hostinger also says "Cancel anytime" — but its Terms of Service say the renewal is charged *"from 30 (thirty) to 0 (zero) calendar days before the end of the current subscription period"*, so on a 24-month plan your real deadline is **month 23 of 24**, not month 24. Hetzner is the only one of the three with an actual contractual notice period: **30 days, to the end of a calendar month**.

And the switch itself is not a switch everywhere. DigitalOcean has no auto-renewal toggle to find, because it does not sell subscriptions — it bills usage in arrears on the first of each month. Hostinger's toggle exists and is **on by default**. Hetzner's contract simply *"continue[s] and automatically renew[s] [itself] until terminated by either party"*.

| Provider | Notice you must give | Auto-renewal mechanism | Source read 2026-10-12 |
|---|---|---|---|
| DigitalOcean | **0 days** — cancel anytime via account settings or support | No toggle; usage invoiced in arrears on the 1st | ToS §6.3 (Last Updated 22 Aug 2026) |
| Hostinger | **0 days to flip the toggle, but it must land before the Charge Date — up to 30 days before term end** | Toggle exists, **default ON** | ToS §16 (Last revised 2026-09-29 14:31:57) |
| Hetzner | **30 days, to the end of a calendar month** | No toggle; contract auto-renews until terminated | General T&C §2.6 (v2.0.0, 27 Oct 2021); US Special Terms §7 |
| Liquid Web | Not verifiable (403 to direct request) | Not verifiable | — |
| Namecheap | Not verifiable (403 to direct request) | Not verifiable | — |

## The Hostinger number nobody puts on the deal page

Hostinger's VPS page is the most honest of the three about the renewal price and the most misleading about the cancellation. Every one of its four KVM cards prints this line directly above the buy button, read on 2026-10-12:

> Choose plan **Renews at $11.99/mo for 2 years. Cancel anytime.**

Two sentences, and the second one quietly contradicts the Terms of Service the first one depends on. Here is the card data and what it costs over a full 24-month term:

| Plan | List price (struck) | Promo /mo | Renewal /mo | Renewal increase | Promo, 24 mo | Renewal, 24 mo |
|---|---|---|---|---|---|---|
| KVM 1 | $19.49 | $6.49 | $11.99 | **+84.7%** | $155.76 | **$287.76** |
| KVM 2 | $24.49 | $8.99 | $14.99 | **+66.7%** | $215.76 | **$359.76** |
| KVM 4 | $42.99 | $12.99 | $28.99 | **+123.2%** | $311.76 | **$695.76** |
| KVM 8 | $73.99 | $25.99 | $49.99 | **+92.4%** | $623.76 | **$1,199.76** |

Now the part that changes how you read the whole deal. Hostinger's ToS §16 states that auto-renewal renews *"for a subsequent subscription period, the length of which is equal to the most recent subscription period before renewal or the initial subscription period"*. The period you bought was **2 years**. So the renewal is not a $11.99 charge — it is **one charge of $287.76**, because `11.99 × 24 = 287.76`. Across all four plans the renewal term is **$2,543.04 against a promo term of $1,307.04, a $1,236.00 swing**, and it lands as four single transactions, not 48 monthly ones.

The formula, so you can run it on any card:

```
renewal lump sum = (renewal $/mo) × (months in the term you originally bought)
effective cancellation deadline = term end date − up to 30 days
```

### The "67% off" badge and the renewal price use different denominators

This is the cleanest trap on the page. KVM 1 is badged **67% off**, and that is arithmetically true — but the discount is measured against the **struck-through list price of $19.49**, not against what you will actually pay next:

- Promo vs list: `1 − 6.49 / 19.49 = 66.7%` → the **67% off** badge.
- Renewal vs list: `1 − 11.99 / 19.49 = 38.5%` → the renewal is still discounted off list.
- Renewal vs promo: `11.99 / 6.49 = 1.847` → you pay **+84.7%**, which is the only number that describes your bank account.

So the badge is a real discount off a price almost nobody pays, and the +84.7% is the number that is absent from the card. Same card, three denominators, and only one of them is printed.

### Where "cancel anytime" actually stops

Hostinger ToS §16, verbatim:

> Charge Date depends on the type of Services and length of subscription period. In any case, Hostinger charges the Payment Method linked to your Account before (e. g., from 30 (thirty) to 0 (zero) calendar days before) the end of the current subscription period.

> We have the right, but not an obligation, to inform you via email about the upcoming auto-renewal before the Charge Date (e.g., Customers having subscriptions for 1 (one) month period will not be informed).

Two consequences, both derivable from that text and neither stated on the pricing page:

1. **On a 24-month plan you have until roughly day 700 of 730.** The charge window opens 30 days early, so a cancellation on day 705 of a 730-day term is too late for the *next* charge. "Cancel anytime" means anytime before month 23.
2. **On a 1-month plan the stated window starts at the moment of purchase.** "30 days before the end" of a 30-day term is day zero. Hostinger does not say it charges on day zero — it says the window runs from 30 to 0 days — but it does say, explicitly, that **monthly subscribers will not be emailed about it at all**. Read those two together: for monthly plans there is no guaranteed warning and no guaranteed window.

The same section also lets you add backup payment methods that *"can be charged by Hostinger automatically if your default Payment Method does not work"*. Turning off one card is not the same as turning off the renewal.

## The one escape hatch, and its 180-day lock

If the $287.76 does land, Hostinger's Refund Policy (Last revised 2026-10-02 07:17:59) contains a sentence that most people would not think to look for:

> "Date of the transaction," for the purpose of this Refund Policy, means the date of purchase of any product or service, **which includes the date any renewal is processed** by Hostinger…

A renewal is a fresh transaction with its own **30-day** refund clock. So the auto-renewal you did not want is, in principle, refundable for 30 days after it is charged — KVM VPS is listed under "PRODUCTS AVAILABLE FOR REFUND UNDER STANDARD TERMS".

But the VPS-specific condition two lines down closes it again:

> VPS hosting plan: Refundable only if at the moment of initiation of the refund both the following conditions are met: (i) VPS hosting plan refund is initiated within 30 days from the date of the transaction of that specific VPS hosting plan and (ii) **more than 180 days have passed from the moment of initiation of last refund for any other VPS hosting plan**, if any.

So: **30 days to claim, but at most one VPS refund every 180 days.** If you refunded a VPS in the last six months — including a different VPS, on a different plan — the renewal that fired without warning is not refundable. Note also that "Upgrades for KVM VPS" sit in the non-refundable list, and that anything bought with cryptocurrency is excluded from refunds outright.

## DigitalOcean: no notice, no toggle, and one clause that is not cancelable at all

DigitalOcean's ToS §6.3 (Last Updated 22 Aug 2026) is unusually blunt on both directions:

> By entering into this TOS and using the Services, you agree to be billed on a recurring basis and to be automatically charged by us or our Payment Processors using your Payment Methods upon invoicing.

> You may cancel your Services account at any time through your account settings or by contacting DigitalOcean support to avoid future charges, except as set forth below.

Zero notice period, genuinely. But the sentence after "except as set forth below" is the one that matters on a VPS deal:

> Notwithstanding anything to the contrary in the TOS or an order form, your purchase of committed usage, reserved capacity, or a similar consumption commitment (e.g., Required Monthly Usage or a Term Spend Minimum) is **non-cancelable and non-reducible**, and the unpaid remainder of such commitment(s) is **immediately due and payable** as of the date of the cancellation…

That is the opposite of a notice period: cancelling does not end the obligation, it **accelerates** it. If your deal involved a spend commitment, "cancel anytime" converts the remaining balance into a single immediate debt.

There is also no auto-renewal switch to look for, because there is no subscription. Per DigitalOcean's billing docs, *"We automatically invoice and charge your team's or organization's primary payment method on the first day of each month for the previous month's usage, or partway through the month when your balance reaches your tier's auto-charge amount."* You are billed for what already ran. The cancellation lever is **destroying the resource**, not flipping a renewal setting — a distinction that matters, because the deactivation doc (last_updated 2026-07-13) makes account deactivation a separate, gated action: you must first resolve team memberships, *"When you delete a team, you must destroy all resources on the team. The payment method associated with the team is be charged for the team's final balance."* Deactivating the account **stops billing**; it does not delete your servers for you.

Two more asymmetries worth knowing before you rely on "cancel anytime":

- **They can end it faster than you can.** ToS §12: *"While we prefer to give advance notice of termination, we reserve the right… to terminate your access to all or any part of the Websites and/or Services at any time, with or without notice, effective immediately."*
- **Your notice to them has to be posted.** ToS §14.5: notices must be sent *"by certified U.S. Mail or by Federal Express (signature required and return receipt requested)"* to their Broomfield, Colorado address. Support tickets are not the contractual notice channel.
- **Prices are not locked.** ToS §6.1 lets them change prices at any time, and *"By continuing to access or use the Websites or Services on or after the date of the price change, you are agreeing to accept and pay the updated prices"* — with deactivation as your *"sole and exclusive remedy"*.

## Hetzner: the only actual notice period of the three

Hetzner's general Terms and Conditions (Version 2.0.0, last updated 27 October 2021) are the only source here that answers the question in the form it was asked:

> 2.5. Contracts are concluded for an unlimited time period unless otherwise agreed.

> 2.6. The contract may be terminated by either party with **30 days' notice to the end of the month**, without specifying any reasons. Differing periods of notice may apply to the Customers depending on the description of relevant services. Notice of termination may be given in text form by letter, fax, email or via the Customer's account on our secure customer interface.

Three things to pull out of that. First, **30 days to the end of a calendar month is not the same as 30 days** — a notice sent on the 3rd of a month does not start the clock until the month ends, so worst case you are paying for close to two further months. Second, **email counts** as valid notice, which is more forgiving than DigitalOcean's certified-mail requirement. Third, the escape hatch in the middle — *"Differing periods of notice may apply… depending on the description of relevant services"* — means the 30 days is a default, not a guarantee for your specific product.

For US-based customers the appended Special Terms are explicit about the renewal mechanism that the general T&C only implies: *"7. Contract Duration and Termination. The contracts will continue and automatically renew themselves until terminated by either party."* Hetzner can also terminate you *"without notice for good cause"* (§2.7), and reserves the right to change prices with prior notification via the customer account or email (§1.3). Separately, §12.1 grants the EU statutory **14-day** withdrawal right, which is a cooling-off period, not a cancellation route for month 13.

## What the three comparison sites put in front of you instead

Read on 2026-10-12, none of the three answers this question on the page you actually land on:

- **LowEndBox** — the homepage is a filter hub plus card feeds. Cards carry title, author, date, comment count, a blurb and a read-more link. There is **no renewal field, no auto-renewal note, and no cancellation field on any card**. The closest thing to a renewal disclosure anywhere on the first screen is the phrase "First Year" inside a headline.
- **Namecheap** — this one is the most instructive, because the machinery exists and is simply not pointed at VPS. On the same homepage, five promo cards print a renewal line: "Renews from $1.24/mo" (Private Email), "Renews for $9.88/mo" (EasyWP), "Renews at $7.88/mo" (FastVPN), "Renews from $3.88/mo" (Personal Site Maker), "Renews from $8.88/mo" (Business Site Maker). The **VPS card prints "From $3.88 Annual plan / Instead of $4.88/mo" and no renewal line at all**. So Namecheap clearly knows how to disclose a renewal price and declines to do it on the VPS card.
- **Liquid Web** — the VPS packages page is the only one of the three that prints a renewal number, and it is more specific than Hostinger's: *"Introductory price. Renews at $2,004 /year after the initial 1-year term."* (8 GB, $150.30/mo), *"$2,676 /year"* (16 GB, $175.50/mo), *"$5,280 /year"* (32 GB, $256.50/mo). Those divide out to $167, $223 and $440 per month — **+11.1%, +27.1% and +71.5%** over the intro monthly rate, and the three discount badges (10%, 21%, 42% off) are computed against exactly those renewal figures. But the page never uses the words "auto-renew" and states **no cancellation notice period anywhere**.

## Not verifiable (and not guessed)

Consistent with how this series handles unreachable sources: where a page could not be read directly, nothing was filled in from memory, from a cache, or from a proxy.

- **Liquid Web** — `liquidweb.com` returns **403** to a direct request from this machine. The figures above come from reading the public page and are labelled as such; the cancellation and auto-renewal terms on their legal pages were not verified.
- **Namecheap** — `namecheap.com` returns **403** to a direct request. The homepage card figures above are from reading the public page; their VPS auto-renewal setting was not verified.
- **Hetzner Cloud specifically** — `hetzner.com/legal/cloud-terms-and-conditions/` returns only a region-redirect shell with no clause text, so no Cloud-specific deviation from the 30-day default could be confirmed. Given §2.6's own *"Differing periods of notice may apply"*, treat 30 days as the general default rather than a Cloud-specific guarantee.

## What to do with this

1. **Never read "Cancel anytime" as a date.** Convert it: `deadline = term end − 30 days` for Hostinger, `end of a calendar month + 30 days` for Hetzner, `now` for DigitalOcean.
2. **Multiply the renewal rate by the term, not by one month.** A Hostinger KVM 1 renewal is a **$287.76** transaction, not a $11.99 one, because the renewal period matches the period you bought.
3. **Put the deadline in a calendar the day you buy**, not the day before expiry — for a 24-month Hostinger term that is month 23.
4. **If you are on Hostinger monthly, assume no email will arrive.** The ToS says so directly. Check the toggle; do not wait for a warning.
5. **Screenshot the renewal line at checkout.** Hostinger's own ToS reserves the right to change *"Services' renewal fees displayed at this Site at the time of your first purchase"*, effective when the service comes up for renewal. The number on the card is not a promise.
6. **Before signing any DigitalOcean deal with a spend commitment, read it as debt.** Committed usage is *"non-cancelable and non-reducible"* and the unpaid remainder becomes *"immediately due and payable"* on cancellation. That is not a subscription; it is a liability.
7. **Know which lever you are pulling.** On DigitalOcean, destroying the Droplet stops the accrual and deactivating the account stops the billing — they are different actions and only the second one ends charges. On Hostinger and Hetzner, the lever is the toggle or a notice in text form, and only Hetzner requires you to give it 30 days in advance.
