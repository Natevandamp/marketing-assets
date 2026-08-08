#!/usr/bin/env python3
"""Daily cards 2026-08-08. Fokus: MicroQuest (Sa) — IG-Karten wie immer für Dose+Refine."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-08"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Die Schublade voller *angefangener* Dosen.",
    subline="Abgesetzt, weil nie sichtbar war, ob sich etwas ändert.\nEin Tag beantwortet das nicht. Wochen schon.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Du siehst sein Gewicht. *Nicht seine Nacht.*",
    subline="Vergleich ohne Kontext ist keine Information.\nDie einzige Tagesform, die du kennst, ist deine.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
