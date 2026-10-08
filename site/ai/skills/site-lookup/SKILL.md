---
name: site-lookup
description: Search and read Lumafare public VPS deal and evaluation articles with source links.
---
# Lumafare site lookup

Use the read-only search and read API for published articles. Keep identifiers, dates, qualifiers, and source URLs intact. Answer in the visitor language, cite the article URL, and state unknowns without filling gaps. Do not infer current prices, discounts, or expiry dates.

Search: `GET /api/agent/articles?q=<terms>&limit=<1..10>`
Read: `GET /api/agent/articles?slug=<exact-slug>`
