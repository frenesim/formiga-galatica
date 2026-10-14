# Local SEO & AI visibility

**Goal:** companies in Almada, Setúbal and the Setúbal peninsula find Formiga Galática when they search Google or ask an AI model (ChatGPT, Claude, Perplexity, Gemini, Copilot) for IT help.

**Started:** 2026-10-14

## Baseline (2026-10-14)

- Cloudflare blocks AI crawlers: `GPTBot` and `ClaudeBot` get **403**; Googlebot and PerplexityBot get 200.
- Titles, descriptions and structured data don't mention Almada or Setúbal. JSON-LD is a generic `WebSite`, not a local business.
- `sitemap.xml` exists (jekyll-sitemap). No hreflang, `og:locale` is `pt` (should be `pt_PT`), no share image, no `llms.txt`.
- No Google Business Profile, Search Console, Bing or Apple listings.

## Phases

| # | Phase | Owner | File |
|---|---|---|---|
| 1 | Technical fixes | Claude + Humberto | [01-technical-fixes.md](01-technical-fixes.md) |
| 2 | Get listed | Humberto | [02-get-listed.md](02-get-listed.md) |
| 3 | Local & sector content | Claude, with Humberto's input | [03-content.md](03-content.md) |
| 4 | Reputation | Humberto | [04-reputation.md](04-reputation.md) |
| 5 | Measurement (monthly) | Both | [05-measurement.md](05-measurement.md) |

Track status in [PROGRESS.md](PROGRESS.md).

## Ground rules

- Same name, address, phone and website everywhere (NAP consistency): **Formiga Galática** · humberto@galaticos.pt · +351 910 193 681 · https://formiga.galaticos.pt
- Copy follows the writing rules in `AGENTS.md` (no assumptions about readers, PT-PT without "você", verifiable claims only).
- No doorway pages: every location or sector page must have content specific to it.
