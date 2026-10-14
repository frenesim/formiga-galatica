# Phase 1: Technical fixes

Make the site readable by AI crawlers and tell search engines it's a local business.

## Tasks

- [ ] **Unblock AI crawlers in Cloudflare** (Humberto). Cloudflare dashboard → `galaticos.pt` → Security → Bots / AI Crawl Control: turn off "Block AI bots" (or allow GPTBot, ClaudeBot, OAI-SearchBot, Claude-SearchBot, Google-Extended, PerplexityBot, Applebot).
  Verify: `curl -s -o /dev/null -w "%{http_code}" -A "GPTBot" https://formiga.galaticos.pt/` returns 200 (same for ClaudeBot).
- [ ] **LocalBusiness structured data** (Claude). `ProfessionalService` JSON-LD in the layout: legal name, NIPC (`taxID`), address or service area, `areaServed` (Almada, Seixal, Barreiro, Setúbal, Sesimbra, Lisboa), phone, email, opening hours, founder (Person, `sameAs` LinkedIn), `sameAs` links, `knowsLanguage` pt/en.
  Needs: address decision + opening hours (see open questions).
- [ ] **Location in titles and descriptions** (Claude). E.g. home `<title>`: "Consultoria informática em Almada e Setúbal para pequenas empresas | Formiga Galática". Update `description` in `_config.yml` and per page.
- [ ] **hreflang** PT↔EN using `alt_url`, plus `x-default` → PT (Claude).
- [ ] **`og:locale` = `pt_PT` / `en_GB`** (Claude).
- [ ] **Share image** (1200×630) for WhatsApp/LinkedIn previews, set as `image` in `_config.yml` (Claude).
- [ ] **`llms.txt`** at the site root: plain-text summary of who we are, services, area served, portfolio, contacts (Claude).
- [ ] **`robots.txt`** explicitly allowing all crawlers and pointing to the sitemap (Claude).
- [ ] Validate with Google's [Rich Results Test](https://search.google.com/test/rich-results) and [Schema validator](https://validator.schema.org/) (Claude).

## Open questions

- Public street address in Almada, or a service-area business with no address shown?
- Opening hours to publish (e.g. Mon–Fri 9:00–18:00)?
