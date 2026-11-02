# Progress — Local SEO & AI visibility

Status: `todo` · `doing` · `done` · `blocked`

| Phase | Status | Notes |
|---|---|---|
| 1. Technical fixes | done | Rich-results test all green 2026-10-31 |
| 2. Get listed | doing | Started 2026-10-31. GBP waiting for video review (uploaded 2026-11-02). Bing/Apple not started. Copy in [02a-listing-copy.md](02a-listing-copy.md) |
| 3. Content | todo | FAQ prices depend on the pricing model |
| 4. Reputation | todo | |
| 5. Measurement | todo | First baseline run after phase 1 |

## Blockers

- ~~**Phone +351 910 193 681 doesn't receive calls, SMS or WhatsApp messages** (reported 2026-10-14). It's a digital SIM (eSIM) used for a WhatsApp Business account; sending works, receiving doesn't. The number is published on every page (contact section, footer, JSON-LD, `llms.txt`) and Google Business Profile may verify by phone/SMS. See task in `02-get-listed.md`.~~ Resolved 2026-10-21: site now uses +351 911 045 538.

## Log

- 2026-11-02 — Humberto uploaded the Google Business Profile verification video. Profile status in the manager now shows "Processing" (checked 2026-11-02); I don't know how long Google's review takes. Plan reviewed: GBP task rewritten (address shown, post-approval checklist), Bing Webmaster Tools can go ahead now, Bing Places and Apple wait for GBP, phase 3 FAQ notes updated for the new way of working. Still untested: phone end to end. Still uncommitted: all changes since f0b0fc0.
- 2026-11-01 — Way of working changed: no more "analysis → proposal with fixed price and date". The free diagnostic is a focused 30-minute conversation on what the visitor thinks would have the biggest impact; we pick the biggest problem solvable in a few weeks, start there and grow. Also rewrote the 2026-11-16 post (questions now: price and what it includes / start small / can stop after first step / ownership and monthly fees / after delivery / real work; "E nós?" matches the new concept) and its LinkedIn caption. Rewritten in PT/EN home ("Como trabalhamos", diagnostic section), diagnostic pages, `llms.txt` and `02a-listing-copy.md`. **Google Business Profile still has the OLD description and services text ("proposta com preço fechado e prazo") — update after verification.** Not yet committed.
- 2026-11-01 — Decision: address stays visible on Google/Bing/Apple. Clients can visit the office (first door of the house) by appointment. Site updated to say so: "no nosso escritório em Charneca da Caparica, por marcação" in `diagnostico-gratuito.md`, EN twin in `en/free-diagnostic.md`, and `llms.txt`. Not yet committed.
- 2026-10-31 — Business Profile wizard finished (verification deferred): services added (IT consulting + 6 custom), description (629/750) saved, photos/storefront/Ads credit/Workspace offers skipped. Open: hide address (home office, decided), confirm hours (wizard jumped ahead after Thursday; Friday not confirmed), secondary category, logo + cover photo, first post, video verification. Browser extension has no permission for www.google.com, where the profile editor lives.
- 2026-10-31 — Google Business Profile created under formigagalatica@gmail.com: name Formiga Galática, category Computer consultant, address shown (Rua Rogério Paulo, 14, 2820-505 Charneca da Caparica), service areas Almada/Seixal/Barreiro/Setúbal/Sesimbra/Lisboa, phone +351 911 045 538, website. Update notifications: No. Verification pending: Google offers video only. Still to fill: hours, description, services, secondary category, photos, first post.
- 2026-10-31 — Search Console: domain property `galaticos.pt` already verified. Sitemap submitted (Success, 9 pages discovered). Indexing requested for `/`, `/en/`, `/diagnostico-gratuito/`, `/notas/`; all four were "URL is unknown to Google" before the request.
- 2026-10-31 — Google account for the Business Profile: formigagalatica@gmail.com. Category names in the kit are unverified (could not be confirmed online); pick from the dropdown.
- 2026-10-31 — Phase 1 closed (rich-results all green). Phase 2 started: listing copy and order of work written in `02a-listing-copy.md`.
- 2026-10-31 — Cloudflare AI-bot block removed (GPTBot/ClaudeBot now 200, `robots.txt` unchanged by Cloudflare). Opening hours Mon–Fri 09:00–18:00 confirmed. SEO changes of 2026-10-30 committed and pushed (deploys via Pages).
- 2026-10-31 — Baseline snapshot of the live site saved in `snapshots/2026-10-31.md` (taken before the 2026-10-30 SEO changes were deployed). Re-run `python3 plans/local-seo-ai/snapshot.py` and diff to compare.
- 2026-10-30 — SEO pass: shorter keyword titles (home, diagnostic, notes), own description for `/notas/`, `author` on posts, BreadcrumbList + back link on notes, `lang="pt-PT"`, 404 page, Atom feed (`jekyll-feed`), footer links to diagnostic/notes, Google verification file kept out of `sitemap.xml`.
- 2026-10-21 — Phone/WhatsApp changed to +351 911 045 538 across the site and plan; phone blocker closed (pending end-to-end test of the new number).
- 2026-10-14 — Plan created. Baseline audit: GPTBot/ClaudeBot blocked (403) by Cloudflare; no local signals in metadata.

- 2026-10-14 — Phase 1 site changes: ProfessionalService JSON-LD (address, geo, areaServed, founder, offers), local titles/descriptions, hreflang PT/EN/x-default, og:locale pt_PT/en_GB, og:image, `llms.txt`, `robots.txt`, address in footer. GPTBot/ClaudeBot still 403 (Cloudflare).

## Monthly log

| Month | Search Console (impr./clicks) | GBP (calls/clicks) | AI prompts mentioning us (of 5 × 5 models) |
|---|---|---|---|
