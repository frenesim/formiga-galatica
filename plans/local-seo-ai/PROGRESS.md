# Progress — Local SEO & AI visibility

Status: `todo` · `doing` · `done` · `blocked`

| Phase | Status | Notes |
|---|---|---|
| 1. Technical fixes | doing | Site changes done. Waiting on: Cloudflare AI-bot setting (Humberto), opening hours confirmation, rich-results validation after deploy |
| 2. Get listed | todo | |
| 3. Content | todo | FAQ prices depend on the pricing model |
| 4. Reputation | todo | |
| 5. Measurement | todo | First baseline run after phase 1 |

## Blockers

- **Phone +351 910 193 681 doesn't receive calls, SMS or WhatsApp messages** (reported 2026-10-14). It's a digital SIM (eSIM) used for a WhatsApp Business account; sending works, receiving doesn't. The number is published on every page (contact section, footer, JSON-LD, `llms.txt`) and Google Business Profile may verify by phone/SMS. See task in `02-get-listed.md`.

## Log

- 2026-10-14 — Plan created. Baseline audit: GPTBot/ClaudeBot blocked (403) by Cloudflare; no local signals in metadata.

- 2026-10-14 — Phase 1 site changes: ProfessionalService JSON-LD (address, geo, areaServed, founder, offers), local titles/descriptions, hreflang PT/EN/x-default, og:locale pt_PT/en_GB, og:image, `llms.txt`, `robots.txt`, address in footer. GPTBot/ClaudeBot still 403 (Cloudflare).

## Monthly log

| Month | Search Console (impr./clicks) | GBP (calls/clicks) | AI prompts mentioning us (of 5 × 5 models) |
|---|---|---|---|
