# Originality audit — /articles/compare-vps-deals-total-cost/ (2026-10-07)

Scope: the published body of `content/articles/compare-vps-deals-total-cost.md`.
Method: every body sentence was split out and checked against English-language pages
(provider docs, rival guides, calculators, backup/transfer explainers) for the same
claim, the same mechanic, or the same wording. A sentence counts as **exclusive** only
if the specific mechanic or wording is not published elsewhere in English. Generic
advice ("check renewal price", "backups matter", "port speed ≠ transfer allowance")
is counted as **common** even when our phrasing is tidier.

## Ratio

| | value |
|---|---|
| Numerator (exclusive words) | **406** |
| Denominator (total body words) | **1125** |
| Ratio | **36.1%** |

Denominator definition: body only — frontmatter excluded, link URLs excluded,
anchor text kept, section headings and the worksheet bullet list included
(1041 sentence words + 41 heading words + 43 bullet words = 1125).

## Exclusive sentences (21 blocks, 406 words)

1. `24w` If two VPS deals advertise different bundles, compare the server you can actually run and the recurring obligations you accept—not the headline alone.
2. `24w` Match CPU, memory, storage, and network terms to your workload; then check renewal billing, paid add-ons, management responsibility, backup and restore options, and region.
3. `13w` Put unknown terms in an “unverified” column instead of assuming they are included.
4. `19w` If a provider does not disclose a field, mark it unknown and decide whether you can accept that uncertainty.
5. `11w` This is a comparison method, not a benchmark claim.
6. `11w` Those are workload-based priorities, not promises about a provider’s performance.
7. `46w` "Use this worksheet:" + the six lines (base service for the chosen billing term / required management or control-panel options / backup, snapshot, or additional storage options / usage charges including outbound transfer / renewal terms and automatic-renewal behavior / taxes or checkout fees shown before payment).
8. `40w` The comparison formula: **cost for the chosen period = base service + required add-ons + usage-based charges + applicable taxes and fees.** Plus "This is a worksheet, not a quote; fill it only from the current plan page and checkout."
9. `9w` Do not treat a missing line item as free.
10. `30w` The practical lesson is to look for the event that ends billing and the term used for renewal; do not assume “stop” or “cancel” means the same thing across services.
11. `10w` These are examples of different bundles, not a universal ranking.
12. `10w` Translate that difference into work, not a made-up dollar amount.
13. `11w` If you cannot find a restore procedure, count recovery as unverified.
14. `26w` If a plan page uses one word without defining it, ask support or leave it marked unknown rather than turning the label into a performance promise.
15. `21w` Make one row per candidate with five columns: workload fit, continuing bill, management tasks, recovery path, and network or region limits.
16. `9w` Mark each item **verified**, **unknown**, or **does not fit**.
17. `14w` This simple status system prevents a polished offer card from hiding a missing term.
18. `12w` This is a hypothetical comparison, not a claim about a current offer.
19. `13w` Choose a VPS deal only after the checkout page agrees with your worksheet.
20. `26w` If a field changes between the plan card and checkout, use the checkout terms for the decision and verify the discrepancy with the provider before paying.
21. `27w` The “best deal” is the offer whose published resources, total obligations, and recovery path fit your use—not simply the one with the most attractive first line.

## What is deliberately NOT counted (common, found on other English pages)

- Renewal price is higher than promo price — covered by many English guides and renewal calculators.
- Managed vs unmanaged responsibility split — Namecheap/Liquid Web docs and dozens of guides.
- "Backup included" is not a recovery plan; retention/RPO questions — HostAdvice, usavps, bitvps.
- Port speed / transfer allowance / traffic policy are different things — server.hk, vps.do, rafftechnologies.
- All sourced provider facts (DigitalOcean powered-off billing, Namecheap lifecycle, Liquid Web bundles) — these come from the provider docs we cite.

## Reading

36% is the honest ceiling for a comparison-method article: the factual half must be
sourced, and sourced facts are by definition not exclusive. The exclusive part is the
operating system of the article — the worksheet, the formula, the five columns, the
verified/unknown/does-not-fit status, and the card-vs-checkout rule. That is the part
competitors would have to copy outright. Next article target: push the exclusive share
up by adding first-party data (our own offer table, dated), not by rewording the advice.

Caveat: the search tooling used for this audit returns a mixed Chinese/English index,
so "not found" means "not found in that index", not a legal-grade uniqueness claim.
