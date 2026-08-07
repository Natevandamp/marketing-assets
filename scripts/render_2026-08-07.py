#!/usr/bin/env python3
"""Daily cards 2026-08-07. Fokus: RefineSimple (PR-Friday x Tropennächte)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-07"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Urlaub, Tag 3. Und die Routine ist *schon weg*.",
    subline="Kein Wecker, kein Frühstück um sieben.\nEin kurzer Blick beantwortet, was der Tag verlegt hat.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Testtag. Nach der *heißesten Nacht* des Jahres.",
    subline="Deine Kraft ist nicht weg. Sie ist heute nur schwerer abrufbar.\nDer Versuch läuft dir nicht davon.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
