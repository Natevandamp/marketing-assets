#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-25"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Die Studie lief *72 Wochen*. Dein Alltag ist *keine Studie*.",
    subline="Dort wurde jede Einnahme dokumentiert.\nZu Hause gibt es nur dein Gedächtnis.\nUnd Morgen, die sich nicht gleichen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Tausend Meinungen übers Training. *Keine kennt deine Nacht.*",
    subline="Die meisten Ratschläge stimmen. Für irgendwen.\nWas heute für dich stimmt, entscheidet dein Zustand.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
