---
title: "VPS Deals: You Delete the Server — Does the IP Address Die With It?"
slug: vps-deals-can-you-keep-your-ip-after-delete
date: 2026-10-21
description: "Read off five hosts' own pages on 2026-10-21. DigitalOcean states in writing that Droplets \"do not have dedicated IP addresses, only leased ones\" — destroy the Droplet and the address \"returns to the available pool,\" and \"it is not possible to get the same IP back.\" Hetzner is the opposite: its official reinstall advice is to delete the server and keep the IP, by switching off the Primary IP's \"auto delete\" or removing it before you delete. Hostinger sells \"a dedicated IP address\" on every KVM VPS using the exact word DigitalOcean denies having — so the phrase on a deal page tells you nothing. Prices checked today: Hetzner Floating IPv4 €3.00/mo (€0.00446/h), Primary IPv4 €0.50 ($0.60)/mo, IPv6 free; DigitalOcean Reserved IPv4 $5.00/mo ($0.01/h) unattached and free attached, with a $1 billing floor that makes the first 100 hours — 4 days 4 hours — free; Namecheap $4.00/mo per extra IP, 4 total. Plus arithmetic nobody publishes: the implied month length differs per product (672 h for Droplets and Hetzner Floating IPs, but 500 h for a DigitalOcean Reserved IPv4), and an unattached Reserved IPv4 at $5.00/mo costs 125% of the $4.00/mo Droplet it used to sit on."
question: If I delete my VPS, rebuild it, or move it to another datacenter, do I get to keep the IP address?
sources:
  - https://docs.digitalocean.com/support/how-do-i-get-a-droplets-dedicated-ip-address/
  - https://docs.digitalocean.com/support/are-my-droplets-ip-addresses-static/
  - https://docs.digitalocean.com/support/can-i-use-my-droplets-ip-as-a-reserved-ip/
  - https://docs.digitalocean.com/support/can-i-preserve-my-droplets-ipv4-address-when-i-transfer-the-droplet/
  - https://docs.digitalocean.com/products/networking/reserved-ips/details/pricing/
  - https://docs.digitalocean.com/products/networking/reserved-ips/details/limits/
  - https://docs.digitalocean.com/products/networking/reserved-ips/details/features/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/cloud/servers/primary-ips/overview/
  - https://docs.hetzner.com/cloud/floating-ips/overview/
  - https://docs.hetzner.com/cloud/servers/faq/
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/support/knowledgebase/article.aspx/522/48/can-i-order-additional-ip-addresses-for-my-vps-plan/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off five hosts' own pages on 2026-10-21: on a DigitalOcean VPS the IP dies with the machine, on a Hetzner VPS it does not have to, and the words "dedicated IP" on a deal page do not tell you which one you are buying.** DigitalOcean writes it plainly — Droplets *"do not have dedicated IP addresses, only leased ones"* — and when you destroy the Droplet, *"the address returns to the available pool"* and *"it is not possible to get the same IP back."* Hetzner gives the opposite instruction: for a reinstall it recommends *"deleting the server completely and creating a new one instead,"* then tells you *"You can keep the public IP address of your old server and use it for the new one. To do this, make sure that your Primary IP does not have 'auto delete' enabled, or simply remove the Primary IP from the server before you delete the server."*

Here is the whole answer in one screen. "Survives delete" means: you destroy the machine, and the address is still yours to attach to the next one.

| Host | The IP that comes with the server | Survives delete? | How you make it survive | Price to hold it |
|---|---|---|---|---|
| **DigitalOcean** | Leased, auto-assigned from a pool | **No** — returns to the pool | Impossible. You must reserve a *new* IP | Reserved IPv4 **free attached, $5.00/mo unattached**; IPv6 free |
| **Hetzner** | Primary IP, an independently managed resource | **Yes, if you act first** | Turn off "auto delete", or detach before deleting | Primary IPv4 **€0.50 / $0.60 per month**; IPv6 **free** |
| **Hetzner** (portable) | Floating IP, project-level | **Yes** — removable at any time | Just unassign it; deletion lock available | Floating IPv4 **€3.00/mo**; IPv6 **€1.00/mo** |
| **Namecheap** | Dedicated IP with the plan | **Not stated** on any page we could reach | — | Extra IP **$4.00/mo**, **4 IPs total** per VPS |
| **Hostinger** | *"a dedicated IP address"* per KVM VPS | **Not stated** | — | Included |
| **Liquid Web** | *"Dedicated IP"* listed under Features | **Not stated** | — | Included |

Three things in that table are worth more than the table itself:

1. **DigitalOcean's IP and DigitalOcean's portable IP come from different pools.** The doc says it outright: *"These two IP types use different pools of IP addresses that are not interchangeable."* So there is no upgrade path from the IP you already have to one you can keep. The day you need portability, you get a new address and you change your DNS.
2. **Hetzner makes the cheap resource the survivable one.** Its Primary IPv4 is €0.50/mo and can be carried through a delete; its Floating IPv4 is €3.00/mo — **6x the price** — and buys you remapping without a power-off, not survival. Most buyers assume it is the other way round.
3. **"Dedicated IP" means two different things.** Hostinger's product page says *"every KVM VPS client gets a dedicated IP address."* DigitalOcean's support page says Droplets *"do not have dedicated IP addresses."* Same phrase, opposite claims, both on live pages today. It is a marketing word, not a contract term.

---

## The four states an IP can be in, and which one you actually have

Every VPS deal hands you an address. Almost none of them tell you which of these it is. This table is the part you can copy into your own buying checklist.

| State | Who | Survives delete | Movable to another machine | Move requires power-off? | Geographic lock | Price (read 2026-10-21) |
|---|---|---|---|---|---|---|
| **Leased** | DigitalOcean Droplet IP | **No** | No | — | — | Included |
| **Reserved** (portable) | DigitalOcean Reserved IPv4 | Yes | Yes, within one datacenter | No | Same datacenter | **Free attached / $5.00/mo unattached** |
| **Reserved IPv6** | DigitalOcean | Yes | Yes, within one datacenter | No | Same datacenter | **Free, even unattached** |
| **BYOIP** | DigitalOcean | Yes | Yes, Droplets only | No | One datacenter per prefix | **Free** to provision and use |
| **Primary IPv4** | Hetzner | Yes, if auto-delete off or detached first | Yes | **Yes — server must be "off"** | Same location | **€0.50 / $0.60 per month** |
| **Primary IPv6** | Hetzner | Yes, same rule | Yes | Yes | Same location | **Free** |
| **Floating IPv4** | Hetzner | Yes | Yes, any time | **No** | Same network zone | **€3.00/mo** (€0.00446/h) |
| **Floating IPv6** | Hetzner | Yes | Yes, any time | No | Same network zone | **€1.00/mo** (€0.00149/h) |
| **Add-on dedicated IP** | Namecheap | Not stated | Not stated | — | — | **$4.00/mo**, max 4 total |
| **Plan "dedicated IP"** | Hostinger, Liquid Web | Not stated | Not stated | — | — | Included |

Two rows in there are the ones that catch people out:

- **Hetzner Primary IP changes need the power off.** The overview says: *"As long as the power state of existing servers is 'off', you can freely add, remove or replace the Primary IPs of those servers."* Floating IPs are the opposite — *"The server does not need to be powered off to assign a Floating IP."* If you are scripting failover, that single difference decides which one you buy.
- **DigitalOcean's Floating/Reserved IP cannot carry mail or reverse DNS.** The limits page lists both: *"SMTP ports 25, 465, and 587 are blocked"* on Reserved IPs, and *"Reserved IPs do not support PTR (rDNS) records."* A portable IP is not a drop-in replacement for the one you had.

---

## DigitalOcean: the trap is that you cannot convert what you already have

Four separate support pages, all read today, say the same thing from different angles:

- *"Droplets do not have dedicated IP addresses, only leased ones."* — [how-do-i-get-a-droplets-dedicated-ip-address](https://docs.digitalocean.com/support/how-do-i-get-a-droplets-dedicated-ip-address/) (last updated 2026-07-13)
- *"Once the Droplet is destroyed, the addresses are released back into a pool of available addresses in the datacenter. Once back in the pool, the chances of obtaining the same address again are unlikely."* — [are-my-droplets-ip-addresses-static](https://docs.digitalocean.com/support/are-my-droplets-ip-addresses-static/)
- *"We do not support converting a Droplet IP address into a Reserved IP... These two IP types use different pools of IP addresses that are not interchangeable."* — [can-i-use-my-droplets-ip-as-a-reserved-ip](https://docs.digitalocean.com/support/can-i-use-my-droplets-ip-as-a-reserved-ip/)
- *"you cannot preserve a Droplet's IP address when transferring the Droplet between regions, nor can you reassign a non-reserved IP address to another Droplet."* — [can-i-preserve-my-droplets-ipv4-address-when-i-transfer-the-droplet](https://docs.digitalocean.com/support/can-i-preserve-my-droplets-ipv4-address-when-i-transfer-the-droplet/)

Also worth knowing before you rebuild: cloning does not carry the address either. *"The copied Droplet has a new IP address."*

### The price of holding a DigitalOcean address

Reserved IPs are **free while attached** to a Droplet. The bill starts when you hold one that is not attached: **$5.00 per month, quoted as $0.01 per hour**, and *"You are not billed unless you accrue $1 or more per reserved IP."*

That last clause produces a number nobody advertises. At $0.01/hour, the $1 floor is reached after **100 hours — exactly 4 days 4 hours**. So a reserved IPv4 you detach, hold for a long weekend, and re-attach or delete inside that window costs you nothing at all. Past it, you are on the hook.

Two more pieces of arithmetic off the same page:

- **An unattached reserved IPv4 costs more than the machine it left.** DigitalOcean's cheapest Droplet is **$4.00/mo** (512 MB / 1 vCPU / 10 GB, hourly $0.00595, read from the [pricing page](https://www.digitalocean.com/pricing/droplets) today). The unattached IP is $5.00/mo — **125% of the server**. Leave one lying around for a year and it is $60.00 for an address attached to nothing.
- **Do not multiply that hourly rate by a real month.** $0.01/h × 730 h would be $7.30, but the published monthly figure is $5.00 — a **31.5%** gap. The reason is visible if you divide the published monthly by the published hourly across products: Droplets imply **672 hours** to the month (4 ÷ 0.00595 = 672.3; 12 ÷ 0.01786 = 671.9; 48 ÷ 0.07143 = 672.0), but a reserved IPv4 implies **500 hours** (5.00 ÷ 0.01). The reserved-IP hourly rate is rounded to the cent, so it does not extrapolate. Use the monthly number.

Default quota, if you are planning more than one: *"By default, you can reserve three reserved IPs per account"*, a Droplet *"cannot have more than one reserved IP address or BYOIP address assigned to them at a time"*, and a reserved IP cannot be assigned to more than one Droplet at a time. Hetzner's default is **10 Floating IPs per account** (up to 20 per server) — **3.3x** DigitalOcean's.

If you own your own address space, BYOIP takes IPv4 blocks *"from `/24` (256 addresses) to `/18` (16,384 addresses)"* and *"Provisioning BYOIP address blocks and using BYOIP addresses is free."* The catch is in the limits: *"Each BYOIP prefix is added to a single datacenter and can only be assigned to resources within that datacenter"*, and the first two addresses of a subnet are not assignable.

---

## Hetzner: the "auto delete" switch, and the detach-first manoeuvre

This is the one place in the whole comparison where a host tells you how to keep your address through a rebuild. The [Cloud Servers FAQ](https://docs.hetzner.com/cloud/servers/faq/) answer to *"How can I reinstall a server?"* says:

> *"We recommend deleting the server completely and creating a new one instead. This ensures that all settings are new and up to date.*
> *You can keep the public IP address of your old server and use it for the new one. To do this, make sure that your Primary IP does not have "auto delete" enabled, or simply remove the Primary IP from the server before you delete the server. You can then assign the IP to the new server."*

A second answer on the same page repeats it from a different angle — for a server you no longer need, *"you can unassign the Primary IPs and create a Snapshot before deleting the server."*

Two caveats we could not close, stated rather than guessed:

- **The default state of "auto delete" is not printed** on the overview, the creating-Primary-IPs guide, or the FAQ. The docs tell you to check it; they do not say what you will find. Check it before you delete, not after.
- **The docs do not state the fate of a Floating IP on server deletion** in the pages we read. What they do say is that Floating IPs are project-level — *"You can freely assign them to or remove them from any server within the same network zone and project"* — and that *"Servers, Snapshots and Floating IPs can be protected in the Hetzner Console and API"* with a deletion lock that must be removed before deletion. Treat the lock as the intended safeguard.

### Hetzner's pricing, and the 6x portability premium

Straight off the two overview pages today:

| Item | Hourly | Monthly | Annual |
|---|---|---|---|
| Primary IPv4 | €0.0008 / $0.0010 | **€0.50 / $0.60** | €6.00 / $7.20 |
| Primary IPv6 | free | **free** | €0 |
| Floating IPv4 | €0.00446 | **€3.00** | €36.00 |
| Floating IPv6 | €0.00149 | **€1.00** | €12.00 |

The spread inside one vendor is the point: a Floating IPv4 costs **6.0x** a Primary IPv4, and **3.0x** a Floating IPv6. You are not paying for the address — you are paying **€2.50/mo, €30.00/yr** for the ability to remap it while the server is running. If your use case is "survive a rebuild," the €0.50 Primary IP plus an auto-delete check gets you there for **one sixth** of the price.

One more number for anyone scripting this: Hetzner publishes Floating IP prices that imply **672.6 hours** to the month for IPv4 (3.00 ÷ 0.00446) and **671.1 hours** for IPv6 (1.00 ÷ 0.00149) — the same 672-hour month DigitalOcean uses for Droplets. Its Primary IPv4 implies a shorter one, **625 hours** (0.50 ÷ 0.0008). Different products, different clocks; budget off the monthly column.

Capacity limits: *"Up to 1 Primary IPv4 per server"*, *"Up to 1 Primary IPv6 per server"*, and a total Primary IP limit of *"Server limit multiplied by 2"* — the docs' own example being a server limit of 10 giving 20 Primary IPs. Floating IPs: 10 per account by default, 20 per server, *"Assign up to 1 server at a time."*

---

## Namecheap, Hostinger, Liquid Web: what the deal pages do and do not say

**Namecheap** is the only one of the three that publishes an IP price. Its knowledgebase article *"Can I order additional IP addresses for my VPS plan?"* states: *"you can order another dedicated IP address at the price of $4.00 per month. Up to 4 IPs can be provided for a VPS in total."* Ordering is not self-serve — you go through Billing/Sales by live chat or email. At three add-ons that is **$12.00/mo, $144.00/yr** on top of the plan. What the page does not say is whether any of those addresses survive a rebuild or a termination; we found no Namecheap page that does, so treat retention as unverified rather than assume it either way.

**Hostinger**'s VPS page says *"every KVM VPS client gets a dedicated IP address. This lets you implement stronger security measures, such as setting firewall rules specific to your IP address."* That is a security pitch, not a retention promise. Hostinger does not state, anywhere we could reach today, whether that address follows you through a reinstall or a plan change. Compare it with DigitalOcean's *"do not have dedicated IP addresses, only leased ones"* and you have the whole problem with the phrase in one sentence pair.

**Liquid Web** lists *"Dedicated IP"* as a line in the Features block of every VPS package card on [its packages page](https://www.liquidweb.com/vps-hosting/packages/), alongside backup size and DDoS protection. It is presented as an included feature with no price, no count, and no retention policy — and its legal pages returned an access challenge to our fetches today, so we could not check the terms. Included, but unspecified.

---

## The check to run before you delete anything

Copy this. It is four questions, and three of them have to be answered *before* you press delete, because on DigitalOcean the answer to the first one is permanently "no."

1. **Is the address leased or portable?** On DigitalOcean, if you did not explicitly reserve it, it is leased and it is gone the moment the Droplet is destroyed. There is no retroactive fix — *"We do not support converting a Droplet IP address into a Reserved IP."*
2. **If portable, is it attached?** A DigitalOcean Reserved IPv4 that is attached is free; the same address unattached is **$5.00/mo**, billed only once it has accrued **$1** — i.e. after **100 hours / 4 days 4 hours**.
3. **If you are on Hetzner, is "auto delete" off?** If you need the Primary IP to outlive the server, switch it off or detach the IP first. This is the only setting in this entire comparison that lets the address that came with the server survive it.
4. **Does anything depend on the address besides DNS?** On DigitalOcean Reserved IPs, mail is out — ports 25, 465 and 587 are blocked — and PTR records are unsupported. If you run a mail host or anything verified by reverse DNS, a portable IP is not a substitute.

And the buying rule that falls out of all of it: **if keeping the address matters, decide it at purchase time.** On DigitalOcean the cheap path is to reserve an IPv4 from day one and leave it attached (free). On Hetzner the cheap path is the €0.50/mo Primary IP plus an auto-delete check, and the €3.00/mo Floating IP only if you need to remap under load. On neither host does the address that simply arrives with the server come with a promise.

---

## What we could not verify

Stated rather than filled in:

- **The default state of Hetzner's "auto delete" flag** on a Primary IP. Not printed on the overview, the creation guide, or the FAQ. The docs tell you to check it; they do not say what you will find.
- **The fate of a Hetzner Floating IP when its server is deleted.** No page we read states it. What is documented is that Floating IPs are freely assignable and removable within a project and can carry a deletion lock.
- **Retention policy for Namecheap, Hostinger and Liquid Web.** Namecheap publishes a price and a cap but no retention statement; Hostinger and Liquid Web use the phrase "dedicated IP" without defining it. Namecheap's and Liquid Web's product and legal pages returned 403 / access challenges to direct fetches on 2026-10-21 — the Namecheap figure here comes from its knowledgebase, which was reachable.

Everything above was read from the providers' own pages on **2026-10-21 (GMT+8)** and is linked in the source list. Where a host does not publish something, this article says so instead of supplying a number.
