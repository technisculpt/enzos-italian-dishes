# Enzo’s traditional Italian dishes

Calabrian family recipes from Roccella Jonica, written and photographed by Enzo.
They were first published in 2016 with Apple iWeb and rebuilt as a static site in 2026.

The site is in [`docs/`](docs/) and is served by GitHub Pages
(Settings → Pages → Deploy from a branch → `main` / `/docs`).

## Editing

- Recipe text, ingredients and steps live in `build.py`. Edit them, then run `python build.py` (needs Pillow).
- Styles are in `docs/assets/style.css`, and the photo viewer is in `docs/assets/site.js`.
- `build.py` reads photos from the original iWeb export (`Enzos_traditional_Italian_dishes/`).
  That folder is git-ignored because it holds private family photos. The processed recipe photos are committed in `docs/images/`.

To preview locally:

```bash
python -m http.server 8765 --directory docs
```
