import pathlib, re, shutil

html = next(pathlib.Path("blog/templates").rglob("home.html"), None)
hero = next(pathlib.Path("blog/static").rglob("hero1.png"), None)
if not html or not hero:
    print("NOT FOUND:", html, hero); raise SystemExit(1)

parts = hero.parts
idx = len(parts) - 1 - parts[::-1].index("static")
folder = "/".join(parts[idx + 1:-1])
print("home.html:", html)
print("photo folder:", folder)

shutil.copy(html, str(html) + ".bak3")
h = html.read_text(encoding="utf-8")

# remove old hero slideshow scripts
def drop(m):
    return "" if ".hero .slide" in m.group(0) else m.group(0)
h = re.sub(r"<script>.*?</script>\s*", drop, h, flags=re.S)

NEW = """{% block hero %}

<style>
.hero .slide{
  position:absolute; inset:0;
  background-size:cover; background-position:center;
  opacity:0 !important;
  animation:none !important;
  transition:opacity 1.5s ease-in-out;
  z-index:0;
}
.hero .slide.active{ opacity:1 !important; }
</style>

<section class="hero">

    <div class="slide active" style="background-image:url('{% static "FOLDER/hero1.png" %}')"></div>
    <div class="slide" style="background-image:url('{% static "FOLDER/hero2.png" %}')"></div>
    <div class="slide" style="background-image:url('{% static "FOLDER/hero3.png" %}')"></div>
    <div class="slide" style="background-image:url('{% static "FOLDER/hero4.png" %}')"></div>

    <div class="hero-content">
        <i class="fa-solid fa-spa hero-flower"></i>
        <h1 id="heroTitle">Japan &amp; Sri Lanka</h1>
        <p id="heroSubtitle">Stories, travel and life from two beautiful islands.</p>

        <div class="chips">
            {% for category in categories %}
                <a href="?category={{ category.name }}" class="chip">{{ category.name }}</a>
            {% empty %}
                <span class="chip">No Categories</span>
            {% endfor %}
        </div>
    </div>

</section>

<script>
/* heroSlideshow */
document.addEventListener("DOMContentLoaded", function () {
  var slides = document.querySelectorAll(".hero .slide");
  if (slides.length < 2) return;
  var i = 0;
  setInterval(function () {
    slides[i].classList.remove("active");
    i = (i + 1) % slides.length;
    slides[i].classList.add("active");
  }, 4000);
});
</script>

{% endblock %}""".replace("FOLDER", folder)

h, n = re.subn(r"\{% block hero %\}.*?\{% endblock %\}", lambda m: NEW, h, count=1, flags=re.S)
if n == 0:
    print("hero block not found"); raise SystemExit(1)

html.write_text(h, encoding="utf-8")
print("DONE")
