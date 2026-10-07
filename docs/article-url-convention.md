# Article URL Convention

**Status:** Locked  
**Locked on:** 2026-10-07

## Final paths

- Public URL: `/articles/<slug>/`
- Markdown source: `content/articles/<slug>.md`
- Generated page: `site/articles/<slug>/index.html`

The article renderer, homepage links, breadcrumbs, and sitemap use the same `/articles/` prefix. The builder discovers Markdown files from `content/articles/` and registers each generated public URL in `sitemap.xml`.

## Why this is locked

The first article has already been published at `/articles/compare-vps-deals-total-cost/`. Published URLs should not be changed because doing so would break existing links and references. Any future prefix or source-directory change requires the owner's written approval. If an approved change moves published URLs, add and verify a permanent 301 redirect for every affected published address.

## Publishing must go through CI

**Status:** Locked
**Locked on:** 2026-10-07

Every article must reach the public site through the GitHub Actions deploy job (`.github/workflows/update.yml`).
A release is only complete when all three exist:

1. **A commit** — the Markdown lands in `content/articles/`, the built page lands in `site/`.
2. **A run record** — the workflow runs via `workflow_dispatch` or `schedule`, and both the refresh and deploy jobs are green.
3. **A live check** — the article URL returns 200, the sitemap count increases by one, and the canonical matches the public URL.

**Do not publish with the local wrangler CLI.** Direct pushes leave no deployment record: when something breaks there is no way to tell who deployed, when, or which revision went out. The local wrangler install stays available as an **emergency rollback** tool only (for example, to pull the site back to the previous version after a bad release). After any emergency rollback, state what was done and follow up with a normal CI deploy so the record is complete.

### Fixed release order

1. `git fetch` then `git pull --rebase origin main`
2. Write the article to `content/articles/<slug>.md`, then run `python build.py` (do not run `scraper.py`)
3. Push normally; never force-push
4. `gh workflow run update.yml --repo takasugiyuta/vps-deals-promo-radar --ref main`
5. `gh run watch <run_id>` and confirm both jobs are green
6. Verify live: article URL 200, sitemap count, the five legacy `/deals/` 301s, and page timestamps matching the repository HEAD
7. Report the commit hash and the run id together

This document is the canonical repository reference for the article URL convention and the release path.
