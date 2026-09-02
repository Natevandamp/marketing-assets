#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-02"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="*Tag 1* läuft auf Motivation. *Tag 3* auf Gedächtnis.",
    subline="Neue Routinen scheitern selten am Anfang.\nSie verschwimmen mitten in der Woche.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="*Mehr Training* kann *weniger Fortschritt* bedeuten.",
    subline="Training setzt den Reiz. Fortschritt entsteht in der Erholung.\nAb einem Punkt nimmt jede Extra-Einheit mehr, als sie gibt.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
