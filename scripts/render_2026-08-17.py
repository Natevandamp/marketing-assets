#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-17"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Jeder Morgen sieht *gleich* aus. Genau das ist das *Problem*.",
    subline="War die Erinnerung von heute – oder von gestern?\nBei gleicher Routine kann der Kopf das kaum trennen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Die Hitze ist *vorbei*. Deine *Erholung* hinkt noch nach.",
    subline="Wochen voller Tropennächte stehen noch in Schlaf und Ruhepuls.\nDer erste kühle Tag ist ein Anfang – kein Freifahrtschein.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
