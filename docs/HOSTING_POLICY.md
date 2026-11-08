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

## Read-only transfer assessment (2026-11-08)

- The legacy source identified for production is `sfalexcom/sfalexcom`, branch `sfAlexcom`, snapshot `0ec671184c689dc9c62fc4252a30288482a56094`; the branch contains `CNAME` with `sfalex.com`.
- The connected `TatianaSF` GitHub account has read-only access to the legacy repository (`pull: true`, `push: false`). Its Pages settings are therefore not inspectable or changeable by this session; the legacy owner or an account with repository admin access must coordinate release of the existing custom domain.
- A read-only DNS lookup returned one apex `A` record, `185.199.108.153`, which is a GitHub Pages address. No apex `AAAA` record was returned. DNS has not been changed. GitHub's current documentation recommends verifying the domain before attaching it to a repository; for an apex, it documents `A`, `ALIAS`, or `ANAME` records and recommends four GitHub Pages `A` addresses when using `A` records.
- A read-only lookup did not find the `_github-pages-challenge-TatianaSF.sfalex.com` TXT record. The current GitHub verification state is unknown; the challenge TXT may need to be created during an authorized transfer.
- The new repository currently publishes by Actions at the standard project URL and has no custom domain (`cname: null`). No domain was attached during this preview task.

### Migration gates

1. Obtain owner/admin access to the legacy Pages settings and verify its current domain/publishing source in GitHub. Keep the old site active until the new build is ready.
2. Verify `sfalex.com` under the intended personal GitHub account using GitHub's Pages domain-verification flow. That flow may require a `_github-pages-challenge-<username>.sfalex.com` TXT record; check whether an existing verification record is present before planning any DNS change.
3. Coordinate removal/release of `sfalex.com` from the legacy repository's Pages settings. The legacy branch-published site also has a root `CNAME`; ensure it no longer claims the custom domain before completing the new attachment.
4. With admin access on `TatianaSF/sfalex`, set `sfalex.com` under Settings → Pages. For an Actions-published site, GitHub says the custom domain is configured in Pages settings; it does not create a `CNAME` file and ignores an existing one.
5. Preserve DNS unless the owner separately authorizes a change. Confirm current records meet GitHub's requirements, wait for validation/certificate provisioning, enforce HTTPS, and validate the apex and `www` behavior before treating the migration as complete.
6. After live validation, remove the preview `noindex` metadata and regenerate canonical/Open Graph metadata for production. Keep the legacy commit backup available for rollback.

Current blockers are legacy Pages-setting access and unknown GitHub domain-verification status. These do not affect the live project preview.

References: [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verifying a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), and [Securing a Pages site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

## Deployment workflow

The workflow builds a clean `_site/` artifact containing only `index.html`, `styles.css`, `script.js`, `public/`, and preview-specific robots/sitemap files. It deploys with the official GitHub Pages Actions. Do not include `production-backup/`, source masters outside the site artifact, credentials, or other local-only material in the deployed artifact.

