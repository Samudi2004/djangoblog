import pathlib, shutil

html = next(pathlib.Path("blog/templates").rglob("base.html"), None)
if not html:
    print("base.html NOT FOUND"); raise SystemExit(1)
print("base:", html)

h = html.read_text(encoding="utf-8")
if "bubbleClip" in h:
    print("already added"); raise SystemExit(0)
shutil.copy(html, str(html) + ".bak8")

# make chips readable (white background instead of pale colour)
h = h.replace('e.style.setProperty("background", c + "22", "important");',
              'e.style.setProperty("background", "rgba(255,255,255,.92)", "important");')

block = """
<script>
/* bubbleClip: hide bubbles over the hero section */
(function () {
  var box = document.getElementById("bubbles");
  var hero = document.querySelector(".hero");
  function clip() {
    if (!box) return;
    if (!hero) { box.style.clipPath = "none"; return; }
    var bottom = Math.max(0, Math.round(hero.getBoundingClientRect().bottom));
    box.style.clipPath = "inset(" + bottom + "px 0 0 0)";
  }
  window.addEventListener("scroll", clip, { passive: true });
  window.addEventListener("resize", clip);
  document.addEventListener("DOMContentLoaded", clip);
  clip();
  setInterval(clip, 200);
})();
</script>
"""
k = h.rfind("</body>")
if k == -1:
    print("</body> not found"); raise SystemExit(1)
h = h[:k] + block + h[k:]
html.write_text(h, encoding="utf-8")
print("DONE")
