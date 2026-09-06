import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-06"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Den Wochenplan schreibt sonntags deine *beste Version*.",
    subline="Leben muss ihn ab Montag die echte.\nDas ist kein Disziplinproblem.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Das nächste Upgrade steckt nicht im *Gerät*.",
    subline="Es steckt in der Entscheidung,\ndie du morgen früh triffst.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
