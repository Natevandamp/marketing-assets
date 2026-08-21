#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-21"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Freitagabend hat *keine Routine*.",
    subline="Essen gehen, später ins Bett. Und die Abenddosis?\nGewohnheiten brauchen feste Auslöser. Freitag hat keine.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Eine *leichte Woche* löscht deinen Fortschritt *nicht*.",
    subline="Dein Körper arbeitet auch, wenn du pausierst.\nSieben ruhigere Tage sind kein Rückschritt.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
