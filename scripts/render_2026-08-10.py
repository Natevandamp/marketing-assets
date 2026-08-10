#!/usr/bin/env python3
"""Daily cards 2026-08-10. Fokus: RefineSimple (Mo) — Serie 'Vielleicht denkst du gerade…',
Trigger Erleichterung/Validierung: Wochen Tropennaechte, diese Woche kuehlt es ab."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-10"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline='„Nehmen Sie das *regelmäßig?“* „Ich *glaube,* ja.“',
    subline="Niemand zählt drei Monate Morgende aus dem Kopf zusammen.\nNachschauen ist einfacher als schätzen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Vielleicht warst du nie *undiszipliniert*. Vielleicht war es nur *zu heiß*.",
    subline="Wochen voller Tropennächte stehen in deinen Erholungsdaten.\nNicht in deinem Charakter.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
