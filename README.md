# Formiga Galática — website

Jekyll site for FORMIGAGALÁCTICA – Consultoria Informática, Lda. Deployed to GitHub Pages via `.github/workflows/pages.yml` on every push to `main`.

```sh
bundle install
bundle exec jekyll serve --livereload   # http://localhost:4000/formiga-galatica/
```

- PT pages at `/`, EN pages under `/en/` (`alt_url` front matter links the pair).
- Shared UI strings: `_data/i18n.yml`. Contact details: `company:` in `_config.yml`.
- New blog post: add `_posts/YYYY-MM-DD-slug.md` with `layout: post` and `lang: pt`.
