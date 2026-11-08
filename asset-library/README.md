# sfAlex image asset library

Prepared from the supplied source packs for the sfAlex website. The approved November 2026 kit is preserved in `../design-reference/approved-2026-11/`; its original source images are also copied byte-for-byte into `masters/approved-design-kit-2026-11/` for the asset library.

## Contents

- `masters/inputs/`: unchanged source images, including the exact user-selected transparent Alex portrait and earlier approved 9:16 visual reference.
- `masters/bridge/`: earlier original Golden Gate Bridge source artwork.
- `masters/approved-design-kit-2026-11/`: unchanged original source images from the approved design kit, including its generated portrait candidate and conceptual venture tile originals.
- `masters/*-official-source.png`: source copies of B4SF and CodexSF marks fetched from their official websites.
- `public/images/`: optimized portrait, bridge backgrounds, and Open Graph image used or retained for the site.
- `public/ventures/`: approved conceptual design tiles alongside preserved earlier official marks and neutral text fallbacks.
- `public/icons/`: favicon/app marks, including the approved bridge wordmark icon.
- `ASSET_INVENTORY.csv`: file source, intended use, dimensions, format, byte size, optimization, and current integration status.

The user-selected transparent portrait master `masters/inputs/alex-rom-owner-transparent-portrait.png` is preserved unchanged and is now used on the site. Responsive WebP and AVIF derivatives preserve its alpha channel and proportions; only resampling and encoding were applied.

The generated portrait candidate in the November design kit remains archived and is not used by the site. The active portrait is the separate transparent image explicitly provided and selected by the user. No facial features were regenerated or altered.

The approved kit includes original Golden Gate Bridge artwork and colorful venture tiles. The tile graphics are conceptual design assets, not verified official brand logos. They are presented with the venture names/descriptions and labeled as conceptual on the page. The prior B4SF/CodexSF official mark files remain preserved for possible replacement.

The earlier verified first-party image URLs were:

- B4SF: https://b4sf.com/media/brand/b4sf-logo-square.png
- CodexSF: https://codexsf.com/codexsf-logo.png

Those official marks are retained locally; standalone usage terms were not established in the prior audit. `openaiSF` is a directory site distinct from OpenAI. No OpenAI logo or affiliation is implied.

## Integration

Optimized approved bridge artwork, the bridge mark, transparent portrait derivatives, and the six conceptual venture tiles are integrated under `public/`. The GitHub Pages build publishes only the website source and `public/`; source masters and the design screenshot remain available in the repository but outside the Pages artifact.
