# CLAUDE.md

Instructions for Claude Code working in this repository. Read `AGENTS.md` first: it holds the writing rules, site structure and plan conventions, and it applies in full. `README.md` covers local setup.

## Branches

- All development happens on `main`. Do not create `dev` or feature branches unless the user asks for one.
- Commit to `main` directly when the user asks for a commit.

## Publishing

- Pushing `main` deploys the live site (https://formiga.galaticos.pt) through `.github/workflows/pages.yml`. The same workflow also runs daily at 06:00 UTC.
- Do not `git push` unless the user explicitly asks for it in that message. Approval for one push does not carry over to the next.
- Before committing site changes, build locally with `bundle exec jekyll build` and check that the build succeeds.

## Commits

- Split commits by task, following the phase or task in the plan (`~/Projects/fg/plans/`) when the work belongs to one.
- Write a short imperative subject line, then a body that says why the change was made.
- Add the attribution trailers that Claude Code provides for the session.
- Never rewrite or reset commits that already exist on `origin/main`. (Exception made once, on 2026-11-07, at Humberto's request: `plans/` was removed from all history.)

## Plans

- Plans live in the private repo `~/Projects/fg/plans/`, never in this public repo. Commit plan changes there.
- Tick finished checkboxes and add a dated log line in `PROGRESS.md`, as `AGENTS.md` describes.
