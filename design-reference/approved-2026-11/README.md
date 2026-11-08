# sfAlex Approved Design Asset Kit

This kit contains a reference screenshot and **separate image assets**. Do not deploy the screenshot itself as the website. Implement the layout as semantic HTML and responsive CSS.

## Reference

- `reference/approved-design-941x1672.png`: the visual target; source reference is a concept mockup, not a literal CSS breakpoint.

## Web-ready assets

- `web-ready/portraits/alex-rom-headshot-reference.webp`: generated portrait candidate. The repo's original owner-provided portrait remains the identity baseline. Use the generated portrait **only if the owner accepts its likeness**, never regenerate or alter facial features automatically.
- `web-ready/backgrounds/golden-gate-hero.webp`: primary full-width hero background with bridge to the right and text-negative-space on the left.
- `web-ready/backgrounds/golden-gate-contact.webp`: contact section background, bridge at lower right.
- `web-ready/ventures/venture-*.webp`: six conceptual logo tiles matching the mockup; **not verified official brand logos**. Use these to match the approved visual style, but preserve originals and official brand master files, and keep replacement reversible.
- `web-ready/branding/sfalex-bridge-mark.svg`: clean vector interpretation of small blue bridge mark next to sfAlex.com.

## Design fidelity

- Light white / almost-white page, navy titles, bright blue accents, very light blue panels.
- Editorial bold serif headings (Georgia fallback), clean sans-serif body (Inter/system sans fallback).
- Floating rounded white cards, subtle blue-gray shadows, rounded square color-rich logos.
- Hero layout: visual integration of portrait with bay photo; do not display portrait in an obvious white-background rectangle. Use a clean mask/cutout only if quality permits, without AI-reinventing the face; otherwise preserve owner's original photo and adjust the crop/frame visually.
- Top header: blue bridge mark at far left, sfAlex.com serif wordmark; simple black hamburger at far right on narrow devices.
- About: two zones on wide screens, three blue icon roles on right.
- Ventures: 2 columns by 3 rows on mobile AND desktop as requested. At very narrow sizes, simplify descriptions to avoid text overflow; preserve full descriptions for screen readers and larger screens.
- Contact: rounded wide banner with bridge at lower right, four interest chips, blue LinkedIn and outlined Facebook CTAs.

## Usage

1. Unzip the package into `C:\Users\inlan\Documents\GitHub\sfalex\design-reference\approved-2026-11\` (or attach this ZIP to Codex and have it extract it there).
2. Ask Codex to inspect existing `AGENTS.md`, `README.md`, `scripts/build_preview.py`, `.github/workflows/pages.yml`, and `index.html/styles.css` before editing.
3. Add optimized assets to `public/` with stable paths and copy source masters to `asset-library/masters/` only when consistent with project policy.
4. Publish *only* via the existing GitHub Actions -> GitHub Pages preview, not to production `sfalex.com`.
5. Never change Cloudflare: DNS only, and **no changes** to its settings.

## Preview testing

Check viewport widths 320, 360, 390, 430, 768, 941 and 1440 px. Verify no horizontal overflow, no card text clipping, no image 404, the exact venture order, and mobile navigation. Capture final before/after screenshots.
