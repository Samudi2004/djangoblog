import pathlib, re, shutil

css = pathlib.Path(r"blog\static\blog\css\style.css")
html = pathlib.Path(r"blog\templates\blog\home.html")
views = pathlib.Path(r"blog\views.py")

for p in (css, html, views):
    if not p.exists():
        print("NOT FOUND:", p)
        raise SystemExit(1)
    shutil.copy(p, str(p) + ".bak")

# 1) views.py: 9 posts on the home page
v = views.read_text(encoding="utf-8")
v = v.replace("paginator = Paginator(posts, 6)", "paginator = Paginator(posts, 9)", 1)
views.write_text(v, encoding="utf-8")

# 2) style.css: remove old grid line, add slider CSS
c = css.read_text(encoding="utf-8")
if "AUTO-SLIDING POSTS" not in c:
    c = re.sub(r"^\.cards\{ display:grid;.*\n", "", c, flags=re.M)
    c += """

/* AUTO-SLIDING POSTS */
.cards{
  display:flex;
  gap:30px;
  overflow-x:auto;
  scroll-snap-type:x mandatory;
  scroll-behavior:smooth;
  scrollbar-width:none;
  padding-bottom:10px;
}
.cards::-webkit-scrollbar{ display:none; }
.cards > .post-card{
  flex:0 0 calc((100% - 60px) / 3);
  scroll-snap-align:start;
}
@media (max-width:992px){
  .cards > .post-card{ flex:0 0 calc((100% - 30px) / 2); }
}
@media (max-width:640px){
  .cards > .post-card{ flex:0 0 100%; }
}
"""
    css.write_text(c, encoding="utf-8")

# 3) home.html: add slider script before the last endblock
h = html.read_text(encoding="utf-8")
if "slides every 4 seconds" not in h:
    js = """<script>
document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelector(".cards");
  if (!cards || cards.children.length <= 3) return;
  setInterval(function () {
    const step = cards.children[0].offsetWidth + 30;
    const atEnd = cards.scrollLeft + cards.clientWidth >= cards.scrollWidth - 5;
    if (atEnd) { cards.scrollTo({ left: 0 }); }
    else { cards.scrollBy({ left: step }); }
  }, 4000); // slides every 4 seconds
});
</script>

"""
    i = h.rfind("{% endblock %}")
    h = h[:i] + js + h[i:]
    html.write_text(h, encoding="utf-8")

print("DONE")
