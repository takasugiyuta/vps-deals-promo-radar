---
title: "VPS Deals: The Free Cloud Firewall Caps You at 50 Rules on One Host and 500 on Another — and One Default Breaks Outbound"
slug: vps-deals-cloud-firewall-rule-limits
date: 2026-10-24
description: "Read off the hosts' own documentation pages on 2026-10-24. Both hosts give the firewall away: DigitalOcean writes \"provided at no additional cost,\" Hetzner writes \"We do not charge for our Cloud Firewalls.\" Both then publish a hard cap — DigitalOcean: \"Each firewall can have up to 50 total incoming and outgoing rules,\" plus \"a maximum of 10 Droplets per firewall and 5 tags per firewall\"; Hetzner: \"Up to 500 (effective) rules per Firewall,\" \"Up to 5 Firewalls per server,\" \"Up to 50 Firewalls across all projects.\" That is a 10x spread on paper, but the two caps are counted on different axes — DigitalOcean counts rules as written, Hetzner counts unique IP prefixes — so the same 300-office-IP allow list eats 2.0% of one budget and 60.0% of the other. Also derived here and published nowhere: a 50,000-prefix deny list consumes 50 of DigitalOcean's 50 rules, leaving zero for allow rules, and it cannot be expressed on Hetzner at any size because Hetzner's FAQ answers \"Can I specify traffic that should get dropped?\" with \"No.\" Plus the migration trap: Hetzner's default permits all outbound traffic when you set no outbound rule; DigitalOcean's default permits none."
question: When a VPS deal throws in a "free cloud firewall," how many rules do I actually get — and is the included layer enough, or will I still be paying for something else?
sources:
  - https://docs.digitalocean.com/products/networking/firewalls/details/limits/
  - https://docs.digitalocean.com/products/networking/firewalls/details/pricing/
  - https://docs.digitalocean.com/products/networking/firewalls/how-to/configure-rules/
  - https://docs.digitalocean.com/products/networking/firewalls/details/features/
  - https://docs.digitalocean.com/products/networking/firewalls/details/availability/
  - https://docs.hetzner.com/cloud/firewalls/overview/
  - https://docs.hetzner.com/cloud/firewalls/faq/
  - https://www.hostinger.com/vps-hosting
---

**Read off the hosts' own documentation pages on 2026-10-24: the firewall that comes with a cheap VPS is free on both hosts and capped on both hosts — 50 rules per firewall at DigitalOcean, 500 effective rules per firewall at Hetzner — and the cap is not the part that will hurt you.** The part that will hurt you is the default. Hetzner writes that *"if you do not set any rule, all inbound traffic will automatically be blocked and **all outbound traffic will automatically be permitted**."* DigitalOcean writes the opposite for outbound: *"If no outbound rules are configured, **no outbound traffic is permitted**."* A firewall config that is safe and invisible on Hetzner — inbound rules only — is a total outage on DigitalOcean: DNS, package updates, NTP and outbound HTTPS all stop the moment the firewall is attached.

Both hosts are explicit that the layer costs nothing. DigitalOcean: *"DigitalOcean Cloud Firewalls are a network-based, stateful firewall service for Droplets **provided at no additional cost**."* Hetzner, in a one-line Pricing section: *"**We do not charge for our Cloud Firewalls.**"* So "is it included" is the wrong question. Every cheap VPS deal on this list includes it. The question is how much firewall you actually got, and the answer is printed in numbers, not adjectives.

Here is the whole comparison. Every cell is verbatim policy from the page named at the bottom of this article, or arithmetic from it.

| | DigitalOcean Cloud Firewalls | Hetzner Cloud Firewalls |
|---|---|---|
| Price | **$0** — "provided at no additional cost" | **$0** — "We do not charge for our Cloud Firewalls" |
| Rule cap per firewall | **50** "total incoming and outgoing rules" | **500** "(effective) rules per Firewall" |
| What counts as one rule | A rule **as written** | A **unique IP prefix** in one direction ("An effective rule corresponds to a unique IP prefix") |
| Firewalls per machine | Not stated | **5** — "Up to 5 Firewalls per server" |
| Firewalls per account / project | Not stated | **50** — "across all projects" |
| Machines per firewall | **10 Droplets**, and **5 tags** | No per-firewall server cap published; applied by server or by label |
| Default inbound with no rules | **Blocked** | **Blocked** |
| Default outbound with no rules | **Blocked** ("no outbound traffic is permitted") | **Allowed** ("all outbound traffic will automatically be permitted") |
| Deny / block rules? | **Yes**, since 4 Aug 2026; "Deny rules take precedence over allow rules" | **No** — "Can I specify traffic that should get dropped? **No**" |
| Rule order matters? | Precedence is defined (deny wins) | **No** — "the order of your Firewall rules does not matter" |
| Protocols an allow rule can express | **ICMP, TCP, UDP** only; `all` is deny-only | **TCP, UDP, ICMP, ESP, GRE**; "All other protocols (like IPIP) will be dropped" |
| Filters private-network traffic? | **Yes** — "Firewalls affect both public and VPC network traffic" | **No** — "Can Firewalls secure traffic to my private Hetzner Cloud Networks? **Not yet**" |
| Can it be put on a load balancer? | **No** — "You cannot apply cloud firewalls to load balancers" | **Not yet** — "we plan to offer this functionality in the future" |
| Traffic logs | **No** — "traffic logs are not available" | Not stated |
| Document last changed | Limits page **2026-08-04** (81 days before this read) | Overview **2021-12-23** (1,766 days); FAQ **2020-03-08** (2,421 days) |

## The 10x gap is real, but the two caps count different things

On paper Hetzner gives you ten times the budget: 500 ÷ 50 = **10.0x**. That comparison is misleading on its own, because the two numbers are denominated in different units, and both hosts say so in their own words.

DigitalOcean counts **rules as you write them**. Its limits page puts it plainly: *"Each firewall can have up to 50 total incoming and outgoing rules"*, *"Deny rules count toward the 50-rule total per firewall"*, and *"Firewall rules are limited to 1,000 entries in the **Sources** or **Destinations** field."*

Hetzner counts something else entirely — it counts **IP prefixes**, not rules. Its FAQ: *"An inbound rule that allows traffic to port 80 for 8 different sources counts as **8 effective rules**"*, and *"**An effective rule corresponds to a unique IP prefix within a given direction**... Multiple ports and protocols for the same prefix are combined into a single effective rule."* Inbound and outbound are counted separately.

So take one real config: one web server, SSH and HTTPS, allowed from **300 office IPs**.

| | DigitalOcean | Hetzner |
|---|---|---|
| Budget consumed | **1 rule** (300 sources fit inside the 1,000-entry field) | **300 effective rules** (one per prefix) |
| Share of the cap | 1 ÷ 50 = **2.0%** | 300 ÷ 500 = **60.0%** |

Same config, same intent: **2.0% of one budget and 60.0% of the other — a 30x difference in how much room you have left.** This is the single most useful thing to know before you commit to a host, and no comparison table on any deal site prints it, because it requires reading two definitions of the word "rule" and dividing.

The composition rule also runs the other way. Hetzner collapses ports and protocols onto a prefix, which is why *"an inbound rule that allows traffic to port 80 for 8 different sources"* is the worst case it shows. DigitalOcean's scarce axis is the number of rule objects; Hetzner's scarce axis is the number of distinct networks you name.

## Derived, and nowhere in either document: what a blocklist actually costs you

DigitalOcean added deny rules on **4 August 2026** — 81 days before this read — and the release note is specific: *"Deny rules take precedence over allow rules that match the same traffic."* But deny rules come with a second, separate ceiling that is easy to miss:

> *"Deny rules count toward the 50-rule total per firewall. Separately, the entries in the **Sources** and **Destinations** fields of all of a firewall's deny rules are limited to a combined total of **1,000**."*

Two caps apply at once, so the binding one depends on the size of your list. With 1,000 entries per rule as the ceiling, the number of rules a deny list eats is `ceil(blocked prefixes ÷ 1,000)`:

| Prefixes you want to block | Deny rules required on DigitalOcean | Share of the 50-rule budget | Rules left for allow |
|---|---|---|---|
| 1,000 | 1 | 2% | 49 |
| 5,000 | 5 | 10% | 45 |
| 25,000 | 25 | 50% | 25 |
| **50,000** | **50** | **100%** | **0** |

At 50,000 prefixes the deny list consumes the entire firewall. You cannot add a single allow rule, because there is no room left to allow anything — and since DigitalOcean's default is *"Cloud firewalls block all traffic that isn't expressly permitted by a rule,"* a firewall with 50 deny rules and no allow rules permits nothing at all.

On Hetzner the same list is not expensive, it is impossible. The FAQ: *"**Can I specify traffic that should get dropped?** No, you only define what traffic is allowed to and from your server. All other traffic will be dropped."* There is no deny action, so a blocklist can only be expressed by inverting your whole firewall into an allowlist. And even inverted, the 500-effective-rule ceiling means a 50,000-prefix list cannot fit.

This is the practical shape of the asymmetry: **DigitalOcean lets you block, and charges you rules for it; Hetzner gives you 10x the rules but no verb for "block."**

## The default that breaks a server during migration

Both hosts block inbound by default. Only one blocks outbound.

DigitalOcean, from the rule-configuration page:

> *"Inbound firewall rules define what traffic to allow or deny to the server... **If no inbound rules are configured, no incoming traffic is permitted.**"*
> *"Outbound firewall rules define what outgoing traffic to allow or deny... **If no outbound rules are configured, no outbound traffic is permitted.**"*

Hetzner, from the FAQ:

> *"If you don't define any rules for the outbound direction, **all traffic is allowed**. If you define one or more outbound rules, the outbound direction also changes to implicit 'deny', and all traffic that doesn't match your rules is dropped."*

Read those together and the failure mode is obvious: a ruleset written on Hetzner with inbound rules only is a **complete** firewall there, and a **half** firewall on DigitalOcean. Attach it to a Droplet and the machine can still be reached, but it can no longer reach anything: DNS resolution on UDP 53, package installs on TCP 443, time sync on UDP 123, and any outbound webhook all fail. Nothing in the DigitalOcean limits page says "you probably want an outbound rule" — it is buried one level down in the how-to page.

There is a second instance of the same split. DigitalOcean requires you to open DHCP by hand for custom images: *"DigitalOcean uses DHCP on port `67`... If you put a Droplet created from a custom image behind a firewall... you need to **create an outbound UDP rule that opens port `67`**."* Hetzner exempts the same traffic unconditionally: *"The Firewall only applies to packets that leave the layer 2 domain... **ARP, DHCP and some ICMPv6 types** like the ones needed for NDP will **always be unaffected**,"* alongside *"Metadata server requests also do not go through the firewall"* and *"our Firewall will always let through traffic to/from certain Hetzner services. This currently includes DNS resolver traffic and traffic for the Hetzner rescue system."*

One host auto-exempts the plumbing. The other makes you write a rule for it and does not tell you at attach time.

## Three more places the two firewalls diverge quietly

**Private traffic.** DigitalOcean: *"Firewalls affect both public and **VPC network** traffic. Rules specific to either must specify the public or private IP range."* Hetzner: *"**Can Firewalls secure traffic to my private Hetzner Cloud Networks?** Not yet, because we consider the private networks to be 'secure'."* If your threat model includes East-West traffic between your own machines, Hetzner's free layer does nothing for it. DigitalOcean's does — which also means DigitalOcean's firewall can break your private traffic if you forget the range.

**Tunnels.** DigitalOcean: *"**Allow rules must use the ICMP, TCP, or UDP protocol.** Only deny rules can use the `all` protocol value."* Hetzner: *"You can filter TCP, UDP, ICMP, **ESP** and **GRE** traffic. All other protocols (like IPIP) will be dropped if you attach a Firewall. GRE protocol has only IPv4 support."* A GRE tunnel or IPsec ESP is expressible as an allow on Hetzner and **not expressible** on DigitalOcean — an allow rule there has no protocol value for it. Conversely, Hetzner's line is a warning in both directions: attaching the firewall silently drops IPIP, and GRE over IPv6 is dropped too.

**Fleet size.** DigitalOcean caps a firewall at *"a maximum of **10 Droplets** per firewall and **5 tags** per firewall,"* and its own workaround for more machines is tagging. Hetzner publishes no per-firewall server cap at all — *"You can apply a Firewall either to an individual server or to all servers with a specific label"* — and caps the other axis instead: 5 firewalls per server, 50 per project. For a 100-machine fleet the arithmetic is `ceil(100 ÷ 10) = 10` DigitalOcean firewalls, each carrying its own copy of the ruleset — 10 × 50 = **500 rule writes** to keep in sync across 10 objects. Hetzner needs one firewall with one label selector. At 500 machines it is 50 firewalls and **2,500 rule writes** on DigitalOcean against one ruleset on Hetzner. On Hetzner the per-server ceiling is also published and generous: 5 firewalls × 500 effective rules = **2,500 effective rules per server**, since *"all rules from the assigned Firewalls will be combined and enforced on the server."* DigitalOcean does not state whether a Droplet can carry more than one firewall, so its per-machine ceiling is not published at all.

**Connection table.** Hetzner publishes one: *"Up to **80000** active, concurrent connections per server (**10000** new connections per second)."* Those two numbers imply a floor on how fast the table can churn — 80,000 ÷ 10,000 = **8 seconds** to fill the entire connection table at the maximum published new-connection rate. DigitalOcean publishes no equivalent figure; its limits page instead warns about state loss on host moves: *"This connection state does not transfer during a live migration, so existing connections reset when we migrate a Droplet to a new host."* Neither host offers logs — DigitalOcean says so directly (*"traffic logs are not available"*), Hetzner does not address it.

## What we could not verify today (and why we are not filling it in)

- **Hostinger** — the VPS product page (read 2026-10-24) advertises *"Managed firewall — Built-in firewall management protects your VPS environment from attacks and malicious traffic,"* lists **"Firewall management"** as a plan feature, and in its FAQ claims *"an AI-powered firewall with an integrated server defense."* It publishes **no rule cap, no machine cap, no protocol list, and no default policy**. There is no number here to compare, so this article makes no claim about sizing it.
- **Namecheap** — the VPS product page returned **403** to a direct request on 2026-10-24. The homepage carries a Security section (SSL, VPN, 2FA, malware cleanup) with **no VPS firewall mention anywhere on it**. Not verifiable.
- **Liquid Web** — `liquidweb.com/vps-hosting/packages/` returned a **Cloudflare Managed Challenge** ("Verifying you are human") on 2026-10-24 rather than the page. We do not work around bot protection, so today's content of that page is **not verifiable** and nothing from it is used here.

One more thing worth weighing, because it is a fact about the documentation and not about the product: the Hetzner FAQ that answers "no, you cannot specify traffic to drop" carries **Last change on 2020-03-08** — 2,421 days before this read, about 6.6 years. The Hetzner overview that carries the limits was last changed **2021-12-23**, 1,766 days ago. The DigitalOcean limits page was updated **2026-08-04**, 81 days ago, and its features page **2026-09-03**. A "no" that old is not necessarily still true; it is simply the newest thing the vendor has published, and it is what you would be relying on.

## What to do with this before you buy

1. **Write your rules before you attach the firewall, not after.** On DigitalOcean, an inbound-only ruleset is a half-configuration that silently cuts all outbound traffic. Add the outbound rules in the same change: DNS (UDP 53), package updates (TCP 443), NTP (UDP 123), and mail or webhooks on whatever port you use.
2. **If you run a custom image on DigitalOcean, open outbound UDP 67.** Hetzner exempts DHCP; DigitalOcean makes it your rule.
3. **Size the firewall on the axis your host counts.** Counting prefixes (office IPs, partner ranges, blocklists)? DigitalOcean's 50 rules go much further than Hetzner's 500 effective rules — 300 prefixes cost 2.0% versus 60.0%. Counting many distinct rules against a handful of networks? Hetzner has 10x the headroom and stacks 5 firewalls per server for up to 2,500 effective rules.
4. **Do not plan on a deny list on Hetzner.** There is no deny action. If blocking specific sources is part of your plan, either the host is disqualifying or your firewall has to be an allowlist end to end.
5. **On DigitalOcean, price your deny list in rules before you need it:** `ceil(prefixes ÷ 1,000)` rules out of 50. Above 25,000 blocked prefixes you are spending more than half your firewall on blocking alone, and at 50,000 you have none left.
6. **Do not expect the free layer to cover a load balancer or private-network segmentation.** Both hosts say no to load balancers today (Hetzner: "not yet"). Hetzner additionally does not filter private network traffic, by design.
7. **Do not expect logs.** DigitalOcean states there are none. If you need to see what was blocked, that is a host-level or third-party job on either host — and the "free firewall" line on the deal page is not paying for it.

Every number above was read off the vendors' own pages on **2026-10-24**; the page-level dates are in the table so you can tell how fresh each claim is. Where a host publishes nothing, this article says so rather than substituting an estimate.
