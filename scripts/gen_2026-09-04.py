import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-04"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Die Abenddosis wohnt *zu Hause*. Du heute Abend *nicht*.",
    subline="Routinen hängen an Orten.\nFreitags bist du woanders.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Messen war nie der schwere Teil. *Entscheiden* schon.",
    subline="Nächste Woche messen die Uhren mehr.\nDie Frage bleibt: Was ist heute dran?",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
