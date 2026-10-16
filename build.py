"""Build the new 'Enzo's traditional Italian dishes' site into docs/.

The words and photos come from the original 2016 iWeb site in
Enzos_traditional_Italian_dishes/. Run:  python build.py
Hand-written CSS and JS live in docs/assets/ and are not touched here.
"""
import html
import math
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
SRC = ROOT / "Enzos_traditional_Italian_dishes"
OUT = ROOT / "docs"
IMG = OUT / "images"

SITE_TITLE = "Enzo’s traditional Italian dishes"
ROCCELLA_URL = "https://www.comune.roccella.rc.it"

# ---------------------------------------------------------------- content

HISTORY = [
    "My father emigrated to Sydney in 1953. "
    "It was another four years before my mother with three children, was able to join him.",
    "Dad bought a house in the southern suburbs of Sydney and they lived there for the rest of their lives. "
    "My daughter now lives there with her family.",
    "Mum knew no other way to cook than to make do with what you had and develop dishes based on available produce. "
    "Even when times were a lot better financially, her favourite dishes consisted of simple available ingredients "
    "and often were vegetarian. Before and after the war in Italy, meat was a very much sought after ingredient but "
    "often not readily available or affordable, so cheaper, vegetarian, pasta based meals were the staple. "
    "This is reflected in a lot of the recipes I am publishing here.",
]

NOTES = [
    ("The recipe titles",
     "I have tried to use the “calabrian dialect” to name the dish, as mum used to call it (in red handwriting). "
     "The name in italics above the title would be its “proper” Italian equivalent."),
    ("Parmesan cheese",
     "I am no expert on Italian cheeses but, as I understand it, what we Australians call “parmesan” cheese refers to "
     "any Italian hard cheese which is suitable for grating. Pecorino (originally made from sheep’s milk) is associated "
     "with the south of Italy, Romano is associated with the centre and Parmiggiano with the north. Any of them would be "
     "suitable for any dish which calls for “parmesan” cheese."),
]

# Each step: (source image, [paragraphs], optional extra inset image)
RECIPES = [
    {
        "slug": "marrow-pasta",
        "src": "Marrow_Pasta_files",
        "italian": "Pasta con zucchini",
        "english": "Marrow pasta",
        "dialect": "Pasta ca cucuzzeia",
        "tags": ["Primo piatto", "Summer", "Vegetarian"],
        "serves": "Ingredients for about 4–5 dishes",
        "blurb": "Young marrow, ripe tomato and potato simmered into a gentle broth for broken spaghetti.",
        "intro": [
            "This dish uses the subtle flavour of the young marrow to provide the background flavour for this pasta dish. "
            "It is a traditional summer “primo piatto” (first course). An important ingredient is a young leaf and flower "
            "from the plant but this is next to impossible to get unless you grow them yourself (they are easy to grow in "
            "full sun in summer). The leaf needs to have its fibrous veins removed and then chopped finely with the flower "
            "and added to the chopped marrow for cooking. The pictures do not show this part of the process as I did not "
            "have some to include when I cooked this meal in mid winter.",
        ],
        "ingredients": [("", ["5 marrows", "2 ripe tomatoes", "1 medium potato", "250g pasta",
                              "basil – preferably fresh", "olive oil"])],
        "tip": "The quantity of pasta required varies for different people. Some prefer a soupy mixture with a lot of broth "
               "and little pasta while others prefer a drier dish with more pasta. The type of pasta is also to be "
               "experimented with. I show broken thin spaghetti while some people might prefer a soup pasta like "
               "maccheroni. The potato is cut into pieces with a feathered edge as the thin edges cook quicker and add a "
               "potato flavour to the mix.",
        "steps": [
            ("shapeimage_5.png", ["Young marrows are preferable. If the marrow is too fleshy due to its size, then carve out "
                                  "the flesh as I have done with the half marrow on the left of the picture (the skin has the "
                                  "most flavour). Slice and dice the marrow."]),
            ("shapeimage_4.png", ["Remove seed and dice two ripe tomatoes. Cook on a hot bed of olive oil. Mash when soft "
                                  "to form a saucy paste. Add enough water to cover the diced marrow."]),
            ("shapeimage_6.png", ["Add the diced marrow to the saucepan and make sure that the added water more than covers "
                                  "the diced marrow.", "Add a dessert spoon of salt and simmer the mixture."]),
            ("shapeimage_2.png", ["Cut the potato into small pieces with a feathered edge and add them to the mix while "
                                  "simmering. The potato pieces should also be covered by the liquid while cooking. The mix "
                                  "will reduce a little while cooking."]),
            ("shapeimage_7.png", ["If using thin spaghetti, break it up for spoon size pieces and cook separately in "
                                  "salted water."]),
            ("shapeimage_8.png", ["When pasta is cooked, drain and add to the mix. Continue cooking at least for a minute "
                                  "or so to allow the flavour to seep into the pasta."]),
        ],
        "serve": ("shapeimage_9.png", ["Serve in a pasta bowl. Usually eaten with a spoon."]),
    },
    {
        "slug": "carciofi",
        "src": "Carciofi_files",
        "italian": "Carciofi con carne",
        "english": "Stuffed artichokes",
        "dialect": "Canciofoli ca carne",
        "tags": ["Secondo", "With meat"],
        "serves": "Ingredients for about 4–5 artichokes",
        "blurb": "Artichoke hearts filled with a soft meatball mixture and simmered in a tomato and garlic broth.",
        "intro": [
            "The hurdle for this dish is cultural. Even though most of the fibrous outside leaves have been removed, there "
            "are still some leaves that are quite fibrous and should not be eaten. However, they are still quite tasty so "
            "they are chewed for the flavour and then demurely spat out onto a side dish. This is a common type of dish "
            "which is eaten simply with some tasty crusty bread. There is some preparation involved but the flavour of the "
            "dish makes it all worthwhile.",
        ],
        "ingredients": [
            ("", ["4–5 artichokes", "1–2 ripe tomatoes", "1–2 cloves of garlic", "olive oil"]),
            ("Filling", ["100g lean mince", "½ cup of grated parmesan cheese", "½ cup of breadcrumbs", "2–3 eggs",
                         "freshly chopped parsley leaves"]),
        ],
        "tip": "The stalk is also very tasty but too fibrous to eat unless the very thick skin is removed. The ratio of meat "
               "to grated cheese and breadcrumbs and eggs can be experimented with as it affects the texture and density "
               "of the filling. I like a soft filling so I prefer more eggs, crumbs and cheese.",
        "steps": [
            ("shapeimage_7.png", ["Remove the seeds from the ripe tomatoes and dice.",
                                  "Slice the garlic and fry both the tomatoes and garlic in a generous layer of olive oil "
                                  "in a saucepan."]),
            ("shapeimage_4.png", ["Mash the tomato/garlic mixture when the tomato is softened and then add water to cover "
                                  "the artichokes as they are placed after preparation. You can turn off the heat until all "
                                  "the artichokes are prepared. It is important that the artichokes go into the tomato/water "
                                  "base as they will go a dark colour after being cut during preparation if left exposed to "
                                  "the air."]),
            ("shapeimage_5.png", ["The artichokes are prepared by taking off the outside leaves which are very fibrous. "
                                  "Peel each one off until the much lighter leaves are visible. Part of the crown comes off "
                                  "with every leaf and that part can be bitten off as it is very tasty eaten raw."],
             "shapeimage_6.png"),
            ("shapeimage_2.png", ["The second part of preparing the artichokes is to cut off the bottom part of the leaves "
                                  "to gain access to the fibrous heart of the artichoke."]),
            ("shapeimage_8.png", ["The third part of preparing the artichokes is to remove the very fibrous small white "
                                  "leaves at the heart of the artichoke. By the end you should have the crown and the "
                                  "younger leaves remaining with a cavity ready for the meat filling."]),
            ("shapeimage_9.png", ["Prepare the meat filling which is basically a meatball mixture (without the garlic and "
                                  "cracked pepper). The filling consists of minced lean meat, eggs, finely chopped parsley, "
                                  "breadcrumbs and parmesan cheese."]),
            ("shapeimage_10.png", ["Combine all the ingredients thoroughly."]),
            ("shapeimage_11.png", ["Spoon the mixture into the empty heart of the artichoke."]),
            ("shapeimage_12.png", ["Place into the tomato based water and add a heaped teaspoon of salt. The amount of salt "
                                   "depends on personal taste. Rotate the artichokes as they cook, to spread the tomato "
                                   "flavour. Leave the lid off for simmering on a low heat while the artichokes cook. The "
                                   "colour of the leaves change to a dull green and the crowns of the artichoke should be "
                                   "soft. The sauce will reduce so more water might need to be added if the crowns are "
                                   "still hard."]),
        ],
        "serve": ("shapeimage_13.png", [
            "I usually eat them with a fork and crusty bread. It is not really a “fork and knife” dish – most bowl type "
            "dishes are traditionally either a spoon only or fork only dish, but suit yourself. It is a very tasty dish and "
            "you can experiment with the filling quantities and the amount of salt."]),
    },
    {
        "slug": "beans-and-potato-stew",
        "src": "Fresh_beans_stew_files",
        "italian": "Fagioli con patate",
        "english": "Beans & potato stew",
        "dialect": "Fagiola chi patati",
        "tags": ["Contorno", "Summer", "Vegetarian"],
        "serves": "Ingredients for about 4 dishes",
        "blurb": "Fresh green beans and potatoes stewed in a light tomato and garlic sauce. Bread essential.",
        "intro": [
            "This dish is traditionally a summer dish although beans are now available throughout the year in a lot of "
            "places. It can be used as a side dish for a meat or fish or simply eaten with bread as I have shown. I have "
            "also added sliced carrots to the mix, especially if I am using it as a side to a main course.",
        ],
        "ingredients": [("", ["500–700g of beans", "1–2 ripe tomatoes", "1–2 cloves of garlic", "olive oil",
                              "1 teaspoon salt", "2–3 medium size potatoes"])],
        "tip": "Which beans to use? I have only used the common green bean which is often well priced and easy to prepare "
               "if stringless. My mother would strive to use borlotti beans which she would grow during the summer months. "
               "She called it “povereia”. She would cook the skin as well when it was young but discard the skin as the "
               "bean matured and the beans inside fattened.",
        "steps": [
            ("shapeimage_6.png", ["Prepare the beans as shown if they are stringless, otherwise you must also remove the "
                                  "string. If using young borlotti beans (the bean shell is tender and mainly green as it "
                                  "begins to turn pink) the string can be sliced off along the length."]),
            ("shapeimage_4.png", ["Remove the seeds and stalk of tomatoes and chop.",
                                  "Slice the garlic cloves and cook both in a saucepan with olive oil generously covering "
                                  "the base.", "Mash the mixture when the tomato is soft."]),
            ("shapeimage_5.png", ["Add enough water to cover the beans and potatoes.",
                                  "Add the prepared beans and heat the watery sauce to boil and let it simmer."]),
            ("shapeimage_2.png", ["When the beans begin to change colour add the potatoes which have been cut into "
                                  "quarters. You can experiment with the size of the potato pieces and when to add them so "
                                  "that the potatoes do not overcook and break apart."]),
            ("shapeimage_8.png", ["Add salt to taste. I like to add enough salt so that the vegetables do not diminish "
                                  "their flavour. Of course you can experiment with how much salt or if you don’t want to "
                                  "add salt at all."]),
            ("shapeimage_7.png", ["The watery sauce will reduce while cooking and the beans will change colour and not be "
                                  "a bright green. At this point, if the potatoes are cooked, the vegetable stew is ready."]),
        ],
        "serve": ("shapeimage_9.png", ["Serve in a dish with tasty crusty bread."]),
    },
]

# ---------------------------------------------------------------- images

def export(src: Path, dest_rel: str) -> str:
    """Copy an original image into docs/images as an optimised JPEG; return its site path and size."""
    dest = IMG / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    im.save(dest, "JPEG", quality=86, optimize=True, progressive=True)
    return f"images/{dest_rel}", im.size


def img_tag(path_size, alt, cls="", lightbox=True, eager=False):
    path, (w, h) = path_size
    attrs = f'src="{path}" width="{w}" height="{h}" alt="{esc(alt)}"'
    if not eager:
        attrs += ' loading="lazy"'
    if cls:
        attrs += f' class="{cls}"'
    if lightbox:
        attrs += " data-lightbox"
    return f"<img {attrs}>"

# ---------------------------------------------------------------- html helpers

def esc(s):
    return html.escape(s, quote=True)


def paras(ps, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "\n".join(f"<p{c}>{esc(p)}</p>" for p in ps)


def starburst_points(n=24, outer=50, inner=44):
    pts = []
    for i in range(n * 2):
        r = outer if i % 2 == 0 else inner
        a = math.pi * i / n - math.pi / 2
        pts.append(f"{50 + r * math.cos(a):.2f},{50 + r * math.sin(a):.2f}")
    return " ".join(pts)


STARBURST = (f'<svg class="burst" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">'
             f'<polygon points="{starburst_points()}"/></svg>')

GINGHAM = '<div class="gingham" aria-hidden="true"></div>'


def nav(active):
    items = [("index.html", "Home", "home"), ("index.html#recipes", "Recipes", "recipes"),
             ("index.html#notes", "Kitchen notes", "notes")]
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if k == active else ""}>{t}</a>' for h, t, k in items)
    return f"""<header class="site-header">
  {GINGHAM}
  <div class="bar wrap">
    <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">E</span><span>Enzo’s <em>traditional</em> Italian dishes</span></a>
    <nav aria-label="Main">{links}</nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <p class="sign">Buon appetito!</p>
    <p>Recipes, words and photos by Enzo. Family recipes from <a href="{ROCCELLA_URL}">Roccella Jonica</a>, Calabria, cooked in Sydney.</p>
    <p class="small">First published in 2016 · rebuilt from the original pages in 2026.</p>
  </div>
  {GINGHAM}
</footer>"""


def page(title, desc, body, active, extra_head=""):
    full = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Fraunces:ital,opsz,wght@0,9..144,400..800;1,9..144,400..700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav(active)}
<main id="main">
{body}
</main>
{FOOTER}
<dialog class="lightbox" aria-label="Photo viewer">
  <button class="lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-prev" type="button" aria-label="Previous photo">‹</button>
  <figure><img alt=""><figcaption></figcaption></figure>
  <button class="lb-next" type="button" aria-label="Next photo">›</button>
</dialog>
<script src="assets/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- pages

def names_block(r, tag="h1"):
    return f"""<div class="names">
  <p class="name-it" lang="it">{esc(r['italian'])}</p>
  <{tag} class="name-en">{esc(r['english'])}</{tag}>
  <p class="name-dialect" lang="it"><span class="as-mum">as Mum called it</span> {esc(r['dialect'])}</p>
</div>"""


def build_recipe(r, idx):
    src = SRC / r["src"]
    hero = export(src / r["serve"][0], f"{r['slug']}/finished.jpg")
    r["hero"] = hero

    ingredients = []
    for heading, items in r["ingredients"]:
        h = f"<h3>{esc(heading)}</h3>" if heading else ""
        lis = "".join(f'<li><label><input type="checkbox"> <span>{esc(i)}</span></label></li>' for i in items)
        ingredients.append(f"{h}<ul class=\"ing-list\">{lis}</ul>")

    steps = []
    for n, step in enumerate(r["steps"], 1):
        im = export(src / step[0], f"{r['slug']}/step-{n:02d}.jpg")
        first = step[1][0]
        alt = f"Step {n}: {first[:90]}{'…' if len(first) > 90 else ''}"
        inset = ""
        if len(step) > 2:
            ins = export(src / step[2], f"{r['slug']}/step-{n:02d}-detail.jpg")
            inset = f'<span class="inset">{img_tag(ins, "Close-up of a peeled artichoke leaf", "inset-img")}</span>'
        steps.append(f"""<li class="step">
  <figure class="step-photo">{img_tag(im, alt)}{inset}</figure>
  <div class="step-text"><span class="step-num" aria-hidden="true">{n}</span>{paras(step[1])}</div>
</li>""")

    prev_r = RECIPES[idx - 1] if idx > 0 else None
    next_r = RECIPES[idx + 1] if idx + 1 < len(RECIPES) else None
    pn = '<nav class="prevnext" aria-label="More recipes">'
    pn += (f'<a class="prev" href="{prev_r["slug"]}.html"><small>Previous</small>{esc(prev_r["english"])}</a>'
           if prev_r else "<span></span>")
    pn += (f'<a class="next" href="{next_r["slug"]}.html"><small>Next</small>{esc(next_r["english"])}</a>'
           if next_r else "<span></span>")
    pn += "</nav>"

    tags = "".join(f"<li>{esc(t)}</li>" for t in r["tags"])
    body = f"""<article class="recipe">
  <header class="recipe-hero wrap">
    <div class="recipe-title">
      <ul class="tags">{tags}</ul>
      {names_block(r)}
      <div class="intro">{paras(r['intro'])}</div>
      <button class="print-btn" type="button" data-print>Print this recipe</button>
    </div>
    <figure class="hero-plate">{img_tag(hero, f"The finished dish: {r['english']}", eager=True)}</figure>
  </header>

  <div class="recipe-body wrap">
    <aside class="ingredients">
      <div class="card">
        <h2>Ingredients</h2>
        <p class="serves">{esc(r['serves'])}</p>
        {''.join(ingredients)}
      </div>
      <div class="tip">
        {STARBURST}
        <div class="tip-inner"><p class="tip-label">Enzo’s tip</p><p>{esc(r['tip'])}</p></div>
      </div>
    </aside>

    <section class="method" aria-labelledby="method-h">
      <h2 id="method-h">Method</h2>
      <ol class="steps">
        {''.join(steps)}
      </ol>
      <div class="serve">
        <figure>{img_tag(hero, f"Ready to eat: {r['english']}")}</figure>
        <div><h3>To serve</h3>{paras(r['serve'][1])}</div>
      </div>
    </section>
  </div>
  <div class="wrap">{pn}</div>
</article>"""
    desc = f"{r['english']} ({r['italian']}): {r['blurb']}"
    (OUT / f"{r['slug']}.html").write_text(page(r["english"], desc, body, "recipes"), encoding="utf-8")


def build_home():

    cards = []
    for r in RECIPES:
        tags = "".join(f"<li>{esc(t)}</li>" for t in r["tags"])
        cards.append(f"""<li class="recipe-card">
  <a href="{r['slug']}.html">
    <figure>{img_tag(r['hero'], r['english'], lightbox=False)}</figure>
    <div class="card-body">
      <ul class="tags">{tags}</ul>
      {names_block(r, 'h3')}
      <p class="blurb">{esc(r['blurb'])}</p>
      <span class="cta">Cook this <span aria-hidden="true">→</span></span>
    </div>
  </a>
</li>""")

    notes = "".join(f'<div class="note"><h3>{esc(h)}</h3><p>{esc(t)}</p></div>' for h, t in NOTES)

    body = f"""<section class="home-hero wrap">
  <div class="hero-copy">
    <p class="eyebrow">Cucina povera · Calabria → Sydney</p>
    <h1>Enzo’s <em>traditional</em> Italian dishes</h1>
    <p class="lede">Simple dishes from Roccella Jonica, made the way Mum made them: with whatever was fresh, cheap and in season.</p>
    <a class="button" href="#recipes">See the recipes</a>
  </div>
  <div class="hero-plates" aria-hidden="true">
    {''.join(f'<span class="plate p{i}">{img_tag(r["hero"], "", lightbox=False, eager=True)}</span>' for i, r in enumerate(RECIPES))}
  </div>
</section>

<section class="history wrap" aria-labelledby="history-h">
  <h2 id="history-h">A little history</h2>
  <div class="history-text">{paras(HISTORY)}</div>
</section>

<section id="recipes" class="recipes wrap" aria-labelledby="recipes-h">
  <div class="section-head">
    <p class="eyebrow">Il ricettario</p>
    <h2 id="recipes-h">The recipes</h2>
    <p>Each dish has three names: the proper Italian, the English, and the Calabrian dialect name Mum used.</p>
  </div>
  <ul class="recipe-grid">
    {''.join(cards)}
  </ul>
</section>

<section id="notes" class="notes wrap" aria-labelledby="notes-h">
  <h2 id="notes-h">Notes from the kitchen</h2>
  <div class="notes-grid">{notes}</div>
</section>"""
    (OUT / "index.html").write_text(
        page(SITE_TITLE, "Traditional Calabrian family recipes from Roccella Jonica, written and photographed by Enzo.",
             body, "home"), encoding="utf-8")


def main():
    if IMG.exists():
        shutil.rmtree(IMG)
    OUT.mkdir(exist_ok=True)
    (OUT / ".nojekyll").write_text("")
    for i, r in enumerate(RECIPES):
        build_recipe(r, i)
    (OUT / "album.html").unlink(missing_ok=True)
    build_home()
    print(f"Built site in {OUT}")


if __name__ == "__main__":
    main()
