# Local SEO & AI visibility

**Goal:** companies in Almada, Setúbal and the Setúbal peninsula find Formiga Galática when they search Google or ask an AI model (ChatGPT, Claude, Perplexity, Gemini, Copilot) for IT help.

**Started:** 2026-10-14

## Baseline (2026-10-14)

- Cloudflare blocks AI crawlers: `GPTBot` and `ClaudeBot` get **403**; Googlebot and PerplexityBot get 200.
- Titles, descriptions and structured data don't mention Almada or Setúbal. JSON-LD is a generic `WebSite`, not a local business.
- `sitemap.xml` exists (jekyll-sitemap). No hreflang, `og:locale` is `pt` (should be `pt_PT`), no share image, no `llms.txt`.
- No Google Business Profile, Search Console, Bing or Apple listings.

## Baseline 2026-11 (numbers to compare against)

Take this snapshot before the listings and content start to move results, then repeat the same checks monthly in the "Monthly log" of [PROGRESS.md](PROGRESS.md). Keep queries, prompts and date ranges identical so the numbers are comparable. Leave a cell as `n/a` when the source has no data, and write "not mentioned" rather than leaving AI answers blank.

Date taken: ____ · By: ____

| Source | Measure | Baseline | Notes |
|---|---|---|---|
| Search Console (`galaticos.pt`) | Impressions, last 3 months | | Check the date picker for data older than 2026-10-31 |
| Search Console | Clicks, last 3 months | | |
| Search Console | Average position | | |
| Search Console | Top 10 queries | | List them, with impressions |
| Search Console | Pages indexed (of 9 in the sitemap) | | Pages report |
| Business Profile insights | Searches, calls, website clicks, direction requests | `n/a` | Starts when the profile is verified (still pending, 2026-11-05) |
| Google search (private window) | Position, or absent, for "informática Almada", "consultoria informática Setúbal", "programas à medida Almada" | | Add or change terms only by adding new rows |
| Site visits (optional) | Visits per month | `n/a` | Only once an analytics tool is installed; no history before that |

AI answers (prompts 1–5 in [05-measurement.md](05-measurement.md), run in a fresh or logged-out session):

| Model | P1 | P2 | P3 | P4 | P5 | What it says about Formiga Galática, if anything |
|---|---|---|---|---|---|---|
| ChatGPT | | | | | | |
| Claude | | | | | | |
| Perplexity | | | | | | |
| Gemini | | | | | | |
| Copilot | | | | | | |

Use `yes` or `no` in the P1–P5 cells.

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

- Same name, address, phone and website everywhere (NAP consistency): **Formiga Galática** · humberto@galaticos.pt · +351 911 045 538 · https://formiga.galaticos.pt
- Copy follows the writing rules in `AGENTS.md` (no assumptions about readers, PT-PT without "você", verifiable claims only).
- No doorway pages: every location or sector page must have content specific to it.
