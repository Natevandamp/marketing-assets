#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-18"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Einmal pro Woche war *ein* Termin. Jeden Morgen sind es *sieben*.",
    subline="Die neue GLP-1-Tablette ändert nicht nur die Form.\nSie ändert die ganze Routine.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Alle machen *Fortschritte*. Nur du *nicht*?",
    subline="Du vergleichst deinen Alltag mit fremden besten Momenten.\nFortschritt misst sich an deinem Zustand – nicht an deren Feed.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
