#!/usr/bin/env python3
"""Create and validate the production GitHub Pages artifact for sfAlex."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_URL = "https://sfalex.com/"
VENTURE_ORDER = (
    "B4SF", "O1SF", "codexSF", "openaiSF", "kitSF", "TatianaSF",
    "Angels of Ukraine", "HackathonSF",
)


class LocalReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value and key in {"src", "href"}:
                self.references.append(value)


def build(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for name in ("index.html", "styles.css", "seo-pages.css", "script.js", "robots.txt", "sitemap.xml", "llms.txt"):
        shutil.copy2(ROOT / name, output / name)
    shutil.copytree(ROOT / "public", output / "public")
    for name in ("about", "ventures", "experience", "ai"):
        shutil.copytree(ROOT / name, output / name)
    (output / ".nojekyll").touch()

    html = (output / "index.html").read_text(encoding="utf-8")
    if re.search(r'<meta\s+name=["\']robots["\'][^>]*noindex', html, re.I):
        raise ValueError("Production HTML must not contain a noindex robots directive")
    if '<link rel="canonical" href="https://sfalex.com/">' not in html:
        raise ValueError("Production canonical URL is not https://sfalex.com/")
    for url in (PRODUCTION_URL, "https://sfalex.com/public/images/og-sfalex-1200x630.png"):
        if url not in html:
            raise ValueError(f"Production social metadata is missing {url}")
    if "Disallow: /" in (output / "robots.txt").read_text(encoding="utf-8"):
        raise ValueError("Production robots.txt must allow indexing")
    if PRODUCTION_URL not in (output / "sitemap.xml").read_text(encoding="utf-8"):
        raise ValueError("Production sitemap is missing the canonical URL")
    venture_names = re.findall(r'<span class="venture-copy"><strong>([^<]+)</strong>', html)
    if tuple(name.strip() for name in venture_names) != VENTURE_ORDER:
        raise ValueError(f"Unexpected venture card order: {venture_names!r}")

    parser = LocalReferences()
    parser.feed(html)
    missing = []
    for reference in parser.references:
        if reference.startswith(("#", "https://", "http://", "mailto:", "tel:", "data:")):
            continue
        path = reference.split("?", 1)[0].split("#", 1)[0]
        target = output / path if path else output
        if path and target.is_dir():
            target = target / "index.html"
        if path and not target.is_file():
            missing.append(reference)
    if missing:
        raise ValueError(f"Missing local HTML references: {missing!r}")

    for page in (output / "index.html", output / "about/index.html", output / "ventures/index.html", output / "experience/index.html"):
        content = page.read_text(encoding="utf-8")
        scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)
        if len(scripts) != 1:
            raise ValueError(f"Expected one JSON-LD block in {page.relative_to(output)}")
        json.loads(scripts[0])
        parser = LocalReferences()
        parser.feed(content)
        for ref in parser.references:
            if ref.startswith(("#", "https://", "http://", "mailto:", "tel:", "data:")):
                continue
            path = ref.split("?", 1)[0].split("#", 1)[0]
            target = (page.parent / path).resolve() if path else page.parent
            if path and target.is_dir():
                target = target / "index.html"
            if path and not target.is_file():
                raise ValueError(f"Missing page asset {ref} referenced by {page.relative_to(output)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "production")
    args = parser.parse_args()
    output = args.output.resolve()
    build(output)
    print(f"Validated production site generated at {output}")


if __name__ == "__main__":
    main()
