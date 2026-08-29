#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-29"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Dein Wecker hat frei. Deine *Routine* auch.",
    subline="Samstage brechen mehr Gewohnheiten,\nals fehlende Disziplin es je tut.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Der produktivste Schritt heute könnte eine *Pause* sein.",
    subline="Anpassung passiert in der Erholung.\nEin Ruhetag ist kein Aufgeben.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
