#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-31"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Irgendwo im *Juli* ist die Routine stehengeblieben.",
    subline="Das ist kein Scheitern. Das ist Sommer.\nMorgen ist der 1. September.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Septemberpläne schreibt dein *motiviertestes* Ich.",
    subline="Trainieren muss sie dein echtes.\nDas schläft mal gut. Und mal nicht.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
