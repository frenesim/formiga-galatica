# AGENTS.md

Working guide for developers and AI agents editing this site. See `README.md` for setup.

## What this is

Website for FORMIGAGALÁCTICA – Consultoria Informática, Lda (brand: **Formiga Galática**), an IT consultancy in Almada that builds simple, made-to-measure tools for small businesses (offices & services, trades & workshops). Live at https://formiga.galaticos.pt (Jekyll, GitHub Pages, deployed by `.github/workflows/pages.yml` on push to `main`).

## Writing rules

- **Never make assumptions about what readers like, know or feel.** No "most people don't care about computers", "for people who don't like IT", "you don't need to understand…", "you'll be surprised". Describe concrete problems, what we do and what the client gets, and let readers decide how it applies to them.
- Plain language, no jargon: say "programas que paga todos os meses", not "SaaS"; "ferramenta feita à medida", not "custom software".
- Portuguese is European Portuguese (PT-PT). **Never use "você"** (reads as PT-BR or distant): drop the pronoun and use "o seu", third-person verbs and imperatives ("marque", "fale connosco"). English mirrors the Portuguese.
- Keep claims verifiable: portfolio facts come from the real projects (no features that aren't built yet).
- Every PT page has an EN twin linked through `alt_url` front matter.

## Structure

- PT pages at `/`, EN under `/en/`. Shared UI strings in `_data/i18n.yml`; contact details in `company:` in `_config.yml`.
- Style is Basecamp/37signals-plain: bold type, one accent colour, no stock images. Colours are CSS variables in `assets/css/style.css` with a dark-mode override.
- `timezone: Europe/Lisbon` in `_config.yml` matters: CI builds in UTC and would otherwise skip same-day posts as "future".

## Plans

Multi-step work lives in `plans/{plan-reference}/`: `00-index.md` (goal, baseline, phase table), numbered phase files with checkbox tasks, and `PROGRESS.md` (status table + dated log). Tick checkboxes and add a log line when a task is done. `plans/` is excluded from the Jekyll build.
