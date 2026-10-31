# Progress — Local SEO & AI visibility

Status: `todo` · `doing` · `done` · `blocked`

| Phase | Status | Notes |
|---|---|---|
| 1. Technical fixes | doing | Site changes and Cloudflare AI-bot setting done, opening hours confirmed. Waiting on: rich-results validation after deploy |
| 2. Get listed | todo | |
| 3. Content | todo | FAQ prices depend on the pricing model |
| 4. Reputation | todo | |
| 5. Measurement | todo | First baseline run after phase 1 |

## Blockers

- ~~**Phone +351 910 193 681 doesn't receive calls, SMS or WhatsApp messages** (reported 2026-10-14). It's a digital SIM (eSIM) used for a WhatsApp Business account; sending works, receiving doesn't. The number is published on every page (contact section, footer, JSON-LD, `llms.txt`) and Google Business Profile may verify by phone/SMS. See task in `02-get-listed.md`.~~ Resolved 2026-10-21: site now uses +351 911 045 538.

## Log

- 2026-10-31 — Cloudflare AI-bot block removed (GPTBot/ClaudeBot now 200, `robots.txt` unchanged by Cloudflare). Opening hours Mon–Fri 09:00–18:00 confirmed. SEO changes of 2026-10-30 committed and pushed (deploys via Pages).
- 2026-10-31 — Baseline snapshot of the live site saved in `snapshots/2026-10-31.md` (taken before the 2026-10-30 SEO changes were deployed). Re-run `python3 plans/local-seo-ai/snapshot.py` and diff to compare.
- 2026-10-30 — SEO pass: shorter keyword titles (home, diagnostic, notes), own description for `/notas/`, `author` on posts, BreadcrumbList + back link on notes, `lang="pt-PT"`, 404 page, Atom feed (`jekyll-feed`), footer links to diagnostic/notes, Google verification file kept out of `sitemap.xml`.
- 2026-10-21 — Phone/WhatsApp changed to +351 911 045 538 across the site and plan; phone blocker closed (pending end-to-end test of the new number).
- 2026-10-14 — Plan created. Baseline audit: GPTBot/ClaudeBot blocked (403) by Cloudflare; no local signals in metadata.

- 2026-10-14 — Phase 1 site changes: ProfessionalService JSON-LD (address, geo, areaServed, founder, offers), local titles/descriptions, hreflang PT/EN/x-default, og:locale pt_PT/en_GB, og:image, `llms.txt`, `robots.txt`, address in footer. GPTBot/ClaudeBot still 403 (Cloudflare).

## Monthly log

| Month | Search Console (impr./clicks) | GBP (calls/clicks) | AI prompts mentioning us (of 5 × 5 models) |
|---|---|---|---|
