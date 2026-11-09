# Search Console and indexing setup

This guide records owner actions; no search account has been verified or sitemap submitted by this project.

## Google Search Console

1. Sign in to Search Console with the account that owns the domain.
2. Add `sfalex.com` as a Domain property if it is not already present.
3. Complete Google's ownership verification. A DNS TXT record may be required; ask the DNS owner to add it. This repository workflow does not change Cloudflare DNS.
4. Open the property and submit `https://sfalex.com/sitemap.xml` in Sitemaps.
5. Use URL Inspection for `/`, `/about/`, `/ventures/`, and `/experience/`; request indexing where useful.
6. Review Page indexing and Enhancements after Google has crawled the pages. Sitemap submission is a discovery hint, not an indexing guarantee.

## Bing Webmaster Tools

1. Sign in to Bing Webmaster Tools and add `https://sfalex.com/`.
2. Import the verified Google Search Console property when available, or complete Bing's offered site verification method.
3. Submit `https://sfalex.com/sitemap.xml` and inspect URL submission and crawl reports.

Keep verification tokens private. Do not paste them into chat or commit them. Track only actual verification/submission dates and observed indexing results; do not infer that a page is indexed from a successful build.
