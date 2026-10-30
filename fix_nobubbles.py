import pathlib, shutil

css = next(pathlib.Path("blog/static").rglob("style.css"), None)
if not css:
    print("style.css NOT FOUND"); raise SystemExit(1)
print("css:", css)

c = css.read_text(encoding="utf-8")
if "NO BUBBLES ON HERO" in c:
    print("already added"); raise SystemExit(0)
shutil.copy(css, str(css) + ".bak7")

c += """

/* NO BUBBLES ON HERO */
.hero{
  position:relative;
  z-index:10;
  isolation:isolate;
}
nav.site-navbar{ z-index:100; }

/* make chips readable on the photo */
.chip{
  background:rgba(255,255,255,.92) !important;
  font-weight:600;
}
"""
css.write_text(c, encoding="utf-8")
print("DONE")
