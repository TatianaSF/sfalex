# sfAlex image asset library

Prepared on 2026-11-08 from the supplied source pack for the sfAlex website.

## Contents

- `masters/inputs/`: unchanged owner-supplied portrait and approved 9:16 design reference.
- `masters/bridge/`: original generated Golden Gate Bridge source images used for the derived responsive formats.
- `masters/*-official-source.png`: source copies of the B4SF and CodexSF logos fetched from their own official domains.
- `public/images/`: responsive portrait/bridge images and the 1200 × 630 Open Graph image.
- `public/ventures/`: official B4SF and CodexSF marks plus text-only fallbacks for O1SF, openaiSF, kitSF, and TatianaSF.
- `public/icons/`: custom sfAlex bridge favicon and app icon sizes.
- `ASSET_INVENTORY.csv`: per-file source, use, dimensions, format, bytes, optimization, and integration status.

The portrait master is byte-for-byte identical to the archive input. No background-removal tool was available, so the original pale background is retained in every portrait asset. The original subject was not regenerated or retouched. Responsive versions only resize the supplied photograph; they do not upscale it beyond its original width.

The two Golden Gate Bridge backgrounds are original artwork generated specifically for this task. They are not cropped from the mockup and require no third-party photo attribution. The supplied reference mockup is retained as a design reference only.

## Venture assets

Verified first-party image URLs:

- B4SF: https://b4sf.com/media/brand/b4sf-logo-square.png
- CodexSF: https://codexsf.com/codexsf-logo.png

The websites publish the displayed assets, but I did not find an explicit standalone logo license statement; confirm brand-use terms before public commercial use. `openaiSF` uses a directory website distinct from OpenAI; its text fallback deliberately avoids OpenAI's logo and any implied affiliation. The other three text fallbacks are neutral wordmarks, not official logo artwork.

## Integration status

Optimized assets under `public/` are integrated into the static site. Source masters and the approved visual reference are preserved in the repository for maintenance; they are not copied into the GitHub Pages artifact. All per-file statuses are recorded in `ASSET_INVENTORY.csv`.
