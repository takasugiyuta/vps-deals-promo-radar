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

This document is the canonical repository reference for the article URL convention.
