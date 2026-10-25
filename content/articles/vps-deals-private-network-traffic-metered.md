---
title: "VPS Deals: Both Hosts Give You the Private Network Free — Only One Charges You for Traffic Between Your Own Servers"
slug: vps-deals-private-network-traffic-metered
date: 2026-10-25
description: "Read off the hosts' own documentation on 2026-10-25. The private network is free at both: DigitalOcean — \"traffic on them doesn't count against bandwidth usage\"; Hetzner — \"We do not charge for our Cloud Networks\" and \"The traffic on the private network interfaces is free.\" The split is in what each host counts. DigitalOcean: \"Any data transfer sent by a Droplet using a public network interface counts against the transfer pool for that Droplet's team\" — so two Droplets in the same datacenter swapping 2,048 GiB over their public IPs burn 1,048 GiB of a $4-plan pool and cost $10.48; over the VPC they cost $0. Hetzner: \"Incoming and internal traffic is free,\" and internal is defined to include \"Other Hetzner Cloud servers with the same network zone via their public IPs\" — so the same traffic is already free there, and because \"all subnets within a Network also have to be from the same network zone,\" a Network can never carry the cross-zone traffic that Hetzner does bill. Conclusion: at DigitalOcean the private network saves you bandwidth money; at Hetzner it saves you nothing on traffic and everything on isolation. Also published nowhere else: DigitalOcean's managed NAT gateway costs $40.00/month for 2 Gbps and 100 GiB, its marginal rate equals the public overage rate of $0.01 per GiB, and \"Any existing Droplet data transfer allotment does not apply to traffic through NAT gateways\" — a premium of $39.00 + $0.01 × GiB over just using the public interface you already have. Plus capacity: Hetzner caps you at 3 networks per server and 100 attached resources per network (300 reachable); DigitalOcean caps a VPC at 10,000 resources."
question: When a VPS deal includes a private network or VPC, is it actually free — and does traffic between my own servers eat the monthly bandwidth allowance that came with the plan?
sources:
  - https://docs.digitalocean.com/products/networking/vpc/details/pricing/
  - https://docs.digitalocean.com/products/networking/vpc/details/limits/
  - https://docs.digitalocean.com/products/networking/vpc/details/features/
  - https://docs.digitalocean.com/platform/billing/bandwidth/
  - https://docs.digitalocean.com/products/droplets/details/private-droplets/
  - https://docs.hetzner.com/networking/networks/overview/
  - https://docs.hetzner.com/networking/networks/faq/
  - https://docs.hetzner.com/cloud/billing/faq/
  - https://docs.hetzner.com/robot/general/traffic/
  - https://docs.hetzner.com/cloud/general/locations/
---

**Read off the hosts' own pages on 2026-10-25: the private network is free at both hosts, and neither bills you for traffic that stays on it. The difference — and it is a big one — is what each host counts as "private."** DigitalOcean counts by *interface*: *"Any data transfer sent by a Droplet using a public network interface counts against the transfer pool for that Droplet's team... Data transfer between Droplets over the VPC network uses a private network interface."* Hetzner counts by *destination and network zone*: *"We only bill for outgoing traffic. Incoming and internal traffic is free,"* and internal is defined to include *"Other Hetzner Cloud servers with the same network zone via their public IPs."*

Put two servers in the same building and push 2,048 GiB between them in a month. On DigitalOcean that is a bill. On Hetzner it is not — and adding a private network at Hetzner does not change the bill either, because it was already zero. That is the whole finding, and it flips the usual "add a VPC to save bandwidth" advice on its head: **the advice is correct on DigitalOcean and worthless on Hetzner.**

## The answer, in four questions

Every cell below is verbatim policy from the pages linked at the bottom, or arithmetic from them. Read on 2026-10-25.

| Question | DigitalOcean | Hetzner |
|---|---|---|
| Does the private network itself cost anything? | **$0** — "traffic on them doesn't count against bandwidth usage" | **$0** — "We do not charge for our Cloud Networks" |
| Does traffic on it count against my plan's bandwidth allowance? | **No** — "traffic on them doesn't count against bandwidth usage" | **No** — "The traffic on the private network interfaces is free; we will not charge you for it" |
| Do two servers in the same location talking over their **public** IPs count? | **Yes** — "Any data transfer sent by a Droplet using a public network interface counts against the transfer pool" | **No** — internal traffic includes "Other Hetzner Cloud servers with the same network zone via their public IPs" |
| Can traffic cross locations on the private network, and what does it cost? | **Yes, and it costs** — "Bandwidth between peered VPC networks in two different datacenters costs $0.01 per GiB" | **No** — "all subnets within a Network also have to be from the same network zone" |

The last row is where a migration plan dies. DigitalOcean sells you the cross-datacenter hop at $0.01 per GiB — exactly its public overage rate. Hetzner refuses to carry it at all.

## Where the two hosts agree: the network costs nothing

Both are unusually blunt about price, which is rare in this category.

DigitalOcean, on the VPC pricing page (last updated 2026-10-15, ten days before this article): *"Network traffic is free within a VPC network or between peered VPC networks in the same datacenter."* The product page repeats the stronger formulation four times across its sub-pages: *"VPC networks are inaccessible from the public internet and other VPC networks, and traffic on them doesn't count against bandwidth usage."*

Hetzner's Networks overview (document ID **NE-92DC9**, last changed 2021-12-23) has a Pricing section that is one sentence long: *"We do not charge for our Cloud Networks."* Its Networks FAQ (document ID **NE-5C84B**, last changed 2020-02-07) answers the direct question — "Will you charge for this feature? How about traffic?" — with *"The Networks feature is free. The traffic on the private network interfaces is free; we will not charge you for it."*

So "is the VPC included" is not the question worth asking. Every cheap VPS deal on this list includes it. The question worth asking is the one in the next section.

## Where they split: what counts as billable traffic between your own servers

This is the part nobody prints, and it is the part that decides your bill.

**DigitalOcean — interface-based.** From the bandwidth billing page (last updated 2026-09-14):

> "Any data transfer sent by a Droplet using a public network interface counts against the transfer pool for that Droplet's team. All IPv6 traffic uses the public interface. Data transfer between Droplets over the VPC network uses a private network interface."

Three consequences in one paragraph. First, two Droplets in NYC3 syncing a database over their public IPv4 addresses consume the team's pooled allowance. Second, **all IPv6 traffic uses the public interface** — moving your internal replication to IPv6 does not make it free, it makes it countable. Third, the only escape is the private interface.

**Hetzner — destination-based.** From the Cloud billing FAQ (document ID **CL-5547E**, last changed 2020-07-07):

> "We only bill for outgoing traffic. Incoming and internal traffic is free. Internal traffic includes: Other Hetzner Cloud servers with the same network zone via their public IPs; Other Hetzner Cloud servers via private communications using the Networks feature; Hetzner Online dedicated root servers; Other Hetzner Online servers, services, or web hosting packages."

And the matching outbound definition: *"Outgoing traffic includes: Other Hetzner Cloud servers with different network zones (`eu-central`, `us-east`, `us-west`, `ap-southeast`) via their public IPs."*

Hetzner therefore has **two** free lanes and DigitalOcean has **one**. Hetzner's second lane — same-zone traffic over public IPs — is the one that surprises people, because it means you can get the bandwidth outcome of a private network without configuring a private network at all.

## What that difference is worth, in dollars

Take the cheapest DigitalOcean plan, $4.00/month, which the pricing page lists with a **500 GiB** transfer allowance. Run two of them for a full cycle. Allowance is pooled at team level, so the pool is 1,000 GiB. Push 2,048 GiB of replication and backup traffic between those two machines.

| Path taken | Counted against the pool | Overage | Cost |
|---|---|---|---|
| Public IPv4 between the two Droplets | 2,048 GiB | 1,048 GiB | **$10.48** |
| VPC private interface between the two Droplets | 0 GiB | 0 GiB | **$0.00** |

At $0.01 per GiB overage, the same 2,048 GiB is $10.48 one way and zero the other — a monthly swing of $125.76 a year for a configuration change. Run the same test on a $6.00/month pair (1,000 GiB each, 2,000 GiB pool) and the overage drops to 48 GiB, or $0.48, because the pool is bigger; at $12.00/month (2,000 GiB each) it vanishes entirely. **The cheaper your VPS deal, the more the private interface is worth to you** — the $4.00 plan has the smallest pool and the largest exposure.

On Hetzner both rows are $0. Same traffic, same hosts, no private network needed.

## The counter-intuitive part: at Hetzner, the private network saves you no bandwidth at all

Follow the definitions to their end and you get a result that sounds wrong until you check it:

1. Hetzner bills only *outgoing* traffic, and outgoing is defined as traffic to the internet **plus** traffic to cloud servers in *different* network zones via public IPs.
2. Traffic to cloud servers in the *same* network zone is already internal — free — even over public IPs.
3. A Network cannot span zones: *"you can connect instances from our locations in Falkenstein, Nuremberg and Helsinki to the same Network. Please note, however, that all locations within a Network have to be from the same network zone as the subnet. All subnets within a Network also have to be from the same network zone."*
4. Therefore the only Hetzner traffic that is billable between two of your own servers is cross-zone traffic — and step 3 says a Network can never carry it.

**So there is no Hetzner traffic pattern that moves from "billed" to "free" by putting it on a private Network.** Everything a Network could carry is already free; everything that is billed cannot be put on one. The Network buys you isolation, RFC 1918 addressing, and the option to drop a public IPv4 — not a cheaper bandwidth line.

What it *does* buy is real money on the IP side. Hetzner's billing FAQ is explicit that separating Primary IPs from servers was done *"for this reason... the ability to reduce costs by removing the IPv4 address,"* and that *"Cloud servers without a Primary IPv4 cost less than before."* A backend node with no public IPv4, reached through the Network from a jump host, is a cheaper node. That is the Hetzner saving — **IP addresses, not traffic.**

The zone geography makes this concrete. Hetzner publishes four network zones and six locations: `eu-central` covers Falkenstein (fsn1), Helsinki (hel1) and Nuremberg (nbg1); `us-east` is Ashburn (ash); `us-west` is Hillsboro (hil); `ap-southeast` is Singapore (sin). Only one of the four zones has more than one location, so multi-location private networking exists in exactly one place — and the same-zone public-IP rule already made it free there.

## The wall you hit when traffic leaves the building

DigitalOcean will carry your private traffic between datacenters. It just charges you for it, at *"Bandwidth between peered VPC networks in two different datacenters costs $0.01 per GiB."*

That number is the same as DigitalOcean's public overage rate of *"$0.01 per GiB"* for Droplets. A private, non-internet-routable, VPC-isolated link between two datacenters costs **exactly what public egress costs**. Peering is a security and topology feature here, not a discount.

| Monthly cross-datacenter private traffic | DigitalOcean peering cost | Hetzner (same zone) |
|---|---|---|
| 100 GiB | $1.00 | €0 — but only inside one zone |
| 1,000 GiB | $10.00 | €0 |
| 1,024 GiB (1 TiB) | $10.24 | €0 |
| 5,000 GiB | $50.00 | €0 |
| Cross-zone (e.g. eu-central → us-east) | — | **Not possible on a Network**; billed as outgoing at €1 ($1.20) per TB in 100 MB blocks |

Two fine print items on the DigitalOcean side. *"We do not support individual VPC networks that span between datacenter regions"* — you need a peering connection, not one big network. And *"VPC peering between datacenters is not available in BLR1."*

## The NAT gateway trap: $40.00/month, and your included transfer does not apply

Here is the number that should stop you before you provision a "private" cluster on DigitalOcean.

From the VPC pricing page: *"NAT Gateways cost $40.00 per month per increment of size. Each increment provides 2 Gbps of symmetrical bandwidth and includes 100 GiB of outbound data transfer per month. Inbound data transfer is free. Outbound data transfer beyond the included amount costs $0.01 per GiB."* And then the sentence that does the damage: *"Any existing Droplet data transfer allotment does not apply to traffic through NAT gateways."*

Put those together with the $0.01/GiB public overage rate. If G GiB of egress goes through the gateway and G would otherwise have fit inside your Droplet's allowance:

```
NAT cost      = $40.00 + max(0, G − 100) × $0.01
Public cost   = $0.00                        (inside the plan's allowance)
Premium       = $39.00 + $0.01 × G
```

| Monthly egress | NAT gateway bill | Same traffic on the Droplet's own public interface | Premium |
|---|---|---|---|
| 500 GiB (the $4 plan's whole allowance) | $44.00 | $0.00 | **$44.00** |
| 1,000 GiB | $49.00 | $0.00 | **$49.00** |
| 3,000 GiB | $69.00 | $0.00 | **$69.00** |
| 6,000 GiB | $99.00 | $0.00 | **$99.00** |

The marginal rate on the gateway equals the public overage rate, so the gateway never becomes the cheaper pipe — it only adds a floor. That $40.00 floor is worth **4,000 GiB** of overage at DigitalOcean's own rate, and the 100 GiB credit that comes with it is worth **$1.00**. You are paying $39.00/month for the thing the gateway actually sells: *"Each NAT gateway receives a single static public IP address for outbound traffic,"* which *"remains static for the lifetime of the NAT gateway resource."*

Buy it for that reason — a stable egress IP for an allowlist at a partner, or for genuinely private Droplets. DigitalOcean does sell those: *"Private Droplets are Droplets with VPC-only networking and no direct public connectivity,"* diagrammed with `eth0: Private IPv4 Only`, and they route out through the gateway automatically when it is the VPC default. If you need that, the $40.00 is the price of admission. If you just wanted "private networking," it is $468/year for nothing.

Sizing is $20.00 per Gbps per month ($40.00 ÷ 2 Gbps), and the size stepper goes 1–5, so the ceiling is $200.00/month for 10 Gbps and 500 GiB. For comparison, DigitalOcean's Partner Network Connect — a real cross-connect, priced *"based on the selected maximum bandwidth"* with *"no additional cost for data transfer"* — runs $840/month for 1 Gbps, $1,540 for 2, $2,520 for 5 and $3,850 for 10. Per Gbps that is $840, $770, $504 and $385: the unit price falls **2.18x** from the smallest to the largest tier. Against metered public egress at $0.01/GiB, a 1 Gbps port breaks even at **84,000 GiB/month**, which is a **278 Mbps** average — about 28% of the port. Above that, the cross-connect wins; below it, metered egress does.

## Capacity: how many machines can actually talk

Both hosts cap the private network hard, and the caps are not on the same axis either.

| Limit | DigitalOcean | Hetzner |
|---|---|---|
| Networks per server | **1** — "Resources do not currently support multiple private network interfaces and cannot be placed in multiple VPC networks" | **3** — "Up to 3 networks per server"; the FAQ adds "For technical reasons, it is not possible to increase this limit" |
| Resources per network | **10,000** — "VPC networks only support up to 10,000 resources, even if the subnet size allows for more" | **100** — "Up to 100 attached resources (servers & Load Balancers) per Network" |
| Subnets per network | Additional subnets must be RFC 1918 with a prefix between `/16` and `/28` | **50** — "Up to 50 subnets per Network" |
| Routes per network | Not published; static routes support one target URN each; VPC-scoped routes are read-only | **100** — "Up to 100 routes per Network" |
| Extra addresses per server | Not offered — one private interface | **5** alias IPs — "Up to 5 alias IPs in addition to the private main IP per server" |

Multiply the reach: Hetzner's 3 networks × 100 attached resources gives a ceiling of **300** peers per server; DigitalOcean's single VPC gives **10,000**. That is a **33x** difference in the direction most people do not expect — the host with the bigger per-network cap is the one that lets you join only one.

Two operational landmines sit inside those numbers. Hetzner's alias IPs must be configured by hand: *"You will have to configure these IP addresses manually; the DHCP cannot provide them."* DigitalOcean locks subnet membership at birth: *"Subnet membership is set when you create a resource. You cannot move a resource to a different subnet after creation."*

## Address planning: 19 reserved ranges on one side, one awkward /32 on the other

DigitalOcean publishes its reserved space explicitly, and there is a lot of it. Globally reserved in every region: `10.244.0.0/16`, `10.245.0.0/16`, `10.246.0.0/24` and `10.229.0.0/16`. Then a per-region /16 for each of the 15 regions in its own table — AMS2, AMS3, ATL1, BLR1, FRA1, LON1, NYC1, NYC2, NYC3, SFO1, SFO2, SFO3, SGP1, SYD1 and TOR1. That is **4 + 15 = 19** reserved CIDRs, and you also may not overlap any other subnet on your team: *"The IP range cannot overlap with the IP range of any other subnet on your team."*

Hetzner reserves less, but one entry is a live trap. Its Networks FAQ lists three: the first IP of your network range, the network and broadcast addresses of any subnet, and *"The special private IP address `172.31.1.1`. This IP address is being used as a default gateway of your server's public network interface."* Note where that sits — inside `172.16.0.0/12`, which Hetzner itself lists as one of the three valid Network ranges (*"`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`"*). Pick the /12 and one address in the middle of it belongs to your public interface.

Two more constraints that shape designs: Hetzner's Networks are *"a layer 3 feature... Networks only support IPv4,"* and *"Since Networks are a layer 3 feature, you can only use the IP addresses allocated by the backend"* — no bringing your own addressing. DigitalOcean's NAT gateway *"does not support custom routing policies"* and *"IPv6 is not supported."* And on neither host is private traffic encrypted by default: Hetzner states plainly that *"Traffic between cloud servers inside a Network is private and isolated, but not automatically encrypted. We recommend you use TLS or similar protocols."*

## One DNS setting that moves you from billed to free

DigitalOcean has a second, quieter private lane that is worth knowing about because it is controlled by a resolver setting rather than by a network.

From the bandwidth billing page: *"Droplets that use the VPC-local DNS resolver can access Spaces buckets over DigitalOcean's internal network instead of the public internet. When a Droplet resolves a Spaces URL through the VPC-local DNS resolver, the request is routed privately and does not count against your Spaces outbound transfer allowance."* Followed by the warning: *"Droplets that use external DNS resolvers (such as Google or Cloudflare) resolve Spaces URLs to the public endpoint, and standard bandwidth billing applies."*

Choosing 1.1.1.1 over DigitalOcean's resolver is, on a Spaces-heavy workload, a billing decision. The fine print: cross-datacenter private Spaces routing works only inside three region groups — AMS (AMS2, AMS3), NYC (NYC1, NYC2, NYC3) and SFO (SFO1, SFO2, SFO3). Of the 15 regions in DigitalOcean's own table, **8** are in a group and **7** are not. And note the asymmetry that catches people: *"Traffic from Droplets to Spaces does not count against your Spaces outbound transfer allowance... but does currently count against your Droplets' outbound transfer allowance."*

Also worth knowing before you plan a peering migration: *"Droplets created before 2 October 2024 require manual updates to enable VPC peering traffic,"* and DOKS worker nodes from the same era need recycling. The same 2024-10-02 date appears in the subnets guide: a Droplet created before its VPC had more than one subnet needs its network service restarted, and one created before that date, or using a custom image, needs routes added manually.

## What we could not verify

Three of the hosts on this list publish nothing we could read on 2026-10-25, and we are not going to guess for them.

- **Namecheap** — `namecheap.com/hosting/vps/` returned **HTTP 403** to this machine. No private-network pricing, no allowance policy, nothing. Not verifiable.
- **Liquid Web** — `liquidweb.com/vps-hosting/packages/` returned **HTTP 403**. Its plan cards list 5 TB, 7 TB and 10 TB of bandwidth and a "10 GB network," but nothing about private networking or whether internal traffic is metered. Not verifiable.
- **Hostinger** — `hostinger.com/vps-hosting` returned **HTTP 200** and was fully readable, and it contains no private-network, VPC or internal-traffic terms anywhere in the page. That is an absence of an answer, not an answer. Not verifiable.

Per house rules we did not switch user agents, use a proxy, or work around any of those blocks.

## What to do with this on Monday

1. **On DigitalOcean, move east-west traffic onto the private interface today.** Any Droplet-to-Droplet replication, backup or database traffic currently aimed at a public IPv4 is consuming the pooled allowance. Confirm the target is the private address, not a hostname that resolves to the public one.
2. **Do the same for IPv6.** *"All IPv6 traffic uses the public interface."* IPv6 does not exempt you.
3. **On Hetzner, do not build a Network to save bandwidth — it will not.** If your servers are in the same network zone, their public-IP traffic is already internal and free. Build the Network for isolation, or to drop a public IPv4 from backend nodes and pay less per server.
4. **Before peering two DigitalOcean datacenters, price it at $0.01/GiB.** It is the public overage rate. A monthly 1 TiB inter-region sync is $10.24 — cheap, but not free, and it arrives as a line item.
5. **Do not buy a NAT gateway to save money.** Run the formula: premium = $39.00 + $0.01 × GiB. Buy it for the static egress IP, or because you are running Private Droplets that have no public interface at all.
6. **Check your capacity ceiling against the 300 vs 10,000 gap** before designing a flat network. Hetzner's 3-networks-per-server cap is documented as impossible to raise; DigitalOcean's 10,000-resource cap is per network and you only get one network per resource.
7. **If you use Spaces, point your Droplets at the VPC-local DNS resolver.** External resolvers send that traffic out the public endpoint and onto the bill.

Every figure above was read from the pages listed below on 2026-10-25. Recompute them against those pages before you sign anything — they change, and two of the Hetzner pages in this set had not been touched in years.
