# vps-deals

English-language static VPS promotion directory using only official provider sources. No offers or prices are fabricated. If `.ilang/site.ilang` has no provider rows, the scraper falls back to the official discovery candidates in that same file. An empty first run is valid when no explicit promotion links are found.

- Site: https://vps-deals-promo-radar.pages.dev
- Edit sources: `.ilang/site.ilang`
- Build: `python build.py`
- Refresh: `python scraper.py`
- No affiliate links are active until approved tracking links and terms are supplied by the owner.

The `lumafare.com` custom-domain step is intentionally deferred until the initial `pages.dev` deployment is live and verified.

Cloudflare Pages settings: build command `python build.py`; output directory `site`; connect the public GitHub repository and deploy its `main` branch. GitHub Actions refreshes official sources every six hours.

The site rules are described using the I-Lang protocol in `.ilang/site.ilang`; protocol information: https://ilang.ai
