# Hosting and domain policy

## Current project preview

- Source repository: `https://github.com/TatianaSF/sfalex`.
- Hosting: GitHub Pages, deployed by GitHub Actions from `main`.
- Preview URL: `https://tatianasf.github.io/sfalex/`.
- The preview uses relative asset URLs, preview-specific canonical/Open Graph URLs, and a `noindex` directive. `robots.txt` disallows crawling on this temporary preview.
- The repository does not configure a custom domain. The preview does not change Cloudflare DNS or nameservers.

## Production domain boundary

`https://sfalex.com` remains on its existing hosting source until a separate, explicitly authorized migration is completed. Do not add `sfalex.com` to this repository's Pages settings or create a `CNAME` here during preview work.

Before transferring the domain, verify the old Pages repository and publishing source, confirm owner access and domain verification, review GitHub's current Pages custom-domain and HTTPS requirements, and prepare a rollback. The cutover must preserve the existing DNS records unless the owner separately authorizes a specific DNS change. Remove preview `noindex` only as part of the approved production cutover.

## Deployment workflow

The workflow builds a clean `_site/` artifact containing only `index.html`, `styles.css`, `script.js`, `public/`, and preview-specific robots/sitemap files. It deploys with the official GitHub Pages Actions. Do not include `production-backup/`, source masters outside the site artifact, credentials, or other local-only material in the deployed artifact.

