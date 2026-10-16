---
title: "Cheap VPS Deals: Which Hosts Will Ask for Your ID — and What Each One Wants First"
slug: vps-deals-identity-verification-kyc
date: 2026-10-16
description: "Read off the providers' own pages on 2026-10-16: Namecheap publishes a list of 18 document types it may request (6 of them, 33.3%, are photo IDs) and gives you a Veriff link that expires in 7 days. Hetzner offers exactly 2 verification paths, 1 of which needs a government ID — and warns that signing up over a VPN makes it harder for them to verify you. Hostinger reserves the right to demand 'government-issued photo identification' and, after a chargeback, a credit-card photo with the first 6 and last 4 digits uncovered — 10 of 16 digits, 62.5% of the number. DigitalOcean's ToS mentions government ID zero times and instead verifies your payment instrument for $0, $5 or $25.00. Liquid Web checks your credit, not your ID."
question: Do I have to hand over a passport or ID to buy a cheap VPS deal, and what happens if I refuse?
sources:
  - https://www.namecheap.com/support/knowledgebase/article.aspx/10465/45/why-we-can-request-the-documents-and-what-they-will-be/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/10520/45/identity-and-payment-verification/
  - https://docs.hetzner.com/general/security-and-identify/fraud-prevention-faq/
  - https://docs.hetzner.com/general/billing-and-account-management/account-getting-started/
  - https://www.hetzner.com/legal/terms-and-conditions/
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.hostinger.com/legal/refund-policy
  - https://www.digitalocean.com/legal/terms-of-service-agreement
  - https://docs.digitalocean.com/platform/billing/manage-payment-methods/
  - https://www.digitalocean.com/pricing/droplets
  - https://www.liquidweb.com/policies/terms-of-service/
  - https://www.liquidweb.com/policies/privacy-policy/
---

**Read off the providers' own pages on 2026-10-16, there is no such thing as a standard VPS signup check: of the five hosts below, two can ask you for a government photo ID (Namecheap, Hostinger), one offers you a choice between an ID document and a non-refundable prepayment (Hetzner), one never mentions government ID anywhere in its terms (DigitalOcean), and one checks your creditworthiness instead of your identity (Liquid Web).** The consequence is also not standardised: Namecheap gives you **7 days** on a Veriff link, Hetzner can simply reject your order, Hostinger can suspend the account, and DigitalOcean's Terms of Service §6.3 lets it bill you "an amount up to your current balance at any time to verify the accuracy of your account information."

That last point is the one nobody writes about. "Do I need ID?" is the wrong question, because only two of these five hosts actually ask it. The useful question is **what each host checks instead of you** — your document, your credit, or your payment instrument — and which of those three you are willing to hand over.

## The trigger matrix, read off official pages on 2026-10-16

| Host | Can demand a government photo ID? | What triggers it | What you hand over | Deadline published? | If you don't |
|---|---|---|---|---|---|
| **Namecheap** | **Yes** — Universal Terms of Service: "government-issued photo identification and/or government-issued business identification, plus whatever else we deem required and necessary" | Domain ownership dispute; account access issue; abuse claims; "or various types of abuse claims" | Photo of the ID (both sides) + a selfie, via **Veriff** | **Yes — 7 days**. "the link is valid for 7 days only" | Not stated on the page |
| **Hetzner** | **Yes, on one of two paths** — "a copy of a valid government-issued ID (e.g., ID card or passport)" | Fraud prevention at registration **or** before an order is processed | ID copy **or** an advance payment with your own credit card | **No deadline published** | Order "may not automatically process" or be rejected; account can be rejected for incomplete/false information |
| **Hostinger** | **Yes, at its discretion** — "government-issued business identification or government-issued photo identification" | "reason to believe that your Account information ... is inaccurate, outdated, incomplete or unjustified"; **or** a chargeback | Supporting documents; after a chargeback, "proof of the payment" or a censored card photo | **No deadline published** | "to suspend or terminate your Account" |
| **DigitalOcean** | **No** — zero occurrences of "government" + ID in the ToS | Adding a payment method | The instrument, not the person: $0 / $5 / $25.00 authorisation | Card preauth holds "up to 7 days"; ACH micro-deposits confirmed "within ten days" | Payment method not verified → not usable |
| **Liquid Web** | **No** — no identity check for account opening | "continuing approval of your creditworthiness" | "financial information as we may reasonably request" | **15 days** to cure a suspension before it becomes termination for cause | "We reserve the right to refuse to provide you with our Services in our sole discretion and without notice" |

Two things jump out of that table. First, **the hosts that can demand an ID are the cheap end of the market** — Namecheap's VPS card starts at $3.88/mo annual and Hostinger's KVM line is a promo-driven product, while the two that never ask (DigitalOcean, Liquid Web) are billing $4.00/mo and $150.30/mo respectively. Second, **only one of the five publishes a clock**. Namecheap's 7 days is the only number on the board.

## Hetzner: two paths, and the "no ID" one costs you money

Hetzner's fraud-prevention FAQ is the most explicit document any of these hosts publishes, and it describes exactly **two** ways to verify:

> "**Verification via ID document:** You provide us with a copy of a valid government-issued ID (e.g., ID card or passport). This allows us to confirm that the information provided during registration matches your identity.
> **Verification via prepayment (credit card):** Alternatively, you can verify your account by making an advance payment with your own credit card."

So **1 of the 2 published paths (50%) requires a government ID**, and the other one is a payment. But read the refund condition on that second path before you pick it:

> "As a general rule, we can only refund unused credit that you added during the account verification process if you completely close the account and no outstanding invoices remain."

And: "We do not issue an invoice for credit top-ups (prepayment). We issue invoices only after we provide the service."

That is the trap in the "I don't want to send my passport" argument. The ID-free route is not free — it is **a deposit you cannot withdraw while you remain a customer.** Verification is also not a one-time event at signup: "As part of our fraud prevention measures, we may ask you to verify your account **before we process an order**." You can register successfully and still be stopped at the till.

Hetzner also publishes the only actionable anti-verification advice any host gives, and it is the opposite of what most buyers do:

> "Please, if it is possible, do not use a free email address ... And during the registration process, do not use a VPN service. VPNs make it more difficult for our team to verify your identity and assess the risk of fraud."

Its registration requirements list **four** items — "a valid email address", "personal or business contact information", "a billing address", and "optionally, a phone number for advanced verification". Only **1 of the 4 (25%)** is optional, and that one is the phone, explicitly labelled as being for verification rather than contact.

One more trigger Hetzner documents that no other host does — **order size**: "For first-time customers, we check whether or not the number and value of the products they order seem plausible ... we may not automatically process these orders or may reject them." Its own workaround is to start small: "we suggest that you try one of our lower-priced servers from our Server Auction ... or one of our smaller cloud servers ... for your first order."

## Namecheap: 18 documents, 6 of which are photo IDs

Namecheap's KB article "Why we can request the documents and what they will be" is the longest public KYC list in this group. It enumerates **18** document types:

Passport · Identity card · Permanent resident card · Health Insurance card with photo (Canada, USA, Australia) · Driver's license · U.S. Military ID · A utility bill or a bank statement · Organization formation documents · Documents that confirm the Security Company's legitimacy · Trademark Notice · DMCA Takedown Notice · HMRC tax notification · A screenshot of the PayPal transaction details · Court orders · Birth Certificate · Death Certificate · Change of name certificate · Marriage license.

Do the arithmetic on that list, because the headline is misleading:

- **6 of 18 (33.3%)** are the photo IDs people mean when they say "KYC" — passport, identity card, permanent resident card, health insurance card with photo, driver's license, U.S. Military ID.
- **10 of 18 (55.6%)** are government or civil-status records (the 6 above plus birth certificate, death certificate, change of name certificate, marriage license).
- **8 of 18 (44.4%)** are not identity documents at all — a utility bill or bank statement, company formation documents, security-company legitimacy documents, a trademark notice, a DMCA takedown notice, an HMRC tax notification, a PayPal transaction screenshot, and court orders.
- The list is self-declared incomplete: "The list of the documents is not complete, and in some cases, we may request providing or filling out additional documents and request their notarization." **Notarisation** is on the table.

The mechanics are more specific than any other host's. Verification runs through **Veriff**, and the walkthrough asks for **three images**: "the client is asked to rake the photos of both ID sides and selfie". The trigger is an email "containing a Veriff link from the Risk Management department" — note that it is *Risk Management*, not Support — and the clock is hard:

> "**Q**: I have not submitted the details yet, but the link does not work. **A**: Please note that the link is valid for 7 days only."

**7 days** is the only published deadline in this entire comparison. Namecheap also splits the world into **11** country groups by which documents Veriff accepts; **1 of those 11** gets all four document types (passport, ID card, driver's licence, residence permit), and **1 of 11** — "New Zealand (Tokelau)" — is listed under "No documents supported". If you live in that second bucket, the published process has no path for you.

## Hostinger: discretionary ID, and a card photo that exposes 62.5% of your number

Hostinger's Universal Terms of Service does not make ID mandatory. It reserves the option:

> "If Hostinger has reason to believe that your Account information or any other information you provide to Hostinger is inaccurate, outdated, incomplete or unjustified, Hostinger reserves the right, in its sole and absolute discretion, to request you to validate the information (including to provide required supporting documents, which might include government-issued business identification or government-issued photo identification), to suspend or terminate your Account."

Two document classes are named (**government-issued business identification**, **government-issued photo identification**), the trigger is "reason to believe" — i.e. Hostinger's sole discretion, not a published rule — and the stated consequence of not complying is suspension or termination.

The second, much more specific trigger is a **chargeback**. From the refund policy:

> "Your use of the Hostinger Services and the ability to checkout using credit card will not resume until you: verify the payment method used for the disputed transaction, either by providing: proof of the payment; or a simple censored photo of the credit card, with uncovered first 6 (six) and last 4 (four) digits."

Run the numbers on that instruction. On a standard 16-digit card number, first 6 + last 4 = **10 of 16 digits uncovered (62.5%)**, with the middle **6 digits (37.5%)** hidden. That is the standard card-brand disclosure pattern — the first 6 are the BIN, the last 4 are the ones merchants are permitted to show — but it is worth knowing that "censored" here means "10 of 16 digits still legible", and that the penalty for not sending it is a **standing lock on credit-card checkout**, not just on the disputed order.

## DigitalOcean: no ID, but it verifies your instrument for up to $25.00

Search DigitalOcean's Terms of Service for a government-ID requirement and you get **zero** hits. What it does require, at §1.3, is "your name, email address, and a valid form of payment", and at §1.2, that you are "18 years of age or older" (or have equivalent legal capacity). §6.2 requires that information be "current, complete and accurate".

The surprising clause is §6.3:

> "You may also be billed an amount up to your current balance at any time to verify the accuracy of your account information."

So DigitalOcean's verification mechanism is a **charge against your own balance**, capped at that balance, at any time. Nothing in the ToS ties it to an identity document.

What DigitalOcean does verify, in detail, is the **payment instrument** — and it prices that verification differently per rail. From the payment-methods doc:

| Method | Verification charge | Timing |
|---|---|---|
| Credit card | Preauthorisation request; "may appear on your statement for up to 7 days", no funds transferred | up to 7 days |
| PayPal | **$5** authorisation | — |
| Google Pay | **$0** | Chromium-based browsers only |
| Apple Pay | **$0** | Safari only |
| Alipay | **$0** | — |
| Crypto | **$25.00** one-time, "applied as a credit against your future service charges" | — |
| Bank account (ACH) | Two micro-deposits; you must confirm "within ten days" | 2 micro-deposits / 10 days |

Measured against DigitalOcean's cheapest Droplet — **$4.00/mo, $0.00595/hr** for `s-1vcpu-512mb-10gb`, read off the pricing page on 2026-10-16 — that ladder is **0.00 months** of server time at $0, **1.25 months** at $5.00, and **6.25 months** at $25.00. The spread between the cheapest and the most expensive way to prove you are a real payment method is **$25.00**, and the two $0 rails are gated on **which browser you are using**.

## Liquid Web: creditworthiness, not identity

Liquid Web's Terms of Service contains no identity-verification requirement for opening an account. The closest provision replaces identity with credit:

> "Delivery of the Services is subject to the continuing approval of your creditworthiness. You shall furnish financial information as we may reasonably request to determine your creditworthiness."

Its privacy policy lists what it collects to create an account: "your name, email address, physical address, phone number, credit card information, and website domain" — **six** fields, and unlike Hetzner, where the phone number is optional and tied to "advanced verification", here it is in the baseline set.

The identity verification that Liquid Web *does* publish is for privacy-rights requests, not hosting, and it carries the only real clocks in its policy: a response "within **45 days**", an appeal window of "**30 days**", and a decision on appeal within "**60 days**". For hosting, the lever is refusal, not verification: "We reserve the right to refuse to provide you with our Services in our sole discretion and without notice."

## What the three big comparison sites actually show you

Checked on 2026-10-16, none of the three answer this question on the first screen:

- **LowEndBox** — the homepage is a stream of teasers. Provider, region, RAM and price appear only inside the headline text; the structured fields are author, date and comment count. There is no mention of identity verification, KYC, ID documents, passports or account approval anywhere on the page. "VPN" appears, but only as a navigation tag under Specializations — the exact opposite of Hetzner's advice, which is that a VPN will get you flagged.
- **Namecheap** — the homepage shows no VPS card at all; VPS is a navigation link only. Domain, email and shared-hosting cards are priced and show renewal figures, and identity verification appears nowhere. The only "validation" language on the page is **SSL certificate types in the footer** — "Domain Validation", "Organization Validation", "Extended Validation" — which are certificate-assurance levels, not account checks, and are routinely mistaken for KYC.
- **Liquid Web** — the packages page lists 8 GB at $150.30/mo (renews at $2,004/year), 16 GB at $175.50/mo (renews at $2,676/year) and 32 GB at $256.50/mo (renews at $5,280/year). There is no mention of verification, ID, or account approval. The only occurrence of "ID" on the page is inside "Dedicated IP address".

So the page that would tell you whether your cheap VPS deal needs a passport does not exist on any of the three. You have to read the host's own legal and support pages, which is what this article did.

## What we could not verify (2026-10-16, no proxies, no UA changes)

- **Liquid Web** — `liquidweb.com/policies/*` returns **403** to our automated fetcher; the quotes above were read from the publicly accessible page. No identity-verification requirement for hosting was found in either policy.
- **Hetzner** — no minimum amount is published for the prepayment verification path, and no deadline is published for responding to a verification request. Both are **not verifiable**; we did not estimate them.
- **Hostinger** — no deadline is published for responding to a validation request, and the refund policy does not state how long the credit-card checkout lock lasts. **Not verifiable.**
- **Vultr** — 403 on this run. Not included.
- **Hetzner's Server Auction and Cloud pricing** — client-rendered; no prices captured, so no price-based arithmetic is asserted for Hetzner anywhere above.

## What to do before you buy, in five minutes

1. **Decide what you are willing to hand over before you hit checkout.** If the answer is "nothing", your realistic shortlist is DigitalOcean (instrument verification, $0 on Google Pay / Apple Pay / Alipay) and Liquid Web (credit check) — not the $3.88/mo end of the market.
2. **If you are going with Hetzner, do not register over a VPN and do not use a throwaway free email address.** Both are named in its own fraud-prevention FAQ as things that make verification harder. Make your first order small; its FAQ says large first-time orders are the ones that get rejected.
3. **If you are going with Hetzner and choose prepayment over the ID, treat that money as locked.** It is only refundable when you fully close the account with no outstanding invoices, and Hetzner issues no invoice for it.
4. **If Namecheap flags you, you have 7 days.** The link comes from the Risk Management department and dies after a week; you will need the ID, both sides, plus a selfie. Check in advance whether your country is in the "No documents supported" group.
5. **Never email an ID.** Namecheap states it "will **never** request you to send your private information as an email attachment" and that government ID is collected only through Veriff. Any email asking otherwise is the phishing attempt, not the check.
6. **On Hostinger, avoid the chargeback route entirely.** A chargeback does not just cost you the dispute — it locks credit-card checkout until you send a card photo showing 10 of 16 digits.
7. **Do not assume "no ID at signup" means "no check ever".** Hetzner verifies before processing an *order*, Hostinger verifies on "reason to believe", and DigitalOcean's ToS §6.3 permits a balance-sized charge at any time. Registration is not approval.
