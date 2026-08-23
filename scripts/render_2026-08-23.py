#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-23"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Eine Nacht ohne Schlaf spürst du sofort. *Ein vergessenes Vitamin nie.*",
    subline="Genau deshalb kommt sonntags der Zweifel.\nWochen nebeneinander sagen mehr\nals ein einzelner Morgen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Der App Store: 1,4 Billionen Dollar. Diese App: *Woche 34*.",
    subline="Build in Public.\nVergleich skaliert endlos.\nNützlichkeit muss das nicht.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
