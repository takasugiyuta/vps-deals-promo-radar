---
title: "Can You Send Email From a Cheap VPS Deal? Port 25, 465 and 587, Read off Providers' Own Docs"
slug: vps-deals-port-25-smtp-blocked
date: 2026-10-13
description: "Read on 2026-10-13: DigitalOcean blocks outbound SMTP ports 25, 465 AND 587 on every Droplet by default, including traffic through a Reserved IP. Hetzner blocks only 25 and 465, leaves 587 open, and will unblock on request after one month and your first paid invoice. The popular 'just use port 587' fix works on one of them and fails on the other."
question: Can I send email from the VPS I'm about to buy, and which SMTP ports does the provider block by default?
sources:
  - https://docs.digitalocean.com/support/why-is-smtp-blocked/
  - https://docs.hetzner.com/cloud/servers/faq/
  - https://digitalocean.com/pricing/droplets
  - https://aws.amazon.com/ses/pricing/
  - https://resend.com/pricing
  - https://www.brevo.com/pricing/
  - https://postmarkapp.com/pricing
---

**The short answer, taken from the providers' own documentation on 2026-10-13: on a DigitalOcean VPS you cannot send a single outbound SMTP message, because all three mail ports are blocked and no unblock path is published. On Hetzner you can send today — on port 587 only — and you can apply to have 25 and 465 opened after one month and your first paid invoice.** The two block lists differ by exactly one port, and it is the one every tutorial tells you to use instead.

DigitalOcean's support article *Why is SMTP blocked?* (last updated 2026-07-13) states it in one sentence:

> SMTP ports 25, 465, and 587 are blocked on Droplets to prevent spam and other abuses on our platform. This block applies to all Droplets by default and includes traffic passing through a Reserved IP address.

Hetzner's Cloud Servers FAQ, read the same day, says:

> That's why we block ports 25 and 465 by default on all cloud servers... Once you have been with us for a month and paid your first invoice, you can create a limit request to unblock these ports for a valid use case... As an alternative, you can also use port 587 to send emails via external mail delivery services. Port 587 is not blocked and can be used without sending a limit request.

| Outbound port | DigitalOcean Droplets | Hetzner Cloud Servers |
|---|---|---|
| 25 (SMTP, server-to-server) | **Blocked by default** | **Blocked by default** |
| 465 (SMTPS, implicit TLS) | **Blocked by default** | **Blocked by default** |
| 587 (submission) | **Blocked by default** | **Open** — usable with no limit request |
| Path to get 25/465 opened | None published; the doc recommends a third-party email provider instead | Limit request after **1 month + first paid invoice**; decided case-by-case |
| Scope of the rule | All Droplets, **including through a Reserved IP** | **Per account**; transferring a server to another account applies the new owner's rules |

## Why the "just use 587" advice breaks on one of them

Almost every "my VPS won't send mail" thread ends with *use port 587 instead of 25*. On Hetzner that is literally the vendor's own recommendation and it works with no permission. On DigitalOcean it cannot work, because 587 is inside the block list — switching ports moves you from one blocked port to another blocked port on the same host.

That leaves a DigitalOcean VPS with two ways out, both of which avoid SMTP entirely:

1. **Call an email API over HTTPS (443).** The block is on SMTP ports; the DigitalOcean doc's own recommendation is to use *"a third-party email as a service provider"*, and every provider below offers an HTTPS API alongside SMTP.
2. **Relay on a non-standard SMTP port.** Several relays accept submission on 2525. 2525 is not in DigitalOcean's published block list — but note carefully what that means: it is absent from the list, not guaranteed by it. Test before you depend on it.

## Test it yourself in 30 seconds, from inside the box

Run this on the VPS, not against it — the question is *outbound*, and an inbound port scan tells you nothing:

```bash
for p in 25 465 587 2525; do
  timeout 5 bash -c "cat < /dev/null > /dev/tcp/smtp.gmail.com/$p" \
    && echo "$p reachable" || echo "$p BLOCKED (no response in 5s)"
done
```

Reading the output: a TCP banner or `succeeded` means the path is open; a five-second hang that ends in failure is the signature of a provider-level filter. Two caveats before you blame the host: check your own `ufw`/`iptables` rules and the provider's cloud firewall first, because a self-inflicted DROP produces the identical timeout; and deliverability is a separate problem — an open port 25 gets your packets out, not into anyone's inbox.

## What sending actually costs instead

Running your own mail server is usually justified as the cheap option. The arithmetic says otherwise for almost everyone — and on DigitalOcean it is not available at any price.

DigitalOcean's cheapest Droplet (512 MB / 1 vCPU / 10 GiB / 500 GiB transfer) is **$4.00/mo at $0.00595/hr** on its pricing page. ($4.00 ÷ $0.00595 = 672.3, which is the same 672-hour monthly cap that shows up across its whole price list.) Amazon SES's pay-as-you-go rate is **$0.10 per 1,000 emails**.

> $4.00 ÷ ($0.10 ÷ 1,000) = **40,000 emails**

So one month of the cheapest possible VPS buys 40,000 delivered emails on SES. Below ~40,000 messages a month, renting the box costs more than not renting it — and the SES number is before you spend a single hour on postfix, SPF, DKIM, DMARC, or a blocklist appeal.

| Route | Official price read 2026-10-13 | Effective cost per 1,000 emails |
|---|---|---|
| Amazon SES, à la carte outbound | $0.10 / 1,000 | **$0.10** |
| Amazon SES, Essentials plan (0–10M/mo) | $0.16 / 1,000 | $0.16 |
| Resend Free | $0 — **3,000 emails/mo, 100/day**, 3 domains | $0 (capped) |
| Resend Pro | $20/mo — 50,000 emails/mo, then $0.90 / 1,000 | $0.40 at full quota |
| Resend Scale | $90/mo — 100,000 emails/mo, then $0.90 / 1,000 | $0.90 at full quota |
| Brevo Free | $0 — **300 emails/day** after account approval | $0 (capped) |
| Postmark Basic | $15/mo — 10,000 emails/mo, then $1.80 / 1,000 | $1.50 at plan floor |
| Postmark Pro | $16.50/mo — 10,000 emails/mo, then $1.30 / 1,000 | $1.65 at plan floor |

Three of those rows contain arithmetic worth doing before you pick a plan.

**SES's entry plan costs 60% more per email than paying à la carte.** $0.16 ÷ $0.10 = 1.60. If all you need is outbound sending, the à la carte rate wins; the plan exists for the bundled features (the Pro and Enterprise tiers also carry fixed monthly charges of $105 and $500 per account per region), not for a per-email discount.

**Resend's free tier is bound by a different limit depending on the month.** It allows 3,000 emails/mo *and* 100 emails/day. In a 31-day month the daily cap permits 3,100, so the monthly quota is what stops you at 3,000. In a 28-day February the daily cap permits only 2,800 — so **the daily limit is the binding one in short months and the monthly quota is the binding one in long months.** If your send pattern is spiky (1,000 invoices on the 1st), the daily cap is your real ceiling regardless.

**Brevo's free tier is 3x Resend's — with a gate.** 300 emails/day × 30 = 9,000/mo against Resend's 3,000/mo, a factor of 3.0. The condition is in Brevo's own FAQ wording: *"Once we approve your account for sending, you can start sending up to 300 emails per day."* Free volume you cannot start using the day you sign up is not the same as free volume you can.

**Postmark's Basic plan is cheaper per month and more expensive per extra email.** Basic is $15.00/mo with overages at $1.80/1,000; Pro is $16.50/mo with overages at $1.30/1,000. Solving for the crossover:

> 15.00 + 1.80x = 16.50 + 1.30x → 0.50x = 1.50 → x = 3 extra thousand

**Above 13,000 emails/month, Pro is the cheaper plan** even though its sticker price is 10% higher. Below that, Basic wins. The same logic applies to Resend Pro vs Scale: Scale costs $70/mo more for 50,000 extra emails, i.e. $1.40 per extra thousand, against an overage rate of $0.90 per thousand — so **stay on Pro and pay overages until you pass 50,000 + (70 ÷ 0.90) × 1,000 ≈ 127,800 emails/month**, at which point Scale is finally ahead.

## What we could not verify today, and why we did not fill it in

Under our own rules we do not bypass bot protection and we do not estimate unreadable numbers, so these are stated as unread rather than guessed:

- **Namecheap** — `namecheap.com` returned a Cloudflare interstitial (*"Just a moment..."*) to a direct request on 2026-10-13. No port policy read.
- **Liquid Web** — 403 to a direct request. Read via a normal page fetch: its VPS packages page shows 8 GB / 4 vCPU / 240 GB / 5 TB at $150.30/mo, 16 GB at $175.50/mo, 32 GB at $256.50/mo, with "Unlimited inbound" and "Dedicated IP address" in the feature list — and **zero mentions of email, SMTP or port 25 anywhere on the page**. The only place the word "inbound" appears is bandwidth.
- **Vultr** — 403 to `vultr.com/docs/` and to its docs article path.
- **Akamai / Linode** — `techdocs.akamai.com/linode/docs/send-email` returns a navigation shell with no body text, and its markdown endpoint 404s. No official statement extracted.
- **Hostinger** — its SMTP-settings help article redirects to a VPS DNS article; no port policy obtained.

For contrast, **LowEndBox**'s home page on 2026-10-13 carries provider, region, virtualization, RAM, price, term, author, date and comment count on its offer cards, and its filter taxonomy includes NVMe, DDoS and VPN — but no mail-related field at all. "email", "SMTP" and "port 25" appear nowhere on the page. A deal listing that never mentions outbound mail cannot tell you whether the box you are about to buy can send one.

## What to do, in order

1. **Decide whether you need port 25 at all.** If you are sending transactional mail (password resets, receipts, form notifications), you do not — use an HTTPS email API and the question disappears.
2. **If you are buying a DigitalOcean VPS, plan for zero outbound SMTP.** Ports 25, 465 and 587 are all blocked, including through a Reserved IP, and there is no published unblock request. Budget for a relay from day one; an API on 443 is the safe path.
3. **If you specifically need port 25, Hetzner is the realistic choice of the two** — but count the delay: one month plus your first paid invoice before you can even file the limit request, and then a case-by-case decision with no published SLA. Do not buy it for a mail launch next week.
4. **Run the four-port test above before you migrate anything**, and re-run it after changing cloud firewall rules.
5. **Price the relay against the box, not against zero.** At SES's $0.10/1,000, the cheapest Droplet's $4.00/mo is 40,000 emails — and that is before the maintenance you do not have to do.
6. **On Hetzner, remember the block follows the account, not the server.** Transfer a server to a project owned by another account and the new owner's port-blocking rules apply; check they have 25 and 465 unblocked *before* you move it.
