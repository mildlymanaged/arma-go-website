# Arma Go website

A statically generated, responsive website for Arma Go built with Astro, TypeScript, Tailwind CSS and Lucide icons. The production output is suitable for free GitHub Pages hosting and can be embedded in Google Sites.

## Project overview

The site uses:

- Astro static generation
- TypeScript
- Tailwind CSS
- Lucide icons
- Minimal client-side JavaScript for the navigation, FAQ, compact header, reveal effects and back-to-top control
- Original ImageGen visuals stored in `public/images`

The site has no database, server-side rendering, account system, contact-form backend, popup, autoplay media or iframe-blocking headers. Email is the primary contact method.

## Install and run locally

Install Node.js 20 or later and pnpm, then run:

```bash
pnpm install
pnpm run dev
```

Open the local address shown in the terminal, normally `http://localhost:4321`.

To check and build the production site:

```bash
pnpm run build
```

To preview the built output:

```bash
pnpm run preview
```

The static production files are written to `dist`.

## Website content

Common editable information is centralised in `src/data/siteContent.ts`, including:

- Brand name and description
- Email addresses and mail links
- Main and legal navigation
- Page metadata
- Image paths and alt text
- Resource-card titles and future article URLs
- FAQ content

Page-specific approved copy is stored in the corresponding file under `src/pages`. Shared layout and interface elements are under `src/components`, while site-wide styling is in `src/styles/global.css`.

To publish a future resource guide, add its URL to the matching empty `href` value in `src/data/siteContent.ts`. Until then, the card is visibly labelled “Guide coming soon”.

## Logo files

The supplied source logos are preserved in:

- `src/assets/brand/arma-go-full.png`
- `src/assets/brand/arma-go-symbol-source.png`

Prepared website versions are stored in `public/images`:

- `arma-go-logo.png` — full supplied logo
- `arma-go-logo-compact.png` — compact horizontal header lockup assembled from the supplied artwork
- `arma-go-logo-horizontal.png` — supplied transparent horizontal logo used in the header and footer
- `arma-go-symbol.png` — transparent-background symbol
- `arma-go-logo-white.png` — white monochrome fallback
- `favicon.png` — symbol favicon

To replace the logo later:

1. Replace the two source files with new approved PNG files using the same names.
2. Update `scripts/process_assets.py` if the new artwork has a different layout.
3. Run `scripts/process_assets.py` with a Python environment that includes Pillow.
4. Review every prepared logo before deployment.

Do not stretch, rotate, recolour or redraw the supplied logo.

## Generated images

The final WebP imagery is stored in `public/images`:

- `home-guidance-v3.webp`
- `work-abroad-v2.webp`
- `study-abroad.webp`
- `employers-partners.webp`
- `how-it-works.webp`
- `about-architecture.webp`
- `resources-still-life.webp`
- `og-card.webp`

To replace an image later, export a WebP with the same filename or update its path, width, height and alt text in `src/data/siteContent.ts`. Preserve the subject, crop and negative-space needs of the page where the image is used.

The local `scripts/process_assets.py` records how the current source PNGs were resized and encoded. Its generated-image source paths belong to the original build environment; update those paths before rerunning the script elsewhere.

## GitHub Pages deployment

### 1. Production URL configuration

The workflow in `.github/workflows/deploy.yml` deploys the site at:

`https://armago.me`

Astro reads these values through:

- `SITE_URL` for the `site` value in `astro.config.mjs`
- `BASE_PATH` for the `base` value in `astro.config.mjs`

The production workflow sets `SITE_URL=https://armago.me` and `BASE_PATH=/`.
All internal links and public asset paths therefore resolve from the custom-domain root.
The `public/CNAME` file preserves the GitHub Pages custom-domain setting.

To test the production origin locally, copy `.env.example` to `.env` and restart the local development server.

### 2. Create and push the GitHub repository

1. Sign in to GitHub and create a new empty repository.
2. Use the repository name you want in the public URL.
3. Do not add a second README, `.gitignore` or licence when creating it.
4. From this project folder, initialise Git if needed, commit the files, add the GitHub repository as the remote and push the `main` branch.

Example:

```bash
git init
git add .
git commit -m "Build Arma Go website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Open the repository on GitHub.
2. Select **Settings**.
3. Select **Pages**.
4. Under **Build and deployment**, choose **GitHub Actions** as the source.
5. Open the **Actions** tab and confirm that **Deploy Arma Go to GitHub Pages** completes successfully.
6. Return to **Settings → Pages** to find the public URL.

Every push to `main` runs the workflow, installs dependencies, builds the static site, uploads the `dist` folder and deploys it to GitHub Pages.

### 4. Update and redeploy

Edit the content, layout or images, then:

```bash
pnpm run build
git add .
git commit -m "Update Arma Go website"
git push
```

GitHub Actions will deploy the updated site automatically.

## Custom domain

The approved custom domain is `armago.me`. GitHub Pages remains deployed through
GitHub Actions, with DNS configured externally. The canonical production origin is
`https://armago.me`, and `www.armago.me` should redirect to the apex domain.

## Embed in Google Sites

After the GitHub Pages URL is public:

1. Open the Google Site.
2. Select **Embed**.
3. Select **By URL**.
4. Paste the public GitHub Pages URL.
5. Choose a full-page embed or resize the embedded frame.
6. Publish the Google Site.
7. Test the published site on desktop and mobile.

For best results, use a tall frame or full-page embed. The Arma Go site remains responsive at narrow widths, has no forced popups and does not access the parent browser window. Navigation and email links work within the embedded page.

## Legal review required

The legal pages are structured drafts and are intentionally marked `noindex` until qualified review is complete. They still contain these required placeholders:

- `[LEGAL REVIEW REQUIRED]`
- `[COMPANY DETAILS REQUIRED]`
- `[EFFECTIVE DATE REQUIRED]`
- `[REFUND TERMS REQUIRED]`
- Approved privacy practices, service terms, payment terms, cancellation terms, liability language, governing-law language and legal contact details

Do not remove the legal-review notices, `noindex` setting or the legal-route sitemap exclusions in `astro.config.mjs` until a qualified legal professional has approved the final copy.
