import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-03"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Im September zieht der *Wecker* um. Deine *Routine* auch.",
    subline="Gewohnheiten hängen an festen Momenten.\nVerschiebt sich der Morgen, verschwinden sie leise.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="*Tausend* Meinungen über Training. Dein Körper hat *eine*.",
    subline="Schlaf, Ruhepuls, die Last der letzten Tage —\nseine Antwort steht jeden Morgen da.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
