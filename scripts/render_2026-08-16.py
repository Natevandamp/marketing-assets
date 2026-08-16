#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-16"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Die Woche ist *geplant*. Nur die *Einnahme* läuft auf Gedächtnis.",
    subline="Termine stehen im Kalender. Das Tägliche soll der Kopf behalten.\nEin Blick genügt – statt abends nachzurechnen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Alle bauen gerade *schneller*. Wir bauen *ruhiger*.",
    subline="2026: 60 % mehr neue Apps als im Vorjahr.\nBuild in Public, Woche 33 – Vertrauen lässt sich nicht beschleunigen.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
