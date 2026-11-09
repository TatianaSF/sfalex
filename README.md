# sfAlex website

Redesigned, responsive portfolio for Alex Rom, implemented as dependency-free HTML, CSS, and JavaScript.

## Preview

- Repository: https://github.com/TatianaSF/sfalex
- GitHub Pages production: https://sfalex.com/
- The former project URL https://tatianasf.github.io/sfalex/ may redirect to the custom domain.

The Pages workflow builds a clean production artifact with canonical and social metadata for `https://sfalex.com/`, an indexable `robots.txt`, and a production sitemap.

## Local development

Python 3 is only needed to prepare the site artifact. To serve the source locally, run:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/`. To build the production artifact locally:

```powershell
python scripts/build_production.py --output dist/production
```

To build a separate noindex preview artifact locally:

```powershell
python scripts/build_preview.py --output _site
```

## Project contents

- `index.html`, `styles.css`, `script.js`: website source.
- `public/`: optimized portrait, approved Golden Gate Bridge backgrounds, conceptual venture design tiles, icons, and social preview image.
- `asset-library/`: asset inventory, user-selected transparent portrait master, earlier official marks, and source masters from the approved kit.
- `design-reference/approved-2026-11/`: full approved design kit, screenshot, web-ready assets, and originals.
- `docs/HOSTING_POLICY.md`: hosting boundary, preview indexing policy, and production-domain migration gate.
- `AGENTS.md`: repository implementation and deployment instructions.
- `.github/workflows/pages.yml`: GitHub Actions Pages build and deployment.
- `llms.txt` and `ai/`: public human-readable discovery summaries.
- `docs/SEARCH_CONSOLE_SETUP.md`: owner steps for search verification and sitemap submission.

The homepage includes Hero, About, Current Ventures, Experience & Highlights, and Let’s Connect. SEO pages are available at `/about/`, `/ventures/`, and `/experience/`. Venture cards appear in this order: B4SF, O1SF, codexSF, openaiSF, kitSF, TatianaSF, Angels of Ukraine, HackathonSF. Conceptual venture images are identified as such.

The user-selected transparent portrait is in use. Its source PNG is preserved unchanged in `asset-library/masters/inputs/`; responsive AVIF/WebP derivatives preserve transparency without altering facial features.

Production includes the homepage, three directory-style SEO pages, and AI-readable summaries. Run local validation with `python -m unittest discover -s tests`.

## Hosting

Pushes to `main` publish the production site using GitHub Pages Actions. Do not change Cloudflare DNS, nameservers, or proxy settings from this repository workflow.
