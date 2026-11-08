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
- Preserve the owner-provided portrait and approved layout reference. Do not regenerate the portrait.
- `asset-library/masters/` preserves supplied masters and source records; `asset-library/public/` contains optimized website assets.
- Never add `production-backup/`, credentials, private keys, personal configuration, or unrelated archives to Git.

## Preview build and validation

- Build the GitHub Pages preview with `python scripts/build_preview.py --output _site`.
- The build rewrites preview-only canonical/social metadata and adds `noindex`; keep production-domain metadata out of the preview artifact.
- Preview publishing is performed only by `.github/workflows/pages.yml` on the `main` branch or manual workflow dispatch.
- Before publishing changes, check the generated artifact for broken local asset references and confirm the venture order and responsive navigation.

