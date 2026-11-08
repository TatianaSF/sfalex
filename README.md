# sfAlex website

Redesigned, responsive portfolio for Alex Rom, implemented as dependency-free HTML, CSS, and JavaScript.

## Preview

- Repository: https://github.com/TatianaSF/sfalex
- GitHub Pages preview: https://tatianasf.github.io/sfalex/
- Production domain: https://sfalex.com (separate legacy deployment; unchanged by this project)

The Pages workflow builds a clean site artifact with preview-only canonical/social metadata and a `noindex` directive. The preview is public and should not be treated as private.

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
- `public/`: optimized portrait, approved Golden Gate Bridge backgrounds, conceptual venture design tiles, icons, and social preview image.
- `asset-library/`: asset inventory, user-selected transparent portrait master, earlier official marks, and source masters from the approved kit.
- `design-reference/approved-2026-11/`: full approved design kit, screenshot, web-ready assets, and originals.
- `docs/HOSTING_POLICY.md`: hosting boundary, preview indexing policy, and production-domain migration gate.
- `AGENTS.md`: repository implementation and deployment instructions.
- `.github/workflows/pages.yml`: GitHub Actions Pages build and deployment.

The site includes Hero, About, Current Ventures, Experience & Highlights, and Let’s Connect. Venture cards appear in this order: B4SF, O1SF, codexSF, openaiSF, kitSF, TatianaSF. The colorful venture images are conceptual design tiles, not verified official brand logos.

The user-selected transparent portrait is in use. Its source PNG is preserved unchanged in `asset-library/masters/inputs/`; responsive AVIF/WebP derivatives preserve transparency without altering facial features.

## Hosting

Pushes to `main` publish the preview using GitHub Pages Actions. The site uses the standard project URL and does not configure a custom domain. Do not change Cloudflare DNS, nameservers, or the legacy production site as part of preview work.
