import pathlib, shutil

html = next(pathlib.Path("blog/templates").rglob("base.html"), None)
if not html:
    print("base.html NOT FOUND"); raise SystemExit(1)
print("base:", html)

h = html.read_text(encoding="utf-8")
if "liveBubbles" in h:
    print("already added"); raise SystemExit(0)
shutil.copy(html, str(html) + ".bak6")

block = """
<style id="liveBubblesStyle">
#bubbles{
  position:fixed; inset:0; overflow:hidden;
  pointer-events:none; z-index:5;
  animation:bubbleHue 14s linear infinite;
}
@keyframes bubbleHue{
  from{ filter:hue-rotate(0deg); }
  to{ filter:hue-rotate(360deg); }
}
.bubble{
  position:absolute; bottom:-120px; border-radius:50%;
  background:radial-gradient(circle at 30% 30%,
    rgba(255,255,255,.95), rgba(232,74,127,.35) 55%, rgba(232,74,127,.15));
  border:1px solid rgba(255,255,255,.8);
  box-shadow:inset 0 0 12px rgba(255,255,255,.7), 0 0 14px rgba(232,74,127,.25);
  opacity:.65;
  animation:bubbleRise linear forwards;
}
@keyframes bubbleRise{
  0%  { transform:translate(0,0) scale(.6); opacity:0; }
  10% { opacity:.65; }
  50% { transform:translate(40px,-55vh) scale(1); }
  100%{ transform:translate(-30px,-125vh) scale(1.1); opacity:0; }
}
</style>
<div id="bubbles"></div>
<script>
/* liveBubbles */
(function () {
  var box = document.getElementById("bubbles");
  function make() {
    if (!box || box.children.length > 40) return;
    var b = document.createElement("span");
    b.className = "bubble";
    var size = 18 + Math.random() * 70;
    b.style.width = size + "px";
    b.style.height = size + "px";
    b.style.left = Math.random() * 100 + "vw";
    b.style.animationDuration = (8 + Math.random() * 9) + "s";
    b.addEventListener("animationend", function () { b.remove(); });
    box.appendChild(b);
  }
  for (var n = 0; n < 12; n++) setTimeout(make, n * 250);
  setInterval(make, 450);
})();
</script>
"""
k = h.rfind("</body>")
if k == -1:
    print("</body> not found"); raise SystemExit(1)
h = h[:k] + block + h[k:]
html.write_text(h, encoding="utf-8")
print("DONE")
