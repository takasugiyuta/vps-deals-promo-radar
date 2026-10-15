---
title: "Cheap VPS Deals: What Each Host Will Actually Take as Payment — and What Crypto Costs You"
slug: vps-deals-payment-methods-accepted
date: 2026-10-15
description: "Read off providers' own pages on 2026-10-15: DigitalOcean takes 7 card brands plus PayPal/Google Pay/Apple Pay/Alipay/Link plus stablecoins from 400+ wallets, and charges $25.00 to verify a crypto wallet but $0 to verify Apple Pay. Hetzner takes 4 card brands, SEPA (EUR accounts only), wire and PayPal, and states plainly 'We do not accept cryptocurrencies.' Hostinger accepts crypto and then says crypto purchases 'will not be refunded.' Namecheap and Liquid Web publish no payment-method list at all."
question: Can I pay for a cheap VPS deal with PayPal or crypto, and can I get that money back if I change my mind?
sources:
  - https://docs.digitalocean.com/platform/billing/manage-payment-methods/
  - https://docs.digitalocean.com/platform/billing/pay-bills/
  - https://docs.digitalocean.com/platform/billing/
  - https://docs.digitalocean.com/support/why-does-digitalocean-require-prepayment-for-paypal/
  - https://docs.digitalocean.com/support/can-i-have-a-refund/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/payment-overview/
  - https://www.hetzner.com/legal/terms-and-conditions/
  - https://www.hostinger.com/legal/refund-policy
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.namecheap.com/hosting/vps/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the providers' own billing pages on 2026-10-15, the answer is that the cheap-VPS market has no shared payment baseline: DigitalOcean takes 7 card brands, 5 third-party wallets and stablecoins from "over 400 wallets"; Hetzner takes 4 card brands, SEPA for EUR accounts only, wire transfer and PayPal — and writes "We do not accept cryptocurrencies"; Hostinger takes crypto and then writes that crypto purchases "will not be refunded." Namecheap and Liquid Web publish no payment-method list on their VPS pages at all.** The payment rail you pick is not a neutral checkout choice. On these three hosts it decides whether you can get a refund, how long your money is in transit, and in one case which browser you are allowed to use.

## The matrix, read off official pages on 2026-10-15

| Rail | DigitalOcean | Hetzner | Hostinger |
|---|---|---|---|
| Card brands | Visa, MasterCard, Amex, Discover, UnionPay, Diners Club, JCB (**7**) | VISA, Mastercard, AMEX, UnionPay (**4**) | Not enumerated on the VPS page; ToS refers to "valid and eligible payment methods specified here" |
| Debit cards | Yes | Not listed separately | Not enumerated |
| SEPA direct debit | No | **Yes — EUR accounts only** | Not verifiable |
| US ACH direct debit | **Yes — qualifying customers, U.S. banks** | No | No |
| Bank / wire transfer | No | Yes (manual) | Not verifiable |
| PayPal | Yes | Yes — **manual payment only** | Not enumerated |
| Google Pay | Yes (Chromium browsers only) | Not listed | Not verifiable |
| Apple Pay | Yes (Safari only) | **No — "even if they are linked to a credit card"** | Not verifiable |
| Alipay | Yes | Not listed | Not verifiable |
| Link | Yes | Not listed | Not verifiable |
| Crypto | **Yes — stablecoins, 400+ wallets, limited availability** | **No — "We do not accept cryptocurrencies."** | **Yes** |
| Explicitly rejected | Virtual, electron and prepaid cards | Apple Pay, crypto, partial payments and payment plans | Not enumerated |

Two things fall out of that grid immediately. First, **there is no method all three accept** except ordinary credit cards — and even there the brand lists differ: Discover, Diners Club and JCB work at DigitalOcean and appear nowhere in Hetzner's list. Second, **the two direct-debit rails are mutually exclusive by geography**: Hetzner's SEPA is "only available for EUR accounts," DigitalOcean's ACH is for "qualifying customers with U.S. bank accounts." A euro-zone customer and a US customer are looking at two completely different automatic-debit options on two different hosts.

## Crypto: three hosts, three incompatible policies

This is the part that actually costs money, and the three majors do not agree on it at all.

**Hetzner refuses it outright.** Its [Payment Overview](https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/payment-overview/) (last changed 2026-07-28, article ID GE-CE966) states: *"We do not accept cryptocurrencies."* Its terms and conditions go further on the compute side — *"The operation of applications for mining cryptocurrencies remains prohibited."*

**Hostinger accepts it and removes the exit.** The [Hostinger Refund Policy](https://www.hostinger.com/legal/refund-policy) says:

> Due to their nature, cryptocurrencies, tokens and digital assets are generally irreversible and their exchange rates are highly volatile and transitory... **Products purchased using cryptocurrencies, tokens or digital assets will not be refunded.**

Note how that stacks with Hostinger's VPS-specific refund gate, which is already the strictest in the group: a VPS plan is refundable only if the request lands *"within 30 days from the date of the transaction"* **and** *"more than 180 days have passed from the moment of initiation of last refund for any other VPS hosting plan."* Pay with a card and you have one narrow, once-per-180-days window. Pay with crypto and you have no window at all — the 30-day policy exists, but the payment rail voids it.

**DigitalOcean accepts it and charges $25.00 to let you.** Per [Manage Payment Methods](https://docs.digitalocean.com/platform/billing/manage-payment-methods/): *"During setup we initiate a one-time authorization charge of $25.00. This payment is applied as a credit against your future service charges."* Access is *"currently limited and may not be available to all customers in all locations,"* and only stablecoins are supported.

Put that $25.00 next to DigitalOcean's own cheapest Droplet, read from the [pricing page](https://www.digitalocean.com/pricing/droplets) the same day: 512 MiB / 1 vCPU / 10 GiB / 500 GiB transfer at **$0.00595/hr and $4.00/mo**. The verification charge is therefore **6.25 months of that machine's list price** (25.00 ÷ 4.00 = 6.25). It is not refunded to you as cash — it is booked as credit, and DigitalOcean's refund answer is a flat *"We do not offer refunds."*

## The setup-price ladder nobody prints on the checkout page

DigitalOcean charges a different amount to verify each wallet type, and the spread is 5x:

| Method added | Authorization charge at setup | Source wording |
|---|---|---|
| Crypto wallet | **$25.00** | "one-time authorization charge of $25.00... applied as a credit against your future service charges" |
| PayPal | **$5** | "you choose a payment method from PayPal and allow a $5 authorization charge" |
| Google Pay | **$0** | "allow a $0 authorization charge" |
| Apple Pay | **$0** | "allow a $0 authorization charge" |
| Alipay | **$0** | "allow a $0 authorization charge" |
| Credit / debit card | no charge, but a hold | "temporary preauthorization holds may appear on your statement for up to 7 days" |

Crypto costs **5.0x** what PayPal costs to attach (25.00 ÷ 5 = 5.0), and PayPal costs infinitely more than the three $0 options. Against the $4.00/mo Droplet: the PayPal $5 is **1.25 months** of service, the crypto $25 is **6.25 months**. The prepayment is credited back, but the point stands — attaching a crypto wallet to a $4/month VPS deal means fronting more than half a year of that machine's price before the machine exists.

There is a neat coincidence worth knowing: **$25 is also DigitalOcean's Tier 1 auto-charge amount.** Per [How to Pay Your Bill](https://docs.digitalocean.com/platform/billing/pay-bills/), the tier table is:

| Tier | Prepayment amount | Auto-charge amount |
|---|---|---|
| Tier 1 | No Prepay | **$25** |
| Tier 2 | $50 | $50 |
| Tier 3 | $250 | $250 |
| Tier 4 | $1,000 | $1,000 |
| Tier 5 | $4,000 | $4,000 |

So a brand-new team is auto-charged the moment it owes $25 — which on that $4.00/mo Droplet is **6.25 months of usage** (25 ÷ 4.00), the same 6.25 ratio as the crypto verification charge. And climbing from Tier 1 to Tier 2 requires a **$50 prepayment = 12.5 months** of the same machine prepaid up front.

## Your browser decides which wallets you are offered

Two of DigitalOcean's five third-party rails are browser-gated, in writing:

- **Google Pay** — *"The Google Pay option only appears if you are using a Chromium-based browser, like Chrome, Brave, or Microsoft Edge."*
- **Apple Pay** — *"The Apple Pay option only appears if you are using the Safari browser."*

Neither statement leaves room for a third case. On a browser that is neither Chromium-based nor Safari — Firefox being the obvious one — the two wallet options the docs describe are simply not offered, which pushes you onto card, PayPal, Alipay, Link, crypto or ACH. Hetzner's version of this is a flat refusal rather than a browser rule: *"We do not accept other forms of payment, even if they are linked to a credit card (e.g. Apple Pay)."* So an Apple Pay user with a Visa behind it can pay DigitalOcean and cannot pay Hetzner.

## The ACH one-way door at DigitalOcean

Adding a US bank account is not symmetric with adding a card. Per the same page:

> Once you add a bank account, ACH direct debit becomes the default payment method on your team. **To change the default payment method, you need to remove the bank account as a payment method.**

And separately: *"You cannot remove the default payment method on the team."* Read together, those two lines mean the bank account **seizes** the default slot, and the only way to give it back to your card is to delete the bank account entirely. Verification is not instant either — manual entry triggers *"two small micro-deposits"* that you must confirm *"within ten days."*

Speed differs by rail in a way that matters if you are restoring a suspended machine. DigitalOcean: card and third-party payments post quickly, but *"When using PayPal, your balance updates after your payment is processed, which often takes several hours"* and *"PayPal also sometimes holds payments for up to 72 hours."* ACH is slowest — *"which can take several business days."* Its own support doc adds that after you clear a past-due balance you *"need to manually turn your resources (like Droplets) back on"* — paying is not the same as being restored.

## Hostinger's refund outcome depends on which country's rail you used

Hostinger's refund policy splits payment methods into a four-level ladder, and the level is set by the rail, not by the product:

| Level | Payment methods | What you can get |
|---|---|---|
| 0 | Cryptocurrencies, tokens, digital assets | **Nothing.** "will not be refunded" |
| 1 | Multibanco (Portugal), GCash (Philippines), Fawry (Egypt) | **Hostinger Balance only** — "products purchased using these payment methods can not be refunded to the original payment source" |
| 2 | VTC Pay (Vietnam) | **Full refunds only** |
| 3 | Everything else | Original funding source, or Hostinger Balance at Hostinger's discretion |

Level 1 is the one to internalise: a Portuguese customer paying by Multibanco and a Vietnamese customer paying by VTC Pay bought the same VPS under the same 30-day policy and have materially different exits. Level 3 also carries a catch — *"once a refund to Hostinger Balance is initiated for a selected invoice, it becomes irrevocable and cannot be refunded to a different source."*

Separately, a chargeback is treated as a breach with a specific reopening condition: Hostinger *"may"* terminate immediately, credit-card checkout is disabled, and service does not resume until you *"verify the payment method used for the disputed transaction"* by supplying *"a simple censored photo of the credit card, with uncovered first 6 (six) and last 4 (four) digits."*

## Hetzner runs a clock, not a card

Hetzner's model is invoice-first, and the [payment overview](https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/payment-overview/) gives hard numbers:

- *"You must pay within ten days for all your invoices. After that, we will send you an email reminder."*
- Automatic charging is *"a few days after we issue the invoice"* for SEPA and credit card; PayPal and wire are **manual**.
- A failed payment *"can be attempted... up to five times"* before you must ask billing to charge the card manually.
- As lateness grows the rails close: *"If your late payment is later or very late, we may deactivate these options... If your invoice is very late, we will only accept payment via a bank/wire transfer."*
- Very late invoices *"may"* go to *"a debt collection agency"* with *"additional fees that will increase the original invoice amount."*

Prepayment works the opposite way from DigitalOcean's. DigitalOcean: *"A one-time prepayment can increase your trust tier and unlock higher limits immediately."* Hetzner: *"We don't provide an invoice for credit top-ups (prepayment). Invoices are issued only after the service has been provided"*, and credit balances are paid out *"only after the account has been fully closed and there are no outstanding invoices."* If prepaying to raise limits is your plan, only one of the two supports it.

## What the three benchmark sites give you: nothing

Checked on 2026-10-15, above the fold:

- **LowEndBox** — the homepage is a region/virtualization/specialization directory plus a post stream. Deal cards carry provider, region, virtualization, RAM, price, term, author, date and comment count. **Zero payment-method text anywhere on the first screen.** The closest thing is a coupon-code mention inside a headline.
- **Namecheap** — the VPS card reads *"From $3.88 Annual plan / Instead of $4.88/mo"* with a 20% badge. Adjacent non-VPS cards print renewal prices ($1.24, $9.88, $7.88, $3.88, $8.88). **No payment-method list on the VPS page.** The plan table does show *"30-day money-back guarantee"* on all five plans, which is a refund fact, not a payment fact.
- **Liquid Web** — three packages at $150.30 / $175.50 / $256.50 per month, renewing at $2,004 / $2,676 / $5,280 per year. Feature lists include "Unlimited inbound" and "Dedicated IP address." **No payment-method text anywhere on the page.**

All three are deal directories and checkout funnels. None answers "what can I pay with, and can I get it back" — which is exactly why that question is worth answering here.

## Not verifiable today

Stated rather than filled in. No proxy, no cache, no alternate user agent was used to read any of these:

- **Namecheap** — its payment-method list is not on the VPS page, and its legal and KB paths returned 403 to a direct request. The 30-day guarantee quoted above is from the readable VPS plan table; the accepted-payment list is **not verifiable**.
- **Liquid Web** — the packages page is readable but carries no payment-method text, and its legal paths returned 403. **Not verifiable.**
- **Vultr** — pricing and legal paths returned 403. **Not verifiable.**
- **Hostinger's full accepted-method list** — the ToS points to methods *"specified here"* via a link not resolvable in the fetched document, so the per-rail refund ladder above (which is complete and quoted) is used instead of an invented brand list.
- **DigitalOcean crypto availability** — the docs state access is *"currently limited and may not be available to all customers in all locations"*; no eligibility rule is published, so whether your account sees the option is **not verifiable** from documentation.

## What to do with this

1. **If you want a refund path, do not pay with crypto.** Hostinger cancels it outright, Hetzner does not accept it, and DigitalOcean's own refund answer is *"We do not offer refunds"* — so the $25.00 crypto verification charge is credit you must spend, not money you can retrieve.
2. **Check the brand before you blame the card.** Discover, Diners Club and JCB work at DigitalOcean and are absent from Hetzner's list; prepaid, virtual and electron cards are rejected at DigitalOcean by name.
3. **Match the debit rail to your currency.** SEPA is EUR-accounts-only at Hetzner; ACH is US-banks-only at DigitalOcean. Neither host offers the other's rail.
4. **Do not add a US bank account to DigitalOcean casually.** It becomes the default automatically, the default cannot be deleted, and reverting means removing the bank account and re-verifying by micro-deposit within ten days.
5. **Budget for settlement lag.** PayPal at DigitalOcean can be held *"up to 72 hours"*; ACH takes *"several business days"*; and paying a past-due DigitalOcean bill does not turn your Droplets back on by itself.
6. **If you pay at Hetzner, treat the invoice as a 10-day deadline with a 5-retry ceiling**, after which only a wire transfer is accepted and a collection agency becomes possible.
7. **If you are in Portugal, the Philippines, Egypt or Vietnam, read Hostinger's rail-specific table before you buy** — Multibanco, GCash and Fawry refund to balance only, VTC Pay refunds fully, and the difference is written into the policy.

Published 2026-10-15. Every figure above was read from the linked official pages on that date; where a host does not publish a number, this page says so instead of estimating one.
