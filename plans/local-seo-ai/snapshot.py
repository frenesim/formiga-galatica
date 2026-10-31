#!/usr/bin/env python3
"""Snapshot the LIVE site's SEO state to plans/local-seo-ai/snapshots/YYYY-MM-DD.md.

Run it again later and diff the two files:
    python3 plans/local-seo-ai/snapshot.py
    diff plans/local-seo-ai/snapshots/2026-10-31.md plans/local-seo-ai/snapshots/<later>.md
"""
import datetime
import json
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SITE = "https://formiga.galaticos.pt"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
BOTS = {
    "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Applebot": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)",
    "GPTBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot",
    "OAI-SearchBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot",
    "ChatGPT-User": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
    "ClaudeBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)",
    "Claude-SearchBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; +Claude-SearchBot@anthropic.com)",
    "PerplexityBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
    "Google-Extended": "Mozilla/5.0 (compatible; Google-Extended)",
}


def fetch(url, ua=BROWSER_UA):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, dict(r.headers), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read().decode("utf-8", "replace")
    except Exception as e:  # network error
        return f"ERR {type(e).__name__}", {}, ""


def first(pattern, html):
    m = re.search(pattern, html, re.S)
    return m.group(1).strip() if m else ""


def jsonld_types(html):
    types = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            types.append("INVALID JSON")
            continue
        for item in data if isinstance(data, list) else [data]:
            types.append(str(item.get("@type")))
    return types


def page_row(url):
    status, _, html = fetch(url)
    return {
        "url": url,
        "status": status,
        "title": first(r"<title>(.*?)</title>", html),
        "description": first(r'<meta name="description" content="(.*?)"', html),
        "canonical": first(r'<link rel="canonical" href="(.*?)"', html),
        "lang": first(r"<html lang=\"(.*?)\"", html),
        "hreflang": len(re.findall(r'rel="alternate" hreflang=', html)),
        "og:image": bool(re.search(r'property="og:image"', html)),
        "json-ld": ", ".join(jsonld_types(html)) or "none",
        "feed link": bool(re.search(r'type="application/atom\+xml"', html)),
        "h1": len(re.findall(r"<h1[ >]", html)),
        "words": len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style).*?</\1>", "", html, flags=re.S)).split()),
    }


def pagespeed(url, strategy):
    api = ("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?"
           + urllib.parse.urlencode([("url", url), ("strategy", strategy), ("category", "performance"),
                                     ("category", "seo"), ("category", "accessibility"), ("category", "best-practices")]))
    status, _, body = fetch(api)
    if status != 200:
        return f"unavailable ({status})"
    cats = json.loads(body)["lighthouseResult"]["categories"]
    return ", ".join(f"{k}={round(v['score'] * 100)}" for k, v in cats.items())


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True).stdout.strip()


def main():
    today = datetime.date.today().isoformat()
    out = [f"# SEO snapshot {today}", "",
           f"Live site: {SITE}  ",
           f"Repo HEAD: `{git('rev-parse', '--short', 'HEAD')}` (`{git('log', '-1', '--format=%s')}`)  ",
           f"Uncommitted changes in working tree: {'yes' if git('status', '--porcelain') else 'no'}", ""]

    out += ["## Crawler access to `/` (HTTP status)", "", "| Bot | Status |", "|---|---|"]
    out += [f"| {name} | {fetch(SITE + '/', ua)[0]} |" for name, ua in BOTS.items()]

    _, _, sitemap = fetch(SITE + "/sitemap.xml")
    urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
    out += ["", f"## Sitemap ({len(urls)} URLs)", ""] + [f"- {u}" for u in urls]

    out += ["", "## Files", "", "| Path | Status |", "|---|---|"]
    for path in ["/robots.txt", "/llms.txt", "/sitemap.xml", "/feed.xml", "/404.html", "/this-page-does-not-exist/"]:
        out.append(f"| {path} | {fetch(SITE + path)[0]} |")

    out += ["", "## Pages", ""]
    for url in [SITE + "/"] + [u for u in urls if u != SITE + "/"]:
        row = page_row(url)
        out += [f"### {url}", ""] + [f"- **{k}:** {v}" for k, v in row.items() if k != "url"] + [""]

    out += ["## Lighthouse (PageSpeed Insights API, home page)", ""]
    for strategy in ("mobile", "desktop"):
        out.append(f"- **{strategy}:** {pagespeed(SITE + '/', strategy)}")

    _, headers, _ = fetch(SITE + "/")
    out += ["", "## Response headers (home)", ""]
    for h in ("server", "cache-control", "content-type", "strict-transport-security", "x-content-type-options", "content-security-policy"):
        out.append(f"- **{h}:** {headers.get(h, headers.get(h.title(), '—'))}")

    out += ["", "## Not captured here (fill in by hand)", "",
            "- Lighthouse scores if the PageSpeed API answered 429 (no API key): run https://pagespeed.web.dev/ for the home page by hand",
            "- Search Console: impressions / clicks / avg. position, indexed pages",
            "- Google Business Profile insights",
            "- AI prompt test (see `05-measurement.md`)", ""]

    dest = Path(__file__).parent / "snapshots" / f"{today}.md"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text("\n".join(out), encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
