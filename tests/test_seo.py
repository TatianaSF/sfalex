import json
import re
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_preview
import build_production


class SeoBuildTests(unittest.TestCase):
    def test_production_build_pages_metadata_schema_and_private_exclusions(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "site"
            build_production.build(out)
            pages = ["index.html", "about/index.html", "ventures/index.html", "experience/index.html"]
            titles, canonicals = set(), set()
            for rel in pages:
                html = (out / rel).read_text(encoding="utf-8")
                title = re.search(r"<title>(.*?)</title>", html).group(1)
                canonical = re.search(r'<link rel="canonical" href="([^"]+)">', html).group(1)
                self.assertNotIn("noindex", html)
                self.assertTrue(title)
                self.assertNotIn(title, titles)
                self.assertNotIn(canonical, canonicals)
                titles.add(title); canonicals.add(canonical)
                blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
                self.assertEqual(len(blocks), 1)
                json.loads(blocks[0])
            self.assertEqual(canonicals, {"https://sfalex.com/", "https://sfalex.com/about/", "https://sfalex.com/ventures/", "https://sfalex.com/experience/"})
            self.assertTrue((out / "llms.txt").is_file())
            for name in ("about.md", "ventures.md", "experience.md"):
                self.assertTrue((out / "ai" / name).is_file())
            self.assertFalse((out / "asset-library").exists())
            self.assertFalse((out / "production-backup").exists())
            self.assertFalse(any(p.suffix.lower() in {".zip", ".pem", ".key"} for p in out.rglob("*")))
            urls = re.findall(r"<loc>(.*?)</loc>", (out / "sitemap.xml").read_text(encoding="utf-8"))
            self.assertEqual(urls, ["https://sfalex.com/", "https://sfalex.com/about/", "https://sfalex.com/ventures/", "https://sfalex.com/experience/"])
            home = (out / "index.html").read_text(encoding="utf-8")
            self.assertEqual(tuple(re.findall(r'<span class="venture-copy"><strong>([^<]+)</strong>', home)), build_production.VENTURE_ORDER)
            destinations = re.findall(r'<a class="venture-card" href="([^"]+)', home)
            self.assertEqual(destinations, ["https://b4sf.com/", "https://o1sf.com/", "https://codexsf.com/", "https://openaisf.com/", "https://kitsf.com/", "https://tatianasf.com/", "https://uateg.com/", "https://hackathonsf.com/"])
            self.assertIn("Startup events connecting founders, builders, investors, and operators in San Francisco.", home)
            self.assertIn("An international memorial initiative honoring Ukrainian children killed by Russia's war.", home)
            self.assertIn("Organizing high-impact hackathons and tech events for San Francisco's builder community.", home)
            self.assertEqual(home.count('property="og:image:width"'), 1)
            self.assertEqual(home.count('property="og:image:height"'), 1)
            self.assertIn('property="og:image:type" content="image/png"', home)
            self.assertIn('name="twitter:image:alt"', home)
            self.assertTrue((out / "public/images/og-sfalex-1200x630.png").is_file())
            self.assertIn("Sitemap: https://sfalex.com/sitemap.xml", (out / "robots.txt").read_text(encoding="utf-8"))
            llms = (out / "llms.txt").read_text(encoding="utf-8")
            for page in ("about", "ventures", "experience"):
                self.assertIn(f"https://sfalex.com/ai/{page}.md", llms)
                self.assertIn(f'href="./{page}/"', home)

    def test_preview_build_remains_noindex_and_uses_preview_canonical(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "preview"
            build_preview.build(out)
            for rel in ("index.html", "about/index.html", "ventures/index.html", "experience/index.html"):
                html = (out / rel).read_text(encoding="utf-8")
                self.assertIn('name="robots" content="noindex, nofollow"', html)
                self.assertNotIn('href="https://sfalex.com/', html)
                self.assertIn("https://tatianasf.github.io/sfalex/", html)
            self.assertIn("Disallow: /", (out / "robots.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
