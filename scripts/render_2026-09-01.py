#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-01"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Die Spritze war *einmal pro Woche*. Die Tablette ist *jeden Morgen*.",
    subline="Nicht schwerer. Nur öfter.\nEine Routine braucht jetzt sieben feste Momente statt einem.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Ein *Ruhetag* fühlt sich an wie *Aufgeben*.",
    subline="Ist er nicht. Fortschritt entsteht in der Erholung.\nDie Frage ist nicht: Bin ich faul? Sondern: Bin ich bereit?",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
