#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-24"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Du hast diese Routine schon mal *neu angefangen*.",
    subline="Montag ist der beliebteste Neustart.\nEr sagt dir nur nichts darüber,\nwie die letzten drei Wochen liefen.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Montags um 18 Uhr ist das Gym am *vollsten*.",
    subline="Der Kalender entscheidet, wann trainiert wird.\nDein Zustand entscheidet, was heute sinnvoll ist.\nZwei verschiedene Fragen.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
