---
title: "Cheap VPS Deals: How Long Your Data Survives After You Cancel — and the One Copy Each Host Keeps"
slug: vps-deals-data-kept-after-cancel
date: 2026-10-18
description: "Read off five hosts' own pages on 2026-10-18: not one of them publishes a retention period for your VPS disk. What they publish is a retention period for backups only — DigitalOcean 4 weeks for weekly and 7 days for daily, Hetzner 7 rolling slots, Namecheap one weekly copy that overwrites itself — and a moment of deletion. Hetzner writes it out plainly: 'we will immediately delete your data... We cannot recover your data after you cancel the product.' Namecheap will erase 'at once' on request. Hostinger may 'destroy any data and files (including back-up copies)' with 'no obligation to provide.' Plus the arithmetic that actually saves you: on every one of DigitalOcean's 29 Standard/Intel/AMD tiers, a permanent snapshot of a full disk costs less than switching on 7-day daily backups — 1.06x to 1.96x less."
question: If I cancel or destroy a cheap VPS, how long does the host keep my data, and can I get it back afterwards?
sources:
  - https://docs.digitalocean.com/support/how-do-i-recover-a-deleted-droplet/
  - https://docs.digitalocean.com/support/how-can-i-destroy-my-droplets-while-maintaining-my-backups/
  - https://docs.digitalocean.com/products/droplets/how-to/destroy/
  - https://docs.digitalocean.com/products/backups/details/pricing/
  - https://docs.digitalocean.com/products/snapshots/details/pricing/
  - https://docs.digitalocean.com/support/how-long-will-my-backup-or-snapshot-take-to-complete/
  - https://www.digitalocean.com/pricing/droplets
  - https://docs.hetzner.com/general/billing-and-account-management/cancellation/cancellations-overview/
  - https://docs.hetzner.com/general/billing-and-account-management/cancellation/30-days-to-the-end-of-the-month/
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/faq/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/10567/21/hosting-packages-life-cycle/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/170/21/how-do-i-cancel-my-hosting-account/
  - https://www.namecheap.com/support/knowledgebase/article.aspx/9197/21/how-can-i-reactivate-my-canceled-hosting-package/
  - https://www.hostinger.com/legal/universal-terms-of-service-agreement
  - https://www.hostinger.com/legal/privacy-policy
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off five hosts' own pages on 2026-10-18: zero of them publish a retention period for your VPS disk. Not one.** What they publish is (a) a retention period for *backups* — and only backups — and (b) a *moment* of deletion. Hetzner is the only one that writes the moment down in plain words: *"After you have finished the cancellation, we at Hetzner will immediately delete your data... We cannot recover your data after you cancel the product."* Namecheap offers you a button that erases *"at once."* Hostinger reserves the right to *"remove and destroy any data and files (including back-up copies)"* with *"no obligation to provide you with such data and files."* DigitalOcean's answer is a sentence most people only read after it is too late: *"If you have neither snapshots nor backups, then we do not have a backup of your Droplet's data available in our system."*

So the real question is not "how long do they keep it." It is **"which one copy is mine, and does it outlive the machine?"** On every host in this comparison the answer is the same shape: automatic backups are *bound to the server and die with it*, while a manually-created snapshot is *yours until you delete it and survives the server's death*. That single distinction — not the price, not the RAM — is what decides whether cancelling a $4/month VPS costs you nothing or costs you everything.

## The survival table — the whole article in one grid

| Host | Automatic backups | Do they survive deleting the server? | Manual snapshot | Published retention for the disk itself |
|---|---|---|---|---|
| **DigitalOcean** | Weekly or daily (also 4/6/12-hourly on usage-based plans) | **No** — must be converted to a snapshot first | Yes, kept until you delete it | **None published** |
| **Hetzner** | Daily, **7 slots** | **No** — *"automatically be deleted if you delete the server"* | Yes — *"remain available even if you delete the server"* | **None** — deletion is *"immediately"* |
| **Namecheap** | Weekly, **during the weekend**, overwritten by the next one | Effectively **no** — one rolling copy | Not offered on VPS | **None** — *"canceled at once and all the data erased immediately"* |
| **Hostinger** | Not documented publicly for VPS | Not documented | Not documented | **None** — *"destroy any data and files (including back-up copies)"* |
| **Liquid Web** | Acronis, **daily**, 100/250/500 GB by tier | Not published | Not mentioned on the page | **None published** |

Two things to notice. First, the "snapshot survives, backup dies" split is identical at DigitalOcean and Hetzner — the two hosts that actually document it. Second, the only host that tells you *when* the disk goes is Hetzner, and its answer is "immediately."

## How far back can you actually roll?

This is the number people think they are buying when they tick "enable backups." It is almost always smaller than they think, because **retention windows and restore points are two different things.**

| Host / plan | How often | How long kept | How many restore points | Worst-case data loss |
|---|---|---|---|---|
| DigitalOcean weekly | Weekly | **4 weeks** | **4** | 7 days |
| DigitalOcean daily | Daily | **7 days** | **7** | 24 hours |
| DigitalOcean usage-based | You choose (4h/6h/12h/daily/weekly) | **Custom** — you set it | Varies | Down to 4 hours |
| Hetzner Backups | Daily | 7 slots | **7** | 24 hours |
| Hetzner Snapshots | Manual | Until you delete it | Up to **30** across all projects | Whatever you last took |
| Namecheap VPS | Weekly, at the weekend | Overwritten each week | **1** | 7 days |
| Namecheap VPS + Complete Management | 3× per week, 100 GB included | Overwritten | 3 per week | ~2–3 days |
| Liquid Web (Acronis) | Daily | **Not published** | Not published | Unknown |

The trap is DigitalOcean weekly: *4 weeks* sounds like the safest option in the table, and it is the longest window — but it only ever holds **4** copies, so your worst case is a full week of missing writes. Daily gives you the same worst case (24 hours) with a *shorter* window. **Length of window and frequency of protection are independent, and the marketing names only tell you one of them.**

Hetzner's 7 slots and DigitalOcean's 7 days are the same number by two different routes: Hetzner caps by *count*, DigitalOcean caps by *age*. If you ever create extra backups on Hetzner, the count cap bites first — *"If all slots are full and you create an additional one, then the oldest Backup will be deleted."*

## The money math: the permanent copy is cheaper than the 7-day copy

This is the part nobody publishes, because it makes the upsell look silly. DigitalOcean prices backups as a **percentage of the Droplet** and snapshots as a **flat rate per GB**. Those two curves cross, and they cross in a place that is almost always on the snapshot's side.

- Backups, Basic plans: **20.0%** of the Droplet's cost per month (weekly), **30.0%** (daily).
- Snapshots: **$0.06 per GB per month**, minimum charge $0.01.

Break-even, solved for the disk you actually use:

```
0.30 × monthly_price  =  0.06 × used_GB
        used_GB       =  5 × monthly_price
```

**If the GB you are using is less than 5× your monthly Droplet price, a snapshot that lasts forever costs less than daily backups that expire in 7 days.**

Run it across every Standard / Intel / AMD tier on DigitalOcean's pricing page as read on 2026-10-18 (snapshot costed at a *full* disk — the most unfavourable case, since DO bills snapshots on actual disk usage):

| Droplet | Disk | $/mo | Daily backups (30%) | Full-disk snapshot @ $0.06/GB | Snapshot is cheaper by |
|---|---|---|---|---|---|
| 512 MiB / 1 vCPU | 10 GiB (10.74 GB) | $4.00 | $1.20 | $0.64 | **1.86x** |
| 1 GiB / 1 vCPU | 25 GiB (26.84 GB) | $6.00 | $1.80 | $1.61 | **1.12x** |
| 2 GiB / 1 vCPU | 50 GiB (53.69 GB) | $12.00 | $3.60 | $3.22 | **1.12x** |
| 2 GiB / 2 vCPU | 60 GiB (64.42 GB) | $18.00 | $5.40 | $3.87 | **1.40x** |
| 4 GiB / 2 vCPU | 80 GiB (85.90 GB) | $24.00 | $7.20 | $5.15 | **1.40x** |
| 8 GiB / 4 vCPU | 160 GiB (171.80 GB) | $48.00 | $14.40 | $10.31 | **1.40x** |
| 16 GiB / 8 vCPU | 320 GiB (343.60 GB) | $96.00 | $28.80 | $20.62 | **1.40x** |

Across **all 29 Standard, Intel and AMD tiers** listed on the page, the ratio runs from **1.06x to 1.96x** — the snapshot wins on every single one. The margin is thinnest on the 1 GiB and 2 GiB tiers (1.12x) and widest on the AMD 8 GiB / 2 vCPU tier (1.96x).

Two caveats, stated honestly. Snapshots are a *manual* action — a snapshot you forget to take protects nothing, whereas backups run on a clock. And the table charges the snapshot for a completely full disk; at realistic usage it is cheaper still, because DO says snapshots of Droplets are *"a best estimate based on the disk usage."*

The flip side matters too: usage-based backup plans price *per GiB* rather than as a percentage, and they get **cheaper the more often you back up** — $0.04/GiB weekly down to **$0.01/GiB** every 4 hours. That is a **4.0x spread** in the opposite direction from what intuition suggests, because you are paying for restorable file size, not for frequency.

## DigitalOcean's own two pages disagree — assume the shorter one

This is worth knowing before you rely on any of it. DigitalOcean's *How to Destroy a Droplet* page says:

> "Destroying a Droplet does not destroy its automated backups. Automated backups remain for **four weeks** after creation and then expire."

Its *How do I recover a deleted Droplet?* page says the backups *"remain available until the end of their retention period, which is **four weeks** for weekly backups, **seven days** for daily backups."*

Both are official and both are live. Read together, the safe assumption is **7 days if you were on daily**, because that is the number the recovery page — the one you would actually be using — commits to. The 4-week figure on the destroy page is the weekly-plan number stated without its qualifier. **Plan for 7, not 28.** The gap is 4x.

The escape hatch is explicit and it is free to know:

> "You can convert backups into snapshots to save the image indefinitely."

## Hetzner: the deletion clock depends on which day you click cancel

Hetzner's 30-days-to-the-end-of-the-month policy (doc ID GE-DB2BC) is the only cancellation rule in this comparison that produces a *date*. The rule: add 30 days to your cancellation date, then roll forward to the end of that month. Because the roll-forward crosses a month boundary, the result is **not a fixed 30 days** — and it is not even monotonic.

```
Let D  = day you cancel
    L  = days in the month you cancel
    L2 = days in the following month

If D + 30 <= L :  days = L - D
Else           :  days = (L - D) + L2
```

Worked from Hetzner's own three examples:

| Cancelling on | +30 days lands on | Takes effect | Total runway |
|---|---|---|---|
| 1 May | 31 May (still May) | 31 May | **30 days** |
| 17 May | 16 June | 30 June | **44 days** |
| 29 May | 28 June | 30 June | **32 days** |

Now extend the same rule to its extremes:

- **1 May → 30 days.** (1 + 30 = 31, still within May's 31 days.)
- **2 May → 59 days.** (2 + 30 = 1 June, which rolls to 30 June.)
- **1 April → 60 days.** (1 + 30 = 1 May, which rolls to 31 May.)

So the spread is **30 to 60 days — a 2.0x difference — decided entirely by which day of the month you click.** Cancelling on 1 May gives you 30 days; cancelling on 2 May gives you 59. **A one-day difference in when you click is a 29-day difference in when your data dies.**

And when it does take effect, Hetzner's cancellation overview (doc ID GE-4A989, last changed 2026-08-06) is unambiguous:

> "After you have finished the cancellation, we at Hetzner will immediately delete your data. So please be absolutely sure that you want to cancel your product. **We cannot recover your data after you cancel the product.**"

There is no grace period after that sentence. Which means on Hetzner the runway above *is* your export window, and you can add up to 29 days to it for the price of waiting one day before you cancel.

## Namecheap: 7 days, 23 days, or instantly — your choice, and the default is not the safe one

Namecheap's *Hosting packages life cycle* (KB 10567) gives the cleanest timeline in this comparison:

- Invoiced **7 days** before the billing date.
- An "Alert" flag appears **15 days** before expiry on 1- and 3-month cycles, **30 days** before on annual and 2-year cycles.
- If the invoice is still unpaid after the billing date: *"your hosting account will be suspended and cancelled **7 days** later (for Shared packages, VPS and Dedicated server) and **23 days** later (for Reseller packages)"* — a **3.29x** difference by product line.

But the cancellation article (KB 170) describes two completely different paths, and only one of them is what most people mean by "cancel":

1. **Default:** turn off auto-renew and let it expire — the package is suspended, then cancelled.
2. **On request:** *"if you wish to have your hosting package canceled at once and **all the data erased immediately**, you may submit a cancellation request."*

Both are one click in the same Manage screen. **If you cancel the VPS intending to come back for your data later, you have chosen the path that erases it now.**

What recovery looks like if you do lose it (KB 9197, updated 5/9/2025):

- VPS server backups are *"generated once a week, during the weekend"* and *"are over-written by newly created ones"* → **one copy, up to 7 days stale.**
- Restoring gives you *"a new IP address."* If anything hardcoded the old IP, restoration is not the end of the job.
- Data-only retrieval — getting your files *without* rebuilding the VPS — costs **$15** added to your Namecheap balance.
- Extra backup space on Complete Management: **$10 per 10 GB = $1.00/GB**, on top of 100 GB included.
- Dedicated servers: *"all data is deleted from the server,"* and it is *"impossible to obtain a backup for User-Responsible servers or servers with the Basic Management option."*

One genuinely counterintuitive line in that same article: external backup storage is **500 GB for Advanced** servers but **200 GB for Complete Management** servers. The higher management tier ships with **2.5x less** backup space.

## Hostinger publishes four retention numbers — none of them for your VPS disk

Hostinger is the clearest example of the pattern. Its privacy policy has a whole section titled *Retention and Deletion*, and it is full of specific, auditable numbers:

| What | Retention |
|---|---|
| Call and meeting recordings | **30 days** |
| Communication data (emails, requests) | **90 days** |
| Data from accounts suspended for safety | **up to one (1) year** |
| De-personalised profile after account closure (email rewritten to `user@deleted.com`) | as long as legally required (tax, accounting, AML) |

Then there is the disk. Hostinger's Universal Terms of Service gives it no number at all — only a right:

> "Hostinger may, in its sole and absolute discretion, remove and destroy any data and files (**including back-up copies**) stored by you on its servers, and has **no obligation to provide you with such data and files**."

Read those side by side and the shape of the whole market appears: **the retention periods that get published are the ones the host needs for its own compliance. The retention period you need is the one nobody writes down.** Hostinger will tell you exactly how long it keeps a recording of a support call (30 days) and will not tell you how long it keeps your server.

## Liquid Web: you can only back up part of the machine

Liquid Web's VPS page (read 2026-10-18) bundles Acronis backups into every package — *"Daily backups are configured for you and scale automatically with your package"* — and publishes the capacity per tier. Compare that capacity against the disk it is meant to protect:

| Package | vCPU / RAM / Disk | Acronis backup included | Backup ÷ disk | Disk you cannot back up |
|---|---|---|---|---|
| 8 GB | 4 vCPU / 8 GB / **240 GB** | **100 GB** | **41.7%** | **140 GB (58.3%)** |
| 16 GB | 6 vCPU / 16 GB / **440 GB** | **250 GB** | **56.8%** | **190 GB (43.2%)** |
| 32 GB | 8 vCPU / 32 GB / **640 GB** | **500 GB** | **78.1%** | **140 GB (21.9%)** |

**On the entry VPS, the included backup covers 41.7% of the disk.** Fill the machine and you are running unprotected on 58.3% of it. The ratio improves as you climb — 56.8%, then 78.1% — so backup coverage is a *tier feature*, not a baseline.

The page states no retention period, no snapshot capability, and nothing about data after cancellation. **Not verifiable:** Liquid Web's policies pages (`/policies/terms-of-service/` and `/legal/terms-of-service/`) returned a Cloudflare human-verification challenge to our direct requests on 2026-10-18, and per our own rules we did not attempt to work around it — so no claim about Liquid Web's post-cancellation data handling is made in this article beyond what its public VPS page states above.

## What the three comparison sites show you first

Checked on 2026-10-18, on the exact pages people land on:

- **LowEndBox** — homepage cards carry title, author, date, comment count and a teaser; provider, RAM, price and region appear only inside the free-text title, when they appear at all. **Zero** mentions of backups, snapshots, retention, or what happens to data after cancellation.
- **Namecheap** — the homepage has **no VPS card at all**; VPS is a navigation link only. Cards that *are* shown (EasyWP, Private Email, .com, Stellar) print promo and renewal prices. **Zero** mentions of backups, snapshots, retention or cancellation data handling.
- **Liquid Web** — `/vps-hosting/packages/` is the most informative of the three: it does name backups ("Automated backups", Acronis with per-tier GB). But it publishes **no retention period, no snapshot feature, and no cancellation or termination data policy.**

So the answer to "how long do they keep my data" is not available on any of the three first screens, and on only one of the five hosts' own documentation.

## Budget the clock before you cancel

One last practical number. DigitalOcean states that creating a snapshot or backup takes *"about 1 to 3 minutes per GB of used disk space"*, and gives the worked case: *"a Droplet with 10 GB of used disk space would take 10 to 30 minutes."*

That is a real, schedulable cost. On a 10 GB disk you need to decide to leave **20 minutes before** you destroy anything — and on a 320 GiB disk at the 3-minute end you are looking at several hours. Nobody loses data because they forgot to click; they lose it because they clicked destroy first and took the snapshot never.

## What to actually do

1. **Take a manual snapshot before you touch anything.** It is the only artefact at DigitalOcean and Hetzner that outlives the server. Hetzner says snapshots *"remain available even if you delete the server a Snapshot was taken of"*; DigitalOcean says you can *"convert backups into snapshots to save the image indefinitely."* Automatic backups do not count: on Hetzner they are *"automatically deleted if you delete the server."*
2. **On DigitalOcean, prefer the snapshot to daily backups on price alone** if your used GB is under **5× your monthly price** — true on all 29 tiers today (1.06x–1.96x cheaper). You get a longer retention for less money; the only thing you give up is automation.
3. **On Hetzner, look at a calendar before you cancel.** Cancelling on the 1st of a 31-day month gives you 30 days; cancelling one day later gives you 59. Same click, 29 extra days of runway. Deletion is immediate when the clock runs out, and it is not reversible.
4. **On Namecheap, do not use "Cancel Service" if you want your data.** That path erases *"at once."* Let it expire instead, and remember the VPS backup is one weekly copy made at the weekend — up to 7 days stale — and restoration hands you a **new IP**.
5. **Budget the snapshot time:** 1–3 minutes per GB of used space. Decide before you destroy, not after.
6. **If you are on Liquid Web's entry VPS, assume 58.3% of your disk is unprotected** unless you have reduced usage to fit the 100 GB included.

The general rule that survives every host in this comparison: **automatic backups are a feature of the server; a snapshot is a thing you own.** The first one is priced as a percentage and expires on a clock. The second one is priced per gigabyte and expires when you say so. On cheap VPS deals, where the whole machine costs less than a month of the data sitting on it, that is the only line item worth reading twice.
