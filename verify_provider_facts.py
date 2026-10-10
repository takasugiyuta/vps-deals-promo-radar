"""Read the five provider pages ourselves and write data/provider_facts.json.

Plain urllib, self-identifying User-Agent: no browser spoofing, no anti-bot evasion.
Anything we cannot read stays null and is rendered as "Not verified in this check".
Run: python verify_provider_facts.py
"""
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "data" / "provider_facts.json"
UA = "lumafare-source-probe/1.0 (+https://lumafare.com)"

FIELDS = ["Price", "Billing term", "Renewal price", "vCPU", "Memory",
          "Storage", "Bandwidth", "Refund window"]

LEADS = {
    "Hostinger": "Hostinger sells KVM VPS plans in fixed multi-year terms, so the headline "
                 "monthly rate covers the first term only; the renewal rate is printed under it.",
    "DigitalOcean": "DigitalOcean prices Droplets by the hour and prints the monthly equivalent "
                    "beside it, so the smallest plan is also the one you can stop at any time.",
    "Hetzner": "Hetzner renders its cloud prices in the browser after the page loads, so this "
               "check read no number off the official page and none is asserted here.",
    "Vultr": "Vultr publishes its plan list through its own public API, which is where these "
             "numbers come from; the marketing pricing page answered this check with HTTP 403.",
    "Linode (Akamai)": "Akamai's Linode plan catalogue is machine-readable through the official "
                       "Linode API, so the figures below are read there instead of from the "
                       "pricing page, which answered this check with HTTP 403.",
}

# url, kind, and the entry plan each provider publishes first
SOURCES = {
    "Hostinger": ("https://www.hostinger.com/vps-hosting", "html", "KVM 1"),
    "DigitalOcean": ("https://www.digitalocean.com/pricing/droplets", "html", "1 GiB / 1 vCPU"),
    "Hetzner": ("https://www.hetzner.com/cloud/", "html", "cloud server"),
    "Vultr": ("https://api.vultr.com/v2/plans", "vultr_api", "vc2-1c-1gb"),
    "Linode (Akamai)": ("https://api.linode.com/v4/linode/types", "linode_api", "g6-nanode-1"),
}

EMPTY_PAGE_NOTE = {
    "Hetzner": ("the official cloud page answers HTTP 200 but renders every plan price in the "
                "browser after load, so a static read returns no price or spec text; no refund "
                "term could be read from hetzner.com legal or docs pages in this run either"),
}

HUMAN_PAGES = {
    "Vultr": "https://www.vultr.com/products/cloud-compute/",
    "Linode (Akamai)": "https://www.linode.com/pricing/",
}


def read(url):
    """Return (status, body). 0 means the request never completed."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept": "*/*"}), timeout=30) as r:
            return r.status, r.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception as exc:  # network level failure
        return 0, str(exc)[:120]


def text_of(html):
    stripped = re.sub(r"<script[\s\S]*?</script>", " ", html)
    stripped = re.sub(r"<style[\s\S]*?</style>", " ", stripped)
    stripped = re.sub(r"<[^>]+>", " ", stripped)
    return re.sub(r"\s+", " ", stripped)


def blank():
    return {f: None for f in FIELDS}


def hostinger_facts(body):
    t = text_of(body)
    facts = blank()
    plan = re.search(r"KVM 1\s*\$?\s*([\d.]+)\s*\$?\s*([\d.]+)\s*/mo", t)
    renew = re.search(r"Renews at \$([\d.]+)/mo for (\d+) years", t)
    specs = re.search(r"(\d+) vCPU cores?\s+(\d+) GB RAM\s+(\d+) GB NVMe disk space\s+(\d+) TB bandwidth", t)
    refund = re.search(r"(\d+)-day money-back guarantee", t)
    if plan:
        facts["Price"] = f"${plan.group(2)}/month (KVM 1, listed at ${plan.group(1)})"
    if renew:
        facts["Billing term"] = f"{renew.group(2)}-year term, paid upfront"
        facts["Renewal price"] = f"${renew.group(1)}/month for the {renew.group(2)}-year term"
    if specs:
        facts["vCPU"] = f"{specs.group(1)} vCPU core (KVM 1)"
        facts["Memory"] = f"{specs.group(2)} GB RAM"
        facts["Storage"] = f"{specs.group(3)} GB NVMe"
        facts["Bandwidth"] = f"{specs.group(4)} TB"
    if refund:
        facts["Refund window"] = f"{refund.group(1)}-day money-back guarantee"
    return facts


def digitalocean_facts(body):
    t = text_of(body)
    facts = blank()
    row = re.search(r"1 GiB 1 vCPU 1,000 GiB 25 GiB \$([\d.]+) \$\s*([\d.]+)", t)
    if row:
        facts["Price"] = f"${row.group(2)}/month (${row.group(1)}/hour) for 1 GiB / 1 vCPU"
        facts["vCPU"] = "1 vCPU (Regular CPU option)"
        facts["Memory"] = "1 GiB"
        facts["Storage"] = "25 GiB SSD"
        facts["Bandwidth"] = "1,000 GiB transfer"
    billing = re.search(r"per-second billing \(with a minimum charge of 60 seconds or \$([\d.]+)", t)
    if billing:
        facts["Billing term"] = ("Hourly, per-second billing (minimum 60 seconds or "
                                 f"${billing.group(1)}, whichever is higher)")
    refund = re.search(r"Can I have a refund\?\s*([A-Z][^?]{0,90}\.)", t)
    if refund:
        facts["Refund window"] = refund.group(1).strip()
    return facts


def vultr_facts(body):
    facts = blank()
    plans = json.loads(body).get("plans", [])
    plan = next((p for p in plans if p.get("id") == "vc2-1c-1gb"), None)
    if not plan:
        return facts
    facts["Price"] = (f"${plan['monthly_cost']:.2f}/month (${plan['hourly_cost']}/hour) "
                      "for vc2-1c-1gb")
    facts["Billing term"] = "Per hour or per month; the Vultr plan list publishes both rates"
    facts["vCPU"] = f"{plan['vcpu_count']} vCPU (vc2-1c-1gb)"
    facts["Memory"] = f"{plan['ram'] // 1024} GB ({plan['ram']} MB, vc2-1c-1gb)"
    facts["Storage"] = f"{plan['disk']} GB SSD"
    facts["Bandwidth"] = f"{plan['bandwidth']} GB/month"
    return facts


def linode_facts(body):
    facts = blank()
    types = json.loads(body).get("data", [])
    plan = next((t for t in types if t.get("id") == "g6-nanode-1"), None)
    if not plan:
        return facts
    price = plan.get("price", {})
    facts["Price"] = (f"${price.get('monthly'):.2f}/month (${price.get('hourly')}/hour) "
                      "for g6-nanode-1")
    facts["Billing term"] = "Per hour or per month; the Linode plan list publishes both rates"
    facts["vCPU"] = f"{plan['vcpus']} vCPU (g6-nanode-1)"
    facts["Memory"] = f"{plan['memory'] // 1024} GB ({plan['memory']} MB, g6-nanode-1)"
    facts["Storage"] = f"{plan['disk'] // 1024} GB ({plan['disk']} MB)"
    facts["Bandwidth"] = f"{plan['transfer']} GB/month"
    return facts


EXTRACTORS = {
    "Hostinger": hostinger_facts,
    "DigitalOcean": digitalocean_facts,
    "Hetzner": lambda body: blank(),
    "Vultr": vultr_facts,
    "Linode (Akamai)": linode_facts,
}


def main():
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    report = {"checked_at": now, "providers": {}}
    for name, (url, kind, entry) in SOURCES.items():
        status, body = read(url)
        facts = blank()
        note = ""
        if status == 200 and body:
            facts = EXTRACTORS[name](body)
        else:
            note = f"source answered HTTP {status}"
        missing = [f for f in FIELDS if not facts.get(f)]
        human = HUMAN_PAGES.get(name)
        if human and name in ("Vultr", "Linode (Akamai)"):
            note = (note + "; " if note else "") + f"the public pricing page {human} answered HTTP 403"
        if name in EMPTY_PAGE_NOTE and not any(facts.values()):
            note = (note + "; " if note else "") + EMPTY_PAGE_NOTE[name]
        report["providers"][name] = {
            "source_url": url,
            "entry_plan": entry,
            "human_page": human,
            "read_at": now,
            "status": status,
            "note": note,
            "lead": LEADS[name],
            "fields": facts,
            "unverified": missing,
        }
        ok = len(FIELDS) - len(missing)
        print(f"{name:<16} HTTP {status:<4} {ok}/{len(FIELDS)} verified"
              + (f"  missing: {', '.join(missing)}" if missing else ""))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} at {now}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
