---
title: What "Renews at $X" Means on a VPS Deal Page
slug: vps-deals-renews-at-x
date: 2026-10-08
description: A VPS deal's discount badge never equals your renewal increase. Here is the one-line formula, tested against eight real plan cards, to get next year's price before you buy.
question: When a VPS deal page says "renews at $X", what will I actually pay next year, and how do I calculate it before I buy?
sources:
  - https://www.liquidweb.com/vps-hosting/packages/
  - https://www.namecheap.com/hosting/vps/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/10567/21/hosting-packages-life-cycle/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9164/22/how-to-renew-your-hosting-account/
  - https://docs.hetzner.com/cloud/billing/faq/
  - https://www.hostinger.com/vps-hosting
---

“Renews at $X” means the price on the card is introductory and your next term bills at $X. On the eight VPS plan cards we read on two official provider pages today, renewal cost between **11% and 72% more** than the introductory payments for the same length of service — and in all eight cases the increase was *larger* than the discount percentage printed on the badge. That is not accidental. It is arithmetic, and it runs in one direction only.

## The one-line answer: your renewal increase is bigger than the discount

If a card advertises a discount of **d** (as a fraction, so 42% off means d = 0.42), and renewal happens at the undiscounted rate:

```
renewal increase = d / (1 - d)

year-two price = year-one price x 1/(1 - d)
```

The reason is simple. The introductory rate is the list rate minus the discount: `intro = list x (1 - d)`. Renewal goes back to the list rate. So `renewal / intro = 1/(1 - d)`, and the increase is `d/(1 - d)`.

A 50% off badge is therefore not “half price, then a bit more”. It is **+100%** — year two costs twice year one. Nobody prints that sentence on the card.

## Eight plan cards, two vendors, one pattern

We read two official VPS pages on 2026-10-08 and applied the formula to every card that printed a renewal figure.

**Namecheap VPS plans** — each card prints both numbers in one sentence, in the form *“You pay $X — renews at $Y/year”*:

- **Spark** — pay $46.56, renews at $58.56/year. Real increase **+25.8%**. Badge said 20% off → formula predicts +25%.
- **Pulsar** — pay $82.56, renews at $106.56/year. Real increase **+29.1%**. Badge said 23% off → formula predicts +30%.
- **Quasar** — pay $154.56, renews at $190.56/year. Real increase **+23.3%**. Badge said 19% off → formula predicts +23%.
- **Magnetar** — pay $298.56, renews at $346.56/year. Real increase **+16.1%**. Badge said 14% off → formula predicts +16%.
- **Hypernova** — pay $562.56, renews at $634.56/year. Real increase **+12.8%**. Badge said 11% off → formula predicts +12%.

**Liquid Web VPS packages** — each card prints *“Introductory price. Renews at $X /year after the initial 1-year term.”*:

- **8 GB** — $150.30/mo (year one = $1,803.60), renews at **$2,004/year**. Real increase **+11.1%**. Badge said 10% off → formula predicts +11%.
- **16 GB** — $175.50/mo (year one = $2,106.00), renews at **$2,676/year**. Real increase **+27.1%**. Badge said 21% off → formula predicts +27%.
- **32 GB** — $256.50/mo (year one = $3,078.00), renews at **$5,280/year**. Real increase **+71.5%**. Badge said 42% off → formula predicts +72%.

Eight out of eight. On seven of them the formula lands within about one percentage point of the printed numbers; the widest gap is Pulsar (+30% predicted vs +29.1% actual), because the badge percentage itself is rounded. Read the [Namecheap VPS plans](https://www.namecheap.com/hosting/vps/) and the [Liquid Web VPS packages](https://www.liquidweb.com/vps-hosting/packages/) pages yourself and run the division — the arithmetic is visible on the page.

## Why the badge understates it

Two things do the work.

**Different denominators.** The badge measures the discount against the *undiscounted monthly rate*. Your increase is measured against *what you actually paid*. Those are different bases, so the two percentages can never be equal — the increase is always the larger one.

**Different units.** Liquid Web's cards put the promo per month and the renewal per year: “$150.30/mo” against “$2,004/year”. Converted to one unit, that is $150.30/mo now versus $167.00/mo after renewal. Namecheap's cards are easier to read because both figures land in the same sentence and the same unit.

So when you see a monthly promo next to an annual renewal, convert before you compare. That single step is the whole trick.

## The conversion table you can copy

Badge → the increase you actually get at renewal, assuming renewal occurs at the undiscounted rate (which is exactly what all eight cards above state):

```
10% off  ->   +11%
20% off  ->   +25%
25% off  ->   +33%
30% off  ->   +43%
40% off  ->   +67%
42% off  ->   +72%
50% off  ->  +100%
60% off  ->  +150%
65% off  ->  +186%
67% off  ->  +203%
70% off  ->  +233%
```

Read it backwards as well: a “70% off” VPS deal, stated honestly, is “year two costs about 3.3× year one”. Both sentences describe the same offer. Only one of them appears on the card.

## Read the verb, not just the number

The wording around the figure carries its own meaning:

- **“renews at $X”** — an exact figure. Used on both the Namecheap and Liquid Web cards above. This is the most useful field on a VPS page.
- **“renews from $X”** — a floor, not a promise. The actual renewal can be higher. Namecheap uses this form on its promotional tiles for other products.
- **“renews for $X”** — exact, equivalent to “at”.
- **“Was $X/mo”** — the undiscounted monthly rate. Handy shortcut: the renewal monthly rate is close to this number. On Namecheap's cards, “was $4.88/mo” matches the $58.56/year renewal exactly ($4.88 × 12).
- **“upon renewal $X”** — the phrasing review sites and community deal posts use. It is their summary of the vendor's terms, not the vendor's own wording. Verify it on the vendor's page.
- **“after the initial N-year term”** — gives you the jump date. A 2-year initial term moves the increase to month 25, not month 13, which changes the answer if you only plan to keep the server 18 months.

## What today's scan could and could not verify

Our own scan run at **2026-10-08T01:06:57Z** attempted eight official pricing and promotion pages. Five returned readable content; the pricing pages for Vultr and Linode (Akamai) and three Contabo URLs did not, so this article prints **no renewal figure for them**. An unreadable official page is not a license to estimate one.

The Hostinger VPS page was readable, and a single scan returned **four separate discount entries from that one page: 70%, 67%, 65% and 63% off**. Two things follow.

First, four different discount percentages on one page tells you the percentage is a marketing field attached to particular plan and term combinations — not a property of the provider. Second, if those badges behaved like the eight verified cards above, they would imply year-two increases of roughly +233%, +203%, +186% and +170% respectively. **We did not capture Hostinger's renewal prices in this scan, so those four numbers are unknown, not confirmed.** Use them as the question to take to the checkout page, not as Hostinger's renewal price.

## The other model: no promo to jump from

Not every provider plays this game. Hetzner's billing FAQ describes servers with both a monthly price cap and an hourly rate, where the bill never exceeds the monthly cap, and where a server is billed for as long as it exists — including while powered off, because resources stay allocated to it. Prices move to current pricing on certain actions: rescaling a server, restoring a deleted one, or moving it to a project in a different currency.

On that model there is no renewal jump to compute. There is a different failure mode: paying for a server you stopped using. The check changes accordingly — find the event that ends billing (deletion), not a renewal date.

## A 60-second check before you pay

1. **Find the undiscounted rate on the same card** — “was”, “regular”, or the renewal line. If none is present, mark renewal *unknown*.
2. **Put both figures in the same unit and the same term** — both monthly, or both annual.
3. **Divide renewal by promo.** That is your real multiplier. The badge is not.
4. **Find the jump date** — the end of the initial term — and price the whole horizon you intend to keep the server, not one year.
5. **Confirm the same renewal figure appears at checkout.** If the plan card and the checkout disagree, the checkout number is the one you will be charged. Keep a screenshot of both.
6. **If no renewal figure exists anywhere, do not assume the promo continues.** “Unknown” is a legitimate answer, and it usually means the deal is priced for people who forget to cancel.

Worth knowing: [Namecheap documents how hosting package renewal timing works](https://www.namecheap.com/support/knowledgebase/article.aspx/10567/21/hosting-packages-life-cycle/) relative to the billing cycle, and [how to renew a hosting package](https://www.namecheap.com/support/knowledgebase/article.aspx/9164/22/how-to-renew-your-hosting-account/), including renewing before the renewal control appears. Renewal mechanics are provider-specific; never transfer one provider's rule to another.

## Bottom line

- Convert the badge before you trust it: **increase = d / (1 − d)**. A 42% off VPS deal is a +72% renewal, verified on the [Liquid Web packages page](https://www.liquidweb.com/vps-hosting/packages/).
- **“Renews at $X” is the most honest field on a VPS page.** When a card has it you can do the math in ten seconds; when it does not, you are guessing.
- **Compare on a 24- or 36-month horizon**, not month one. The ranking of two VPS deals frequently flips once renewal is included.
- **Prefer pages that print renewal.** Of the pages we checked today, both vendors that published a renewal figure did so on the plan card itself. That transparency is worth more than a slightly bigger headline discount.

The cheapest VPS deal is not the one with the biggest badge. It is the one whose year-two price you already know.
