# Hosting and domain policy

## Production hosting

- Source repository: `https://github.com/TatianaSF/sfalex`, branch `main`.
- Hosting: GitHub Pages, deployed by GitHub Actions.
- Production URL: `https://sfalex.com/`.
- Custom domain is configured in the repository's GitHub Pages settings; do not add a repository `CNAME` file for the Actions deployment.
- Cloudflare is used only for DNS. Do not change DNS records, nameservers, or proxy settings from this repository workflow.
- `scripts/build_production.py` creates the indexable production artifact. `scripts/build_preview.py` remains a separate noindex preview builder and must not be used for production.

## Cutover state (2026-11-08)

- `sfalex.com` is verified under the `TatianaSF` GitHub account (confirmed in GitHub Settings > Pages and by GitHub accepting the Pages API update).
- GitHub Pages API `PUT /repos/TatianaSF/sfalex/pages` returned HTTP `204`; readback showed `cname: sfalex.com`, `build_type: workflow`, source `main:/`.
- HTTPS enforcement was `false` immediately after attaching the domain. Enable it only after GitHub reports certificate readiness.
- Legacy `sfalexcom/sfalexcom` Pages settings remain `cname: null`, branch source `sfAlexcom`; the legacy branch no longer has a root `CNAME` file.
- The local legacy source snapshot and archive are preserved under `production-backup/`; that directory is ignored by Git and must never be deployed. Archive SHA-256: `7d59ae3127a695241ef6ba81f4b6ec394a73b590ba85928cc6a898181c92bb98`.
- Cloudflare records were not changed by this workflow. Existing domain verification and GitHub Pages records are owner-managed.

## Recovery

- Preserve the `production-backup/` directory and the legacy repository. The backup archive contains the source snapshot; the adjacent repository clone retains history at commit `0ec671184c689dc9c62fc4252a30288482a56094`.
- If the new production deployment has a critical defect, a repository admin may redeploy a known-good commit from `TatianaSF/sfalex` using the existing Pages workflow. Do not change DNS as part of rollback.
- Restoring the legacy production source/domain requires an administrator of `sfalexcom/sfalexcom`; the currently authenticated `TatianaSF` account has read-only access there. Do not claim that legacy rollback is executable without that access.

## Artifact contents

The production artifact contains `index.html`, `styles.css`, `script.js`, `public/`, an indexable `robots.txt`, a production `sitemap.xml`, and `.nojekyll`. Do not include `production-backup/`, asset masters outside the web asset tree, credentials, local configuration, or unrelated archives.

The production artifact must use canonical and social URLs under `https://sfalex.com/` and must not contain a `noindex` directive. The preview builder remains independently available for explicit noindex preview builds.

## References

- [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Verifying a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Securing a Pages site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
