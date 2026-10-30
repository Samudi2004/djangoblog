import pathlib, shutil

html = next(pathlib.Path("blog/templates").rglob("base.html"), None)
if not html:
    print("base.html NOT FOUND"); raise SystemExit(1)
print("base:", html)
shutil.copy(html, str(html) + ".bak5")

h = html.read_text(encoding="utf-8")
if "colourCycle" in h:
    print("already added"); raise SystemExit(0)

js = """
<style id="colourCycleStyle">
nav.site-navbar{ transition:background .8s, box-shadow .8s; }
.site-navbar .brand, .site-navbar .brand i,
.site-navbar .nav-links a, .site-navbar .btn-outline-pink,
.site-navbar .hi i, .chip{ transition:color .8s, border-color .8s, background .8s; }
</style>
<script>
/* colourCycle */
(function () {
  var colours = ["#e84a7f", "#8e44ad", "#2980b9", "#27ae60", "#e67e22"];
  var i = 0;
  function apply() {
    var c = colours[i % colours.length];
    var nav = document.querySelector("nav.site-navbar");
    if (nav) {
      nav.style.setProperty("background", c + "33", "important");
      nav.style.setProperty("box-shadow", "0 8px 30px " + c + "66", "important");
      nav.querySelectorAll(".brand, .brand i, .nav-links a, .hi i").forEach(function (e) {
        e.style.setProperty("color", c, "important");
      });
      nav.querySelectorAll(".btn-outline-pink").forEach(function (e) {
        e.style.setProperty("color", c, "important");
        e.style.setProperty("border-color", c, "important");
      });
    }
    document.querySelectorAll(".chip").forEach(function (e) {
      e.style.setProperty("color", c, "important");
      e.style.setProperty("background", c + "22", "important");
    });
    document.querySelectorAll(".section-title, .post-card .badge-cat, .arrow").forEach(function (e) {
      if (e.classList.contains("section-title")) e.style.setProperty("color", c, "important");
      else e.style.setProperty("background", c, "important");
    });
    i++;
  }
  document.addEventListener("DOMContentLoaded", function () {
    apply();
    setInterval(apply, 3000);
  });
})();
</script>
"""
k = h.rfind("</body>")
if k == -1:
    print("</body> not found"); raise SystemExit(1)
h = h[:k] + js + h[k:]
html.write_text(h, encoding="utf-8")
print("DONE")
