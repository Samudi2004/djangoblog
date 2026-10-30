import pathlib, re, shutil

def find(pattern, root):
    r = list(pathlib.Path(root).rglob(pattern))
    return r[0] if r else None

css  = find("style.css", "blog/static")
html = find("home.html", "blog/templates")
hero = find("hero1.png", "blog/static")

for name, p in (("style.css", css), ("home.html", html), ("hero1.png", hero)):
    if p is None:
        print("NOT FOUND:", name)
        raise SystemExit(1)
    print("found", name, "->", p)

# static-relative path of the photos, e.g. blog/img/hero1.png
parts = hero.parts
idx = len(parts) - 1 - parts[::-1].index("static")
folder = "/".join(parts[idx + 1:-1])
print("static folder for photos:", folder)

shutil.copy(css, str(css) + ".bak")
shutil.copy(html, str(html) + ".bak")

# ---------- home.html ----------
h = html.read_text(encoding="utf-8")

new_slides = ""
for n in range(1, 5):
    cls = "slide active" if n == 1 else "slide"
    new_slides += ('    <div class="' + cls + '" style="background-image:url(\'{% static "'
                   + folder + '/hero' + str(n) + '.png" %}\')"></div>\n')

h = re.sub(r'[ \t]*<div class="slide[^"]*"[^>]*></div>\s*', "", h)
h = h.replace('<section class="hero">', '<section class="hero">\n\n' + new_slides, 1)

if "heroSlideshow" not in h:
    js = """<script>
/* heroSlideshow */
document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".hero .slide");
  if (slides.length < 2) return;
  let i = 0;
  setInterval(function () {
    slides[i].classList.remove("active");
    i = (i + 1) % slides.length;
    slides[i].classList.add("active");
  }, 5000);
});
</script>

"""
    k = h.rfind("{% endblock %}")
    h = h[:k] + js + h[k:]
html.write_text(h, encoding="utf-8")

# ---------- style.css ----------
c = css.read_text(encoding="utf-8")
c = re.sub(r"\.hero \.slide\{[^}]*\}\s*", "", c)
c = re.sub(r"\.hero \.s\d\{[^}]*\}\s*", "", c)
c = re.sub(r"@keyframes heroFade\{.*?\}\s*\}\s*", "", c, flags=re.S)
if "HERO SLIDESHOW JS" not in c:
    c += """

/* HERO SLIDESHOW JS */
.hero .slide{
  position:absolute;
  inset:0;
  background-size:cover;
  background-position:center;
  opacity:0;
  transition:opacity 1.5s ease-in-out;
  z-index:0;
}
.hero .slide.active{ opacity:1; }
"""
css.write_text(c, encoding="utf-8")

print("DONE")
