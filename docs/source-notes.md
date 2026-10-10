# How the provider figures are read

`verify_provider_facts.py` does the reading and writes `data/provider_facts.json`.
It uses plain urllib with a self-identifying User-Agent. No browser UA is faked and
no anti-bot control is worked around. Whatever a run cannot read stays `null` and is
rendered as "Not verified in this check".

| Provider | Entry point used | Why |
|---|---|---|
| Hostinger | https://www.hostinger.com/vps-hosting (static read) | plan table is in the HTML |
| DigitalOcean | https://www.digitalocean.com/pricing/droplets (static read) | price table is in the HTML |
| Hetzner | Chrome over the DevTools protocol + `website-price-api.hetzner.com` | the cloud page prints no number until JS runs; even then the price comes from a separate price service |
| Vultr | `https://api.vultr.com/v2/plans` | www.vultr.com answers HTTP 403 to this client |
| Linode (Akamai) | `https://api.linode.com/v4/linode/types` | www.linode.com/pricing/ answers HTTP 403 to this client |

## Browser reads (Hetzner)

The Hetzner cloud page renders plan rows only in a browser, and its prices come from
`https://website-price-api.hetzner.com/api/v1/products/<product-key>` — the same request
the page makes. Two captures are committed under `data/browser_reads/`:

- `hetzner_regular_performance.txt` — rendered text of
  https://www.hetzner.com/cloud/regular-performance/ (vCPU, RAM, disk, traffic per plan).
- `hetzner_terms.txt` — rendered text of
  https://www.hetzner.com/legal/terms-and-conditions/ (cancellation right, notice period).

How a capture is refreshed: open Chrome with remote debugging on port 9222, connect over
the DevTools protocol, navigate, let the page render, dismiss the cookie banner, then save
`document.body.innerText` to the matching filename and re-run
`python verify_provider_facts.py`.

Prices are read from the price API at run time, so they are current at each run; the two
captures are only re-taken when the plan rows or the legal text need re-reading.

## Promotion cards

A promotion card is published only when that plan's own discount, price, renewal price and
specs were read off the official page. A card that would carry a discount name with no
number is dropped instead of published.
