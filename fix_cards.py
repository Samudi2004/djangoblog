import pathlib, re, shutil

css  = next(pathlib.Path("blog/static").rglob("style.css"), None)
html = next(pathlib.Path("blog/templates").rglob("home.html"), None)
if not css or not html:
    print("NOT FOUND", css, html); raise SystemExit(1)
print("css :", css); print("html:", html)

shutil.copy(css,  str(css)  + ".bak2")
shutil.copy(html, str(html) + ".bak2")

# ---- CSS: remove old slider/grid rules, add a forced slider ----
c = css.read_text(encoding="utf-8")
c = re.sub(r"/\* AUTO-SLIDING POSTS \*/.*?(?=\n/\*|\Z)", "", c, flags=re.S)
c = re.sub(r"^\.cards\{ display:grid;.*\n", "", c, flags=re.M)
c += """

/* AUTO-SLIDING POSTS (forced) */
.cards{
  display:flex !important;
  flex-wrap:nowrap !important;
  gap:30px;
  overflow-x:auto;
  scroll-snap-type:x mandatory;
  scrollbar-width:none;
  padding-bottom:10px;
}
.cards::-webkit-scrollbar{ display:none; }
.cards > *{
  flex:0 0 calc((100% - 60px) / 3) !important;
  max-width:calc((100% - 60px) / 3);
  scroll-snap-align:start;
}
@media (max-width:992px){
  .cards > *{ flex:0 0 calc((100% - 30px) / 2) !important; max-width:calc((100% - 30px) / 2); }
}
@media (max-width:640px){
  .cards > *{ flex:0 0 100% !important; max-width:100%; }
}
"""
css.write_text(c, encoding="utf-8")

# ---- HTML: add auto-scroll script once ----
h = html.read_text(encoding="utf-8")
h = re.sub(r"<script>\s*document\.addEventListener\(\"DOMContentLoaded\", function \(\) \{\s*const cards.*?</script>\s*", "", h, flags=re.S)
js = """<script>
/* cardSlider */
document.addEventListener("DOMContentLoaded", function () {
  const box = document.querySelector(".cards");
  if (!box || box.children.length <= 3) return;
  setInterval(function () {
    const step = box.children[0].getBoundingClientRect().width + 30;
    const atEnd = box.scrollLeft + box.clientWidth >= box.scrollWidth - 5;
    if (atEnd) { box.scrollTo({ left: 0, behavior: "smooth" }); }
    else { box.scrollBy({ left: step, behavior: "smooth" }); }
  }, 3000);
});
</script>

"""
k = h.rfind("{% endblock %}")
h = h[:k] + js + h[k:]
html.write_text(h, encoding="utf-8")
print("DONE")
