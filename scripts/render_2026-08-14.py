#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-14"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Nicht der *Montag* ist das Problem. Das *Wochenende* ist es.",
    subline="Kein Wecker, anderer Rhythmus : die Einnahme rutscht durch.\nEin Blick genügt. Auch samstags um 11.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Ein PR lässt sich nicht *erzwingen*. Nur *vorbereiten*.",
    subline="Bestleistungen sind eine Folge, kein Termin.\nDein Zustand entscheidet, wann sich das Strecken lohnt.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
