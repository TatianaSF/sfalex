# sfAlex project instructions

## Scope and infrastructure

- This repository contains the redesigned sfAlex static website and its asset library.
- GitHub is the only source-control and hosting platform for this project. GitHub Actions publishes the project preview to `https://tatianasf.github.io/sfalex/`.
- Do not change Cloudflare DNS, nameservers, the legacy `sfalex.com` site, or any other hosting account from this repository workflow.
- Do not configure `sfalex.com` as a custom domain here without a separately authorized migration task.
- Keep the project Pages preview marked `noindex` until an explicitly approved domain migration.

## Source and assets

- Keep the six venture cards in this order: B4SF, O1SF, codexSF, openaiSF, kitSF, TatianaSF.
- Keep website asset paths relative so the site works under the `/sfalex/` project path.
- Preserve the user-selected transparent portrait at `asset-library/masters/inputs/alex-rom-owner-transparent-portrait.png` and the approved layout reference. Do not regenerate or modify the portrait.
- Use `design-reference/approved-2026-11/reference/approved-design-941x1672.png` as the current visual authority.
- Use the user-selected transparent portrait; do not substitute the generated design-kit candidate or prior opaque portrait unless asked.
- The six colorful venture tiles are conceptual illustrations, not verified official logos. Keep that distinction visible in the page and preserve previous official source marks.
- Keep Current Ventures to two columns down to 320px; at very narrow widths hide only long descriptions visually, keeping them accessible to assistive technology.
- `asset-library/masters/` preserves supplied masters and source records; `asset-library/public/` contains optimized website assets.
- Never add `production-backup/`, credentials, private keys, personal configuration, or unrelated archives to Git.

## Preview build and validation

- Build the GitHub Pages preview with `python scripts/build_preview.py --output _site`.
- The build rewrites preview-only canonical/social metadata and adds `noindex`; keep production-domain metadata out of the preview artifact.
- Preview publishing is performed only by `.github/workflows/pages.yml` on the `main` branch or manual workflow dispatch.
- Before publishing changes, check the generated artifact for broken local asset references and confirm the venture order and responsive navigation.

