---
title: Who Actually Collects the VAT on Your VPS Deal
slug: vps-deals-who-collects-vat
date: 2026-10-09
description: Nobody on a VPS deal page tells you who charges the tax. Read the hosts' own billing docs side by side and one rule governs all of them — the collector is set by your tax location, and that location is seeded from the billing address on the payment method you attach first.
question: On a VPS deal, who collects the VAT — the host, the payment provider, or me — and what actually decides it?
sources:
  - https://docs.digitalocean.com/platform/billing/taxes/
  - https://docs.digitalocean.com/platform/billing/taxes/eu/
  - https://docs.digitalocean.com/platform/billing/taxes/tza/
  - https://marketplace.digitalocean.com/vendors/saas-tax
  - https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/value-added-tax/
  - https://www.hostinger.com/support/4933340-how-to-set-up-or-change-your-tax-code-at-hostinger/
  - https://www.hostinger.com/support/5401907-how-to-download-invoices-for-hostinger-purchases/
  - https://www.digitalocean.com/pricing/droplets
  - https://www.liquidweb.com/vps-hosting/packages/
---

Four parties can end up accounting for the VAT on a VPS deal, and which one you get is decided before you ever see a price with tax on it: **the host**, **the marketplace vendor**, **you**, or **nobody at all**. Every tax document we read on 2026-10-09 keys that decision to a single variable — your tax location — and every one of them derives that location from an address attached to your payment method. DigitalOcean states it plainly: *"Your tax location is typically based on your account address, which is initially set to the payment address of your primary payment method when you sign up."* Hostinger goes further and puts the country dropdown **on the payment step itself**: *"Once you have chosen a period and created your account, you will be asked to select a payment method. Before submitting the payment, select your country."*

So the payment rail is not what matters — the address on the rail is. That distinction is worth real money: on DigitalOcean's own published schedule, the identical $6.00/mo Basic Droplet invoices at **$6.30 in the UAE and $7.62 in Hungary**, a 21% spread on the same resource, with no VPN, no coupon and no plan change.

## The four collectors, and how to tell which one you got

| Collector | When it applies | Documented example |
|---|---|---|
| **The host** | Your tax location appears on the host's published country schedule and you have no valid business tax ID on file | DigitalOcean charges EU VAT at the member-state rate; Hetzner charges Germany 19% |
| **The marketplace vendor** | You buy through a marketplace and your location is one where the platform has pushed collection to the seller | DigitalOcean Marketplace: Japan (JCT), Saudi Arabia, Switzerland and the UAE are all **"Vendor"**, not DigitalOcean |
| **You** | You are a registered business in a reverse-charge or withholding regime | Hetzner: EU customers with a valid VAT ID are invoiced *"according to the 'Reverse-Charge' procedure, without German tax"*; Tanzania: *"you may be required to withhold 15% of the gross payment"* |
| **Nobody** | Your location is outside every schedule the host publishes | Hetzner: *"Customers from these countries will receive their invoice without VAT"* |

The second row is the one nobody writes about. DigitalOcean publishes an explicit Responsibility to Collect and Remit Taxes matrix for its Marketplace, and for **four of the twenty jurisdictions listed — Japan, Saudi Arabia, Switzerland and the UAE — the answer is "Vendor," not DigitalOcean**, for both domestic and cross-border sales. If you buy a VPS-adjacent service through that marketplace in Zurich, the company whose logo is on the invoice is not the company doing the remitting.

The third row is where the money actually hides. Tanzania is the clearest published case: DigitalOcean charges **18% VAT** *and separately*, under the Tanzania Income Tax Act, a registered Tanzanian business *"may be required to withhold 15% of the gross payment for digital services from DigitalOcean."* The doc is explicit that *"Withholding tax is separate from value-added tax."* One purchase, two tax mechanisms, two different remitters.

## What a $6.00 VPS actually invoices at, by tax location

DigitalOcean's published schedule lists **39 tax locations** with rates from 5% to 27%. Applying those rates to the $6.00/mo Basic 1 GiB Droplet list price:

| Tax location | Published rate | Landed monthly on $6.00 |
|---|---|---|
| United Arab Emirates | 5% | **$6.30** |
| Thailand | 7% | $6.42 |
| Switzerland | 8.1% | $6.49 |
| Singapore | 9% | $6.54 |
| Australia / Japan / South Korea / Vietnam | 10% | $6.60 |
| India / Peru / Tanzania / Uganda | 18% | $7.08 |
| Germany (EU) | 19% | $7.14 |
| United Kingdom | 20% | $7.20 |
| Russia | 22% | $7.32 |
| Iceland | 24% | $7.44 |
| Norway | 25% | $7.50 |
| Finland (EU) | 25.5% | $7.53 |
| Hungary (EU) | 27% | **$7.62** |

DigitalOcean notes that *"Prices listed on the DigitalOcean website do not include applicable VAT charges"* — so every figure in the right-hand column is a number the pricing page will never show you.

Now the part that deletes the top of that table entirely: *"If you have a valid VAT ID in the European Union, you can add it to your team to remove tax charges from your invoice. If you have a valid VAT ID but don't add it to your team, your invoice includes tax charges."* The 27% is not a fact about Hungary. It is a fact about whether you typed a number into a form.

## Two hosts, same day, three different EU rates

We read DigitalOcean's EU VAT table and Hetzner's VAT page on the same day. They disagree on three member states:

| EU country | DigitalOcean | Hetzner |
|---|---|---|
| Estonia | 24% | 22% |
| Luxembourg | 16% | 17% |
| Romania | 21% | 19% |

They also disagree on South Africa: DigitalOcean publishes **15.5%** (effective 1 May 2019), Hetzner publishes **15.00%** (effective 1 January 2021). Hetzner's table carries "Starting on" dates; DigitalOcean's does not. We are not going to adjudicate which is current — the point for a buyer is that the rate on your invoice is whatever the host's billing engine decided, and two major hosts reading the same statute land on different numbers. Check the invoice, not the schedule.

Hetzner also splits the world differently from DigitalOcean. Where DigitalOcean applies one EU regime, Hetzner has five outcomes: **Germany 19%**, **EU with a valid VAT ID → reverse charge, no German tax**, **EU without one → the VAT rate of your country of origin**, **a short list of non-EU countries** (Australia 10%, Norway 25%, Singapore 9%, South Africa 15%, Switzerland 8.10%, UK 20%, plus sales tax in Texas, Utah, Arizona, Colorado and New Mexico), and **everyone else → no VAT**. Hetzner is also the only one of the two that charges US state sales tax by name: *"We charge an 8% sales tax for customers in Texas... We use the address in your account to figure this out."*

## The Hostinger trap: the VAT you paid is gone

Hostinger's tax page contains a sentence that should be printed on every checkout screen: *"Due to taxes being forwarded automatically, the VAT already applied to an invoice cannot be refunded."* And *"Invoices already issued will remain unchanged."*

The consequence is procedural, not theoretical. The VAT ID field lives on the payment step — *"Before submitting the payment, select your country"* — and if you skip it, Hostinger's only remedy is prospective: *"If you didn't add your tax identification code during the purchasing process... The new information will appear on your future invoices. Invoices already issued will remain unchanged."* Buying a 24-month promotional term and remembering your VAT number in month two costs you the tax on month one permanently.

There is also a ceiling on what Hostinger will even issue. Tax-compliant invoices are available **only** for entities with a valid tax ID in the EU/Northern Ireland, India or Indonesia; *"tax invoices cannot be issued for countries outside the EU/Northern Ireland, India, and Indonesia."* A UAE-registered company *"receive[s] a regular invoice showing VAT charged, rather than a fiscal invoice"* — and Hostinger charges UAE companies **5%**. If your finance team needs a reclaimable fiscal invoice, that is a purchasing decision you make before the order, not after.

## What the deal pages tell you: nothing

We opened the three biggest sites ranking for VPS deals. LowEndBox lists a German VPS at "€3.49/Month" and a Dutch one in euros with **no tax qualifier anywhere on the page** — despite both being in VAT-applicable jurisdictions. Liquid Web's VPS packages page shows three cards at $150.30, $175.50 and $256.50/mo with renewal terms, and its closest thing to tax language is a value prop reading *"Clear inclusions and predictable pricing from day one"* — no tax, no VAT, no statement of whether those figures are inclusive or exclusive. Namecheap's public billing knowledgebase, checked the same day, publishes **no VAT or tax schedule at all**; its checkout is the only place the number appears.

A shopper cannot determine from any of those first screens what they will actually be charged. That is the gap, and it is identical across all three.

## The ten-second check before you buy

```
1. Identify your tax location  -> the billing address of the payment method
                                  you attach FIRST, not your nationality
2. Look up that location on the host's published tax schedule
   - listed?       -> host collects.  landed = posted x (1 + rate)
   - not listed?   -> host collects nothing.  Check whether YOUR country
                      requires you to self-account (reverse charge / WHT)
3. Buying on a marketplace?    -> check the "who remits" matrix.  In Japan,
                                  Saudi Arabia, Switzerland and the UAE on
                                  DigitalOcean Marketplace it is the VENDOR
4. Registered business?        -> enter the VAT/GST ID BEFORE you submit
                                  payment.  Already-paid VAT is not refundable
                                  at Hostinger, and prior invoices do not change
5. Compare landed prices, not posted prices
```

Step 4 is where the money is, and it is the one step every checkout flow lets you skip. The rate is not the decision — the form field is.

## What we could not verify

Vultr, Linode (Akamai) and Contabo pricing pages refused automated reads on 2026-10-09, and we did not reach their tax documentation, so no landed-cost figures for them appear here. Namecheap publishes no tax schedule in its public knowledgebase, so we cannot state what it charges or where — we can only state that the number is not published in the place a buyer would look. DigitalOcean lists Canada, the EU and the United States as "Varies" rather than as single rates; we have not resolved those to a per-jurisdiction number and have left them out of the table rather than estimating.
