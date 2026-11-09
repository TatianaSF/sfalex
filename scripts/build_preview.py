#!/usr/bin/env python3
"""Create a clean, noindex GitHub Pages preview artifact for sfAlex."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREVIEW_URL = "https://tatianasf.github.io/sfalex/"


def build(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for name in ("index.html", "styles.css", "seo-pages.css", "script.js", "llms.txt"):
        shutil.copy2(ROOT / name, output / name)
    shutil.copytree(ROOT / "public", output / "public")
    for name in ("about", "ventures", "experience", "ai"):
        shutil.copytree(ROOT / name, output / name)

    html_path = output / "index.html"
    html = html_path.read_text(encoding="utf-8")
    html = html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '  <meta name="robots" content="noindex, nofollow">',
        1,
    )
    html = html.replace('href="https://sfalex.com/"', f'href="{PREVIEW_URL}"', 1)
    html = html.replace('content="https://sfalex.com/"', f'content="{PREVIEW_URL}"')
    html = html.replace(
        'content="https://sfalex.com/public/images/og-sfalex-1200x630.png"',
        f'content="{PREVIEW_URL}public/images/og-sfalex-1200x630.png"',
    )
    html = html.replace('"url": "https://sfalex.com/"', f'"url": "{PREVIEW_URL}"')
    html_path.write_text(html, encoding="utf-8", newline="\n")

    (output / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (output / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{PREVIEW_URL}</loc></url>\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    (output / ".nojekyll").touch()
    for html_path in output.rglob("*.html"):
        html = html_path.read_text(encoding="utf-8")
        html = html.replace("https://sfalex.com/", PREVIEW_URL)
        html = html.replace('content="website"', 'content="website"', 1)
        if 'name="robots"' not in html:
            html = html.replace("</head>", '  <meta name="robots" content="noindex, nofollow">\n</head>', 1)
        html_path.write_text(html, encoding="utf-8", newline="\n")
    (output / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (output / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + PREVIEW_URL + '</loc></url></urlset>\n', encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    build(args.output.resolve())
    print(f"Preview site generated at {args.output.resolve()}")


if __name__ == "__main__":
    main()

