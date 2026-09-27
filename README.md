# dauxillium

One-page HTML design example for D’auxilium / David Monier.

Preview: https://kurosato.github.io/dauxillium/

```sh
python3 build.py  # regenerate portable, offline HTML
python3 serve.py  # preview at http://127.0.0.1:8794
```

- `index.html`: page, inline CSS and gallery interaction.
- `assets/`: local photographs and existing logo.
- `dauxillium-voorbeeld.html`: downloadable single-file demo, including images.
- `sources.json`: public image sources and retrieval date.
- No external fonts, tracking, cookies, build dependencies or form backend.

Prototype only, not the official business website. Confirm copy, photo rights/selection and business details before a production launch. No domain or existing website migration has been performed.

GitHub Pages serves the `main` branch at the repository root. `.nojekyll` keeps the site a plain static HTML publication.

## Current design

The one-page example focuses on **haarden** and **maatkasten**. **Schilderwerken** is a smaller third collection; the kitchen is only a secondary example. Each of the three cards opens its own photo collection in a native accessible dialog. Previous/next controls, arrow keys, Escape, touch swipes and focus return are supported.

To add project photos:
1. Place a web-sized JPEG in `assets/` and record its provenance in `sources.json`.
2. Add a `<figure>` with image, descriptive alt text and caption to the matching `gallery-haarden`, `gallery-maatkasten` or `gallery-schilderwerken` template in `index.html`.
3. Run `python3 build.py` to update the offline example. Gallery counts are automatic.
4. Check the collection on mobile and desktop before publishing.

The opening photo was supplied for this revision. A higher-resolution original can replace the current small image later without changing the layout. Keep `noindex, nofollow` on this example; final indexing and domain setup belong to the eventual production migration.
