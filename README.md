# vps-deals

English-language static VPS promotion directory using only official provider sources. No offers or prices are fabricated. If `.ilang/site.ilang` has no provider rows, the scraper falls back to the official discovery candidates in that same file. An empty first run is valid when no explicit promotion links are found.

- Site: https://lumafare.com
- Edit sources: `.ilang/site.ilang`
- Build: `python build.py`
- Refresh: `python scraper.py`
- No affiliate links are active until approved tracking links and terms are supplied by the owner.

Custom domain selected from owner instruction: `lumafare.com`. Cloudflare must verify/control DNS before this canonical host can serve the site.

Cloudflare Pages settings: build command `python build.py`; output directory `site`; connect the public GitHub repository and deploy its `main` branch. GitHub Actions refreshes official sources every six hours.

The site rules are described using the I-Lang protocol in `.ilang/site.ilang`; protocol information: https://ilang.ai
