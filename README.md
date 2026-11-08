# sfAlex website

Redesigned, responsive portfolio for Alex Rom, implemented as dependency-free HTML, CSS, and JavaScript.

## Preview

- Repository: https://github.com/TatianaSF/sfalex
- GitHub Pages preview: https://tatianasf.github.io/sfalex/
- Production domain: https://sfalex.com (separate legacy deployment; unchanged by this project)

The Pages workflow builds a clean site artifact and applies preview-only canonical/social metadata plus `noindex`. The preview is public and should not be treated as private.

## Local development

Python 3 is only needed to prepare the preview artifact. To serve the source locally, run:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/`. To build the exact Pages artifact locally:

```powershell
python scripts/build_preview.py --output _site
```

## Project contents

- `index.html`, `styles.css`, `script.js`: website source.
- `public/`: optimized portrait, Golden Gate Bridge backgrounds, venture marks, icons, and social preview image.
- `asset-library/`: source notes, asset inventory, preserved masters, and approved visual reference.
- `docs/HOSTING_POLICY.md`: hosting boundary, preview indexing policy, and production-domain migration gate.
- `AGENTS.md`: repository-specific implementation and deployment instructions.
- `.github/workflows/pages.yml`: GitHub Actions Pages build and deployment.

The responsive design includes Hero, About, Current Ventures, Experience & Highlights, and Let’s Connect. Venture cards appear in this order: B4SF, O1SF, codexSF, openaiSF, kitSF, TatianaSF.

## Assets

The original owner-provided portrait is preserved and resized for responsive AVIF/WebP display; synthetic facial features were not generated. The optimized versions are used by the website. Golden Gate Bridge artwork and venture image sources are documented in `asset-library/README.md` and `asset-library/ASSET_INVENTORY.csv`.

## Hosting

Pushes to `main` publish the preview using GitHub Pages Actions. The site uses the standard project URL and does not configure a custom domain. Do not change Cloudflare DNS, nameservers, or the legacy production site as part of preview work.
