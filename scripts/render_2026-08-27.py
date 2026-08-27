#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-27"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Alle fragen, *wie lange* du schläfst. Kaum jemand: *wie regelmäßig*.",
    subline="Schlafforschung: Der Rhythmus zählt mehr als die Stundenzahl.\nFür Routinen gilt dasselbe.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Alle machen Fortschritte. *Nur du nicht?*",
    subline="Du vergleichst deinen Alltag mit den\nHighlights der anderen.\nDas einzige Maß mit Aussagekraft:\ndu gegen dich, unter vergleichbaren Bedingungen.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
